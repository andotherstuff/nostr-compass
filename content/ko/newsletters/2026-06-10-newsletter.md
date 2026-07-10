---
title: 'Nostr Compass #26'
date: 2026-06-10
publishDate: 2026-06-10
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-10-newsletter.md
translationDate: 2026-07-08
---

Marmot Protocol 조직이 v2 프로토콜 초안과 네이티브 클라이언트 계보를 위해 세 개의 새 저장소를 공개했습니다: `darkmatter`라는 Rust 워크스페이스, SwiftUI iOS 앱 `darkmatter-ios`, Kotlin/Compose Android 앱 `darkmatter-android`. 원래의 Flutter Whitenoise는 아카이브되었습니다. Chama는 17개의 릴리스를 일주일에 압축하여 v3.0.0에서 독립 앱 라인을 넘어선 뒤 v3.1.0에서 전체 거래방 UI 재작성과 판매자별 상점을 실현했으며, 이는 홀더 전용 Shamir 공유, 중재자 대체, 전 세계 커뮤니티 라우팅, 종단 간 거래 알림 위에 구축되었습니다. Coracle은 오픈 소스 Caravel과 zooid 스택에 의해 지원되는 유료 호스팅 릴레이 서비스를 출시했으며, 심층 Flotilla 통합이 계획되어 있습니다. Angor는 v0.2.30에서 기본값을 mainnet으로 전환하고 v0.2.29에서 3명 사용자 UAT 자금 조달 테스트를 실현했습니다. Amethyst는 지난주의 NIP-32 / NIP-F4 / Tor 작업을 계속하는 41개의 미출시 PR을 실현했습니다. NIP-67 (EOSE 완전성 힌트)과 NIP-50 자동완성이 병합되어 코어 릴레이 프로토콜의 두 가지 오랜 정확성 격차를 닫았습니다. NIP-GART는 긴급 경보를 위한 프라이버시 보존 와이어 형식을 제안하고, NIP-46은 logout 메서드를 얻었습니다.

## 주요 소식

### Marmot v2 (Dark Matter): 프로토콜 재초안, 네이티브 클라이언트, 아카이브된 Flutter 앱

