# Bunker signing — how it actually works

This is a reference for anyone touching `publish/lib/bunker.ts` in the
**compass** repo. It documents the NIP-46 lifecycle, the Amber-side
persistence model, the failure modes we used to hit, and the
persistent-session design that fixed them.

> Compass signs as a **different npub** than blog/towardsliberty. Its bunker
> config lives at `~/.config/compass-publish/`, not `~/.config/blog-publish/`.
> Same protocol, separate authorization in Amber.

## Compass identity

| Field | Value |
|---|---|
| npub | `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923` |
| pubkey_hex | `775954f7314112489a4a29ec692b72386fd60bcceb0308d423101ea979c57a80` |
| Bunker config | `~/.config/compass-publish/bunker.json` |
| Client key | `~/.config/compass-publish/client_key` (persistent — never rotate) |
| Authority | `publish/config/author.json` — the pipeline verifies the bunker signs as this exact pubkey before broadcasting |

The `pubkey_hex` in `author.json` is the canonical compass identity. The
bunker URI prefix (`bunker://<remote-signer-pubkey>?...`) is a **different**
thing — it's Amber's endpoint, not the compass identity. The pipeline calls
NIP-46 `get_public_key` after `connect` to discover the actual signing
pubkey and refuses to proceed if it doesn't match `author.json`.

## TL;DR

- One `BunkerSigner` instance per publish run. One `connect` handshake, many
  `signEvent` calls over the same relay subscription.
- Same `bunker://` URI keeps working forever. No re-pairing between sessions.
- `client_key` is the persistent identity. Never rotate it.
- Cold preflight: ~800 ms. Per-sign cost when warm: ~350 ms.

## The protocol (NIP-46)

The user holds the actual nsec inside Amber. Our laptop holds a `client_key`
(a separate disposable secp256k1 secret) that signs *RPC requests* to Amber.
The bunker URI looks like:

```
bunker://<remote-signer-pubkey>?relay=wss://...&relay=wss://...&secret=<one-time>
```

The flow:

1. **Connect** (one time per process):
   - Client derives `client_pubkey` from `client_key`.
   - Client subscribes to relays in the URI for `kind 24133` events tagged
     with `#p=client_pubkey` from `authors=[remote-signer-pubkey]`.
   - Client publishes a `kind 24133` event encrypted to `remote-signer-pubkey`
     with method `"connect"` and the `secret` from the URI.
   - Amber receives it, validates the secret, **stores `client_pubkey` in its
     local DB**, and replies `"ack"`.
   - From now on Amber recognizes this client purely by `client_pubkey`. The
     secret is dead.

2. **Every subsequent RPC** (`sign_event`, `nip44_encrypt`, `ping`, etc.):
   - Client encrypts the request and publishes a `kind 24133` event tagged
     `#p=remote-signer-pubkey`.
   - Amber checks its DB: is `event.pubkey` (i.e. `client_pubkey`) authorized?
     Yes → process. No → silently ignore.
   - Amber publishes a `kind 24133` response tagged `#p=client_pubkey`, which
     our open subscription receives.

The spec on the secret (§"Initiating a connection"):

> Optional secret can be used for **one successfully established connection
> only**, _remote-signer_ SHOULD ignore new attempts to establish connection
> with old secret.

So the URI's `secret=` is one-shot. After consumption, **the URI is still
usable** because the secret is now ignored — Amber identifies us by
`client_pubkey`, which it stored at first connect.

## Amber's persistence model

Source: `app/src/main/java/com/greenart7c3/nostrsigner/database/ApplicationDao.kt`
+ `ApplicationEntity.kt` + `service/BunkerRequestUtils.kt`.

Amber stores authorized clients in a Room SQLite table `application`:

