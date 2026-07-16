---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
draft: false
type: newsletters
translationOf: /en/newsletters/2026-07-15-newsletter.md
translationDate: 2026-07-15
description: "Vector v0.4.0가 그룹 채팅의 기본 전송 방식을 Marmot에서 개방형 Concord 프로토콜로 전환하고 며칠 뒤 Concord v2를 출시하며, Amethyst가 자체 클린룸 Concord 구현을 병합하고, Sonar가 크로스 플랫폼 알파와 스티커 팩 명세와 함께 Bitchat에서 분리되며, Divine Mobile 1.0.16이 저장 데이터 암호화와 ProofMode 출처 정보를 도입하고, Bitchat 1.7.0이 실시간 푸시투토크 음성을 추가하며, MDK v0.9.4가 외부 서명자 로그인에 상한을 둔다."
---

Nostr에 대한 주간 가이드, Nostr Compass에 다시 오신 것을 환영합니다.

**이번 주:** [Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)가 그룹 채팅의 기본 전송 방식으로서 [Marmot](/ko/topics/marmot/)을 은퇴시키고 [Concord](/ko/topics/concord-protocol/)를 채택했습니다. Concord는 Soapbox의 Armada도 사용하는 개방형 MIT 라이선스 커뮤니티 프로토콜이며, 4일 뒤 Vector는 봇용 슬래시 명령어 선택기, 자폭 타이머, NIP-58 badge를 담은 Concord v2를 출시했습니다. 같은 주에 [Amethyst가 자체 클린룸 방식의 와이어 호환 Concord 구현을 병합했습니다](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities). [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec)는 크로스 플랫폼 알파와 함께 Bitchat에서 분리되었으며, 이번 주 스티커 팩 kind 제안의 인용된 명세 출처입니다. [Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)은 더 깊이 있는 비디오 편집기, 저장 데이터 암호화, 그리고 워터마크 클립 다운로드에도 유지되는 ProofMode 출처 정보를 도입했습니다. [Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh)은 DM용 실시간 푸시투토크 음성과 공개 메시에서의 서명된 푸시투토크를 추가했습니다. [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence)는 외부 서명자 로그인에 상한을 두고 초안 유지 기능을 추가하며, Vector가 그룹 채팅 명세에서 손을 떼는 바로 그 주에 강화 작업을 이어갔습니다.

