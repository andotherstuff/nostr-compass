---
title: 'Nostr Compass #17'
date: 2026-04-08
translationOf: /en/newsletters/2026-04-08-newsletter.md
translationDate: 2026-04-09
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [Amethyst](https://github.com/vitorpamplona/amethyst)가 Arti Tor 통합과 재설계된 Shorts UI가 포함된 [v1.08.0](#amethyst-ships-arti-tor-merges-pure-kotlin-mls-and-marmot)을 출시했고, [Quartz](/ko/topics/quartz/) 라이브러리에 [MLS](/ko/topics/mls/)와 [Marmot](/ko/topics/marmot/)의 순수 Kotlin 구현을 병합했습니다. [Nostur](https://github.com/nostur-com/nostur-ios-public)는 동영상 녹화, 애니메이션 GIF 프로필, 비공개 답글이 포함된 [v1.27.0](#nostur-v1270-adds-video-recording-and-private-replies)을 출시했습니다. [Shosho](https://github.com/r0d8lsh0p/shosho-releases)는 Shows(OBS와 연결되는 맞춤형 라이브 스트림 정보)와 TikTok 스타일의 세로 동영상 캐러셀이 포함된 [v0.15.0](#shosho-v0150-launches-shows-and-vertical-video-carousel)을 공개했습니다. [Nymchat](https://github.com/Spl0itable/NYM)는 회전하는 일회용 키를 사용하는 향상된 [NIP-17](/ko/topics/nip-17/) 그룹 채팅과 함께 [Marmot 되돌리기 릴리스](#nymchat-reverts-marmot-ships-enhanced-nip-17-group-chats)를 내놓았습니다. [Nostr VPN](https://github.com/mmalmi/nostr-vpn)은 여섯 개 릴리스에 걸쳐 [exit node 지원과 Umbrel 패키징](#nostr-vpn-ships-exit-node-support-and-umbrel-packaging)을 추가했습니다. [Amber](https://github.com/greenart7c3/Amber)는 연결별 [NIP-46](/ko/topics/nip-46/) 서명 키와 Zapstore 인앱 업데이트가 포함된 [v6.0.0-pre1](#amber-v600-pre1-adds-per-connection-nip-46-signing-keys)로 올라섰습니다. [Notedeck](https://github.com/damus-io/notedeck)는 Zapstore를 통한 APK 자체 업데이트가 포함된 [v0.10.0-beta](#notedeck-v0100-beta-ships-zapstore-self-update)에 도달했고, [NIP-58](/ko/topics/nip-58/) (Badges)은 [kind 마이그레이션](#nip-updates)을 받았습니다. 이번 주 NIP 심층 분석은 [NIP-17](/ko/topics/nip-17/) (Private Direct Messages)과 [NIP-46](/ko/topics/nip-46/) (Nostr Remote Signing)을 다룹니다.

## Top Stories

### Amethyst ships Arti Tor, merges pure Kotlin MLS and Marmot

vitorpamplona가 유지 관리하는 Android 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)는 [v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3)부터 [v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0)까지 네 개의 릴리스를 배포했고, 아직 릴리스되지 않은 대규모 작업 묶음을 [Quartz](/ko/topics/quartz/) 라이브러리(공유 Kotlin Multiplatform Nostr 모듈)에 병합했습니다. 핵심 릴리스는 v1.08.0 "Arti Tor"로, 앱의 Tor 연결을 C 기반 Tor 라이브러리에서 Tor Project의 Rust 구현인 [Arti](https://gitlab.torproject.org/tpo/core/arti)로 옮깁니다. 이 전환은 이전 C Tor 바인딩에서 발생하던 무작위 충돌을 해결합니다. Arti는 메모리 안전성과 async I/O를 위해 Rust로 처음부터 다시 작성된 Tor Project의 장기적인 C 코드베이스 대체물입니다.

v1.07.3 릴리스는 Shorts UI를 재설계해 페이지 단위 디자인을 사진, 쇼츠, 긴 동영상을 위한 edge-to-edge 피드로 바꿨습니다. 같은 릴리스는 badges를 kind `10008`로, bookmarks를 kind `10003`으로 옮겨 이번 주 [병합된](#nip-updates) [NIP-58](/ko/topics/nip-58/) kind 마이그레이션과 맞췄습니다. v1.07.4는 Nostr Wallet Connect secret 처리 문제를 수정했고, v1.07.5는 이미지 업로드 충돌을 수정했습니다.

아직 태그된 릴리스에는 포함되지 않았지만 main에는 이미 들어간 작업으로, 팀은 [MLS](/ko/topics/mls/)와 [Marmot](/ko/topics/marmot/) 프로토콜 모두의 전체 Kotlin 구현을 작성해 네이티브 C/Rust 라이브러리 바인딩이 더 이상 필요 없게 만들었습니다. [PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147)은 핵심 Marmot MLS 그룹 메시징 계층을 추가하고, [PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149)는 그룹 채팅 UI를 추가하며, [PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146)은 구독 관리자와 함께 수신 및 발신 메시지 프로세서를 추가합니다. [PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141)은 MLS 그룹 상태 영속화와 KeyPackage rotation 관리를 추가하고, [PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150)은 향상된 GroupInfo signing과 함께 전체 MLS 테스트 스위트를 추가하며, [PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158)은 KeyPackage publication status 추적을 더합니다. [PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166)은 Nostr 암호화 연산을 위한 순수 Kotlin secp256k1 구현을 추가해 네이티브 C 라이브러리 의존성을 대체합니다. Kotlin MLS 구현까지 더해지면서 [Quartz](/ko/topics/quartz/)는 네이티브 바인딩 없이도 Nostr signing과 Marmot 그룹 메시징을 수행할 수 있게 되었고, 이는 iOS를 포함한 Kotlin Multiplatform 타깃으로 나아갈 길을 엽니다.

팀은 또한 [NIP-AC](/en/topics/nip-ac/) (P2P Voice and Video Calls) 지원도 구축하고 있습니다. [PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)은 NIP-AC call state machine에 대한 전체 테스트 스위트를 추가하고, [PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)는 앱 재시작 후 오래된 call offer가 다시 트리거되는 일을 막습니다.

### Nostur v1.27.0 adds video recording and private replies

iOS Nostr 클라이언트 [Nostur](https://github.com/nostur-com/nostur-ios-public)는 4월 2일 [v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0)을 출시했습니다. 이 릴리스는 업로드 전 잘라내기가 가능한 인앱 동영상 녹화를 추가해, 사용자가 짧은 영상을 촬영하고 길이를 조정한 뒤 클라이언트를 벗어나지 않고 게시할 수 있게 합니다. 애니메이션 GIF 지원은 프로필 사진과 배너 사진까지 확장되며, animated WebP 렌더링도 추가됐습니다. 새로운 Shortcuts 통합을 통해 사용자는 Apple Shortcuts 자동화에서 Nostr 게시물을 보낼 수 있습니다. 이번 릴리스는 또한 비공개 답글을 추가했고, Nostur와 다른 클라이언트 사이의 메시지 전달에 영향을 주던 DM 호환성 문제도 수정했습니다.

### Shosho v0.15.0 launches Shows and vertical video carousel

Nostr 라이브 스트리밍 앱 [Shosho](https://github.com/r0d8lsh0p/shosho-releases)는 4월 7일 [v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0)과 [v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1)을 출시했습니다. 핵심 기능은 Shows입니다. 스트리머는 라이브를 시작하기 전에 맞춤형 쇼 정보를 설정하고, 자신의 쇼를 OBS나 다른 외부 인코더에 연결할 수 있습니다. 이렇게 하면 "무엇을 스트리밍하는가"라는 메타데이터를 실제 라이브 시작 행위와 분리할 수 있어, 방송 전에 제목, 설명, 상품을 미리 준비할 수 있습니다. 같은 릴리스는 라이브, 클립, 리플레이를 전체 화면 피드에서 스와이프해 넘기는 TikTok 스타일의 세로 동영상 캐러셀과, 프로필 페이지에서 바로 동영상 클립 게시와 상품 추가를 할 수 있는 Quick Add도 포함합니다. v0.15.1은 키보드가 라이브 스트림 채팅 입력창을 가리던 버그를 수정합니다.

## Shipping This Week

### Notedeck v0.10.0-beta ships Zapstore self-update

Damus 팀의 데스크톱 및 모바일 클라이언트 [Notedeck](https://github.com/damus-io/notedeck)는 APK 자체 업데이트를 시험하기 위한 테스트 프리릴리스로 [v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1)과 [v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2)를 배포했습니다. [PR #1417](https://github.com/damus-io/notedeck/pull/1417)은 Android에서 Nostr/Zapstore 업데이터를 통한 APK 자체 업데이트를 추가하며, 이는 [뉴스레터 #14의 Nostr 네이티브 업데이트 탐색 작업](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr)을 바탕으로 합니다. 이 업데이트 흐름은 relay에 게시된 Nostr 이벤트를 통해 새 릴리스를 발견하고, 개발자가 호스팅하는 위치(GitHub releases, Blossom CDN, 그 밖의 소스)에서 APK를 다운로드한 뒤, 서명된 Nostr 이벤트와 SHA-256 해시를 대조해 검증하고 설치합니다. [PR #1438](https://github.com/damus-io/notedeck/pull/1438)은 Login과 CreateAccount 버튼이 즉시 뒤로 이동해 버리던 welcome screen 버그를 수정하고, [PR #1424](https://github.com/damus-io/notedeck/pull/1424)은 Agentium AI session view의 텍스트 overflow를 수정합니다.

### Amber v6.0.0-pre1 adds per-connection NIP-46 signing keys

[Amber](https://github.com/greenart7c3/Amber)는 [NIP-55](/ko/topics/nip-55/) (Android Signer Application) signer 앱으로, 4월 4일 [v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1)을 출시했습니다. 가장 중요한 변화는 [NIP-46](/ko/topics/nip-46/) (Nostr Remote Signing) bunker 프로토콜을 위한 연결별 서명 키입니다. Amber는 이제 모든 bunker 연결에 단일 키페어를 쓰는 대신, 연결된 각 클라이언트마다 별도의 키를 생성합니다. 한 클라이언트 연결이 손상되더라도 공격자는 다른 클라이언트에 대해 signer를 사칭할 수 없습니다.

[PR #377](https://github.com/greenart7c3/Amber/pull/377)은 Zapstore를 통한 인앱 업데이트 확인 및 설치를 추가해, [Notedeck](#notedeck-v0100-beta-ships-zapstore-self-update)과 함께 Nostr 네이티브 앱 배포를 채택합니다. [PR #375](https://github.com/greenart7c3/Amber/pull/375)는 AndroidKeyStore 실패 시 충돌 대신 사용자에게 경고를 표시하도록 처리하고, [PR #371](https://github.com/greenart7c3/Amber/pull/371)은 무제한 저장소 증가를 막기 위해 크기 제한과 콘텐츠 잘라내기가 포함된 데이터베이스 정리를 추가합니다. 이 프리릴리스에는 [지난주 v5.0.x 주기에서 다룬](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504) [NIP-42](/ko/topics/nip-42/) relay auth 화이트리스트와 mnemonic recovery phrase 로그인도 포함되어 있습니다.

### Nostria ships native mobile app

SondreB가 유지 관리하는 크로스 플랫폼 Nostr 클라이언트 [Nostria](https://github.com/nostria-app/nostria)는 Android용 네이티브 모바일 앱을 출시했고, [v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11)부터 [v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18)까지 여덟 개의 릴리스를 배포했습니다. 가장 중요한 새 기능은 [Amber](https://github.com/greenart7c3/Amber)와 Aegis 같은 signer를 위한 네이티브 로컬 signer 지원입니다. Linux, macOS, Windows용 [데스크톱 설치 파일](https://www.nostria.app/download)도 함께 제공됩니다. [PR #610](https://github.com/nostria-app/nostria/pull/610)은 적응형 런타임 제한과 preview URL 정리를 통해 피드 메모리 압박을 줄입니다. v3.1.14는 [Web of Trust](/ko/topics/web-of-trust/) provider인 Brainstorm과의 통합을 수정합니다. v3.1.15는 음악 관련 개선에 집중합니다. 새 Android 앱은 [Zapstore](https://zapstore.dev/apps/app.nostria)에서 받을 수 있습니다.

### diVine 1.0.8 ships resumable uploads and DMs

짧은 형식의 동영상 클라이언트 [diVine](https://github.com/divinevideo/divine-mobile)는 87개의 병합된 PR과 함께 [1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8)을 출시했습니다. resumable upload를 통해 제작자는 불안정한 연결에서 업로드가 끊겨도 처음부터 다시 시작하지 않고 청크 단위로 이어서 올릴 수 있습니다. 이 릴리스는 동영상 품질 및 bitrate 설정, double-tap 좋아요, DM 개선도 추가합니다. [PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722)는 데스크톱 동영상 캡처를 위한 macOS 카메라 플러그인을 추가하고, [PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820)은 알림 시스템을 enrichment와 grouping이 포함된 BLoC 아키텍처로 옮깁니다. 팀은 또한 AI 생성 스티커와 카테고리 아트를 OpenMoji SVG로 교체했습니다([PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844), [PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)).

### Manent v1.3.0 adds sensitive note blurring and NIP-42 auth

개인 암호화 노트 및 파일 저장 앱 [Manent](https://github.com/dtonon/manent)는 4월 2일 [v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0)을 출시했습니다. 이제 사용자는 노트를 민감한 항목으로 표시해 목록 보기에서 흐리게 처리할 수 있어, 가볍게 스크롤할 때 사적인 내용을 가릴 수 있습니다. 이번 릴리스는 또한 [NIP-42](/ko/topics/nip-42/) (Authentication of Clients to Relays) 지원을 추가해, 이벤트를 받기 전에 인증을 요구하는 relay에 Manent가 인증할 수 있게 합니다. Manent는 모든 데이터를 사용자의 키페어를 사용해 Nostr relay에 암호화 저장하므로, NIP-42 지원은 저장에 활용할 수 있는 relay 집합을 넓혀 줍니다.

### Wisp v0.17.0 through v0.17.3 add live stream zaps and wallet backup

Android Nostr 클라이언트 [Wisp](https://github.com/barrydeen/wisp)는 [v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta)부터 [v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta)까지 여섯 개의 릴리스를 배포했고, 44개의 PR을 병합했습니다. v0.17.0은 지갑 백업 안전 프롬프트와 zap UX 개선을 추가합니다. [v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta)은 플랫폼 전반에서 라이브 스트림 채팅 가시성과 라이브 스트림 zap 기능을 더합니다. [PR #423](https://github.com/barrydeen/wisp/pull/423)은 프로필 자동 검색, zap 성공 애니메이션, 사용자 상태 개선을 추가합니다. [PR #426](https://github.com/barrydeen/wisp/pull/426)은 큰 태그 목록이 있는 이벤트에서 `computeId`가 out-of-memory로 충돌하던 문제를 수정합니다. v0.16.x 릴리스는 emoji shortcode 자동완성, 그룹 채팅 UI 개선, 모든 알림 경로에 걸친 차단 사용자 필터링을 추가했습니다.

### Mostro ships deep links, Nostr exchange rates, and a duplicate payment fix

Nostr 위에 구축된 P2P Bitcoin 거래소 [Mostro](https://github.com/MostroP2P/mostro)는 이번 주 서버 데몬과 모바일 클라이언트 양쪽에서 업데이트가 있었습니다. 서버 측에서는 [PR #692](https://github.com/MostroP2P/mostro/pull/692)가 오래된 주문 쓰기로 인해 중복 결제가 발생하는 문제를 막아, 판매자가 같은 거래에 대해 두 번 지급받을 수 있는 버그를 차단합니다. [PR #693](https://github.com/MostroP2P/mostro/pull/693)은 전체 주문 덮어쓰기 대신 dev_fee 쓰기에 표적화된 업데이트를 사용합니다.

Flutter 클라이언트 [Mostro Mobile](https://github.com/MostroP2P/mobile)은 4월 3일 [v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3)을 출시했습니다. 이 릴리스는 서로 다른 Mostro 인스턴스에서 오는 딥 링크를 처리해, 사용자가 올바른 거래 서버로 연결되는 링크를 탭할 수 있게 합니다. [PR #498](https://github.com/MostroP2P/mobile/pull/498)은 백그라운드 알림 파이프라인에서 admin 및 dispute DM을 감지하고, 앱은 이제 HTTP/cache fallback과 함께 Nostr에서 환율을 가져옵니다. [PR #560](https://github.com/MostroP2P/mobile/pull/560)은 특정 네트워크 조건에서 앱이 relay에 도달하지 못하게 하던 relay 연결 차단 버그를 수정합니다.

### Unfiltered v1.0.12 adds hashtags and comments

이미지 중심 콘텐츠에 초점을 맞춘 Nostr 클라이언트 [Unfiltered](https://github.com/dmcarrington/unfiltered)는 [v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12)를 출시했습니다. [PR #69](https://github.com/dmcarrington/unfiltered/pull/69)는 hashtag 지원을 추가하고, [PR #72](https://github.com/dmcarrington/unfiltered/pull/72)는 게시물에 댓글을 작성하고 표시하는 기능을 추가합니다. [PR #71](https://github.com/dmcarrington/unfiltered/pull/71)은 게시물당 여러 이미지를 다룰 때의 내비게이션 문제를 수정합니다.

### Primal Android ships wallet multi-account sharing and remote signer auto-reconnect

Android Nostr 클라이언트 [Primal](https://github.com/PrimalHQ/primal-android-app)은 4월 7일 릴리스를 배포했습니다. 이번 업데이트는 지갑 다중 계정 공유와 Dev Tools의 지갑 삭제가 포함된 overflow menu를 추가합니다. remote signer는 이제 연결이 끊기면 자동으로 다시 연결되며, 지갑 서비스도 자체 auto-reconnect 로직을 갖게 됐습니다. 수정 사항에는 poll zap 투표가 더 이상 Top Zaps로 나타나지 않는 문제, 빈 poll option 충돌 방지, 지갑이 없을 때 wallet balance 숨김, NWC 응답에서 WalletException 타입을 에러 코드에 매핑하는 작업이 포함됩니다.

### Titan v0.1.0 launches native nsite:// browser with Bitcoin name registration

Nostr 웹을 위한 네이티브 데스크톱 브라우저 [Titan](https://github.com/btcjt/titan)은 4월 7일 [v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0)을 출시했습니다. Titan은 Bitcoin에 등록된 사람이 읽을 수 있는 이름을 조회해 `nsite://` URL을 해석하고, 사이트의 콘텐츠 이벤트를 얻기 위해 Nostr relay를 질의하며, [Blossom](/ko/topics/blossom/) 서버에서 가져온 페이지를 렌더링합니다. 결과적으로 DNS도, TLS 인증서도, 호스팅 제공자도 없는 웹 브라우징 경험이 만들어집니다. 이름은 Bitcoin 거래와 연결된 [웹 인터페이스](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register)를 통해 등록됩니다. 초기 릴리스는 macOS `.dmg`(ARM, Intel용 Rosetta 2 지원)로 배포되며, Nix 개발 환경 지원도 포함합니다.

### Bikel v1.5.0 ships native foreground service for de-Googled phones

주행 기록을 Nostr를 통해 공공 인프라 데이터로 바꾸는 탈중앙화 사이클링 트래커 [Bikel](https://github.com/Mnpezz/bikel)은 4월 4일 [v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0)을 출시했습니다. 이 릴리스는 GMS 의존 Expo TaskManager에서 커스텀 네이티브 foreground service로 전환해, LineageOS, GrapheneOS, 그 밖의 de-Googled Android 변형에서 안정적인 백그라운드 주행 추적을 보장합니다. Bikel Bot은 Cashu nutzaps를 통한 자율 eCash 수집이 가능한 dual-pocket 아키텍처를 갖추게 됐습니다. v1.4.3과 v1.4.2는 비표준 Android 환경에서의 백그라운드 추적 동기화를 수정하고, 앱은 OSM 자전거 거치대 지도 포인트 토글도 추가합니다.

### Sprout adds NIP-01, NIP-23, and NIP-33 support

내장 Nostr relay를 갖춘 Block의 커뮤니케이션 플랫폼 [Sprout](https://github.com/block/sprout)은 4월 6일 [desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7)을 출시했습니다. 이번 주 팀은 [NIP-23](/en/topics/nip-23/) (Long-form Content) kind `30023` article, `d` 태그 기반 교체를 사용하는 [NIP-33](/en/topics/nip-33/) parameterized replaceable event, 그리고 [NIP-01](/ko/topics/nip-01/)/[NIP-02](/en/topics/nip-02/) kind `1` text note와 kind `3` follow list 지원을 추가했습니다. 이번 릴리스는 54개 테마를 갖춘 적응형 IDE 테마 시스템, workflow 및 agent run history UX 개선, members sidebar 정리도 포함합니다.

### mesh-llm v0.56.0 ships distributed config protocol

노드 신원에 Nostr 키페어를 사용하는 분산 LLM 추론 시스템 [mesh-llm](https://github.com/michaelneale/mesh-llm)은 4월 7일 [v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0)을 출시했습니다. 이 릴리스는 ownership semantics가 포함된 분산 config 프로토콜, 메모리 사용량을 줄이기 위한 비대칭 KV cache 양자화(Q8_0 keys와 Q4 values), identity keystore를 위한 OS keychain 저장, 메시지 queue를 이용한 부드러운 chat streaming, fullscreen layout과 flash attention 기반 KV cache splitting 수정 사항을 추가합니다.

### Nostr VPN ships exit node support and Umbrel packaging

신호에는 Nostr relay를 사용하고 암호화 터널에는 WireGuard를 사용하는 P2P VPN [Nostr VPN](https://github.com/mmalmi/nostr-vpn)은 이번 주 [v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0)부터 [v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6)까지 여섯 개의 릴리스를 배포했습니다. v0.3.x 주기는 Windows와 macOS에서 exit node 지원을 추가해, 피어가 네트워크 안의 다른 노드를 통해 인터넷 트래픽을 라우팅할 수 있게 합니다. invite와 alias 전파도 이제 Nostr를 통해 동기화되므로, 사용자는 별도의 바깥 채널 조율 없이 네트워크 접근 권한을 공유할 수 있습니다. 이번 릴리스들은 self-hosted 배포를 위한 Umbrel 패키징, 기억된 public endpoint를 이용한 NAT punch-through, 오래된 exit node 자동 정리, 공개된 프로토콜 사양도 추가합니다. 프로젝트는 또한 self-healing default route와 underlay repair를 통해 macOS route 처리를 안정화했고, Tauri 기반 Android 빌드도 추가했습니다. 빌드는 macOS(Apple Silicon 및 Intel), Linux(AppImage 및 .deb), Windows, Android에서 제공됩니다.

### Nymchat reverts Marmot, ships enhanced NIP-17 group chats

MLS 지원 채팅 클라이언트 [Nymchat](https://github.com/Spl0itable/NYM)은 [v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261)부터 [v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274)까지 14개의 릴리스를 배포했습니다. 가장 중요한 변화는 프로토콜 방향 전환입니다. [v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261)은 Marmot MLS 그룹 채팅을 추가했지만, [v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268)은 Marmot의 다중 장치 지원이 아직 완성되지 않아 장치 간 그룹 채팅 상태 동기화에 문제가 생기면서 다시 [NIP-17](/ko/topics/nip-17/)으로 되돌렸습니다. v3.58.271은 모든 메시지에 대해 회전하는 일회용 키를 사용하는 향상된 NIP-17 그룹 채팅을 도입해, timing 및 correlation 공격을 막도록 설계됐습니다. 이번 주에는 세밀한 설정 제어가 가능한 친구 시스템([v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)), 암호화된 앱 설정 속 MLS 그룹 채팅 메시지 동기화, 여러 relay 연결성 수정도 포함됐습니다.

### nak v0.19.5 adds Blossom multi-server and outbox publishing

fiatjaf의 커맨드라인 Nostr 도구킷 [nak](https://github.com/fiatjaf/nak)은 [v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5)를 출시했습니다. `blossom` 명령은 이제 여러 [Blossom](/ko/topics/blossom/) 서버에 한 번에 업로드할 수 있도록 다중 `--server` 플래그를 받습니다. 새 `key` 명령은 부분 키를 왼쪽에 0을 채워 확장합니다. `event` 명령은 outbox model을 통해 이벤트를 게시하는 `--outbox` 플래그를 얻었고, `fetch`는 이벤트가 반환되지 않을 때 에러 코드와 함께 종료합니다.

## In Development

### White Noise adds thumbhash previews and push registration bridge

[Marmot](/ko/topics/marmot/) 프로토콜 위에 구축된 개인 메신저 [White Noise](https://github.com/marmot-protocol/whitenoise)는 다섯 개의 PR을 병합했습니다. [PR #549](https://github.com/marmot-protocol/whitenoise/pull/549)는 blurhash 이미지 미리보기를 더 작은 payload 크기로 더 선명한 placeholder 이미지를 생성하는 최신 알고리즘 thumbhash로 교체합니다(보통 blurhash의 약 50-100 bytes에 비해 30 bytes 이하). 이 알고리즘은 원본의 종횡비와 색 분포를 유지합니다. 오래된 콘텐츠를 위해 blurhash는 fallback으로 남겨 둡니다. [PR #548](https://github.com/marmot-protocol/whitenoise/pull/548)은 whitenoise-rs를 업데이트하고 [MIP-05](/ko/topics/mip-05/) push registration bridge를 추가해, [지난주 다룬 push notification spec 작업](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications)을 클라이언트와 연결합니다. [PR #493](https://github.com/marmot-protocol/whitenoise/pull/493)은 채팅 메시지에 cursor 기반 pagination을 추가해, 이전 로딩 전략을 스크롤 기반 접근으로 교체합니다.

### Route96 adds dynamic label configuration and zero-egress cleanup

v0l의 [Blossom](/ko/topics/blossom/) 미디어 서버 [Route96](https://github.com/v0l/route96)는 세 개의 PR을 병합했습니다. [PR #80](https://github.com/v0l/route96/pull/80)은 admin API를 통한 동적 label model 설정을 추가해, 운영자가 서버를 재시작하지 않고도 콘텐츠 분류 모델을 교체할 수 있게 합니다. [PR #82](https://github.com/v0l/route96/pull/82)는 admin UI에 label configuration 필드를 추가합니다. [PR #79](https://github.com/v0l/route96/pull/79)는 한 번도 다운로드되지 않은 파일을 자동으로 제거하는 zero-egress file cleanup 정책을 추가해, 운영자의 저장 비용을 낮춥니다.

### Snort ships security hardening and DVM payment invoices

웹 클라이언트 [Snort](https://github.com/v0l/snort)는 이번 주 포괄적인 보안 감사와 함께 두 개의 릴리스를 배포했습니다. 수정 사항에는 Schnorr signature 검증, [NIP-46](/ko/topics/nip-46/) relay message forgery 방지(손상된 relay를 통해 공격자가 signing request를 주입하는 것을 막음), PIN 암호화 개선, NIP-26 delegation 신뢰 제거가 포함됩니다. 성능 개선은 WASM에서의 batched Schnorr verification, lazy-loaded route, 사전 컴파일된 번역, 이벤트당 이중 검증 제거에서 나옵니다. [PR #618](https://github.com/v0l/snort/pull/618)은 [NIP-90](/en/topics/nip-90/) (Data Vending Machine) kind `7000` payment-required invoice 표시를 추가해, DVM이 결제 요구와 함께 응답할 때 Snort가 Lightning invoice를 피드에 직접 렌더링하게 합니다.

### Damus improves LMDB compaction

iOS 클라이언트 [Damus](https://github.com/damus-io/damus)는 [PR #3719](https://github.com/damus-io/damus/pull/3719)를 병합해 일정에 따라 자동 LMDB compaction을 수행하도록 했고, 로컬 데이터베이스가 시간이 지나며 무제한으로 커지는 일을 막습니다. [PR #3663](https://github.com/damus-io/damus/pull/3663)는 BlurOverlayView가 고장난 것처럼 보이지 않고 보호 기능처럼 보이도록 개선합니다.

### Captain's Log adds tag indexing and note sync

Nodetec의 Nostr 네이티브 장문 글쓰기 도구 [Captain's Log](https://github.com/nodetec/captains-log) (Comet)는 이번 주 네 개의 PR을 병합했습니다. [PR #156](https://github.com/nodetec/captains-log/pull/156)은 노트 전반에 걸친 태그 인덱싱과 sync 지원을 추가하고, [PR #157](https://github.com/nodetec/captains-log/pull/157)은 노트 sync와 태그 처리를 리팩터링하며, [PR #159](https://github.com/nodetec/captains-log/pull/159)은 휴지통으로 보낸 노트 sync를 수정해 삭제된 노트가 장치 간에도 삭제 상태를 유지하게 합니다.

### Relatr v0.2.x redesigns plugin system with Nostr-native validator marketplace

[Relatr](https://github.com/ContextVM/relatr)는 [Web of Trust](/ko/topics/web-of-trust/) 점수 엔진으로, 사회적 그래프 거리와 설정 가능한 validator를 바탕으로 신뢰 순위를 계산합니다. 이번 주 v0.2.x 계열을 배포하며 플러그인 시스템을 전면 재설계했습니다. validator는 이제 다단계 host orchestration capability(Nostr query, social graph lookup, NIP-05 resolution)를 지원하도록 포크된 휴대용 함수형 표현 언어 Elo로 작성됩니다. 플러그인은 kind `765` Nostr 이벤트로 게시되므로, 배포 자체가 relay 네트워크에 네이티브하게 올라갑니다. 새 [plugin marketplace](https://relatr.net)는 운영자가 브라우저에서 validator를 발견하고, 설치하고, 가중치를 설정할 수 있게 하며, 로컬 작성과 게시를 위한 CLI(`relo`)도 제공합니다. 이 아키텍처는 sandboxed되어 있어, 플러그인은 host가 명시적으로 제공한 capability만 호출할 수 있으므로 악성 validator가 정의된 범위를 벗어날 수 없습니다. 이제 Relatr 인스턴스는 웹사이트에서 관리할 수 있고, 어떤 플러그인이 점수 알고리즘을 구성하는지와 각 가중치를 완전히 볼 수 있습니다.

### Shopstr improves mobile navigation and access control

Bitcoin으로 사고파는 Nostr 네이티브 마켓플레이스 [Shopstr](https://github.com/shopstr-eng/shopstr)는 이번 주 메인 앱과 동반 프로젝트 [Milk Market](https://github.com/shopstr-eng/milk-market) 전반에 걸쳐 158개의 커밋을 푸시했습니다. 수정 사항에는 모바일 community 레이아웃 개선, 내비게이션 시 메뉴 자동 닫기 동작, dropdown 자동 닫기가 포함됩니다. 보호된 route는 이제 로그인하지 않고 직접 URL로 접근할 수 없으며, slug 매칭 로직은 여러 개의 정확 일치 항목도 올바르게 처리합니다.

### Pollerama adds notifications, movie search, and rating UI

Nostr 기반 polling, survey, social rating 앱 [Pollerama](https://github.com/formstr-hq/nostr-polls)는 thread 알림, 영화 검색 기능, rating UI 전면 개편을 추가했습니다. 이번 릴리스는 피드 로딩 문제를 수정하고 의존성 버전도 올립니다.

### Purser builds Nostr-native payment daemon with Marmot encryption

[Purser](https://github.com/EthnTuttle/purser)는 Zaprite 대체를 목표로 하는 Nostr 네이티브 payment daemon으로, 이번 주 아홉 개의 PR을 병합하며 핵심 아키텍처를 구축했습니다. 이 프로젝트는 판매자와 고객 간 암호화 메시징을 위해 MDK를 통한 [Marmot](/ko/topics/marmot/) MLS를 사용하고, 결제 제공자로 Strike와 Square를 사용합니다. 이번 주에는 config와 catalog 로딩, message schema 검증, MDK communication layer, Strike 및 Square provider 구현, polling engine, anti-spam rate limiting, pending payment 영속화, order processing pipeline이 들어왔습니다. 팀이 local mode에서 mock MLS를 제거하고 실제 암호화를 사용하도록 바꾸면서, 이제 99개 테스트 전체가 실제 mdk-core MLS 동작을 실행합니다.

### Vector refactors DM attachments and adds profile editing

Tauri로 구축된 privacy 중심 Nostr 메신저 [Vector](https://github.com/VectorPrivacy/Vector)는 프론트엔드를 리팩터링하는 [PR #55](https://github.com/VectorPrivacy/Vector/pull/55)를 병합했습니다. DM 첨부파일 복호화와 저장은 vector-core 라이브러리로 이동했고, 앱은 이제 프로필 편집도 지원합니다. 업로드 취소 플래그는 TauriSendCallback을 통해 제대로 연결됐고, 사용되지 않던 첨부파일 미리보기 callback도 정리됐습니다.

## Protocol and Spec Work

### NIP Updates

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**Merged:**

- **[NIP-58](/ko/topics/nip-58/) (Badges): Profile Badges move to kind 10008, Badge Sets to kind 30008** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Profile Badges를 kind `30008`에서 kind `10008`로 옮기고(pubkey당 하나의 replaceable event), Badge Sets를 위한 kind `30008`을 도입합니다. 이전에는 Profile Badges가 Badge 정의와 같은 kind(`30008`)를 사용해 `d` 태그로 키가 정해지는 parameterized replaceable event였습니다. 새 kind `10008`은 단순한 replaceable event로, pubkey당 하나이며 `d` 태그가 필요 없습니다. 클라이언트는 이제 사용자당 하나의 replaceable event만 질의하면 되고, parameterized replaceable event를 스캔할 필요가 없습니다. Amethyst v1.07.3은 이미 이 마이그레이션을 포함하고 있습니다.

- **[NIP-34](/ko/topics/nip-34/) (Git Stuff): Add git-related follow lists** ([PR #2130](https://github.com/nostr-protocol/nips/pull/2130)): NIP-34 저장소 및 issue 추적을 위한 follow list 규약을 추가합니다. 사용자는 `git-repos`나 `git-issues` 같은 `d` 태그를 가진 kind `30000` follow set을 게시하고, 안에는 추적하려는 저장소(kind `30617`)를 가리키는 `a` 태그 참조를 담습니다. 클라이언트는 이 follow set을 구독해, kind `3` contact list가 pubkey에 대해 동작하는 것과 비슷하게 사용자의 피드에 저장소 활동을 보여줄 수 있습니다.

**Open PRs and Discussions:**

- **NIP-AC: P2P Voice and Video Calls over WebRTC** ([PR #2301](https://github.com/nostr-protocol/nips/pull/2301)): 원래의 NIP-100(0xChat이 구현함)을 세 가지 방식으로 확장합니다. 첫째, 메타데이터 누출을 없애기 위해 [NIP-59](/ko/topics/nip-59/) gift wrap으로 감싼 [NIP-44](/ko/topics/nip-44/) 암호화로 이동합니다. 둘째, 음성 및 영상 통화 설정을 위한 WebRTC 워크플로(offer, answer, ICE candidate)를 명시합니다. 셋째, 각 피어가 다른 모든 피어와 직접 WebRTC 연결을 맺는 mesh 그룹 통화 모델을 정의합니다. 이 사양은 NIP-100과 하위 호환되지 않습니다. Amethyst는 이미 이에 맞춰 개발 중이며, call state machine 테스트 스위트([PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143))와 오래된 call offer 처리([PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164))가 이번 주에 반영됐습니다.

- **[NIP-340](/en/topics/nip-340/) (FROST Quorum)** ([PR #2299](https://github.com/nostr-protocol/nips/pull/2299)): Nostr에서 [FROST](/ko/topics/frost/) (Flexible Round-Optimized Schnorr) threshold signing을 위한 규약을 제안합니다. FROST는 signer 집단이 Nostr 신원을 공동으로 제어하게 해 주며, 전체 개인 키를 재구성하지 않고도 t-of-n 구성원만으로 이벤트에 서명할 수 있게 합니다. 이 NIP는 [FROSTR 프로젝트](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11)의 Igloo signer 작업을 바탕으로, 서명 라운드 조정, 키 share 배포, threshold-signed event 게시 방법을 정의합니다.

- **[NIP-5D](/en/topics/nip-5d/) (Nostr Web Applets)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): iframe 안에서 실행되는 sandboxed 웹 애플리케이션("napplets")이 호스팅 애플리케이션("shell")과 통신하기 위한 `postMessage` 프로토콜을 정의합니다. shell은 구조화된 message API를 통해 napplet에 Nostr signing, relay access, 사용자 컨텍스트를 제공합니다. 반면 iframe sandbox는 키에 직접 접근하는 일을 막습니다. 이는 [NIP-5A](/en/topics/nip-5a/)의 정적 웹사이트 호스팅 모델을, Nostr 이벤트를 읽고 쓸 수 있는 상호작용 애플리케이션 쪽으로 확장합니다. 이 NIP는 동작하는 runtime 구현과 함께 활발히 개발 중입니다.

- **[NIP-5C](/en/topics/nip-5c/) (Scrolls)** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): 이전 NIP-A5 제안에서 이름이 바뀌었습니다. Nostr에서 WebAssembly 프로그램을 게시하고 발견하기 위한 규약을 정의합니다. WASM 바이너리는 Nostr 이벤트로 저장되고, 클라이언트는 이를 다운로드해 sandboxed runtime에서 실행할 수 있습니다. [데모 앱](https://nprogram.netlify.app/)은 브라우저 안에서 실행되는 scrolls를 보여 주며, 어떤 클라이언트든 가져와 실행할 수 있는 예제 프로그램이 Nostr 이벤트로 게시돼 있습니다.

- **[NIP-85](/ko/topics/nip-85/) (Trusted Assertions): Clarifications** ([PR #2304](https://github.com/nostr-protocol/nips/pull/2304)): 서비스 제공자당 여러 키와 relay를 다루는 사양 문구를 더 엄격하게 다듬어, 제공자가 여러 pubkey나 relay endpoint에 걸쳐 동작할 때 클라이언트가 assertion을 어떻게 처리해야 하는지 분명히 합니다.

- **[NIP-24](/ko/topics/nip-24/) (Extra Metadata Fields): published_at for replaceable events** ([PR #2300](https://github.com/nostr-protocol/nips/pull/2300)): [NIP-23](/en/topics/nip-23/) (Long-form Content)의 `published_at` 태그를 모든 replaceable 및 addressable event로 일반화합니다. 이 태그는 표시 전용입니다. `published_at`이 `created_at`과 같으면 클라이언트는 해당 시점을 "created"로 표시하고, 값이 다르면(이벤트가 업데이트되었기 때문) "updated"로 표시할 수 있습니다. 이를 통해 kind `0` 프로필은 "joined at" 날짜를 표시할 수 있고, 다른 replaceable event도 업데이트를 거쳐도 원래의 게시 시점을 유지할 수 있습니다. 보완 제안으로 [NIP-51](/ko/topics/nip-51/) ([PR #2302](https://github.com/nostr-protocol/nips/pull/2302))은 동일한 태그를 list event에도 추가합니다.

- **[NIP-59](/ko/topics/nip-59/) (Gift Wrap): Ephemeral gift wrap kind** ([PR #2245](https://github.com/nostr-protocol/nips/pull/2245)): 기존 kind `1059` gift wrap의 ephemeral 대응물로 kind `21059`를 추가합니다. Ephemeral event(kinds `20000`-`29999`)는 [NIP-01](/ko/topics/nip-01/) semantics를 따르며, relay는 이를 저장할 것으로 기대되지 않고 전달 후 폐기할 수 있습니다. 이를 통해 애플리케이션은 일반 [NIP-17](/ko/topics/nip-17/) DM과 같은 3계층 암호화 모델을 유지하면서도, relay에서 전달 후 사라지는 gift-wrapped 메시지를 보낼 수 있어 대용량 메시징의 저장 요구를 줄일 수 있습니다.

### OpenSats announces sixteenth wave of Nostr grants

[OpenSats](https://opensats.org)는 4월 8일 [열여섯 번째 Nostr grants 물결](https://opensats.org/blog/sixteenth-wave-of-nostr-grants)을 발표하며, 신규 4건과 갱신 1건을 지원했습니다. [Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp)는 기여자 Robert Nagy가 [Quartz](/ko/topics/quartz/)와 Commons 모듈 위에 독립형 데스크톱 앱을 구축하도록 자금을 받았고, 이를 통해 Android 클라이언트의 기능 세트를 지속적인 relay 연결을 갖춘 마우스 중심 인터페이스로 가져가게 됩니다. [Nostr Mail](https://github.com/nogringo/nostr-mail)는 [NIP-59](/ko/topics/nip-59/) gift wrap에 싸인 kind `1301` 이벤트를 사용해 Nostr 위에서 전체 이메일 시스템을 구축하기 위한 지원을 받았으며, Flutter 클라이언트와 Gmail/Outlook 호환용 SMTP bridge 서버도 포함됩니다. [Nostrord](https://github.com/Nostrord/nostrord)는 Discord 스타일의 그룹 메시징, moderation, thread를 갖춘 Kotlin Multiplatform [NIP-29](/en/topics/nip-29/) relay 기반 그룹 클라이언트를 위한 지원을 받았습니다. [Nurunuru](https://github.com/tami1A84/null--nostr)는 LINE과 유사한 친숙한 인터페이스를 모델로 한 일본어 중심 Nostr 클라이언트의 네이티브 iOS 버전을 만들기 위한 자금을 받았고, 온보딩에는 passkey 기반 biometric login이 포함됩니다. HAMSTR는 [열한 번째 물결](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr)에서 처음 지원된 뒤 이번에 갱신 지원을 받았습니다.

## NIP Deep Dive: NIP-17 (Private Direct Messages)

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)은 Nostr에서 private direct message를 위한 현재 표준을 정의합니다. 이 사양은 이전 [NIP-04](/ko/topics/nip-04/) (Encrypted Direct Messages) 방식을 대체합니다. NIP-04는 발신자, 수신자, 타임스탬프가 모두 relay에 노출되는 메타데이터 누출 문제가 있었고, 더 약한 암호화 구성을 사용했습니다. NIP-17은 암호화를 위해 [NIP-44](/ko/topics/nip-44/) (Encrypted Payloads)를 사용하고, 메타데이터 보호를 위해 [NIP-59](/ko/topics/nip-59/) (Gift Wrap)를 결합해, relay가 누가 누구와 대화하는지 볼 수 없는 3계층 시스템을 만듭니다.

이 프로토콜은 서로 안에 쌓인 세 가지 event kind를 사용합니다. 가장 안쪽 계층은 실제 메시지인 서명되지 않은 kind `14` 이벤트입니다.

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

kind `14` 이벤트는 의도적으로 서명되지 않았습니다(`sig`가 비어 있음). 사양은 이를 부인 가능성을 제공하는 것으로 설명하지만, 실제 보호 수준은 제한적입니다. rumor를 감싸는 kind `13` seal은 발신자의 실제 키로 서명됩니다. 수신자는 메시지 내용을 공개하지 않더라도, 서명된 seal을 제3자에게 보여 주며 발신자가 자신과 통신했다는 사실을 증명할 수 있습니다. 영지식 증명을 사용하면 수신자는 자신의 개인 키를 드러내지 않고도 정확한 메시지 내용까지 증명할 수 있습니다. 서명되지 않은 rumor는 서명된 봉투 안에 들어 있는 서명 없는 편지와 비슷합니다. 봉투의 서명이 발신자를 내용물과 연결합니다. 진정한 부인 가능성은 Signal의 HMAC 같은 대칭 인증이 필요하지만, 메시지가 self-authenticating이어야 하는 Nostr의 탈중앙 relay 모델과는 맞지 않습니다. NIP-17의 진짜 강점은 부인 가능성이 아니라 메타데이터 프라이버시와 콘텐츠 기밀성입니다.

이 서명되지 않은 메시지는 kind `13` seal에 감싸지며, 이 seal은 실제 발신자가 서명하고 [NIP-44](/ko/topics/nip-44/)로 수신자에게 암호화됩니다.

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

seal에는 태그가 없으므로, 설령 복호화되더라도 수신자를 드러내지 않습니다. seal은 발신자의 실제 키로 서명되므로, 수신자는 seal의 `pubkey`가 내부 kind `14`의 `pubkey`와 일치하는지 확인해 메시지를 인증할 수 있습니다.

그다음 이 seal은 임의의 일회용 키로 서명되고 수신자 앞으로 지정된 kind `1059` gift wrap에 다시 감싸집니다.

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

gift wrap의 `pubkey`는 이 메시지만을 위해 생성된 임의의 키이며, `created_at`은 최대 이틀 전까지 무작위화됩니다. relay가 실제로 보는 최외곽 계층은 이것입니다. 정체를 알 수 없는 pubkey에서 수신자 앞으로 온 메시지이지만, 타임스탬프는 실제 발송 시점을 반영하지 않습니다. 이 무작위 타임스탬프는 저장된 이벤트를 나중에 분석하는 공격에는 방어가 되지만, relay에 능동적으로 연결된 적대자는 gift wrap이 처음 나타난 시점을 여전히 관찰할 수 있으므로 이 방어는 나중에 relay 데이터를 조회하는 수동 관찰자에게만 제한적으로 유효합니다. pubkey는 임의이고 타임스탬프는 가짜이므로, relay는 실제 발신자를 판별할 수 없습니다. 메시지를 읽으려면 수신자가 자신의 키와 임의 pubkey를 사용해 gift wrap을 복호화하고, 그 안에서 seal을 찾은 뒤, 자신의 키와 seal 안의 발신자 pubkey를 사용해 seal을 복호화해, 마지막으로 안쪽의 kind `14` 메시지를 찾아야 합니다.

NIP-17은 forward secrecy를 제공하지 않습니다. 모든 메시지는 정적인 Nostr 키페어를 사용해 암호화됩니다(NIP-44는 발신자와 수신자 키로부터 키를 도출합니다). 개인 키가 손상되면, 그 키로 암호화된 과거와 미래의 모든 메시지를 복호화할 수 있습니다. 이는 의도된 절충입니다. 암호화가 nsec에만 의존하기 때문에, 사용자가 자신의 nsec를 백업해 두면 gift wrap을 여전히 저장하고 있는 어떤 relay에서든 전체 메시지 기록을 복구할 수 있습니다. [Marmot](/ko/topics/marmot/)에 사용되는 MLS 같은 프로토콜은 회전하는 키 재료를 통해 forward secrecy를 제공하지만, 그 대가로 상태 동기화가 필요하고 키 회전 이후에는 과거 메시지를 복구할 수 없게 됩니다.

NIP-17은 또한 암호화된 파일 메시지를 위한 kind `15`도 정의합니다. 이 kind는 `file-type`, `encryption-algorithm`, `decryption-key`, `decryption-nonce` 태그를 추가해, 수신자가 Blossom 서버에 업로드되기 전에 AES-GCM으로 암호화된 첨부 파일을 복호화할 수 있게 합니다. kind `10050`은 사용자가 선호하는 DM relay 목록을 게시하는 데 사용되며, 발신자는 gift wrap을 어디로 전달해야 하는지 알 수 있습니다. 메시지 안의 `pubkey`와 `p` 태그 집합이 채팅방을 정의하며, 참가자를 추가하거나 제거하면 깔끔한 이력이 분리된 새 방이 만들어집니다.

구현은 주요 클라이언트 대부분을 아우릅니다. [nospeak](https://github.com/psic4t/nospeak)는 모든 일대일 메시징에 NIP-17을 사용합니다. [Flotilla](https://gitea.coracle.social/coracle/flotilla)는 proof-of-work DM에 NIP-17을 사용합니다. [Amethyst](https://github.com/vitorpamplona/amethyst), [Primal](https://github.com/PrimalHQ/primal-android-app), [Nostur](https://github.com/nostur-com/nostur-ios-public), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel), [Coracle](https://github.com/coracle-social/coracle)은 모두 NIP-17을 기본 DM 프로토콜로 구현하고 있습니다. 이 사양은 또한 gift wrap에 `expiration` 태그를 설정해 사라지는 메시지도 지원합니다.

## NIP Deep Dive: NIP-46 (Nostr Remote Signing)

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)은 사용자의 개인 키를 클라이언트 애플리케이션과 분리하는 프로토콜을 정의합니다. 사용자가 웹 앱에 nsec를 붙여 넣는 대신, 개인 키를 보관하는 remote signer("bunker"라고도 부름)를 실행하고, 이 signer가 Nostr relay를 통해 서명 요청에 응답합니다. 클라이언트는 개인 키를 절대 보지 못합니다. 이렇게 하면 공격 표면이 줄어듭니다. 손상된 클라이언트가 서명을 요청할 수는 있어도 키 자체를 빼내 갈 수는 없습니다.

이 프로토콜은 요청과 응답 모두에 kind `24133`을 사용하며, [NIP-44](/ko/topics/nip-44/) (Encrypted Payloads)로 암호화됩니다. 클라이언트는 세션용 일회성 `client-keypair`를 생성하고, 서로의 pubkey로 태그된 NIP-44 암호화 메시지를 통해 remote signer와 통신합니다. 아래는 클라이언트가 remote signer에 보내는 서명 요청 예시입니다.

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

암호화된 `content`는 JSON-RPC와 유사한 구조를 담고 있습니다.

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

remote signer는 요청을 복호화하고, 사용자에게 승인을 요청하거나(또는 설정된 권한에 따라 자동 승인하거나), 사용자의 개인 키로 이벤트에 서명한 뒤, 응답으로 서명된 이벤트를 반환합니다.

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

연결은 양쪽 어느 쪽에서든 시작할 수 있습니다. remote signer는 자신의 pubkey와 relay 정보를 담은 `bunker://` URL을 제공합니다. 클라이언트는 자신의 client pubkey, relay, 연결 검증용 secret이 포함된 `nostrconnect://` URL을 제공합니다. `secret` 파라미터는 연결 스푸핑을 막습니다. 바깥 채널로 URL을 전달받은 당사자만 핸드셰이크를 완료할 수 있습니다.

정의된 메서드는 여덟 가지입니다. 세션을 설정하는 `connect`, 이벤트에 서명하는 `sign_event`, 사용자의 pubkey를 알아내는 `get_public_key`, keepalive용 `ping`, 레거시 암호화를 위한 `nip04_encrypt`/`nip04_decrypt`, 현재 암호화를 위한 `nip44_encrypt`/`nip44_decrypt`, relay 관리를 위한 `switch_relays`입니다. relay 마이그레이션은 remote signer가 처리하므로, 시간이 지나 새 relay로 연결을 옮겨도 세션은 끊기지 않습니다.

클라이언트는 permission 시스템을 통해 연결 시점에 필요한 capability를 요청합니다. `nip44_encrypt,sign_event:1,sign_event:14` 같은 permission 문자열은 NIP-44 암호화 접근과 kind `1`, kind `14` 이벤트에 대한 서명 접근만 요청합니다. remote signer는 이 권한을 수락, 거부, 수정할 수 있습니다. 이는 읽기와 노트 게시를 하는 웹 클라이언트가 `sign_event:1` 권한만 받을 수 있고, DM 클라이언트는 여기에 `sign_event:14`와 `nip44_encrypt` 권한까지 추가로 받을 수 있음을 뜻합니다.

[Amber](https://github.com/greenart7c3/Amber)는 Android에서 NIP-46을 구현하고 있으며, 이번 주의 [v6.0.0-pre1](#amber-v600-pre1-adds-per-connection-nip-46-signing-keys)은 클라이언트 간 격리를 위해 연결별 서명 키를 추가합니다. [nsec.app](https://github.com/nicktee/nsecapp) (이전 이름은 Nostr Connect)은 웹 기반 bunker를 제공합니다. [nostr-tools](https://github.com/nbd-wtf/nostr-tools)는 JavaScript 클라이언트를 위한 `BunkerSigner`를 포함하고 있으며, [지난주 PR #530](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing)은 수동 relay 관리를 위한 `skipSwitchRelays`를 추가했습니다. 이 프로토콜은 auth challenge도 지원합니다. remote signer가 추가 인증(비밀번호, biometric, hardware token)을 요구할 때는, 클라이언트가 브라우저에서 열어 사용자가 완료할 수 있는 `auth_url`로 응답합니다.

---

이번 주는 여기까지입니다. 만들고 있는 것이 있거나 공유할 소식이 있다면 Nostr에서 DM을 보내 주세요. 아니면 [nostrcompass.org](https://nostrcompass.org)에서 저희를 찾아오셔도 됩니다.
