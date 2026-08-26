---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
translationOf: /en/newsletters/2026-08-12-newsletter.md
translationDate: 2026-08-12
draft: false
type: newsletters
description: "양자 이후 대비 신원 도구, 강화된 암호화 메시징과 서명, 휴대용 커뮤니티 설정, NIP와 Concord 전반의 프로토콜 작업"
---

[Nostr Compass](https://nostrcompass.org)에 다시 오신 것을 환영합니다. Nostr 주간 가이드입니다.

**이번 주:** [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension)은 기존 Nostr 신원 옆에 post-quantum 키와 옵트인 보호 메시지를 추가합니다. [Divine](https://github.com/divinevideo/divine-mobile)은 계정 격리, 다이렉트 메시지 검증, 게시 확인을 강화하고, [MDK](https://github.com/marmot-protocol/mdk)는 암호화 그룹 수렴과 복구를 강화하며, [Amber](https://github.com/greenart7c3/Amber)는 그룹화된 서명 결정을 명시적으로 만듭니다. 릴리스는 지갑 연결, 암호화 채팅, 소셜 발견, 기기 동기화, 원격 서명을 개선하고, 프로토콜 작업은 신원과 암호화 커뮤니티를 다룹니다. 심층 분석에서는 인증된 삭제 요청과 분산 신고를 설명합니다.

## 주요 소식

### nostr-wot-extension 0.4.0은 Nostr 신원 옆에 post-quantum 키를 추가

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0)은 Nostr 신원을 관리하고 서명하는 브라우저 확장입니다. 24단어 시드에서 생성된 계정은 이제 기존 Nostr 키와 함께 ML-KEM-1024 암호화 및 ML-DSA-87 서명 키를 도출할 수 있습니다. 원클릭 흐름은 Nostr 공개 키를 두 post-quantum 공개 키에 바인딩하고 ML-DSA 소유 증명을 포함하는 kind `10203` 증명을 게시합니다. 12단어 니모닉, bare `nsec`, 원격 서명자, 또는 읽기 전용 키에서 가져온 계정은 도출 흐름을 사용할 수 없으며, 확장은 계정 보기에서 그 제한을 설명합니다.

릴리스는 또한 옵트인 post-quantum 다이렉트 메시지를 추가합니다. ML-KEM 공유 비밀을 HKDF를 통해 기존 [NIP-44 암호화 메시지 대화 키](https://github.com/nostr-protocol/nips/blob/master/44.md)와 결합한 다음, 릴레이 전달을 위해 일반적인 [NIP-59](/ko/topics/nip-59/)(gift wrap) 메타데이터 숨김 gift-wrap 레이어를 유지합니다. 수신자가 옵트인한 후 암호화는 조용히 폴백하지 않으며, 복호화는 적절한 경로를 자동으로 선택합니다. 이는 새 메시지 경로를 현재 Nostr 개인 키의 나중 복구로부터 보호하지만, secp256k1 이벤트 서명을 대체하지는 않습니다. 릴리스는 그 더 큰 마이그레이션을 릴레이와 클라이언트와의 향후 조정에 맡긴다고 명시합니다.

### Divine Mobile 1.0.19는 계정, 다이렉트 메시지, 게시를 강화

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19)는 Nostr를 통해 비디오를 게시하고 검색하는 모바일 숏폼 비디오 클라이언트입니다. 계정 전환기는 이제 각 로그인 신원을 계정 범위 컨테이너 주변에 구축하고, 게시 수정은 비디오가 잘못된 계정으로 전송되는 것을 방지합니다. 릴레이 게시 경로는 이제 명시적 성공 의미가 있는 `OK` 응답을 기다리며, 릴레이 `CLOSED` 프레임은 요청을 걸어두는 대신 자체 보류 쿼리를 종료할 수 있습니다.

[다이렉트 메시지 처리](https://github.com/divinevideo/divine-mobile/pull/6368)는 인증되지 않은 rumor 필드와 서명되지 않은 seal을 거부하고, 네 가지 누락 메시지 케이스를 복원하며, 완전히 팔로우한 참가자의 그룹 대화를 받은편지함으로 라우팅합니다. 릴리스는 또한 목록이 업데이트될 때 어드레서블 비디오 이벤트의 태그를 보존하고, 관찰된 삭제 요청을 소비하여 제거된 비디오가 로컬 상태에서 사라지게 합니다. 이러한 변경은 지난주 다룬 릴레이별 쿼리 타임아웃 작업을 따르지만, 초점을 검색 격리에서 신원 경계, 메시지 검증, 게시 확인으로 옮깁니다.

### MDK 0.9.11은 Marmot 그룹 수렴과 복구를 강화

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11)은 Nostr를 통해 전달되는 암호화 그룹 메시징 프로토콜 Marmot을 위한 Rust 개발 키트입니다. 릴리스는 그룹 상태 머신 주변에 더 큰 수렴 및 복구 시스템을 구축합니다. 오래된 수렴 패스는 현재 그룹 팁에서 다시 열리고, 인바운드 capability projection은 원자적으로 커밋되며, 지연된 메시지는 재시작 전반에 걸쳐 제한된 수명을 받고, 커밋 주소 지정 체크포인트는 신원의 자체 커밋 포크를 복구하는 데 도움이 됩니다. 비안정 전송은 대기열에 넣고 복구할 수 있으며, epoch-stall 경로는 backfill로 에스컬레이션하고 전송된 메시지는 수렴 작업을 견딥니다.

[스토리지 및 호스트 통합](https://github.com/marmot-protocol/mdk/pull/1201)은 병렬 강화 패스를 받습니다. MDK는 가지치기된 SQLite projection을 안전하게 삭제하고, 가져온 개인 키, [NIP-49](/ko/topics/nip-49/)(암호화된 개인 키 형식) 암호화 키 내보내기 중간 결과, OpenMLS 직렬화 버퍼를 영점화하며, 디버그 출력에서 그룹 이미지 키를 편집합니다. 계정 가져오기는 중단 후 재개할 수 있고, iOS 및 Android 개인 스토리지 경로가 수정되며, 호스트는 일시 중지 전에 스토리지를 명시적으로 닫을 수 있습니다. 새로운 경량 roster 및 로컬 멤버십 projection은 애플리케이션이 읽어야 하는 것을 줄이고, Hermes 커넥터는 여러 에이전트 생성 이미지를 하나의 Marmot 앨범으로 전달할 수 있습니다.

### Nostria 4.1.67은 암호화 커뮤니티 관리를 확장

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67)은 Nostr를 위한 웹 및 데스크톱 소셜 클라이언트입니다. 실험적 [NIP-29](/ko/topics/nip-29/)(릴레이 관리 그룹) 릴레이 관리 그룹과 4.1.53에서 도입된 Concord 암호화 커뮤니티를 기반으로, 커뮤니티 해산, 아이콘 및 배너 관리, 압축 미리보기가 있는 암호화 사진 업로드, 전체 리액션 선택기, 사용자가 노트나 기사를 읽는 동안 커뮤니티를 열어 두는 듀얼-pane 레이아웃을 추가합니다. 릴리스는 또한 스레드 메시징과 공개, 그룹, 비공개 채팅을 위한 통합 허브를 추가합니다.

### Amber 6.4.0은 모든 그룹화된 서명 결정을 명시적으로 만듦

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0)은 Nostr 개인 키를 서명을 요청하는 애플리케이션과 분리해 두는 Android 서명자입니다. 재설계된 다중 요청 화면은 각 요청과 각 그룹에 Approve 및 Deny 컨트롤을 제공하여 이전 선택 및 확인 흐름을 대체합니다. Amber의 릴레이 매개 bunker 인터페이스를 통해 전송된 거부된 요청은 이제 적절한 오류 응답을 받으므로, 요청 클라이언트는 정체된 서명자와의 거부를 구별할 수 있습니다.

