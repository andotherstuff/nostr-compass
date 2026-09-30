# Compass42 identity research

Checked at2026-09-30T15:33:44.824663+00:00. Public read-only work; no registry edits, DMs, signatures or relay writes. Nak validates returned event signatures by default; --no-verify was never used. Existing verified entries reused rather than inferred from similarly named accounts. NIP17 inbox availability was NOT tested; authentic identity does not prove current delivery.

Directory npub.world returnedHTTP400 for all21exact requested names. search.nos.today NIP11 explicitly advertisesNIP50;18bounded kind0namequeries were run. Most timedout at9seconds; Dossier/NostrAtlas/Opal candidates were unrelated and not used. Timeouts are transport results, not absence proofs.

## Proposed exact aliases to verified existing identities

- **ContextVM's TypeScript SDK** → existing`ContextVM SDK` (`npub1dvmcpmefwtnn6dctsj3728n64xhrf06p9yude77echmrkgs5zmyqw33jdm`). Primary repository ContextVM/sdk is the existing registered ContextVM SDK project; no new publisher key needed.
- **Nymbot** → existing`Nymchat / Luxas` (`npub16jdfqgazrkapk0yrqm9rdxlnys7ck39c7zmdzxtxqlmmpxg04r0sd733sv`). Primary Zapstore listing links this publisher; signed kind0 event400cbf0035cbae9efbc2f401c8a41ad477097be09a25b0de5d460060b0171bbc explicitly says Developer behind Nymbot.ai,Nymchat.app. This proves person-role beyond release signing alone.
- **Opal** → existing`derek_ross` (`npub18ams6ewn5aj2n3wt2qawzglx9mr4nzksxhvrdc4gzrecw7n5tvjqctp424`). Canonical repo owned by derekross; existing verified developer identity. Fresh kind0 event99fa64de9a0e60e08f1eada69b1c0ca1adcbc4e808fd9a7c2263088e73dde8f1 and grownostr.org NIP05 document match key.
- **fips-pub-domains tests signed public names for a mesh** → existing`fr34aky` (`npub1yptpz34agws3z95dqxgvyhwnhkulav5vueryjpzrl32p57euwteqwha52w`). Canonical repo ownerfr34aky; existing registered maintainer. Fresh signed kind0 eventf34e0cd6c9bdd8e698f5a94288f4dfcf2c2d3838121c66da4ad9b11a980ad6f9 namefr34aky + relayted.de NIP05 confirms publicidentity.
- **ngit-grasp** → existing`ngit / DanConwayDev` (`npub15qydau2hjma6ngxkl2cyar74wzyjshvl65za5k5rl69264ar2exs5cyejr`). Canonical repository is gitworkshop.dev/danconwaydev.com/ngit-grasp; fresh danconwaydev.com NIP05 maps DanConwayDev/_ to a008def15796fba9a0d6fab04e8fd57089285d9fd505da5a83fe8aad57a3564d, matching existing verifiedngit/DanConwayDev key.

## Researched omission records

### Cyberspace: researched_unresolved

Canonical GitHubrepository page200, no public npub found. Both guessed README main/master raw routes404; no inference from those failures. Public ownerprofile inspection recorded separately; NIP50 timedout; directory400.

Sources: https://raw.githubusercontent.com/arkin0x/cyberspace/main/README.md, https://raw.githubusercontent.com/arkin0x/cyberspace/master/README.md

### Dossier: researched_unresolved

Canonical primaryproject source/README has no bound project or maintainer npub. Public directory failed400. NIP50 name search, where applicable, returned unrelated results or timedout; no defensible monitored identity established. Preserve project untagged and out of outreach.

Sources: https://raw.githubusercontent.com/satanrayshe/dossier/main/README.md

### Elisym: researched_unresolved

Canonical primaryproject source/README has no bound project or maintainer npub. Public directory failed400. NIP50 name search, where applicable, returned unrelated results or timedout; no defensible monitored identity established. Preserve project untagged and out of outreach.

Sources: https://raw.githubusercontent.com/elisymlabs/elisym/main/README.md

### Elisym's commerce packages: researched_unresolved

Canonical primaryproject source/README has no bound project or maintainer npub. Public directory failed400. NIP50 name search, where applicable, returned unrelated results or timedout; no defensible monitored identity established. Preserve project untagged and out of outreach.

