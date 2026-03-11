---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-03-11
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [Shopstr](https://github.com/shopstr-eng/shopstr)와 [Milk Market](https://github.com/shopstr-eng/milk-market)이 에이전트 기반 커머스를 위한 MCP 인터페이스를 추가했고, [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber), [strfry](https://github.com/hoytech/strfry)는 앱, signer, relay 소프트웨어 전반에 [NIP-42](/ko/topics/nip-42/) (릴레이에 대한 클라이언트 인증) relay 인증과 보호된 이벤트 지원을 더했다. [Route96](https://github.com/v0l/route96)는 AI 라벨링, moderation queue, perceptual hashing, 기계 판독 가능한 서버 문서를 중심으로 두 번의 릴리스를 냈다. 이미 웹에서 서비스 중인 [Samizdat](https://github.com/satsdisco/samizdat)는 첫 Android alpha를 출시했고, 이후 [NIP-55](/ko/topics/nip-55/) (Android 서명 애플리케이션) signer 지원도 추가했다. [Formstr](https://github.com/formstr-hq/nostr-forms)는 [NIP-49](/ko/topics/nip-49/) (개인 키 암호화)을 통한 signup을 추가했고, [Amethyst](https://github.com/vitorpamplona/amethyst)는 Namecoin 기반 [NIP-05](/ko/topics/nip-05/) (도메인 검증) 해석 작업을 내보냈으며, [Mostro](https://github.com/MostroP2P/mostro)는 [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)를 출시했다. NIPs 저장소는 [NIP-91](/ko/topics/nip-91/) (필터용 AND 연산자)와 [NIP-66](/ko/topics/nip-66/) (릴레이 탐색 및 가동 모니터링)에 대한 방어 지침도 병합했다.

## 뉴스

<a id="shopstr-and-milk-market-open-mcp-commerce-surfaces"></a>
### Shopstr와 Milk Market, MCP 커머스 인터페이스 공개

Lightning과 Cashu 결제를 지원하는 P2P 마켓플레이스 [Shopstr](https://github.com/shopstr-eng/shopstr)는 [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2))를 병합해, 에이전트 계정 관리를 위한 API-key 인증 MCP 서버를 추가했다. 이 변경으로 에이전트 탐색용 `.well-known/agent.json`, MCP 온보딩 및 상태 엔드포인트, 주문 생성 및 결제 검증 라우트, 전용 구매 및 읽기 도구, API key 설정 화면이 들어갔다. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236)은 여기에 메시지, 주소, 주문 업데이트, 상품 사양 선택 같은 판매자 측 동작을 더했다. [PR #235](https://github.com/shopstr-eng/shopstr/pull/235)의 보안 수정은 단일 반복 SHA-256 API key 해시를 100,000회 salted PBKDF2로 교체했다.

에이전트는 이제 페이지를 스크레이핑하거나 클라이언트 동작을 역분석하지 않고도, 기존 [NIP-47](/ko/topics/nip-47/) (Nostr Wallet Connect) 및 [NIP-60](/ko/topics/nip-60/) (Cashu Wallet) 결제 흐름을 사용해 [NIP-99](/ko/topics/nip-99/) (분류형 목록) 목록을 읽고 checkout까지 진행할 수 있다.

Nostr 기반 식품 마켓플레이스 [Milk Market](https://github.com/shopstr-eng/milk-market)도 [milk.market](https://milk.market)에서 같은 MCP 및 API-key 기반을 [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3)으로 도입했다. [PR #10](https://github.com/shopstr-eng/milk-market/pull/10)은 구독 주문, 구매 후 배송지 변경, Stripe와 기타 fiat 결제 경로를 위한 멀티 머천트 및 멀티 통화 checkout 처리를 추가한다. 후속 [PR #11](https://github.com/shopstr-eng/milk-market/pull/11)은 새 설치 시 failed relay publishes 테이블이 생성되지 않아 첫 로드에서 500 오류를 내던 시작 데이터베이스 초기화 버그를 수정했다. 에이전트 대상 인터페이스는 Shopstr의 Bitcoin 네이티브 checkout과 Milk Market의 fiat 및 Bitcoin 혼합 checkout 모두에서 동작한다.

### Bunker, Signer, Relay 전반의 NIP-42 relay 인증

OAuth 공급자를 Nostr 서명으로 연결하는 [NIP-46](/ko/topics/nip-46/) (Nostr Connect) bunker인 [OAuth Bunker](https://github.com/flox1an/oauth-bunker)는 [NIP-07](/ko/topics/nip-07/) (브라우저 확장 서명자) 로그인, 단일 신원 자동 선택, 삭제된 신원 정리 기능을 추가했다([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). 이제 신원이 하나뿐이면 bunker가 프롬프트를 띄우지 않고 자동으로 그것을 선택한다. 신원을 삭제하면 매달린 assignment와 connection도 함께 제거된다. [Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc)은 할당된 사용자용 `ALWAYS_ALLOWED_KINDS` 설정 경로를 추가하며, 기본값으로 kind `30078` 앱 전용 데이터를 허용해 위임된 신원이 이벤트별 승인 없이 앱 전용 저장소에 쓸 수 있게 한다.

Android의 대표 [NIP-55](/ko/topics/nip-55/) signer인 [Amber](https://github.com/greenart7c3/Amber)는 한 주 동안 네 번의 pre-release를 포함한 [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4)를 배포했다. [PR #317](https://github.com/greenart7c3/Amber/pull/317)은 kind `22242` 요청에 대한 [NIP-42](/ko/topics/nip-42/) relay 인증 처리를 추가한다. 구현에는 relay별 권한을 추적하는 새 데이터베이스 컬럼과 `(pkKey, type, kind, relay)`에 대한 고유 인덱스가 포함된다. 사용자는 relay별 또는 wildcard `*` 범위로 모든 relay에 대해 허용 또는 거부를 선택하고 이를 저장할 수 있는 전용 인증 화면을 보게 된다. wildcard 권한은 특정 kind에 대한 relay별 항목을 모두 지운다. [PR #318](https://github.com/greenart7c3/Amber/pull/318)은 뒤이어 다중 이벤트 요청 화면을 별도 화면으로 이동하는 대신 composable card로 인라인 세부 정보를 보여주도록 리팩터링했다. 이 릴리스에는 기본 프로필 relay 업데이트, bottom-sheet 요청 표시, StrongBox keystore 비활성화를 통한 MediaTek 기기 충돌 수정도 포함된다.

relay 측에서는 [strfry PR #156](https://github.com/hoytech/strfry/pull/156)이 [NIP-70](/ko/topics/nip-70/) (보호된 이벤트)을 위한 NIP-42 인증 처리를 구현했고, [PR #176](https://github.com/hoytech/strfry/pull/176)은 보호된 이벤트를 포함한 repost를 거부한다.

<a id="notedeck-adds-nip-11-relay-limits-and-agentium-features"></a>
### Notedeck, NIP-11 relay 제한과 Agentium 기능 추가

Damus 팀의 네이티브 데스크톱 클라이언트 [Notedeck](https://github.com/damus-io/notedeck)은 이번 주 14개의 PR을 병합했다. [PR #1316](https://github.com/damus-io/notedeck/pull/1316)은 [NIP-11](/ko/topics/nip-11/) (릴레이 정보 문서) relay 제한값 가져오기를 추가해, 이제 모든 outbox relay가 relay 정보 문서의 `max_message_length`와 `max_subscriptions`를 존중한다. 구현에는 백그라운드 job 처리, 연결 재시도를 위한 jitter 포함 exponential backoff, 커스텀 HTTP Accept 헤더가 들어간다. [PR #1312](https://github.com/damus-io/notedeck/pull/1312)는 계정 전환 후 DM이 가끔 로드되지 않던 버그를 수정했고, [PR #1333](https://github.com/damus-io/notedeck/pull/1333)은 오류 발생 시 broadcast spam을 막기 위해 multicast relay 통신에 backoff 메커니즘을 추가했다.

Agentium 서브시스템(Notedeck 내장 코딩 에이전트 UI, 내부 명칭 "Dave")은 클립보드 이미지 붙여넣기, kind `31991` 이벤트를 통한 기기 간 동기화 실행 구성([NIP-33](/ko/topics/nip-33/) (매개변수화된 대체 가능 이벤트)), git worktree 생성기, 세션별 backend 선택용 model picker를 받았다([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338)은 headless UI 테스트를 위해 `egui_kittest`를 통합했고, [PR #1339](https://github.com/damus-io/notedeck/pull/1339)은 클라이언트별 새 contact list 생성 수를 추적하는 dashboard card를 추가했다. 오픈 상태인 [PR #1314](https://github.com/damus-io/notedeck/pull/1314)는 ElectrumX 조회, SOCKS5 Tor 라우팅, 검색창 통합과 함께 Amethyst의 Namecoin NIP-05 해석을 Notedeck으로 포팅한다.

<a id="divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import"></a>
### diVine, E2E 테스트 인프라와 NIP-49 가져오기를 포함한 v1.0.6 출시

[divine.video](https://divine.video)에서 Vine 아카이브를 복원하는 쇼트폼 루프 비디오 클라이언트 [diVine](https://github.com/divinevideo/divine-mobile)은 127개의 병합된 PR을 담은 [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6)을 출시했다. 이 릴리스는 [NIP-49](/ko/topics/nip-49/) 계정 가져오기, 외부 [NIP-05](/ko/topics/nip-05/) 지원, 다중 계정 처리, macOS 및 실험적 Linux 빌드, 로컬 스토리지 기반으로 다시 설계한 drafts 및 clips 라이브러리를 추가한다.

엔지니어링 측면에서는 [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928)이 Docker backend 스택(relay, API, Blossom, Postgres, Redis, ClickHouse)을 상대로 Patrol을 사용한 네이티브 UI 자동화용 전체 E2E 통합 테스트 인프라를 추가한다. 다섯 개의 인증 여정 테스트는 등록, 검증, 비밀번호 재설정, 세션 만료, 토큰 갱신을 다룬다. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105)는 비디오 로딩을 HLS 우선에서 direct MP4와 자동 HLS fallback으로 전환해 로드 시간을 30-60초에서 거의 즉시 수준으로 줄였다. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076)는 즉시 cold-start 표시를 위해 홈 피드 API 응답을 SharedPreferences에 캐시한다. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104)는 피드에서 `ai-generated` 콘텐츠 라벨을 숨김으로 강제하며, [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100)은 diVine 호스팅 비디오만 보여주는 안전 설정을 추가한다. Hive에서 Drift로의 프로필 캐시 마이그레이션은 [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883), [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903)에 걸쳐 계속되며, Hive 코드 약 1,074줄을 Drift DAO로 대체한다.

### Vector v0.3.2, NIP-77 negentropy sync와 MLS 개선 포함

[NIP-17](/ko/topics/nip-17/) (비공개 다이렉트 메시지)과 [NIP-44](/ko/topics/nip-44/) (Encrypted Payloads) 암호화를 사용하는 MLS 그룹 암호화 기반 프라이버시 데스크톱 메신저 [Vector](https://github.com/VectorPrivacy/Vector)는 [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2)를 출시했다. 핵심 변화는 MLS 그룹 sync를 위한 NIP-77 negentropy([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac))로, parallel boot를 사용해 놓친 메시지를 훨씬 빠르게 따라잡는다. 이 릴리스는 완전한 Linux 지원을 포함한 재구축된 오디오 엔진, blurred preview가 있는 이미지 spoiler, rich link preview가 붙는 클릭 가능한 hyperlink, 그룹 관리자를 위한 `@everyone` 포함 `@mention` ping, emoji shortcode autocomplete, 그룹 mute, 기존 reaction에 tap-to-react, 취소 가능한 파일 업로드도 추가한다. Vector는 [commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)에서 NIP-17 그룹 채팅 이벤트를 명시적으로 필터링하며, 그룹 암호화에는 MLS만 사용한다.

## 릴리스

### Route96 v0.5.0 및 v0.5.1

Blossom과 [NIP-96](/ko/topics/nip-96/) (HTTP File Storage)를 지원하는 미디어 서버 [Route96](https://github.com/v0l/route96)는 [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0)과 [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1)을 출시했다. v0.5.0은 자동 AI 라벨링, 라벨이 없는 업로드의 소급 백필, flagged file용 moderation queue, EXIF 기반 프라이버시 거부, 금지 해시 처리를 추가한다.

v0.5.1은 perceptual image hash, 유사 이미지 조회를 위한 locality-sensitive hashing, 배치 admin 엔드포인트, 그리고 에이전트 도구용 서버의 Blossom 및 NIP-96 API 표면을 설명하는 공개된 [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1)를 추가한다. [PR #58](https://github.com/v0l/route96/pull/58)은 백그라운드 worker를 완전 비동기 Tokio task로 옮기고, [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8)는 hot loop를 피하기 위한 backoff를 추가한다.

### Samizdat v1.0.0-alpha

[samizdat.press](https://samizdat.press)에서 이용 가능한 장문 리더이자 퍼블리셔 [Samizdat](https://github.com/satsdisco/samizdat)는 첫 Android 빌드인 [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha)를 출시했다. 앱은 Press, Feed, Saved, Write 보기로 이어지는 하단 탭 내비게이션과 함께 큐레이션된 Nostr 장문 기사 Press 페이지로 시작한다. Android 빌드는 생체 인증 잠금 해제를 갖춘 Android Keystore 암호화를 통한 네이티브 키 저장소를 추가하고, `nostr:` URI와 `samizdat.press` 딥링크를 처리하며, 직접 키 가져오기를 요구하는 대신 Android 앱 chooser를 통한 signer handoff(Amber, Primal 등)를 지원한다. pull-to-refresh, 다양한 화면 크기의 safe-area 처리, 네이티브 share, clipboard, haptics, splash-screen 통합도 이제 웹 래퍼가 아니라 Android shell에 포함된다.

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6)은 Amber와 Primal 흐름을 위한 intent 기반 [NIP-55](/ko/topics/nip-55/) 서명을 추가하고, [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614)은 JavaScript bridge 우회책을 `startActivityForResult`를 사용하는 네이티브 Capacitor plugin으로 교체한다. 이 앱은 Android 7.0+ (API 24)가 필요하며, 이번 alpha에서는 debug APK로 배포되고, 아직 push notification은 없다. 현재 게시 기능은 signer 앱에 의존하며, `nsec` 로그인은 로컬 읽기와 계정 접근을 담당한다.

### Calendar by Form* v0.2.0

[calendar.formstr.app](https://calendar.formstr.app)에서 제공되는, [NIP-59](/ko/topics/nip-59/) (Gift Wrap) 기반 비공개 이벤트 공유를 지원하는 탈중앙화 캘린더 앱 [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)는 [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38)과 함께 [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0)을 출시했다. 이 릴리스는 [NIP-52](/ko/topics/nip-52/) (Calendar Events)의 반복 이벤트 처리를 확장해, v0.1.0의 단일 이벤트 기반을 넘어선다. 내부 변경은 로컬 이벤트 저장소, signer 처리, Android notification 배선에도 영향을 준다. 지난달 저장소 이전에 이어 Formstr 조직에서 나온 두 번째 활발한 애플리케이션이다.

### Mostro v0.16.4

Nostr 기반 P2P Bitcoin 거래소 [Mostro](https://github.com/MostroP2P/mostro)는 [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)를 출시했다. [지난주 다룬](/ko/newsletters/2026-03-04-newsletter/) 분쟁 세션 복구([PR #599](https://github.com/MostroP2P/mostro/pull/599))와 자동 종료([PR #606](https://github.com/MostroP2P/mostro/pull/606)) 수정이 여기에 포함된다. 이번 릴리스의 새 내용으로는 kind `38384` 사용자 평점 이벤트에 `days` 필드를 추가하는 [PR #625](https://github.com/MostroP2P/mostro/pull/625), 같은 평점 이벤트에 만료를 추가하는 [PR #612](https://github.com/MostroP2P/mostro/pull/612), 하드코딩된 24시간 창 대신 구성된 만료 설정을 주문 이벤트에 적용하는 [PR #614](https://github.com/MostroP2P/mostro/pull/614)이 있다. [PR #622](https://github.com/MostroP2P/mostro/pull/622)은 중복 개발 수수료 결제를 막기 위한 idempotency 검사를 추가한다.

### Mostro Mobile v1.2.1

Mostro P2P 거래소용 Flutter 클라이언트 [Mostro Mobile](https://github.com/MostroP2P/mobile)은 11개의 새 기능과 11개의 버그 수정을 담은 [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1)을 출시했다. 이 릴리스는 분쟁 채팅의 암호화 멀티미디어 렌더링([PR #514](https://github.com/MostroP2P/mobile/pull/514)), 주문이 종료 상태에 도달했을 때 분쟁 UI 자동 종료([PR #503](https://github.com/MostroP2P/mobile/pull/503)), NWC 지갑 가져오기를 위한 QR 스캔([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), 프랑스어 번역, FCM push notification 처리를 추가한다. [PR #496](https://github.com/MostroP2P/mobile/pull/496)은 bip340 의존성을 v0.2.0에 고정해 Schnorr signature padding 버그를 수정한다.

### 0xchat v1.5.4

Cashu 지원을 갖춘 Telegram 스타일 메시징 클라이언트 [0xchat](https://github.com/0xchat-app/0xchat-app-main)는 Linux 데스크톱 수정에 초점을 맞춘 [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release)를 배포했다. AppImage dock icon, emoji 렌더링, context menu freeze, reply/copy UI 멈춤이 여기에 포함된다. 이 릴리스는 이미지 업로드 문제와 npub.cash 통합도 수정한다. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49)는 아무 일도 하지 않으면서 glassmorphic repaint를 강제하던 3초 polling timer를 제거해 불필요한 UI rebuild를 없애고, relay, contacts, channel 시작을 막던 event cache load를 동시 실행으로 바꿔 로그인 초기화도 풀어낸다.

### Keep v0.6.0

Android용 FROST threshold signer [Keep](https://github.com/privkeyio/keep-android)는 [NIP-55](/ko/topics/nip-55/)와 [NIP-46](/ko/topics/nip-46/) 지원을 갖춘 채 [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0)과 [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1)을 출시했다. v0.6.0은 wallet descriptor 조정 및 관리 UI, 생체 인증이 포함된 backup/restore 흐름([PR #184](https://github.com/privkeyio/keep-android/pull/184)), threshold share에서 `nsec` 복구([PR #187](https://github.com/privkeyio/keep-android/pull/187)), Rust UniFFI를 통한 cross-platform animated QR frame 생성([PR #188](https://github.com/privkeyio/keep-android/pull/188)), chain 검증이 포함된 signing audit trail([PR #189](https://github.com/privkeyio/keep-android/pull/189))을 추가한다. v0.6.1은 라이선스를 AGPL-3.0에서 MIT로 전환한다([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump.me](https://njump.me)에서 Nostr 콘텐츠를 보여주는 정적 게이트웨이 [njump](https://github.com/fiatjaf/njump)는 `note1` 코드 파싱의 호환성 깨짐 변경과 기저 nostr 라이브러리 업데이트를 담은 [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0)을 출시했다.

### Roadstr v0.1.1

Nostr를 사용하는 탈중앙화 도로 이벤트 신고 앱 [Roadstr](https://github.com/jooray/roadstr)는 첫 데모 릴리스 [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1)을 배포했다. 이 앱은 openfreemap.org의 vector tile을 사용해 지도 위에 도로 이벤트를 표시한다.

### Bitcredit v0.5.3

Nostr 전송 계층과 전용 relay를 갖춘 전자 어음 애플리케이션 [Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core)는 [bit.cr](https://www.bit.cr/)에서 [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)를 출시했다. [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)은 결제 및 수락 상태를 위한 `payment_actions`와 `bill_state` 필드를 API에 추가하고, [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)는 익명 signer의 서명 주소 처리를 수정한다.

### OpenChat v0.1.0-alpha.3

Marmot 프로토콜의 .NET MLS 및 C# 라이브러리 위에 구축된 채팅 애플리케이션 [OpenChat](https://github.com/DavidGershony/openChat)은 [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3)를 출시했다. 이 릴리스는 Amber와 [NIP-46](/ko/topics/nip-46/) 흐름을 위한 외부 signer 지원([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), 크래시 윈도우 데이터 손실을 없애기 위해 MLS state persistence를 MLS 서비스 내부로 이동하는 변경([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), 새 CI 파이프라인을 통한 Windows, Linux, Android 빌드 배포를 포함한다.

### OpenSignal v1.0.0

Nostr용 Kotlin Multiplatform 트레이딩 copilot [OpenSignal](https://github.com/turizspace/opensignal)는 [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0)을 출시했다. 이 릴리스는 domain logic, chart 렌더링, Nostr 인증 및 게시, Blossom [NIP-96](/ko/topics/nip-96/) 업로드 지원, ONNX 기반 AI 추론 hook을 Desktop 및 Android shell 전반에서 공유하는 KMP 모듈을 패키징한다. 공개된 아키텍처에는 chart screenshot 분석, 모델 학습 파이프라인, 크기와 경고가 포함된 구조화된 거래 계획을 생성하는 risk engine을 위한 FastAPI AI 서비스도 포함된다. 로그인은 raw `nsec` 키 또는 외부 signer를 모두 지원하며, 출력 흐름은 로컬 전용 분석이 아니라 Nostr event 게시로 끝난다.

## 프로젝트 업데이트

### Formstr

Nostr 기반 Google Forms 대안 [Formstr](https://github.com/formstr-hq/nostr-forms)은 [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8))를 병합해 [NIP-49](/ko/topics/nip-49/) (개인 키 암호화) 암호화 개인 키를 사용하는 signup 흐름을 추가했다. 이 변경 전에는 사용자가 Formstr를 쓰려면 [NIP-07](/ko/topics/nip-07/) 브라우저 확장이나 raw `nsec` 붙여넣기 중 하나가 필요했다. 새 흐름은 클라이언트 측에서 key pair를 생성하고, NIP-49의 scrypt + XChaCha20-Poly1305 방식으로 사용자가 고른 비밀번호로 개인 키를 암호화한 뒤, 결과 `ncryptsec` 문자열을 저장한다. 이제 사용자는 signer 확장을 설치하지 않고도 비밀번호로 다시 로그인할 수 있다. 키 관리는 끝까지 클라이언트 측에 머문다.

### Amethyst

기능이 풍부한 Android 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)는 [지난주 열려 있던](/ko/newsletters/2026-03-04-newsletter/) Namecoin 기반 [NIP-05](/ko/topics/nip-05/) 해석 작업을 포함한 네 개의 PR을 병합했다. [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)는 `.bit`, `d/`, `id/` 식별자에 대해 ElectrumX를 통한 검열 저항형 NIP-05 검증을 추가한다. Amethyst가 NIP-05 필드에서 이런 접미사 중 하나를 감지하면, ElectrumX-NMC 서버에 이름의 거래 기록을 질의하고, 최신 출력에서 `NAME_UPDATE` 스크립트를 파싱해 Nostr pubkey를 추출하며, 36,000블록(Namecoin의 만료 창)보다 오래된 이름은 거부한다. ElectrumX 연결은 Tor가 활성화되면 SOCKS5를 통해 라우팅되며, clearnet과 `.onion` 엔드포인트 사이에서 동적으로 서버를 선택한다. 1시간 TTL을 가진 LRU 캐시는 반복 블록체인 질의를 막는다.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771)은 그 흐름의 race condition과 resolver 정확성을 수정한다. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785)는 새 사용자가 signup 중 일반 NIP-05 식별자와 Namecoin 기반 식별자 모두에서 follow list를 가져올 수 있게 한다. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786)은 사용자가 어떤 서버가 조회를 처리할지 고를 수 있도록 커스텀 ElectrumX 서버 설정을 추가한다.

### nostr-idb

IndexedDB에 Nostr event를 저장하는 helper 메서드를 제공하는 라이브러리 [nostr-idb](https://github.com/hzrd149/nostr-idb)는 [NIP-91](/ko/topics/nip-91/) AND 태그 필터 지원을 추가하는 [PR #6](https://github.com/hzrd149/nostr-idb/pull/6)을 병합했다. 이 변경은 클라이언트 측 필터 매칭에 교집합 의미론을 추가해, IndexedDB 질의가 나열된 태그 값 중 하나가 아니라 전부를 요구할 수 있게 한다. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8)은 라이브러리를 최신 NIP-DB 인터페이스로 업데이트하고, 후속 [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972)은 subscribe deadlock을 고치고 nostr-tools를 production 의존성에서 제거한다.

### Pensieve

ClickHouse 분석을 갖춘 archive-first Nostr 인덱서 [Pensieve](https://github.com/andotherstuff/pensieve)는 API CPU 급증을 줄이기 위해 항목별 cache TTL 강제와 key별 miss coalescing을 추가하는 [PR #8](https://github.com/andotherstuff/pensieve/pull/8)을 병합했다. 비용이 가장 높은 시계열 엔드포인트(engagement stats, 시간대별 activity, kind별 activity)는 이제 동기화된 재계산 폭풍을 일으키는 대신 10분 서버 측 TTL을 사용한다.

### Blossom

탈중앙화 미디어 호스팅 프로토콜이자 서버 스택인 [Blossom](https://github.com/hzrd149/blossom)은 두 개의 BUD-11 인증 업데이트를 병합했다. [PR #91](https://github.com/hzrd149/blossom/pull/91)은 선택적 인증을 별도의 BUD로 옮기고 `x` 및 `server` 태그의 역할을 명확히 한다. [PR #93](https://github.com/hzrd149/blossom/pull/93)은 엔드포인트별 auth 동작을 정리하고 업로드 검증용 `X-SHA-256` 헤더를 공식화한다. 이 두 PR은 인증 로직을 BUD-11로 통합하고 업로드, 삭제, 미디어 관리 흐름의 요청 해싱에 대한 모호함을 제거한다.

<a id="nip-updates"></a>
## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-91](/ko/topics/nip-91/) (필터용 AND 연산자)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): 태그 필터에 교집합 의미론을 추가해 relay가 나열된 태그 값 중 하나가 아니라 모두를 요구하는 질의에 응답할 수 있게 한다. 태그가 많은 질의에서 클라이언트 측 후처리와 대역폭을 줄인다.

- **[NIP-66](/ko/topics/nip-66/) (릴레이 탐색 및 가동 모니터링): Defensive Measures** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): [지난주 다룬](/ko/newsletters/2026-03-04-newsletter/) outbox 벤치마크 작업에 이어, 이 사양은 relay 모니터링 데이터의 좋지 않은 경로에 대한 경고를 추가한다. 클라이언트는 동작을 위해 kind `30166` 모니터링 이벤트를 필수로 요구해서는 안 된다. 모니터는 틀릴 수도 있고, 오래됐을 수도 있고, 악의적일 수도 있다. 클라이언트는 출처를 교차 검증하고 단일 피드만 보고 사용자의 relay 그래프 큰 부분을 잘라내지 않아야 한다.

- **[NIP-39](/ko/topics/nip-39/) (프로필 내 외부 신원): kind 10011 레지스트리 정리** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): kind `10011` 참조를 사양에 직접 추가해, [지난주 다룬](/ko/newsletters/2026-03-04-newsletter/#amethyst) Amethyst 구현과 맞춘다.

**오픈 PR 및 논의:**

- **[NIP-70](/ko/topics/nip-70/) (보호된 이벤트): 보호된 이벤트를 포함한 repost 거부** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): relay가 원본 이벤트에는 NIP-70을 적용하면서 동일한 콘텐츠를 담은 repost는 받아들인다면 `-` 태그는 사실상 효력이 없다. 이 PR은 relay가 kind 6 및 kind 16의 보호된 이벤트 repost도 거부해야 한다는 규칙을 추가한다. [strfry PR #176](https://github.com/hoytech/strfry/pull/176)이 이미 이를 구현했다.

- **[NIP-71](/ko/topics/nip-71/) (비디오 이벤트): 다중 오디오 트랙** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): 대체 트랙, 언어 변형, 오디오 전용 스트림을 위한 audio `imeta` 태그를 추가한다. 클라이언트는 안정적인 비디오 파일을 유지한 채 오디오 언어를 전환하거나, podcast 같은 콘텐츠를 위해 오디오를 별도 트랙으로 제공할 수 있다.

- **[NIP-11](/ko/topics/nip-11/) (릴레이 정보 문서) 및 [NIP-66](/ko/topics/nip-66/) relay 속성** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): relay 정보 문서에 구조화된 `attributes` 필드를 추가해, 클라이언트와 discovery 도구가 현재의 자유 텍스트 설명을 넘어 기계 판독 가능한 메타데이터를 얻을 수 있게 한다.

<a id="nip-deep-dive-nip-49-private-key-encryption"></a>
## NIP 심층 분석: NIP-49 (개인 키 암호화)

[NIP-49](/ko/topics/nip-49/)는 클라이언트가 개인 키를 비밀번호로 암호화하고 그 결과를 `ncryptsec` bech32 문자열로 인코딩하는 방법을 정의한다. [Formstr](#formstr)는 새 signup 흐름에서 NIP-49를 사용한다.

이 형식은 전용 event kind에 묶여 있지 않다. 클라이언트는 원시 32바이트 secp256k1 개인 키에서 시작하고, scrypt로 사용자의 비밀번호에서 대칭 키를 파생하며, XChaCha20-Poly1305로 키를 암호화한 뒤, 결과를 bech32 `ncryptsec` 문자열로 감싼다. 1바이트 플래그는 이 키가 암호화 전에 안전하지 않게 처리된 적이 있었는지를 기록한다.

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

위 JSON 이벤트는 애플리케이션 수준 예시이지 NIP-49 요구사항은 아니다. NIP는 암호화된 키 형식을 표준화할 뿐이다. 클라이언트는 `ncryptsec`를 로컬에 저장하거나, 앱 전용 저장소로 동기화하거나, 백업 문자열로 내보낼 수 있다. 비밀번호는 키 파생 전에 Unicode NFKC로 정규화되므로, 클라이언트와 플랫폼이 달라도 같은 비밀번호가 일관되게 복호화된다.

1바이트 키 보안 플래그에는 세 가지 정의된 값이 있다. `0x00`은 키 처리 이력이 알려지지 않았음을 뜻하고, `0x01`은 키가 암호화 전에 안전하지 않게 처리된 것이 알려져 있음을 의미하며(예: 웹 폼에 평문으로 붙여넣음), `0x02`는 키가 안전한 문맥에서 생성 및 암호화되었고 한 번도 노출되지 않았음을 뜻한다. 클라이언트는 이를 사용해 안전하지 않은 이력이 알려진 키를 가져올 때 경고를 표시할 수 있다.

NIP-49는 평문 `nsec` 내보내기보다 키를 더 잘 보호하지만, 암호화 강도는 비밀번호와 설정된 scrypt 비용만큼만 강하다. `LOG_N` 값이 높을수록 오프라인 추측은 어려워지지만 정상 복호화는 느려진다. 이 사양은 공격자가 오프라인 크래킹을 위해 암호문을 수집하는 데 이득을 보기 때문에, 암호화된 키를 공개 relay에 게시하지 말라고 경고한다. 비교하자면 [NIP-46](/ko/topics/nip-46/) 원격 서명은 키를 아예 노출하지 않고, [NIP-55](/ko/topics/nip-55/) Android 서명은 키를 전용 signer 앱 안에 둔다. NIP-49는 다른 자리를 채운다. 자기 키를 직접 관리하는 사용자를 위한 휴대 가능한 암호화 백업이다.

구현 사례로는 signup용 [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434), ncryptsec backup 및 restore를 지원하는 [Amber](https://github.com/greenart7c3/Amber), 계정 가져오기를 지원하는 [diVine v1.0.6](#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import), FROST share 내보내기를 지원하는 [Keep v0.6.0](#keep-v060), 그리고 [nsec.app](https://nsec.app) 및 [Alby](https://github.com/getAlby/hub) 같은 키 관리 도구가 있다.

<a id="nip-deep-dive-nip-70-protected-events"></a>
## NIP 심층 분석: NIP-70 (보호된 이벤트)

[NIP-70](/ko/topics/nip-70/)은 보호된 이벤트를 정의한다. 이벤트가 `["-"]` 태그를 가지면, relay는 [NIP-42](/ko/topics/nip-42/) 인증을 요구하고 인증된 pubkey가 이벤트 작성자와 일치하지 않는 한 이를 거부해야 한다.

NIP-42 인증 흐름은 다음과 같다. relay가 무작위 문자열이 담긴 `AUTH` challenge를 보내면, 클라이언트는 relay URL과 challenge를 태그에 포함한 서명된 kind `22242` 이벤트로 응답한다. relay는 서명을 검증하고 auth 이벤트의 pubkey가 게시되는 보호된 이벤트의 pubkey와 일치하는지 확인한다. 두 pubkey가 일치하지 않으면 relay는 `restricted` 메시지 접두사와 함께 이벤트를 거부한다.

이벤트 콘텐츠 자체는 여전히 공개일 수 있다. `-` 태그가 제어하는 것은 그 태그를 존중하는 relay에 누가 해당 이벤트를 게시할 수 있느냐뿐이다. 이는 [NIP-29](/ko/topics/nip-29/) (릴레이 기반 그룹)의 반폐쇄형 피드, 멤버 전용 relay 공간, 그리고 작성자가 relay 그래프를 통한 재배포를 제한하고 싶은 다른 문맥을 포괄한다. NIP-70은 새로운 event kind가 아니라 단일 태그 관례이므로, 기존 어떤 event kind에도 `-` 태그를 실을 수 있다.

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

relay가 원본 이벤트의 제3자 게시를 막더라도, 누군가는 그 내용을 repost 안에 넣어 다시 게시할 수 있다. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251)은 relay가 보호된 이벤트의 kind 6 및 kind 16 repost도 거부하도록 요구함으로써 이 문제를 다룬다. [strfry PR #156](https://github.com/hoytech/strfry/pull/156)은 보호된 이벤트용 NIP-42 인증 처리를 추가했고, [strfry PR #176](https://github.com/hoytech/strfry/pull/176)은 보호된 콘텐츠를 포함한 repost를 차단한다.

NIP-70은 relay 동작을 제어한다. 수신자는 여전히 내용을 다른 곳에 복사할 수 있으며, 사양도 이를 명시한다. `-` 태그는 relay에 재게시를 거부하라는 기계 판독 가능한 신호를 준다. 비교하면 [NIP-62](/ko/topics/nip-62/) (Vanish Requests)는 relay에 사후 삭제를 요청하고, NIP-70은 수집 시점에 무단 게시를 막는다. 두 방식은 상호 보완적이다. 작성자는 이벤트를 보호된 것으로 표시해 확산을 제한하고, 이후 내용을 받아들인 relay에서 제거하고 싶다면 삭제를 요청할 수 있다.

---

이번 주는 여기까지입니다. 만들고 있는 것이 있거나 공유할 소식이 있나요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ko/topics/nip-17/) DM으로 연락</a>하시거나 Nostr에서 찾아주세요.
