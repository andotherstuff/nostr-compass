---
title: 'Nostr Compass #12'
date: 2026-03-04
translationOf: /en/newsletters/2026-03-04-newsletter.md
translationDate: 2026-03-04
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [Marmot Development Kit](https://github.com/marmot-protocol/mdk)이 암호화 미디어와 다중 언어 바인딩을 포함한 [첫 공개 릴리스](#marmot-development-kit-첫-공개-릴리스-출시)를 출시했습니다. [Nostrability](https://github.com/nostrability/outbox)가 14개 relay 선택 알고리즘에 대한 [outbox 모델 벤치마크](#outbox-모델-분석)를 발표했습니다. [Wisp](https://github.com/barrydeen/wisp)가 8일 만에 [첫 알파에서 베타](#wisp-알파에서-베타까지)로 Tor와 [NIP-55](/ko/topics/nip-55/) (Android 서명자 애플리케이션) 서명을 추가했습니다. [NIP-91](#nip-업데이트) (AND 필터)이 병합되었습니다. [Vector v0.3.1](#vector-v031)이 15배 성능 향상과 함께 negentropy 동기화를 제공합니다. 이번 호에는 프로토콜이 세 개의 relay를 서비스하는 사양 재작성에서 Damus App Store 폭발, 메시 네트워킹과 AI 에이전트 제안까지 추적하는 Nostr 2월의 5년 회고도 포함됩니다.

## 뉴스

### Outbox 모델 분석

[Nostrability](https://github.com/nostrability/outbox)가 탈중앙화 relay 네트워크에서 다양한 relay 선택 알고리즘이 event를 얼마나 잘 검색하는지 테스트하는 일련의 outbox 모델 벤치마크를 발표했습니다. 프로젝트는 10일 동안 16개의 PR과 76개의 커밋을 병합하여, [NIP-65](/ko/topics/nip-65/) (Relay List Metadata) 구현 전략에 대한 가장 철저한 실증 분석을 만들어냈습니다.

벤치마크는 5개 언어의 15개 클라이언트 및 라이브러리에서 실제 팔로우 목록을 대상으로 14개 relay 선택 알고리즘을 테스트합니다. 인기 relay만 쿼리하는 기준선 접근법은 대략 26%의 event를 검색합니다. Thompson Sampling을 사용한 탐욕적 집합 커버는 80-90% 재현율에 도달합니다. 쌍곡선 할인과 EWMA relay 지연 추적을 사용하는 지연 인식 변형을 추가하면 6개 테스트 프로필에서 2초 시점의 완전성이 62-80%에서 72-96%로 향상되었습니다.

[NIP-66](/ko/topics/nip-66/) (Relay Monitoring) 죽은 relay 필터링이 중요한 역할을 했습니다. [nostr.watch](https://nostr.watch) 활성 데이터를 기반으로 relay 후보를 사전 필터링하면 죽은 relay가 40-64% 제거되고 relay 성공률이 30%에서 75-85%로 두 배 증가했습니다. 피드 로딩 시간은 39% 감소했습니다(10개 프로필에서 40초에서 24초로). EOSE 레이스 시뮬레이션에서는 첫 relay가 완료될 때 중단하는 것보다 EOSE에 200ms 유예 기간을 더해 기다리는 것이 완전성을 향상시켰습니다.

relay 라우팅을 완전히 다시 작성할 수 없는 클라이언트의 경우, "하이브리드 outbox 강화" 접근법은 기존의 하드코딩된 앱 relay 위에 저자별 outbox 쿼리를 추가합니다. 이 하이브리드는 26% 기준선 대비 80%의 1년 event 재현율을 달성하여, 레거시 relay 아키텍처를 가진 클라이언트에게 마이그레이션 경로를 제공합니다.

### ContextVM, MCP NIP 제출 및 임시 Gift Wrap 출시

Nostr와 [Model Context Protocol](https://modelcontextprotocol.io/)을 연결하는 프로토콜 [ContextVM](https://contextvm.org)이 이번 주 [NIPs 저장소](https://github.com/nostr-protocol/nips)에 두 개의 제안을 제출했습니다. [PR #2246](https://github.com/nostr-protocol/nips/pull/2246)은 임시 kind 25910 event를 사용하여 Nostr를 통해 MCP JSON-RPC 메시지를 전송하는 규약으로 CVM을 공식화합니다. [PR #2245](https://github.com/nostr-protocol/nips/pull/2245)는 [NIP-59](/ko/topics/nip-59/) (Gift Wrap)를 [NIP-01](/ko/topics/nip-01/) (Basic Protocol Flow) 임시 의미론을 따르는 임시 kind(21059)로 확장하여, relay가 전달 후 래핑된 메시지를 폐기할 수 있게 합니다.

임시 gift wrap 규약은 ContextVM SDK v0.6.x 릴리스 계열에서 [CEP-19](https://docs.contextvm.org/spec/ceps/cep-19/)로 출시되었습니다. [SDK 구현](https://github.com/ContextVM/sdk)은 세 가지 설정을 가진 `GiftWrapMode` 열거형을 추가합니다: OPTIONAL(두 kind 모두 수락하고 피어 기능을 자동 감지), EPHEMERAL(kind 21059만), PERSISTENT(kind 1059만). AI 도구 호출의 경우, 임시 모드는 relay에 중간 요청-응답 트래픽을 저장하는 것을 피하여 저장 비용과 프라이버시 노출을 모두 줄입니다.

독립 운영자로부터 Wolfram Alpha 쿼리 서버를 포함한 새로운 공개 MCP 서버가 네트워크에 등장했습니다. ContextVM 팀은 v0.6.x 릴리스 주기와 함께 CEP-15(공통 도구 스키마)와 CEP-17(서버 relay 목록 게시)을 발표했습니다.

### Marmot Development Kit 첫 공개 릴리스 출시

[Pika](https://github.com/sledtools/pika)와 [White Noise](https://github.com/marmot-protocol/whitenoise)에서 [Marmot](/ko/topics/mls/) 암호화 메시징을 구동하는 Rust 라이브러리 [MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit)가 첫 공개 릴리스로 [v0.6.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.6.0)을 출시했습니다. 200개 이상의 PR이 이 버전에 병합되었으며, 6명의 새 기여자가 참여했습니다.

이 릴리스에는 HKDF 시드 파생(MIP-01 v2)을 사용한 암호화 미디어 지원(MIP-04), 결정론적 커밋 경합 해결(MIP-03), 암호화된 로컬 저장소, Marmot 커밋 및 제안을 위한 관리자 인증 검증, 프로토콜 확장성을 위한 GREASE 지원이 포함됩니다. Kotlin, Python, Ruby, Windows용 바인딩과 Android 크로스 컴파일이 함께 제공됩니다. 라이브러리는 보안 권고 수정과 메모리에서 민감한 값을 제로화하는 `Secret<T>` 타입이 포함된 OpenMLS 0.8.0으로 업그레이드됩니다.

동반 프로토콜 변경([MIP-03](https://github.com/marmot-protocol/marmot/pull/48))은 kind 445 메시지의 [NIP-44](/ko/topics/nip-44/) (Encrypted Payloads) 암호화를 ChaCha20-Poly1305로 대체했습니다. NIP-44는 사양상 UTF-8 문자열 입력을 요구하여 표준 TypeScript Nostr 라이브러리를 통해 원시 Marmot 메시지 바이트를 전달하는 것이 불가능했습니다. 대체 방식은 Marmot exporter secret에서 직접 키를 파생합니다. 이 호환성 깨뜨리는 변경은 [코어 사양](https://github.com/marmot-protocol/marmot/pull/48), [MDK](https://github.com/marmot-protocol/mdk/pull/208), [TypeScript SDK](https://github.com/marmot-protocol/marmot-ts/pull/54) 전반에 걸친 조율된 업데이트가 필요했습니다.

hzrd149가 유지 관리하는 TypeScript 구현 [marmot-ts](https://github.com/marmot-protocol/marmot-ts)는 자체적으로 호환성을 깨뜨리는 API 변경이 포함된 4개의 PR을 병합했습니다. [종합 업데이트](https://github.com/marmot-protocol/marmot-ts/pull/52)에는 생성/게시/순환 라이프사이클을 위한 키 패키지 관리자, `sendChatMessage` 편의 메서드, 가입 없이 초대 미리보기(`readInviteGroupInfo`), 순방향 비밀성 순환을 위한 자기 업데이트, 구조화된 디버그 로깅이 추가되었습니다. 그룹 복호화 API는 `readGroupMessage`에서 `decryptGroupMessage`로 이름이 변경되었으며 더 풍부한 결과 변형(processed/skipped/rejected/unreadable)이 제공됩니다. gzuuus는 NIP-65 relay 지원과 MIP-00에 따른 최후의 수단 키 패키지 처리가 포함된 예제 정리에 기여했습니다.

모바일 앱과 새로운 TUI를 모두 구동하는 Rust 백엔드 [White Noise CLI](https://github.com/marmot-protocol/whitenoise-rs)(`wn`)는 10일 동안 16개의 PR을 병합했습니다. 서명자 라이프사이클 처리가 RAII 스코프 가드를 통한 취소 안전성을 확보하여([PR #538](https://github.com/marmot-protocol/whitenoise-rs/pull/538)), 중단된 작업이 서명자 상태를 누출할 수 있는 부류의 버그를 수정했습니다. 로그인은 이제 필수 relay 목록(kind 10002/10050/10051)이 누락되면 차단되며([PR #515](https://github.com/marmot-protocol/whitenoise-rs/pull/515)), giftwrap 구독은 inbox 목록이 없을 때 [NIP-65](/ko/topics/nip-65/) relay로 대체됩니다([PR #518](https://github.com/marmot-protocol/whitenoise-rs/pull/518)). 디버그 모드([PR #528](https://github.com/marmot-protocol/whitenoise-rs/pull/528))는 데이터베이스 쿼리와 MLS 래칫 트리 검사를 JSON 출력으로 노출합니다. 기타 수정 사항으로 서명자 재등록 후 구독 복구, welcome 메시지 캐치업 타이밍, relay 필터 검증, 사용자 검색 반경 제한이 처리되었습니다.

Marmot은 이번 주 핵심 Rust 스택을 넘어 크게 확장되었습니다. White Noise 메시징 스택에 대한 터미널 기반 인터페이스 [White Noise TUI](https://github.com/marmot-protocol/wn-tui)가 3월 3일 출시되었습니다. `wn` CLI를 서브프로세스로 래핑하고 Elm에서 영감을 받은 단방향 아키텍처를 통해 JSON 출력을 렌더링하며, 읽지 않음 표시기가 있는 다중 대화 탐색, 그룹 생성 및 멤버 검색, 실시간 메시지 스트리밍, 터미널에서의 이모지 리액션을 제공합니다.

[DavidGershony](https://github.com/DavidGershony)가 Rust 도구 체인의 계층화된 아키텍처를 반영하는 완전한 C# Marmot 스택을 발표했습니다. [dotnet-mls](https://github.com/DavidGershony/dotnet-mls)는 C#로 MLS RFC 9420 암호화 프리미티브를 구현합니다. [marmot-cs](https://github.com/DavidGershony/marmot-cs)는 이를 기반으로 Nostr relay 전송을 추가하며, MDK의 C# 동등물로 기능합니다. [OpenChat](https://github.com/DavidGershony/openChat)은 .NET 9와 Avalonia UI로 구축된 크로스 플랫폼 데스크톱 앱으로, NIP-44 DM, Marmot 그룹 암호화, [NIP-46](/ko/topics/nip-46/) (Nostr Connect) 원격 서명, 다중 relay 상태 표시기를 갖춘 작동하는 채팅 클라이언트로 통합합니다.

[MDK PWA Reference](https://github.com/zerosats/mdk-pwa-reference)는 Marmot 암호화 애플리케이션 구축을 위한 Progressive Web App 템플릿을 제공하며, AI 에이전트의 그룹 채팅 참여와 Arkade 지갑 인프라를 통한 Bitcoin 결제에 대한 실험적 지원이 포함됩니다.

### Wisp, 알파에서 베타까지

[Wisp](https://github.com/barrydeen/wisp)는 2월 24일 [첫 알파](https://github.com/barrydeen/wisp/releases/tag/v0.1.0-alpha)에서 3월 3일 [v0.3.4-beta](https://github.com/barrydeen/wisp/releases/tag/v0.3.4-beta)까지, 8일 동안 19개의 릴리스, 115개의 병합된 PR, 276개의 커밋을 생산한 새로운 Android Nostr 클라이언트입니다.

기능 궤적은 대부분의 클라이언트가 수개월이 걸리는 영역을 커버합니다. v0.1.0은 outbox/inbox relay 모델 지원과 온보딩 흐름과 함께 출시되었습니다. v0.1.3까지 클라이언트는 Amber를 위한 [NIP-55](/ko/topics/nip-55/) intent 기반 서명, `.onion` relay 연결을 위한 내장 Tor SOCKS5 프록시, [NIP-47](/ko/topics/nip-47/) (Nostr Wallet Connect)를 갖추었습니다. v0.2.0은 뮤트 목록 필터링과 커스텀 이모지 지원으로 베타로 승격했으며, v0.2.4는 콘텐츠 경고 오버레이를 추가했습니다. v0.3.x 시리즈에서는 노트에 대한 [NIP-13](/ko/topics/nip-13/) proof-of-work, 영구 설정이 있는 백그라운드 PoW 마이닝, `.onion` relay 저장, 뮤트 스레드 알림이 도입되었습니다.

Google ML Kit을 통한 온디바이스 번역은 초기 모델 다운로드 후 네트워크 접근 없이 로컬에서 실행됩니다. 대화형 소셜 그래프 시각화는 약 30fps의 velocity Verlet 물리 시뮬레이션과 핀치-투-줌 내비게이션 및 프로필 검사를 사용합니다.

## 릴리스

### Vector v0.3.1

Marmot 암호화 메시징 앱 [Vector](https://github.com/VectorPrivacy/Vector)가 그룹 관리 개선과 성능 작업이 포함된 [v0.3.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.1)을 출시했습니다. 다중 관리자 그룹, 일괄 초대, npub으로 초대, 그룹 아바타가 협업 기능을 확장합니다. Android 백그라운드 알림은 이제 인라인 답장 및 읽음 표시 액션을 지원합니다.

[Negentropy](/ko/topics/negentropy/) 기반 결정론적 동기화는 오프라인 기간 동안 놓친 메시지를 포함한 전체 대화 기록을 검색합니다. 음성-텍스트 변환은 Android에서 GPU 가속으로 재구축되었습니다. 파일 첨부 처리가 다운로드 진행률, 재시도 상태, 디렉토리 압축 및 전송, 전반적 실시간 진행 표시기와 함께 전면 개편되었습니다. 부팅 시간, 이미지 처리, 오디오 재생, 전반적 UI 반응성에서 15배 이상의 성능 향상이 이루어졌습니다. 앱 설치 크기는 3분의 1 이상 줄었으며, 프런트엔드는 대략 절반으로 감소했습니다. 32비트 ARM Android 지원이 추가되었습니다.

### Alby Hub v1.21.5

Nostr Wallet Connect([NIP-47](/ko/topics/nip-47/)) 지원이 포함된 자체 보관 Lightning 노드 [Alby Hub](https://github.com/getAlby/hub)이 [v1.21.5](https://github.com/getAlby/hub/releases/tag/v1.21.5)를 출시했습니다. 기본 NWC 구성에 두 번째 relay가 추가되어 relay 재시작 시 안정성이 향상되었습니다. 거래 목록의 잘못된 zap 데이터 수정은 잘못된 형식의 [NIP-57](/ko/topics/nip-57/) (Lightning Zaps) event에 대한 표시 문제를 해결합니다. 새 앱 스토어 항목에는 Alby CLI와 LNVPS가 포함됩니다.

### nospeak v0.12.x

텍스트 기반 Nostr 메시징 클라이언트 [nospeak](https://github.com/psic4t/nospeak)이 해당 기간 동안 3개의 릴리스를 출시했습니다. [v0.12.0](https://github.com/psic4t/nospeak/releases/tag/v0.12.0)은 4자리 키패드 PIN 앱 잠금과 벵골어, 태국어, 베트남어, 힌디어, 아랍어, 히브리어, 우르두어, 터키어, 일본어, 중국어, 한국어, 네덜란드어, 폴란드어, 러시아어, 페르시아어를 포함한 15개 이상의 새 언어 번역과 RTL 지원을 추가했습니다. [v0.12.1](https://github.com/psic4t/nospeak/releases/tag/v0.12.1)은 순수 검정 배경과 시안 악센트의 Cypher 테마와 Android 동영상 포스터 생성을 도입했습니다. [v0.12.2](https://github.com/psic4t/nospeak/releases/tag/v0.12.2)는 채팅 내보내기와 연락처 메뉴의 프로필 보기를 추가했습니다.

### Citrine v2.0.0-pre2

greenart7c3의 Android 개인 relay [Citrine](https://github.com/greenart7c3/Citrine)이 새 데이터베이스 인덱스와 재구성된 Kotlin 코루틴을 통한 relay 성능 개선이 포함된 [v2.0.0-pre2](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre2)를 출시했습니다. 각 호스팅 웹 앱은 이제 자체 포트에서 시작됩니다. 전문 검색과 event 확장이 가능한 재설계된 event 화면이 변경 사항을 완성합니다.

### NoorNote v0.5.x

Nostr 기반 노트 작성 애플리케이션 [NoorNote](https://github.com/77elements/noornote)가 [v0.5.0](https://github.com/77elements/noornote/releases/tag/v0.5.0)부터 [v0.5.7](https://github.com/77elements/noornote/releases/tag/v0.5.7)까지 8개의 릴리스를 출시했습니다. v0.5.0의 Android 출시에는 [NIP-55](/ko/topics/nip-55/) Amber 서명자 지원과 [NIP-71](/ko/topics/nip-71/) (Video Events) 노트 게시가 추가되었습니다. v0.5.1의 재설계된 환영 페이지에는 공개 타임라인 미리보기가 포함되었으며 APK가 15 MB로 축소되었습니다. v0.5.2의 Relay Browser는 공유 가능한 URL을 통한 공개 relay 타임라인 탐색과 함께 미디어 다운로드 및 [NIP-30](/ko/topics/nip-30/) 커스텀 이모지 리액션을 지원합니다. v0.5.7까지의 후속 릴리스에서는 협업 "tribes" 노트 공유 시스템의 동기화 경합 조건이 해결되었습니다.

### NosCall v0.5.1

Nostr 음성 및 영상 통화 앱 [NosCall](https://github.com/sanah9/noscall)이 음성 메시지 지원, 그룹 입장이 포함된 최적화된 데스크톱 경험, 데스크톱 연락처 즐겨찾기, 연락처 메모 및 필터링, 데이터 내보내기 및 정리 옵션, 시스템 글꼴 크기 접근성 지원이 포함된 [v0.5.1](https://github.com/sanah9/noscall/releases/tag/v0.5.1-release)을 출시했습니다.

### Shosho v0.13.0

Nostr 라이브 스트리밍 앱 [Shosho](https://github.com/r0d8lsh0p/shosho-releases)가 스트림 카드 메뉴에서 MP4 리플레이 다운로드와 프로필용 [NIP-05](/ko/topics/nip-05/) (DNS-Based Verification)이 포함된 [v0.13.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.13.0)을 출시했습니다. RTMP 퍼블리셔가 Expo Modules API로 마이그레이션되었습니다. 저대역폭 연결에서의 스트리밍 성능이 향상되었으며, 구형 기기의 충돌과 iOS의 [Zap.Stream](https://zap.stream) 스트리밍 문제가 수정되었습니다.

### nostr-java v2.0.0

[nostr-java](https://github.com/tcheeric/nostr-java)가 구성 가능한 WebSocket 버퍼 크기를 포함한 [v2.0.0](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.0)을 출시하여, 애플리케이션이 잘림 없이 더 큰 Nostr event를 처리할 수 있게 되었습니다. 메이저 버전 범프는 연결 API의 호환성을 깨뜨리는 변경을 반영합니다.

### Prism 1.1.0

[Prism](https://github.com/hardran3/Prism)이 장문 콘텐츠 지원(kind 30023 문서)과 앱에서 직접 작성할 수 있는 Markdown 편집기가 포함된 [1.1.0](https://github.com/hardran3/Prism/releases/tag/1.1.0)을 출시했으며, [1.1.1](https://github.com/hardran3/Prism/releases/tag/1.1.1) 버그 수정 릴리스가 뒤따랐습니다.

### Angor v0.2.6

Bitcoin 크라우드펀딩 플랫폼 [Angor](https://github.com/block-core/angor)가 Boltz 통합과 1-클릭 투자 흐름이 포함된 [v0.2.6](https://github.com/block-core/angor/releases/tag/v0.2.6)을 출시했습니다. 투자와 펀드 프로젝트 유형 모두 testnet에서 종단 간 작동합니다. 팀은 UI가 대략 70% 완성되었다고 언급합니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-91: 필터용 AND 연산자](https://github.com/nostr-protocol/nips/pull/1365)**: relay 구독에서 태그 배열에 대한 AND 필터 의미론을 추가합니다. 현재 태그 필터에 여러 값을 지정하면(예: 여러 `p` 태그) 그 중 하나라도 포함하는 event와 일치합니다. NIP-91은 클라이언트가 지정된 모든 태그 값을 동시에 일치하는 event를 요구할 수 있게 하여, 대역폭을 줄이고 더 빠른 인덱스 작업을 가능하게 합니다. nostr-rs-relay, satellite-node, worker-relay, applesauce를 포함한 여러 relay 구현이 이미 존재합니다. 이전에는 NIP-119로 번호가 매겨졌습니다.

- **[NIP-30: 태그에 이모지 세트 주소](https://github.com/nostr-protocol/nips/pull/2247)**: [NIP-30](/ko/topics/nip-30/)의 커스텀 이모지 태그에 이제 선택적 이모지 세트 주소를 포함할 수 있습니다. 클라이언트에서 이모지를 클릭하면 해당 이모지가 속한 세트를 열어 북마크하거나 탐색할 수 있습니다. [Chachi](https://github.com/purrgrammer/chachi) 클라이언트에서 시작되었습니다.

- **[NIP-29: unallowpubkey 및 unbanpubkey 추가](https://github.com/nostr-protocol/nips/pull/2111)**: [NIP-29](/ko/topics/nip-29/) 그룹 채팅을 위한 두 가지 새 관리자 명령입니다. `unallowpubkey`는 pubkey를 차단하지 않고 허용 목록에서 제거합니다. `unbanpubkey`는 pubkey를 멤버 목록에 다시 추가하지 않고 차단을 해제합니다. 이전에는 허용 목록에서 제거하는 유일한 방법이 동시에 차단하는 것이었고, 차단 해제 시 사용자를 멤버로 다시 추가해야 했습니다.

**오픈 PR 및 논의:**

- **[NIP-A7: Spells](https://github.com/nostr-protocol/nips/pull/2244)** (2월 27일 제출): purrgrammer가 제안한 spells는 kind 777 event로 게시되는 이동 가능한 저장된 Nostr 쿼리입니다. spell은 구조화된 태그(`k`는 kind, `authors`는 pubkey, `tag`는 임의 태그 필터)로 REQ 또는 COUNT 필터를 인코딩하며 런타임 변수를 지원합니다: `$me`는 로그인한 사용자의 pubkey로 해석되고, `$contacts`는 사용자의 kind 3 팔로우 목록으로 확장됩니다. 상대 타임스탬프(`7d`, `2w`, `1mo`)로 하드코딩된 날짜 없이 롤링 시간 윈도우를 정의할 수 있습니다. [nak](https://github.com/fiatjaf/nak)과 [Grimoire](https://github.com/purrgrammer/grimoire)에서 이미 구현되어 있으며, spells로 사용자는 클라이언트 간에 이동하는 큐레이션된 피드를 생성, 공유, 구독할 수 있습니다.

- **[NIP-59: 임시 Gift Wrap (kind 21059)](https://github.com/nostr-protocol/nips/pull/2245)** (2월 27일 제출): [NIP-59](/ko/topics/nip-59/) gift wrap의 임시 변형을 추가합니다. Kind 21059는 NIP-01 임시 의미론을 따르므로, relay가 전달 후 event를 폐기합니다. 메시지 지속성이 불필요한 MCP 전송을 위해 ContextVM이 제안했습니다.

- **[ContextVM: Nostr를 통한 MCP JSON-RPC](https://github.com/nostr-protocol/nips/pull/2246)** (2월 27일 제출): 주소 지정 및 상관 관계를 위한 `p`와 `e` 태그가 있는 임시 kind 25910 event를 사용하여 Nostr를 통해 Model Context Protocol 메시지를 전송하는 방법을 명시합니다. 의도적으로 간결하며, 프로토콜 세부 사항은 [ContextVM 사양](https://docs.contextvm.org)에 위임합니다.

- **[NIP-29: 오디오/비디오 라이브 스페이스](https://github.com/nostr-protocol/nips/pull/2238)** (2월 25일 제출, 초안): fiatjaf의 초안으로 [NIP-29](/ko/topics/nip-29/) 그룹에 라이브 오디오 및 비디오를 확장합니다. 그룹 메타데이터 event에 선택적 `livekit`과 `no-text` 태그를 추가합니다. 사용자가 음성 스페이스에 참여하려면, 클라이언트가 relay의 `/.well-known/nip29/livekit/{groupId}`에서 JWT를 요청합니다. relay는 그룹 멤버십을 확인하고 사용자의 16진수 pubkey를 `sub` 클레임으로 토큰을 발급하며, 이를 [LiveKit](https://livekit.io/)에 전달하여 미디어 전송을 처리합니다. 음성 방 접근은 그룹의 기존 권한 모델을 상속하므로, relay 측 멤버십 규칙이 누가 말할 수 있는지를 결정합니다. Pyramid과 Chachi에서 테스트 중입니다.

- **[협업 Event 소유권](https://github.com/nostr-protocol/nips/pull/2235)** (2월 24일 제출): pablof7z가 `p` 태그에 공동 소유자 pubkey를 나열하고 `k` 태그에 대상 event kind를 포함하는 포인터 event(kind 39382)를 제안합니다. 나열된 모든 소유자는 동일한 `d` 태그로 해당 kind의 event를 게시할 수 있으며, 클라이언트는 모든 소유자를 쿼리하고 가장 최근 event를 취하여 현재 상태를 해석합니다. 공저 귀속은 검증 가능한 `a` 태그가 포인터를 역참조하고 저자가 `p` 태그에 나타날 때만 표시되어, 위조된 주장을 방지합니다. 이를 통해 단일 키페어에 제어권을 할당하지 않고도 공유 위키 페이지와 공동 작성 리소스가 가능합니다.

- **[NIP-09: 리포스트의 연쇄 삭제](https://github.com/nostr-protocol/nips/pull/2234)** (2월 24일 제출): 원저자가 노트를 삭제할 때, relay는 이를 참조하는 kind 6 또는 kind 16 리포스트도 삭제해야 합니다. 리포스트가 저자가 원본을 삭제한 후에도 실수로 유출된 정보를 보존할 수 있다는 프라이버시 우려에 의해 동기 부여되었습니다. 이 변경은 relay 측만 해당되며, 클라이언트 수정이 필요하지 않습니다.

- **[NIP-07: peekPublicKey](https://github.com/nostr-protocol/nips/pull/2233)** (2월 23일 제출): [NIP-07](/ko/topics/nip-07/) 브라우저 확장에 `peekPublicKey()` 메서드를 추가합니다. `getPublicKey()`와 달리 사용자 확인 프롬프트 없이 현재 pubkey를 반환하여, 사용자가 자동 로그인을 활성화했을 때 무음 자동 로그인을 가능하게 합니다.

- **[NIP-BB: Book](https://github.com/nostr-protocol/nips/pull/2248)** (2월 28일 제출, 초안): Nostr에서 구조화된 도서 출판을 위한 4개의 주소 지정 가능 event kind(30300-30303)를 정의합니다. Cover event는 제목, 표지 이미지, [NIP-32](/ko/topics/nip-32/) (Labeling) 레이블을 통한 라이선스, 언어 코드를 포함하는 루트 메타데이터를 보유합니다. Index event는 base62 분수 인덱싱을 사용하여 각 챕터를 위치에 매핑하며, 저자가 번호를 다시 매기지 않고 기존 챕터 사이에 새 챕터를 삽입할 수 있습니다. Chapter event는 선택적 이미지가 있는 구조적 헤더로 작동하고, Episode event는 위치 지정 이미지 태그와 함께 최대 30,000자의 실제 산문을 담습니다. 리뷰는 Zap 설명을 리뷰 텍스트로 사용하여 Cover event에 대한 Zap으로 이루어집니다.

- **[NIP-54: Asciidoc에서 Djot으로 전환](https://github.com/nostr-protocol/nips/pull/2242)** (2월 26일 제출): 12월의 [d-tag 국제화 수정](/ko/newsletters/2025-12-31-newsletter/)에 이어, 이 PR은 [NIP-54](/ko/topics/nip-54/) 위키의 Asciidoc 마크업 형식을 [Djot](https://djot.net/)으로 대체하고 비라틴 문자를 위한 근거 섹션과 위키링크 예제를 추가할 것을 제안합니다.

- **[NIP-66: 방어 조치](https://github.com/nostr-protocol/nips/pull/2240)** (2월 26일 제출): [nostrability/outbox](#outbox-모델-분석) 벤치마크에서 얻은 교훈을 바탕으로, [NIP-66](/ko/topics/nip-66/) 엣지 케이스에 대한 명시적 안내를 추가합니다. 동반 [PR #2241](https://github.com/nostr-protocol/nips/pull/2241)은 SSL, 지리적 위치, 네트워크, 연결성 검사를 위한 출력 태그를 정의합니다.

- **NIP-C1: 암호화 신원 증명** (위키 항목, kind 30817): APK 서명 인증서를 Nostr 프로필에 암호화적으로 연결하는 kind 30509 event를 제안합니다. 증명은 인증서의 개인 키(ECDSA, RSA PKCS1v15, Ed25519 및 기타 표준 알고리즘 지원)로 Nostr pubkey를 포함하는 정규 메시지에 서명한 다음, Nostr 키로 서명된 kind 30509 event에 서명을 게시하는 방식으로 작동합니다. 검증자는 앱의 Android 서명 인증서를 제어하는 사람이 게시를 주장하는 Nostr pubkey도 제어하는지 확인할 수 있습니다. 증명은 기본적으로 1년 후 만료되며 명시적으로 취소할 수 있습니다. [Zapstore](https://github.com/zapstore/zapstore) 도구 체인에서 구현되었습니다.

- **NIP-31402: SARA 수익 공유 오퍼링 레지스트리** (위키 항목, kind 30817): Nostr relay에 Simple Autonomous Revenue Agreement (SARA) 오퍼링을 게시하기 위한 kind 31402 주소 지정 가능 event를 정의합니다. 발행자는 풀 지분 백분율, 지급 트리거, sats 기준 임계값, 기간 길이, 단계별 가격 책정을 포함하는 Lightning 정산 수익 공유 조건을 알립니다. 에이전트와 인간은 중앙 플랫폼 없이 relay 전반에서 오퍼링을 발견하고 자율적으로 구독할 수 있습니다. kind 번호는 SARA가 L402 결제 관계의 반환 구간을 나타내므로 kind 30402(같은 저자가 동반 위키 항목으로 게시한 L402 Service Registry)를 반영합니다.

## 오픈 PR 및 프로젝트 업데이트

### Damus: [NIP-89](/ko/topics/nip-89/) (Recommended Application Handlers)

[PR #3337](https://github.com/damus-io/damus/pull/3337)은 [Damus](https://github.com/damus-io/damus)에 NIP-89 클라이언트 태그 지원을 구현합니다. 앱은 이제 모든 게시 경로(메인 앱, 공유 확장, 하이라이터, 초안)에서 클라이언트 태그를 발행하며, 다른 앱이 태그를 포함할 때 타임스탬프 옆에 "via ClientName"을 표시합니다. 외관 설정의 프라이버시 토글로 태그 발행을 비활성화할 수 있습니다. [PR #3652](https://github.com/damus-io/damus/pull/3652)는 설정에 NostrDB와 Kingfisher 캐시 디스크 사용량을 내보내기 지원과 함께 대화형 파이 차트로 분류하는 저장 공간 섹션을 추가합니다.

오픈: [PR #3657](https://github.com/damus-io/damus/pull/3657)는 인용된 노트에 대한 [NIP-65](/ko/topics/nip-65/) relay 대체를 추가합니다. 인라인 `nevent`에 저자 pubkey가 포함되어 있지만 relay 힌트가 없고 사용자 풀에서 노트가 누락된 경우, Damus는 저자의 kind 10002 relay 목록을 가져와 쓰기 relay에서 다시 시도합니다.

### Amethyst: [NIP-39](/ko/topics/nip-39/) (External Identities), NIP-C0, [NIP-66](/ko/topics/nip-66/)

[Amethyst](https://github.com/vitorpamplona/amethyst)가 28개의 PR에 걸쳐 대규모 NIP 구현을 병합했습니다. 외부 신원 주장이 이제 [NIP-39](/ko/topics/nip-39/)에 따라 전용 kind 10011 event로 게시되며([PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747)), 역호환 대체와 함께 소셜 신원을 kind 0 메타데이터에서 분리합니다. NIP-C0을 통한 코드 스니펫 지원([PR #1744](https://github.com/vitorpamplona/amethyst/pull/1744))은 언어, 확장자, 런타임, 라이선스, 의존성에 대한 접근자가 있는 kind 1337 event를 추가합니다. [NIP-66](/ko/topics/nip-66/) relay 모니터링 구현([PR #1742](https://github.com/vitorpamplona/amethyst/pull/1742))은 RTT 메트릭, 네트워크 유형, 지원되는 NIP, geohash에 대한 전체 태그 파싱을 포함하는 두 event kind를 모두 다룹니다.

Amethyst Desktop에 암호화 DM이 도착했으며([PR #1710](https://github.com/vitorpamplona/amethyst/pull/1710)), [NIP-04](/ko/topics/nip-04/) (Encrypted Direct Messages)와 [NIP-17](/ko/topics/nip-17/) (Private Direct Messages)를 모두 지원하는 분할 창 채팅 레이아웃이 제공됩니다. 새로운 relay 피드 화면([PR #1733](https://github.com/vitorpamplona/amethyst/pull/1733))은 팔로우/언팔로우 기능과 함께 특정 relay의 게시물을 탐색할 수 있게 합니다. 오픈: 검열 저항 NIP-05 검증([PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734))은 HTTP DNS 대신 Namecoin 블록체인을 대상으로 해석하는 `.bit` 식별자에 대한 병렬 검증 경로를 추가합니다. Amethyst가 NIP-05 필드에서 `.bit` 접미사를 감지하면, ElectrumX-NMC 서버에서 이름의 거래 내역을 쿼리하고, 최신 출력에서 `NAME_UPDATE` 스크립트를 파싱하여 Nostr pubkey를 추출하며, 36,000 블록(Namecoin의 만료 기간)보다 오래된 이름은 거부합니다. ElectrumX 연결은 Tor가 활성화되면 SOCKS5를 통해 라우팅되며, clearnet과 `.onion` 엔드포인트 간 동적 서버 선택이 이루어집니다. 1시간 TTL의 LRU 캐시가 반복적인 블록체인 쿼리를 방지합니다.

### Notedeck: Outbox 아키텍처

[PR #1303](https://github.com/damus-io/notedeck/pull/1303)은 [Notedeck](https://github.com/damus-io/notedeck)을 임시 relay 풀 관리에서 계정 범위 구독을 가진 중앙화된 outbox 모델로 마이그레이션합니다. Messages 모듈은 이제 기본 DM relay 목록이 없으면 이를 게시하고 kind 10050에 따라 수신자가 선호하는 relay로 DM을 라우팅합니다.

### Pika: 그룹별 프로필 및 튜토리얼 피드

iOS, Android, 데스크톱 빌드를 제공하는 Marmot 암호화 메시징 앱 [Pika](https://github.com/sledtools/pika)에 그룹별 프로필([PR #368](https://github.com/sledtools/pika/pull/368))이 추가되었습니다. 사용자는 이제 각 그룹 채팅에 대해 별도의 표시 이름, 사진, 커스텀 자기소개를 설정할 수 있습니다. 이 프로필은 Marmot 그룹 내부에서 암호화된 kind 0 event로 게시되어, 그룹 외부의 누구에게도 보이지 않으며, 그룹별 프로필이 설정되지 않은 경우 사용자의 글로벌 Nostr 프로필로 대체됩니다. 새 멤버가 가입하면 관리자가 모든 저장된 그룹 프로필을 재방송하고 각 멤버가 커밋 시 자신의 프로필을 재게시합니다. 프로필 사진은 Blossom 업로드 전에 Marmot 미디어 암호화됩니다. 이 PR에는 16개의 새 단위 테스트가 포함되며, CLI 명령(`update-group-profile`)과 UI를 통해 기능이 노출됩니다.

새로운 `pika-news` 웹 앱([PR #401](https://github.com/sledtools/pika/pull/401))은 Pika의 자체 GitHub PR을 모니터링하고 PR diff에서 단계별 튜토리얼 안내를 자동 생성하여, [NIP-07](/ko/topics/nip-07/) 인증이 포함된 서버 렌더링 페이지로 게시합니다. 사용자는 Nostr 인증 채팅을 통해 특정 튜토리얼에 대해 실시간으로 토론할 수 있습니다.

### diVine: 임베더블 위젯 및 비디오 답글

Nostr 네이티브 동영상 공유 플랫폼 [diVine](https://github.com/divinevideo/divine-mobile)이 10일 동안 132개의 PR을 병합했습니다. 임베더블 iframe 위젯([PR #1843](https://github.com/divinevideo/divine-mobile/pull/1843))은 사용자의 프로필과 최신 동영상을 렌더링하는 독립적인 `/embed?npub=...` 페이지를 제공합니다. 기능 플래그 뒤에 위치한 비디오 답글 기능([PR #1915](https://github.com/divinevideo/divine-mobile/pull/1915))은 [NIP-92](/ko/topics/nip-92/) (Media Attachments) imeta 메타데이터와 함께 Kind 1111 댓글([NIP-22](/ko/topics/nip-22/))을 사용합니다. Bluesky에서 영감을 받은 3방향 콘텐츠 필터([PR #1797](https://github.com/divinevideo/divine-mobile/pull/1797))는 17개 [NIP-32](/ko/topics/nip-32/) 콘텐츠 경고 카테고리에 걸쳐 표시/경고/숨기기 제어를 제공합니다.

### strfry: REQ 필터 검증

[PR #163](https://github.com/hoytech/strfry/pull/163)은 C++ Nostr relay [strfry](https://github.com/hoytech/strfry)에 구성 가능한 REQ 필터 검증을 추가합니다. 운영자는 REQ당 최대 필터 수, 필수 저자 또는 태그 존재, 허용 kind 화이트리스트, 필터당 kind 제한을 설정할 수 있습니다. 이 기능은 엄격한 필터 적용이 필요한 NWC relay 배포를 대상으로 합니다. 오픈: [PR #173](https://github.com/hoytech/strfry/pull/173)은 수집 시 event 페이로드에 대한 선택적 zstd 압축을 추가합니다.

### rust-nostr: [NIP-62](/ko/topics/nip-62/) Request to Vanish

Rust Nostr 프로토콜 라이브러리 [rust-nostr](https://github.com/rust-nostr/nostr)가 세 가지 데이터베이스 백엔드 전반에 [NIP-62](/ko/topics/nip-62/) (Request to Vanish) 지원을 추가했습니다: [LMDB](https://github.com/rust-nostr/nostr/pull/1268), [SQLite](https://github.com/rust-nostr/nostr/pull/1270), [인메모리](https://github.com/rust-nostr/nostr/pull/1272). LMDB 구현에는 배포별로 [NIP-09](/ko/topics/nip-09/)와 NIP-62 적용을 활성화 또는 비활성화할 수 있는 구성 가능 옵션이 포함됩니다.

### NDK: 협업 Event 및 NIP-46 타임아웃

JavaScript/TypeScript용 Nostr Development Kit [NDK](https://github.com/nostr-dev-kit/ndk)가 인가된 저자를 정의하는 주소 지정 가능 포인터 event(kind 39382)를 사용하는 다중 저자 협업 문서를 위한 `NDKCollaborativeEvent`를 도입하는 [PR #380](https://github.com/nostr-dev-kit/ndk/pull/380)을 병합했습니다. `NDKNip46Signer`에 대한 구성 가능한 타임아웃([PR #381](https://github.com/nostr-dev-kit/ndk/pull/381))은 bunker가 응답하지 않을 때 [NIP-46](/ko/topics/nip-46/) 원격 서명 작업이 무한정 중단되는 것을 방지합니다.

### TENEX: 에이전트 분류 및 Pubkey 게이팅

Nostr 네이티브 AI 에이전트 오케스트레이션 플랫폼 [TENEX](https://github.com/tenex-chat/tenex)가 보안 관련 2개의 PR을 병합했습니다. TIP-01 역할 기반 에이전트 분류([PR #91](https://github.com/tenex-chat/tenex/pull/91))는 에이전트 카테고리(principal, orchestrator, worker, advisor, auditor)를 거부 도구 맵을 통한 자동화된 도구 제한에 매핑합니다. 프론트 도어 pubkey 게이팅([PR #87](https://github.com/tenex-chat/tenex/pull/87))은 화이트리스트 또는 백엔드 서명된 pubkey의 event만 알려진 에이전트와 함께 라우팅되도록 보장하며, 알 수 없는 pubkey는 감사를 위한 OpenTelemetry 스팬과 함께 자동으로 삭제됩니다.

### Zap Cooking: 멤버십 대시보드

Nostr 기반 레시피 공유 플랫폼 [Zap Cooking](https://github.com/zapcooking/frontend)이 10일 동안 25개의 PR과 85개의 커밋을 병합했습니다. 멤버십 대시보드([PR #228](https://github.com/zapcooking/frontend/pull/228))는 만료일과 관리/업그레이드 옵션이 있는 구독 상태를 표시하고, 클라이언트 측 및 서버 측 검사와 함께 Sous Chef와 Zappy 등급에 대한 기능 게이트를 다시 활성화하며, 26개 파일에 걸쳐 등급 명명을 표준화합니다. 2단계 그룹 메시지 로딩([PR #227](https://github.com/zapcooking/frontend/pull/227))은 즉시 표시를 위한 빠른 3일 초기 가져오기와 백그라운드 40일 백필을 제공합니다.

지갑 니모닉 저장이 pubkey 파생 암호화에서 [NIP-44](/ko/topics/nip-44/) 자기 암호화로 이동했으며([PR #224](https://github.com/zapcooking/frontend/pull/224)), 이전 방식이 `SHA-256(pubkey)`에서 키를 파생하여 pubkey가 공개이므로 사실상 비암호화된 취약점을 수정합니다. 기존 지갑은 첫 로드 시 자동으로 마이그레이션됩니다. [NIP-29](/ko/topics/nip-29/) 그룹 채팅에 빨간 점 뱃지의 읽지 않음 표시기와 kind 9009 초대 코드로 초대 전용 접근이 추가되었습니다([PR #213](https://github.com/zapcooking/frontend/pull/213)). 링크 미리보기와 Nostr event 임베드가 이제 DM과 그룹 메시지에서 렌더링됩니다([PR #218](https://github.com/zapcooking/frontend/pull/218)). 설정의 Nostr 백업 섹션([PR #210](https://github.com/zapcooking/frontend/pull/210))은 순환 3슬롯 버전 관리와 함께 [NIP-78](/ko/topics/nip-78/) (Application-specific Data) 암호화 저장소를 통해 팔로우 및 뮤트 목록을 저장합니다. 알림 서비스 지연, IntersectionObserver를 통한 지연 DOM 렌더링(200 event 피드에서 DOM 노드를 ~15,000개에서 ~3,000개로 감소), 확장된 outbox 캐시 TTL을 통해 시작 성능이 향상되었습니다([PR #208](https://github.com/zapcooking/frontend/pull/208)). 사용자 정의 가능한 인쇄 레시피 모달([PR #205](https://github.com/zapcooking/frontend/pull/205))은 실시간 미리보기와 함께 포함할 섹션을 토글할 수 있게 합니다. [Branta SDK](https://github.com/BrantaOps/branta-core) 통합([PR #222](https://github.com/zapcooking/frontend/pull/222))은 POST 및 GET 요청에 대한 검증 가드레일을 추가합니다.

### Keep: Rust 기반 상태 마이그레이션

Android용 Nostr 기반 개인 키 관리자 [Keep](https://github.com/privkeyio/keep-android)이 4개의 Kotlin 구성 저장소를 삭제하고 keep-mobile 레이어의 Rust 기반 공유 상태로 대체하는 [PR #178](https://github.com/privkeyio/keep-android/pull/178)을 병합했습니다. 10초 폴링 루프가 Rust의 푸시 기반 `KeepStateCallback`으로 대체되었습니다. [PR #179](https://github.com/privkeyio/keep-android/pull/179)는 암호 보호가 포함된 암호화 백업 및 복원을 추가합니다.

### Mostro Mobile: 분쟁 채팅 암호화

Mostro P2P Bitcoin 거래 플랫폼의 모바일 클라이언트 [Mostro Mobile](https://github.com/MostroP2P/mobile)이 분쟁 채팅 암호화의 2단계 마이그레이션을 출시했습니다. 첫 번째 단계([PR #495](https://github.com/MostroP2P/mobile/pull/495))는 mostro 전용 래핑에서 관리자의 pubkey에서 파생된 공유 키 암호화로 전환합니다. 이를 기반으로 [PR #501](https://github.com/MostroP2P/mobile/pull/501)은 `NostrEvent`로 메시지 모델을 통합하고 gift wrap event를 디스크에 암호화 저장하여, P2P 채팅 패턴과 일관성을 유지합니다. BIP-340 서명 수정([PR #496](https://github.com/MostroP2P/mobile/pull/496))은 bip340 의존성을 0.2.0으로 오버라이드하여, 1-2%의 Schnorr 서명이 무효화되고 공개 키가 `0x00`으로 시작하는 키에 대해 100% 실패를 유발하는 `bigToBytes()` 패딩 버그를 해결합니다. Order Details는 이제 영어, 스페인어, 이탈리아어, 프랑스어로 현지화된 사람이 읽을 수 있는 상태 레이블을 원시 프로토콜 값 대신 표시합니다([PR #502](https://github.com/MostroP2P/mobile/pull/502)). HalCash가 추가되고 SEPA가 결제 방법에서 제거되었습니다([PR #493](https://github.com/MostroP2P/mobile/pull/493)). SEPA 이체가 24시간을 초과할 수 있기 때문입니다(SEPA Instant는 유지).

서버 측에서는 [Mostro](https://github.com/MostroP2P/mostro)가 개시자 필드를 포함하도록 분쟁 세션 복원을 수정했으며([PR #599](https://github.com/MostroP2P/mostro/pull/599)), 판매자가 자금을 해제하면 활성 분쟁을 자동으로 닫아 관리자 클라이언트가 해결을 확인할 수 있도록 결제된 Nostr event를 게시합니다([PR #606](https://github.com/MostroP2P/mostro/pull/606)).

## Nostr 2월의 5년

[지난 달 뉴스레터](/ko/newsletters/2026-01-28-newsletter/#nostr-1월의-5년)는 초기 개발부터 Damus 폭발, 2026년 보안 인프라까지 Nostr의 1월 이정표를 추적했습니다. 이번 회고는 2021년부터 2026년까지 각 2월에 일어난 일을 다룹니다.

### 2021년 2월: 재작성

존재한 지 3개월 된 Nostr의 2월은 프로토콜의 가장 중요한 초기 변경을 만들어냈습니다. 2월 14-15일, fiatjaf가 [NIP-01을 재작성](https://github.com/nostr-protocol/nostr/commit/33a1a70)하여 원래의 메시지 형식을 현재까지 프로토콜이 사용하는 EVENT/REQ/CLOSE 모델로 대체했습니다. 이 재작성 전에는 클라이언트와 relay가 더 단순한 구조를 통해 통신했습니다. event 게시(EVENT)와 구독 관리(REQ/CLOSE)를 분리하면서 확장에 필수적인 relay 측 필터링이 가능해졌습니다.

[NIP-04](/ko/topics/nip-04/)도 같은 달에 등장하여, secp256k1을 통한 Diffie-Hellman 키 교환에서 파생된 공유 비밀을 사용한 암호화 다이렉트 메시지를 추가했습니다. 암호화는 기본적(AES-256-CBC)이었으며 나중에 [NIP-44](/ko/topics/nip-44/)의 감사된 암호화로 대체되었지만, 소수의 초기 사용자에게 프로토콜 위의 첫 개인 통신 채널을 제공했습니다.

도구가 [noscl](https://github.com/fiatjaf/noscl)(터미널 기반 relay 상호작용을 위한 Go 커맨드라인 클라이언트)로 확장되었고, futurepaul이 초기 Rust 구현인 [nostr-rs](https://github.com/futurepaul/nostr-rs)를 시작했습니다. 전체 네트워크는 2~3개의 relay에서 운영되었고, [텔레그램 그룹](https://t.me/nostr_protocol)을 통해 조율되었으며, 약 7명의 활동적인 기여자가 있었습니다.

### 2022년 2월: 모멘텀 구축

2021년 12월 31일의 [Hacker News 게시물](https://news.ycombinator.com/item?id=29749061)이 계속해서 개발자를 2월까지 끌어들였습니다. [nostr-protocol/nostr](https://github.com/nostr-protocol/nostr) 저장소(공식 [NIPs 저장소](https://github.com/nostr-protocol/nips)는 2022년 5월까지 존재하지 않았음)는 2월에 vinliao의 NIP-13 (Proof of Work), fiatjaf의 NIP-14 (Reputation), Cameri의 NIP-15 (Resource Relations), melvincarvalho의 [NIP-17](https://github.com/nostr-protocol/nostr/pull/75) (Git Updates Over Nostr)을 포함한 6개의 pull request를 받았습니다. NIP 번호는 나중에 Private Direct Messages로 재할당되었으며, Nostr에서의 git 협업은 [gitworkshop.dev](https://gitworkshop.dev)로 발전하는 것을 통해 별도로 계속되었습니다.

Greg Heartsfield의 [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay)가 그 달의 주역으로 34개의 커밋과 3개의 릴리스를 기록했습니다. 2월 12일 버전 0.5.0은 [NIP-05](/ko/topics/nip-05/) 검증 사용자 게시 제한을 추가했습니다. 버전 0.5.1과 0.5.2가 이후 2주에 걸쳐 뒤따랐으며, 이 relay가 단독으로 네트워크 트래픽의 대부분을 처리했습니다.

Robert C. Martin(Uncle Bob)은 Clojure 데스크톱 클라이언트 [more-speech](https://github.com/unclebob/more-speech)를 구축하며 1월 18일부터 2월 말까지 69개의 커밋을 기록했습니다. 그의 참여는 더 넓은 소프트웨어 엔지니어링 커뮤니티의 관심을 끌었습니다. fiatjaf의 [nos2x](https://github.com/fiatjaf/nos2x) 브라우저 확장이 2월에 [NIP-04](/ko/topics/nip-04/) 복호화 지원과 relay 선호 정책을 출시하여, 웹 클라이언트가 키 위임에 여전히 사용하는 `window.nostr` 인터페이스([NIP-07](/ko/topics/nip-07/))를 구현했습니다.

여전히 주요 웹 클라이언트였던 [Branle](https://github.com/fiatjaf/branle)이 2월 13일에 `web+nostr` 프로토콜 핸들러 등록을 추가하여, Nostr 애플리케이션 간 딥 링킹의 초기 시도를 보여주었습니다. [nostr-tools](https://github.com/nbd-wtf/nostr-tools)는 NIP-05 검증을 강화했습니다. [go-nostr](https://github.com/nbd-wtf/go-nostr)는 11개 커밋에 걸쳐 NIP-04 암호화 DM 지원과 NIP-12 (Generic Tag Queries) 파싱을 추가했습니다. 네트워크는 대략 7-15개의 relay에서 운영되었으며, 활동적인 사용자 기반은 수백 명 수준이었을 것으로 추정됩니다. Damus와 Nostream은 아직 존재하지 않았으며 2022년 4월까지 등장하지 않았습니다.

### 2023년 2월: 국제적 관심

2023년 2월은 Nostr에 가장 큰 대중적 관심을 가져왔습니다. William Casarin의 iOS 클라이언트 [Damus](https://github.com/damus-io/damus)가 반복된 거절 후 [1월 31일 Apple App Store에 승인](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store)되었습니다. 2월 1일까지 미국 소셜 네트워킹 부문 10위에 올랐습니다. 이틀 후인 2월 2일, 보도에 따르면 중국 사이버공간관리국의 요청으로 [Apple이 중국 App Store에서 Damus를 삭제](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/)했습니다.

TechCrunch와 CoinDesk를 포함한 주요 매체가 삭제를 보도하면서 앱과 프로토콜 모두에 대한 인식을 증폭시켰습니다. nostr.directory의 메타데이터가 있는 고유 공개 키는 2월 3일까지 300,000개를 넘었습니다. 모든 relay는 자비를 들여 운영하는 열성적인 이들이 운영했으며, 인프라는 부하를 처리하기 위해 분주했습니다. 2월 초까지 약 289개의 relay가 추적되었으며, 이 수치는 계속 증가했습니다.

[NIPs 저장소](https://github.com/nostr-protocol/nips)는 그 달에 29개의 병합된 pull request를 기록하여, 프로토콜 역사상 최고의 월간 수치를 달성했습니다. [NIP-57](https://github.com/nostr-protocol/nips/pull/224) (Lightning Zaps)과 [NIP-23](https://github.com/nostr-protocol/nips/pull/220) (Long-form Content)이 모두 2월 13일에 병합되어, 하루 만에 Bitcoin 소액 결제를 추가하고 Nostr를 짧은 게시물 너머로 확장했습니다. [NIP-65](/ko/topics/nip-65/) (Relay List Metadata)는 1주일 전인 2월 7일에 병합되어 이후의 outbox 모델을 가능하게 했습니다. [NIP-46](/ko/topics/nip-46/) (Nostr Connect)과 [NIP-58](/ko/topics/nip-58/) (Badges)도 월말 전에 도입되었습니다.

Human Rights Foundation이 2월 21일 [Nostr와 Damus 개발을 위해 William Casarin에게 $50,000를 지원](https://hrf.org/devfund2023q1)했으며, 이는 Nostr 프로젝트에 대한 최초의 기관 지원금 중 하나였습니다. OpenSats는 아직 Nostr 펀드를 시작하지 않았습니다(이는 [2023년 7월](https://opensats.org/blog/nostr-grants-july-2023)에 이루어졌습니다).

### 2024년 2월: 프로토콜 내구성

2024년 2월은 성장에서 프로토콜 내구성으로 초점이 전환되었습니다. 전년도 7월부터 열려 있던 [NIP-17](/ko/topics/nip-17/) (Private Direct Messages)은 [NIP-44](/ko/topics/nip-44/)의 감사된 암호화와 [NIP-59](/ko/topics/nip-59/) gift wrapping을 사용하여 노후화된 [NIP-04](/ko/topics/nip-04/) 암호화를 대체하기 위해 작업 중이었습니다. NIP-04는 relay 운영자에게 메타데이터를 노출하여, 발신자-수신자 쌍을 볼 수 있었습니다. NIP-17은 일회용 키페어 뒤에 발신자 신원을 숨기며, 3월의 마지막 검토 라운드 후 봄에 병합되었습니다.

[NIP-29](/ko/topics/nip-29/) (Simple Groups)가 수개월의 논의 끝에 [2월 28일 병합](https://github.com/nostr-protocol/nips/pull/566)되어, relay가 관리자 역할과 접근 제어가 있는 모더레이션된 그룹 채팅을 호스팅하는 방법을 정의했습니다. [NIP-92](/ko/topics/nip-92/) (imeta 태그)가 2월 1일 병합되어, 클라이언트가 미디어 event에 이미지 크기와 blurhash 미리보기를 첨부하는 방법을 표준화했습니다.

2월 16일, NIPs 저장소에 프로토콜 사양의 하위 호환성을 깨뜨리는 변경을 추적하는 파일 [BREAKING.md](https://github.com/nostr-protocol/nips/commit/62c48eff)가 추가되었습니다. 이 파일의 생성은 Nostr가 호환성을 깨뜨리는 변경에 공식 문서가 필요한 성숙도 수준에 도달했음을 인정했습니다.

그 달 22개의 pull request가 병합되었습니다. [npub.cash](https://github.com/cashubtc/npubcash-server)가 서버 운영 없이 모든 npub이 결제를 받을 수 있는 Lightning 주소 서비스로 출시되었습니다. 2월 8일에 발표된 [학술 논문](https://arxiv.org/abs/2402.05709)은 무료 relay의 95%가 기부로 운영 비용을 충당할 수 없으며, 유료 relay의 35%가 1,000 sats(당시 약 $0.45) 미만의 입장료를 부과하고 있다고 밝혔습니다.

### 2025년 2월: 인프라 성장

2025년 2월은 NIPs 저장소에 28개의 병합된 pull request를 기록했습니다. [삭제권](/ko/topics/nip-62/) NIP이 2월 19일 병합되어, 데이터 이동성과 사용자 제어에 관한 규제 질문에 대응하여 사용자가 relay에 자신의 데이터 삭제를 요청하는 방법을 정의했습니다.

[NIP-60](/ko/topics/nip-60/) (Cashu Wallet)과 NIP-61 (Nutzaps)이 단순화 업데이트를 받아 ecash 토큰 저장 형식을 간소화했습니다. q-tag(인용 태그) 도입이 여러 NIP에 걸쳐 계속되어, event가 인용과 스레딩을 위해 다른 event를 참조하는 방법을 표준화했습니다.

클라이언트 릴리스는 꾸준한 진전을 보여주었습니다. [Notedeck](https://github.com/damus-io/notedeck) v0.3.0 알파가 1월 마지막 날 출시되었으며, 채택이 2월까지 계속되었습니다. Primal v2.1이 2월 7일에, Go relay 구현 [GRAIN](https://github.com/0ceanSlim/grain) v0.3.0이 2월 21일에 릴리스되었습니다.

NOSTRLDN v5가 런던 Nostr 커뮤니티를 다섯 번째 밋업으로 모았습니다. DVMCP 브리지가 Nostr의 Data Vending Machines([NIP-90](/ko/topics/nip-90/))를 Model Context Protocol과 연결하여, 다음 달에 도착할 AI 에이전트 통합 작업을 예고했습니다.

### 2026년 2월: 소셜 미디어를 넘어

*2026년 2월 활동은 Nostr Compass 호 [#8](/ko/newsletters/2026-02-04-newsletter/)부터 [#11](/ko/newsletters/2026-02-25-newsletter/)에서 가져왔습니다.*

2026년 2월은 단일 Nostr 월 중 가장 광범위한 애플리케이션 레이어 개발을 보여주었습니다. [Mostro](https://github.com/MostroP2P/mostro)가 탈중앙화 P2P Bitcoin 거래를 위한 [첫 공개 베타](/ko/newsletters/2026-02-11-newsletter/#mostro-첫-공개-베타-출시)를 출시했고, [Zapstore](https://github.com/zapstore/zapstore)가 수개월의 릴리스 후보 테스트 후 [1.0 안정 버전](/ko/newsletters/2026-02-11-newsletter/#zapstore-v100)에 도달했습니다. [White Noise v0.3.0](/ko/newsletters/2026-02-25-newsletter/#white-noise-v030)이 Amber 서명자 지원과 160개 이상의 병합된 개선 사항과 함께 실시간 [Marmot](/ko/topics/mls/) 암호화 메시징을 제공했습니다.

pablof7z의 경쟁 AI 에이전트 제안(에이전트 워크플로를 위한 NIP-AE, MCP 서버 공지를 위한 NIP-AD)과 joelklabo의 AI Agent Messages가 [NIP-90](/ko/topics/nip-90/)을 확장하는 [DVM Agent Coordination 제안](/ko/newsletters/2026-02-25-newsletter/#nip-업데이트)과 함께 등장했습니다. [ContextVM](/ko/newsletters/2026-02-25-newsletter/#contextvm-nostr를-통한-mcp)이 Model Context Protocol을 Nostr 전송에 연결하는 SDK 개선을 출시했습니다. [Burrow](/ko/newsletters/2026-02-25-newsletter/#burrow-ai-에이전트를-위한-mls-메시지)가 AI 에이전트와 인간 모두를 위한 [Marmot](/ko/topics/mls/) 암호화 메시징을 추가하여, Nostr의 신원 및 relay 인프라를 기계 간 통신으로 확장했습니다.

[FIPS](/ko/newsletters/2026-02-25-newsletter/#fips-nostr-네이티브-메시-네트워킹)가 secp256k1 키페어를 노드 신원으로 사용하고 UDP, 이더넷, 블루투스, LoRa 라디오를 통한 transport 불가지론 라우팅을 제공하는 Nostr 네이티브 메시 네트워킹의 작동하는 Rust 구현을 출시했습니다. 이 설계는 Nostr의 키 모델이 소셜 미디어를 넘어 물리적 네트워크 인프라로 확장됨을 보여주었습니다.

[OpenSats가 열다섯 번째 Nostr 보조금 물결을 발표](https://opensats.org/blog/fifteenth-wave-of-nostr-grants)하여, ContextVM과 Nostube를 포함한 프로젝트에 자금을 지원했습니다. 프로토콜 변경에는 Nostr Wallet Connect를 위한 [NIP-47](/ko/topics/nip-47/) 보류 인보이스 지원과 relay 측 카운트 추정을 위한 [NIP-45](/ko/topics/nip-45/) (Counting Results) HyperLogLog가 포함되었습니다. [Web of Trust](/ko/topics/web-of-trust/) 점수를 위한 [NIP-85](/ko/topics/nip-85/) (Trusted Assertions) 서비스 제공자 검색 가능성도 병합되었습니다. [rust-nostr](https://github.com/rust-nostr/nostr)가 전면적인 API 재설계를 시작했으며, Nostria 3.0과 [Frostr](https://github.com/FROSTR-ORG) (iOS TestFlight)가 모두 출시되었습니다. [Blossom](/ko/topics/blossom/)의 로컬 캐시 레이어가 relay 간 미디어 가용성 문제를 해결했습니다.

### 전망

5년간의 2월 프로토콜 역사는 기반 작업에서 애플리케이션 레이어 다양화까지 일관된 진행을 보여주며, 2023년 사용자 유입이 전환점이었습니다. 2021년에 7명의 기여자가 3개의 relay에서 작업했습니다. 2026년에는 동일한 프로토콜이 프로덕션 인프라에서 실행되는 메시 네트워킹과 자율 에이전트 제안을 지원했습니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 공유할 뉴스가 있다면 <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ko/topics/nip-17/) DM으로 연락하시거나</a> Nostr에서 찾아주세요.
