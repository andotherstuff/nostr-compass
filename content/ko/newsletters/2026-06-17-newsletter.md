---
title: 'Nostr Compass #27'
date: 2026-06-17
publishDate: 2026-06-17
translationOf: /en/newsletters/2026-06-17-newsletter.md
translationDate: 2026-08-26
draft: false
type: newsletters
---

이번 주에는 signer 작업, P2P 거래 프로토콜, 주요 클라이언트 릴리스가 쏟아졌습니다. [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)은 170개가 넘는 PR을 묶어 [NIP-60](/ko/topics/nip-60/) Cashu 지갑, [NIP-61](/ko/topics/nip-61/) nutzap, [NIP-82](https://github.com/nostr-protocol/nips/blob/master/82.md) 소프트웨어·앱 피드, [NIP-F4](/ko/topics/nip-f4/) 팟캐스트 지원, CLINK on-chain zap 검증, KMP 1·2단계 iOS 마이그레이션, Tor 자체 복구 드라이버를 추가합니다. [Clave v1.0.0(build 102)](https://github.com/DocNR/clave/releases/tag/v1.0.0)은 App Store에 제출되어, push로 깨어나는 백그라운드 서명과 들어오는 서명 검증을 iOS에 제공합니다. [Mostro Core v0.13.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0)은 relay 기반 주문 통신을 [NIP-44](/ko/topics/nip-44/) gift wrap 다이렉트 메시지로 교체한 Protocol v2를 출시했고, [Mostro v0.17.5](https://github.com/MostroP2P/mostro/releases/tag/v0.17.5)는 운영자 측 악용 방지 보증금을 선택 사항이자 설정 가능 항목으로 바꿨습니다. [Signet v1.11.0](https://github.com/Letdown2491/signet/releases/tag/v1.11.0)은 공개 정보만으로 누구나 kill-switch 명령을 위조할 수 있었던 [NIP-17](/ko/topics/nip-17/)(gift wrap 비공개 DM) 관리 명령 서명 우회를 패치합니다. [Chama](https://github.com/jesuspirate/chama)는 엿새 동안 일곱 번의 escrow 릴리스를 내며 거래방을 빽빽한 제어판에서 역할별 대화형 화면으로 바꿨습니다. signer 쪽에서는 [Amber v6.2.1](https://github.com/greenart7c3/Amber/releases/tag/v6.2.1), Clave(build [100](https://github.com/DocNR/clave/releases/tag/v0.2.0-build100), [101](https://github.com/DocNR/clave/releases/tag/v0.2.0-build101), [102](https://github.com/DocNR/clave/releases/tag/v1.0.0)), [Nostur 1.29.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.29.0-desktop)이 모두 이번 주 병합된 새 [NIP-46](/ko/topics/nip-46/) `logout` 메서드([PR #2373](https://github.com/nostr-protocol/nips/pull/2373))를 구현했습니다. [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1)과 Amethyst는 Nostr 키를 위한 공통 Lightning 인터페이스 제안인 CLINK noffer 지원을 모두 출시합니다. [NIP-29](/ko/topics/nip-29/) relay 그룹에는 banner tag, 초대 코드, 메시지 고정, [NIP-17](/ko/topics/nip-17/) DM을 통한 그룹 신고, 역할 기반 접근 제어를 다루는 다섯 제안이 열렸습니다.

## 주요 소식

### Amethyst v1.12.0, Cashu 지갑·nutzap·CLINK 드라이버·Tor 자체 복구 출시

[Amethyst](https://github.com/vitorpamplona/amethyst)는 Vitor Pamplona가 만드는 대표적인 Android Nostr 클라이언트입니다. [v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)은 Newsletter #25에서 미출시 작업으로 다룬 93개 PR([NIP-32](/ko/topics/nip-32/) 해시태그 라벨링, NIP-F4 팟캐스트 화면, 음악 트랙, 임시 signer, NIP-05 필터가 있는 onchain zap)과 Newsletter #26의 작업(이어진 [NIP-F4](/ko/topics/nip-f4/), Tor watchdog 기반)에 이번 주의 상당한 새 작업을 더해 묶었습니다. 새 작업은 Cashu·nutzap 화면, CLINK on-chain zap 드라이버, Tor 자체 복구 묶음, KMP iOS 마이그레이션에 집중합니다.

[NIP-60](/ko/topics/nip-60/) Cashu 지갑 지원과 [NIP-61](/ko/topics/nip-61/) nutzap 렌더링은 [PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075)에 들어왔습니다. mint별 잔액 보기([PR #3115](https://github.com/vitorpamplona/amethyst/pull/3115))와 Lightning 주소, on-chain zap, Cashu mint, NWC를 하나의 프로필 결제 화면([PR #3185](https://github.com/vitorpamplona/amethyst/pull/3185))에 모은 통합 결제 카드 UI([PR #3191](https://github.com/vitorpamplona/amethyst/pull/3191))도 함께합니다. on-chain zap 검증용 CLINK 드라이버는 [PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039), [PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177), [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182)에 담겼습니다. CLINK는 Common Lightning Interface for Nostr Keys로, 이번 주 [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1)도 같은 noffer 인터페이스를 출시합니다. Amethyst는 검증 상태 머신, 재검증 드라이버, 최소 on-chain zap 금액도 추가합니다([PR #3030](https://github.com/vitorpamplona/amethyst/pull/3030)). [PR #3201](https://github.com/vitorpamplona/amethyst/pull/3201)은 [NIP-17](/ko/topics/nip-17/)에 따라 p-tag 사용자를 대상으로 한 kind 1 답글을 gift wrap하는 비공개 노트를 도입해, 작성기가 대상 지정에 따라 공개 노트나 sealed 그룹 답글을 만듭니다.

Tor 신뢰성 작업은 완전한 자체 복구 stack으로 들어왔습니다. [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053)은 Arti를 v2.3.0으로 올리고 watchdog과 통합 테스트를 추가하고, [PR #3223](https://github.com/vitorpamplona/amethyst/pull/3223)은 Tor가 준비될 때까지 Tor 경유 relay 연결을 막으며, [PR #3224](https://github.com/vitorpamplona/amethyst/pull/3224)는 적대적 네트워크가 loop를 멈추게 하지 못하도록 Arti bootstrap을 60초 timeout으로 제한합니다. [PR #3231](https://github.com/vitorpamplona/amethyst/pull/3231)은 Tor가 Active 상태지만 모든 circuit이 죽었을 때 자체 복구합니다. 그 결과 네트워크 변경과 절전·재개 주기 뒤에도 수동 개입 없이 복구되는 Tor stack이 되었습니다. KMP iOS 마이그레이션 1단계와 2단계는 [PR #3047](https://github.com/vitorpamplona/amethyst/pull/3047)과 [PR #3050](https://github.com/vitorpamplona/amethyst/pull/3050)에 담겨, `quartz`와 `commons` 모듈의 iOS CI를 열고 iOS Amethyst 빌드의 기반을 놓습니다.

### Mostro Core v0.13.0, Protocol v2로 relay 중개 제거

[Mostro](https://github.com/MostroP2P/mostro)는 Nostr를 주문장과 거래 통신 계층으로 쓰고 Lightning으로 결제하는 P2P Bitcoin 거래소입니다. wire protocol을 정의하는 Rust 라이브러리 [mostro-core v0.13.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0)은 relay 경유 메시징 모델을 changelog에서 Protocol v2라 부르는 kind 14 이벤트 기반 NIP-44 다이렉트 전송으로 교체합니다. 거래별 action은 이제 [NIP-44](/ko/topics/nip-44/)에 따라 wrap되고 참가자가 주문 생성 때 만든 거래별 키에 묶인 kind 14 메시지로 이동합니다. 거래 대화가 공개 addressable 이벤트를 왕복하지 않습니다.

이전 모델에서는 전체 거래 대화가 이벤트를 나르는 모든 relay에 노출되었습니다. 다이렉트 kind 14 전송은 주문 설정, 분쟁 절차, 정산 메타데이터를 양측과 Mostro daemon 사이에 두고, relay에는 암호화 envelope만 보입니다. 전송 변경과 함께 v0.13.0은 v2 신원 증명을 거래 키에도 묶어([commit log](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0)) 새 프로토콜을 겨냥한 replay 위험 한 부류를 닫습니다. daemon 쪽 [Mostro v0.17.5](https://github.com/MostroP2P/mostro/releases/tag/v0.17.5)는 악용 방지 보증금을 선택 사항이자 운영자가 설정할 수 있는 항목으로 바꿨습니다. 특정 거래를 시작하기 전에 양측이 소액 보증금을 잠가야 할 수 있으며, 정상 완료 시 돌려받고 지연, 불참, 고의 방해 때 몰수됩니다. 보증금은 네트워크 전체에 강제되지 않고 node 운영자 수준에서 켜집니다. Mostro는 비수탁형을 유지하고 각 운영자가 시장 마찰과 악용 방지 사이의 절충을 선택합니다. 클라이언트 쪽 [Mostro Mobile v1.2.8](https://github.com/MostroP2P/mobile/releases/tag/v1.2.8)은 고정 기본 relay를 대신하는 bootstrap relay 탐색([PR #610](https://github.com/MostroP2P/mobile/pull/610)), 보증금 도입 5단계인 주문 생성 시 maker 악용 방지 보증금([PR #608](https://github.com/MostroP2P/mobile/pull/608)), 맥락과 함께 알림 기록에 보존되는 주문 취소([PR #602](https://github.com/MostroP2P/mobile/pull/602))를 비롯한 17개 기능으로 새 경로를 지원합니다. 이틀 뒤 나온 [v1.2.9](https://github.com/MostroP2P/mobile/releases/tag/v1.2.9)는 node info 이벤트의 악용 방지 보증금 정책을 표시해, 사용자가 주문을 열기 전에 Mostro instance의 보증금 규칙을 볼 수 있게 합니다([PR #617](https://github.com/MostroP2P/mobile/pull/617)).

### Signet v1.11.0, NIP-17 관리 명령 서명 우회 패치

[Signet](https://github.com/Letdown2491/signet)은 관리자가 host machine에 손대지 않고 Nostr로 signer를 panic, revive하거나 상태를 확인할 수 있는 kill-switch 기능을 갖춘 원격 bunker signer입니다. [v1.11.0](https://github.com/Letdown2491/signet/releases/tag/v1.11.0)은 [NIP-17](/ko/topics/nip-17/) gift wrap 관리 명령 경로가 서명된 seal을 검증하지 않고 서명되지 않은 내부 rumor가 주장하는 작성자만 확인하던 보안 버그를 수정합니다. [NIP-44](/ko/topics/nip-44/) conversation key는 대칭형이므로 signer pubkey, admin npub, admin relay 같은 공개 정보만 가진 공격자도 외부에서 gift wrap을 위조하고 `panic`, `resumeall`, `alive`를 비롯한 모든 kill-switch 명령을 실행할 수 있었습니다. 수정본은 seal에 `verifyEvent`를 호출하고 rumor 작성자를 seal 서명에 묶어, 서명되지 않은 위조를 입구에서 거부합니다. 사양과 패치 전 코드 경로가 공격자에게 분명한 재현 절차를 제공하므로 Signet 운영자는 신속히 업그레이드해야 합니다.

### Chama v3.2.0~v3.5.0, 거래방을 다시 그리고 자금 경로 강화

[Chama](https://github.com/jesuspirate/chama)는 Fedimint ecash와 2-of-3 Shamir secret sharing을 결합해 서버 없는 거래 정산을 제공하는 Nostr 네이티브 P2P escrow 클라이언트입니다. Newsletter #26은 독립형 앱이 되고 판매자별 storefront를 추가한 v2.0.0~v3.1.0을 다뤘습니다. 이번 주의 후속 릴리스 여섯 건은 [v3.2.0](https://github.com/jesuspirate/chama/releases/tag/v3.2.0)에서 시작해 6월 15일 [v3.5.0](https://github.com/jesuspirate/chama/releases/tag/v3.5.0)까지 이어졌습니다. 거래방 UI를 역할마다 하나의 질문, 즉 ‘지금 무엇을 해야 하는가’를 중심으로 다시 그리고 부분 실패에 대비해 자금 경로를 강화합니다. [v3.2.0](https://github.com/jesuspirate/chama/releases/tag/v3.2.0)은 구매자, 판매자, 중재자에게 각각 색으로 구분된 action prompt를 제공해 모든 거래 상태에서 각 역할의 다음 행동을 보여 줍니다. [v3.3.0](https://github.com/jesuspirate/chama/releases/tag/v3.3.0)은 거래 engine의 합의 규칙 두 가지를 조이고 효과를 내려면 클라이언트가 함께 채택하도록 요구했습니다. [v3.3.1](https://github.com/jesuspirate/chama/releases/tag/v3.3.1)은 가격과 결제 수단을 거래자 커뮤니티의 통화에 맞췄습니다. [v3.4.0](https://github.com/jesuspirate/chama/releases/tag/v3.4.0)은 일시적 장애, race, 닫힌 tab 때문에 사용자 sats가 조용히 사라지지 않도록 자금 경로에 다섯 가지 강화 수정을 더했습니다. [v3.5.0](https://github.com/jesuspirate/chama/releases/tag/v3.5.0)은 거래를 은밀히 기울일 수 있는 역할인 중재자에 클라이언트 측 guardrail 두 가지를 추가했습니다.

### Clave 1.0, push로 깨어나는 백그라운드 서명과 함께 App Store로

[Clave](https://github.com/DocNR/clave)는 사용자의 Nostr private key를 iPhone Keychain에 보관하는 iOS [NIP-46](/ko/topics/nip-46/) 원격 signer입니다. 앱은 end-to-end 암호화 채널로 서명을 요청하며 키 자체는 받지 않습니다. [v1.0.0 build 102](https://github.com/DocNR/clave/releases/tag/v1.0.0)은 8개월간의 TestFlight beta 뒤 1.0 이정표에 도달해 이번 주 App Store에 제출되었습니다. 릴리스는 push로 깨어나는 백그라운드 서명을 제공합니다. 앱이 닫혀 있어도 Clave가 요청을 복호화하고 권한을 확인한 뒤 서명하고 응답할 수 있어, signer 응답성을 막던 iOS foreground 요구가 사라집니다. 들어오는 서명은 모든 서명 Nostr 이벤트의 hash 방식을 정하는 기본 사양인 [NIP-01](/ko/topics/nip-01/)의 canonical 이벤트 serialization 형식에 BIP-340 Schnorr를 적용하고 replay freshness guard를 더해 검증합니다. 악성 앱이 다시 서명한 이벤트를 응답 채널로 몰래 넣을 수 없습니다.

릴리스는 kind 범위 권한 모델과 세 단계 민감도를 갖춘 최신 [NIP-44](/ko/topics/nip-44/) 암호화 계층도 도입하고, 신뢰도가 낮은 ‘매번 묻기’ 요청이 사용자가 승인하기 전에 오류를 반환하던 edge case를 수정하며, 앱 하나의 pairing이 여러 신원을 거칠 수 있는 다중 계정 pairing을 추가합니다. bunker pairing은 Clave가 [PR #2381](https://github.com/nostr-protocol/nips/pull/2381)에서 제안한 [NIP-46](/ko/topics/nip-46/) connect metadata 확장을 통해 실제 앱 신원을 표시합니다. 깔끔한 연결 종료는 [PR #2373](https://github.com/nostr-protocol/nips/pull/2373)에서 병합된 새 [NIP-46](/ko/topics/nip-46/) `logout` 메서드를 사용하므로, pairing된 앱은 수동 unpair 없이 session을 끝낼 수 있습니다. 이벤트 kind별 override가 있는 앱별 신뢰 수준(Full, Medium, Low), 모든 서명의 활동 log, 사용자가 직접 마련하는 push proxy가 기능을 완성합니다. proxy stack은 MIT license이며 클라이언트별 상호운용 matrix는 [`docs/nip46-compatibility.md`](https://github.com/DocNR/clave/blob/main/docs/nip46-compatibility.md)에서 추적합니다.

## 릴리스

### Amber v6.2.1, NIP-46 logout 추가와 signer 배터리 소모 감소

[Amber](https://github.com/greenart7c3/Amber)는 대표적인 Android Nostr signer입니다. [v6.2.1](https://github.com/greenart7c3/Amber/releases/tag/v6.2.1)은 relay 재연결과 websocket ping의 배터리 소모를 줄이고, 죽은 relay를 subscription pool에서 제거하며, relay 알림을 갱신할 때 기기를 깨우지 않습니다. 릴리스는 클라이언트가 원격 signer session을 깔끔하게 끝낼 수 있도록 [NIP-46](/ko/topics/nip-46/) `logout` 메서드 지원도 추가합니다. 같은 메서드가 이번 주 [PR #2373](https://github.com/nostr-protocol/nips/pull/2373)으로 사양에 병합되었습니다. event kind 39701(공개 웹 bookmark) parsing도 추가되어 사용자가 Amber에서 bookmark 이벤트에 바로 서명할 수 있습니다. 설정은 그룹화된 Material 3 카드와 구분되는 아이콘으로 다시 만들었고, 애플리케이션 권한 화면의 탐색 충돌을 수정했으며, database를 atomic하게 만들어 계정별 database 연결 leak을 닫았습니다.

### Nostur 1.29.0, 익명 답글과 원격 signer logout 출시

[Nostur](https://github.com/nostur-com/nostur-ios-public)는 Fabian이 만드는 iOS Nostr 클라이언트입니다. [1.29.0-desktop](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.29.0-desktop)은 zap receipt에 답하고 익명 답글을 보내는 기능을 추가합니다. signer 쪽에서는 원격 bunker 연결 절차를 개선하고, 사용자가 계정에서 logout할 때 원격 signer에 [NIP-46](/ko/topics/nip-46/) `logout`을 보내며, 원격 signer 연결 실패 때 spinner가 멈추던 문제를 수정합니다. 앱 relay와 DM relay의 충돌로 생긴 DM loading 문제, 답글로 이동했다 돌아올 때 게시물이 중복되는 문제도 고쳤고 알림 행에 media thumbnail을 표시합니다.

### Citrine v3.0.0, Negentropy·NIP-42 AUTH·onion relay 필터링 출시

[Citrine](https://github.com/greenart7c3/Citrine)은 Android 로컬 relay aggregator입니다. major version이 오른 [v3.0.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0)은 집합 조정 sync를 위한 [NIP-77](/ko/topics/nip-77/) Negentropy 지원, relay aggregator의 외부 signer와 [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH 지원, aggregator fetch에서 [NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) mute list 준수를 추가합니다. aggregator는 작성자당 fetch를 relay 세 곳으로 제한하고 source 및 indexer relay를 설정할 수 있으며, restart와 네트워크 변경 뒤에도 cache된 follow, mute, metadata를 재사용하고, 제한되거나 통제된 네트워크에서는 멈추며, outbound proxy가 꺼졌을 때 onion relay URL을 걸러냅니다. 보호된 이벤트를 포함한 repost는 거부하고, mute list는 기본적으로 오래된 데이터 삭제 대상에서 보존합니다.

### FIPS v0.4.0-rc1, Nym mixnet 전송과 mDNS LAN 탐색 추가

[FIPS](https://github.com/jmcorgan/fips)는 FIPS mesh sync 프로토콜 구현입니다. [v0.4.0-rc1](https://github.com/jmcorgan/fips/releases/tag/v0.4.0-rc1)은 v0.3.0과 wire 호환되므로 버전이 섞인 mesh도 상호운용되며 일제 업그레이드가 필요 없습니다. 릴리스는 node가 서로를 찾고 연결하는 두 가지 새 방법을 추가합니다. 단일 container demo와 mixnet-relay 예시를 갖춘 Nym mixnet outbound 전송, 그리고 선택 사항인 로컬 link의 mDNS/DNS-SD 탐색입니다. counter만 제공하는 새 `show_metrics` 질의는 hot path 비용 없이 Prometheus scraper를 쓸 수 있게 하며, FMP와 FSP rekey는 양방향 packet loss에도 중단 없이 작동하도록 강화되었습니다.

### Calendar by Formstr v1.6.1·v1.6.2, 이벤트별 알림 추가

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar)는 [NIP-52](/ko/topics/nip-52/) 캘린더 클라이언트입니다. [v1.6.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.1)은 이벤트별 알림 설정([PR #109](https://github.com/formstr-hq/nostr-calendar/pull/109))을 추가해, 사용자가 각 캘린더 이벤트의 알림을 개별적으로 켜거나 끌 수 있습니다. [v1.6.2](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.2)는 Amber login을 수정해([PR #185](https://github.com/formstr-hq/nostr-calendar/pull/185)) Amber 6.2.x의 새 [NIP-46](/ko/topics/nip-46/) handshake가 끝까지 작동하게 합니다.

### Bitchat v1.5.2·v1.5.3, Nostr·BLE 전송 강화

[Bitchat](https://github.com/permissionlesstech/bitchat)은 Bluetooth와 Nostr를 쓰는 mesh 채팅 클라이언트입니다. [v1.5.2](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.2)는 flood를 막기 위해 iOS peer 알림을 rate limit하고([PR #972](https://github.com/permissionlesstech/bitchat/pull/972)), Nostr 검증과 BLE announce 확인을 강화해([PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012)) relay 측 Nostr ingest 경로가 잘못된 메시지를 로컬 mesh handler에 도달하기 전에 거부합니다. [v1.5.3](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.3)은 `NostrRelayManager`와 `NetworkActivationService` 사이의 재귀적 `dispatch_once` 때문에 발생한 시작 충돌을 고친 hotfix입니다([PR #1343](https://github.com/permissionlesstech/bitchat/pull/1343)).

### Keep v1.0.5, signer 정책을 감사된 Rust core로 이동

[Keep](https://github.com/privkeyio/keep-android)은 [keep](https://github.com/privkeyio/keep) Rust core를 감싸는 Android signer입니다. [v1.0.5](https://github.com/privkeyio/keep-android/releases/tag/v1.0.5)는 [keep v0.4.8](https://github.com/privkeyio/keep/releases/tag/v0.4.8)에 고정하고, 부하 아래 handshake가 첫 이벤트를 잃지 않도록 bunker 초기화 race를 수정하며([PR #296](https://github.com/privkeyio/keep-android/pull/296)), bunker `onConnect` callback으로 Authorized Clients 화면을 채우고([PR #291](https://github.com/privkeyio/keep-android/pull/291)), kill switch의 단일 기준을 keep-mobile에 통합합니다([PR #284](https://github.com/privkeyio/keep-android/pull/284)). upstream Rust core는 6월 13일 [v0.4.9](https://github.com/privkeyio/keep/releases/tag/v0.4.9)를 내놓았습니다. Kotlin에서 중복 구현했던 [NIP-55](/ko/topics/nip-55/)와 [NIP-46](/ko/topics/nip-46/) signer 정책(권한 결정, 민감 kind 기간 제한, 만료, keyed-HMAC 변조 감지 audit chain, 호출자 TOFU, 영속 signing rate limiter)을 감사된 Rust core로 옮기고 [NIP-44](/ko/topics/nip-44/) v3 cipher 구현을 더했습니다. 이 core는 다음 keep-mobile 업데이트에 포함됩니다.

### ants v0.4.5, 기사 portal link 추가와 portal 목록에 Habla 복원

[ants](https://github.com/dergigi/ants)는 dergigi의 Nostr 검색·reader 도구입니다. [v0.4.5](https://github.com/dergigi/ants/releases/tag/v0.4.5)는 장문 게시물용 기사 카드 action을 추가합니다. 기사 portal link, 기사별 `naddr` 공유, `nevent` 복사, raw JSON 접근이 포함됩니다. 기사 portal 목록은 Habla를 복원하고, 사라진 목적지를 교체하며, imwald portal을 제거해 새로 정리했습니다. 릴리스는 기사 안 anchor navigation을 보존하면서 footnote 렌더링도 복원하고, login 복구 중 프로필을 가져오기 전에 relay 연결을 기다려 header avatar가 제대로 나타나게 합니다.

### Morganite v0.0.3, 필요할 때 Tor를 켜는 Android 로컬 Blossom cache 출시

[Morganite](https://github.com/greenart7c3/Morganite)는 Amber와 Citrine의 개발자 greenart7c3가 만든 새 Android 로컬 Blossom cache입니다. cache는 [BUD-08](https://github.com/hzrd149/blossom/blob/master/buds/08.md) 로컬 mirror로 작동하고 1GB를 넘으면 사용 빈도가 가장 낮은 blob부터 제거합니다. [v0.0.3](https://github.com/greenart7c3/Morganite/releases/tag/v0.0.3)은 필요할 때 Tor를 시작하고 유휴 상태가 되면 중지해 배터리를 아끼며, 작성자 조회 뒤 Nostr relay 연결을 끊어 백그라운드 소모를 막고, 필터 없는 logcat stream과 누수된 HTTP client로 인한 배터리 소모를 수정하며, 교체된 `OkHttp` client를 main thread 밖에서 해제합니다. 릴리스는 Blossom server 목록을 조회하기 전에 사용자 inbox relay를 가져와 blob 탐색이 outbox 모델을 따르게 하고, 로컬 cache에 없을 때 `HEAD` 요청으로 blob을 내려받아 cache warmup을 실제 클라이언트 수요에 맞춥니다.

### Coracle 0.6.34·0.6.35, NIP-46 login·오래된 피드·답글 toggle 수정

[Coracle](https://github.com/coracle-social/coracle)은 hodlbod가 만드는 Nostr 웹 클라이언트입니다. [0.6.34](https://github.com/coracle-social/coracle/releases/tag/0.6.34)는 [NIP-46](/ko/topics/nip-46/) login, 보기를 전환한 뒤 home timeline이 새로 고쳐지지 않던 오래된 feed 상태, 켰을 때 모든 항목을 걸러내던 답글 toggle을 수정합니다. feed 및 목록 보기도 다시 만들고, toast safe-area inset 문제를 수정하며, image loading을 개선합니다. [0.6.35](https://github.com/coracle-social/coracle/releases/tag/0.6.35)는 답글을 끄면 repost도 숨겨지던 문제를 고친 작은 후속 릴리스로, repost filter가 답글 filter를 과도하게 적용하지 않습니다.

### Zeus v13.1.0-rc1, CLINK noffer와 queue 없는 NWC 출시

[Zeus](https://github.com/ZeusLN/zeus)는 wallet connect와 noffer 결제를 위한 Nostr 기능을 갖춘 self-custody Bitcoin·Lightning 지갑입니다. [v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1)은 Primal과 협력해 iOS에 queue 없는 [NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md) Nostr Wallet Connect 결제를 추가해, 결제된 NWC invoice가 더는 백그라운드 queue에서 기다리지 않게 합니다. Zeus Pay가 모든 계정에 CLINK noffer를 생성하는 CLINK noffer 결제도 출시해, 송신자가 Nostr 키만으로 어떤 Zeus 사용자에게든 결제할 수 있습니다. Zeus Pay에는 Nostr Zap 선택 해제도 추가되어, 수신자가 NWC를 끄지 않고 kind 9735 receipt 경로만 끌 수 있습니다.

### Alby Extension v3.14.3, NIP-07 signer가 쓰는 noble/scure 암호 stack 마이그레이션

[Alby Extension](https://github.com/getAlby/lightning-browser-extension)은 Lightning 기능과 함께 [NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) 서명과 Nostr Wallet Connect를 제공하는 browser extension입니다. [v3.14.3](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.3)은 `@noble/curves`, `@noble/hashes`, `@noble/ciphers`, `@noble/secp256k1`, `@scure/bip32`, `@scure/base` stack을 v2 및 v3 major로 마이그레이션합니다. 이들은 [NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) signer 경로가 이벤트 서명과 [NIP-44](/ko/topics/nip-44/) 암호화에 의존하는 암호 라이브러리이므로, major version 변경은 Nostr 웹 클라이언트가 요청한 모든 서명 이벤트에서 extension이 만드는 wire format에 영향을 줍니다.

### Mostro Mobile v1.2.8·v1.2.9, Protocol v2 지원과 보증금 정책 표시

[Mostro Mobile](https://github.com/MostroP2P/mobile)은 Mostro의 mobile 클라이언트입니다. [v1.2.8](https://github.com/MostroP2P/mobile/releases/tag/v1.2.8)은 위 주요 소식에서 다룬 [mostro-core v0.13.0 Protocol v2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0)의 클라이언트 측 지원을 도입하고 총 17개 기능을 추가합니다. [PR #608](https://github.com/MostroP2P/mobile/pull/608)의 maker 악용 방지 보증금, [PR #610](https://github.com/MostroP2P/mobile/pull/610)의 bootstrap relay 탐색, [PR #602](https://github.com/MostroP2P/mobile/pull/602)의 알림 기록에 보존되는 주문 취소, [PR #605](https://github.com/MostroP2P/mobile/pull/605)의 주문 생성 화면 fiat 금액 한도가 포함됩니다. [v1.2.9](https://github.com/MostroP2P/mobile/releases/tag/v1.2.9)는 node info 이벤트의 악용 방지 보증금 정책을 표시해([PR #617](https://github.com/MostroP2P/mobile/pull/617)), 사용자가 주문을 열기 전에 Mostro instance의 보증금 규칙을 볼 수 있게 합니다.

### ZapBook build 4~27, 다중 계정·Marmot 키 게시·circle 재초대 출시

[ZapBook](https://github.com/codeswot/ZapBook)은 codeswot가 iOS와 Android용으로 만드는 Nostr 네이티브 소셜 독서 앱입니다. 1~100명이 진척을 공유하고 격려로 서로 sats를 zap하는 독서 circle을 중심으로 구성됩니다. 프로젝트는 6월 11일 [build 4](https://github.com/codeswot/ZapBook/releases/tag/v1.0.0-build.4)부터 6월 15일 [build 27](https://github.com/codeswot/ZapBook/releases/tag/v1.0.0-build.27)까지 tag가 붙은 build 17건과 병합 PR 7건을 출시했습니다. 원활한 계정 전환이 있는 다중 계정 지원은 [PR #25](https://github.com/codeswot/ZapBook/pull/25)에 들어와, 사용자가 여러 Nostr 신원을 앱에 보관하고 session을 오갈 수 있습니다. 초기 [Marmot](/ko/topics/marmot/) key package 게시(kind 443)는 onboarding 완료 때 자동으로 실행되며([PR #20](https://github.com/codeswot/ZapBook/pull/20)), 독서 circle에서 초대 전용 그룹 메시징을 쓰기 위한 전제 조건입니다. circle에서 제거된 멤버 처리는 이제 새 재초대를 올바르게 처리해([PR #24](https://github.com/codeswot/ZapBook/pull/24)), 제거 뒤 다시 추가한 멤버가 새 초대를 받지 못하던 버그 한 부류를 닫습니다. 릴리스 계열은 reader 안 semantic 검색을 위해 ONNX embedding inference를 백그라운드 isolate로 옮기고([PR #19](https://github.com/codeswot/ZapBook/pull/19)), 환경별 설정용 `APP_ID_SUFFIX`와 NWC service를 통합해 하나의 hub가 여러 ZapBook build를 지원하게 합니다.

### Alby Hub v1.23.0, 삭제된 앱의 NIP-47 게시 수정과 Bitrefill의 NWC 전환

[Alby Hub](https://github.com/getAlby/hub)는 self-hosted Lightning·Nostr hub입니다. [v1.23.0](https://github.com/getAlby/hub/releases/tag/v1.23.0)의 Nostr 외 기능은 규모가 크지만(Just-in-Time channel, debit card 충전용 Cards 페이지, 실험적 Ark 결제 backend, stories home 페이지) Compass 범위 밖입니다. [NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md) 쪽에서는 삭제된 앱의 NIP-47 info 게시 재시도를 중단해 제거된 연결이 kind 13194 info 이벤트를 계속 재게시하지 않게 하고([PR #2391](https://github.com/getAlby/hub/pull/2391)), Bitrefill custom app 항목을 없애 표준 NWC 연결로 바꿉니다([PR #2420](https://github.com/getAlby/hub/pull/2420)). app store 앱의 readonly option([PR #2415](https://github.com/getAlby/hub/pull/2415))은 hub 안 store를 통해 게시된 NWC 앱의 권한 범위를 좁힙니다.

### 함께 출시된 항목

이번 주 Nostr 관련 내용은 있지만 릴리스별 내용이 적은 소규모 릴리스는 다음과 같습니다. [Nostria v3.1.48~v3.1.50](https://github.com/nostria-app/nostria/releases)은 Web Bookmarks 출시를 이어가며 v3.1.50에서 알림 신뢰성과 event thread database 최적화를 추가했습니다. [Deepmarks v0.7.0~v0.7.5](https://github.com/ostermayer/deepmarks-public/releases)는 [NIP-B0](https://github.com/nostr-protocol/nips/pull/2280) 소셜 bookmark 클라이언트를 다듬었고, 이번 주 [PR #96](https://github.com/andotherstuff/nostr-compass/pull/96)으로 프로젝트 웹사이트 link도 추가했습니다. [Keep v1.1.1~v1.1.4](https://github.com/privkeyio/keep-android/releases)는 위에서 다룬 v1.0.5 signer 릴리스 위에 F-Droid 재현 가능 build 수정 네 건을 출시했습니다. 데스크톱 note 클라이언트 [NoorNote v0.11.1, v0.12.0, v0.13.0, v0.13.1](https://github.com/77elements/noornote/releases), Boris reader의 [Boris v0.12.2](https://github.com/dergigi/boris/releases/tag/v0.12.2), [Nostr Mail Client v0.13.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.13.0), [Feeder 2.21.1](https://github.com/spacecowboy/Feeder/releases/tag/2.21.1), Nostr CLI의 내용 없는 maintenance bump [nak v0.19.13](https://github.com/fiatjaf/nak/releases/tag/v0.19.13), hash tree 주소 기반 릴리스 publisher의 gateway mutable root cache를 갱신한 [Hashtree v0.2.68~v0.2.71](https://github.com/mmalmi/hashtree/releases), Nostrify 기반 relay 구현을 올린 [NYM v3.72.501·v3.72.502](https://github.com/Spl0itable/NYM/releases), 병합 PR 85건을 바탕으로 iOS Nostr 클라이언트 minor 릴리스 세 건을 낸 [swift-nostr-client 0.3.0, 0.4.0, 0.5.0](https://github.com/yysskk/swift-nostr-client/releases), LaWallet Nostr Wallet Connect bridge에서 PR 18건을 병합한 [lawallet-nwc v0.11.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v0.11.0), Astraea Nostr 클라이언트를 다듬은 [Astraea v5.35.59~v5.35.62](https://github.com/mouse484/astraea/releases)가 있습니다. [BTC Recharge와 giftcardshop의 NIP-05 검증 Nostr DM bot](https://github.com/andotherstuff/nostr-compass/pull/101)은 새 Shops 분류로 프로젝트 directory에 추가되었습니다.

## 미출시 변경 사항

### diVine, 다음 short-form video 릴리스를 향해 PR 119건 병합

[diVine](https://github.com/divinevideo/divine-mobile)은 Nostr 기반에서 Vine archive를 복원하는 Nostr 네이티브 short-form loop video 클라이언트입니다. 이번 주 tag 릴리스 없이 PR 119건을 병합했습니다. 실질적인 Nostr 기능 작업에는 relay `OK`가 없어도 실패로 표시하지 않는 REST 우선 video 게시 경로([PR #5221](https://github.com/divinevideo/divine-mobile/pull/5221), [PR #5220](https://github.com/divinevideo/divine-mobile/pull/5220)), 전체 blocklist가 바뀔 때 curated 및 liked grid를 다시 거르는 작업([PR #5208](https://github.com/divinevideo/divine-mobile/pull/5208)), 재설치 regression 뒤 DM 대화 목록 복구([PR #5202](https://github.com/divinevideo/divine-mobile/pull/5202)), 프로필의 Nostr badge 표시 복원([PR #5218](https://github.com/divinevideo/divine-mobile/pull/5218)), 댓글 인용문의 `nostr:` 참조를 link로 만드는 작업([PR #5225](https://github.com/divinevideo/divine-mobile/pull/5225))이 포함됩니다. video editor stack은 clip 다중 선택 병합·삭제, zoom을 추적하는 letterbox scrim이 있는 pinch-to-zoom canvas, clip crop·rotate·flip 변환을 추가했습니다.

### Pollerama, signer 개편과 기능 묶음을 포함한 PR 15건 병합

[Pollerama](https://github.com/formstr-hq/nostr-polls)(저장소 `formstr-hq/nostr-polls`)는 Form* 계열의 Nostr 네이티브 poll·feed 클라이언트이며, 이번 주 v1.6.2를 출시한 [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)의 형제 프로젝트입니다. `nostr-polls`의 최신 tag 릴리스는 3월의 [v1.6.4](https://github.com/formstr-hq/nostr-polls/releases/tag/v1.6.4)이므로 기간 안의 작업은 다음 tag를 기다리며 아직 출시되지 않았습니다. 그러나 병합 흐름은 활발했습니다. abh3po, geralt-debugs, SIDDHANTCOOKIE의 기여를 포함해 6월 9~16일 PR 15건이 들어왔습니다. signer 쪽에서는 [PR #198](https://github.com/formstr-hq/nostr-polls/pull/198)로 기존 서명 기능을 교체하고 [PR #201](https://github.com/formstr-hq/nostr-polls/pull/201)로 대체 구현을 업그레이드했습니다. [PR #200](https://github.com/formstr-hq/nostr-polls/pull/200)은 login할 때 kind 0 metadata 갱신이 실행되지 않게 하여, 새 login이 사용자가 요청하지 않은 프로필 이벤트를 게시하지 않습니다. 기능 묶음은 프로필 보기에서 게시할 수 있는 프로필 editor([PR #205](https://github.com/formstr-hq/nostr-polls/pull/205)), 개선된 repost 절차([PR #209](https://github.com/formstr-hq/nostr-polls/pull/209)), 더 쉬운 topic 탐색 경로([PR #202](https://github.com/formstr-hq/nostr-polls/pull/202))를 포함합니다. 다음 tag 릴리스가 이 작업을 모두 가져갑니다.

### 라이브러리 및 도구 작업

[NDK PR #375](https://github.com/nostr-dev-kit/ndk/pull/375)와 [rust-nostr](https://github.com/rust-nostr/nostr), [nostr-tools](https://github.com/nbd-wtf/nostr-tools) 저장소의 병합 작업은 이번 주 각각 PR 한두 건에 tag 릴리스 없이 조용했습니다. [ContextVM SDK](https://github.com/contextvm/contextvm-sdk)(병합 PR 1건), [mesh-llm](https://github.com/agentvm/mesh-llm)(병합 PR 37건, 열린 PR 8건), [Zap Cooking](https://github.com/seth-for-real/zap-cooking)(병합 PR 26건), [Routstrd](https://github.com/routstrd/routstrd)(병합 PR 2건) 작업도 기간 안에 릴리스 tag 없이 이어졌습니다.

## NIP 업데이트 및 프로토콜 사양 작업

이번 주 프로토콜 작업은 signer 강화와 [NIP-29](/ko/topics/nip-29/) 그룹 거버넌스 두 곳에 집중되었습니다.

**이번 주 병합:**
- **[NIP-46](/ko/topics/nip-46/)(Nostr Connect).** [PR #2373](https://github.com/nostr-protocol/nips/pull/2373)은 클라이언트가 원격 signer session을 깔끔하게 끝낼 수 있는 `logout` 메서드를 추가합니다. Amber, Clave, Nostur가 모두 같은 주에 지원을 출시했습니다.
- **NIP-CC(Community Chat).** [PR #2365](https://github.com/nostr-protocol/nips/pull/2365)는 클라이언트 측 구조에 현대적인 [NIP-GC(Group Chat)](https://github.com/nostr-protocol/nips/pull/2331) 사양을 참조하도록 NIP-CC를 갱신해, community room 사양을 canonical 그룹 채팅 primitive와 맞춥니다.

**열린 NIP-29 묶음(relay 기반 그룹 거버넌스):**
- **Banner tag.** [PR #2383](https://github.com/nostr-protocol/nips/pull/2383)은 그룹 metadata kind 39000 이벤트에 `banner` tag를 추가합니다.
- **초대 코드 suffix.** [PR #2380](https://github.com/nostr-protocol/nips/pull/2380)은 일회성 초대를 그룹 ID 자체에 encode할 수 있도록 그룹 식별자에 초대 코드 suffix를 도입합니다.
- **메시지 고정.** [PR #2379](https://github.com/nostr-protocol/nips/pull/2379)는 update-pin-list 중재 action과 고정된 목록을 방송하는 kind 39005 이벤트를 추가합니다.
- **NIP-17 DM을 통한 그룹 신고.** [PR #2377](https://github.com/nostr-protocol/nips/pull/2377)은 멤버가 그룹 악용을 relay의 관리 연락처에 [NIP-17](/ko/topics/nip-17/) gift wrap DM으로 신고하는 절차를 정의해, 중재 traffic을 공개 그룹 event stream에서 분리합니다.
- **역할 기반 접근 제어.** [PR #2376](https://github.com/nostr-protocol/nips/pull/2376)은 기존 admin/member 구분 위에 RBAC 역할 기능을 추가합니다.

**열린 NIP-46 후속 작업:**
- **connect 요청의 클라이언트 metadata.** [PR #2381](https://github.com/nostr-protocol/nips/pull/2381)은 연결하는 클라이언트가 connect 요청에 선택적 `name`, `url`, `icon` field를 보내 signer가 pairing 화면에 애플리케이션 신원을 표시할 수 있게 합니다. Clave build 101이 이 제안을 구현합니다.
- **조용한 timeout 방지.** [PR #2375](https://github.com/nostr-protocol/nips/pull/2375)는 사용자 입력이 필요한 signer가 사용자가 결정할 때까지 요청을 열어 두도록 사양을 조여, Clave build 100이 구현 측에서 패치한 실패 형태를 수정합니다.

**그 밖의 열린 작업:**
- **NIP-100 Sovereign Agent Identity Network(SNIN).** [PR #2378](https://github.com/nostr-protocol/nips/pull/2378)은 autonomous agent의 신원과 capability 탐색을 위한 agent 간 프로토콜을 제안합니다. 제안의 범위가 넓어 review에서 더 작은 여러 조각으로 나뉠 가능성이 큽니다.

**Blossom 사양.** [BUD-00 PR #108](https://github.com/hzrd149/blossom/pull/108)은 6월 15일 병합되어 BUD 정의를, server가 구현하지 않는 Blossom blob 기반 클라이언트 측 관례와 data format까지 포함하도록 넓혔습니다. 이 변경은 BUD-10(`blossom:` URI scheme), BUD-08(Morganite가 이번 주 구현한 로컬 cache 관례) 같은 BUD를 이전의 out-of-band 확장 위치에서 canonical 번호 체계 안으로 가져옵니다.

## NIP 심층 분석: NIP-77(Negentropy)

[NIP-77](/ko/topics/nip-77/)은 Nostr relay를 위한 집합 조정 프로토콜을 정의합니다. 클라이언트와 relay 또는 bridge의 relay 두 곳이 각각 filter에 맞는 이벤트 집합을 갖고 있으며, 모든 항목을 다시 보내지 않고 합집합으로 수렴하려 합니다. 단순한 방법은 모든 event ID를 wire로 보내 diff하는 것입니다. 사용량이 많은 filter에서는 집합이 얼마나 다른지와 무관하게 더 큰 집합의 크기에 비례해 비용이 늘어납니다. NIP-77은 그 비용을 대칭 차이에 비례하도록 줄입니다.

사양은 두 relay 메시지 `NEG-OPEN`과 `NEG-MSG` 위에서 작동합니다. 클라이언트는 `["NEG-OPEN", <subscription_id>, <filter>, <initial_message>]`로 조정 session을 엽니다. `<initial_message>`는 클라이언트가 보는 집합을 설명하는 hex encode Negentropy payload입니다. 응답은 `NEG-MSG` frame으로 오며 양측은 고정점에 이를 때까지 메시지를 교환합니다. 각 `NEG-MSG`는 범위를 자체 fingerprint가 있는 하위 범위로 나눠 불일치를 좁히거나, 작은 범위의 ID를 나열해 수신자가 직접 diff를 계산할 수 있게 leaf를 종료합니다. 상대에게 있고 자신에게 없는 이벤트가 있다고 판단하면 해당 ID에 정상 `REQ`를 보냅니다. 자신에게 있고 상대에게 없는 이벤트의 upload 경로는 사양이 반대편에 대한 정상 `EVENT` 게시로 남겨 둡니다.

그 아래의 data structure는 순서가 있는 Merkle tree 변형입니다. 로컬 집합의 각 이벤트는 `(created_at, id)`를 key로 삼아 범위별 bucket에 들어가고, 각 범위는 담긴 ID에서 계산한 작은 fingerprint를 가집니다. 클라이언트와 relay의 fingerprint가 일치하면 해당 범위는 수렴한 것으로 보고 건너뜁니다. 다르면 응답하는 측이 범위를 절반 또는 하위 범위로 나눠 각각의 fingerprint를 보내고, 불일치 안으로 재귀합니다. 이벤트가 작은 threshold보다 적은 leaf 범위는 그대로 보냅니다. 수렴한 범위는 안에 이벤트가 몇 개 있든 확인 비용이 거의 들지 않는 것이 핵심입니다.

`created_at` 순서의 framing은 두 가지 이유로 중요합니다. 첫째, Nostr의 기존 pagination은 같은 timestamp에 `until`과 `since`를 쓰므로 reconciler가 archive 전체를 다시 sync하지 않고 session 사이에서 재개할 수 있습니다. 상한을 cache하고 다음 sync를 그 지점에서 시작합니다. 둘째, 정렬된 key가 주어지면 범위 분할이 결정적이므로 클라이언트와 relay는 별도의 협상 메시지 없이 다음 boundary에 항상 합의합니다. sync 비용은 대칭 차이의 크기를 d, 더 큰 집합을 n이라 할 때 약 O(d log n)입니다. 단순 ID dump의 O(n) 비용과 N개의 REQ를 내는 O(n) round trip보다 훨씬 작습니다.

구현에는 세 가지 절충이 있습니다. fingerprint 크기(사양은 범위당 32byte 사용)는 collision 확률과 bandwidth 사이의 절충입니다. fingerprint가 작으면 byte를 아끼지만 event를 빠뜨리는 잘못된 일치 가능성이 커집니다. leaf threshold, 즉 분할을 멈추고 ID를 그대로 보낼 시점은 round trip과 메시지당 bandwidth 사이의 절충입니다. threshold가 작으면 교환 횟수가 늘고 크면 leaf 메시지가 커집니다. 프로토콜은 양측이 같은 범위에 대해 같은 fingerprint를 계산할 수 있다고 가정합니다. 그러려면 두 구현이 합의한 `(created_at, id)` pair의 안정적인 serialization이 필요하며, 그래서 사양은 fingerprint 구성의 byte order를 엄격히 지정합니다.

NIP-11 `supported_nips`에 NIP-77을 광고하는 relay에서는 클라이언트가 일반 `REQ` 기반 sync 대신 또는 그와 함께 조정을 쓸 수 있습니다. 클라이언트는 필요에 따라 프로토콜을 고릅니다. 이전 상태가 없고 최신 traffic을 받으려는 새 subscription은 `REQ`를 사용합니다. 중단 뒤 따라잡으려는 장기 mirror는 archive에 비해 대칭 차이가 작으므로 `NEG-OPEN`을 사용합니다. 두 경로는 서로 다른 배포 맥락에서 보완 관계입니다.

`NEG-OPEN` 교환 예시:

```
→ ["NEG-OPEN", "sync-1", {"kinds":[1],"authors":["abc..."]}, "<hex initial Negentropy message>"]
← ["NEG-MSG", "sync-1", "<hex relay response>"]
→ ["NEG-MSG", "sync-1", "<hex client refinement>"]
← ["NEG-MSG", "sync-1", "<hex leaf with IDs the relay has and client lacks>"]
→ ["REQ", "fetch-1", {"ids":[...]}]
← [...EVENT messages...]
← ["EOSE", "fetch-1"]
→ ["CLOSE", "sync-1"]
```

[Citrine v3.0.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0)은 이번 주 relay aggregator에 [NIP-77](/ko/topics/nip-77/) 지원을 출시했습니다. Android 로컬 relay가 bulk `REQ` pull 대신 외부 relay와 조정할 수 있게 된 것은 이번이 처음입니다.

## NIP 심층 분석: NIP-61(Nutzap)

[NIP-61](/ko/topics/nip-61/)은 Nostr 이벤트로 전달되는 P2P Cashu ecash 결제를 정의합니다. 송신자는 수신자의 Nostr에서 파생된 public key에 잠긴 Cashu token을 게시하고, 수신자는 편한 때 mint에서 교환합니다. 결제 순간 수신자가 Lightning으로 접근 가능해야 하는 NIP-57 zap과 달리 nutzap은 수신자가 원하는 때 교환할 수 있는 독립적인 ecash token입니다.

사양은 Cashu의 P2PK lock primitive와 세 가지 event kind를 조합합니다. kind 10019는 수신자의 mint 추천입니다. 수신자가 nutzap을 받을 mint 하나 이상과 proof를 잠그는 데 쓰는 Cashu public key를 나열하는 replaceable 이벤트입니다. 이 key는 수신자의 Nostr identity key와 다릅니다. identity key가 ecash secret을 다룰 필요가 없도록 nutzap 수신용으로 파생한 wallet 범위 key입니다. 송신자는 보내기 전에 kind 10019를 읽어, 수신자가 이미 신뢰하는 mint에서 교환할 수 있는 token을 만듭니다.

kind 9321은 결제 이벤트입니다. Cashu `proof` tag 하나 이상을 담으며 각 tag에는 kind 10019에 있는 수신자의 nutzap pubkey에 묶인 P2PK lock proof가 들어갑니다. mint URL을 담은 `u` tag, zap 대상 note를 식별하는 선택적 `e`와 `a` tag, 수신자용 `p` tag도 있습니다. 수신자는 정상 Nostr subscription으로 kind 9321을 받고, proof가 자신의 kind 10019에 나열된 mint에서 자신의 nutzap pubkey에 잠겼는지 검증하며, 해당 private key로 proof를 풀어 [NIP-60](/ko/topics/nip-60/) 지갑에 보관하거나 Lightning으로 melt합니다. kind 7375는 사용된 proof를 수신자의 wallet event chain에 기록해, relay에서 다시 sync한 지갑이 같은 source의 nutzap proof를 중복 계산하지 않게 합니다.

신뢰 모델은 이 설계가 명시적으로 치르는 대가입니다. Cashu mint가 기반 가치를 보유하므로 악성 또는 압류된 mint는 교환을 거부할 수 있습니다. NIP-61은 NIP-60의 수탁 위험을 물려받으며 이를 없애려 하지 않습니다. 대신 offline에서 쓸 수 있고 즉시 확정되는 소액 결제를 얻습니다. token 자체가 결제이므로 수신자는 Lightning node를 운영하거나 실시간으로 들어오는 HTLC를 받을 필요가 없고, 같은 mint의 proof를 가진 송신자는 custodian으로 한 번도 network hop하지 않고 결제할 수 있습니다. kind 10019 광고는 social layer의 gate입니다. 수신자의 신뢰 집합 밖 mint를 고른 송신자는 교환 불가능한 token을 만들 위험을 지므로, 수신자의 교환 범위가 예측 가능하게 유지됩니다.

NIP-57과 비교하면 검증 경로도 더 단순합니다. NIP-57 zap receipt는 수신자의 LNURL service가 게시한 kind 9735이므로, 검증자가 LNURL endpoint를 가져와 receipt의 signing key가 endpoint가 선언한 key와 일치하는지 확인해야 합니다. nutzap은 결제의 암호 proof인 P2PK lock proof 자체를 inline으로 담아, mint의 public key를 가진 검증자는 제3자와 왕복하지 않고 proof의 유효성을 확인할 수 있습니다. 반면 nutzap 검증에는 mint keyset을 이해해야 하고 NIP-57 검증에는 표준 LNURL infrastructure만 필요합니다.

두 zap 형식은 상호 보완적으로 공존합니다. Lightning routing을 갖춘 수신자와 Lightning 정산 의미를 유지하며 sats 단위로 결제하려는 송신자에게는 NIP-57 zap이 알맞습니다. offline 수신자, Lightning 수수료가 전송 가치보다 커지는 소액 결제 중심 흐름, Lightning infrastructure가 없는 사용자를 대상으로 하는 클라이언트에는 NIP-61 zap이 알맞습니다.

nutzap 이벤트 예시:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

[Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)은 이번 주 NIP-60 지갑 기능과 함께 NIP-61 nutzap 렌더링을 출시해([PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075)), 받은 nutzap을 timeline에 렌더링하고 지갑에 mint별 잔액 보기를 제공하는 최초의 주요 Android 클라이언트가 되었습니다.
