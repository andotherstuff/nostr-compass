---
title: 'Nostr Compass #21'
date: 2026-05-06
publishDate: 2026-05-06
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-06-newsletter.md
translationDate: 2026-05-13
---

Nostr Compass에 오신 것을 환영합니다. Nostr의 주간 가이드입니다.

**이번 주:** Marmot Protocol이 첫 번째 MIP-05 알림 프리미티브, 주소 지정 가능한 NIP-51 키 패키지, 강화된 보안 검토를 포함한 MDK 0.8.0을 출시했습니다. LaWallet NWC가 OpenSats 펀딩 이후 최대 릴리스인 v0.10.0을 출시하며, 완전한 관리자 대시보드, 사용자 지갑, 종단간 활동 로그, 새로운 LightningAddress 1→N 및 NWCConnection 스키마를 제공합니다. Amethyst가 JWT 갱신 중 오디오 끊김 제거, 수명주기 인식 키 데이터 구독, 릴레이 keep-alive 재연결, 애니메이션 발언 참가자 표시기를 포함한 Nests 안정화 스프린트를 진행했습니다. ngit가 PR 제출을 위한 GRASP 서버 감지 수정과 멀티 리모트 상태 이벤트 필터링을 수정한 v2.4.2와 v2.4.3을 출시했습니다. GRAIN이 프로덕션 강화와 자동 데이터 손실 수정을 포함한 v0.5.4를 출시했습니다. Mostro Core가 PGP 서명 릴리스 아티팩트를 포함한 v0.10.1을 출시했습니다. Clave가 iOS에서 멀티 계정 지원을 포함한 v0.2.0을 출시했습니다.

## 주요 소식

### MDK 0.8.0이 MIP-05 알림 프리미티브와 주소 지정 가능한 키 패키지 추가

Marmot 프로토콜의 Rust 핵심 라이브러리인 MDK가 5월 4일에 v0.8.0을 출시했습니다. 이번 릴리스는 첫 번째 MIP-05 알림 빌딩 블록을 포함하며, MIP-00 키 패키지를 주소 지정 가능한 이벤트로 이전하여 사용자의 키 패키지를 제자리에서 교체할 수 있게 합니다. 혼합 버전 그룹 호환성을 개선하고, 모바일 바인딩을 위한 UniFFI 커버리지를 확장하며, 관리자 작업, 커밋, 저장소, 암호화 경계, 리플레이 처리에 대한 유효성 검사 경로를 강화합니다. MIP-05 프리미티브에는 PR #235에 추가된 리프 인덱스 헬퍼가 포함되어 있으며, 이는 다운스트림 클라이언트에게 그룹 구조를 노출하지 않고 수신자별 푸시 알림을 전달하기에 충분한 정보를 제공합니다. PR #273은 mdk-core crates.io 게시를 복원하고, PR #269는 외부 클라이언트 테스트 스위트가 Marmot의 테스트 하네스를 공유할 수 있도록 test-utils Cargo 기능 뒤에 test_util 모듈을 노출합니다.

### LaWallet NWC v0.10.0이 전체 모노레포와 사용자 지갑 출시

LaWallet 팀의 NIP-47 Nostr Wallet Connect 구현인 LaWallet NWC가 4월 30일에 v0.10.0을 출시했습니다. 이것은 프로젝트가 OpenSats 펀딩을 받은 이후 최대 릴리스입니다. 전체 모노레포, 완전한 관리자 대시보드, 사용자 지갑, 종단간 활동 로그, 동적 브랜딩, 새로운 LightningAddress 1→N 및 NWCConnection 스키마를 제공합니다. PR #191에서 출시된 사용자 대면 지갑은 온보딩, 홈, 송수신, 스캔, 통화, 활동 피드, 오프라인 캐시를 포함합니다.

### Amethyst가 keep-alive, JWT 복원력, 수명주기 구독으로 Nests 안정화

기능이 풍부한 Android 클라이언트인 Amethyst가 프로덕션에서 통화를 끊는 실패 모드에 초점을 맞춘 안정화 스프린트와 함께 NIP-53 Nests 오디오룸 작업을 계속했습니다. PR #2733의 오디오 끊김 수정은 JWT 갱신 중 활성 스트림과 새 자격증명 취득을 겹칩니다. PR #2730의 새로운 keep-alive 메커니즘이 수동 사용자 작업 없이 끊어진 릴레이를 재연결하고, PR #2728은 레거시 KeyDataSourceSubscription을 LifecycleAwareKeyDataSourceSubscription으로 교체합니다. PR #2724는 멀티 스피커 세션에서 발언 중인 참가자를 강조하는 애니메이션 외부 링 표시기를 추가합니다.

