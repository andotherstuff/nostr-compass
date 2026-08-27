---
title: 'Nostr Compass #28'
date: 2026-06-24
publishDate: 2026-06-24
translationOf: /en/newsletters/2026-06-24-newsletter.md
translationDate: 2026-08-27
draft: false
type: newsletters
---

주간 Nostr 가이드 Nostr Compass에 다시 오신 것을 환영합니다.

**이번 주:** [Sprout가 Buzz로 이름을 바꾸고](#sprout가-buzz로-이름을-바꾸고-persona-team-managed-agent를-relay-event로-게시) persona, team, managed-agent 기록을 Nostr relay event로 게시하기 시작했습니다. 기기 간 읽음 상태와 메시지별 읽음 표시가 기존 badge-frontier 모델을 대체합니다. sandwich.farm의 [Napplets](#napplets-명확한-trust-boundary를-갖춘-조합형-nostr-앱)는 Nostr와 Blossom으로 배포하는 조합형 Nostr 앱을 위한 trust-boundary 프로토콜로 출시됩니다. [Conduit](#conduit가-marketplace-mvp를-강화하고-공개-relay를-기본값으로-전환)(Nostr 기반 3개 앱 marketplace monorepo: 구매자 Market, Merchant Portal, Store Builder, 그리고 저장소 안의 자체 NIP 및 사양 디렉터리)는 17개 PR을 병합해 marketplace MVP를 강화하고, 공개 relay를 기본값으로 전환하며, 프라이버시를 지키는 분석 기능을 추가합니다. [BitBlik](#bitblik이-nostr-기반-p2p-blik-lightning-교환-프로토콜을-출시)은 암호화된 Nostr DM 위에 P2P BLIK-Lightning 교환 프로토콜을 내놓습니다. coordinator는 법정화폐와 Lightning hold invoice 사이를 원자적으로 결제합니다. [Amethyst](#amethyst-v1121부터-v1126까지-v1120-출시를-후속-보완)는 지난주 지갑·팟캐스트·운동 기능 출시에 이어 Health Connect Workouts, Road Events, 접을 수 있는 답글, 분류기를 갖춘 relay 지연 상태 추적, macOS 공증 수정을 내놓습니다. [Amber](#amber-v622가-nip-46-client-metadata를-구현)는 지난주 제안된 NIP-46 client-metadata 확장을 구현해 signer 요청 화면에 네이티브 앱 아이콘과 신원을 표시합니다. [Haven](#haven이-marmot에서-비공개-위치-공유를-출시)은 Marmot 암호화 메시징 프로토콜 위에 비공개 위치 공유를 출시합니다. [CodeDeck](#codedeck-nostr를-통한-원격-agentic-coding)은 암호화된 Nostr relay를 통해 휴대폰에서 노트북의 Claude Code 세션을 제어하게 해주고, pairing을 QR 스캔 한 번으로 줄인 뒤 세션별 모델 선택을 추가합니다. [Grain](#grain-v080-rc1이-완전한-nostr-client-engine을-출시)은 outbox 모델을 사용하는 가져오기 가능한 Go Nostr client library를 제공합니다. Mostro Core, Wisp와 Dark Wisp, Citrine, FIPS, Kubo(부모가 선별한 YouTube 채널과 의무 trust-gated 어린이 feed), Pollerama(web-of-trust 점수, 기기 내 relay engine, "알 수도 있는 사람" 목록)는 후속 patch를 내놓습니다. 미출시 작업에는 sandwich.farm의 브라우저 기반 MLS coordinator, nostter의 UX 개선 sprint, Zap Cooking의 여러 프로젝트에 걸친 NIP-46 수정과 composer 개편, Shopstr의 Cashu escrow lifecycle, divine.video, Nostur가 포함됩니다. 새로 추적하는 프로젝트는 Social Agents Prototype, git-over-Nostr issue triage 도구 PRana, routstr-chat입니다. 프로토콜 쪽에서는 NIP-99에 Conduit, BitBlik, Shopstr의 commerce 작업과 직접 맞물리는 on-graph checkout 및 escrow 제안이 추가됐습니다. 6월 마지막 Compass인 만큼 이번 호는 [Nostr의 여섯 번의 6월](#nostr의-여섯-번의-6월)로 마무리합니다.

---

## 주요 소식

### Amethyst v1.12.1부터 v1.12.6까지, v1.12.0 출시를 후속 보완

[Amethyst](https://github.com/vitorpamplona/amethyst)는 [지난주 v1.12.0 출시](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)에 이어 수요일부터 금요일까지 patch 여섯 개를 빠르게 내놓았습니다. [v1.12.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.1)은 Health Connect Workouts와 Share-as-Image 작업을 추가하고, bootstrap callback이 gate와 경쟁하지 않도록 Tor `Active` flag를 결정적으로 만듭니다. [v1.12.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.2)는 Road Events와 접을 수 있는 답글을 추가하고, [v1.12.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.3)은 분류기와 dashboard UI를 갖춘 relay 지연 상태 추적 및 macOS 공증 수정을 도입합니다. [v1.12.4](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.4)부터 [v1.12.6](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.6)까지는 Crowdin 번역과 번역자 credit 자동화를 제공합니다.

### Sprout가 Buzz로 이름을 바꾸고 persona, team, managed agent를 relay event로 게시

[Sprout](/en/newsletters/2026-04-29-newsletter/#sprout-adds-owner-attestation-and-multi-workspace-support)는 Block이 만든 self-hostable workspace입니다. 사람과 AI agent가 같은 channel에서 협업하며 모든 메시지, reaction, workflow 단계, review 승인, git event가 서명된 Nostr event로 기록됩니다. 이번 주 프로젝트 이름이 [Buzz](https://github.com/block/buzz)로 바뀌었습니다. GitHub는 이제 기존 `block/sprout` slug를 `block/buzz`로 redirect하며, 저장소와 license, 제품 방향은 그대로입니다. 과거 호에서 다룬 Sprout는 모두 같은 프로젝트를 가리킵니다.

이름 변경과 함께 상당한 제품 작업도 들어왔습니다. [PR #1189](https://github.com/block/buzz/pull/1189)를 통해 persona, team, managed-agent 기록을 Nostr relay event로 게시하므로, 상태를 복제하지 않고도 같은 agent 신원이 여러 workspace와 audit log에 나타날 수 있습니다. 새 desktop pane은 profile에 NIP-OA owner attestation을 보여 줍니다([PR #1198](https://github.com/block/buzz/pull/1198)). channel thread의 읽지 않음 badge frontier는 메시지별 읽음 표시로 교체되어 기기 간 읽지 않음 개수가 정확히 유지됩니다([PR #1178](https://github.com/block/buzz/pull/1178)). inbox에는 reminder event의 작성자와 출처 표시가 추가됩니다([PR #1176](https://github.com/block/buzz/pull/1176)).

임시 channel의 기본 만료 기간은 이제 7일입니다([PR #1182](https://github.com/block/buzz/pull/1182)). agent별 relay override는 workspace 기본값으로 fallback하기 전에 설정된 relay를 우선합니다([PR #1131](https://github.com/block/buzz/pull/1131)). Windows build는 shell tool용 Git-for-Windows toolchain 전체를 bundle합니다([PR #1145](https://github.com/block/buzz/pull/1145)).

### Napplets: 명확한 trust boundary를 갖춘 조합형 Nostr 앱

Sandwich.farm은 이번 주 [napplet.run](https://napplet.run)을 조합형 Nostr applet, 즉 napplet을 위한 프로토콜로 발표했습니다. napplet은 한 가지 일을 수행하고 sandbox 환경에서 실행되며, nsite와 같은 event 형태를 사용해 Nostr와 Blossom에서 resolve되는 작은 프로그램입니다. 프로젝트는 세 저장소로 출시됩니다. [napplet/web](https://github.com/napplet/web)은 web package를 담고 있으며 이번 주 조율된 출시에서 51개 하위 package version tag(`@napplet/core`, `@napplet/sdk`, `@napplet/nap`, `@napplet/shim`, `@napplet/conformance`)를 만들었습니다. [napplet/naps](https://github.com/napplet/naps)는 15개 PR을 병합한 NAPs 사양 track입니다. [kehto/web](https://github.com/kehto/web)은 41개 PR을 병합한 web runtime이며 [kehto.github.io/web/playground](https://kehto.github.io/web/playground)에 playground가 있습니다. 대응하는 사양 PR은 dskvr(sandwich.farm)가 연 [NIP-5D #2303](https://github.com/nostr-protocol/nips/pull/2303)입니다.

아키텍처의 전제는 프로토콜 계층에 정의된 trust boundary입니다. shell은 서명, key 접근, relay 쓰기 같은 위험한 작업을 중개하고, runtime은 구현과 상위 UX를 담당하며, napplet은 이동 가능하고 일회성이며 어떤 단일 host에도 포획되기 어렵게 유지됩니다. Napplet은 같은 shell 안에서 서로 통신할 수 있고, 설계상 runtime lock-in이 없습니다. 저자는 napplet을 Pablof7z의 NMP 및 Soapbox의 Tiles와 함께 논하며, 같은 문제를 푸는 병렬적 접근으로 놓습니다. Amethyst v1.12.6의 [NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)와 [NIP-5D](/ko/topics/nip-5d/) 지원 덕분에 napplet은 출시 시점에 적어도 하나의 실제 client 구현을 확보했다고 설명합니다. 역사적 배경도 있습니다. sandwich.farm의 앞선 `napp.run`(NIP-07 native-app prototype)과 Thorium fork인 `dryft` browser가 현재 설계에 영향을 준 뒤 중단되었습니다.

### Conduit가 marketplace MVP를 강화하고 공개 relay를 기본값으로 전환

[Conduit](https://github.com/Conduit-BTC/conduit-mono)는 `Conduit-BTC` 조직이 [conduit.market](https://conduit.market)에서 운영하는 3개 앱 marketplace monorepo입니다. 구매자용 Market, Merchant Portal, Store Builder로 이루어지며, 저장소 안의 `nips/`와 `specs/` 디렉터리에서 Conduit 고유의 Nostr commerce primitive를 정의합니다. 그 아래에는 [Conduit-BTC/conduit-relay](https://github.com/Conduit-BTC/conduit-relay)의 Scope-2 [khatru](https://github.com/fiatjaf/khatru) extension이 실행됩니다. 두 저장소 모두 올해 초 열렸고, 이번 주 프로젝트는 marketplace MVP를 강화하는 PR 17개를 병합했습니다.

출시 PR은 marketplace 정확성에 집중됩니다. listing 안전 상태([PR #110](https://github.com/Conduit-BTC/conduit-mono/pull/110)), merchant 쪽 제품 가격 및 배송 지역 강화([PR #115](https://github.com/Conduit-BTC/conduit-mono/pull/115))입니다. relay 쪽에서 [PR #102](https://github.com/Conduit-BTC/conduit-mono/pull/102)는 commerce capability 감지를 바로잡고, [PR #112](https://github.com/Conduit-BTC/conduit-mono/pull/112)는 제3자의 안전하지 않은 relay hint를 무시하며, [PR #128](https://github.com/Conduit-BTC/conduit-mono/pull/128)은 새 client의 기본값을 공개 Conduit relay domain으로 설정합니다. 프라이버시를 지키는 분석 기능은 [PR #109](https://github.com/Conduit-BTC/conduit-mono/pull/109)와 [PR #129](https://github.com/Conduit-BTC/conduit-mono/pull/129)에 들어왔고, `dompurify` 업데이트는 OSV advisory를 닫습니다([PR #116](https://github.com/Conduit-BTC/conduit-mono/pull/116)). 이 작업은 이번 주의 더 넓은 [NIP-99](/ko/topics/nip-99/) commerce 흐름에 놓입니다. [PR #2323](https://github.com/nostr-protocol/nips/pull/2323)은 주문 흐름, escrow, dispute를 포괄하는 NIP-99 marketplace용 on-graph checkout 계층을 제안합니다. NIP-99를 완전한 전자상거래로 확장해 온 [Gamma Markets Market Spec](https://github.com/GammaMarkets/market-spec)은 Conduit 등이 구축하는 사양 계층이 되었고, 같은 주 Shopstr는 Cashu escrow lifecycle을 출시했습니다.

### BitBlik이 Nostr 기반 P2P BLIK-Lightning 교환 프로토콜을 출시

[BitBlik](https://github.com/bit-blik/bitblik)은 이번 주 Nostr 위에 구축된 P2P BLIK ↔ Lightning 교환 프로토콜로 공개됐습니다. BLIK은 폴란드 은행이 발행하는 즉시결제 체계입니다. BitBlik coordinator는 taker가 지불한 BLIK 법정화폐와 maker가 자금을 댄 Lightning hold invoice 사이를 원자적으로 결제하며, 거래 lifecycle은 Nostr에서 진행됩니다. Flutter 앱, CLI, coordinator는 `core` package를 공유하고, 프로젝트는 `bit-blik/bitblik` GitHub monorepo와 [www.bitblik.app](https://www.bitblik.app) web build, Zapstore 앱 `app.bitblik`을 통해 배포됩니다.

프로토콜은 client-coordinator RPC에 암호화된 Nostr DM([NIP-44](/ko/topics/nip-44/))을 사용합니다. offer는 kind `38383` parameterised replaceable event로, RPC 요청은 kind `25195`로, RPC 응답은 kind `25196`으로, 상태 갱신은 kind `25197`로 게시됩니다. coordinator는 taker가 BLIK code를 제출하는 동안 Lightning hold invoice를 보류하고, BLIK 송금이 확인되면 preimage를 공개하며, invoice 결제를 maker에게 전달합니다.

---

## 태그된 릴리스

### Amber v6.2.2가 NIP-46 client metadata를 구현

[Amber](https://github.com/greenart7c3/Amber)는 greenart7c3가 관리하는 주요 Android [NIP-46](/ko/topics/nip-46/) remote signer입니다. 대응하는 사양 PR이 병합된 같은 주에 [v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2)를 출시했습니다. 이 릴리스는 요청 화면과 앱 목록에 native 앱 아이콘과 새 client-metadata field를 표시하고, 연결할 때마다 client metadata를 저장하며, connect 및 accept 시점에 native 앱 아이콘과 이름을 가져옵니다. 변경은 DocNR의 [NIP-46 PR #2381](https://github.com/nostr-protocol/nips/pull/2381)과 직접 맞물립니다. 이 PR은 connect 요청에 optional client metadata를 추가해 signer가 요청자의 의미 있는 이름과 아이콘을 표시할 수 있게 합니다. Amber v6.2.2는 event kind 30618 지원도 추가하고 Active relays 화면에서 기본 relay와 connection relay를 분리합니다.

릴리스는 signer의 보안 표면을 강화합니다. 복호화된 NIP-46 요청 및 응답 body가 더 이상 log에 기록되지 않고, encrypt 및 decrypt payload는 ciphertext로 저장되어 필요할 때만 복호화됩니다. 모든 logcat 출력은 `BuildConfig.DEBUG` 뒤로 제한되고, browser caller(null-package)는 항상 확인을 묻도록 강제됩니다. clipboard에 복사한 `nsec`, `ncryptsec`, seed word는 민감 정보로 표시되어 일정 시간 뒤 지워집니다. 명시적인 backup 및 data-extraction 제외 설정도 defense in depth로 추가됐습니다. Active relays의 중첩 scroll crash, 경쟁 상태가 있는 bunker 요청 중복 제거에서 발생하는 `LazyColumn` duplicate-key crash, 릴리스 update 확인의 `EOSE` race도 수정합니다.

### Haven이 Marmot에서 비공개 위치 공유를 출시

[Haven](https://github.com/mehmetefeumit/Haven-App)은 [Marmot](/ko/topics/marmot/) 프로토콜을 사용해 Nostr 위에서 실행되는 Android 및 iOS용 비공개 censorship-resistant 위치 공유 앱으로 이번 주 공개됐습니다. 새 프로젝트의 첫 릴리스로, 저장소는 나흘 동안 [v0.1.0](https://github.com/mehmetefeumit/Haven-App/releases/tag/v0.1.0)부터 [v0.1.4](https://github.com/mehmetefeumit/Haven-App/releases/tag/v0.1.4)까지 다섯 번 출시했습니다. Haven은 Dart와 Flutter로 만들었고 Zapstore에서 개발자 서명 앱으로 게시됩니다. Nostr용 MLS 기반 end-to-end 암호화 메시징 계층인 Marmot가 group 상태와 ciphertext 배포를 담당합니다. Haven은 이 패턴을 메시징에서 위치 공유로 확장하며, 각 group의 암호화된 상태가 해당 group이 공유하기로 동의한 위치 update를 담습니다.

### CodeDeck: Nostr를 통한 원격 agentic coding

[CodeDeck](https://github.com/JeroenOnNostr/codedeck)은 Tauri v2, React 19, Rust backend로 만든 Android 및 desktop용 multi-session agentic-coding interface로 이번 주 공개됐습니다. 사용자는 암호화된 Nostr relay를 거쳐 휴대폰에서 노트북의 [Claude Code](https://www.anthropic.com/claude-code) 세션을 제어할 수 있습니다. 프로젝트는 같은 나흘 동안 [v2026.06.17](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.06.17), [v2026.6.18](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.6.18), [v2026.6.20](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.6.20)을 출시했습니다. 전송 모델은 Nostr를 암호화된 control plane으로 사용합니다. CodeDeck 휴대폰은 노트북 옆에서 실행되는 bridge가 subscribe하는 암호화 event로 명령을 게시하고, 노트북은 같은 relay를 통해 세션 출력을 다시 게시합니다.

v2026.06.17은 `nostr-vpn` FIPS mesh를 앱의 Android VPN service로 내장합니다. 따라서 test 휴대폰에 CodeDeck만 설치해 두면 어디서든 노트북으로 앱의 개발 build를 빌드, 설치, 실행, 조작할 수 있습니다. v2026.6.18은 pairing과 mesh invite를 QR 스캔 한 번으로 합치고, v2026.6.20은 세션별 모델 선택을 추가해 각 세션이 선택한 모델로 시작하게 합니다.

### Grain v0.8.0-rc1이 완전한 Nostr client engine을 출시

0ceanSlim이 관리하는 Go relay [Grain](https://github.com/0ceanSlim/grain)은 [v0.8.0-rc1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc1)을 내놓았으며, 이제 Nostr relay인 동시에 자체 기반인 가져오기 가능한 Go client library이기도 합니다. v0.7.x가 browser에서 relay를 운영하는 데 집중했다면, v0.8 계열은 cgo나 HTTP 의존성 없는 순수 Go standalone outbox-model Nostr client engine `client/core`를 제공합니다. engine은 공유 relay pool을 관리하고 각 사용자의 relay 목록을 resolve하며, 모든 읽기와 게시를 [gossip / outbox 모델](https://mikedilger.com/gossip-model/)에 따라 routing합니다. 사용자의 note는 그 사람의 outbox relay에서 읽고, 게시한 답글은 parent 작성자의 inbox relay로 전달합니다. Grain 자체 web frontend가 이제 이 library의 reference consumer이므로, UI는 쓸 수 있는 앱인 동시에 downstream Go 프로젝트의 구현 예시입니다.

릴리스는 native [NIP-44](/ko/topics/nip-44/) 암호화(v2 및 v3), [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) relay AUTH, [NIP-65](/ko/topics/nip-65/), [NIP-17](/ko/topics/nip-17/), [NIP-51](/ko/topics/nip-51/), [NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md) relay 목록, [NIP-89](/ko/topics/nip-89/) client tag, [Blossom](/ko/topics/blossom/) 및 [NIP-96](/ko/topics/nip-96/) media 지원을 도입합니다. 이전에 relay routing을 직접 다시 구현해야 했던 downstream Go 앱은 이제 engine을 바로 `import`할 수 있습니다.

### Mostro Core v0.13.1이 Protocol v2를 후속 보완

[Mostro Core](https://github.com/MostroP2P/mostro-core)는 [지난주 Protocol v2 출시](/en/newsletters/2026-06-17-newsletter/#mostro-core-v0130-cuts-the-relay-middleman-with-protocol-v2)의 후속 릴리스로 [v0.13.1](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.1)을 내놓아, 프로토콜의 price-feed contract에 `PriceTooStale` error variant를 추가했습니다. 이번 주 daemon 쪽에서는 [PR #752](https://github.com/MostroP2P/mostro/pull/752)가 잘못된 order ID를 조용히 버리는 대신 `CantDo(NotFound)` error로 client에 드러냅니다. [PR #785](https://github.com/MostroP2P/mostro/pull/785)는 내부 protocol version이 활성 transport를 따르게 하고, [PR #778](https://github.com/MostroP2P/mostro/pull/778)은 CUP 및 MLC용 El Toque fiat-cross provider 3단계를 도입하며, [PR #782](https://github.com/MostroP2P/mostro/pull/782)는 사양에 맞춰 [NIP-33](https://github.com/nostr-protocol/nips/blob/master/33.md) info tag `protocol_versions`를 `protocol_version`으로 바꿉니다.

### Wisp v1.1.2와 Dark Wisp variant

barrydeen의 Kotlin 및 Jetpack Compose Android client [Wisp](https://github.com/barrydeen/wisp)는 [v1.1.2](https://github.com/barrydeen/wisp/releases/tag/v1.1.2)를 출시했습니다. 자신에게 보내는 wallet leg가 결정적인 transaction 순서에서 서로 구분되도록 유지하고([PR #586](https://github.com/barrydeen/wisp/pull/586)), media가 많은 note에서도 버티도록 inline video player를 지연 생성하며([PR #592](https://github.com/barrydeen/wisp/pull/592)), event-relays 집합의 `ConcurrentModificationException`을 수정하고([PR #595](https://github.com/barrydeen/wisp/pull/595)), chat bubble content의 intrinsic measurement를 수정해 `SubcomposeLayout` crash를 피합니다([PR #596](https://github.com/barrydeen/wisp/pull/596)). 릴리스는 lock 밖에서 spam 점수를 계산하는 incremental feed filter도 도입합니다. Wisp team은 이번 주 Zapstore에 Dark Wisp v1.1.0도 게시했습니다. ZEC, DASH, BCH, LTC zap target과 anon mode를 추가한 multi-currency variant입니다.

### Citrine v3.0.1

Greenart7c3의 Android local Nostr relay [Citrine](https://github.com/greenart7c3/Citrine)은 [v3.0.1](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.1)을 출시하며 한 가지 문제를 고쳤습니다. 등록되지 않은 Pokey receiver의 등록을 해제할 때 생기는 crash가 더 이상 relay를 중단시키지 않습니다.

### FIPS v0.4.0-rc2

Free Internetworking Peering System인 [FIPS](https://github.com/jmcorgan/fips)는 v0.3.x wire format 위의 packaging 검증 release candidate로 [v0.4.0-rc2](https://github.com/jmcorgan/fips/releases/tag/v0.4.0-rc2)를 tag했습니다. v0.4.0 계열은 peer reachability를 위한 Nym mixnet transport와 선택형 mDNS LAN discovery를 추가하고, 단일 node throughput을 높이고 packet당 CPU 사용량을 줄이도록 data plane을 개편합니다. operator 읽기 표면은 data-plane hot path 밖으로 옮겨 부하 아래에서도 observability가 반응하도록 했고, `fipstop` TUI를 다시 만들었으며, packet loss 중에도 중단 없이 FMP와 FSP를 rekey하도록 강화했습니다. 이는 release candidate이며 v0.4.0 stable 출시는 2026-06-21로 잠정 예정됐습니다.

### Kubo v2026.06.12와 v2026.06.20이 trust-gated 어린이 feed를 고정하고 부모 선별 YouTube를 추가

JeroenOnNostr의 Trust Extended Permissions Protocol(TEPP) 기반 Nostr-native YouTube Kids 대안 [Kubo](https://github.com/JeroenOnNostr/kubo)는 이번 주 두 릴리스를 내놓았습니다. [v2026.06.12](https://zapstore.dev/apps/com.kubo.app)(calendar versioning, 파생 `versionCode` `YYYYMMDD`)는 trust-gated 어린이 feed를 의무화합니다. 아이가 보거나 상호작용할 수 있는 모든 post, profile, reaction, repost가 이제 부모가 허용한 사람으로 범위가 제한된 TEPP를 통과합니다. 새 설치에서는 처음부터 trust gate가 켜지고 onboarding 중 아이의 circle이 초기화되므로 첫 실행부터 feed가 보호됩니다. 릴리스는 부모용 managed group chat도 도입하고 trust event를 가족의 private relay 집합으로 routing하며, trust data를 불러올 수 없으면 검증되지 않은 content를 유출하는 대신 아무것도 보여 주지 않는 fail-closed 동작을 합니다.

[v2026.06.20](https://zapstore.dev/apps/com.kubo.app)은 부모가 선별하는 YouTube channel을 추가합니다. 부모가 channel을 검색해 어린이 feed에 넣으면 아이에게 부모가 승인한 channel의 video만 보입니다. HTTP fast lane과 optimistic UI가 약 10초 걸리던 추가 경로를 대체합니다. 릴리스는 Trust Extended Permissions를 끄는 선택지도 없앱니다. 프로젝트가 의무 trust를 중심으로 만들어졌으므로 toggle은 이제 항상 켜져 있습니다. 전용 Support page를 추가하고, group chat의 `@mention`이 원시 `nostr:npub1…` 대신 클릭 가능한 `@name`으로 렌더링되게 고치며, mention 자동완성을 추가하고, trust 게시가 mirror flag가 아닌 실제 enforcement 상태를 기준으로 gate되게 수정합니다. 두 릴리스 모두 Zapstore에서 개발자 서명 Android 앱 `com.kubo.app`으로 추적됩니다.

### Pollerama v1.9.0부터 v1.9.4까지 web-of-trust 점수, 기기 내 relay engine, "알 수도 있는 사람" 목록 추가

abh3po가 만든 Form* 계열 Nostr poll 및 feed client [Pollerama](https://github.com/formstr-hq/nostr-polls)는 [pollerama.fun](https://pollerama.fun)에서 운영되며, 이번 주 Zapstore에 릴리스 다섯 개를 냈습니다. v1.9.0은 새 기기 내 relay engine을 도입합니다. 내장 local relay가 사용자가 본 모든 것을 저장하고 local cache에서 먼저 앱에 응답하므로, feed, profile, thread가 offline에서도 즉시 열리고 background에서 network와 동기화됩니다. 모든 relay traffic(읽기와 쓰기)은 main thread 밖에서 이 engine을 통과합니다. 이미 불러온 note, profile, reaction, zap은 다시 가져오지 않고 local storage에서 바로 나옵니다.

v1.9.2는 follow 목록을 sync engine과 별도로 cache해 Home 및 Notes feed와 모든 Following/Network view가 실행 또는 재개 시 간혹 비어 보이던 문제를 고칩니다. 사용자가 작성자를 follow하지 않아도 relay hint에서 참조 note를 가져와 DM 안에서 공유된 note가 안정적으로 열리게 합니다. relay connection, cache 크기, sync 상태를 보여 주고 재연결 또는 local cache 삭제 control을 제공하는 Network 설정 panel도 추가합니다. v1.9.3은 실행 crash와 Home feed loading regression을 수정합니다.

v1.9.4는 profile에 web-of-trust trust 점수를 도입합니다. 내가 follow하는 사람 중 몇 명이 이 사람도 follow하는지를 network chip으로 표시합니다. "알 수도 있는 사람" 목록은 web of trust에서 follow 추천을 가져와 내 follow 중 몇 명이 그 사람을 follow하는지에 따라 순위를 매깁니다. Network 설정은 이제 web-of-trust 크기와 마지막 계산 시점을 보여 주고 필요할 때 다시 계산하는 button을 제공합니다. Trust 점수와 추천은 web-of-trust worker가 background에서 계산하므로 앱을 막지 않습니다.

### 그 밖의 태그된 릴리스

[nogringo/nostr-mail-client v0.13.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.13.1)은 Amber, Aegis, Primal의 [NIP-55](/ko/topics/nip-55/) signer-app login을 복구하고 signer 앱에 contact 서명을 반복해서 요청하지 않게 합니다. [Cameri/nostream v3.0.0](https://github.com/Cameri/nostream/releases/tag/v3.0.0)은 web-app factory에서 `unsafe-inline`을 제거하고 script nonce를 구현합니다. [LaWallet NWC v1.0.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v1.0.0)은 공유 가능한 QR-link card 활성화, Remote Wallet 인식, Lightning Address 자동 provisioning을 갖춘 프로젝트 최초의 1.0 릴리스입니다. [Formstr Nostr Calendar v2.0.0부터 v2.0.2](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.0.2)는 PWA를 추가하고 offline replaceable event를 수정하며([PR #194](https://github.com/formstr-hq/nostr-calendar/pull/194)), signer method를 bind해 private-form 제출이 동작하게 합니다([PR #199](https://github.com/formstr-hq/nostr-calendar/pull/199)). [Spl0itable/NYM](https://github.com/Spl0itable/NYM), [codeswot/ZapBook](https://github.com/codeswot/ZapBook), [77elements/noornote](https://github.com/77elements/noornote), [mattn/nostr-relay](https://github.com/mattn/nostr-relay), [mattn/algia](https://github.com/mattn/algia), [mouse484/astraea](https://github.com/mouse484/astraea), [dergigi/boris](https://github.com/dergigi/boris), [fiatjaf/nak](https://github.com/fiatjaf/nak), [Spl0itable/nosflare](https://github.com/Spl0itable/nosflare), [nostrord/nostrord](https://github.com/nostrord/nostrord)의 소규모 릴리스가 한 주를 채웠습니다.

---

## 미출시 변경 사항

### Cordn Ad-hoc CVM: browser 기반 MLS coordinator

Sandwich.farm의 새 web 앱 [Cordn Ad-hoc](https://github.com/sandwichfarm/cordn-adhoc-cvm)은 ad-hoc [Cordn](https://github.com/Cordn-msg/cordn) group을 위해 browser tab에서 실행되는 MLS coordinator로 이번 주 공개됐습니다. 이 패턴은 독특합니다. browser tab이 [ContextVM](/ko/topics/contextvm/) Nostr coordinator process를 실행하고 coordinator pubkey를 게시하며, Nostr relay를 통해 MCP 요청을 받고, backend 없이 MLS key package, welcome, join 요청, group 메시지를 browser storage에 저장합니다. 앱은 같은 pubkey를 쓰는 coordinator 여러 개가 동시에 실행되지 않게 하고, raw Nostr event, decode된 요청, instance heartbeat를 담은 operator debug log를 제공합니다.

### SnowCait/nostter가 UX 개선 PR 19개를 병합

SnowCait의 web Nostr client [nostter](https://github.com/SnowCait/nostter)는 이번 주 릴리스 없이 PR 19개를 병합했습니다. `nostrapp.link`를 `app-manager.nostter.app`으로 교체하고([PR #2234](https://github.com/SnowCait/nostter/pull/2234)), `deck.nostter.app`을 `frame-ancestors` allowlist에 추가해([PR #2233](https://github.com/SnowCait/nostter/pull/2233)) 프로젝트 표면을 `nostter.app` domain 아래로 통합합니다. Followee의 replaceable event는 IndexedDB에 cache되고([PR #2231](https://github.com/SnowCait/nostter/pull/2231)), seen-on 및 via option을 분리해 seen-on relay 상태의 reactivity를 복구합니다([PR #2230](https://github.com/SnowCait/nostter/pull/2230)).

### Zap Cooking이 여러 프로젝트에 걸친 NIP-46 bug를 고치고 composer를 개편

Nostr 기반 recipe 공유 client [Zap Cooking](https://github.com/zapcooking/frontend)은 이번 주 PR 16개를 병합했습니다. 영향 범위가 가장 넓은 변경은 [PR #452](https://github.com/zapcooking/frontend/pull/452)입니다. Primal remote signer가 signer 자신의 pubkey로 event를 찍어 Primal을 통해 routing하는 모든 client에서 upload, zap, auth가 깨졌습니다. Zap Cooking이 이 경로를 발견해 patch했습니다. 수정은 client에 국한되지만 bug는 [NIP-46](/ko/topics/nip-46/) 전반에 존재합니다. [PR #458](https://github.com/zapcooking/frontend/pull/458)은 countdown timer, 통합 reply/comment UI, Write/Preview tab으로 composer를 다시 만듭니다. SSR 수정 세 건([PR #460](https://github.com/zapcooking/frontend/pull/460), [PR #461](https://github.com/zapcooking/frontend/pull/461), [PR #462](https://github.com/zapcooking/frontend/pull/462))과 [PR #454](https://github.com/zapcooking/frontend/pull/454)는 profile 및 recipe route를 안정화합니다. explore 화면은 drag-to-scroll 행, profile link가 있는 avatar cursor, community용 sticky-tab 수정을 얻습니다([PR #456](https://github.com/zapcooking/frontend/pull/456)).

### Shopstr가 Cashu escrow lifecycle과 storefront 도구를 도입

[NIP-99](/ko/topics/nip-99/) marketplace [Shopstr](https://github.com/shopstr-eng/shopstr)는 이번 주 중요한 PR 여러 개를 병합했습니다. [PR #512](https://github.com/shopstr-eng/shopstr/pull/512)는 marketplace용 end-to-end P2PK Cashu escrow lifecycle을 구현합니다. 이는 같은 주 [NIP-99 PR #2323](https://github.com/nostr-protocol/nips/pull/2323)의 on-graph checkout 계층 제안 및 Conduit 출시로 이어지는 더 넓은 commerce 흐름과 맞물립니다. [PR #543](https://github.com/shopstr-eng/shopstr/pull/543)은 company listing, company 상세 조회, storefront 가져오기, seller reputation 조회용 읽기 도구를 추가합니다. [PR #229](https://github.com/shopstr-eng/shopstr/pull/229)는 profile 및 shop image에 URL 붙여넣기를 지원하고, [PR #359](https://github.com/shopstr-eng/shopstr/pull/359)는 marketplace 통계 fetch에 timestamp를 포함합니다.



### divine.video mobile 및 desktop 작업

Vine archive를 복원한 rabble의 short-form loop video client [divine.video](https://github.com/divinevideo/divine-mobile)는 이번 주 playback과 편집에 집중한 PR을 병합했습니다. addressable video를 feed에서 중복 제거하고([PR #5465](https://github.com/divinevideo/divine-mobile/pull/5465)), local Nostr tag filter가 정확히 일치하도록 해 잘못된 결과를 피하며([PR #5463](https://github.com/divinevideo/divine-mobile/pull/5463)), video editor가 sticker layer를 포함한 draft를 crash 없이 복구하고([PR #5474](https://github.com/divinevideo/divine-mobile/pull/5474)), Messages badge가 follow 중이지만 아직 답하지 않은 읽지 않은 chat을 셉니다([PR #5473](https://github.com/divinevideo/divine-mobile/pull/5473)).

### Nostur가 NIP-46 client-metadata 지원과 DM 새로고침 수정 도입

Fabian의 iOS client [Nostur](https://github.com/nostur-com/nostur-ios-public)는 [지난주 1.29.0 릴리스](/en/newsletters/2026-06-17-newsletter/#nostur-1290-ships-anonymous-replies-and-remote-signer-logout)에 이어 canonical 저장소에 PR 네 개를 병합했습니다. [PR #74](https://github.com/nostur-com/nostur-ios-public/pull/74)는 NIP-46 bunker connect 요청에 client metadata를 추가합니다. DocNR이 제안하고 Amber v6.2.2가 이번 주 출시한 것과 같은 형태입니다. [PR #75](https://github.com/nostur-com/nostur-ios-public/pull/75)와 [PR #76](https://github.com/nostur-com/nostur-ios-public/pull/76)은 iPhone이 foreground로 전환된 뒤 DM 새로고침과 foreground 복구 경로를 수정합니다. [PR #78](https://github.com/nostur-com/nostur-ios-public/pull/78)은 사용자 지정 NWC 설정에 QR scan을 추가합니다.

---

## 새로 추적 및 발견한 프로젝트

### Social Agents Prototype: 사람의 승인 gate를 둔 Nostr-native AI agent 협업

[Social Agents Prototype](https://github.com/SrulyRosenblat/social_agents_prototype_nostr)은 분산 agent 간 통신을 탐구하는 Nostr 기반 실험적 AI 도구입니다. Agent는 network 전체에 atomic 질문을 broadcast하고 관련 agent만 응답하며, 주고받는 모든 메시지는 전송 전에 사람의 승인 gate를 통과합니다. 저자는 Sruly Rosenblat입니다. 이 프로젝트는 이번 주 Buzz 및 NIP-100 SNIN과 같은 agent 협업 영역에 있지만 형태는 다릅니다. Social Agents Prototype은 agent를 broadcast-and-listen 참여자로 모델링하고, 모든 메시지에 사람의 승인을 요구합니다. 같은 문제에 대한 여러 병렬 접근이 이번 주 드러났습니다.

### PRana: NIP-34 issue용 작업 목록

DocNR의 [PRana](https://github.com/DocNR/prana)는 참여를 선택한 git-over-Nostr 저장소에서 올바르게 열린 [NIP-34](/ko/topics/nip-34/) issue의 작업 목록입니다. 이 도구는 git-over-Nostr stack의 한 계층 위에 있습니다. 참여 저장소의 NIP-34 issue event를 받아 triage queue로 보여 줍니다. 출시는 [NIP-34 PR #2384](https://github.com/nostr-protocol/nips/pull/2384)가 만료 문제를 풀기 위해 maintainers tag 제거를 제안한 같은 주에 이뤄졌습니다. 이 변경은 PRana 같은 도구가 저장소 전반의 issue 권한을 resolve하는 방식에 직접 영향을 줍니다.

### routstr-chat: Nostr의 Routstr 프로토콜을 통한 local LLM 접근

Routstr team의 [routstr-chat](https://github.com/Routstr/routstr-chat)은 Routstr 프로토콜로 Nostr를 통해 어떤 LLM 모델에도 접근하는 완전한 local chat interface입니다. Routstr 프로토콜은 Nostr에 게시된 provider announcement(kind `38421`)를 통해 inference 요청을 routing하고 Cashu로 결제합니다. 자세한 내용은 [Newsletter #20](/en/newsletters/2026-04-29-newsletter/#routstrd-launches-a-local-router-for-inference-over-nostr)에서 다뤘습니다. chat client는 이 프로토콜 위의 사용자 표면입니다. routing daemon인 Routstrd가 discovery와 payment를 처리하고, chat 앱은 대화 UI를 제공합니다.

---

## 프로토콜 작업

### NIP 업데이트

이번 주 NIP 활동은 유난히 많았습니다. 두 건이 병합됐고 중요한 공개 제안이 잇달았습니다.

#### NIP-46 client metadata가 Amber와 Nostur에 구현

[지난주 Clave가 제안한](/en/newsletters/2026-06-17-newsletter/#clave-10-ships-to-the-app-store-with-push-woken-background-signing) [NIP-46 PR #2381](https://github.com/nostr-protocol/nips/pull/2381)은 이제 양쪽에 실제 구현을 갖췄습니다. [Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2)는 bunker connect 요청의 새 optional `optional_client_metadata` field를 읽어 request 화면과 app 목록에 native 앱 아이콘과 metadata를 보여 줍니다. [Nostur PR #74](https://github.com/nostur-com/nostur-ios-public/pull/74)는 client 쪽에서 이 field를 추가합니다. 세 프로젝트가 함께 bunker pairing의 신원 격차를 닫습니다. 이제 `bunker://` pairing은 앱이 이미 `nostrconnect://`를 통해 알릴 수 있었던 것과 같은 `name`, `url`, `image`를 전달합니다.

#### NIP-86 signevent와 동반 relay roles event

[staab의 PR #2389](https://github.com/nostr-protocol/nips/pull/2389)는 relay 관리 API인 [NIP-86](/ko/topics/nip-86/)에 `signevent` 작업을 병합해, relay admin이 relay를 대신해 [NIP-43](https://github.com/nostr-protocol/nips/blob/master/43.md) event를 관리할 수 있게 합니다. 동반 공개 제안인 [staab의 PR #2390](https://github.com/nostr-protocol/nips/pull/2390)은 relay가 role definition을 선언하고 admin이 member를 해당 role에 assign하거나 unassign할 수 있게 하는 relay-roles event를 정의합니다. 두 PR은 조합하도록 설계됐습니다. NIP-86은 admin에게 작업을 주고 roles event는 authorization model을 제공합니다.

#### NIP-99: marketplace용 on-graph checkout 계층

[Colabonate의 PR #2323](https://github.com/nostr-protocol/nips/pull/2323)은 이번 주 여러 작업을 가장 강하게 잇는 중심 고리입니다. 설계 feedback 요청으로 제시된 이 제안은 [NIP-99](/ko/topics/nip-99/)와 Gamma Market Spec stack의 두 가지 격차를 짚습니다. 첫째는 graph 위에 사는 checkout 흐름입니다. buy-now 이후 상태, order 생성, payment, delivery 확인을 어떤 client든 읽을 수 있는 공개 addressable Nostr event로 둡니다. 둘째는 web-of-trust 신호만으로 충분하지 않은 일부 거래, 즉 고가 물품, 처음 만난 거래 상대, 익명 marketplace, 실물 배송을 위한 escrow 및 dispute resolution입니다. NIP-99가 listing의 silo를 닫았듯 이 제안은 marketplace의 client 간 silo를 닫습니다. 같은 주에 자체 `nips/` 및 `specs/` 디렉터리를 둔 [Conduit](https://github.com/Conduit-BTC/conduit-mono)이 출시됐고, [Shopstr PR #512](https://github.com/shopstr-eng/shopstr/pull/512)는 end-to-end Cashu escrow lifecycle을 도입했으며, [BitBlik](https://github.com/bit-blik/bitblik)은 자체 escrow primitive를 갖춘 P2P BLIK ↔ Lightning을 내놓았습니다. 독립 저장소인 [Gamma Markets Market Spec](https://github.com/GammaMarkets/market-spec)도 active tracking에 들어왔습니다.

#### NIP-34: 만료 문제를 풀기 위해 maintainers tag 제거

[dhalsim의 PR #2384](https://github.com/nostr-protocol/nips/pull/2384)는 [issue #2382](https://github.com/nostr-protocol/nips/issues/2382)를 해결하기 위해 [NIP-34](/ko/topics/nip-34/) repository announcement에서 maintainers tag를 제거합니다. maintainers tag에는 정의된 만료 의미가 없어 downstream 도구가 maintainer 지정이 아직 유효한지 판단하기 어려웠습니다. 변경의 영향 범위는 넓습니다. flotilla-budabit patch(이번 주 중요한 patch 활동이 있는 유일한 추적 NIP-34 저장소), Iris team의 8개 저장소 NIP-34 배포 설정, BitBlik NIP-34 mirror, 새 Amber NIP-34 mirror, DocNR의 PRana issue-worklist 도구에 영향을 줍니다. PR의 교차 reviewer로는 DanConwayDev(ngit), vitorpamplona(Amethyst), TheAwiteb, chebizarro가 참여합니다.

#### NIP-29 group 상태(작업 중)

[dtonon의 PR #2372](https://github.com/nostr-protocol/nips/pull/2372)는 [NIP-29](/ko/topics/nip-29/)에 대한 group-states framing을 제안하며 feedback을 받기 위한 작업 중 초안으로 공유됐습니다. 이는 [#27에서 다룬 NIP-29의 진화](/en/newsletters/2026-06-17-newsletter/)를 새로운 framing으로 이어갑니다.

#### NIP-79 Stories와 NIP-76 Reels Feed(둘 다 anaskmh 제안)

같은 저자가 이번 주 두 개의 short-form media 사양을 내놓았습니다. [PR #2386](https://github.com/nostr-protocol/nips/pull/2386)은 NIP-79 Stories를 제안합니다. 24시간 뒤 만료되는 full-screen 사진, video, text slide로, 개별 slide는 kind `19`, 여러 slide 순서를 지정하는 ordered `e` tag를 담은 addressable event는 kind `34237`, 선택형 privacy-preserving seen-by receipt는 kind `15750`을 씁니다. [PR #2385](https://github.com/nostr-protocol/nips/pull/2385)는 short-form video Reels Feed용 NIP-76을 제안합니다. 둘 다 divine.video 같은 기존 video client가 출시하는 것과 병렬인 사양이지 그 구현은 아닙니다.

#### kind 1111을 kind 1 note의 답글로 사용

[zhoreeq의 PR #2358](https://github.com/nostr-protocol/nips/pull/2358)은 kind `1` note에 kind `1111` [NIP-22](/ko/topics/nip-22/) comment-thread 답글을 쓰지 말라고 권고하던 문장을 NIPs corpus에서 제거합니다([issue #2250](https://github.com/nostr-protocol/nips/issues/2250)). diff는 작지만 영향은 넓습니다. 일반 kind-1 timeline note에 NIP-22의 thread comment 형태를 쓰려는 모든 client가 이제 명시적인 근거를 얻습니다.

---

## Nostr의 여섯 번의 6월

6월의 [저장소 역사](https://github.com/nostr-protocol/nips/commits/master/)는 Nostr가 프로토콜 초기 단계에서 조합 가능한 애플리케이션 기반으로 나아간 흐름을 보여 줍니다. 2021년에는 작업 전체가 프로토콜 저장소 하나에 들어갔습니다. 2022년에는 표준화 과정과 최초의 진지한 client가 별도 프로젝트가 됐습니다. 2023년의 대중적 확산은 relay, payment, 풍부한 identity를 시급하게 만들었고, 2024년은 초기 signing 및 messaging의 지름길을 교체했습니다. 2025년에는 이 contract가 private group, git 협업, media, commerce로 이어졌으며, 2026년에는 Nostr를 agent workspace, exchange, 개발자 도구의 한 계층으로 쓰는 제품이 출시됐습니다. 서명된 event가 relay를 통해 이동할 수 있음을 입증하는 단계에서 그 사실을 구현 세부 사항으로 만드는 단계로 나아간 것입니다.

### 2021년 6월: 프로토콜 초기 단계

Nostr는 약 7개월 된 프로젝트였습니다. fiatjaf의 [최초 프로토콜 글](https://fiatjaf.com/nostr.html)과 [`fiatjaf/nostr`](https://github.com/fiatjaf/nostr) 저장소가 공개 프로젝트의 거의 전부를 담고 있었습니다. 소수 개발자가 모든 변경을 review할 수 있었고 reference 구현은 Python script였습니다. 아직 client 생태계가 아니었습니다. platform이 identity를 배정하지 않아도 사용자가 event에 서명하고 relay를 선택할 수 있다는 주장이었습니다.

전용 NIPs 저장소가 없었으므로 제안과 구현 예시는 여전히 [주 프로토콜 history](https://github.com/nostr-protocol/nostr/commits?since=2021-06-01&until=2021-07-01)를 공유했습니다. 이 단계에서는 작은 범위가 장점이었습니다. 새 구현자는 프로토콜 전체를 처음부터 끝까지 이해할 수 있었습니다. 비용도 있었습니다. 모든 새 동작이 같은 소수 집단에 의존했고, 2022년의 저장소 분리와 client 확산이 이 한계를 없애기 시작했습니다.

### 2022년 6월: NIPs 저장소의 형성

2022년 중반 Nostr에는 5월에 만들어진 별도 [`nostr-protocol/nips`](https://github.com/nostr-protocol/nips) 저장소가 필요할 만큼 제안자가 늘었습니다. 약 20개 사양이 기본 event format, follow list, 암호화 DM, relay metadata, bech32 identifier를 다뤘습니다. 문서를 원래 code 저장소 밖으로 옮기면서 프로젝트 governance가 달라졌습니다. client는 독립적으로 발전할 수 있고, 공유 wire 동작은 명시적 제안과 review를 받을 수 있었습니다.

Astral과 Anigma를 비롯한 최초의 공개 web client가 초기 형태로 운영됐고, William Casarin의 [Damus 저장소](https://github.com/damus-io/damus/commits?since=2022-06-01&until=2022-07-01)는 TestFlight 배포로 나아가고 있었습니다. 사용자층은 여전히 작고 개발자 중심이었지만, 이제 체계에는 두 개의 증폭 표면이 생겼습니다. 더 많은 사람이 사양을 유지하지 않고도 애플리케이션을 만들 수 있었고, 더 많은 사람이 원래 client를 소유하지 않고도 사양을 개선할 수 있었습니다.

### 2023년 6월: Damus 이후 채택 급증

2023년 6월이 되자 Damus의 App Store 출시 뒤 이어진 대중적 확산이 engineering 문제를 바꾸었습니다. [Primal](https://github.com/PrimalHQ)과 Iris는 프로토콜 초기 대화를 따라오지 않은 사람을 위한 제품을 만들었고, [strfry](https://github.com/hoytech/strfry)는 늘어난 traffic을 처리하는 operator에게 고성능 relay를 제공했습니다. network에는 구현 수만 더 필요한 것이 아니었습니다. 사용자, follow, event history가 늘어도 반응성을 유지하는 client와 relay가 필요했습니다.

따라서 프로토콜 작업은 routing과 가치 전송에 집중됐습니다. [NIP-65 relay 목록](https://github.com/nostr-protocol/nips/blob/master/65.md)은 새 outbox 모델에 이동 가능한 기준점을 주었고, [NIP-57 zap](https://github.com/nostr-protocol/nips/blob/master/57.md)은 event 및 identity를 Lightning receipt와 연결했습니다. 단계 변화는 실용적이었습니다. identity와 publishing이 사용자를 끌어들였지만, 더 큰 network가 과부하된 공개 feed 하나 이상으로 동작하게 한 것은 선택적 relay routing과 wallet 상호운용성이었습니다.

### 2024년 6월: signer, gift wrap, messaging upgrade

2024년 6월이 되자 signing은 개별 client 밖으로 이동하기 시작했습니다. [NIP-46 사양](https://github.com/nostr-protocol/nips/blob/master/46.md), [nsecBunker](https://github.com/kind-0/nsecbunkerd), [Amber](https://github.com/greenart7c3/Amber)는 web 및 Android 애플리케이션이 사용자의 secret key를 가져오지 않고 서명을 요청하는 방법을 제공했습니다. 이는 초기 가정을 뒤집었습니다. 이동성은 더 이상 모든 client에 nsec을 복사하는 것이 아니라, 전문 signer가 그 주위에 경계를 강제하게 하는 것이었습니다.

Messaging도 같은 이유로 바뀌었습니다. [NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)은 NIP-44 암호화와 NIP-59 gift wrapping을 결합해 NIP-04가 노출하는 metadata를 줄였고, [NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)는 client가 직접 렌더링하지 않는 event type의 handler를 추천하게 했습니다. 이 환경에서 MLS-over-Nostr 논의가 시작됐습니다. 프라이버시와 애플리케이션 discovery가 client 간 contract가 되면서, 하나의 client가 모든 기능을 담으려 하기보다 private group과 더 풍부한 event별 애플리케이션을 준비했습니다.

### 2025년 6월: Marmot, git-over-Nostr 성숙, client의 긴 꼬리

2025년 6월이 되자 MLS-over-Nostr에는 정식 [Marmot 사양](https://github.com/marmot-protocol/marmot)과 공개 구현 [White Noise](https://github.com/marmot-protocol/whitenoise)가 있었습니다. [NIP-34 git event](https://github.com/nostr-protocol/nips/blob/master/34.md), ngit, GitWorkshop도 쓸 수 있는 code-review 흐름으로 성숙했습니다. 이 프로젝트들은 같은 설계 단계에 있었습니다. relay를 coordination에 사용하면서 민감한 group 상태나 repository object는 목적에 맞는 계층으로 옮겼고, text-note client를 애플리케이션 전체로 취급하지 않았습니다.

Commerce와 media도 같은 패턴을 따랐습니다. [NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) wallet과 NIP-61 nutzap은 Cashu 상태를 이동 가능한 event에 담았고, Wavlake, Divine, [NIP-99 marketplace 구현](https://github.com/nostr-protocol/nips/blob/master/99.md)은 음악, video, listing에 전용 event kind를 사용했습니다. 애플리케이션은 identity와 relay 기반을 유지하면서도 domain별 storage, payment, moderation, presentation을 도입했고, Nostr는 겉으로 보기에 점점 덜 "소셜 network"가 되어 갔습니다.

### 2026년 6월: 출시가 많았던 달

2026년 6월에는 Nostr를 더 큰 제품 안의 한 구성 요소로 다루는 출시가 이어졌습니다. [Buzz](https://github.com/block/buzz)는 사람과 agent를 위한 self-hosted workspace-as-relay 패턴을 열었고, [Napplets](https://napplet.run)는 Nostr와 Blossom 위 조합형 앱의 trust boundary를 정의했으며, [Conduit](https://conduit.market)은 marketplace 애플리케이션과 자체 프로토콜 문서를 나란히 두었습니다. 이 프로젝트들은 더 이상 서명된 event가 협업을 지원할 수 있는지 묻지 않았습니다. 어떤 작업을 event에 둘지, 어떤 작업을 blob이나 local 상태에 둘지, host가 어떤 권한을 유지할지를 결정했습니다.

[BitBlik](https://www.bitblik.app)은 Nostr를 P2P 법정화폐-Lightning 교환에 사용했고, [CodeDeck](https://github.com/JeroenOnNostr/codedeck)은 암호화 relay를 통해 coding 세션을 전달했으며, [Haven](https://github.com/mehmetefeumit/Haven-App)은 conventional messenger 밖에 Marmot를 적용했습니다. [2021년 prototype 저장소](https://github.com/nostr-protocol/nostr)와의 거리는 프로젝트 수가 늘어난 것만으로 설명되지 않습니다. abstraction이 바뀌었습니다. team은 이동 가능한 identity, relay discovery, 암호화, payment를 기존 구성 요소로 삼아 시작하고 그 위의 애플리케이션별 경계를 설계하는 데 힘을 쓸 수 있게 됐습니다.
