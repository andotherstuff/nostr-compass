---
title: 'Nostr Compass #8'
date: 2026-02-04
translationOf: /en/newsletters/2026-02-04-newsletter.md
translationDate: 2026-02-04
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** rust-nostr가 SDK 아키텍처를 전면 개편하는 21개의 PR과 함께 주요 API 재설계를 출시했습니다. Nostria 3.0이 듀얼 패인 네비게이션, 리스트 관리, 완전한 UI 개편과 함께 출시되었습니다. Vector가 SIMD 가속을 추가하여 65배에서 184배의 속도 향상을 달성하고 암호화된 그룹 메시징을 위한 [Marmot](/ko/topics/marmot/) 프로토콜 지원을 출시했습니다. Frostr가 TestFlight를 통해 iOS에 임계값 서명을 가져왔습니다. Damus가 크로스 relay 콘텐츠 발견을 위한 [NIP-19 (Bech32 인코딩 엔티티)](/ko/topics/nip-19/) relay 힌트를 구현했습니다. Primal Android가 NWC 암호화와 지갑 거래 내보내기를 추가했습니다. nostr-tools와 NDK가 안정성 개선을 받았습니다. NIP-82 (소프트웨어 애플리케이션)가 디바이스 플랫폼의 98%를 커버하도록 확장되었습니다. NIPs 저장소가 [NIP-47 (Nostr Wallet Connect)](/ko/topics/nip-47/)에 hold invoice 지원을 병합했습니다. 새로운 프로토콜 제안에는 팟캐스팅을 위한 NIP-74, 브라우저 event 데이터베이스를 위한 NIP-DB, 탈중앙화 콘텐츠 큐레이션을 위한 TRUSTed Filters 제품군이 포함됩니다. 새로운 프로젝트로는 콘텐츠 마이그레이션을 위한 Instagram to Nostr v2, 탈중앙화 3D 프린팅 마켓플레이스를 출시하는 Pod21, AI 에이전트가 관리하는 커뮤니티를 소개하는 Clawstr, 라이브 스트리밍과 화상 통화 기능을 확장하는 Shosho와 NosCall이 있습니다.

## 뉴스

### rust-nostr, 주요 API 재설계 출시