### ngit v2.4.2와 v2.4.3이 GRASP 서버 감지와 멀티 리모트 상태 이벤트 수정

NIP-34 협업을 위한 명령줄 도구 및 git 플러그인인 ngit가 4월 28일에 v2.4.2를, 5월 1일에 v2.4.3을 출시했습니다. v2.4.2는 repo_grasps가 정규화된 호스트명을 포함하지만 비교가 전체 클론 URL에 대해 이루어지던 URL 정규화 불일치를 수정합니다. v2.4.3은 저장소가 같은 식별자를 공유하는 여러 nostr:// 리모트를 가질 때 발생하는 상태 이벤트 모호성을 수정합니다.

### GRAIN v0.5.4가 프로덕션 강화와 자동 데이터 손실 수정 제공

Go 기반 Nostr 릴레이 및 클라이언트 라이브러리인 GRAIN이 4월 30일에 v0.5.4를 출시했습니다. 이번 릴리스에는 v0.5.3 이후 누적된 6가지 수정 사항이 포함되며, 컨테이너 재시작 시 이전에 이벤트를 삭제하던 Docker 빠른 시작의 자동 데이터 손실 버그와 주소 지정 가능한 이벤트 읽기의 저장소 레이어 정확성 버그가 수정됩니다.

### Mostro Core v0.10.1이 PGP 서명 릴리스 아티팩트 추가

Mostro 데몬의 P2P 기능을 제공하는 Rust 라이브러리인 Mostro Core가 4월 28일에 v0.10.1을 출시했습니다. 새 릴리스는 PGP 서명 릴리스 아티팩트와 릴리스 검증 흐름을 추가하여 다운스트림 패키저가 아티팩트 출처를 확인할 수 있게 합니다.

## 릴리스

### Clave v0.2.0이 NIP-46(Nostr Connect) 서명으로 iOS에서 멀티 계정 지원 출시

iOS NIP-46 원격 서명 앱인 Clave가 5월 5일에 v0.2.0을 출시했습니다. 가장 큰 업데이트는 멀티 계정 지원입니다: Clave는 이제 하나의 기기에서 최대 4개의 계정을 보유할 수 있으며, 원탭 전환기와 계정별 격리를 제공합니다. PR #23은 멀티 계정을 위한 iOS 배관을 추가하고, PR #22는 APNs 페이로드에 signer_pubkey 필드를 추가하여 기기가 원격 서명 요청이 어느 계정에 속하는지 알 수 있게 합니다.

### Wisp가 v1.0.3 → v1.0.5 안정화 작업 출시

Android 클라이언트인 Wisp가 5월 4일에 v1.0.3, v1.0.4, v1.0.5를 출시하며 안정화 작업을 진행했습니다. PR #506은 전체 미디어 로딩 중 흐린 이미지 미리보기를 위한 Thumbhash를 추가하고, PR #514는 하단 탭 전환 끊김을 줄입니다.

### Amber 6.1.0-pre1이 레이아웃 및 안정성 수정 출시

NIP-55 및 NIP-46용 Android 서명 앱인 Amber가 새 앱 연결 흐름의 레이아웃 패스와 여러 충돌 수정을 포함한 v6.1.0-pre1을 출시했습니다. PR #416은 ActivityStatsBar 레이아웃과 텍스트 오버플로우 문제를 수정합니다.

### Routstr Core v0.4.3이 결제, 환불, 사용 보고 개선

Routstr Core가 5월 1일에 결제 및 환불 처리, 비용 추적, 사용 보고 개선을 포함한 v0.4.3 사전 릴리스를 출시했습니다.

### Nostria v3.1.37에서 v3.1.41이 웹 북마크와 자동 테마 추가

멀티 플랫폼 Nostr 클라이언트인 Nostria가 NIP-B0 웹 북마크 지원, 기기 설정을 따르는 자동 테마, 앱 내 PDF 보기를 추가하며 v3.1.37에서 v3.1.41을 출시했습니다.

### NoorNote v0.8.9가 데스크톱 첫 실행 빈 화면 수정

NoorNote가 4월 28일에 데스크톱 앱의 첫 실행 시 빈 화면 버그를 수정한 v0.8.9를 출시했습니다.

