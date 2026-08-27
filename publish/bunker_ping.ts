import { preflightBunker, closeBunker } from "./lib/bunker.ts";
const t0 = Date.now();
try {
  const pk = await preflightBunker();
  console.log("BUNKER OK  signs as:", pk, `(${Date.now() - t0}ms)`);
} catch (e) {
  console.log("BUNKER FAIL:", (e as Error).message, `(${Date.now() - t0}ms)`);
} finally {
  await closeBunker();
}