Sources: https://raw.githubusercontent.com/elisymlabs/elisym/main/README.md

### Holoboard: researched_unresolved

Primary site and README contain no bound project/maintainer npub. NIP50queries Holoboard/ptrio42 timedout; directory400. App release signing identity is not inferred as inbox.

Sources: https://holoboard.space, https://github.com/ptrio42/holoboard.space/blob/main/README.md

### Hubstr Blossom: researched_unresolved

Canonical primaryproject source/README has no bound project or maintainer npub. Public directory failed400. NIP50 name search, where applicable, returned unrelated results or timedout; no defensible monitored identity established. Preserve project untagged and out of outreach.

Sources: https://raw.githubusercontent.com/johninnis/hubstr-blossom/main/README.md, https://raw.githubusercontent.com/johninnis/hubstr-blossom/master/README.md

### Hubstr Blossom server: researched_unresolved

Same project as Hubstr Blossom at johninnis/hubstr-blossom; primary masterREADME contains no npub. Separate fullheading alias needs same researchedunresolved record.

Sources: https://github.com/johninnis/hubstr-blossom/blob/master/README.md

### Iris Chat: project_signing_only

Primary README publishes npub1399g0q2gtwjcglyjcg3jw3rcllqhm375pwases5hkvqa56aqe5wsz2eaap as decentralizedGit/distribution location. Exact kind0 query returned no profile for it. Repository signing/distribution role alone does not establish monitored contact identity. Existing Iris project/mmalmi personal aliases are possible but no new exact role binding verified here.

Sources: https://raw.githubusercontent.com/irislib/iris-chat-rs/main/README.md

### LibreNostr: researched_unresolved

Canonical primaryproject source/README has no bound project or maintainer npub. Public directory failed400. NIP50 name search, where applicable, returned unrelated results or timedout; no defensible monitored identity established. Preserve project untagged and out of outreach.

Sources: https://raw.githubusercontent.com/Lwb89dev/librenostr/main/README.md

### Meshstr: project_signing_only

Raw primaryREADME explicitly lists publisher npub1dxlsl0yzz9yglsephmjmlgrm4cvy4zqmpvtv87mwzwjtrhdzsyjq4xs7uy for signed kind30817 protocol docs and repositories. Publisher role is verified, monitored messaging role not established. Generic NIP50 search timedout; omit outreach until person/projectprofile binding.

Sources: https://gitlab.pocketlabs.dev/meshstr/meshstr, https://gitlab.pocketlabs.dev/meshstr/meshstr/-/raw/main/README.md

### Newlay: researched_unresolved

Canonical primaryproject source/README has no bound project or maintainer npub. Public directory failed400. NIP50 name search, where applicable, returned unrelated results or timedout; no defensible monitored identity established. Preserve project untagged and out of outreach.

Sources: https://code.relay.tools/opensauce/newlay

### Nostr Atlas: donation_identity_only

Primary site zap button binds npub1qsvv5ttv6mrlh38q8ydmw3gzwq360mdu8re2vr7rk68sqmhmsh4svhsft3 as donationbeneficiary. Signed kind0 eventf84405041c85145eca404fca1bdf40eb3c6200bd225a12f2fe63196dc9587768 identifies personal sai y2k profile/website. This supports project donation recipient, not a maintained project notification inbox; omitted pending explicit role evidence.

Sources: https://nostr-atlas.web.app

### Nostr double ratchet: project_signing_only

Primary README binds npub1xdhnr9mrv47kkrn95k6cwecearydeh8e895990n3acntwvmgk2dsdeeycm to decentralized repository. This key is already no_dm as Sirius Business Ltd repository signer; omit outreach. Existing mmalmi verified maintainer might serve a separately role-proven alias, but never treat this repo key as inbox.

Sources: https://raw.githubusercontent.com/irislib/nostr-double-ratchet/main/README.md, https://raw.githubusercontent.com/irislib/nostr-double-ratchet/master/README.md

### WatchTower: verified_new_maintainer_identity

Canonical WatchTower repository owned byiqbqioza. PublicGitHubownerprofile directly publishes npub1takuya0nl8u82tgppggscgnpfz5m5vueckmr5r6xnm5nkyu555lq2uqwf4 and njump.me/iqbqioza.com. Exact Nakkind0 event8df09797a08fc5c4a093cfe5dd2eba0277da407ef02bff827d1a284b159c2182 signed by5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e identifies takuya / iqbqioza and websiteiqbqioza.com. NIP05HTTP403; publicprimarykey+signedprofile supplies cross-binding independently. No NIP17inboxchecked.

