## Notable Code and Documentation Changes

### Meiso mirrors group keys into secure storage and comments on personal tasks through Amber

[Meiso](https://github.com/higedamc/meiso) is an Android task manager whose tasks are encrypted and synchronized through Nostr relays. A [secure-storage mirror for group keys](https://github.com/higedamc/meiso/pull/170) now keeps the keys that decrypt a shared task list in the platform's protected store, so a shared list survives app restarts without leaving its keys in ordinary application storage.

Commenting also works for users who keep their key in a signer. [Personal-task comments in Amber mode](https://github.com/higedamc/meiso/pull/164) let someone whose signing happens in the [NIP-55](/en/topics/nip-55/) (Android signer application) flow annotate their own tasks, a path that previously assumed a locally held key. Both changes keep signature verification on the Rust side, so the checks that decide whether a synchronized task is authentic stay in one implementation instead of being duplicated per platform.

### Clave completes its sign-in callback and pins it to an exact host

Signing in to a website with an iOS signer has to return the user to the page that asked. [Clave](https://github.com/DocNR/clave), an iOS [NIP-46](/en/topics/nip-46/) (remote signing over relays) signer that uses push notifications to sign while the app is closed, [completes the two-phase Sign in with Clave callback flow](https://github.com/DocNR/clave/pull/98), so the request and the return leg are handled as one sequence and the calling site receives a result it can act on.

The matching authorization work is narrower than it looks. [Exact-host matching](https://github.com/DocNR/clave/pull/97) replaces comparison against the registrable domain, so an approval granted to one host is not honored for a sibling subdomain, and a [Universal Link replay fix](https://github.com/DocNR/clave/pull/93) prevents a captured callback link from being presented a second time to obtain another sign-in.

### nostr-components adds zaps and YouTube to its extension and ships a directory site

[nostr-components](https://github.com/saiy2k/nostr-components) provides embeddable web components that place Nostr profiles, posts, follow buttons, and comment sections into any website. Its browser extension gained [zap actions and YouTube support](https://github.com/saiy2k/nostr-components/pull/122), so a reader can send a zap from an embedded component and Nostr content attached to YouTube pages is rendered by the same components as everything else.

A second surface shipped alongside the extension. The merged [Nostr Atlas directory site](https://github.com/saiy2k/nostr-components/pull/117) puts the project's components on a public page of its own, which gives an integrator somewhere to see them running against live relay data before embedding them.

writer_model: claude-opus-5 (bounded first-party fallback candidate; wrapper run `7dee2ec3-0440-4980-a0a5-9dd9ce854a4c`)
GATE: PASS (3/3 approved project groups present; style and paragraph-link checks passed; all linked PRs resolved merged 2026-09-09)
