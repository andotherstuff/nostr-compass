---
title: 'Nostr Compass #9'
date: 2026-02-11
translationOf: /en/newsletters/2026-02-11-newsletter.md
translationDate: 2026-02-12
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** Mostro가 3년간의 개발 끝에 첫 퍼블릭 베타를 출시하여 Nostr를 통한 P2P Bitcoin 거래를 모바일로 가져왔습니다. OpenSats가 열여섯 번째 Bitcoin 보조금을 수여했으며, Minibits Wallet이 Nostr 통합 Cashu 지갑으로 갱신 보조금을 받았습니다. **Zapstore가 1.0 안정 릴리스에 도달하여** 탈중앙화 Android 앱 스토어의 성숙을 표시합니다. Coracle 0.6.29가 주제 및 하이라이트 댓글 기능을 추가했습니다. Igloo Desktop v1.0.3가 Frostr 임계값 서명을 위한 주요 보안 강화를 출시했습니다. Amber v4.1.2-pre1이 Flow 아키텍처로 마이그레이션했습니다. Angor가 개편된 펀딩 UI와 NIP-96 이미지 서버 설정과 함께 v0.2.5에 도달했습니다. NostrPress가 Nostr 프로필을 정적 블로그로 변환하는 도구로 등장했습니다. Antiprimal이 Primal의 독점 캐시 서버를 표준 Nostr NIP으로 브릿지하는 표준 호환 게이트웨이를 공개했습니다. Primal Android가 듀얼 지갑 지원, 감사 로깅, `lookup_invoice` 메서드로 NWC 인프라를 확장하는 18개의 PR을 병합했습니다. diVine이 API 기반 비디오 피드를 출시했습니다. Marmot TypeScript SDK가 참조 채팅 앱을 독립 저장소로 분리하고 ts-mls v2로의 마이그레이션을 시작했습니다. NIPs 저장소가 NIP-45의 HyperLogLog 근사 카운팅을 병합하고 kind 0에서 신원 tag를 추출했습니다. vitorpamplona의 일련의 제안이 kind 0 메타데이터 event를 체계적으로 경량화하기 시작했습니다. 프로토콜 제안으로는 NAT 통과를 위한 Nostr Relay Connect와 서명된 웹 클레임을 위한 Nostr Web Tokens가 있습니다. 이번 주 심층 분석은 크로스 relay event 메트릭을 위한 NIP-45의 HyperLogLog 근사 카운팅과, 현재 Blossom을 권장하며 비권장으로 표시된 NIP-96의 HTTP 파일 저장소 프로토콜을 다루며, 프로젝트들이 두 미디어 표준 사이의 전환을 진행하고 있습니다.

## 뉴스

### Mostro 첫 퍼블릭 베타 출시

