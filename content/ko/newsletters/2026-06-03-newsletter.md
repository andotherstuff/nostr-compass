---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-03-newsletter.md
translationDate: 2026-07-01
---

Amber 6.2.0은 사양보다 앞서 NIP-44 v3 암호화를 출시합니다. Mostro는 여덟 개의 PR에 걸쳐 Cashu 정산 escrow의 기초를 도착시켜, 기존 Cashu Development Kit을 Lightning과 함께 두 번째 정산 백엔드로 감쌉니다. NIP-F4 팟캐스트가 27개월의 논쟁 끝에 병합됩니다. fiatjaf는 bunker 대 Marmot 아키텍처 논쟁을 다시 여는 논쟁적인 NIP-17 키 분리 제안을 엽니다. Amethyst는 52개의 미출시 PR에 걸쳐 NIP-32 해시태그 라벨링, 전용 팟캐스트 화면, 온체인 zap을 도착시켰습니다.

## 주요 소식

### Amber 6.2.0: NIP-44 v3 암호화 출시

6월 1일에 릴리스된 [Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0)은 전용 승인 화면, intent 프리뷰, bunker 프리뷰, 이력 로깅, 잘못된 요청에 대한 자동 거부와 함께 [NIP-44 v3 암호화 지원](https://github.com/greenart7c3/Amber/pull/448)을 추가합니다. 이 릴리스는 또한 [NIP-44 v3 ContentProvider authority](https://github.com/greenart7c3/Amber/commit/8b93340)를 등록하므로 다른 Android 앱이 기존 v2 경로와 함께 v3 암호화를 요청할 수 있습니다. NIP-44 자체는 [NIP-17](/ko/topics/nip-17/) 프라이빗 DM, NIP-46 bunker 트래픽 및 기타 Nostr 프리미티브에서 사용되는 버전이 지정된 암호화 페이로드 사양입니다; Amber의 v3는 별도의 signer 메서드로 신호되는 v2와 함께 옵트인이므로 수신자 측 클라이언트는 알고리즘을 명시적으로 협상할 수 있습니다. 해당 NIPs PR은 아직 도착하지 않았으므로, Amber는 다운스트림 클라이언트 통합을 위해 등록된 wire 형식 및 ContentProvider authority와 함께 프로토콜 합의보다 앞서 v3를 롤아웃하고 있습니다.

NIP-46 세션은 이제 연결 시 ping 요청을 자동 수락하여, 페어링 후 첫 왕복에서 프롬프트를 제거합니다. `sign_message` signer 메서드는 사용 중단되고 사용되지 않은 후 완전히 제거되었습니다.

Amber가 지배적인 Android signer이므로, v3를 원하는 모든 다운스트림 클라이언트는 NIPs PR이 도착할 때까지 Amber의 wire 형식을 대상으로 해야 합니다. 이는 프로토콜이 따라잡을 때까지 최종 v3 사양에 대한 Amber에게 암묵적인 발언권을 부여합니다. 트레이드는 실제적입니다: 프로덕션의 v3는 Amber가 결국의 NIP에 대한 구현 피드백을 수집할 수 있게 하며, 다른 클라이언트가 이제 매칭해야 하는 임시 단일 구현 참조 지점의 비용이 있습니다.

### Mostro: CDK를 통한 Cashu escrow 통합

grunch는 이번 주에 MostroP2P 전반에 걸쳐 여덟 개의 PR을 도착시켜, Nostr 조정 P2P Bitcoin 거래소에서 Lightning과 함께 두 번째 정산 백엔드로 Cashu의 기존 P2PK multisig 프리미티브(NUT-10 및 NUT-11)를 통합했습니다. 암호학적 프리미티브는 Cashu의 것입니다; 작업은 통합 스캐폴딩과 새로운 escrow 백엔드 trait입니다. 5월 30일에 릴리스된 [Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0)은 [2-of-3 multisig escrow에 대한 프로토콜 유형](https://github.com/MostroP2P/mostro-core/pull/150), proof별 P_M 서명을 추가하고, 응답 검증을 통해 escrow 이벤트를 허용합니다. 아키텍처는 [PR #756](https://github.com/MostroP2P/mostro/pull/756)에 문서화되어 있으며 [PR #757](https://github.com/MostroP2P/mostro/pull/757)에서 명확히 한 주문별 거래 키를 사용합니다.

구현은 하루 동안 여섯 개의 후속 PR에 걸쳐 롤아웃되었습니다. [F2(PR #758)](https://github.com/MostroP2P/mostro/pull/758)는 구성, escrow 모드, 조건부 부팅을 추가했습니다. 다음 슬라이스 [F3(PR #760)](https://github.com/MostroP2P/mostro/pull/760)는 Lightning 구현과 Cashu 스텁이 있는 `EscrowBackend` trait를 정의하여, Mostro가 주문 상태 머신을 변경하지 않고 정산 백엔드를 전환할 수 있게 합니다. [F4(PR #759)](https://github.com/MostroP2P/mostro/pull/759)는 mint 및 지갑 작업을 위해 [CDK](https://github.com/cashubtc/cdk)(Cashu Development Kit)를 감쌌습니다. [F5(PR #761)](https://github.com/MostroP2P/mostro/pull/761)의 데이터베이스 작업은 compare-and-swap escrow 잠금과 active-locked 쿼리를 추가했습니다. [F6(PR #762)](https://github.com/MostroP2P/mostro/pull/762)는 엔드투엔드 escrow 테스트를 위해 전용 CI 작업에 컨테이너화된 mint를 구축했습니다. Mostro 흐름은 이미 릴레이를 통한 주문 조정에 NIP-59 gift-wrapped DM을 사용하므로, Cashu escrow는 wire 프로토콜을 건드리지 않고 Lightning과 함께 두 번째 정산 옵션으로 슬롯을 채웁니다.

## 릴리스

### ngit v2.5.0: GRASP 대체 및 lazy git fetch

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0)은 저장소에 등록된 GRASP 서버가 하나 이상 있을 때 새 제안에 대해 PR kind를 생성하도록 `git push pr/<branch>` 및 `ngit send`의 기본 동작을 변경합니다. 이전에는 60 KB를 초과하는 큰 커밋이나 서브모듈이 포함된 커밋에 대해서만 이 동작이 트리거되었습니다. PR을 저장소의 GRASP 서버에 push할 수 없을 때, ngit는 이제 선언된 서버를 통한 GRASP-06 라우팅으로 대체됩니다. `ngit send --git-server` 플래그 또는 `git push -o git-server=<url>`은 기여자가 커스텀 git URL 또는 GRASP 서버를 명시적으로 대상으로 지정할 수 있게 합니다.

`ngit init` 재게시는 이제 기존 공지에서 알 수 없는 태그를 보존하므로, 미래의 ngit 버전이나 제3자 도구에 의해 추가된 태그는 재게시에서 살아남습니다. 노란색 경고는 이월된 태그를 나열하며, `--clean`은 요청에 따라 이를 제거합니다. `ngit pr apply`, `ngit pr checkout`, `ngit pr list`는 git 서버를 lazily 조회하고 단일 fetch 헬퍼를 공유하므로, 커밋이 이미 로컬에 있을 때 checkout이 더 이상 무조건 fetch하지 않습니다. `ngit pr checkout`은 또한 저장소의 선언된 git 서버가 PR tip을 운반하지 않을 때 대체로 PR 이벤트에서 제출자가 제공한 clone URL을 시도하며, `ngit pr apply`의 기존 동작과 일치합니다. ngit는 Nostr를 통한 git 협업에 대한 참조 [NIP-34](/ko/topics/nip-34/) 구현이며, v2.5.0은 GRASP를 새 기여자를 위한 일급 경로로 만듭니다.

### Jumble v26.5.7: EXIF 제거 및 검증된 zap 카운트

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7)은 사용자 프라이버시와 데이터 무결성에 직접 영향을 미치는 두 가지 변경을 추가합니다. EXIF 위치 및 카메라 식별자는 이제 이미지가 클라이언트를 떠나기 전에 이미지 업로드에서 제거되어, Jumble에서 게시된 모든 이미지에 영향을 미쳤던 오랫동안 지속된 메타데이터 유출 표면을 닫습니다. Zap 카운트는 이제 암호학적으로 검증된 영수증에서만 계산되며, 공격자가 노트의 zap 총계를 과장할 수 있었던 잘못 형성된 zap 이벤트의 부풀려진 카운트를 수정합니다. 이 릴리스는 또한 [NIP-17](/ko/topics/nip-17/) DM에 대한 발신자 identity 검증을 추가하여, 발신자가 seal에서 자신의 `pubkey`를 위조할 수 있는 스푸핑 표면을 닫습니다.

### nostr-calendar v1.6.0: RSVP 및 중복 참가자 처리

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0)은 Formstr의 RSVP 흐름을 도착시키고([PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)) 이벤트 초대에서 중복 참가자를 방지합니다([PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168)). publish 함수의 `waitForAll` 옵션은 이제 기본값이 false로 되어 UI가 느린 릴레이에서 차단되지 않도록 합니다([PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170)). [PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157)은 약속 스케줄링 및 예약에 대한 Formstr의 두 NIP 제안 초안을 출시했습니다.

### Sprout 0.3.6: Sprout × mesh-llm 및 채널 섹션

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6)은 이번 주 v0.3.1에서 v0.3.6까지 여섯 릴리스 런의 헤드라인입니다. 프로세스 내 Sprout × mesh-llm 통합은 [PR #798](https://github.com/block/sprout/pull/798)에 도착하여, Sprout가 릴레이 admission을 통해 mesh-llm 노드를 서비스하고 소비할 수 있게 합니다. 사용자 정의 채널 섹션은 [PR #792](https://github.com/block/sprout/pull/792)에서 Nostr를 통해 기기 간에 동기화되고, 채널 섹션은 [PR #800](https://github.com/block/sprout/pull/800)에서 릴레이 동기화와 함께 모바일에 도착합니다. 변경 가능한 팔로우 및 음소거 컨트롤이 있는 스레드 인식 알림은 [PR #761](https://github.com/block/sprout/pull/761)에 도착합니다.

다운로드 카드가 있는 임의 파일 유형 첨부 파일은 [PR #810](https://github.com/block/sprout/pull/810)에 도착하여, Sprout를 이미지 전용 첨부 파일 이상으로 확장합니다. 모바일은 Pulse 소셜 피드 탭([PR #772](https://github.com/block/sprout/pull/772))과 피드, 작성, 필터 표면 전반에 걸친 Pulse 다듬기([PR #796](https://github.com/block/sprout/pull/796))를 얻었습니다.

### NostrBotKit v0.5.0: Rust 봇 프레임워크의 Marmot 그룹 채팅

Codeberg에서 5월 24일에 릴리스된 [NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md)은 자체 호스팅 Rust 봇 프레임워크에 [Marmot](/ko/topics/marmot/)(MLS-over-Nostr, [NIP-104](https://github.com/nostr-protocol/nips/pull/2014)) 지원을 추가합니다. `marmot: true`가 설정되면 봇은 MLS 키 패키지(kind 443, 30443, 10051)를 게시하고, 그룹 초대를 자동으로 수락하며, 참여한 그룹에서 메시지를 수신합니다. 두 개의 새로운 명령 유형인 `dm_marmot` 및 `dm_marmot_npub`는 봇이 cron 작업 또는 웹훅을 통해 명명된 Marmot 그룹 또는 1:1 Marmot 채팅에 메시지를 보낼 수 있게 합니다. 다른 봇과의 피드백 루프를 방지하기 위해, NostrBotKit 봇은 `/command` 또는 `@botname/command`를 통해 명시적으로 자신에게 주소가 지정된 메시지에만 응답합니다. MIP-04를 사용한 암호화된 첨부 파일은 자동 복호화되고 Blossom 또는 NIP-96을 통해 재업로드되며, MLS 상태 데이터베이스는 봇의 private 키에서 파생된 키로 암호화됩니다. NostrBotKit은 NIP-104 봇 지원을 출시한 첫 Rust 프레임워크로, 기존 TypeScript 경로와 다른 운영자 프로필에 Marmot 암호화 봇 배포를 열어줍니다.

### noscrypt v0.1.14: 서명된 암호 라이브러리 릴리스

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14)는 secp256k1, NIP-04, NIP-44 프리미티브에 대해 여러 Nostr 클라이언트가 사용하는 C 암호 라이브러리의 보안 릴리스입니다. 이 릴리스는 유지 관리자의 public 키에 대해 검증할 수 있는 [PGP 서명 다운로드](https://www.vaughnnugent.com/resources/software/modules/noscrypt)와 함께 출시됩니다. noscrypt를 번들하는 다운스트림 클라이언트는 통합하기 전에 서명을 검증해야 합니다.

### Chama v1.3.0: Fedimint를 사용한 새로운 Nostr 네이티브 P2P escrow

6월 1일에 릴리스된 [Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0)은 정산을 위해 Fedimint ecash와 2-of-3 Shamir secret sharing을 사용하는 새로운 Nostr 네이티브 P2P escrow 클라이언트의 네 릴리스 런의 헤드라인입니다. 이 프로젝트는 [getchama.app](https://getchama.app)에서 출시되며 서버 없이 실행됩니다. v1.3.0은 "heal that sticks"(세션 재시작에서 살아남는 성공적인 재브로드캐스트 및 거래 healing)와 pay-rail 매칭을 도입하며, 미국 지향 Chama는 미국 결제 rail을 먼저 표시합니다. 다중 유닛 storefront 기초 작업은 [v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11)(다중 유닛 스키마) 및 [v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12)(storefront 재고 회계사 + 네이티브 Fedimint 브릿지 복구 강화)에 걸쳐 도착했습니다. Chama는 서버리스 아키텍처와 Fedimint 기반 escrow 정산으로 구별되며, Nostr 마켓플레이스 카테고리에서 Mostro와 Shopstr에 합류합니다.

## 미출시 변경 사항

### Amethyst: NIP-32 해시태그 라벨링, 팟캐스트 화면, 음악 트랙

Amethyst는 릴리스 태그를 컷팅하지 않고 이번 주에 52개의 PR과 411개의 커밋을 병합했습니다. 가장 큰 기능적 추가는 [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111)로, `L` 네임스페이스 및 `l` 라벨 태그가 있는 kind 1985 이벤트를 사용하여 [NIP-32](/ko/topics/nip-32/) 해시태그 라벨링과 라벨 기반 해시태그 피드를 구현합니다. 이는 취약한 텍스트 매치 `#tag` 메커니즘을 라벨러 기반 발견 모델로 대체하며, 사용자는 콘텐츠 작성자를 팔로우하는 방식으로 특정 라벨러 npub를 팔로우할 수 있습니다. [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105)는 에피소드 리스트와 인라인 플레이어가 있는 전용 팟캐스트 화면을 추가하며, [NIP-F4](/ko/topics/nip-f4/) 팟캐스트 사양 병합 후 며칠 내에 도착했습니다. [PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071)은 팔로우 리스트 필터링이 있는 소프트웨어 앱 피드를 추가하고, [PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067)은 [NIP-51](/ko/topics/nip-51/) set을 통한 음악 트랙 및 플레이리스트 지원을 추가합니다.

익명 게시물 업로드를 위한 임시 signer는 [PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123)에 도착하여, 사용자가 업로드 서비스에 identity 키를 노출하지 않고 익명으로 게시할 수 있게 합니다. Arti v2.3.0에 대한 통합 테스트가 있는 Tor 자체 치유 watchdog가 [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053)에 도착하여, 일시적인 네트워크 중단 동안 Amethyst의 Tor 라우팅을 강화합니다. Gemini에서 돌아오는 사용자를 위한 온체인 zap과 NIP-05 필터는 [PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052)에 도착하여, Lightning을 넘어 온체인 Bitcoin 결제로 zap 표면을 넓힙니다.

### Shopstr: OpenGraph 프리뷰 URL 검증

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504)는 마켓플레이스 리스팅에서 OpenGraph 프리뷰 URL을 렌더링하기 전에 검증하여, 악의적인 판매자가 조작된 OG 메타데이터를 통해 스크립트된 콘텐츠를 임베드할 수 있는 잠재적 XSS 표면을 닫습니다. Shopstr 호스팅 상점은 외부 링크에 대한 OG 프리뷰를 표시하며, 검증되지 않은 URL은 공격자가 상점 UI에 임의의 콘텐츠를 주입할 수 있게 했습니다.

## NIP 업데이트 및 프로토콜 사양 작업

### NIP-F4(팟캐스트)가 2년 후 병합됨

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093)이 5월 28일에 병합되었으며, fiatjaf가 원본 초안을 연 후 2년 3개월이 지났습니다. NIP-F4는 오디오 파일 메타데이터(URL, mime type, 언어 ISO 코드, 대체 URL, NIP-96 서비스 플래그, bitrate, duration)에 대한 `imeta` 태그, `title` 태그, 선택적 `image` 및 `description` 태그, 주제 라벨용 `t` 태그가 있는 kind 54 이벤트로 팟캐스트 에피소드를 정의합니다. 이 사양은 의도적으로 RSS를 진실의 소스로 유지합니다: 에피소드는 RSS 팟캐스트 GUID를 참조하는 `i` 태그를 운반할 수 있으므로, Nostr 클라이언트는 오디오 호스팅을 복제하지 않고 기존 팟캐스트 피드에 연결할 수 있습니다. PR 스레드의 긴 논쟁(팟캐스트 네임스페이스 공동 저자 Dave Jones, Alex Gleason, Mike Terenzio와 함께)은 Nostr가 RSS 위에 소셜 계층을 제공하는 반면 RSS는 배포 계층을 유지하는 공존 모델로 정착했습니다. Amethyst의 [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) 팟캐스트 화면은 사양 병합 후 며칠 내에 도착하며, Jumble의 GIF picker 작업에는 초기 팟캐스트 첨부 파일 스캐폴딩도 포함되어 있습니다.

### NIP-17 키 분리(PR #2361)

fiatjaf는 6월 1일에 [PR #2361](https://github.com/nostr-protocol/nips/pull/2361)을 열어 NIP-17이 identity 키를 암호화 키에서 분리할 것을 제안했습니다. 수신자는 새로운 kind 10044 이벤트에서 암호화 키를 광고하고, 발신자는 광고가 존재할 때 gift-wrap 내부 seal에 광고된 키를 사용하며, 광고가 없을 때만 수신자의 identity 키로 대체됩니다. 이 PR은 또한 seal에 발신자의 암호화 pubkey를 운반하는 `n` 태그를 추가하므로, 수신자는 은퇴한 모든 키에 대한 시행착오 복호화 없이 올바른 대화 키를 유도할 수 있습니다. 명시된 동기는 bunker UX입니다: 현재 설계에서는 암호화 키가 signer가 보유한 identity 키이므로, bunker 사용자는 복호화를 위해 수신된 모든 DM을 signer를 통해 왕복해야 합니다. 분리는 클라이언트가 서명을 위해 identity 키를 bunker에 유지하면서 로컬에서 암호화 키를 보유할 수 있게 합니다.

이 제안은 이번 주 가장 논쟁적인 리뷰를 끌었습니다. Cody Tseng(Jumble)은 이를 크로스 클라이언트 DM 상호 운용성에 대한 가장 쉬운 경로로 지원합니다. Vitor Pamplona(Amethyst)는 두 가지 근거로 반대합니다: bunker 외부에 새로운 장기 복호화 secret을 추가하며, 이를 출시하지 않는 클라이언트는 출시하는 클라이언트의 메시지를 조용히 복호화하지 못하며, break가 seal 계층에 있기 때문에 저하 경로가 없습니다. Pamplona는 문제가 [Marmot](/ko/topics/marmot/)의 key package와 epoch rotation으로 이미 올바르게 해결되었으며, 기본 NIP-17 사양에 키 분리를 다시 적용하는 것은 Marmot이 2년 동안 설계해 온 것과 같은 종류의 상호 운용성 실패를 만든다고 주장합니다. fiatjaf의 반박은 세 부분입니다: 분리는 수신자별로 선택 사항이고, n-tag 수정은 시행착오 복호화 우려를 해결하며, 대안은 Telegram이 메시징 사용 사례를 먹는 동안 bunker UX를 깨진 채로 유지하는 것입니다. 스레드는 병합 결정 없이 열려 있으며 분기의 가장 주목받는 NIP 논의입니다.

### NIP-Silent Payments 결제 흐름(PR #2362)

[silentius-satoshi는 6월 1일에 PR #2362](https://github.com/nostr-protocol/nips/pull/2362)를 더 넓은 [Nostr Silent Payments NIP 초안(PR #2355)](https://github.com/nostr-protocol/nips/pull/2355)의 동반자로 열었습니다. 결제 흐름 NIP은 silent payment 영수증 알림용 kind 8352([NIP-59](/ko/topics/nip-59/) gift wrap을 통해 전달되어 영수증 링크가 공개적으로 관찰 가능하지 않음)과 동일한 Silent Payments 지갑에 대해 기기 간에 동기화되는 암호화된 UTXO 캐시용 kind 10353을 정의합니다. 두 개가 함께 지불자는 공개 릴레이 계층에서 온체인 링크를 노출하지 않고 Nostr 네이티브 프리미티브를 사용하여 Silent Payments 주소로 결제를 신호할 수 있습니다.

### NIP-PIP Perfect IP Packets(PR #2364)

[RandyMcMillan은 6월 1일에 PR #2364](https://github.com/nostr-protocol/nips/pull/2364)를 초안으로 열었습니다. 이는 세 개의 새로운 주소 지정 가능한 kind가 있는 packet-tree 전송을 도입합니다: 39078은 manifest를 운반하고, 39079는 개별 슬라이스를 운반하며, 39080은 복구 요청을 운반합니다. 이 사양은 큰 파일이 주소 지정 가능한 슬라이스로 분할되는 wire 형식을 정의하며, manifest는 슬라이스 트리를 설명하고 복구 요청은 수신자가 누락된 슬라이스를 요청할 수 있게 합니다. 초기 초안 상태가 적용되며, 이 제안은 아직 유지 관리자 리뷰를 끌지 못했습니다.

### NIP-29 오디오/비디오 라이브 공간(PR #2238)

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238)이 5월 28일에 병합되어, [NIP-29](/ko/topics/nip-29/) 릴레이 기반 그룹을 오디오 및 비디오 라이브 공간 지원으로 확장했습니다. 그룹은 이제 활성 라이브 공간 세션을 참조할 수 있으며, [NIP-53](/ko/topics/nip-53/) 스타일 라이브 활동 이벤트가 NIP-29 그룹 컨텍스트에 앵커링될 수 있게 합니다.

### NIP-71 비디오 다중 오디오 트랙(PR #2255)

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255)가 5월 28일에 병합되어, NIP-71 비디오 이벤트에 오디오 트랙 `imeta` 태그를 추가했습니다. 새 형식은 URL, 해시, mime 유형, 언어 태그(ISO-639-1과 원본 버전 플래그 포함), 대체 URL, NIP-96 서비스 신호, bitrate, duration을 운반합니다. 이는 오디오 전용 스트리밍(비디오 팟캐스트), 안정적인 오디오로 해상도 전환, 여러 언어 트랙, 서버가 오디오를 비디오 파일에 직접 임베드하지 않을 때 저장소 감소를 가능하게 합니다. 클라이언트는 단일 트랙 동작을 가정하기 전에 오디오 트랙 가용성을 확인해야 합니다.

### NIP-59 임시 gift wrap(PR #2245)

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245)가 5월 28일에 병합되어, 기존 kind 1059 gift wrap의 임시 대응물로 kind 21059를 추가했습니다. 시맨틱은 표준 NIP-59 wrap과 일치하지만 NIP-01에 따른 임시 이벤트 규칙을 따릅니다(릴레이가 브로드캐스트 후 삭제하며 유지하지 않음). 이는 앱이 요구 사항에 따라 지속성을 선택할 수 있게 합니다: 입력 표시기 및 존재 ping은 임시로 이익을 얻는 반면, DM 이력은 지속성이 필요합니다.

### NIP-78 애플리케이션 특정 kind(PR #2292)

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292)가 5월 28일에 병합되어, NIP-78 애플리케이션 특정 데이터를 일반 주소 지정 가능한 kind로 재분류하고, 이전의 별도 범위를 삭제했습니다. 이는 replaceability 시맨틱을 단순화하고 NIP-78을 다른 애플리케이션 상태 NIP이 사용하는 주소 지정 가능한 이벤트 모델과 정렬합니다.

### NIP-85 명확화(PR #2304)

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304)가 5월 28일에 [NIP-85](/ko/topics/nip-85/) Trusted Assertion의 서비스 provider별 여러 키 및 릴레이에 대한 언어의 작은 개선과 함께 병합되어, 릴레이 assertion 서비스에 대한 운영자 키 회전 경로를 명확히 했습니다.

### NIP-01 릴레이 연결 관리 한 줄(PR #2307)

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307)이 5월 28일에 병합되어, 클라이언트가 릴레이 연결 수명을 처리하는 방법에 대한 단일 문장을 NIP-01에 추가했습니다. 이 수정은 클라이언트가 가져오기 후 WebSocket 연결을 열어 둘지 여부에 대해 달랐던 오랫동안 지속된 격차를 다루며, 이는 유휴 연결을 삭제하는 릴레이에서 조용한 메시지 손실로 이어졌습니다.

