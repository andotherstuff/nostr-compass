## News

### ngit v3 and GitWorkshop v4 move CI, private repositories, and releases onto signed Nostr events

[ngit](https://ngit.dev/ngit.git) is a command-line tool that carries git branches, patches, and pull requests between contributors as [NIP-34](/en/topics/nip-34/) (git repository collaboration) events, and [GitWorkshop](https://ngit.dev/gitworkshop.git) is the web interface where maintainers and contributors read and review that activity. Both reached a new major version in a [coordinated version 3 launch](https://ngit.dev/v3) that also ships ngit-grasp v3 and a first release of ngit-ci at 0.1. The 2.6 series already moved branch, patch, and pull-request review onto Nostr; this launch takes on three jobs that still pulled a project back toward a hosted forge, which are automated checks, private code, and release distribution.

Automated checks arrive with [ngit-ci 0.1](https://ngit.dev/ngit-ci.git), a self-hosted continuous-integration service coordinated through signed Nostr events. Because the instructions and the results are signed events, the checks travel on the same transport that already carries the code review, and a project can run them on hardware its maintainers control. Private code arrives with [ngit-grasp v3](https://ngit.dev/ngit-grasp.git), which supports private repositories through GRASP-08, the private-repository part of the GRASP git-hosting specification. Version 3 also states maintainer authority explicitly, so the keys that speak for a repository are named instead of implied.

Release distribution is the third piece. A project can now publish signed releases and their assets without a forge, using Nostr events for the release records and [Blossom](/en/topics/blossom/), the hash-addressed blob storage that authorizes uploads with Nostr keys, for the files themselves. The [version 3 launch notes](https://ngit.dev/v3) also gather what used to be scattered across repositories into one documentation site covering ngit, ngit-grasp, ngit-ci, and GitWorkshop, so a contributor can read the client, server, CI, and web pieces of the same workflow in one place.

### fips2go exposes an embedded mesh node to chosen Android apps

[fips2go](https://github.com/fr34aky/fips2go) is a newly tracked Android app that runs a node of FIPS, the Free Internetworking Peering System, a decentralized mesh network that uses Nostr keypairs as node identities. The node runs inside the app, and a per-app VPN decides which installed applications can reach it. An app the user selects keeps its ordinary internet access and additionally resolves `.fips` names through the embedded node, so a mesh service becomes reachable from a normal Android app without rooting the device or routing every byte of phone traffic through the mesh.

Current release [v0.3.4](https://github.com/fr34aky/fips2go/releases/tag/v0.3.4) pairs that access control with a default-deny inbound filter, so the phone answers only the traffic it chose to accept. Identity backup uses Android Keystore, and local peers are found over mDNS so two phones on the same network can pair without a coordinator. Recovery after a network change and a diagnostics view round out the release. The app ships through its [signed Zapstore listing](https://zapstore.dev/apps/naddr1qqgx7un89enxjurn9eskuerjda5kgqgcwaehxw309aex2mrp0yh85ctswd6x7un99ejx2aszyqs9vy2xh4p6zygk35qepsja6w7mnl4j3nnyvjgyg079gxnm83e0yqcyqqq8uzclek0pe).

### nsite-clay edits and republishes a single-page site from the browser

Publishing a static site to Nostr has meant a command-line tool and a build step. [nsite-clay](https://github.com/jooray/nsite-clay) removes both for the single-document case: a user opens one HTML page, edits its document object model in place, and publishes the result without installing anything or running a server. The edited document is serialized, uploaded as a content-addressed blob to Blossom, and announced by republishing the site's [NIP-5A](/en/topics/nip-5a/) (static websites) manifest, which is the event set that maps a site's paths to blob hashes.

The workflow is visible in the project's own pages. Its [browser publisher](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html) performs the upload and manifest republication from the page itself, and its [editing guide](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html) walks through the edit-and-publish loop. For a writer who wants one page under their own key, the whole cycle now fits in a browser tab, and because the output is an ordinary NIP-5A site, any client or gateway that already reads those manifests serves it unchanged.

### Wingman App pairs a Nostr browser with a local signer and a file workspace

[Wingman App](https://github.com/OtherStuffAI/wm-app) is a cross-platform Nostr browser that carries its own signer and a Tower-backed file workspace, with desktop and mobile builds from one Flutter shell. The shell injects a [NIP-07](/en/topics/nip-07/) (browser signing interface) provider into the pages it loads, so a web client opened inside Wingman finds a signer without a browser extension, and the key stays in the application the user installed. Its embedded Flight Deck gives the same window a work surface beside the browsing view, and Drive sync keeps files against the Tower service.

Signed requests reach services over HTTP as well. Wingman implements [NIP-98](/en/topics/nip-98/) (HTTP authentication with a signed Nostr event) in its core crate, where the [request-signing implementation](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs) builds the auth event a server verifies before it answers. That gives the app one identity for relay events, page-level signing, and authenticated file operations, which is the part a user notices: signing in to a Nostr web app and reaching a private file store use the same key and the same approval path.

### Mafrend 1.2.0-alpha adds Marmot-backed private groups with per-group maps

A place-based chat app is only as private as its membership list. [Mafrend 1.2.0-alpha](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.2.0-alpha), the Android app that treats a location on a map as a chat room, adds private groups carried over [Marmot](/en/topics/marmot/), the encrypted group-messaging protocol built on Nostr, so a conversation about a place can be held among a closed set of members instead of in the open.

The [release](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.2.0-alpha) gives each group a secure invitation flow and a membership review step, so joining is a decision the group makes and not the effect of following a link. Each group also gets its own map, which keeps the pins, rooms, and conversations of one group separate from another, and group media is encrypted, so photos shared with a private group are protected on the same terms as its messages.

### FIPS 0.5.1 repairs Debian and Ubuntu packages that installed but could not start

Every FIPS package for Debian 12 and Ubuntu 22.04 from 0.3.0 through 0.5.0 installed cleanly and then failed to run, because the binaries carried a `GLIBC_2.39` dependency those releases do not provide. [Version 0.5.1](https://github.com/jmcorgan/fips/releases/tag/v0.5.1) rebuilds them against the platforms they target, so operators on the two most common long-term-support bases can start a mesh node from the distributed package instead of building from source.

Two discovery fixes ship in the [same release](https://github.com/jmcorgan/fips/releases/tag/v0.5.1), covering the path by which a node learns about peers and their advertised addresses before it can carry traffic. Together with the rebuilt packages, that restores a working install-and-join path on both distributions.

### Primal Android 3.5.27 checks who is asking before it signs or pays

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27), a release of the mobile Nostr client and wallet, tightens two authorization paths at once. A request to the local signer is now rejected when the identity in the request does not match the account the signer holds, which closes the case where an app asks for a signature under one key and receives one from another. Incoming [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) requests are authenticated before they are processed, so a wallet command is acted on only after the client establishes that the sender is entitled to send it.

The two merged changes behind the release cover [the local signer identity check](https://github.com/PrimalHQ/primal-android-app/pull/1108) and [the wallet-request authentication path](https://github.com/PrimalHQ/primal-android-app/pull/1105). The release also corrects zap-poll routing, so a zap cast on a poll is attributed to the option the user picked instead of going astray.

writer_model: claude-opus-5 (bounded first-party fallback candidate; wrapper run `7dee2ec3-0440-4980-a0a5-9dd9ce854a4c`)
GATE: PASS (7/7 approved News items present; style and paragraph-link checks passed; exact GitHub and non-GitHub sources resolved 2026-09-09)