태그가 붙은 릴리스로는 NSEC Bunker 지원을 추가한 [n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support), cdk, cdk-nwc, cdk-ffi 전반에 걸쳐 NIP-47 wallet-service 지원을 추가한 [cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi), Nostr Connect를 개선하고 ncryptsec1 가져오기를 추가한 [Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import), 예약 발송과 함께 macOS에 안착한 [Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications), DM 마스터 토글을 추가한 [Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages), 키 백업을 NIP-49 형식으로 강화한 [Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts), 최초 실행 FROST 온보딩을 추가한 [Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding), Cashu 지갑과 relay 기반 푸시 알림을 추가한 [Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications), 태블릿 모드와 그룹 채팅 사진을 추가한 [Kubo](#kubo-ships-tablet-mode-and-group-chat-photos), 그리고 git, diff, read-file 헬퍼 요청을 추가한 [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests)가 있습니다.

아직 릴리스되지 않은 쪽에서는, [Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards)가 54개의 병합된 PR을 통해 암호화된 NIP-85 카드로 계정이 연락처에 별명을 붙일 수 있게 했고, [Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug)이 My Kitchen 3단계를 출시하고 NDK 풀 정족수 버그를 수정했으며, [Kehto](#kehto-streams-outbox-reads-before-relay-discovery)가 relay 탐색이 끝나기 전에 outbox 읽기를 스트리밍하고, [Wired와 TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing)가 NIP-57 크리에이터 수익 분배를 추가했으며, [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout)가 일회성 게스트 체크아웃을 중심으로 판매자 주문함을 재구축했고, [Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002)가 240개의 병합된 PR을 통해 채널 생성자 프로비저닝을 강화했으며, [Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing)가 다중 계정과 QR 페어링을 갖춘 NIP-49 서명자를 채택했습니다. 이번 주 새로 추적된 프로젝트: [OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr), [Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles), 그리고 Discovery 선정작 [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer)로, Heartwood 하드웨어 동반 기기로 요청을 프록시하는 키 없는 NIP-55 서명자입니다.

NIPs 저장소는 지난 한 주 동안 아무것도 병합하지 않았고 여섯 개의 제안을 열었습니다: [kind:10011 즐겨찾기 팔로우 세트](#open-kind10011-favorite-follow-sets), [NIP-4E를 확장하는 비공개 암호화 드라이브](#open-private-encrypted-drive-extends-nip-4e), [NIP-DA 권한 기반 비공개 데이터 공유](#open-nip-da-permissioned-private-data-sharing), [스티커 팩 kind 10031과 30031](#open-sticker-pack-kinds-10031-and-30031), [NIP-29 메시지 고정](#open-nip-29-message-pinning-with-kind9010-and-kind39005), 그리고 [NIP-66 relay 탐색 재구조화](#open-nip-66-relay-discovery-restructure). Deep Dive는 [NIP-99와 Gamma Markets 커머스 확장](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)을 다룹니다.

---

## 주요 소식

### Vector v0.4.0가 그룹 채팅을 Marmot에서 Concord로 옮기고, 며칠 뒤 Amethyst가 자체 Concord 클라이언트를 출시하다

[Vector](https://github.com/VectorPrivacy/Vector)는 DM과 그룹 채팅을 위한 단일 바이너리, 프라이버시 우선 클라이언트를 중심으로 구축된 Nostr 메신저입니다. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)는 앱의 메시징 엔진을 공유 `vector-core` 라이브러리로 재작성하고, 같은 릴리스에서 그룹 채팅의 기본 전송 방식으로서 [Marmot](/ko/topics/marmot/)(MLS-over-Nostr)을 은퇴시키고 종단 간 암호화 커뮤니티 프로토콜인 [Concord](/ko/topics/concord-protocol/)를 채택했습니다. 기존 Marmot 그룹 기록은 이전되지 않으며, 릴리스 노트는 사용자에게 업그레이드 전에 Marmot 그룹 데이터를 백업하라고 안내합니다. Vector 자체 릴리스 노트는 Concord를 "우리의 맞춤형 메시징 프로토콜"이라고 설명하지만, 그 기반인 [CORD-01부터 CORD-07까지의 명세](https://github.com/concord-protocol/concord)는 별도로 공개되어 있고, MIT 라이선스이며, 이미 Vector 외부에서 구현되어 있습니다. Soapbox의 Discord 스타일 클라이언트 [Armada](https://gitlab.com/soapbox-pub/armada)는 같은 Concord 명세 위에 Communities 기능을 구축하고 있으며, 하루 뒤 [Amethyst가 자체 클린룸 방식의 와이어 호환 Concord 구현을 병합했습니다](https://github.com/vitorpamplona/amethyst/pull/3566)(아래에서 자세히 다룹니다). 같은 Vector 릴리스는 모든 트래픽에 대한 선택적 Tor 라우팅, QR 또는 붙여넣은 bunker URI를 통한 [NIP-46](/ko/topics/nip-46/) 원격 서명자 로그인, 앱 내 전환기를 갖춘 다중 계정, 그리고 클라이언트 간에 공유되는 커스텀 이모지 팩을 추가합니다. 메시지 삭제는 DM과 그룹 채팅에서 양쪽 모두에게 메시지를 제거하며, Vector는 표준 [NIP-17](/ko/topics/nip-17/) 삭제 흐름을 따르는 대신 의도적으로 일회성 서명 키를 보관하는데, 이는 프로젝트가 릴리스 노트에서 명시적으로 밝히는 프라이버시 동기의 결정입니다. 4일 뒤, [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)이 **Concord v2**를 출시했습니다. 이는 기존 Communities를 계속 작동시키면서 Communities에 중요한 프라이버시 및 안정성 개선을 가져오는 것으로 설명되며, 봇용 타입 지정 매개변수를 갖춘 Discord 스타일 슬래시 명령어 선택기, 채팅별 자폭 타이머, 그리고 버그 헌터를 위한 NIP-58 badge 시스템을 함께 담고 있습니다. 그룹 채팅에서 Marmot을 떠나는 이 움직임은 아래의 [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence)가 계속해서 그 명세에 투자하는 바로 그 주에 나왔습니다.

### Amethyst가 종단 간 암호화 커뮤니티를 위한 클린룸 Concord 구현을 출시하다

[Amethyst](https://github.com/vitorpamplona/amethyst)는 기능이 풍부한 Android 및 멀티플랫폼 Nostr 클라이언트입니다. [PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)은 서버 없는 종단 간 암호화 커뮤니티를 다루는 [Concord](/ko/topics/concord-protocol/)(CORD-01부터 CORD-07)의 완전한 구현을 추가합니다. 여기에는 일반 relay 위에서 gift-wrap된 제어, 채팅, 방명록 평면, 모든 클라이언트가 서버를 신뢰하는 대신 로컬에서 검증하는 소유자 기반 역할 및 차단 집행, 그리고 제거된 구성원의 접근을 끊기 위한 재키잉이 포함됩니다. 프로토콜과 암호화 코드는 `quartz/`에, 상태 및 뷰 모델은 `commons/`에, 화면과 내비게이션은 Android용 `amethyst/`에 있으며, 얇은 CLI 동사가 `cli/` 아래에 있습니다. 아직 데스크톱 UI는 없는데, 공유 로직이 `quartz`/`commons`에 있어 나중에 Desktop이 채택할 수 있기 때문입니다. 이 구현은 클린룸 방식입니다. 공개된 CORD 명세와 관찰된 와이어 상수를 바탕으로 Amethyst 자체 MIT 라이선스 아래 구축되었으며, Armada의 AGPL-3.0 코드베이스와는 별개입니다. Armada 자체 테스트 벡터 값이 Quartz의 단위 테스트로 이식되어 두 클라이언트가 실제로 와이어 수준에서 상호 운용됨을 확인했고, 이로써 Concord는 며칠 사이에 세 개의 독립 구현을 갖게 되었습니다. Vector가 먼저 출시했고, Armada가 Soapbox의 참조 클라이언트이며, 이제 Amethyst의 명세 기반 빌드가 더해졌습니다.

### Sonar가 크로스 플랫폼 알파와 스티커 팩 명세와 함께 Bitchat에서 분리되다

[Sonar](https://sonarprivacy.xyz/)는 Bitchat에서 성장한 블루투스 메시 및 Nostr 메신저 겸 지갑으로, White Noise와 상호 운용되는 Marmot 그룹 DM을 갖추고 있습니다. 코드는 [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar)에 있습니다. [v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7)은 열기와 스크롤 성능이 로컬 우선으로 유지되도록 Signal 스타일의 경계 있는 대화 기록 윈도잉을 추가하고, 근처 탐색 상태를 피어 간에 동기화하며, content-type과 HTTP 상태 처리에서 실패하던 Blossom 미디어 업로드를 수정합니다. 앞선 [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6)은 더 빠른 채팅 새로고침을 위해 실시간 Marmot 이벤트를 소진했고 통화, 메시징, 지갑, 푸시 전반에 걸쳐 Android-iOS 기능 격차를 좁혔습니다. Sonar는 또한 [PR #2410](#open-sticker-pack-kinds-10031-and-30031)의 인용된 명세 출처로, 프로젝트 자체의 "Sonar Stickers" 명세 아래 스티커 팩 이벤트 kind를 등록하며, 이번 출시에 이번 주 프로토콜 작업으로 향하는 직접적인 허브 링크를 제공합니다.

### Divine Mobile 1.0.16이 더 깊이 있는 비디오 편집기, 저장 데이터 암호화, ProofMode 출처 정보를 도입하다

[Divine](https://github.com/divinevideo/divine-mobile)은 Web-of-Trust 피드 큐레이션을 갖춘 Nostr 기반 숏폼 비디오 클라이언트입니다. #30 이후 첫 태그 릴리스인 [v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16)은 비디오 편집기에 클립 전환, 역재생, 보이스오버 녹음기, 타임라인 비트 마커를 추가하며, 사용자가 불투명한 참여 신호에 맡기는 대신 직접 스와이프해 추천을 조정할 수 있게 하는 피드 조정 컨트롤도 함께 제공합니다. 이 릴리스는 또한 로컬 데이터에 대한 저장 데이터 암호화를 켜고, 앱이 중단되어도 유지되는 백그라운드 업로드를 추가하며, 워터마크 클립이 다운로드될 때 [ProofMode](/ko/topics/proofmode/) 출처 데이터를 함께 전달해 인간이 만든 증명이 전송 중에 벗겨지지 않도록 합니다. Divine은 또한 16세 미만 계정에 대한 새로운 보호 기능을 도입하고 로컬라이제이션을 17개 언어와 284개의 번역 문자열로 확장했습니다.

### Bitchat v1.7.0이 DM과 공개 메시를 위한 실시간 푸시투토크 음성을 추가하다

[Bitchat](https://github.com/permissionlesstech/bitchat)은 Nostr relay로의 선택적 게이트웨이를 갖춘 블루투스 메시 채팅 앱입니다. #30이 게시된 저녁에 릴리스된 [v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0)은 [PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403)에서 실시간 푸시투토크 음성을 추가하는데, 발신자가 버튼을 누르는 동안 오디오를 스트리밍하고 스트림이 끊기면 음성 메모로 대체합니다. 또한 [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406)에서 서명된 공개 메시 푸시투토크를 추가해 공유 메시 채널의 실시간 음성 버스트가 발신자 인증을 담도록 합니다. 이 릴리스는 또한 검증된 재공지 시 링크를 재바인딩하여 같은 피어를 새 ID로 인식함으로써 peer-ID 회전을 복구하고([PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)), 현재 도달할 수 없는 피어로 향하는 직접 메시지가 곧바로 실패하는 대신 store-and-forward 전달로 대기열에 들어가도록 합니다([PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)). 이는 v1.6.0의 [NIP-13](/ko/topics/nip-13/) proof-of-work와 메시-to-Nostr 게이트웨이 작업을 다룬 #30의 보도에서 직접 이어집니다.

### MDK v0.9.4가 외부 서명자 로그인에 상한을 두고 초안 유지를 추가하다

[MDK](https://github.com/marmot-protocol/mdk)는 [Marmot](/ko/topics/marmot/) 프로토콜의 참조 SDK로, #30이 그 명세가 채택되었음을 다룬 MLS-over-Nostr 메시징 계층입니다. [v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4)는 [PR #793](https://github.com/marmot-protocol/mdk/pull/793)에서 클라이언트가 외부 서명자 로그인 중에 거치는 권고 디렉터리 단계에 상한을 두어, 원격 서명자가 느리거나 응답하지 않을 때 무한 재시도 루프를 방지합니다. 같은 릴리스는 [PR #812](https://github.com/marmot-protocol/mdk/pull/812)에서 초안 메시지 유지와 프로필-웹사이트 바인딩을 추가하며, MDK가 v0.9.0을 낸 이후 이어온 점진적 강화 작업을 계속합니다.

---

## 태그 릴리스

### n_cord v1.1이 NSEC Bunker 지원을 추가하다

[n_cord](https://github.com/0n4t3/n_cord)는 Discord와 IRC에서 영감을 받은 Nostr 기반 채팅 클라이언트입니다. [v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1)은 [NIP-46](/ko/topics/nip-46/) NSEC Bunker 지원을 답글 처리 버그 수정과 함께 추가합니다.

### cdk v0.17.3이 cdk, cdk-nwc, cdk-ffi 전반에 NIP-47 wallet-service 지원을 추가하다

[cdk](https://github.com/cashubtc/cdk)는 Cashu 개발 키트입니다. 이 릴리스는 대부분의 측면에서 Bitcoin/Lightning 전용이지만, [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3)은 전용 NWC 서비스 크레이트, 지갑 통합, `cdk-ffi`용 FFI 바인딩, 종단 간 테스트 커버리지와 함께 [NIP-47](/ko/topics/nip-47/)(Nostr Wallet Connect) 서비스 지원을 추가하여, cdk 위에 구축된 Cashu 지갑에 표준 Nostr Wallet Connect 표면을 제공합니다.

### Coop Mobile v0.2.4가 Nostr Connect를 개선하고 ncryptsec1 가져오기를 추가하다

[Coop Mobile](https://git.reya.su/reya/coop-mobile)은 모바일 플랫폼용 [NIP-17](/ko/topics/nip-17/) 비공개 메시징 클라이언트입니다. [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4)는 [NIP-46](/ko/topics/nip-46/) Nostr Connect 흐름을 개선하고, 일부 연결에서 영구적으로 멈춰 있던 로딩 표시를 수정하며, 재설계된 신원 가져오기 화면과 함께 [NIP-49](/ko/topics/nip-49/) `ncryptsec1` 암호화 키 형식에 대한 가져오기 지원을 추가합니다.

### Nmail v0.14.0이 예약 발송 및 푸시 알림과 함께 macOS에 안착하다

[Nmail](https://github.com/nogringo/nostr-mail-client)은 Nostr 기반 메일 클라이언트입니다. [v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0)은 앱을 macOS로 가져오고, 대기 중인 메시지를 위한 전용 예약 메일함과 함께 예약 발송을 추가하며, 푸시 알림을 추가합니다. 이 릴리스는 또한 주소록 Nostr 식별자 해석을 자체 구현 대신 NDK의 [NIP-05](/ko/topics/nip-05/) 리졸버로 전환합니다.

### Nostrord v2.2.0이 DM 마스터 토글과 더 풍부한 직접 메시지를 추가하다

[Nostrord](https://github.com/nostrord/nostrord)는 Android, iOS, 웹, 데스크톱용 [NIP-29](/ko/topics/nip-29/) relay 기반 그룹 채팅 클라이언트입니다. [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0)은 모든 직접 메시지 기능을 한 번에 비활성화하는 마스터 토글을 추가하고([PR #175](https://github.com/nostrord/nostrord/pull/175)) "더 풍부한 직접 메시지"를 출시하며([PR #186](https://github.com/nostrord/nostrord/pull/186)), relay 풀을 통합하고 좀비 WebSocket을 감지한 릴리스를 다룬 #30의 보도에서 이어집니다.

### Nostr WoT 0.3.86이 키 백업과 서명 프롬프트를 강화하다

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension)는 Nostr 신원과 Lightning 지갑을 짝지어주는 브라우저 확장 프로그램입니다. [v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86)은 암호화된 키 백업을 표준 [NIP-49](/ko/topics/nip-49/) 형식으로 옮기고, 서명 프롬프트가 요약 대신 전체 이벤트와 모든 tag를 표시하도록 하며, relay 데이터를 그 서명에 대해 검증하고, 계정 전환 시 활성 신원이 노출되지 않도록 합니다. 이 확장 프로그램은 또한 사용되지 않던 `scripting` 브라우저 권한을 제거합니다.

### Keep Android v1.1.8이 최초 실행 FROST 온보딩을 추가하다

[Keep](https://github.com/privkeyio/keep-android)은 임계값 FROST 키 조각 위에 구축된 Android 서명자입니다. [v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8)은 FROST 키 조각을 설명하고 새 사용자가 첫 서명 요청이 도착하기 전에 Manual, Basic, Auto 중 서명 정책을 선택하게 하는 최초 실행 흐름을 추가하는데, 이는 기반이 되는 keep-mobile 크레이트의 임계값 서명 모델에 대한 Android 측 최초 온보딩입니다.

### Noscall v0.6.0이 Cashu 지갑과 relay 기반 푸시 알림을 추가하다

[Noscall](https://github.com/sanah9/noscall)은 Nostr 기반의 안전한 음성 및 영상 통화 앱입니다. [v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release)은 멀티 민트 잔액, ecash 송수신, 견적 유지 기능이 있는 Lightning 지불 및 수령을 갖춘 계정 범위의 Cashu 지갑을 추가합니다. 이 릴리스는 또한 Android 푸시 알림을 Firebase Cloud Messaging에서 UnifiedPush를 통한 Nostr-relay 기반 전달 경로로 이전하고, 로그인 재시도 중 iOS VoIP 및 APNs 푸시 신뢰성을 개선합니다.

### Kubo가 태블릿 모드와 그룹 채팅 사진을 출시하다

[Kubo](https://github.com/JeroenOnNostr/kubo)는 Web-of-Trust 피드 큐레이션을 갖춘 아동 안전 Nostr 비디오 플랫폼입니다. [kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05)는 아동 피드용 선택적 태블릿 그리드 레이아웃과 그룹 채팅 메시지에 사진을 첨부하는 지원을 추가하고, Android에서 가입 버튼이 화면 키보드 뒤에 숨는 문제를 수정합니다.

### Nostr Codex Phone v0.2.9가 git/diff/read-file 헬퍼 요청을 추가하다

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone)은 암호화된 Nostr DM을 통해 통신하는 로컬 코딩 어시스턴트 워커를 위한 모바일 제어 표면입니다. [v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9)는 git, diff, read-file, status, history 헬퍼 요청을 포함한 모바일 OpenCode 도구 액션, 세션 고정 및 검색 개선, 작업 중단 컨트롤을 추가하며, 앞선 v0.2.8에서 출시된 암호화된 [Blossom](/ko/topics/blossom/) 업로드 래퍼를 함께 담고 있습니다.

### GitWorkshop v3.0.3이 저장소 탐색기에서 새로 공지된 ref를 수정하고, 첫 Android 빌드를 출시하다

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop)은 NIP-34 저장소를 탐색하고 검토하기 위한 git-over-Nostr 웹 UI입니다. [v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3)은 탐색기가 이미 저장소를 로드한 뒤 그 저장소가 공지하는 ref를 브랜치, 태그, 커밋, 코드 브라우징 뷰가 해석하지 못하던 문제를 수정하며, CI 워크플로 타이밍 정리와 함께 태그 및 커밋 기록에 대해 직접 확인되었습니다. 같은 주에 GitWorkshop은 첫 네이티브 Android 빌드를 [Zapstore](https://zapstore.dev)에 게시했으며, v3.0.0에서 시작해 몇 시간 만에 v3.0.3에 도달했습니다. 웹 UI가 주요 인터페이스로 남아 있으며, Android 패키지는 동일한 NIP-34 저장소 브라우징을 처음으로 휴대폰에 가져옵니다.

### Bitcoin-Safe가 Flathub에 도달하며 Nostr Sync & Chat 플러그인을 부각시키다

[Bitcoin-Safe](https://bitcoin-safe.org)는 하드웨어 서명자 워크플로를 중심으로 구축된 자기 수탁 Bitcoin 지갑입니다. 이 프로젝트는 이번 주에 [Flathub 패키지를 출시](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe)했는데, 이는 주류 Linux 앱 스토어에 첫 등록입니다. Flathub 릴리스는 Bitcoin-Safe의 Sync & Chat 플러그인을 더 넓은 청중 앞에 세웁니다. 이 플러그인은 프로젝트 자체의 [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat) 라이브러리를 통해 [NIP-17](/ko/topics/nip-17/) 직접 메시지를 사용하여, 사용자의 여러 기기 간에 지갑 라벨을 동기화하고 신뢰하는 참가자 간 원격 멀티시그 공동 서명을 위한 PSBT를 주고받습니다. Nostr 계층 자체는 앞서 [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0)(2026-06-29)에서 출시되어 QR, USB, 블루투스와 함께 "Share via Chat & Sync" 연결 유형을 중심으로 트랜잭션 서명을 재설계했습니다. 이번 주의 소식은 그 기존 기능을 처음으로 주류 Linux 청중 앞에 세우는 Flathub 패키징입니다.

---

## 아직 릴리스되지 않은 변경 사항

### Amethyst가 암호화된 NIP-85 카드로 계정이 연락처에 별명을 붙일 수 있게 하다

위에서 다룬 [Concord 구현](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) 외에도, Amethyst는 지난 한 주 동안 54개의 다른 PR을 병합했습니다. 그중 대표작은 [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548)로, 계정이 다른 사용자에 대한 자체 kind 30382 [NIP-85](/ko/topics/nip-85/) 연락처 카드를 게시함으로써 그 사용자에게 별명을 붙일 수 있게 합니다. 별명, 비공개 메모, 그리고 모든 커스텀 [NIP-30](/ko/topics/nip-30/) 이모지 단축코드 매핑은 카드의 [NIP-44](/ko/topics/nip-44/) 암호화 콘텐츠 안에 있어 서명 계정만 읽을 수 있으며, 카드는 로그인 시 계정의 확장된 outbox relay 집합을 통해 동기화되고 이후 점진적으로 동기화됩니다. 피드, 채팅, 멘션은 공개 표시 이름 대신 별명을 렌더링하며, 프로필 페이지의 사용자 실명 위에 탭 가능한 별명 카드를 표시합니다.

### Zap Cooking이 My Kitchen 3단계를 출시하고 NDK 풀 정족수 버그를 수정하다

[Zap Cooking](https://github.com/zapcooking/frontend)은 Nostr 기반 레시피 공유 및 요리 커뮤니티 앱입니다. "My Kitchen" 식사 계획 기능을 이어가는 43개의 PR을 병합하여, 이번 단계에서 장보기 목록 생성, 레시피 선택기, 주간 계획 그리드를 도입했습니다. 같은 변경 세트는 relay 읽기가 정족수의 relay가 이미 응답한 지점을 지나서까지 대기하게 만들 수 있던 [NDK](https://github.com/nostr-dev-kit/ndk)(Nostr Development Kit) 연결 풀 정족수 준비 버그를 수정합니다.

### Kehto가 relay 탐색 전에 outbox 읽기를 스트리밍하다

[Kehto](https://github.com/kehto/web)는 [NIP-5D](/ko/topics/nip-5d/) Nostr 애플릿, 즉 "napplet"을 위한 초기 웹 기반 런타임입니다. 26개의 PR을 병합했습니다. [PR #193](https://github.com/kehto/web/pull/193)은 이전에 어떤 relay라도 열기 전에 [NIP-65](/ko/topics/nip-65/) relay 목록 로딩이 끝나기를 기다리던 outbox 읽기를 수정하는데, 이 때문에 끝내 해결되지 않는 relay 목록 로드가 이벤트 전달과 쿼리 타임아웃 모두를 막을 수 있었습니다. 이 수정은 검증된 relay 힌트를 즉시 열고 쓰기 relay가 발견되는 대로 결과를 스트리밍합니다. 두 번째 변경([PR #196](https://github.com/kehto/web/pull/196))은 프로젝트의 신원 감사 페이지를 Napplet 플랫폼의 수명 주기 계약인 NAP-SHELL과 정렬하며, 이번 주 `napplet/web` 릴리스 곳곳에서 보이는 같은 프로토콜 정렬 작업의 일부입니다.

### Wired와 TAO가 NIP-57 크리에이터 수익 분배를 추가하다

[Wired](https://github.com/smolgrrr/Wired)와 [TAO](https://github.com/smolgrrr/TAO)는 Nostr 기반의 표현의 자유에 초점을 맞춘 쌍둥이 소셜 클라이언트로, 같은 PR 목록을 공유합니다. 둘 다 [PR #121](https://github.com/smolgrrr/Wired/pull/121)을 병합했는데, 이는 게시물로 보낸 zap이 원래 게시자를 넘어 기여자들에게 자동으로 분할될 수 있도록 [NIP-57](/ko/topics/nip-57/) 크리에이터 수익 분배를 구현합니다. 이는 이 쌍이 proof-of-work 신호를 21비트로 높인 작업을 릴리스되지 않은 작업으로 다룬 #30의 보도에서 이어집니다.

### Conduit Mono가 일회성 게스트 체크아웃을 중심으로 판매자 주문함을 재구축하다

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono)는 [NIP-99](/ko/topics/nip-99/) 클래시파이드 리스팅에 인접한 마켓플레이스 프로토콜입니다. [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174)는 브라우저가 생성한 일회성 키를 사용한 게스트 체크아웃을 추가합니다. 게스트는 그 일회용 키로 암호화된 주문과 지불 보고서를 판매자에게 보내고, 판매자는 전화나 이메일로 대역 외에서 후속 조치를 하므로 구매자는 결코 지속적인 수신함 신원이 필요하지 않습니다. [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175)는 판매자 주문함을 단일 공유 주문 상태 모델을 중심으로 재구축하여, 구매자와 판매자 역할을 분리하고 물리적 또는 혼합 주문이 배송됨 상태로 넘어가기 전에 추적 코드와 배송사를 요구합니다. 이 프로젝트의 체크아웃 흐름은 [NIP-17](/ko/topics/nip-17/) 비공개 메시지, [NIP-44](/ko/topics/nip-44/) 암호화, [NIP-59](/ko/topics/nip-59/) gift wrap 위에 구축됩니다. 이번 주의 [NIP Deep Dive](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)는 바로 이 주문 상태 문제가 향하는 [Gamma Markets](/ko/topics/gamma-markets/) 규약을 다룹니다.

### Buzz가 kind 39002를 중심으로 채널 생성자 프로비저닝을 강화하다

[Buzz](https://github.com/block/buzz)는 AI 에이전트와 인간을 Nostr 위에서 연결하는 집단지성 통신 플랫폼입니다. 지난 한 주 동안 240개의 PR을 병합하며, kind 44200 에이전트 턴 메트릭을 다룬 #30의 보도에서 이어지는 relay 계층 강화 흐름을 계속했습니다. 이번 주의 수정([PR #1830](https://github.com/block/buzz/pull/1830))은 kind 39002 채널 프로비저닝 로직이 실행되기 전에 채널의 생성자를 구성원으로 취급하여, 설정 중 생성자 자신의 채널이 그를 거부할 수 있던 경쟁 조건을 막습니다.

### Nostr Docs가 다중 계정과 QR 페어링을 갖춘 NIP-49 서명자를 채택하다

[Nostr Docs](https://github.com/formstr-hq/nostr-docs)는 Nostr 네이티브 협업 문서 애플리케이션입니다. 5개의 PR을 병합했으며, 주목할 만한 것([PR #50](https://github.com/formstr-hq/nostr-docs/pull/50))은 다중 계정 전환과 QR 페어링을 갖춘 완전한 [NIP-49](/ko/topics/nip-49/) 인증을 위해 `@formstr/signer` 패키지를 채택하여, 앞선 자체 서명 경로를 대체합니다.

### 그 외 출시

지난 한 주 동안 여러 추적 프로젝트에 자체 문단을 둘 만큼의 새로운 표면은 아니지만 소소한 서명자 상호 운용 및 신뢰성 수정이 안착했습니다: Nostr 기반 GitHub 대안을 위한 명령줄 클라이언트인 [ngit-cli](https://github.com/DanConwayDev/ngit-cli)는 `ngit init`이 nsec를 반복해서 요청하는 대신 실행 가능한 설정 안내를 제공하도록 하는 [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3)을 출시했고; Nostr 기반의 비공개 암호화 노트 및 파일 앱인 [Manent](https://github.com/dtonon/manent)는 Amber가 16진수 pubkey를 반환할 때 깨지던 Android 서명자 로그인을 수정하고 bunker 로그인 스크롤을 개선한 [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1)을 출시했으며; 슬림하고 Google 서비스가 없는 Nostr 클라이언트인 [NoorNote](https://github.com/77elements/noornote)는 놓치던 Nostrord 그룹 알림을 수정하고 자기 게시 알림 토글을 추가한 [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8)을 출시했고; AI 에이전트와 인간을 위한 신뢰 인식 Nostr MCP 서버인 [Bray](https://github.com/forgesworn/bray)는 [NIP-46](/ko/topics/nip-46/) bunker 연결 시 클라이언트 이름 메타데이터를 전송하는 [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0)을 출시했으며; Nostr 웹 클라이언트인 [Lumilumi](https://github.com/TsukemonoGit/lumilumi)는 오프라인 대체를 위해 [NIP-65](/ko/topics/nip-65/) relay 목록을 로컬 저장소에 캐시하고; Nostr 기반의 로컬 도시 및 커뮤니티 앱인 [Earthly](https://github.com/moogmodular/earthly)는 [NIP-50](/ko/topics/nip-50/) 지리 검색을 추가하며; 무료 오픈소스 Lightning 지갑 및 계정 시스템인 [lnbits](https://github.com/lnbits/lnbits)는 대체로 Lightning에 초점을 맞춘 릴리스 안에서 `send_nostr_dm`이 논블로킹으로 게시하도록 하는 [PR #3925](https://github.com/lnbits/lnbits/pull/3925)를 출시했습니다.

---

## 새로 추적 및 발견됨

### OpenDiscord v1.0.1이 Nostr 기반 Discord 스타일 클라이언트로 출시되다

[OpenDiscord](https://github.com/sofia-gros/open-discord)는 역할 기반 권한과 WebRTC/SFU 음성 로비를 갖춘 Nostr 기반 Discord 스타일 서버-채널 클라이언트입니다. [v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1)은 프로젝트의 첫 태그 설치 프로그램 릴리스입니다.

### Auditable Voting v0.1.140이 주최자, 투표자, 감사 프록시 역할을 정렬하다

[Auditable Voting](https://github.com/tidley/auditable-voting)은 클라이언트 전용 Nostr 투표 셸입니다. [v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140)은 주최자, 투표자, 감사 프록시 역할을 주최자가 서명한 정확한 공개 설문지 정의 이벤트와 정렬하여, 감사 프록시가 오래된 생성 계정이나 다른 워커 또는 주최자로부터 유지된 상태에 대해 작동할 수 있던 격차를 막습니다.

### Cambium v0.3.2가 Heartwood와 짝을 이루어 키 없는 NIP-55 서명자가 되다

[Cambium](https://github.com/forgesworn/cambium)은 이번 호의 Discovery 선정작입니다. 자체 개인 키 자료를 전혀 보관하지 않고, 모든 서명 요청을 [NIP-46](/ko/topics/nip-46/)을 통해 동반 Heartwood 하드웨어 서명자로 프록시하는 Android [NIP-55](/ko/topics/nip-55/) 서명자입니다. 이 프로젝트는 추적 프로젝트 Bray와 `forgesworn` GitHub 조직을 공유하며, Heartwood 자체는 Cambium의 Android 측이 이제 대화하는 relay-to-serial 서명 브리지를 출시한 것으로 #30에서 다뤄졌습니다. [v0.3.2](https://github.com/forgesworn/cambium)는 선택된 신원이 앱의 기존 바인딩과 다를 때 실시간으로 경고하도록 승인 시트를 다듬고, 활동 로그 쓰기를 단일 논블로킹 대기열로 옮깁니다.

### 이번 주 함께 출시됨: echoes, Dispatch, Linky

이번 주 언급할 만한 세 가지 출시가 더 있습니다. [echoes](https://github.com/Lwb89dev/echoes)는 Nostr를 통해 비공개로 동기화되는 오프라인 우선, 종단 간 암호화 노트 앱입니다. [Dispatch](https://github.com/freecritter/dispatch)는 모든 저장이 [NIP-44](/ko/topics/nip-44/)로 암호화되고 연결 불가능한 전용 키 아래 Nostr를 통해 백업되는 로컬 우선 여행 정리 도구이며, 그 [v0.3.0](https://github.com/freecritter/dispatch) 릴리스는 앱이 사용자의 개인 키를 직접 다루지 않도록 Amber [NIP-55](/ko/topics/nip-55/) 로그인을 추가합니다. [Linky](https://github.com/hynek-jina/linky)는 Nostr 연락처와 DM을 Lightning 및 Cashu 결제와 하나의 프로그레시브 웹 앱에 결합합니다.

---

## 프로토콜 작업 및 NIP 업데이트

지난 한 주 동안 [NIPs 저장소](https://github.com/nostr-protocol/nips)에 병합된 PR은 없습니다. 여섯 개의 제안이 열렸습니다.

### 열림: kind:10011 즐겨찾기 팔로우 세트

fiatjaf의 [PR #2413](https://github.com/nostr-protocol/nips/pull/2413)은 kind:10011 즐겨찾기 팔로우 세트를 추가합니다. 이는 kind:10012(즐겨찾기 relay 세트)가 kind:30002 relay 세트를 가리키는 `a` tag를 담는 기존 패턴을 반영하여, 같은 즐겨찾기 메커니즘을 kind:30000 팔로우 세트로 확장함으로써 클라이언트가 자신의 연락처 목록을 대체하지 않고도 큐레이션된 팔로우 목록을 북마크할 수 있게 합니다.

### 열림: NIP-4E를 확장하는 비공개 암호화 드라이브

Form* 팀의 [PR #2412](https://github.com/nostr-protocol/nips/pull/2412)는 `d` 식별자 tag와 `t` 하위 유형 tag로 구별되는 일반 Metadata 이벤트 kind 34578을 제안하며, 그 위에 구축된 비공개 암호화 파일 시스템도 함께 제안하는데, 이는 Form* 자체의 아직 실험적인 Form* Drive 클라이언트에 이미 구현되어 있습니다. 파일 레코드는 `t=files`인 Metadata 이벤트입니다. 파일 blob은 [Blossom](/ko/topics/blossom/) 서버에 있고 암호화된 인덱스만 relay에 있으며, 각 파일 청크는 [NIP-44](/ko/topics/nip-44/) v2 HKDF 파생 암호화가 적용된 자체 일회성 키페어를 갖습니다. 동반 Decoupled Encryption Key 이벤트는 모든 파일의 메타데이터가 그것에 대해 복호화되는 하나의 드라이브 전역 대칭 키를 보관하며, [NIP-4E](/ko/topics/nip-4e/), 즉 fiatjaf의 아직 열려 있는 저장소 추상화 초안([PR #1647](https://github.com/nostr-protocol/nips/pull/1647), 2024년 12월부터 열림) 위에 명시적으로 구축됩니다.

그 단일 드라이브 전역 키는 유출된 키 하나가 드라이브 내 단 하나가 아니라 모든 파일의 메타데이터를 노출한다는 것을 의미합니다. 파일별 일회성 키페어는 청크 암호화 키만 다르게 할 뿐 메타데이터 복호화 키는 바꾸지 않기 때문입니다. 아직은 오래된 이벤트가 손실될 수 있음을 경고하는 새 Metadata 이벤트를 게시하는 것 외에 순환이나 폐기 경로가 존재하지 않습니다. 더 좁은 두 번째 제안은 같은 기반 NIP-4E 아이디어에 다른 각도에서 접근합니다: fiatjaf의 [PR #2361](https://github.com/nostr-protocol/nips/pull/2361)은 [NIP-17](/ko/topics/nip-17/) 메시징에 한정하여 신원 키와 암호화 키를 분리하며, 6월 1일부터 열려 있습니다. 두 PR 모두 병합되지 않아, 이는 설계 공간의 활발하고 논쟁적인 영역으로 남아 있습니다. Form*는 Drive 클라이언트가 실험적이며 곧 업데이트가 있을 것이라고 말합니다.

### 열림: NIP-DA 권한 기반 비공개 데이터 공유

JAFairweather의 [PR #2411](https://github.com/nostr-protocol/nips/pull/2411)은 범위 지정 데이터 승인을 통한 권한 기반 비공개 데이터 공유를 위한 새 NIP-DA 초안입니다. 각 사용자는 범위별로 하나의 암호화된 권위 있는 레코드를 relay에 보관하며, 접근은 그 범위의 대칭 키를 [NIP-59](/ko/topics/nip-59/) gift wrap 안에서 비공개로 전달함으로써 부여되므로, relay는 암호문만 저장하고 누가 누구에게 접근을 부여했는지 결코 알지 못합니다. 폐기는 단순히 키 순환일 뿐이며, 모든 소비자의 사본을 다시 쓸 필요가 없습니다. 저자는 이를 [NIP-17](/ko/topics/nip-17/) DM(데이터 스냅샷은 담을 수 있지만 실시간 업데이트나 폐기는 담을 수 없음)과 NIP-51 비공개 목록(키 자료를 담지 않음)과는 구별되는 것으로 위치시키며, 두 개의 독립 구현, 즉 JavaScript 참조 라이브러리와 go-nostr 상의 Go CLI를 인용하고, relay.damus.io, nos.lol, relay.primal.net에 대해 교차 테스트했습니다.

### 열림: 스티커 팩 kind 10031과 30031

vincenzopalazzo의 [PR #2410](https://github.com/nostr-protocol/nips/pull/2410)은 Event Kinds 표에 kind 30031(주소 지정 가능 스티커 팩)과 kind 10031(사용자의 스티커 팩 목록)을 등록하며, [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec)가 이번 주 출시하는 "Sonar Stickers" 형식으로 명세됩니다. 이 kind들은 클라이언트가 스티커 팩을 이모지 세트로 착각할 수 없도록 [NIP-30](/ko/topics/nip-30/) 커스텀 이모지 kind 30030과 10030보다 의도적으로 한 칸 위에 자리합니다. 스티커 이미지 바이트는 HTTPS [Blossom](/ko/topics/blossom/) 호환 서버에 있으며, 전송된 스티커 참조는 평문 해시를 담아 편집된 주소 지정 가능 팩이 오래된 메시지에 이미 전송된 스티커의 모습을 조용히 바꿀 수 없도록 합니다. 동반 PR은 별도의 `registry-of-kinds` 프로젝트에 같은 kind들을 등록합니다.

### 열림: kind:9010과 kind:39005를 통한 NIP-29 메시지 고정

Anderson-Juhasc의 [PR #2379](https://github.com/nostr-protocol/nips/pull/2379)는 [NIP-29](/ko/topics/nip-29/) relay 기반 그룹에 메시지 고정을 추가합니다: kind:9010 `update-pin-list`는 고정된 이벤트 전체 목록을 표시 순서대로 `e` tag로 담는 모더레이션 이벤트여서, 단일 이벤트가 고정, 고정 해제, 재정렬, 또는 고정 집합 비우기를 할 수 있으며, kind:39005는 최신 승인된 목록을 노출하는 relay가 생성한 미러입니다. 이 설계는 검토 피드백 이후 [PR #1163](https://github.com/nostr-protocol/nips/pull/1163)의 앞선 추가/제거 쌍 방식을 대체하며, 9009와 39003이 그 이후 `create-invite`와 그룹 역할에 의해 사용되었기 때문에 kind 번호 9010/39005를 택합니다. Anderson-Juhasc는 또한 [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages)를 유지 관리하며, 그 [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0)이 바로 이번 주에 출시됩니다.

### 열림: NIP-66 relay 탐색 재구조화

VincenzoImp의 [PR #2241](https://github.com/nostr-protocol/nips/pull/2241)은 [NIP-66](/ko/topics/nip-66/) relay 탐색의 상당한 재구조화입니다. 느슨한 "Other tags include" 산문을 구조화된 Indexed Tags 섹션으로 대체하고, relay 탐색 필터링을 위해 NIP-11의 `attributes` 필드를 반영하는 `W` tag를 추가하며, 표준화된 네임스페이스(`ISO-639-1`, `ISO-3166-1`, `IANA-asn`, `IANA-tz`, `nip66.label.city`)를 사용하는 `l` 라벨 tag를 추가하고, RTT, SSL/TLS, 네트워크, 지리, DNS, HTTP tag를 새로운 Check Types 표와 함께 전용 섹션으로 정리합니다. 또한 필드 이름이 잘못되고 `kind`가 빠지고 검증 유형 이름이 유효하지 않던 깨진 예제 이벤트를 수정하고, [issue #2171](https://github.com/nostr-protocol/nips/issues/2171)을 종료합니다. 추가된 모든 tag가 선택 사항이므로 모든 변경은 하위 호환성을 유지합니다.

---

## NIP Deep Dive: NIP-99와 Gamma Markets 커머스 확장

원래의 Nostr 마켓플레이스 명세인 [NIP-15](/ko/topics/nip-15/)는 현시점에서 레거시입니다. 이는 판매자 부스(kind 30017)와 그 아래 정리된 상품(kind 30018)을 모델링했으며, 한때 그 위에서 돌아가던 클라이언트들, 그중 Shopstr는 이후 활성 명세인 [NIP-99](/ko/topics/nip-99/) 클래시파이드 리스팅으로 옮겨갔습니다. NIP-99 자체는 활성 리스팅용 kind 30402 또는 초안용 kind 30403인 단일 주소 지정 가능 이벤트이며, 먼저 부스를 만들 필요가 없습니다. 리스팅 이후의 모든 것은 정의하지 않은 채 둡니다: 배송비, 주문 상태, 영수증, 리뷰, 그리고 여러 리스팅을 하나의 상점 아래 묶는 방법 등, 정확히 NIP-15에서 결코 이전되지 않은 부분들입니다. [Gamma Markets](/ko/topics/gamma-markets/)는 그 공백을 채우며, 오늘날 이해할 가치가 있는 현대적인 커머스 계층입니다.

### NIP-99가 남겨둔 공백

NIP-99 리스팅의 `content` 필드는 Markdown 설명을 담고, `price`와 `location`은 이벤트에 직접 자리하며, `t` tag는 일반 해시태그 콘텐츠처럼 검색 가능하게 만듭니다. pubkey, kind, `d` tag 튜플로 주소 지정이 가능하기 때문에, 판매자는 같은 `d` tag로 새 버전을 게시함으로써 리스팅을 제자리에서 편집합니다:

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

그것이 명세 전부입니다: 서명되고 갱신 가능한 클래시파이드 광고. 일회성 클래시파이드를 넘어 실제 전자상거래를 위해 NIP-99를 구현하는 모든 클라이언트는 배송, 주문 메시지, 리뷰에 대한 자체 비공개 규약을 발명하게 되었습니다. 두 NIP-99 클라이언트가 각각 리스팅을 올바르게 렌더링하면서도 서로 간에 결제를 완료할 공유된 방법이 여전히 없을 수 있었습니다.

### Gamma Markets: NIP-99가 남겨둔 것을 표준화하기

Gamma Markets는 Nostr 마켓플레이스 개발자들의 작업 그룹, 즉 Shopstr, Cypher, Plebeian Market, Conduit Market을 만든 팀들이 NIP-99의 기존 kind 30402 이벤트 위에 구축한 공유 전자상거래 규약 집합에 붙인 이름입니다. 이 명세는 [PR #1784](https://github.com/nostr-protocol/nips/pull/1784)를 통해 표준 NIP-99 문서에서 링크되며, 자체 저장소 [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec)에서 유지 관리됩니다.

Gamma Markets는 두 개의 독립적인 리스팅 인접 kind를 추가합니다. Kind 30405는 여러 리스팅을 하나의 상품 컬렉션으로 묶으며, 명시적 `a` tag로 각각을 참조합니다:

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Kind 30406은 국가별 가격 책정과 선택적 무게 또는 거리 기반 비용 규칙을 갖춘 배송 옵션을 정의합니다:

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

주문 생성, 결제 요청, 상태 및 배송 업데이트, 결제 영수증은 모두 전송 방식을 다시 감싸는 대신, 역할별로 세 가지 kind로 나뉜 일반 [NIP-17](/ko/topics/nip-17/) gift-wrap된 비공개 메시지로 이동합니다: kind 14는 자유 형식의 구매자/판매자 통신을 담고, kind 16은 모든 주문 상태 전환을 담으며(`type` tag 1부터 4가 주문 생성, 결제 요청, 상태 업데이트, 배송 업데이트를 표시), kind 17은 구매자의 결제 영수증을 담습니다. 주문 생성 메시지는 gift-wrapping 전에 이렇게 생겼습니다:

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

완료된 구매를 평가하는 것은 별도의 주소 지정 가능 kind 31555이며, 리뷰하는 리스팅을 다시 가리킵니다:

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

주문 메시지를 NIP-17 위에 태우는 것은 Gamma Markets 체크아웃이 맞춤형 주문 메시지 kind 대신, 클라이언트가 이미 DM용으로 제공하는 것과 동일한 비공개 메시지 전송 방식을 사용한다는 것을 의미합니다.

이 명세의 핵심 설계 선택은 아무것도 계단식으로 상속되지 않는다는 것입니다. 컬렉션에 속한 리스팅은 컬렉션의 배송 옵션이나 설명을 자동으로 상속하는 대신 `a` tag로 명시적으로 참조하며, 리스팅이 사용하는 배송 옵션도 같은 명시적 방식으로 참조됩니다. 이는 상품이 상위 부스가 정의한 통화와 배송 표를 조용히 상속하던 NIP-15의 부스 모델을 의도적으로 뒤집은 것입니다. 절충은 모든 리스팅에서 더 명시적인 태깅을 요구하는 대신, 먼저 상위 객체를 해석할 필요 없이 리스팅의 전체 구성을 이벤트 자체에서 항상 읽을 수 있다는 것입니다.

### 이것이 실제로 나타나는 곳

이번 주 [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) 작업은 Gamma Markets가 표준화하는 것과 같은 주문 메시지 영역에 자리합니다: [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174)의 일회성 키 게스트 체크아웃과 [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175)의 판매자 주문함 재구축은 둘 다 Gamma Markets의 kind 14, 16, 17 메시지가 형식화하는 구매자/판매자 주문 상태 문제를 해결합니다. Conduit Mono는 그 kind들을 직접 채택하지 않고 그것들과 나란히 자체 주문 상태 모델을 운영합니다. 명세를 저술한 네 프로젝트 중 하나인 Shopstr도 지난 한 주 동안 자체 커머스 배관을 계속 움직였습니다: [PR #568](https://github.com/shopstr-eng/shopstr/pull/568)은 중복된 NIP-17 gift-wrap 로직을 공유 모듈로 추출하고, [PR #567](https://github.com/shopstr-eng/shopstr/pull/567)은 [NIP-98](/ko/topics/nip-98/) HTTP 인증 파서를 완전한 테스트 커버리지로 가져오는데, 이는 Gamma Markets 주문 흐름이 구매자와 판매자에게 안전하게 도달하기 위해 의존하는 바로 그 메시징 및 인증 계층에 대한 유지 관리입니다.

NIP-15는 부스와 상품을 표준화한 뒤 결제, 배송, 리뷰, 주문 상태를 애플리케이션 문제로 남겨둠으로써 상점 역할을 잃었습니다. Gamma Markets는 새 메시징 계층을 발명하는 대신 Nostr의 기존 DM 스택인 NIP-17 위에 구축하여, NIP-99의 단일 리스팅 형태를 건드리지 않고 그 빠진 표면의 대부분을 채웁니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 공유할 소식이 있으신가요? NIP-17 DM으로 연락하시거나 Nostr에서 저희를 찾아주세요.