### Kubo v0.3.4에서 v0.4.1이 부모 통제와 Web of Trust 피드 큐레이션을 갖춘 아동 안전 Nostr 비디오 플랫폼 출시

Nostr 기반의 아동 안전 비디오 플랫폼인 Kubo가 5월 4일과 5일에 걸쳐 v0.3.4에서 v0.4.1을 출시했습니다. 각 어린이는 별도의 Nostr 키 쌍과 비디오 중심 피드를 받으며, 부모는 시간 제한(일일 15~180분), 허용 시간 창, 게시 작업 가시성을 통제합니다.

## 미출시 변경사항

### Sprout가 Desktop v0.0.4와 v0.0.5, NIP-OA 에이전트 인증, 페어링 릴레이 사이드카 출시

Block의 내장 릴레이가 있는 Nostr 클라이언트인 Sprout가 5월 5일에 Desktop v0.0.4를, 5월 6일에 v0.0.5를 출시했습니다. PR #471은 NIP-OA 에이전트 인증을 릴레이의 NIP-43 멤버십 흐름에 연결하여 자율 에이전트가 특정 인간 공개키가 자신의 작업을 승인했음을 증명할 수 있게 합니다. NIP-AB 기기 페어링을 위한 새로운 임시 사이드카 릴레이가 PR #467에서 sprout-pair-relay로 도착합니다.

### nostream이 Marmot 릴레이 지원과 NIP-25 반응 추가

Node.js 릴레이 구현인 nostream이 PR #602에서 MIPs 00부터 03을 포함하는 Marmot Protocol 릴레이 지원을, PR #589에서 NIP-25 반응 지원을, PR #586에서 #g 필터를 위한 지오해시 접두사 매칭을 병합했습니다.

### strfry가 연결별 관찰 가능성 추가 및 nofiles 한도 감소

C++ Nostr 릴레이인 strfry가 관찰 가능성을 대상으로 한 14개의 PR을 병합했습니다. PR #218은 연결별 보류 중인 아웃바운드 관찰 가능성과 구성 가능한 배압 한도를 추가합니다. PR #224는 이벤트별 모니터 팬아웃에서 std::function 힙 할당을 제거합니다.

### Damus가 Tenor GIF를 Purple 프록시로 교체하고 압축 UX 출시

Damus가 Tenor GIF 통합을 Damus Purple 프록시로 교체하는 PR #3737을 병합했습니다.

### Primal Android가 탐색, 알림, NIP-05 인증 배지 개선

Primal Android가 _@domain 식별자를 가진 사용자의 깜박이는 NIP-05 인증 배지를 수정하는 PR #1043을 병합했습니다.

### Alby Hub이 앱 연결에서 NWC 결제 추가

Alby Hub이 앱 연결에서의 결제를 허용하는 PR #2267을 병합했습니다.

### routstrd-auth: NIP-98 인증과 npub RBAC를 갖춘 팀용 도커화 Routstrd

4월 27일에 생성된 routstrd-auth는 npub 기반 역할 기반 액세스 제어와 NIP-98 HTTP 인증을 갖춘 멀티 사용자 팀 배포를 위한 Routstrd의 도커화 변형입니다.

### Routstrd가 데몬 클라이언트와 원격 모드를 위해 Hermes 통합

Routstrd가 Hermes Agent와의 통합을 추가하는 PR #22를 병합하여 에이전트의 구성 파일이 Routstrd가 Nostr를 통해 발견하는 모델 제공업체와 API 키로 채워집니다.

### whitenoise-rs가 계정별 데이터베이스 격리와 제안 업그레이드 출시

whitenoise-rs가 메시지 프로젝션 테이블을 계정별 데이터베이스로 이동하는 PR #796을 병합하고, PR #791은 그룹이 새로운 제안 유형으로 기능을 확장할 수 있는 제안 업그레이드를 추가합니다.

### Angor 0.2.21이 컴팩트 앱 흐름과 키 제공자 및 네트워크 전환 강화 출시

Angor가 5월 6일에 모바일 디자인 성능 개선, 컴팩트 앱 흐름, 보안 키 제공자를 포함한 0.2.21을 출시했습니다.

## 새로 추적 및 발견

### BitMacro Signer: 클라이언트 측 키 암호화를 갖춘 자체 호스팅 가능한 NIP-46 벙커

BitMacro Signer는 NIP-46 벙커 모델을 사용하는 자체 호스팅 가능한 Nostr 서명 도구입니다. 키는 저장 전에 클라이언트에서 암호화되어 서버는 평문을 보유하지 않습니다.

