---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
translationOf: /en/newsletters/2026-07-01-newsletter.md
translationDate: 2026-07-01
draft: false
type: newsletters
---

주간 Nostr 가이드 Nostr Compass에 다시 오신 것을 환영합니다.

**이번 주:** [FIPS v0.4.0](#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul)은 Nym mixnet 전송, 선택형 mDNS LAN 탐색, 손실 중 무중단 rekey, 데이터 plane 개편을 내놓았으며 v0.3.0과 wire 호환됩니다. [Whitenoise Linux](#whitenoise-linux-surfaces-as-a-desktop-marmot-client)는 Rust와 Slint로 만든 데스크톱 Marmot 클라이언트로 모습을 드러냈고, 메시지 효과를 전용 kind-9 이벤트로 옮기는 프로토콜 제안도 내놓았습니다. [CustID v0.1.10-beta](#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow)는 NIP-46 원격 signer로 동작하고 NFC로 물리적 접근 챌린지에 응답하는 하드웨어 기반 모바일 신원 vault로 출시되었습니다. [myco](#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh)는 v0.1.0의 새 BLE L2CAP 전송으로 FIPS mesh 위의 peer-to-peer nsite 공유를 시작했습니다. [Nostr Codex Phone](#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr)은 암호화 Nostr DM으로 로컬 Codex worker를 제어하는 Android 앱으로 출시되었습니다. [Amethyst의 미출시 line](#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section)은 NIP-89 app-handler parsing, NIP-34용 Git Repositories feed, nSite와 napplet용 Discover section을 추가했습니다. [Notedeck](#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)은 한 주에 NIP-37, NIP-52, NIP-22를 구현했습니다. [Applesauce](#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut)는 12개 sub-package release와 nbunksec NIP-46 helper 및 Cashu-ts v4 wallet upgrade를 내놓았습니다. [Meiso v1.4.0](#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing)은 addressable kind-35000 기반 Shared-Key Collaborative Lists를 출시했습니다. NIPs repository는 relay roles event, NIP-44의 65,535-byte 제한 해제, NIP-34 fork semantics, NIP-46 client metadata, NIP-86 signevent method를 포함한 PR 다섯 개를 병합했습니다. 심층 분석은 [NIP-86(Relay Management API)](#nip-deep-dive-nip-86-relay-management-api)과 [NIP-89(Recommended Application Handlers)](#nip-deep-dive-nip-89-recommended-application-handlers)를 다룹니다.

---

## 주요 소식

### FIPS v0.4.0, Nym mixnet 전송과 mDNS 탐색 및 데이터 plane 개편

[FIPS](https://github.com/jmcorgan/fips)는 중앙 인프라 없이 node가 서로를 발견하고 traffic을 routing하는 Nostr용 비공개 self-organizing peer-to-peer mesh network입니다. [FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0)은 Nym mixnet 전송, 선택형 mDNS LAN 탐색, 데이터 plane 개편, packet loss 중 무중단 rekey, render-snapshot harness 위에서 다시 쓴 `fipstop` TUI, hot path 밖의 observability plane, 새 OpenWrt apk 및 Nix flake 패키징 대상을 추가했습니다. 모두 v0.3.0과 wire 호환되므로 rolling upgrade 중 혼합 mesh도 상호운용됩니다. 릴리스의 중심은 peer 탐색용 새 전송 두 가지입니다. 새 [outbound Nym mixnet 전송](https://github.com/jmcorgan/fips/releases/tag/v0.4.0)은 FIPS traffic을 `nym-socks5-client` SOCKS5 proxy를 거쳐 [Nym](https://nymtech.net/) cover-traffic network에 섞어, link-level 관찰자가 어떤 mesh peer끼리 통신하는지 상관관계를 찾지 못하게 합니다. `examples/sidecar-nostr-mixnet-relay`는 별도 프로세스로 Nostr relay traffic을 같은 경로에 실어 나릅니다. 선택형 mDNS transport는 LAN에서 `_fips._udp` service record를 광고하고 탐색하므로, operator가 수동 peer 주소나 multicast seed를 설정하지 않아도 같은 로컬 네트워크의 FIPS node가 서로를 찾습니다. 기본값은 꺼짐이며 명시적으로 켜야 합니다.

단일 node 처리량을 높이도록 데이터 plane도 다시 만들었습니다. peer별 encrypt와 decrypt는 이제 receive loop 밖의 전용 worker task에서 실행되므로, 바쁜 peer 하나가 전체 node의 crypto를 직렬화하지 않습니다. Linux send path는 가능한 경우 generic segmentation offload와 connected-UDP socket을 쓰고, receive hot path는 예전에 packet마다 만들던 buffer copy를 피합니다. macOS에는 v0.3.0의 Linux `recvmmsg` batching에 대응하는 `recvmsg_x` batched receive가 추가되었습니다. `fipsctl`과 `fipstop`의 전체 `show_*` 읽기 surface는 이제 control accept task가 lock-free `ArcSwap`에 게시하는 tick별 snapshot에서 응답하므로, receive loop가 바쁜 node에서도 operator 질의가 즉시 처리됩니다. counter만 반환하는 새 `show_metrics` 질의(`fipsctl stats metrics`)는 hot-path 비용 없이 Prometheus scraping을 지원합니다.

FMP와 FSP session rekey는 이제 양방향 packet loss와 reordering에서도 중단되지 않습니다. inbound frame은 K-bit cutover가 pending session을 승격하기 전에 그 session으로 인증되므로 오래되거나 spoofed frame이 rekey를 망칠 수 없습니다. rekey message-1 재전송에는 상한이 생겼고, link-dead heartbeat는 rekey를 인식하며, 고지연 link의 양쪽 동시 시작 race는 symmetric jitter로 엇갈립니다. `fipstop` TUI는 미리 준비한 control-socket 출력에 대해 모든 view의 정확한 text grid와 cell별 style을 검증하는 render-snapshot harness 위에서 다시 만들어졌습니다. 패키징 대상도 추가되었습니다. OpenWrt 25+용 `.apk`는 SDK 없이 기존 `.ipk` cross-compile과 설치 filesystem payload를 재사용해 빌드되며, 프로젝트 root의 `flake.nix`는 고정 toolchain으로 네 binary(`fips`, `fipsctl`, `fips-gateway`, `fipstop`)를 Nix/NixOS에서 source부터 빌드합니다.

### Whitenoise Linux, 데스크톱 Marmot 클라이언트로 등장

[Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git)는 데스크톱 [Marmot](/ko/topics/marmot/) 클라이언트입니다. Nostr relay 위의 MLS group messaging을 Slint UI가 있는 단일 Rust binary로 패키징하며, 모든 비밀값을 password로 암호화된 하나의 vault에 보관합니다.

이번 주 가장 중요한 논의는 Whitenoise 메시지 효과를 parent message를 참조하는 전용 kind-9 이벤트로 전달하자는 제안입니다. 현재 wire format은 메시지 본문 끝에 `dmfx:sparkle` 같은 marker를 붙이므로 이 관례를 모르는 renderer에서는 본문이 오염됩니다. 효과를 별도 이벤트로 옮기면 메시지 text가 깨끗해지고, 더 넓은 Marmot stack이 마주할 설계 질문도 드러납니다. 선택적 rich feature를 inline body 관례로 담을지 sidecar event로 담을지의 문제입니다.

### CustID, NIP-46과 NFC challenge flow를 갖춘 모바일 identity vault로 출시

[CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c)는 Nostr와 SISTR protocol 위에 만든 모바일 identity vault CustID의 첫 공개 beta입니다. CustID는 여러 Nostr identity를 hardware-backed secure storage에 보관하고, 다른 client를 위한 [NIP-46](/ko/topics/nip-46/) remote signer로 동작하며, NFC와 QR code를 통해 물리적·온라인 접근 challenge에 응답합니다.

이 beta는 NIP-46 signer와 NFC challenge-response flow를 완성했으며 zero-knowledge-proof access flow는 향후 milestone으로 남았습니다. 이 릴리스는 앱의 background [NIP-65](/ko/topics/nip-65/) keep-alive layer도 제거했습니다. 기존 layer는 profile별 read relay마다 WebSocket을 열고 client가 즉시 버리는 kind까지 받아들였습니다. 이제 signing-request 알림을 전달하는 NIP-46 socket만 background에서 유지됩니다. 이 수정 덕분에 휴대폰에서 CustID를 다른 client용 bunker로 실용적으로 운영할 수 있습니다.

### myco, FIPS mesh 위에서 peer-to-peer nsite 공유 시작

[myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0)은 6월 27일 공개되어 7월 1일 v0.1.0에 도달했습니다. myco는 주변 사람에게서 앱을 설치하는 Rust Android 앱입니다. FIPS mesh가 전달할 수 있는 모든 transport(UDP, TCP, Tor, Bluetooth)를 통해 peer-to-peer [nsite](/ko/topics/nip-5a/)를 공유하며 완전히 offline으로 작동합니다. FIPS를 transport substrate로, NIP-5A의 static-website event format을 payload로 직접 결합해 nsite로 배포된 앱이 relay나 HTTP에 의존하지 않고 mesh peer 사이를 이동하게 합니다.

v0.1.0은 FIPS가 설치된 휴대폰 두 대가 네트워크 없이 BLE로 peer가 될 수 있는 L2CAP Bluetooth radio path, peer별 speedtest, 앱의 Circle bottom-sheet에서 NFC로 시작하는 공유를 추가합니다. myco는 직접 설치할 수 있도록 Zapstore에도 게시되었습니다.

### Nostr Codex Phone, Nostr로 로컬 Codex worker를 다루는 모바일 control surface로 출시

[Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone)는 암호화 Nostr direct message로 로컬 Codex coding-assistant worker를 제어하는 Android client로 이번 주 출시되었습니다. 여러 repository session, voice transcription, routed worker session, Blossom media upload, 선택적 음성 응답을 지원하므로, 집에서 Codex worker를 실행하는 개발자는 휴대폰이 relay에 접근할 수 있는 어디서든 요청을 보낼 수 있습니다.

이 프로젝트는 #28에 출시된 [CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr)의 직접적인 형제입니다. 둘 다 agentic-coding workflow를 암호화 DM과 함께 Nostr transport에 올리고, network에 구멍을 뚫지 않고 휴대폰에서 집의 worker에 닿게 하는 pairing 및 messaging layer로 Nostr를 사용합니다. 로컬 agent의 control plane으로 Nostr를 쓰는 방식이 확립된 pattern이 되고 있습니다.

### Coop Mobile, 첫 versioned build 게시

[Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1)과 [v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2)는 Android용 [NIP-17](/ko/topics/nip-17/) 암호화 direct-messaging client Coop Mobile의 첫 versioned build로 이번 주 출시되었습니다. 두 릴리스는 message parsing과 QR 처리 주변의 crash safety를 강화하고 logout 때 저장된 모든 데이터를 지웁니다.

### Amethyst, NIP-89 UI와 Git Repositories feed 및 napplet Discover section 구축

[Amethyst](https://github.com/vitorpamplona/amethyst)의 main branch에는 이번 주 여러 새 surface가 만들어졌습니다. [Git Repositories feed](https://github.com/vitorpamplona/amethyst/pull/3406)는 [NIP-34](/ko/topics/nip-34/) repo를 community와 author로 filter할 수 있는 Android timeline category로 만들고, 앱을 떠나지 않고 repo 내용과 commit을 읽는 [smart-HTTP git browser](https://github.com/vitorpamplona/amethyst/pull/3415)와 짝을 이룹니다. napplet host에는 curated web app과 followed nSite 및 napplet을 나열하는 [Discover section](https://github.com/vitorpamplona/amethyst/pull/3409)이 생겼으며, [NIP-89](/ko/topics/nip-89/) handler event와 [NIP-5A](/ko/topics/nip-5a/) site event를 source로 씁니다. Note display는 NIP-89 tag를 통해 [어떤 Nostr 앱이 event를 작성했는지 표시](https://github.com/vitorpamplona/amethyst/pull/3422)합니다. sync 쪽에서는 streaming reconciliation과 자동 relay capability detection을 갖춘 [NIP-77 negentropy 지원](https://github.com/vitorpamplona/amethyst/pull/3434)이 들어왔습니다.

### Buzz v0.3.38, relay attack surface 강화와 provider-independent model 선택

[Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38)은 Buzz가 persona, team, managed agent, NIP-OA owner attestation을 signed Nostr event로 게시할 때 드러나는 [relay attack surface](https://github.com/block/buzz/pull/1369)를 강화합니다. Buzz relay는 team의 Nostr identity와 상태를 담은 공개 record이며, 이 릴리스는 Buzz가 정의한 well-known event kind의 input validation과 replay protection을 강화했습니다. model 선택도 일반화되어 Buzz team이 새 Databricks AI Gateway v2 backend를 포함해 Buzz adapter가 있는 어느 provider든 지정할 수 있습니다.

### Notedeck, NIP-37 private-sync relay와 NIP-52 calendar 및 NIP-22 comment 구현

Damus 팀의 native Rust desktop client [Notedeck](https://github.com/damus-io/notedeck)은 한 주에 protocol 세 가지를 구현했습니다. private-sync relay는 이제 kind `10013` [NIP-37](/ko/topics/nip-37/) list로 유지되어 사용자의 private-content relay set을 public NIP-65 outbox와 분리합니다. `horizon` calendar pane은 nostrdb에서 [NIP-52](/ko/topics/nip-52/) event를 읽고 three-pane layout으로 다시 설계되었습니다. `headway` pane은 kind `1111`에 [NIP-22](/ko/topics/nip-22/) comment-event model을 추가했습니다. NIP-22가 NIP-10 reply threading을 대체하는 통합 comment surface로 정의한 kind입니다.

### Applesauce, nbunksec NIP-46 session과 Cashu v4 wallet upgrade 추가

signer, relay, wallet, content용 modular Nostr toolkit [Applesauce](https://github.com/hzrd149/applesauce)는 sub-package 전반에 걸쳐 [6.2.x release](https://github.com/hzrd149/applesauce/releases)를 냈습니다. signer package는 `nbunksec` import/export helper를 추가해 [NIP-46](/ko/topics/nip-46/) bunker session을 client 사이에서 옮길 수 있는 portable artifact로 다룹니다. wallet package는 [Cashu](/ko/topics/nip-60/) binding을 `@cashu/cashu-ts` v4로 올렸으며, 이 버전에서는 proof amount가 `Amount` value object가 되고 token-decoding API가 바뀝니다.

---

## Tagged release

### mostro-core v0.14.0

[mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0)은 [Mostro](/ko/topics/nip-69/) P2P fiat trading network의 다음 protocol iteration을 제공합니다. [v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2)에 이은 릴리스이며 새 core를 채택한 [mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0)과 함께 나왔습니다. 이번 주 core repository에는 병합 PR 세 개가 들어왔고, 주변 stack(mostro daemon과 Mostro mobile)은 shared types crate v0.14.0에 맞춰집니다.

### ngit v2.6.1

[NIP-34](/ko/topics/nip-34/) repository용 canonical git-over-nostr CLI [ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli)은 이번 주 병합된 [NIP-34 GRASP-06 fork semantics](https://github.com/nostr-protocol/nips/pull/2395)를 구현합니다. repo-state event의 `personal-fork` tag를 `u` tag로 바꾸는 변경입니다.

### mesh-llm v0.72.0 및 v0.72.1

[mesh-llm](https://github.com/Mesh-LLM/mesh-llm)은 Nostr-addressable JSON-RPC surface 뒤에서 open-source LLM을 실행하는 ContextVM stack의 inference component입니다. [v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0)과 [v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1)은 큰 단일 prompt에서 발생하는 batching crash를 고치고 MCP bridge를 deprecated helper에서 옮겼습니다.

### Meiso v1.4.0, MLS를 대체하는 Shared-Key Collaborative Lists 출시

[Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0)은 기존 MLS 기반 task 공유를 더 단순한 addressable-event 설계로 바꾸는 Shared-Key Collaborative Lists model을 도입합니다. 각 shared list는 member에게 배포되는 전용 Nostr key를 만들고, task는 [NIP-44](/ko/topics/nip-44/)로 self-encrypted된 content와 `d=task-id`를 가진 kind `35000` addressable event이며 relay는 task별 Last-Write-Wins를 강제합니다. 이 설계는 client 구현과 relay-level conflict resolution을 단순화하는 대신 MLS의 forward secrecy와 post-compromise security를 포기합니다.

### Cordn 0.3.2

[Cordn 0.3.2](https://github.com/Cordn-msg/cordn)는 group message 게시에서 ephemeral sender pubkey를 제거하고 stale re-request로부터 join-request flow를 강화하는 "more-private-coordinator" track을 제공합니다. Cordn은 [#28의 Cordn Ad-hoc CVM 출시](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator)에서 다룬 MLS 기반 messaging stack이며, 이번 릴리스는 이에 맞춘 coordinator 쪽 update입니다.

---

## 미출시 변경

### diVine, 출시 후 다듬기 PR 108개 병합

Vine을 되살리는 short-form looping video client [diVine](https://github.com/divinevideo/divine-mobile)은 출시 후 대규모 polish 단계에 있습니다. 이번 주 Nostr 관련 작업은 `nostrconnect://` 실패를 structured reason code로 옮기는 [NIP-46](/ko/topics/nip-46/) connect-flow 안정화입니다.

### Zap Cooking, cross-project NIP-46 수정과 composer 개편 계속

[Zap Cooking](https://github.com/zapcooking/frontend)은 recipe를 long-form Nostr event로 게시하는 Nostr recipe-sharing client입니다. 이번 주 작업은 [#28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes)에서 미출시 변경으로 다룬 cross-project [NIP-46](/ko/topics/nip-46/) 수정과 composer 개편을 이어갑니다.

### Conduit, listing flow와 marketplace 정확성 강화

[Conduit](https://github.com/Conduit-BTC/conduit-mono)는 buyer market, merchant portal, store builder를 아우르는 Nostr 기반 three-app marketplace monorepo입니다. 이번 주 작업은 [#28의 출시 보도](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default)에서 다룬 marketplace 정확성 강화를 계속하며, 지난 호 protocol 소식이었던 [NIP-99](/ko/topics/nip-99/) commerce 흐름을 바탕으로 합니다.

### Pollerama v1.12부터 v1.13.1, client tag 선택과 profile tab 및 thread 상한 추가

[Pollerama](https://github.com/formstr-hq/nostr-polls)는 poll과 note에 초점을 두고 web-of-trust discovery를 강화한 Android Nostr client입니다. 이번 주 Zapstore에 v1.12.0, v1.13.0, v1.13.1을 출시했습니다. 사용자는 작성한 note와 poll에 붙일 client tag를 preset에서 고르거나 직접 입력할 수 있습니다. 깊게 중첩된 comment와 reply chain은 몇 단계 뒤 멈추고 note 페이지의 전체 thread로 연결됩니다. profile 페이지는 Notes로 열리며 Posts와 Conversations tab으로 나뉩니다. 새로 follow한 account가 앱 재시작 뒤 사라지는 follow persistence bug가 수정되었고 follow button은 진행 상태를 표시합니다.

### getwired.app과 get-tao.app, NIP-13 confess 제출 flow 수정

submit 때 spam을 억제하도록 NIP-13 proof-of-work를 추가하는 anonymous-posting flow를 공유하는 [getwired.app](https://github.com/smolgrrr/Wired)과 [get-tao.app](https://github.com/smolgrrr/TAO)은 PoW mining 중 UX가 일관되도록 [confess 제출 flow](https://github.com/smolgrrr/Wired/pull/57)를 고쳤습니다.

### nostui, mention timeline tab 추가

Rust로 만든 terminal Nostr client [nostui](https://github.com/akiomik/nostui)는 활성 pubkey를 tag한 kind:1 event를 TUI의 전용 view로 보여주는 [mention timeline tab](https://github.com/akiomik/nostui/pull/463)을 추가했습니다.

### Heartwood, identity별 NIP-46 bunker URI와 HSM-mode signing bridge 추가

[Heartwood](https://github.com/forgesworn/heartwood)는 signing key가 client에 전혀 전달되지 않는 [NIP-46](/ko/topics/nip-46/) signer입니다. client는 작은 relay에 NIP-46으로 통신하고 relay는 signature를 만드는 attached hardware device에 serial frame protocol로 통신합니다. 이번 주 프로젝트에는 [relay-to-serial signing bridge](https://github.com/forgesworn/heartwood/pull/11)와 [identity별 bunker connection](https://github.com/forgesworn/heartwood/pull/16)이 들어와, 여러 identity를 가진 hardware device 하나가 각각에 별도 bunker URI를 노출합니다.

### Nostter auth 및 signer refactor

[Nostter](https://github.com/SnowCait/nostter)는 이번 주 [auth와 signer layer](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth)를 다시 만들며 login 상태를 single signal로 옮기고 signer dispatch를 strategy module로 추출했습니다. 목표는 NIP-07 web extension, NIP-46 remote bunker, raw nsec이 하나의 code path를 공유하는 깔끔한 signer abstraction입니다.

### Dart NDK, NIP-07 signer 분리와 NIP-59 timestamp 무작위화

[Dart NDK](https://github.com/relaystr/dart_ndk)는 [NIP-07](/ko/topics/nip-07/) signer를 core package에서 Flutter WebView가 있는 `ndk_flutter`로 옮기고, 암호화 메시지의 timing correlation을 어렵게 하도록 [NIP-59 gift-wrap timestamp를 무작위화](https://github.com/relaystr/dart_ndk/pull/667)했습니다.

### Milk Market, NIP-23 storefront page와 Square 결제 처리 추가

Shopstr 팀의 marketplace storefront [Milk Market](https://github.com/shopstr-eng/milk-market)은 seller의 [NIP-23](/ko/topics/nip-23/) long-form event를 기반으로 한 blog 페이지를 모든 storefront에 추가하고, 편집 가능한 section과 직접 blog-setting route를 제공했습니다. 같은 주에 seller용 대체 payment processor [Square](https://github.com/shopstr-eng/milk-market/pull/30)와 결제된 order의 shipping-label 자동 구매도 추가했습니다.

### Calendar by Formstr, iOS 앱 출시

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar)는 이번 주 [PR #159 IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159)을 병합해 [NIP-52](/ko/topics/nip-52/) calendar client를 iOS로 가져왔습니다. [PR #197](https://github.com/formstr-hq/nostr-calendar/pull/197)은 local time의 calendar-date parsing을 고치고, [PR #201](https://github.com/formstr-hq/nostr-calendar/pull/201)은 `run-tests` label로 시작되는 Playwright E2E workflow를 추가합니다.

### cagliostr, NIP-22와 coordinate별 NIP-09 및 NIP-13 proof-of-work 강제

Go relay 구현 [cagliostr](https://github.com/mattn/cagliostr)는 이번 주 세 enforcement path를 강화했습니다. incoming event에 [설정 가능한 NIP-13 proof-of-work](https://github.com/mattn/cagliostr/pull/7)를 적용하고, event-id 삭제만으로 닿지 않는 replaceable event를 `a` tag로 삭제하도록 [addressable coordinate별 NIP-09 삭제](https://github.com/mattn/cagliostr/pull/8)를 지원하며, 지나치게 과거나 미래 timestamp의 event를 거부하는 [설정 가능한 NIP-22 timestamp 제한](https://github.com/mattn/cagliostr/pull/9)을 추가했습니다.

---

## 새로 추적·발견한 프로젝트

[Vanderwarker wellbeing suite](https://git.vanderwarker.family/wellbeing)는 하나의 publisher signing key로 현실 세계 telemetry를 Nostr event로 게시합니다. 다섯 sibling app으로 구성됩니다. [Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android)은 fitness data를 `kind:30078`로 Nostr에 고정하는 step tracker, [Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android)은 하루 phone unlock 횟수를 게시하는 앱, [Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android)은 현재 media playback을 User Status로 게시하는 앱, [Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android)는 15분마다 battery level, voltage, temperature를 게시하는 앱, [Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android)는 일일 data usage를 게시하는 앱입니다. 다섯 앱 모두 6월 24일부터 30일 사이 Zapstore에 등장했습니다.

[ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9)는 Rust와 Slint로 만든 암호화 serverless 실시간 위치 공유 Android 앱으로 6월 29일 출시되었습니다. [#28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot)에서 다룬 [Haven](https://github.com/mehmetefeumit/Haven-App) [Marmot](/ko/topics/marmot/) 기반 위치 공유 앱의 sibling이지만 transport architecture가 다릅니다. ntrack은 암호화 Nostr DM으로 위치 update를 전달하고 Haven은 Marmot group message를 사용합니다.

[NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell)은 Nostr 앱을 만들기 위한 초기 application shell scaffold입니다. 프로젝트는 이번 주 첫 user-facing documentation을 게시했습니다.

[NIPs by Pollerama](https://nips.pollerama.fun)(repository [abh3po/better-nips](https://github.com/abh3po/better-nips), 2026-06-29 생성)는 [NostrHub](https://nostrhub.io)의 `kind:30817` community-authored NIP을 위한 새 client로, nostrhub.io에 대한 trust-weighted 대체 surface입니다. 각 `kind:30817` NIP은 full Markdown rendering과 정의하는 event kind를 보여주는 공유 가능한 URL(`#/nip/<naddr>`)을 가집니다. client는 Following, Web of Trust(follows-of-follows), Global의 세 feed를 제공하며 trust-weighted approval 또는 최신순으로 정렬할 수 있습니다. approval은 kind `1985`의 [NIP-32](/ko/topics/nip-32/) label로 게시되며 tag `["L","nostrhub"]`, `["l","approve","nostrhub"]`, 대상 NIP address를 가리키는 `a` tag, `better-nips`를 알리는 `client` tag를 포함합니다. NostrHub 자체가 서명하는 event와 정확히 같은 형태라 두 client의 approval이 상호 호환됩니다. ranking에서는 direct follow의 approval이 second-degree follow보다 높은 weight를 받고, Global feed는 user의 social graph 밖 approval도 보여줍니다.

signing stack은 [`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer)이며 [NIP-07](/ko/topics/nip-07/), [NIP-46](/ko/topics/nip-46/) bunker와 nostrconnect, [NIP-49](/ko/topics/nip-49/) ncryptsec, [NIP-55](/ko/topics/nip-55/) Android signer를 다루는 full login modal을 제공합니다. session은 reload 때 조용히 다시 attach됩니다. network layer는 [`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay)를 사용합니다. 이 Web Worker는 큰 web-of-trust set이 한 relay로 fan-out되지 않도록 사용자의 [NIP-65](/ko/topics/nip-65/) outbox를 relay별로 나눕니다. community NIP은 NostrHub, `better-nips`, 다른 미래 client 중 어디에 hosted되든 protocol 수준에서 모두 같고 ranking은 moderator curation이 아니라 social graph에서 나온다는 설계입니다. 이는 [#25](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling)의 deep dive가 다룬 NIP-32 labeling flow와 직접 맞물립니다.

이번 주 새 [NIP-34](/ko/topics/nip-34/) repo cluster 두 개가 나타났습니다. [Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git)는 video 중심 Nostr client이며, [nostrapps.com cluster](wss://gitnostr.com)는 sibling project 세 개를 게시합니다. [verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git)는 desktop용 napp VM, [hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git)는 customizable communities client, [napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git)는 HTML microapps spec과 runtime입니다. 이 cluster는 지난 호 lead story에서 다룬 [napplet](/ko/topics/nip-5d/) 작업과 나란히 놓입니다.

---

## Protocol 작업과 NIP update

### 병합: NIP-44, 65,535-byte payload 제한 해제

[PR #1907](https://github.com/nostr-protocol/nips/pull/1907)은 2024-09부터 열린 채 6월 28일 병합되었습니다. [NIP-44](/ko/topics/nip-44/) versioned-encryption envelope의 plaintext payload 상한 65,535 byte를 없애고 4 GiB(`uint32_max`)까지 높입니다. NIP-44 wire format은 payload length를 `uint16`으로 encode했고 원 사양은 interop을 위해 이를 엄격히 요구했습니다. 병합된 변경은 version byte에 tag된 longer-length field를 채택해 v2 구현은 wire 호환성을 유지하고 v3+ 구현은 더 긴 길이를 전달합니다. [NIP-17](/ko/topics/nip-17/) direct message, [NIP-59](/ko/topics/nip-59/) gift wrap, [NIP-46](/ko/topics/nip-46/) remote-signer payload 또는 다른 NIP-44 암호화 Nostr message를 쓰는 client는 이제 application layer에서 나누지 않고 64 KiB보다 큰 단일 event를 교환할 수 있습니다.

### 병합: NIP-86, signevent method와 Relay Roles event 추가

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389)은 [NIP-86](/ko/topics/nip-86/) relay management JSON-RPC API에 `signevent` method를 추가해 administrator가 relay의 자체 pubkey로 event를 서명하도록 요청할 수 있게 합니다. 함께 나온 [PR #2390](https://github.com/nostr-protocol/nips/pull/2390)은 relay가 administrator와 moderator를 선언하도록 게시하는 replaceable Relay Roles event를 정의합니다. 둘을 합치면 NIP-86 client는 relay의 admin list를 조회하고 out-of-band trust 없이 인증된 request가 현재 admin에게서 왔는지 검증할 수 있습니다. 두 변경은 아래에서 심층 분석합니다.

### 병합: NIP-34, GRASP-06에서 personal-fork를 `u`로 교체

[PR #2395](https://github.com/nostr-protocol/nips/pull/2395)은 6월 24일 병합되어 [NIP-34](/ko/topics/nip-34/) repo-state event(`kind:30618`)의 `personal-fork` tag를 "upstream"을 뜻하는 `u` tag로 바꾸고, wire format을 GitWorkshop suite가 구현해 온 GRASP-06 fork semantics와 맞췄습니다. 이 변경은 다른 fork-semantics 해법을 제안한 [PR #2384](https://github.com/nostr-protocol/nips/pull/2384)(`NIP-34: remove maintainers to solve expiry issues`)를 닫습니다. 병합된 방향은 ngit v2.6.x가 구현하므로 사양과 reference CLI가 일치합니다. 기존 `personal-fork` repo도 계속 상호운용되며 새 repo와 ngit v2.6 line은 `u` tag를 게시합니다.

### 병합: NIP-46 client metadata, Amber 출시 뒤 upstream 반영

[PR #2381](https://github.com/nostr-protocol/nips/pull/2381)은 6월 23일 병합되어 [NIP-46](/ko/topics/nip-46/) `connect` request에 optional client metadata를 추가했습니다. client가 signer connect 때 이름, icon URL, homepage URL을 게시할 수 있습니다. [Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2)는 지난주 이 metadata extension을 출시했고 [#28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata)에서 다뤘습니다. 이번 주 upstream NIP이 이미 출시된 구현을 따라잡았습니다.

### 공개: epoch 기반 deterministic NIP-17 wrapper key

[PR #2397](https://github.com/nostr-protocol/nips/pull/2397)과 [PR #2396](https://github.com/nostr-protocol/nips/pull/2396)은 수렴하는 두 NIP-17 wrap-key 제안입니다. PR #2397은 [NIP-59](/ko/topics/nip-59/) gift wrap을 작성하는 ephemeral signing key를 coarse time epoch에 묶인 conversation별 seed에서 deterministically 유도해, conversation key를 아는 recipient가 subscribe할 pubkey를 예측하게 하자고 제안합니다. 현재 사양은 wrap마다 새 random key를 요구해 이 예측이 불가능합니다. PR #2396은 companion 변경으로, conversation wrap을 conversation key 자체로 서명해 wrap pubkey가 conversation identifier 역할도 하게 합니다. 둘은 metadata leakage 없이 filter 가능한 NIP-17 conversation을 만드는 경로를 정의합니다. 둘 다 열려 있고 논의 중입니다.

### 공개: relay가 kind:13 seal event를 거부해야 한다는 NIP-59 제안

[PR #2399](https://github.com/nostr-protocol/nips/pull/2399)은 [NIP-59](/ko/topics/nip-59/) gift wrap의 inner seal인 kind:13 event가 publish request의 top level에 나타나면 relay가 거부해야 한다고 제안합니다. seal event는 wrap 안에서만 의미가 있고 유출된 seal은 recipient pubkey를 노출하기 때문입니다. 함께 나온 [issue #2398](https://github.com/nostr-protocol/nips/issues/2398)은 seal을 ephemeral kind로 다시 정의하자고 더 나아갑니다. NIP-01 ephemeral kind는 relay에 저장되지 않으므로 protocol 수준에서 규칙을 강화하고 relay별 policy 의존을 없앨 수 있습니다.

### 공개: NIP-29 group state

[PR #2372](https://github.com/nostr-protocol/nips/pull/2372)은 [NIP-29](/ko/topics/nip-29/)(relay 기반 group)에 명시적 group-state semantics를 추가합니다. group이 open, closed, public, private, archived라는 뜻과 state transition이 member event와 상호작용하는 방식을 정의합니다. client별이던 의미를 relay 사양으로 끌어옵니다.

### 공개: NIP-34 optional multi-maintainer 지원

[PR #2324](https://github.com/nostr-protocol/nips/pull/2324)은 위에서 다룬 병합 [PR #2395](https://github.com/nostr-protocol/nips/pull/2395)(GRASP-06 fork semantics)의 companion 제안입니다. [NIP-34](/ko/topics/nip-34/) repo announcement event(`kind:30617`)에 optional multi-maintainer 지원을 더해 repeated `maintainer` tag로 여러 canonical maintainer pubkey를 선언하게 합니다. 선언된 maintainer가 서명한 patch와 issue는 client가 official로 신뢰합니다. 공동 maintainer가 있는 NIP-34 repo가 모든 작업을 pubkey 하나로 보내거나 off-protocol coordination에 의존해야 하던 문제를 해결합니다.

### 공개: filter용 NIP-91 AND operator, 제안은 병합되지 않음

[PR #2252](https://github.com/nostr-protocol/nips/pull/2252)는 Nostr [filter](/ko/topics/nip-01/)용 AND operator 제안으로, 이전에 닫힌 [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)의 설계를 다시 엽니다. [nostr-rs-relay](https://github.com/v0l/nostr-rs-relay), applesauce, [Amethyst](https://github.com/vitorpamplona/amethyst), worker-relay에 이미 구현되어 있지만 spec PR 자체는 열려 있습니다.

### 종료: pats2sats commerce NIP 네 개

이번 주 Nostr commerce 제안 네 개가 닫혔습니다. Escrow([#2334](https://github.com/nostr-protocol/nips/pull/2334)), Reservations([#2335](https://github.com/nostr-protocol/nips/pull/2335)), [NIP-99](/ko/topics/nip-99/) Marketplace Listing Extension([#2346](https://github.com/nostr-protocol/nips/pull/2346)), Accommodation Listing Profile([#2333](https://github.com/nostr-protocol/nips/pull/2333))입니다. 같은 commerce surface는 이제 [Gamma Market Spec](https://github.com/GammaMarkets/market-spec)에 통합되고 있습니다. 이 project-owned extension repository는 NIP-99 marketplace listing 위에 order, checkout, escrow, dispute semantics를 조합합니다. Compass는 Marmot와 Blossom처럼 NIPs repository 밖의 protocol-spec repo로 이를 추적합니다. 이번 주 열린 PR에는 client-attribution 명확화([#11](https://github.com/GammaMarkets/market-spec/pull/11)), product-identity 변경용 supersedes tag([#8](https://github.com/GammaMarkets/market-spec/pull/8)), merchant-review semantics([#7](https://github.com/GammaMarkets/market-spec/pull/7))가 있습니다.

### 공개: Bitcoin identity linkage

Bitcoin identity를 Nostr identity에 연결하는 제안 두 개가 이번 주 열렸습니다. [NIP-352 Bitcoin Silent Payment Address](https://github.com/nostr-protocol/nips/pull/2392)와 [Bitcoin-OTC Identity Linkage Proof](https://github.com/nostr-protocol/nips/pull/2401)입니다.

---

## NIP 심층 분석: NIP-86(Relay Management API)

[NIP-86](/ko/topics/nip-86/)은 relay management를 위한 JSON-RPC interface를 정의해 authorized client가 표준 API로 relay에 administrative command를 보내게 합니다. client 하나로 relay별 tooling 없이 어느 NIP-86-compatible relay든 관리할 수 있습니다. 이번 주 spec merge 두 개([PR #2389](https://github.com/nostr-protocol/nips/pull/2389), [PR #2390](https://github.com/nostr-protocol/nips/pull/2390))는 relay-signed event와 relay가 선언한 administrator 사이의 고리를 닫습니다.

### Transport

NIP-86 management request는 relay가 WebSocket connection을 제공하는 것과 같은 URI로 보내는 HTTP POST이며 `Content-Type: application/nostr+json+rpc`를 사용합니다. request body는 다음 형태의 JSON document입니다.

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

authentication은 `Authorization` header의 [NIP-98](/ko/topics/nip-98/) HTTP-auth signed event를 사용합니다. relay는 method를 실행하기 전에 signing pubkey가 administrator list에 있는지 검증합니다. relay response는 다음 형태의 JSON document입니다.

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### 이번 주 이전부터 있던 method

기존 method set은 pubkey ban(`banpubkey`, `allowpubkey`, `listbannedpubkeys`), event ban(`banevent`, `allowevent`, `listbannedevents`), relay metadata(`changerelayname`, `changerelaydescription`, `changerelayicon`), allowed-pubkey list 관리(`allowkind`, `disallowkind`, `listallowedkinds`), relay 통계를 반환하는 `stats`를 다룹니다. client가 그 위에 typed binding을 올릴 수 있도록 표준 JSON-RPC service와 의도적으로 비슷한 형태입니다.

### 이번 주 변경

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389)은 spec에 `signevent` method를 추가합니다. method는 partial event template(kind, tags, content)을 argument로 받아 relay가 자체 pubkey를 `pubkey` field에 넣어 서명한 complete event를 반환하도록 요청합니다. relay가 자기 자신에 대한 protocol-level event를 게시하기 위한 전제입니다. blocked-pubkey announcement, relay metadata, 아래의 새 Relay Roles event는 모두 operator-controlled key로 relay가 서명해야 하지만, 대부분 relay operator는 administrative client에 private key를 보관하고 싶어 하지 않습니다.

[PR #2390](https://github.com/nostr-protocol/nips/pull/2390)은 Relay Roles event를 정의합니다. relay가 자체 pubkey로 `signevent`를 통해 서명하여 게시하는 parameterised replaceable event kind로, administrator와 moderator pubkey를 명시적 role semantics와 함께 선언합니다. NIP-86-aware client는 추적하는 relay에서 Relay Roles event를 가져와 event tag로 admin list를 만들고, out-of-band trust나 relay별 설정 없이 authenticated NIP-86 request가 현재 admin에게서 왔는지 검증할 수 있습니다. 두 PR은 함께 고리를 닫습니다. `signevent`가 mechanism이고 Relay Roles가 그 위에 만든 첫 event kind입니다.

### NIP-86 request 예시

완전한 NIP-86 `banpubkey` request는 다음과 같습니다.

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

`Authorization` header에는 NIP-98 signed event가 담깁니다.

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

signing pubkey는 relay의 admin set(이제 relay-roles event에 선언됨)에 있어야 하고, `u` tag는 relay의 HTTPS URL과 일치해야 하며, `payload` tag는 JSON request body의 SHA-256과 일치해야 합니다. relay는 다음을 반환합니다.

```json
{
  "result": true,
  "error": null
}
```

### 구현

- [Amethyst](https://github.com/vitorpamplona/amethyst)는 Android에 NIP-86 relay management UI를 제공합니다(v1.07.0+).
- spec을 구현한 reference relay에는 [strfry](https://github.com/hoytech/strfry), [khatru](https://github.com/fiatjaf/khatru), 그리고 spec의 `Implementation Status` section이 연결하는 여러 작은 구현이 있습니다.

구현자들이 `signevent`와 Relay Roles 변경을 반영하면 NIP-86-aware client는 relay-roles event를 relay admin list의 canonical source로 다루기 시작할 것입니다.

---

## NIP 심층 분석: NIP-89(Recommended Application Handlers)

[NIP-89](/ko/topics/nip-89/)는 parameterised replaceable event kind 두 개를 정의합니다. 앱 개발자가 게시하는 application handler `kind:31990`과 사용자가 쓰는 앱을 추천하는 `kind:31989`입니다. 둘을 통해 client는 out-of-band coordination 없이 모르는 event kind를 처리하는 application을 찾을 수 있습니다. native로 처리하지 못하는 `kind:30030` event를 만난 longform reader는 NIP-89 graph에서 handler를 질의하고, 해당 event를 처리하는 published app으로 사용자를 보내는 `Open in...` flow를 제공할 수 있습니다. NIP-89는 이번 호 곳곳의 napplet/napps 작업이 composable Nostr-native applet으로 확장하는 cross-app routing 문제의 원래 기반입니다.

### Application handler event(`kind:31990`)

app developer는 app이 지원하는 event kind와 Nostr entity를 app에서 여는 방법을 설명하는 handler event를 하나 이상 게시합니다.

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

`d` tag는 handler를 식별해 replace할 수 있게 하고, 각 `k` tag는 app이 처리하는 event kind를 선언합니다. 각 platform tag(`web`, `ios`, `android`, ...)는 호출하는 client가 open 때 대체할 [NIP-19](/ko/topics/nip-19/) encoded entity placeholder `<bech32>`가 있는 URL template를 제공합니다. 같은 routing pattern을 공유한다면 handler event 하나가 여러 지원 kind를 알릴 수 있어 app discovery를 compact하게 유지하고 kind마다 별도 handler event를 만드는 일을 피합니다.

### User recommendation event(`kind:31989`)

사용자는 특정 event kind에 어떤 앱을 쓰는지 선언하는 recommendation을 게시합니다.

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

`d` tag는 추천 대상 event kind를 담습니다. 각 `a` tag는 `kind:31990` handler event를 가리키는 NIP-01 address pointer이며, 추천 relay와 recommendation이 적용되는 platform을 함께 담습니다. 같은 recommendation에 platform별 여러 앱을 나열할 수 있습니다.

### Client tag와 privacy tradeoff

NIP-89는 event를 게시하는 앱이 작성 event에 붙일 수 있는 optional `client` tag도 정의합니다.

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

이를 통해 event를 보여주는 client는 어느 앱에서 왔는지 표시하고, 더 풍부한 handler metadata를 조회하며, handler가 선언한 rendering hint를 따를 수 있습니다. 사양은 privacy 비용도 명시합니다. 모든 event에 `client` tag를 내보내면 사용자의 software identity가 공개되고 시간이 지나며 usage pattern이 드러납니다. spec은 client가 opt-out을 제공하도록 권합니다.

Amethyst의 [PR #3422](https://github.com/vitorpamplona/amethyst/pull/3422)는 event display에서 NIP-89 `t`, `i`, `a`, `client` tag를 parse하고 보여주어 timeline에서 note를 작성한 앱을 직접 드러냅니다.

### 실제 discovery flow

모르는 event kind를 받은 client는 다음 순서를 밟습니다. (1) 사용자의 follow graph에서 해당 event kind와 일치하는 `d` tag를 가진 `kind:31989` event를 질의합니다. (2) 추천된 각 `a` tag를 `kind:31990` handler event로 resolve합니다. (3) 현재 platform과 맞는 `web`, `ios`, `android` URL template의 handler를 고릅니다. (4) entity의 `bech32` encoding을 URL template에 대입합니다. (5) 결과 URL을 `Open in...` 선택지로 제공합니다. 이 flow는 social filter를 거칩니다. 신뢰하지 않는 relay의 임의 handler event를 질의하면 악성 앱으로 redirect될 수 있으므로, 모든 published handler를 똑같이 신뢰하는 것보다 사용자가 follow하는 사람에서 시작하는 편이 안전한 기본값입니다.

### NIP-89와 napplet layer

Amethyst의 Discover section, napplet-host runtime, `client`-tag display는 Android에 완전한 NIP-89 consumer surface를 함께 만듭니다. 지난 호에 출시된 napplet spec은 NIP-89 handler event가 가리킬 수 있는 대상을 확장합니다. Nostr와 Blossom 위에서 composable Nostr-native runtime을 실행하는 sandboxed applet입니다. NIP-89가 discovery 및 routing graph이고 napplet runtime은 그 graph가 가리킬 수 있는 execution target 하나입니다.

---

*피드백, 수정 사항, 빠뜨린 프로젝트가 있다면 [github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass)에 issue를 열거나 npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923으로 NIP-17 DM을 보내주세요.*
