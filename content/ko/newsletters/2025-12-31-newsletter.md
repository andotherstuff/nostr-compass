---
title: 'Nostr Compass #3'
date: 2025-12-31
translationOf: /en/newsletters/2025-12-31-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr 프로토콜 생태계에 대한 주간 가이드입니다.

**이번 주:** 2025년이 끝나가며, Nostr 진화의 12월 이정표 5년을 되돌아봅니다. 2020년 12월 fiatjaf의 첫 클라이언트 릴리스부터, 2022년 12월 Jack Dorsey의 결정적 14 BTC 기부, 그리고 이번 달 [NIP-55](/ko/topics/nip-55/) 서명자 확산과 NDK의 162배 캐시 속도 향상까지, 12월은 꾸준히 프로토콜의 전환점을 만들어 왔습니다. 이번 특집호는 12월마다의 기술적 역사를 따라가며, 두 개의 실험적 relay에서 50개국 2,500개 이상의 노드로 성장한 과정을 기록합니다. 여기에 Quartz를 통한 Amethyst의 데스크톱 모듈 구체화, 메시징 기능을 얻은 Notedeck, 웹 앱을 호스팅하는 Citrine, 비라틴 문자 국제화를 바로잡은 [NIP-54](/ko/topics/nip-54/)까지 다룹니다.

## 12월 회고: Nostr의 다섯 번의 12월

Nostr는 올해로 다섯 살이 됩니다. fiatjaf는 2020년 11월 7일 프로토콜을 시작했고, 이후의 모든 12월은 개념 검증, 글로벌 운동, 프로덕션 생태계로 이어지는 서로 다른 진화 단계를 보여줬습니다. 이번 글은 2020년 12월부터 2025년 12월까지, Nostr의 기반을 세우고 돌파구를 만든 형성기의 기술적 회고입니다.

### 2020년 12월: 창세기