이번 주 [marmot-protocol](https://github.com/marmot-protocol) GitHub 조직 아래에 세 개의 새 저장소가 나타났으며, 함께 Marmot v2 프로토콜 초안과 Flutter 앱 라인을 대체하는 네이티브 클라이언트 계보의 초기 진행 형태를 형성합니다. [`darkmatter`](https://github.com/marmot-protocol/darkmatter) (Rust, 5월 13일 생성, 지난 7일간 34개 커밋)는 `spec/`에 v2 프로토콜 초안, `crates/cgka-engine`에 OpenMLS 기반 CGKA 엔진, 속성 테스트가 있는 적합성 시뮬레이터, 수렴 증명을 위한 Tamarin 형식 모델을 보유합니다. [`darkmatter-ios`](https://github.com/marmot-protocol/darkmatter-ios) (Swift, 5월 25일 생성)는 Rust 워크스페이스에서 생성된 벤더된 `MarmotKit` UniFFI xcframework에 의해 지원되는 SwiftUI 클라이언트입니다. [`darkmatter-android`](https://github.com/marmot-protocol/darkmatter-android) (Kotlin/Jetpack Compose, 5월 25일 생성)는 동일한 Rust 바인딩 위에 있습니다. 원래의 Flutter Whitenoise는 [`whitenoise-archive`](https://github.com/marmot-protocol/whitenoise-archive)로 표시되었으며 ("ARCHIVED: 이것은 원래의 White Noise Flutter 앱이었습니다"), 새 [`whitenoise`](https://github.com/marmot-protocol/whitenoise) Dart 저장소가 활성 Flutter 라인을 병렬로 운반합니다.

이것을 완성된 피벗이 아니라 더 신뢰할 수 있는 Marmot을 향한 초기 진행으로 읽으십시오. darkmatter README는 자신을 "Marmot v2 프로토콜 초안, CGKA 엔진, 적합성 워크스페이스 후보"로 라벨링하고 직접 말합니다: "이 초안과 엔진이 채택될 때까지 MDK는 배포된 Rust 프로토콜 구현으로 남습니다". 워크스페이스 내에서 cgka-engine 크레이트는 `0.1.0`으로 태그되어 있으며, "단일 내부 소비자, semver 안정성 없음"입니다. 모든 사양 페이지는 "상태: 내부 검토용 초안"을 담고 있습니다. 워크스페이스 저장소의 별 세 개와 iOS 및 Android 앱의 별 0개는 작업이 사전 공지 상태임을 확인합니다. 방향, 범위, 규율이 여기서의 신호입니다; 프로덕션 준비 상태는 주장되지 않았습니다.

프로토콜 초안은 v1에서 v2로의 델타를 구체화합니다. Marmot 시작 이래 그룹 이름, 설명, 관리자 pubkey, Nostr 그룹 라우팅 id, 릴레이 목록, 그룹 이미지 데이터, 사라지는 메시지 설정을 하나의 우산 아래 운반해 온 MIP-01의 모놀리식 `marmot_group_data` MLS 확장은 [버전화된 앱 컴포넌트로 분할](https://github.com/marmot-protocol/darkmatter/blob/master/spec/mip-coverage.md)됩니다: 이름과 설명을 위한 `marmot.group.profile.v1`, 관리자 pubkey를 위한 `marmot.group.admin-policy.v1`, 무작위 `nostr_group_id`와 정규 릴레이 목록을 위한 `marmot.transport.nostr.routing.v1`, 이미지 해시, 암호화 키, nonce, 업로드 키를 위한 `marmot.group.blossom.image.v1`, 사라지는 메시지 초 수를 위한 `marmot.group.message-retention.v1`. 각 컴포넌트는 정확한 바이트와 자체 버전 관리 경로를 소유하므로, 미래의 기능은 나머지 그룹 상태가 MLS 확장 합의를 다시 밟도록 강제하지 않고 하나의 컴포넌트를 개정할 수 있습니다. MIP-00 자격 증명도 새 기초 문서 `account-identity-proof-v1.md`를 얻었으며, "v2에서 새로운 것이며 파괴적"으로 호출됩니다. 신원 증명은 이제 KeyPackage 구성과 별개로 자체 표면에 존재합니다.

라이브러리 델타는 사양 재작업을 뒷받침합니다. `cgka-engine`은 새 로컬 그룹 상태 머신입니다: OpenMLS를 래핑하고, `Stable`, `PendingPublish`, `Merging`, `Recovering` 에폭 상태를 소유하며, 의도를 MLS 커밋으로 변환하고, 모든 인바운드 전송 봉투에 대해 타입 지정된 `IngestOutcome`과 `GroupEvent` 값을 반환하며, 명시적으로 전송도 지속성도 출시하지 않습니다. `TransportPeeler` trait는 Nostr을 엔진에서 분리하고, `StorageProvider` trait는 SQLite (SQLCipher 지원 `storage-sqlite`를 통해)를 엔진에서 분리합니다. 오늘의 MDK는 이 모든 것을 함께 포장합니다; 계층을 분할하면 하나의 엔진이 지금 Nostr 릴레이 전송 아래에 위치하고, 수렴 모델을 다시 작성하지 않고도 나중에 함께 출시된 [QUIC 스트림과 브로커 전송](https://github.com/marmot-protocol/darkmatter/blob/master/docs/quic-broker-deployment.md) 아래에도 위치할 수 있습니다. 수렴 자체는 `distributed-convergence.md`로 문서화되어 있으며, 결정론적 브랜치 선택, 정책 게이트 자격, 유지된 앵커 재생, 오래된 브랜치 거부, 배송 재정렬, 중복, 앱 출력 무효화, welcome/commit 핸드오프, 제안 소비, 동기화 중 아웃바운드 게이팅을 다루는 Tamarin 모델에서 증명되었습니다. 그런 다음 Rust 속성 테스트는 엔진이 실제 OpenMLS 객체와 시뮬레이터 하네스로 동일한 규칙을 따르는지 확인합니다. 이 범위의 형식적 방법 신뢰성 작업은 현재 Marmot 스택에는 없습니다.

두 네이티브 클라이언트 모두 플랫폼 네이티브 UI 툴킷을 위해 Flutter를 삭제합니다. [`darkmatter-ios`](https://github.com/marmot-protocol/darkmatter-ios)는 MIP-05 푸시 웨이크를 디바이스에서 해독하는 Notification Service Extension을 갖춘 순수 SwiftUI이며, Rust 워크스페이스에서 빌드된 생성된 `MarmotKit` Swift 패키지를 벤더링하고, `dev.ipf.darkmatter` 번들 ID 및 앱 그룹 아래에 등록됩니다. [`darkmatter-android`](https://github.com/marmot-protocol/darkmatter-android)는 Kotlin과 Jetpack Compose이며, `just` 기반 빌드가 서명된 `arm64-v8a` APK를 생성하고 `local.properties`에서 텔레메트리 엔드포인트를 읽습니다. Android README는 아키텍처 원칙을 직접 명시합니다: "Dark Matter는 프로토콜 데이터를 소유하고 SQLite에 저장합니다. Android 앱은 그 데이터를 렌더링하고, Android 플랫폼 동작을 관리하며, UI 라이프사이클 상태를 유지해야 합니다. Android 앱은 Dark Matter 데이터를 위한 두 번째 데이터베이스가 되어서는 안 됩니다". 이는 UI 계층에 적용된, cgka-engine README가 Rust 계층에서 강제하는 경계 규율을 반영합니다.

Marmot에게 네이티브 클라이언트가 중요한 이유는 프로토콜의 가장 많이 인용되는 약점이 불균일한 배송 조건에서 모바일 신뢰성이었기 때문입니다: 마감을 놓친 알림 웨이크, 네트워크 플랩 중 MLS 커밋 경쟁, 에폭 진행을 좌초시키는 백그라운드 페치 한도. SwiftUI와 Compose는 Flutter가 플러그인 브리지를 통해 도달하는 플랫폼 백그라운드 처리 프리미티브에 대한 직접 액세스를 클라이언트에 제공하고, UniFFI 바인딩 경로는 두 플랫폼에서 정적 라이브러리로 출시되는 하나의 Rust 워크스페이스에 프로토콜 로직을 유지합니다. Flutter Whitenoise 라인은 아카이브되지 않은 [`whitenoise`](https://github.com/marmot-protocol/whitenoise) 저장소에서 계속되므로 공지는 추가적입니다: v2 사양이 수렴하는 동안 새 네이티브 클라이언트 계보가 Flutter 앱과 병렬로 실행됩니다. MDK 또는 현재 Whitenoise 앱에서의 프로덕션 전환은 초안, 엔진, 클라이언트가 프로덕션 준비 릴리스에 도달하는 것을 기다립니다.

### Chama v2.0.0에서 v3.1.0까지: 일주일 만의 독립 P2P 에스크로

뉴스레터 #25에서 v1.3.0으로 소개된 Nostr 네이티브 P2P 에스크로 클라이언트는 지난 7일 동안 17개의 태그된 릴리스를 출시했으며, 6월 9일 [v3.1.0](https://github.com/jesuspirate/chama/releases/tag/v3.1.0)에서 거래방 UI 재작성 및 판매자별 상점으로 끝났습니다. 버전 자취가 이야기를 말합니다: [v2.0.0](https://github.com/jesuspirate/chama/releases/tag/v2.0.0)은 파괴적 베이스이며, 그런 다음 [v2.0.1](https://github.com/jesuspirate/chama/releases/tag/v2.0.1), [v2.0.2](https://github.com/jesuspirate/chama/releases/tag/v2.0.2), [v2.0.3](https://github.com/jesuspirate/chama/releases/tag/v2.0.3)은 Fedi WebView 자금 조달 레일 격차를 닫습니다; [v2.1.0](https://github.com/jesuspirate/chama/releases/tag/v2.1.0), [v2.2.0](https://github.com/jesuspirate/chama/releases/tag/v2.2.0), [v2.3.0](https://github.com/jesuspirate/chama/releases/tag/v2.3.0), [v2.3.1](https://github.com/jesuspirate/chama/releases/tag/v2.3.1)은 중재자 계층을 강화합니다; [v2.4.0](https://github.com/jesuspirate/chama/releases/tag/v2.4.0), [v2.5.0](https://github.com/jesuspirate/chama/releases/tag/v2.5.0), [v2.6.0](https://github.com/jesuspirate/chama/releases/tag/v2.6.0)은 자기 수탁 표면과 전 세계 커뮤니티 라우팅을 추가합니다; [v2.7.0](https://github.com/jesuspirate/chama/releases/tag/v2.7.0), [v2.8.0](https://github.com/jesuspirate/chama/releases/tag/v2.8.0), [v2.9.0](https://github.com/jesuspirate/chama/releases/tag/v2.9.0), [v2.10.0](https://github.com/jesuspirate/chama/releases/tag/v2.10.0)은 평이한 영어 키 복사, 그룹 신청, 분쟁 마감 중재, 평판을 계층화합니다. [v3.0.0](https://github.com/jesuspirate/chama/releases/tag/v3.0.0)은 종단 간 거래 알림으로 패키지를 묶고, 6월 9일 [v3.1.0](https://github.com/jesuspirate/chama/releases/tag/v3.1.0)은 Reserved → Locked → Settled 진행 척추, 역할 색상 액션 카드, 판매자별 상점 리스팅 클래스 (큐레이션된 스왑, 대출장, 청구서) 주위에 거래 화면을 재작성합니다.

아키텍처 피벗은 v2.0.0에 있습니다. 에스크로 LOCK 형식이 변경되어 2-of-3 Shamir 분할의 각 공유가 그 소지자에게만 암호화됩니다 (sharePolicy `holder-only-v1`). 페더레이션의 무기명 ecash는 더 이상 단일 참가자로부터만 재구성되지 않으므로, 자신의 공유와 페더레이션 보유 공유 모두를 가진 악의적인 당사자가 동의 없이 거래를 완료할 수 있는 경로가 닫힙니다. 2.0 이전 클라이언트는 "공유를 찾을 수 없음"으로 큰 소리로 실패합니다; 거래는 오래된 클라이언트에서 완료될 수 없으며, 그 과정에서 자금은 손실되지 않습니다. v2.0 잠금은 결제하기 위해 v2.x의 모든 당사자가 필요합니다. v2.0.0은 또한 다중 유닛 상점과 sats 전용 마켓 뷰를 추가했습니다.

v2.1.0은 중재자 대체를 도입했습니다: Shamir 인덱스 2의 중재자 공유는 커뮤니티 중재자 풀 위의 결정론적 우선순위에 암호화되므로, 부재중인 중재자는 거래를 좌초시키지 않고 대체될 수 있습니다. v2.2.0은 ₿121 거래에서 야생에서 대체가 작동함을 증명하고 힐링 대체 백업을 추가했습니다. v2.3.0은 잠금 시 리스팅 중재자 커뮤니티 멤버십을 확인함으로써 마지막 중재자 프론트러닝 격차를 닫았고, v2.3.1은 자동 할당된 중재자 슬롯이 잠금이 그들을 앉힐 때까지 미리보기였던 형제 경쟁을 닫았습니다.

자기 수탁 표면은 v2.4.0 (Nostr에 암호화되어 저장된 Fedimint ecash 지갑용 BIP-39 복구 문구)과 v2.5.0 (Nostr 신원과 지갑 시드를 소유하는 마스터 nsec 백업)에서 도착했습니다. v2.6.0은 로컬 Chama가 없는 국가의 사용자를 가장 가까운 페더레이션으로 라우팅하는 글로벌 커뮤니티 선택기 주위로 온보딩을 재작업했습니다; 이전 빌드는 폴백 없이 사용자를 되돌렸습니다. v2.7.0은 복구 키 화면을 평이한 영어로 다시 작성했습니다 ("계정과 그 안의 돈에 대한 유일한 키; Chama는 그것을 결코 보지 않으며 재설정할 수 없습니다; 잃어버리면 누구도 계정을 되찾을 수 없습니다"). v2.8.0은 그룹 신청, 다크/라이트 테마, 두 개의 새 이벤트 kind (38120 명부, 38121 신청)를 추가했습니다. v2.9.0은 마감 시 분쟁 해결을 변경했습니다: 만료에 도달한 경합 거래는 이제 중재자 판결로 해결됩니다; 이전 동작은 자동 환불이었습니다. 릴리스는 COORDINATED로 표시되어 있으므로 분쟁의 모든 당사자가 업데이트해야 합니다. v2.10.0은 새 이벤트 kind 38123으로 거래별 엄지 위/엄지 아래 평가를 추가했습니다.

v3.0.0은 앱이 작동하기 위해 조정 커뮤니티를 필요로 하지 않는 이정표입니다. 종단 간 거래 알림은 실행 가능한 상태 전환에서만 사용자에게 ping합니다: 상대방이 sats를 잠갔음, 지급 준비 완료, 분쟁이 중재자로서 사용자의 판결을 요구함, 또는 거래가 결제되거나 만료됨. Me 화면의 하나의 토글이 알림을 켜거나 끄고, 권한 프롬프트는 토글이 활성화될 때만 실행됩니다. fire-once dedup은 상태 재로드가 경보 폭풍을 트리거하지 않도록 유지합니다. 잘못된 chama 가드레일 버그도 [PR #103](https://github.com/jesuspirate/chama/pull/103)에서 닫혔습니다. 이전 버전은 하나의 chama의 라벨로 다른 chama의 페더레이션을 가진 리스팅을 스탬프할 수 있었습니다. Windows와 Linux 데스크톱 번들이 릴리스와 함께 출시됩니다; macOS dmg는 서명과 공증이 도착할 때까지 보류됩니다.

Chama는 이제 Mostro와 Shopstr에 Nostr 네이티브 마켓플레이스로 합류하며, 서버리스 아키텍처, Fedimint 지원 2-of-3 Shamir 에스크로, 소지자 전용 공유 암호화, 그리고 세 개 중 조정 커뮤니티 없이 자립형 데스크톱 및 모바일 클라이언트를 출시하는 유일한 것으로 구별됩니다.

### Coracle Hosting: 유료 릴레이 서비스와 오픈 소스 Caravel 스택

6월 3일 Hodlbod가 [hosting.coracle.social](https://hosting.coracle.social)에서 [Coracle Hosting을 발표](https://nos.lol/e/f8586160cd12df479c261397353c99e6f3e4d870b616382e1b4338bad3ab498a)했습니다. 이는 NWC 또는 카드를 통해 반복적인 lightning 결제를 받는 호스팅 커뮤니티 릴레이 서비스입니다. 서비스는 Coracle의 청구 및 프로비저닝 프론트엔드인 [Caravel](https://gitea.coracle.social/coracle/caravel)과 단일 머신에서 많은 가상 릴레이를 호스팅하는 릴레이 런타임 [zooid](https://gitea.coracle.social/coracle/zooid)에 의해 지원됩니다. 둘 다 Coracle의 자체 호스팅 gitea에서 오픈 소스입니다. Caravel은 운영자가 릴레이별로 전환할 수 있는 선택적 [livekit](https://livekit.io) 및 [Blossom](/ko/topics/blossom/) 통합과 함께 출시됩니다. 회원 수 제한이 있는 무료 티어를 통해 운영자는 결제 세부 정보를 제출하기 전에 서비스를 평가할 수 있습니다.

Hodlbod는 비즈니스 모델에 대해 솔직합니다: 다른 사람도 실행할 수 있는 스택의 호스팅 버전을 판매함으로써 오픈 소스로 수익화합니다. 경쟁적 해자는 다음 계획 단계인 [Flotilla](https://flotilla.social) 통합입니다. Flotilla는 사용자 표면을 소유하므로 Flotilla 내부에서 제공되는 호스팅 옵션은 관리형 인프라를 선호하는 사용자를 위한 기본 경로가 됩니다. Hodlbod는 다른 Caravel 운영자가 연락하면 Flotilla의 대체 호스팅 선택기에 추가할 것을 제안했으며, 연합 호스팅 시장으로의 문을 열어 두었습니다.

Caravel은 유료 회원 티어를 가진 공개 Nostr 릴레이 프로비저닝 플랫폼으로 [relay.tools](https://relay.tools)에 합류합니다. relay.tools는 Caravel보다 앞서 있으며 오늘날 지배적인 릴레이 생성 서비스로 출시되어 커뮤니티 릴레이의 자체 디렉토리와 유료 회원 또는 조정자 참여 흐름을 갖추고 있습니다. Caravel의 구별되는 특징은 조정된 스택입니다: 릴레이 런타임 (zooid), 청구 및 프로비저닝 프론트엔드 (Caravel 자체), 클라이언트 측 선택기 (Flotilla 통합, 아직 진행 중)가 하나의 설계로 출시됩니다. 다른 구별되는 특징은 zooid의 프로세스당 다중 릴레이 밀도이며, 여기서 고객 릴레이는 단일 호스트 프로세스를 공유하므로 운영자는 많은 작은 커뮤니티에 걸쳐 호스팅 비용을 상각합니다. 이것은 2000년대 초 공유 웹 호스팅을 실행 가능하게 만든 것과 동일한 밀도 논쟁이며, Nostr의 릴레이 계층에 적용됩니다.

## 릴리스

### Angor v0.2.29 및 v0.2.30: mainnet 기본값 및 3명 사용자 UAT 자금 조달 테스트

6월 4일 [Angor v0.2.29](https://github.com/block-core/angor/releases/tag/v0.2.29)와 6월 8일 [v0.2.30](https://github.com/block-core/angor/releases/tag/v0.2.30)은 분산 Bitcoin-and-Nostr 자금 조달 프로토콜의 이번 주 두 릴리스입니다. v0.2.30의 헤드라인 변경은 기본 네트워크를 mainnet으로 전환하는 [PR #893](https://github.com/block-core/angor/pull/893)입니다. Angor는 여전히 불안정한 알파 릴리스로 출시되지만, default-mainnet 스위치는 프로토콜이 데스크톱 및 모바일 클라이언트의 testnet 전용 단계를 지났음을 신호합니다. v0.2.30은 또한 이미지 업로드와 스크롤 재설정이 있는 원 탭 모바일 프로젝트 생성 흐름 ([PR #889](https://github.com/block-core/angor/pull/889))을 실현하고 lightning 인보이스 스피너가 매달릴 수 있었던 경쟁 조건을 해결합니다 ([PR #890](https://github.com/block-core/angor/pull/890)).

v0.2.29는 미확인 지출이 있는 10라운드에 걸친 3명 사용자 자금 전송을 다루는 종단 간 UAT 테스트를 [PR #881](https://github.com/block-core/angor/pull/881)에서 추가했으며, 이는 Angor 테스트 스위트에서 첫 번째 다중 사용자 자금 조달 흐름 테스트입니다. 릴리스는 또한 Angor CLI와 MCP 서버의 구현 계획 ([PR #792](https://github.com/block-core/angor/pull/792))을 추가했으며, [PR #880](https://github.com/block-core/angor/pull/880)에서 MCP 테스트 워크플로를 위한 CLI 개선을 수행했습니다. DavidGershony의 [PR #885](https://github.com/block-core/angor/pull/885)는 런타임 네트워크 전환 후 잘못된 네트워크를 사용한 Boltz lightning 인보이스를 수정했으며, 이는 v0.2.30의 mainnet 기본값 이후 프로덕션에서 나타났을 버그입니다. 설정은 이제 데이터 삭제 중 선택적 복구 지갑 파일 정리를 제공합니다 ([PR #883](https://github.com/block-core/angor/pull/883)).

### Sprout v0.3.15: 일시적 채널 TTL 갱신 및 ACP 슬래시 명령

6월 10일에 출시된 [Sprout v0.3.15](https://github.com/block/sprout/releases/tag/v0.3.15)는 6월 2일 v0.3.7로 시작된 실행의 여덟 번째 릴리스입니다. 뉴스레터 #25는 mesh-llm 통합 및 채널 섹션 작업과 함께 v0.3.1에서 v0.3.6 실행을 다루었습니다; v0.3.7에서 v0.3.15는 그 하류이며, 광택과 몇 가지 사용자 대면 추가에 초점을 맞춥니다. 가장 사용자에게 보이는 변경은 [PR #902](https://github.com/block/sprout/pull/902)에서 일시적 채널의 TTL 갱신입니다: 사용자가 일시적 채널을 아카이브 해제하면 Sprout는 채널의 time-to-live를 연장하므로 아카이브 해제는 원래 만료 타이머 아래에서 즉시 재아카이브하지 않습니다. 모바일 커스텀 이모지는 설정 재설계와 함께 [PR #906](https://github.com/block/sprout/pull/906)에 도착하고, 반응 카운트는 이제 변경 시 애니메이션됩니다 ([PR #904](https://github.com/block/sprout/pull/904)).

[PR #905](https://github.com/block/sprout/pull/905)는 여러 단어 표시 이름이 깨지고 [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) `nostr:npub` 언급 추출이 조용히 삭제되는 오랜 격차를 수정합니다. 데스크톱용 디렉토리 기반 팀 UI는 설치, 동기화, 표시 명령과 함께 [PR #912](https://github.com/block/sprout/pull/912)에서 출시됩니다. 슬래시 명령은 이제 [ACP](https://agentclientprotocol.com) 커넥터를 통해 통과합니다 ([PR #919](https://github.com/block/sprout/pull/919)). Sprout UI는 경로에서 벗어나 있으면서 Sprout가 `/help` 스타일 명령을 에이전트 런타임으로 직접 전달할 수 있게 합니다.

### Wisp v1.1.1: Spark 지갑 통합 및 nsec 붙여넣기 가드

6월 5일에 출시된 [Wisp v1.1.1](https://github.com/barrydeen/wisp/releases/tag/v1.1.1)은 [PR #548](https://github.com/barrydeen/wisp/pull/548)에서 [Spark](https://www.spark.money) 하위 화면이 있는 2계층 지갑 연결 화면과 [PR #549](https://github.com/barrydeen/wisp/pull/549)에서 iOS 지갑 UI와의 대시보드 패리티를 실현합니다. 릴리스에는 앱 어느 곳에서든 `nsec1` 접두사 붙여넣기를 감지하고 필드가 그것을 수락하는 것을 차단하여 Nostr UX에서 가장 많이 인용된 풋건 중 하나를 닫는 시스템 전체 [nsec 붙여넣기 가드](https://github.com/barrydeen/wisp/pull/553)가 포함됩니다. QR 스캔 로그인과 `npub` 및 `nprofile`용 감시 전용 모드가 [PR #552](https://github.com/barrydeen/wisp/pull/552)에서 출시되며, 사용자가 프로필을 읽기 전용으로 탐색할 수 있게 합니다. Zap 메시지는 이제 참여 서랍에서 미니 게시물로 렌더링되므로 ([PR #559](https://github.com/barrydeen/wisp/pull/559)), zap 노트는 sat 금액과 함께 텍스트를 운반합니다. 스레드 답글의 신뢰 웹 필터가 [PR #583](https://github.com/barrydeen/wisp/pull/583)에 도착하여, 사용자가 팔로우 그래프 밖의 계정에서 오는 답글 스팸을 숨길 수 있습니다.

### Nostria v3.1.46 및 nospeak 1.1.3: 알림 재작업 및 ICE 재시작

6월 7일 [Nostria v3.1.46](https://github.com/nostria-app/nostria/releases/tag/v3.1.46)은 마지막 보기 이후 새 알림만 계산하도록 알림 카운터를 재작업하는 3릴리스 실행을 종료하며, 스크롤을 통해 오래된 알림을 로드하면 배지 카운트가 부풀려지는 오랜 인플레이션을 제거합니다. [Nostria v3.1.45](https://github.com/nostria-app/nostria/releases/tag/v3.1.45)는 lightning 및 QR 코드 결제에 영향을 미치는 분할 결제 버그를 수정하고 Android의 컴포지터에서 실행 불가능한 것으로 이전에 계획된 반투명 UI를 삭제했습니다.

6월 4일 [nospeak v1.1.3](https://github.com/psic4t/nospeak/releases/tag/v1.1.3)은 1대1 음성 통화에서 FAILED 상태의 ICE 재시작을 추가합니다. 표준 WebRTC 동작은 ICE 후보가 대체 경로 없이 타임아웃될 때 통화를 삭제합니다; ICE 재시작 경로는 후보를 재협상하므로 통화가 일시적인 NAT 또는 네트워크 변경에서 복구됩니다. Android 통화는 이제 비디오 통화 중 화면을 켜둡니다.

## 미출시 변경

### Amethyst: NIP-32 / NIP-F4 / Tor 트랙을 계속하는 41개 PR

Amethyst는 이번 주 릴리스 태그를 자르지 않고 41개의 PR을 병합했으며, 이는 지난주의 52개 PR과 뉴스레터 #25에서 다룬 [NIP-32](/ko/topics/nip-32/) 해시태그 라벨링 및 [NIP-F4](/ko/topics/nip-f4/) 팟캐스트 작업 위에 있습니다. 활성 브랜치는 다음 태그된 릴리스를 위해 기능을 계속 축적하며, 지난주의 헤드라인 추가 위에 광택을 계층화합니다: 해시태그 라벨러 발견, 팟캐스트 화면, 음악 트랙 및 플레이리스트, Tor 자체 치유 워치독, 익명 업로드용 일시적 서명자, NIP-05 필터링이 있는 온체인 zap. Amethyst의 PR 처리량은 모든 Nostr 클라이언트 중 가장 높게 유지되며, 미출시 대기열은 다른 Android Nostr 클라이언트가 매칭해야 할 사실상의 로드맵입니다.

### Damus: OK 메시지의 릴레이 추적 및 v1.17 변경 로그

6월 3일 병합된 [Damus PR #3786](https://github.com/damus-io/damus/pull/3786)는 릴레이의 성공적인 `OK` 메시지를 게시 후 릴레이 목록에 추가합니다. 이전 Damus 빌드는 릴레이에서 일반 메시지를 받을 때만 seen-relays 목록을 채웠으며, 이는 게시물을 확인했지만 이벤트를 되돌려주지 않은 릴레이가 사용자에게 보이지 않았음을 의미했습니다. 이 변경은 게시물이 선호하는 아웃박스 릴레이에 도착했음을 확인하려는 사용자에게 중요합니다. [PR #3796](https://github.com/damus-io/damus/pull/3796)은 프로필 뷰에서 `AttributeGraph` 사이클을 수정하고, [PR #3725](https://github.com/damus-io/damus/pull/3725)는 다음 태그된 릴리스 이전에 v1.17 변경 로그를 실현합니다.

### Shopstr: NIP-34 이중 게시

Shopstr의 [ngit의 shopstr 저장소](https://relay.ngit.dev/npub1u350hpq840naxzkkle4gmdtvzanfxmjd9m9tytn5355aua7jh2cqgfuw39/shopstr.git)가 이번 주 Nostr에서 [NIP-34](/ko/topics/nip-34/) git 저장소로 공지되어 ngit의 추적된 저장소에 합류했습니다. 상점 클라이언트의 GitHub 저장소는 여전히 주요 개발 표면입니다; NIP-34 공지는 병렬 git-over-Nostr 협업 경로를 사용할 수 있게 합니다. 이것은 [Mostro](https://relay.ngit.dev/) 이후 NIP-34에 이중 게시하는 두 번째 주요 Nostr 마켓플레이스 프로젝트이며, Nostr의 git 전송으로의 프로젝트 메타데이터 점진적 마이그레이션을 계속합니다.

### Hermes-Marmot: MLS를 통한 AI 에이전트 게이트웨이

[hermes-marmot](https://github.com/notmandatory/hermes-marmot)은 [Hermes Agent](https://github.com/NousResearch/hermes-agent)의 플러그인으로, Rust Marmot Development Kit의 Python 바인딩인 [mdk-python](https://github.com/marmot-protocol/mdk-python)을 사용하여 AI 에이전트의 메시징 표면을 [Marmot](/ko/topics/marmot/) (MLS-over-Nostr) 그룹에 연결합니다. 플러그인을 통해 사용자는 [Whitenoise](https://whitenoise.chat)를 포함하여 kind 445 MLS 메시지를 사용하는 모든 Nostr 클라이언트에서 AI 에이전트에게 DM을 보낼 수 있습니다. 인바운드 DM은 [nostr-sdk](https://github.com/rust-nostr/nostr) Python 바인딩을 통해 [NIP-59](/ko/topics/nip-59/) 기프트 랩 언랩핑을 사용하고, 인바운드 welcome은 `UnwrappedGift.from_gift_wrap`을 통해 `mdk.process_welcome` 및 `mdk.accept_welcome`으로 흐릅니다. 접근 제어는 `MARMOT_ALLOWED_USERS` (쉼표로 구분된 npub 허용 목록) 또는 오픈 개발 접근을 위한 `MARMOT_ALLOW_ALL_USERS=true`를 통해 실행됩니다.

저장소는 새롭고 (마지막 업데이트 5월 27일) 작습니다. 그 중요성은 아키텍처적입니다: LLM 에이전트 런타임과 MLS 암호화된 Nostr 메시징 채널 사이의 첫 번째 공개 브리지이며, Whitenoise 자체를 넘어 mdk-python의 첫 번째 프로덕션 사용입니다. 이 패턴은 두 엔드포인트가 모두 MLS 키를 보유하고 릴레이가 암호문만 보는 에이전트 대 에이전트 통신을 가리킵니다.

## NIP 업데이트 및 프로토콜 사양 작업

### NIP-67 EOSE 완전성 힌트 (PR #2317) 병합

mattn의 [PR #2317](https://github.com/nostr-protocol/nips/pull/2317)이 6월 6일에 병합되어 [NIP-67](/ko/topics/nip-67/)을 프로토콜에 추가했습니다. NIP는 `EOSE` 릴레이 메시지를 선택적 세 번째 요소로 확장합니다: `["EOSE", <subscription_id>, "finish"]`는 필터와 일치하는 모든 저장된 이벤트가 전달되었음을 신호하고, 벌거벗은 `["EOSE", <subscription_id>]`는 완전성 주장을 담지 않습니다. 힌트를 생략하는 릴레이는 클라이언트에게 더 있을 수 있다고 말하고 있습니다; NIP-11에서 NIP-67 광고를 생략하는 릴레이는 기존 레거시 휴리스틱 아래 오늘의 동작을 유지합니다. 변경은 양방향으로 하위 호환됩니다: 레거시 클라이언트는 후행 배열 요소를 무시하고, 레거시 릴레이는 그것을 생략합니다.

병합된 사양의 동기는 두 가지입니다. 첫째, 조용한 데이터 손실: 클라이언트가 300 이벤트 내부 캡을 가진 릴레이에 대해 마지막 500개 노트를 요청하고, 릴레이가 300 이벤트를 반환하며, 클라이언트 (표준 `received < limit` 휴리스틱을 사용)는 결과가 완전하다고 결론짓습니다. 201번째부터 N번째로 오래된 일치하는 노트는 클라이언트가 그 사실을 모른 채 릴레이에 읽지 않은 상태로 남습니다. 둘째, 필수 낭비된 왕복: 릴레이가 응답을 300 이벤트에서 캡할 때, 캡을 소진하는 모든 구독은 필터가 정확히 300 이벤트와 일치하는 경우에도 완료를 확인하기 위해 순전히 `until=<oldest_created_at>`으로 두 번째 `REQ`를 필요로 합니다. 두 실패 모드 모두 모든 캡 소진 구독에서 모든 클라이언트가 지불합니다. `"finish"` 힌트는 하나의 기존 메시지에 있는 하나의 선택적 문자열이며 두 비용을 모두 제거합니다.

### NIP-50 자동완성 확장 (PR #2357) 병합

Alex Gleason의 [PR #2357](https://github.com/nostr-protocol/nips/pull/2357)이 6월 6일에 병합되어 [NIP-50](/ko/topics/nip-50/) 검색에 `autocomplete:true/false` 토큰을 추가했습니다. 확장을 통해 클라이언트가 쿼리를 typeahead 조회로 표시할 수 있으므로 릴레이는 토큰이 없는 쿼리의 기본값으로 전체 텍스트 검색을 사용하면서 접두사 매칭을 사용합니다. Ditto의 릴레이는 이를 팔로우 팩, 목록, `title` 태그가 있는 모든 이벤트에 대해 구현하여 제목 접두사에 대한 일치를 반환합니다; 기본 검색 경로는 전체 텍스트 스코어링을 실행합니다. 이 토큰 없이는 자동완성 스타일 UI가 접두사 검색 의도를 전달할 방법이 없었고 릴레이는 쿼리 모양에서 추측해야 했습니다. 토큰은 검색당 힌트이며 릴레이 전체 기능이 아니므로 릴레이는 일반 자동완성 지원을 주장하지 않고 하나의 이벤트 클래스 (제목)에 대해 구현할 수 있습니다.

### NIP-GART 긴급 경보 및 위치 브로드캐스트 (PR #2374)

disinqa가 6월 9일에 공개한 [PR #2374](https://github.com/nostr-protocol/nips/pull/2374)는 신뢰할 수 있는 수신자 그룹에 주소가 지정된 긴급 경보 및 위치 브로드캐스트를 위한 Nostr의 프라이버시 보존 와이어 형식을 정의합니다. 명시된 설계 목표는 이벤트를 재생 안전하고 서명 확인 가능한 종단 간으로 유지하면서 릴레이 운영자로부터 발신자 신원, 그룹 멤버십, 페이로드를 숨기는 것입니다. NIP 번호는 아직 TBD이며 제안은 초기 초안입니다. 사용 사례는 표준 긴급 경보 패턴입니다: 위협받는 사용자가 사전 공유된 신뢰할 수 있는 연락처 그룹만 해독할 수 있는 위치 ping을 브로드캐스트하며, 릴레이는 발신자, 수신자 집합, 페이로드에 대해 눈이 멀었습니다. 와이어 형식 세부 사항은 PR에 있으며 메인테이너가 검토하면서 진화할 가능성이 높습니다.

### NIP-46 logout 메서드 (PR #2373)

hzrd149가 6월 8일에 공개한 [PR #2373](https://github.com/nostr-protocol/nips/pull/2373)은 클라이언트가 세션이 종료되었음을 bunker에 명시적으로 알릴 수 있도록 `logout` 메서드를 [NIP-46](/ko/topics/nip-46/)에 추가합니다. 지금까지 bunker 세션을 종료하는 유일한 방법은 세션 타임아웃을 기다리거나 연결 사용을 중지하는 것이었고, 둘 다 bunker가 사라진 클라이언트의 세션 상태를 유지하게 합니다. 제안은 짧고 (하나의 새 메서드) 오래 지속되는 bunker 통합을 더 깨끗하게 만드는 종류의 정리 변경입니다.

### NIP-95 하이브리드 릴레이-P2P 제안이 롱폼으로 유통

npub `91bea5cd9361504c409aaf459516988f68a2fcd482762fd969a7cdc71df4451c`에서 6월 4일 *Protocolo Híbrido Relay-P2P via WebRTC*라는 제목으로 `kind:30023` 게시물로 롱폼 [NIP-95 사양](https://github.com/nostr-protocol/nips)이 유통되었습니다. 포르투갈어 문서는 Nostr 클라이언트가 저장된 이벤트 검색 및 오프라인 배달을 위해 릴레이를 계속 사용하면서 실시간 메시징을 위해 WebRTC를 통해 서로 직접 연결하는 하이브리드 피어 투 피어 릴레이 프로토콜을 정의합니다. 저자는 사양을 "LLM 준비"로 명시적으로 프레임하여 AI 모델이 작동하는 클라이언트 또는 서버 코드를 생성할 수 있는 수준의 세부 정보로 메시지 정의, 논리적 흐름, 데이터 스키마, 상태 규칙을 제공했습니다. 제안은 아직 NIP PR로 도착하지 않았습니다; `kind:30023`을 통한 유통은 공식 nostr-protocol/nips 풀 리퀘스트의 관례적 전조입니다.

### NIP-44 v3가 두 번째 서명자를 얻다: Clave가 사양을 이식

[지난주 Amber의 v6.2.0 NIP-44 v3 롤아웃](/ko/newsletters/2026-06-03-newsletter/#nip-44-v3-amber-implementation-ahead-of-spec)은 병합된 NIPs PR 이전에 출시되어 v3를 상호 운용하기 위해 다른 클라이언트가 미러링해야 하는 Amber 전용 확장으로 남겨두었습니다. 그 단일 구현 프레이밍이 이번 주 변경되었습니다. 푸시 기반 iOS NIP-46 원격 서명자 [Clave](https://github.com/DocNR/clave)가 6월 3일과 4일에 여덟 개의 커밋에 걸쳐 독립적인 NIP-44 v3 포트를 실현했습니다. 암호 프리미티브는 세 개의 커밋에서 출시됩니다: [HKDF + ECDH 키 계층](https://github.com/DocNR/clave/commit/99ca5a5aacb501d1666c489fcdea30187c7853fa), [v3 패딩 알고리즘](https://github.com/DocNR/clave/commit/8808cdca54d32b4ae57856bd4b07ed73a45e8e5c), [최상위 공개 API 및 암호화 컨텍스트](https://github.com/DocNR/clave/commit/ae1f506a53cb2c8aa16523540dbe790876c1839e). 그 위에 NIP-46 표면이 [LightSigner 내부의 RPC 디스패치 배선](https://github.com/DocNR/clave/commit/f37aa1afc8368862fc3ebac533408442349bfc38)과 [v3 컨텍스트 (kind 및 scope)를 담는 PendingRequest 스키마](https://github.com/DocNR/clave/commit/e51bcb49fc61cfa89b6030d61b203e046aeddb0a)에서 이어지므로 서명자는 v3 페이로드가 어떤 이벤트 kind와 사용 사례에 대해 승인되었는지 기록할 수 있습니다.

Clave는 사용자 대면 표면에서 Amber와 갈라집니다. [민감도 계층을 갖춘 권한 부여 스키마](https://github.com/DocNR/clave/commit/0a8b7de63c1f2994a80a66bf139ec519fab12877)를 통해 사용자는 선택한 민감도 수준에서 특정 이벤트 kind 및 scope에 대해 v3 암호화를 부여할 수 있습니다. 첫 만남에서 [일회성 설명 카드가 있는 v3 컨텍스트 인식 승인 프롬프트](https://github.com/DocNR/clave/commit/2cf563cb15b0406f5e8aaa0b4e34b887ff1896a1)가 v3를 사용자에게 소개합니다. 작업은 main에 있으며 [Xcode 프로젝트에 배선](https://github.com/DocNR/clave/commit/4bd0c26d7cf308386ef15e5d96ee5673d6db2d4a)되었지만 미출시입니다; 가장 최근 태그된 빌드는 5월 12일의 [v0.2.0-build79](https://github.com/DocNR/clave/releases/tag/v0.2.0-build79)입니다.

NIPs PR이 병합되기 전에 두 개의 독립적인 구현이 프로덕션 경로에서 NIP-44 v3를 실현하며, 이는 프로토콜 PR이 공식화할 기본 와이어 형식에 대한 사례를 강화합니다. 이제 크로스 구현 상호 운용성 테스트가 사양 수렴으로의 경로가 되며, Amber의 Android 승인 표면과 Clave의 iOS 민감도 계층 모델이 두 참조 포인트가 됩니다. v3를 배선하는 다른 원격 서명자 (nsec.app의 noauth는 2025년 5월 이후 휴면 상태이며 다른 bunker는 v3 작업을 발표하지 않음)는 합의를 더 강화할 것입니다.

### NIP-34 활동: Iris가 새로운 hashtree 전송으로 스택을 채택

Iris는 6월 8일에 [`hashtree`](https://njump.me/nevent1qqs8kmy7a9dn5awurlp9q26lsaetl7dc4wauzdl8ww68dzmn09e074gpzfmhxue69uhhgetdwqhxjunfwvh8gmc850du0)의 NIP-34 저장소 공지를, 6월 9일에 [`iris-apps`](https://njump.me/nevent1qqsq4grx000f6p0r8hdv4lqhcgn7707vmktv2j528kn0ldps4y9g49qpzfmhxue69uhhgetdwqhxjunfwvh8gmcmq47as), [`iris-drive`](https://njump.me/nevent1qqsyj5r0tyqvpp9v7qnras90u6kzqtpqx6ktntwym66m8qyngvf59vqpzfmhxue69uhhgetdwqhxjunfwvh8gmcpts6pf), [`iris-chat-rs`](https://njump.me/nevent1qqs0x98hpsv8vmrxvwm2rs9exxttrue5qv5p2n2sqjeylz2kgdmd7tgpzfmhxue69uhhgetdwqhxjunfwvh8gmca8783s)를 게시하여 `wss://temp.iris.to`에서 제공되는 새 `htree://` 스킴 아래 클론 URL을 광고했습니다. hashtree 전송은 GRASP 라우팅 클론에 대한 콘텐츠 주소 지정 대안이며, 이 네 개의 공지는 그 첫 번째 공개 사용입니다. 저장소에는 빈 설명이 있고 아키텍처 세부 사항은 아직 나타나고 있지만, (사용자 정의 Iris 내부 매니페스트 대신) NIP-34 공지를 통해 게시하기로 한 선택은 Iris가 더 넓은 NIP-34 git-over-Nostr 스택에 헌신하고 있음을 신호합니다.

## NIP 심층 분석: NIP-67 (EOSE 완전성 힌트)

[NIP-67](/ko/topics/nip-67/)은 [NIP-01](/ko/topics/nip-01/)의 가장 오래된 정확성 격차 중 하나를 닫습니다. 원본 사양은 `EOSE`를 `REQ`에 대한 저장된 이벤트와 실시간 구독 이벤트 사이의 경계로 정의하지만, 릴레이가 저장된 모든 일치 항목 배달을 완료했는지 아니면 내부 캡 때문에 도중에 멈췄는지는 결코 지정하지 않았습니다. 모든 릴레이는 클라이언트의 `limit`과 독립적으로 구독당 캡 (일반적으로 300에서 1000 이벤트)을 강제하며, 클라이언트는 그 캡을 관찰할 방법이 없었습니다.

표준 해결 방법은 수신된 카운트를 요청된 `limit`과 비교하는 것이었습니다. `received < limit`이면 결과를 완전한 것으로 처리하고, 그렇지 않으면 `until=<oldest_created_at>`로 페이지네이션합니다. 두 브랜치 모두 깨져 있습니다. `received < limit` 브랜치는 조용히 잘라냅니다: 300에서 캡된 릴레이에 대해 500개 노트를 요청하는 클라이언트는 300개 이벤트를 보고 `300 < 500`이므로 결과가 완전하다고 결론짓고 나머지를 결코 가져오지 않습니다. 릴레이에 보유된 이벤트는 기존 메시지를 통해 "더 사용 가능"을 신호할 수 없습니다. 두 번째 브랜치로서의 페이지네이션은 낭비입니다: 캡과 정확히 일치하는 필터는 완전성을 확인하기 위해 두 번째 `REQ`를 필요로 하며, 릴레이에서 전체 필터 스캔을 소비하면서 0 이벤트를 반환합니다.

NIP-67의 수정은 `EOSE` 메시지의 하나의 선택적 문자열입니다:

```
["EOSE", "<sub_id>", "finish"]   // 명시적: 모든 저장된 이벤트가 배달됨
["EOSE", "<sub_id>"]              // 완전성 주장 없음
```

[NIP-11](/ko/topics/nip-11/) `supported_nips`에서 NIP-67을 광고하고 벌거벗은 `EOSE`를 발산하는 릴레이는 클라이언트에게 더 있다고 말하고 있습니다. 광고를 생략하는 릴레이는 오늘의 동작을 유지하고 클라이언트는 기존 휴리스틱으로 폴백합니다. 레거시 클라이언트는 후행 배열 요소를 무시합니다. 하위 호환성은 양방향으로 유지되며, 새 동사나 이벤트 kind가 없습니다.

NIP-67을 검토할 가치가 있는 것은 의도적으로 제한한 범위입니다. 사양은 커서 또는 페이지네이션 토큰을 정의하지 않으므로 `until` 기반 페이지네이션은 메커니즘으로 남습니다. 릴레이 캡은 현재 위치에 머물며 NIP는 그 노출을 요구하지 않습니다. NIP-67은 `EOSE`를 저장된-대-실시간 경계로 유지하고 경계에서 예/아니오 신호만 추가합니다: "당신을 위해 더 있습니다" vs "그게 전부입니다". 이 최소한의 표면은 NIP-01 확장에 대해 상대적으로 짧은 검토 기간 후에 PR이 병합된 이유이며, mattn이 PR에서 영어 텍스트에 AI 번역이 사용되었다고 명시적으로 언급하는 이유입니다. 변경은 번역 불확실성이 중요하지 않을 만큼 작습니다.

캡을 강제하는 릴레이와 클라이언트 간의 NIP-67 인식 교환 예시. 릴레이의 NIP-11 광고:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1781136000,
  "kind": 11,
  "tags": [],
  "content": "{\"supported_nips\":[1,11,50,67]}",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

이어지는 와이어 수준 교환:

```
→ ["REQ", "abc", {"kinds":[1],"limit":500}]
← [...300개의 EVENT 메시지...]
← ["EOSE", "abc"]               // "finish" 없음: 캡에 도달, 더 사용 가능
→ ["REQ", "def", {"kinds":[1],"limit":300,"until":1780900000}]
← [...178개의 EVENT 메시지...]
← ["EOSE", "def", "finish"]     // 명시적으로 완료
```

178개 이벤트 응답은 이전에는 완료를 확인하기 위해 세 번째 `REQ`를 트리거했을 것입니다. NIP-67에서 클라이언트는 거기서 멈춥니다.

NIP-67은 또한 드문 합의로 도착하는 NIP-01 수정으로도 주목할 만합니다. 대부분의 NIP-01 변경은 프로토콜의 작은 표면이 모든 구현에서 하중을 부담하기 때문에 긴 논의 스레드를 끕니다. NIP-67은 확장된 검토 기간 (공개에서 병합까지 약 7주) 후에 병합되었으며, 이는 NIP-01 변경이 충분히 작고 실패 모드가 충분히 구체적일 때 (조용한 데이터 손실, 필수 낭비된 왕복) 프로토콜 메인테이너가 코어 메시지 어휘를 확장할 의향이 있음을 시사합니다.

## NIP 심층 분석: NIP-50 (검색)

[NIP-50](/ko/topics/nip-50/)은 `REQ` 메시지의 `search` 필터 필드를 정의하며, 클라이언트가 쿼리 문자열에 대한 전체 텍스트 매치로 이벤트를 필터링하도록 릴레이에 요청할 수 있게 합니다. 병합된 기본 사양은 의도적으로 최소한입니다: `search` 필드는 문자열이고, 각 릴레이는 자체 검색 의미를 결정하며 (어떤 필드가 인덱싱되는지, 스코어링이 어떻게 작동하는지, 어간이 적용되는지), 릴레이는 NIP-11 문서에서 NIP-50 지원을 광고합니다. 클라이언트는 쿼리 문자열 자체를 통해서만 검색 알고리즘을 제어합니다.

이 미니멀리즘은 NIP-50의 강점이자 제약입니다. 강점은 어떤 릴레이든 어떤 품질 수준에서든 검색을 구현할 수 있다는 것입니다: 기본 하위 문자열 스캔이 사양을 만족하고, Elasticsearch 또는 Meilisearch를 실행하는 릴레이도 동등하게 만족합니다. 제약은 클라이언트가 검색 의도를 표현할 방법이 없다는 것입니다. 프로필 언급 typeahead UI는 표시 이름에 대한 접두사 매칭을 원합니다; 전체 텍스트 콘텐츠 검색은 노트 본문 전체에서 토큰화된 전체 텍스트 스코어링을 원합니다. 동일한 `search` 필드가 두 가지를 모두 담고, 릴레이는 쿼리 모양에서 추측해야 합니다.

[PR #2357](https://github.com/nostr-protocol/nips/pull/2357)은 첫 번째 NIP-50 확장 토큰을 추가합니다: 검색 쿼리에 임베드된 `autocomplete:true` 또는 `autocomplete:false`는 클라이언트가 어떤 모드를 원하는지 신호합니다. Ditto의 릴레이는 팔로우 팩, 목록, `title` 태그가 있는 모든 이벤트에 대해 토큰을 구현하여 `autocomplete:true`가 있을 때 접두사 매칭으로 전환합니다. 토큰은 쿼리 내에 인라인으로 존재하므로 (별도의 필터 필드는 그대로 유지) 검색 문자열과 함께 이동하고 와이어 프로토콜 범프가 필요하지 않습니다:

```
search: "fiat autocomplete:true"
```

이와 같은 토큰 모양의 힌트는 NIP-50이 항상 릴레이 특정 방언을 처리해 온 방법입니다. 릴레이는 이미 `language:en` 및 `domain:example.com`과 같은 토큰을 지원했습니다. 각각은 릴레이 특정으로 남고, 각 릴레이는 자체 방언을 문서화합니다. NIP-50의 PR #2357은 `autocomplete`를 릴레이 사설 토큰에서 사양이 축복한 것으로 승격시켜, 릴레이 전반에 걸친 typeahead 인식 검색으로의 길을 엽니다.

kind 0 프로필 제목을 인덱싱하는 릴레이를 대상으로 하는 autocomplete 토큰이 있는 NIP-50 `REQ` 예시:

```json
{
  "id": "b7c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f7081a2b3c4d5e6f70819a2b3c4d5",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1781136000,
  "kind": 1,
  "tags": [
    ["client", "example-mention-picker"]
  ],
  "content": "Sent search: kinds=[0], search=\"fiat autocomplete:true\", limit=10",
  "sig": "12d3e4f5061728394a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f7081a2b3c4d5e6f70819a2b3c4d5e6f7081a2b3c4d5e6f708192"
}
```

실제 와이어 수준 REQ:

```
["REQ", "mention-picker", {"kinds":[0],"search":"fiat autocomplete:true","limit":10}]
```

토큰을 인식하지 못하는 릴레이는 `autocomplete:true`를 리터럴 검색 문자열의 일부로 취급하고 전체 텍스트 매칭으로 폴백하여 (다르게 순위 지정되었더라도) 올바른 결과를 반환합니다. 우아한 성능 저하는 사용 가능할 때 접두사 매칭을 선호하는 클라이언트가 토큰을 무조건 포함하는 것이 안전하게 만듭니다.

다음 가능성 있는 NIP-50 확장은 kind별 순위 제어입니다: 기본 관련성 점수 대신 "created_at 내림차순으로 순위"를 말하는 힌트. 여러 릴레이가 이미 `sort:newest`를 릴레이 사설 토큰으로 수용하며, `autocomplete`를 사양에 가져온 것과 동일한 승격 경로가 적용됩니다. 검색은 릴레이가 결과 품질로 경쟁하는 몇 안 되는 Nostr 프리미티브 중 하나로 남습니다; 배송의 신뢰성은 모든 준수하는 릴레이에서 동일합니다. 점진적인 토큰을 통해 클라이언트는 릴레이가 무거운 새 사양을 출시하도록 강요하지 않고 그 품질 경쟁을 활용할 수 있습니다.