### NIP-C7 kind 9 채팅 제약 조건(PR #2310)

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310)이 5월 28일에 병합되어, NIP-C7 채팅 뷰를 kind 9 메시지로만 제한합니다. 이는 NIP-C7 스타일 채팅 표면을 구현하는 클라이언트에서 임시 채팅을 kind 1 타임라인 게시물에서 분리합니다.

### NIP-55 단순화(PR #2363)

greenart7c3가 6월 1일에 연 [PR #2363](https://github.com/nostr-protocol/nips/pull/2363)은 Android signer 애플리케이션 사양을 단순화합니다. Vitor Pamplona는 "Looks good"으로 승인했고 fiatjaf는 병합 준비가 되었는지 물었습니다. 이 변경은 Amber가 이번 주에 출시한 NIP-44 v3 ContentProvider authority 등록의 길을 마련합니다.

### NIP-44 v3(사양 이전의 Amber 구현)

Amber는 암호화 업그레이드 및 ContentProvider authority 등록을 구현하는 여덟 개의 커밋으로 v6.2.0에서 NIP-44 v3를 출시했지만, NIPs 저장소 사양 PR은 아직 도착하지 않았습니다. NIP-44 자체는 서명된 이벤트 내부에서 사용되는 버전이 지정된 암호화 페이로드 형식을 정의합니다; 기존 v2(2024년부터 프로덕션에서)는 secp256k1 ECDH, HKDF, 패딩, ChaCha20, HMAC-SHA256, base64를 사용합니다. v3 wire 형식은 nonce 앞에 새로운 버전 바이트(0x03)를 추가하여, 수신자 클라이언트가 알고리즘을 명시적으로 협상할 수 있게 합니다. Amber의 구현에는 잘못된 v3 요청에 대한 자동 거부, v2 승인과 별개의 전용 승인 화면, 이력에 대한 방향별 평문 로깅이 포함됩니다. NIPs PR이 병합될 때까지 v3는 Amber 특정 확장으로 서 있습니다. 안정적인 프로토콜 전반 신호가 아니라 미래 지향 신호로 취급하십시오.

## NIP 심층 분석: NIP-32 (Labeling)

[NIP-32](/ko/topics/nip-32/)는 Nostr 액터가 네임스페이스가 지정된 라벨 어휘와 함께 주소 지정 가능한 kind 1985 이벤트를 사용하여 이벤트, pubkey, 릴레이, URL 또는 주제를 라벨링하는 구조화된 방법을 정의합니다. 이 사양은 두 개의 새로운 태그를 도입합니다: `L`은 라벨 네임스페이스를 나타내고, `l`은 그 네임스페이스 내의 라벨을 나타냅니다. 라벨 대상 태그(`e`, `p`, `a`, `r` 또는 `t`)는 무엇이 라벨링되는지를 지정합니다. 네임스페이스 요구 사항은 여러 라벨 시스템이 충돌하는 것을 방지합니다: `nip28.moderation`의 `spam` 라벨은 `relay-report`의 `spam` 라벨과 다른 시맨틱을 운반합니다.

NIP-32를 조정을 넘어 유용하게 만드는 설계 선택은 라벨이 프로토콜 수준 진실이 아니라 assertion이라는 것입니다. Kind 1985 이벤트는 특정 pubkey가 특정 대상을 특정 네임스페이스에서 라벨링했다는 것만 말합니다. 신뢰 모델은 클라이언트에게 위임됩니다: 각 클라이언트는 존중할 라벨러, 읽을 네임스페이스, 각 라벨에 부여할 UI 어포던스를 선택합니다. 동일한 프리미티브는 콘텐츠 경고, 라이선스 할당, kind 1 노트의 ISO-639-1 언어 태그, ISO-3166-2 지리적 태그, 콘텐츠 분류, 분산 조정 제안, 평판 점수를 운반합니다.

이번 주 Amethyst의 [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111)은 지금까지 가장 큰 배포입니다. NIP-32를 통한 해시태그 라벨링과 라벨 기반 해시태그 피드를 추가하여, 사용자가 신뢰할 수 있는 라벨러가 할당한 라벨로 탐색할 수 있게 합니다. 원래 Nostr에서 해시태그 발견을 주도한 이전 `#tag` 텍스트 매치 메커니즘은 라벨링되지 않은 노트에 대한 대체로 남아 있습니다. 라벨로서의 해시태그 모델은 동일한 노트가 다른 라벨러에 의해 할당된 여러 라벨로 발견 가능하다는 것을 의미하며, 사용자는 기본 노트에 영향을 미치지 않고 특정 라벨러를 음소거하거나 부스트할 수 있습니다.

자체 라벨링도 지원됩니다. 저자는 언어, 위치, 주제를 선언하기 위해 자신의 kind 1 노트에 직접 `L` 및 `l` 태그를 첨부할 수 있습니다. `["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]`으로 태그된 노트는 자신을 영어로 식별하며, 제3자 라벨링 인프라 없이 언어 인식 클라이언트에 의해 필터링될 수 있습니다.

kind 1 노트를 영어로 태그하고 조정 태그를 할당하는 NIP-32 라벨 이벤트 예시:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

Amethyst 롤아웃은 최근 Trusted Relay Assertion 작업과 결합되어, NIP-32가 Nostr의 "대상에 대한 사용자 주도 assertion" 패턴의 표준 기질이 되고 있음을 시사합니다. 다음 테스트는 라벨러 자체가 신뢰 계층을 개발할지 여부입니다: 사용자가 콘텐츠 작성자를 팔로우하는 방식으로 특정 라벨러 npub를 팔로우할지 여부입니다.

## NIP 심층 분석: NIP-F4 (Podcasts)

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md)가 이번 주에 병합되었으며, fiatjaf가 원본 초안(PR #1093)을 연 후 2년 3개월이 지났습니다. F 접두사는 평범한 hex 번호 매기기입니다: NIP-F0에서 NIP-FF는 NIP-0A에서 NIP-0D와 동일한 1바이트 hex 공간을 사용하며, 상위 hex 범위는 01-99 십진수 범위가 채워지고 있는 지금 오버플로우 역할을 합니다. NIP-F4는 팟캐스트가 에피소드 및 메타데이터를 Nostr 이벤트로 게시하면서 오디오 파일 자체에 대한 보완 계층으로 RSS를 유지하는 방법을 정의합니다.

핵심 아키텍처 선택은 각 팟캐스트가 자체 Nostr keypair라는 것입니다. 사양은 이것으로 직접 시작합니다: "each podcast is its own Nostr keypair". 이는 팟캐스트가 팟캐스팅 존재를 일반 kind 0 / kind 1 마이크로블로깅 존재와 결합할 수 있게 하며, 팟캐스트가 키 이전 또는 MuSig2 스타일 공유 서명을 통해 시간이 지남에 따라 소유권을 변경할 수 있게 합니다. 네 개의 이벤트 kind가 게시 계층을 운반합니다:

- **`kind:10154`**: replaceable 팟캐스트 메타데이터. `title`, `image`, `description`, 선택적 `website` 태그와 `role`이 `host`, `cohost`, 또는 `editor`인 저자를 표시하는 선택적 `p` 태그를 운반합니다.
- **`kind:10164`**: 저자 반대 청구. 사양의 예시는 kind `10064`(수정을 위해 열려 있는 오타)를 사용하지만, 제목과 주변 텍스트는 이를 `kind:10164`로 식별합니다. 사용자는 자신이 저작한 팟캐스트 pubkey를 나열하므로, 클라이언트는 `kind:10154`의 `p` 태그를 추정된 저자의 동등한 청구에 대해 검증할 수 있습니다. 이것 없이는 팟캐스트가 누구든 호스트로 잘못 태그할 수 있습니다.
- **`kind:54`**: 팟캐스트 pubkey가 직접 저작한 에피소드 이벤트. 태그에는 `title`, 선택적 `image`, `description`, 하나 이상의 `audio` 태그가 포함됩니다. 각 `audio` 태그는 `["audio", "<audio-url>", "<optional_media_type>"]`입니다. 사양은 "추가 발견 후 나중에 여기서 지정할 다른 중요한 필드"를 언급하며, 병합된 형식은 의도적으로 최소입니다.
- **`kind:10054`**: [NIP-51](/ko/topics/nip-51/) 스타일 즐겨찾기 팟캐스트 리스트로, 사용자가 팔로우하는 팟캐스트를 표시할 수 있게 합니다.

병합 주변의 스레드 논쟁에는 Podcasting 2.0 공동 저자 [Dave Jones](https://github.com/daveajones), [Alex Gleason](https://github.com/alexgleason), [Mike Terenzio](https://github.com/mterenzio), [Pablo F7z](https://github.com/pablof7z), [staab](https://github.com/staab)가 참여했습니다. Jones는 RSS를 대체하려는 모든 시도에 강하게 반대하며 다음과 같이 주장했습니다: "여러 번 시도되었지만 항상 실패합니다", JSONfeed, XMPP, AMP, Twitter의 API, Spotify의 실패한 마이그레이션을 인용했습니다. Terenzio는 제안을 RSS 위의 소셜 계층으로 재구성하여 RSS 자체를 배포 계층으로 유지했습니다. fiatjaf는 물러서서 제안이 성숙하도록 두는 데 동의했습니다: "당신이 말한 모든 것에 동의하지만 여전히 우리가 해낼 수 있다고 생각합니다, 잠시 여기서 멈추죠". 2년 후 병합된 사양은 대체보다 공존에 더 가깝게 도착합니다.

세 가지 설계 질문이 병합된 사양에 명시적으로 남아 있습니다:

- `kind:10164` 오타(예시는 `10064`를 보여줍니다)는 클라이언트가 안전하게 상호 운용될 수 있으려면 조정되어야 합니다.
- RSS GUID 링크 없는 에피소드 수준 발견은 열려 있습니다. 병합된 사양에는 `i` 태그, `podcast:item:guid` 형식, RSS 브릿징 메커니즘이 없습니다. 기존 RSS 카탈로그를 kind 54 이벤트로 브릿징하려는 클라이언트는 브릿지 관례를 스스로 정의해야 합니다.
- `kind:54` 정의의 "다른 중요한 필드" stub는 bitrate, duration, 언어, 트랜스크립트 포인터, chapter, 세그먼트별 메타데이터를 후속 제안을 위한 열린 영역으로 남깁니다.

Amethyst의 [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105)는 병합 후 며칠 내에 에피소드 리스트와 인라인 플레이어가 있는 전용 팟캐스트 화면을 도착시키며, 첫 번째 주요 클라이언트 구현입니다. Jumble은 GIF picker와 함께 초기 팟캐스트 첨부 파일 스캐폴딩을 출시했습니다. Wavlake는 여전히 가장 큰 Nostr 네이티브 팟캐스트 플랫폼으로 남아 있으며, 기존 kind 31337 음악 트랙 이벤트를 NIP-F4의 kind 54 에피소드 모델과 정렬할지 결정해야 합니다.

병합된 사양의 최소 태그 세트와 일치하는 NIP-F4 kind 54 에피소드 이벤트 예시:

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge, and why coexistence with RSS turned out to be the right architectural choice.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

PR #1093은 27개월 동안 열려 있었으며, 병합된 NIPs PR의 중앙값 열린 기간을 훨씬 초과합니다. NIP-F4에 대한 다음 테스트는 kind 10164 오타가 조정되는지, 에피소드 발견 및 RSS 브릿지 관례가 구현자에서 나오는지, 주요 팟캐스트 호스트가 사양이 권장하는 대로 팟캐스트별 keypair 하에 게시하는지 여부입니다.