Nostr가 존재한 첫 번째 완전한 달에 fiatjaf는 Quasar(Vue.js)와 absurd-sql을 사용해 로컬 스토리지를 구현한 프로토콜 최초의 클라이언트 [Branle](https://github.com/fiatjaf/branle)를 공개했습니다. 당시 fiatjaf는 이미 핵심 아키텍처를 세워 두었습니다. 사용자는 secp256k1 공개키로 식별되고, 모든 게시물은 암호학적으로 서명되며, relay는 서로 통신하지 않는 단순 저장소로 동작했습니다. 11월 16일에 시작된 텔레그램 그룹 [@nostr_protocol](https://t.me/nostr_protocol)에서 조율하던 소수의 초기 사용자들을 위해 한두 개의 실험적 relay가 돌아갔습니다. [초기 문서](https://fiatjaf.com/nostr.html)는 이를 "검열 저항적인 글로벌 소셜 네트워크를 만들 수 있는 가장 단순한 오픈 프로토콜"이라고 설명했고, 그 전제가 증명되기까지는 2년이 더 필요했습니다.

### 2021년 12월: 초기 개발

2021년 12월 31일, Cameri가 제출한 글을 통해 Nostr는 [Hacker News 첫 페이지](https://news.ycombinator.com/item?id=29749061)에 올랐고 110점과 138개의 댓글을 기록했습니다. 이는 더 넓은 개발자 커뮤니티가 프로토콜을 본격적으로 접한 첫 순간이었습니다. 당시 네트워크는 대략 7개의 relay와 1,000명 미만의 사용자로 운영됐습니다. Branle은 12월 31일 개인 키 가져오기와 멀티 relay 지원을 포함한 업데이트를 받았습니다. 커맨드라인 클라이언트 noscl도 터미널 기반 상호작용을 제공했습니다. 프로토콜 사양은 fiatjaf의 문서에 존재했지만, 공식 [NIPs 저장소](https://github.com/nostr-protocol/nips)가 만들어진 것은 2022년 5월이었습니다. fiatjaf의 표현대로, 이 프로토콜은 아직 "진행 중인 작업"이었습니다.

### 2022년 12월: 전환점

2022년 12월은 Nostr를 틈새 실험에서 주류 운동으로 바꿔놓았습니다. 촉매는 12월 15일에 왔습니다. Jack Dorsey가 프로토콜을 발견한 뒤 "우리가 Bluesky에 원했던 것이 100퍼센트지만, 회사가 만든 것은 아니다"라고 말하며 fiatjaf에게 [14.17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding)(약 245,000~250,000달러)를 기부했습니다. 12월 16일 fiatjaf는 이 자금을 Damus 개발자 William Casarin(jb55)과 나누겠다고 발표했고, Dorsey는 자신의 Nostr 계정(npub: `npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`)을 인증했습니다. 이 자금 지원은 프로젝트를 하룻밤 사이에 정당화했습니다.

같은 주, Twitter의 혼란은 채택을 더 밀어올렸습니다. 12월 14일과 15일에는 New York Times, CNN, Washington Post의 저명한 기자 계정이 정지됐습니다. 12월 18일 Twitter는 [Nostr, Mastodon, 기타 플랫폼 홍보 계정 금지](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/)를 발표했습니다. 이 정책은 반발 이후 다음 날 철회됐습니다. 그 이탈 흐름은 사용자들을 대안을 찾게 만들었습니다.

프로토콜 개발도 급증했습니다. 12월 16일 [NIP-19](/ko/topics/nip-19/)가 병합되며([#57](https://github.com/nostr-protocol/nips/pull/57)) 사람이 읽을 수 있고 구별 가능한 bech32 식별자(npub, nsec, note, nprofile, nevent)를 도입했습니다. NIPs 저장소에는 그달 36개 이상의 커밋이 기록됐고, NIP-40과 NIP-07 업데이트도 포함됐습니다. 클라이언트도 빠르게 늘어났습니다. Damus는 몇 시간 만에 TestFlight 베타 정원을 채웠고, Astral은 프로필 생성을 위해 Branle을 포크했으며, Snort는 "빠르고 검열 저항적인" 웹 클라이언트로 출시됐고, Vitor Pamplona는 Amethyst 개발을 시작했습니다. Alby v1.22.1 "Kemble's Cascade of Stars"는 12월 22일 [NIP-19](/ko/topics/nip-19/) 지원과 함께 출시됐습니다. 12월 7일 기준 Nostr에는 프로필을 가진 사용자가 약 800명이었지만, 2023년 1월 31일 Damus가 App Store에 올라간 뒤에는 폭발적으로 성장해 2023년 6월까지 315,000명 이상으로 늘었습니다.

### 2023년 12월: 생태계의 성숙

2023년 12월은 Nostr 프로토콜 보안에서 결정적인 변곡점이었습니다. 12월 20일, 독립적인 Cure53 보안 감사(NOS-01)에서 TypeScript, Go, Rust 구현 전반의 10개 이슈, 즉 타이밍 공격과 forward secrecy 우려가 발견된 뒤 [NIP-44 개정 3](https://github.com/nostr-protocol/nips/pull/746)이 병합됐습니다. 업데이트된 사양은 결함이 있던 [NIP-04](/ko/topics/nip-04/) 암호화를 ChaCha20과 HMAC-SHA256으로 대체했고, 현재 [NIP-17](/ko/topics/nip-17/) 개인 DM과 [NIP-59](/ko/topics/nip-59/) gift wrapping을 떠받치는 암호학적 기반을 세웠습니다. 같은 주인 12월 21일에는 [OpenSats가 네 번째 보조금 웨이브를 발표](https://opensats.org/blog/nostr-grants-december-2023)하며 Lume, noStrudel, ZapThreads, 독립적인 NIP-44 감사 등 7개 프로젝트를 지원했습니다. 이는 Damus, Coracle, Iris 등을 지원한 [2023년 7월 첫 번째 웨이브](https://opensats.org/blog/nostr-grants-july-2023)에 이은 것이며, 총 Nostr Fund 배분액은 39개 보조금에 걸쳐 약 340만 달러에 도달했습니다.

이 달은 생태계의 지속 가능성에 대한 긴장도 드러냈습니다. 12월 28일 William Casarin(jb55)은 [Stacker News 글](https://stacker.news/items/368863)에서 Apple의 인앱 zap 제한이 수익 가능성을 심각하게 막고 있다며 2024년이 "아마 Damus의 마지막 해가 될 것"이라고 썼습니다. Damus 팀은 이전에 VC 자금을 거절한 바 있습니다. 한편 [Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1)은 12월 26일 출시되며 [NIP-47](/ko/topics/nip-47/)에 `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info` 메서드를 확장했고, 이후 클라이언트 전반에 표준이 되는 지갑 통합의 토대를 마련했습니다.

### 2024년 12월: 프로토콜의 전진

2024년 12월은 11월 30일 [Notedeck Alpha 출시](https://damus.io/notedeck/)로 시작됐습니다. Damus 팀의 Rust 기반 데스크톱 클라이언트인 Notedeck은 다중 컬럼 인터페이스와 다중 계정 지원을 제공했습니다. Linux, macOS, Windows용으로 빌드됐고(Android는 2025년 예정), 처음에는 Damus Purple 구독자에게 배포되며 iOS를 넘어서는 전략적 확장을 보여줬습니다. 2주 뒤인 12월 16일에는 [OpenSats가 아홉 번째 보조금 웨이브를 발표](https://opensats.org/blog/9th-wave-of-nostr-grants)하며 AlgoRelay, Pokey, Nostr Safebox([NIP-60](/ko/topics/nip-60/) [Cashu](/ko/topics/cashu/) 토큰 저장), LumiLumi를 지원했습니다. 그 결과 총 Nostr Fund 배분액은 약 900만 달러가 되었고, 전년 대비 67% 증가했습니다.

이달에는 생태계 전반에서 클라이언트 성숙도도 크게 올라갔습니다. [Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0)은 12월 23일 File Metadata([NIP-92](/ko/topics/nip-92/)/[NIP-94](/ko/topics/nip-94/)) 지원, Blossom 통합, [NIP-50](/ko/topics/nip-50/) relay 검색과 함께 나왔습니다. [Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0)은 12월 12일 재작업된 온보딩과 nostr-editor 통합을 포함해 출시됐습니다. 프로토콜 개발도 계속 활발해서 12월 9일부터 22일까지 30개의 pull request가 제출됐고 그중 10개가 병합됐습니다. 여기에는 [NIP-46](/ko/topics/nip-46/)을 [NIP-44](/ko/topics/nip-44/) 암호화만 사용하도록 다시 쓰는 작업과 Signal 수준의 double ratchet 암호화를 위한 [NIP-104](/ko/topics/nip-104/) 작업이 포함됩니다. 네트워크 통계로는 일일 trusted pubkey event가 224,000개를 넘었고, contact list를 가진 신규 프로필은 전년 대비 4배 늘었으며, 공개 글쓰기 event는 50% 증가했습니다.

### 2025년 12월: 생태계 확장

2025년 12월은 프로토콜 성숙과 생태계 확장이 계속 이어졌습니다. 12월 21일 [OpenSats는 열네 번째 Nostr 보조금 웨이브를 발표](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)하며 세 프로젝트를 지원했습니다. 장문 콘텐츠용 creator portal과 [Cashu](/ko/topics/cashu/)/Nutzaps 결제를 통합한 멀티 플랫폼 클라이언트 YakiHonne, Amethyst를 구동하고 향후 iOS 버전을 가능하게 할 Vitor Pamplona의 Kotlin Multiplatform 라이브러리 Quartz, 그리고 PlebOne의 RSS-대-Nostr 양방향 통합인 Nostr Feedz입니다. 추가 갱신 보조금은 Dart NDK와 Mattn의 nostr-relay에 배정됐습니다.

프로토콜 진화도 계속됐습니다. [NIP-BE](/ko/topics/nip-be/)(Bluetooth Low Energy 메시징, [#1979](https://github.com/nostr-protocol/nips/pull/1979))는 11월에 병합돼 오프라인 기기 동기화를 가능하게 했습니다. [NIP-A4](/ko/topics/nip-a4/)(공개 메시지, kind 24, [#1988](https://github.com/nostr-protocol/nips/pull/1988))는 그달 말에 병합되며 스레딩 복잡성을 피하기 위해 `q` 태그를 사용하는 알림 화면 메시지를 정의했습니다. [NIP-29](/ko/topics/nip-29/)은 주요 명확화를 받으며([#2106](https://github.com/nostr-protocol/nips/pull/2106)) 진정으로 비공개이고 발견 불가능한 그룹을 위한 `hidden` 태그를 도입했습니다. [NIP-55](/ko/topics/nip-55/) 사양도([#2166](https://github.com/nostr-protocol/nips/pull/2166)) 정교화되어, 개발자가 백그라운드 프로세스에서 `get_public_key`를 호출하는 흔한 구현 실수를 바로잡았습니다.

클라이언트 측에서는 [Primal Android가 완전한 NIP-55 서명자](/en/newsletters/2025-12-24-newsletter/#news)가 되었고, `LocalSignerContentProvider`를 구현하는 여덟 개의 병합된 PR을 통해 Amber와 Aegis에 합류했습니다. [NDK 라이브러리는 162배 빠른 캐시 쿼리](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)를 달성했습니다. 중복 쓰기와 불필요한 LRU 캐시 조회를 제거하며 약 3,690ms에서 약 22ms로 개선됐습니다([PR #371](https://github.com/nostr-dev-kit/ndk/pull/371), [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)). Shopstr는 zap 기반 플래시 세일용 [Zapsnags](/en/newsletters/2025-12-24-newsletter/#news)를 도입했습니다. White Noise는 프라이버시 보호형 푸시 알림 [MIP-05](/ko/topics/mip-05/)를 출시했습니다. 자세한 내용은 [뉴스레터 #1](/en/newsletters/2025-12-17-newsletter/)과 [뉴스레터 #2](/en/newsletters/2025-12-24-newsletter/)에서 확인할 수 있습니다.

---

다섯 해 전 fiatjaf는 두 개의 실험적 relay에서 소수의 사용자를 위해 Branle을 공개했습니다. 오늘날 이 프로토콜은 140개 이상의 클라이언트, 50개국에 걸친 2,500개 이상의 relay, 수십만 개 키페어를 연결하는 성장하는 신뢰의 그물을 지원합니다. 이번 12월에도 주요 릴리스의 흐름은 이어졌습니다. Bluetooth 메시징, Android 서명자 확산, 인프라 보조금은 크로스플랫폼 도구에 대한 지속적인 투자를 보여줍니다.

## 뉴스

**Amethyst 데스크톱이 형태를 갖추다** - OpenSats 열네 번째 웨이브의 Quartz 보조금은 이미 결과를 내고 있습니다. [PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625)는 Compose Multiplatform을 사용해 Amethyst용 완전한 `:desktopApp` 모듈을 만들며, Desktop JVM에서 로그인과 글로벌 피드 화면이 동작합니다. 아키텍처는 `:commons` 모듈을 Kotlin Multiplatform으로 전환하고, `commonMain`, `jvmAndroid`, `androidMain`, `jvmMain`의 깔끔한 소스셋 구조를 도입해 Android와 데스크톱 간 UI 컴포넌트 공유를 가능하게 하면서, 플랫폼별 결정은 각 타깃에 맡깁니다. 이는 동일한 Kotlin Multiplatform 접근을 통해 장기적으로 iOS 버전까지 이어질 기반을 마련합니다.

**Amethyst 음성 답글** - davotoula의 크리스마스 선물입니다. [PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622)는 파형 시각화, 재녹음 지원, 미디어 서버 선택, 업로드 진행률 표시를 갖춘 전용 음성 답글 화면을 추가합니다. 사용자는 이제 루트 음성 메시지와 음성 답글 모두에 오디오로 답할 수 있습니다.

**Notedeck에 메시징 추가** - Damus 데스크톱 클라이언트 Notedeck은 [PR #1223](https://github.com/damus-io/notedeck/pull/1223)에서 메시지 기능을 얻으며, 타임라인 탐색을 넘어 직접 커뮤니케이션 영역으로 확장됐습니다.

**Citrine이 웹 앱을 호스팅** - Citrine은 이제 [웹 애플리케이션을 호스팅](https://github.com/greenart7c3/Citrine/pull/81)할 수 있어, 휴대폰을 로컬 우선 Nostr 웹 서버로 바꿉니다. 별도의 [PR #85](https://github.com/greenart7c3/Citrine/pull/85)는 네트워크 연결이 복구될 때 자동 재연결과 event 브로드캐스팅을 추가했고, Android API 레벨 전반에 걸친 포괄적인 테스트도 포함합니다.

**Nostrability 개발자 툴킷 레지스트리** - [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264) 트래커는 TypeScript, Rust, Python, Go, Dart, Swift 등 다양한 언어의 SDK, 라이브러리, 개발자 도구를 큐레이션한 레지스트리를 유지합니다. Nostr 개발을 처음 시작한다면, 자신의 스택에 맞는 도구를 찾는 출발점으로 유용합니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

- **[NIP-54](/ko/topics/nip-54/)** - 위키 `d` 태그 정규화를 위한 중요한 국제화 수정([#2177](https://github.com/nostr-protocol/nips/pull/2177)). 기존 규칙은 모든 비ASCII 문자를 `-`로 변환해 일본어, 중국어, 아랍어, 키릴 문자 등 비라틴 문자 지원을 깨뜨렸습니다. 업데이트된 사양은 UTF-8 문자를 보존하고, 대소문자 변형이 있는 문자에만 소문자 처리를 적용하며, 포괄적인 예시를 포함합니다. `"ウィキペディア"`는 그대로 `"ウィキペディア"`로 유지되고, `"Москва"`는 `"москва"`가 되며, `"日本語 Article"` 같은 혼합 스크립트는 `"日本語-article"`로 정규화됩니다.

## 릴리스

**Zapstore 1.0-rc1** - Nostr 기반 permissionless 앱 스토어가 [새 아키텍처의 첫 release candidate](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1)를 출시했습니다. 완전한 UI 리프레시, 개선된 에러 처리를 갖춘 재작성된 패키지 매니저, 큐레이션 탐색용 App Stacks, 다시 설계된 프로필 화면, 백그라운드 업데이트 확인, 릴리스 목록의 무한 스크롤이 포함됩니다.

**KeyChat v1.38.1** - MLS 기반 암호화 메시징 앱이 [UnifiedPush 지원](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489)을 추가해 Android와 Linux 푸시 알림을 제공하고, 프라이버시 관련 작업을 위한 생체 인증도 도입했습니다. Android, Windows, macOS, Linux에서 사용할 수 있습니다.

**Alby Go v2.0.0** - 모바일 Lightning 지갑 companion 앱이 [시각적 리디자인](https://github.com/getAlby/go/releases/tag/v2.0.0)과 함께 출시됐습니다. 새 로고, 갱신된 색상 팔레트, 재설계된 주소록, 개선된 금액 입력 키보드가 포함됩니다. BTC Map은 이제 홈 화면에서 접근할 수 있고, 거래 설명은 알림에 표시됩니다.

**nak v0.17.4** - fiatjaf의 커맨드라인 Nostr 도구가 [새 버전으로 릴리스](https://github.com/fiatjaf/nak/releases/tag/v0.17.4)됐습니다. 지난주 v0.17.3에서 수정된 LMDB Linux 제한 문제에 이은 릴리스입니다.

## 주목할 코드 및 문서 변경

*열린 pull request와 주시할 만한 초기 단계 작업들입니다.*

### Damus (iOS)

[NIP-19 relay 힌트](https://github.com/damus-io/damus/pull/3477)는 event 조회 시 relay 힌트 소비를 구현합니다. 사용자가 nevent, nprofile, naddr 링크를 열면 Damus는 bech32 TLV 데이터에서 relay 힌트를 추출하고, 사용자의 relay 풀에 없는 콘텐츠를 가져오기 위해 일시적인 relay에 연결합니다. 구현에는 동시 조회 중 경쟁 상태를 막기 위한 ref-counted 정리 로직이 포함됩니다. [이미지 URL 감지](https://github.com/damus-io/damus/pull/3474)는 작성기에 붙여넣은 이미지 URL을 자동으로 미리보기 썸네일로 바꾸며, 여러 이미지가 있을 때 캐러셀 위치 배지를 표시합니다. [npub 붙여넣기 변환](https://github.com/damus-io/damus/pull/3473)은 붙여넣은 npub/nprofile 문자열을 비동기 프로필 해석과 함께 멘션 링크로 바꿉니다.

### Amethyst (Android)

[결제 대상](https://github.com/vitorpamplona/amethyst/pull/1627)은 [NIP-57](/ko/topics/nip-57/) zap 분배를 위한 event 인터페이스를 추가해, 게시물이 들어오는 zap을 여러 수신자가 나눠 받을 수 있게 합니다. 협업, 수익 분배, 혹은 콘텐츠 제작자와 그들이 사용하는 도구에 함께 팁을 주는 상황에 유용합니다. [Quartz 기능 동등성 문서](https://github.com/vitorpamplona/amethyst/pull/1624)는 Android, Desktop JVM, iOS 타깃별 구현 기능을 추적하는 자세한 표를 추가하며, iOS에는 핵심 암호화(`Secp256k1Instance`), JSON 직렬화, 데이터 구조가 아직 부족하다고 적고 있습니다.

### Notedeck (Desktop)

[타임라인 필터 재구축](https://github.com/damus-io/notedeck/pull/1226)은 언팔로우한 계정이 계속 피드에 나타나는 버그를 고칩니다. 타임라인 필터가 contact list를 기준으로 한 번만 생성되고 이후 갱신되지 않았는데, 이번 수정은 `contact_list_timestamp` 추적과 `invalidate()` 메서드를 추가해 팔로우 상태가 바뀔 때 재구성을 유도합니다.

### Citrine (Android Relay)

[ContentProvider API](https://github.com/greenart7c3/Citrine/pull/86)는 로컬 relay의 event 데이터베이스를 다른 Android 앱에 `ContentResolver`를 통해 노출합니다. WebSocket 인터페이스와 달리, 앱이 지속적인 연결을 유지하거나 Nostr relay 프로토콜을 직접 구현할 필요가 없습니다. ContentProvider는 Android의 네이티브 IPC를 통해 직접적이고 동기적인 데이터베이스 접근을 제공합니다. 외부 앱은 ID, pubkey, kind, 날짜 범위로 event를 조회하고, 검증을 거쳐 새 event를 삽입하거나, 소켓 연결을 관리하지 않고 삭제할 수 있습니다.

### rust-nostr (Library)

[NIP-40 relay 레벨 지원](https://github.com/rust-nostr/nostr/pull/1183)은 relay builder 수준에서 만료 처리 기능을 추가합니다. 만료된 event는 이제 저장 전에 거부되고, 클라이언트로 보내기 전에도 필터링되므로, 각 데이터베이스 구현이 만료 검사를 개별적으로 처리할 필요가 없어집니다.

### nak (CLI)

[Blossom mirror](https://github.com/fiatjaf/nak/pull/91)는 커맨드라인 도구에 blob 미러링 기능을 구현합니다.

### Mostro (P2P Trading)

[개발 수수료 감사 event](https://github.com/MostroP2P/mostro/pull/559)는 개발 펀드 지급에 대한 투명한 감사 추적을 kind 8383 Nostr event를 통해 추가합니다. 이 구현은 성공적인 수수료 지급 뒤에 비차단 방식으로 감사 event를 발행하며, 프라이버시를 위해 구매자와 판매자 pubkey는 제외한 채 주문 세부 정보와 결제 해시를 포함합니다.

### MDK (Marmot Development Kit)

세 가지 보안 감사 수정이 적용됐습니다. [작성자 검증](https://github.com/marmot-protocol/mdk/pull/40)은 rumor pubkey가 MLS 발신자 자격 증명과 일치하도록 강제해 가장 공격을 막습니다. [KeyPackage 신원 바인딩](https://github.com/marmot-protocol/mdk/pull/41)은 자격 증명 신원이 event 서명자와 일치하는지 검증합니다. [관리자 업데이트 검증](https://github.com/marmot-protocol/mdk/pull/42)은 비어 있는 관리자 집합과 비멤버 관리자 할당을 막습니다.

### Shopstr (Marketplace)

[HODL invoice escrow](https://github.com/shopstr-eng/shopstr/pull/217)는 실물 상품을 위한 trust-minimized 결제 시스템을 구현합니다. 아키텍처는 Alby의 `makeHoldInvoice`를 사용해 구매자 자금을 구매자 본인 지갑에 잠가 두고, 판매자의 재고 확인이 끝난 뒤에만 정산이 이뤄지게 합니다. 핸드셰이크 프로토콜은 [NIP-17](/ko/topics/nip-17/) 암호화 DM을 통해 흐릅니다. 구매자가 주문 요청을 보내면, 판매자가 HODL invoice로 응답하고, 구매자는 결제해 자금이 잠긴 뒤, 판매자가 재고와 배송을 확인하면 정산이 이뤄집니다. 다중 판매자 장바구니 지원은 여러 판매자 간 결제를 분할합니다.

### Jumble (Web Client)

[relay별 discovery 모드](https://github.com/CodyTseng/jumble/pull/713)는 특정 relay에서 팔로우 중인 사용자의 게시물을 숨기는 토글을 추가해, 언어 기반 discovery 피드(예: nostr.band/lang/*)를 가능하게 합니다. 이 기능은 작성자 pubkey가 사용자의 팔로우 목록에 포함된 게시물을 걸러내고, relay URL별 토글 상태를 localStorage에 저장합니다.

### White Noise (Encrypted Messaging)

[미디어 업로드 재시도](https://github.com/marmot-protocol/whitenoise/pull/937)는 실패한 업로드를 위한 재시도 옵션을 추가합니다. [프로필 편집 경고](https://github.com/marmot-protocol/whitenoise/pull/927)는 사용자가 프로필 변경을 할 때 경고를 보여줍니다. 백엔드에서는 [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422)가 AccountGroup 생성 과정의 경쟁 상태를 수정합니다.

### npub.cash (Lightning Address Service)

[v3 재작성](https://github.com/cashubtc/npubcash-server/pull/40)은 모노레포와 서버를 Bun으로 이전하고, SQLite 지원을 추가하며, v1 호환성을 제거하고, LUD-21을 구현하며, 실시간 mint quote 업데이트를 도입합니다.

### nostr-java (Library)

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1)은 [두 개의 PR](https://github.com/tcheeric/nostr-java/pull/499)에 걸친 WebSocket 처리 리팩터링과 더 견고한 테스트를 포함해 출시됐습니다.

### NIPs Repository

[NIP-54 Djot 마이그레이션](https://github.com/nostr-protocol/nips/pull/2180)은 위키 사양의 별도 변경안을 제안합니다. 콘텐츠 형식을 Asciidoc에서 더 가벼운 마크업 언어 Djot로 전환하고, 위키 링크를 위한 reference-style 링크를 도입해 소스 형태에서 문서 간 상호 참조를 더 읽기 쉽게 만듭니다. [NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179)은 FROST(Flexible Round-Optimized Schnorr Threshold signatures)를 사용해 Nostr 그룹을 위한 threshold multi-signature 거버넌스를 제안합니다. Quorum은 T-of-N 구조를 통해 구성원들이 직접 대표하거나 대표자 평의회에 위임할 수 있는 공유 nsec입니다. 평의회가 바뀌면 기존 nsec는 폐기되고 새로운 nsec가 배포되며, 이전 평의회의 마지막 행위는 거버넌스 전환 event에 서명하는 것입니다. 이 사양은 멤버십(공개 또는 비공개), 선거와 투표(일반 투표, 불신임 투표), 선택적 자연어 "법", 그리고 quorum이 다른 quorum의 구성원이 될 수 있는 quorum ontology를 정의해, 지역 단위가 상위 지역 단체에 참여하는 계층 구조까지 가능하게 합니다. 활용 사례는 소스 코드 개발, 회사 이사회, HOA, 관리형 커뮤니티까지 폭넓습니다.

---

이번 주와 올해는 여기까지입니다. 뭔가를 만들고 있나요? 공유할 소식이 있나요? 여러분의 프로젝트를 다뤄주길 원하시나요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ko/topics/nip-17/) DM으로 연락</a>하시거나 Nostr에서 찾아주세요.