NIP-34 저장소 발견이 이번 주 26개의 새로운 저장소 발표를 발견했으며, 그 중 4개가 두드러집니다.

### gnostr: Nostr 위에 직접 구축된 git 구현

gnostr는 Nostr 위에 직접 구축된 git 구현으로, 처음부터 만들어진 Nostr 네이티브 버전 제어 클라이언트로서 자체 작업 트리 명령어를 제공합니다.

### nostr-archive: Nostr와 Blossom 위의 내용 주소 지정 아카이브 사양

nostr-archive는 Nostr와 Blossom 위의 내용 주소 지정 아카이브를 위한 초안 사양 및 참조 구현입니다.

### flower-cache: 로컬 Blossom 캐시 서버

flower-cache는 원격 Blossom 서버의 블롭 세트의 핫 로컬 미러를 원하는 클라이언트에 유용한 로컬 Blossom 캐시 서버입니다.

### micro-vpn-ansible: NIP-34를 통한 VPN 배포를 위한 Ansible 플레이북

micro-vpn-ansible은 NIP-34 저장소로 호스팅되는 마이크로 VPN 배포를 위한 소규모 Ansible 플레이북 모음입니다.

## 프로토콜 작업

### NIP 업데이트

- Nostr 위의 브로커리스 해시레이트 시장 (초안 제안): 현재 해시레이트 시장 참여자들이 사용자를 KYC하는 위탁 브로커라고 주장하는 익명 초안 NIP. Nostr 이벤트 위의 P2P 해시레이트 시장을 제안합니다.
- Curated Feeds: DVM 피드의 더 간단한 대안 (초안 제안): NIP-90 DVM이 간단한 피드 큐레이션에 너무 무겁다고 주장하며, 순서 있는 이벤트 ID 목록을 가진 얇은 주소 지정 가능한 이벤트를 대신 제안합니다.
- Profile Colors: 결정론적 시각적 정체성 (초안 제안): 클라이언트 전반에 걸쳐 일관된 시각적 정체성을 위해 Nostr 공개키에서 결정론적 읽기 가능한 색상을 파생하는 새로운 NIP 초안.
- Namecoin-Track NIPs: 정체성, 릴레이, TLS, 평판 고정 (초안 클러스터): Nostr 스택 요소를 Namecoin 고정 레코드로 이동하는 초안 NIP 클러스터.

## NIP 심층 분석: NIP-34 (git stuff)

NIP-34는 Nostr 릴레이에서 git 저장소, 패치, 풀 리퀘스트, 이슈, 병합 상태를 호스팅하기 위한 이벤트 종류를 정의합니다. 저장소는 kind 30617 주소 지정 가능한 이벤트로 발표됩니다. 패치는 git format-patch 출력을 전달하는 kind 1617을 사용합니다. 풀 리퀘스트는 kind 1618을 사용합니다. 이슈는 마크다운 콘텐츠와 함께 kind 1621을 사용합니다. 상태 이벤트는 스레드를 Open(1630), Applied/Merged 또는 Resolved(1631), Closed(1632), Draft(1633) 사이에서 이동시킵니다. 이번 주 NIP-34 소식은 지난 주 GitWorkshop v2 출시와 같습니다: 브라우저 내 PR 병합 버튼이 작동하는 이유는 GRASP 서버, ngit, nostr:// 클론 URL 스키마가 완전히 분산된 포지의 루프를 함께 닫기 때문입니다.

## NIP 심층 분석: NIP-53 (Live Activities)

NIP-53은 Nostr의 라이브 활동을 위한 표준 이벤트 표면을 정의합니다: 라이브 스트림, 영구 미팅 공간, 예약된 컨퍼런스 이벤트, 청취자 존재, 라이브 채팅. 라이브 스트림은 kind 30311 주소 지정 가능한 이벤트로 발표됩니다. NIP-53은 영구 룸과 그 안에서 열리는 예약된 이벤트를 분리합니다: kind 30312 Meeting Space는 룸을 정의하고, kind 30313 Conference Event는 해당 룸의 예약되거나 진행 중인 미팅을 나타냅니다. Nostr 라이브 활동 표면은 의도적으로 얇습니다: NIP-53은 활동을 발표하고, 다른 NIP들이 zaps(NIP-57), zap 목표(NIP-75), 비디오 녹화(NIP-71)와 같은 인접 관심사를 처리합니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 공유할 소식이 있다면, Nostr에서 DM을 보내거나 nostrcompass.org에서 찾아보세요.
