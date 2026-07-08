---
title: 'Nostr Compass #23'
date: 2026-05-21
publishDate: 2026-05-21
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-21-newsletter.md
translationDate: 2026-07-01
---

Primal 3.5는 재구축된 Android 셸을 출시했고, Amethyst는 온체인 Bitcoin zap을 추가했으며, White Noise는 markdown 렌더링과 딥 링크를 얻었고, Keycast는 보안 감사를 통과했으며, AgentNoise는 Marmot 암호화 채팅을 통해 로컬 AI 코딩 에이전트를 제어할 수 있게 합니다. Hostr는 리스팅, 예약, EVM 기반 escrow를 다루는 네 개의 초안 NIP과 함께 Nostr 상의 P2P 임대 숙박 플랫폼을 출시합니다. Angor는 암호화된 메시징을 NIP-04에서 NIP-44로 마이그레이션하고, Dart NDK는 NIP-77과 웹 signer를 추가하며, Alby js-sdk v8은 네이티브 NWC 다중 릴레이 재연결을 출시하고, KeyChat은 Signal 일회성 prekey 삭제의 forward secrecy 격차를 패치합니다. 프로토콜 측에서는 Mostro의 anti-abuse 본드가 Phase 2에 도달하고, Wisp는 프라이빗 답장과 gift-wrapped 반응을 출시하며, Namecoin NIP-05 구현 웨이브는 한 주 만에 여섯 개의 클라이언트를 다룹니다.

## 주요 소식

### Primal 3.5 for Android

자체 캐싱 릴레이 인프라로 지원되는 소셜 클라이언트인 Primal은 이번 주에 재구축된 애플리케이션 셸과 함께 [3.5.9](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.9)를 출시했습니다. 재설계는 이전 내비게이션 구조를 업데이트된 레이아웃과 새로운 Explore 화면으로 대체하여, 주요 발견 표면에 전용 홈을 제공합니다. 이 릴리스는 링크 프리뷰에 오디오 재생을 추가하므로, 노트에 임베드된 오디오 파일이 피드를 떠나지 않고 인라인으로 재생됩니다. NIP-05 검증 배지는 이제 프로필에 인라인으로 표시되어 identity 확인을 한눈에 볼 수 있게 합니다. 알림 필터링은 개편되어 사용자가 알림 리스트에 도달하는 이벤트 유형을 좁힐 수 있게 되었습니다. 에디터는 더 나은 이벤트 링크 처리를 얻었고, 기본 데이터베이스 계층은 안정성 수정을 받았습니다.

### White Noise: markdown, 딥 링크, 오디오 메타데이터

