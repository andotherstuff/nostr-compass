import { afterEach, describe, expect, test } from "bun:test";
import { createServer } from "node:http";
import type { Socket } from "node:net";
import { WebSocketServer } from "ws";
import { broadcastToRelays, queryNewest } from "./relays.ts";
import type { SignedEvent } from "./bunker.ts";

const openSockets = new Set<Socket>();

afterEach(() => {
  for (const socket of openSockets) socket.destroy();
  openSockets.clear();
});

async function startUncooperativeRelay(eventId?: string) {
  let resolveClosed!: () => void;
  const closed = new Promise<void>((resolve) => {
    resolveClosed = resolve;
  });

  const server = createServer();
  const wss = new WebSocketServer({ noServer: true });
  server.on("connection", (socket) => {
    openSockets.add(socket);
    socket.on("close", () => {
      openSockets.delete(socket);
    });
  });
  server.on("upgrade", (request, socket, head) => {
    socket.once("close", resolveClosed);
    wss.handleUpgrade(request, socket, head, (ws) => {
      (ws as typeof ws & { testSocket: Socket }).testSocket = socket;
      wss.emit("connection", ws, request);
    });
  });
  wss.on("connection", (ws) => {
    ws.once("message", (data) => {
      const request = JSON.parse(data.toString()) as unknown[];
      const response = eventId
        ? ["OK", eventId, true, "accepted"]
        : ["EOSE", request[1]];
      // Stop reading before replying so the client's close frame is ignored.
      const socket = (ws as typeof ws & { testSocket: Socket }).testSocket;
      socket.pause();
      socket.removeAllListeners("data");
      ws.send(JSON.stringify(response));
    });
  });

  await new Promise<void>((resolve) => server.listen(0, "127.0.0.1", resolve));
  const address = server.address();
  if (!address || typeof address === "string") throw new Error("Missing relay address");

  return {
    url: `ws://127.0.0.1:${address.port}`,
    closed,
    stop: () =>
      new Promise<void>((resolve) => {
        wss.close();
        server.close(() => resolve());
      }),
  };
}

describe("broadcastToRelays", () => {
  test("closes the connection after a relay receipt without waiting for a close handshake", async () => {
    const event = {
      id: "a".repeat(64),
      pubkey: "b".repeat(64),
      sig: "c".repeat(128),
      kind: 1059,
      created_at: 1,
      tags: [],
      content: "encrypted",
    } satisfies SignedEvent;
    const relay = await startUncooperativeRelay(event.id);

    try {
      const receipts = await broadcastToRelays(event, [relay.url]);
      expect(receipts[0].ok).toBe(true);
      const connectionClosed = await Promise.race([
        relay.closed.then(() => true),
        Bun.sleep(250).then(() => false),
      ]);
      expect(connectionClosed).toBe(true);
    } finally {
      for (const socket of openSockets) socket.destroy();
      await relay.stop();
    }
  });
});

describe("queryNewest", () => {
  test("closes the connection after EOSE without waiting for a close handshake", async () => {
    const relay = await startUncooperativeRelay();

    try {
      const result = await queryNewest([relay.url], {
        kinds: [10002],
        authors: ["d".repeat(64)],
        limit: 1,
      });
      expect(result).toBeUndefined();
      const connectionClosed = await Promise.race([
        relay.closed.then(() => true),
        Bun.sleep(250).then(() => false),
      ]);
      expect(connectionClosed).toBe(true);
    } finally {
      for (const socket of openSockets) socket.destroy();
      await relay.stop();
    }
  });
});