Sources: https://github.com/iqbqioza/watchtower, https://github.com/iqbqioza, https://njump.me/iqbqioza.com

### deed: researched_unresolved

Canonical primaryproject source/README has no bound project or maintainer npub. Public directory failed400. NIP50 name search, where applicable, returned unrelated results or timedout; no defensible monitored identity established. Preserve project untagged and out of outreach.

Sources: https://raw.githubusercontent.com/zig-nostr/deed/main/README.md

### nostr-java: researched_unresolved

Canonical primaryproject source/README has no bound project or maintainer npub. Public directory failed400. NIP50 name search, where applicable, returned unrelated results or timedout; no defensible monitored identity established. Preserve project untagged and out of outreach.

Sources: https://raw.githubusercontent.com/tcheeric/nostr-java/main/README.md

Evidence files: `/opt/data/tmp/compass_identity_20260930/primary_sources.json`, `all_primary_directory_checks.json`, `nip50_checks.json`, `known_alias_kind0.jsonl`, `new_primary_kind0.jsonl`, `additional_binding_checks.json`, `github_profile_checks.json`. Unrelated genericsearch candidates are preserved for audit, never accepted recipients.

Existing researched unresolved Armada, nostter, Scramble remain unchanged. This report resolves classification of21previously missing labels, not proof that outreach was sent.

Finalclassification count:5verifiedexistingaliases+1verifiednewmaintainer+15researchedomissions=21exactlabels. WatchTower sourceevidence under watchtower_kind0.jsonl and github_profile_checks.json.

# Three late Compass identity labels

Read-only research; no registry edits or messages. NIP17 inbox discovery remains separate. Returned Nostr profiles were checked by Nak default signature validation.

## Iris's shared runtime

verified_existing_maintainer_alias: `npub1g53mukxnjkcmr94fhryzkqutdz2ukq4ks0gvy5af25rgmwsl4ngq43drvk`

The story includes mmalmi/iris-kit, mmalmi/nostr-pubsub and mmalmi/fips-ts, all existing verified mmalmi scopes. Reuse personal maintainer identity; do not treat npub1xdhnr9... SiriusBusinessLtd repository signer from primaryREADME as inbox. That signing key stays no_dm.

Sources: https://github.com/mmalmi/iris-kit, https://github.com/mmalmi/nostr-pubsub, https://github.com/mmalmi/fips-ts

## Nostr WoT

verified_new_maintainer_identity: `npub1gxdhmu9swqduwhr6zptjy4ya693zp3ql28nemy4hd97kuufyrqdqwe5zfk`

Primarynostr-wot.com homepage and authorblog ViewonNostr link publish this key. Exact Nak signature-verified kind0 event4b62ff9faac0c92a6a060120950ec233abf1079ef0d620cb15641042f9ca9e20 has nameleon and websitenostr-wot.com. Key-to-owned primaryprojectsite and primarysite-to-key crossbind maintainer identity. NIP17inbox notchecked. npubdirectory400; boundedNIP50search timedout, not falselyreported absent.

Sources: https://nostr-wot.com, https://nostr-wot.com/blog/introducing-widgets, https://github.com/nostr-wot/nostr-wot-extension

## ZapTracker

verified_new_maintainer_identity: `npub1s56kqwj9ewz89dn5ns8elfwc4y7vygl0v4etglamw2gkc84cp8ts893h9f`

PrimarydevREADME of pratik227/zap_dashboard identifies Team Pratik with GitHubpratik227 link; primaryGitHubrepo owner agrees. PublicNostrprofile for pratik227 was discovered on Damus; exact signature-verified kind0 eventb5f8bd919fa80999865d2a91576c5b4679f604b0a6554d3b39716a4740eb726e namespratik227 and explicitly says CreatorOfhttps://zap-tracker.netlify.app/. This is personalcreator-role evidence beyond release-key inference. Legacy profiledomain has hyphen; currentREADME liveapp useszaptracker.netlify.app. Name and primaryTeamrepository link identify maintainer, but this is not a verified separateproject account. NIP17inbox notchecked. npubdirectory400,NIP50timedout.

