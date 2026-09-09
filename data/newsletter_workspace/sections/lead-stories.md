## Top Stories

### Signed git workflows move CI, private repositories, and releases onto Nostr

The [September 8 v3 launch](https://ngit.dev/v3) brings ngit, GitWorkshop, ngit-grasp, and ngit-ci into one signed workflow. [ngit](https://ngit.dev/ngit.git) carries branches, patches, and pull requests as [NIP-34](/en/topics/nip-34/) events, while [GitWorkshop](https://ngit.dev/gitworkshop.git) provides the review interface. The launch adds ngit-ci 0.1, a self-hosted continuous-integration service whose instructions and results travel as signed Nostr events, so checks can run on maintainer-controlled hardware alongside code review.

The same release gives [ngit-grasp v3](https://ngit.dev/ngit-grasp.git) private repositories through the GRASP-08 private-repository extension and makes maintainer authority explicit. Signed release records can point to assets in [Blossom](/en/topics/blossom/), keeping both release metadata and content-addressed files outside a hosted forge. The [new documentation site](https://ngit.dev/v3) gathers the client, private-repository, CI, and web components.

### nsite-clay makes browser publishing recoverable

An [August 31 signer-prompt fix](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8), [publication recovery](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0), and [September 2 editing controls](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7) make [nsite-clay](https://github.com/jooray/nsite-clay) a browser publishing tool for a single-page site. A user edits the document object model in place, serializes the result, uploads it as a content-addressed [Blossom](/en/topics/blossom/) blob, and republishes the site's [NIP-5A](/en/topics/nip-5a/) manifest. No local build or server is required.

The [browser publisher](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html) now makes failed publication recoverable and reduces repeated signer prompts, while the [editing guide](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html) documents the loop. The result remains an ordinary NIP-5A site for existing gateways.

### Wingman App joins browsing, signing, and files

The September work adds [file pickers](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec), [profile publication](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704), [safe signer and session restore](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6), and [tested mobile builds](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac) to [Wingman App](https://github.com/OtherStuffAI/wm-app). Its Flutter shell injects a [NIP-07](/en/topics/nip-07/) provider into pages opened inside the app, while Flight Deck and Tower-backed Drive provide a work surface and file workspace beside the browser.

Wingman signs authenticated HTTP requests using [NIP-98](/en/topics/nip-98/). The [request implementation](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs) builds the event a server verifies before answering, giving one installed identity a consistent approval path for relay actions, web-app signing, and files.

### Shosho ships Livelier's self-hosted streams

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) shipped September 1 with support for [Livelier](https://github.com/r0d8lsh0p/livelier), whose [August 31 attribution update](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc) identifies the bridge and Owncast source in bridged profiles. Livelier watches Owncast's public directory, checks whether a video stream is live, and then publishes an addressable `kind:30311` [NIP-53](/en/topics/nip-53/) event. Discovery travels over Nostr while video remains on the streamer's server.

Chat crosses the bridge as `kind:1311` events. The [bridge design](https://github.com/r0d8lsh0p/livelier) opens a source-side connection only while a Nostr reader is subscribed, labels derived identities, and sends transient chat to a relay that deletes it after three hours. The discovery relay accepts live-event writes only from the bridge key; the chat relay uses [NIP-42 authentication](/en/topics/nip-42/) and [NIP-70 protected-event flags](/en/topics/nip-70/).

### Communitator makes relay templates inspectable before signing

The [August 31 launch series](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c) gives [Communitator](https://github.com/dyne/communitator) canonical templates for kind `10002` relay lists, kind `10063` Blossom servers, and kind `10050` private-message inboxes. Before a signer connects, the application shows normalized endpoints, read/write permissions, event kinds, fixed publication relays, and destinations.

The [bounded signing and publication flow](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501) separates connecting from applying. Each event is signed separately, one run uses at most four WebSocket connections, and a destination counts only after a positive [NIP-01](/en/topics/nip-01/) `OK`. Results distinguish complete, partial, failed, and cancelled delivery. Shared templates remain untrusted recommendations; the [consent surface](https://github.com/dyne/communitator#security-and-consent) explains relay and network observability.

### cal.emre.xyz publishes NIP-52 appointment availability

The public repository opened in an [initial September 2 commit](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743), followed by a signed [September 3 handler announcement](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac) for [cal.emre.xyz](https://cal.emre.xyz). A host publishes availability as a `kind:31923` [NIP-52](/en/topics/nip-52/) event; a guest publishes a `kind:31925` RSVP.

It reads host events and accepted busy RSVPs from relays, excludes overlapping timespans, and keeps Nostr events as the scheduling record without copying them into a separate database. Hosts can sign with [NIP-07](/en/topics/nip-07/), [NIP-46](/en/topics/nip-46/), or a local key; guests can generate a separate key. Its [repository](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) also exposes the resulting `naddr` and calendar links, with email disabled by default.

### Plektos makes private events one encrypted channel

The [September 2 private-event implementation](https://github.com/derekross/plektos/pull/12) makes each [Plektos](https://github.com/derekross/plektos) gathering a private channel inside a [Concord](/en/topics/concord-protocol/) encrypted community. The guest list, RSVP roster, sign-up board, thread, contributions, cover images, edits, and deletions are encrypted together; an invitation carries only that event's key and no plaintext calendar event is published.

The [September 6 lifecycle audit](https://github.com/derekross/plektos/pull/14) anchors the event-definition id for direct lookup when more than 500 wraps exist, while retaining a paginated fallback. Invitation bundles expire 30 days after an event ends and can be disabled, but someone who already obtained a channel key can retain it. A separate [parser-security repair](https://github.com/derekross/plektos/pull/16) makes malformed type-length-value (TLV) [NIP-19](/en/topics/nip-19/) identifiers fail instead of trapping the parser.

writer_model: claude-opus-5 (bounded first-party fallback candidate; wrapper run `7dee2ec3-0440-4980-a0a5-9dd9ce854a4c`)

GATE: PENDING REVIEW