[Amber의 태그된 소스](https://github.com/greenart7c3/Amber/tree/v6.4.0)는 또한 출시된 모든 로케일에서 113개 이상의 이벤트 kind에 대해 현지화된 사람이 읽을 수 있는 레이블을 추가합니다. 추가 항목에는 Concord 그룹 이벤트, [NIP-51](/ko/topics/nip-51/)(Git 리포지토리 북마크) Git 리포지토리 북마크, [NIP-53](/ko/topics/nip-53/)(룸 프레즌스) 룸 프레즌스 이벤트가 포함되어, 사용자가 서명을 승인하기 전에 낯선 데이터에 대한 더 많은 맥락을 제공합니다. concurrent-map 가드는 또한 `NegativeArraySizeException`을 발생시킬 수 있는 릴레이 구독 충돌을 수정합니다.

### Safebox Acorn은 휴대용 복구 컴포넌트를 웹 앱에서 분리

[Safebox Acorn](https://github.com/trbouma/safebox-acorn)은 Nostr 기반 상태로 사용자 제어 키, 자금, 레코드를 보호하는 독립 Python 컴포넌트 및 명령줄 인터페이스입니다. Acorn을 더 넓은 Safebox 웹 애플리케이션에서 분리하면 다른 Python 프로젝트가 웹 인터페이스를 맡지 않고도 런타임과 키, Nostr 프로필, 릴레이, 레코드, Cashu, Lightning, 암호화 helper를 설치하여 사용할 수 있습니다. 현재 record-protection 원시 기능은 새로운 256비트 키를 생성하고, 별도로 제공된 엔트로피에서 하나를 도출하며, 정확한 키를 checksummed 24단어 복구 구문으로 인코딩할 수 있습니다.

프로젝트의 [복구 및 연속성 가이드](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/)는 Acorn을 가정 또는 커뮤니티 Safebox 내부의 교체 가능한 프로토콜 컴포넌트로 프레이밍합니다. 설계는 로컬 릴레이와 독립 복제본을 통해 암호화된 상태를 사용 가능하게 유지하여 복구가 하나의 appliance, 애플리케이션, 릴레이, mint, 또는 서비스 제공자에 의존하지 않도록 합니다. 문서는 현재 경계에 대해 신중합니다. protected-record 암호화는 아직 설계 중이므로, 해당 프로필이 구현되고 검토될 때까지 애플리케이션은 레코드가 새 record-protection 키에 의존하지 않도록 해야 합니다.


## 태그 릴리스

### Mostro Core 0.14.2는 암호화 채팅 봉투를 변경

[Mostro Core](https://github.com/MostroP2P/mostro-core)는 Mostro 교환 데몬과 클라이언트가 사용하는 공유 타입 및 피어 투 피어 함수의 Rust 라이브러리입니다. [버전 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2)는 gift-wrap 채팅 메시지를 피어 공유 비밀에서 도출된 별도 대화 암호화 및 서명 키를 사용하는 kind 14 봉투로 대체합니다. 새 리더는 작성자, 서명, 수신자, 타임스탬프, 콘텐츠 크기를 검증하며, 레거시 gift-wrap helper는 마이그레이션 중 클라이언트가 두 형식을 모두 읽을 수 있도록 유지됩니다.

### Mostro 0.18.1은 Cashu escrow 경로를 시작하고 데몬을 강화

[Mostro](https://github.com/MostroP2P/mostro)는 Nostr를 통해 주문을 조정하는 피어 투 피어 Lightning 교환 데몬입니다. [버전 0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1)은 Cashu escrow 백엔드를 위한 기반을 마련하며, 구성, 데이터베이스 helper, mint 통합, 시작 배선, 첫 lock 액션을 포함합니다. 또한 Nostr를 통해 신뢰할 수 있는 노드가 발표한 가격을 사용할 수 있고, 교체 가능한 info 이벤트에서 첫 연락에 대한 proof-of-work 요구 사항을 광고합니다. 릴리스는 NIP-44 denial-of-service 수정을 위해 Nostr 의존성을 업데이트하고, 복원 세션 로그에서 개인 키를 제거하며, 승인되지 않은 cooperative-cancel 메시지를 거부하고, LNURL 가져오기를 server-side request forgery 및 hang에 대해 강화하고, payout 인보이스를 검증하며, 재시작 후 hold-invoice 구독을 복원합니다.

### LaWallet NWC 2.3.0은 Nostr 알림과 zap 영수증을 추가

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc)는 [Nostr Wallet Connect](/ko/topics/nip-47/)를 통해 지갑을 연결하는 오픈소스 Lightning Address 플랫폼입니다. [버전 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0)은 각 지갑이 수신 및 전달 알림을 구성 가능한 Nostr 이벤트로 보낼 수 있게 하며, 수신자 `p` 태그, 선택된 릴레이, 템플릿 콘텐츠, 선택적 [NIP-44](/ko/topics/nip-44/) 암호화를 포함합니다. 재시도는 동일한 서명된 이벤트 ID를 재사용합니다. 또한 zap 요청을 수락하고 정산 후 서명된 [NIP-57](/ko/topics/nip-57/) kind 9735 영수증을 게시하며, 새 주소 capability 보기는 해결된 주소가 NIP-05, NIP-57, 관련 Lightning Address 프로토콜을 지원하는지 표시합니다.

### nostr-double-ratchet TypeScript 0.0.166은 공개 초대를 세션 키에 바인딩

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet)은 Nostr 릴레이를 통한 end-to-end 암호화 다이렉트 및 그룹 메시징을 위한 TypeScript 및 Rust 원시 기능을 제공합니다. [TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166)은 초대 응답이 세션 키의 소유권을 증명하도록 요구하여, 재사용 가능한 공개 초대가 하나의 Nostr 신원을 다른 당사자의 세션에 바인딩하는 것을 방지합니다. 릴리스는 또한 잘못된 형식의 rumor 필드를 거부하고 페이로드 검증을 강화합니다. 기존 세션은 계속 작동하지만, 업데이트된 초대자는 오래된 초대 대상의 증명 없는 응답을 거부합니다.

### cln-nip47 0.2.0은 NWC 요청을 확장하고 격리

[cln-nip47](https://github.com/daywalker90/cln-nip47)은 [Nostr Wallet Connect](/ko/topics/nip-47/)를 통해 지갑에 노드를 노출하는 Core Lightning 플러그인입니다. [버전 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0)은 hold 인보이스를 생성, 취소, 정산하는 NWC 메서드와 `hold_invoice_accepted` 알림을 추가하고, 연결된 노드가 실제로 지원하는 메서드 집합을 광고합니다. 트랜잭션 목록 응답은 이제 500개 항목과 약 128 kB에서 중단되며, 요청 이벤트는 이벤트 ID로 중복 제거되고, 한 클라이언트의 실패한 알림이 더 이상 다른 클라이언트에 대한 전달을 막지 않습니다. 릴리스는 또한 NWC 사양에 더 이상 포함되지 않는 두 multi-payment 메서드를 제거합니다.

### ClipRelay 0.1.3은 유휴 기간 후 릴레이 및 서명자 연결을 복원

[ClipRelay](https://github.com/tajava2006/cliprelay)는 [NIP-44](/ko/topics/nip-44/)로 동일한 신원에 콘텐츠를 암호화하여 Nostr 릴레이를 통해 사용자 클립보드를 기기 간에 동기화합니다. 해당 [데스크톱](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) 및 [Android](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3) 0.1.3 릴리스는 입력한 텍스트를 다른 기기의 클립보드로 직접 보낼 수 있는 텍스트 상자를 추가합니다. 또한 유휴 기간 후 실제 릴레이 왕복으로 활성 상태를 테스트하며, 재구독에서 소켓 교체 및 재구축된 연결 풀로 에스컬레이션하고, 정체된 [NIP-46](/ko/topics/nip-46/)(릴레이 매개 원격 서명) 서명자 호출은 이제 타임아웃되고 자동으로 재구축됩니다.

### NoorNote 1.3.2는 기사 발견을 소셜 그래프로 이동

[NoorNote](https://github.com/77elements/noornote)는 웹, 데스크톱, Android에서 소셜 게시물, 암호화 메시지, 장문 기사, 기타 이벤트 kind를 다루는 Nostr 클라이언트입니다. [버전 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2)는 평면적인 전역 기사 피드를 1차, 2차, 3차 연락처에서 가져온 발견으로 대체하여, 독자에게 팔로우 그래프에 뿌리를 둔 기사 타임라인을 제공합니다. 또한 알 수 없는 발신자의 재생된 다이렉트 메시지 버스트를 릴레이 기록이 도착할 때 토스트 스택을 만드는 대신 하나의 롤링 알림으로 축소합니다.

### Bray 2.4.0은 컴팩트 원격 서명 방언을 추가

[Bray](https://github.com/forgesworn/bray)는 소프트웨어 에이전트와 사람에게 릴레이 접근, 신원, 게시, 원격 서명 도구를 제공하는 Nostr MCP 서버입니다. [버전 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0)은 [NIP-46](/ko/topics/nip-46/)에서 사용하는 문자열 형식뿐 아니라 이벤트가 객체인 서명 요청도 수락하고, 이벤트 ID, 서명, 공개 키, 타임스탬프만 반환하는 `sign_event_compact`를 추가합니다. 더 작은 요청 및 응답 형식은 제약된 하드웨어 서명자의 메모리 사용량을 줄이며, 표준 `sign_event` 흐름은 변경되지 않고 두 방언 모두 수신된 이벤트 ID에 대한 서명을 생성합니다.


## 새로 발견됨

### Pact는 상호 동의 에이전트 bond를 Nostr에 가져옴

[Pact](https://github.com/bobodread876/pact)는 이번 주 새로 발견되었으며, MATE.md와 초안 NIP-BD 전송을 기반으로 한 소프트웨어 에이전트를 위한 초기 단계 관계 레이어입니다. 서명되고 상호 동의된 bond는 에이전트 자체 키가 보유하며 Nostr를 통해 게시할 수 있고, 비공개 bond는 [NIP-59](/ko/topics/nip-59/) gift wrapping을 사용합니다. 모노레포에는 MCP 서버, TypeScript SDK, 명령줄 클라이언트, 자체 호스팅 가능한 데몬, 웹 인터페이스가 포함됩니다. 최신 리포지토리 활동은 이번 호의 주간 창보다 이전이므로, 이는 새 릴리스 주장이 아닌 발견 메모입니다.


## 개발 중

### nostrord는 그룹 음소거를 기기 간에 동기화

[nostrord](https://github.com/nostrord/nostrord)는 릴레이 관리 커뮤니티를 위한 크로스 플랫폼 클라이언트입니다. [PR #250](https://github.com/nostrord/nostrord/pull/250)은 각 계정의 그룹별 음소거 선택을 자체 암호화된 [NIP-78](/ko/topics/nip-78/)(애플리케이션별 데이터) kind `30078` 이벤트에 저장하여, 한 기기에서 만든 설정이 릴레이에 그룹 목록을 공개하지 않고 다른 기기로 사용자를 따라갈 수 있게 합니다. 교체 가능한 레코드는 최신 이벤트 순서를 사용하고, 실시간 변경을 수신하며, 서명 또는 게시가 실패할 때 인터페이스를 롤백하여 로컬 상태가 동기화되지 않은 채로 남지 않습니다. 음소거된 그룹은 다음 방문을 위한 읽지 않은 위치를 유지하면서 가시적인 읽지 않은 합계에 기여하지 않습니다.

### Amethyst는 Concord 초대 수명 주기를 완성

[Amethyst](https://github.com/vitorpamplona/amethyst)는 Concord 프로토콜을 구현하는 암호화 커뮤니티 지원 Android Nostr 클라이언트입니다. [PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888)은 커뮤니티 refounding 후에도 초대 링크가 같은 어드레서블 좌표에서 bundle을 재발행하여 살아남게 하며, ban 검사는 제거된 멤버가 그 복구 경로를 사용하는 것을 방지합니다. 또한 앱과 `amy` 명령줄 클라이언트 모두에서 암호화된 CORD-05 초대 목록을 구현하고, 링크별 폐기 tombstone을 추가하며, 링크를 폐기할 수 있는 유일하게 저장된 서명 키를 삭제하기 전에 릴레이 확인을 요구합니다. 같은 작업은 `amy`에 이후 커뮤니티 epoch를 따르는 데 필요한 control-key 전달, refounding, rekeying, stranded-member 복구 경로를 제공합니다.

### Buzz는 각 커뮤니티의 외관을 데스크톱과 모바일에 걸쳐 전달

[Buzz](https://github.com/block/buzz)는 데스크톱 및 모바일 클라이언트를 갖춘 Nostr 기반 커뮤니티 워크스페이스입니다. 병합된 데스크톱 [PR #3653](https://github.com/block/buzz/pull/3653)과 모바일 [PR #3767](https://github.com/block/buzz/pull/3767)은 각 커뮤니티의 테마, accent, system-mode 선택을 해당 커뮤니티 릴레이의 암호화된 NIP-78 레코드로 저장합니다. 두 클라이언트는 동일한 버전 지정 페이로드를 공유하고 신원 범위 로컬 캐시를 유지하므로, 커뮤니티나 계정을 변경할 때 릴레이를 사용할 수 없는 동안 잘못된 외관이 적용되지 않습니다. 교체 순서, 보호된 쓰기, 연결 종료 후 재구독은 두 클라이언트가 재연결 후 다시 수렴할 수 있게 합니다.

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10)은 호 마감 전에 성능 및 안정성 패스로 이어졌습니다. 0.5.9 이후 도입된 회귀를 제거하고, 채널 로딩을 가속하며, 초기 타임라인 보존을 제한하고, 읽음 상태 지속을 병합하고, 새로운 채널 타임라인을 보존하며, 프로젝트 이벤트에 대한 리액션에서 릴레이 ingest worker가 충돌하는 것을 중단합니다. 또한 스레드 메시지를 채널로 보내는 기능을 추가하고 데스크톱 검색을 의도한 범위로 좁힙니다.


## NIP 업데이트 및 프로토콜 사양 작업

### NIPs

[NIPs PR #2435](https://github.com/nostr-protocol/nips/pull/2435)는 Nostr 이벤트를 통해 Git 리포지토리 협업을 표준화하는 [NIP-34](/ko/topics/nip-34/)(Git over Nostr)에 대한 공개 수정입니다. pull-request 이벤트에 선택적 `b` 태그를 추가하여 작성자가 리포지토리 기본값이 아닌 대상 브랜치를 지정할 수 있게 합니다. 제안은 ngit과 GitWorkshop에 이미 구현된 지원과 일치하지만, 아직 사양에 들어가지 않았습니다.

[NIPs PR #2434](https://github.com/nostr-protocol/nips/pull/2434)는 post-quantum 신원 키에 대한 공개 제안입니다. [NIP-06](/ko/topics/nip-06/)(니모닉 키 파생) 니모닉 키 파생 시드에서 기존 secp256k1 키 옆에 post-quantum 암호화 및 서명 키를 도출한 다음, kind `10203` 증명으로 공개 키를 Nostr 신원에 바인딩합니다. 초안은 secp256k1이 나중에 깨질 경우 더 이른 메시지의 기밀성을 보호한다는 주장으로 범위를 제한합니다. 오늘의 이벤트 서명을 대체하지는 않습니다.

[NIPs PR #2431](https://github.com/nostr-protocol/nips/pull/2431)은 브라우저 서명자를 위한 공개 [NIP-07](/ko/topics/nip-07/)(브라우저 확장 서명) 수정입니다. 클라이언트가 서명 또는 암호화 요청에 기대하는 공개 키를 첨부하여, 서명자가 해당 계정을 사용하거나 호출을 거부하도록 요구할 수 있습니다. 이는 사용자가 서명자에서 계정을 전환한 후 페이지가 다른 신원으로 조용히 계속되는 것을 방지합니다.

[NIPs PR #1813](https://github.com/nostr-protocol/nips/pull/1813)은 창 동안 실질적인 작업 후에도 공개 double-ratchet 제안으로 남아 있습니다. 메시지와 함께 키가 진행되는 forward-secret 암호화 대화를 지정하며, nostr-double-ratchet 라이브러리와 Iris에서 이미 구현을 사용할 수 있습니다. 아직 병합된 NIP가 아닌 초안입니다.

[NIPs PR #2433](https://github.com/nostr-protocol/nips/pull/2433)은 창 동안 열렸다가 병합 없이 닫혔습니다. [NIP-42](/ko/topics/nip-42/)(릴레이 인증) 릴레이 오류를 명확히 하여 `auth-required`는 다른 인증이 결과를 변경할 수 있음을, `restricted`는 변경할 수 없음을 의미하도록 제안했습니다. 이 구분은 한 키로 인증되었지만 다른 키에 대한 권한이 여전히 없는 연결을 다룹니다. 닫힌 상태는 문구가 사양에 들어가지 않았음을 의미합니다.

이전에 아직 제안된 상태로 다룬 [NIPs PR #2378](https://github.com/nostr-protocol/nips/pull/2378)은 이제 병합 없이 닫혔습니다. 제안된 agent passport, discovery, task, marketplace, invoice, connection 이벤트는 따라서 NIP 집합 밖에 남아 있습니다.

[NIPs 커밋 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab)는 [NIP-29](/ko/topics/nip-29/)에 대한 문서 전용 수정을 병합했습니다. 그룹 메타데이터 예시에 `previous` 태그를 추가하여, 교체 이벤트가 대체하는 이벤트를 식별하는 방법을 보여줍니다. 이는 예시를 명확히 할 뿐 새 프로토콜 기능을 도입하지 않습니다.

### Concord and CORDs

[CORD PR #18](https://github.com/concord-protocol/concord/pull/18)은 암호화 Community List를 kind `33302` 이벤트에 샤딩하고, 50 멤버십 제한을 제거하며, 릴레이 제한 내에 머물도록 은퇴한 항목을 가지치기합니다. 다른 두 공개 제안은 [비공개 멘션 locator](https://github.com/concord-protocol/concord/pull/16)와 메시지를 폐기하지 않고 채팅을 일시 중단하는 [pause signal](https://github.com/concord-protocol/concord/pull/17)을 추가합니다.

[CORD-02 PR #15](https://github.com/concord-protocol/concord/pull/15)는 8월 6일에 병합되어 커뮤니티 control plane에 대한 쓰기를 제한합니다. 소유자와 staff는 새 `control_root` 서명 비밀을 보유하고, 모든 멤버는 중재 상태를 검증하고 복호화하는 데 필요한 도출된 공개 키와 read key를 유지합니다. write key는 스팸 장벽이며, 권한을 확립하는 내부 actor 서명과 roster 검사를 대체하지 않습니다.

이전에 공개 초안으로 다룬 [CORD PR #12](https://github.com/concord-protocol/concord/pull/12)는 이제 병합 없이 닫혔습니다. control-plane 부분은 위의 더 좁은 병합된 CORD-02 수정으로 대체되었고, restricted-write 채널과 다른 초안 자료는 사양에 들어가지 않았습니다.

## NIP 심층 분석

### 이벤트 삭제 요청(NIP-09)

[기본 사양](https://github.com/nostr-protocol/nips/blob/master/09.md)에서 정의된 [NIP-09](/ko/topics/nip-09/)(이벤트 삭제 요청)은 이벤트 작성자에게 해당 작성자의 이벤트 하나 이상의 제공을 중단하도록 릴레이와 클라이언트에 요청하는 서명된 방법을 제공합니다. 모든 사본을 지우지는 않습니다. 원래 이벤트를 배포한 것과 같은 릴레이 네트워크를 통해 작성자의 의도를 전달합니다.

요청은 일반적인 서명된 kind `5` 이벤트입니다. 태그에는 특정 이벤트 ID에 대한 하나 이상의 `e` 참조 또는 어드레서블 이벤트 좌표에 대한 `a` 참조가 포함되며, [NIP-09 태그 규칙](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request)에 따르면 참조된 각 이벤트 kind에 대해 `k` 태그를 포함해야 합니다. 선택적 `content`는 이유를 설명할 수 있습니다. `a` 참조의 경우, 릴레이는 해당 좌표에서 타임스탬프가 요청의 `created_at`보다 늦지 않은 모든 버전을 제거해야 하며, 이는 오래된 삭제 요청이 이후 교체를 억제하는 것을 방지합니다.

[작성자 권한이 보안 경계](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior)입니다. 릴레이는 참조된 이벤트의 `pubkey`가 삭제 요청의 `pubkey`와 일치할 때만 해당 이벤트 게시를 중단해야 하며, 클라이언트는 이벤트를 숨기기 전에 그 검사를 수행해야 합니다. 릴레이는 참조된 이벤트를 보유하지 않을 수 있어 요청을 수락할 때 관계를 검증하지 못할 수 있으므로, 클라이언트는 릴레이 수락을 삭제가 승인되었다는 증거로 취급할 수 없습니다. 사양은 또한 다른 클라이언트가 이미 원본 이벤트를 보유하고 나중에 요청을 만날 수 있으므로 릴레이가 kind `5` 요청을 보존하도록 요청합니다.

다음은 [서명된 kind `5` 이벤트](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943)입니다.

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

삭제는 서명된 객체의 취소가 아닌 협력적 정책으로 남아 있습니다. 릴레이, 캐시, 스크린샷, 또는 오프라인 클라이언트는 원본 바이트를 보존할 수 있으며, kind `5` 요청 자체를 삭제해도 취소되지 않습니다. 클라이언트는 대상을 숨기거나, 소유권을 포기한 것으로 표시하거나, 요청 이유를 표시할 수 있지만, 보편적 삭제가 보장될 수 없음을 사용자에게 알려야 합니다. 이는 이벤트가 게시될 때 선택한 시간 이후 릴레이가 이벤트 저장을 중단하도록 요청하는 `expiration` 태그가 있는 [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)과 다릅니다. NIP-09는 이후 작성자 결정을 다루며 이미 배포된 이벤트를 가리킬 수 있습니다.

현재 구현은 서로 다른 레이어에서 그 정책을 적용합니다. [Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623)은 삭제된 비디오를 클라이언트 이벤트 저장소에서 제거하고, [strfry PR #251](https://github.com/hoytech/strfry/pull/251)은 유효한 삭제 요청을 gift-wrap 수신자까지 확장하며, [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md)는 클라이언트에서 NIP-09 지원을 선언합니다. [nostrord의 그룹 클라이언트](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt)는 또 다른 현재 구현 경로를 제공합니다.

### 신고(NIP-56)

[기본 사양](https://github.com/nostr-protocol/nips/blob/master/56.md)에서 정의된 [NIP-56](/ko/topics/nip-56/)(신고 이벤트)은 계정, 이벤트, 또는 참조된 blob에 대한 서명된 신고를 표준화합니다. 신고 신호를 중재 결정과 분리하여, 각 클라이언트나 릴레이가 신뢰하는 신고자와 해당 정책에 맞는 응답을 선택할 수 있게 합니다.

신고는 kind `1984`를 사용하며 `p` 태그로 신고된 계정을 식별해야 합니다. 노트를 신고하려면 이벤트 ID에 대한 `e` 태그도 필요합니다. 태그의 세 번째 값은 지정된 카테고리 중 하나를 담습니다. `nudity`, `malware`, `profanity`, `illegal`, `spam`, `impersonation`, `other`. blob에 대한 신고는 해시를 `x` 태그에, blob을 참조한 이벤트를 `e` 태그에, 위치를 `server` 태그에 사용할 수 있습니다. 고정 카테고리 목록이 충분히 정확하지 않을 때 [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md)의 선택적 `L` 및 `l` 태그로 namespaced 레이블을 추가할 수 있습니다.

[이벤트는 하나의 키가 주장을 했다는 것만 증명](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting)합니다. 신고된 콘텐츠는 유효한 kind `1984`가 존재한다고 해서 거짓, 불법, 또는 제거 가능해지지 않으며, 개방형 릴레이는 익명 신고를 투표로 안전하게 집계할 수 없습니다. 사양은 신고를 조작하기 쉬우므로 자동 릴레이 중재에 반대하면서, 이미 신뢰하는 중재자의 신고에 대해 릴레이 관리자가 조치할 수 있도록 허용합니다. 클라이언트는 대신 사용자의 소셜 그래프를 통해 신고에 가중치를 줄 수 있습니다. 예를 들어, 신뢰하는 여러 연락처가 같은 계정을 플래그한 후 콘텐츠를 흐리게 처리합니다.

다음은 [서명된 kind `1984` 이벤트](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2)입니다.

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56과 NIP-09는 서로 다른 문제를 해결](https://github.com/nostr-protocol/nips/tree/master)합니다. kind `1984` 신고는 다른 사람의 계정이나 이벤트를 대상으로 할 수 있지만, 삭제 권한을 부여하지 않습니다. kind `5` 요청은 원본 작성자의 의도를 표현하며 해당 작성자 자신의 이벤트에 대해서만 유효합니다. 둘 다 제거를 보장하지 않습니다. NIP-56은 의도적으로 조치를 로컬 중재 정책에 위임하고, NIP-09는 릴레이와 클라이언트가 인증된 요청을 존중하는 데 의존합니다.

구현은 서로 다른 제품에서 그 선택을 노출합니다. [Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591)은 숏폼 비디오 클라이언트에서 신고 전달을 수정하고, [Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250)은 marketplace 참가자를 위한 제한된 맥락으로 신고를 읽으며, [nostrord의 NIP-56 모듈](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt)은 신고 이벤트를 게시하고 처리합니다. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support)도 현재 NIP-56 지원을 나열합니다.


---

[Nostr Compass 프로젝트](https://github.com/andotherstuff/nostr-compass)를 통해 프로젝트나 뉴스를 공유하려면 NIP-17 DM을 보내주세요.