Sources: https://github.com/pratik227/zap_dashboard, https://raw.githubusercontent.com/pratik227/zap_dashboard/dev/README.md, https://github.com/pratik227, https://damus.io/nprofile1qqsg2dtq8fzuhprjke6fcrul5hv2j0xzy0hk2u4507ah9ytvr6uqn4chexkgx, https://zap-tracker.netlify.app/


## Final discovery identities

### SCRUTINY Lens

Canonical primaryREADME and publicGitHubownerprofile publish no bound project/maintainer npub. npub.world directory400; boundedNIP50namequery timedout or found no project-bound profile. No defensible monitoredcontact identity established; omit mentions/outreach.

- https://github.com/crocs-muni/scrutiny-lens
- https://raw.githubusercontent.com/crocs-muni/scrutiny-lens/main/README.md
- https://github.com/crocs-muni

### Mangatsu

Canonical repository owned byimattau. PublicprimaryGitHubownerprofile directly publishes thisnpub. Exact Nak signature-verified kind0 event6f67cf441d5b72a9318fc6023926ccb2aea70464140b4a0617777682295d9697 identifies lostcause, nip05lostcause@3nostr.com, website3nostr.com. Primaryowner-to-key publication binds maintainer role, beyond releasekey inference. Sharedtwoapps recipient must dedupe; no NIP17inboxchecked.

- https://github.com/imattau/Mangatsu
- https://raw.githubusercontent.com/imattau/Mangatsu/master/README.md
- https://github.com/imattau

### Noteds

Canonical repository owned byimattau. PublicprimaryGitHubownerprofile directly publishes thisnpub. Exact Nak signature-verified kind0 event6f67cf441d5b72a9318fc6023926ccb2aea70464140b4a0617777682295d9697 identifies lostcause, nip05lostcause@3nostr.com, website3nostr.com. Primaryowner-to-key publication binds maintainer role, beyond releasekey inference. Sharedtwoapps recipient must dedupe; no NIP17inboxchecked.

- https://github.com/imattau/noteds
- https://raw.githubusercontent.com/imattau/noteds/main/README.md
- https://github.com/imattau

### Statim

Canonical primaryREADME and publicGitHubownerprofile publish no bound project/maintainer npub. npub.world directory400; boundedNIP50namequery timedout or found no project-bound profile. No defensible monitoredcontact identity established; omit mentions/outreach.

- https://github.com/alaibe/statim
- https://raw.githubusercontent.com/alaibe/statim/main/README.md
- https://github.com/alaibe

### Hubstr Relay

Canonical primaryREADME and publicGitHubownerprofile publish no bound project/maintainer npub. npub.world directory400; boundedNIP50namequery timedout or found no project-bound profile. No defensible monitoredcontact identity established; omit mentions/outreach.

- https://github.com/johninnis/hubstr-relay
- https://raw.githubusercontent.com/johninnis/hubstr-relay/master/README.md
- https://github.com/johninnis

### wot

Primaryetemiz/wot README has only abbreviated exampleuserseednpub, no maintainer/projectkey. Ownerprofile has no publicnpub. NIP50etemiz timedout; directory400. This Rustclient/server is distinct from NostrWoT extension/Leon; never reuse similarly namedproject identity.

- https://github.com/etemiz/wot
- https://raw.githubusercontent.com/etemiz/wot/master/README.md
- https://github.com/etemiz

### nostr-relay-khatru

PrimarymasterREADME and ownerGitHubprofile contain no contactnpub. ExactboundedNIP50rzazo24 returned0events; directory400. Khatruupstreamauthorfiatjaf is not inferred to maintain this independentrelay; leave untagged/out of outreach.

- https://github.com/rzazo24/nostr-relay-khatru
- https://raw.githubusercontent.com/rzazo24/nostr-relay-khatru/master/README.md
- https://github.com/rzazo24

### Iris Meet

PrimaryREADME explicitly gives npub1xdhnr9mrv47kkrn95k6cwecearydeh8e895990n3acntwvmgk2dsdeeycm as sourceGitpublisher; existing registry marks this SiriusBusinessLtd repository key no_dm. Do not infer human/monitorednotification inbox from sourcekey. NIP50IrisMeet returned4unrelated profiles. Corporatekey stays excluded; no new personal maintainer binding established in this bounded sweep.

- https://github.com/irislib/meet
- https://raw.githubusercontent.com/irislib/meet/master/README.md
- https://github.com/irislib
