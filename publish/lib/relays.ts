// Relay multiplexer for broadcast (used only when stage 5 is explicitly enabled).

import WebSocket from "ws";
import type { SignedEvent } from "./bunker.ts";

export type RelayReceipt = {
  relay: string;
  ok: boolean;
  reason?: string;
  ms: number;
};

const PER_RELAY_TIMEOUT_MS = 15_000;

function sendToRelay(relay: string, event: SignedEvent): Promise<RelayReceipt> {
  const start = Date.now();
  return new Promise((resolve) => {
    let settled = false;
    const finalize = (r: Omit<RelayReceipt, "relay" | "ms">) => {
      if (settled) return;
      settled = true;
      try {
        ws.terminate();
      } catch {
        /* ignore */
      }
      resolve({ relay, ms: Date.now() - start, ...r });
    };

    let ws: WebSocket;
    try {
      ws = new WebSocket(relay, { handshakeTimeout: PER_RELAY_TIMEOUT_MS });
    } catch (e) {
      finalize({ ok: false, reason: `connect: ${(e as Error).message}` });
      return;
    }

    const timer = setTimeout(() => {
      finalize({ ok: false, reason: "timeout waiting for OK" });
    }, PER_RELAY_TIMEOUT_MS);

    ws.on("open", () => {
      try {
        ws.send(JSON.stringify(["EVENT", event]));
      } catch (e) {
        clearTimeout(timer);
        finalize({ ok: false, reason: `send: ${(e as Error).message}` });
      }
    });

    ws.on("message", (data) => {
      try {
        const msg = JSON.parse(data.toString()) as unknown;
        if (Array.isArray(msg) && msg[0] === "OK" && msg[1] === event.id) {
          clearTimeout(timer);
          if (msg[2] === true) finalize({ ok: true });
          else finalize({ ok: false, reason: typeof msg[3] === "string" ? msg[3] : "rejected" });
        }
      } catch {
        /* ignore */
      }
    });

    ws.on("error", (err: Error) => {
      clearTimeout(timer);
      finalize({ ok: false, reason: `socket: ${err.message}` });
    });

    ws.on("close", () => {
      clearTimeout(timer);
      finalize({ ok: false, reason: "closed without OK" });
    });
  });
}

export async function broadcastToRelays(
  event: SignedEvent,
  relays: string[],
): Promise<RelayReceipt[]> {
  return Promise.all(relays.map((r) => sendToRelay(r, event)));
}

export type MinimalEvent = {
  id: string;
  pubkey: string;
  created_at: number;
  kind: number;
  tags: string[][];
  content: string;
};

const QUERY_TIMEOUT_MS = 6_000;

// Fetches the newest event matching {kinds, authors} from one relay, closing
// as soon as EOSE or the timeout fires. Used to check whether a recipient has
// published a NIP-65 relay list (kind 10002) before deciding NIP-17 vs NIP-04.
function queryOneRelay(
  relay: string,
  filter: { kinds: number[]; authors: string[]; limit?: number },
): Promise<MinimalEvent | undefined> {
  return new Promise((resolve) => {
    let settled = false;
    let best: MinimalEvent | undefined;
    const subId = Math.random().toString(36).slice(2, 10);
    const finalize = (v: MinimalEvent | undefined) => {
      if (settled) return;
      settled = true;
      try {
        ws.send(JSON.stringify(["CLOSE", subId]));
      } catch {
        /* ignore */
      }
      try {
        ws.terminate();
      } catch {
        /* ignore */
      }
      resolve(v);
    };

    let ws: WebSocket;
    try {
      ws = new WebSocket(relay, { handshakeTimeout: QUERY_TIMEOUT_MS });
    } catch {
      finalize(undefined);
      return;
    }

    const timer = setTimeout(() => finalize(best), QUERY_TIMEOUT_MS);

    ws.on("open", () => {
      try {
        ws.send(JSON.stringify(["REQ", subId, filter]));
      } catch {
        clearTimeout(timer);
        finalize(best);
      }
    });

    ws.on("message", (data) => {
      try {
        const msg = JSON.parse(data.toString()) as unknown;
        if (!Array.isArray(msg)) return;
        if (msg[0] === "EVENT" && msg[1] === subId) {
          const ev = msg[2] as MinimalEvent;
          if (!best || ev.created_at > best.created_at) best = ev;
        } else if (msg[0] === "EOSE" && msg[1] === subId) {
          clearTimeout(timer);
          finalize(best);
        }
      } catch {
        /* ignore malformed relay frames */
      }
    });

    ws.on("error", () => {
      clearTimeout(timer);
      finalize(best);
    });

    ws.on("close", () => {
      clearTimeout(timer);
      finalize(best);
    });
  });
}

// Queries multiple relays in parallel for the newest matching event, returns
// the newest one seen across all of them (or undefined if none respond).
export async function queryNewest(
  relays: string[],
  filter: { kinds: number[]; authors: string[]; limit?: number },
): Promise<MinimalEvent | undefined> {
  const results = await Promise.all(relays.map((r) => queryOneRelay(r, filter)));
  let best: MinimalEvent | undefined;
  for (const r of results) {
    if (r && (!best || r.created_at > best.created_at)) best = r;
  }
  return best;
}
