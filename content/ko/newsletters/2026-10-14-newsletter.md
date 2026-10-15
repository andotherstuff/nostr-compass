---
title: "Nostr Compass #44"
date: 2026-10-14
publishDate: 2026-10-14
draft: false
type: newsletters
description: "데스크톱 Amethyst, Amber 보안 수정, 비공개 첨부 파일, 인증된 소프트웨어 설치, 콘텐츠 경고 및 상태."
translationOf: /en/newsletters/2026-10-14-newsletter.md
translationDate: 2026-10-15
---

**[Amethyst](#amethyst)**는 Android 인터페이스를 데스크톱으로 가져오고 네이티브 Wayland 지원을 추가합니다. **[Amber](#amber)**는 권한 철회, 복사한 비밀정보 지우기, 키 손실을 일으킬 수 있었던 설정 변경 문제를 수정합니다. **[Keep](#keep-android)**은 자동 서명 권한을 강화하고, **[MDK](#mdk)**는 비공개 첨부 파일 스트리밍과 오래된 메시지부터 따라잡는 기능을 제공합니다. **[Zap Cooking](#zap-cooking)**은 팔로우 목록 편집과 인증된 멤버십을 위한 보호 조치를 병합합니다. 아래에서 [릴리스 세부 사항](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0)과 함께 프로토콜 변경 사항 및 공개 상태의 작동 방식을 살펴봅니다.

## 주요 소식

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0)은 Android 소셜 클라이언트의 공유 인터페이스를 데스크톱으로 가져오며, 맞춤 피드, 넓은 창용 덱, 선택적으로 활성화하는 잠금 기능, 암호화된 미디어, [Blossom 업로드](/ko/topics/blossom/)를 제공합니다. [NIP-85 신뢰할 수 있는 확인 정보](/ko/topics/nip-85/)의 제공자 점수는 요청, 알림, 배지에 활용할 수 있도록 로컬에서 인덱싱되며, 사용자가 제공자와 임곗값을 선택합니다.

오늘 나온 [v1.19.0 릴리스](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0)는 네이티브 Wayland 지원과 별도로 설치한 FFmpeg 및 ffprobe를 사용하는 데스크톱 동영상 압축을 추가합니다. 키 저장 관련 수정은 반복되는 키체인 프롬프트와 Linux 키링 오류를 해결합니다. 캘린더 모음과 RSVP 렌더링이 지원되고, Android 로그인 인터페이스에는 [NIP-46 원격 서명](/ko/topics/nip-46/)이 추가됩니다. 암호화된 봉투를 병렬로 개봉한 뒤 순차적으로 인덱싱하며, relay 재연결과 피드 작성자의 relay 목록 처리도 수정됩니다. [relay 클라이언트는 속도 제한에 따른 백오프를 준수한 뒤](https://github.com/vitorpamplona/amethyst/pull/4422) 구독이나 게시를 재개합니다.

[신뢰 제공자 relay 변경](https://github.com/vitorpamplona/amethyst/pull/4437)은 사용자의 kind 10040 목록에 있는 제공자 relay를 사용자 자신의 신뢰할 수 있는 relay로 취급합니다. 이러한 연결은 기본적으로 직접 경로를 사용하며, Tor를 사용하려면 신뢰할 수 있는 relay 설정을 활성화해야 합니다. 메인 클라이언트의 [NIP-42 relay 인증](/ko/topics/nip-42/)은 이러한 relay에 사용자의 공개 키를 노출할 수 있습니다.

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9)는 Android Nostr 서명기의 보안 결함 세 가지를 수정합니다. [철회된 권한](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw)이 캐시 경쟁 상태로 인해 남아 있는 일이 더 이상 없으며, 명시적 거부는 완전 신뢰 상태보다 우선합니다. [복사한 비밀정보](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p)는 프로세스가 종료된 경우에도 시스템이 예약한 작업에 의해 60초 후 클립보드에서 지워집니다. 그동안 내용은 계속 읽을 수 있으며, 나중에 복사한 텍스트도 함께 지워질 수 있습니다. [“잠금 해제된 기기 필요”](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5) 설정을 변경할 때는 비밀정보 마이그레이션이 완료될 때까지 기존 래핑 키를 보존하지만, 이전에 분실한 키는 여전히 복구되지 않습니다. 이 릴리스는 여러 요청이 포함된 nostrconnect 승인을 수정하고 URI에 지정된 relay로 응답하도록 바로잡습니다. 6.6.8 및 이전 버전 사용자는 업데이트해야 합니다.

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0)은 [FROST 임계값 서명기](/ko/topics/frost/)로, 기기 내 분산 키 생성과 중단된 지분 작업의 인증된 복구를 추가합니다. StrongBox를 지원하지 않는 기기도 처리합니다. 임계값 서명에서는 참여 기기들이 서명 비밀값의 지분을 보유하고 협력하여 서명을 생성합니다. 어떤 기기가 참여할 수 있는지는 설정 및 복구 단계에서 결정됩니다.

