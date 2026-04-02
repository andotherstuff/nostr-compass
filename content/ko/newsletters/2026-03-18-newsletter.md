---
title: 'Nostr Compass #14'
date: 2026-03-18
translationOf: /en/newsletters/2026-03-18-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [Amethyst](https://github.com/vitorpamplona/amethyst)가 완전한 [NIP-47](/ko/topics/nip-47/) (Nostr Wallet Connect) 메서드 지원을 완성했고, [Alby Hub](https://github.com/getAlby/hub)이 [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6)에서 다중 relay 지원을 추가했으며, [Amber](https://github.com/greenart7c3/Amber)가 내장 Tor와 더 세밀한 서명자 권한이 포함된 [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3)을 출시했고, [Zeus](https://github.com/ZeusLN/zeus)가 [PR #3835](https://github.com/ZeusLN/zeus/pull/3835)에서 위험한 NWC keysend 경로를 제거했습니다. [Notedeck](https://github.com/damus-io/notedeck)이 [NIP-94](/ko/topics/nip-94/) (File Metadata) 이벤트를 통해 릴리스를 발견하는 서명된 업데이터가 포함된 [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2)를 출시했고, [Damus](https://github.com/damus-io/damus)가 오래된 [NIP-65](/ko/topics/nip-65/) (Relay List Metadata) 상태를 수정했으며, [Nostrability Outbox](https://github.com/nostrability/outbox)가 수정된 데이터로 벤치마크 결과를 개정했고, [Primal iOS](https://github.com/PrimalHQ/primal-ios-app)가 DM용 직접 relay 구독을 테스트하고 있습니다. [Primal Android](https://github.com/PrimalHQ/primal-android-app)가 [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7)을, [Route96](https://github.com/v0l/route96)이 [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0)을, [OpenChat](https://github.com/DavidGershony/openChat)이 [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11)에서 Marmot 상호운용성을 강화했고, [Pika](https://github.com/sledtools/pika)가 [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1)에서 런타임을 통합했으며, [Nostria](https://github.com/nostria-app/nostria)가 [NIP-85](/ko/topics/nip-85/) (Trusted Assertions) Web of Trust 필터링을 추가했습니다. NIPs 저장소는 [NIP-54](/ko/topics/nip-54/) (Wiki) Djot 마크업과 [NIP-19](/ko/topics/nip-19/) (Bech32-Encoded Entities) 5000자 입력 제한을 병합했습니다.

## 뉴스

### Wallet Connect 지원이 확대되고, 지갑 클라이언트가 장애 경로를 강화

[Amethyst](https://github.com/vitorpamplona/amethyst), vitorpamplona가 유지 관리하는 Android 클라이언트가 [PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828)을 병합하여 [NIP-47](/ko/topics/nip-47/) 구현을 거의 완전한 프로토콜 커버리지에 도달시켰습니다. 이 패치는 `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`, 보류 인보이스 메서드, TLV 레코드가 포함된 keysend 지원, kind `13194`를 통한 기능 검색, [NIP-44](/ko/topics/nip-44/) (Encrypted Payloads)가 포함된 kind `23197` 알림 이벤트를 추가합니다. 이로써 클라이언트는 앱별 확장에 의존하지 않고 훨씬 넓은 NWC 인터페이스를 확보했습니다.

주변 지갑 스택도 같은 방향으로 움직였습니다. 많은 NWC 배포 뒤에 있는 자체 보관 Lightning 노드이자 지갑 서비스인 [Alby Hub](https://github.com/getAlby/hub)이 다중 relay 지원과 더 간단한 연결 및 스왑 흐름이 포함된 [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6)을 출시했습니다. 모바일 Lightning 지갑 [Zeus](https://github.com/ZeusLN/zeus)는 해당 흐름에서 무소음 자금 유출 경로를 확인한 후 NWC keysend 지원을 제거하는 [PR #3835](https://github.com/ZeusLN/zeus/pull/3835)를 병합했으며, 동시에 대기 중인 이벤트 및 Cashu 활동 처리도 수정했습니다. Nostr에서의 지갑 연결은 더 넓어지고 있으며, 구현자들은 보안이 어려운 흐름을 제거하고 있습니다.

### Notedeck, 릴리스 검색을 Nostr로 이전

[지난 주 Notedeck 보도에 이어](/en/newsletters/2026-03-11-newsletter/), Damus 팀의 네이티브 데스크톱 클라이언트 [Notedeck](https://github.com/damus-io/notedeck)이 [PR #1326](https://github.com/damus-io/notedeck/pull/1326) 병합 후 [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2)를 출시했습니다. 새 업데이터는 서명된 kind `1063` 릴리스 이벤트를 구독하고, 로컬 플랫폼을 매칭하며, 참조된 바이너리를 다운로드하고, 설치 전에 SHA256 해시를 검증합니다. 릴리스 메타데이터는 더 이상 GitHub API나 프로젝트 웹사이트에서 가져올 필요가 없습니다. 신뢰할 수 있는 릴리스 pubkey와 relay 연결이면 충분합니다.

같은 패치에 GitHub 릴리스 아티팩트에서 해당 이벤트를 게시하는 `notedeck-release` CLI도 추가되어, 릴리스 파이프라인에 Nostr 네이티브 게시 경로와 검색 경로가 모두 생겼습니다. 이는 또한 Damus와 Notedeck 업데이터 모델을 Zapstore의 relay 게시 서명 릴리스 흐름에 훨씬 더 가깝게 만듭니다: Zapstore의 `zsp` 도구는 이미 소프트웨어 자산을 kind `1063` 또는 `3063` 이벤트로 처리하므로, 이 경로는 하나의 클라이언트나 하나의 게시자에 잠겨 있지 않습니다. 나머지 릴리스 후보는 실용적인 데스크톱 작업으로, 팔로우 칼럼, 프로필 "View As User", [NIP-59](/ko/topics/nip-59/) (Gift Wrap) 지원, 실시간 노트 통계, [NIP-11](/ko/topics/nip-11/) (Relay Information Document) 제한 처리가 포함되지만, 업데이터가 이 릴리스 주기 이후에도 살아남을 부분입니다.

### Relay 상태가 런타임 동작에 더 가까워지고 있음

[Damus](https://github.com/damus-io/damus)가 [PR #3665](https://github.com/damus-io/damus/pull/3665)를 병합하여, 오래된 저장 relay 목록 이벤트 ID를 최신 kind `10002` 이벤트에 대한 직접 데이터베이스 쿼리로 대체했습니다. 이전 값이 오래되면, relay 추가 및 제거 작업이 부트스트랩이나 1년 전 목록으로 대체되어 일부 relay 변경이 성공한 것처럼 보이면서 활성 상태는 변하지 않는 경우가 있었습니다. [PR #3690](https://github.com/damus-io/damus/pull/3690)은 LMDB 압축 시 오래된 `lock.mdb` 상태를 삭제하여 다음 실행 시 `SIGBUS`로 앱이 충돌하지 않도록 두 번째 장애 경로를 수정합니다.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app)가 [PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194)를 열어, 대화가 열려 있는 동안 채팅 상대의 [NIP-04](/ko/topics/nip-04/) (Encrypted Direct Messages) 쓰기 relay에 직접 구독하면서 캐시 서버를 대체 수단으로 유지합니다. [Nostur](https://github.com/nostur-com/nostur-ios-public)가 [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53)을 열어, 무작위 relay 점수, nostr.watch의 [NIP-66](/ko/topics/nip-66/) 활성 필터링, Thompson 샘플링을 결합하여 relay 선택을 고정 휴리스틱에서 학습된 정책으로 변경합니다. 클라이언트들은 오랫동안 relay 선택을 설정 데이터로 취급했습니다. 이제 더 많은 앱이 측정과 복구 로직이 필요한 라이브 상태로 취급하고 있습니다.

## 릴리스

### Primal Android 3.0.7

Primal의 Android 클라이언트 [Primal Android](https://github.com/PrimalHQ/primal-android-app)가 새로운 투표 및 지갑 사이클이 포함된 [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7)을 출시했습니다. [PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945)는 zap 기반 투표를 추가하고, [PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948)은 대규모 투표에서도 사용성을 유지하도록 투표 로딩을 페이지네이션하며, [PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965)는 모든 거래에 대한 zap 영수증을 가져옵니다. 같은 릴리스는 [PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968)에서 지원되는 이벤트에 [NIP-89](/ko/topics/nip-89/) (Recommended Application Handlers) 클라이언트 메타데이터를 태그하여, 다운스트림 클라이언트가 이벤트 출처를 더 깔끔하게 귀속할 수 있게 합니다.

### Amber v4.1.3

[지난 주 Amber 보도에 이어](/en/newsletters/2026-03-11-newsletter/), [NIP-55](/ko/topics/nip-55/) 흐름을 위한 Android 서명자 앱 [Amber](https://github.com/greenart7c3/Amber)가 [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3)을 출시했습니다. 이 릴리스는 최근의 [NIP-42](/ko/topics/nip-42/) relay 인증 작업 위에 더 많은 운영 강화를 수행합니다: [PR #327](https://github.com/greenart7c3/Amber/pull/327)은 Orbot 지원과 함께 내장 Tor를 추가하고, [PR #324](https://github.com/greenart7c3/Amber/pull/324)는 거친 NIP 기반 암호화 권한을 콘텐츠 타입별 규칙으로 대체하며, [PR #336](https://github.com/greenart7c3/Amber/pull/336)은 오프라인 버전에서 네트워크 권한을 제거하고 [PR #335](https://github.com/greenart7c3/Amber/pull/335)는 이를 유지하기 위한 CI 검사를 추가합니다. [PR #322](https://github.com/greenart7c3/Amber/pull/322)는 또한 PIN 저장을 암호화된 DataStore로 이동합니다.

이 릴리스는 서명자 경계 자체를 강화합니다. 이는 실제 키나 relay 인증 결정을 Amber에 넘기는 모든 Android 흐름에 유용합니다. 어려운 부분은 서명자가 무엇을 할 수 있느냐만이 아니기 때문입니다. 얼마나 좁게 범위를 한정할 수 있느냐이기도 합니다.

### Route96 v0.6.0

[지난 주 Route96 보도에 이어](/en/newsletters/2026-03-11-newsletter/), Blossom과 [NIP-96](/ko/topics/nip-96/) (HTTP File Storage)를 지원하는 미디어 서버 [Route96](https://github.com/v0l/route96)이 [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0)을 릴리스했습니다. 이 릴리스는 구성과 화이트리스트 상태를 핫 리로드가 가능한 데이터베이스로 이동하고 오래되거나 접근이 적은 파일에 대한 보존 정책을 추가합니다. 또한 더 풍부한 `GET /user/files` 엔드포인트와 다운로드 및 트래픽에 대한 파일 통계 추적을 추가하여, 운영자가 스토리지 서버가 어떻게 사용되고 있는지 더 잘 파악할 수 있게 합니다.

### OpenChat v0.1.0-alpha.11

[지난 주 OpenChat 보도에 이어](/en/newsletters/2026-03-11-newsletter/), Marmot 스택 위에 구축된 Avalonia 기반 채팅 클라이언트 [OpenChat](https://github.com/DavidGershony/openChat)이 빠른 프로토콜 작업 후 [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11)을 출시했습니다. [커밋 c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c)는 Welcome 이벤트를 [NIP-59](/ko/topics/nip-59/) gift wrap으로 래핑하고 이전 MIP-00 태그 정규화 심을 제거하며, [커밋 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1)는 MIP-02 준수 감사를 완료하고, [커밋 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f)는 MIP-03 그룹 메시지 암호화에 대해 동일한 작업을 수행합니다. [커밋 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547)은 또한 NIP-44 처리를 공유 marmot-cs 구현으로 통합하여, 클라이언트 측 암호화 드리프트의 위험을 줄입니다.

### nak v0.19.0 및 v0.19.1

fiatjaf의 커맨드라인 Nostr 도구킷 [nak](https://github.com/fiatjaf/nak)이 [v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0)과 [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1)을 출시했습니다. 0.19 시리즈는 [커밋 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47)에서 그룹 포럼 UI를 추가하고, [커밋 da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3)에서 그룹 메타데이터 편집을 전체 교체 흐름으로 전환하며, [커밋 bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf)에서 이전 `no-text` 처리를 `supported_kinds`로 대체합니다. 그룹 구현자에게 이는 CLI를 그룹 사양과 클라이언트가 나아가는 방향에 맞추는 것입니다.

## 프로젝트 업데이트

### Amethyst

[지난 주 Amethyst 보도에 이어](/en/newsletters/2026-03-11-newsletter/), Nostr에서 가장 넓은 프로토콜 표면을 가진 Android 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)가 NIP-47 패치 이후 지갑 및 relay 작업을 계속했습니다. [PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853)은 relay 관리 화면에 [NIP-45](/ko/topics/nip-45/) (Event Counting) COUNT 쿼리를 추가하여, 사용자가 각 relay가 홈 피드, 알림, DM, 인덱스 데이터에 대해 실제로 보유하고 있는 이벤트 수를 볼 수 있게 합니다. [PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849)는 [NIP-17](/ko/topics/nip-17/) (Private Direct Messages) 채팅을 위한 암호화 파일 업로드를 추가하며, 스토리지 호스트가 암호화 버전을 거부할 때 비암호화 업로드로의 재시도 경로도 포함합니다.

[PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791)은 또한 하트비트 표시기가 포함된 완전한 [NIP-46](/ko/topics/nip-46/) (Nostr Connect) 데스크톱 벙커 로그인을 제공합니다. 이는 원격 서명 실패가 사용자 측에서 무작위 UI 오류처럼 느껴지는 경우가 많기 때문에 중요합니다. 클라이언트는 서명자가 활성 상태인지와 가장 최근에 응답한 시점을 표시하며, 현재 세션이 벙커를 사용할 때 이를 명확하게 보여줍니다.

### Nostria

로컬 우선 스택으로 구축된 멀티 플랫폼 클라이언트 [Nostria](https://github.com/nostria-app/nostria)가 피드와 스레드 답글에 대한 Web of Trust 필터링을 추가하는 [PR #561](https://github.com/nostria-app/nostria/pull/561)을 병합했습니다. 이 기능은 기존 신뢰 서비스 순위 데이터를 사용하며, 피드 필터와 답글 필터 모두로 노출하여 임계값을 통과하지 못하는 저자를 숨기면서도 신뢰할 수 있는 하위 항목이 있을 때 스레드 구조를 보존합니다. 이를 통해 사용자는 "모두 보기"와 하드코딩된 목록 기반 큐레이션 사이의 중간 레이어를 얻습니다.

같은 주에 요약 페이지에 콘텐츠 필터링과 리포스트 지원을 추가하는 [PR #563](https://github.com/nostria-app/nostria/pull/563)도 도착했습니다. 추적된 PR 목록 외에도, Nostria는 파워 유저 인터페이스를 더 많이 채워왔습니다. 이제 인앱 가입이 가능한 최신 Brainstorm Web of Trust 서비스, NWC와 BOLT-11 인보이스를 사용한 DM 내 송금 및 수금 흐름, 이모지 NIP을 통한 Nostr 네이티브 GIF 처리, 팟캐스트 피드에서 기존 Lightning 분할을 가져올 수 있는 더 강력한 RSS 임포트 경로를 지원합니다. Nostria는 랭킹, 미디어, 결제, 게시를 하나의 연결된 앱 표면으로 취급하고 있습니다.

### Nostur

nostur-com이 유지 관리하는 iOS 클라이언트 [Nostur](https://github.com/nostur-com/nostur-ios-public)가 outbox 라우팅을 고정 계획에서 점수화된 정책으로 변경하는 [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53)을 열었습니다. 이 패치는 무작위 relay 점수, 캐시된 nostr.watch 피드를 사용한 [NIP-66](/ko/topics/nip-66/) relay 활성 필터링, Thompson 샘플링을 추가하여 relay 성공 및 실패 데이터가 이후 선택에 반영됩니다. 설계는 너무 많은 relay가 필터링될 때의 안전 밸브를 유지하고 `.onion` relay를 보존합니다. 이는 클라이언트가 relay 선택을 적응형 시스템으로 취급하는 가장 명확한 현재 사례 중 하나입니다.

### Nostrability Outbox

[이전 Outbox 벤치마크 보고서에 이어](/ko/newsletters/2026-03-04-newsletter/), [NIP-65](/ko/topics/nip-65/)와 [NIP-66](/ko/topics/nip-66/) 클라이언트 라우팅에 초점을 맞춘 벤치마크 및 분석 프로젝트 [Nostrability Outbox](https://github.com/nostrability/outbox)가 이번 주 자체 주장을 강화하는 데 시간을 보냈습니다. [PR #35](https://github.com/nostrability/outbox/pull/35)는 부풀린 Thompson 샘플링 결과를 1,511회 실행에 걸친 전면 재벤치마크로 대체하고 NDK 스타일 라우팅을 위한 `CG3` 변형을 권장합니다. [PR #43](https://github.com/nostrability/outbox/pull/43)은 감쇠 및 사용 사례 비교를 추가하고, `0 follows` 캐시 오염 버그를 수정한 후 캐시 TTL을 고정하고 Telluride 데이터셋을 재실행합니다.

이것은 일반적인 의미의 제품 작업은 아니지만, 프로젝트의 수치가 이제 더 날카롭고 이전에 과대 주장한 부분에서 덜 화려하기 때문에 클라이언트 저자에게 중요합니다. 수정된 결과는 여전히 유용합니다. 무작위 선택은 Outbox가 관심을 가지는 사례에서 순수하게 결정론적인 라우팅을 지속적으로 능가하며, Thompson 스타일 학습은 클라이언트가 유용한 relay 이력을 유지할 때 커버리지를 실질적으로 향상시킬 수 있고, [NIP-66](/ko/topics/nip-66/) 활성 필터링은 죽은 relay에 대한 낭비 시간을 줄입니다. 이 작업은 또한 구체적인 구현 제안으로 전환되고 있으며, [NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387), [Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53), [Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833), [rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282), [welshman #53](https://github.com/coracle-social/welshman/pull/53), [applesauce #54](https://github.com/hzrd149/applesauce/pull/54) 및 [applesauce #55](https://github.com/hzrd149/applesauce/pull/55)가 포함됩니다.

### White Noise 백엔드

White Noise와 기타 Marmot 도구에서 사용하는 Rust 백엔드 [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)가 Blossom 미디어 처리 주변에 두 개의 경계 강화 패치를 병합했습니다. [PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637)은 Blossom URL에 HTTPS를 강제하고 업로드 타임아웃을 추가하며, [PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642)는 blob 다운로드를 `100 MiB`로 제한하여 과대한 미디어 풀이 서비스 거부 경로로 변하는 것을 차단합니다. 개인 메시징 소프트웨어의 경우 미디어 URL은 암호화된 애플리케이션 로직과 신뢰할 수 없는 네트워크 인프라 사이의 가장 날카로운 인터페이스 중 하나입니다. 이번 주 팀은 그 경계를 강화했습니다.

### rust-nostr

Rust 프로토콜 라이브러리 [rust-nostr](https://github.com/rust-nostr/nostr)가 `LocalRelayBuilderNip42`에 편의 생성자를 추가하는 [PR #1280](https://github.com/rust-nostr/nostr/pull/1280)을 병합했습니다. 새로운 읽기 및 쓰기 헬퍼는 임베디드 relay와 테스트 설정에 [NIP-42](/ko/topics/nip-42/) 인증 정책을 코드로 변환하는 더 명확한 방법을 제공합니다. 이는 작은 라이브러리 패치이지만, 매번 보일러플레이트를 반복하지 않고 인증이 활성화된 로컬 또는 앱 번들 relay를 구축하는 팀에게 중요합니다.

### Pika

[이전 Pika 보도에 이어](/ko/newsletters/2026-03-04-newsletter/), Marmot 기반 메시징 앱 [Pika](https://github.com/sledtools/pika)가 런타임 통합에 초점을 맞춘 릴리스 주기로 [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1)과 [pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1)을 출시했습니다. [PR #542](https://github.com/sledtools/pika/pull/542)는 CLI와 사이드카를 위한 공유 Marmot 런타임 파사드를 도입하며, 앱 호스트가 동일한 표면으로 이동합니다. [PR #556](https://github.com/sledtools/pika/pull/556)은 OpenClaw 에이전트 수명 주기와 프로비저닝 상태를 강화하고, [PR #600](https://github.com/sledtools/pika/pull/600)은 관리 환경을 위한 백업에서 복원과 더 엄격한 복구 안전성을 추가합니다.

여기서 직접적인 사용자 대면 표면은 지난 Pika 기사보다 작지만, 아키텍처 변경은 의미가 있습니다. 그룹, 미디어, 통화, 세션 로직을 하나의 공유 런타임 뒤로 가져오면 Marmot 스택이 성장함에 따라 앱과 데몬이 서로 엇나갈 가능성이 줄어듭니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-54](/ko/topics/nip-54/) (Wiki): Asciidoc에서 Djot으로 전환** ([PR #2242](https://github.com/nostr-protocol/nips/pull/2242)): kind `30818`의 위키 콘텐츠가 이제 Djot을 정규 마크업 형식으로 사용합니다. 병합된 텍스트는 명시적 위키링크 동작, kind `818`에 대한 병합 요청 예제, kind `30819`에 대한 리디렉트 예제, `d` 태그에 대한 비라틴 정규화 예제를 추가합니다. 이는 구현자에게 Asciidoc보다 더 깔끔한 파싱 대상을 제공하고 Ruby 중심 도구 체인에 의존하는 사양 경로 하나를 더 제거합니다.

- **[NIP-19](/ko/topics/nip-19/) (Bech32-Encoded Entities): 입력 제한 추가** ([PR #2264](https://github.com/nostr-protocol/nips/pull/2264)): 사양이 이제 Bech32 인코딩된 엔티티 문자열을 5000자로 제한할 것을 권장합니다. 이는 작은 변경이지만 실질적인 파서 가치가 있습니다. NIP-19 문자열이 이제 많은 클라이언트에서 QR 흐름, 딥 링크, 공유 시트, 사용자 입력 전반에 나타나기 때문입니다.

**오픈 PR 및 논의:**

- **[NIP-49](/ko/topics/nip-49/) (Private Key Encryption)를 위한 Nostr Key File** ([PR #2269](https://github.com/nostr-protocol/nips/pull/2269)): 비밀번호로 암호화된 키 내보내기 및 가져오기를 위한 `.nostrkey` 파일 형식을 제안합니다. 병합되면 클라이언트에 원시 `ncryptsec` 문자열을 복사하는 것보다 더 일반적인 파일 기반 백업 경로를 제공할 것입니다.

- **[NIP-43](/ko/topics/nip-43/) (Relay Access Metadata and Requests)의 멤버십 상태 일관성** ([PR #2267](https://github.com/nostr-protocol/nips/pull/2267)): relay가 pubkey당 하나의 권위 있는 멤버십 상태를 유지해야 한다는 섹션을 추가합니다. 이를 통해 멤버십 변경과 재생된 기록에 대한 그룹 클라이언트 로직이 단순화됩니다.

- **[NIP-17](/ko/topics/nip-17/) (Private Direct Messages)에 대한 삭제 안내** ([PR #2260](https://github.com/nostr-protocol/nips/pull/2260)): gift wrap된 삭제 이벤트를 통한 개인 메시지 편집 및 삭제의 구체적인 경로를 제안합니다. 작업은 아직 진행 중이지만, NIP-17이 이전 DM 흐름을 완전히 대체하려면 클라이언트 저자에게 답이 필요합니다.

- **[NIP-222](/ko/topics/nip-222/)를 위한 공유 인텐트 URI** ([PR #2266](https://github.com/nostr-protocol/nips/pull/2266)): 모바일 및 데스크톱 앱이 공유 콘텐츠를 Nostr 클라이언트에 전달하는 방법을 표준화하는 초안입니다. 이는 현재 앱 간 흐름에서 가장 거친 상호운용성 경계 중 하나입니다.

## NIP 심층 분석: NIP-94 (File Metadata)

[NIP-94](/ko/topics/nip-94/)는 kind `1063`을 파일의 일급 메타데이터 이벤트로 정의합니다. [사양](https://github.com/nostr-protocol/nips/blob/master/94.md)은 이벤트에 사람이 읽을 수 있는 `content`와 다운로드 URL, MIME 타입, 해시, 크기, 미리보기, 대체 소스, 스토리지 서비스 힌트를 위한 기계 판독 가능 태그를 제공합니다. 이것이 중요한 이유는 파일이 relay에서 자체 객체로 쿼리 가능해지기 때문입니다. 클라이언트가 파일이 무엇인지 이해하기 위해 주변 콘텐츠에서 메타데이터를 추출할 필요가 없습니다.

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

태그는 처음 보이는 것보다 더 많은 작업을 수행합니다. `x`는 제공된 파일을 식별하고, `ox`는 서버 측 변환 전의 원본 파일을 식별합니다. 미리보기 태그는 클라이언트가 전체 자산을 다운로드하지 않고 탐색 가능한 파일 인덱스를 구축할 수 있게 하며, `summary`는 그 옆에 짧은 발췌문을 제공할 수 있습니다. `fallback`은 메인 URL이 실패할 때 두 번째 소스를 제공하고, `service`는 [NIP-96](/ko/topics/nip-96/) 또는 다른 호스트와 같은 파일 뒤의 스토리지 프로토콜을 암시합니다. 따라서 NIP-94는 소셜 게시 아래, 원시 스토리지 위에 위치합니다. 파일 주변의 대화가 아닌 파일을 설명합니다.

그래서 이번 주의 Notedeck 업데이터가 흥미롭습니다. [PR #1326](https://github.com/damus-io/notedeck/pull/1326)은 소프트웨어 릴리스 검색에 서명된 kind `1063` 이벤트를 사용한 다음 게시된 SHA256에 대해 다운로드된 바이너리를 검증합니다. 동일한 이벤트 형태가 소프트웨어 아티팩트나 미디어 업로드를 설명할 수 있습니다. NIP-94는 안정적일 만큼 오래되었지만, 더 많은 프로젝트가 메타데이터 이벤트를 사람을 위한 장식이 아닌 기계를 위한 전송으로 취급하고 있기 때문에 성장할 여지가 아직 있습니다.

## NIP 심층 분석: NIP-54 (Wiki)

[NIP-54](/ko/topics/nip-54/)는 kind `30818`을 위키 문서 이벤트로 정의합니다. [사양](https://github.com/nostr-protocol/nips/blob/master/54.md)은 `d` 태그를 정규화된 문서 주제로 취급하고 많은 저자가 같은 주제에 대한 항목을 게시할 수 있게 합니다. 문서 본문은 `content`에 들어가고, 태그는 정규화된 신원, 표시 제목, 요약, 이전 버전에 대한 참조를 처리합니다. 이는 NIP-54가 단순한 콘텐츠 형식이 아님을 의미합니다. 각 클라이언트가 여전히 어떤 문서 버전을 보여줄지 결정해야 하므로, 검색 및 랭킹 문제이기도 합니다.

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

이번 주 병합은 [PR #2242](https://github.com/nostr-protocol/nips/pull/2242)에서 정규 마크업을 Asciidoc에서 Djot으로 변경합니다. 이것이 구현자에게 중요한 이유는 Djot이 더 타이트한 독립 사양과 언어 간 더 단순한 파서 이야기를 가지고 있기 때문입니다. 병합된 텍스트는 또한 참조 스타일 위키링크가 해석되는 방법, 병합 요청이 kind `818`을 사용하는 방법, 리디렉트가 kind `30819`를 사용하는 방법, 비라틴 스크립트에 대해 `d` 태그 정규화가 어떻게 동작해야 하는지를 명확히 합니다. 이것들이 두 개의 독립적인 클라이언트가 링크가 가리키는 문서에 동의하게 만드는 부분입니다.

NIP-54는 또한 프로토콜에서 특이한 위치에 있습니다. 위키 클라이언트는 콘텐츠 렌더링이 필요하지만, 랭킹 정책도 필요합니다. 리액션, relay 목록, 연락처 목록, 명시적 존중 신호가 모두 주어진 주제에 대해 어떤 문서가 승리하는지에 영향을 줍니다. Djot 전환이 랭킹 문제를 해결하지는 않지만, 그 아래에 있던 파서 모호성 중 하나를 제거합니다. 그래서 이 병합이 지금 중요합니다: 변경은 더 나은 산문 형식보다는 다중 클라이언트 위키 동작을 일관되게 구현하기 쉽게 만드는 것에 더 관련됩니다.

무언가를 만들고 있거나 보도를 원하시나요? Nostr에서 `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`으로 [NIP-17](/ko/topics/nip-17/) DM을 통해 연락해 주세요.
