---
title: "Nostr Compass #34"
date: 2026-08-05
publishDate: 2026-08-05
translationOf: /en/newsletters/2026-08-05-newsletter.md
translationDate: 2026-08-06
draft: false
type: newsletters
description: "Sandstr는 목 데이터로 Nostr 클라이언트 투어를 제공하고, nostr-mill은 이벤트별 서명 동의를 추가하며, nostrord는 릴레이 호스팅 그룹을 확장합니다. 심층 분석에서는 릴레이 검색과 휴대용 하이라이트를 다룹니다."
---

[Nostr Compass](https://github.com/andotherstuff/nostr-compass)에 다시 오신 것을 환영합니다. Nostr 주간 가이드입니다.

**이번 주:** [Sandstr](https://sandstr.app/)는 신규 사용자가 키를 만들거나 앱을 설치하지 않고도 시뮬레이션된 Nostr 클라이언트를 탐색할 수 있게 합니다. [nostr-mill](https://github.com/0ceanSlim/nostr-mill)은 이벤트별 서명자 동의와 클라이언트 간 키 복구를 추가하고, [nostrord](https://github.com/nostrord/nostrord)는 릴레이 호스팅 그룹, 서명자, 모더레이션, 업로드, 하이라이트를 확장합니다. 프로토콜 작업은 Nostr 이벤트 형식, 지갑 연결, 릴레이 검색, napplet, Marmot, Concord에 걸쳐 있으며, 심층 분석에서는 릴레이 지원 검색과 휴대용 하이라이트를 설명합니다.

## 주요 소식

### nostr-mill 1.6.0은 서명 동의와 계정 복구를 브라우저에 제공

[nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0)은 임베딩 가능한 브라우저 계정 선택기이자 서명자입니다. 이제 이벤트 kind별로 동의를 요청하고 서명 전에 디코딩된 콘텐츠와 태그를 표시하며, 기간 제한이 있는 권한 부여와 권한 관리자를 제공합니다. 이 릴리스는 매번 묻도록 구성된 카테고리가 묻지 않고 서명할 수 있었던 첫 세션 버그도 수정합니다. 선택적 Google 온보딩은 기존 `nsec`을 가져올 수 있고, 키를 사용자의 Drive 앱 데이터 폴더에 암호화하여 저장하며, 여러 ID를 지원하고, [NIP-49](/ko/topics/nip-49/)(암호화된 개인 키 형식) `ncryptsec`을 내보낼 수 있습니다.

[실험적 릴레이 백업](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0)은 scrypt와 HKDF로 강력한 복구 구문을 도출하고, 키를 `ncryptsec`으로 래핑하며, 가져온 이벤트를 검증하고, 복구 전에 릴레이 정족수를 요구합니다. [NIP-55](/ko/topics/nip-55/)(Android 서명자 인텐트) 로그인은 이제 Amber의 클립보드 리턴 경로를 사용하고, [NIP-46](/ko/topics/nip-46/)(릴레이 매개 원격 서명) 연결은 기본적으로 조용합니다. 브랜딩 컨트롤과 반응형 권한 화면이 릴리스를 마무리하며, 운영자가 옵트인하지 않는 한 기존 통합을 변경하지 않습니다.

### nostrord 2.5.0은 릴레이 그룹에 안정적이고 릴레이 고유의 ID를 부여

[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0)은 릴레이 호스팅 커뮤니티를 위한 크로스 플랫폼 클라이언트입니다. 이제 그룹 ID와 호스트 릴레이 모두에서 [NIP-29](/ko/topics/nip-29/)(릴레이 관리 그룹) ID를 도출하고, 멤버십과 관리자 배지를 같은 방식으로 범위 지정하며, 그룹 `naddr` 딥 링크를 수락하고, 비공개 그룹 스레드를 기기 간에 동기화합니다.

이 [릴리스](https://github.com/nostrord/nostrord/releases/tag/v2.5.0)는 또한 [NIP-56](/ko/topics/nip-56/)(신고 이벤트) 모더레이션 받은 편지함, NIP-55를 통한 Amber 로그인, NIP-46 서명자 트래픽에 대한 속도 제한 백오프, 해결되지 않은 참조에 대한 재시도가 있는 [NIP-84](/ko/topics/nip-84/)(휴대용 하이라이트) 렌더링, Blossom 또는 [NIP-96](/ko/topics/nip-96/)(HTTP 파일 저장소)을 통한 미디어 업로드를 추가합니다. Google 로그인은 이제 계정 생성 전에 키를 백업하고 연결 해제를 확인합니다. 스레드 답글은 더 풍부한 콘텐츠와 관리자 삭제를 얻고, 데스크톱 키체인과 모바일 키보드 수정은 이러한 프로토콜 기능을 사용 가능한 상태로 유지합니다.

### Primal Android 3.5.25는 원격 서명과 팔로우 목록 필터링을 업데이트

[Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25)는 피드, 검색, 원격 서명을 갖춘 모바일 Nostr 클라이언트입니다. 원격 서명자를 현재 프로토콜 동작에 맞게 업데이트하고, 팔로우 뮤트 목록을 추가하며, Explore에서 검색을 열고, 정체된 릴레이 연결을 자동으로 복구하고, 요청 타임아웃을 인터페이스에 노출하며, 잘못된 팔로우 목록 항목을 거부하고, 폴백 릴레이 URL을 새로 고칩니다. 피드 프리페칭, 낮은 메모리 사용량, 100MB 캐시 상한은 이러한 피드를 최신 상태로 유지하는 비용을 줄입니다. 단일 이미지 노트는 이제 전체 콘텐츠 너비를 사용하고, 프로필 컨트롤과 미디어 프리로딩은 더 작은 상호작용 및 순서 지정 수정을 받습니다.

### Nostur 1.30.2는 다이렉트 메시지의 비공개 답글과 미디어를 확장

[Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527)는 Apple 플랫폼 Nostr 클라이언트입니다. 비공개 답글 작업을 항상 노출하고, 제한과 지우기 컨트롤이 있는 대화별 DM 미디어 캐시를 추가하며, 게시물과 채팅에서 이름 및 태그 완성을 개선하고, 라이브 채팅에서 참조된 메시지를 표시하고, 채팅 알림에 방 제목을 포함합니다. 피드 페이지네이션 및 중첩 답글 수정은 검색 및 대화 렌더링 회귀를 해결합니다.

### Chama 5.7.0은 중재자 기록과 캐시된 거래 복구를 추가

[Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0)은 서명된 Nostr 이벤트 체인을 통해 피어 거래와 중재를 조정합니다. 중재자의 잠긴 금액, 보증금 기간, 자금 조달 아웃포인트를 표시하고, 백업이 부재 중인 중재자를 대체한 시점을 기록하며, 양 당사자의 서명이 필요한 휴면 kind `38136` 결함 증명을 정의합니다. 명시적 복구는 불완전한 릴레이 기록을 내구성 있는 기기 캐시에 대해 재시도하고 복구된 이벤트를 다시 게시하는 반면, 실패한 게시는 다음 연결을 위해 대기열에 추가됩니다. 이 릴리스는 또한 작성자의 kind `38113` 이벤트를 지불 기록으로 처리하여 기기 간 중복 중재자 프리미엄 지불을 방지합니다.

### Auditable Voting 0.1.165는 위임 투표용지 전달을 복원

[Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165)는 유권자 자격 증명을 투표용지 내용과 분리하면서 검증 가능한 투표를 수행합니다. 인증된 위임 전달과 컨트롤 DM 백필을 통해 위임 블라인드 투표용지 발행을 복원하고, 블라인드 자격 증명 다이렉트 메시지를 구성된 비공개 릴레이에 유지하며, 감사 프록시를 0.1.52로 업데이트합니다.

### Sandstr는 신규 사용자가 목 데이터로 Nostr 클라이언트를 시험해 볼 수 있게 함

[Sandstr](https://sandstr.app/)는 신규 사용자가 클라이언트를 설치하거나 키 페어를 만들기 전에 인터페이스를 비교할 수 있도록 Nostr 클라이언트의 대화형 브라우저 시뮬레이션을 제공합니다. 8월 3일 출시에는 Damus, Amethyst, Primal, Snort, YakiHonne, Coracle, Wisp의 참조 검증된 복제와 Gossip, Keychat, Olas의 명확하게 라벨이 붙은 초기 미리보기가 포함됩니다. 모든 것이 목 데이터에 대해 로컬로 실행되므로 시뮬레이션은 키를 생성하거나 릴레이에 연결하지 않습니다. 각 시뮬레이션은 실제 클라이언트의 웹사이트와 소스 리포지토리로 연결되어 Sandstr를 또 다른 Nostr 클라이언트가 아닌 온보딩 및 인터페이스 비교 도구로 만듭니다. 피드, 프로필, 스레드, 다이렉트 메시지, 검색, zap, 릴레이 컨트롤의 느낌을 처음 사용자에게 사전에 ID나 보안 결정을 요구하지 않고 보여줍니다.


### mineracks signer는 브라우저 확장과 데스크톱 벙커를 결합

[mineracks signer](https://github.com/mineracks/mineracks-signer)는 동일한 프로젝트에서 두 가지 서명 표면을 제공합니다. 브라우저 확장은 [NIP-07](/ko/topics/nip-07/)을 구현하여 웹 애플리케이션이 개인 키를 받지 않고 서명을 요청할 수 있게 하고, 데스크톱 애플리케이션은 릴레이를 통해 통신하는 클라이언트를 위한 [NIP-46](/ko/topics/nip-46/) 원격 서명자를 노출합니다.

프로젝트의 [데스크톱 0.1.0 릴리스](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0)는 키 자료를 NIP-49 암호화 키 인코딩으로 저장하고 복호화된 키를 인터페이스에 전달하는 대신 Rust 프로세스 내에 유지합니다. 각 요청은 호출 애플리케이션과 요청된 작업을 표시하며, 애플리케이션별 자동 승인은 선택 사항이고 취소 가능합니다. 첫 번째 데스크톱 빌드는 Apple Silicon을 지원하지만 Intel Mac은 지원하지 않습니다.

## 릴리스

### Jumble 26.8.1은 작업 증명 컨트롤과 댓글 미리보기를 추가

[Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1)은 웹 및 데스크톱 Nostr 클라이언트입니다. 게시를 위한 작업 증명 난이도를 기억하고, 검증된 작업 배지를 표시하며, 외부 콘텐츠 위에 링크된 댓글을 미리 보고, 전체 화면 뷰어에서 이미지를 저장하고, 긴 프로필 약력을 온디맨드로 확장합니다. 리액션 알림은 이제 지원되지 않는 이벤트 kind를 버리고, 릴레이 연결 해제 알림은 덜 시끄러워지며, 기본 릴레이가 새로 고쳐지고, 미디어 자동 재생 충돌이 수정되었습니다.

### nostr-calendar 2.1.0은 비공개 양식 서명자 바인딩을 복원

[nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0)은 캘린더, 이벤트, 양식 응답을 Nostr 데이터로 게시합니다. 비공개 양식 제출을 활성 서명자에 바인딩하고, 의도적인 중복 이벤트를 릴레이에 저장하며, 릴레이 가져오기를 수정하고, 캘린더 날짜를 현지 시간으로 구문 분석하고, 앱 알림과 iOS 클라이언트를 추가합니다. 서명자 수정은 오래된 ID가 사용할 수 없는 암호화된 응답을 생성하는 것을 방지합니다.

### Manent 2.0.0은 저장된 노트에 태그 지정 및 검색을 추가

[Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0)은 서명된 Nostr 노트의 개인 아카이브입니다. 로컬 태그와 검색을 추가하여 독자가 서명된 콘텐츠를 수정하지 않고 저장된 이벤트를 구성하고 검색할 수 있게 합니다.

### nosvelte 0.6.1은 EOSE 후 빈 구독을 닫음

[nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1)은 릴레이 데이터를 위한 반응형 Svelte 컴포넌트와 훅을 제공합니다. 빈 검색은 이제 End of Stored Events에서 해결되고, 취소는 기본 `REQ`를 닫으며, 재시도는 오래된 오류를 지우고, 목록 훅은 문서화된 빈 값을 반환합니다. 또한 `d` 태그가 어디에 나타나든 어드레서블 이벤트를 인식하고, 대체된 메타데이터와 기사를 교체하고, 이벤트 ID로 리액션을 중복 제거하고, 릴레이의 첫 번째 배치에서 모든 이벤트를 유지합니다.

## 미릴리스 변경 사항

### NMP는 릴레이 입장을 선언에 묶고 그룹 쿼리를 확장

[NMP](https://github.com/pablof7z/nmp)는 Nostr 애플리케이션과 릴레이 지원 그룹 인터페이스를 구축하기 위한 TypeScript 툴킷입니다. [PR #1254](https://github.com/pablof7z/nmp/pull/1254)는 릴레이 입장이 이를 승인하는 선언의 소유자를 따르도록 하여 권한 결정을 서명된 Nostr 상태에 연결된 상태로 유지합니다. [PR #1255](https://github.com/pablof7z/nmp/pull/1255)는 하나의 좁은 조회 형태를 가정하는 대신 [NIP-29](/ko/topics/nip-29/) 릴레이 관리 그룹 쿼리를 일반화합니다. 두 변경 사항 모두 병합되었지만 아직 태그가 지정된 릴리스에 나타나지 않았습니다.

### Mosaico는 릴레이 레코드에서 관리 그룹 ID를 도출

[Mosaico](https://github.com/pablof7z/mosaico)는 릴레이 관리 커뮤니티를 탐색하고 관리하기 위한 Nostr 클라이언트입니다. [PR #758](https://github.com/pablof7z/mosaico/pull/758)은 관리 그룹의 ID를 권위 있는 레코드를 호스팅하는 릴레이에서 도출합니다. [PR #757](https://github.com/pablof7z/mosaico/pull/757)은 관리 상태를 해결할 때 그룹의 게시된 레코드를 관찰합니다. 이를 통해 서로 다른 릴레이에서 비슷한 이름을 가진 두 그룹을 구별하고 클라이언트에 관리 메타데이터를 위한 릴레이 지원 소스를 제공합니다.

### Divine은 멀티 릴레이 쿼리 중 느린 릴레이를 격리

[Divine](https://github.com/divinevideo/divine-mobile)은 Nostr를 통해 비디오를 게시하고 검색하는 모바일 숏폼 비디오 클라이언트입니다. [PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673)은 하나의 정체된 연결이 전체 요청의 타임아웃 예산을 소비하도록 하는 대신 각 릴레이 쿼리에 자체 타임아웃을 부여합니다. 응답성이 높은 릴레이의 결과는 느린 엔드포인트가 독립적으로 포기되는 동안 도착할 수 있습니다. 이 변경은 하나의 릴레이를 결합된 결과의 권위로 취급하지 않고 검색을 개선합니다.

### rust-nostr은 암호화, 해시, 조정을 강화

[rust-nostr](https://github.com/rust-nostr/nostr)는 Nostr 클라이언트, 릴레이, 프로토콜 구현을 위한 Rust 라이브러리이자 툴킷입니다. [PR #1421](https://github.com/rust-nostr/nostr/pull/1421)은 [NIP-44](/ko/topics/nip-44/) 버전 지정 암호화 경로의 할당을 줄이고, [PR #1423](https://github.com/rust-nostr/nostr/pull/1423)은 호환되지 않는 다이제스트 값을 실수로 혼합하기 어렵게 만드는 형식화된 해시를 도입합니다. [커밋 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69)는 잘못된 형식의 [NIP-77](/ko/topics/nip-77/) Negentropy 집합 조정 메시지가 로컬 릴레이를 연결 해제하는 것을 방지합니다. 병합된 작업은 다음 릴리스 전에 암호화된 페이로드 처리와 조정 실패 동작을 모두 강화합니다.

### Zeus는 지출 예산을 청구하기 전에 NWC 지불을 직렬화

[Zeus](https://github.com/ZeusLN/zeus)는 Nostr Wallet Connect를 통해 지갑 작업을 노출할 수 있는 모바일 Bitcoin 및 Lightning 지갑입니다. [PR #4305](https://github.com/ZeusLN/zeus/pull/4305)는 결제를 기다리는 대신 보류 중인 지불을 [NIP-47](/ko/topics/nip-47/) Nostr Wallet Connect 예산에 계산합니다. [PR #4303](https://github.com/ZeusLN/zeus/pull/4303)은 동시 요청이 동일한 승인 한도를 경쟁적으로 통과할 수 없도록 지불 처리를 직렬화합니다. 병합된 쌍은 지갑의 Nostr 제어 표면에서 예산 집행 격차를 닫습니다.

### Nostr Components는 하나의 릴레이 연결 시도를 공유

[Nostr Components](https://github.com/saiy2k/nostr-components)는 애플리케이션에 Nostr 데이터와 상호작용을 추가하기 위한 재사용 가능한 웹 컴포넌트 라이브러리입니다. [PR #105](https://github.com/saiy2k/nostr-components/pull/105)는 동시에 마운트된 컴포넌트가 진행 중인 릴레이 연결 시도를 공유할 수 있게 합니다. 각 소비자는 결과 연결을 계속 받지만, 동시 마운트는 첫 번째 핸드셰이크가 보류 중인 동안 더 이상 중복 소켓을 열지 않습니다. 이 변경은 여러 독립 컴포넌트로 조립된 애플리케이션에서 피할 수 있는 릴레이 부하를 줄입니다.

## NIP 업데이트 및 프로토콜 사양 작업

### Nostr 이벤트 형식 및 검색

[NIP PR #2430](https://github.com/nostr-protocol/nips/pull/2430)은 스티커 팩을 어드레서블 kind `30031` 정의로, 사용자의 설치된 팩을 교체 가능한 kind `10031`로 제안합니다. 각 스티커 태그는 숏코드, SHA-256 해시, MIME 유형을 가지며, 이미지는 [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md)(Blossom 블롭 저장소) 서버에 남아 있습니다. 공개 초안은 이미지 바이트를 이벤트에 넣지 않고 팩 ID와 설치를 표준화합니다.

[NIP PR #2429](https://github.com/nostr-protocol/nips/pull/2429)는 kind `31436` 어드레서블 Gopher 문서를 제안합니다. 각 이벤트는 하나의 UTF-8 텍스트 또는 메뉴 노드를 보유하고, 하나의 pubkey 아래에서 서명된 노드는 모든 릴레이 지원 RFC 1436 브리지가 제공할 수 있는 gopherhole을 형성합니다. 공개 제안은 게시를 하나의 Gopher 호스트 이름에 묶는 대신 일반 어드레서블 이벤트 저장소를 사용합니다.

[NIP PR #2428](https://github.com/nostr-protocol/nips/pull/2428)은 에포크 티켓 방식의 비공개 그룹을 제안합니다. 그룹은 에포크 사이에서 멤버십 자격 증명을 순환하고, 클라이언트는 참여하기 위해 현재 에포크의 티켓을 제시합니다. 초안은 영구적인 베어러 토큰을 평생 멤버십으로 취급하도록 릴레이에 요구하지 않고 비공개 채팅을 대상으로 합니다.

지난주 제안으로 다룬 [NIP PR #2425](https://github.com/nostr-protocol/nips/pull/2425)는 이제 [NIP-B0](/ko/topics/nip-b0/)(어드레서블 웹 북마크)에 URI 명확화를 병합했습니다. 북마크가 `d` 태그에 대상을 저장할 때 생략된 HTTPS 접두사와 명시적 URI 스킴을 구별하여 클라이언트가 모호한 대상을 재구성하는 것을 방지합니다.

### 지불 및 지갑 연결

7월 22일 호에서 제안으로 다룬 [NIP PR #2419](https://github.com/nostr-protocol/nips/pull/2419)는 이제 더 작은 [NIP-47](/ko/topics/nip-47/)(Nostr Wallet Connect) 코어를 병합했습니다. 연결 URI, 암호화된 릴레이 전송, 기능 검색, 암호화 협상, 공통 메서드는 NIP에 남아 있고, 알림, 보류 인보이스, keysend, 거래 기록, 메타데이터, 딥 링크 페어링은 전용 확장 리포지토리로 이동합니다. 기존 연결은 호환성을 유지하며 지갑은 선택적 계약을 독립적으로 구현할 수 있습니다.

지난주 제안으로 다룬 [NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2)는 이제 해당 확장 리포지토리에 BIP-321 지불 방법을 병합했습니다. BIP-321은 다양한 레일을 운반할 수 있는 공통 Bitcoin 지불 URI를 제공하므로 NWC 호출자는 기본 명령 유형마다 새로운 코어 RPC를 추가하지 않고도 지불을 요청하거나 보낼 수 있습니다.

### Napplet 호스트 기능

[NAP PR #95](https://github.com/napplet/naps/pull/95)는 Nostr 분산 샌드박스 애플리케이션을 위한 카탈로그 검색을 제안합니다. napplet은 호스트에 어떤 애플리케이션과 기능을 사용할 수 있는지 묻고, 호스트는 전체 로컬 환경을 노출하는 대신 정책으로 필터링된 메타데이터를 반환합니다. 이 계약은 검색 중에 실행 권한을 부여하지 않고 시작 결정을 지원합니다.

[NAP PR #33](https://github.com/napplet/naps/pull/33)은 셸 매개 파일 및 블롭 업로드를 제안합니다. napplet은 바이트와 의도를 제공하고, 호스트는 NIP-96 또는 Blossom 레일을 선택하고, 승인에 서명하고, 진행 상황을 보고하고, URL, 해시, MIME 데이터, 첨부 가능한 [NIP-94](/ko/topics/nip-94/)(파일 메타데이터) 태그를 반환합니다. 저장소 자격 증명과 HTTP 권한은 napplet에 들어가지 않습니다.

### Marmot 암호화 그룹

[Marmot PR #410](https://github.com/marmot-protocol/marmot/pull/410)은 수렴 및 지연 입력 규칙을 병합했습니다. 클라이언트는 현재 에포크 종속성이 없는 객체를 오래되거나 잘못된 입력과 구별하고, 리소스 거부 후 다시 가져올 수 있는 상태로 유지하며, 다른 커밋이 복호화 컨텍스트를 변경할 때 재시도합니다. 도메인 분리된 상태 커밋먼트는 프로덕션 와이어 필드를 추가하지 않고 적합성 테스트에 공유 수렴 오라클을 제공합니다.

### Concord 커뮤니티 플레인

[Concord PR #14](https://github.com/concord-protocol/concord/pull/14)는 CORD-08 사라지는 메시지를 병합했습니다. 하나의 커뮤니티 메타데이터 값이 수명을 설정하고, 채팅 루머와 암호화 랩은 [NIP-40](/ko/topics/nip-40/)(이벤트 만료) 태그를 가지며, 삭제 이벤트와 kind `1740` 타이머 알림은 면제됩니다. 서명된 타이머는 커뮤니티 상태와 함께 이동하지만, 릴레이 삭제는 암호화 삭제 보장이 아닌 보존 요청으로 남아 있습니다.

[Concord PR #13](https://github.com/concord-protocol/concord/pull/13)은 CORD-04에 순환 방지 고정을 병합했습니다. 각 채널은 컨트롤 플레인에 하나의 전체 교체 고정 목록을 가지고, 항목은 원래 서명된 봉인과 메시지별 NIP-44 확장 키를 가지므로 새 멤버가 오래된 에포크 키를 받지 않고도 작성자와 평문을 검증할 수 있습니다. 비공개 목록은 채널 에포크에 봉인된 상태로 유지될 수 있고, 상한은 목록 크기를 제한하며, 작성자 삭제는 컨트롤 플레인 체인을 포크하지 않고 고정을 제거합니다.

## NIP 심층 분석

### 검색 기능(NIP-50)

[기본 사양](https://github.com/nostr-protocol/nips/blob/master/50.md)에서 정의된 [NIP-50](/ko/topics/nip-50/)은 릴레이를 위한 선택적 검색 필터를 추가합니다. 클라이언트가 이미 작성자, 이벤트 kind, 식별자 또는 태그를 알고 있을 때 일반 Nostr 필터는 작동합니다. NIP-50은 입력이 `best nostr apps`와 같은 인간 쿼리일 때 검색을 다룹니다.

[NIP-50 와이어 형식](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field)은 `REQ` 메시지 내의 일반 필터에 `search` 문자열을 추가합니다. 요청은 해당 필드를 `kinds`, `authors`, `ids`, 태그 필터, `limit`과 결합할 수 있고, 하나의 REQ는 여러 독립 필터를 운반할 수 있습니다. 지원하는 릴레이는 주로 이벤트의 `content`에 대해 일치시키고, 이벤트 kind가 유용하게 만들 때 다른 필드를 사용할 수 있으며, `limit`을 적용하기 전에 자체 관련성 점수로 정렬해야 합니다. 그 순서는 일반적인 최신 순 이벤트 스트림과 다릅니다.

쿼리 문자열은 사양의 [`key:value` 확장](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions)을 포함할 수 있습니다. `include:spam`, `domain:`, `language:`, `sentiment:`, `nsfw:`를 명명하며, 릴레이는 구현하지 않은 확장을 무시해야 합니다. 클라이언트는 릴레이의 [NIP-11](/ko/topics/nip-11/) `supported_nips` 필드를 통해 선언된 지원을 발견하지만, 관련 없는 응답을 거부할 준비가 되어 있다면 다른 곳에 필터를 보낼 수 있습니다.

[NIP-50 사양](https://github.com/nostr-protocol/nips/blob/master/50.md)은 토큰화, 스테밍, 순위 지정, 언어 감지, 감정 분석, 스팸 분류를 의도적으로 표준화하지 않습니다. 두 개의 준수 릴레이는 동일한 쿼리에 대해 서로 다른 이벤트와 다른 순서를 반환할 수 있습니다. 이는 릴레이를 진실의 원천이 아닌 인덱스 및 순위 제공자로 만듭니다. 사양은 여러 지원 릴레이를 쿼리하고, 반환된 이벤트가 클라이언트의 사용 사례를 충족하는지 확인하고, 정밀도가 낮은 결과를 제공하는 릴레이를 버릴 것을 권장합니다.

이는 정확한 [NIP-01 필터링](https://github.com/nostr-protocol/nips/blob/master/01.md)과 다릅니다. `authors` 또는 `#t` 필터에는 클라이언트가 직접 검증할 수 있는 결정적 일치 의미가 있지만, 검색 일치는 인덱스와 불투명한 점수에 의존할 수 있습니다. NIP-50은 NIP-01의 서명된 이벤트 봉투와 릴레이 전송을 유지하지만, 개방형 검색을 가능하게 하기 위해 재현율과 순서 지정의 변동을 받아들입니다.

아래 이벤트는 [7개의 NIP-01 이벤트 필드](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures)를 사용한 예시 검색 결과입니다. 반복되는 16진수 값은 유효한 서명이 아닌 자리 표시자입니다.

```json
{
  "id": "2943d6b43bcbf0ee4a8b4cac912111be0309607b8bb435ae40529989bea7f6c5",
  "pubkey": "3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d",
  "created_at": 1785771175,
  "kind": 1,
  "tags": [],
  "content": "I've been working on a customizable client (mostly relay feeds, but a ton of other things and subtle details too). It's called Hallway for reasons I don't remember and it's a fork of Fevela which is a fork of Jumble, but very rewritten for speed and simplicity...",
  "sig": "5b058b89dab9bd09d81bdc10eff95536125b87fbcbbc97f08d835c1272b2a3190cc3d340e42f54acb0d7e0e4b00355ab91292d0305c84a2d73b538319c0da12c"
}
```

현재 클라이언트는 서로 다른 검색 표면에서 동일한 필터를 사용합니다. [Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts)는 전용 검색 릴레이에 NIP-50 검색을 보내고, [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts)는 릴레이 풀을 통해 이벤트를 검색하며, [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts)는 장문 읽기를 위한 릴레이 지원 검색을 조정합니다. 서로 다른 결과 처리는 NIP-50이 릴레이와 클라이언트에 남기는 자유를 반영합니다.

### 하이라이트(NIP-84)

[기본 사양](https://github.com/nostr-protocol/nips/blob/master/84.md)에서 정의된 [NIP-84](/ko/topics/nip-84/)는 하이라이트에 kind `9802`를 할당합니다. 선택된 구절이나 비텍스트 미디어에 대한 참조를 읽기, 소셜, 주석 클라이언트 간에 이동할 수 있는 서명된 이벤트로 바꿉니다.

[이벤트의 `content`](https://github.com/nostr-protocol/nips/blob/master/84.md#format)에는 선택된 텍스트가 포함되며 소스가 오디오, 비디오 또는 다른 비텍스트 매체일 때 비어 있을 수 있습니다. 하이라이트는 어드레서블 이벤트에는 `a` 태그로, 일반 이벤트에는 `e` 태그로 Nostr 소스를 가리키고, `r` 태그는 웹 URL을 식별합니다. URL을 생성하는 클라이언트는 게시하기 전에 추적 및 기타 유용하지 않은 쿼리 매개변수를 제거하여 외형적 URL 변형이 동일한 소스에 대한 참조를 분열시키지 않도록 해야 합니다.

선택적 [`p` 태그](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution)는 소스를 하나 이상의 Nostr pubkey에 귀속시킵니다. 네 번째 값은 `author` 또는 `editor`와 같은 역할을 식별할 수 있고, `context` 태그는 선택만으로는 불명확할 때 주변 텍스트를 보존할 수 있습니다. 인용 하이라이트는 두 번째 kind `1` 노트를 게시하는 대신 `comment` 태그를 추가합니다. 소스의 `r` 태그는 `source` 마커를 받고, 댓글에서 언급된 pubkey나 URL은 `mention`을 가지므로 렌더러가 귀속과 사용자의 응답을 구별할 수 있습니다.

[kind `9802` 정의](https://github.com/nostr-protocol/nips/blob/master/84.md)는 하이라이트를 교체 가능한 이벤트가 아닌 일반 이벤트로 만듭니다. 선택을 반복하거나 수정하면 다른 서명된 이벤트가 생성되고, 하나를 제거하는 것은 일반적인 삭제 요청 흐름과 릴레이 보존 정책에 의존합니다. 사양은 바이트 오프셋, 선택자 또는 정규 문서 스냅샷을 정의하지 않으므로 클라이언트는 웹 소스가 변경된 후 구절을 재배치하지 못할 수 있습니다. 공개 하이라이트는 읽기 관심사도 드러내며, 비공개 주석은 별도의 암호화 및 공유 설계가 필요합니다.

NIP-84는 전체 기사를 kind `30023`으로 게시하는 [NIP-23 장문 이벤트](https://github.com/nostr-protocol/nips/blob/master/23.md)와 다릅니다. 하이라이트는 다른 곳에 남아 있을 수 있는 자료를 인용하거나 가리킵니다. 또한 교체 가능한 참조 컬렉션을 저장하는 [NIP-51 북마크 세트](https://github.com/nostr-protocol/nips/blob/master/51.md)와도 다릅니다. NIP-84는 각 선택을 독립적으로 서명되고, 귀속 가능하고, 검색 가능하고, 논의 가능하게 만듭니다.

이 예시 하이라이트에는 [7개의 NIP-01 이벤트 필드](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures)가 포함되어 있습니다. 식별자와 서명은 자리 표시자입니다.

```json
{
  "id": "0d57c07cfdfe8ec00711e2af88a666b61fc35c167b90b02dfb5db7ffba7b794a",
  "pubkey": "07367baec8e73c076b14e47fba3b0d5c014d559d7986a7172a79a8a64419d7c2",
  "created_at": 1785797755,
  "kind": 9802,
  "tags": [
    ["context", "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will be able to derive your nsec, read all your encrypted data and sign events as you."],
    ["alt", "This is a highlight created in https://primal.net iOS application"],
    ["a", "30023:1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139:nostr-quantum-preparation"],
    ["p", "1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139", "", "mention"]
  ],
  "content": "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will b",
  "sig": "219f3c1e572d1a087d667dc0d3a5443c77c0db3a5d42ce4e630604901ac63d2c879a86269d81e220bb77fd48b1579adafc333075e53c6eb0a108791fdd4a1622"
}
```

이 형식은 이미 클라이언트 경계를 넘고 있습니다. [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0)은 이번 주에 NIP-84 렌더링을 추가했고, [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts)는 장문 클라이언트에서 하이라이트 이벤트를 렌더링하며, [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts)는 선택된 콘텐츠에서 이를 게시합니다. 이러한 구현은 하나의 서비스가 주석을 소유할 필요 없이 읽기, 생성, 소셜 렌더링을 다룹니다.

---

[Nostr Compass 프로젝트](https://github.com/andotherstuff/nostr-compass)를 통해 프로젝트나 뉴스를 공유하려면 NIP-17 DM을 보내주세요.
