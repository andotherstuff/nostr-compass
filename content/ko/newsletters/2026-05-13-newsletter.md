---
title: 'Nostr Compass #22'
date: 2026-05-13
publishDate: 2026-05-13
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-13-newsletter.md
translationDate: 2026-05-13
---

Nostr Compass에 오신 것을 환영합니다. Nostr 프로토콜 개발의 주간 가이드입니다.

**이번 주:** Nostr VPN이 7일간 8개의 릴리스를 출시하며 재설계된 기기 페어링 흐름부터 TCP 처리량을 약 두 배로 늘리는 FIPS AEAD 스왑까지 진행했습니다. Marmot Protocol(White Noise의 기반)이 사용자 차단 기능을 완성하는 프론트엔드 릴리스를 출시하고 MDK와 백엔드에서 31개의 PR이 병합되었습니다. Grain이 하나의 마일스톤에 4개의 새로운 NIP 구현을 담은 v0.6.0을 출시했습니다. Citrine이 내장 Tor와 릴레이 집계를 포함한 v3.0.0-pre1을 출시했습니다. Amber가 연결 흐름 및 서명 개선을 포함한 v6.1.0-pre2를 출시했습니다. Alby Hub이 AI 및 에이전트 페이지와 Core Lightning 통합을 포함한 v1.22.2를 출시했습니다. Mostro가 동시 테이커 본드와 mostro-core v0.11.0을 출시했습니다. Jumble이 최근 검색 기록과 계정 데이터 지속성 수정을 포함한 5개의 릴리스를 출시했습니다. Nostrord가 그룹 공유 모달과 Arch Linux 패키지를 포함한 3개의 릴리스를 출시했습니다. Flotilla가 영상 통화, 이메일 렌더링, 룸 언급을 포함한 1.8.0을 출시했습니다. Calendar by Formstr가 예약 스케줄링과 Android 캘린더 동기화를 포함한 v1.5.1을 출시했습니다. Tamagostrich가 sats 보상을 포함한 분산형 NIP-78 다마고치를 출시했습니다.

## 주요 소식

### Nostr VPN이 v4.0.10에 이르는 8개의 릴리스 출시

Nostr 피어 발견을 사용하는 Rust 기반 분산형 메시 VPN인 Nostr VPN이 macOS, Linux, Windows, Android에서 v4.0.1부터 v4.0.10까지 8개의 릴리스를 출시했습니다. v4.0.8의 주요 변경사항: AEAD가 RustCrypto chacha20poly1305 소프트웨어 백엔드에서 ring 0.17의 BoringSSL ChaCha20-Poly1305로 교체되어 aarch64에서는 수동 튜닝된 NEON을, x86_64에서는 AVX2/AVX-512를 사용합니다. 동일한 하드웨어의 Docker 벤치마크에서 2노드 직접 TCP 처리량이 437에서 1097 Mbps로 증가했습니다. v4.0.9는 UDP 전송 경로에 sendmmsg(2) 배치 처리를 추가하여 TCP 단일 스트림을 1066에서 1548 Mbps(1.45×)로 밀어올렸습니다. v4.0.10은 기기 페어링의 전체 UX 개선을 제공했습니다.

### Marmot / White Noise가 사용자 차단 완성과 MDK 및 백엔드 31개 PR 병합을 포함한 프론트엔드 릴리스 출시

White Noise가 5월 7일에 v2026.5.7+24를 출시하여 차단 기능 세트를 완성했습니다. 차단된 사용자는 이제 초대, 채팅 미리보기, 메시지 타임라인, 검색 결과, 알림에서 숨겨지고, 그들의 메시지는 더 이상 읽지 않은 배지에 집계되지 않습니다. MDK는 PR #258로 확장 v3 와이어 포맷과 disappearing_message_secs 스키마를 도입하여 메시지 사라짐 기능의 기반을 마련했습니다.

### Grain v0.6.0이 NIP-40, NIP-50, NIP-70, NIP-45 추가

