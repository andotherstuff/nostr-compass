---
title: "Keycast: Team Nostr Remote Signing"
date: 2026-05-21
draft: false
categories:
  - Signing
  - Security
  - Teams
---

Keycast is a self-hosted NIP-46 remote signing server built for teams. It stores Nostr private keys encrypted at rest in SQLite, generates NIP-46 bunker connection strings, and runs signer processes that approve or deny remote signing requests according to configurable per-key policies. The project is maintained by the Marmot Protocol organization.

## How It Works

The server has four main components: an Axum API that handles team management and NIP-98 HTTP auth, a SvelteKit web frontend that uses NIP-07 for authentication, a signer manager that watches authorization rows and spawns one `signer_daemon` per authorization, and a SQLite database with migrations.

Team members sign in through their NIP-07 browser extension. The web app requests a NIP-98 HTTP auth event signed locally by the extension, then sends that auth header to the API. The API verifies the event, extracts the pubkey, and checks team membership. Stored keys are encrypted with a root `master.key` file that must be mounted separately from the image and never committed.

The signer daemon decrypts the stored key and bunker key on startup, connects to configured relays, and calls `Authorization::validate_policy` before approving each NIP-46 signing request. Policies specify which event kinds a particular bunker connection is allowed to sign.

## Security Audit (May 2026)

A security audit completed in May 2026 addressed auth, permission, data integrity, and dependency issues. Key changes:

- NIP-98 auth now requires exactly one `u` tag and one `method` tag, rejects stale or future timestamps, and validates request-body `payload` hashes
- `ALLOWED_PUBKEYS` is parsed exactly and enforced server-side; the frontend exposes `/api/config?pubkey=<hex>` so the browser can check allowlist status without receiving the full server list
- Empty policies default-deny sign/encrypt/decrypt requests; policy creation rejects unknown or malformed permission configs
- SQLite connections enable foreign-key enforcement; team deletion no longer loses permission join data before cleanup
- Server-side route protection now covers nested app routes such as `/teams/:id`
- Web responses set CSP, frame, content-type, referrer, permissions, and HSTS headers
- A SQL migration normalizes old allowed-kinds permission JSON from `{"sign":[...]}` to `{"allowed_kinds":[...]}` on startup

The audit notes residual items in [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) before trusting the deployment with real team keys.

## Deployment

Docker Compose deployment mounts `master.key` into API and signer containers, runs containers as a non-root UID/GID with a read-only root filesystem, and uses Caddy labels to route `/api/*` to the API and everything else to the web app. The published image at `ghcr.io/marmot-protocol/keycast` is tagged with `master`, `latest`, and `sha-<commit>`.

---

**Primary sources:**
- [Keycast Repository](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - May 2026 security audit results

**Mentioned in:**
- [Newsletter #23: Keycast Security Audit Complete](/en/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**See also:**
- [NIP-46: Nostr Remote Signing](/en/topics/nip-46/)
- [NIP-07: Browser Extension Signer](/en/topics/nip-07/)
- [Marmot Protocol](/en/topics/marmot/)
