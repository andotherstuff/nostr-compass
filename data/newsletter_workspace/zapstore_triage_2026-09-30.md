# Zapstore app triage — 2026-09-30

Source: `data/zapstore_releases/zapstore_2026-09-29.json` generated 2026-09-29. The collector recorded 985 release events, 173 Nostr-relevant events, and 59 distinct relevant app IDs. Six `new_app` release records cover four apps: BuhoGO, Holoboard, Nostr Clips, and Staircase.

Verdicts: **13 GREEN, 23 MAYBE, 23 SKIP**. Every app ID was checked against its live Zapstore URL. Fifty-eight pages rendered the named app; `ngit-grasp` rendered a generic page, so its row links the exact signed event viewer. A signed listing establishes publication by its key, not implementation or product ownership. Version in each row is the latest listed version; reasons may describe an earlier substantive release in the same window.

## Primary sources for selection

- [Holoboard repository](https://github.com/ptrio42/holoboard.space/blob/main/README.md), [September 24 changelog](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md), and [signed Zapstore listing](https://zapstore.dev/apps/space.holoboard.app). The listing app ID is `space.holoboard.app`, publisher `npub178umpxtdflcm7a08nexvs4mu384kx0ngg9w8ltm5eut6q7lcp0vq05qrg4` (hex `f1f9b0996d4ff1bf75e79e4cc8577c89eb633e68415c7faf74cf17a07bf80bd8`), and signed 1.0.0 release event `ab2aa301761856572e12af949da6adb4a884f51d3ed7c413db48c3d23eb6aa42`. The repository describes a separately generated board key; do not identify the Zapstore publisher as the board/DM account.
- [Amber 6.6.6](https://github.com/greenart7c3/Amber/releases/tag/v6.6.6), [Flotilla 1.11.2](https://github.com/coracle-social/flotilla/releases/tag/1.11.2), [Ditto 2.42.3](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.42.3), [Iris Chat v2026.9.24.4](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.4).
- [LibreNostr 0.6.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.0) and [0.6.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.2); [Myco 0.8.0](https://github.com/Origami74/myco/releases/tag/v0.8.0) and [0.8.1](https://github.com/Origami74/myco/releases/tag/v0.8.1); [Sonar alpha.15.1](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15.1).
- [Staircase repository](https://code.relay.tools/opensauce/staircase) and [0.1.7 release page](https://code.relay.tools/opensauce/staircase/releases/tag/v0.1.7) respond, but the frontend did not expose the repository body to this read-only pass. Keep MAYBE pending code or product confirmation.

## Complete app inventory

### GREEN

- **Amber 6.6.6** — [Zapstore listing](https://zapstore.dev/apps/com.greenart7c3.nostrsigner) (`com.greenart7c3.nostrsigner`): 6.6.6 repairs padded nostrconnect secrets and publishes feedback to repository-advertised relays.
- **Armada 0.63.0** — [Zapstore listing](https://zapstore.dev/apps/buzz.armada.app) (`buzz.armada.app`): 0.63.0 adds background notifications across signer modes and reduces relay connections.
- **Ditto 2.42.3** — [Zapstore listing](https://zapstore.dev/apps/pub.ditto.app) (`pub.ditto.app`): 2.42.3 adds torrent discovery and relay-aware broadcast, distinct from #41 Top 8 coverage.
- **Flotilla 1.11.2** — [Zapstore listing](https://zapstore.dev/apps/social.flotilla) (`social.flotilla`): 1.11.2 recovers stalled remote-signer sessions and messages delayed by slow relays.
- **Holoboard 1.0.0** — [Zapstore listing](https://zapstore.dev/apps/space.holoboard.app) (`space.holoboard.app`): User-submitted Nostr paid board; Sep 24 Android release and simpler promotion invoice flow.
- **Iris Chat 2026.9.29** — [Zapstore listing](https://zapstore.dev/apps/to.iris.chat) (`to.iris.chat`): Sep 24 voice/video calling, local connection support, and linked-device controls.
- **LibreNostr 0.7.0** — [Zapstore listing](https://zapstore.dev/apps/com.librenostr.android) (`com.librenostr.android`): 0.6.0 routes relay and media traffic through built-in Tor, fail-closed; 0.6.2 improves local WoT filtering and relay choice.
- **Mafrend 1.3.0-alpha** — [Zapstore listing](https://zapstore.dev/apps/com.mafrend.application) (`com.mafrend.application`): 1.3.0-alpha adopts newer Marmot private-group spec with breaking compatibility; label alpha.
- **Myco 0.8.1** — [Zapstore listing](https://zapstore.dev/apps/app.myco) (`app.myco`): 0.8.0 adds Nostr identity, signer login, and an app store; 0.8.1 improves author-relay discovery.
- **Newlay 0.3.45** — [Zapstore listing](https://zapstore.dev/apps/tools.relay.newlay.android) (`tools.relay.newlay.android`): 0.3.45 streams large relay results with backpressure and fixes MLS coordinator delivery.
- **ngit-grasp 3.0.5** — [signed release event](https://primal.net/e/6ff00b9230e4523e6f14aaf6e5088f91e5696be38b9304a4e1cef384e3318d41) (`ngit-grasp`): 3.0.5 recovers live sync under unhealthy relays and fixes NIP-34 push races.
- **Nostrich: Nostr Client 1.1** — [Zapstore listing](https://zapstore.dev/apps/org.nostrich.app) (`org.nostrich.app`): 1.1 adds public/private lists as feeds, scheduled notes, and authenticated-relay chat display.
- **Sonar 0.1-alpha.15.1** — [Zapstore listing](https://zapstore.dev/apps/chat.bitchat.sonar) (`chat.bitchat.sonar`): Alpha.15.1 fixes schema-index failure that repeatedly re-published shares and rate-limited relays.

### MAYBE

- **21Meetup 1.6.6** — [Zapstore listing](https://zapstore.dev/apps/space.einundzwanzig.meetup) (`space.einundzwanzig.meetup`): Repaired second- and third-degree Nostr trust graph; niche, verify app release.
- **BitBlik 0.11.2** — [Zapstore listing](https://zapstore.dev/apps/app.bitblik) (`app.bitblik`): Offer loading and battery fixes; verify a distinct Nostr order-flow effect.
- **Boris 1.6.22** — [Zapstore listing](https://zapstore.dev/apps/org.dergigi.boris) (`org.dergigi.boris`): Oversized identifier or relay hint no longer crashes the feed; narrow fix.
- **Cambium 0.7.1** — [Zapstore listing](https://zapstore.dev/apps/dev.forgesworn.cambium) (`dev.forgesworn.cambium`): Enrollment check code and board/Sapwood verification UX; verify Nostr security consequence.
- **Cellibacy 2.0.8** — [Zapstore listing](https://zapstore.dev/apps/com.scuba323.cellibacy) (`com.scuba323.cellibacy`): One of six related NIP-58 badge dashboards; group as one lead and inspect source.
- **Holy Fit 2.0.8** — [Zapstore listing](https://zapstore.dev/apps/com.scuba323.holyfit) (`com.scuba323.holyfit`): Same six-app NIP-58 badge dashboard rollout; avoid six separate stories.
- **Imwald Android 0.5.11** — [Zapstore listing](https://zapstore.dev/apps/eu.imwald.android) (`eu.imwald.android`): Kind 30040/30041 publication cards and improved gift-wrap/send semantics; niche.
- **Linky 26.9.21** — [Zapstore listing](https://zapstore.dev/apps/fit.linky.app) (`fit.linky.app`): Contact and wallet navigation; verify change to Nostr contacts rather than layout alone.
- **Morganite 0.0.5** — [Zapstore listing](https://zapstore.dev/apps/com.greenart7c3.morganite) (`com.greenart7c3.morganite`): Blossom fetches from .onion servers using Tor; narrow but relay-adjacent media impact.
- **Nostr Clips 0.3.7** — [Zapstore listing](https://zapstore.dev/apps/com.scrollstr.app) (`com.scrollstr.app`): New Zapstore listing for existing Scrollstr; 0.3.7 notes only link a comparison, so avoid launch claim.
- **Nunlock 2.0.7** — [Zapstore listing](https://zapstore.dev/apps/com.scuba323.nunlock) (`com.scuba323.nunlock`): Same six-app NIP-58 badge dashboard rollout; inspect source as a single grouped candidate.
- **Nymchat - Geohash Mesh Chat 3.75.545** — [Zapstore listing](https://zapstore.dev/apps/com.nym.bar) (`com.nym.bar`): Generic changelog in signed listing; inspect exact version diff before promotion.
- **PosterChan 1.0.2404** — [Zapstore listing](https://zapstore.dev/apps/place.poster.app) (`place.poster.app`): Forty-four version tags collapse to one candidate; private GRASP push/ref gate may be material.
- **PsstPsst 26.9.1** — [Zapstore listing](https://zapstore.dev/apps/chat.psstpsst.app) (`chat.psstpsst.app`): Message delivery after network interruptions improves, but notes lack mechanism.
- **SaintStream 2.0.9** — [Zapstore listing](https://zapstore.dev/apps/com.scuba323.saintstream) (`com.scuba323.saintstream`): Same six-app NIP-58 badge dashboard rollout; avoid duplicate coverage.
- **Sister Charge 2.0.8** — [Zapstore listing](https://zapstore.dev/apps/com.scuba323.sistercharge) (`com.scuba323.sistercharge`): Same six-app NIP-58 badge dashboard rollout; avoid duplicate coverage.
- **SkateSpots 1.5.9** — [Zapstore listing](https://zapstore.dev/apps/org.skatespots.app) (`org.skatespots.app`): 1.5.4 repairs persisted DM inbox relays, but narrow application reach.
- **Staircase 0.1.7** — [Zapstore listing](https://zapstore.dev/apps/tools.relay.staircase) (`tools.relay.staircase`): New signed listing for Cordn-over-Nostr MLS messenger; source repo exists, exact client behavior needs corroboration.
- **Tenna 0.12.2** — [Zapstore listing](https://zapstore.dev/apps/pub.soapbox.tenna) (`pub.soapbox.tenna`): 0.12.0 grants permissioned background refresh for sites; assess Nostr site implications.
- **The Habit 2.0.2** — [Zapstore listing](https://zapstore.dev/apps/com.scuba323.thehabit) (`com.scuba323.thehabit`): Same six-app NIP-58 badge dashboard rollout; avoid duplicate coverage.
- **Zap Cooking 1.6.0** — [Zapstore listing](https://zapstore.dev/apps/cooking.zap.app) (`cooking.zap.app`): Published posts no longer return as drafts; distinct from #41 image-description PR, modest reach.
- **ZEUS 13.2.2** — [Zapstore listing](https://zapstore.dev/apps/app.zeusln.zeus) (`app.zeusln.zeus`): NWC secret display and stricter connection-string parsing amid Lightning-heavy release.
- **Zzub 0.0.16** — [Zapstore listing](https://zapstore.dev/apps/social.cloudfodder.zzub) (`social.cloudfodder.zzub`): Project-board restoration and project-wide view; verify concrete Nostr delivery change.

### SKIP

- **Angor 0.2.36** — [Zapstore listing](https://zapstore.dev/apps/io.angor.app) (`io.angor.app`): Bitcoin recovery and fee estimation, no Nostr-facing change.
- **Astraea 1.1.0** — [Zapstore listing](https://zapstore.dev/apps/com.example.epochs) (`com.example.epochs`): Visual theme change only.
- **Barattolo 1.5** — [Zapstore listing](https://zapstore.dev/apps/store.barattolo.app) (`store.barattolo.app`): Android splash-screen polish only.
- **Bookshelf 0.1.26** — [Zapstore listing](https://zapstore.dev/apps/eu.decentnewsroom.bookshelf) (`eu.decentnewsroom.bookshelf`): Recommendation and rating presentation, little relay-facing substance.
- **BuhoGO 1.9.3** — [Zapstore listing](https://zapstore.dev/apps/mybuho.buhogo) (`mybuho.buhogo`): First Zapstore listing, but this release focuses on Spark exit and wallet naming; NWC support predates it.
- **Chama 6.4.13** — [Zapstore listing](https://zapstore.dev/apps/app.chama.market) (`app.chama.market`): Trade alerts and payments, no demonstrated Nostr relay change.
- **Divine 1.0.23** — [Zapstore listing](https://zapstore.dev/apps/co.openvine.app) (`co.openvine.app`): Documentation-only release.
- **Echoes 1.1.0** — [Zapstore listing](https://zapstore.dev/apps/com.echoes.echoes) (`com.echoes.echoes`): Visual refresh; sync and encryption unchanged.
- **fips2go 0.8.0** — [Zapstore listing](https://zapstore.dev/apps/org.fips.android) (`org.fips.android`): 0.8.0 syncs names over FIPS mesh, not Nostr relays; #41 covered 0.7.0 Nostr discovery.
- **K.ai 1.8.1** — [Zapstore listing](https://zapstore.dev/apps/ai.alohak.kai) (`ai.alohak.kai`): Local AI memory and speech behavior, no distinct Nostr interaction.
- **Kairos 1.1.0** — [Zapstore listing](https://zapstore.dev/apps/dev.echoes.checkmarks) (`dev.echoes.checkmarks`): Shared visual theme update only.
- **My Signet 0.14.0** — [Zapstore listing](https://zapstore.dev/apps/app.mysignet) (`app.mysignet`): Empty release notes; no substantiated user or protocol change.
- **NoorNote 1.8.1** — [Zapstore listing](https://zapstore.dev/apps/com.noornote.app) (`com.noornote.app`): Visual navigation and glass theme only.
- **Nymbot - Private AI Assistant 1.0.7** — [Zapstore listing](https://zapstore.dev/apps/ai.nymbot) (`ai.nymbot`): On-device file reading for AI assistant, no distinct Nostr change.
- **Roadstr 0.5.11** — [Zapstore listing](https://zapstore.dev/apps/app.roadstr) (`app.roadstr`): Navigation and map reports dominate; no broad Nostr relay change established.
- **Shosho – Live Streaming Marketplace 1.2.0** — [Zapstore listing](https://zapstore.dev/apps/com.shosho.app) (`com.shosho.app`): New Bitcoin wallet capability, no Nostr-specific change demonstrated.
- **Table Mesh 0.2.1** — [Zapstore listing](https://zapstore.dev/apps/org.tablemesh.app) (`org.tablemesh.app`): Bluetooth/Wi-Fi game transfer without a demonstrated relay surface.
- **Treasures 2.11.6** — [Zapstore listing](https://zapstore.dev/apps/to.treasures.app) (`to.treasures.app`): Maintenance copies earlier map release without new user-facing work.
- **TWENTY ONE Companion 1.13.0** — [Zapstore listing](https://zapstore.dev/apps/space.einundzwanzig.mobile) (`space.einundzwanzig.mobile`): Navigation restructuring with no distinct Nostr behavior.
- **Voca 1.4.2** — [Zapstore listing](https://zapstore.dev/apps/com.voca.app) (`com.voca.app`): Diagnostics-upload repair, no distinct Nostr-facing feature.
- **Whistle 1.11.2** — [Zapstore listing](https://zapstore.dev/apps/org.getwhistle.whistle) (`org.getwhistle.whistle`): Zapstore screenshots and minor cleanup only.
- **XM Arcade 1.1.3** — [Zapstore listing](https://zapstore.dev/apps/com.xmarcade.app) (`com.xmarcade.app`): Android icon and presentation fixes only.
- **YakiHonne 2.0.9** — [Zapstore listing](https://zapstore.dev/apps/com.yakihonne.yakihonne) (`com.yakihonne.yakihonne`): Camera and playback lifecycle fixes, weak newsletter value.

## Continuity and scope notes

- Issue #41 (2026-09-23) already covered Amber 6.6.5, Armada 0.61.0, Ditto 2.40.0, fips2go 0.7.0, and a Zap Cooking image-description PR. Only the separate changes named above can justify follow-up coverage.
- NIP-58 exists in the [NIPs repository](https://github.com/nostr-protocol/nips/blob/master/58.md), but the six related wellness app release claims still need repository or product corroboration before one grouped story is selected.
- `new_app` in this fetch means newly seen Zapstore publication. It does not establish that the underlying software first launched this week; Nostr Clips and Staircase need that distinction in any prose.