Grain이 5월 6일에 v0.6.0을 출시하며 4개의 새로운 NIP 구현을 추가했습니다. NIP-40 이벤트 만료를 통해 게시자는 만료 타임스탬프를 설정하여 릴레이가 이벤트 만료 후 삭제할 수 있습니다. NIP-50 전문 검색을 통해 클라이언트는 REQ 메시지에서 검색 필터를 발행할 수 있습니다. NIP-70 보호 이벤트는 릴레이가 작성자의 명시적인 허가 없이 이벤트를 재공유하는 것을 방지합니다. NIP-45 카운트 쿼리를 통해 클라이언트는 릴레이에 일치하는 이벤트 수를 반환하도록 요청할 수 있습니다.

## 이번 주 출시

### Citrine v3.0.0-pre1이 내장 Tor와 릴레이 집계 제공

Citrine이 프라이버시 보호 릴레이 액세스를 위한 내장 Tor 지원과 Citrine이 여러 업스트림 릴레이에서 이벤트를 가져와 로컬 클라이언트에 제공하는 릴레이 집계를 포함한 v3.0.0-pre1을 출시했습니다. PR #139는 효율적인 집합 조정 기반 이벤트 동기화를 위한 NIP-77(Negentropy Reconciliation) 지원을 추가합니다.

### Amber v6.1.0-pre2가 새 앱 연결 흐름 개선

Amber가 v6.1.0-pre2를 출시했습니다. 주요 수정사항: 서명자 대화상자가 벙커 요청을 수락한 후 올바르게 닫히고, 잘못된 형식의 벙커 요청에는 잘못된 요청 화면이 표시되며, 인텐트 기반 서명 요청에 속도 제한이 추가되었습니다.

### Alby Hub v1.22.2가 AI 및 에이전트 페이지와 Core Lightning 지원 추가

Alby Hub이 v1.22.2를 출시했습니다. 새로운 AI 및 에이전트 페이지는 Alby Hub의 Lightning 및 NWC 기능을 AI 에이전트와 MCP 호환 도구에 공개합니다. Core Lightning(CLN)이 LND 및 LDK와 함께 지원되는 백엔드가 되었습니다.

### Mostro가 동시 테이커 본드와 mostro-core v0.11.0 출시

Mostro가 테이커 본드 기능을 진전시키는 11개의 PR을 병합했습니다. PR #733은 여러 테이커가 동시에 본드 인보이스를 제출하고 먼저 잠금을 획득한 자가 이기는 동시 테이커 본드를 구현합니다. mostro-core가 PR #144로 Action::PayBondInvoice와 Status::WaitingTakerBond를 추가하여 v0.11.0을 출시했습니다. mostro-cli가 v0.15.0을 출시했습니다.

### Jumble이 최근 검색과 계정 지속성을 포함한 5개의 릴리스 출시

Jumble이 v26.5.2부터 v26.5.6을 출시했습니다. v26.5.5는 최근 검색 기록을 추가합니다. v26.5.6에서 중요한 지속성 버그가 수정되어 계정과 캐시 데이터가 앱 완전 재시작 후에도 유지됩니다.

### Nostrord가 그룹 공유 모달, 미디어 업로드, Arch Linux 패키지 출시

Nostrord가 v1.0.0, v1.0.1, v1.0.2를 출시했습니다. v1.0.1은 AUR을 통해 nostrord-bin으로 PGP 서명 아티팩트, 최신으로 이동 버튼, 채팅에서 이미지/미디어 붙여넣기를 포함한 Arch Linux 패키지를 출시했습니다. v1.0.2는 PR #49를 통해 nostr:naddr URI와 nostrord.com/open/ 링크를 모두 생성하는 공유 모달로 그룹 공유를 추가합니다.

### FIPS v0.3.0이 크로스 플랫폼 지원, Nostr 피어 발견, 수정되지 않은 LAN을 위한 게이트웨이 출시

