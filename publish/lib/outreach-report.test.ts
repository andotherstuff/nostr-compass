import { describe, expect, test } from "bun:test";
import { countSentRows } from "./outreach-report.ts";

describe("outreach report", () => {
  test("counts sent rows using the receipt's camelCase eventId field", () => {
    expect(countSentRows([
      { status: "sent", eventId: "abc" },
      { status: "sent", eventId: "def" },
      { status: "failed" },
    ])).toBe(2);
  });
});
