import { expect, test } from "bun:test";
import { closeRelayPool } from "./lib/bunker.ts";

test("closeRelayPool closes every relay retained by the signer pool", () => {
  const closed: string[][] = [];
  const pool = {
    relays: new Map([
      ["wss://relay.one/", {}],
      ["wss://relay.two/", {}],
    ]),
    close(relays: string[]) {
      closed.push(relays);
    },
  };

  closeRelayPool(pool);

  expect(closed).toEqual([["wss://relay.one/", "wss://relay.two/"]]);
});
