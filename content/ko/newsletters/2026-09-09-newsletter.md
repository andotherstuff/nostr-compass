---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
translationOf: /en/newsletters/2026-09-09-newsletter.md
translationDate: 2026-09-11
draft: false
type: newsletters
description: "Nostr Compass #39에서는 서명된 git 워크플로, 브라우저 게시, 자체 호스팅 라이브 스트림, 커뮤니티 릴레이 동의, 비공개 이벤트, 주요 릴리스, 그리고 NIP-21/NIP-27 링크 규약을 살펴봅니다."
---

Nostr 주간 안내서 [Nostr Compass](https://nostrcompass.org)에 다시 오신 것을 환영합니다.

**이번 주:** [ngit과 GitWorkshop](https://ngit.dev/v3)은 서명된 git 워크플로를 Nostr와 [Blossom](/ko/topics/blossom/)으로 옮기고, [nsite-clay](https://github.com/jooray/nsite-clay)는 브라우저 게시를 복구 가능하게 만들며, [Wingman App](https://github.com/OtherStuffAI/wm-app)은 탐색, 로컬 서명, 인증, 파일을 하나로 결합합니다. [Shosho와 Livelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0)는 자체 호스팅 스트림을 Nostr에 연결하고, [Communitator](https://github.com/dyne/communitator)는 서명 전에 릴레이 템플릿을 검토할 수 있게 하며, [cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743)는 예약 가능 시간대를 게시하고, [Plektos](https://github.com/derekross/plektos/pull/16)는 비공개 이벤트를 암호화합니다. 태그가 지정된 릴리스에서는 [Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4), [Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27), [LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0), [SkateSpots](https://zapstore.dev/apps/org.skatespots.app)에 복구 및 개인정보 보호 관련 작업이 추가되었습니다. 개발 작업은 [NIP-27](/ko/topics/nip-27/) 렌더링, [Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397)의 서명된 릴레이 환경설정, [NIP-A3](/ko/topics/nip-a3/) 결제 대상, Blossom 미러에 걸쳐 진행되었습니다. [NIPs 저장소](https://github.com/nostr-protocol/nips)에 병합된 변경 사항은 라이브 전용 구독과 인증된 애플리케이션 데이터를 명확히 설명합니다. 심층 분석에서는 [NIP-21](/ko/topics/nip-21/) 링크와 NIP-27 참조가 Nostr 프로필과 이벤트를 애플리케이션 간에 전달하는 방식을 설명합니다.

## 주요 소식

### 서명된 git 워크플로가 CI, 비공개 저장소, 릴리스를 Nostr로 옮기다

[9월 8일 v3 출시](https://ngit.dev/v3)는 ngit, GitWorkshop, ngit-grasp, ngit-ci를 하나의 서명된 워크플로로 통합합니다. [ngit](https://ngit.dev/ngit.git)은 브랜치, 패치, pull request를 [NIP-34](/ko/topics/nip-34/) 이벤트로 전달하고, [GitWorkshop](https://ngit.dev/gitworkshop.git)은 검토 인터페이스를 제공합니다. 이번 출시에는 자체 호스팅 지속적 통합 서비스인 ngit-ci 0.1도 추가되었습니다. 이 서비스의 지시와 결과는 서명된 Nostr 이벤트로 전달되므로, 유지관리자가 제어하는 하드웨어에서 코드 검토와 함께 검사를 실행할 수 있습니다.

같은 릴리스에서 [ngit-grasp v3](https://ngit.dev/ngit-grasp.git)는 GRASP-08 비공개 저장소 확장을 통해 비공개 저장소를 지원하고 유지관리자의 권한을 명시적으로 나타냅니다. 서명된 릴리스 기록은 [Blossom](/ko/topics/blossom/)의 자산을 가리킬 수 있으므로, 릴리스 메타데이터와 콘텐츠 주소 기반 파일을 모두 호스팅형 포지 외부에 보관할 수 있습니다. [새 문서 사이트](https://ngit.dev/v3)는 클라이언트, 비공개 저장소, CI, 웹 구성요소를 한곳에 모았습니다.

### nsite-clay가 브라우저 게시를 복구 가능하게 만들다

[8월 31일 서명자 프롬프트 수정](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8), [게시 복구](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0), [9월 2일 편집 제어 기능](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7)을 통해 [nsite-clay](https://github.com/jooray/nsite-clay)는 단일 페이지 사이트를 위한 브라우저 게시 도구가 되었습니다. 사용자는 문서 객체 모델을 그 자리에서 편집하고 결과를 직렬화한 뒤, 콘텐츠 주소 기반 [Blossom](/ko/topics/blossom/) blob으로 업로드하고 사이트의 [NIP-5A](/ko/topics/nip-5a/) manifest를 다시 게시합니다. 로컬 빌드나 서버는 필요하지 않습니다.

이제 [브라우저 게시 도구](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html)는 게시 실패 시 복구를 지원하고 반복되는 서명자 프롬프트를 줄이며, [편집 안내서](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html)는 이 과정을 설명합니다. 결과물은 기존 게이트웨이에서 사용할 수 있는 일반적인 NIP-5A 사이트로 유지됩니다.

### Wingman App이 탐색, 서명, 파일을 결합하다

9월 작업에서는 [파일 선택기](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec), [프로필 게시](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704), [안전한 서명자 및 세션 복원](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6), [테스트를 거친 모바일 빌드](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac)가 [Wingman App](https://github.com/OtherStuffAI/wm-app)에 추가되었습니다. Flutter 셸은 앱 내부에서 열린 페이지에 [NIP-07](/ko/topics/nip-07/) provider를 주입하며, Flight Deck과 Tower 기반 Drive는 브라우저 옆에 작업 공간과 파일 작업 영역을 제공합니다.

Wingman은 [NIP-98](/ko/topics/nip-98/)을 사용해 인증된 HTTP 요청에 서명합니다. [요청 구현](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs)은 서버가 응답하기 전에 검증하는 이벤트를 생성하여, 설치된 하나의 신원이 릴레이 작업, 웹 앱 서명, 파일에 대해 일관된 승인 경로를 사용하도록 합니다.

### Shosho, Livelier의 자체 호스팅 스트림 지원

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0)은 9월 1일 [Livelier](https://github.com/r0d8lsh0p/livelier) 지원과 함께 출시되었다. Livelier의 [8월 31일 출처 표시 업데이트](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc)는 브리지된 프로필에 브리지와 Owncast 출처를 표시한다. Livelier는 Owncast의 공개 디렉터리를 모니터링하고 동영상 스트림의 라이브 여부를 확인한 다음, 주소 지정이 가능한 `kind:30311` [NIP-53](/ko/topics/nip-53/) 이벤트를 게시한다. 탐색은 Nostr를 통해 이루어지지만 동영상은 스트리머의 서버에 남는다.

채팅은 `kind:1311` 이벤트로 브리지를 통과한다. [브리지 설계](https://github.com/r0d8lsh0p/livelier)는 Nostr 리더가 구독 중일 때만 소스 측 연결을 열고, 파생된 신원에 라벨을 지정하며, 임시 채팅을 3시간 후 삭제하는 릴레이로 전송한다. 탐색 릴레이는 브리지 키에서 전송된 라이브 이벤트 쓰기만 허용하며, 채팅 릴레이는 [NIP-42 인증](/ko/topics/nip-42/)과 [NIP-70 보호 이벤트 플래그](/ko/topics/nip-70/)를 사용한다.

### Communitator, 서명 전에 릴레이 템플릿을 검토할 수 있도록 개선

[8월 31일 출시 시리즈](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c)를 통해 [Communitator](https://github.com/dyne/communitator)에 kind `10002` 릴레이 목록, kind `10063` Blossom 서버, kind `10050` 비공개 메시지 수신함을 위한 정규 템플릿이 추가되었다. 서명자가 연결되기 전에 애플리케이션은 정규화된 엔드포인트, 읽기/쓰기 권한, 이벤트 kind, 고정 게시 릴레이, 목적지를 보여준다.

[범위가 제한된 서명 및 게시 흐름](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501)은 연결과 적용을 분리한다. 각 이벤트는 개별적으로 서명되며, 한 번의 실행에서 WebSocket 연결은 최대 4개까지만 사용하고, 긍정적인 [NIP-01](/ko/topics/nip-01/) `OK`를 받은 경우에만 목적지 전송으로 집계한다. 결과는 완전 전송, 부분 전송, 실패, 취소로 구분된다. 공유 템플릿은 신뢰할 수 없는 권고 사항으로 취급되며, [동의 화면](https://github.com/dyne/communitator#security-and-consent)은 릴레이와 네트워크에서 관찰 가능한 정보를 설명한다.

### cal.emre.xyz, NIP-52 약속 가능 시간 게시

공개 저장소는 [9월 2일 최초 커밋](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743)으로 개설되었으며, 이어서 [cal.emre.xyz](https://cal.emre.xyz)를 위한 서명된 [9월 3일 핸들러 발표](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac)가 게시되었다. 호스트는 가능한 시간을 `kind:31923` [NIP-52](/ko/topics/nip-52/) 이벤트로 게시하고, 게스트는 `kind:31925` RSVP를 게시한다.

이 서비스는 릴레이에서 호스트 이벤트와 수락된 일정 중복 RSVP를 읽고, 겹치는 시간대를 제외하며, Nostr 이벤트를 별도 데이터베이스에 복사하지 않고 일정 기록으로 유지한다. 호스트는 [NIP-07](/ko/topics/nip-07/), [NIP-46](/ko/topics/nip-46/), 또는 로컬 키로 서명할 수 있으며, 게스트는 별도의 키를 생성할 수 있다. [저장소](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743)에서는 생성된 `naddr`와 캘린더 링크도 제공하며, 이메일은 기본적으로 비활성화되어 있다.

### Plektos, 비공개 이벤트 전체를 하나의 암호화 채널로 구성

[9월 2일 비공개 이벤트 구현](https://github.com/derekross/plektos/pull/12)은 각 [Plektos](https://github.com/derekross/plektos) 모임을 [Concord](/ko/topics/concord-protocol/) 암호화 커뮤니티 내부의 비공개 채널로 만든다. 게스트 목록, RSVP 명단, 신청 게시판, 스레드, 기여 내역, 표지 이미지, 수정 사항, 삭제 사항이 함께 암호화된다. 초대에는 해당 이벤트의 키만 포함되며, 평문 캘린더 이벤트는 게시되지 않는다.

[9월 6일 수명 주기 감사](https://github.com/derekross/plektos/pull/14)는 wrap이 500개를 초과할 때 직접 조회할 수 있도록 이벤트 정의 id를 기준점으로 사용하면서, 페이지 단위 대체 조회 방식도 유지한다. 초대 번들은 이벤트 종료 30일 후 만료되며 비활성화할 수도 있지만, 이미 채널 키를 획득한 사람은 이를 계속 보유할 수 있다. 별도의 [파서 보안 수정](https://github.com/derekross/plektos/pull/16)은 잘못된 type-length-value (TLV) [NIP-19](/ko/topics/nip-19/) 식별자가 파서를 중단시키는 대신 처리 실패로 끝나도록 한다.

## 태그된 릴리스

### Vector 0.4.4, 암호화 커뮤니티 복구 안전성 개선

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4)는 커뮤니티 복구, 키 교체, 관리, 답글 라우팅 수정과 함께 8월 31일 출시되었다. 재창립은 습격당한 커뮤니티에서 공격자가 사용한 초대 경로를 차단한다. 대체 멤버십은 오래된 로컬 상태를 무효화하며, 한 명의 멤버에게 연결할 수 없더라도 더 이상 명단 전체가 멈추지 않는다. 비어 있는 키 교체는 거부되고, 승격 과정에서 온라인 멤버가 유지되며, 필수 멤버에게 연결할 수 없으면 작업이 실행되지 않는다.

이 [릴리스](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4)는 관리자 삭제 및 차단 내역을 영구 저장하고, 비밀번호 변경 후 방명록을 다시 암호화하며, 재시작 후에도 알림 답글을 해당 대화에 연결하고, 검증된 멀티플레이어 경로만 사용한다. 이는 복구 제어 기능이며, 이미 획득한 키를 폐기하는 기능은 아니다.

### Primal Android 3.5.27, 서명자와 지갑 신원 확인

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27)은 [서명자 신원 확인](https://github.com/PrimalHQ/primal-android-app/pull/1108)과 [지갑 요청 인증](https://github.com/PrimalHQ/primal-android-app/pull/1105)이 8월 31일 병합된 후 9월 3일 출시되었다. 로컬 서명은 요청의 신원이 현재 보유한 계정과 일치하지 않으면 요청을 거부하며, 수신된 [NIP-47](/ko/topics/nip-47/) 요청은 처리 전에 인증된다. Zap 투표 라우팅은 투표가 답글에 표시되는 경우에도 표를 투표 작성자에게 전송한다.

### GRAIN 0.8.0-rc2, 확인 응답은 보냈지만 저장되지 않는 경로 차단

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2)는 비동기 LMDB 데이터베이스 기록기가 저장 공간이 가득 찬 것을 감지하기 전에 저장 실패 상황에서도 `OK`를 반환할 수 있었던 문제를 수정해 9월 7일 출시되었습니다. 이제 릴레이는 사용량이 80%와 95%에 도달하면 경고하고, 삭제에 필요한 공간을 남기기 위해 97%부터 새 이벤트를 거부하며, 수락 후 발생한 기록 실패를 보고합니다. 보존 처리는 가장 오래된 항목부터 순회하고, 종료 과정에서는 늦게 도착한 메시지를 처리하며, 유효하지 않은 필터가 더 이상 함께 있는 유효한 필터까지 폐기하지 않습니다.

이 [릴리스](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2)는 또한 kind `10166` 모니터 공지와 kind `30166` 릴레이 보고서를 대조 확인하고, 오래된 보고서를 제거하며, 설정된 릴레이를 대체 경로로 유지합니다. 또한 정적인 0 대신 실제 제한과 인증 정보를 [NIP-11](/ko/topics/nip-11/)에 보고합니다.

### LibreNostr 0.5.0–0.5.2, Tor 라우팅 장애 시 연결 차단

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0)은 릴레이, zap, 업로드, 미디어, 재생, 미리보기를 하나의 SOCKS 포트를 통해 라우팅하는 Orbot 모드와 zap 시트 충돌 수정 사항을 포함해 9월 7일 출시되었습니다. Orbot이나 프록시를 사용할 수 없으면 직접 경로로 트래픽이 유출되지 않도록 연결을 중단합니다. [Version 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1)은 느린 [NIP-50](/ko/topics/nip-50/) 검색 때문에 로컬 결과가 지연되지 않도록 했으며, [0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2)는 재귀적인 스레드 레이아웃을 교체하고 스레드 순서를 수정했습니다.

이 [장애 시 차단 동작](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0)은 릴리스에 명시된 모든 네트워크 접점에 적용되며, 해당 클라이언트가 장시간 유지되므로 재시작이 필요합니다. 패치 릴리스는 이 방식을 유지하면서 관련 없는 검색, 스택 깊이, 레이아웃 오류를 제한합니다.

### SkateSpots, 기기 내 릴레이 경로 추가

서명된 [9월 8일 Zapstore 릴리스](https://zapstore.dev/apps/org.skatespots.app)는 SkateSpots에 선택 사항인 Citrine 릴레이를 추가했습니다. 스팟, 크루, 메시지, 지도 데이터를 로컬에서 불러올 수 있고, 게시물은 오프라인 상태에서 대기열에 들어가며, 휴대전화에 로컬 사본이 보관됩니다. 기존 stash와 메시지 콘텐츠는 계속 종단간 암호화됩니다. 결제 확인에서는 접근 권한을 부여하거나 기여 금액을 집계하기 전에 인보이스 금액과 제공업체가 발급한 zap 영수증을 요구합니다.

[로컬 릴레이](https://zapstore.dev/apps/org.skatespots.app)는 저장과 연속성을 위한 선택 사항이며, 모든 원격 릴레이를 대체하는 것은 아닙니다. 스케이터는 연결이 끊긴 동안에도 계속 작업한 뒤 나중에 서명된 활동을 동기화할 수 있습니다. 결제 변경 사항은 사용자가 직접 작성한 영수증이 결제 완료 증명으로 사용되는 것을 막습니다.

### Whistle 1.8.15, 암호화 그룹의 수명 주기 복구 수정

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15)는 경로 수준 상태 보유자가 애플리케이션 전체의 릴레이 구독과 위치 업데이트를 종료하지 않도록 Android 수명 주기 문제를 수정한 뒤 9월 3일 출시되었습니다. 릴리스 노트에는 잠금 또는 doze 상태 이후 연결 상태가 새로 고쳐지고, 관찰된 사례에서 501개 이벤트의 적체가 복구되었다는 내용도 있습니다.

이 [버그](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15)는 장시간 유지되는 서비스의 소유권을 수명이 짧은 화면에 연결한 데서 발생했습니다. activity 범위의 인스턴스를 계속 유지하고 일회성 읽기 전에 소켓을 확인함으로써, 일반적인 Android 화면 이동과 백그라운드 일시 중지가 빈 그룹처럼 보일 가능성을 줄였습니다.

### TWENTY ONE Companion 1.12.0, 암호화 DM과 기존 채팅 분리

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0)은 [NIP-17](/ko/topics/nip-17/) gift-wrapped DM을 포함해 9월 5일 출시되었습니다. 암호화된 받은편지함은 이전의 space 채팅과 분리되어 있습니다. 해당 메시지는 애초에 암호화되지 않았고 이전할 수 없으므로 기존 채팅은 별도로 유지됩니다. 릴레이 정책이 허용하는 범위에서 PDF와 동영상을 지원하며, 개인 숨김 설정은 운영자 차단으로 바뀌지 않은 채 동기화됩니다.

이처럼 [명확히 구분하는 방식](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0)은 보안 모델의 일부입니다. 이전 기록을 보안 받은편지함이라고 부르면 그 출처를 잘못 나타내게 되며, 이를 알리지 않고 이전하면 작성 당시에는 존재하지 않았던 암호화가 적용된 것처럼 보일 수 있습니다.

### ZapStore 1.1.2, 이벤트 id와 인증서 교체 검증

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2)는 NIP-01 이벤트 id 검증 기능과 함께 9월 4일 출시되었습니다. 클라이언트는 수신 이벤트의 id를 다시 계산하고, 일치하지 않으면 사용하기 전에 거부합니다. 이 릴리스는 ZapStore 외부에서 설치된 패키지도 식별합니다. 서버에서는 [인증서 해시 보존](https://github.com/zapstore/relay/pull/8)을 통해 반복된 `apk_certificate_hash` 태그를 유지하므로, Android 서명 키를 교체할 때 승인된 계보를 보존할 수 있습니다.

[이벤트 id 검사](https://github.com/zapstore/zapstore/releases/tag/1.1.2)는 릴레이나 캐시가 기존 id를 유지한 채 태그 또는 콘텐츠를 변경하지 못하게 합니다. 설치 출처 표시는 동일한 애플리케이션 id를 가진 Android 패키지가 다른 경로에서 설치되었을 때 별도의 출처 정보를 제공합니다.

### Amber 6.6.1, 서명자 응답의 귀속 관계 유지

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1)은 선택 사항인 `kind`가 누락되어도 허용하도록 권한 구문 분석을 수정하고, 거부된 서명 요청이 원래 요청 id를 반환하도록 한 뒤 9월 4일 출시되었습니다. 호출한 애플리케이션은 거부 응답을 제출한 작업과 연결할 수 있습니다. 이 릴리스는 원격 서명자 기본값도 갱신하고 인덱서 릴레이를 추가했습니다.

이러한 [수정 사항](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1)은 양방향의 귀속 관계를 유지합니다. 선택 사항인 필드가 없어도 권한 기록을 계속 사용할 수 있으며, 거부 응답도 이를 유발한 요청과 연결된 상태로 유지됩니다. 릴레이 기본값 변경은 검색에 영향을 주지만, 서명자의 로컬 승인 결정을 대체하지는 않습니다.

## 개발 중

### Zap Cooking, 릴레이 힌트가 포함된 NIP-27 참조 렌더링

[9월 4일 병합된 변경 사항](https://github.com/zapcooking/frontend/pull/665)을 통해 [Zap Cooking](https://github.com/zapcooking/frontend)은 이제 글, 레시피, 에디터 미리보기, 인쇄 화면에서 `nostr:npub` 및 `nostr:nprofile` 참조를 렌더링한다. 유효하지 않은 식별자는 텍스트로 남고, 확인 과정은 작업을 차단하지 않으며, 에디터는 실제로 서명될 Markdown을 미리 보여준다. 릴레이 정보가 있으면 단순 `npub`은 아웃박스 릴레이와 그에 맞는 `p` 태그가 포함된 `nprofile`이 된다.

같은 주에는 [작성자 범위로 제한된 kind `30023` 조회](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7)를 수정하고, 중복 제거 및 오래된 쿼리 방지 기능과 함께 [검증된 NIP-50 검색 릴레이](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea)를 추가했으며, 의존성 변경으로 잔액과 거래 내역이 작동하지 않게 된 후 [NIP-47 지갑 호출](https://github.com/zapcooking/frontend/pull/705)을 복구했다.

### Conduit, 서명된 릴레이 및 Blossom 설정 조정

[Conduit](https://github.com/Conduit-BTC/conduit-mono)는 9월 2일 [Blossom 설정 편집](https://github.com/Conduit-BTC/conduit-mono/pull/374)을, 9월 7일 [서명된 설정 조정](https://github.com/Conduit-BTC/conduit-mono/pull/397)을 병합했다. Market과 Merchant는 유효한 최신 kind `10002` 릴레이 목록과 kind `10050` 인박스 선언을 유지하고, 더 새로운 이벤트가 잘못된 형식이더라도 사용 가능한 서명 목록을 보존하며, 명시적으로 비어 있는 목록과 조회할 수 없는 목록을 구분한다. 또한 선언된 릴레이에 연결하지 못하더라도 이를 코드의 기본값으로 대체하지 않는다.

[kind `10063` 편집기](https://github.com/Conduit-BTC/conduit-mono/pull/374)를 사용하면 해당 서버에 접속하거나 선언되지 않은 기본 서버를 삽입하지 않고도 순서가 지정된 HTTPS 미디어 서버 목록을 불러오고, 순서를 변경하고, 검토하고, 외부에서 서명하고, 게시한 뒤 다시 읽을 수 있다.

### 세 클라이언트에 도입된 NIP-A3 결제 대상

9월 1일부터 3일까지 [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851), [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98)는 NIP-A3 kind `10133` 결제 대상을 구현했다. Amethyst는 호환되는 대상이 있을 때만 사용자가 선택적으로 결제 앱으로 넘길 수 있도록 하며 이를 zap으로 바꾸지 않는다. Grimoire는 지갑 URI를 만들기 전에 고정 레지스트리를 사용한다. Pollerama는 Monero 주소를 검증하고 대상을 조회하기 전에 작성자의 릴레이 목록을 가져온다. 각 클라이언트에는 여전히 허용된 결제 방식, 릴레이 경로, 정확한 표시가 필요하다.

### Ditto, Blossom 대체 경로와 라이브 임베드 확장

[Ditto](https://github.com/soapbox-pub/ditto)는 9월 6일 [광범위한 Blossom 대체 경로 및 미러링](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07)을 병합했다. 이제 아바타, 배지, 배너, 커뮤니티 이미지, 사용자 지정 이모지, 애플리케이션 아이콘은 동일한 blob 해시를 사용해 선언된 서버에서 가져오기를 시도한다. 미러 업로드에는 표준 BUD-11 인증 토큰을 사용한다. [9월 4일 변경 사항](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa)에서는 간결한 `kind:30311` 라이브 스트림 임베드를 추가했다.

## 프로토콜 및 명세 작업

### Nostr 구현 가능성

[NIP-01](/ko/topics/nip-01/)에는 9월 4일 병합된 [`limit: 0` 필터에 관한 설명](https://github.com/nostr-protocol/nips/pull/2460)이 추가됐다. 릴레이는 저장된 이벤트를 하나도 반환하지 않아야 하고, 초기 쿼리가 완료되면 반드시 `EOSE`를 전송해야 하며, 새롭게 일치하는 이벤트를 받을 수 있도록 구독을 활성 상태로 유지해야 한다. 클라이언트는 로컬 기록을 유지하면서 필터 필드 하나만으로 실시간 전용 구독을 열 수 있다. 이 설명에는 여러 릴레이 구현체와 공개 릴레이에서 호환되는 동작이 기록되어 있다.

[NIP-78](/ko/topics/nip-78/)에는 9월 3일 병합된 [인증된 앱 데이터 요구 사항](https://github.com/nostr-protocol/nips/pull/2458)이 추가됐다. 릴레이는 kinds `78` 및 `30078`에 대해 [NIP-42](/ko/topics/nip-42/) 인증을 요구하는 것이 권장되며, 인증된 이벤트 작성자에게만 이를 제공하는 것이 권장된다. 이는 권고 사항일 뿐 기밀성을 보장하지 않는다. 클라이언트는 임의의 릴레이를 비공개 저장소로 간주할 수 없다. 또한 이 병합에서는 사용자 지정 앱 데이터 kind를 범용 공개 교환 형식으로 사용하는 것을 권장하지 않는다.

[NIP-AC](/ko/topics/nip-ac/)는 명시적으로 논의가 열려 있는 [WebRTC 시그널링 제안](https://github.com/nostr-protocol/nips/pull/2461)으로 9월 4일 공개됐다. 이 제안은 ping, 연결 요청, offer, answer, ICE candidate에 임시 ephemeral kinds를 사용하며, `p`로 수신자를 지정하고 세션 `e` 태그로 그룹화한다. kind `30600`은 검색을 지원한다. 릴레이는 해당 시그널링 이벤트를 브로드캐스트하는 것이 권장되며 이를 저장해서는 안 되고, 피어는 직접 연결된다. 번호는 아직 잠정적이며, 클라이언트는 [NIP-65 릴레이 목록](/ko/topics/nip-65/)을 사용하는 것이 권장된다. 기밀성이 필요한 애플리케이션은 offer, answer, candidate 콘텐츠를 [NIP-44](/ko/topics/nip-44/)로 암호화하는 것이 권장된다.

## NIP 심층 분석: 이벤트 텍스트의 URI 링크와 참조

다른 애플리케이션에서 Nostr 식별자를 열려면 먼저 애플리케이션 간에 전달 가능한 의미가 있어야 한다. [NIP-21](/ko/topics/nip-21/)은 `nostr:` URI 스킴 뒤에 [NIP-19](/ko/topics/nip-19/) 식별자를 배치해 브라우저, 운영 체제, 애플리케이션이 처리할 수 있는 단일 형식을 제공한다. [NIP-27](/ko/topics/nip-27/)은 읽을 수 있는 이벤트 `content` 안에서 동일한 URI가 무엇을 의미하는지 정의한다. NIP-21은 애플리케이션 경계를 넘고, NIP-27은 서명된 글 안에 프로필이나 이벤트 참조를 유지한다. 어느 쪽도 이벤트 kind를 만들거나 릴레이 메시지를 변경하지 않는다. [두 명세](https://github.com/nostr-protocol/nips/tree/master)는 링크 및 렌더링 동작만 정의한다.

### URI 디스패치와 NIP-19 의미론

[NIP-21의 문법](https://github.com/nostr-protocol/nips/blob/master/21.md)은 `nostr:` 뒤에 하나의 NIP-19 bech32 엔티티가 오는 형식이다. `nsec`은 개인 키를 인코딩하므로 제외된다. 권한, 경로 또는 쿼리 구성 요소가 없으므로 규격을 준수하는 링크는 `nostr://npub1...`이 아니라 `nostr:npub1...`이다. 플랫폼이나 클라이언트가 핸들러로 등록할 수 있지만, 사양은 설치된 애플리케이션을 선택하거나 웹 대체 동작을 정의하지 않는다.

접두사는 클라이언트가 무엇을 디코딩해야 하는지 알려준다. `npub`에는 공개 키가, `note`에는 이벤트 id가 담긴다. `nprofile`은 프로필에 선택적 릴레이 힌트를 추가하고, `nevent`는 이벤트 id에 릴레이, 작성자, kind를 추가하며, `naddr`에는 주소 지정 가능 이벤트의 작성자, kind, `d` 식별자와 선택적 릴레이가 담긴다. 이러한 형식은 [NIP-19 type-length-value 필드](https://github.com/nostr-protocol/nips/blob/master/19.md)를 사용한다. 힌트는 검색 범위를 좁히지만, 릴레이가 이벤트를 보유하고 있는지 또는 작성자가 통제권을 갖고 있는지를 입증하지는 않는다. 가져온 모든 이벤트는 여전히 id를 다시 계산하고 서명을 확인해야 한다.

[NIP-21 사양](https://github.com/nostr-protocol/nips/blob/master/21.md)의 프로필 형식은 다음과 같다.

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)은 HTML 브리지도 정의한다. Nostr 이벤트를 제공하는 페이지는 `<link rel="alternate">`에 해당 이벤트의 `naddr`를 넣을 수 있고, 프로필은 `<link rel="me">` 또는 `<link rel="author">`에 `nprofile`을 넣을 수 있다.

### NIP-27 렌더링과 선택적 태그

[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)은 kind `1` 노트와 kind `30023` 글처럼 사람이 읽을 수 있는 이벤트 콘텐츠에 적용된다. 작성기는 `@name`을 표시할 수 있지만, 서명되는 문자열에는 `nostr:nprofile1...`을 게시한다. 리더는 URI를 검색하고 해당 NIP-19 엔티티를 디코딩한 뒤 대상을 가져오며, 이름, 카드, 미리보기 또는 로컬 링크를 렌더링할 수 있다. 디코딩에 실패하면 URI는 일반 텍스트로 남는다. 원본 콘텐츠는 다시 작성해서는 안 된다. 이를 변경하면 NIP-01 직렬화, id, 서명이 바뀐다.

콘텐츠 참조와 태그는 서로 관련되어 있지만 역할은 구분된다. [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)은 선택적 `p` 및 `e` 태그와 [NIP-18](/ko/topics/nip-18/)의 `q` 태그를 설명한다. 클라이언트는 알림이나 스레드 관계를 만들지 않고 참조를 표시할 수 있다. 인용을 검색할 수 있게 하려면 URI와 `q` 태그를 모두 기록해야 한다. [Zap Cooking의 9월 4일 구현](https://github.com/zapcooking/frontend/pull/665)은 URI를 유지하면서 릴레이 힌트와 일치하는 `p` 태그를 추가해 이러한 구분을 따른다. `p` 또는 `q`를 추가해도 URI가 비공개로 바뀌지는 않으며, NIP-27에는 숨겨진 멘션 모드가 없다.

다음 [kind `1` 이벤트](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a)는 `wss://nos.lol`에서 복구되었으며, 구체적인 NIP-27 참조로 포함하기 전에 검증되었다. 이 이벤트의 `content`에는 버전에 독립적인 주소 지정 가능 이벤트를 가리키는 `naddr`가 들어 있다. 이를 디코딩하면 kind `30402`, 작성자 `91036d...310a`, 워크북의 `d` 식별자, `wss://nos.lol/` 힌트를 얻는다. `q`, `p`, `t`, `zap`, `client` 태그는 애플리케이션이 선택한 것이며 NIP-27의 요구 사항이 아니다.

```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### 신뢰, 실패 동작 및 클라이언트 구현

안전한 리더는 완전한 `nostr:` 토큰을 찾고, bech32를 검증하며, NIP-19를 디코딩하고, `nsec`을 거부하며, 알 수 없는 TLV 유형을 무시하고, 잘못된 형식이거나 지나치게 큰 텍스트는 그대로 둔다. `npub`과 `nprofile`은 프로필 쿼리로 이어지고, `note`와 `nevent`는 변경 불가능한 이벤트를 식별하며, `naddr`는 해당 kind, 작성자 및 `d` 태그에 맞는 최신 유효 주소 지정 가능 이벤트를 선택한다. 릴레이 힌트는 검색 범위를 줄이지만 신뢰 범위를 넓히지는 않는다. [NIP-01 이벤트 규칙](https://github.com/nostr-protocol/nips/blob/master/01.md)에 따라 클라이언트는 가져온 `nevent`의 id를 검증하고, 주소 지정 가능 이벤트의 교체 규칙을 적용하기 전에 모든 `naddr` 후보의 서명을 확인한다.

인라인 미리보기는 개인정보 보호와 리소스 비용을 고려해 클라이언트가 선택할 사항이다. 모든 참조를 가져오면 독자의 관심사가 드러나고 조회 요청이 폭증할 수 있으므로, 클라이언트는 캐시를 사용하고, 화면에 표시될 때까지 가져오기를 미루며, 동시 요청 수를 제한하고, 익숙하지 않은 미디어는 클릭해야 불러오도록 할 수 있다. [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)에 따라 미리보기는 현재 작성자가 서명한 텍스트와 명확히 구분되어야 한다. 실패한 경우 검증된 콘텐츠로 조용히 처리해서는 안 되며, 해석되지 않은 텍스트나 이용할 수 없는 카드로 표시해야 한다.

식별자 유형에 따라서도 신뢰 방식이 달라진다. `nevent`는 변경 불가능한 바이트를 가리키므로, 클라이언트는 직렬화된 id가 요청한 id와 다른 이벤트를 거부할 수 있다. `naddr`는 교체 가능한 좌표를 가리키므로, 클라이언트는 표시할 버전을 결정하기 전에 각 후보를 검증하고 주소 지정 가능 이벤트 규칙을 적용해야 한다. 어느 경우든 릴레이 힌트는 첫 번째 쿼리에 유용하지만, 해당 릴레이나 반환된 콘텐츠를 보증하지는 않는다. [NIP-19의 TLV 정의](https://github.com/nostr-protocol/nips/blob/master/19.md)는 이러한 검사를 명시적으로 수행하는 데 필요한 데이터를 제공한다.

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)은 Nostr 외부에서 열 수 있는 이식 가능한 링크를 정의하고, NIP-27은 동일한 링크가 서명된 텍스트 안에서 지속적으로 유지되도록 한다. NIP-21만 구현한 클라이언트는 붙여넣은 URI를 열 수 있지만 내장된 참조를 렌더링할 수는 없다. NIP-27을 완전히 지원하려면 스캔, 안전한 디코딩, 가져오기 정책, 로컬 렌더링, 알림 및 인용 태그에 관한 명시적인 선택이 추가로 필요하다. 공통 URI를 사용하면 클라이언트가 이러한 계층을 동일하게 표시하도록 강제하지 않으면서도 상호 운용성을 유지할 수 있다. [Damus](https://github.com/damus-io/damus)는 인라인 참조를 유형이 지정된 멘션으로 모델링한다. Damus의 [멘션 코드](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift)는 `npub`과 `nprofile`을 프로필 참조에, `note`와 `nevent`를 이벤트 참조에, `naddr`를 주소 참조에 매핑하며, [NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift)는 이를 적절한 대상으로 연결한다. [Primal Android](https://github.com/PrimalHQ/primal-android-app)는 [스킴과 붙여넣은 형식을 파싱하고](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt), bech32를 검증하며 릴레이 힌트를 추출한 다음, [참조를 노트 콘텐츠 모델에 매핑한다](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt). [Zap Cooking](https://github.com/zapcooking/frontend/pull/665)은 기사, 레시피, 편집기 미리보기 및 인쇄 보기에서 동일한 참조를 렌더링한다.

---

프로젝트나 뉴스 항목을 공유하려면 [Nostr Compass 프로젝트](https://github.com/andotherstuff/nostr-compass)를 통해 NIP-17 DM을 보내면 된다.
