---
title: 'Nostr Compass #11'
date: 2026-02-25
translationOf: /en/newsletters/2026-02-25-newsletter.md
translationDate: 2026-02-25
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0)이 160개 이상의 개선 사항과 함께 실시간 메시지 전송과 Amber 서명자 지원을 도입했습니다. [diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5)는 동영상 재생 문제를 수정하고 크리에이터 애널리틱스를 위한 Kind 22236 view event를 추가했습니다. [Pika](https://github.com/sledtools/pika), [Ridestr](https://github.com/variablefate/ridestr), [Unfiltered](https://github.com/dmcarrington/unfiltered)가 업데이트를 출시했습니다. [FIPS](https://github.com/jmcorgan/fips)는 Nostr 네이티브 메시 네트워킹의 작동하는 Rust 구현을 공개했습니다. Notecrumbs는 damus.io 링크 미리보기의 안정성 수정을 받았습니다. [ContextVM](https://contextvm.org)은 Nostr와 Model Context Protocol을 연결합니다. 새 프로젝트로는 AI 에이전트와 인간 간 MLS 암호화 메시지를 위한 [Burrow](https://github.com/CentauriAgent/burrow)와 브라우저 기반 볼트 및 신원 관리를 위한 [Nostria Signer](https://github.com/nostria-app/nostria-signer-extension)가 있습니다. 심층 분석은 NIP-55 Android 서명과 NIP-60 Cashu 지갑 동기화를 다룹니다.

## 뉴스

### Notecrumbs 안정성 개선

damus.io 링크 미리보기를 구동하는 Nostr API 및 웹 서버 [Notecrumbs](https://github.com/damus-io/notecrumbs)가 안정성 문제를 해결하는 일련의 수정을 받았습니다.

[동시성 수정](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49)은 inflight 중복 제거 메커니즘을 watch 채널로 교체했습니다. 동일한 노트를 요청하는 두 호출자가 모두 fetcher가 되어, 한쪽이 다른 쪽이 알림을 구독하기 전에 완료되면 데드락이 발생할 수 있었습니다. 원자적 연산과 함께 watch 채널을 사용하면 오직 하나의 fetcher만 실행되고 나머지는 결과를 기다립니다.

[속도 제한](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17)은 relay 과부하에 대한 2단계 방어를 구현합니다. 사용자가 동일한 노트에 반복적으로 접근하면 시스템이 5분 쿨다운 윈도우로 relay 요청을 디바운스합니다. 이 보호는 모든 [NIP-19](/ko/topics/nip-19/) 유형과 프로필 피드에 적용되어 트래픽이 많을 때 relay로의 비례적 스팸을 방지합니다.

[성능 개선](https://github.com/damus-io/notecrumbs/commit/38670b3972b6)은 보조 데이터 가져오기를 백그라운드 tokio 작업으로 이동했습니다. 페이지가 7.5초까지 누적될 수 있던 순차적 relay 타임아웃을 기다리지 않고 캐시된 데이터로 즉시 렌더링됩니다. nostrdb 0.10.0 업그레이드가 이 수정들과 함께 이루어졌습니다.

### ContextVM: Nostr를 통한 MCP

[ContextVM](https://contextvm.org)은 Nostr와 [Model Context Protocol](https://modelcontextprotocol.io/) (MCP)을 연결하는 도구 모음입니다. 최근 커밋으로 결제를 지원하는 새로운 [CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/) 명세가 도입되었으며, 2월 내내 [SDK](https://github.com/ContextVM/sdk) 개선이 이루어지고 있습니다.

SDK는 Nostr를 통한 MCP용 TypeScript 클라이언트 및 서버 transport를 제공합니다. 개발자는 Nostr 네트워크 전반에 MCP 서버를 노출할 수 있고, 클라이언트는 이에 연결할 수 있습니다. Relay는 암호화된 event를 맹목적으로 라우팅하는 메시지 버스 역할을 합니다. 네이티브 Nostr 지원이 없는 클라이언트는 프록시 레이어를 통해 연결합니다. 라이브러리는 relay 관리와 event 인증을 위한 암호화 서명을 처리하며, Node.js와 브라우저 환경 모두에서 작동합니다.

[CVMI](https://github.com/ContextVM/cvmi)는 서버 검색과 메서드 호출을 위한 CLI를 제공합니다. [Relatr](https://github.com/ContextVM/relatr)는 소셜 그래프 거리와 프로필 검증을 결합하여 개인화된 신뢰 점수를 계산합니다.

ContextVM은 브리지 레이어로 자리매김하고 있습니다. 기존 MCP 서버는 기존 transport를 유지하면서 Nostr 상호운용성을 얻습니다.

### White Noise, 탈중앙화 사용자 검색 문서화

[jgmontoya의 블로그 게시물](https://blog.jgmontoya.com/2026/02/22/user-search.html)은 [White Noise](https://github.com/marmot-protocol/whitenoise)가 탈중앙화 relay 네트워크 전반에서 사용자 검색을 처리하는 방식을 자세히 설명합니다.

프로필 배포가 핵심 과제입니다. 통합 데이터베이스를 갖춘 중앙화 메신저와 달리, Nostr 프로필은 중앙 인덱스 없이 수십 개의 relay에 분산됩니다. White Noise는 병렬로 실행되는 생산자-소비자 아키텍처로 이를 해결합니다.

생산자 프로세스는 사용자의 팔로우에서 출발하여 소셜 그래프를 지속적으로 확장하고, 증가하는 거리에서 팔로우 목록을 가져와 발견된 pubkey를 프로필 해석 큐에 추가합니다. 소비자는 점점 비용이 증가하는 5단계로 일치를 해석합니다. 로컬 사용자 테이블(가장 빠름), 이전 검색에서 캐시된 프로필, 연결된 relay, [NIP-65](/ko/topics/nip-65/)에 따른 사용자 relay 목록, 사용자가 선언한 relay에 대한 직접 쿼리(가장 느림) 순입니다.

콜드 검색은 약 3초가 걸리고, 캐시에서의 웜 검색은 약 10밀리초로 줄어듭니다. 확립된 소셜 그래프가 없는 신규 사용자의 경우 시스템이 잘 연결된 부트스트랩 노드를 주입하며, 그룹 멤버십은 명시적 팔로우 외에 암묵적 소셜 신호로도 작용합니다.

저자는 계측이 최적화에 결정적이었다고 언급하며, 메트릭 없이는 개선이 추측에 불과했다고 말합니다.

### FIPS: Nostr 네이티브 메시 네트워킹

[FIPS](https://github.com/jmcorgan/fips)(Free Internetworking Peering System)는 Nostr 키쌍(secp256k1)을 노드 신원으로 사용하는 자기 조직 메시 네트워크의 작동하는 Rust 구현으로, [설계 문서](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)가 기능하는 코드와 함께 제공됩니다.

이 프로토콜은 인프라 독립성을 다룹니다. 노드는 중앙 서버나 인증 기관 없이 자동으로 서로를 발견하며, 스패닝 트리가 좌표 기반 라우팅을 제공하고 bloom filter가 도달 가능성 정보를 전파하여 노드가 로컬 지식만으로 포워딩 결정을 내릴 수 있게 합니다. Transport 불가지론성은 같은 프로토콜이 UDP, 이더넷, 블루투스, LoRa 라디오, 또는 데이터그램 가능한 어떤 매체에서도 작동한다는 의미입니다.

두 암호화 레이어가 트래픽을 보호합니다. 링크 계층 암호화(Noise IK 패턴)는 상호 인증과 순방향 비밀성으로 이웃 간 홉별 통신을 보호합니다. 세션 계층 암호화(Noise XK 패턴)는 중간 라우터에 대한 종단 간 보호를 제공하며, 목적지만이 페이로드를 복호화할 수 있습니다. 이는 TLS가 신뢰할 수 없는 네트워크를 통과할 때도 HTTP 트래픽을 보호하는 방식과 유사합니다.

아키텍처는 라우팅에 "탐욕적 임베딩" 스패닝 트리를 사용합니다. 각 노드는 트리 루트와 부모에 대한 상대적 위치를 기반으로 좌표를 받습니다. 패킷은 목적지에 더 가까운 좌표를 향해 탐욕적으로 라우팅되며, bloom filter가 도달 가능한 엔드포인트를 알립니다. 탐욕적 라우팅이 실패하면(로컬 최솟값), 노드는 트리 기반 경로로 대체할 수 있습니다.

Rust 구현은 이미 bloom filter 검색을 갖춘 UDP transport를 포함합니다. 향후 작업은 피어 부트스트래핑을 위한 Nostr relay 통합을 목표로 합니다.

## 릴리스

이번 주에는 relay 인프라와 클라이언트 애플리케이션 전반에 걸친 릴리스가 있었으며, 새 프로젝트도 등장했습니다.

### HAVEN v1.2.0

네 가지 relay 기능과 [Blossom](/ko/topics/blossom/) 미디어 서버를 번들로 제공하는 올인원 개인 relay [HAVEN](https://github.com/bitvora/haven)이 [v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0)을 출시했습니다. 이 릴리스는 [지난주 다룬](/ko/newsletters/2026-02-18-newsletter/#haven-v120-rc3) RC 단계를 벗어납니다.

다중 npub 지원으로 단일 HAVEN 인스턴스가 화이트리스트를 통해 여러 Nostr 신원을 서비스할 수 있으며, 접근 제어를 위한 새 블랙리스트 기능도 추가되었습니다. 다시 작성된 백업 시스템은 이식 가능한 JSONL 형식을 사용하며, JSONL 파일에서 노트를 가져오는 `haven restore` 명령이 제공됩니다. 클라우드 스토리지 통합으로 원격 백업 관리를 위한 `--to-cloud` 및 `--from-cloud` 플래그가 추가되었습니다.

[Web of Trust](/ko/topics/web-of-trust/) 개선 사항으로는 신뢰 계산을 위한 구성 가능한 깊이 수준과 메모리 오버헤드를 줄이는 잠금 없는 최적화를 갖춘 자동 24시간 새로 고침 간격이 포함됩니다. relay 요청을 위한 사용자 에이전트 구성과 구성 가능한 Blastr 타임아웃 설정, 압축된 JSONL로의 데이터 내보내기가 릴리스를 완성합니다.

### White Noise v0.3.0

[MLS](/ko/topics/mls/) 기반 암호화 메시징 앱으로 [Marmot](/ko/topics/marmot/) 프로토콜을 구현하는 [White Noise](https://github.com/marmot-protocol/whitenoise)가 160개 이상의 개선 사항과 함께 [v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0)을 출시했습니다.

이 릴리스는 폴링 대신 스트리밍 연결을 통한 실시간 메시지 전송을 도입하여 메시지가 즉시 도착합니다. Amber 지원([NIP-55](/ko/topics/nip-55/))으로 개인 키가 앱에 닿을 필요가 없습니다. 이미지 공유는 이제 업로드 진행 추적과 로딩 중 blurhash 자리 표시자와 함께 작동하며, 전체 화면 보기는 핀치-투-줌을 지원합니다.

그룹 메시지는 채팅 목록에 발신자 이름이 표시되고 [MLS](/ko/topics/mls/) 암호화가 순방향 비밀성을 보장하는 안정성 개선을 받았습니다. 사용자 검색은 팔로우에서 최대 4단계 거리까지 확장되며, 결과가 발견되는 대로 스트리밍됩니다.

Marmot 프로토콜 변경과 암호화된 로컬 스토리지로의 전환으로 인해 업그레이드 시 모든 로컬 데이터가 초기화되는 중단 변경이 있습니다. 업그레이드 전에 nsec 키를 백업하시기 바랍니다.

### diVine 1.0.5

복원된 Vine 아카이브를 기반으로 한 단편 루프 동영상 클라이언트 [diVine](https://github.com/divinevideo/divine-mobile)이 광범위한 동영상 재생 수정과 새로운 탈중앙화 애널리틱스 시스템을 담은 [1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5)를 출시했습니다.

팬텀 일시 정지, 동영상 간 이중 오디오, 썸네일과 첫 프레임 사이의 검은 화면, 처리된 플레이어 충돌이 모두 해결되었으며, 풀링된 동영상 플레이어가 홈 피드의 일관된 재생을 담당합니다.

Kind 22236 임시 view event가 크리에이터 애널리틱스와 추천을 지원합니다. 시스템은 홈, 검색, 프로필, 공유 등 트래픽 소스별로 루프 수를 추적하면서 자기 조회를 필터링합니다. Nostr event imeta 태그의 로컬 파일 경로 누출이 BUD-01 명세에 따라 클라이언트 측에서 구성된 표준 Blossom URL로 수정되었습니다.

[NIP-46](/ko/topics/nip-46/) 원격 서명자 개선에는 병렬화된 relay 연결과 콜백 URL 지원이 포함됩니다. Android는 서명자 승인 후 앱 재개 시 WebSocket 연결을 재연결합니다.

### Coracle 0.6.30

relay 관리와 [Web of Trust](/ko/topics/web-of-trust/) 모더레이션에 집중한 웹 기반 Nostr 클라이언트 [Coracle](https://github.com/coracle-social/coracle)이 피드의 미디어 탐색을 개선하는 동영상 썸네일 지원과 함께 [0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30)을 출시했습니다. iOS 클라이언트 측에서는 Nostur도 업데이트를 받았습니다.

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public)가 새로운 라이브 스트림 피드 섹션과 재설계된 설정 화면을 담은 [v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0)을 출시했습니다. GIF는 이제 Blossom 미디어 서버에 호스팅할 수 있어 중앙화 서비스 의존도를 줄입니다. Klipy GIF 통합은 Tenor를 사용할 수 없을 때 백업을 제공합니다. DM 대화의 연도 헤더와 언급 수 표시가 사용자 향 변경 사항을 완성합니다.

개발자 도구와 CLI 앱도 이번 주 업데이트를 받았습니다.

### nak v0.18.5

fiatjaf의 Nostr용 커맨드라인 도구 [nak](https://github.com/fiatjaf/nak)이 사용자 프로필 가져오기 및 표시를 위한 새 `nak profile` 서브커맨드와 함께 [v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5)를 출시했습니다. `git clone` 명령은 이제 `nostr://` URI에서 [NIP-05](/ko/topics/nip-05/) 이름을 지원하여 사람이 읽을 수 있는 식별자로 저장소 복제가 가능합니다.

### Pika v0.5.3

[Marmot](/ko/topics/marmot/) 프로토콜을 기반으로 iOS, Android, 데스크톱용으로 구축된 [MLS](/ko/topics/mls/) 암호화 메신저 [Pika](https://github.com/sledtools/pika)가 [v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3)을 출시했습니다. 최근 커밋은 데스크톱 앱에 파일 업로드와 드래그 앤 드롭 미디어 지원을 추가하고, Cloudflare Workers 배포 수정이 이루어졌습니다.

Pika는 모든 비즈니스 로직을 소유하는 Rust 코어를 사용하며, iOS(SwiftUI)와 Android(Kotlin)는 상태 스냅샷을 렌더링하는 얇은 UI 레이어 역할을 합니다. MDK(Marmot Development Kit)가 MLS 구현을 제공합니다. 프로젝트는 알파 상태임을 명시하며 민감한 작업에 사용하지 말 것을 권고합니다.

### Ridestr v0.2.6

Cashu 결제가 포함된 탈중앙화 차량 공유 플랫폼 [Ridestr](https://github.com/variablefate/ridestr)이 [v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6)을 출시했습니다. 이 릴리스는 TalkBack 접근성 문제를 수정하고, 결제 수단 전환 시 드라이버가 근처 목록에서 사라지거나 드라이버가 오프라인 상태가 될 때 선택된 드라이버 수가 업데이트되지 않는 버그를 해결합니다.

"전체에 전송" 기능이 이제 "Broadcast RoadFlare"로 변경되었으며, 새 드라이버 설치 시 발생하는 자동 실패 문제가 수정되었습니다. Ridestr은 신뢰 없는 차량 결제를 위한 HTLC 에스크로와 기기 전반의 [NIP-60](/ko/topics/nip-60/) 지갑 동기화를 구현합니다.

### Unfiltered v1.0.6

Android용 Instagram 유사 사진 공유 앱 [Unfiltered](https://github.com/dmcarrington/unfiltered)가 개선된 사용자 검색과 60초마다 자동 relay 재연결을 담은 [v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6)을 출시했습니다.

Kotlin과 Jetpack Compose로 구축된 Unfiltered는 rust-nostr 바인딩과 Blossom 호환 서버를 이미지 호스팅에 사용합니다. Amber 통합([NIP-55](/ko/topics/nip-55/))이 안전한 키 관리를 처리합니다. 앱은 알고리즘이나 광고 없이 팔로우한 계정의 게시물을 시간 순으로 표시합니다.

이번 주에는 두 개의 새 메시지 및 서명 프로젝트도 출시되었습니다.

### Burrow: AI 에이전트를 위한 MLS 메시지

[Burrow](https://github.com/CentauriAgent/burrow)는 전화번호나 중앙화 서버 없이 MLS 암호화 통신을 위한 [Marmot](/ko/topics/marmot/) 프로토콜을 구현하는 메신저입니다. 인간 사용자와 AI 에이전트 모두 참여할 수 있습니다.

자동화 시스템 통합을 위한 JSONL 출력 모드가 있는 순수 Rust CLI 데몬이 제공됩니다. Flutter 크로스 플랫폼 앱은 Android, iOS, Linux, macOS, Windows를 지원합니다. 미디어 첨부파일은 메시지와 함께 암호화되고, WebRTC가 구성 가능한 TURN 서버로 음성 및 영상 통화를 처리합니다.

Burrow는 Nostr 인프라 위에 MLS 암호화를 레이어링합니다. 신원은 Nostr 키쌍(secp256k1)을 사용하고 MLS KeyPackage는 kind 443 event로 게시됩니다. 메시지는 kind 445 event로 [NIP-44](/ko/topics/nip-44/)로 암호화되며, 초대는 [NIP-59](/ko/topics/nip-59/) 선물 포장을 사용합니다.

[OpenClaw](https://openclaw.ai) 통합으로 AI 에이전트가 전체 도구 접근권으로 참여할 수 있습니다. 감사 로깅이 있는 접근 제어 목록이 연락처와 그룹 권한을 관리합니다. 이 조합으로 Burrow는 탈중앙화 인프라에서 Signal 수준 암호화가 필요한 에이전트 간 및 에이전트-인간 메시지 시나리오에 적합합니다.

### Nostria Signer Extension

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension)는 Nostr 사용자를 위한 볼트와 신원 관리를 제공하는 Chromium 기반 브라우저 확장 프로그램입니다.

여러 계정을 담은 여러 볼트로 사용자가 다양한 맥락에 맞는 신원을 정리할 수 있습니다. 국제화에는 RTL 언어 지원이 포함됩니다. Angular와 TypeScript(코드베이스의 79.2%)로 구축되어 브라우저 확장 프로그램과 Progressive Web App 모두로 작동합니다.

Nostria Signer는 브라우저 확장 서명을 위한 [NIP-07](/ko/topics/nip-07/)을 구현하여 웹 기반 Nostr 클라이언트가 개인 키에 직접 접근하지 않고 event 서명을 요청할 수 있게 합니다. 자동화된 지갑 마이그레이션이 Chrome 웹 스토어를 통해 배포되는 업데이트를 처리합니다. 사용자는 `dist/extension` 폴더에서 사이드로드할 수도 있습니다.

개발자들은 실험적 상태를 강조합니다. 개발자가 분실된 키에 대한 접근을 복원할 수 없으므로 사용자가 직접 비밀 복구 문구를 관리해야 합니다.

## 프로젝트 업데이트

### Formstr, 새 조직으로 이전

Nostr 위의 Google Forms 대안인 [Formstr](https://github.com/formstr-hq/nostr-forms)가 저장소를 `abh3po/nostr-forms`에서 `formstr-hq` 조직으로 이전했습니다. 이 OpenSats 보조금 수혜 프로젝트는 새 위치에서 개발을 계속합니다.

### 주목할 만한 오픈 PR

Nostr 프로젝트 전반에서 진행 중인 작업:

- **Damus Outbox 모델** ([PR #3602](https://github.com/damus-io/damus/pull/3602)): iOS에서 gossip/outbox relay 모델 구현 계획. 이 아키텍처 변경은 수신자가 실제로 읽는 relay에 게시하여 메시지 전달을 개선합니다.

- **Notedeck 크로스 플랫폼 알림** ([PR #1296](https://github.com/damus-io/notedeck/pull/1296)): Android FCM, macOS, Linux를 지원하는 Damus 데스크톱 클라이언트용 네이티브 알림 시스템.

- **NDK Cashu v3 업그레이드** ([PR #370](https://github.com/nostr-dev-kit/ndk/pull/370)): Nostr Development Kit의 지갑 통합을 cashu-ts v3으로 업데이트.

- **Zeus Cashu 오프라인** ([PR #3742](https://github.com/ZeusLN/zeus/pull/3742)): Zeus Lightning 지갑의 오프라인 ecash 전송 및 수신.

- **Shopstr 암호화 디지털 전달** ([PR #231](https://github.com/shopstr-eng/shopstr/pull/231)): 디지털 상품의 암호화 전달과 물리적 상품을 위한 동적 무게 지원 추가.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**이번 주 병합됨:**

- **[NIP-85 서비스 제공자 검색 가능성](https://github.com/nostr-protocol/nips/pull/2223)**: [NIP-85](/ko/topics/nip-85/) 명세에 이제 클라이언트가 신뢰할 수 있는 어서션 제공자를 발견하는 방법에 대한 안내가 포함됩니다. 클라이언트가 [Web of Trust](/ko/topics/web-of-trust/) 점수나 기타 계산된 메트릭이 필요할 때, 사용자가 이미 팔로우하거나 신뢰하는 제공자의 kind 30085 공지를 relay에 쿼리할 수 있습니다.

- **[NIP-29 비관리 그룹 제거](https://github.com/nostr-protocol/nips/pull/2229)**: [NIP-29](/ko/topics/nip-29/) 그룹 채팅 명세에서 비관리 그룹(어떤 멤버든 다른 사람을 추가할 수 있는) 지원이 삭제되었습니다. 모든 NIP-29 그룹은 이제 명시적 관리자 역할을 갖춘 relay 측 관리가 필요하여, 구현을 단순화하고 스팸 경로를 줄입니다.

- **[NIP-11 사용 중단된 필드 제거](https://github.com/nostr-protocol/nips/pull/2231)**: [NIP-11](/ko/topics/nip-11/) relay 정보 문서에 더 이상 사용 중단된 `software` 및 `version` 필드가 포함되지 않습니다. 구현체는 응답에서 이를 제거해야 합니다.

- **[NIP-39 신원 태그 이동](https://github.com/nostr-protocol/nips/pull/2227)**: 외부 신원 주장([NIP-39](/ko/topics/nip-39/) GitHub, Twitter 등의 `i` 태그)이 kind 0 프로필에서 전용 kind 30382 event로 이동되었습니다. 이로써 신원 검증이 프로필 메타데이터에서 분리됩니다.

**AI 에이전트 NIP 진행 상황:**

네 개의 AI 관련 NIP이 활발한 개발을 계속하고 있습니다. [지난주 보도](/ko/newsletters/2026-02-18-newsletter/#ai-에이전트-nip-등장) 이후:

- **[NIP-AE: 에이전트](https://github.com/nostr-protocol/nips/pull/2220)** (2월 19일 업데이트): 에이전트 정의를 위한 kind 4199와 프롬프팅("넛지")을 위한 kind 4201로 에이전트 신원을 정의합니다. 에이전트는 확장된 설명을 위해 [NIP-94](/ko/topics/nip-94/) 파일 메타데이터를 참조할 수 있습니다.

- **[NIP-XX: AI 에이전트 메시지](https://github.com/nostr-protocol/nips/pull/2226)** (2월 18일 업데이트): 상태, 스트리밍 델타, 프롬프트, 응답, 도구 호출, 오류, 취소를 위한 7개의 임시 event kind(25800-25806)로 대화형 메시지를 표준화합니다. Kind 31340 "AI Info" event로 에이전트가 지원하는 모델과 기능을 알릴 수 있습니다.

- **[NIP-AC: DVM 에이전트 조정](https://github.com/nostr-protocol/nips/pull/2228)** (2월 18일 공개): 자율 에이전트 워크플로를 위해 [NIP-90](/ko/topics/nip-90/)을 확장합니다. 에이전트 검색을 위한 하트비트, 품질 추적을 위한 작업 리뷰, 결과 커밋을 위한 데이터 에스크로, 다단계 파이프라인을 위한 워크플로 체인, 경쟁적 제공자 선택을 위한 스웜 입찰이 추가됩니다. 참조 구현이 2020117.xyz에서 실행됩니다.

- **[NIP-AD: MCP 서버 공지](https://github.com/nostr-protocol/nips/pull/2221)** (2월 12일 공개): Nostr에서 Model Context Protocol 서버와 스킬의 공지를 표준화합니다. 이미 TENEX 플랫폼에서 사용 중입니다.

**기타 오픈 PR:**

- **[NIP-144: 서비스 인증 프로토콜](https://github.com/nostr-protocol/nips/pull/2232)**: 클라이언트가 Nostr의 서비스 제공자에게 신원과 권한을 증명하는 방법을 정의합니다.

- **[NIP-DC: Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)**: alexgleason이 Webxdc(탈중앙화 웹 애플리케이션)를 Nostr event와 통합하는 것을 제안합니다.

## NIP 심층 분석: NIP-55 (Android 서명자 애플리케이션)

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)는 Android Nostr 클라이언트가 전용 서명자 애플리케이션에 암호화 작업을 요청하는 방법을 정의합니다. 이번 주 [White Noise v0.3.0](#white-noise-v030)과 [Unfiltered v1.0.6](#unfiltered-v106) 모두 Amber 지원을 추가함에 따라, Android 서명 프로토콜을 살펴봅니다.

**통신 채널:**

NIP-55는 두 가지 메커니즘으로 앱 간 서명을 지원합니다. Intent는 일회성 작업에 시각적 피드백과 함께 수동 사용자 승인을 제공합니다. Content Resolver는 사용자가 지속적 권한을 부여할 때 자동화된 서명을 지원하여, 반복 프롬프트 없이 백그라운드에서 앱이 서명할 수 있게 합니다.

통신은 커스텀 `nostrsigner:` URI 체계를 사용합니다. 클라이언트는 다음과 같이 접촉을 시작합니다:

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**지원되는 작업:**

명세는 일곱 가지 암호화 메서드를 정의합니다. event 서명(`sign_event`), 공개 키 가져오기(`get_public_key`), [NIP-04](/ko/topics/nip-04/) 암호화/복호화, [NIP-44](/ko/topics/nip-44/) 암호화/복호화, zap event 복호화(`decrypt_zap_event`)입니다.

**권한 모델:**

클라이언트는 신뢰 관계를 확립하기 위해 `get_public_key`를 한 번 호출하여 서명자의 패키지 이름과 사용자 pubkey를 받습니다. 명세는 클라이언트가 이 값들을 저장하고 `get_public_key`를 다시 호출하지 않도록 요구하여 핑거프린팅 공격을 방지합니다.

서명 요청의 경우 사용자는 한 번 승인하거나 백그라운드 작업에 대해 "내 선택 기억"을 부여할 수 있습니다. 사용자가 작업을 지속적으로 거부하면 서명자는 "rejected" 상태를 반환하여 반복 프롬프트를 방지합니다.

**구현:**

[Amber](https://github.com/greenart7c3/amber)가 Android의 주요 NIP-55 서명자입니다. NIP-55를 지원하는 클라이언트로는 [Amethyst](https://github.com/vitorpamplona/amethyst), [White Noise](#white-noise-v030), [Unfiltered](#unfiltered-v106) 등이 있습니다. 웹 애플리케이션은 서명자 응답을 직접 받을 수 없어 콜백 URL이나 클립보드 작업을 사용해야 합니다.

**다른 서명 NIP과의 관계:**

NIP-55는 [NIP-07](/ko/topics/nip-07/)(브라우저 확장)과 [NIP-46](/ko/topics/nip-46/)(relay를 통한 원격 서명)을 보완합니다. NIP-07이 데스크톱 브라우저를 처리하고 NIP-46이 크로스 기기 서명을 처리하는 동안, NIP-55는 최소 지연으로 네이티브 Android 통합을 제공합니다.

## NIP 심층 분석: NIP-60 (Cashu 지갑)

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)은 [Cashu](/ko/topics/cashu/) ecash 지갑이 Nostr relay에 상태를 저장하여 애플리케이션 간 지갑 동기화를 지원하는 방법을 정의합니다. [Ridestr v0.2.6](#ridestr-v026)이 기기 전반의 지갑 동기화에 NIP-60을 사용함에 따라, 이 프로토콜을 살펴봅니다.

**Event Kind:**

NIP-60은 네 가지 event 유형을 사용합니다. 교체 가능한 kind 17375는 민트 URL과 P2PK ecash 결제 수신을 위한 전용 개인 키를 포함하는 지갑 구성을 저장합니다. 토큰 event(kind 7375)는 미사용 암호화 증명을 담고, 지출 내역(kind 7376)은 사용자 투명성을 위해 거래를 기록합니다. 선택적 kind 7374는 민트 결제 견적을 추적합니다.

**지갑 아키텍처:**

지갑 상태는 relay에 저장되어 애플리케이션 전반에서 접근 가능합니다. 사용자의 지갑 event는 Cashu 민트에 대한 암호화된 참조와 사용자의 Nostr 신원과 별개인 지갑 전용 개인 키를 담습니다. 이 분리가 중요합니다. 지갑 키는 ecash 작업을 처리하고 Nostr 키는 소셜 기능을 처리합니다.

```json
{
  "kind": 17375,
  "content": "<nip44-encrypted-wallet-config>",
  "tags": [["d", "cashu-wallet"]]
}
```

**증명 관리:**

Cashu 증명은 소지자 증권입니다. 한번 사용되면 증명이 무효화됩니다. NIP-60은 롤오버 메커니즘으로 이를 관리합니다. 지출 시 클라이언트는 나머지 미사용 증명으로 새 토큰 event를 생성하고 [NIP-09](/ko/topics/nip-09/)를 통해 원본을 삭제합니다. 삭제된 토큰 ID는 상태 추적을 위해 `del` 필드에 들어갑니다.

클라이언트는 주기적으로 민트에 대해 증명을 검증하여 이미 사용된 자격 증명을 감지해야 합니다. 민트당 여러 토큰 event가 허용되며, 지출 내역 event는 선택적이지만 사용자가 거래를 추적하는 데 도움이 됩니다.

**보안 모델:**

모든 민감한 데이터는 [NIP-44](/ko/topics/nip-44/) 암호화를 사용합니다. 지갑 개인 키는 평문으로 나타나지 않습니다. relay가 내용을 이해하지 못하고 암호화된 블롭을 저장하기 때문에, 신뢰할 수 없는 relay에서도 지갑 상태는 비공개를 유지합니다.

**구현:**

NIP-60을 지원하는 지갑으로는 [Nutsack](https://github.com/gandlafbtc/nutsack)과 [eNuts](https://github.com/cashubtc/eNuts)가 있습니다. [Ridestr](#ridestr-v026) 같은 클라이언트는 NIP-60을 크로스 기기 동기화에 사용하여, 사용자가 데스크톱에서 충전하고 모바일에서 수동 이체 없이 지출할 수 있게 합니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 공유할 뉴스가 있다면 <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ko/topics/nip-17/) DM으로 연락하시거나</a> Nostr에서 찾아주세요.
