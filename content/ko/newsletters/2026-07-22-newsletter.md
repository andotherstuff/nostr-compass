---
title: 'Nostr Compass #32'
date: 2026-07-22
translationOf: /en/newsletters/2026-07-22-newsletter.md
translationDate: 2026-07-30
draft: false
type: newsletters
---

Nostr에 대한 주간 가이드, Nostr Compass에 다시 오신 것을 환영합니다.

**이번 주:** [IndieSats](#indiesats-drops-its-publisher-role-and-relaunches-as-open-nostr-music-infrastructure)는 키 수탁, 화이트리스트, 의무 수익 배분을 폐지하고 아티스트가 자신의 키로 발행하는 개방형 relay, 플레이어, 탐색 레이어로 재출범했습니다. [Nostrord v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays)은 다섯 개의 [NIP-29 명세 PR이 병합된](#protocol-work-and-nip-updates) 주에 그룹 모더레이션, 뮤트 리스트, onion relay를 탑재했습니다. [Zapstore 1.1.0](#zapstore-110-makes-the-device-key-portable-and-adds-background-auto-updates)은 Amber로 백업할 수 있는 휴대 가능한 암호화 디바이스 키와 선택형 백그라운드 자동 업데이트를 도입했습니다. [즐겨찾기 팔로우 세트 리스트 kind](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house)는 병합된 지 며칠 만에 리넘버링 PR이 열렸습니다. [Iris 프로젝트들](#the-iris-projects-ship-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week)은 한 주에 nostr-pubsub, fips-ts 브라우저 런타임, nostr-social-graph 2.0.0을 출시했습니다.

태그 릴리스로는 bunker 서명 승인을 일괄 처리하는 [Amber v6.3.0](#amber-v630-groups-bunker-signing-approvals-and-adds-expert-list-support), Buzz 워크스페이스를 지원하는 두 번째 클라이언트 [Armada v0.37.0](#armada-v0370-opens-buzz-workspaces-from-a-second-client), 안정적인 NIP-17 전송과 엄격한 TLS 검증을 적용한 [Divine Mobile 1.0.17](#divine-mobile-1017-hardens-relay-security-and-dm-delivery), NIP-34 pull request 명령을 추가한 [nak v0.20.2](#nak-v0202-adds-nip-34-pull-request-workflows)가 있습니다.

아직 릴리스되지 않은 변경으로는 [Snort](#snort-rewrites-query-synchronization-around-eose-proven-coverage)가 EOSE로 입증된 캐시 범위를 기록하도록 바뀌었고, [Shopstr](#shopstr-binds-payment-validation-to-signed-receipts-and-server-side-prices)는 결제 무결성의 두 가지 허점을 막았습니다. [Mostr](#mostr-bridges-activitypub-private-chats-and-nostr-dms)는 ActivityPub 비공개 채팅과 Nostr DM을 연결했고, [nostream](#nostream-merges-eight-prs-without-cutting-a-release)은 이번 주 Deep Dive에서 다루는 접근 제어 스택을 병합했습니다. [Amethyst](#amethyst-lands-v1130-pre-release-qa-on-napplet-isolation-and-concord-authority)는 88개의 PR을 병합했고 Desktop에서 완전한 NIP-88 투표 기능을 구현했습니다.

NIPs 저장소는 이번 주 [NIP-29 클러스터](#protocol-work-and-nip-updates)와 [kind:10011 즐겨찾기 팔로우 세트](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house)를 포함한 다섯 개의 PR을 병합했고, [NIP-47 단순화](#protocol-work-and-nip-updates)와 [신뢰된 relay 단언](#protocol-work-and-nip-updates)에 대한 논의를 열었습니다. Deep Dive는 [relay 접근 제어 쌍인 NIP-42와 NIP-43](#nip-deep-dive-nip-42-and-nip-43)을 다룹니다.

---

## 주요 소식

### IndieSats가 퍼블리셔 역할을 내려놓고 개방형 Nostr 음악 인프라로 재출범하다

[IndieSats](https://zapstore.dev)는 이번 주까지 퍼블리셔 역할을 맡았던 Nostr 기반 음악 플랫폼입니다. 아티스트의 키를 보관하고 화이트리스트를 운영했으며, 수익의 2%를 의무적으로 가져갔습니다. 이 프로젝트는 [7월 20일에 게시한 전환 발표](https://njump.me/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u)에서 세 역할을 모두 폐지했습니다. 재출범한 플랫폼은 개방형 relay, 플레이어, 탐색 레이어라는 세 가지 개방형 인프라로 구성됩니다. 이제 아티스트는 자신의 Nostr 프로필로 음악을 발행합니다. 트랙 단위 2% 플랫폼 몫은 선택 사항이지만 발행 시 기본으로 선택되며, 아티스트가 이를 해제하면 결제액 전부를 받을 수 있습니다. 플랫폼은 아티스트가 자신의 작업물을 삭제할 수 있도록 [NIP-09](/ko/topics/nip-09/) kind:5 삭제 요청도 처리합니다. [7월 21일에 공개된 v1.1.5 업데이트](https://zapstore.dev/apps/com.indiesats.app)는 트랙 발행 형식을 Amethyst와 다른 Nostr 음악 클라이언트가 기대하는 이벤트 형식으로 바꾸고 relay 전송을 명시적으로 만들었습니다. 프로토콜이 플랫폼을 대체한다고 논의해 온 분야에서, 플랫폼이 자발적으로 자신을 프로토콜 구성 요소로 분해한 실제 사례입니다.

### Nostrord v2.3.0이 그룹 모더레이션, 뮤트 리스트, onion relay를 탑재하다

Android, iOS, 웹, 데스크톱용 그룹 채팅 클라이언트 [Nostrord](https://github.com/nostrord/nostrord)는 [v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0)을 출시하며 모든 UI에 연결된 그룹 모더레이션 액션([PR #192](https://github.com/nostrord/nostrord/pull/192)), 크로스-relay 탐지를 갖춘 동의 기반 그룹 초대([PR #195](https://github.com/nostrord/nostrord/pull/195)), 크로스 플랫폼 [NIP-51](/ko/topics/nip-51/) 뮤트 리스트([PR #188](https://github.com/nostrord/nostrord/pull/188)), 그리고 Tor .onion relay 지원을 탑재했습니다. 이 릴리스는 하위 그룹, 메시지 고정, 배너, 초대 코드를 다루는 다섯 개의 PR이 병합된 기반 [NIP-29](/ko/topics/nip-29/) 명세와 같은 주에 나왔는데(자세한 내용은 이번 주 [프로토콜 섹션](#protocol-work-and-nip-updates)에서), 이로써 Nostr의 그룹 채팅은 이제 더 깊어진 명세와 그 대부분을 실제로 구동하는 클라이언트를 모두 갖게 되었습니다. 이는 relay 그룹 위에 구축하는 다른 모든 이들의 피드백 루프를 단축합니다.

### Zapstore 1.1.0이 디바이스 키를 휴대 가능하게 만들고 백그라운드 자동 업데이트를 추가하다

[Zapstore](https://github.com/zapstore/zapstore)는 릴리스에 개발자 키로 서명하며 중앙 운영자가 보증하지 않는 Nostr 네이티브 앱 스토어입니다. 3월 초 이후 이 뉴스레터에서 처음 다루는 [버전 1.1.0](https://github.com/zapstore/zapstore/releases/tag/1.1.0)은 기존 앱 스토어와의 가장 큰 두 가지 격차를 메웁니다. 업데이트 측면에서는 선택형 백그라운드 다운로드가 Wi-Fi에서 실행되고 자동 또는 단계적 방식으로 설치되어, 사용자가 스토어를 수동으로 열지 않아도 앱을 최신 상태로 유지합니다. 신원 연속성은 휴대 가능한 암호화 디바이스 키로 확보합니다. 사용자는 [Amber](https://github.com/greenart7c3/Amber)에 키를 백업할 수 있습니다. 이 과정은 Android 서명자 인터페이스인 [NIP-55](/ko/topics/nip-55/)를 사용하므로 휴대전화를 바꿔도 디바이스 신원을 유지합니다. 버전 1.1.0은 앱 카탈로그를 디바이스가 서명한 kind:10067 이벤트로 relay에 옮기고, 오버플로 메뉴에 [NIP-56](/ko/topics/nip-56/) 검증 신고를 추가해 다른 클라이언트도 활용할 수 있는 방식으로 문제 앱을 신고하게 합니다. 설치를 시작하기 전에 릴리스에 첨부된 C1 증명도 검증하여 개발자가 서명한 항목과 디바이스가 실행하는 항목의 연결을 강화합니다.

### 즐겨찾기 팔로우 세트 리스트 kind가 병합되고 즉시 이사하다

한 주 안에서 명세 조정 스토리가 펼쳐졌습니다. [PR #2413](https://github.com/nostr-protocol/nips/pull/2413)이 7월 15일에 병합되어 [NIP-51](/ko/topics/nip-51/)(리스트) 아래에 즐겨찾기 팔로우 세트를 위한 교체 가능한 리스트 kind를 표준화했습니다. 클라이언트가 일반 리스트 kind를 과부하시키는 대신 사용자가 큐레이션한 팔로우 계정 세트를 발행할 수 있는 전용 kind입니다. 며칠 안에 할당된 kind:10011이 이미 다른 곳에서 사용 중인 것으로 밝혀져, 후속 [PR #2417](https://github.com/nostr-protocol/nips/pull/2417)이 리스트를 kind:10021로 리넘버링하기 위해 현재 열린 상태입니다. 아직 병합된 kind에 대해 출시된 것이 없어, 이는 리넘버링하기에 가장 저렴한 시점입니다. 클라이언트가 kind:10011 이벤트를 발행하기 시작하면 충돌을 되돌리는 비용이 커집니다. 리스트 소비 기능을 구축하는 개발자는 해결될 때까지 병합된 텍스트가 아니라 리넘버링 PR을 추적해야 합니다.

### Iris 프로젝트들이 한 주에 pubsub 라이브러리, 브라우저 FIPS 런타임, 소셜 그래프 2.0을 출시하다

Iris 주변의 세 릴리스가 함께 나왔으며 서로 맞물립니다. [nostr-pubsub](https://github.com/mmalmi/nostr-pubsub)는 Nostr 이벤트를 위한 전송 중립적 publish/subscribe 라이브러리입니다. [처음 추적된 v0.1.3부터 v0.5.2까지의 릴리스](https://github.com/mmalmi/nostr-pubsub/releases)는 nostr-tools의 SimplePool을 기반으로 한 브라우저 relay carrier, 잘못된 서명이 구독자에게 도달하지 않도록 전송 경계에서 수행하는 이벤트 검증, 범위가 제한된 과거 query를 제공합니다. [fips-ts](https://github.com/mmalmi/fips-ts)는 기존에 Rust stack으로 제공되던 Noise-over-secp256k1 peer 전송 [FIPS](/ko/topics/fips/)를 TypeScript 런타임으로 브라우저에 가져옵니다. [0.0.24부터 0.0.30까지의 릴리스](https://github.com/mmalmi/fips-ts/releases)는 WebRTC datachannel carrier, peer 탐색을 위한 Nostr 기반 signaling, 최근 peer 캐시, 브라우저 저장소용 IndexedDB adapter를 추가했으며 참조 Rust 구현과 wire-compatible합니다. 세 번째 구성 요소인 [nostr-social-graph v2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0)은 소셜 그래프 라이브러리의 주요 버전입니다. Nostr 신원 그래프를 위한 서명된 roster 연산, 표준 3개 필드 URI에서 bootstrap하는 디바이스 승인 흐름, 공유 Rust 및 TypeScript test vector를 갖춘 FIPS 전송 신원 facet을 제공합니다. 이들을 묶는 [Iris Stack](https://stack.iris.to/)은 해당 라이브러리와 Blossom, Hashtree, 암호화 messaging을 통합하는 프로젝트 실험 공간입니다. 이를 조합하면 웹 앱은 Nostr로 peer를 탐색하고, 암호화된 FIPS channel을 열고, 서명된 소셜 그래프를 유지할 수 있으며 전 과정을 TypeScript로 구현할 수 있습니다.

---

## 태그 릴리스

### Amber v6.3.0이 bunker 서명 승인을 묶고 Expert List 지원을 추가하다

[Amber](https://github.com/greenart7c3/Amber)는 Android [NIP-46](/ko/topics/nip-46/) 원격 서명자입니다. [v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0)은 bunker 서명을 위한 그룹화된 다중 요청 승인을 추가하여, 대기 중인 서명 요청 묶음을 한 번에 하나의 프롬프트가 아니라 함께 검토하고 승인할 수 있습니다. 이 릴리스는 또한 Expert List(kind 12022)와 Expert Pack(kind 32022) 이벤트 지원, 화면의 민감한 콘텐츠를 숨기는 프라이버시 모드, 그리고 프로필 메타데이터보다 먼저 계정의 [NIP-65](/ko/topics/nip-65/) relay 리스트를 가져와 서명자 흐름이 사용자의 실제 relay 세트에서 시작되도록 하는 변경을 추가합니다. 이는 2026-07-08 호에서 다룬 v6.2.x 라인을 이어갑니다.

### Nostrord v2.2.0 후속

[v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays)이 이번 주 주요 소식 섹션을 이끄는 가운데, 태그 릴리스 항목에서는 주요 소식이 다루지 않은 내용만 언급합니다. v2.3.0은 #31에서 다룬 v2.2.0의 DM 제어 기능을 이어가며, 이 클라이언트가 2주 연속으로 낸 주간 릴리스입니다.

### Armada v0.37.0이 두 번째 클라이언트에서 Buzz 워크스페이스를 열다

[Armada](https://gitlab.com/soapbox-pub/armada)는 Discord 스타일 Nostr 클라이언트입니다. [v0.37.0](https://gitlab.com/soapbox-pub/armada/-/commit/7a0d0ade51fb8a7bafa4513d2881d275bb2c7dde)은 Buzz relay를 향상된 [NIP-29](/ko/topics/nip-29/) 워크스페이스 모드로 지원하며, relay의 [NIP-11](/ko/topics/nip-11/) 메타데이터를 통해 이를 감지합니다. 클라이언트는 Buzz 포럼 게시물과 댓글을 kind 45001과 45003으로 렌더링하고, 편집과 삭제를 스트림 타임라인에 반영하며, 접속 상태, 워크플로, 작업, 허들, 공유 캔버스 화면을 추가합니다. Projects 워크스페이스는 [NIP-34](/ko/topics/nip-34/) 저장소 공지, 패치, pull request, 이슈, 상태 이벤트를 relay에서 직접 읽습니다([구현 commit](https://gitlab.com/soapbox-pub/armada/-/commit/7d5603a3e21d564301d667113d28de4407d6f642)). 이로써 Buzz 워크스페이스는 대화와 저장소 작업을 모두 지원하는 두 번째 클라이언트를 갖게 되었습니다.

### Wisp v1.2.0이 다중 계정 전환기와 접을 수 있는 답글 스레드를 추가하다

[Wisp](https://github.com/barrydeen/wisp)는 내장 지갑 지원을 갖춘 프라이버시 지향 Nostr 클라이언트입니다. [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0)은 재로그인 없이 프로필 간을 이동하는 다중 계정 전환기, 긴 대화를 위한 접을 수 있는 답글 스레드, 노트 링크가 열리기 전에 추적 매개변수를 제거하는 기능, 그리고 지갑 거래 내역 보기를 추가합니다. 이 릴리스는 2026-07-08 호에서 다룬 Wisp 업데이트를 이어갑니다.

### Divine Mobile 1.0.17이 relay 보안과 DM 전송을 강화하다

Nostr 짧은 동영상 클라이언트 [Divine Mobile](https://github.com/divinevideo/divine-mobile)은 영구적으로 유지되는 스톱모션 편집기와 강화된 Nostr 경로를 담은 [1.0.17](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.17)을 출시했습니다. 이제 DM은 relay의 `OK` 응답을 기다리고, 영속 큐를 통해 재시도하며, 수신자의 kind 10050 inbox relay 리스트를 따라 전송됩니다([PR #6046](https://github.com/divinevideo/divine-mobile/pull/6046)). NIP-46 페어링은 `auth_url` challenge를 복구 가능한 서명 단계로 보존합니다([PR #6151](https://github.com/divinevideo/divine-mobile/pull/6151)). [PR #6278](https://github.com/divinevideo/divine-mobile/pull/6278)은 프로덕션 relay WebSocket과 NIP-96 업로드, LNURL, zap에 쓰이는 HTTP 요청에서 허용적인 인증서 수락을 제거해, 디버그 루프백 연결을 제외한 환경에서 플랫폼 TLS 검증을 복원합니다. 중단된 업로드는 서버가 마지막으로 확인한 offset부터 재개할 수 있어, 앱이 백그라운드로 전환되어도 발행이 처음부터 다시 시작되지 않습니다.

### ClipRelay v0.1.2(신규 프로젝트)가 Nostr relay를 통해 디바이스 간 클립보드를 동기화하다

[ClipRelay](https://github.com/tajava2006/cliprelay)는 새로 출시된 크로스 플랫폼 앱(Android, macOS, Windows, Linux)으로, 자신의 디바이스 간에 클립보드를 동기화합니다. 한 머신에서 복사하고 다른 머신에서 붙여넣습니다. 모든 트래픽은 자신에게 주소가 지정된 [NIP-44](/ko/topics/nip-44/) 암호화 이벤트로 Nostr relay를 통해 이동하므로, 실행할 서버도 만들 계정도 없으며, 개인키는 앱 밖에 유지됩니다. [v0.1.2](https://github.com/tajava2006/cliprelay/releases)는 절전 모드에서 깨어난 머신이 계속 발행하면서 조용히 수신을 멈추던 미묘한 동기화 실패를 수정하고, 이전에 죽은 구독을 정상으로 보고하던 relay 상태 표시기를 강화합니다. 이는 ClipRelay가 뉴스레터에 처음 등장하는 것입니다.

### Sonar v0.1-alpha.11이 알파 라인을 이어가다

지난주의 주요 소식이었던 [Sonar](https://github.com/hedwig-corp/bitchat-to-sonar)는 Rust mesh link engine 작업, BLE와 mesh 수정, relay 진단을 담은 [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11)을 출시했습니다. #31에서 다룬 알파 릴리스의 점진적 후속 버전입니다.

### nak v0.20.2가 NIP-34 pull request 워크플로를 추가하다

Nostr 명령줄 도구 [nak](https://github.com/fiatjaf/nak)는 [v0.20.2](https://github.com/fiatjaf/nak/releases/tag/v0.20.2)를 출시했습니다. [NIP-34](/ko/topics/nip-34/) pull request를 생성하고 가져오고 병합하는 명령과 개별 패치를 가져오는 명령을 추가했으며, 저장소 공지를 다시 작성하지 않고도 push할 수 있게 되었습니다. [11개 commit으로 구성된 릴리스 범위](https://github.com/fiatjaf/nak/compare/v0.20.1...v0.20.2)는 [NIP-29](/ko/topics/nip-29/) 부모 그룹 처리도 추가하고, 더 많은 outbox relay를 조회하며, relay 연결 타임아웃을 설정 가능하게 만들고, 기본 `--sec` 값만 있을 때의 bunker 선택 문제를 수정합니다.

### 이번 주의 작은 출시

네 가지 소규모 릴리스를 한 줄씩 소개합니다. Nostr 통화 앱 [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release)은 푸시 알림을 UnifiedPush로 이전해 통화 시그널링을 Google 푸시 인프라에서 분리했습니다. Nostr를 시그널링에 사용하는 mesh VPN [nostr-vpn v4.1.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.3)은 플랫폼 전반에서 exit DNS 정책을 통합하고, WireGuard 또는 private exit 세션이 끝난 뒤 원래 route와 DNS 상태를 복원합니다. 4월에 다룬 Nostr와 Lightning 기반 음악 및 팟캐스트 aggregator [StableKraft v1.3.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.3.0)은 Android 잠금 화면과 헤드셋 제어를 네이티브로 지원하고 재생 범위 wake lock을 추가해 Doze 중에도 오디오가 계속 재생됩니다. Zapstore의 새 앱 Hakari는 암호화된 Nostr 이벤트로 체중 기록을 백업합니다.

### Amethyst가 napplet 격리와 Concord 권한에 대한 v1.13.0 프리릴리스 QA를 진행하다

[Amethyst](https://github.com/vitorpamplona/amethyst)는 v1.13.0 릴리스를 앞두고 이번 주 88개의 PR을 병합했습니다. [PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650)은 napplet 계정 격리, Concord 권한 수정과 약 30개의 기타 수정을 다루는 프리릴리스 QA 작업입니다. 마감 직전 변경에는 Desktop에서 [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) 투표 렌더링, 생성, 투표, 명시된 relay 기준 집계, kind 1068 검색을 완전히 지원하는 작업이 포함됩니다([PR #3664](https://github.com/vitorpamplona/amethyst/pull/3664)). NIP-50 검색은 결과를 BM25 관련성으로 정렬하고, 대규모 tag watcher는 범위를 제한한 병합 방식을 사용합니다([PR #3663](https://github.com/vitorpamplona/amethyst/pull/3663)). 별도의 relay 저장소 개선은 측정한 비용에 따라 query index를 선택하고, tag-author-kind index를 추가하며, fanout마다 각 실시간 이벤트를 한 번만 직렬화합니다([PR #3660](https://github.com/vitorpamplona/amethyst/pull/3660)). 보고된 benchmark에서 한 query 형태는 149ms에서 4ms로, 일반적인 DM room query는 14.2ms에서 0.66ms로 줄었습니다.

---

## 릴리스되지 않은 변경 사항

### Snort가 EOSE로 입증된 범위를 중심으로 query 동기화를 재작성하다

[Snort](https://github.com/v0l/snort)는 웹 Nostr 클라이언트로, [commit 8a62770](https://github.com/v0l/snort/commit/8a627700d8a5af9527cb68655d844dd14a3ac79d)에서 query와 캐시 동기화 경로를 재작성했습니다. 이제 클라이언트는 EOSE에 도달한 query 구간을 기록하고, 이 watermark를 사용해 이미 포함된 캐시 범위를 건너뛰며, 하나의 relay pool listener 뒤에서 이벤트 dispatch를 중앙화합니다. 검색 filter는 NIP-11 문서에서 [NIP-50](/ko/topics/nip-50/) 지원을 알린 relay에만 보냅니다. 후속 수정은 동시에 발생하는 watermark 업데이트를 직렬화하고 timeline 경계의 포함 조건을 바로잡았습니다. [commit 9d1721b](https://github.com/v0l/snort/commit/9d1721b8b5696a6f96f462170c469c232cabe672)은 분할된 follows feed의 실시간 구독을 복원해, 페이지를 불러온 뒤 도착한 이벤트가 캐시 구간 밖에서 멈추지 않게 합니다.

### Shopstr가 서명된 receipt와 서버 측 가격에 결제 검증을 연결하다

[Shopstr](https://github.com/shopstr-eng/shopstr)는 Nostr marketplace 클라이언트로, 결제 무결성의 두 가지 허점을 막았습니다. [PR #552](https://github.com/shopstr-eng/shopstr/pull/552)는 Zapsnag가 kind 9735 receipt를 구매로 처리하기 전에 서명, 서명자, 내장된 zap 요청, 수신자와 상품 tag, BOLT11 금액, 선택적 preimage를 invoice payment hash와 대조해 검증하도록 합니다. [PR #449](https://github.com/shopstr-eng/shopstr/pull/449)는 Cashu quote 생성을 Shopstr API route 뒤로 옮겨 listing을 조회하고 서버에서 가격을 다시 계산합니다. 따라서 브라우저에서 변조한 금액으로 mint invoice를 결정할 수 없습니다.

### Mostr가 ActivityPub 비공개 채팅과 Nostr DM을 연결하다

ActivityPub과 Nostr를 연결하는 bridge인 [Mostr](https://gitlab.com/soapbox-pub/mostr)는 이제 일대일 Pleroma ChatMessage 객체와 암호화된 Nostr DM을 양방향으로 전달합니다([commit 36ee547](https://gitlab.com/soapbox-pub/mostr/-/commit/36ee547035f9287029f71656c472fe029a7ab31b)). ActivityPub 비공개 채팅은 Nostr 수신자에게 주소를 지정한 kind 4 이벤트로 바뀌며, bridge된 Fediverse 사용자에게 보낸 kind 4 메시지는 복호화되어 ChatMessage 객체로 federation됩니다. bridge는 이 이벤트를 [NIP-42](/ko/topics/nip-42/)로 제한한 설정된 DM relay에만 전송하고 별도의 relay key로 인증합니다. 이 상호운용 경로는 기존 [NIP-04](/ko/topics/nip-04/) 암호화를 사용합니다. NIP-17 gift wrapping은 이번 구현에 포함되지 않습니다.

### nostream이 릴리스 없이 여덟 개의 PR을 병합하다

TypeScript relay 구현인 [nostream](https://github.com/Cameri/nostream)은 이번 주 릴리스 없이 여덟 개의 PR을 병합했습니다. 핵심 두 건은 [PR #702](https://github.com/Cameri/nostream/pull/702)와 [PR #676](https://github.com/Cameri/nostream/pull/676)으로, 함께 relay 운영자에게 작동하는 인증 및 멤버십 접근 제어 스택을 제공합니다. 이번 주 NIP Deep Dive는 이 핸드셰이크를 자세히 설명합니다. [PR #694](https://github.com/Cameri/nostream/pull/694)는 일반 `#e`, `#p`, `#g` 및 유사한 tag filter가 일치하는 tag row마다 같은 이벤트를 한 번씩 반환할 수 있던 문제를 수정해, 구독 내 중복 프로토콜 트래픽을 줄입니다.

### FIPS v0.4.1이 Iris 전송 레이어를 강화하다

[jmcorgan/fips](https://github.com/jmcorgan/fips)는 antipoison 상태에 상한을 두고 수렴과 MTU 처리를 수정하며 CPU 사용량을 줄인 유지보수 릴리스 [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1)을 출시했습니다. Iris 프로젝트 묶음의 브라우저 TypeScript 런타임 [fips-ts](https://github.com/mmalmi/fips-ts)는 이 Rust 전송과 wire-compatible하므로, 여기의 수정 사항은 브라우저 상호운용성에 직접 반영됩니다.

---

## 프로토콜 작업 및 NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-29](/ko/topics/nip-29/)(Relay 기반 그룹): 하위 그룹** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319), 2026-07-16 병합): NIP-29는 멤버십, 역할, 채팅 기록이 주소 지정 가능한 `kind:39000` 시리즈 이벤트로 단일 relay에 존재하고, 모더레이션 작업이 `kind:9000` 시리즈 관리자 이벤트로 전달되는 relay 호스팅 그룹을 정의합니다. 이 PR은 같은 relay에 있는 다른 그룹의 `d` 식별자를 가리키는 `parent` tag를 메타데이터에 추가해 그룹이 자신을 하위 그룹으로 선언할 수 있게 합니다. 그 밖의 모든 면에서 하위 그룹은 일반 그룹입니다. 부모 그룹에 가입해도 하위 그룹의 멤버십은 부여되지 않고, 각 하위 그룹의 `kind:39001` 관리자 리스트가 자체 범위에서 권한을 가지므로 관리자 역할도 상속되지 않습니다. 각 하위 그룹은 독립된 `kind:9000`/`kind:9001` 멤버 이벤트를 유지합니다. 이 계층 구조를 지원하는 relay는 NIP-11 relay 정보 문서의 `nip29` 객체에서 `"subgroups": true`로 알리므로, 클라이언트는 중첩 커뮤니티를 만들기 전에 지원 여부를 확인할 수 있습니다.

- **[NIP-29](/ko/topics/nip-29/): 메시지 고정** ([PR #2379](https://github.com/nostr-protocol/nips/pull/2379), 2026-07-15 병합; [PR #2416](https://github.com/nostr-protocol/nips/pull/2416), 2026-07-17 병합): 그룹 관리자는 이제 relay 기반 그룹 안에서 메시지를 고정할 수 있습니다. 이 메커니즘은 일반 이벤트 id를 참조하는 `e` tag로 전체 순서가 있는 고정 리스트를 전달하는 새로운 모더레이션 이벤트 `kind:9010` `update-pin-list`와, relay가 가장 최근에 수용된 고정 리스트를 미러링하도록 재생성하는 새로운 선택적 그룹 수준 이벤트 `kind:39005` *group pinned events*를 추가합니다. 각 `kind:9010`이 단일 항목을 토글하는 대신 전체 리스트를 교체하기 때문에, 고정, 고정 해제, 재정렬, 고정 지우기는 모두 하나의 새 리스트를 제출하는 것으로 표현됩니다. 후속 PR #2416은 형식을 확장하여 `a` tag도 고정 리스트에서 수용되어, 관리자가 일반 채팅 메시지와 함께 주소 지정 가능한 이벤트(장문 게시물, 위키 페이지, 기타 매개변수화된 교체 가능 콘텐츠)를 고정할 수 있게 합니다. relay는 고정 수에 상한을 둘 수 있으며, 병합된 명세 텍스트는 tag가 나타나는 순서대로 고정을 표시하도록 권장합니다.

- **[NIP-29](/ko/topics/nip-29/): 배너 tag와 초대 코드 접미사** ([PR #2383](https://github.com/nostr-protocol/nips/pull/2383), 2026-07-16 병합; [PR #2380](https://github.com/nostr-protocol/nips/pull/2380), 2026-07-16 병합): 그룹 메타데이터에 대한 두 가지 표시 및 온보드 추가 사항입니다. PR #2383은 `kind:39000` 그룹 메타데이터 이벤트에 선택적 `banner` tag를 추가하여, 기존 `name`, `picture`, `about` 필드와 함께 클라이언트가 그룹 페이지의 헤더 이미지를 렌더링할 수 있게 합니다. PR #2380은 그룹 공유 링크를 위한 초대 코드 접미사를 정의합니다. 초대 코드는 그룹의 `naddr` 식별자에 `naddr1...?invite=<code>`로 추가될 수 있습니다. bech32 문자 집합은 `?`를 포함하지 않기 때문에, 접미사 앞부분은 그 자체로 유효한 naddr로 남아, 확장을 이해하지 못하는 클라이언트도 그룹을 해석할 수 있습니다. 이를 이해하는 클라이언트는 `kind:9021` 가입 요청의 `code` tag를 미리 채우며, 이는 기존 `kind:9009` `create-invite` 모더레이션 이벤트와 짝을 이루어 닫힌 그룹의 입장을 단순화합니다.

- **[NIP-51](/ko/topics/nip-51/)(리스트): 즐겨찾기 팔로우 세트, kind:10011** ([PR #2413](https://github.com/nostr-protocol/nips/pull/2413), 2026-07-15 병합): NIP-51은 표준 리스트 kind를 정의하며, 교체 가능한 `kind:10000` 시리즈 리스트(사용자당 하나)와 주소 지정 가능한 `kind:30000` 시리즈 세트(사용자당 여러 개, `d` tag로 키가 지정됨)로 나뉩니다. 이 PR은 `kind:10011`, *즐겨찾기 팔로우 세트*를 추가하는데, 이는 `a` tag가 `kind:30000` 팔로우 세트를 가리키는 표준 교체 가능 리스트입니다. `kind:30002` relay 세트를 참조하는 `a` tag를 보유한 `kind:10012`(relay 피드)의 거울로서, 새 kind는 사용자가 자신이나 다른 사람이 발행한 pubkey 컬렉션의 큐레이션된 리스트와 같은 이름 붙은 팔로우 세트를 북마크하고, 클라이언트가 원탭 팔로잉 또는 피드 전환을 위해 이를 표면화할 수 있게 합니다. 이 kind 번호는 이미 이의가 제기되어 있다는 점에 유의하세요. 아래의 열린 리넘버링 PR을 참조하세요.

- **[NIP-46](/ko/topics/nip-46/)(Nostr Connect): 무응답 타임아웃 지침** ([PR #2375](https://github.com/nostr-protocol/nips/pull/2375), 2026-07-15 병합): NIP-46은 클라이언트가 relay를 통해 서명자(bunker)에게 암호화된 JSON-RPC 형식 요청을 보내고 암호화된 응답을 기다리는 원격 서명 프로토콜입니다. 병합된 변경은 한 문장의 wire 동작을 규정합니다. 알 수 없거나 지원하지 않는 메서드로 보낸 요청에는 반드시 오류로 응답해야 합니다. 이전에는 구현하지 않은 메서드를 받은 서명자가 응답하지 않을 수 있었고, 클라이언트는 자체 타임아웃이 발생할 때까지 "지원하지 않는 메서드"와 "서명자 오프라인"을 구분하지 못한 채 기다려야 했습니다. 의무화된 오류 응답을 통해 클라이언트는 빠르게 실패하고 로컬 타임아웃 전에 의미 있는 오류를 표시할 수 있습니다.

**열린 PR 및 토론:**

- **kind:10011을 kind:10021로 리넘버링** ([PR #2417](https://github.com/nostr-protocol/nips/pull/2417)): 새로 병합된 즐겨찾기 팔로우 세트 리스트를 `kind:10011`에서 `kind:10021`로 옮기는데, `10011`이 이미 다른 곳에서 사용 중이기 때문입니다. 리넘버링 PR은 원래 병합 후 며칠 안에 열혔으므로, 즐겨찾기 팔로우 세트를 구현하는 클라이언트는 이 PR을 추적하고 `10011`이 아닌 최종 번호를 목표로 해야 합니다.

- **[NIP-47](/ko/topics/nip-47/)(Nostr Wallet Connect): 코어 단순화** ([PR #2419](https://github.com/nostr-protocol/nips/pull/2419)): 앱이 Nostr를 통해 원격 지갑에서 Lightning 결제를 요청할 수 있게 하는 지갑 연결 프로토콜인 NIP-47을 더 작은 코어 명세로 좁히는 것을 제안합니다. 선택적이고 더 전문화된 기능은 `47.md`에서 전용 확장 저장소인 [nostr-wallet-connect/nwc](https://github.com/nostr-wallet-connect/nwc)로 옮겨, 확장 명세가 코어와 독립적으로 진화할 수 있게 합니다. 명시된 목표는 코어를 작고 안정적이며 구현하기 쉽게 유지하는 것으로, 최소한의 지갑 연결 레이어를 더 풍부한 선택적 동작에서 분리하는 이전 NWC 통화에서 합의된 방향을 따릅니다. NIP-47이 지갑과 앱 전반에 걸쳐 얼마나 널리 배포되어 있는지를 고려할 때, NWC를 구사하는 모든 이는 재구조화 논의를 추적해야 합니다.

- **신뢰된 Relay 단언(초안, 번호 미할당)** ([PR #2418](https://github.com/nostr-protocol/nips/pull/2418)): Nostr relay에 대한 신뢰 평가를 발행하는 표준을 제안하며, [NIP-11](/ko/topics/nip-11/)(relay가 자신에 대해 주장하는 것)과 [NIP-66](/ko/topics/nip-66/)(모니터가 측정한 것) 옆에 "우리가 내린 결론" 레이어로 자리합니다. 단언 제공자는 관찰된 지표, 운영자 평판, 사용자 신고에서 신뢰 점수를 계산하고, 클라이언트는 연결할 relay를 선택할 때 이러한 단언을 조회합니다. 초안은 `kind:30385`(점수, 신뢰성, 품질, 접근성, 운영자, 정책, 관할권 tag를 담는 주소 지정 가능한 신뢰된 Relay 단언)와 `kind:10385`(사용자가 선택한 단언 제공자를 담는 교체 가능한 신뢰된 제공자 리스트)를 도입하고, relay 및 운영자 신고에 [NIP-32](/ko/topics/nip-32/) label을 재사용합니다. 아직 NIP 번호는 할당되지 않았으며 초기 단계 초안입니다.

- **필터용 AND 연산자("NIP-91", 제안됨, 번호가 아직 저장소에 없음)** ([PR #2252](https://github.com/nostr-protocol/nips/pull/2252)): NIP-01에서 tag filter는 OR만 지원합니다. `"#t": ["meme", "cat"]` filter는 둘 중 하나의 tag가 있는 이벤트와 일치합니다. 이 제안은 index 가능한 tag에 `&` 수정자를 추가하여 `"&t": ["meme", "cat"]`가 두 tag를 모두 가진 이벤트만 반환하게 합니다. relay가 서버에서 교집합을 계산해 더 좁은 결과를 반환합니다. 호환성 규칙은 AND가 OR보다 우선하고, 지원 relay는 AND 값을 OR에서 무시하며, 클라이언트는 확장을 지원하지 않는 relay를 위해 표준 `#` OR tag도 포함하도록 합니다. 클라이언트는 그렇게 받은 더 넓은 결과를 로컬에서 교차 처리합니다. 이 PR은 이전 제안을 다시 열었으며 nostr-rs-relay Docker image, netstr, Snort worker relay를 구현 사례로 나열합니다. NIP-91은 PR branch에만 있고 저장소 README의 NIP index에는 없으므로 아직 잠정 번호입니다.

- **Nostr 웹 애플릿("NIP-5D", 제안됨, 번호가 아직 저장소에 없음)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): iframe이나 webview에서 실행되는 sandbox 웹 애플리케이션("napplet")이 호스팅 애플리케이션("shell")과 통신하는 `postMessage` 프로토콜을 정의합니다. 명세는 의도적으로 얇은 core입니다. message envelope, sandbox 규칙(napplet iframe은 `sandbox="allow-scripts"`를 사용하되 `allow-same-origin`은 포함하지 않아야 하며, shell은 iframe 안에 `window.nostr` NIP-07을 노출해서는 안 됨), 위조할 수 없는 `MessageEvent.source` window 참조를 통한 발신자 식별(`event.origin`을 사용하지 않음), manifest 기반 capability negotiation을 규정합니다. 서명, relay 접근, 저장소, napplet 간 통신에 쓰는 실제 프로토콜 메시지는 각 capability domain을 담당하는 NAP(Nostr Applet Protocol) 확장 명세에 위임됩니다. 서명과 암호화는 항상 shell이 중재하므로 key가 sandbox에 들어가지 않습니다. 이 제안은 NIP-5A napplet manifest 명세에 의존합니다. Amethyst의 v1.13.0 프리릴리스 작업에는 napplet 계정 격리가 포함되어 client-side napplet hosting이 활발한 구현 영역이 되었습니다. 위의 "NIP-91"과 마찬가지로 5D 번호는 잠정적입니다.

---

## NIP Deep Dive: NIP-42와 NIP-43

모두에게 열리지 않은 relay를 운영하려면 과거에는 모든 기능을 직접 만들어야 했습니다. 유료 또는 초대 전용 relay 운영자는 보통 DM으로 수집한 pubkey를 텍스트 파일에 적어 별도 경로에서 화이트리스트를 관리했습니다. 연결된 클라이언트에게 "신원을 증명하라"고 요청할 표준 방식도, 사용자가 가입을 요청하거나 멤버 여부를 확인할 표준 방식도 없었습니다. 읽기나 쓰기를 제한하려는 relay마다 자체 비공개 메커니즘을 구축했고 클라이언트는 이들과 상호운용할 수 없었습니다. [NIP-42](/ko/topics/nip-42/)는 이 문제에서 신원 증명 부분을, [NIP-43](/ko/topics/nip-43/)은 멤버십 부분을 표준화합니다. 이번 주 TypeScript relay nostream은 두 부분을 end-to-end로 병합했습니다. [PR #702](https://github.com/Cameri/nostream/pull/702)는 암호화된 kind를 인증된 수신자만 읽도록 제한하고, [PR #676](https://github.com/Cameri/nostream/pull/676)은 가입 및 탈퇴 요청 이벤트 전략을 추가했습니다. 두 PR 모두 7월 20일에 병합되었습니다.

### NIP-42: 클라이언트의 relay 인증

[NIP-42](/ko/topics/nip-42/)는 한 가지 질문에 답합니다. 이 연결에는 누가 있는가? 읽기나 쓰기를 제한하려는 relay는 연결 시점이나 요청에 인증이 필요할 때 challenge 문자열을 담은 `AUTH` 메시지를 보냅니다. 클라이언트는 서명된 임시 이벤트 kind 22242를 담은 자체 `AUTH` 메시지로 응답하고, relay는 auth 이벤트가 일반 쓰기인 것처럼 `OK` 메시지로 답합니다. 인증은 연결이 유지되는 동안 유효합니다. 여러 `AUTH` 메시지를 차례로 보내면 하나의 연결에서 여러 pubkey를 인증할 수 있습니다.

서명된 auth 이벤트는 다음과 같습니다:

```json
{
  "id": "4ef6f2c0b1a84c9a3d0f9c58e2a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0",
  "pubkey": "c308e1f882c1f1dff2a43d4294239ddeec04e575f2d1aad1fa21ea7684e61fb5",
  "created_at": 1753195800,
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com/"],
    ["challenge", "challengestringhere"]
  ],
  "content": "",
  "sig": "8b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1"
}
```

relay가 이벤트 `id`의 `sig`를 `pubkey`로 검증하므로, `pubkey`가 증명 대상 신원입니다. Kind 22242는 임시 범위에 속합니다. 이 이벤트는 연결 수준 자격 증명이므로 relay는 저장하거나 다른 클라이언트에 broadcast해서는 안 됩니다. `relay` tag는 서명을 하나의 relay URL에 결합해 가로챈 auth 이벤트가 다른 relay에서 재사용되지 않게 합니다. `challenge` tag는 현재 연결에서 발급된 특정 challenge 문자열에 결합해 이후 재사용을 막습니다. `created_at`은 약 10분 범위 안에서 현재 시각과 가까워야 하므로 오래된 auth 이벤트는 자동으로 만료됩니다. 빈 `content` 필드는 아무 내용도 발행하지 않음을 확인합니다.

명세는 또한 게이팅을 클라이언트에게 가시적으로 만드는 두 가지 기계 판독 가능 접두사를 정의합니다. 클라이언트가 아직 인증하지 않아서 구독을 거부하는 relay는 `auth-required:`로 시작하는 `CLOSED` 메시지로 답하고, 거부된 쓰기는 같은 접두사를 가진 `OK`를 받습니다. 인증했지만 여전히 그 액션에 대한 권한이 부족한 클라이언트는 대신 `restricted:`를 받습니다. 그 구별이 바로 [nostream의 PR #702](https://github.com/Cameri/nostream/pull/702)가 구축하는 것입니다. 암호화된 kind의 읽기는 이제 요청하는 pubkey가 자신이 수신자임을 증명할 때까지 `auth-required:`로 닫힐 수 있습니다.

### NIP-43: Relay 접근 메타데이터 및 요청

[NIP-43](/ko/topics/nip-43/)은 후속 질문에 답합니다. 이제 relay가 당신이 누구인지 알았으니, 당신은 무엇을 할 수 있는가? NIP-42가 라이브 연결에서의 핸드셰이크라면, NIP-43은 멤버십 상태를 설명하고 사용자가 이를 변경하도록 요청할 수 있게 하는 발행된 이벤트의 집합입니다. relay 측에서, relay의 [NIP-11](/ko/topics/nip-11/) `self` 필드의 pubkey가 서명한 kind 13534 이벤트는 pubkey당 하나의 `member` tag를 나열하며, kind 33534로 발행된 역할 정의를 가리키는 선택적 역할 인수가 있습니다. Kind 8000은 멤버가 추가되는 것을 알리고 kind 8001은 제거를 알리며, 둘 다 영향받는 멤버를 위한 `p` tag와 함께 같은 relay 키로 서명됩니다. 사용자 측에서, kind 28934는 `claim` tag에 초대 코드를 담은 가입 요청이고, kind 28935는 사용자가 claim을 요청할 때 relay가 즉석에서 생성하는 일회성 초대 코드 이벤트이며, kind 28936은 탈퇴 요청입니다.

가입 요청은 다음과 같습니다:

```json
{
  "id": "9f0e1d2c3b4a59687a6b5c4d3e2f1098a7b6c5d4e3f2019a8b7c6d5e4f3021a9b8",
  "pubkey": "ee1d336e13779e4d4c527b988429d96de16088f958cbf6c074676ac9cfd9c958",
  "created_at": 1753195900,
  "kind": 28934,
  "tags": [
    ["-"],
    ["claim", "invite-code-from-operator"]
  ],
  "content": "",
  "sig": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2"
}
```

`pubkey`는 가입을 요청하는 사용자이고, kind 28934는 이벤트를 가입 요청으로 표시합니다. `-` tag는 [NIP-70](/ko/topics/nip-70/) 보호 이벤트 marker로, relay가 작성자에게서 직접 받은 이벤트만 수락하게 합니다. `claim` tag에는 별도 경로로 받은 초대 코드가 들어갑니다. `created_at`은 현재 시각에서 몇 분 이내여야 하므로 오래된 요청은 재사용할 수 없습니다. relay는 `OK` 메시지로 claim에 응답하고, 만료되거나 잘못된 코드 같은 실패에는 NIP-42의 `restricted:` 접두사를 재사용하며, kind 13534 리스트를 갱신하고 kind 8000 add-member 이벤트를 발행할 수 있습니다. 멤버십은 의도적으로 단일 이벤트에서 파생하지 않습니다. 명세는 relay가 서명한 리스트를 하나의 입력으로 취급하며, 현재 멤버 여부를 판단하는 클라이언트는 relay의 kind 13534와 멤버 본인의 이벤트를 모두 확인해야 합니다. 클라이언트는 NIP-11 문서의 `supported_nips` 섹션에서 이 NIP를 지원한다고 알리는 relay에만 가입, 초대, 탈퇴 요청을 보내야 합니다. [nostream의 PR #676](https://github.com/Cameri/nostream/pull/676)은 이러한 request kind를 실제 멤버십 변경으로 처리하는 relay 측 로직입니다.

### 역사

NIP-42는 둘 중 훨씬 오래되었습니다. 2023년 1월 2일 [commit c80be21c](https://github.com/nostr-protocol/nips/commit/c80be21c)로 NIPs 저장소에 들어왔습니다. 여기서 fiatjaf는 semisol이 초안을 작성한 이전 relay-auth NIP을 대폭 단순화해, 복잡한 challenge 방식을 명세가 지금도 사용하는 하나의 서명된 임시 이벤트로 축소했습니다. NIP-43은 훨씬 뒤인 2025년 10월 30일에 도입되었습니다. hodlbod의 [PR #1079](https://github.com/nostr-protocol/nips/pull/1079)가 병합되면서 NIP-42의 `restricted:` 접두사 위에 relay 접근 메타데이터와 요청을 추가했습니다. 2년 반의 간격은 멤버십 레이어가 표준화되기 전까지 유료 및 비공개 relay 운영자들이 임시 화이트리스트를 얼마나 오래 사용했는지 보여줍니다.

### 구현

relay 측에서, [nostream](https://github.com/Cameri/nostream)은 이번 주 병합 후 이제 양쪽 절반을 모두 출시합니다. [strfry](https://github.com/hoytech/strfry)는 NIP-42를 구현하여, 인제스터에서 kind 22242 auth 이벤트를 검증하고 설정에서 challenge를 발행합니다. [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay)는 연결 레이어에서 AUTH 핸드셰이크를 처리하며 challenge와 타임스탬프 창을 다루는 테스트가 있습니다. Go relay 프레임워크인 [khatru](https://github.com/fiatjaf/khatru)는 연결당 인증된 pubkey를 추적하여 정책이 그 위에 읽기와 쓰기를 게이트할 수 있게 합니다. 클라이언트 측에서, [Amethyst](https://github.com/vitorpamplona/amethyst)는 Concord 암호화 커뮤니티를 위한 스트림별 auth를 포함하여 relay challenge에 대한 kind 22242 응답에 서명합니다. 두 NIP는 접근 제어를 깔끔한 선으로 나눕니다. NIP-42는 신원 증명으로, 하나의 연결, 하나의 challenge, 몇 분의 유효 기간으로 범위가 지정되며, 정책에 대해 아무것도 말하지 않습니다. NIP-43은 정책으로, 일반 relay 이벤트로 표현됩니다. 누가 멤버인지, 누가 추가되거나 제거되었는지, 그리고 사용자가 그러한 전이를 어떻게 요청하는지. 구현자가 명심해야 할 격차는 NIP-43의 선택적 역할 메타데이터를 넘어선 더 세분화된 권한을 표준화하는 것이 아직 아무것도 없다는 점이므로, 이분법적인 멤버/비멤버 구분 이상을 수행하는 relay는 그 레이어를 스스로 설계하고 있습니다.

---

이번 주는 여기까지입니다. 무언가를 구축하고 있거나 공유할 소식이 있으신가요? NIP-17 DM으로 연락하거나 Nostr에서 저희를 찾아주세요.
