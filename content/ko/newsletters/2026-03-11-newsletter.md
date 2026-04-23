---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [Shopstr](https://github.com/shopstr-eng/shopstr)와 [Milk Market](https://github.com/shopstr-eng/milk-market)이 에이전트 기반 상거래를 위한 MCP 인터페이스를 추가했습니다. [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber), [strfry](https://github.com/hoytech/strfry)는 앱, 서명자, relay 소프트웨어 전반에 걸쳐 [NIP-42](/ko/topics/nip-42/)(클라이언트의 relay 인증) relay-auth와 protected-event 지원을 더했습니다. [Route96](https://github.com/v0l/route96)는 AI 라벨링, moderation queue, perceptual hash, 기계 판독 가능한 서버 문서를 둘러싼 두 개의 릴리스를 냈습니다. 이미 웹에서 동작 중인 [Samizdat](https://github.com/satsdisco/samizdat)는 첫 Android alpha를 공개했고, 이후 [NIP-55](/ko/topics/nip-55/)(Android 서명자 애플리케이션) 지원도 추가했습니다. [Formstr](https://github.com/formstr-hq/nostr-forms)는 [NIP-49](/ko/topics/nip-49/)(개인 키 암호화)를 통한 가입 기능을 넣었고, [Amethyst](https://github.com/vitorpamplona/amethyst)는 Namecoin 기반 [NIP-05](/ko/topics/nip-05/)(도메인 검증) 해석 작업을 출시했습니다. [Mostro](https://github.com/MostroP2P/mostro)는 [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)를 출시했고, NIPs 저장소는 [NIP-91](/ko/topics/nip-91/)(필터용 AND 연산자)과 [NIP-66](/ko/topics/nip-66/)(relay 발견 및 가용성 모니터링)에 대한 방어적 가이드를 병합했습니다.

## 뉴스

### Shopstr와 Milk Market이 MCP 상거래 인터페이스를 개방

[Shopstr](https://github.com/shopstr-eng/shopstr)는 Lightning과 Cashu 결제를 지원하는 P2P 마켓플레이스로, [PR #234](https://github.com/shopstr-eng/shopstr/pull/234)([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2))를 병합하며 에이전트 계정 관리를 위한 API key 인증 MCP 서버를 추가했습니다. 이 변경은 에이전트 발견용 `.well-known/agent.json`, MCP 온보딩과 상태 엔드포인트, 주문 생성 및 결제 검증 경로, 전용 구매 및 조회 도구, API key 설정 화면을 포함합니다. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236)은 이를 확장해 판매자 측 메시지, 주소, 주문 업데이트, 제품 사양 선택 작업까지 제공합니다. [PR #235](https://github.com/shopstr-eng/shopstr/pull/235)의 보안 수정은 단일 반복 SHA-256 API key 해싱을 100,000회 salted PBKDF2로 교체했습니다.

에이전트는 페이지 스크래핑이나 클라이언트 동작 역공학 없이도 기존 [NIP-47](/ko/topics/nip-47/)(Nostr Wallet Connect)와 [NIP-60](/ko/topics/nip-60/)(Cashu Wallet) 결제 흐름을 이용해 [NIP-99](/ko/topics/nip-99/)(Classified Listings) 리스팅을 읽고 결제 단계까지 이동할 수 있습니다.

[Milk Market](https://github.com/shopstr-eng/milk-market)은 [milk.market](https://milk.market)에서 운영되는 Nostr 기반 식품 마켓플레이스로, [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3)에서 동일한 MCP 및 API key 기반 구조를 도입했습니다. [PR #10](https://github.com/shopstr-eng/milk-market/pull/10)은 구독 주문, 구매 후 배송지 변경, Stripe를 포함한 법정화폐 결제 경로를 위한 다중 판매자 및 다중 통화 체크아웃 처리를 추가합니다. 이어진 [PR #11](https://github.com/shopstr-eng/milk-market/pull/11)은 신규 설치에서 failed relay publishes 테이블이 생성되지 않아 첫 로드 시 500 오류를 내던 데이터베이스 초기화 버그를 고쳤습니다. 이 에이전트 인터페이스는 Shopstr에서는 Bitcoin 네이티브 결제와, Milk Market에서는 법정화폐와 Bitcoin을 섞은 결제 흐름과 함께 동작합니다.

### Bunker, 서명자, relay 전반의 NIP-42 relay auth

[OAuth Bunker](https://github.com/flox1an/oauth-bunker)는 OAuth 제공자와 Nostr 서명을 연결하는 [NIP-46](/ko/topics/nip-46/)(Nostr Connect) bunker로, [NIP-07](/ko/topics/nip-07/)(브라우저 확장 서명자) 로그인, 자동 단일 신원 선택, 삭제된 신원의 정리 기능을 추가했습니다([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). 신원이 하나뿐이면 더 이상 선택을 묻지 않고 자동으로 그 신원을 선택합니다. 신원을 삭제할 때는 매달린 할당과 연결도 함께 제거합니다. [commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc)는 할당된 사용자를 위한 `ALWAYS_ALLOWED_KINDS` 설정 경로를 추가했고, 기본값으로 앱 전용 데이터인 kind `30078`을 허용합니다. 덕분에 위임된 신원은 각 event마다 별도 승인을 요구하지 않고 앱 전용 저장소에 쓸 수 있습니다.

[Amber](https://github.com/greenart7c3/Amber)는 Android용 대표적인 [NIP-55](/ko/topics/nip-55/) 서명자로, 한 주 동안 네 번의 프리릴리스를 거쳐 [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4)를 공개했습니다. [PR #317](https://github.com/greenart7c3/Amber/pull/317)은 kind `22242` 요청에 대한 [NIP-42](/ko/topics/nip-42/) relay 인증 처리를 추가합니다. 구현은 relay별 권한을 추적하는 새 데이터베이스 컬럼과 `(pkKey, type, kind, relay)`에 대한 고유 인덱스를 도입합니다. 사용자는 relay별 또는 와일드카드 `*` 범위로 모든 relay에 대해 허용 또는 거부를 선택할 수 있는 전용 인증 화면을 보게 되며, 그 선택은 영속화됩니다. 와일드카드 권한은 특정 kind에 대한 개별 relay 권한을 모두 정리합니다. [PR #318](https://github.com/greenart7c3/Amber/pull/318)은 이어서 다중 event 요청 화면을 별도 화면 이동 대신 composable 카드 안에 세부 정보를 바로 표시하도록 리팩터링했습니다. 이번 릴리스는 기본 프로필 relay 업데이트, bottom-sheet 요청 표시, StrongBox keystore를 비활성화해 MediaTek 기기에서 발생하던 충돌 수정도 포함합니다.

relay 측에서는 [strfry PR #156](https://github.com/hoytech/strfry/pull/156)이 [NIP-70](/ko/topics/nip-70/)(Protected Events)을 위한 NIP-42 인증 처리를 구현했고, [PR #176](https://github.com/hoytech/strfry/pull/176)은 protected event를 포함한 repost를 거부합니다.

### Notedeck이 NIP-11 relay 제한과 Agentium 기능을 추가

[Notedeck](https://github.com/damus-io/notedeck)는 Damus 팀이 만드는 네이티브 데스크톱 클라이언트로, 이번 주 14개의 PR을 병합했습니다. [PR #1316](https://github.com/damus-io/notedeck/pull/1316)은 [NIP-11](/ko/topics/nip-11/)(Relay Information Document)의 relay 제한 정보를 가져오는 기능을 추가해, 모든 outbox relay가 이제 relay 정보 문서의 `max_message_length`와 `max_subscriptions`를 존중합니다. 구현에는 백그라운드 작업 처리, 연결 재시도를 위한 지터가 있는 지수 백오프, 맞춤형 HTTP Accept 헤더가 포함됩니다. [PR #1312](https://github.com/damus-io/notedeck/pull/1312)는 계정 전환 후 DM이 가끔 로드되지 않던 버그를 고쳤고, [PR #1333](https://github.com/damus-io/notedeck/pull/1333)은 에러 시 relay 멀티캐스트 통신이 브로드캐스트 스팸이 되지 않도록 백오프 메커니즘을 추가했습니다.

Agentium 하위 시스템(Notedeck 내부의 코딩 에이전트 UI, 내부 명칭은 "Dave")에는 클립보드 이미지 붙여넣기, kind `31991` event를 통한 기기 간 동기화가 가능한 named run configuration([NIP-33](/ko/topics/nip-33/)(매개변수화된 교체 가능 event)), git worktree 생성기, 세션별 백엔드 선택을 위한 모델 선택기가 추가됐습니다([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338)은 헤드리스 UI 테스트를 위해 `egui_kittest`를 통합했고, [PR #1339](https://github.com/damus-io/notedeck/pull/1339)은 클라이언트별 새 contact list 생성 수를 추적하는 대시보드 카드를 추가했습니다. 열린 [PR #1314](https://github.com/damus-io/notedeck/pull/1314)는 ElectrumX 조회, SOCKS5 Tor 라우팅, 검색창 통합을 포함해 Amethyst의 Namecoin NIP-05 해석 기능을 Notedeck으로 이식합니다.

### diVine v1.0.6, E2E 테스트 인프라와 NIP-49 가져오기 포함

[diVine](https://github.com/divinevideo/divine-mobile)은 [divine.video](https://divine.video)에서 Vine 아카이브를 복원하는 짧은 루프형 비디오 클라이언트로, 127개의 병합된 PR과 함께 [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6)을 출시했습니다. 이 릴리스는 [NIP-49](/ko/topics/nip-49/) 계정 가져오기, 외부 [NIP-05](/ko/topics/nip-05/) 지원, 다중 계정 처리, macOS 및 실험적 Linux 빌드, 로컬 스토리지 기반으로 다시 설계된 초안 및 클립 라이브러리를 추가합니다.

엔지니어링 측면에서 [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928)은 relay, API, Blossom, Postgres, Redis, ClickHouse로 구성된 Docker 백엔드 스택을 대상으로 Patrol을 이용한 네이티브 UI 자동화 기반의 완전한 E2E 통합 테스트 인프라를 추가합니다. 다섯 개의 인증 여정 테스트가 등록, 검증, 비밀번호 재설정, 세션 만료, 토큰 갱신을 다룹니다. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105)은 비디오 로딩을 HLS 우선 방식에서 직접 MP4 우선 방식으로 바꾸고 자동 HLS fallback을 추가해, 로딩 시간을 30~60초에서 거의 즉시 수준으로 줄였습니다. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076)은 홈 피드 API 응답을 SharedPreferences에 캐시해 콜드 스타트 시 즉시 표시되게 하고, [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104)는 `ai-generated` 콘텐츠 라벨이 붙은 항목을 피드에서 숨김 처리하며, [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100)은 diVine 호스팅 비디오만 보이게 하는 안전 설정을 추가합니다. Hive에서 Drift로의 프로필 캐시 마이그레이션도 [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883), [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903)에 걸쳐 계속 진행되며, 약 1,074줄의 Hive 코드를 Drift DAO로 대체하고 있습니다.

### Vector v0.3.2, NIP-77 negentropy 동기화와 MLS 개선 포함

[Vector](https://github.com/VectorPrivacy/Vector)는 [NIP-17](/ko/topics/nip-17/)(개인 다이렉트 메시지)과 [NIP-44](/ko/topics/nip-44/)(암호화 payload)를 사용하는 MLS 그룹 암호화 기반의 프라이버시 중심 데스크톱 메신저로, [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2)를 출시했습니다. 핵심 변경은 MLS 그룹 동기화를 위한 NIP-77 negentropy([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac))입니다. 이를 통해 parallel boot를 사용해 놓친 메시지를 훨씬 더 빠르게 따라잡을 수 있습니다. 이 릴리스는 Linux 전체 지원이 포함된 재구축된 오디오 엔진, 흐림 미리보기가 있는 이미지 spoiler, 풍부한 링크 미리보기를 갖춘 클릭 가능한 하이퍼링크, 그룹 관리자용 `@everyone`을 포함한 `@mention` 알림, 이모지 shortcode 자동완성, 그룹 음소거, 기존 리액션에 대한 탭 반응, 취소 가능한 파일 업로드도 추가합니다. Vector는 [NIP-17](/ko/topics/nip-17/) 그룹 채팅 event를 명시적으로 필터링하며([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), 그룹 암호화에는 MLS만 사용합니다.

## 릴리스

### Route96 v0.5.0 및 v0.5.1

[Route96](https://github.com/v0l/route96)는 Blossom과 [NIP-96](/ko/topics/nip-96/)(HTTP 파일 저장)를 지원하는 미디어 서버로, [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0)과 [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1)을 출시했습니다. v0.5.0은 자동 AI 라벨링, 라벨이 없는 기존 업로드에 대한 소급 백필, 문제 있는 파일을 위한 moderation queue, EXIF 기반 프라이버시 거부, 금지된 해시 처리 기능을 추가합니다.

v0.5.1은 perceptual image hash, 유사 이미지 조회를 위한 locality-sensitive hashing, 배치 관리자 엔드포인트, 에이전트 도구용 서버의 Blossom 및 NIP-96 API 표면을 설명하는 공개 [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1)를 추가합니다. [PR #58](https://github.com/v0l/route96/pull/58)은 백그라운드 워커를 완전 비동기 Tokio task로 옮기고, [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8)은 hot loop를 피하기 위한 백오프를 추가합니다.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat)는 [samizdat.press](https://samizdat.press)에서 제공되는 장문 리더 및 퍼블리셔로, 첫 Android 빌드인 [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha)를 공개했습니다. 앱은 장문 Nostr 글이 큐레이션된 Press 페이지로 시작하며, Press, Feed, Saved, Write 보기를 오가는 하단 탭 내비게이션을 갖춥니다. Android 빌드는 Android Keystore 암호화를 통한 네이티브 키 저장과 생체 잠금 해제를 추가했고, `nostr:` URI와 `samizdat.press` 딥링크를 처리하며, 직접 키 가져오기 대신 Android 앱 chooser를 통한 서명자 handoff(Amber, Primal 등)를 지원합니다. pull-to-refresh, 다양한 화면 크기에서의 safe-area 처리, 네이티브 공유, 클립보드, 햅틱, 스플래시 화면 통합도 웹 래퍼가 아니라 Android 셸에 포함됩니다.

[commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6)은 Amber와 Primal 흐름을 위한 intent 기반 [NIP-55](/ko/topics/nip-55/) 서명을 추가했고, [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614)은 JavaScript bridge 우회 코드를 `startActivityForResult`를 사용하는 네이티브 Capacitor 플러그인으로 교체했습니다. 앱은 Android 7.0 이상(API 24)을 요구하고, 이 alpha에서는 debug APK로 배포되며, 아직 푸시 알림은 없습니다. 현재 게시 기능은 서명자 앱에 의존하고, `nsec` 로그인은 로컬 읽기와 계정 접근만 다룹니다.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)는 [calendar.formstr.app](https://calendar.formstr.app)에서 제공되는 탈중앙화 캘린더 앱으로, [NIP-59](/ko/topics/nip-59/)(Gift Wrap) 기반 비공개 event 공유를 지원합니다. 이번에 [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38)와 함께 [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0)을 출시했습니다. 이 릴리스는 [NIP-52](/ko/topics/nip-52/)(Calendar Events)의 반복 event 처리를 확장하며, v0.1.0의 단일 event 기반을 넘어섭니다. 하부 변경은 로컬 event 저장소, 서명자 처리, Android 알림 배선에도 영향을 줍니다. Formstr 조직에서 지난달 저장소 이전에 이어 두 번째로 활발히 개발되는 애플리케이션입니다.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro)는 Nostr 기반 P2P Bitcoin 거래소로, [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)를 출시했습니다. [지난주](/en/newsletters/2026-03-04-newsletter/) 다뤘던 dispute-session restore([PR #599](https://github.com/MostroP2P/mostro/pull/599))와 auto-close([PR #606](https://github.com/MostroP2P/mostro/pull/606)) 수정이 포함됩니다. 이번 릴리스의 새로운 내용은 kind `38384` 사용자 평점 event에 `days` 필드를 추가하는 [PR #625](https://github.com/MostroP2P/mostro/pull/625), 해당 평점 event에 만료를 더하는 [PR #612](https://github.com/MostroP2P/mostro/pull/612), 주문 event를 하드코딩된 24시간 창 대신 구성 가능한 만료 설정으로 전환하는 [PR #614](https://github.com/MostroP2P/mostro/pull/614), 그리고 중복 개발 수수료 지급을 막는 idempotency 검사 [PR #622](https://github.com/MostroP2P/mostro/pull/622)입니다.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile)은 Mostro P2P 거래소의 Flutter 클라이언트로, 11개의 신규 기능과 11개의 버그 수정을 포함한 [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1)을 출시했습니다. 이번 릴리스는 분쟁 채팅의 암호화 멀티미디어 렌더링([PR #514](https://github.com/MostroP2P/mobile/pull/514)), 주문이 종료 상태에 도달했을 때 분쟁 UI를 자동으로 닫는 기능([PR #503](https://github.com/MostroP2P/mobile/pull/503)), NWC 지갑 가져오기를 위한 QR 스캔([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), 프랑스어 번역, FCM 푸시 알림 처리를 추가합니다. [PR #496](https://github.com/MostroP2P/mobile/pull/496)은 bip340 의존성을 v0.2.0으로 고정해 Schnorr 서명 패딩 버그를 수정합니다.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main)은 Cashu를 지원하는 Telegram 스타일 메시징 클라이언트로, Linux 데스크톱 수정에 초점을 둔 [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release)를 출시했습니다. AppImage dock 아이콘, 이모지 렌더링, 컨텍스트 메뉴 멈춤, 답글 및 복사 UI 정지 문제가 고쳐졌고, 이미지 업로드와 npub.cash 통합 관련 수정도 포함됐습니다. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49)는 아무 일도 하지 않으면서 glassmorphic 리페인트를 강제하던 3초 폴링 타이머를 제거해 불필요한 UI 재구성을 없앴고, event cache 로딩을 동시 실행으로 바꿔 relay, 연락처, 채널 초기화를 막던 로그인 정체도 해결했습니다.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android)은 [NIP-55](/ko/topics/nip-55/)와 [NIP-46](/ko/topics/nip-46/)을 지원하는 Android용 FROST threshold 서명자로, [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0)과 [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1)을 출시했습니다. v0.6.0은 지갑 descriptor 조정과 관리 UI, 생체 인증이 포함된 백업/복원 흐름([PR #184](https://github.com/privkeyio/keep-android/pull/184)), threshold share로부터의 `nsec` 복구([PR #187](https://github.com/privkeyio/keep-android/pull/187)), Rust UniFFI 기반의 크로스플랫폼 애니메이션 QR 프레임 생성([PR #188](https://github.com/privkeyio/keep-android/pull/188)), chain verification을 포함한 서명 감사 추적([PR #189](https://github.com/privkeyio/keep-android/pull/189))을 추가합니다. v0.6.1은 라이선스를 AGPL-3.0에서 MIT로 전환합니다([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump)은 [njump.me](https://njump.me)에서 Nostr 콘텐츠를 보여주는 정적 게이트웨이로, `note1` 코드 파싱의 호환성 깨뜨리는 변경과 기반 nostr 라이브러리 업데이트를 포함한 [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0)을 출시했습니다.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr)는 Nostr를 이용한 탈중앙화 도로 이벤트 신고 앱으로, 초기 데모 릴리스 [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1)을 공개했습니다. 앱은 openfreemap.org의 vector tile을 사용해 지도 위에 도로 이벤트를 표시합니다.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core)는 Nostr 전송 계층과 전용 relay를 갖춘 e-bill 애플리케이션으로, [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)을 출시했습니다. [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)은 결제 및 수락 상태를 위한 `payment_actions`와 `bill_state` 필드를 API에 추가했고, [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)는 익명 서명자의 signing address 처리를 고쳤습니다.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat)은 Marmot 프로토콜의 .NET MLS 및 C# 라이브러리 위에 구축된 채팅 애플리케이션으로, [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3)를 출시했습니다. 이번 릴리스는 Amber와 [NIP-46](/ko/topics/nip-46/) 흐름을 위한 외부 서명자 지원([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), 충돌 사이 데이터 유실 가능성을 없애기 위해 MLS 상태 영속성을 MLS 서비스 내부로 옮긴 변경([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), 새 CI 파이프라인을 통한 Windows, Linux, Android 빌드 공개를 포함합니다.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal)은 Nostr용 Kotlin Multiplatform 트레이딩 copilot으로, [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0)을 출시했습니다. 이 릴리스는 도메인 로직, 차트 렌더링, Nostr 인증과 게시, Blossom [NIP-96](/ko/topics/nip-96/) 업로드 지원, ONNX 기반 AI 추론 훅을 Desktop과 Android 셸 전반에서 공유하는 KMP 모듈을 패키징합니다. 공개된 아키텍처에는 차트 스크린샷 분석용 FastAPI AI 서비스, 모델 학습 파이프라인, 규모와 경고를 포함한 구조화된 거래 계획을 생성하는 리스크 엔진도 포함됩니다. 로그인은 원시 `nsec` 키 또는 외부 서명자를 지원하며, 출력 흐름은 로컬 분석에 머무르지 않고 Nostr event 게시로 끝납니다.

## 프로젝트 업데이트

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms)는 Nostr 기반의 Google Forms 대안으로, [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434)([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8))를 병합해 [NIP-49](/ko/topics/nip-49/)(개인 키 암호화) 기반 가입 흐름을 추가했습니다. 이전에는 Formstr를 쓰려면 [NIP-07](/ko/topics/nip-07/) 브라우저 확장 또는 원시 `nsec` 붙여넣기가 필요했습니다. 새 흐름은 클라이언트 측에서 키페어를 만들고, 사용자가 고른 비밀번호로 NIP-49의 scrypt + XChaCha20-Poly1305 스킴을 사용해 개인 키를 암호화한 뒤, 결과 `ncryptsec` 문자열을 저장합니다. 사용자는 서명자 확장을 설치하지 않고도 비밀번호만으로 다시 로그인할 수 있습니다. 키 관리는 전 과정에서 클라이언트 측에 머뭅니다.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst)는 지난주 오픈 상태였던 Namecoin 기반 [NIP-05](/ko/topics/nip-05/) 해석 작업을 실제로 배포한 네 개의 PR을 병합했습니다. [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)는 `.bit`, `d/`, `id/` 식별자에 대해 ElectrumX를 사용한 검열 저항형 NIP-05 검증을 추가합니다. Amethyst가 NIP-05 필드에서 이러한 접미사를 감지하면 ElectrumX-NMC 서버에서 이름의 거래 이력을 조회하고, 최신 출력의 `NAME_UPDATE` 스크립트를 파싱해 Nostr pubkey를 추출하며, 36,000블록(Namecoin 만료 기간)보다 오래된 이름은 거부합니다. ElectrumX 연결은 Tor가 켜져 있으면 SOCKS5를 통해 라우팅되고, clearnet과 `.onion` 엔드포인트 사이를 동적으로 선택합니다. 1시간 TTL의 LRU 캐시가 반복적인 블록체인 조회를 방지합니다.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771)은 이 흐름의 경쟁 상태와 resolver 정확도를 수정합니다. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785)는 신규 사용자가 일반 NIP-05 식별자나 Namecoin 기반 식별자에서 팔로우 목록을 가져와 가입할 수 있게 하며, [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786)은 어떤 ElectrumX 서버를 사용할지 사용자가 직접 고를 수 있는 설정을 추가합니다.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb)는 IndexedDB에 Nostr event를 저장하는 도우미 라이브러리로, [NIP-91](/ko/topics/nip-91/) AND 태그 필터 지원을 추가하는 [PR #6](https://github.com/hzrd149/nostr-idb/pull/6)을 병합했습니다. 이 변경은 클라이언트 측 필터 매칭에 교집합 의미론을 추가해, IndexedDB 조회가 주어진 태그 값 중 하나가 아니라 모두를 요구할 수 있게 합니다. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8)은 라이브러리를 최신 NIP-DB 인터페이스로 업데이트했고, 후속 [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972)은 subscribe deadlock을 수정하고 nostr-tools를 프로덕션 의존성에서 제거합니다.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve)는 ClickHouse 분석을 제공하는 archive-first Nostr 인덱서로, [PR #8](https://github.com/andotherstuff/pensieve/pull/8)을 병합해 항목별 캐시 TTL 강제와 키별 miss coalescing을 추가했습니다. 가장 비용이 높은 시계열 엔드포인트(engagement stats, 시간대별 활동, kind별 활동)는 이제 동기식 재계산 폭주를 유발하는 대신 10분 서버 측 TTL을 사용합니다.

### Blossom

[Blossom](https://github.com/hzrd149/blossom)은 탈중앙화 미디어 호스팅 프로토콜 및 서버 스택으로, BUD-11 인증 관련 두 가지 업데이트를 병합했습니다. [PR #91](https://github.com/hzrd149/blossom/pull/91)은 선택적 인증을 별도 BUD로 분리하고 `x` 및 `server` 태그의 역할을 명확히 합니다. [PR #93](https://github.com/hzrd149/blossom/pull/93)은 엔드포인트별 인증 동작을 정리하고 업로드 검증을 위한 `X-SHA-256` 헤더를 공식화합니다. 이 두 PR은 인증 로직을 BUD-11로 통합하고 업로드, 삭제, 미디어 관리 흐름의 요청 해시 처리에 있던 모호성을 없앱니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-91](/ko/topics/nip-91/) (필터용 AND 연산자)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): 태그 필터에 교집합 의미론을 추가해 relay가 나열된 모든 태그 값을 요구하는 질의를 처리할 수 있게 합니다. 태그가 많은 질의에서 클라이언트 측 후처리와 대역폭을 줄여줍니다.

- **[NIP-66](/ko/topics/nip-66/) (Relay Discovery and Liveness Monitoring): 방어 조치** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): [지난주](/en/newsletters/2026-03-04-newsletter/) 다룬 outbox 벤치마크 작업에 이어, 이 사양은 relay 모니터링 데이터의 불리한 경로에 대한 경고를 추가합니다. 클라이언트는 동작을 위해 kind `30166` 모니터링 event를 필수로 요구해서는 안 됩니다. 모니터는 틀릴 수도, 오래됐을 수도, 악의적일 수도 있습니다. 따라서 클라이언트는 여러 출처를 교차 검증해야 하며, 단일 피드만 보고 사용자의 relay 그래프 중 큰 부분을 끊어내면 안 됩니다.

- **[NIP-39](/ko/topics/nip-39/) (프로필의 외부 신원): kind 10011 레지스트리 정리** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): kind `10011` 참조를 사양에 직접 추가해, [지난주](/en/newsletters/2026-03-04-newsletter/) 다룬 Amethyst 구현과 사양을 정렬합니다.

**열린 PR 및 논의:**

- **[NIP-70](/ko/topics/nip-70/) (Protected Events): protected event를 포함한 repost 거부** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): relay가 원본 event에는 NIP-70을 적용하면서 같은 콘텐츠를 담은 repost를 허용하면 `-` 태그는 사실상 효력이 없습니다. 이 PR은 relay가 protected event를 담은 kind 6 및 kind 16 repost도 거부해야 한다는 규칙을 추가합니다. [strfry PR #176](https://github.com/hoytech/strfry/pull/176)은 이미 이를 구현했습니다.

- **[NIP-71](/ko/topics/nip-71/) (Video Events): 다중 오디오 트랙** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): 대체 트랙, 언어 변형, 오디오 전용 스트림을 위한 오디오 `imeta` 태그를 추가합니다. 클라이언트는 비디오 파일은 그대로 유지한 채 오디오 언어만 바꾸거나, 팟캐스트 같은 콘텐츠를 위해 오디오를 별도 트랙으로 제공할 수 있습니다.

- **[NIP-11](/ko/topics/nip-11/) (Relay Information Document) 및 [NIP-66](/ko/topics/nip-66/) relay 속성** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): relay 정보 문서에 구조화된 `attributes` 필드를 추가해, 클라이언트와 discovery 도구가 현재의 자유 형식 설명문을 넘어서는 기계 판독 가능한 메타데이터를 활용할 수 있게 합니다.

## NIP 심층 분석: NIP-49 (개인 키 암호화)

[NIP-49](/ko/topics/nip-49/)는 클라이언트가 개인 키를 비밀번호로 암호화하고 그 결과를 `ncryptsec` bech32 문자열로 인코딩하는 방법을 정의합니다. [Formstr](#formstr)는 새 가입 흐름에서 NIP-49를 사용합니다.

이 형식은 전용 event kind에 묶여 있지 않습니다. 클라이언트는 원시 32바이트 secp256k1 개인 키에서 시작해, scrypt로 사용자의 비밀번호에서 대칭 키를 파생하고, XChaCha20-Poly1305로 키를 암호화한 뒤, 결과를 bech32 `ncryptsec` 문자열로 감쌉니다. 1바이트 플래그는 암호화 전에 그 키가 안전하지 않은 방식으로 취급된 적이 있는지 여부를 기록합니다.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

위 JSON event는 애플리케이션 수준의 예시일 뿐 NIP-49 요구 사항은 아닙니다. NIP는 암호화된 키 형식 자체를 표준화합니다. 클라이언트는 `ncryptsec`를 로컬에 저장하거나, 앱별 스토리지로 동기화하거나, 백업 문자열로 내보낼 수 있습니다. 비밀번호는 키 파생 전에 Unicode NFKC로 정규화되어, 동일한 비밀번호가 클라이언트와 플랫폼 전반에서 일관되게 복호화되도록 합니다.

1바이트 키 보안 플래그에는 세 가지 값이 정의됩니다. `0x00`은 키 처리 이력이 알 수 없음을 의미하고, `0x01`은 암호화 전에 평문 웹 폼에 붙여넣는 식으로 안전하지 않게 취급된 것이 알려졌음을 의미하며, `0x02`는 키가 안전한 환경에서 생성되고 암호화되어 한 번도 노출된 적이 없음을 뜻합니다. 클라이언트는 이를 이용해 안전하지 않은 이력이 있는 키를 가져올 때 경고를 띄울 수 있습니다.

NIP-49는 평문 `nsec` 내보내기보다 키를 더 잘 보호하지만, 암호화 강도는 비밀번호와 구성된 scrypt 비용에 달려 있습니다. `LOG_N` 값이 높을수록 오프라인 추측은 어려워지지만, 정당한 복호화 작업도 느려집니다. 사양은 암호화된 키를 공개 relay에 게시하지 말라고 경고합니다. 공격자가 오프라인 크래킹용 암호문을 수집하는 데 유리해지기 때문입니다. 비교하자면 [NIP-46](/ko/topics/nip-46/) 원격 서명은 키를 아예 노출하지 않고, [NIP-55](/ko/topics/nip-55/) Android 서명은 전용 서명자 앱 안에 키를 보관합니다. NIP-49는 다른 자리를 채웁니다. 자기 키를 직접 관리하는 사용자를 위한 이동 가능한 암호화 백업입니다.

구현 사례로는 가입 흐름의 [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434), ncryptsec 백업 및 복원을 지원하는 [Amber](https://github.com/greenart7c3/Amber), 계정 가져오기를 지원하는 [diVine v1.0.6](#divine-v106-e2e-테스트-인프라와-nip-49-가져오기-포함), FROST share 내보내기를 지원하는 [Keep v0.6.0](#keep-v060), 그리고 [nsec.app](https://nsec.app), [Alby](https://github.com/getAlby/hub) 같은 키 관리 도구가 있습니다.

## NIP 심층 분석: NIP-70 (Protected Events)

[NIP-70](/ko/topics/nip-70/)은 protected event를 정의합니다. event가 `["-"]` 태그를 갖고 있으면, relay는 [NIP-42](/ko/topics/nip-42/) 인증을 요구하고 인증된 pubkey가 event 작성자와 일치하는 경우가 아니면 이를 거부해야 합니다.

NIP-42 인증 흐름은 다음과 같습니다. relay가 무작위 문자열이 담긴 `AUTH` challenge를 보내고, 클라이언트는 relay URL과 challenge를 태그에 포함한 서명된 kind `22242` event로 응답합니다. relay는 서명을 검증하고, auth event의 pubkey가 게시 중인 protected event의 pubkey와 일치하는지 확인합니다. 일치하지 않으면 relay는 `restricted` 메시지 접두사와 함께 event를 거부합니다.

event 내용 자체는 공개일 수 있습니다. `-` 태그는 그 태그를 존중하는 relay에 누가 event를 게시할 수 있는지만 제어합니다. 이는 [NIP-29](/ko/topics/nip-29/) 반폐쇄형 피드, 멤버 전용 relay 공간, 기타 작성자가 relay 그래프를 통한 재배포를 제한하고 싶은 상황에 적용됩니다. NIP-70은 새로운 event kind가 아니라 단일 태그 규약이므로, 기존 어떤 event kind에도 붙을 수 있습니다.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

relay가 원본 event의 제3자 게시를 막더라도, 누군가는 내용을 repost 안에 다시 담을 수 있습니다. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251)은 relay가 protected event를 포함한 kind 6 및 kind 16 repost도 거부하도록 요구해 이 문제를 해결합니다. [strfry PR #156](https://github.com/hoytech/strfry/pull/156)은 protected event용 NIP-42 인증 처리를 추가하고, [strfry PR #176](https://github.com/hoytech/strfry/pull/176)은 protected 콘텐츠를 담은 repost를 막습니다.

NIP-70은 relay 동작을 제어합니다. 수신자가 내용을 다른 곳에 복사하는 것 자체는 막지 못하며, 사양도 이를 명시합니다. `-` 태그는 relay가 재게시를 거부할 수 있도록 하는 기계 판독 가능한 신호입니다. 비교하자면 [NIP-62](/ko/topics/nip-62/)(Request to Vanish)는 사후에 relay에 삭제를 요청하고, NIP-70은 수집 시점에서 권한 없는 게시를 막습니다. 두 방식은 상호보완적입니다. 작성자는 확산을 제한하기 위해 event를 protected로 표시하고, 이후 이를 수용한 relay에서 내용을 제거하고 싶다면 삭제를 요청할 수 있습니다.

---

이번 주는 여기까지입니다. 뭔가를 만들고 있거나 공유할 소식이 있나요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ko/topics/nip-17/) DM으로 연락</a>하시거나 Nostr에서 찾아주세요.