FIPS가 Linux 전용에서 Linux, macOS, Windows, OpenWrt로 확장하는 주요 마일스톤인 v0.3.0을 출시했습니다. 노드는 이제 공개 Nostr 릴레이에서 kind:37195 파라미터화 교체 가능 이벤트로 서명된 오버레이 광고를 게시합니다. Nostr VPN 처리량 향상을 이끈 동일한 ring 0.17 ChaCha20-Poly1305 스왑이 FIPS v0.3.0에도 적용됩니다.

### Camelus v1.10.1이 데스크톱 빌드 출시

Camelus가 Windows와 Linux 데스크톱 빌드를 포함한 v1.10.1을 출시하여 모바일 전용 배포에서 확장했습니다.

### Flotilla 1.8.0이 영상 통화, 이메일 렌더링, 룸 언급 출시

Flotilla가 1.8.0을 출시했습니다. 보이스 룸이 이제 영상을 지원하여 참가자가 통화 중 카메라를 켜거나 화면을 공유할 수 있습니다. welshman 라이브러리 업데이트를 통해 이메일 렌더링이 추가되었습니다. 룸 언급을 통해 사용자는 클릭 가능한 인라인 링크로 다른 룸과 릴레이를 참조할 수 있습니다.

### Calendar by Formstr가 예약 스케줄링과 Android 캘린더 동기화를 포함한 v1.5.1 출시

Calendar by Formstr가 5월 10일에 v1.5.0을, 5월 11일에 v1.5.1을 출시했습니다. 예약 스케줄링을 통해 사용자는 예약 가능한 시간대를 만들 수 있습니다. 읽기 전용 Android 캘린더 통합이 Nostr 이벤트를 기기 캘린더와 동기화합니다.

## 개발 중

### Amethyst가 예약 게시물, NIP-9A 커뮤니티 규칙, 데스크톱 로컬 릴레이 추가

Amethyst가 이번 주 78개의 PR을 병합했습니다. 예약 게시물이 PR #2765에서 구현됩니다. PR #2841에서 데스크톱 빌드가 SQLite 이벤트 지속성을 가진 내장 로컬 릴레이를 얻습니다. NIP-9A 커뮤니티 규칙을 구현하는 3개의 PR: PR #2798은 전송 전에 커뮤니티 규칙에 대해 게시물을 검증하고, PR #2799는 구조화된 NIP-9A 규칙 편집기를 추가하며, PR #2800은 옵트인 NIP-9A 피드 필터를 추가합니다.

### Shopstr가 MCP 감사 로깅과 세션 보안 추가

Shopstr가 5개의 PR을 병합했습니다. MCP 도구 레이어의 감사 로깅이 PR #456에서 구현됩니다. PR #477에서 세션 보안이 강화되어 원본 API 키에 세션을 고정하고 TTL 제거가 추가됩니다.

### Dart NDK가 웹 지원과 시일 서명 검증 추가

Dart NDK가 6개의 PR을 병합했습니다. PR #571에서 SembastCacheManager에 웹 지원이 추가됩니다. NIP-59 Gift Wrap 흐름의 시일 서명 검증이 PR #595에서 구현됩니다.

## 새로운 프로젝트

### Tamagostrich가 sats 보상을 포함한 분산형 NIP-78 다마고치 출시

Tamagostrich는 IDENTITY Hackathon 2026에서 출시된 브라우저 기반 가상 펫 게임으로, 아기 타조 Nori가 Nostr 소셜 활동을 통해 성장합니다. 펫 상태는 크로스 기기 동기화를 위해 NIP-78 kind:30078 이벤트에 저장됩니다. 마일스톤 보상은 NIP-47을 통해 sats로 지급됩니다: 레벨 5에서 50 sats, 레벨 10에서 210 sats, 최대 레벨 21에서 420 sats가 사용자의 lud16 주소로 전송됩니다.

## 프로토콜 및 사양 작업

이번 주 5개의 새로운 제안이 개설되었습니다.

PR #2331은 NIP-9A: 검증 가능한 커뮤니티 규칙을 제안하며, 기계 판독 가능한 암호화 서명 커뮤니티 규칙 문서를 위한 kind:34551을 도입합니다.