Nostr와 MLS([RFC 9420](https://www.rfc-editor.org/rfc/rfc9420)) 위에 구축된 Marmot 암호화 그룹 메시징 앱인 White Noise는 프런트엔드와 백엔드 저장소 전반에 걸쳐 지금까지 가장 바쁜 주 중 하나를 보냈습니다.

프런트엔드에서 [PR #665](https://github.com/marmot-protocol/whitenoise/pull/665)는 채팅 메시지에 대한 전체 markdown 렌더링을 추가하므로, bold, italic, code 블록, 링크가 이제 메시지 뷰에서 네이티브로 렌더링됩니다. [PR #675](https://github.com/marmot-protocol/whitenoise/pull/675)는 이전에 마지막이 아닌 admin에게 차단되었던 그룹 나가기 흐름을 활성화하고, [PR #661](https://github.com/marmot-protocol/whitenoise/pull/661)은 HTTP 리디렉션 인프라 없이 사용자, 채팅, 설정을 다루는 `whitenoise://` 및 `whitenoise-staging://` URI에 대한 네이티브 딥 링크 지원을 추가합니다.

whitenoise-rs의 백엔드에서 [PR #835](https://github.com/marmot-protocol/whitenoise-rs/pull/835)는 kind:30443 게시에 대해 `d_tag` 슬롯을 재사용하여 key package 회전이 제대로 작동하게 하며, NIP-33 replaceable 이벤트 시맨틱을 활성화하여 연속적인 key package 회전이 릴레이에서 이전 이벤트를 대체하고 현재 key package만 유지하도록 합니다. [PR #833](https://github.com/marmot-protocol/whitenoise-rs/pull/833)은 오디오 첨부 파일에 대한 선택적 `duration_ms` 및 `waveform` 필드로 `FileMetadata`를 확장하며, MIP-04 미디어 태그에 동일한 필드를 추가하는 MDK의 [PR #300](https://github.com/marmot-protocol/mdk/pull/300)과 조정됩니다. 새로운 `whitenoise-markdown` 크레이트([PR #836](https://github.com/marmot-protocol/whitenoise-rs/pull/836))는 이전 nostr-sdk 토큰 파서를 전용 markdown 렌더링 라이브러리로 대체합니다.

Marmot 프로토콜 사양 자체는 [PR #68](https://github.com/marmot-protocol/marmot/pull/68)에서 보안 수정을 받았으며, MIP-01의 이미지 키 유도에 대해 HKDF-SHA256을 명시적으로 지정함으로써 구현 차이를 초래할 수 있는 모호성을 제거하는 보안 문제를 닫습니다. MDK에서 [PR #307](https://github.com/marmot-protocol/mdk/pull/307)은 환영 실패 이유를 정리하고 저장된 길이를 제한하여 별도의 보안 발견 사항을 닫습니다.

### Amethyst v1.10.0: 온체인 Bitcoin zap

Amethyst는 이번 주에 네 개의 릴리스를 출시했으며, [v1.10.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.10.0)이 헤드라인입니다. 이 릴리스는 NIP-BC 온체인 Bitcoin zap 지원을 추가하여, 사용자가 Bitcoin 트랜잭션을 통해 온체인에서 직접 정산되는 zap을 보내고, 받고, 표시할 수 있게 합니다. 이전 릴리스는 비준수 파일명을 거부하도록 Blossom blob 감지를 수정했고([v1.09.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.09.2)), 데스크톱 빌드용 ProGuard 규칙을 패치했으며, 확장된 반응 갤러리에서 온체인 Bitcoin zapper를 전용 ₿ 행으로 표시하기 위해 pull request [#2977](https://github.com/vitorpamplona/amethyst/pull/2977)을 병합했습니다. 페이지 매김이 있는 진행 중인 온체인 트랜잭션 이력 화면은 [PR #2974](https://github.com/vitorpamplona/amethyst/pull/2974)에 도착했습니다.

### AgentNoise: White Noise를 통한 코딩 에이전트 제어

nvk의 [AgentNoise](https://github.com/nvk/agentnoise)는 White Noise를 실행하는 전화기를 로컬 Codex 및 Claude 코딩 에이전트 세션의 제어 표면으로 사용할 수 있게 하는 Rust 네이티브 데스크톱 헬퍼입니다. 이 도구는 하나 이상의 White Noise 채팅을 수신하고, 첫 페어링 PIN 흐름을 통해 발신자를 인증하며, 구성된 런처를 통해 로컬 코딩 에이전트를 시작합니다. 전화기에서 `/claude <prompt>`를 보내면 머신 호스트명과 짧은 프롬프트 요약으로 명명된 새로운 White Noise 작업 세션이 열리고, 진행 업데이트와 최종 출력이 해당 채팅으로 스트리밍됩니다. 의도적으로 Rust 우선이며 신뢰할 수 있는 브리지 경로에서 Node를 제외합니다. 프로젝트는 이번 주에 [v0.1.24](https://github.com/nvk/agentnoise/releases/tag/v0.1.24)에 도달하여, 전화기에서 읽을 수 있는 더 짧은 답장, 짧은 고유 접두사에 의한 job 참조, 옵트인 로컬 세션 watcher를 추가했습니다. AgentNoise는 `marmot-protocol/whitenoise-rs`의 `wn` 및 `wnd` CLI를 하위 프로세스로 구동하므로 White Noise 클라이언트 자체와 Nostr 전송을 공유합니다.

### Keycast 보안 감사 완료

SQLite에서 정지 상태에서 암호화된 Nostr private 키를 저장하는 팀 지향 NIP-46 원격 서명 서버인 [Keycast](https://github.com/marmot-protocol/keycast)는 2026년 5월에 보안 감사를 완료했습니다. 강화 단계는 auth, permission, 데이터 무결성, 종속성 문제를 다루었으며, 결과는 [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md)에 문서화되어 있습니다. 변경 사항에는 다음이 포함됩니다: NIP-98 HTTP auth는 이제 정확히 하나의 `u` 태그와 하나의 `method` 태그를 요구하고, 오래된 타임스탬프를 거부하며, `payload` 해시를 검증합니다; `ALLOWED_PUBKEYS` 허용 목록은 정확하게 파싱되고 서버 측에서 강제됩니다; 빈 정책은 이제 기본적으로 sign/encrypt/decrypt 요청을 거부합니다; SQLite 연결에서 외래 키 강제가 활성화됩니다; `/teams/:id`와 같은 중첩된 앱 경로는 서버 측에서 보호됩니다. SQL 마이그레이션은 시작 시 이전 allowed-kinds 권한 JSON을 정규화합니다. 이 프로젝트는 여전히 초기 단계이며 감사는 실제 팀 키로 신뢰하기 전에 잔여 항목을 언급합니다.

### Scramble: 데스크톱 및 Android용 Marmot 클라이언트

[Scramble](https://github.com/DavidGershony/Scramble)(이전의 OpenChat)은 [Marmot Protocol](/ko/topics/marmot/)을 위한 .NET/Avalonia 데스크톱 및 Android 클라이언트로, MIPs 00-04을 구현합니다: KeyPackage 게시(kind:30443), NostrGroupData MLS 확장으로 그룹 메타데이터, NIP-59 gift-wrapped 환영 이벤트(kind:444), ChaCha20-Poly1305 암호화 메시지(kind:445), Blossom 암호화 미디어 첨부 파일. White Noise 및 다른 Marmot 호환 클라이언트와 완전히 상호 운용 가능합니다.

프로젝트는 이번 주에 13개의 릴리스를 출시했으며, 다중 기기 지원이 주요 기능입니다. 각 기기는 고유한 KeyPackage 슬롯(kind:30443의 `d` 태그)을 생성합니다. 시작 시 Scramble은 릴레이에서 사용자 자신의 KeyPackage를 가져오고, 피어 기기 슬롯 ID를 감지하며, staged commit 흐름을 사용하여 기존 MLS 그룹에 자동으로 추가합니다. 자동 추가는 현재 사용자가 admin인 그룹으로 제한됩니다; 비 admin 그룹은 그룹 admin에게 요청하라는 안내와 함께 건너뜁니다. Forward secrecy 공개 배너는 새로 연결된 기기에 이전 메시지를 사용할 수 없음을 알립니다. 슬롯 ID 조정 패스(`TryReconcileSlotId`)는 릴레이 KeyPackage 바이트를 로컬 키 자료와 매칭하여 올바른 `d` 태그를 채택함으로써 사전 다중 기기 버전에서 마이그레이션된 기기를 처리합니다. Amber 및 NIP-46 사용자를 위한 외부 signer 재연결도 수정되었습니다: `ExternalSignerService`의 내장 자동 재연결을 차단하던 `IsConnected` 가드가 `NostrService`의 아홉 개 호출 사이트 모두에서 제거되었습니다.

### Hostr: Nostr 상의 P2P 임대 숙박

[Hostr](https://hostr.network)([source](https://github.com/sudonym-btc/hostr))는 완전히 Nostr 위에 구축된 P2P 임대 숙박 플랫폼입니다. 프로젝트가 애플리케이션과 병렬로 개발하고 있는 네 개의 초안 NIP을 사용하여 전체 Airbnb 스타일 흐름(속성 검색 및 리스팅, 예약 협상, 결제 정산)을 다룹니다.

숙박 NIP은 [NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md) 분류 리스팅(kind:30402 활성, kind:30403 초안)을 유형(`room`, `house`, `apartment`, `villa`, `hotel`, `hostel`, `resort`), 체크인/체크아웃 시간, 최소 체류, 구성 가능한 정밀도로 위치 기반 검색을 위한 H3 지리 공간 셀 인덱스에 대한 숙박 특정 태그로 확장합니다. 예약 NIP은 전체 협상 및 수명 주기 프로토콜을 정의합니다: kind:32122 replaceable 예약 이벤트는 `d` 거래 ID, 리스팅 앵커 `a` 태그, 역할(`buyer`, `seller`, `escrow`)이 있는 참가자 `p` 태그를 포함합니다; kind:1327 구조화된 메시지 rumor는 NIP-59 gift wrap을 통해 프라이빗 협상 단계 반대 제안을 전달하여 협상이 공개 릴레이에서 벗어나 유지되도록 합니다; kind:1326 append-only 전환 이벤트는 예약이 커밋되면 공개 감사 추적을 만듭니다. 구매자 프라이버시는 암호화된 `participant_proof` 태그를 통해 구매자의 실제 identity에 바인딩된 거래별 임시 Nostr 키를 통해 보존됩니다. Escrow NIP은 kind:30303 escrow 서비스 광고와 kind:17388 사용자 신뢰 선언을 정의합니다; 참조 구현은 Rootstock의 EVM 스마트 계약을 사용하며, `contractBytecodeHash`는 클라이언트가 배포된 계약이 알려진 감사된 구현과 일치하는지 검증할 수 있게 합니다. 마켓플레이스 리스팅 NIP은 모든 NIP-99 마켓플레이스 프로필에서 공유되는 제네릭 태그를 정의하며, `instantBook`, `negotiable`, `quantity`, `securityDeposit`, `cancellationPolicy`, `maxDisputePeriod`를 포함합니다. 이번 주에 프로젝트는 앱 스토어 제출을 준비하고 에이전트용 자동화를 위한 MCP 클라이언트 identity 지원을 병합했습니다.

이번 주 Shakespeare MiniApps 플랫폼에 두 개의 새 항목이 등장했습니다: [InkPress](https://inkpress.shakespeare.wtf)는 구조화된 잡지 스타일 콘텐츠를 Nostr 이벤트로 게시하는 AI 잡지 생성기이고, [PressStr](https://pressstr.shakespeare.wtf)는 Soapbox 스택을 위한 글쓰기 및 게시 플랫폼입니다.

## 이번 주 출시

### ngit v2.4.4

**ngit**는 [v2.4.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.4)를 출시하여, git 서버가 Nostr 상태보다 fast-forward 앞서 있는 경우에 대한 `ngit sync --trust-server`(`-t`)를 추가했습니다. 이 상황이 감지되면 sync는 영향을 받는 refs를 보고하고 업데이트된 상태 이벤트에 서명하고 게시하기 위해 플래그를 요구합니다; `nostr.trust-server-domains` git 구성 설정은 플래그 없이 자동으로 신뢰해야 하는 서버에 대한 세미콜론으로 구분된 허용 목록을 제공합니다.

### Amber v6.1.0-pre3, PSBT 서명 추가

**Amber**는 새 앱 연결을 위한 개선된 레이아웃, 크래시 수정, 권한 화면의 select/deselect all 옵션과 함께 [v6.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre3)을 출시했습니다. [PR #438](https://github.com/greenart7c3/Amber/pull/438)은 Intent 기반 및 NIP-46 릴레이 기반 경로 모두를 통해 PSBT 서명 지원을 추가하여, Amber가 요청하는 앱에 nsec를 노출하지 않고 Partially Signed Bitcoin Transaction에 서명할 수 있게 합니다.

### Wisp v1.1.0, 프라이빗 답장 출시 및 Amber 지원 제거

**Wisp**는 NIP-17 gift wrap을 통한 프라이빗 답장([PR #540](https://github.com/barrydeen/wisp/pull/540)), 프라이빗 답장에 대한 gift-wrapped 반응 및 DIP-03 zap([PR #543](https://github.com/barrydeen/wisp/pull/543)), 노트 자동 번역([PR #523](https://github.com/barrydeen/wisp/pull/523)), zap 대화 상자의 레지스터 스타일 법정 화폐 입력과 함께 [v1.1.0](https://github.com/barrydeen/wisp/releases/tag/v1.1.0)을 출시했습니다. [PR #541](https://github.com/barrydeen/wisp/pull/541)은 프라이빗 zap을 자체 개발한 DM 릴레이 평문 방식에서 적절한 DM 릴레이 라우팅을 사용하는 DIP-03로 마이그레이션합니다. 동일한 릴리스 사이클에서 NIP-55 원격 signer 지원이 제거되었고([PR #531](https://github.com/barrydeen/wisp/pull/531)), Amber 및 기타 외부 signer 통합이 제거되었으며, 번들된 로컬 릴레이가 제거되었습니다([PR #533](https://github.com/barrydeen/wisp/pull/533)). Wisp는 Android용 Nostr 소셜 클라이언트입니다.

### Calendar by Formstr v1.5.4, 새 참가자를 위한 gift wrap 수정

**Calendar by Formstr**는 [v1.5.4](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.4)(v1.5.2 → v1.5.4 시퀀스의 최신)를 출시했습니다. [PR #160](https://github.com/formstr-hq/nostr-calendar/pull/160)은 새 참가자와 함께 프라이빗 캘린더 이벤트를 편집할 때 `p` 태그에 새 pubkey가 있는 업데이트된 이벤트를 게시했지만 해당 참가자에게 gift wrap 초대를 생성하거나 전달하지 않아 마지막 순간 추가에 대한 초대 흐름을 깨뜨리는 버그를 수정합니다. [PR #156](https://github.com/formstr-hq/nostr-calendar/pull/156)은 프라이빗 이벤트 복호화 주위에 오류 처리를 추가하여 클라이언트가 복호화할 수 없는 이벤트에서 더 이상 throw하지 않도록 하고, [PR #138](https://github.com/formstr-hq/nostr-calendar/pull/138)은 시간대에 걸쳐 드리프트되는 반복 이벤트 시간을 수정합니다.

### Applesauce v6.1.0, NIP-34 git cast 및 NIP-51 lookup 릴레이 추가

**Applesauce**는 상당한 NIP-34(git-over-Nostr) 지원과 함께 패키지 전반에 걸쳐 [v6.1.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.1.0)을 출시했습니다: applesauce-common은 새로운 `GitRepository`, `GitGraspList`, `FavoriteGitRepos` cast와 매칭 팩토리를 추가하고, `User.favoriteGitRepos$`, `User.gitAuthors$`, `User.graspServers$` 반응형 속성을 노출하여 애플리케이션이 사용자가 팔로우하는 git 리포지토리, repo 유지 관리자, 구성된 GRASP 서버를 동일한 User 객체에서 직접 나열할 수 있게 합니다. 동일한 릴리스는 특정 데이터를 찾을 위치를 발견하는 데 사용되는 relay-list 계열의 최근 추가인 NIP-51 kind 10086 lookup 릴레이 리스트에 대한 지원을 추가합니다. applesauce-core는 NIP-01 replaceable 주소 조회를 위한 `EventCast`의 `replaceableAddress`와 `pointer`, `kind`, `getReplaceableAddressForEvent` 헬퍼를 얻고, 기본 `User` cast에 `timeline$()` 메서드를 추가합니다. [PR #73](https://github.com/hzrd149/applesauce/pull/73)은 오프라인 릴레이를 조용히 드롭하는 pool 수동 메서드를 수정합니다.

### Sprout v0.0.16, Sprig 바이너리 및 huddle 프로토콜 v2 출시

인간과 AI 에이전트가 동일한 방과 이벤트 로그를 공유하는 Block의 자체 호스팅 Nostr 릴레이 기반 팀 워크스페이스인 **Sprout**는 새로운 Sprig 올인원 바이너리의 롤링 빌드와 함께 데스크톱 앱의 [v0.0.16](https://github.com/block/sprout/releases/tag/v0.0.16)을 출시했습니다([PR #605](https://github.com/block/sprout/pull/605)). Sprig 바이너리는 쉬운 배포를 위해 ACP 하네스, 에이전트, 개발자 MCP를 단일 busybox 스타일 바이너리로 번들합니다. [PR #611](https://github.com/block/sprout/pull/611)에 추가된 `--no-memory` 플래그를 통해 운영자는 ACP 하네스에 대한 NIP-AE 핵심 메모리 주입을 비활성화할 수 있습니다. 실시간 측에서 [PR #609](https://github.com/block/sprout/pull/609)는 huddle 음성 프로토콜을 최대 10명의 동시 피어를 지원하는 v2 프레임 헤더로 확장합니다.

### Nostrord v1.0.3, OS 키체인 및 다중 계정 추가

**Nostrord**는 OS 키체인 및 암호 대체를 사용하여 강화된 로컬 키 저장소, 다중 계정 지원, Android에서 signer 앱을 여는 탭 가능한 bunker QR 코드와 함께 [v1.0.3](https://github.com/nostrord/nostrord/releases/tag/v1.0.3)을 출시했습니다.

### Angor, NIP-44로 마이그레이션 및 보안 강화 출시

Nostr와 Taproot 위에 구축된 Bitcoin 크라우드펀딩 앱인 **Angor**는 이번 주에 보안 강화 및 Nostr 통합 변경 세트와 함께 세 개의 unstable 릴리스([v0.2.24](https://github.com/block-core/angor/releases/tag/v0.2.24), [v0.2.25](https://github.com/block-core/angor/releases/tag/v0.2.25), [v0.2.26](https://github.com/block-core/angor/releases/tag/v0.2.26))를 출시했습니다. [PR #860](https://github.com/block-core/angor/pull/860)은 Nostr 암호화 메시징을 NIP-04에서 NIP-44로 마이그레이션하여, 사용 중단된 XOR 기반 방식을 ChaCha20-Poly1305 암호화로 대체합니다. [PR #861](https://github.com/block-core/angor/pull/861)은 임시 Nostr 인증 키를 사용하여 선택된 지갑 없이 Blossom 미디어 업로드를 허용하여, 아직 지갑을 연결하지 않은 사용자에 대한 업로드 차단을 해제합니다. 보안 시리즈는 몇 가지 강화된 카테고리를 다루었습니다: [PR #854](https://github.com/block-core/angor/pull/854)는 AngorKey에 대한 유형 안전성과 니모닉 메모리 보호를 추가하고, [PR #856](https://github.com/block-core/angor/pull/856)은 timelock, 수수료율, dust 임계값, 페널티 규칙에 대한 프로토콜 수준 검증을 강제하며, [PR #851](https://github.com/block-core/angor/pull/851)은 여덟 개의 중간 및 낮은 심각도 카테고리에 걸쳐 breaking하지 않는 강화를 적용합니다. [PR #859](https://github.com/block-core/angor/pull/859)는 AOT 컴파일을 활성화하고 런타임 코드 생성을 제거하여 GrapheneOS 호환성을 수정하고, [PR #855](https://github.com/block-core/angor/pull/855)는 OS가 프로세스를 종료하기 전에 지갑 상태를 유지하여 Android swipe-kill에서의 지갑 손실을 방지합니다.

### Alby js-sdk v8.0, NWC 다중 릴레이 재연결 출시

**Alby js-sdk**는 NWC 다중 릴레이 구독 지원과 함께 v8.0 라인([v8.0.1](https://github.com/getAlby/js-sdk/releases/tag/v8.0.1)에서 [v8.0.3](https://github.com/getAlby/js-sdk/releases/tag/v8.0.3)까지)을 출시했습니다. [PR #516](https://github.com/getAlby/js-sdk/pull/516)은 nostr-tools 종속성을 업데이트하고 여러 릴레이에 걸쳐 네이티브 자동 재연결을 활성화하여, 이전 폴링 접근 방식을 릴레이 네이티브 재연결 로직으로 대체합니다. [PR #542](https://github.com/getAlby/js-sdk/pull/542)는 모든 `console.debug` 호출을 주입 가능한 로거 인터페이스로 대체하여, 애플리케이션 개발자가 자체 로깅 인프라를 통해 SDK 진단을 라우팅할 수 있게 합니다. 이 릴리스는 WebSocket 폴리필을 제거하여 서버 측 소비자에 대해 Node.js 22 이상을 요구합니다. v8.0.2는 특정 번들러를 깨뜨린 utils crypto import 버그에 대한 수정을 추가했습니다.

### KeyChat v1.41.1, forward secrecy 수정

Signal 프로토콜을 Nostr 릴레이 전송과 결합한 메시징 앱인 **KeyChat**은 [v1.41.1+6513](https://github.com/keychat-io/keychat-app/releases/tag/v1.41.1+6513)을 출시했습니다. 헤드라인 수정은 성공적인 복호화 직후 Signal 일회성 prekey를 삭제하여 forward secrecy를 강제하며, 나중에 기기가 손상된 경우 유지된 prekey가 과거 메시지를 복호화하는 데 사용될 수 있는 격차를 닫습니다. 이 릴리스는 또한 단일 링크로 구성된 메시지에 대한 URL 프리뷰를 추가하고, 20 MB 자동 임계값과 함께 새로운 `FileDownloadManager` 아래로 미디어 자동 다운로드를 중앙 집중화하며, 유료 릴레이 수수료 구성이 항상 올바르게 로드되도록 콜드 스타트에서 강제 새로 고침하기 위해 NIP-11 릴레이 정보 가져오기를 리팩터링합니다.

## 개발 중

**Citrine**은 NIP-70 강제를 구현하는 [PR #151](https://github.com/greenart7c3/Citrine/pull/151)을 병합했습니다: Android 릴레이는 이제 사양이 요구하는 대로 보호된 이벤트 콘텐츠를 임베드하는 리포스트를 차단합니다. [PR #149](https://github.com/greenart7c3/Citrine/pull/149)는 릴레이 설정 화면에서 여러 연결 주소, localhost, 로컬 Wi-Fi, Tor에 대한 표시 및 복사 작업을 추가합니다. [PR #141](https://github.com/greenart7c3/Citrine/pull/141)은 Amber와의 외부 signer 통합을 통해 NIP-42 AUTH 챌린지 처리를 추가합니다.

**Mostro**는 anti-abuse 본드 롤아웃의 Phase 2에 도달했습니다. [PR #737](https://github.com/MostroP2P/mostro/pull/737)은 solver 지시 분쟁 slash 로직을 도입합니다: admin 핸들러는 이제 mostro-core에서 `BondResolution` 페이로드를 소비하여, admin이 분쟁을 해결할 때 어느 쪽의 본드도 slash할 수 있게 합니다. [PR #736](https://github.com/MostroP2P/mostro/pull/736)에서 병합된 Phase 1.5는 전용 `PayBondInvoice` action과 `WaitingTakerBond` 상태를 도입하여, taker의 anti-abuse 본드 지불을 구매자의 거래 지불금에서 분리했습니다. 모바일 클라이언트는 [PR #592](https://github.com/MostroP2P/mobile/pull/592)에서 전체 Phase 1.5 UX를 추가했습니다. Mostro는 Nostr 위에 구축된 P2P Bitcoin 거래 프로토콜입니다.

**Damus**는 릴레이 신호 표시기를 복원하는 [PR #3773](https://github.com/damus-io/damus/pull/3773)을 병합했으며, [PR #3775](https://github.com/damus-io/damus/pull/3775)는 초기 연결 실패 후 재연결을 거부하는 릴레이를 수정합니다.

**rust-nostr**는 이벤트 완결 traits와 NIP 특정 이벤트 빌더를 추가하는 [PR #1358](https://github.com/rust-nostr/nostr/pull/1358)을 병합하여, 특정 프로토콜 함수에 대해 올바르게 유형이 지정된 이벤트를 더 쉽게 구성할 수 있게 합니다. [PR #1363](https://github.com/rust-nostr/nostr/pull/1363)은 connect 응답을 보내기 전에 NIP-46 signer가 알림을 구독하도록 보장하는 수정을 백포트하여, connect 직후 도착하는 클라이언트 메시지가 누락될 수 있는 race condition을 닫습니다.

**dart-nostr**는 Namecoin `.bit` 릴레이 리졸버와 TLSA pin 레코드를 추가하는 [PR #44](https://github.com/ethicnology/dart-nostr/pull/44)를 병합하여, Flutter 애플리케이션이 Namecoin DNS를 통해 `wss://example.bit/` 릴레이 URL을 실제 WebSocket 주소로 해결할 수 있게 합니다.

**Dart NDK**(Dart/Flutter Nostr 개발 키트, 현재 `relaystr/ndk`)는 오프라인 이벤트 서명 프로토콜인 NIP-77을 구현하는 [PR #464](https://github.com/relaystr/ndk/pull/464)를 병합했습니다. signer 측에서 [PR #602](https://github.com/relaystr/ndk/pull/602) 및 [PR #601](https://github.com/relaystr/ndk/pull/601)는 웹 특정 이벤트 signer와 `PlatformEventVerifier` 추상화를 추가하여, Flutter 웹 앱이 별도의 코드 경로 없이 플랫폼 signer를 사용할 수 있게 합니다; [PR #604](https://github.com/relaystr/ndk/pull/604)는 런타임 signer 선택을 위한 이벤트 signer 팩토리를 도입합니다. [PR #608](https://github.com/relaystr/ndk/pull/608)은 사용자의 NIP-17 DM 릴레이 리스트(kind:10050)를 가져오는 `getDmRelays()`를 추가하고, [PR #600](https://github.com/relaystr/ndk/pull/600)은 NIP-46 서명된 필드 보존을 수정하여 원격 signer가 왕복에서 필드를 잃지 않도록 합니다.

**Pages by Form\***([repo](https://github.com/formstr-hq/nostr-docs))는 [pages.formstr.app](https://pages.formstr.app)에 호스팅된 Formstr의 Nostr 네이티브 협업 문서 앱으로, 이번 주에 암호화 첨부 파일 및 문서 관리 흐름을 강화하는 네 개의 PR을 병합했습니다. [PR #37](https://github.com/formstr-hq/nostr-docs/pull/37)은 암호화된 첨부 파일을 인라인화하여 DOCX, HTML, PDF 내보내기에서 누락된 이미지를 수정합니다: Blossom 서버에서 `<encrypted-file>` blob을 가져오고, 저장된 키와 nonce로 AES-GCM 256비트를 사용하여 복호화하고, 이미지 MIME 유형을 검증하고, base64 데이터 URL로 변환하여, 암호화된 형태로 Blossom에만 존재하는 이미지를 내보내기에서 보존합니다. [PR #39](https://github.com/formstr-hq/nostr-docs/pull/39)는 로컬 문서 검색 메커니즘을 추가하고, [PR #38](https://github.com/formstr-hq/nostr-docs/pull/38)은 이름 바꾸기 흐름을 정리하며, [PR #40](https://github.com/formstr-hq/nostr-docs/pull/40)은 공유 백업 처리를 수정합니다.

**Zap Cooking**은 사용자에게 보이는 변경 없이 피드 렌더링 프리미티브를 놓는 피드 개편의 첫 단계인 [PR #396](https://github.com/zapcooking/frontend/pull/396)을 병합했습니다. 이 PR은 `url`, `m`(MIME), `dim`(dimensions), `blurhash`, `alt`, `x`(파일 해시), `fallback` 슬롯을 읽는 NIP-92 `imeta` 태그 파서와, SSR-safe null 대체와 함께 canvas를 통해 PNG 데이터 URL을 생성하는 손으로 이식된 canonical blurhash 디코더(~200 LOC)를 도입합니다. `imeta` 태그가 없는 경우 파서는 현재 피드가 이미 사용하는 것과 동일한 휴리스틱을 사용하여 이벤트 콘텐츠에서 원시 이미지 및 비디오 URL을 추출하는 것으로 대체됩니다.

**Nurunuru**(ぬるぬる, `tami1A84/null--nostr`)는 Rust FFI 엔진을 공유하는 네이티브 Android, iOS, 웹 변형이 있는 Nostr 클라이언트로, [PR #176](https://github.com/tami1A84/null--nostr/pull/176)에서 v1.5.0 Native → Web 동기화를 병합했습니다. 이 동기화는 이미 Android v1.4.9 및 iOS 1.0.4에 출시된 여러 기능 추가를 웹 빌드에 가져옵니다: [NotificationModal](https://github.com/tami1A84/null--nostr/pull/176)은 이제 생일 알림, 상호 팔로우 zap 감지, 커스텀 이모지 반응 알림을 표시합니다; 반응 선택기는 Unicode 기본 반응 빠른 행을 삭제하고 UX를 커스텀 이모지에 집중시킵니다; `lib/recommendation.js`의 추천 엔진은 아이콘이나 표시 이름이 없는 사용자를 필터링하고, 백그라운드에서 Recommended를 로드하면서 Following 항목을 우선시합니다. 음성 입력은 반대 방향으로 가는 하나의 기능입니다: 웹 빌드는 이미 ElevenLabs Scribe 스트리밍을 사용하며, v1.5.0은 네이티브 측을 OS 표준 `SpeechRecognizer`(Android) 및 `SFSpeechRecognizer` + `AVAudioEngine`(iOS)로 부분 동기화하는 반면, 전체 네이티브 Scribe 통합은 v1.6으로 연기됩니다.

## 프로토콜 및 사양 작업

**PR [#2251](https://github.com/nostr-protocol/nips/pull/2251)**은 NIP-70 보호된 이벤트 사양을 강화합니다: 이제 보호된 이벤트의 전체 콘텐츠를 임베드하는 리포스트는 릴레이가 거부해야 한다고 명시적으로 명시합니다. NIP-70은 노트 작성자가 자신의 노트가 재게시되는 것에 동의하지 않음을 알리는 `-` 태그를 정의합니다. 원래 사양은 릴레이 필터링 동작을 다루었지만 리포스트 사례는 모호하게 남겼습니다. 이 PR은 그 격차를 닫습니다. Citrine의 [PR #151](https://github.com/greenart7c3/Citrine/pull/151)은 같은 주에 릴레이 측에서 강제를 구현합니다.

**PR [#1653](https://github.com/nostr-protocol/nips/pull/1653)**은 프라이빗 초안 이벤트를 저장하고 동기화하기 위한 Drafts NIP을 제안합니다. 이 제안은 작성자 자신의 키에 대한 `draft` 상태와 NIP-44 암호화가 있는 replaceable 이벤트를 사용하여, 클라이언트가 진행 중인 작업을 다른 사람이 볼 수 없이 릴레이에 저장할 수 있게 합니다. 초안 이벤트는 결국의 kind와 태그를 포함한 전체 의도된 게시 이벤트를 암호화된 콘텐츠로 포함합니다.

**Snapshots([PR #2279](https://github.com/nostr-protocol/nips/pull/2279))**는 replaceable Nostr 이벤트의 정확한 한 버전을 보존하기 위한 불변 스냅샷 이벤트를 정의하는 열린 제안입니다. 스냅샷 이벤트는 특정 시점의 replaceable 이벤트의 전체 콘텐츠를 포함하며, replaceable 이벤트의 주소로 다시 링크하는 `a` 태그가 있어 모든 이력 버전을 함께 쿼리할 수 있습니다. 이는 릴레이가 이전 버전 유지를 중단한 후에도 관찰자가 이력 상태를 검사할 수 있게 합니다.

**Namecoin NIP-05 웨이브:** 이번 주에는 `.bit` NIP-05 해결을 Nostr 클라이언트에 추가하기 위한 조정된 push가 있었습니다. NIP 논의 피드는 Aegis([#14](https://github.com/ZharlieW/Aegis/pull/14), signer에서 서명 시 검증 추가), nostter([#2128](https://github.com/SnowCait/nostter/pull/2128)), dart-nostr([#44](https://github.com/ethicnology/dart-nostr/pull/44))에 대한 오픈소스 PR과 함께 upstream NIP 초안([PR #2349](https://github.com/nostr-protocol/nips/pull/2349))을 캡처했습니다. Aegis PR은 검증을 생산자 측에 배치하는 것으로 주목할 만합니다: signer는 `.bit` identity를 주장하는 kind:0 이벤트에 서명하기 전에 Namecoin 체인을 확인하고 불일치 시 사용자에게 경고하여, 이벤트가 어떤 릴레이에도 도달하기 전에 문제를 잡습니다.

## NIP 심층 분석: NIP-07 (window.nostr for Web Browsers)

[NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md)은 브라우저 확장이 웹 애플리케이션에 노출하는 `window.nostr` 인터페이스를 정의합니다. 이는 웹에서 가장 널리 배포된 signer 인터페이스이며, Alby, nos2x, Flamingo, horse를 포함한 확장에 의해 구현됩니다.

인터페이스에는 두 개의 필수 메서드와 여러 선택적 메서드가 있습니다. `window.nostr.getPublicKey()`는 private 키를 호출 페이지에 노출하지 않고 사용자의 public 키를 hex 문자열로 반환합니다. `window.nostr.signEvent(event)`는 `created_at`, `kind`, `tags`, `content`가 있는 부분 이벤트를 받고, `id`, `pubkey`, `sig`가 추가된 완전한 서명된 이벤트를 반환합니다. 핵심은 private 키가 확장의 격리된 컨텍스트를 절대 떠나지 않는다는 것입니다; 웹 애플리케이션은 서명되지 않은 이벤트를 제출하고 서명된 이벤트를 받습니다.

선택적 메서드는 암호화를 다룹니다: 이전 NIP-04 방식(현재 사용 중단)을 위한 `window.nostr.nip04.encrypt` 및 `window.nostr.nip04.decrypt`, 그리고 현재 NIP-44 방식을 위한 `window.nostr.nip44.encrypt` 및 `window.nostr.nip44.decrypt`. 따라서 NIP-44를 지원하는 확장은 호출 페이지가 nsec를 보지 않고도 직접 메시지 암호화와 pubkey 키 암호화가 필요한 다른 애플리케이션 모두를 처리할 수 있습니다.

사양에는 확장 작성자에 대한 권장 사항도 포함됩니다: 확장 manifest에서 `"run_at": "document_end"`로 스크립트를 로드하여 페이지가 로드될 때 `window.nostr`을 동기적으로 사용할 수 있도록 하고, 클라이언트가 확장이 주입하기 전에 `window.nostr`을 확인하는 race condition을 피합니다.

NIP-07의 실행 예시는 위에서 다룬 Keycast 프로젝트입니다. Keycast 웹 프런트엔드는 NIP-98 HTTP auth 이벤트에 서명하기 위해 NIP-07을 사용합니다: SvelteKit 앱은 사용자의 nsec를 직접 처리하지 않습니다. `window.nostr.signEvent`를 호출하여 auth 헤더를 생성한 다음, 해당 헤더를 Keycast API로 보냅니다. 이 아키텍처는 전체 팀 키 관리 흐름 동안 키 자료가 브라우저 확장에 유지된다는 것을 의미합니다.

```json
{
  "id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 1,
  "tags": [],
  "content": "Hello from a NIP-07 signed event",
  "sig": "0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2cdd"
}
```

## NIP 심층 분석: NIP-39 (external identities in profiles)

[NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md)는 Nostr 사용자가 자신의 프로필에서 외부 플랫폼 identity에 대한 제어를 선언하는 방법을 정의합니다. 각 선언은 kind:10011 이벤트 내부의 `i` 태그를 사용하여, 독립적으로 검증할 수 있는 증명과 함께 다른 플랫폼의 특정 계정에 대한 소유권을 주장합니다.

각 태그는 `["i", "platform:identity", "proof"]` 형식을 따르며, 여기서 `platform:identity`는 플랫폼 이름과 사용자명을 콜론 구분자로 결합합니다(`github:semisol`, `twitter:semisol_public`). `proof`는 플랫폼 자체의 검증 가능한 아티팩트를 가리킵니다.

GitHub의 경우 증명은 Gist ID입니다. 사용자는 자신의 GitHub 계정에서 `Verifying that I control the following Nostr public key: npub1...` 텍스트를 포함하는 공개 Gist를 생성합니다. 주장을 검증하는 클라이언트는 `https://gist.github.com/<identity>/<proof>`를 가져와서 Gist가 주장된 GitHub 사용자명에 의해 작성되었고 예상 pubkey를 포함하는지 확인합니다. Twitter의 경우 증명은 tweet ID이고, Mastodon의 경우 게시물 ID이며, Telegram의 경우 공개 그룹의 메시지 참조입니다.

Identity provider 이름은 `a-z`, `0-9` 및 문자 `._-/`만 포함해야 하며 `:`를 포함해서는 안 됩니다. Identity 이름은 소문자로 정규화되어야 하며, 여러 개가 존재하는 경우 기본 alias가 사용됩니다.

이번 주에 진행 중인 Namecoin `.bit` NIP-05 논의는 더 넓은 identity 스택에서 NIP-39의 역할을 보여줍니다: 중앙 검증 기관 없이 Nostr 키를 다른 곳의 확립된 identity와 교차 참조하는 표준화된 릴레이 독립적인 방법을 제공합니다. 클라이언트는 명명된 플랫폼의 공개 아티팩트를 가져와서 증명을 독립적으로 검증할 수 있으며, 증명은 제네릭 플랫폼 자격 증명이 아니라 Gist 또는 tweet 텍스트의 특정 Nostr pubkey에 바인딩됩니다.

```json
{
  "id": "b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 10011,
  "tags": [
    ["i", "github:semisol", "9721ce4ee4fceb91c9711ca2a6c9a5ab"],
    ["i", "twitter:semisol_public", "1619358434134196225"],
    ["i", "mastodon:bitcoinhackers.org/@semisol", "109775066355589974"]
  ],
  "content": "",
  "sig": "1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3eff"
}
```

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 공유할 소식이 있다면 Nostr에서 DM을 보내거나 [nostrcompass.org](https://nostrcompass.org)에서 찾아주세요.
