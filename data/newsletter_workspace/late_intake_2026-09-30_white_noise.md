# White Noise release evidence for Compass edition 42

Verified 2026-09-30 approximately 15:08–15:12 UTC, with uncached authenticated GitHub wrapper. Read-only task; no project/source edits or external writes.

## Current releases

- Android stable: android-v2026.9.30, published 2026-09-30T07:10:08Z; not prerelease, not draft. https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30
- Android previous stable: android-v2026.9.21, published 2026-09-21T15:53:04Z. The android-pr-previews release is a prerelease artifact bucket, excluded.
- whitenoise-ios and whitenoise-mac release-list APIs returned empty arrays, so no new tagged release claimed for these repos.
- Legacy Flutter whitenoise latest release remains v2026.5.22+25, published 2026-05-22T14:53:28Z. It is outside this reporting window and excluded.

## Source bindings

- GitHub mirror discovery used `github-local search marmot-protocol/whitenoise-android --query poll --scope threads --limit 8 --json`; mirror status observed current, last_sync_at2026-09-30T15:09:45Z. Mirror revealed closed poll-adoption PR and open newer poll issues; only the stable tagged contents are described as released.
- Full live release object: /opt/data/tmp/compass_whitenoise_android_release_20260930.json
- Exact live tag comparison: /opt/data/tmp/compass_whitenoise_android_release_diff_20260930.json
- https://github.com/marmot-protocol/whitenoise-android/compare/android-v2026.9.21...android-v2026.9.30
- Base b3bf1acc3ec681fea1459cf392656208187cc3dd; released head6b7ed7e9fd8e3af52646b2b63d0989399c3ae44a;107 commits.
- API compare is capped at300 files; local immutable Git objects were available and inspected to recover full scope:924files,56157insertions,7548deletions. No reliance on API cap as complete file inventory.
- Relevant live PR bodies and mergedAt receipts: /opt/data/tmp/compass_whitenoise_release_prs_20260930.json; all22 queried PRs authoritatively MERGED.
- Full tag commit inventory appears below. Production source patches inspected for crop, account defaults, polling actions, consent revision, history notices, dictation and chat search. PR summaries provide corroborating scope, including explicit limitations.

## Continuity and claim boundaries

Prior edition41 already covers Sep21 delivery, voice dictation, text-to-speech, navigation, account switching, AMOLED, shareable profile/invite QR cards and group actions. The new entry explicitly follows that release, then covers new polls, account defaults, crop, folder removal, waves, history notices and changed recovery/signing behavior. This is a distinct release and substantive delta.

Poll creation is group-only (not direct conversations), accepts2–10options, supports single/multiple choices and optional deadlines (bounded30days). Do not claim custom deadline UI; its open issue is newer work. Pending edits survive in-process controller replacement, not process death. Explicit file transfer changes do not add partial-byte resume or establish faster raw throughput. GIPHY support matches bounded iOS envelopes; do not claim unrestricted remote-media support. Do not describe hardware acceptance or performance measurements as universal guarantees.

## Release-note coverage

Every substantive release-note category is represented: polls, folder deletion, account disappearing defaults, focal crop, Wave hi, paging, dictation, attachments, paste/composer, notifications, push recovery, Amber signing, incomplete-history notices, and fresh log-sharing choice. Additional substantive tag changes represented in proposed prose: pending-message edit handoff, iOS GIPHY interoperability, document metadata handling, AGPL-3.0-only license.

Minor UI fixes covered collectively by paging/composer/notification wording: keyboard-visible focused messages/actions/notices, group-id search, account-switch scroll/avatar refresh, group-name/nickname updates, member mute visibility, captioned portrait sizing, notification identity/dismissal, device-credential unlock recreation, stale send/image errors, local group deletion recovery. Large-group invite warning is an additional small UI safeguard; release notes do not prioritize it. CI, reproducibility, tests, localization copy cleanup, dependency/build changes and developer telemetry/demo tooling are not standalone news.