PR #2335는 Nostr 마켓플레이스를 위한 예약 이벤트를 제안하며, kind:32122(파라미터화 교체 가능 예약 이벤트), kind:1326(추가 전용 전환 감사 레코드), kind:32124(거래 후 리뷰)를 정의합니다. 협상은 NIP-59 gift-wrapped 메시지를 통해 비공개로 진행됩니다.

PR #2334는 Nostr 마켓플레이스를 위한 에스크로 서비스를 제안하며, 에스크로 운영자가 EVM 계약 주소와 수수료 일정을 선언하기 위한 kind:30303을 사용합니다.

PR #2333은 NIP-99 마켓플레이스 리스팅을 위한 숙박 리스팅 프로필을 제안하며, 단기 임대 리스팅을 위한 H3 지리공간 인덱스 g 태그로 NIP-99를 확장합니다.

PR #2332는 NIP-BC: 온체인 Zaps(kind 8333)를 제안하며, Nostr 키와 Bitcoin Taproot 주소 간의 직접적인 동일성을 활용합니다. kind 번호는 NIP-57을 반영합니다: 9735는 Lightning P2P 포트, 8333은 Bitcoin 메인넷의 P2P 포트입니다.

## NIP 심층 분석: NIP-78 (앱별 데이터)

NIP-78은 애플리케이션이 Nostr 이벤트를 사용하여 사용자를 대신하여 임의의 비공개 또는 공개 데이터를 저장하는 표준 방법을 정의합니다. 핵심 이벤트 종류는 30078으로, d 태그가 애플리케이션 정의 식별자 문자열인 파라미터화 교체 가능 이벤트입니다. 애플리케이션은 저장 슬롯에 고유한 d 태그를 부여하고 지속해야 하는 JSON 또는 텍스트 콘텐츠를 포함한 30078 이벤트를 게시합니다. 주요 동기는 중앙 서버 없는 크로스 기기 동기화입니다. 비공개 애플리케이션 데이터의 경우 NIP-78 이벤트는 게시 전에 NIP-44를 사용하여 콘텐츠 필드를 암호화할 수 있습니다. 현재 사용자로는 Tamagostrich(펫 상태 동기화), Wisp(지갑 백업 및 보안 설정), NosPress(CMS 오케스트레이션 상태), 여러 Nostr 클라이언트 설정 동기화 구현이 있습니다.

---

주요 소스:
- NIP-78 사양: https://github.com/nostr-protocol/nips/blob/master/78.md
- Tamagostrich: https://github.com/Negr087/tamagostrich

관련 항목: NIP-51 Lists, NIP-65 Relay List Metadata

## NIP 심층 분석: NIP-98 (HTTP 인증)

NIP-98은 Nostr 키 쌍이 HTTP 서버에 대한 요청을 승인할 수 있게 하는 HTTP 인증 체계를 정의하여 사용자 이름, 비밀번호, OAuth 토큰을 제거합니다. 클라이언트는 kind 27235의 단기 Nostr 이벤트를 구성하고, 개인 키로 서명하고, JSON을 base64로 인코딩하여 Authorization: Nostr <base64> HTTP 헤더로 전송합니다. kind 27235 이벤트는 method 태그에 HTTP 메서드, u 태그에 전체 요청 URL, created_at 타임스탬프를 포함합니다. 서버는 서명을 검증하고, 메서드와 URL이 일치하는지 확인하며, 리플레이 공격을 방지하기 위해 타임스탬프가 최근 것인지 확인합니다. NIP-98은 Blossom(BUD-01)의 블롭 업로드 인증, Routstr의 요청별 API 액세스 제어, Sprout의 git 전송 인증, Alby Hub의 관리자 API 인증에 사용됩니다.

---

주요 소스:
- NIP-98 사양: https://github.com/nostr-protocol/nips/blob/master/98.md
- BUD-01: https://github.com/hzrd149/blossom/blob/master/buds/01.md

관련 항목: NIP-96 HTTP File Storage Integration

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 공유할 소식이 있다면, Nostr에서 DM을 보내거나 nostrcompass.org에서 찾아보세요.