Nostr 기반 P2P Bitcoin 거래소인 [Mostro](https://github.com/MostroP2P/mostro)가 3년간의 개발 끝에 첫 퍼블릭 베타인 [모바일 앱 v1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0)을 릴리스했습니다. 이 앱은 Nostr를 주문 조정에, Lightning을 정산에 사용하여 수탁 중개자 없이 사용자가 직접 Bitcoin을 거래할 수 있게 합니다.

이번 릴리스는 Android에서 향상된 백그라운드 안정성을 갖춘 푸시 알림, 문제 발생 시 진단 데이터를 캡처하고 공유할 수 있는 선택적 로깅 시스템, 가산 초기화를 사용한 부드러운 relay 업데이트, 국제화 지원이 포함된 Phase 2 UI 개선을 도입합니다. 이 앱은 [Zapstore](https://zapstore.dev)와 [GitHub 직접 다운로드](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0)로 제공됩니다.

Mostro는 Shopstr, Plebeian Market과 함께 Nostr 네이티브 상거래 애플리케이션에 합류하며, 법정화폐-Bitcoin 거래 조정에 초점을 맞춘다는 점이 차별화됩니다. 기반이 되는 [Mostro 데몬](https://github.com/MostroP2P/mostro)은 Nostr relay를 통해 주문 매칭과 분쟁 해결을 처리합니다.

### OpenSats 열여섯 번째 Bitcoin 보조금

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants)가 17개 오픈소스 프로젝트에 보조금을 발표했습니다. Nostr 관련 주요 사항: [NIP-60](/ko/topics/nip-60/) 지갑 event 지원과 Nutzap 통합을 갖춘 Android [Cashu](/ko/topics/cashu/) 지갑인 [Minibits Wallet](https://github.com/minibits-cash/minibits_wallet)이 갱신 보조금을 받았습니다. Minibits는 Nostr event를 사용하여 ecash 토큰 상태를 저장하므로, relay 동기화를 통해 기기 간 지갑 백업이 가능합니다.

### NostrPress: Nostr 프로필을 정적 블로그로

[NostrPress](https://github.com/besoeasy/NostrPress) ([blog.besoeasy.com](https://blog.besoeasy.com))는 Nostr 프로필을 어디서든 배포 가능한 완전한 정적 블로그로 변환하는 도구입니다. 사용자가 아무 클라이언트를 통해 Nostr에 기사를 게시하면, NostrPress가 해당 event로부터 로컬 미디어 호스팅과 RSS 피드를 갖춘 독립형 웹사이트를 생성합니다.

Nunjucks 템플릿과 JavaScript로 구축된 NostrPress는 플랫폼 종속 없는 사이트를 생성합니다. 생성된 결과물은 모든 정적 파일 서버, GitHub Pages, Netlify, 개인 VPS에서 호스팅 가능한 일반 HTML/CSS입니다. [Npub.pro](https://github.com/nostrband/nostrsite) 및 [Servus](https://github.com/servus-social/servus)와 함께 Nostr 콘텐츠를 전통적인 웹사이트로 변환하는 옵션에 합류합니다.

### Antiprimal: Primal 캐시에 대한 표준 호환 게이트웨이

Alex Gleason과 Soapbox 팀이 만든 [antiprimal](https://gitlab.com/soapbox-pub/antiprimal) ([antiprimal.net](https://antiprimal.net))은 Primal의 독점 캐시 서버를 표준 Nostr 프로토콜 메시지로 브릿지하는 WebSocket 게이트웨이입니다. Primal은 `wss://cache.primal.net/v1`을 통해 event 통계, 콘텐츠 검색, Web of Trust 계산 같은 기능을 제공하지만, 이에 접근하려면 표준 Nostr 클라이언트가 사용할 수 없는 비표준 `cache` 필드가 포함된 독점 메시지 형식이 필요합니다. Antiprimal은 표준 NIP 요청을 Primal의 형식으로 변환하고 응답을 다시 변환합니다.

게이트웨이는 [NIP-45](/ko/topics/nip-45/) COUNT 쿼리(리액션, 답글, 리포스트, zap 수, 팔로워 수), [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) 검색, [NIP-11](/ko/topics/nip-11/) relay 정보, Primal의 사전 계산된 Web of Trust 데이터를 위한 [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) Trusted Assertions를 지원합니다. 동반 봇은 NIP-85 kind 30382(사용자 통계) 및 kind 30383(event 참여도) event를 설정 가능한 relay에 게시합니다. Bun에서 TypeScript로 구축되었고 Nostrify 라이브러리를 사용합니다. 2월 6일에 생성되어 첫 3일간 53개의 커밋이 있으며, antiprimal.net에서 운영 중입니다.

### Ikaros: Signal과 Nostr를 위한 AI 에이전트 메시징 게이트웨이

Soapbox 팀이 만든 [Ikaros](https://gitlab.com/soapbox-pub/ikaros)는 AI 에이전트가 Signal과 Nostr 암호화 DM 모두를 통해 통신할 수 있게 하는 메시징 게이트웨이입니다. 이 브릿지는 [Agent Client Protocol](https://agentclientprotocol.org) (ACP)을 사용하여 ACP 호환 AI 코딩 어시스턴트를 실제 메시징 네트워크에 연결합니다. 세 개의 pull request가 이번 주 프로젝트의 초기 빌드를 구성합니다.

[PR #1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1)은 송수신 지원, 완료 시 명시적 플러시가 있는 응답 버퍼링, `nsec` 및 16진수 개인 키 형식, 자동 재연결이 포함된 다중 relay 게시, 대화형 설정 마법사를 갖춘 완전한 [NIP-04](/ko/topics/nip-04/) 암호화 DM 어댑터를 구현합니다. 어댑터는 nostr-tools v2.23.0을 사용하고 ACP SDK를 v0.14.1로 업데이트합니다.

[PR #2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2)는 세션 업데이트 경합 상태로 인한 무음 메시지 드롭을 수정합니다. 세션이 맵에 등록되기 전에 도착한 수신 알림이 조용히 유실되었는데, 수정 사항은 등록이 완료되면 재생할 수 있도록 해당 알림을 버퍼링합니다. [PR #3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3)는 에이전트 상호작용에 Signal 사용자 및 그룹 이름/UUID 메타데이터를 추가하여, AI 에이전트가 누구와 어떤 그룹에서 대화하는지 알 수 있게 합니다. 이 프로젝트는 Nostr DM으로 접근 가능한 AI 에이전트가 Signal에서도 접근 가능하고, 그 반대도 가능한 설계 영역을 열어줍니다.

### Kind 0 슬리밍 캠페인

vitorpamplona가 이번 주 kind 0(사용자 메타데이터) event에서 데이터를 전용 event kind로 체계적으로 추출하는 일련의 PR을 열었습니다. 이 캠페인은 커지는 문제를 해결합니다. kind 0 event가 시간이 지나면서 대부분의 클라이언트가 사용하지 않는 필드를 축적하여, 모든 프로필 가져오기의 크기를 부풀렸습니다.

[PR #2216](https://github.com/nostr-protocol/nips/pull/2216)(병합됨)은 이 tag의 채택이 미미했기 때문에 신원 tag(`i` tag)를 kind 0에서 kind 10011로 이동합니다. [PR #2213](https://github.com/nostr-protocol/nips/pull/2213)은 [NIP-05](/ko/topics/nip-05/) 검증을 kind 10008로 이동하는 것을 제안하며, 이를 통해 사용자가 여러 NIP-05 식별자를 가질 수 있고 NIP-05 주소로 event를 필터링할 수 있습니다. [PR #2217](https://github.com/nostr-protocol/nips/pull/2217)은 Lightning 주소(lud06/lud16)를 별도의 kind로 추출하여, Lightning 통합이 있는 클라이언트에만 관련된 zap 관련 필드를 모든 kind 0 사용자가 갖고 다니는 것을 중단하도록 제안합니다.

이 제안들은 kind 0 구조에 대한 더 넓은 논의를 다시 활성화시켰으며, 여기에는 kind 0 콘텐츠의 문자열화된 JSON을 구조화된 tag로 대체하자는 오래된 제안인 [PR #1770](https://github.com/nostr-protocol/nips/pull/1770)도 포함됩니다.

### 암호화 메시징 보안에 NIP-70 지원 필수

[Marmot](/ko/topics/marmot/) 프로토콜의 White Noise 구현이 [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) (Protected Events) 및 [NIP-42](/ko/topics/nip-42/) (Authentication)에 대한 relay 지원의 [치명적 격차를 발견했습니다](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html). 테스트 결과 Damus, Primal, nos.lol을 포함한 주요 공개 relay가 필수 인증 챌린지를 시작하는 대신 `blocked: event marked as protected` 오류로 protected event를 거부하는 것으로 나타났습니다.

이는 핵심 보안 기능을 깨뜨립니다. NIP-70은 사용된 MLS KeyPackage의 안전한 삭제를 가능하게 하여, "지금 수집하고 나중에 복호화" 공격을 방지합니다. 이 지원 없이는 암호화 메시징 프로토콜이 미래의 키 손상으로부터 사용자를 보호할 수 없습니다. White Noise는 이에 대응하여 NIP-70을 기본적으로 비활성화했으며, 지원하는 relay를 가진 사용자를 위한 선택적 플래그를 유지합니다.

**운영자를 위한 요청:** 완전한 NIP-42 인증 흐름을 구현해주십시오. Protected event를 수신하면 소유권 증명을 요청한 후, 검증된 쓰기를 수락해야 합니다. 인증 없이 protected event를 거부하면, 암호화 메시징 애플리케이션이 의존하는 프로토콜 보안 보장이 깨집니다.

## 릴리스

### Coracle 0.6.29

hodlbod의 웹 클라이언트인 [Coracle](https://github.com/coracle-social/coracle) ([coracle.social](https://coracle.social))이 [0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29)를 출시했습니다. 이 릴리스는 kind 9802 하이라이트에 대한 주제 및 댓글 표시를 추가합니다. 리스트 네비게이션 항목이 추가되어 메인 UI에서 사용자 큐레이션 리스트에 빠르게 접근할 수 있습니다. 내부적으로 Coracle은 relay 관리와 event 처리를 담당하는 공유 Nostr 라이브러리인 Welshman의 최신 버전으로 업그레이드했습니다. 기본 relay 목록이 갱신되었고 Glitchtip 오류 추적이 코드베이스에서 제거되었습니다.

### Igloo Desktop v1.0.3

[FROST](/ko/topics/frost/) 기반 임계값 서명 및 키 관리 애플리케이션인 [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop)이 광범위한 보안 강화와 함께 [v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3)을 출시했습니다. IPC 검증, Electron 격리, 서버 측 요청 위조 방어를 위한 SSRF 인식 relay 검사를 도입합니다. 온보딩 및 공유 가져오기 흐름이 키 배포를 단순화하고, relay 계획에 정규화 및 우선순위 병합이 포함되며, 프리로드 기반 Electron API 아키텍처가 렌더러와 메인 프로세스 사이의 보안 경계를 개선합니다. 서명자 keep-alive 시스템이 임계값 서명 세션 안정성을 유지하고, 복구 UX 개선이 키 복원의 마찰을 줄입니다.

### Amber v4.1.2-pre1

Android event 서명자인 [Amber](https://github.com/greenart7c3/Amber)가 [v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1)을 릴리스하여 v4.1.1에서 도입된 누락된 relay 신뢰 점수 표시를 수정하고, Nostr가 아닌 암호화/복호화 요청에 대한 JSON 파싱 문제를 해결하며, 더 예측 가능한 상태 관리를 위해 계정 모델을 LiveData에서 Flow로 마이그레이션했습니다. Bunker 비밀이 전체 UUID로 전환되었고 Gradle 플러그인 9으로 업그레이드됩니다.

### Mostro Mobile v1.1.0 및 Daemon v0.16.1

모바일 릴리스의 전체 내용은 [위 뉴스 섹션](#mostro-첫-퍼블릭-베타-출시)을 참조하세요. 서버 측에서 [Mostro 데몬](https://github.com/MostroP2P/mostro)이 [v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1)을 출시하여, 시작 시 NIP-01 kind 0 메타데이터를 자동 게시하는 기능([PR #575](https://github.com/MostroP2P/mostro/pull/575))을 추가했습니다. 이를 통해 데몬이 온라인 상태가 되면 네트워크에 자신의 신원을 알립니다. 개발 수수료 계산 문서도 수정됩니다([PR #571](https://github.com/MostroP2P/mostro/pull/571)).

### Angor v0.2.5

Bitcoin과 Nostr 기반의 탈중앙화 P2P 펀딩 프로토콜인 [Angor](https://github.com/block-core/angor) ([angor.io](https://angor.io))가 3개의 병합된 PR과 함께 [v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5)를 출시했습니다. [PR #649](https://github.com/block-core/angor/pull/649)는 자금 관리 섹션(V2)을 재설계하여, 이전 레이아웃을 개별 UTXO 및 투자 포지션 추적을 위한 인터페이스로 교체합니다. [PR #651](https://github.com/block-core/angor/pull/651)는 업데이트된 버튼 스타일, 닫을 수 있는 대화 상자, "주소 복사" 명령, 주소 모니터링 취소 지원, 개선된 투자 흐름 처리로 InvoiceView를 개편합니다. [PR #652](https://github.com/block-core/angor/pull/652)는 설정에서 구성 가능한 [NIP-96](/ko/topics/nip-96/) ([명세](https://github.com/nostr-protocol/nips/blob/master/96.md)) 이미지 서버를 추가하여, 사용자가 프로젝트 이미지와 문서를 처리하는 미디어 업로드 엔드포인트를 선택할 수 있게 합니다. [v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4)는 전 주에 출시되었습니다.

### Ridestr v0.2.2 및 v0.2.3

[지난주 다룬](/ko/newsletters/2026-02-04-newsletter/#ridestr-v020-roadflare-릴리스) 탈중앙화 라이드셰어 플랫폼인 [Ridestr](https://github.com/variablefate/ridestr)가 v0.2.0 "RoadFlare Release" 이후 [v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2) (Bridge Payment Hotfix)와 [v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3)으로 빠른 반복을 계속했습니다. v0.2.2 핫픽스는 크로스 민트 [Cashu](/ko/topics/cashu/) 브릿지 결제가 처리 중이거나 결국 성공할 수 있는 상태에서 자동 취소되는 버그를 해결하여, 느린 정산에서의 조기 라이드 취소를 방지합니다. "내 위치" 버튼의 UI 깜빡임과 깨진 터치 히트박스도 수정됩니다. v0.2.3은 추가 버그 수정을 포함합니다. 두 릴리스 모두 Ridestr(라이더 앱)와 Drivestr(드라이버 앱)의 별도 APK를 포함합니다.

### Nostr PHP 1.9.4

Nostr 프로토콜용 PHP 헬퍼 라이브러리인 [Nostr PHP](https://github.com/nostrver-se/nostr-php) ([nostr-php.dev](https://nostr-php.dev))가 요청 클래스에 구성 가능한 `timeout` 속성을 추가하는 [1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4)를 출시했습니다([PR #106](https://github.com/nostrver-se/nostr-php/pull/106)). 개발자가 relay 연결 및 메시지 요청에 대한 사용자 정의 타임아웃 기간을 설정하여, 응답이 없거나 느린 relay에서의 무한 대기를 방지할 수 있습니다.

### Zapstore v1.0.0

Nostr 기반의 무허가 Android 앱 스토어인 [Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0) ([zapstore.dev](https://zapstore.dev))가 수개월의 릴리스 후보 기간을 거쳐 **안정 1.0 릴리스 마일스톤에 도달했습니다**.

1.0 릴리스는 핵심 안정성 개선을 포함합니다. 설치 완료 후 삭제 버튼이 즉시 나타나도록 보장하는 설치 버튼 상태 처리, 확장 가능한 기술 세부 정보가 포함된 사용자 친화적 오류 메시지, 임시 키를 사용한 Nostr 암호화 DM으로 전송하는 "이슈 보고" 버튼이 있습니다. 폴링과 배치 추적이 포함된 업데이트 화면, 중단된 전송을 위한 개선된 다운로드 감시 기능, 기기 성능 기반의 동적 동시 다운로드 제한, 더 빈번한 설치된 패키지 동기화, 개선된 버전 비교 로직도 포함됩니다. 팀은 치명적인 flutter_secure_storage 이슈를 수정하고 패키지 관리자의 엣지 케이스 처리를 강화했습니다.

이 마일스톤은 Nostr의 첫 번째 전용 앱 배포 플랫폼의 성숙을 나타내며, 개발자가 중앙화된 앱 스토어 게이트키핑 없이 사용자에게 직접 Android 애플리케이션을 게시할 수 있게 합니다.

### ZSP v0.3.1

[Zapstore](https://github.com/zapstore/zapstore) 팀의 Go CLI 도구로, Zapstore의 이전 퍼블리싱 도구를 대체하여 Android 앱의 서명 및 Nostr relay 업로드를 처리하는 [ZSP](https://github.com/zapstore/zsp)가 [v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1)을 릴리스했습니다. ZSP는 GitHub, GitLab, Codeberg, F-Droid 또는 로컬 파일에서 APK를 획득한 후 메타데이터를 파싱하고, Nostr event에 서명(개인 키, [NIP-46](/ko/topics/nip-46/) bunker, [NIP-07](/ko/topics/nip-07/) 브라우저 확장을 통해)하고, [Blossom](/ko/topics/blossom/) 서버에 아티팩트를 업로드합니다. 네트워크 연결 없이 키스토어 연결을 위한 완전한 오프라인 모드, 프로토콜 준수를 위한 Blossom 업로드의 `Content-Digest` 헤더, F-Droid 저장소에서의 arm64-v8a APK 감지 수정, GitLab 후행 쿼리 파라미터 수정, 설정을 위한 완전한 `.env` 파일 지원이 추가됩니다.

### Damus iOS 1.17

iOS Nostr 클라이언트인 [Damus](https://github.com/damus-io/damus)가 버전 1.17로 업데이트되었습니다([PR #3606](https://github.com/damus-io/damus/pull/3606)). 임시 리스 해제 후 연결이 닫히는 RelayPool 이슈를 수정하여([PR #3605](https://github.com/damus-io/damus/pull/3605)), 구독이 예기치 않게 중단되는 것을 방지합니다. 탭 간 전환 시 즐겨찾기 타임라인에 event가 표시되지 않는 버그도 해결합니다([PR #3603](https://github.com/damus-io/damus/pull/3603)).

### nak v0.18.3

Nostr army knife CLI인 [nak](https://github.com/fiatjaf/nak)이 세 가지 안정성 수정과 함께 [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3)을 출시했습니다. AUTH 챌린지 tag가 nil이거나 너무 짧을 때의 패닉 방지, 파싱된 값 사용 전 dateparser 오류 확인, `://` 구분자가 없는 Cashu mint URL 처리가 포함됩니다.

### Mi: 브라우저 기반 로컬 Relay

[Shakespeare](https://shakespeare.wtf) MiniApp인 [Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git) ([mi.shakespeare.wtf](https://mi.shakespeare.wtf))는 사용자의 Nostr event를 IndexedDB에 보관하는 브라우저 기반 로컬 relay입니다. Mi는 연결된 relay에서 프로필(kind 0), 연락처 목록(kind 3), relay 목록(kind 10002), 지갑 event를 가져와 로컬에 저장하여, 사용자가 자신의 데이터에 오프라인으로 접근할 수 있게 합니다. React와 nostr-tools 2.15.0으로 구축되었습니다.

### Agora v1.0.2

Soapbox 팀의 탈중앙화 활동주의 및 모금 플랫폼인 [Agora](https://gitlab.com/soapbox-pub/agora) ([agora.spot](https://agora.spot))가 직접 설치 가능한 Android APK와 함께 [v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2)를 출시했습니다. Compass에서 처음 언급되는 Agora는 1월 17일에 다음과 같은 미션 성명으로 출시되었습니다: "자유를 위한 글로벌 운동에 동참하세요. 전 세계 현장의 활동가에게 지원을 보내고 지역 활동에 참여하세요."

이 플랫폼은 사용자가 국가별로 탐색하고, 위치 태그가 붙은 "액션"(시위, 캠페인, 커뮤니티 조직)을 생성하며, 스레드 댓글을 통해 토론하는 세계 지도를 중심으로 합니다. 모든 콘텐츠가 Nostr relay를 통해 전파되므로 조정을 중단시키기 위해 중앙 서버를 다운시킬 수 없습니다. CI 강제 번역 패리티를 갖춘 다국어를 지원하고, 업로드를 위한 [Blossom](/ko/topics/blossom/) 미디어 서버를 통합하며, 글로벌/지역 토글이 있는 검색, 해시태그 탐색, 사용자 프로필, 리액션 시스템을 포함합니다. v1.0.2 릴리스는 현재 Android 빌드로, 직접 APK 다운로드로 제공됩니다.

### xonos v0.1.6

Bevy 게임 엔진으로 구축된 실험적 3D Nostr 클라이언트인 [xonos](https://codeberg.org/xonos/xonos)가 [v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6)을 출시했습니다. xonos는 텍스트 음성 변환 기능을 갖춘 3D 공간 환경에서 Nostr event를 렌더링하며, 소셜 프로토콜 데이터가 기존 2D 인터페이스 밖에서 어떻게 작동할 수 있는지를 탐구합니다.

## 프로젝트 업데이트

### Primal Android, NWC 인프라 확장

[Primal Android](https://github.com/PrimalHQ/primal-android-app)가 이번 주 18개의 PR을 병합하여 [지난주 시작된](/ko/newsletters/2026-02-04-newsletter/#primal-android-nwc-암호화-출시) NWC 구축을 계속했습니다. [PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883)은 양쪽 지갑(Spark 및 외부)에 대한 NWC 연결 지원을 추가하고, [PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879)는 결제 상태 확인을 위한 `lookup_invoice` NWC 메서드를 구현합니다.

[PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880)은 지갑 상호작용 디버깅을 위한 NWC 요청-응답 감사 로깅을 추가합니다. [PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877)는 `PrimalNwcService`에 다중 계정 지원을 추가하여, 여러 프로필을 가진 사용자가 별도의 지갑 연결을 유지할 수 있게 합니다. [PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882)는 만료된 예산 보류의 주기적 정리를 구현하여, 오래된 결제 예약이 지갑 작업을 차단하는 것을 방지합니다.

UI 작업에는 지갑 업그레이드 화면 재설계([PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)), 지갑 업그레이드 FAQ([PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)), 온보딩 중 Lightning 주소 설정([PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)), Lightning 이외 유형에서 zap 거래가 일반 결제로 표시되는 문제 수정([PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887))이 포함됩니다.

### diVine, API 기반 비디오 피드 출시

짧은 형식 비디오 클라이언트인 [diVine](https://github.com/divinevideo/divine-mobile)이 이번 주 19개의 PR을 병합하여 API 기반 아키텍처로 전환했습니다. [PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468)이 API 기반 비디오 피드를 도입하고, [PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466)이 트렌딩, 최근, 홈 API 엔드포인트를 추가합니다. [PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433)은 효율적인 피드 렌더링을 위해 특정 비디오 컨트롤러를 인덱싱합니다.

프로필 처리는 [PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440)이 다른 프로필 보기에 캐시 플러스 프레시 패턴을 구현하여 개선되었으며, 데이터 신선도를 보장하면서 로드 시간을 줄입니다. 알림 수정([PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)), 댓글 흐름 리팩토링([PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)), 알림 화면의 탭 스와이핑([PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388))도 출시되었습니다.

### White Noise: 키링 통합 및 사용자 검색

[Marmot](/ko/topics/marmot/) 프로토콜의 [White Noise](https://github.com/marmot-protocol/whitenoise-rs) 백엔드가 이번 주 4개의 PR을 병합했습니다. 두 PR이 키링 처리를 개선했습니다. [PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468)은 `WhitenoiseConfig`를 통해 키링 서비스 식별자를 구성 가능하게 만들고, [PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475)는 플랫폼 네이티브 저장소를 갖춘 단일 `keyring-core` 크레이트로 구현을 통합하여, 분산된 플랫폼별 코드를 대체합니다. 별도로, [PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470)이 사용자 검색 기능을 추가합니다.

### Marmot TS, 참조 채팅 앱 분리

[Marmot](/ko/topics/marmot/) TypeScript SDK ([marmot-ts](https://github.com/marmot-protocol/marmot-ts))가 [PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40)을 병합하여 내장된 참조 채팅 애플리케이션을 제거하고 독립 저장소인 [marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat)으로 분리했습니다. 2월 6일에 생성된 이 저장소는 자체 CI 파이프라인, 탭 채팅 뷰, 독립적인 빌드 시스템을 갖춘 Marmot TypeScript SDK의 참조 구현입니다. 이 분리를 통해 SDK는 라이브러리 관심사에 집중하고 채팅 앱은 독립적으로 UX를 반복할 수 있습니다.

오픈 PR ([#41](https://github.com/marmot-protocol/marmot-ts/pull/41))은 marmot-ts를 ts-mls v2.0.0으로 마이그레이션하며, 통합 컨텍스트 객체를 갖춘 재설계된 API, 메시지 처리 유틸리티(event 생성, 읽기, 역직렬화), 키 패키지 메타데이터 헬퍼, 삭제 event 지원을 가져옵니다.

### Alby Hub 업데이트

[Alby Hub](https://github.com/getAlby/hub)이 이번 주 5개의 PR을 병합했습니다. [PR #2049](https://github.com/getAlby/hub/pull/2049)는 앱 스토어 인터페이스에 Alby CLI를 추가합니다. [PR #2033](https://github.com/getAlby/hub/pull/2033)은 거래 목록에서 잘못된 zap 데이터 처리를 수정하고, [PR #2046](https://github.com/getAlby/hub/pull/2046)은 LNClient 인터페이스에서 사용되지 않는 `ListTransactions` 메서드를 제거합니다.

### Notedeck, 대시보드 및 Agentium 출시

Damus의 크로스 플랫폼 Nostr 클라이언트인 [Notedeck](https://github.com/damus-io/notedeck)이 이번 주 6개의 PR을 병합했습니다. [PR #1247](https://github.com/damus-io/notedeck/pull/1247)이 초기 대시보드 앱을 추가합니다. [PR #1293](https://github.com/damus-io/notedeck/pull/1293)은 Dave AI 어시스턴트를 듀얼 AI 모드와 씬 기반 에이전트 관리를 갖춘 시스템으로 변환하는 멀티 에이전트 개발 환경인 Agentium을 도입합니다. [PR #1276](https://github.com/damus-io/notedeck/pull/1276)이 Signal 스타일 키바인딩을 갖춘 멀티라인 메시지 컴포저를 추가하고, [PR #1278](https://github.com/damus-io/notedeck/pull/1278)이 미디어 성능 개선을 제공합니다. 주목할 오픈 PR로는 [outbox 인프라](https://github.com/damus-io/notedeck/pull/1288)와 [NIP-34](/ko/topics/nip-34/) [Git App 계획](https://github.com/damus-io/notedeck/pull/1289)이 있습니다.

### Agora 대규모 UI 개편 출시

[Agora](https://gitlab.com/soapbox-pub/agora)가 v1.0.2 릴리스와 함께 이번 주 7개의 PR을 병합했습니다. [PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106)이 가장 크며, 설정, 프로필 편집, 지도 상호작용, 검색 결과, 댓글 필터링, Blossom 서버 관리에 걸쳐 11개의 UI 작업을 완료합니다. 인증되지 않은 사용자의 리액션 버튼을 비활성화하고(이전에는 지도에서 게시물에 반응하려고 할 때 무음 실패가 발생), 날짜선 지도 패닝을 수정하고, 검색 결과에 일치하는 텍스트를 굵게 표시하는 기능을 추가했습니다.

[PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108)은 피드 게시물과 스레드 페이지 아래에 댓글 수를 추가합니다. [PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107)은 event 로드 실패 시 자동 재시도와 재시도 소진 시 명시적 리로드 버튼을 추가합니다. [PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104)는 해시태그 탐색을 글로벌 범위로 기본값을 변경합니다. 이전의 국가 범위 기본값은 결과가 없는 경우가 많았습니다.

[PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109)는 모든 언어의 번역 패리티를 검사하는 CI 단계를 추가하여, 누락된 값이 있으면 빌드가 실패합니다. [PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110)은 스크롤 리듬을 유지하기 위해 피드에서 큰 노트를 클리핑하고, [PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111)은 작은 글꼴 크기로 인한 액션 댓글 시 iOS 모바일 줌 문제를 수정합니다.

### Clawstr, CLI 및 Lightning Zap 버튼 출시

AI 에이전트가 Nostr에서 커뮤니티를 생성하고 관리하는 Reddit 영감을 받은 플랫폼인 [Clawstr](https://gitlab.com/soapbox-pub/clawstr)가 이번 주 3개의 PR을 병합했습니다. [PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11)은 AI 에이전트 스킬 정의의 모든 수동 nak 명령을 `@clawstr/cli` 패키지(`npx -y @clawstr/cli@latest`)로 교체하여, 수동 JSON event 구성을 CLI 명령으로 대체하고 지갑 작업(init, balance, zap, npc) 및 [NIP-50](/ko/topics/nip-50/) 전문 검색을 추가합니다.

[PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13)은 "For Humans" 문서 페이지와 `ProfileZapDialog` 컴포넌트를 추가합니다. Zap 버튼은 사용자의 Lightning 주소가 설정된 프로필 페이지에 나타나며 로그인 없이 작동하고, 사전 설정된 sats 금액과 QR 코드 표시로 LNURL-pay를 직접 사용합니다. [PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12)는 `wallet sync` 명령을 문서화하여, Lightning 주소로의 결제가 에이전트가 명시적으로 지갑을 동기화할 때까지 NPC가 보유하는 방식을 설명합니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-45: HyperLogLog 응답](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45 (Event 카운팅)](/ko/topics/nip-45/)가 이제 HyperLogLog (HLL) 근사 카운팅을 지원합니다. COUNT 응답과 함께 256바이트 HLL 레지스터 값을 반환할 수 있습니다. 여러 relay에서 이 레지스터를 병합하면 전체 event 세트를 다운로드하지 않고 근사 카디널리티를 계산할 수 있습니다. 주요 사용 사례는 단일 relay를 권위적 출처로 의존하지 않는 팔로워 및 리액션 수입니다. 리액션 event 두 개만으로도 256바이트 HLL 페이로드보다 더 많은 대역폭을 소비합니다. HyperLogLog++ 보정을 적용하면 작은 카디널리티에서 정확도가 향상됩니다.

- **[NIP-39: 신원 Tag를 Kind 0에서 이동](https://github.com/nostr-protocol/nips/pull/2216)** - [NIP-39](/ko/topics/nip-39/) 신원 주장 tag(`i` tag)가 kind 0 메타데이터 event에서 전용 kind 10011로 추출되었습니다. 이 tag를 지원하는 클라이언트가 거의 없어, 가치를 제공하지 않으면서 모든 kind 0 가져오기에 크기를 추가했다는 것이 근거입니다. vitorpamplona의 kind 0 추출 PR 시리즈 중 첫 번째입니다([뉴스 섹션](#kind-0-슬리밍-캠페인) 참조).

**오픈 PR 및 논의:**

- **[NIP-XX: Nostr Relay Connect (NRC)](https://github.com/nostr-protocol/nips/pull/2214)** - woikos가 공개 랑데부 relay를 통한 암호화 터널링으로 Nostr relay에 접근하는 프로토콜을 제안합니다. 이 메커니즘은 홈 서버나 모바일 기기에서 실행되는 개인 relay를 포함하여 NAT나 방화벽 뒤의 relay 접근을 가능하게 합니다. 터널링은 랑데부 relay가 트래픽을 복호화할 수 없는 상태에서 kind 24891/24892 event와 [NIP-44](/ko/topics/nip-44/) 암호화를 사용합니다. 실용적인 활용 예시로, 모든 Nostr 클라이언트가 로컬 저장소(IndexedDB, SQLite)를 크로스 디바이스 동기화를 위한 relay 엔드포인트로 노출할 수 있습니다. 표준 NIP-01 시맨틱(REQ, EVENT, CLOSE, COUNT)이 터널을 통해 투명하게 전달됩니다. 참조 구현은 Go(ORLY Relay)와 TypeScript(Smesh)로 존재합니다.

- **[Nostr Web Tokens (NWT)](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btc가 JSON Web Tokens(JWT)에서 영감을 받은, 웹 당사자 간에 서명된 클레임을 전달하기 위한 Nostr event 형식인 Nostr Web Tokens를 제안합니다. NWT는 [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (HTTP Auth)과 [Blossom 인가 event](/ko/topics/blossom/) 모두를 나타낼 수 있어, 토큰 유효 기간의 유연성을 제공합니다. 참조 Go 라이브러리가 제공됩니다. 해당 PR에는 [동영상 설명](https://github.com/pippellia-btc/nostr-web-tokens)과 NIP-98 및 Blossom Auth와의 [상세 비교](https://github.com/pippellia-btc/nostr-web-tokens#comparisons)가 링크되어 있습니다.

- **[NIP-47 단순화](https://github.com/nostr-protocol/nips/pull/2210)** - rolznz가 구현이 복잡하고 채택되지 않은 `multi_` 메서드를 [NIP-47 (Nostr Wallet Connect)](/ko/topics/nip-47/)에서 제거하는 것을 제안합니다. [지난주의 hold invoice 추가](/ko/newsletters/2026-02-04-newsletter/#nip-업데이트) 이후 명세를 정리하면서 암호화 및 하위 호환성 처리의 중복도 줄입니다.

- **[NIP-05: 자체 Event Kind로 이동](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplona가 NIP-05 검증을 kind 0에서 kind 10008로 이동하는 것을 제안하여, 사용자당 여러 NIP-05 식별자와 NIP-05 주소에 의한 필터링을 가능하게 합니다. Kind 0 슬리밍 캠페인의 일부입니다.

- **[NIP-57: Kind 0에서 Lightning 주소 분리](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplona가 [NIP-57](/ko/topics/nip-57/)에 따라 lud06/lud16(Lightning 주소)을 kind 0에서 전용 event kind로 추출하는 것을 제안하며, kind 0 슬리밍 노력을 계속합니다.

- **[프로필 하이퍼커스터마이제이션](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjaf가 현재 kind 0이 지원하는 것을 넘어서는 확장 프로필 커스터마이제이션 기능을 제안합니다.

## NIP 심층 분석: NIP-45 (Event 카운팅)과 HyperLogLog

[NIP-45](/ko/topics/nip-45/) ([명세](https://github.com/nostr-protocol/nips/blob/master/45.md))는 event 자체를 전송하지 않고 필터와 일치하는 event의 수를 relay에 요청하는 방법을 정의합니다. 이번 주 [HyperLogLog 지원](https://github.com/nostr-protocol/nips/pull/1561)의 병합은 여러 독립 relay에 걸쳐 항목을 카운팅하는 근본적인 문제를 해결하는 확률적 데이터 구조를 추가합니다.

**문제:**

단일 relay에서 event를 카운팅하는 것은 간단합니다. COUNT 요청을 보내고 숫자를 받으면 됩니다. 네트워크 전체에서 카운팅하는 것은 더 어렵습니다. A relay가 50개의 리액션을 보고하고 B relay가 40개를 보고하면, 많은 event가 양쪽 relay에 존재하기 때문에 합계는 90이 아닙니다. 모든 event를 다운로드하여 중복을 제거하지 않으면 실제 수를 계산할 수 없습니다.

**HyperLogLog:**

HyperLogLog (HLL)는 고정된 양의 메모리를 사용하여 집합의 고유 원소 수를 추정하는 확률적 알고리즘입니다. NIP-45 구현은 카운팅되는 event 수에 관계없이 정확히 256바이트를 소비하는 1바이트 256개의 레지스터를 사용합니다. 알고리즘은 각 event ID의 이진 표현을 검사하고 선행 0의 위치를 추적하는 방식으로 작동합니다. ID가 많은 0으로 시작하는 event는 통계적으로 드물기 때문에, 그 출현은 큰 집합을 나타냅니다.

**NIP-45에서의 작동 방식:**

COUNT 요청에 응답할 때 base64로 인코딩된 레지스터 값이 포함된 `hll` 필드를 포함할 수 있습니다:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

여러 relay에서 HLL 값을 수집한 후, 각 레지스터 위치에서 최대값을 취하여 병합합니다. 병합된 HLL은 relay 전체의 모든 event 집합의 합집합을 나타내며, 자동으로 중복을 처리합니다. 최종 카디널리티 추정은 병합된 레지스터에서 계산됩니다.

**정확도:**

256개의 레지스터로 표준 오차는 약 5.2%입니다. 실제 수가 1,000인 경우, 추정값은 일반적으로 948에서 1,052 사이에 들어갑니다. 더 큰 수에서도 상대 오차는 일정합니다. 실제 수가 100,000이면 약 94,800에서 105,200으로 추정됩니다. HyperLogLog++ 보정은 기본 알고리즘이 과대추정하는 경향이 있는 작은 카디널리티(약 200 미만)에서 정확도를 향상시킵니다.

**중요한 이유:**

소셜 메트릭(팔로워 수, 리액션 수, 리포스트 수)은 소셜 미디어 클라이언트의 핵심 기능입니다. HLL 없이는 단일 "신뢰할 수 있는" relay에 쿼리하거나(수를 중앙화), 모든 relay에서 전체 event를 다운로드해야 합니다(대역폭 낭비). HLL은 실제 수에 관계없이 relay당 256바이트의 총 오버헤드로 여러 relay에서 좋은 근사 수를 얻을 수 있게 합니다. 리액션 event 두 개만으로도 전체 HLL 페이로드보다 더 많은 대역폭을 소비합니다.

명세는 상호 운용성을 위해 레지스터 수를 256으로 고정합니다. 어떤 relay 구현을 실행하든 모든 relay가 병합 가능한 HLL 값을 생성합니다. 이 표준화 덕분에 HLL 지원을 한 번 구현하면 이를 지원하는 모든 relay로부터 혜택을 받을 수 있습니다.

**현재 상태:**

fiatjaf가 열었으며, 이번 주 병합되기 전 수개월간 논의 중이었던 PR입니다. 서버 구현은 COUNT 핸들러에 HLL 계산을 추가해야 하고, 클라이언트 구현은 카운트 집계 로직에 HLL 병합을 추가해야 합니다.

## NIP 심층 분석: NIP-96 (HTTP 파일 저장소)과 Blossom으로의 전환

[NIP-96](/ko/topics/nip-96/) ([명세](https://github.com/nostr-protocol/nips/blob/master/96.md))은 Nostr 클라이언트가 HTTP 미디어 서버에서 파일을 업로드, 다운로드, 관리하는 방법을 정의했습니다. 현재 [Blossom](/ko/topics/blossom/) (BUD 기반 미디어 호스팅)을 권장하며 "비권장"으로 표시되어 있지만, Angor v0.2.5가 [NIP-96 서버 설정을 추가](#angor-v025)하고 ZSP v0.3.1이 [Blossom 서버로 업로드](#zsp-v031)하는 등, 진행 중인 프로토콜 전환을 보여주기 때문에 이번 주 여전히 관련성이 있습니다.

**NIP-96 작동 방식:**

`/.well-known/nostr/nip96.json`을 가져와 파일 서버의 기능을 파악하며, 여기에는 API URL, 지원되는 콘텐츠 유형, 크기 제한, 사용 가능한 미디어 변환이 포함됩니다:

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

업로드 시 [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) 인가 헤더(업로더의 신원을 증명하는 서명된 Nostr event)와 함께 API URL로 `multipart/form-data` POST를 보냅니다. 서버는 파일 URL, 원본 및 변환된 SHA-256 해시, MIME 유형, 크기를 포함하는 [NIP-94](/ko/topics/nip-94/) 파일 메타데이터 구조를 반환합니다:

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

다운로드는 `<api_url>/<sha256-hash>`로의 GET 요청을 사용하며, 이미지 리사이징 등 서버 측 변환을 위한 선택적 쿼리 파라미터가 있습니다. 삭제는 NIP-98 인증과 함께 DELETE를 사용하며, 원본 업로더만 자신의 파일을 삭제할 수 있습니다. 파일 목록 엔드포인트는 사용자 업로드의 페이지네이션된 결과를 반환합니다.

선호하는 업로드 서버를 선언하기 위해 kind 10096 event를 게시하면, 수동 설정 없이 적절한 서버가 자동 선택됩니다.

**비권장 이유:**

NIP-96은 파일 URL을 특정 서버에 묶었습니다. `files.example.com`이 다운되면 해당 서버의 URL을 참조하는 모든 Nostr 노트가 미디어를 잃었습니다. 서버가 주소였고, 그 주소는 취약했습니다.

[Blossom](/ko/topics/blossom/) (Blobs Stored Simply on Mediaservers)은 파일 콘텐츠의 SHA-256 해시를 표준 식별자로 만들어 이를 뒤집습니다. Blossom URL은 `https://blossom.example/<sha256>.png`처럼 보이지만, 동일한 파일을 호스팅하는 모든 Blossom 서버가 같은 해시 경로에서 제공합니다. 하나의 서버가 사라지면 같은 해시로 다른 서버에 쿼리합니다. 콘텐츠 주소 지정은 데이터를 기본적으로 서버 간 이동 가능하게 만듭니다.

Blossom은 API도 단순화합니다. NIP-96은 JSON 응답, 변환 정책, 디스커버리 엔드포인트와 함께 멀티파트 폼 업로드를 사용했습니다. Blossom은 업로드에 일반 PUT, 다운로드에 GET, 인가에 서명된 Nostr event(HTTP 헤더가 아님)를 사용합니다. Blossom 명세는 모듈식 문서로 나뉘어 있습니다. BUD-01은 서버 프로토콜, 인가, 검색을 다루고, BUD-02는 blob 업로드를, BUD-03은 사용자 서버를, BUD-04는 서버 간 미러링을 다룹니다.

비권장 처리는 2025년 9월 NIPs 인덱스에서 NIP-96을 "비권장"으로 표시한 [PR #2047](https://github.com/nostr-protocol/nips/pull/2047)을 통해 이루어졌습니다.

**실제 전환 과정:**

nostr.build와 void.cat 같은 서버가 NIP-96을 지원했고 Blossom 엔드포인트를 추가하거나 마이그레이션했습니다. 다양한 단계의 전환이 진행 중입니다. 이번 주 Angor의 v0.2.5 릴리스는 프로젝트 이미지를 위한 NIP-96 서버 설정을 추가했고, ZSP의 v0.3.1 릴리스는 프로토콜 준수를 위한 `Content-Digest` 헤더와 함께 아티팩트를 Blossom 서버로만 업로드합니다. Amethyst와 Primal은 Blossom 업로드를 지원합니다. 나머지 NIP-96 구현이 마이그레이션을 완료할 때까지 공존이 계속될 것입니다.

**계승되는 것:**

Kind 10096 서버 선호 event는 Blossom 서버 선택에 유용하게 남아있습니다. NIP-94 파일 메타데이터(kind 1063 event)는 어떤 업로드 프로토콜로 생성되었든 파일 속성을 설명합니다. NIP-96이 다운로드 URL에 사용한 SHA-256 해싱은 Blossom의 콘텐츠 주소 지정의 기반이 되었습니다. NIP-96의 설계는 Blossom이 무엇을 단순화했는지를 알려주었습니다. 탈중앙화 네트워크의 미디어 호스팅은 relay 계층의 검열 저항성에 맞는 콘텐츠 주소 지정 저장소가 필요하다는 교훈이었습니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나, 공유할 뉴스가 있거나, 프로젝트를 다뤄주길 원하신다면 <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM으로 연락하시거나</a> Nostr에서 찾아주세요.
