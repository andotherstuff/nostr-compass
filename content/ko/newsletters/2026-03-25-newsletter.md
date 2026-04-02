---
title: 'Nostr Compass #15'
date: 2026-03-25
translationOf: /en/newsletters/2026-03-25-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [Primal Android](https://github.com/PrimalHQ/primal-android-app)가 3.0 지갑 릴리스에 이어 [Follow Packs, zap 보강, `primalconnect://` 딥 링크](#primal-adds-follow-packs-zap-enrichment-and-deep-links)를 추가했습니다. [BigBrotr](https://github.com/BigBrotr/bigbrotr)는 1,085개의 relay에서 4,100만 개 이벤트를 스캔해 16,599개의 유효한 개인 키를 찾은 [nsec 유출 분석](#bigbrotr-maps-exposed-private-keys-across-the-relay-network)을 발표했고, [npub.world](https://npub.world)는 같은 주에 프로필 페이지에 유출 경고를 통합했습니다. Martti Malmi는 Nostr relay를 통해 신호를 주고받고 WireGuard 터널을 생성하는 Tailscale 대안 [nostr-vpn](#nostr-vpn-launches-as-a-tailscale-alternative)을 출시했고, 7일 동안 11개의 릴리스를 배포했습니다. [Vector](https://github.com/VectorPrivacy/Vector) 팀은 [Nostr 위에서 작동하는 P2P DOOM](#open-source-doom-runs-peer-to-peer-over-nostr)을 오픈소스로 공개했고, [FIPS](https://github.com/jmcorgan/fips)는 [v0.2.0](#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples)을 출시했으며, [Nostrability Schemata](https://github.com/nostrability/schemata)는 한 주 만에 [6개 언어](#nostrability-schemata-goes-multilingual)로 확장되었습니다.

## 뉴스

### Primal adds Follow Packs, zap enrichment, and deep links

[지난주 3.0.7 보도에 이어](/ko/newsletters/2026-03-18-newsletter/), [Primal Android](https://github.com/PrimalHQ/primal-android-app)는 이번 주 온보딩, 작성기 UX, 지갑 컨텍스트에 관한 후속 작업을 진행했습니다. 새롭게 설계된 온보딩은 Follow Packs([PR #949](https://github.com/PrimalHQ/primal-android-app/pull/949))를 도입했고, 노트 작성기에 네이티브 GIF 버튼이 추가되었으며, zap 보강 서비스([PR #979](https://github.com/PrimalHQ/primal-android-app/pull/979))는 지갑 거래에 zap 컨텍스트를 주석으로 붙이고, `primalconnect://` 딥 링크 프로토콜([PR #969](https://github.com/PrimalHQ/primal-android-app/pull/969))은 앱 간 내비게이션을 가능하게 합니다.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app)도 같은 작업을 TestFlight를 통해 병렬로 배포하고 있으며, 지갑 전환([PR #191](https://github.com/PrimalHQ/primal-ios-app/pull/191)), 투표 구현, 온보딩 리팩터링이 같은 시기에 반영되고 있습니다.

### BigBrotr maps exposed private keys across the relay network

Nostr relay 분석 플랫폼 [BigBrotr](https://github.com/BigBrotr/bigbrotr)가 relay 네트워크의 노출된 개인 키에 대한 [상세 분석](https://bigbrotr.com/blog/exposed-nsec-analysis/)을 발표했습니다. 이 연구는 이벤트 콘텐츠에 포함된 유효한 nsec 문자열을 찾기 위해 1,085개 relay에서 4,100만 개 이벤트를 스캔했고, 16,599개의 유효한 개인 키를 발견했습니다. 이 수치는 경고처럼 보이지만, 일치 항목의 92%를 차지하는 "Mr.nsec"라는 봇을 제외하면 해석이 달라집니다. 봇 트래픽을 제거하면 2만 1천 명 이상의 총 팔로워를 가진 실제 계정은 38개뿐이었고, 어느 계정도 자신의 키가 공개되어 있다는 인식의 징후를 보이지 않았습니다.

팀은 nsec-leak-checker를 [NIP-90](/ko/topics/nip-90/) (Data Vending Machine) 서비스로 구축하여, 사용자가 자신의 개인 키를 검사기에 노출하지 않고도 스캔된 데이터셋 어디에 나타나는지 확인할 수 있게 했습니다. [npub.world](https://npub.world)는 같은 주에 이 유출 데이터를 통합하여, 노출된 키가 탐지된 프로필 페이지에 경고 배너를 표시했습니다. 이 조합은 네트워크에 DVM과 에이전트를 위한 프로그래밍 인터페이스와 일반 사용자를 위한 사람이 읽을 수 있는 경고를 동시에 제공합니다. 이 기반 데이터셋은 또한 대체 가능 및 주소 지정 가능 이벤트 materialized view와 동기화 유휴 타임아웃 수정을 추가한 [BigBrotr v6.4.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.4.0)에도 반영됩니다.

### Nostr VPN launches as a Tailscale alternative

Iris의 제작자 Martti Malmi(mmalmi)는 Nostr relay를 신호용으로 사용하고 WireGuard(boringtun 경유)로 암호화 터널을 만드는 P2P VPN인 [nostr-vpn](https://github.com/mmalmi/nostr-vpn)을 만들고 출시했습니다. 동기는 직접적이었습니다. "Tailscale이 제3자 계정을 요구하는 게 짜증나서 Nostr VPN을 만들었다"는 설명 그대로입니다. 이 도구는 Nostr 키페어를 신원으로 사용하여 장치 간 메시 네트워크를 구성하며, 중앙 조정 서버가 없습니다.

프로젝트는 [v0.2.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.2)부터 [v0.2.13](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.13)까지 7일 동안 11개의 릴리스를 배포했습니다. 이 질주는 Windows 지원, 로컬 네트워크 탐지를 위한 LAN 페어링, 모바일 장치를 위한 Android 사이드카를 추가했습니다. 아키텍처는 단순합니다. 두 장치가 Nostr relay를 통해 연결 메타데이터를 교환한 뒤 직접적인 WireGuard 터널을 수립합니다. Nostr는 탐색과 NAT 우회 신호를 담당하고, WireGuard는 실제 트래픽을 담당합니다. 신원은 Nostr 키페어입니다.

Malmi는 또한 Signal 스타일 보안 메시지 채널 라이브러리인 [nostr-double-ratchet](https://github.com/mmalmi/nostr-double-ratchet) 작업도 계속 밀어붙였고, 같은 주에 [v0.0.86](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.86)부터 [v0.0.93](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.93)까지 6개의 릴리스를 배포했습니다.

### Open-source DOOM runs peer-to-peer over Nostr

[Vector](https://github.com/VectorPrivacy/Vector) 팀은 피어 탐색에 Nostr, 종단간 암호화에 [Marmot](/ko/topics/marmot/), 그리고 전송에 n0의 QUIC 네트워킹 라이브러리 [Iroh](https://github.com/n0-computer/iroh)를 사용하는 P2P 멀티플레이어 DOOM 구현을 오픈소스로 공개했습니다. 이 게임은 4.2 MB WebXDC 파일로 배포되며, 채팅 메시지 안에서 전송할 수 있고, 경기를 호스팅하거나 조정할 서버가 필요하지 않습니다.

기술적 접근 방식은 원래 1993년식 lockstep 넷코드를 실시간 하이브리드 동기화 모델로 대체합니다. 플레이어는 Nostr relay 쿼리를 통해 서로를 발견하고, Marmot 암호화 채널을 통해 세션을 협상한 다음, 저지연 게임 트래픽을 위해 Iroh의 QUIC gossip 계층으로 넘깁니다. 이 스택은 탐색에 Nostr, 암호화에 Marmot, 전송에 Iroh를 사용합니다.

Vector는 이번 주 보안 강화 작업도 배포했습니다. 릴리스에는 안티 디버그 보호와 민감한 키 재료를 위한 zeroize가 포함된 메모리 강화 키 볼트, 전체 DM 및 그룹 메시지 필터링이 포함된 사용자 차단, Mini Apps용 WebXDC 실시간 채널 수정이 포함됩니다.

### FIPS v0.2.0 ships Tor transport, reproducible builds, and sidecar examples

자유 인터넷 피어링 시스템이자 Nostr 인접 메시 네트워킹 프로젝트인 [FIPS](https://github.com/jmcorgan/fips)가 [v0.2.0](https://github.com/jmcorgan/fips/releases/tag/v0.2.0-rel)을 출시했습니다. 이 릴리스는 익명화된 메시 링크를 위한 Tor 전송 지원, 재현 가능한 빌드, Nostr relay를 통해 연결하는 사이드카 예제, OpenWrt 패키지 워크플로의 Nostr 릴리스 게시를 추가합니다. 또한 drain-window 프레임으로 인해 발생하던 rekey 이후 지터 스파이크를 수정합니다. 와이어 형식은 v0.1.0에서 변경되었으므로, 기존 v0.1.0 노드는 업그레이드 없이는 v0.2.0과 상호운용할 수 없습니다.

### Nostrability Schemata goes multilingual

Nostr 이벤트 kind를 검증하기 위한 JSON Schema 정의를 유지하는 [Nostrability Schemata](https://github.com/nostrability/schemata) 프로젝트가 한 주 만에 JavaScript 전용에서 6개 언어로 확장되었습니다. Rust, Go, Dart, Swift, Python용 새 패키지가 각각 데이터 패키지와 검증기를 함께 제공합니다. [v0.2.6](https://github.com/nostrability/schemata/releases/tag/v0.2.6)은 17개의 새로운 이벤트 kind 스키마도 추가했습니다.

[Nostrability 상호운용성 추적기](https://nostrability.github.io/nostrability/)도 병행해서 대대적인 개편을 받았습니다. 새로운 What's New 탭은 Atom 피드와 Nostr 이벤트를 통해 업데이트를 게시하고, 앱 카테고리 필터링을 통해 방문자가 특정 클라이언트 유형으로 좁혀 볼 수 있으며, 이제 추적기는 GitHub 저장소 메타데이터에서 프로그래밍 언어를 자동 감지합니다. Nostrability는 이제 자체 npub도 갖게 되어, 프로젝트 자체가 자신이 문서화하는 프로토콜을 통해 발견될 수 있습니다. 여러 언어를 넘나드는 라이브러리 저자에게 다중 언어 스키마 패키지는 각 프로젝트가 별도의 스키마 복사본을 유지할 필요 없이 동일한 이벤트 kind 정의를 네이티브 import로 사용할 수 있음을 의미합니다.

## 릴리스

### Amethyst v1.06.0 and v1.06.1

vitorpamplona가 유지 관리하는 Android 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)가 3월 23일 [v1.06.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.0)과 [v1.06.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.1)을 출시했습니다. 핵심 기능은 [NIP-85](/ko/topics/nip-85/) (Trusted Assertions) 데이터를 사용한 가중 투표 방식의 투표 지원이며, 재설계된 poll 및 zap poll 카드가 포함됩니다. 새 렌더링은 일반 투표와 zap 가중 투표 모두에 더 깔끔한 시각적 배치를 제공합니다. 이어지는 v1.06.1은 투표 렌더링 경로에서 도입된 안정성 회귀를 해결하는 동시 수정 충돌 수정을 포함합니다.

### Amber v5.0.0 and v5.0.1

[NIP-55](/ko/topics/nip-55/) (Android Signer Application) 서명자 앱 [Amber](https://github.com/greenart7c3/Amber)가 최근 4.1.x 프리릴리스 작업을 안정 버전으로 승격해 3월 18일 [v5.0.0](https://github.com/greenart7c3/Amber/releases/tag/v5.0.0)을 출시했습니다. 이 안정 릴리스에는 지난주 다뤘던 [NIP-42](/ko/topics/nip-42/) relay 인증, 내장 Tor, 콘텐츠 타입별 권한, 암호화 PIN 저장 변경이 포함됩니다. 이어서 [v5.0.1](https://github.com/greenart7c3/Amber/releases/tag/v5.0.1)은 오프라인 빌드 flavor에서 인터넷 권한을 제거하여, 해당 빌드가 Android 권한 계층에서 네트워크 요청을 할 수 없게 합니다.

### Mostro v0.17.0 and Mostro Mobile v1.2.2

Nostr 기반 P2P Bitcoin 거래소 [Mostro](https://github.com/MostroP2P/mostro)가 3월 18일 [v0.17.0](https://github.com/MostroP2P/mostro/releases/tag/v0.17.0)을 출시했습니다. 서버 릴리스는 v0.16.x 주기의 분쟁 및 평판 작업을 이어가며, 구매자와 판매자에 대한 더 완전한 거래 평판 데이터를 Nostr 이벤트로 추가합니다. Flutter 클라이언트 [Mostro Mobile](https://github.com/MostroP2P/mobile)는 3월 23일 [v1.2.2](https://github.com/MostroP2P/mobile/releases/tag/v1.2.2)로 뒤따르며 최신 프로토콜 변경과 모바일 인터페이스를 맞추고 있습니다.

### Shosho v0.14.0

Nostr 라이브 스트리밍 앱 [Shosho](https://github.com/r0d8lsh0p/shosho-releases)가 3월 19일 Shosho Shop 출시와 함께 [v0.14.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.14.0)을 배포했습니다. 이 릴리스는 프로필에 Shop 탭, Browse 내 Shop, 라이브 및 클립에 In-Live Shop 버튼을 추가합니다. 릴리스 노트에 따르면 기존 "Nostr products"가 자동으로 표시되고 구매자는 구매를 위해 판매자의 Plebeian Market 페이지로 이동합니다. 다만 Shosho의 릴리스 노트는 목록 이벤트 kind를 식별하지 않으므로, Shosho Shop이 [Shopstr](https://github.com/shopstr-eng/shopstr)가 README에서 명시적으로 지원하는 것과 동일한 [NIP-99](/ko/topics/nip-99/) 분류 광고 목록을 읽는지 아직 확인할 수 없습니다.

### Applesauce v5.2.0

hzrd149의 Nostr 애플리케이션용 헬퍼 패키지 모음 [Applesauce](https://github.com/hzrd149/applesauce)가 3월 22일 [v5.2.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core@5.2.0)을 출시했습니다. 이 릴리스는 여섯 개 패키지에 걸쳐 있습니다. SQLite 패키지는 중복 삽입을 일으키던 이벤트 태그의 UNIQUE 제약 충돌을 수정합니다. signers 패키지는 [NIP-55](/ko/topics/nip-55/) 네이티브 Android signer 인터페이스를 감싸는 `AndroidNativeSigner`를 추가하여, 웹뷰 기반 앱이 커스텀 브리지 코드 없이 하드웨어 기반 서명을 사용할 수 있게 합니다. relay 패키지는 relay와 pool 상태 객체에 `challenge` 필드를 추가해 [NIP-42](/ko/topics/nip-42/) 인증 상태를 추적하므로, 앱이 relay가 인증을 요청하는 시점을 감지하고 프로그램적으로 대응할 수 있습니다. core 패키지는 이벤트 참조 중복 제거를 위한 `isEventPointerSame`과 `isAddressPointerSame` 메서드를 얻고, common 패키지는 사용자의 Blossom 미디어 서버를 해석하는 `user.blossomServers$`를 추가합니다. Applesauce는 noStrudel, Satellite, 그 외 여러 웹 클라이언트를 구동하므로, 이 수정은 웹 클라이언트 계층 전체에 전파됩니다.

### Wisp ships 16 releases in one week

Android Nostr 클라이언트 [Wisp](https://github.com/barrydeen/wisp)가 이번 주 [v0.9.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.9.3-beta)부터 [v0.13.1-beta](https://github.com/barrydeen/wisp/releases/tag/v0.13.1-beta)까지 16개의 릴리스를 배포했습니다. 추가된 기능에는 다중 계정 지원, 방해를 줄이는 zen 알림 모드, 초안 및 예약 게시, 안전 콘텐츠 필터, 새 flame 아이콘이 포함됩니다.

### Manent v1.2.0

비공개 암호화 노트 및 파일 저장 앱 [Manent](https://github.com/dtonon/manent)가 3월 20일 [v1.2.0](https://github.com/dtonon/manent/releases/tag/v1.2.0)을 출시했습니다. 이 릴리스는 앱에서 직접 카메라 촬영, 저장 비용을 줄이기 위한 업로드 전 이미지 크기 조정, 저장된 이미지를 검토하기 위한 pinch-to-zoom을 추가합니다. Manent는 사용자의 키페어를 사용해 노트와 파일을 Nostr relay에 암호화 저장하므로, 휴대폰이나 데스크톱 앱은 relay 데이터에서 전체 상태를 재구성할 수 있는 얇은 클라이언트가 됩니다.

### diVine 1.0.7

짧은 형식의 동영상 클라이언트 [diVine](https://github.com/divinevideo/divine-mobile)가 3월 21일 [1.0.7](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.7)을 출시하며, 멈춘 동영상을 자동 재개하는 비디오 재생 watchdog을 추가했습니다. [v1.0.6](/en/newsletters/2026-03-11-newsletter/#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import)의 E2E 테스트 인프라와 직접 MP4 로딩 이후, 이 릴리스는 오류를 던지지 않고 중간에 멈추는 동영상이라는 남은 재생 실패 경로를 겨냥합니다.

### Alby Extension v3.14.2

[NIP-07](/ko/topics/nip-07/) (Browser Extension Signer) 브라우저 확장인 [Alby Extension](https://github.com/getAlby/lightning-browser-extension)이 3월 18일 [v3.14.2](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.2)를 출시하며 Lightning 주소 QR 코드 표시와 Schnorr 서명을 추가했습니다. Schnorr 추가는 브라우저 확장을 Nostr가 기본적으로 사용하는 secp256k1 서명 체계와 맞춥니다.

### NoorNote v0.6.5 through v0.6.11

노트 작성 앱 [NoorNote](https://github.com/77elements/noornote)가 [v0.6.5](https://github.com/77elements/noornote/releases/tag/v0.6.5)부터 [v0.6.11](https://github.com/77elements/noornote/releases/tag/v0.6.11)까지 7개의 릴리스를 배포했습니다. 핵심 추가 사항은 Follow Packs입니다. 이는 사용자가 대량으로 탐색하고 구독할 수 있는 큐레이션된 계정 묶음으로, Twitter Lists와 유사하지만 온보딩을 위해 설계되었습니다. 사용자는 사용자 정의 제목, 설명, 커버 이미지를 갖춘 Follow Packs를 만들고, 편집하고, 공유할 수 있습니다. 이 시리즈는 또한 기본 Nostr 라이브러리를 NDK v2에서 v3로 업그레이드하여 relay 연결 처리와 구독 관리가 개선되었습니다. Picture notes와 재설계된 relay 연결 경험이 나머지를 채웁니다.

### nak v0.19.1 and v0.19.2

relay 상호작용, [NIP-19](/ko/topics/nip-19/) (Bech32-Encoded Entities) 식별자 인코딩과 디코딩, 이벤트 서명, relay 데이터 쿼리를 위한 fiatjaf의 커맨드라인 Nostr 도구킷 [nak](https://github.com/fiatjaf/nak)이 3월 17일과 20일 [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1), [v0.19.2](https://github.com/fiatjaf/nak/releases/tag/v0.19.2)를 출시했습니다. 이 두 포인트 릴리스는 지난주 [v0.19.0](/ko/newsletters/2026-03-18-newsletter/)의 그룹 포럼 UI 추가 이후를 잇습니다.

### Calendar by Form* v0.2.1

[NIP-52](/ko/topics/nip-52/) (Calendar Events) 기반 탈중앙화 캘린더 앱 [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)가 3월 20일 [v0.2.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.1)을 출시했습니다. 이 릴리스는 이벤트 알림에 영향을 주던 알림 템플릿 문제를 수정합니다. Calendar는 이벤트를 Nostr kind 31922(날짜 기반) 및 kind 31923(시간 기반) 이벤트로 저장하므로, 이 kind를 지원하기로 선택한 어떤 Nostr 클라이언트도 캘린더 데이터를 렌더링할 수 있습니다. 이 앱은 탈중앙화 폼 Formstr와 투표 앱 Pollerama도 유지하는 Formstr 팀이 구축했습니다.

### NYM v3.50 through v3.53

Bitchat과 브리지된 경량 일시적 채팅 클라이언트 [NYM](https://github.com/Spl0itable/NYM)이 v3.50부터 v3.53까지 28개의 릴리스를 배포했습니다. 가장 눈에 띄는 기능은 채널에서 `@nymbot` 멘션에 응답하고 relay 상태 및 관리 기능을 제공하는 내장 챗봇 Nymbot입니다. "hardcore mode"는 전송되는 각 메시지마다 새 키페어를 생성하여 대화 스레드를 신원 수준에서 연결할 수 없게 만듭니다. 대가도 분명합니다. 지속적 신원은 잃지만 메시지 단위 익명성을 얻습니다. relay 프록시 계층도 작업을 받았으며, 더 나은 연결성을 위한 샤딩 relay 프록시 워커, geohash 채널 지원, 시스템 시계가 부정확한 노드를 위한 clock skew 허용이 포함됩니다.

## 프로젝트 업데이트

### Ditto adds Bluesky bridge and Wikipedia integration

Soapbox 팀의 커스터마이즈 가능한 Nostr 소셜 클라이언트 [Ditto](https://github.com/soapbox-pub/ditto)가 이번 주 세 가지 뚜렷한 기능 트랙에 걸쳐 300개 이상의 커밋을 기록했습니다. 첫 번째는 Bluesky 브리지(19개 커밋)입니다. Bluesky 게시물을 전체 피드 스타일 스레드로 인라인 렌더링하고, 공식 Discover(whats-hot) 피드를 기반으로 하는 Bluesky 탐색 페이지에 사이드바 내비게이션을 추가하며, 댓글, 공유, 리액션, 링크 복사용 액션 버튼을 연결합니다. 사용자가 Ditto 내부에서 Bluesky 게시물에 답글을 달면 작성 모달은 이 상호작용의 크로스 프로토콜 성격을 알리는 면책 안내를 표시합니다. [NIP-73](/ko/topics/nip-73/) (External Content IDs) kind 17 리액션이 이 크로스 프로토콜 모델을 구동합니다. Nostr 사용자가 Bluesky 게시물에 반응하면, 그 리액션은 외부 콘텐츠 식별자를 참조하는 표준 Nostr 이벤트로 저장됩니다. 이는 Bluesky 게시물에서 YouTube 동영상, 웹페이지에 이르기까지 어떤 외부 콘텐츠에 대한 반응도 브리지할 수 있는 동일한 NIP-73 패턴입니다.

두 번째 트랙은 Wikipedia 통합(9개 커밋)입니다. Ditto는 이제 일반 링크 미리보기 대신 세부 페이지에서 풍부한 Wikipedia 문서 콘텐츠를 렌더링하고, 문서 썸네일이 포함된 검색 자동완성을 추가하며, Wikipedia API에서 추천 콘텐츠를 끌어오는 `/wikipedia` 페이지를 제공합니다. Wikipedia와 Archive.org 결과도 일반 검색 자동완성 드롭다운에 나타납니다. 세 번째 트랙은 Capacitor를 통한 iOS 플랫폼 지원으로, 원격 빌드 스크립트와 플랫폼 구성이 UI 전면 개편(55개 커밋)과 함께 반영되었습니다. 이 개편은 앱의 모든 페이지에서 backdrop-blur 헤더를 새로운 arc 기반 내비게이션 디자인으로 대체합니다. 총 314개의 커밋은 Ditto를 Nostr 전용 클라이언트에서, Bluesky와 Wikipedia를 Nostr 피드와 나란한 일급 콘텐츠 소스로 취급하는 다중 프로토콜 집계기로 옮겨갑니다.

### Pika builds a NIP-34 forge CI pipeline

Marmot 기반 암호화 메시징 앱 [Pika](https://github.com/sledtools/pika)가 사전 병합 CI가 포함된 자체 호스팅 [NIP-34](/ko/topics/nip-34/) forge에 집중한 33개의 PR을 이번 주 병합했습니다. 이 forge는 NIP-34 이벤트로 패치를 수신하고, 병합 전에 CI 검사를 실행하며, 구조화된 상태를 Nostr 이벤트를 통해 다시 보고하는 git 호스팅 계층입니다. [PR #701](https://github.com/sledtools/pika/pull/701)은 lane 기반 사전 병합 및 야간 CI를 추가하며, 각 코드 경로(Rust, TypeScript, Apple 빌드)가 독립적인 성공/실패 상태를 가진 자체 lane에서 실행됩니다. [PR #715](https://github.com/sledtools/pika/pull/715)은 격리를 위해 관리형 CI 에이전트를 Incus OpenClaw 컨테이너로 전환하고, [PR #733](https://github.com/sledtools/pika/pull/733)은 커맨드라인에서 호스팅된 forge와 상호작용하기 위한 `ph forge` CLI를 추가합니다. 지원 PR은 병합용 저장소 쓰기 권한([PR #736](https://github.com/sledtools/pika/pull/736)), 라이브 상태 배지가 포함된 구조화된 CI 메타데이터([PR #722](https://github.com/sledtools/pika/pull/722)), Apple 야간 빌드 분리([PR #738](https://github.com/sledtools/pika/pull/738)), forge 인증 및 브랜치 조회 수정([PR #734](https://github.com/sledtools/pika/pull/734))을 처리합니다. 이는 NIP-34 git 이벤트 위에 구축된 최초의 실동 CI/CD 시스템 중 하나로, Nostr 기반 소스 코드 호스팅을 기본 패치 교환에서 개발자가 GitHub나 GitLab에서 기대하는 병합 및 테스트 워크플로로 확장합니다.

### Nostria adds communities, code snippets, and voice event handling

sondreb가 유지 관리하는 크로스 플랫폼 Nostr 클라이언트 [Nostria](https://github.com/nostria-app/nostria)는 #14에서 다룬 Web of Trust 필터링을 넘어 이번 주 앱 표면을 확장했습니다. 핵심 추가 사항은 커뮤니티 생성, 모더레이터 및 relay 구성, 이미지 미리보기가 포함된 게시 승인 추적, Posts와 Moderators 탭이 있는 전용 커뮤니티 페이지를 포함한 완전한 [NIP-72](/ko/topics/nip-72/) (Moderated Communities) 구현입니다.

같은 기간에는 구문 강조 편집기가 포함된 코드 스니펫 렌더링 및 편집, 오디오 대화를 위한 음성 이벤트 답글 지원, 다이렉트 메시지용 채팅 relay 설정, Web Share API를 통한 채널 공유, 미디어 플레이어용 툴바 도킹 시스템, 최신 Brainstorm Web of Trust 서비스용 인앱 가입, NWC와 BOLT-11 인보이스를 사용한 DM 내 송금 및 수금 흐름, Nostr 네이티브 GIF 처리, 팟캐스트 피드의 기존 Lightning 분할을 가져올 수 있는 더 강력한 음악가용 RSS 임포트 경로도 추가되었습니다.

### nostr-vpn rapid iteration

[초기 출시](#nostr-vpn-launches-as-a-tailscale-alternative)를 넘어서, [nostr-vpn](https://github.com/mmalmi/nostr-vpn)의 커밋 로그는 실제 배포 중 맞닥뜨린 구체적 문제를 보여줍니다. [v0.2.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.3)부터 [v0.2.5](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.5)까지는 초기 설치 스크립트와 크로스 플랫폼 CLI를 추가했습니다. [v0.2.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.6)과 [v0.2.7](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.7)은 Windows 지원을 도입했고, 그 과정에서 설정 쓰기를 위한 UAC 경로 인용과 데몬 소유 설정 업데이트가 필요했습니다. [v0.2.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.8)부터 [v0.2.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.10)까지는 Windows GUI 서비스 동작, CLI 서브프로세스 처리, 머신 범위 서비스 구성 문제를 수정했습니다. [v0.2.12](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.12)는 LAN 탐색을 timed LAN pairing으로 대체했습니다. 이는 동일한 로컬 네트워크에 있는 두 장치가 relay 신호 없이 사용자 주도로 페어링하는 흐름입니다. 패턴은 전형적인 초기 단계 현장 테스트입니다. 각 릴리스가 특정 배포 실패를 겨냥하고, 사용자 기반이 일일 반복이 가능할 만큼 작으며, 개발자 자신이 릴리스 사이에 이 도구를 직접 사용하고 있습니다.

### Comet automated builds

Nodetec의 Nostr 네이티브 장문 작성 도구 [Comet](https://github.com/nodetec/comet)(구 Captain's Log)가 이번 주 40개가 넘는 자동화된 알파 빌드를 생성했습니다. Comet은 [NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md) 장문 글을 작성하고 게시하기 위한 데스크톱 앱으로, 로컬 초안 저장, 마크다운 편집, 사용자의 relay 세트로 원클릭 게시를 제공합니다. 자동 빌드 파이프라인은 main 브랜치의 모든 커밋에 대해 태그된 릴리스를 생성하므로, 순수 릴리스 수는 기능 속도를 측정하는 지표로는 오해의 소지가 있습니다. 40개의 빌드가 보여주는 것은 앱이 매일 활발히 개발되고 있으며, 각 커밋이 몇 분 안에 테스트, 패키징, 다운로드 가능 상태가 된다는 점입니다.

## NIP 업데이트

3월 17일부터 24일까지 [NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

3월 18일부터 3월 24일까지 병합된 NIP는 없었습니다.

**해당 기간 동안 업데이트된 오픈 PR 및 논의:**

- **NIP-AA: Nostr 위의 자율 에이전트** ([PR #2259](https://github.com/nostr-protocol/nips/pull/2259)): Nostr 네트워크에서 동작하는 자율 에이전트를 위한 규약을 제안합니다. 이 PR은 에이전트가 자신을 식별하고, 서비스를 발견하며, Nostr 이벤트를 통해 다른 에이전트 및 인간과 조율하는 방법을 정의합니다.

- **[NIP-50](/ko/topics/nip-50/) (검색): 정렬 확장** ([PR #2283](https://github.com/nostr-protocol/nips/pull/2283)): NIP-50 검색 쿼리에 top, hot, zaps, new를 포함한 정렬 파라미터를 추가합니다. 이를 통해 클라이언트는 전체 텍스트 검색을 지원하는 relay에서 결과를 클라이언트 측 정렬 대신 순위화된 형태로 요청할 수 있습니다.

- **NIP-A5: WASM 프로그램** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Nostr 위에서 WebAssembly 프로그램을 게시하고 발견하기 위한 규약을 제안합니다. WASM 바이너리는 Nostr 이벤트로 배포될 수 있으며, relay는 이식 가능한 실행 코드의 탐색 계층 역할을 할 수 있습니다.

- **NIP-CF: Combine Forces 상호운용 가능한 napps** ([PR #2277](https://github.com/nostr-protocol/nips/pull/2277)): 서로 다른 클라이언트와 서비스 전반에서 기능을 조합할 수 있는 상호운용 가능한 Nostr 애플리케이션("napps")을 위한 규약을 정의합니다.

- **Snapshots NIP** ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279)): relay 동기화와 백업을 위한 relay 상태 스냅샷 메커니즘을 제안합니다.

- **Checkpoints NIP** ([PR #2278](https://github.com/nostr-protocol/nips/pull/2278)): snapshots 제안을 보완하는, 알려진 양호한 relay 상태를 표시하는 checkpoint 이벤트를 제안합니다.

- **[NIP-58](/ko/topics/nip-58/) (Badges): Badge Sets 리팩터링** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): 배지 컬렉션이 조직되고 참조되는 방식을 재구성합니다.

- **[NIP-11](/ko/topics/nip-11/) (Relay Information Document): 확장** ([PR #2280](https://github.com/nostr-protocol/nips/pull/2280)): 더 풍부한 기계 판독 가능한 relay 메타데이터를 위해 relay 정보 문서에 추가 필드를 넣습니다.

## Five Years of Nostr Marches

[지난달 뉴스레터](/ko/newsletters/2026-03-04-newsletter/#five-years-of-nostr-februaries)는 NIP-01(기본 프로토콜 흐름) 재작성부터 Damus App Store 물결, 메시 네트워킹, 에이전트 제안까지 Nostr의 2월이 어떻게 전개되었는지 다뤘습니다. 이번 회고는 2021년부터 2026년까지 각 3월에 무슨 일이 일어났는지 추적합니다.

### March 2021: Two Commits

존재한 지 네 달째이던 Nostr의 2021년 3월은 프로토콜 저장소에 단 두 개의 커밋만 남겼고, 둘 다 3월 4일에 이루어졌습니다. fiatjaf는 [nostwitter 인스턴스 링크를 추가](https://github.com/nostr-protocol/nostr/commit/dcd8cc3)해 초기 방문자를 실제 배포 지점으로 안내했고, [기본 필터 정의에 kind를 추가](https://github.com/nostr-protocol/nostr/commit/54dfb46)했습니다. 두 번째 커밋은 특히 의미심장합니다. 2021년 3월에는 Nostr 이벤트를 kind별로 필터링할 수조차 없었습니다. 프로토콜은 그만큼 원시적이었습니다. 네트워크는 두세 개 relay로 운영되었고, Telegram 그룹이 유일한 조정 채널이었습니다. NIPs 저장소는 아직 존재하지 않았으며, 프로토콜 제안은 메인 nostr 저장소의 파일로 존재했습니다. 그달 커미터는 fiatjaf 한 명뿐이었습니다. 5년 뒤 VPN, 멀티플레이어 게임, 메시 네트워킹을 지원하게 될 프로토콜의 2021년 3월 전체 산출물이 하나의 git diff에 들어갑니다.

### March 2022: Pre-Damus Building

메인 프로토콜 저장소는 2022년 3월에 커밋이 0개였습니다. 개발은 도구 저장소로 완전히 이동해 있었습니다. 당시 주요 Nostr 인터페이스였던 fiatjaf의 Vue.js 웹 클라이언트 [Branle](https://github.com/fiatjaf/branle)은 Docker 배포 지원과 [NIP-05](/ko/topics/nip-05/) (DNS-Based Verification) 표시 이름 수정처럼 `_@` 접두사를 제거하는 검증 배지 개선을 포함해 5개의 커밋을 받았습니다. Robert C. Martin의 Clojure 데스크톱 클라이언트 [more-speech](https://github.com/unclebob/more-speech)는 스레딩, 키보드 내비게이션, 편집 창을 추가하며 13개 이상의 커밋을 기록했습니다. 그달 Nostr 위에서 적극적으로 개발한 가장 유명한 소프트웨어 저자는 암호화폐 개발자가 아니라, 수백만 부가 팔린 "Clean Code"의 저자였습니다. 그는 Clojure로 Nostr 클라이언트를 쓰고 있었습니다. 이 언어 선택은 초기 커뮤니티의 성격을 거의 그대로 보여줍니다. 자기 자신을 위해 만드는 고집 있는 프로그래머들의 집합이었습니다.

relay 네트워크는 약 15개 relay와 수백 명 수준의 활성 사용자 기반으로 확장되어 있었습니다. Damus는 아직 존재하지 않았고 2022년 4월이 되어서야 만들어집니다. Nostream도 아직 나타나지 않았습니다. 그달의 작업은 인프라였습니다. 이미 매일 이 도구를 사용하고 있던 작은 커뮤니티를 위해 기존 도구를 더 신뢰성 있게 만드는 작업이었습니다.

### March 2023: Post-Explosion Infrastructure

Damus App Store 물결과 30만 개 공개 키를 넘긴 급증 이후 한 달이 지난 2023년 3월은 그 성장 충격을 흡수하는 달이었습니다. [NIPs 저장소](https://github.com/nostr-protocol/nips)는 프로토콜 역사상 두 번째로 많은 28개의 pull request를 병합했습니다. [NIP-51](/ko/topics/nip-51/) (Lists)이 병합되어 클라이언트에 구조화된 팔로우, 뮤트, 북마크 컬렉션을 제공했고, [NIP-39](/ko/topics/nip-39/) (External Identities in Profiles)가 도입되었으며, NIP-78(Application-Specific Data)은 비공개 상태가 필요한 앱에 범용 저장 kind를 제공했고, [NIP-57](/ko/topics/nip-57/) (Lightning Zaps)의 재작성([PR #392](https://github.com/nostr-protocol/nips/pull/392))은 zap 흐름을 통합하고 용어를 명확히 했습니다. 그달 가장 많이 논의된 PR은 50개가 넘는 댓글이 달린 대체 멘션 처리 제안([PR #381](https://github.com/nostr-protocol/nips/pull/381))이었습니다.

그달 가장 영향력이 컸던 새 프로젝트는 relay 연결, 이벤트 서명, 캐싱, 구독 관리를 위한 TypeScript 라이브러리 [NDK](https://github.com/nostr-dev-kit/ndk)였습니다. pablof7z는 2023년 3월 16일 [초기 커밋](https://github.com/nostr-dev-kit/ndk/commit/09e5e03)을 만들었고, 11일 뒤인 3월 27일에는 이를 처음부터 다시 썼으며("basically another initial commit"), 3월 31일까지 LNURL과 zap 지원을 동작시키고 있었습니다. NDK는 15일 만에 아무것도 없는 상태에서 zap 가능 상태로 갔습니다. NDK가 만들어진 지 5일 뒤인 3월 21일, Alby 팀은 [NIP-47](/ko/topics/nip-47/)의 참조 구현인 [NWC](https://github.com/getAlby/nostr-wallet-connect) (Nostr Wallet Connect)를 만들었고, 이는 Lightning 지갑을 Nostr 애플리케이션에 연결했습니다. 이후 3년간 웹 기반 Nostr 개발을 떠받치게 될 두 프로젝트가 같은 30일 창 안에서 태어났습니다. OpenSats는 아직 Nostr 펀드를 시작하지 않았으며, 첫 번째 물결은 NDK가 만들어진 지 네 달 뒤인 [2023년 7월](https://opensats.org/blog/nostr-grants-july-2023)에 도착합니다.

그달의 다른 주목할 만한 생성물로는 NostrGit, NostrChat, LNbits의 nostr-signing-device 프로젝트, nostrmo가 있었습니다. 지능형 relay 선택에 초점을 둔 Rust 데스크톱 클라이언트 [Gossip](https://github.com/mikedilger/gossip)은 세 번의 릴리스를 냈습니다. 프로토콜은 빌드 모드에 있었고, 2023년 3월에 만들어진 도구들은 3년이 지난 지금도 여전히 사용되고 있습니다.

### March 2024: Protocol Maturation

2024년 3월은 프로토콜을 장기 사용에 맞게 다듬는 시기였습니다. NIPs 저장소는 12개의 pull request를 병합했습니다. 가장 중요한 것은 130개 이상의 댓글과 44일의 검토 끝에 3월 5일 병합된 [NIP-34](/ko/topics/nip-34/) (Git Stuff), [PR #997](https://github.com/nostr-protocol/nips/pull/997)였습니다. 논의 스레드는 탈중앙화 GitHub를 어떻게 만들 것인지에 대한 커뮤니티 토론의 타임캡슐입니다. jb55는 `git send-email`과의 유사성을 언급했고, Giszmo는 교차 포크 탐색을 위해 루트 커밋 해시를 사용하자고 제안했으며("GitHub는 하지 않는 것이고 우리는 할 수 있다"), mikedilger는 SSH 키 대신 [NIP-98](/ko/topics/nip-98/) (HTTP Auth) 이벤트 서명 인증을 제안했고, fiatjaf는 버전 관리 일반성의 필요성을 단호하게 부인했습니다. "각 버전 관리 시스템을 위한 게 아니라 git만을 위한 것이다. 다른 건 아무도 쓰지 않는다." PR을 연 지 몇 시간 안에 fiatjaf는 이미 nak, go-nostr, gitstr이 Nostr를 통한 패치를 수용하도록 바꿨습니다. 당시 이미 OpenSats 그랜티였던 ngit의 DanConwayDev는 토론에서 가장 활발한 기여자 중 하나였습니다. 프로필 메타데이터용 봇 필드도 병합되어, 클라이언트가 자동 계정과 인간 계정을 기계적으로 구분할 수 있게 되었습니다.

[Amethyst](https://github.com/vitorpamplona/amethyst)는 git 이벤트 지원, 위키 문서, 의료 데이터 렌더링, 콘텐츠 편집을 하나의 릴리스에 담은 v0.85.0을 배포했습니다. [Mostro](https://github.com/MostroP2P/mostro)는 v0.10.0에 도달했습니다. Cloudflare Workers 위에서 구동되는 서버리스 Nostr relay [Nosflare](https://github.com/Spl0itable/nosflare)는 relay 로직이 edge에서 돌아갈 수 있음을 보여주었습니다. OpenSats는 Amethyst 클라이언트에 대한 지속적인 기여를 위해 Bruno Garcia에게 [Long-Term Support grant](https://opensats.org/blog/bruno-garcia-receives-lts-grant)를 발표했습니다.

### March 2025: Infrastructure Expansion

2025년 3월에는 10개의 NIP가 병합되었습니다. 핵심은 [NIP-66](/ko/topics/nip-66/) (Relay Discovery and Liveness Monitoring), [PR #230](https://github.com/nostr-protocol/nips/pull/230)로, 25개월 여정 끝에 3월 3일 병합되었습니다. dskvr는 2023년 2월에 relay 모니터링을 처음 제안했고, 클라이언트 측에서 처리할 수 있다는 반응을 받았으며, 개별 클라이언트가 수천 개 relay에 동시에 연결하는 것이 왜 비현실적인지 설명했고, 일곱 번의 완전한 초안을 거쳤으며, 미국 북동부, 브라질, 미국 서부, 미국 동부, 호주, 인도, 한국, 남아프리카의 여덟 지역에 모니터링 노드를 구축했고, relay 도구 체인이 따라오기를 기다렸습니다. 병합될 무렵에는 이미 nostr.watch, relaypag.es, monitorlizard, Snort, noStrudel, Jumble에 구현이 존재했습니다. NIP-66 데이터는 나중에 [뉴스레터 #12](/ko/newsletters/2026-03-04-newsletter/#outbox-모델-분석)에서 다룬 Nostrability outbox 벤치마크를 구동하게 됩니다. NIP-C0(Code Snippets)도 병합([PR #1852](https://github.com/nostr-protocol/nips/pull/1852), 댓글 63개)되어 소스 코드 공유를 위한 kind 1337 이벤트를 추가했습니다.

이달에는 Nostr용 첫 MCP 서버들도 등장했습니다. [nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)는 3월 23일, [nwc-mcp-server](https://github.com/getAlby/nwc-mcp-server)는 3월 14일에 나타났으며, 이는 Anthropic이 2024년 11월 Model Context Protocol을 발표한 지 불과 4개월 뒤였습니다. 이 초기 브리지는 2025년 말과 2026년 초에 이어진 완전한 [ContextVM](/ko/topics/contextvm/) SDK와 에이전트 상거래 작업에 앞섰습니다.

[Gossip](https://github.com/mikedilger/gossip)은 v0.14.0을 배포했습니다. relay 인지형 피드 관리에 초점을 둔 hodlbod의 웹 클라이언트 [Coracle](https://github.com/coracle-social/coracle)은 세 차례 릴리스를 냈습니다. OpenSats는 [열 번째 Nostr grants 물결](https://opensats.org/blog/10th-wave-of-nostr-grants)을 발표하며 2023년 중반부터 이어진 자금 흐름을 계속했습니다.

### March 2026: Convergence

*2026년 3월 활동은 Nostr Compass [#12](/ko/newsletters/2026-03-04-newsletter/)부터 [#15](#)호(이번 호)까지의 이슈에서 가져왔습니다.*

2026년 3월은 서로 흩어져 있던 흐름이 실동 시스템으로 수렴한 달입니다. [Marmot Development Kit](/ko/newsletters/2026-03-04-newsletter/#marmot-development-kit-첫-공개-릴리스-출시)은 암호화 미디어, 다중 언어 바인딩, 그리고 사양, Rust, TypeScript 전반의 조율된 업데이트가 필요했던 ChaCha20-Poly1305 마이그레이션과 함께 첫 공개 릴리스를 냈습니다. [Shopstr와 Milk Market](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)는 에이전트 주도 구매를 위한 MCP 상거래 인터페이스를 추가했습니다. [NIP-42](/ko/topics/nip-42/) relay 인증은 [Amber](/en/newsletters/2026-03-11-newsletter/#nip-42-relay-auth-across-bunker-signer-and-relay), strfry, OAuth Bunker에 동시에 도입되어 signer, relay, bunker 소프트웨어 사이의 고리를 닫았습니다. [Notedeck](/ko/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr)은 [NIP-94](/ko/topics/nip-94/) (File Metadata) 릴리스 이벤트를 사용한 Nostr 네이티브 소프트웨어 업데이트를 출시했습니다.

이번 주에는 [BigBrotr](#bigbrotr-maps-exposed-private-keys-across-the-relay-network)가 유출된 개인 키를 찾기 위해 전체 relay 네트워크를 스캔하고 분석과 DVM 검사기를 모두 공개했습니다. [Nostr VPN](#nostr-vpn-launches-as-a-tailscale-alternative)은 Nostr의 키 모델이 소셜 미디어만이 아니라 네트워크 인프라에도 작동함을 보여주었습니다. [DOOM](#open-source-doom-runs-peer-to-peer-over-nostr)은 Nostr 탐색, Marmot 암호화, QUIC 전송이 실시간 멀티플레이어 게임을 구동할 수 있음을 입증했습니다. [Amber](#amber-v500-and-v501)는 v5.0.0으로 도약했고, [Wisp](#wisp-ships-16-releases-in-one-week)는 7일 동안 16개의 릴리스를 냈습니다. 한 주 동안 주요 프로젝트에서 25개가 넘는 태그 릴리스가 나왔습니다.

그달 첫 24일 동안 7개의 NIP가 병합되었습니다. 프로토콜은 [NIP-54](/ko/topics/nip-54/) (Wiki) Djot 마크업, [NIP-19](/ko/topics/nip-19/) (Bech32-Encoded Entities) 입력 제한, [NIP-91](/ko/topics/nip-91/) (AND Operator for Filters) 불리언 쿼리 로직, [NIP-85](/ko/topics/nip-85/) (Trusted Assertions) Web of Trust assertions를 추가했습니다. 오픈 제안은 자율 에이전트(NIP-AA)부터 WASM 프로그램(NIP-A5), [NIP-50](/ko/topics/nip-50/)용 검색 정렬 확장까지 걸쳐 있습니다.

### Looking Ahead

Nostr의 다섯 번의 3월은 분명한 궤적을 그립니다. 2021년에는 한 사람이 kind별 이벤트 필터링조차 안 되던 프로토콜에 두 개의 커밋을 남겼습니다. 2023년에는 Damus 이후의 폭증을 흡수하기 위해 NDK와 NWC가 5일 간격으로 탄생했습니다. 2024년에는 141개 댓글이 달린 PR 스레드가 소셜 프로토콜 위에서 git 협업이 어떻게 작동해야 하는지를 토론했습니다. 2025년에는 25개월 동안 일곱 번 다시 쓰인 relay 모니터링 사양이 마침내 병합되었습니다. 2026년에는 누군가 Tailscale이 계정을 요구하는 데 질려서 Nostr 키페어를 사용하는 VPN을 만들었고, 또 다른 누군가는 Nostr relay를 통해 피어를 발견하고 Marmot로 게임 플레이를 암호화하는 멀티플레이어 DOOM을 배포했습니다. 1,085개 relay에서 4,100만 개 이벤트를 스캔한 BigBrotr의 결과는 네트워크가 얼마나 성장했는지에 대한 구체적인 측정치를 제공합니다. 2026년 3월의 프로토콜 표면적은 2021년 3월의 눈으로 보면 거의 알아볼 수 없을 정도로 넓어졌지만, secp256k1 키로 서명된 이벤트를 relay를 통해 배포한다는 기본 모델은 변하지 않았습니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 공유할 뉴스가 있다면 <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ko/topics/nip-17/) (Private Direct Messages) DM으로 연락하시거나</a> Nostr에서 찾아주세요.