```kotlin
data class ApplicationEntity(
    @PrimaryKey val key: String,        // <- this is client_pubkey
    val name: String,
    val relays: List<NormalizedRelayUrl>,
    val pubKey: String,                 // <- the user's npub
    var isConnected: Boolean,
    val secret: String,
    var deleteAfter: Long,              // <- 0L = never delete
    val lastUsed: Long,
    val localKey: String = "",
    ...
)
```

Primary lookup query:

```kotlin
@Query("SELECT * FROM application WHERE `key` = :key")
suspend fun getByKey(key: String): ApplicationWithPermissions?
```

The only deletion query that runs automatically:

```kotlin
@Query("DELETE FROM application WHERE deleteAfter < :time AND deleteAfter > 0")
suspend fun deleteOldApplications(time: Long): Int
```

Default `deleteAfter = 0L`, which means **Amber never automatically deletes
authorized clients**. The entry survives:
- App restart
- Phone reboot (Amber re-reads DB on `ConnectivityService.onCreate`)
- Battery optimization killing the foreground service (the DB is intact
  on next service start)

Things that DO invalidate the authorization:
- User manually revokes the connection in Amber → Authorized Apps
- User uninstalls / clears Amber's app data
- User set a TTL when approving (then `deleteAfter > 0`)

That's it. There is no per-session re-pairing requirement.

## The failure mode we hit before (and why "fresh URI" felt like the fix)

Old `publish/lib/bunker.ts` shelled out to `nak event --connect-as` per
signature. nak's NIP-46 client (`fiatjaf.com/nostr/nip46.ConnectBunker`) does
the full lifecycle on every invocation:

1. `nip46.NewBunker(...)` — opens a relay subscription
2. `bunker.RPC(ctx, "connect", [target, secret])` — handshake
3. The signature RPC
4. Process exits, subscription closes

A blog publish run signs 3 events back-to-back:
- Blossom upload auth (kind 24242)
- NIP-23 article (kind 30023)
- Announcement note (kind 1)

So we got 3 independent connect handshakes per run. Each one:
- Re-subscribed to 3 relays
- Re-derived NIP-44 conversation keys
- Re-published the connect event
- Raced relay liveness, Amber dispatcher liveness, and Android scheduling

Any one of these three rolls could land on a transient Amber stall and the
30-second nak timeout fired with no logs. The "fix" of pasting a fresh URI
worked because the act of opening Amber to copy it incidentally cleared
whatever stall was happening — same URI, same client_pubkey, retried success.

## The fix: one persistent BunkerSigner

`publish/lib/bunker.ts` now uses `nostr-tools/nip46`'s `BunkerSigner` as a
module-level singleton. Reading nostr-tools source for proof:

```javascript
// BunkerSigner.fromBunker — opens ONE long-lived subscription
static fromBunker(clientSecretKey, bp, params = {}) {
    const signer = new BunkerSigner(clientSecretKey, params);
    signer.conversationKey = getConversationKey(clientSecretKey, bp.pubkey);
    signer.bp = bp;
    signer.setupSubscription();   // <- long-lived
    return signer;
}

setupSubscription() {
    this.subCloser = this.pool.subscribe(
        this.bp.relays,
        {
            kinds: [NostrConnect],
            authors: [this.bp.pubkey],
            "#p": [getPublicKey(this.secretKey)],
            limit: 0
        },
        { onevent: ..., onclose: ... }
    );
}

// Every RPC routes a response through the SAME open subscription
async sendRequest(method, params) {
    // ... publish request ...
    this.listeners[id] = { resolve, reject };   // <- waits on shared sub
}
```

So one connect, one subscription, N sign requests with one shared response
listener routing by RPC id.

### Measured behavior (validation 2026-05-18)