[rust-nostr](https://github.com/rust-nostr/nostr) SDK가 이번 주 라이브러리 전반에 걸쳐 브레이킹 체인지를 도입하는 21개의 병합된 PR과 함께 대대적인 아키텍처 개편을 거쳤습니다. 이번 재설계는 대부분의 Rust 개발자가 의존하는 핵심 API에 영향을 미칩니다.

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245)는 알림 API를 재설계하고, [PR #1244](https://github.com/rust-nostr/nostr/pull/1244)는 더 깔끔한 상태 처리를 위해 `RelayNotification::Shutdown`을 `RelayStatus::Shutdown`으로 교체합니다. 서명자 API는 이제 [PR #1243](https://github.com/rust-nostr/nostr/pull/1243)을 통해 다른 SDK 패턴과 정렬됩니다. Client와 Relay 메서드는 [PR #1242](https://github.com/rust-nostr/nostr/pull/1242)에서 정리되었고, 클라이언트 옵션은 이제 빌더 패턴을 사용합니다([PR #1241](https://github.com/rust-nostr/nostr/pull/1241)).

메시지 전송 API는 [PR #1240](https://github.com/rust-nostr/nostr/pull/1240)에서, REQ 구독 취소는 [PR #1239](https://github.com/rust-nostr/nostr/pull/1239)에서, relay 제거는 [PR #1229](https://github.com/rust-nostr/nostr/pull/1229)에서 재설계되었습니다. [오픈 PR #1246](https://github.com/rust-nostr/nostr/pull/1246)은 재설계를 마무리하기 위해 블로킹 API 지원을 추가합니다.

이번 변경은 SDK에 일관성을 가져오지만 기존 프로젝트에서 마이그레이션 작업이 필요합니다. rust-nostr 기반으로 개발하는 개발자는 업그레이드 전에 changelog를 주의 깊게 검토해야 합니다.

### Instagram to Nostr v2, 콘텐츠 마이그레이션 지원

새로운 도구를 통해 크리에이터가 중앙 집중식 플랫폼의 기존 콘텐츠를 Nostr로 마이그레이션할 수 있습니다. [Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2)는 사용자의 개인 키에 대한 접근 없이 Instagram, TikTok, Twitter, Substack에서 가져오기를 지원합니다.

이 도구는 일반적인 온보딩 장벽을 해결합니다: 새 플랫폼에서 처음부터 시작하기를 망설이는 사용자가 이제 콘텐츠 히스토리를 보존할 수 있습니다. 또한 새 사용자에게 Nostr 계정을 선물하거나 기존 계정에 콘텐츠를 제안하는 것을 지원하여, 다른 사람들의 프로토콜 전환을 돕는 데 유용합니다.

### Pod21: 탈중앙화 3D 프린팅 네트워크

[Pod21](https://github.com/gobrrrme/Pod21) ([pod21.com](https://pod21.com))은 마켓플레이스 조정을 위해 Nostr를 사용하여 3D 프린터 운영자와 구매자를 연결합니다. 이 플랫폼에는 마켓플레이스 상호작용을 처리하는 [NIP-17 (비공개 다이렉트 메시지)](/ko/topics/nip-17/) 호환 DM 봇이 포함되어 있어, 구매자가 암호화된 다이렉트 메시지를 통해 인쇄를 요청하고 제작자와 협상할 수 있습니다.

제작자는 자신의 인쇄 용량과 능력을 나열하고, 구매자는 목록을 탐색하며 봇을 통해 주문을 시작합니다. 이 아키텍처는 다른 Nostr 상거래 애플리케이션과 유사한 패턴을 따릅니다: 발견을 위한 relay 기반, 주문 조정을 위한 암호화된 메시징, 결제를 위한 Lightning. Pod21은 Ridestr 및 Shopstr와 함께 프로토콜을 통해 실제 거래를 조정하는 Nostr 애플리케이션으로 합류합니다.

### Clawstr: AI 에이전트 소셜 네트워크

[Clawstr](https://github.com/clawstr/clawstr)가 AI 에이전트가 Nostr에서 커뮤니티를 생성하고 관리하는 Reddit 영감을 받은 플랫폼으로 출시됩니다. 이 플랫폼은 자율 에이전트가 주제별 커뮤니티를 설립하고, 콘텐츠를 큐레이션하며, 사용자와 상호작용할 수 있게 합니다. 커뮤니티는 서브레딧처럼 기능하지만 AI 모더레이터와 큐레이터가 토론을 안내합니다. 이 아키텍처는 에이전트 간 및 에이전트와 인간 간 상호작용을 위해 Nostr의 오픈 프로토콜을 사용하여, 탈중앙화 소셜 미디어에서 커뮤니티 형성의 새로운 모델을 확립합니다.

## 릴리스

### Ridestr v0.2.0: RoadFlare 릴리스

[Ridestr](https://github.com/variablefate/ridestr)가 개인 라이드셰어 네트워크를 도입하는 "RoadFlare Release"로 명명된 [v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0)을 출시했습니다. 이 기능을 통해 라이더는 즐겨찾는 드라이버를 신뢰할 수 있는 네트워크에 추가할 수 있습니다. 드라이버는 팔로워를 승인하고 암호화된 위치를 공유하여, 라이더가 신뢰할 수 있는 드라이버가 온라인이고 근처에 있을 때 볼 수 있게 합니다. 라이드 요청은 알려진 드라이버에게 직접 전달됩니다.

자동 에스크로 복구, 더 나은 기기 간 지갑 동기화, 점진적 폴링을 통한 더 빠른 결제 처리로 결제 신뢰성이 개선되었습니다. [PR #37](https://github.com/variablefate/ridestr/pull/37)은 이러한 기능을 지원하는 Phase 5-6 인프라를 추가합니다. [v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1)은 결제 대화 상자 버그와 라이드 후 "즐겨찾기에 추가" 흐름에 대한 핫픽스로 이어졌습니다.

### Nostria 3.0

sondreb의 글로벌 스케일을 위해 구축된 크로스 플랫폼 클라이언트인 [Nostria](https://github.com/nostria-app/nostria)가 완전한 UI 개편, 새 로고, 수백 개의 수정 사항과 함께 버전 3.0을 출시했습니다. 이 릴리스는 집중적인 6주간의 개발 주기를 나타냅니다.

듀얼 패인 네비게이션이 가장 큰 UX 변화로, 데스크톱 사용자가 리스트, 세부정보, 스레드 간 이동 시 컨텍스트 전환을 줄일 수 있습니다. 새로운 홈 섹션은 사용 가능한 모든 기능의 개요를 제공하며, 모든 화면이 통합된 툴바, 레이아웃, 기능을 공유합니다.

리스트 관리가 가장 중요한 기능 업데이트로, 애플리케이션 전체에 통합됩니다. 사용자는 프로필 리스트를 관리하고 Streams, Music, Feeds 등 모든 기능에서 콘텐츠를 필터링할 수 있습니다. 스레드의 스팸이 지겹다면 즐겨찾기로 필터링하여 그들의 답글만 볼 수 있습니다. Quick Zaps는 구성 가능한 값으로 원탭 zap을 추가합니다. Copy/Screenshot은 어디서든 event를 공유하기 위한 클립보드 스크린샷을 생성합니다. Muted Words는 이제 프로필 필드(name, display_name, NIP-05)를 필터링하여, 사용자가 단일 금지 단어로 모든 브릿지된 프로필을 차단할 수 있습니다. 설정은 더 빠른 구성 변경을 위해 검색 가능해졌습니다.

이 릴리스는 BOLT11 및 BOLT12 결제 요청 렌더링, 텍스트 크기 및 글꼴 선택, 기사 및 event와 같은 참조 콘텐츠 렌더링이 포함된 메시지 섹션의 "Note-to-Self" 메시징을 추가합니다. 새로운 공유 대화 상자는 이메일, 웹사이트 또는 여러 수신자에게 다이렉트 메시지를 통한 빠른 공유를 가능하게 합니다. 추가 기능으로는 커스텀 이모지 세트, Interests(동적 피드로서의 해시태그 리스트), 북마크, 공개 Relay 피드, Nostria 아이콘이 여는 옵션을 포함한 전체 메뉴 커스터마이징이 있습니다.

Android, iOS, Windows 및 [nostria.app](https://www.nostria.app/)의 웹에서 사용 가능합니다.

### Applesauce v5.1.0

hzrd149의 [Applesauce](https://github.com/hzrd149/applesauce) 라이브러리 제품군이 모든 패키지에서 v5.1.0을 릴리스했습니다. [applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0)는 Nostr Connect 원격 서명자에 대한 `switch_relays` 및 `ping` 메서드 지원을 추가하여, 서명자 연결을 프로그래밍 방식으로 관리하는 데 유용합니다. [applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0)는 병렬 비동기 로딩을 위한 `loadAsyncMap`을 도입합니다. [applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0)는 `useAction().run()`에 패딩 인수를 추가합니다. [applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0)는 `onlyEvents` 없이 문자열을 직접 처리하도록 event-to-store 매핑을 업데이트합니다.

### nak v0.18.3

fiatjaf의 [nak](https://github.com/fiatjaf/nak) (Nostr Army Knife)가 mattn의 안정성 수정과 함께 [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3)에 도달했습니다. 이 릴리스는 mint URL에 `://` 구분자가 없을 때의 패닉을 방지하고, 날짜 값을 사용하기 전에 dateparser 오류를 검증하며, AUTH 챌린지 태그 파싱의 엣지 케이스를 처리합니다. 이러한 방어적 수정은 잘못된 입력을 처리할 때 CLI를 더 탄력적으로 만듭니다.

### Aegis v0.3.7

크로스 플랫폼 데스크톱 서명자인 [Aegis](https://github.com/ZharlieW/Aegis)가 [NIP-07 (브라우저 확장 인터페이스)](/ko/topics/nip-07/) 서명과 함께 Nostr 앱 브라우저 지원을 추가한 [v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7)을 출시했습니다. 이 릴리스는 [NIP-04 (암호화된 다이렉트 메시지)](/ko/topics/nip-04/) 및 [NIP-44 (버전 암호화)](/ko/topics/nip-44/) 암호화 event를 기록하여, 사용자가 어떤 애플리케이션이 암호화 작업을 요청하는지 추적할 수 있습니다. 브라우저 세그먼트는 이제 웹 앱만 표시하도록 플랫폼별로 필터링됩니다.

### Bitchat v1.5.1 (iOS)

Nostr와 Bluetooth 메시를 사용하는 오프라인 가능 메시징 앱인 [Bitchat](https://github.com/permissionlesstech/bitchat)이 iOS 보안 강화와 함께 [v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1)을 릴리스했습니다. [PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012)는 처리 전에 Nostr event 서명을 검증하고, 유효하지 않은 giftwrap과 내장된 패킷을 거부하며, 과대 페이로드를 제한하고, 스푸핑된 BLE 발표 발신자 ID를 차단합니다. [PR #998](https://github.com/permissionlesstech/bitchat/pull/998)은 발신자 ID를 연결 UUID에 바인딩하여 iOS BLE 메시 인증을 수정하고, 메시 네트워크에서 신원 스푸핑을 방지합니다. [PR #972](https://github.com/permissionlesstech/bitchat/pull/972)는 여러 메시 기기가 근처에 있을 때 피어 발견 플러드를 방지하기 위해 알림 속도 제한을 추가합니다.

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app)이 [PR #148](https://github.com/keychat-io/keychat-app/pull/148)을 통해 [NIP-47](/ko/topics/nip-47/) Nostr Wallet Connect 지원을 추가한 [v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495)를 릴리스했습니다. 사용자는 이제 메시징 앱 내 결제를 위해 외부 Lightning 지갑을 연결할 수 있습니다. 이 릴리스는 또한 macOS 데스크톱 알림을 추가합니다.

### Nostrmo v3.5.0

크로스 플랫폼 Flutter 클라이언트인 [Nostrmo](https://github.com/haorendashu/nostrmo)가 피드 시스템을 전면 개편한 [v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0)을 출시했습니다. 이 업데이트는 고정 피드를 커스터마이징 가능한 대안(General Feed, Mentioned Feed, Relay Feed)으로 교체하며, 각각 새로운 편집 페이지를 통해 구성할 수 있습니다. 이 릴리스는 더 나은 event 라우팅을 위한 outbox 모델 지원을 구현하고 구성 가능한 크기 제한과 구독 지원으로 로컬 relay 기능을 확장합니다.

### Shosho v0.11.1

Nostr용 라이브 스트리밍 앱인 [Shosho](https://github.com/r0d8lsh0p/shosho-releases)가 녹화 및 VOD 기능과 함께 [v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1)을 릴리스했습니다. 이 업데이트는 스트림을 시청하는 사람을 보여주는 방 참석자 표시기, 더 나은 토론 구성을 위한 스레드 채팅 대화, [NIP-46](/ko/topics/nip-46/)을 통한 iOS에서의 Nostr Connect 지원을 추가합니다. 스트리머는 이제 실시간 청중과의 채팅 상호작용을 유지하면서 나중에 시청할 수 있도록 방송을 저장할 수 있습니다.

### NosCall v0.5.0

Nostr용 오디오 및 화상 통화 앱인 [NosCall](https://github.com/sanah9/noscall)이 카테고리별 통화 정리를 위한 연락처 그룹, 연결 최적화를 위한 relay 관리, 개선된 NAT 트래버설을 위한 구성 가능한 ICE 서버 설정과 함께 [v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release)을 출시했습니다. 이 릴리스는 다크 모드 지원도 추가합니다. NosCall은 통화 시그널링 및 조정을 위해 Nostr를 사용하여, 중앙 집중식 서버 없이 피어 투 피어 통화를 가능하게 합니다.

### diVine 1.0.4

rabble의 짧은 루핑 비디오 클라이언트인 [diVine](https://github.com/divinevideo/divine-mobile)이 Zapstore 제출에 앞서 Android 사전 릴리스 알파로 [1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4)를 릴리스했습니다. 이 릴리스는 nsec 가져오기, nsecBunker 및 Amber와 함께하는 [NIP-46 (Nostr Connect)](/ko/topics/nip-46/) 원격 서명, nostrconnect:// URL 처리를 포함한 Nostr 키 관리 테스트에 중점을 둡니다. 팀은 relay 호환성 및 다른 클라이언트와의 비디오 상호 운용성에 대한 피드백을 요청하고 있습니다. [PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265)는 절대 컨테이너 경로 대신 상대 경로를 저장하여 앱 업데이트 후 비디오 클립이 사용할 수 없게 되는 iOS 파일 경로 처리 문제를 수정합니다. [PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251)은 댓글에서 프로필을 볼 때 네비게이션 문제를 수정합니다.

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus)가 [이전 에디션에서 다룬 NWC 수정 사항](/ko/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---nwc-수정)을 통합하여 안정 릴리스로 [v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2)를 출시했습니다.

### Frostr Igloo iOS TestFlight

[Frostr](https://github.com/FROSTR-ORG) ([frostr.org](https://frostr.org/))가 [TestFlight](https://testflight.apple.com/join/72hjQe3J)에서 [Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios)를 출시하여 Apple 기기로 임계값 서명을 확장했습니다. Frostr는 FROST (Flexible Round-Optimized Schnorr Threshold) 서명을 사용하여 nsec 키를 기기 간에 분산된 조각으로 분할하고, 내결함성을 갖춘 k-of-n 서명을 가능하게 합니다. "데모 모드"로 참여하는 사용자는 프로토콜의 실시간 조정 기능을 보여주는 라이브 2-of-2 임계값 서명 실험에 참여합니다. iOS 릴리스는 12월에 크로스 앱 서명 요청을 위한 [NIP-55 (Android 서명자)](/ko/topics/nip-55/) 지원과 함께 출시된 [Igloo for Android](https://github.com/FROSTR-ORG/igloo-android) (v0.1.2)와 합류합니다. 두 모바일 클라이언트는 [Igloo desktop](https://github.com/FROSTR-ORG/igloo-desktop)과 [Frost2x](https://github.com/FROSTR-ORG/frost2x) 브라우저 확장을 보완합니다.

## 프로젝트 업데이트

### Damus, NIP-19 Relay 힌트 구현

[Damus](https://github.com/damus-io/damus)가 event 가져오기를 위한 [NIP-19](/ko/topics/nip-19/) relay 힌트 사용을 구현한 [PR #3477](https://github.com/damus-io/damus/pull/3477)을 병합했습니다. 이 기능은 [NIP-10 (답글 스레드)](/ko/topics/nip-10/), [NIP-18 (리포스트)](/ko/topics/nip-18/), NIP-19 참조에서 힌트를 추출하여 사용자의 구성된 풀에 없는 relay의 노트를 볼 수 있게 합니다. 구현은 참조 카운트 정리가 포함된 임시 relay 연결을 사용하여 영구적인 relay 풀 확장을 방지합니다.

추가 수정에는 Lightning 인보이스 파싱([PR #3566](https://github.com/damus-io/damus/pull/3566)), 지갑 뷰 로딩([PR #3554](https://github.com/damus-io/damus/pull/3554)), relay 리스트 타이밍([PR #3553](https://github.com/damus-io/damus/pull/3553)), 시각적 "팝핑"을 줄이기 위한 프로필 프리로딩([PR #3550](https://github.com/damus-io/damus/pull/3550))이 포함됩니다. [드래프트 PR #3590](https://github.com/damus-io/damus/pull/3590)은 진행 중인 [NIP-17](/ko/topics/nip-17/) 비공개 DM 지원을 보여줍니다.

### Primal Android, NWC 암호화 출시

[Primal Android](https://github.com/PrimalHQ/primal-android-app)는 지갑 인프라에 초점을 맞춘 18개의 병합된 PR과 함께 매우 활발한 한 주를 보냈습니다. 앱은 이제 Lightspark의 자기 수탁 Lightning 프로토콜인 Spark와 통합됩니다. [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874)는 NWC 암호화 지원을 추가하고, [PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872)는 연결이 설정될 때 NWC 정보 event를 전송합니다.

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870)은 회계 및 세금 목적에 유용한 지갑 거래 CSV 내보내기를 가능하게 합니다. [PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716)은 노트 에디터에 로컬 계정 전환기를 추가합니다. 여러 지갑 복원 수정([PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876), [PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875), [PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873))은 비-Spark 지갑 구성을 가진 사용자의 엣지 케이스를 해결합니다.

### Marmot TypeScript SDK, 메시지 히스토리 추가

[Marmot](https://github.com/marmot-protocol/marmot) 프로토콜의 TypeScript 구현이 계속 개발 중입니다. hzrd149의 [PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38)은 참조 채팅 애플리케이션을 위한 페이지네이션이 포함된 메시지 히스토리 지속성을 구현하고, [PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39)는 라이브러리 사용성을 개선합니다.

Rust 측에서는 [PR #161](https://github.com/marmot-protocol/mdk/pull/161)이 실패 시 메시지 컨텍스트를 보존하기 위한 재시도 가능한 상태 처리를 구현하고, [PR #164](https://github.com/marmot-protocol/mdk/pull/164)는 SQLite와의 tokio 패닉을 방지하기 위해 std::sync::Mutex로 전환합니다. whitenoise-rs 백엔드는 [Amber 통합](https://github.com/marmot-protocol/whitenoise-rs/pull/418) ([PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)), [MDK 및 nostr-sdk 0.44로 업그레이드](https://github.com/marmot-protocol/whitenoise-rs/pull/467) ([PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467))를 추가하고, NewMessage 및 GroupInvite event 유형과 함께 [PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460)을 통한 실시간 알림 스트리밍을 도입합니다.

### HAVEN, 주기적 WoT 새로고침 추가

개인 relay인 [HAVEN](https://github.com/bitvora/haven)이 주기적 [Web of Trust](/ko/topics/web-of-trust/) 새로고침을 추가한 [PR #108](https://github.com/bitvora/haven/pull/108)을 병합했습니다. 이 기능은 사용자의 소셜 그래프가 발전함에 따라 신뢰 점수가 최신 상태를 유지하도록 보장하여, 시간이 지남에 따라 스팸 필터링 정확도를 향상시킵니다.

### nostr-tools

핵심 JavaScript 라이브러리인 [nostr-tools](https://github.com/nbd-wtf/nostr-tools)는 이번 주 여러 개선을 받았습니다. 커밋에는 [NIP-27 (텍스트 노트 참조)](/ko/topics/nip-27/) 멘션에서 [줄바꿈 후 해시태그 파싱 수정](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5), 연결 정리를 위한 [유휴 추적과 함께 손상된 relay 객체 자동 정리](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2), 싱글 스레드 성능 최적화를 위한 [메시지 큐 제거](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638), 더 나은 TypeScript 임포트를 위한 [소스 파일 내보내기](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139)가 포함됩니다.

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk)가 [기기 슬립/웨이크 사이클 후 재연결 및 오래된 연결 처리 수정](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3)과 함께 [beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0)을 출시하여 모바일 애플리케이션의 안정성 문제를 해결했습니다.

### Notedeck

Damus 팀의 데스크톱 클라이언트인 [Notedeck](https://github.com/damus-io/notedeck)에 [NIP-34 (Git 협업)](/ko/topics/nip-34/) 뷰어를 추가하는 [오픈 PR #1279](https://github.com/damus-io/notedeck/pull/1279)가 있습니다. 이를 통해 클라이언트 내에서 직접 Nostr relay에 게시된 git 저장소, 패치, 이슈를 탐색할 수 있어, Notedeck이 ngit 기반 워크플로우의 잠재적 프론트엔드가 될 수 있습니다.

### njump

Nostr 웹 게이트웨이인 [njump](https://github.com/fiatjaf/njump)가 [PR #152](https://github.com/fiatjaf/njump/pull/152)를 통해 두 가지 [NIP-51 (리스트)](/ko/topics/nip-51/) event 유형에 대한 지원을 추가했습니다. 게이트웨이는 이제 클라이언트가 다양한 컨텍스트에서 표시할 수 있는 사용자의 카테고리별 그룹인 kind:30000 Follow Sets와 공유 및 그룹 팔로우를 위해 설계된 큐레이션된 프로필 컬렉션인 kind:39089 Starter Packs를 렌더링합니다. 이러한 추가로 사용자가 nevent 링크를 공유할 때 njump가 커뮤니티 큐레이션 리스트를 표시할 수 있습니다.

### Amethyst

Android 클라이언트인 [Amethyst](https://github.com/vitorpamplona/amethyst)가 플레이어 뷰에서 비디오 공유를 방해하는 버그를 수정했습니다([PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)). "비디오 공유" 옵션이 콘텐츠 파라미터가 컨트롤 버튼 컴포넌트에 전달되지 않아 표시되지 않았습니다. 사용자는 이제 플레이어에서 직접 다른 앱으로 Nostr 비디오 콘텐츠를 공유할 수 있습니다. [PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693)은 특정 잘못된 형식의 event를 파싱할 때 발생하는 Jackson JSON 역직렬화 충돌을 수정합니다.

### Jumble

relay 피드 브라우징에 초점을 맞춘 웹 클라이언트인 [Jumble](https://github.com/CodyTseng/jumble)이 [PR #743](https://github.com/CodyTseng/jumble/pull/743)에서 클립보드를 통한 오디오 파일 업로드를 추가했습니다. 사용자는 이제 오디오 파일을 게시물 편집기에 직접 붙여넣을 수 있으며, 구성된 미디어 서버에 업로드하고 노트에 URL을 포함합니다. 이 기능은 기존 이미지 붙여넣기 기능을 반영합니다.

### Flotilla

hodlbod의 [NIP-29 (Relay 기반 그룹)](/ko/topics/nip-29/) 커뮤니티 클라이언트인 [Flotilla](https://github.com/coracle-social/flotilla)가 [PR #270](https://github.com/coracle-social/flotilla/pull/270)을 통해 알림을 출시했습니다. 이 업데이트는 앵커 기반 폴링에서 웹용 로컬 풀 알림과 모바일용 푸시 알림으로 알림 시스템을 리팩토링합니다. 이 아키텍처는 제안된 NIP-9a 표준(아래 [PR #2194](https://github.com/nostr-protocol/nips/pull/2194) 참조)을 구현하며, 사용자가 relay에 웹훅 콜백을 등록하고 필터가 일치할 때 암호화된 event 페이로드를 수신합니다.

### Formstr

Nostr 네이티브 폼 애플리케이션인 [Formstr](https://github.com/abh3po/nostr-forms)가 [PR #422](https://github.com/abh3po/nostr-forms/pull/422)에서 폼 가져오기 및 암호화된 폼 지원을 추가했습니다. 사용자는 이제 응답 링크를 통해 또는 다른 Formstr 인스턴스에서 기존 폼을 가져올 수 있습니다. 암호화 기능을 통해 폼 작성자는 지정된 수신자만 제출물을 읽을 수 있도록 응답을 제한할 수 있어, 민감한 정보를 수집하는 설문조사에 유용합니다.

### Pollerama

[nostr-tools](https://github.com/nbd-wtf/nostr-tools)를 기반으로 구축된 [Pollerama](https://github.com/abh3po/nostr-polls) ([pollerama.fun](https://pollerama.fun))가 [PR #141](https://github.com/abh3po/nostr-polls/pull/141)과 [PR #142](https://github.com/abh3po/nostr-polls/pull/142)를 통해 설문조사를 위한 [NIP-17](/ko/topics/nip-17/) DM 공유를 추가했습니다. 사용자는 이제 암호화된 다이렉트 메시지를 통해 연락처에 직접 설문조사를 공유할 수 있습니다.

### Nostrability Schemata

Nostr event를 위한 JSON 검증 스키마 컬렉션인 [Nostrability schemata](https://github.com/nostrability/schemata)가 [PR #59](https://github.com/nostrability/schemata/pull/59)를 통해 [NIP-59 (Gift Wrap)](/ko/topics/nip-59/) 커버리지를 추가했습니다. 이 업데이트에는 기존 [NIP-17](/ko/topics/nip-17/) 스키마 커버리지를 보완하는 kind 13 (seal) 및 kind 1059 (gift wrap) event에 대한 스키마가 포함됩니다.

### Vector

[NIP-17](/ko/topics/nip-17/), [NIP-44](/ko/topics/nip-44/), [NIP-59](/ko/topics/nip-59/)를 사용한 제로 메타데이터 암호화를 갖춘 프라이버시 중심 데스크톱 메신저인 [Vector](https://github.com/VectorPrivacy/Vector)가 SIMD 가속 성능 최적화를 도입한 [PR #39](https://github.com/VectorPrivacy/Vector/pull/39)를 병합했습니다. 16진수 인코딩은 65배, 이미지 프리뷰 생성은 최대 38배, 바이너리 검색 인덱싱을 통한 메시지 조회는 184배 빨라졌습니다. 이 PR은 Apple Silicon용 ARM64 NEON 내장 함수와 런타임 감지가 포함된 Windows 및 Linux용 x86_64 AVX2/SSE2를 추가합니다. 메시지 구조체가 472바이트에서 128바이트로 줄어들고 인터닝을 통해 npub 저장이 99.6% 감소하여 메모리 사용량이 줄었습니다.

Vector v0.3.0 (2025년 12월)은 MLS 프로토콜 기반 그룹 메시징을 위한 [MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk)를 통합하여, 클라이언트에 전방 비밀성을 갖춘 종단 간 암호화 그룹을 가져왔습니다. MIP-04 파일 공유는 이제 [White Noise](/ko/newsletters/2026-01-28-newsletter/#marmot-protocol-updates)와의 상호 운용성을 위해 설계된 MLS 그룹용 imeta 첨부 파일을 처리합니다. 이 릴리스는 또한 WebXDC 기반 P2P 멀티플레이어 게임이 있는 Mini Apps 플랫폼, The Nexus라는 탈중앙화 앱 스토어, 인앱 결제를 위한 PIVX 지갑 통합, 전체 히스토리 추적이 가능한 메시지 편집, 이미지 업로드 중 4배 메모리 감소를 도입했습니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-47: Hold Invoice 지원](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/ko/topics/nip-47/)가 이제 hold invoice를 지원하여, 수신자가 결제를 명시적으로 정산하거나 취소해야 하는 고급 결제 워크플로우를 가능하게 합니다. 이 PR은 세 가지 새로운 RPC 메서드를 추가합니다: `make_hold_invoice`는 사전 생성된 프리이미지와 결제 해시를 사용하여 hold invoice를 생성하고, `settle_hold_invoice`는 원본 프리이미지를 제공하여 결제를 청구하며, `cancel_hold_invoice`는 결제 해시를 사용하여 결제를 거부합니다. 새로운 `hold_invoice_accepted` 알림은 지불자가 결제를 잠글 때 발생합니다. 이를 통해 pay-to-unlock 콘텐츠, 마켓플레이스 에스크로 시스템, 결제 게이팅과 같은 사용 사례가 가능합니다. 구현이 이미 [Alby Hub](https://github.com/getAlby/hub/pull/1298), [Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382), [dart NDK](https://github.com/relaystr/ndk/pull/147)에서 진행 중입니다.

- **[NIP-05: 소문자 요구 사항](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (도메인 검증)](/ko/topics/nip-05/)가 이제 `nostr.json` 파일의 16진수 공개 키와 로컬 이름 모두에 대해 명시적으로 소문자를 요구합니다. 이는 명세에서 암묵적이었지만 명시되지 않아, 일부 구현이 대소문자를 혼용하고 다른 구현이 소문자로 정규화할 때 상호 운용성 문제를 야기했습니다. NIP-05 식별자를 검증하는 클라이언트는 이제 키나 이름에 대문자가 포함된 `nostr.json` 응답을 거부해야 합니다.

- **[NIP-73: 국가 코드](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (지오태그)](/ko/topics/nip-73/)가 이제 geohash의 대안으로 ISO 3166 국가 코드를 지원합니다. Event는 정확한 좌표 없이 국가 수준의 위치를 나타내기 위해 `["g", "US", "countryCode"]` 태그를 포함할 수 있습니다. 이를 통해 정확한 위치가 불필요하거나 바람직하지 않은 애플리케이션을 위한 국가 기반 콘텐츠 필터링 및 발견이 가능합니다. 이 PR은 또한 명세 문서에 누락된 geohash 예제를 추가했습니다.

**오픈 PR 및 논의:**

- **[NIP-82: 소프트웨어 애플리케이션](https://github.com/nostr-protocol/nips/pull/1336)** - franzap이 kind 30063 릴리스 event를 사용하여 Nostr를 통해 소프트웨어 애플리케이션이 배포되는 방식을 정의하는 이 드래프트 명세에 대한 주요 업데이트를 발표했습니다. 업데이트는 이제 macOS, Linux, Windows, FreeBSD, WASM 환경, VS Code 확장, Chrome 확장, Web Bundles/PWA를 포함하여 전 세계 디바이스 플랫폼의 약 98%를 커버합니다. 팀은 다음으로 Android, PWA, iOS 지원에 집중하고 있으며, 개발자들이 이 공유 표준으로 수렴하도록 초대하고 있습니다. Zapstore는 앞으로 몇 주 내에 새 형식으로 마이그레이션할 계획입니다.

- **[NIP-74: 팟캐스트](https://github.com/nostr-protocol/nips/pull/2211)** - 팟캐스트 쇼(kind 30074)와 에피소드(kind 30075)를 위한 주소 지정 가능한 event를 정의합니다. 쇼에는 제목, 설명, 카테고리, 커버 이미지와 같은 메타데이터가 포함됩니다. 에피소드는 부모 쇼를 참조하고 enclosure URL, 재생 시간, 챕터 마커를 포함합니다. 명세는 Podcasting 2.0 메타데이터 표준과 통합되며 Lightning을 통한 V4V (value-for-value) 수익화를 위한 값 태그를 포함합니다. Nostr 네이티브 팟캐스트 퍼블리싱 플랫폼인 [transmit.fm](https://transmit.fm)과 같은 플랫폼은 이 형식을 사용하여 relay에 직접 게시할 수 있어, 팟캐스터가 중개자 없이 콘텐츠를 배포할 수 있습니다.

- **[NIP-FR: 친구 전용 노트](https://github.com/nostr-protocol/nips/pull/2207)** - ViewKey라는 공유 대칭 키를 사용하여 사용자 정의 친구 목록에만 표시되는 노트를 게시하는 메커니즘을 제안합니다. 작성자는 NIP-44를 사용하여 ViewKey로 노트(kind 2044)를 암호화합니다. ViewKey 자체는 [NIP-59 (Gift Wrap)](/ko/topics/nip-59/)를 통해 각 친구에게 한 번 배포됩니다. ViewKey를 보유한 친구는 노트를 복호화하여 읽을 수 있고, 그 외의 모든 사람은 암호문만 볼 수 있습니다. 작성자가 친구를 제거하면 ViewKey가 로테이션됩니다: 새 키가 생성되어 gift wrap을 통해 남은 모든 친구에게 재배포되며, 제거된 친구가 향후 게시물에 접근할 수 없도록 보장합니다. 이 접근 방식은 콘텐츠 암호화(대칭, 효율적)와 키 배포(비대칭, 친구별)를 분리하여 자주 요청되는 프라이버시 기능을 가능하게 하면서 프로토콜을 경량으로 유지합니다.

- **[NIP-DB: 브라우저 Nostr Event 데이터베이스 인터페이스](https://nostrhub.io/e/1a451c1581888215ae5c311d36c8a7c7d9e5e81f1f4010de4afaf7fcbd553e90)** ([spec](https://github.com/hzrd149/nostr-bucket/blob/master/nip.md)) - 로컬 Nostr event 저장소를 제공하는 브라우저 확장을 위한 표준 `window.nostrdb` 인터페이스를 제안합니다. API에는 event 추가, ID 또는 필터별 쿼리, 일치 항목 카운트, 업데이트 구독 메서드가 포함됩니다. 웹 애플리케이션은 이 인터페이스를 사용하여 relay 요청 없이 로컬 캐시된 event에서 읽을 수 있어, 대역폭과 지연 시간을 줄입니다. hzrd149의 [nostr-bucket](https://github.com/hzrd149/nostr-bucket) 브라우저 확장은 참조 구현을 제공하며, 모든 브라우저 탭에 인터페이스를 주입합니다. 동반 [폴리필 라이브러리](https://github.com/hzrd149/window.nostrdb.js)는 확장이 없는 환경을 위해 IndexedDB를 사용하여 동일한 API를 구현합니다.

- **[TRUSTed Filters](https://nostrhub.io/e/237667820943d1c8bbe7ab7732623ae51b337f177776ece439d4a8be84708eb7)** - vitorpamplona의 [병합된 Trusted Assertions PR #1534](https://github.com/nostr-protocol/nips/pull/1534)를 기반으로 구축된 탈중앙화 콘텐츠 큐레이션을 위한 5개의 관련 제안 모음입니다. 핵심 명세는 사용자가 event 필터링 및 순위 지정을 위해 신뢰하는 서비스를 지정할 수 있는 Trust Provider Preferences 선언을 위한 kind 17570 event를 도입합니다. Trust provider는 클라이언트가 구독할 수 있는 어설션(kind 37571), 통계(kind 37572), 순위(kind 37573)를 게시합니다. 시스템은 필터 유형과 변환을 지정하기 위해 W/w 태그가 있는 플러그인 아키텍처를 사용합니다. 이를 통해 스팸 감지, 평판 점수, 콘텐츠 순위와 같은 계산 집약적 작업이 전용 인프라에서 실행되면서 사용자가 신뢰하는 provider에 대한 제어를 유지할 수 있습니다. 이 제품군에는 필터 프리셋, 사용자 순위, 신뢰할 수 있는 event, 플러그인 정의에 대한 별도의 명세가 포함됩니다.

- **[NIP-9a: 푸시 알림](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbod이 kind 30390 등록 event를 사용하는 relay 기반 푸시 알림 표준을 제안합니다. 사용자는 수신하려는 event의 필터와 웹훅 콜백 URL을 포함하는 등록을 생성합니다. 등록은 relay의 pubkey(NIP-11 `self` 필드에서)로 암호화됩니다. 일치하는 event가 발생하면 relay는 event ID(중복 제거를 위한 평문)와 event 자체(사용자에게 NIP-44 암호화)와 함께 콜백에 POST합니다. 이 아키텍처를 통해 relay가 중개 푸시 서버로부터 event 콘텐츠를 보호하면서 알림을 푸시할 수 있습니다. Flotilla의 [PR #270](https://github.com/coracle-social/flotilla/pull/270)이 이 표준을 구현합니다.

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - kind 33400 event를 사용하여 에스크로가 포함된 탈중앙화 계약 작업 프로토콜을 제안합니다. 시스템은 세 가지 역할을 정의합니다: 중재자는 가용성과 조건을 발표하고, 후원자는 에스크로된 Bitcoin으로 자금이 지원된 작업을 생성하며, 프리 에이전트는 결제를 청구하기 위해 작업을 완료합니다. 중재자는 필요할 때 분쟁을 해결합니다. 이 프로토콜은 납품물이 수락되거나 중재가 종료될 때까지 자금이 잠기는 무신뢰 프리랜서 작업 조정을 가능하게 합니다.

## NIP 심층 분석: NIP-47 (Nostr Wallet Connect)

[NIP-47](/ko/topics/nip-47/)은 Nostr를 통신 레이어로 사용하는 원격 Lightning 지갑 제어 프로토콜인 Nostr Wallet Connect (NWC)를 정의합니다. 이번 주 hold invoice 지원 추가로 NWC는 이제 전체 Lightning 작업 범위를 커버합니다.

프로토콜은 간단한 교환을 통해 작동합니다. 지갑 애플리케이션은 기능을 설명하는 "wallet info" event(kind 13194)를 게시합니다. 클라이언트 애플리케이션은 인보이스 결제, 인보이스 생성, 잔액 확인과 같은 작업을 지갑에 요청하는 암호화된 요청(kind 23194)을 보냅니다. 지갑은 암호화된 결과(kind 23195)로 응답합니다.

NWC는 클라이언트와 지갑 간에 [NIP-44](/ko/topics/nip-44/) 암호화를 사용하며, 지갑 작업을 위한 전용 키 쌍을 사용하여 사용자의 주 신원과 분리합니다. 이러한 분리는 NWC 연결이 손상되어도 사용자의 Nostr 신원이 노출되지 않음을 의미합니다.

**지원되는 메서드:**

명세는 핵심 Lightning 작업을 위한 메서드를 정의합니다: `pay_invoice`는 결제를 보내고, `make_invoice`는 수신을 위한 인보이스를 생성하며, `lookup_invoice`는 결제 상태를 확인하고, `get_balance`는 지갑 잔액을 반환하며, `list_transactions`는 결제 내역을 제공합니다. 새로 병합된 `pay_keysend`는 인보이스 없이 결제를 가능하게 하고, `hold_invoice`는 조건부 결제를 지원합니다.

**예제 Event:**

지갑 서비스는 기능을 광고하는 정보 event(kind 13194)를 게시합니다:

```json
{
  "kind": 13194,
  "pubkey": "<wallet service pubkey>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

클라이언트는 인보이스를 결제하기 위해 암호화된 요청(kind 23194)을 보냅니다:

```json
{
  "kind": 23194,
  "pubkey": "<client ephemeral pubkey from connection URI secret>",
  "content": "<NIP-44 encrypted: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<wallet service pubkey>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<client ephemeral key signature>"
}
```

지갑 서비스는 결제 결과로 응답합니다(kind 23195):

```json
{
  "kind": 23195,
  "pubkey": "<wallet service pubkey>",
  "content": "<NIP-44 encrypted: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<client ephemeral pubkey>"],
    ["e", "<request event id>"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

응답의 `e` 태그는 원본 요청을 참조하여, 클라이언트가 응답을 요청에 매칭할 수 있게 합니다.

**Hold Invoice:**

이번 주 [PR #1913](https://github.com/nostr-protocol/nips/pull/1913)은 에스크로 스타일 결제를 가능하게 하는 hold invoice 지원을 추가했습니다. 수신자가 프리이미지를 공개하여 즉시 결제를 청구하는 표준 인보이스와 달리, hold invoice는 수신자가 이 결정을 연기할 수 있게 합니다. 지불자가 hold invoice에 전송하면 결제 경로를 따라 자금이 잠깁니다. 수신자는 정산(프리이미지를 공개하고 자금 청구)하거나 취소(결제를 거부하고 자금을 지불자에게 반환)를 선택합니다. 두 작업 모두 발생하지 않으면 결제가 타임아웃되어 자금이 자동으로 반환됩니다. PR은 `make_hold_invoice`, `settle_hold_invoice`, `cancel_hold_invoice` 세 가지 NWC 메서드와 `hold_invoice_accepted` 알림을 추가합니다. 이 메커니즘은 Ridestr의 라이드셰어 에스크로 및 마켓플레이스 분쟁 해결과 같은 애플리케이션을 지원합니다.

**현재 구현:**

주요 지갑이 NWC를 지원합니다: Zeus, Alby, 그리고 이번 주 [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874)를 통해 Primal이 모두 지갑 측 지원을 구현합니다. 클라이언트 측에서는 Damus, Amethyst 및 대부분의 주요 Nostr 클라이언트가 zap 및 결제를 위해 NWC 지갑에 연결할 수 있습니다.

이 프로토콜은 관심사 분리를 가능하게 합니다: 사용자는 한 기기에서 지갑을 실행하면서 다른 기기에서 Nostr와 상호작용할 수 있으며, Nostr relay가 통신 채널 역할을 합니다. 이 아키텍처는 모바일 클라이언트가 직접 자금을 보유할 필요가 없어, 지갑 인프라를 소셜 클라이언트와 분리하여 보안을 향상시킵니다.

**보안 고려 사항:**

NWC 연결은 민감하게 취급해야 합니다. 암호화가 메시지 콘텐츠를 보호하지만, 지갑 pubkey와 연결 비밀은 보호되어야 합니다. 애플리케이션은 사용자가 연결을 취소하고 지출 한도를 설정할 수 있어야 합니다. 프로토콜은 기능 제한을 지원하므로, 지갑이 특정 연결이 수행할 수 있는 작업을 제한할 수 있습니다.

## NIP 심층 분석: NIP-59 (Gift Wrap)

[NIP-59](/ko/topics/nip-59/)는 어떤 Nostr event든 여러 레이어의 암호화로 캡슐화하여 relay와 관찰자로부터 발신자의 신원을 숨기는 프로토콜을 정의합니다. 이번 주 친구 전용 노트(NIP-FR) 및 푸시 알림(NIP-9a) 제안이 모두 gift wrapping에 의존하므로, 이해할 가치가 있는 기본 프라이버시 프리미티브입니다.

**세 개의 레이어:**

Gift wrapping은 세 개의 중첩된 구조를 사용합니다:

1. **Rumor** (서명되지 않은 event): 서명 없는 Nostr event로서의 원본 콘텐츠. Rumor는 relay가 서명되지 않은 event를 거부하기 때문에 직접 relay에 전송할 수 없습니다.

2. **Seal** (kind 13): Rumor가 [NIP-44](/ko/topics/nip-44/)를 사용하여 암호화되고 kind 13 event에 배치됩니다. Seal은 실제 작성자의 키로 서명됩니다. 이것이 작성자임을 증명하는 암호학적 증거입니다.

3. **Gift Wrap** (kind 1059): Seal이 암호화되어 무작위의 일회용 키 쌍으로 서명된 kind 1059 event에 배치됩니다. Gift wrap에는 수신자에게 라우팅하기 위한 `p` 태그가 포함됩니다.

**흔한 오해: 부인 가능성**

명세는 서명되지 않은 rumor가 "부인 가능성"을 제공한다고 언급하지만, 이는 오해의 소지가 있습니다. Seal 레이어는 실제 작성자가 서명합니다. 수신자가 gift wrap을 복호화하고 seal을 복호화하면, 누가 메시지를 보냈는지에 대한 암호학적 증거를 갖게 됩니다. 수신자는 자신의 개인 키를 노출하지 않고 발신자의 신원을 밝히는 영지식 증명을 구성할 수도 있습니다.

Gift wrap이 실제로 제공하는 것은 **관찰자로부터의 발신자 프라이버시**입니다: relay와 제3자는 무작위 키로 서명된 gift wrap만 보기 때문에 누가 메시지를 보냈는지 알 수 없습니다. 하지만 수신자는 항상 알고 증명할 수 있습니다.

**예제 Event:**

다음은 명세의 완전한 3레이어 구조입니다("오늘 밤 파티에 가나요?" 전송):

Rumor (서명되지 않음, relay에 게시 불가):
```json
{
  "created_at": 1691518405,
  "content": "Are you going to the party tonight?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

Seal (kind 13, 실제 작성자가 서명, 암호화된 rumor 포함):
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

Gift wrap (kind 1059, 무작위 임시 키로 서명, 암호화된 seal 포함):
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

주목하세요: seal의 `pubkey`는 실제 작성자(`611df01...`)이고, gift wrap의 `pubkey`는 무작위 일회용 키(`18b1a75...`)입니다. Relay는 gift wrap만 보기 때문에 메시지를 실제 작성자에게 귀속시킬 수 없습니다.

**각 레이어가 보호하는 것:**

Rumor는 서명되지 않아 relay에 직접 게시할 수 없습니다. Seal은 실제 작성자가 서명하여 수신자에게 작성자임을 증명합니다. Gift wrap은 무작위 일회용 키로 서명되어 relay와 관찰자로부터 실제 작성자를 숨깁니다. 수신자만이 두 레이어를 통해 복호화하여 원본 콘텐츠에 도달하고 seal에 대한 작성자의 서명을 검증할 수 있습니다.

**현재 애플리케이션:**

[NIP-17 (비공개 다이렉트 메시지)](/ko/topics/nip-17/)는 암호화된 DM을 위해 gift wrap을 사용하여 이전 NIP-04 방식을 대체합니다. 제안된 NIP-FR(친구 전용 노트)은 Gift Wrapping을 사용하여 친구에게 ViewKey를 배포하며, 친구는 해당 키로 암호화된 노트를 복호화합니다. NIP-9a (푸시 알림)는 gift wrap 원칙을 사용하여 알림 페이로드를 암호화합니다.

**메타데이터 보호:**

타이밍 분석을 막기 위해 타임스탬프를 무작위화해야 합니다. Relay는 kind 1059 event를 제공하기 전에 AUTH를 요구하고 표시된 수신자에게만 제공해야 합니다. 여러 수신자에게 전송할 때는 각각에 대해 별도의 gift wrap을 생성합니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 계신가요? 공유할 뉴스가 있나요? 프로젝트를 다뤄드릴까요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM으로 연락하시거나</a> Nostr에서 찾아주세요.