[버전 1.3.1](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1)은 자동 서명이 기억된 거부, ‘묻기’ 권한, 만료된 승인 또는 권한 읽기 실패를 무시하지 못하도록 합니다. 만료 시 거부는 유지하면서 백그라운드 승인을 제거합니다. [앱별 정책 마이그레이션](https://github.com/privkeyio/keep-android/pull/532)은 더 엄격한 결정을 유지하면서 권한을 코어가 소유한 저장소로 옮깁니다.

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21)은 Nostr를 매개로 하는 거래 애플리케이션에서 사용하는 [네이티브 지갑 브리지를 인증하고](https://github.com/jesuspirate/chama/pull/29), 프로덕션 환경에서 URL 기반 브리지 리디렉션을 비활성화하며, 지급 금액을 검증합니다. 내용물을 읽을 수 없는 지갑은 초기화하지 않습니다.

[버전 6.4.22](https://github.com/jesuspirate/chama/releases/tag/v6.4.22)는 외부인의 event에 대한 재생 처리를 강화하고, 후속 관계를 확인하며, 빈 중재자 풀을 거부하고, 서명된 LOCK 시각을 기준으로 환불 시점을 산출합니다. 합의 변경 사항은 2026년 11월 1일부터 서명된 CREATE event에 적용되며, 클라이언트 보호 조치는 즉시 적용됩니다. 릴리스 노트에는 거래 게시물에서 선택한 페더레이션과 더스트 지급에 관한 주의 사항이 그대로 남아 있습니다. 이후의 [서명기 및 복구 변경](https://github.com/jesuspirate/chama/releases/tag/v6.4.23)은 보호된 시드 읽기 기능과 복구 가능한 지연 잠금을 추가하며, [v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24)는 대규모 거래 목록 처리를 개선합니다.

### Zap Cooking

레시피 및 소셜 클라이언트인 [Zap Cooking은 팔로우 목록 편집 보호 조치를 병합하여](https://github.com/zapcooking/frontend/pull/795) 불완전하거나 오래되었거나 예상치 못하게 축소된 읽기 결과에 대응합니다. 팔로우 작업은 기존 tag와 내용을 보존하는 하나의 보호된 업데이트 경로를 공유합니다. 게시 전에 서명자의 신원을 확인합니다. [멤버십 인가 수정](https://github.com/zapcooking/frontend/pull/802)은 인증된 요청에 서명한 공개 키를 사용합니다. [관리용 비밀정보를 노출하던 경로는 제거되었지만](https://github.com/zapcooking/frontend/pull/801), 배포 시에는 여전히 비밀정보 교체가 필요하며, 변경 사항의 병합만으로 교체가 이루어졌다고 볼 수는 없습니다. 이후의 [스레드 및 북마크 수정](https://github.com/zapcooking/frontend/pull/833)은 실제 답글 루트를 보존하고 실패한 북마크 쓰기를 복구합니다. [레시피 tag 필드](https://github.com/zapcooking/frontend/pull/836)는 더 이상 키 입력을 프로필 또는 NIP-50 검색 서비스로 전송하거나, 저장되지 않은 변경 사항이 있는 상태에서 편집기를 벗어나게 하지 않습니다.

## 태그가 지정된 릴리스

### MDK

[MDK v0.13.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.13.0)은 [Marmot 암호화 그룹](/ko/topics/marmot/)의 런타임으로, 진행 상황 표시와 취소 기능을 갖춘, 스트리밍 및 재개 가능한 비공개 첨부 파일을 추가합니다. 또한 메시지, 그룹, relay 식별자를 제외한 비공개 [NIP-56 신고](/ko/topics/nip-56/)를 [NIP-59 선물 포장](/ko/topics/nip-59/)을 통해 배포 운영자에게 보냅니다. 따라잡기는 최대 256개의 event로 이루어진 배치를 오래된 것부터 처리하며, relay의 CLOSED 거부를 유지합니다. SOCKS5 라우팅은 직접 연결로의 대체 없이 relay, 미디어, 탐색 서비스를 포괄합니다.

[릴리스 가이드](https://github.com/marmot-protocol/mdk/blob/v0.13.0/docs/release/0.13.0.md)는 바인딩, 헤더, 네이티브 아티팩트를 함께 변경하도록 요구합니다. 데이터베이스 스키마는 101에서 107로 올라가며 다운그레이드 경로는 없습니다. 호스트의 비밀정보 저장소는 마이그레이션이 필요합니다. MarmotKit과 C 아티팩트는 안정 버전이지만, WN Agent는 여전히 사전 릴리스이며 워크스페이스 크레이트는 crates.io에 게시되지 않았습니다. [MLS 에포크](/ko/topics/mls/) 다섯 개를 초과하여 늦게 도착하는 기록은 기록 불완전 안내 없이도 여전히 복호화할 수 없을 수 있으며, 인증된 에이전트 클라이언트는 전체 API에 대한 접근 권한을 유지합니다.

이 릴리스는 [첫 번째 확인 응답 이후에도 대기 상태로 남은 프로필, 팔로우 목록, relay 목록 저장을 재시도](https://github.com/marmot-protocol/mdk/pull/2228)하기도 합니다. 이러한 백그라운드 재시도는 재시작 후에는 유지되지 않습니다. [초대 조회는 탐색 relay에서 KeyPackage의 삭제 및 만료 여부를 확인](https://github.com/marmot-protocol/mdk/pull/2211)하지만, 그 응답으로 수신자가 여전히 KeyPackage의 비공개 자료를 보유하고 있음을 증명할 수는 없습니다. [활동 반응 대상](https://github.com/marmot-protocol/mdk/pull/2187)은 이제 인증된 행위자와 개별 그룹 커밋에서 일관되게 도출되며, 행위자 정보가 없는 과거 기록은 여전히 불완전합니다.

이후 master 브랜치의 작업은 [누수된 relay 구독을 닫고 활성화 재생을 페이지로 나누어 500 event로 제한한다](https://github.com/marmot-protocol/mdk/pull/2274). [에포크 간격 복구](https://github.com/marmot-protocol/mdk/pull/2298)는 비교에 실패한 relay에서 최신 event 256개를 가져오지만, 전체 이력이 완전하다고 보증하지는 않는다. [자체 업데이트 커밋은 누락된 모든 그룹 relay에 재시도한다](https://github.com/marmot-protocol/mdk/pull/2275). 새로운 주의 안내 검사는 [오래된 것으로 확인된 에포크](https://github.com/marmot-protocol/mdk/pull/2273)와 [아직 relay에 전달해야 하는 커밋](https://github.com/marmot-protocol/mdk/pull/2288)을 다룬다. 사용자가 위험을 인지하고 진행할 수 있으므로, 이 검사들이 그룹의 분기 가능성을 없애 주는 것은 아니다.

[저장 공간 부족으로 차단된 첨부 파일 다운로드](https://github.com/marmot-protocol/mdk/pull/2249)는 여유 공간이 부족할 때도 재개 가능한 진행 상태를 유지한다. 사용자가 명시적으로 시작한 대용량 다운로드는 파일 싱크를 사용하며, 스테이징과 체크포인트를 위해 본문 크기의 약 5~6배에 해당하는 여유 공간이 필요하다. [검증된 공개 event 미리보기](https://github.com/marmot-protocol/mdk/pull/2304)에는 크기가 제한된 암호화 계정 캐시가 추가되며, [더 이상 유효하지 않은 항목만 포함된 KeyPackage 결과](https://github.com/marmot-protocol/mdk/pull/2305)는 불완전한 relay 조회와 구분할 수 있게 된다. 이는 이후에 이루어진 소스 변경으로, 호스트 측에서도 그에 맞게 도입해야 한다. 가져오기가 완료된 event ID 기반 미리보기는 이후의 삭제 여부를 다시 확인하지 않는다.

에이전트 브리지 역시 과도하게 큰 응답이 메모리를 고갈시키지 않도록 [백엔드 출력에 한도를 적용](https://github.com/marmot-protocol/mdk/pull/2103)하고, [커넥터의 실제 삭제 응답을 받아들인다](https://github.com/marmot-protocol/mdk/pull/2301). 출력 한도로 턴이 중단되더라도 이미 전달된 텍스트는 전달된 상태로 남는다.

### Myco

[Myco v0.11.0](https://github.com/Origami74/myco/releases/tag/v0.11.0)은 휴대전화 또는 fips 데스크톱 간 USB 연결을 추가하고, 서명된 아티팩트 및 아이콘 해시를 포함하는 [현재 제안된 NIP-5D 매니페스트 형식](https://github.com/Origami74/myco/pull/135)을 도입한다. 구형 휴대전화도 여전히 페어링할 수 있지만, 이러한 napplet을 열려면 업데이트해야 한다. [다운로드 정책 변경](https://github.com/Origami74/myco/pull/133)은 인터넷, 메시, 사용자 설정 HTTP 목적지를 구분한다. 인터넷 정책에서는 작성자가 제공한 힌트와 리디렉션으로 로컬 네트워크를 탐색할 수 없지만, 사용자가 설정한 목적지에는 제한이 없다. 소프트웨어 클라이언트는 [작성자의 BUD-03 Blossom 서버에서 blob을 검색](https://github.com/Origami74/myco/pull/134)하기도 한다. 이는 아티팩트 검색을 개선하지만 해당 서버에 설치 트래픽을 노출한다. 이러한 HTTP 변경이 WebSocket 연결에도 동등한 보호를 제공하는 것은 아니다. [주변 메시 가용성 검사](https://github.com/Origami74/myco/pull/132)는 blob을 다운로드하거나 공개 Blossom 서버에 접속하지 않고 피어에 blob 보유 여부를 조회한다. 범위가 제한된 이러한 HEAD 요청에는 메시 권한이 필요하다. 보유자 수가 아티팩트 전체의 가용성이 계속 유지되고 있음을 입증하지는 않는다.

이번 릴리스는 로밍 통신사의 시간 초과가 relay 및 아티팩트 조회를 가로막지 않도록 [업스트림 DNS 서버에 병렬로 질의해 먼저 도착한 응답을 사용](https://github.com/Origami74/myco/pull/137)하기도 한다. Outbox 발행은 목록에 있는 모든 쓰기 relay를 대상으로 하며, 느린 목적지로의 전달은 백그라운드에서 이루어진다. 인터넷 메시는 기본적으로 꺼져 있으며, 웹 이미지는 재시작 후 유지되지 않는다.

### Unfiltered

[Unfiltered 1.0.13](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.13)은 Android 사진 클라이언트에 읽기/쓰기 relay 목록과 outbox 라우팅을 추가한다. [릴리스 노트](https://njump.me/nevent1qqsy8287ykdstql8ec2udgr8slj3czzkkdkjjc36xwn4lnjrrhggfwgu8dmj2)는 relay 역할을 설명하며, 목록이 없는 계정은 기본 공개 relay 세 개로 시작한다. Nearby는 정밀도가 낮은 geohash와 인접 셀을 사용한다. 게시물에 위치를 추가하는 기능은 사용자가 선택해야 하며 기본적으로 꺼져 있다. 그래도 해당 tag는 지역을 공개적으로 드러낸다. 확인한 발행 결과가 의미하는 것은 소켓의 대기열에 들어갔다는 것이며, relay의 수락 여부는 아직 확인되지 않은 상태다.

### monostr

[monostr 0.17.0](https://github.com/schmidt1024/monostr/releases/tag/v0.17.0)은 사용자가 개인 감시자를 통해 Monero 팁을 받을 수 있게 하며, [0.18.0](https://github.com/schmidt1024/monostr/releases/tag/v0.18.0)은 새로 설정하는 경우 팁 금액과 알림 발신자 이름을 기본적으로 숨긴다. 사진은 기본적으로 탭해야 로드되며, 선택 기능인 Primal 집계 수치와 클라이언트 tag는 비활성화되어 있다. 호스팅되는 감시자는 여전히 등록된 지갑의 비공개 보기 키를 통해 그 지갑으로 들어오는 모든 결제를 알게 된다. 공개 영수증에는 금액을 숨겨도 수신자, 시간, 참조 게시물이 남는다.

### Grocery

[Grocery 1.0.2](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.2)는 공유 암호화 장보기 목록에 패스키 기반 Nostr 신원과 목록별 Marmot 채팅을 결합한다. 소지자 키를 붙여 넣어 목록에 참여할 수 있으며, 이 키는 읽기와 편집 권한을 부여한다. 패스키 로그인은 브라우저와 제공업체가 WebAuthn의 의사 난수 함수 확장을 지원하는지에 달려 있다. 구성원 tag는 relay에 계속 노출된다. [버전 1.0.3](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.3)은 복호화된 내용을 로컬에 캐시하여 다시 열어도 목록을 유지하며, relay가 목록을 다시 전달할 때까지 키만 남아 있던 경우를 수정한다.

### Roadstr

[Roadstr 1.1.0](https://github.com/roadstrapp/roadstr-app/releases/tag/v1.1.0)은 다른 Roadstr 클라이언트의 kind 1315/1316을 해당 kind에 의도된 유효 기간과 확인 규칙에 따라 읽는다. 소형 코덱은 실험적인 MeshCore 무선 및 relay 브리지를 위해 재구성 가능한 서명된 보고를 보존한다. 호환 발행과 무선 전송은 기본적으로 꺼져 있으며, 공유 전에 동의를 받는다. 무선 보고는 수신 범위 안에 있는 누구에게나 위치, 시간, 서명 공개 키를 노출한다. 테스트에는 시뮬레이션된 무선 장치를 사용했으며, 실제 하드웨어, Android BLE, 공개 relay 발행은 아직 검증되지 않았다.

### OUTKAST

[OUTKAST 1.1.3](https://github.com/Lwb89dev/outkast/releases/tag/v1.1.3)은 Android 클라이언트의 아티클 댓글과 인용 게시물 처리를 개선한다. 아티클 댓글은 아티클을 루트로, 댓글을 부모로 삼는 kind 1111을 사용하며, 일반 노트 답글은 계속 kind 1을 사용한다. 인용 검색은 q tag와 링크를 포함하는 기존 e 멘션을 모두 받아들이며, 새로 발행하는 인용에는 q tag를 추가한다. 발행에 실패하면 낙관적으로 반영한 반응을 되돌린다.

### Bookshelf

[Bookshelf 0.1.28](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.28)은 장과 하위 색인을 모두 발행자가 정한 순서대로 담은 kind-30040 출판물 색인을 [중첩된 구조로 읽는 기능](https://njump.me/nevent1qqs8pukgjrnuzryv0z67lze2y0jsshepdckuss25qggvwn5skxqfa7gslzul0)을 설명한다. 오프라인 사본은 그 계층 구조와 각 등장 위치에 연결된 북마크를 유지한다. 새로 고침은 좌표를 기준으로 최신 개정본을 가져오지만, 결과가 불완전하거나 더 오래되었거나 가져오기에 실패하면 이전 다운로드를 유지한다. 재전파는 원래 서명된 하위 항목들을 보존한다. 확장 범위를 제한하고 부분적인 분기도 읽을 수 있게 하여, 구조가 누락된 상태를 완성된 책처럼 제시하지 않도록 한다.

### Ditto

[Ditto 2.45.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.45.0)은 콘텐츠 피드 전반에서 Global을 Discover로 대체한다. Discover는 사용자가 팔로우하는 사람들이 팔로우하는 사람들을 대상으로 하며, 사용자 본인과 이미 팔로우한 계정을 제외하고 공통 연결을 기준으로 게시물의 순위를 매긴다. 로그아웃한 사용자와 팔로우가 없는 계정에는 대신 엄선된 시작용 네트워크가 표시된다. 이로써 기본 탐색의 범위는 사회적 이웃으로 바뀐다. 스팸 저항성과 해당 계정들의 신뢰성은 여전히 별개의 문제다.

### Postr

[Postr 1.1.2](https://njump.me/nevent1qqsf4uu87v5r7awyfhktjqnuc9m6xzfngpvr7gj37zca05sx7lk03vqy4wq7x)는 선택한 프로필 신원이 임시 저장과 발행을 거치는 동안에도 멘션에 연결된 상태로 유지되게 한다. 작성기는 서명과 전송 중에 계정, 텍스트, 멘션, 첨부 파일을 고정하고, 작업이 끝날 때까지 새로 들어오는 공유 항목을 보관한다. 재시도는 이전부터 대기 중이던 게시물을 포함해 원래 서명된 event를 보존한다. @ 뒤에 이름을 입력하는 것만으로는 충분하지 않다. 사용자가 프로필을 선택해야 하며, 이전 임시 저장본에서 이미 사라진 신원은 다시 선택해야 한다.

### Nostrautica

[Nostrautica Android 0.11.0](https://github.com/jooray/nostrautica/releases/tag/android-v0.11.0)은 커뮤니티를 해당 커뮤니티의 모임과 연결합니다. 연결된 event의 참여 승인을 받으면 별도의 두 번째 승인 없이 커뮤니티 회원 자격도 얻을 수 있습니다. 가입 양식은 이를 안내하고 신청자가 거부할 수 있도록 합니다. 기존 참석자에게는 한 번의 탭으로 수락할 수 있는 초대가 전달됩니다. 각 event는 자체 참가자, 매칭, 채팅을 유지하며, 커뮤니티에는 소속 event 목록이 표시됩니다. 릴리스 노트는 event와 커뮤니티의 운영자가 서로 다른 경우를 지원한다고 설명하지만, 독립적인 상호운용성 또는 암호화 테스트가 이루어졌음을 입증하지는 않습니다.

### Minibits

[Minibits v0.4.4 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.4-beta.1)은 지갑이 백그라운드에 있는 동안 Android의 [Nostr Wallet Connect](/ko/topics/nip-47/) 결제 처리가 중단되고, 처리가 쌓이면서 애플리케이션 응답 없음 오류로 이어질 수 있었던 문제를 수정합니다. 네이티브 릴리스에는 지난 5개월간의 무선 업데이트 변경 사항이 함께 포함됩니다. [버전 0.4.5 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.5-beta.1)은 Android에서 iOS로의 NFC 전송을 수정하며, 향후 무선 업데이트를 받으려면 이 버전이 필요합니다. 이는 릴리스에서 보고한 수정 사항이며, 백그라운드 처리는 여전히 휴대전화의 수명 주기 제한에 영향을 받습니다.

### NoorNote

[NoorNote v1.9.0](https://github.com/77elements/noornote/releases/tag/v1.9.0)에서는 사용자가 글 편집기에서 레시피를 게시하고, 공유된 레시피 묶음을 열고, 팔로우하는 작성자의 레시피를 둘러볼 수 있습니다. 지난주에 다룬 웹사이트 카드와 프로필 그리드가 이번 릴리스에 포함되었으며, relay 속도 제한 처리와 Android의 직접 `nostr:` 링크도 함께 제공됩니다. 웹사이트 링크 제공은 사이트 콘텐츠 검증과는 별개이며, 게이트웨이를 통해 접속하면 클릭으로 발생한 요청이 해당 게이트웨이에 노출됩니다.

### Gittr

[Gittr v1.0.2](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.2)는 [NIP-46 원격 서명](/ko/topics/nip-46/)을 통해 Amber를 사용하는 Nostr Git 개발 플랫폼을 Android용으로 패키징합니다. APK는 기존에 호스팅된 `gittr.space` 애플리케이션을 열기 때문에, 사용자는 여전히 이 서비스가 제공하는 브라우저 코드와 가용성에 의존합니다. 이 래퍼 안에서는 브라우저 확장 프로그램을 통한 서명을 사용할 수 없으며, 자체 호스팅은 별도의 Git 배포 방식으로 남아 있습니다.

### Dart NDK

[Dart NDK 0.11.0 개발 버전 0](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.0)은 Dart 및 Flutter 툴킷의 [인증 동의 처리기](https://github.com/relaystr/ndk/pull/862)와 NIP-46 서명자의 relay 전환 기능을 사전 릴리스로 제공합니다. 이 변경 사항들은 지난주에 병합된 작업으로 다루었으며, 이제 릴리스로 배포되었습니다. 서명자는 대체 relay 목록을 따를 수 있으며, 애플리케이션은 이 목록을 영구 저장해야 합니다. [개발 버전 1](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.1)은 relay 정보에서 문자가 포함된 NIP 식별자를 지원합니다. 두 릴리스 모두 기존 통합과의 호환성을 깨뜨리는 변경 사항을 포함합니다.

### Cambium

[Cambium v0.9.0](https://github.com/forgesworn/cambium/releases/tag/v0.9.0)은 네이티브 Android 앱에 [네 가지 승인 옵션](https://github.com/forgesworn/cambium/pull/32)을 제공합니다. 한 번, 한 시간, 하루 또는 무기한입니다. 권한 부여 범위는 작업과 event kind별로 정해집니다. Cambium은 원격 서명을 통해 Heartwood 하드웨어 서명자로 요청을 전달하며, 어떤 요청에 서명할지는 여전히 Heartwood가 결정합니다. 웹사이트 승인은 계속 일회성으로 유지됩니다. 페어링된 서명자에는 테스트 및 재연결 제어, 지원되는 전송용 relay 업데이트, 민감 정보가 가려진 진단 정보가 추가됩니다. [NIP-55, Android 서명](/ko/topics/nip-55/)의 일괄 요청은 요청 순서와 개별 거부를 보존하며, 재사용되어 의미가 모호한 인텐트에는 명시적으로 표시되는 일회성 동의를 요구합니다.

### Grain

[Grain v0.8.1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.1)은 여러 사용자에게 서비스를 제공하는 애플리케이션을 위해 Go 클라이언트 라이브러리의 [NIP-42 relay 인증](/ko/topics/nip-42/)을 수정합니다. 각 `UserContext`는 전용 인증 연결, relay 기본 설정, 연결 유지 상태를 소유하며, 공유 풀은 인증을 수행하지 않습니다. 라이브러리는 수신한 ID와 서명을 검증하고, 구독 일치 여부를 확인하며, tag 및 시간 필터를 올바르게 직렬화합니다. 인증을 사용하는 호출자는 `UserContext`로 이전해야 합니다. relay의 저장 및 제공 동작은 변경되지 않으며, 인증에는 여전히 연결이 열릴 때 챌린지가 필요합니다.

### Nmail

암호화 메일 클라이언트인 [Nmail v0.18.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.18.0)은 낯선 발신자의 메일을 요청함에, 차단된 발신자의 메일을 스팸함에 넣습니다. 수락과 차단 상태는 기기 간에 동기화됩니다. 기존 받은편지함의 발신자도 수락해야 하며, 모두 수락 옵션을 사용할 수 있습니다. 스팸함은 알림을 보내지 않고, 대기 중인 요청에 대해서는 같은 발신자의 알림이 반복되지 않습니다. 답장에는 수신에 사용된 신원이 적용됩니다. 초기화 또는 로그인 후의 메일함 복원 문제 수정과 함께, 비공개 relay 관리, 동기화 코드 복사 전 기기 잠금 확인, 공통 테마, 더 풍부한 연락처 정보 보존, Windows 설치 프로그램이 제공됩니다.

### Meiso

[Meiso v1.5.0](https://github.com/higedamc/meiso/releases/tag/v1.5.0)은 Nostr로 동기화되는 작업 관리자에 암호화 댓글과 읽지 않음 표시를 제공합니다. 댓글은 [NIP-44 암호화](/ko/topics/nip-44/)를 적용한, 주소 지정이 가능한 kind 35002 event를 사용하며, 어떤 작업에 연결되는지에 관한 정보는 암호문 안에 유지됩니다. 이번 릴리스는 [오프라인 전송](https://github.com/higedamc/meiso/pull/212), 재연결 후 누락분 동기화, 저장된 relay를 사용한 시작, 빈 목록 전파를 수정합니다. 또한 부분 동기화로 작업이 삭제되는 것을 방지합니다. 읽지 않음 표시와 누락분 동기화 기능이 닫힌 애플리케이션을 위한 알림 서비스를 추가하는 것은 아닙니다.

### Haps

실험적인 소프트웨어 설치 도구인 [Haps v0.1.13](https://github.com/mmalmi/haps/releases/tag/v0.1.13)은 기본적으로 사용자의 [신뢰망](/ko/topics/web-of-trust/)에 속한 사람이 정확히 해당 릴리스를 감사했을 것을 요구합니다. 감사에서는 고정된 소스와 다시 빌드한 산출물을 비교할 수 있으며, 감사 결과를 비공개로 유지하거나 공개할 수 있습니다. [버전 0.1.14](https://github.com/mmalmi/haps/releases/tag/v0.1.14)는 이름만으로 설치할 때 사용자에게 게시자를 확인하도록 요청하며, 자동화에서는 게시자를 지정해야 합니다. 감사는 근거를 제공하지만, 네이티브 프로그램과 빌드 레시피는 여전히 샌드박스 없이 실행됩니다. 감사 요구 사항은 한 번의 작업에 한해 우회할 수 있지만, 서명, 무결성, 게시자 확인 검사는 그대로 유지됩니다.

### Sidecar

[Sidecar v1.16.0](https://github.com/dmnyc/sidecar/releases/tag/v1.16.0)은 브라우저 확장 프로그램 형태의 소셜 클라이언트에 [라이브 스트림 탐색 및 재생](https://github.com/dmnyc/sidecar/pull/479)을 추가하며, 서명된 채팅, 반응, zap을 지원합니다. 저장된 스트림 북마크는 암호화된 계정 백업 및 복원을 지원하며, 비공개 알림 음소거를 통해 사용자가 알림을 제어할 수 있습니다. 검색에는 팔로우 및 음소거 제어가 추가되고, 자동 잠금과 지갑 내역 새로 고침 관련 변경 사항도 함께 제공됩니다.

### Ants

검색 인터페이스인 [Ants v0.7.0](https://github.com/dergigi/ants/releases/tag/v0.7.0)은 로그인 없이 [구조화된 검색을 라우팅합니다](https://github.com/dergigi/ants/pull/316). [NIP-65 relay 목록](/ko/topics/nip-65/)을 통해 작성자가 공지한 쓰기용 relay와 언급된 사용자의 읽기용 relay로 보냅니다. 탐색 과정에서는 조회할 신원과 relay의 수를 제한하며, 취소되거나 제한 시간이 지나면 중단합니다. 목록이 없으면 대체 라우팅을 유지합니다. 텍스트 쿼리는 여전히 검증된 [NIP-50 검색 relay](/ko/topics/nip-50/)를 사용합니다.

### soyLI

[soyLI v0.27.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.27.0)은 제안된 [NIP-5D 애플리케이션](/ko/topics/nip-5d/)을 위한 napplet 게시 및 실행 도구로, 키보드 단축키와 Git 호스팅 서비스 GRASP를 통한 포크 없는 제안을 추가하며, 재시도 시 정확한 리비전을 확인합니다. [v0.26.0 릴리스](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.0)는 최초 게시 후 검증된 아웃박스 relay에 서명된 릴리스를 배포합니다. 삭제 시에는 전송을 시도한 대상을 추적하지만, 알려지지 않은 사본까지 회수할 수는 없습니다. [버전 0.26.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.1)은 읽기, 실행, 검토에 허용되는 용량을 100 MiB로 늘리되, 새 빌드와 게시에는 25 MiB 제한을 유지합니다. 이후 도입된 [직접 표시 메타데이터](https://github.com/zeSchlausKwab/napplet-soy/pull/14)는 작성자의 표지와 클립을 서명된 매니페스트에 직접 배치하며, 보조 event를 폐지합니다. 동결된 이전 작업은 계속 지원됩니다. 버전이 지정된 이 Soy 확장에는 호환되는 리더가 필요하며, 고정된 NIP-5D 명세에는 포함되지 않습니다.

### nostream

relay 서버 [nostream v3.3.0](https://github.com/cameri/nostream/releases/tag/v3.3.0)은 WebSocket 읽기 및 쓰기 왕복 시간 측정, 선택적 인증 감지, 미러 대상 탐색을 위한 [NIP-66 relay 모니터링](/ko/topics/nip-66/) 프로브를 추가한다. 관찰된 동작이 [NIP-11 relay 정보](/ko/topics/nip-11/)와 일치하지 않으면 경고한다. 속도 제한이 적용된 OK 응답에는 밀리초 단위의 백오프 시간을 담은 선택적 다섯 번째 요소를 포함할 수 있다. [버전 3.4.0](https://github.com/cameri/nostream/releases/tag/v3.4.0)은 IP 메시지 제한으로 `REQ` 또는 `COUNT`가 거부될 때 [CLOSED 응답](https://github.com/cameri/nostream/pull/821)에 밀리초 단위의 백오프 시간을 나타내는 네 번째 요소를 추가한다. 이 버전에는 [PostgreSQL negentropy 조정 코어](https://github.com/cameri/nostream/pull/809)와 정렬된 event 목록이 포함된다. [NIP-77](/ko/topics/nip-77/) relay 전송 메시지와 지원 기능 광고는 여전히 별도 작업으로 남아 있다.

### Bark

[Bark v1.3.15](https://github.com/forgesworn/bark/releases/tag/v1.3.15)은 원격 서명 승인에 키보드 조작, 명시적인 event 및 신원 검토, [1분, 5분 또는 10분의 결정 시간](https://github.com/forgesworn/bark/pull/52)을 제공한다. 백그라운드에서 유효 기간이 지난 결정과 대기 중인 요청을 거부하며, 결정 전달에 실패하면 재시도할 수 있도록 팝업을 열어 둔다. [버전 1.3.17](https://github.com/forgesworn/bark/releases/tag/v1.3.17)은 서명자 핸드셰이크가 완료되면 [NIP-07 브라우저 서명](/ko/topics/nip-07/)을 사용할 수 있게 하며, 선택적 진단은 계속 진행된다. 업데이트 후 기존 탭의 브리지를 복원한다.

### Mostro

[Mostro v0.19.3](https://github.com/MostroP2P/mostro/releases/tag/v0.19.3)은 진행 중인 주문이 없어도 신원 인증을 거친 사용자의 본인 평판 조회 요청에 응답한다. 이 P2P 거래소는 요청한 거래 키에 비공개로 응답을 보내며, [병합된 CLI 명령](https://github.com/MostroP2P/mostro-cli/pull/203)으로 해당 조회를 수행할 수 있다. 평판 가져오기는 실제 가져오기 기능이 구현되지 않은 미리보기 상태로 남아 있으므로, 운영자는 비활성화해 두어야 한다. [이후 병합된 작업](https://github.com/MostroP2P/mostro/pull/1057)은 Lightning 에스크로 보호 여유값을 공개하고 안전하지 않은 구성을 거부한다. 최소 18블록이라는 기준은 LND의 기본 홀드 만료 설정을 전제로 한다.

### Elisym

[Elisym의 commerce 0.11.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.11.0)은 판매자 수익에서 수수료를 공제하는 방식을 지원하며, 서명된 상점 프로필 tag로 분할 결제 지원 여부를 선언하고 수수료가 적용될 때 호환되지 않는 상점을 거부한다. [병합된 관리자 기능 작업](https://github.com/elisymlabs/elisym/pull/170)은 Nostr relay에서 주문과 상품 목록을 읽는다. 이 기능은 상점의 비밀 키를 요구하므로 제공되는 브라우저 코드와 확장 프로그램을 신뢰해야 한다. 로컬 관리자 기능도 계속 사용할 수 있다. 호스팅 배포와 메인넷 수수료 활성화 여부는 아직 검증되지 않았다. [Merchant-node 0.10.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.10.0)은 원장을 업그레이드하며 다운그레이드는 지원하지 않는다.

### Routstrd

[Routstrd v0.4.16](https://github.com/Routstr/routstrd/releases/tag/v0.4.16)은 시간 초과된 [Nostr Wallet Connect](/ko/topics/nip-47/) 충전이 곧바로 또 다른 결제 가능한 인보이스를 생성하지 못하게 한다. 결제가 성공하거나 실패할 때까지 [기존 민트 작업을 확인](https://github.com/Routstr/routstrd/pull/144)하며, 상태를 확인할 수 없으면 충전을 일시 중지한 상태로 유지한다. 추론 게이트웨이는 Nostr 검토 라벨에 따라 제공자를 활성화하며, 실험적 라벨은 명시적으로 사용을 선택해야 한다. [버전 0.4.17](https://github.com/Routstr/routstrd/releases/tag/v0.4.17)에는 이를 지원하는 SDK가 포함된다. 미결 작업 보호 장치는 메모리에만 유지되므로, 데몬을 재시작하면 해당 보호가 사라진다.

### Buzz

[Buzz 데스크톱 0.5.28](https://github.com/block/buzz/releases/tag/desktop-v0.5.28)은 인증된 직원이 연결을 전환하지 않고도 relay의 [모든 커뮤니티를 탐색하고 관리](https://github.com/block/buzz/pull/8027)할 수 있게 한다. 관리 작업은 검토한 커뮤니티, relay, 서명자를 그대로 유지한다. 인증이 비활성화되어 있어도 콘솔에서 읽기는 가능하다. 별도로 [병합된 relay 작업](https://github.com/block/buzz/pull/8197)은 비공개 작성자 기록에 대해 적절한 tag가 붙은 삭제 event를 쿼리와 실시간 전달 모두에서 숨긴다. 이 서버 수정 사항은 배포가 필요하며, 이미 공개된 사본과 과거의 tag 없는 삭제 기록은 수정 범위에 포함되지 않는다.

### Earthly

[Earthly v0.1.21](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.21)은 사용자가 [공개 Nostr 지도 데이터셋을 웹사이트에 임베드](https://github.com/zeSchlausKwab/earthly/pull/35)할 수 있게 하며, 미리보기와 외형 및 초기 카메라 위치 설정 기능을 제공한다. Maps MCP 통합은 채팅에서 지도를 생성하고 게시한 뒤 공유 링크나 임베드를 생성한다. 이 통합은 아직 개인용 연결 플러그인 시범 운영 단계에 있다. 임베드는 최대 300개 지형지물과 48 KiB까지의 인라인 데이터셋을 지원하며, 비공개 데이터셋, 미게시 데이터셋, blob 기반 데이터셋은 제외된다.

### Milk Market

[Milk Market의 모바일 v0.3.0](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.0)은 웹 편집기와 동일한 섹션 및 필드를 갖춘 완전한 상점 디자인 편집기를 판매자 앱에 제공한다. 상품별 페이지 디자인은 메타데이터와 소셜 이미지를 포함해 테마 및 섹션 선택을 재정의할 수 있다. 이 릴리스는 모바일과 웹 구성이 일치하도록 유지하는 검사 기능을 추가한다. [버전 0.3.1](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.1)은 모바일 미리보기 카드의 대비를 수정한다. Android 다운로드 파일은 릴리스에 첨부되어 있으며, iOS 버전은 TestFlight에서 이용할 수 있다.

### Zeus

[Zeus v13.2.3](https://github.com/ZeusLN/zeus/releases/tag/v13.2.3)에는 지난주에 다룬 [LDK 라우팅 수수료 수정](https://github.com/ZeusLN/zeus/pull/4353)이 포함되어 이제 정식으로 제공된다. LDK 기반 Nostr Wallet Connect 서비스는 응답과 지출 기록에 보고된 라우팅 수수료를 포함할 수 있다. 예산 검사는 여전히 정산 전에 인보이스 금액을 대상으로 하며, 반올림된 수수료는 이후 차감되고 라우팅 수수료에는 별도로 1,000사토시 상한이 적용된다. 이 릴리스는 내장 LND도 업데이트하고 rust-lightning 보안 수정 사항을 포함한다. 실제 NWC 기기 검증은 아직 확인되지 않았다. 이후 [병합된 Zaplocker 제거 작업](https://github.com/ZeusLN/zeus/pull/4933)은 해당 서비스의 Nostr 증명 및 상환 절차를 폐지한다. 해당 서버가 아직 결제를 보류 중인 상태에서 업그레이드하면 상환 기능이 사라지므로, 송금자는 홀드 인보이스가 만료되어 환불될 때까지 기다려야 한다. 이 폐지는 v13.2.3에 포함되지 않으며, 적용하려면 서버를 비활성화하고 기존 사용자에게 경고해야 한다.

## 개발 중

### nosvelte

[nosvelte의 event 검증기 수정](https://github.com/akiomik/nosvelte/pull/162)은 서명을 검증하기 전에 event에 제공된 ID를 해당 필드의 정규 해시와 대조한다. 이 Svelte 라이브러리의 기본 검증기는 이전에 ID가 바뀌어 있어도 올바르게 서명된 필드를 허용했으므로, 콘텐츠가 다른 event의 식별자를 차지하여 대체 처리를 방해할 수 있었다. 병합된 변경 사항은 기본 검증기를 사용하는 버전 1 요청 및 전송 경로에 적용되며, 레거시 내보내기나 사용자 지정 검증기가 [NIP-01의 event 형식](/ko/topics/nip-01/)에 부합함을 보장하지는 않는다. 이후의 [요청 필터 수정](https://github.com/akiomik/nosvelte/pull/171)은 relay event 필드를 검사하고 복사한 뒤 일치 여부를 판정한다. 이제 잘못된 형식의 데이터로 인해 기본 제공자의 구독이 종료되거나 그다음 유효한 event가 버려지는 일이 발생하지 않는다. 호출자가 제공한 엔진 클라이언트는 이전의 의존성 일치 판정 동작을 유지할 수 있다.

### nostter

nostter는 [외부에서 제공된 relay 힌트를 제한](https://github.com/SnowCait/nostter/pull/2684)하여 보안 WebSocket URL만 허용하고 로컬 호스트 이름과 전역 주소가 아닌 IP 주소를 거부한다. 계정에서 선택한 로컬 relay와 원격 서명자 URL은 기존 경로를 유지하며, DNS 리바인딩은 검사 범위에 포함되지 않는다. 이 웹 클라이언트는 또한 독자가 표시 버튼을 누른 뒤에만 [실험적인 분리형 콘텐츠 경고 페이로드를 읽고](https://github.com/SnowCait/nostter/pull/2680), 참조된 event ID와 작성자 일치 여부, 원본 event kind와 일치하는 `k` tag를 확인한다. 반응과 답글은 원본 event를 대상으로 한다. 이 병합된 변경 사항은 현재의 [NIP-36](/ko/topics/nip-36/) 게시 형식을 바꾸지 않는다.

### Coracle

[Coracle의 목록 편집기](https://github.com/coracle-social/coracle/pull/679)는 비동기 디코딩이 완료될 때까지 기다린 뒤 양식을 렌더링함으로써 편집 및 삭제 기능을 복구한다. 이전에는 편집 시 목록의 필드가 사라졌으며, 저장과 삭제 모두 event를 게시하지 않았다.

### Routstr Core

[Routstr Core의 현재 버전 0.5.0 소스](https://github.com/Routstr/routstr-core/releases/tag/v0.5.0)는 [자동 생성된 Nostr 개인 키를 더 이상 로그에 기록하지 않으며](https://github.com/Routstr/routstr-core/pull/812), [최초 부팅 시의 공개 신원을 유지한다](https://github.com/Routstr/routstr-core/pull/818). [제공자 공지](https://github.com/Routstr/routstr-core/pull/823)에서는 localhost와 IP 주소가 직접 표기된 사설 또는 링크 로컬 HTTP 주소를 제외한다. 이 검사에서는 호스트 이름을 IP 주소로 해석하지 않는다. 현재 tag에는 기록된 공개일인 10월 7일 이후 병합된 작업도 포함되어 있으므로, 과거 바이너리와 배포본은 여전히 검증되지 않았다. 이전에 노출된 로그는 여전히 운영자가 검토해야 한다.

### Alby Hub

[Alby Hub의 인보이스 권한 부여 변경](https://github.com/getAlby/hub/pull/2629)은 결제 확정과 취소를 요청한 앱이 생성한 인보이스로 제한한다. 이 자체 호스팅 지갑은 [NIP-47, Nostr Wallet Connect](/ko/topics/nip-47/)를 통해 앱 연결을 제공한다. 한 연결이 자신의 인보이스를 관리할 수 있다고 해서 다른 앱의 인보이스에 대한 권한까지 부여되어서는 안 된다. 별도의 [격리된 연결 개인정보 보호 수정](https://github.com/getAlby/hub/pull/2621)은 격리된 연결의 브라우저 성공 처리 경로에서 주 지갑의 Lightning 주소를 제거한다.

### nak

[병합된 nak의 relay 명령](https://github.com/fiatjaf/nak/pull/222)은 연결·읽기·쓰기 소요 시간과 relay 정보를 조사한 다음, 서명되지 않은 kind 30166 탐색 event를 출력한다. 이 결과를 `nak event`로 파이프하면 서명과 게시가 이루어지므로, 같은 터미널 도구로 주기적인 [NIP-66 relay 모니터링](/ko/topics/nip-66/)을 수행할 수 있다. 실제로 관찰된 인증 또는 제한 응답은 공지된 relay 정보보다 우선한다. 쓰기 탐사에는 일회용 키로 서명한 임시 event를 사용하며, kind 10166 모니터 공지는 여전히 별도의 작업이다.

### Kehto

[Kehto의 매니페스트 검증](https://github.com/kehto/web/pull/277)은 실행 전에 현행 단일 아티팩트 서명 매니페스트와 아티팩트 바이트를 확인하며, 레거시 파싱은 별도로 유지한다. napplet 셸은 [권장 핸들러도 검증하고](https://github.com/kehto/web/pull/294), 저장된 선택과 충돌하면 사용자에게 확인하며, 수락된 호출 URL을 소진 처리해 반복 전달을 방지한다. 매니페스트 검증은 게시자의 신원과 아티팩트 바이트를 확인할 뿐, 애플리케이션 코드가 안전하다는 사실을 입증하지는 않는다. 이제 [게임패드 스냅샷](https://github.com/kehto/web/pull/297)은 포커스와 표시 상태를 따른다. Paja/playground 프레임은 애플리케이션 코드가 실행되기 전에 네이티브 게임패드, HID, USB에 대한 직접 접근을 차단하고, 중개를 통한 접근은 호스트에 맡긴다. 이를 사용하는 측에는 해당 호스트 패키지가 필요하며, 셸 준비 상태는 별개의 기능이다. 이후의 [Paja 진입 허용 변경](https://github.com/kehto/web/pull/305)은 필수로 지정된 실험적 도메인을 사용할 수 없을 때 경고하되 로딩은 허용한다. 해당 도메인은 여전히 API나 권한 부여를 제공하지 않는다.

### napplet SDK

[napplet SDK는 URI 기반 호출과 보존형 전달을 구현한다](https://github.com/napplet/web/pull/228). [게시 메타데이터는 독립 실행형 HTML에서도 유지되며](https://github.com/napplet/web/pull/226), [선택적 애플리케이션 참조](https://github.com/napplet/web/pull/239)는 아티팩트 해시를 바꾸지 않고 매니페스트를 서명된 목록 및 스크린샷과 연결한다. 애플리케이션 참조 형식은 여전히 제안 단계다. 참조 셸 테스트는 실제 운영 환경의 탐색, 설치, 서명 검증을 호스트에 맡긴다.

### rust-nostr

Rust Nostr 라이브러리 [rust-nostr는 최종 relay 오류와 함께 부분 다운로드 진행 상황을 보존한다](https://github.com/nostrdevkit/nostr/pull/1483). 실패한 relay는 실패 집합에 그대로 남으므로, 호출자는 동기화가 조기에 중단되었다는 증거를 잃지 않고도 이미 수신한 event를 사용할 수 있다.

### Pensieve

[Pensieve의 대조 안전성 수정](https://github.com/andotherstuff/pensieve/pull/92)은 [누락된 event 제외 작업](https://github.com/andotherstuff/pensieve/pull/90)에 뒤이어 이루어졌다. relay 및 아카이브 도구는 실패를 분류하기 전에 누락된 정확한 ID를 다시 요청하므로, 조회 한도 때문에 잘린 후반부가 잘못된 제외 처리로 이어지는 것을 방지한다. 일시 중지 집계는 작업별로 이루어지며, 이미 보관된 event는 별도로 처리한다. 완료된 작업에도 명시적인 누락 event 기록이 남을 수 있으므로, 완료되었다는 사실만으로 아카이브가 완전하다고 볼 수는 없다.

[지속적인 Premium Primal 대조](https://github.com/andotherstuff/pensieve/pull/84)는 10월 12일 활성화되었다. 운영자의 [배포 기록](https://github.com/andotherstuff/pensieve/pull/93)에 따르면 수정된 바이너리 두 개가 모두 배포되었고, 실패에 따른 일시 중지가 10월 13일 활성화되었다. 이후의 [제외 항목 이월](https://github.com/andotherstuff/pensieve/pull/95)은 동일한 relay와 겹치는 시간 구간에 대해 원래 입증된 제외 항목만 재사용하며, 연쇄 이월과 새로 섞인 ID는 제외한다. [그 배포는 같은 날 오후에 기록되었다](https://github.com/andotherstuff/pensieve/pull/97). [아카이브 사전 점검 및 캐시 정체 수정](https://github.com/andotherstuff/pensieve/pull/98)은 [10월 14일 배포되었다](https://github.com/andotherstuff/pensieve/pull/99). 그 이후의 [이월 우선순위 수정](https://github.com/andotherstuff/pensieve/pull/103)은 병합되었지만, 해당 소스 기록상으로는 아직 배포되지 않았다.

### njump

Nostr 웹 뷰어 [njump는 재정의 파일이 제공되지 않으면 내장된 relay 기본값을 복원한다](https://github.com/fiatjaf/njump/pull/173). 또한 [동시에 실행되는 Markdown 렌더러](https://github.com/fiatjaf/njump/pull/171)와 [시간 초과 시의 응답 헤더](https://github.com/fiatjaf/njump/pull/169)를 격리하여, 인용된 장문 event를 렌더링하거나 동시 요청을 처리할 때 프로세스를 비정상 종료시킬 수 있었던 경쟁 상태를 수정한다. 이는 병합된 서버 변경 사항이며, 실제 서비스 배포 여부는 아직 검증되지 않았다.

### Nostr Components

[Nostr Components의 zap 서명 수정](https://github.com/saiy2k/nostr-components/pull/187)은 선택한 서명기가 거부하면 결제 흐름을 중단한다. 임베드 가능한 소셜 위젯은 거부 이후 더 이상 무작위 익명 신원으로 대체하지 않는다. 이 위젯의 [영수증 집계](https://github.com/saiy2k/nostr-components/pull/197)는 relay 사본, 인보이스, 요청 ID의 중복을 제거하기 전에 [NIP-57 zap 영수증](/ko/topics/nip-57/)을 검증한다.

### rx-nostr

반응형 클라이언트 라이브러리 [rx-nostr의 버전 4 검증 변경](https://github.com/penpenpng/rx-nostr/pull/207)은 JavaScript와 WebAssembly 전반에서 정규 event 구조, ID, 서명을 일관되게 확인한다. 요청 조건 목록이 비어 있으면 아무것과도 일치하지 않은 채 완료되며, 레거시 전송은 목적지가 없을 때 실패를 보고한다. 게시 관찰자는 확정 처리를 바꿀 수 없으며, 해제된 요청의 하위 요청은 다시 시작할 수 없다. [유한 쿼리 구간](https://github.com/penpenpng/rx-nostr/pull/213)은 제공된 모든 구간이 끝난 뒤 역방향 쿼리가 완료될 수 있게 한다. 이러한 변경은 호환성을 깨뜨리는 API 변경이 있는 사전 릴리스인 [4.0.0 베타 2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%404.0.0-beta.2)에 포함되어 있다.

### eHagaki

소셜 클라이언트 [eHagaki는 단계적 아웃박스 전달을 추가하여](https://github.com/Lokuyow/ehagaki/pull/268), 서명 전에 작성자의 대상 relay를 고정한다. 민감한 게시물 처리 흐름은 각 relay 자체의 수신 확인을 이용해, 페이로드를 참조하는 구조보다 페이로드를 먼저 해당 relay에 보낸다. 페이로드만 성공적으로 전송된 경우 작성 화면은 유지된다. [전체 게시 이력 스캔](https://github.com/Lokuyow/ehagaki/pull/312)은 검증된 결과를 점진적으로 저장한다. 스캔이 완료된 것으로 표시되더라도 모호한 범위는 미확인 상태로 남으며, 이를 설명하는 정보 컨트롤이 제공된다. [Citrine 로컬 relay 지원](https://github.com/Lokuyow/ehagaki/pull/315)은 검증된 탐색 범위를 보존하고, 외부 게시가 성공한 뒤 서명된 event를 정확히 그대로 보관한다. 로컬 수신 확인이 실패한 외부 전송을 성공으로 바꾸지는 않으며, 이 기능은 오프라인 게시 대기열을 추가하지 않는다. [업로드된 미디어 관리](https://github.com/Lokuyow/ehagaki/pull/321)는 지원되는 NIP-96 및 Blossom 서버에 업로드된 이미지와 동영상의 목록 조회와 삭제를 제공한다. [이후의 데이터베이스 마이그레이션](https://github.com/Lokuyow/ehagaki/pull/325)은 초안과 삭제 요청을 유지하면서 캐시된 표시 이력과 게시 이력을 초기화한다. 또한 초기화 후 대기열에 있던 이전 동기화 결과가 이력을 다시 채우지 못하게 한다.

### Formstr

[Formstr의 제출 결과 수정](https://github.com/formstr-hq/nostr-forms/pull/508)은 어떤 relay도 수락하지 않은 양식 응답을 거부한다. 이 Nostr 양식 애플리케이션은 relay별 결과를 표시하고, 입력한 답변을 보존한 채 재시도할 수 있게 한다. 웹훅과 확인 페이지는 수락될 때까지 기다리며, SDK에도 같은 검사가 적용된다. relay의 수신 확인이 장기 저장 보장과 같은 것은 아니지만, 게시가 전부 실패했을 때 더 이상 성공 메시지가 표시되지 않는다.

### Auditable Voting

[Auditable Voting에 선택형 비공개 워커 투표 일괄 처리 기능이 추가된다](https://github.com/tidley/auditable-voting/pull/35). 주최자가 서명한 정의에서 워커 신원, DM relay, 공개 임계값 또는 기한을 지정한다. 투표자는 [NIP-17 gift-wrap으로 감싼 투표지](/ko/topics/nip-17/)를 보내고 해당 워커를 기준으로 수신증을 인증한다. 위임은 대기열 등록과 공개를 모두 허용해야 한다. 공개된 투표지는 워커의 신원을 사용한다. 워커는 제출 내용을 읽을 수 있으며, 기한에 따라 공개되는 묶음은 규모가 작을 수 있다. 유효한 비공개 경로를 찾지 못하면, 검토한 클라이언트는 공개 제출 방식으로 전환한다. 이는 병합된 개발 작업이다.

### MintRadar

[MintRadar에 선택형 gift-wrap 알림이 추가된다](https://github.com/hroomnik007/MintRadar/pull/122). 이 알림은 mint 또는 melt 문제, 오래된 소프트웨어, 해당 작업에 대한 지원 중단을 대상으로 한다. Cashu mint 디렉터리는 [관심 목록 제어 기능을 연결](https://github.com/hroomnik007/MintRadar/pull/123)하여 해당 알림 설정을 조정하고, 서버가 응답한 뒤 이를 확인한다. 원자적 선점으로 중첩된 점검이 같은 알림을 보내지 않도록 하며, relay 게시에 실패하면 선점을 해제하여 재시도할 수 있게 한다. [NIP-17 비공개 메시지](/ko/topics/nip-17/)는 알림 내용을 보호하지만, relay가 수락해도 수신자가 읽었는지는 확인되지 않는다.

### Nostr Docs

[Nostr Docs의 로컬 relay 마이그레이션](https://github.com/formstr-hq/nostr-docs/pull/65)은 협업용 Markdown 편집기의 읽기와 쓰기를 IndexedDB event 캐시와 재시도용 발신함을 갖춘 Web Worker를 통해 처리한다. 문서 제목과 tag는 새로고침 후에도 유지되며, 연속적인 메타데이터 편집에는 점점 큰 타임스탬프가 부여되어 같은 초에 이루어진 두 편집도 구분된다. 기존 암호화 키 저장 방식은 그대로 유지된다. 대체 경로인 네트워크 풀에는 워커 발신함의 내구성이 없으며, 대기열에 등록된 게시를 수락했다고 해서 relay 수락이 성립하는 것은 아니다.

### Pakstr

[Pakstr의 네이티브 로컬 서명기](https://git.nostrdev.com/stuff/pakstr/pulls/105)를 통해 Android 애플리케이션 셸이 기기에서 Nostr 계정을 생성할 수 있다. 키는 Android Keystore로 보호되는 래핑 키로 암호화되어 네이티브 계층에 보관된다. 서명 결과는 웹 애플리케이션으로 반환되기 전에 검증된다. 셸은 [NIP-07 브라우저 서명](/ko/topics/nip-07/)과 암호화된 요청을 지원한다. 서명기 선택 화면은 필요할 때만 열리며, 동시 요청을 조율한다.

### Nostr WoT SDK

신뢰망 라이브러리 [Nostr WoT SDK는 인증 동의의 적용 범위를 확장](https://github.com/nostr-wot/nostr-wot-sdk/pull/15)하여 타입이 지정된 네이티브 및 원격 요청자까지 포함한다. 동의 창을 표시하기 전에 저장된 거부 내역을 확인하며, 재사용 가능한 동의는 요청에 사용된 전송 방식과 대상에 연결된다. 웹 요청은 기본적으로 여전히 일회성이다. [관리형 Blossom 업로드](https://github.com/nostr-wot/nostr-wot-sdk/pull/13)는 변경 불가능한 바이트 데이터를 검증하고 취소를 지원하며, 활성 세션이 바뀌면 중단된다. 인증은 서버에 귀속되며 리디렉션에도 제한이 적용된다.

### NosTube

[NosTube v0.2.49](https://github.com/flox1an/nostube/releases/tag/v0.2.49)는 데스크톱 설치 프로그램을 제공한다. 이와 별개로, 병합된 서버 작업은 [내구성 있는 예약 게시 기능을 추가한다](https://github.com/flox1an/nostube/pull/126). event는 예정 시각 전에 서명되어 SQLite에 저장되며, 중단 후 누락된 작업을 따라잡는 워커가 게시한다. [편집 및 삭제 흐름](https://github.com/flox1an/nostube/pull/124)은 삭제 표식, 미러 전달, 소유 파일 정리를 추적한다. [최초 실행 설정](https://github.com/flox1an/nostube/pull/134)은 사용자의 브라우저 서명기와 서버가 관리하는 채널 키를 구분한다. 과거의 소유권 없는 blob은 여전히 자동 정리 대상에서 제외된다.

### diVine

[diVine 1.0.24](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.24)는 크레딧 표시를 포함한 비공개 클립 공동 작업과 서명된 촬영 또는 편집 출처 검사를 추가한다. 시청자가 선택한 번역 자막은 번역이 대기 중이거나 검증되지 않은 동안 원문 자막으로 대체된다. 이러한 출처 검사가 편집되지 않은 녹화물임을 보장하지는 않는다.

이 짧은 동영상 클라이언트의 [라우팅 변경 사항](https://github.com/divinevideo/divine-mobile/pull/9884)은 텍스트 및 영상 채팅 메시지에 대해 수신자의 수신함 relay를 조회하며, 전달 여부가 불확실한 결과를 그대로 유지한다. [발신자 사본 처리](https://github.com/divinevideo/divine-mobile/pull/10006)를 통해 사용자가 보낸 그룹 메시지가 자신의 다른 기기에도 표시된다. 이전에 폐기된 사본을 가져오려면 계정을 다시 가져와야 한다. [일부 전송 후 취소된 그룹 전송](https://github.com/divinevideo/divine-mobile/pull/10031)은 “모두에게 전송되지 않음” 기록을 유지한다. 취소는 최종 상태이며 해당 기록은 재시도할 수 없다. 그룹 생성과 상대방이 새로 시작한 대화방 인식은 여전히 [기본적으로 꺼진 플래그 뒤에 있다](https://github.com/divinevideo/divine-mobile/pull/10020).

이후 main 브랜치의 변경 사항은 [중단된 데이터베이스 복원 사본을 임시 캐시 밖에 보관](https://github.com/divinevideo/divine-mobile/pull/10118)하고, [재구축 중 예약 게시물, 대기 중인 신고, 프로필 편집 사항, 삭제된 채팅 기록을 보존한다](https://github.com/divinevideo/divine-mobile/pull/10115). [전송 기한에는 relay 재연결 시간도 포함](https://github.com/divinevideo/divine-mobile/pull/10127)되어, 중단된 전송의 재시도 기준 시간이 160초에서 137초로 줄어든다. [인덱서 수신함 조회는 크기가 제한된 별도 풀을 사용](https://github.com/divinevideo/divine-mobile/pull/10116)하여 피드 읽기 작업 뒤에서 기다리지 않으며, 확인 전에 연락처 목록이 바뀌어도 [팔로우 제어 기능은 선택한 동작을 유지한다](https://github.com/divinevideo/divine-mobile/pull/10147). 이러한 후속 병합으로 재연결이 느릴 때 relay 수신 확인을 기다릴 수 있는 시간이 줄어든다. 데이터베이스 복구로 이전에 손실된 데이터를 복원할 수는 없다. 이후 추가된 [선택형 녹화 사본](https://github.com/divinevideo/divine-mobile/pull/10110)을 사용하면 Android 및 iOS 갤러리 백업으로 새로 녹화한 클립을 보존할 수 있다. 서명된 출처 정보가 없는 사본에는 경고가 표시되고 다시 가져올 수 없다. 이 기능은 기본적으로 꺼져 있으며 추가 저장 공간이 필요하다.

### Conduit

[Conduit의 상거래 애플리케이션에 공용 영속 수신함이 추가](https://github.com/Conduit-BTC/conduit-mono/pull/616)되어 Market과 Merchant 전반에서 암호화된 메시지 전달 및 복구를 유지한다. 발신자 자신의 사본 전송이 실패해도 수신자 relay의 수락은 유지되며, 복구 시에는 동일한 바이트 데이터를 재사용하여 의미상 중복 전송을 방지한다. [공용 서명기 기반 지갑](https://github.com/Conduit-BTC/conduit-mono/pull/635)이 두 애플리케이션을 연결한다. 이 복구 경로는 복구용 평문을 서명기에 맡긴다. 소스 통합만으로는 실제 배포나 자금을 투입한 인수 테스트가 이루어졌다고 볼 수 없다. 여러 계정 경로가 URL 하나를 공유하더라도 [독립적인 relay 권한 부여](https://github.com/Conduit-BTC/conduit-mono/pull/645)는 유지된다. 한 경로를 비활성화해도 다른 서명된 relay 목록이나 수신함 권한 부여가 더 이상 삭제되지 않으며, 인증이 필요하거나 불완전한 읽기는 이용 불가 결과를 유지한다. [병합된 결제 라우터](https://github.com/Conduit-BTC/conduit-mono/pull/613)는 구매자가 승인한 한 건의 자금 조달 결제를 판매자와 공급자에 대한 Lightning 지급, 그다음 Conduit 수수료로 나누며, 의도와 정확히 대조·정산하고 공용 Nostr 수신함을 통해 암호화된 복구를 수행한다. 프로덕션 및 스테이징 실행은 여전히 비활성화되어 있다. 제공자 측 완료가 수신자의 수령이나 결제의 최종 종결을 입증하지는 않는다.

### Bitcredit

[Bitcredit의 영속 데이터 암호화](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1041)는 개인 신원의 니모닉을 사용하여 Nostr 재전송 대기열을 포함한 전자 어음 애플리케이션의 신원, 회사 및 어음 키를 보호한다. 초기화하려면 일치하는 니모닉이 필요하다. [인스턴스 관리](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1043)를 통해 testnet 및 mainnet 인스턴스가 한 기기에서 각자의 백그라운드 Nostr 구독을 독립적으로 계속 실행할 수 있다.

## 새 프로젝트

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0)은 암호화된 보관함을 Nostr를 통해 동기화하는 비밀번호 관리자를 출시했다. 외부 서명기를 지원하고 동시에 생성된 항목 버전들을 유지하며, Bitwarden JSON 가져오기와 내보내기를 제공한다. 변경 사항은 relay의 수락을 기다리기 전에 로컬에 저장된다. 이번 릴리스에는 Android, 데스크톱 및 CLI 다운로드가 함께 제공된다. 프로젝트는 아직 초기 단계임을 밝히고 중요한 비밀번호에는 검증된 관리자를 사용하도록 권고한다. 해당 버전으로 태그된 프로토콜 명세는 아직 비어 있다. [웹 저장소](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md)에는 보호 대상 데이터와 함께 암호화 키가 저장된다.

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md)은 Nostr 기반 MLS 그룹 채팅의 Common Lisp 구현을 추가했다. 10월 9일 코드는 경쟁하는 커밋의 수렴과 암호화된 Blossom 첨부 파일을 추가했으며, 작성자는 MDK의 wn 명령줄 클라이언트와 상호운용성 테스트를 수행했다고 보고했다. 이 구현은 보안 감사를 받지 않았으며, 계정 키와 메시지 로그는 저장 시 암호화되지 않는다. 시간 제한이 있는 수렴 구간, 롤백 가능 범위를 넘어선 재생, 그룹 해산은 아직 구현되지 않았다. 검토된 테스트 하네스는 일회용 로컬 relay를 사용한다.

### nalgorithm Android

[nalgorithm의 Android 릴리스](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0)는 선호도에 따라 순위를 매긴 Nostr 피드와 오프라인에서 재생할 수 있는 백그라운드 오디오 요약을 생성한다. 사용자는 Lightning으로 요금이 부과되는 호스팅형 추론 또는 휴대전화에서 요청하는 본인 키 기반 추론을 선택한다. 이 둘은 별개의 경로다. 로그인은 원격 서명을 통해 Amber를 지원한다. 후속 릴리스는 [본인 키 기반 순위 지정과 팔로우 목록 검색을 수정](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1)한 뒤, [다른 relay에 장애가 발생해도 정상 작동하는 relay의 좋아요를 보존](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2)하고 요약 복구를 개선한다. [버전 1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3)은 모델 설정 순서를 재배치하고 연결 테스트에 필요한 입력이 누락되면 이를 알린다.

## 프로토콜 및 명세 작업

### 인증된 napplet 엔드포인트

napplet 애플리케이션을 위한 NAP 명세에서 10월 9일 병합된 [NAP-INC 엔드포인트 식별자](https://github.com/napplet/naps/pull/104)는 단순한 핸들러 이름을 인증된 식별자로 대체한다. 이제 서로 다른 게시자가 사용하는 동일한 이름은 같은 피어를 식별하지 않는다. 런타임은 여전히 통신을 중재하며, 루트 또는 스냅샷 매니페스트에는 이름이 지정된 `d` 좌표가 필요하지 않다.

### 호출 링크의 핸들러 추천

역시 10월 9일 병합된 [호출 링크 추천](https://github.com/napplet/naps/pull/99)은 선택 사항인 `#naddr` 핸들러 추천을 허용한다. 셸은 검색과 설치를 제공할 수 있으며, 대체 수단으로 일반적인 해석 절차를 사용한다. 저장된 기본 설정과 셸 정책이 우선한다. 따라서 추천 핸들러는 사용자의 기존 선택을 대체하거나 링크 발신자에게 설치 권한을 넘기지 않으면서 검색을 위한 힌트를 제공한다.

### 전달 수락과 애플리케이션 작업

[인텐트 공고 및 전달 변경 사항](https://github.com/napplet/naps/pull/91)은 게시자 간 충돌을 방지하는 식별자를 사용하여 동일한 검증된 매니페스트에서 역할과 인텐트를 도출한다. 전달 수락은 더 이상 출발지 애플리케이션이 계속 실행 중인지에 좌우되지 않는다. `ok: true` 응답은 전달 책임을 수락한다는 뜻이며, 목적지의 애플리케이션 작업이 완료되었다는 뜻은 아니다. 병합된 이 명세 변경에서도 재시도와 재시작 동작은 런타임 정책으로 남는다.

### Cyberspace 작업 체인

[Cyberspace의 개정된 체인 규칙](https://github.com/arkin0x/cyberspace/pull/48)은 포크가 발생하면 서명된 작업 체인을 생성 지점부터 무효화하고, 클라이언트가 다른 작업에 서명하기 전에 현재 유효한 체인의 선두를 확인하도록 요구한다. Nostr 기반의 이 세계는 구현체가 따라야 할 규범적 판정 결과를 포함한 [서명된 합성 체인 140개](https://github.com/arkin0x/cyberspace/pull/49)를 추가한다. [복사본 출처 표기 규칙](https://github.com/arkin0x/cyberspace/pull/47)은 원본 객체에 대한 `q` 참조를 사용하고 공개 리믹스의 경우 원작자에게 알린다. 봉인된 복사본은 이 알림을 생략한다. 이들은 병합된 프로젝트 명세이며, 배포된 검증기가 이를 어느 범위까지 지원하는지는 확인되지 않았다.

### relay 영속 저장 확인 응답

[검토 중인 영속 저장 제안](https://github.com/nostr-protocol/nips/pull/2496)은 영속 저장 확인 응답, PROOF 질의, 그리고 선택 사항인 서명된 kind 1797 relay 증명을 도입한다. 서명은 저장했다는 주장의 주체가 어느 relay인지 확인할 수 있게 하지만, 계속 보관하고 있음을 증명하지는 않는다. 질의는 클라이언트가 어떤 event에 관심이 있는지도 드러낸다.

### Marmot 그룹의 공유 고정 항목

[Marmot의 검토 중인 고정 제안](https://github.com/marmot-protocol/marmot/pull/434)은 최대 64개의 메시지 참조에 대해 구성원 및 관리자 권한을 갖춘 인증된 공유 상태를 정의한다. 변경 사항이 효력을 가지려면 MLS Commit과 epoch 전환이 필요하며, 그 결과로 생기는 모든 구성원 리프가 이 기능을 지원해야 한다. 고정은 메시지 본문을 복사하거나 보관 기간을 늘리지 않으므로, 이용할 수 없는 대상은 계속 확인되지 않은 상태로 남는다. 제공된 테스트 픽스처는 인증된 상태를 전제로 하며, 암호학적 처리나 클라이언트 간 수렴을 입증하지 않는다.

## NIP 심층 분석: NIP-36과 NIP-38

### 표시 전 콘텐츠 경고

[NIP-36, 민감한 콘텐츠](/ko/topics/nip-36/)는 작성자가 event에 `content-warning` tag를 추가하고, 선택적으로 사유를 포함할 수 있게 한다. 클라이언트는 독자가 표시하기로 선택할 때까지 콘텐츠를 숨길 수 있다. [명세](https://github.com/nostr-protocol/nips/blob/master/36.md)는 인터페이스를 클라이언트에 맡기고 추가적인 라벨 tag를 허용한다. 경고를 추가해도 누가 event를 읽을 수 있는지는 바뀌지 않는다. 공개 게시물의 경우 relay와 다른 클라이언트는 여전히 그 콘텐츠를 수신한다.

[Amethyst의 경고 tag 파서](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt)는 해당 tag를 인식하고, 사유가 없거나 비어 있으면 지정되지 않은 것으로 처리한다. [Coracle의 작성 화면](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte)은 사유를 tag에 기록한다. [콘텐츠 보기](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte)는 독자의 민감한 콘텐츠 설정을 따르고 콘텐츠를 표시하는 동작을 제공한다. [noStrudel의 노트 보기](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx)는 경고 인터페이스를 표시하기 전에 자체 경고 기본 설정과 펼침 상태를 적용한다.

[NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md)은 event를 암호화하거나 숨김을 요구하지 않는다. 경고가 없다는 사실은 콘텐츠에 대해 아무것도 말해 주지 않는다. 경고가 미리보기와 표시 제어에 어떤 영향을 미칠지는 클라이언트가 결정한다.

### 프로필 상태와 만료

[NIP-38, 사용자 상태](/ko/topics/nip-38/)는 주소 지정이 가능한 kind 30315 event를 사용한다. 작성자, kind, `d` tag가 상태 좌표를 식별하며, `general`과 `music`에는 정의된 의미가 있다. 더 새로운 event는 해당 좌표의 이전 상태를 대체하지만, 다른 `d` 값은 별도로 유지된다. 빈 콘텐츠는 상태를 지운다. [명세](https://github.com/nostr-protocol/nips/blob/master/38.md)는 URL, 프로필, event 및 주소에 대한 참조도 허용한다.

이 서명된 [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) event는 만료된 일반 상태를 보여 준다. 작성자의 원래 철자를 그대로 유지했다.

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[Damus의 상태 모델](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift)은 만료 시간이 있는 일반 상태와 음악 상태를 처리한다. [Nostria의 상태 서비스](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts)는 비어 있거나 만료된 값을 무시하고 트랙 재생 시간을 사용해 음악 상태를 게시한다. 일반적인 구독에서는 일반 유형과 음악 유형만 요청한다. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt)는 상태를 지울 때 `d` 식별자를 보존한다. 따라서 사용자 정의 유형에는 공통 전송 구조 외에도 별도의 합의가 필요하다.

상태는 작성자가 공개적으로 밝히는 내용이다. 온라인 접속 여부나 누군가가 트랙을 들었다는 사실을 증명하지는 않는다. 음악이나 연락 가능 여부를 게시하면 생활 습관이 드러날 수 있으며, 선택적으로 설정하는 만료 시간은 오래된 상태가 표시되는 것을 제한할 뿐 삭제를 보장하지는 않는다. [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md)은 NIP-36과 마찬가지로 여전히 선택적으로 적용하는 초안 사양이다. 클라이언트는 어느 쪽이든 독립적으로 구현할 수 있으며, 독자가 무엇을 보게 되는지는 클라이언트의 표시 설정에 따라 결정된다.