## Proposed prose

### White Noise Android adds group polls and account-specific disappearing-message defaults

[White Noise Android](https://github.com/marmot-protocol/whitenoise-android) is a Nostr messenger for private Marmot-encrypted conversations. Following the delivery and sharing improvements [covered last week](/en/newsletters/2026-09-23-newsletter/#white-noise-android-2026921-improves-encrypted-chat-reliability-and-sharing), [the September 30 release](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30) adds group polls with selectable answers, result bars, and deadlines through the Marmot Development Kit. It also adds [device-local disappearing-message defaults for each account](https://github.com/marmot-protocol/whitenoise-android/pull/2799): new direct conversations and groups inherit the chosen duration, while existing conversations and their individual settings keep their current policy. [Wave hi](https://github.com/marmot-protocol/whitenoise-android/pull/2765) sends a greeting that mentions a newly added member without disturbing the current draft.

The [release](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30) lets users choose the focal crop for profile and group images and delete a chat folder without deleting its conversations. Its [history notices](https://github.com/marmot-protocol/whitenoise-android/pull/2869) show when recovery leaves account or group history potentially incomplete, with separate dismissal controls. [Conversation paging](https://github.com/marmot-protocol/whitenoise-android/pull/2818) avoids rebuilding the displayed timeline on a jump to recent messages, and [pending-message edits](https://github.com/marmot-protocol/whitenoise-android/pull/2825) retain their text while the original send obtains its confirmed event ID. That edit handoff covers conversation changes within the running app; it does not establish persistence across process death.

[Dictation now chooses Paste or Send for each recording](https://github.com/marmot-protocol/whitenoise-android/pull/2768), with automatic finishing placing the transcript in the draft. [Offline-provider setup](https://github.com/marmot-protocol/whitenoise-android/pull/2888) explains on-device processing, keeps its consent separate from other speech providers, and restores interrupted media after capture ends. [General-file handling](https://github.com/marmot-protocol/whitenoise-android/pull/2830) accepts bounded, nonempty documents with accurate filenames, MIME metadata, and failure messages; [explicit attachment downloads](https://github.com/marmot-protocol/whitenoise-android/pull/2879) use Android's user-initiated transfer jobs with a foreground fallback. [Paste controls](https://github.com/marmot-protocol/whitenoise-android/pull/2877) now use Android’s system action so GrapheneOS Secure Paste can grant clipboard access. Android also [renders iOS GIPHY shares as animated media](https://github.com/marmot-protocol/whitenoise-android/pull/2806) while respecting download policy.

[Notification fixes](https://github.com/marmot-protocol/whitenoise-android/pull/2808) refresh sender nicknames and clean up alerts when a conversation opens. The [notification recovery changes](https://github.com/marmot-protocol/whitenoise-android/pull/2712) preserve pending push work through unavailable foreground ownership and use bounded retries. [Amber signing](https://github.com/marmot-protocol/whitenoise-android/pull/2802) coordinates same-account approval bursts to prevent rate limits from cancelling sends. The [new audit configuration](https://github.com/marmot-protocol/whitenoise-android/pull/2872) asks for a fresh log-sharing choice before uploading to the new receiver. The source also [adopts AGPL-3.0-only licensing](https://github.com/marmot-protocol/whitenoise-android/pull/2840).

## Exact merged PR receipts

- [Adopt MDK 0.11 polls and v5 audit host configuration](https://github.com/marmot-protocol/whitenoise-android/pull/2872) — MERGED, merged 2026-09-29T14:36:37Z
- [Add account defaults for disappearing messages](https://github.com/marmot-protocol/whitenoise-android/pull/2799) — MERGED, merged 2026-09-23T14:54:01Z
- [Let each dictation choose Paste or Send, and retire the app-wide default](https://github.com/marmot-protocol/whitenoise-android/pull/2768) — MERGED, merged 2026-09-22T15:25:02Z
- [fix: make push recovery durable and bounded](https://github.com/marmot-protocol/whitenoise-android/pull/2712) — MERGED, merged 2026-09-24T06:34:42Z
- [Prevent Amber rate limiting from cancelling sends](https://github.com/marmot-protocol/whitenoise-android/pull/2802) — MERGED, merged 2026-09-23T06:18:41Z
- [Show when history may be incomplete](https://github.com/marmot-protocol/whitenoise-android/pull/2869) — MERGED, merged 2026-09-29T10:17:58Z
- [Handle arbitrary safe documents with truthful metadata and errors](https://github.com/marmot-protocol/whitenoise-android/pull/2830) — MERGED, merged 2026-09-25T15:47:23Z
- [Keep restarted attachment download jobs cancellable](https://github.com/marmot-protocol/whitenoise-android/pull/2893) — MERGED, merged 2026-09-30T06:06:27Z
- [Add Delete folder action to folder settings](https://github.com/marmot-protocol/whitenoise-android/pull/2884) — MERGED, merged 2026-09-29T20:01:19Z
- [Let people choose the focal crop for profile and group images](https://github.com/marmot-protocol/whitenoise-android/pull/2795) — MERGED, merged 2026-09-23T07:59:40Z
- [Give our thumbs a break: add Wave hi](https://github.com/marmot-protocol/whitenoise-android/pull/2765) — MERGED, merged 2026-09-24T08:10:19Z
- [Measure media latency and keep explicit attachment downloads running](https://github.com/marmot-protocol/whitenoise-android/pull/2879) — MERGED, merged 2026-09-29T17:16:39Z
- [Improve offline dictation setup and restore media during processing](https://github.com/marmot-protocol/whitenoise-android/pull/2888) — MERGED, merged 2026-09-29T22:04:58Z
- [Preserve edits to pending outgoing messages during confirmation](https://github.com/marmot-protocol/whitenoise-android/pull/2825) — MERGED, merged 2026-09-28T12:40:53Z
- [Render iOS GIPHY envelopes as animated media](https://github.com/marmot-protocol/whitenoise-android/pull/2806) — MERGED, merged 2026-09-23T13:29:44Z
- [License White Noise Android under AGPL-3.0](https://github.com/marmot-protocol/whitenoise-android/pull/2840) — MERGED, merged 2026-09-24T14:56:47Z

## Full tag commit inventory

- [Match Zapstore signer rehearsal to publication (#2748)](https://github.com/marmot-protocol/whitenoise-android/commit/c81896d5c9a81d263df290c1b3ab924527e89bf4)
- [Add protected legacy Zapstore deletion (#2750)](https://github.com/marmot-protocol/whitenoise-android/commit/c5df05644ec5f25eafde8398523798f03c6d80c2)
- [Parallelize CI and retain each job build cache](https://github.com/marmot-protocol/whitenoise-android/commit/a505bbf569912b83afbbed167991cbc88c2e10a4)
- [Isolate installer test provider roots](https://github.com/marmot-protocol/whitenoise-android/commit/ec801c882279cf0dc8c96bb6cbfa782d44057e6e)
- [Regenerate Compose reports on warm CI runs](https://github.com/marmot-protocol/whitenoise-android/commit/26144abb38a3eb39bfa0ae671e8640832ea46002)
- [Reduce contention between CI test workers](https://github.com/marmot-protocol/whitenoise-android/commit/ce9e43893e9945360ac933ffb0f08ff4b7d875ee)
- [Build reproducibility evidence in parallel](https://github.com/marmot-protocol/whitenoise-android/commit/305f162807b1f24b7e1aa754c6f720595659ea01)
- [Seed authoritative manual attention in tests](https://github.com/marmot-protocol/whitenoise-android/commit/ea6c7a0f3d940f1c1c965e5b7fba83554b995e49)
- [Parallelize security scans and cache previews](https://github.com/marmot-protocol/whitenoise-android/commit/5c4ce02309257988efd71b26bf77be84bfd88a39)
- [Run release lint once outside APK builds](https://github.com/marmot-protocol/whitenoise-android/commit/6c47ba263351391270119c8e3071b0a2e5d12511)
- [Keep release lint in standalone runtime runs](https://github.com/marmot-protocol/whitenoise-android/commit/7b95616b768062d50d7b52a37bec7c552acdd031)
- [Tune Gradle heap for release compilation](https://github.com/marmot-protocol/whitenoise-android/commit/da99d9c732d7075bc2ee12dacd510cb48fe3e9ef)
- [Share reproducibility input downloads once](https://github.com/marmot-protocol/whitenoise-android/commit/9173d82ecb6647d14078a0a6650c6dbe3229e5f9)
- [Fix mention IME composition range crash (#2746)](https://github.com/marmot-protocol/whitenoise-android/commit/cd6d7284c95c69e61821ce55cc49dcacdecb0123)
- [Record release build task timings](https://github.com/marmot-protocol/whitenoise-android/commit/704d70b105ff05a8b5b9f52c68f1185618227bff)
- [Wait for native observers in regression tests](https://github.com/marmot-protocol/whitenoise-android/commit/69b08cf4ecda078fdfcdfa50bc4449e57d3d8e80)
- [Remove unused CI packaging work](https://github.com/marmot-protocol/whitenoise-android/commit/b4247221e76432d6e2960e1ebca2d6ab42da2ffd)
- [Handle ABI-targeted preview APK outputs](https://github.com/marmot-protocol/whitenoise-android/commit/c315f9bb8acf34bb617dea66060012e7dc0a3b93)
- [Merge pull request #2743 from marmot-protocol/perf/halve-android-ci](https://github.com/marmot-protocol/whitenoise-android/commit/f1c02fc888acbd68de053a2ecba1a30d1be90691)
- [chore(deps): bump agp from 9.4.0 to 9.4.1 (#2756)](https://github.com/marmot-protocol/whitenoise-android/commit/558cec5b3c3ac2d322b1b26a45467bceb5a6c867)
- [chore(deps): bump the actions group with 3 updates (#2759)](https://github.com/marmot-protocol/whitenoise-android/commit/2b346cd6dbc0b51d12c2a80822e93313e64b3155)
- [chore(deps): bump androidx.tracing:tracing from 2.0.1 to 2.0.2 (#2757)](https://github.com/marmot-protocol/whitenoise-android/commit/3091cdb44cfa123a522671bbc042a030fa8b29e9)
- [chore(deps): bump com.google.android.gms:play-services-base (#2755)](https://github.com/marmot-protocol/whitenoise-android/commit/05cd4eb44b0fed24d2ae0004ca0412b84d7a8a6e)
- [Fix dictated send tail reveal wiring (#2744)](https://github.com/marmot-protocol/whitenoise-android/commit/cad86210268b4194795b1b11f93b992bc8796c73)
- [Copy audit: 43 revised strings across English and every maintained translation (#2752)](https://github.com/marmot-protocol/whitenoise-android/commit/62e77801a5552fcd5e4be74d429f1bdae9e1a10e)
- [fix(composer): consolidate media and resize gestures (#2751)](https://github.com/marmot-protocol/whitenoise-android/commit/a57644db2cefd25c68e58431e3a582f26faeaed2)
- [Fix five independent quick-win issues: nicknames, group rename, page-error noise, metered media default, stale send errors (#2770)](https://github.com/marmot-protocol/whitenoise-android/commit/615e2ac4e8ac314596a8fd0d2dc51a06fdc70fba)
- [Warn before large-group member invitations (#2769)](https://github.com/marmot-protocol/whitenoise-android/commit/b892bf146ba9d6d5ee8a173abb409572b8d13530)
- [Fix browser-installable PR preview links (#2777)](https://github.com/marmot-protocol/whitenoise-android/commit/73f8a5294a8e21dd493bf757cb051cfce2ffd395)
- [Add pending send observability (#2771)](https://github.com/marmot-protocol/whitenoise-android/commit/c1552a5919589bf8911144c1bb336dfec76d8370)
- [Let each dictation choose Paste or Send, and retire the app-wide default (#2768)](https://github.com/marmot-protocol/whitenoise-android/commit/763f4525ee822d4a502fc7491f63f1fc5f4f4533)
- [fix(reactions): harden removal coordination (#2749)](https://github.com/marmot-protocol/whitenoise-android/commit/b4c922cbf0af85311548e8e514719ea3fc607615)
- [Add Wave hi to member-added messages](https://github.com/marmot-protocol/whitenoise-android/commit/6cc30975c4edc67ce9454c962a7c4ebd065f6965)
- [Map group-system deletion in the test guide](https://github.com/marmot-protocol/whitenoise-android/commit/c6adda92e84abfd247c4229581488cf2d6980346)
- [Fix wave button localization and CI coverage](https://github.com/marmot-protocol/whitenoise-android/commit/574f6596fe30305b5069ff4a857c67795b5e43e6)
- [Remember accepted waves per invite event](https://github.com/marmot-protocol/whitenoise-android/commit/d42fc86bf9bdd2b8e4629f576eb904c824924607)
- [Fix bounded-window recovery (#2778)](https://github.com/marmot-protocol/whitenoise-android/commit/c1769e71f8a313a0eb7adca3f1ef4bfd4aae0619)
- [Fix seven independent quick-win issues: quick reactions, dictation errors, keyboard-covered notices, account-switch scroll, group recovery, notification routing, removal copy (#2787)](https://github.com/marmot-protocol/whitenoise-android/commit/8f916aee050b8b6066c6a30d774d8571cda0502b)
- [Prevent Amber rate limiting from cancelling sends (#2802)](https://github.com/marmot-protocol/whitenoise-android/commit/467169f53a28049dad5843eaba377f90d0e305db)
- [Fix pending send cancellation race (#2792)](https://github.com/marmot-protocol/whitenoise-android/commit/cd012a87b72edbcdbbebb3cda3c4cc9359322bae)
- [Let people choose the focal crop for profile and group images (#2795)](https://github.com/marmot-protocol/whitenoise-android/commit/d6028f9a6683850c4e99b54aa296d9fccd22a5ff)
- [Fix four independent quick-win issues: avatar spacing, per-member mute, banner blur, video preview (#2804)](https://github.com/marmot-protocol/whitenoise-android/commit/362d701ee13b82181da4faa1ac8833fddd750c18)
- [Move conversation window preparation off the main thread (#2798)](https://github.com/marmot-protocol/whitenoise-android/commit/e72fed20d74aae18b1d6d5a92ff3fed79725afd8)
- [Start pasted-npub DM preparation concurrently (#2803)](https://github.com/marmot-protocol/whitenoise-android/commit/e01494c3a4e9f898d44a1aeb880bc806bad2999e)
- [Fix two independent quick-win issues: test-only preview APKs, first-frame quick-switch avatars (#2809)](https://github.com/marmot-protocol/whitenoise-android/commit/58e71f495fea9015d0341c71da61e25df8bd1cb6)
- [Render iOS GIPHY envelopes as animated media (#2806)](https://github.com/marmot-protocol/whitenoise-android/commit/d19d3123eb077f1ae48fc7a25c2b6e041fc96ad0)
- [Fix device credential unlock across activity recreation (#2793)](https://github.com/marmot-protocol/whitenoise-android/commit/6a4d68690b584de56debd07fd4c5b9882b9e785a)
- [Add account defaults for disappearing messages (#2799)](https://github.com/marmot-protocol/whitenoise-android/commit/a14519c7ed7ec4efab96016aae550163a9c4ee82)
- [Fix chat search and profile UI quick wins (#2807)](https://github.com/marmot-protocol/whitenoise-android/commit/def18c696acca60f06b9684307c4c3dcaa7bc612)
- [fix: make push recovery durable and bounded (#2712)](https://github.com/marmot-protocol/whitenoise-android/commit/22bcfff9531172e11a5a00294b7c081b228c8a76)
- [Keep lifted message visible above keyboard (#2821)](https://github.com/marmot-protocol/whitenoise-android/commit/5b0d0f9fc1312e2418e9e48646f83d1af2a864b5)
- [Restore random profile name dice across kind-zero editors (#2819)](https://github.com/marmot-protocol/whitenoise-android/commit/576e51463e6e2bbf0c92afd5c84512883ae1fe3b)
- [Merge pull request #2765 from marmot-protocol/wave-button](https://github.com/marmot-protocol/whitenoise-android/commit/2e43e83242f3eae8c76f3482c45adf216c7806b6)
- [Add long CJK fast-scroll regression for RectList crash (#2827)](https://github.com/marmot-protocol/whitenoise-android/commit/b8145b14f1de5594d237dad7dc8d41829edc3d49)
- [Fix notification identity and conversation-open cleanup (#2808)](https://github.com/marmot-protocol/whitenoise-android/commit/af22e80d504e1af91fd84ac8eebc73c57c7dc00b)
- [Make conversation history paging measurable, and take the rebuild out of jump-to-newest (#2818)](https://github.com/marmot-protocol/whitenoise-android/commit/6cf67a68a14aeac7be50ee6fd24057fd479dbb58)
- [Fix Android splash mark safe zone (#2832)](https://github.com/marmot-protocol/whitenoise-android/commit/804681ad2019fea4b75190f1afd1f55349bb8c88)
- [Keep read-aloud message bubbles at natural height (#2833)](https://github.com/marmot-protocol/whitenoise-android/commit/0701c8cde509e86824294db2c81fca15b2047de6)
- [Add MIT license to White Noise Android (#2837)](https://github.com/marmot-protocol/whitenoise-android/commit/b8aa6bc936ddb076374d200d98e6e7aabcbb7336)
- [Hide empty Shared in Chat categories (#2831)](https://github.com/marmot-protocol/whitenoise-android/commit/3b988a0672726dd3e06749f6eab6ba8984d59fdf)
- [License White Noise Android under AGPL-3.0 (#2840)](https://github.com/marmot-protocol/whitenoise-android/commit/b02547ff659f311544a25cb198c74b7991be356d)
- [Adopt faster MarmotKit media downloads (#2839)](https://github.com/marmot-protocol/whitenoise-android/commit/4e5fc24c3d62deb3f7e217652bc933aae579e552)
- [Give the jump-to-newest badge one count owner that paging cannot move (#2824)](https://github.com/marmot-protocol/whitenoise-android/commit/3f9aaa037392861d5b7f24ec0947d4f06208c8c5)
- [Give newer pages the same runway as older history, and show when one is in flight (#2826)](https://github.com/marmot-protocol/whitenoise-android/commit/88140d10d915eb3ecef71eeea029fede4ef68e1f)
- [Recover local chat deletion from closed transport (#2805)](https://github.com/marmot-protocol/whitenoise-android/commit/f2a67ca0a607bc0523c046e2c2b72fdec8ae9b8d)
- [Keep a caught fling coasting, and stop the older-edge paging loop (#2848)](https://github.com/marmot-protocol/whitenoise-android/commit/657c0fc506590508a5e5be023f98d4381f4656b3)
- [Improve captioned portrait media sizing (#2847)](https://github.com/marmot-protocol/whitenoise-android/commit/681b0c54c98ff72005ffdb4490a771ddee4ced3b)
- [Stop tracking machine-specific Android Studio files](https://github.com/marmot-protocol/whitenoise-android/commit/08e319ec9092d5412f681a0d48af5eebda5f859a)
- [Recover active chats omitted by live window replacements (#2828)](https://github.com/marmot-protocol/whitenoise-android/commit/13e20d6fc342468dd55709ce805a029dea46cda6)
- [Keep focused text actions reachable above the keyboard (#2836)](https://github.com/marmot-protocol/whitenoise-android/commit/ecd4503883a2ba9879a8ed88b67dd8e57ee158c8)
- [Handle arbitrary safe documents with truthful metadata and errors (#2830)](https://github.com/marmot-protocol/whitenoise-android/commit/b1563e1b927b293bd54e88c608b59bfe54c4337e)
- [Merge pull request #2851 from marmot-protocol/chore/untrack-machine-specific-idea-files](https://github.com/marmot-protocol/whitenoise-android/commit/278bf9c1d571a9c84fc429f3d8000a3698e02915)
- [Adopt MDK snapshot 228f4d94 (#2849)](https://github.com/marmot-protocol/whitenoise-android/commit/e374d22980bf663d5bedf9366910475c8894841b)
- [Move the Edit label into a pill beside Send (#2852)](https://github.com/marmot-protocol/whitenoise-android/commit/e4ed772bc55c6299be6e618a37dfda46306027c1)
- [Add resumable two-profile conversation demo to Developer Tools (#2838)](https://github.com/marmot-protocol/whitenoise-android/commit/f7703a936e609ebcec52429755ec6bd5c1c87712)
- [Wire Android host performance telemetry into MDK (#2850)](https://github.com/marmot-protocol/whitenoise-android/commit/bb0039f41ac95f45aa3ee371907487a739561274)
- [Keep transient group-recovery reads quiet (#2856)](https://github.com/marmot-protocol/whitenoise-android/commit/2de3722d001238b37385b7598bec1972ca70c5ef)
- [Stabilize the cold Amber signer burst test (#2855)](https://github.com/marmot-protocol/whitenoise-android/commit/e301c192cc7658b9adba9d0965f6c8b73f8fe5dc)
- [Adopt MDK snapshot 03b1809e with startup recovery responsiveness (#2858)](https://github.com/marmot-protocol/whitenoise-android/commit/777b89cf00e941fb862afa1a4f5ba88ef5248a30)
- [Hide Auto fill on an empty composer long press (#2857)](https://github.com/marmot-protocol/whitenoise-android/commit/50ddaaa00e57c9a8b367140ef7d53a277ea8c2c1)
- [Preserve edits to pending outgoing messages during confirmation (#2825)](https://github.com/marmot-protocol/whitenoise-android/commit/cdc2cf62ef58b835891cd5f0273d4d60a7b8ec93)
- [Adopt MarmotKit 0.11.0 (#2868)](https://github.com/marmot-protocol/whitenoise-android/commit/984747b53f204ae285abb377b2a32d3db458b10f)
- [chore(deps): bump work from 2.11.2 to 2.12.0 (#2866)](https://github.com/marmot-protocol/whitenoise-android/commit/10c64a5284e87346b64b8cf3649124faa2119922)
- [chore(deps): bump androidx.fragment:fragment from 1.9.0 to 1.9.1 (#2865)](https://github.com/marmot-protocol/whitenoise-android/commit/1b9f1da1eaef3604d1e77151c4ff360fe1d85d60)
- [chore(deps): bump roborazzi from 1.74.0 to 1.75.0 (#2864)](https://github.com/marmot-protocol/whitenoise-android/commit/cb909a377e02e45dcaba37f0100fa1d66e2fa96e)
- [Show when history may be incomplete (#2869)](https://github.com/marmot-protocol/whitenoise-android/commit/e09b60e3a5a50f6422fd161e08b32e959c40d07e)
- [chore(deps): bump the actions group with 2 updates (#2867)](https://github.com/marmot-protocol/whitenoise-android/commit/5c1d14dbeb72e7ebb3b456a352689e29254d16de)
- [chore(deps): bump the kotlin group across 1 directory with 2 updates (#2583)](https://github.com/marmot-protocol/whitenoise-android/commit/86fddb7d831149070c54873cbc18f362e651cf91)
- [Adopt MDK 0.11 polls and v5 audit host configuration (#2872)](https://github.com/marmot-protocol/whitenoise-android/commit/586be0f925ca54a5864e32c8bdf1d38d343dfb54)
- [Retry superseded conversation paging and reply jumps (#2875)](https://github.com/marmot-protocol/whitenoise-android/commit/4638dcbc38c0714da69ce90343a25eadd40567c7)
- [Keep dictation controls visible and pause media only during capture (#2876)](https://github.com/marmot-protocol/whitenoise-android/commit/42bdc36e2da8552c6c08fabc59d5d091bed4f350)
- [test: stabilize master CI screenshot and notification checks (#2881)](https://github.com/marmot-protocol/whitenoise-android/commit/6ce18b02ed68c23f7b4545f82c1bd1111bfe2e16)
- [Measure media latency and keep explicit attachment downloads running (#2879)](https://github.com/marmot-protocol/whitenoise-android/commit/689d3bb548208d3a69d3e75c62d4d7699f6890a5)
- [Fix large received APK attachment handoff (#2882)](https://github.com/marmot-protocol/whitenoise-android/commit/58b665bf3a37c63c06db9990816f1a3be25d4147)
- [Fix attachment worker foreground service type (#2886)](https://github.com/marmot-protocol/whitenoise-android/commit/a6b83f4356eea5ce04b1fb8cbd249fb8d51bc90d)
- [Keep unfocused composer long press from opening keyboard (#2885)](https://github.com/marmot-protocol/whitenoise-android/commit/cc0685da97360ec8a7f4c7d9c54d9c44dec15e34)
- [Settle failed received file opens after durable work (#2887)](https://github.com/marmot-protocol/whitenoise-android/commit/018c28afcc0d499dfc9ac292a98cbce91046edc9)
- [Use system Paste action with GrapheneOS Secure Paste (#2877)](https://github.com/marmot-protocol/whitenoise-android/commit/ba75331b3316581f679d733be592c887e639104d)
- [Add Delete folder action to folder settings (#2884)](https://github.com/marmot-protocol/whitenoise-android/commit/a3425b3403c2b326cdd04009b259e6fc732e5a8d)
- [Test Paste availability after window focus returns (#2889)](https://github.com/marmot-protocol/whitenoise-android/commit/9783d975c573f8ee2548fcbc9622a348ef884566)
- [Improve offline dictation setup and restore media during processing (#2888)](https://github.com/marmot-protocol/whitenoise-android/commit/d51bdd5884e4339509e4d8f4f614229923896f9c)
- [Replace blocked DM composer with unblock notice (#2890)](https://github.com/marmot-protocol/whitenoise-android/commit/8f334f6c990081bd222843ba2592a2a75c1216ff)
- [Trace dictation retries and keep its notification compact (#2894)](https://github.com/marmot-protocol/whitenoise-android/commit/b4954358dd0bce9b5e9f0e625996e0576ec6c4c6)
- [Preserve attachment job ownership across Android restarts (#2893)](https://github.com/marmot-protocol/whitenoise-android/commit/debcc18c037838f344273417214a643a97428e3a)
- [Restore Paste on collapsed composer long press (#2892)](https://github.com/marmot-protocol/whitenoise-android/commit/662e99dde4fdaaced7adc95d228c4693f374f57a)
- [Dismiss stale group-image errors without losing Copy (#2891)](https://github.com/marmot-protocol/whitenoise-android/commit/4866b6e26a2a43a80af98ae7f282613094b6ec19)
- [Prepare Android 2026.9.30 build 20 (#2896)](https://github.com/marmot-protocol/whitenoise-android/commit/6b7ed7e9fd8e3af52646b2b63d0989399c3ae44a)