```
TEST 1 - cold start, full bunker.json untouched
  preflight 917ms, pubkey b7ed68b062de6b4a...
TEST 2 - rapid back-to-back signs (3x)
  sign 1 = 363ms, id 35505925b4bf...
  sign 2 = 435ms, id c9398d3c9576...
  sign 3 = 364ms, id f33af8ffd923...
TEST 3 - after a 30s idle, prove session is still alive
  sign after 30s idle = 335ms, id a19b58335fdb...
TEST 4 - tear down + cold restart proves connect path is reentrant
  reconnect preflight = 756ms, pubkey b7ed68b062de6b4a...
  sign after reconnect = 326ms, id 4b42f5bcc6e6...
ALL TESTS PASSED
```

Three observations:

- Steady-state sign cost: 326-435 ms. (Was 5-9s per `nak event` for the same
  work, with handshake dominating.)
- 30s idle did not drop the subscription.
- `closeBunker()` + `preflightBunker()` round-trips cleanly, proving teardown
  is correct (no leaked sockets, no stuck listeners).

## API

```ts
import { preflightBunker, signWithBunker, closeBunker } from "./bunker.ts";

// Optional. Pre-warms the session and surfaces clear errors if Amber unreachable.
const userPubkey = await preflightBunker(expectedPubkey);

// Sign anything. First call auto-preflights.
const signed = await signWithBunker(unsignedEvent, expectedPubkey);

// Optional. Tears down. Process exit is also fine.
await closeBunker();
```

## Timeouts (all surface clean, actionable errors)

| Phase | Timeout | Error template |
|-------|---------|----------------|
| `connect` (in `getSigner`) | 15s | "Bunker connect timed out... Open Amber, force-stop+reopen if foreground." |
| `sign_event` (per request) | 25s | "Bunker sign_event timed out... pending approval dialog in Amber." |

No more silent 30s hangs. Every error message tells the user exactly what to
do.

## When a fresh bunker URI IS actually needed

The list is short and recoverable:

1. **User revoked the authorization in Amber.** Authorized Apps → swipe to
   revoke. Then `client_pubkey` is no longer in Amber's DB and re-connect is
   silently dropped.
2. **User uninstalled/reinstalled Amber, or wiped app data.** DB gone.
3. **User explicitly approved with a TTL** (the "delete after N days" option
   in Amber's connect dialog). After TTL, Amber's
   `deleteOldApplications` cron clears the row.
4. **`~/.config/blog-publish/client_key` was deleted/regenerated locally.**
   New `client_pubkey` — Amber doesn't know us.

In all these cases the fix is the same: revoke any stale entry in Amber,
generate a fresh `bunker://...` URI from Amber's Bunker tab, write it to
`~/.config/blog-publish/bunker.json`. Do NOT touch `client_key` unless case
(4) applies.

## Security properties

| Property | Mechanism |
|----------|-----------|
| Bunker URI never in argv | Held in process memory; no subprocess spawned |
| Bunker URI never in logs | `redact()` strips `bunker://...` before any throw |
| `bunker.json` owner-only | Auto-`chmod 0600` on read |
| `client_key` never rotated automatically | Generated once on first run, persisted at 0600 |
| Signature pubkey checked | `signed.pubkey !== expectedPubkey` throws before returning |

## Files

- `publish/lib/bunker.ts` — the singleton implementation
- `publish/stages/sign.ts` — calls `signWithBunker` for the newsletter (kind 30023)
- `publish/stages/announce.ts` — calls `signWithBunker` for the announcement (kind 1)
- `~/.config/compass-publish/bunker.json` — the URI (never committed)
- `~/.config/compass-publish/client_key` — persistent client key (never committed)

## References

- NIP-46: https://github.com/nostr-protocol/nips/blob/master/46.md
- nostr-tools `BunkerSigner`: `node_modules/nostr-tools/lib/esm/nip46.js`
- Amber source: https://github.com/greenart7c3/Amber
  - `service/BunkerRequestUtils.kt` — request/response handling
  - `database/ApplicationDao.kt` — persistence queries
  - `database/ApplicationEntity.kt` — schema (especially `key`, `lastUsed`, `deleteAfter`)
- nak source (the old approach): https://github.com/fiatjaf/nak
