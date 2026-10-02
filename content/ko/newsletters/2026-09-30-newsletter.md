---
title: "Nostr Compass #42"
date: 2026-09-30
publishDate: 2026-09-30
translationOf: /en/newsletters/2026-09-30-newsletter.md
translationDate: 2026-10-02
draft: false
type: newsletters
description: "Nostr Compass #42는 Compass Android 앱을 소개하고, White Noise 투표, 안정판 Dart NDK, Holoboard와 FIPS, 새로운 Nostr 앱, relay 및 signer 변경 사항, 그리고 여섯 해에 걸친 9월의 이정표를 다룹니다."
---

매주 Nostr를 안내하는 [Nostr Compass](https://nostrcompass.org)에 다시 오신 것을 환영합니다.

Nostr Compass 전용 [Nostr Compass Android 앱](https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android)은 뉴스레터, 팟캐스트 에피소드, 토픽 가이드, 기여자 음성 메모를 한곳에 모읍니다. [최신 서명 릴리스 노트](https://zapstore.dev/apps/naddr1qq2x7un89ehx7um5wf3k7mtsv9ehxtnpwpcqzxrhwden5te0wfjkccte9eaxzurnw3hhyefwv3jhvq3qwav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qqxpqqqplqk563kdn)에 따르면 서명이 검증된 전체 뉴스레터, 오프라인에서도 볼 수 있는 저장된 호와 110개의 토픽 가이드, 그리고 기사와 제공되는 녹취록 전반에 걸친 로컬 검색을 제공합니다. 기여자는 음성 메모를 녹음하고 답장할 수 있으며, 보내기 전에 저장된 녹음을 검토하고, 앱에 개인 키를 저장하지 않은 채 Amber를 통해 서명할 수 있습니다. 공개 녹음은 Nostr와 Blossom에 게시됩니다.

[최신 앱 업데이트](https://zapstore.dev/apps/naddr1qq2x7un89ehx7um5wf3k7mtsv9ehxtnpwpcqzxrhwden5te0wfjkccte9eaxzurnw3hhyefwv3jhvq3qwav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qqxpqqqplqk563kdn)는 Android가 백그라운드 작업을 중단해도 대기 중인 녹음과 업로드 체크포인트를 보존하고, Amber 승인이 필요한 시점을 표시하며, 알림에서 해당 녹음을 바로 엽니다. 에피소드 보기와 음성 메모 보기는 각자의 스크롤 위치를 유지하며, 재생은 같은 지점에서 이어집니다. 새 녹음 알림은 Android의 스케줄링과 권한에 따라 달라집니다.

**이번 주:** [White Noise](#white-noise-android-adds-group-polls-and-account-specific-disappearing-message-defaults)는 암호화된 그룹 투표와 불완전한 채팅 기록에 대한 알림을 추가하고, [Holoboard](#holoboard-adds-nostr-promotion-commands-and-an-android-app)는 [비공개 메시지 홍보 명령](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md#2026-09-23)과 Android 앱을 추가하며, [fips-pub-domains](#fips-pub-domains-tests-signed-public-names-for-a-mesh)는 메시에서 서명된 공개 이름을 시험하고, [Marmot MDK](#marmot-mdk-0110-makes-account-history-gaps-visible)는 누락된 암호화 그룹 기록을 드러내며, [Myco](#myco-080081-gives-nearby-apps-their-own-nostr-store)는 근처 앱 공유에 Nostr 신원과 스토어를 제공합니다. [nostream](#nostream-310-adjusts-relay-proof-of-work-to-load)은 relay 수락 기준을 부하에 맞춰 조정하고, [Nostr double ratchet](#nostr-double-ratchet-0017100172-closes-a-removed-member-gap)은 제거된 멤버와 관련된 공백을 막습니다. 개발 작업으로는 [Amethyst의 암호화 그룹 상호 운용성](#amethyst-repairs-encrypted-group-interoperability)이 수리되고, [Divine의 암호화된 동영상 메시지](#divine-adds-encrypted-video-to-direct-messages)가 추가되며, [Nostr Atlas](#nostr-atlas-opens-a-directory-for-checkable-identities)가 공개됩니다. 프로토콜 업데이트는 신원 증명, relay 초대, 팔로우 세트, 제안된 도메인 클레임을 다듬습니다. 월말 [9월 회고](#six-years-of-nostr-septembers)는 같은 질문들을 따라 Nostr의 여섯 해를 되짚습니다.

## 주요 소식 {#top-stories}

### Holoboard가 Nostr 홍보 명령과 Android 앱을 추가 {#holoboard-adds-nostr-promotion-commands-and-an-android-app}

[Holoboard](/ko/topics/holoboard/)는 Lightning 결제로 끌어올릴 수 있는 순위를 통해 [Nostr 노트를 찾는 보드](https://holoboard.space)입니다. 원래 게시물은 Nostr event로 남아 있으며, Holoboard는 순위와 표시 데이터를 자체 HTTP API로 제공합니다. 보드의 정렬 순서를 relay 고유의 피드로 기대하는 독자라면 이 차이가 중요합니다.

[9월 23일 변경 기록](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md#2026-09-23)에는 암호화된 [NIP-17](/ko/topics/nip-17/) 경로와 레거시 [NIP-04](/ko/topics/nip-04/) 경로 모두를 통한 다이렉트 메시지 홍보 명령이 기록되어 있습니다. NIP-17은 비공개 메시지를 감싸 그 내용과 발신자를 relay로부터 숨기며, NIP-04는 이전의 다이렉트 메시지 암호화 형식입니다. 사용자는 같은 대화 안에서 홍보 인보이스를 요청하고, 첫 유료 홍보에 대해 레이블이 붙은 견적 하나를 받으며, `YES`로 답장해 만료 알림을 받도록 선택할 수 있습니다. 홍보 발신기는 실패한 relay에 재시도하며, [9월 24일 업데이트](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md)는 Android 앱을 추가하고 인보이스 흐름을 단순화합니다.

프로젝트의 [relay 통합 노트](https://github.com/ptrio42/holoboard.space/blob/main/relay/README.md)는 Nostr상의 일반 노트와 댓글, 암호화된 받은편지함 라우팅, 인용 및 삭제 처리를 설명합니다. 서명된 [Zapstore Android 등록 정보](https://zapstore.dev/apps/space.holoboard.app)는 앱 릴리스가 존재함을 뒷받침하지만, 등록 정보의 키가 Holoboard의 공개 보드 신원으로 확인된 것은 아닙니다. 이 프로젝트를 Compass에서 다루는 것은 이번이 처음입니다.

### fips-pub-domains가 메시를 위한 서명된 공개 이름을 시험 {#fips-pub-domains-tests-signed-public-names-for-a-mesh}

[fips-pub-domains](/ko/topics/fips-pub-domains/)는 공개 도메인 이름을 FIPS 노드에 바인딩하는 새로운 [리졸버이자 이름 체계 실험](https://github.com/fr34aky/fips-pub-domains)입니다. FIPS는 피어 탐색에 Nostr 메시지를 사용하는 암호화 메시입니다. [첫 릴리스](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0)는 이러한 클레임을 DNS TXT 레코드, 선택적 DNSSEC 검증, 로컬에 고정된 바인딩, Linux 리졸버 데몬, 그리고 휴대전화용 FIPS 클라이언트인 fips2go와의 Android 통합과 결합합니다. 서명된 클레임만으로는 공개 도메인의 소유권이 입증되지 않으며, 클라이언트에는 DNS 또는 DNSSEC 증거, 설정된 증인, 또는 이전에 신뢰한 고정 값이 필요합니다.

[0.2.0 릴리스](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0)는 클레임에 DNSSEC 증명을 추가해 메시 relay만 있는 클라이언트도 고정되지 않은 이름을 검증할 수 있게 하고, 검증된 여러 서버가 하나의 도메인을 제공할 수 있게 합니다. 또한 오래된 고정 값과 DNS 장애 조치를 수리합니다. [버전 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1)은 시작에 실패하던 systemd 유닛을 수정하고 서버를 root 권한 없이 실행합니다. 기존 설치는 수정 사항을 받으려면 해당 유닛을 교체해야 합니다.

Android에서는 [병합된 fips2go 변경](https://github.com/fr34aky/fips2go/pull/55)이 DNS 프록시에서 검증된 공개 이름 바인딩을 따릅니다. [두 번째 병합된 변경](https://github.com/fr34aky/fips2go/pull/59)은 설정된 Nostr relay로의 연결을 메시 위로 전달하므로, 휴대전화에 인터넷 연결이 없어도 리졸버가 이전에 본 적 없는 도메인 클레임을 가져와 검증할 수 있습니다. 기기에서의 결과는 해당 풀 리퀘스트에서 유지관리자가 보고한 것이며, 더 넓은 배포를 입증하지는 않습니다.

프로젝트의 [2노드 및 메시 전용 relay 테스트](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)는 초기 구현에 대해 유지관리자가 보고한 증거이며, 프로덕션 배포가 아닙니다. 이 프로젝트의 [NIP-DB](/ko/topics/nip-db/) [제안](https://github.com/nostr-protocol/nips/pull/2487)은 아직 열려 있고, [초안](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)의 event kind는 등록 전까지 임시 값으로 남아 있습니다. 지난주 fips2go 기사는 메시 부트스트랩과 피어 탐색을 다뤘고, 이번 주 작업은 공개 이름과 검증을 다룹니다.

### Marmot MDK 0.11.0이 계정 기록의 공백을 드러냄 {#marmot-mdk-0110-makes-account-history-gaps-visible}

[Marmot MDK](https://github.com/marmot-protocol/mdk)는 [MLS로 암호화된 Nostr 그룹 메시징](/ko/topics/marmot/)을 위한 Rust 런타임과 생성된 바인딩을 제공하며, 지난주의 지속성 있는 전송 릴리스에 이어 [버전 0.11.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.11.0)을 내놓았습니다. 이제 계정 복구는 필요한 모든 relay가 잘리지 않은 event 비교를 마친 뒤에만 기록 공백을 완료로 선언하며, 입증되지 않은 공백은 호스트가 사용자에게 보여 줄 수 있는 지속성 있는 알림을 생성합니다. 전달 대기열이 가득 차면 event를 버리는 대신 계정 데이터베이스로 넘기며, 실시간 전달은 전송 커서를 전진시켜 재시작 후 같은 기록을 다시 가져오지 않게 합니다.

[전체 릴리스 노트](https://github.com/marmot-protocol/mdk/blob/v0.11.0/docs/release/0.11.0.md)는 선택적인 암호화 그룹 투표, 바인딩의 상태 비저장 event 검증, 16 KB 메모리 페이지에 맞춰 정렬된 Android 라이브러리도 설명합니다. 애플리케이션은 이 소스 집합에서 생성된 바인딩과 네이티브 라이브러리를 함께 옮겨야 합니다. 계정 데이터베이스는 처음 열 때 스키마 98까지 마이그레이션되며, 데이터베이스 다운그레이드는 지원되지 않습니다. 기존의 간헐적인 따라잡기 결함 때문에 그룹 epoch 다섯 개보다 더 뒤처진 메시지가 알림 없이 복호화할 수 없는 상태로 남을 수 있으므로, 이 릴리스가 모든 경우에 완전한 기록 복구를 주장하지는 않습니다.

### Myco 0.8.0–0.8.1이 근처 앱에 자체 Nostr 스토어를 제공 {#myco-080081-gives-nearby-apps-their-own-nostr-store}

[Myco](https://github.com/Origami74/myco)는 napplet이라 불리는 작은 Nostr 프로그램을 오프라인 상태를 포함해 근처 휴대전화와 주고받는 Android 앱입니다. [버전 0.8.0](https://github.com/Origami74/myco/releases/tag/v0.8.0)은 각 설치에 게스트 Nostr 신원을 부여하고, 기존 키 또는 계정 키를 공유하지 않고 서명을 승인하는 Android signer인 Amber로 로그인할 수 있게 합니다. 또한 Discover 탭을 그 자체가 napplet인 앱 스토어로 대체합니다. 이 스토어는 서명된 앱 등록 정보와 추천을 읽으며, 다운로드한 업데이트는 인터넷 연결 없이도 사용자의 Circle 안에서 휴대전화 사이로 전달될 수 있습니다.

[버전 0.8.1](https://github.com/Origami74/myco/releases/tag/v0.8.1)은 작성자가 알리는 relay를 조회해 이러한 등록 정보를 더 쉽게 찾게 합니다. 이전 빌드는 공개 기본값에 의존했습니다. 캐시된 프로필과 앱을 즉시 보여 주고, 느린 relay 응답은 다음 방문을 위해 저장하며, 실패하는 relay에 대해서는 재시도 간격을 늘리고, 화면이 열려 있는 동안 구독을 유지합니다. 두 업데이트 모두 기존 휴대전화 간 유선 형식을 유지합니다. 업데이트된 휴대전화는 napplet 업데이트를 다운로드하고 공유할 수 있으며, 이전 휴대전화는 그 공지만 전달합니다.

## 태그된 릴리스 {#tagged-releases}

### White Noise Android가 그룹 투표와 계정별 사라지는 메시지 기본값을 추가 {#white-noise-android-adds-group-polls-and-account-specific-disappearing-message-defaults}

[White Noise Android](https://github.com/marmot-protocol/whitenoise-android)는 [Marmot](/ko/topics/marmot/)으로 암호화된 비공개 대화를 위한 Nostr 메신저입니다. [지난주에 다룬](/en/newsletters/2026-09-23-newsletter/#white-noise-android-2026921-improves-encrypted-chat-reliability-and-sharing) 전달 및 공유 개선에 이어, [9월 30일 릴리스](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30)는 Marmot Development Kit를 통해 선택 가능한 답변, 결과 막대, 마감 시한을 갖춘 그룹 투표를 추가합니다. 또한 [계정별 기기 로컬 사라지는 메시지 기본값](https://github.com/marmot-protocol/whitenoise-android/pull/2799)을 추가합니다. 새 다이렉트 대화와 그룹은 선택한 기간을 이어받지만, 기존 대화와 개별 설정은 현재 정책을 유지합니다. [Wave hi](https://github.com/marmot-protocol/whitenoise-android/pull/2765)는 현재 초안을 건드리지 않고 새로 추가된 멤버를 언급하는 인사를 보냅니다.

[이 릴리스](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30)는 사용자가 프로필 및 그룹 이미지의 초점 자르기 영역을 고르고, 대화를 삭제하지 않고 채팅 폴더를 삭제할 수 있게 합니다. [기록 알림](https://github.com/marmot-protocol/whitenoise-android/pull/2869)은 복구 후 계정이나 그룹 기록이 불완전할 가능성이 있을 때 이를 표시하며, 각각 별도로 닫을 수 있습니다. [대화 페이징](https://github.com/marmot-protocol/whitenoise-android/pull/2818)은 최근 메시지로 이동할 때 표시된 타임라인을 다시 만들지 않으며, [대기 중인 메시지 편집](https://github.com/marmot-protocol/whitenoise-android/pull/2825)은 원래 전송이 확인된 event ID를 얻는 동안 그 텍스트를 유지합니다. 이 편집 인계는 실행 중인 앱 안에서의 대화 변경을 다루며, 프로세스가 종료된 뒤에도 유지된다는 것을 입증하지는 않습니다.

[받아쓰기는 이제 녹음마다 붙여넣기 또는 보내기를 선택](https://github.com/marmot-protocol/whitenoise-android/pull/2768)하며, 자동 완료 시에는 녹취 텍스트를 초안에 넣습니다. [오프라인 제공자 설정](https://github.com/marmot-protocol/whitenoise-android/pull/2888)은 기기 내 처리를 설명하고, 그 동의를 다른 음성 제공자와 분리하며, 캡처가 끝난 뒤 중단된 미디어를 복원합니다. [일반 파일 처리](https://github.com/marmot-protocol/whitenoise-android/pull/2830)는 정확한 파일 이름, MIME 메타데이터, 실패 메시지와 함께 크기가 제한된 비어 있지 않은 문서를 받아들입니다. [명시적 첨부 파일 다운로드](https://github.com/marmot-protocol/whitenoise-android/pull/2879)는 Android의 사용자 시작 전송 작업을 사용하며 포그라운드 대체 경로를 둡니다. [붙여넣기 제어](https://github.com/marmot-protocol/whitenoise-android/pull/2877)는 이제 Android의 시스템 동작을 사용하므로 GrapheneOS Secure Paste가 클립보드 접근을 허용할 수 있습니다. Android는 또한 다운로드 정책을 존중하면서 [iOS의 GIPHY 공유를 애니메이션 미디어로 렌더링](https://github.com/marmot-protocol/whitenoise-android/pull/2806)합니다.

[알림 수정](https://github.com/marmot-protocol/whitenoise-android/pull/2808)은 발신자 닉네임을 새로 고치고 대화를 열면 알림을 정리합니다. [알림 복구 변경](https://github.com/marmot-protocol/whitenoise-android/pull/2712)은 포그라운드 소유권을 사용할 수 없는 동안에도 대기 중인 푸시 작업을 보존하고 횟수가 제한된 재시도를 사용합니다. [Amber 서명](https://github.com/marmot-protocol/whitenoise-android/pull/2802)은 같은 계정의 연속 승인 요청을 조율해 속도 제한 때문에 전송이 취소되지 않도록 합니다. [새 감사 설정](https://github.com/marmot-protocol/whitenoise-android/pull/2872)은 새 수신처에 업로드하기 전에 로그 공유 여부를 다시 묻습니다. 소스는 또한 [AGPL-3.0-only 라이선스를 채택](https://github.com/marmot-protocol/whitenoise-android/pull/2840)합니다.


### nostream 3.1.0이 relay 작업 증명을 부하에 맞춰 조정 {#nostream-310-adjusts-relay-proof-of-work-to-load}

[nostream](https://github.com/Cameri/nostream)은 PostgreSQL 기반의 TypeScript Nostr relay입니다. [버전 3.1.0](https://github.com/cameri/nostream/releases/tag/v3.1.0)은 관측된 event 비율이 변함에 따라 운영자가 정한 한도 안에서 event 작업 증명 기준을 높이거나 낮출 수 있습니다. 이 설정은 기본적으로 꺼져 있고, 각 워커의 측정된 비율을 사용하며, 기존의 정적 공개 키 기준과는 독립적으로 유지됩니다. 따라서 발신자가 다른 수락 요건을 보게 되기 전에 운영자가 먼저 이 기능을 켜야 합니다.

같은 [릴리스](https://github.com/Cameri/nostream/releases/tag/v3.1.0)는 relay, WebSocket, event 지표와 네트워크 상태 점검 결과, 설정 가능한 운영자 알림을 보여 주는 관리자 대시보드를 추가합니다. 관리자 API는 기본적으로 비활성화되어 있습니다. 이 제어 기능은 새 정책을 명시적 설정 아래 두면서 운영자가 relay 부하와 도달성 문제를 구별하도록 돕습니다.

부하 감응형 작업 증명 릴리스 이후, nostream은 [신뢰할 수 있는 모더레이터 신고에 대한 조치](https://github.com/cameri/nostream/pull/788)를 병합했습니다. [NIP-56](/ko/topics/nip-56/)은 콘텐츠 신고 event를 정의합니다. 새 `nip56.hideActionableReports` 옵션은 신고 기능도 활성화되어 있을 때 신고된 event를 REQ 및 COUNT 결과에서 제외합니다. event 신고는 해당 event를 숨기고, 공개 키 신고는 그 작성자의 모든 event를 숨깁니다. 새 옵션의 기본값은 false이므로, 신고 수집만 활성화하면 기존 조회 결과가 유지됩니다.

### Nostr double ratchet 0.0.171–0.0.172가 제거된 멤버 관련 공백을 막음 {#nostr-double-ratchet-0017100172-closes-a-removed-member-gap}

[Nostr double ratchet](https://github.com/irislib/nostr-double-ratchet)은 Nostr로 전달되는 암호화된 비공개 채팅을 위한 TypeScript 라이브러리입니다. [버전 0.0.171](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.171)은 멤버십 변경 후 그룹의 발신자 키를 교체해, 이전 키를 가진 채 제거된 사람이 업데이트된 발신자의 이후 메시지를 복호화할 수 없게 합니다. 그 발신자가 재시작한 후에도 마찬가지입니다. 또한 제거된 로컬 소유자의 전송이나 키 교체를 거부하고, 키 배포 중 멤버십이 바뀌면 전송을 중단합니다.

[버전 0.0.172](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.172)는 기존의 계정 서명 기기 승인을 선택적인 암호화 초대 응답에 담습니다. 업데이트를 사용하는 수신자는 별도의 등록 event가 도착하기 전에 발신자의 기기를 검증할 수 있으며, 연결된 기기는 재시작 후에도 승인을 유지합니다. 초대 필드는 선택 사항이며 원래의 핸드셰이크와 ratchet 메시지 형식을 그대로 둡니다.

[버전 0.0.173–0.0.175](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.175)는 지속성 있는 그룹 키 인계와 게시 전에 저장되는 대기열 전달 상태로 이 제거 작업을 확장해, 중단된 인계가 재시작 후 복구되도록 합니다. 게시 콜백은 로컬 그룹 컨텍스트를 전달하므로, 애플리케이션은 제거 후 지속성 있는 재시도를 취소하면서도 멤버십 제어는 전달 가능한 상태로 유지할 수 있습니다. 대기열의 전송은 원래의 내부 event ID를 보존합니다. 중복된 초대 응답은 이미 수립된 세션을 보존하고, 연락처가 바뀌어도 구독은 안정적으로 유지되며, 앱 키 스냅숏은 변경 가능한 사본을 공유하지 않고 기기 이름을 유지합니다. 서명된 유선 형식은 바뀌지 않으며, [0.0.173 노트](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.173)는 수신 세션 대체 경로와 로컬 그룹 에코 필터링을 갖춘 Rust 0.0.168도 보고합니다.

### Scramble 0.7.4–0.7.5가 새 그룹 멤버가 봐야 할 메시지를 가져옴 {#scramble-074075-fetches-the-messages-a-new-group-member-should-see}

[Scramble](https://github.com/DavidGershony/Scramble)은 네이티브 Android 인터페이스를 갖춘 크로스 플랫폼 Marmot 그룹 메신저입니다. [버전 0.7.5](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.5)에서는 각 그룹이 자체 relay 기록 기준점을 갖습니다. 이전에는 가장 활발한 대화의 기준점이 모든 그룹에 적용되어, 새로 가입한 그룹의 가입 이후 메시지가 한 번도 요청되지 않아 비어 있는 채로 남을 수 있었습니다. 재연결 경로에도 같은 수정이 적용되며, 로컬 활동이 없는 그룹은 이제 사용 가능한 모든 메시지를 요청합니다. MLS는 여전히 새 멤버가 가입 전에 보내진 메시지를 복호화하지 못하게 막습니다.

앞선 [0.7.4 릴리스](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.4)는 재활용된 Android 행에 클릭 핸들러가 누적되어 초대 수락이 반복되던 문제를 수정하고, 네이티브 앱에서 사용자 지정 Blossom 미디어 서버 설정이 유지되도록 합니다. 버전 0.7.5는 네이티브 Android APK만 제공하므로, 이전 Avalonia 파일 이름을 추적하던 사용자는 업데이트 대상을 바꿔야 합니다. 계정과 기록은 두 Android 빌드 사이에서 이동하지만, 이전 0.6.x MLS 엔진에서 만든 그룹은 0.7.x로 마이그레이션되지 않습니다.

[Scramble 0.7.6](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.6)은 그룹이 사용했던 모든 라우팅 주소를 조회하고, 시간 제한을 없애고, 오래된 저장 주소를 수리하고, 복구한 내용을 보고하는 수동 누락 메시지 가져오기 제어를 추가합니다. 여전히 사용자가 가입하기 전의 epoch는 복호화할 수 없습니다. 네이티브 관리자는 현재 멤버 명단 상태와 가시적인 실패 결과를 바탕으로 다른 멤버를 승격하거나 강등할 수 있으며, 2인 대화에서는 여전히 이 제어가 숨겨집니다. 그룹 정보의 복사 동작이 이제 반응하지만, 초대된 대화에서는 여전히 프로토콜 그룹 ID 대신 내부 채팅 식별자가 복사될 수 있습니다. [버전 0.7.7](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.7)은 또한 [다른 멤버의 커밋이 도착하면 보류된 메시지를 처리](https://github.com/DavidGershony/Scramble/commit/35e72177a0009ec96e8494caed7e9c250b66c7cb)하며, [0.7.8](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.8)은 그 수동적 멤버 경로에 대한 회귀 테스트를 추가합니다.

### Amber 6.6.6이 원격 signer 연결 비밀 값을 수리 {#amber-666-repairs-remote-signer-connection-secrets}

[Amber](https://github.com/greenart7c3/Amber)는 애플리케이션에 계정 키를 넘기지 않고 Nostr event 서명을 승인하는 Android signer입니다. 지난주의 백업 암호화 변경에 이어, [버전 6.6.6](https://github.com/greenart7c3/Amber/releases/tag/v6.6.6)은 `nostrconnect` 파서를 수정합니다. 패딩된 비밀 값처럼 `=`를 포함한 연결 매개변수가 Amber가 응답하기 전에 변형되었습니다. 그 결과 signer 연결이 다른 면에서는 유효해 보여도 NDK 기반 클라이언트가 비밀 값 검사에 실패했습니다.

[이 릴리스](https://github.com/greenart7c3/Amber/releases/tag/v6.6.6)는 또한 피드백 이슈를 Amber의 저장소 공지가 알리는 relay로 보내며, 공지를 가져올 수 없으면 이전 relay로 대체합니다. 더 긴 Tor 시간 제한은 느린 relay가 그 게시를 확인할 시간을 더 줍니다. 나머지 변경은 Amber 테마의 아이콘과 텍스트 가시성을 개선합니다.

### FIPS 0.5.2가 Nostr 탐색 과정의 개인정보 유출을 차단 {#fips-052-stops-a-nostr-discovery-privacy-leak}

[FIPS](https://github.com/jmcorgan/fips)는 Nostr 신원과 relay 메시지를 사용해 피어를 탐색하는 암호화 메시입니다. [0.5.2 유지보수 릴리스](https://github.com/jmcorgan/fips/releases/tag/v0.5.2)는 NAT 통과 삭제 요청에 노드의 라우팅 키로 서명하는 것을 중단합니다. 이 서명은 relay에서 그 키를 통과 트래픽과 연결했습니다. 또한 relay 연결에 쓰이는 TLS 라이브러리를 공개된 보안 권고를 수정한 버전으로 업데이트하고, 링크 및 세션 키 갱신에서 메시지가 유실되던 여러 경우를 수리합니다.

[릴리스 노트](https://github.com/jmcorgan/fips/releases/tag/v0.5.2)는 모든 플랫폼의 운영자에게 업그레이드를 요청하며, Windows 키 파일 권한, 게이트웨이, 패키지 서비스에 대한 별도 수정도 자세히 설명합니다. 임시 노드는 더 이상 이후 재시작 시 덮어쓸 수 있는 비공개 `fips.key`를 기록하지 않습니다. 안정적인 신원을 의도한 운영자는 업그레이드 전에 영구 모드를 설정해야 합니다. 이 릴리스는 메시 유선 형식을 바꾸지 않으므로, 버전이 섞인 노드를 개별적으로 업그레이드할 수 있습니다.

### napplet soyLI 0.23.1–0.23.4가 백엔드 게시와 signer 승인을 수리 {#napplet-soyli-02310234-repairs-backend-publishing-and-signer-approval}

[napplet.soy의 soyLI](https://github.com/zeSchlausKwab/napplet-soy)는 샌드박스에서 실행되는 작은 Nostr 프로그램을 위한 제작 및 게시 도구 모음입니다. 지난주의 공유 창작물 릴리스에 이어, [버전 0.23.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.1)은 백엔드 매니페스트, 핸들러, 스키마를 제작자 검사와 멀티플레이어 미리보기에 포함합니다. 이식 가능한 제공자 설정은 프로젝트 매니페스트에 두고, 비공개 신원 바인딩과 개발용 데이터베이스는 게시되는 소스 스냅숏 밖에 둡니다.

[버전 0.23.2](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.2)는 생성된 공개 백엔드 컨텍스트를 한때 커밋했던 프로젝트가 엄격한 검증을 거쳐 다시 게시할 수 있게 하면서도, 도달 가능한 기록 속의 비공개 바인딩, 저널, 데이터베이스, 자격 증명은 계속 거부합니다. 이후의 [0.23.4 릴리스](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.4)는 사용자가 서명하는 데 몇 초가 걸릴 때 유효한 확장 프로그램 또는 원격 signer 승인을 거부할 수 있던 영구 백엔드 세션 실패를 수정합니다. 공개 호스트에도 공유 호스트 수정이 필요하며, 제작자의 CLI만 업데이트해서는 배포된 호스트가 수리되지 않았습니다.

### Dart NDK 0.10.0이 Blossom 인증과 원격 서명의 범위를 지정 {#dart-ndk-0100-scopes-blossom-auth-and-remote-signing}

[Dart NDK](https://github.com/relaystr/ndk)는 Nostr relay 접근, 서명, 지갑 요청, 미디어 작업을 위한 Flutter 및 Dart 라이브러리입니다. 지난주의 프리릴리스에 이어, [0.10.0-dev.7](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.7)은 Blossom 미디어 요청이 서버가 거부할 때까지 익명으로 유지되고, 그 뒤에는 작업이 어떤 신원을 드러낼 수 있는지 지정하는 명시적 정책을 통해 인증하도록 변경합니다. 이 인증을 요청 경로 전체에 전달하고 이전의 `useAuth` 및 `customSigner` 옵션을 대체하며, 이는 프리릴리스 API를 사용하는 앱에 호환성을 깨는 통합 변경입니다.

[Dev.9](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.9)는 가장 느린 relay가 확인할 때까지 원격 signer 응답을 붙잡아 두지 않습니다. [Dev.8](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.8)은 백그라운드 relay 폴링과 캐시 작업을 줄이며, 다른 수정 사항은 지갑 시드 저장과 정산 기한에 관한 것입니다. [안정판 0.10.0 릴리스](https://github.com/relaystr/ndk/releases/tag/v0.10.0)는 이제 이 개발 계열을 아래의 연결 메타데이터 및 비공개 구독 ID 변경과 함께 묶어 제공합니다. [dev.9와의 비교](https://github.com/relaystr/ndk/compare/v0.10.0-dev.9...v0.10.0)에는 그 병합된 변경이 포함되어 있습니다. 업그레이드하는 애플리케이션은 미디어 인증 API 변경과 원격 signer 응답 경로를 모두 검토해야 합니다.

안정판 릴리스에는 [NIP-46 연결 메타데이터와 요청 권한](https://github.com/relaystr/ndk/pull/852)이 포함되어, 별도의 연결 필드를 `Nip46ClientMetadata` 값으로 대체합니다. 이는 로그인 위젯이 애플리케이션 신원과 요청 권한을 bunker에 전달할 수 있게 하는 소스 API 변경입니다. 또 다른 [요청 ID 변경](https://github.com/relaystr/ndk/pull/860)은 프로덕션에서 무작위 16진수 32자를 사용해, 사용 사례 이름과 페이지 단계가 relay에 보이는 구독 ID에 드러나지 않게 합니다. 명시적 ID는 여전히 NIP-01의 64자 제한 안에 머물며, 디버그 모드에서는 짧은 진단용 이름을 유지합니다.

### Mostro Core 0.16.0이 이전 gift-wrap 전송을 제거 {#mostro-core-0160-removes-the-old-gift-wrap-transport}

[Mostro Core](https://github.com/MostroP2P/mostro-core)는 Mostro의 Nostr 기반 P2P 거래 클라이언트와 코디네이터가 사용하는 메시지 프로토콜을 제공합니다. [버전 0.16.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.16.0)은 프로토콜 v1 gift-wrap 전송과 이전의 wrap 및 unwrap 함수를 제거해, 더 새로운 전송을 라이브러리 경로로 남깁니다. 이 라이브러리를 통해 여전히 v1 메시지를 구성하거나 읽는 애플리케이션에는 호환성을 깨는 변경입니다.

[라이브러리 릴리스](https://github.com/MostroP2P/mostro-core/releases/tag/v0.16.0)는 코디네이터의 [이제 공개된 0.19.0 릴리스](https://github.com/MostroP2P/mostro/releases/tag/v0.19.0)보다 먼저 나왔습니다. 이전 클라이언트를 지원하는 운영자는 전송 마이그레이션의 양쪽을 모두 업데이트해야 합니다. 앞선 [0.15.1 태그](https://github.com/MostroP2P/mostro-core/releases/tag/v0.15.1)는 협력적 취소 분쟁 상태를 추가하지만, 호환성 측면의 이정표는 전송 제거입니다.

### Cambium 0.6.0–0.7.1이 relay 메시지로 잠금 해제용 휴대전화를 등록 {#cambium-060071-enrolls-an-unlock-phone-through-relay-messages}

[Cambium](https://github.com/forgesworn/cambium)은 Heartwood 하드웨어 키를 위한 Android 서명 보조 앱으로, 재시작 후 보드의 잠금을 해제할 수도 있습니다. [버전 0.6.0](https://github.com/forgesworn/cambium/releases/tag/v0.6.0)은 USB 케이블 없이 보드의 Nostr relay를 통해 휴대전화를 잠금 해제용으로 등록할 수 있게 합니다. 사용자는 보드의 버튼을 누르기 전에 휴대전화, 보드, 그리고 보드의 등록 인터페이스인 Sapwood에서 다섯 개의 요청 단어를 비교합니다. 새로 공지된 relay에는 무작위 연결 지연이 적용되어, 휴대전화의 첫 접촉이 보드의 업데이트를 본 정확한 시점을 드러내지 않습니다.

[버전 0.7.0](https://github.com/forgesworn/cambium/releases/tag/v0.7.0)은 초대 흐름을 뒤집습니다. 휴대전화가 Sapwood의 수명이 짧은 QR 코드를 스캔하고, 일회용 키로 암호화된 일회성 event 하나를 돌려보냅니다. 어떤 relay도 수락하지 않으면 재시도 시 같은 event를 다시 게시하며, 이전 버전 Sapwood를 위해 기존의 코드 표시 경로도 남아 있습니다. [0.7.1 패치](https://github.com/forgesworn/cambium/releases/tag/v0.7.1)는 최종 확인 코드를 계속 보이게 하고 F-Droid 빌드 재현성을 개선합니다. QR 흐름에는 여전히 명시된 최신 Sapwood 및 Heartwood 버전이 필요합니다.

### Bray 3.5.0–3.5.2가 에이전트가 시작하는 Nostr 지갑 지출을 제한 {#bray-350352-limits-agent-initiated-nostr-wallet-spending}

[Bray](https://github.com/forgesworn/bray)는 AI 어시스턴트가 범위가 지정된 인터페이스를 통해 relay, 신원, 지갑 작업을 요청할 수 있게 하는 Nostr 도구 서버입니다. [3.5.0 릴리스](https://github.com/forgesworn/bray/releases/tag/v3.5.0)는 Nostr Wallet Connect 결제 한 건당 상한과 저장되는 일일 예산을 추가하며, 어시스턴트 호스트가 지원하는 경우 사람의 확인을 거칩니다. 별도의 지출 연결을 제공하려면 이제 명시적인 지갑 서비스 설정이 필요하며, 사용 전에 각 권한 부여를 다시 확인하고, 인보이스 조회를 해당 권한 부여 안의 해시로 한정합니다.

[이 릴리스](https://github.com/forgesworn/bray/releases/tag/v3.5.0)는 또한 사용자에게 지갑 연결 URI를 채팅에 붙여넣지 말고 비공개 파일에 보관하라고 안내하며, 실패가 입증된 것처럼 불확실한 결제를 재시도하지 않습니다. [버전 3.5.2](https://github.com/forgesworn/bray/releases/tag/v3.5.2)는 relay가 요청된 결제 수단 필터를 거부한 뒤 마켓플레이스 결제 수단을 로컬에서 대조합니다. 이러한 검사는 위임받은 어시스턴트가 지출할 수 있는 범위를 제한하고, relay 필터에 대한 가정 때문에 일치하는 제안이 가려지는 것을 막습니다.

### Mafrend 1.3.0-alpha가 비공개 지도 그룹을 최신 Marmot으로 이전 {#mafrend-130-alpha-moves-private-map-groups-to-current-marmot}

[Mafrend](https://github.com/DestBro/mafrend-zapstore)는 사람들이 장소를 탐색하고 목적지를 중심으로 채팅할 수 있게 하는 지도 기반 Nostr 소셜 앱입니다. [1.3.0-alpha 릴리스](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.3.0-alpha)는 비공개 그룹을 더 새로운 [Marmot 암호화 그룹](/ko/topics/marmot/) 명세로 업그레이드하고, 채팅과 리뷰에서 프로필 보기를 추가합니다. 그룹 형식은 이전 알파 채팅과 호환되지 않으므로, 사용자는 이를 호환성 단절이 있는 알파 마이그레이션으로 취급해야 합니다.

[같은 릴리스](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.3.0-alpha)는 지도 및 마커 개선과 함께 스크린숏 공유와 채팅 변경을 추가합니다. 프로필 기능은 프로젝트에서 여전히 진행 중으로 표시되어 있습니다. 의미 있는 Nostr 변경은 비공개 그룹 상호 운용성의 전환이며, 이전 테스트 그룹을 가진 사용자는 업그레이드 전에 호환성 안내를 확인해야 합니다.

### Sonar alpha.15–alpha.15.1이 암호화 그룹 게시를 수리 {#sonar-alpha15alpha151-repairs-encrypted-group-publishing}

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar)는 Bluetooth 메시와 Nostr로 대화를 전달할 수 있는 비공개 메신저입니다. [Alpha.15](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15)는 메시지에 대한 이모지 반응과 암호화된 채팅 안에서의 비공개 현지 시각 공유를 추가하며, 그 공유를 철회하는 설정도 제공합니다. 지갑은 Cashu로 전환되지만, 그 결제 변경은 메시징 업데이트와 별개입니다.

[Alpha.15.1](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15.1)은 이전 브랜치 빌드가 다른 스키마 버전을 기록한 뒤 대화 색인이 비어 버릴 수 있던 실행 실패를 수리합니다. 색인이 없으면 앱은 다시 열 때마다 현지 시각 공유를 다시 암호화해 모든 그룹에 재게시했으며, 때로는 relay 속도 제한이 개입하기 전까지 수백 개의 event를 보냈습니다. 이 핫픽스는 해당 로컬 상태를 다시 구축하고 반복되는 그룹 게시를 멈춥니다.

### Elisym의 커머스 패키지가 비공개 Nostr 주문을 도입 {#elisyms-commerce-packages-introduce-private-nostr-orders}

[Elisym](https://github.com/elisymlabs/elisym)은 현재 서명된 event 기반 커머스 흐름을 구축하고 있는 Nostr 기반 에이전트 도구 모음입니다. [병합된 `commerce` 패키지](https://github.com/elisymlabs/elisym/pull/120)는 결제 및 판매자 구성 요소를 위한 스토어 상품, 소유자 권한 부여, 비공개로 감싼 주문과 영수증, 제안 검증을 정의합니다. 이후의 [commerce 0.2.0 태그](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0)는 주문에서 해당 주문의 결제 참조를 도출해, 결제 조회를 서명된 구매 흐름에 묶습니다.

패키지 계열은 별도의 결제 코어 및 브라우저 결제 작업도 도입하지만, [릴리스 태그](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0)가 완전한 판매자 결제 기능이 배포되었음을 입증하지는 않습니다. 스토어 권한 부여 event kind는 프로젝트의 1차 자료에서 명시적으로 임시로 표시되어 있습니다. SDK, MCP, CLI, 결제 코어의 열한 개 태그는 하나의 개발 중인 커머스 기능을 나타냅니다.

[Elisym의 새 패키지 릴리스](https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmerchant-node%400.1.0)는 자체 호스팅 판매자 노드를 패키지로 묶으며, [MCP 0.31.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmcp%400.31.0)은 커머스 상품을 위한 `buy_product`와 `get_order`를 추가합니다. 이후의 commerce 및 merchant-node 릴리스는 같은 결제 흐름 안에 Tempo 결제 지원을 추가합니다. 이 패키지들은 기존의 서명된 상품 및 비공개 주문 통합을 진전시키지만, 태그 목록이 임시 event 스키마를 표준으로 만들거나 완전한 호스팅 서비스 출시를 입증하지는 않습니다.

### Flotilla 1.11.2가 멈춘 signer와 불완전한 relay 피드를 해결 {#flotilla-1112-unsticks-signers-and-incomplete-relay-feeds}

[Flotilla](https://github.com/coracle-social/flotilla)는 대화, 방, 공유 공간을 위한 Nostr 클라이언트입니다. [버전 1.11.2](https://github.com/coracle-social/flotilla/releases/tag/1.11.2)는 시작 과정이 원격 signer를 기다리며 멈췄을 때 사용자에게 빠져나갈 방법을 제공하고, 로컬 애플리케이션 데이터가 지워진 세션은 로그아웃시킵니다. 이제 방은 더 큰 공간의 동기화가 끝나기 전에도 메시지를 표시할 수 있으며, 피드는 어떤 relay가 다른 relay보다 늦게 응답했다는 이유만으로 게시물을 빠뜨리지 않습니다.

[같은 릴리스](https://github.com/coracle-social/flotilla/releases/tag/1.11.2)는 앱의 기존 키로 서명한 F-Droid 빌드를 게시하고 Obtainium을 위해 GitHub 릴리스를 최신 상태로 유지합니다. 이 배포 작업은 업데이트 채널을 바꾸는 사용자에게 중요하지만, 당장 업그레이드할 이유는 relay와 signer 수정입니다.

### Ditto 2.42.3이 relay 전달 상태를 보여 주고 계정 경계를 강화 {#ditto-2423-shows-relay-delivery-and-tightens-account-boundaries}

[Ditto](https://gitlab.com/soapbox-pub/ditto)는 사용자가 relay를 선택하고 인증할 수 있게 하는 Nostr 소셜 클라이언트입니다. [버전 2.42.3](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.42.3)에서는 게시물의 Event Details에 사용자 relay와 작성자 relay 중 어디에 그 게시물이 있는지 표시되며, Broadcast는 누락된 relay만 대상으로 합니다. 이 릴리스는 응답하지 않는 읽기 relay도 알려 주고 재시도 제어를 제공해, 게시물을 다시 모든 곳에 보내지 않고도 누락된 게시물을 진단하기 쉽게 합니다.

[릴리스 노트](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.42.3)에 따르면 계정을 전환해도 더 이상 이전 계정의 relay로 게시물이 전송되지 않고, 음소거된 사용자는 일반 휴대전화 알림을 발생시킬 수 없으며, 게시물 속 링크나 이미지가 독자의 로컬 네트워크에 있는 기기에 접근할 수 없습니다. 느린 relay의 게시물이 Follows 및 Loved 피드에서 사라지지 않으며, 라이브 스트림 채팅과 webxdc 게임은 전체 화면을 반복해서 다운로드하지 않고 업데이트됩니다. 토렌트와 오디오 탐색도 새로 추가되었지만, Nostr에 가장 넓은 영향을 주는 변경은 relay 라우팅과 계정 격리입니다.

### Iris Chat 2026.9.24.4가 암호화된 대화에 통화를 도입 {#iris-chat-20269244-brings-calls-into-encrypted-conversations}

[Iris Chat](https://github.com/irislib/iris-chat-rs)은 double-ratchet 계열의 채팅 프로토콜을 사용하는 종단 간 암호화 Nostr 메신저입니다. [9월 24일 릴리스](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.4)는 호환되는 연락처와의 음성 및 영상 통화를 추가하며, 인터넷을 쓸 수 없을 때 기존 로컬 연결을 통한 통화도 포함됩니다. 사용자는 영상 품질을 낮추거나, 영상 통화를 음성으로 받거나, Android의 통화 인터페이스로 수신 통화를 처리할 수 있습니다. 통화를 받거나 거절하면 연결된 다른 기기의 벨소리도 멈춥니다.

[이 릴리스](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.4)는 별도의 서명 앱으로 로그인하고 연결된 기기 중 어떤 기기가 접속해 있는지 볼 수 있게 합니다. 이후의 [9월 24일 패치](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.5)는 지연된 메시지의 원래 타임스탬프를 유지하고, 재연결 패킷이 유실된 뒤의 근거리 전달을 개선합니다. 이는 초기 단계의 기기 간 동작과 통화 동작이므로, 호환되는 Iris 빌드를 실행할 수 있는 연락처에게 가장 유용합니다.

이후 개발자가 서명한 [9월 30일 업데이트](https://primal.net/e/17fd3f325dda1feb0c1e51c6e1af0f7b3efe42ecff75e9527ac435cdc6a30c7a)는 제거된 멤버의 로컬 그룹 기록을 보존하면서 전송을 비활성화하고, 연결된 기기 간 및 대규모 그룹의 전달을 개선하며, 읽음 표시와 읽지 않은 메시지 수를 수리합니다. 통화에는 오디오 장치 선택과 발신 신호음 복원이 추가되며, 오래된 마이크 상태가 더 이상 수신 오디오를 무음으로 만들지 않습니다. 시간 지정 음소거, 이미지 복사, 끌어다 놓은 파일 첨부, 알림 라우팅, 푸시 등록이 수정되며, 로그아웃 시 로컬 캐시가 지워지고 기기를 제거하면 그 세션이 종료됩니다. [두 번째 업데이트](https://primal.net/e/89ec93e25caf31831714e807c927b6d50d3d5fc38044df845163ff656db3f711)는 같은 기기의 다른 Iris 앱이 캐시한 파일에 대한 접근을 개선하고, Nearby가 꺼져 있어도 로컬 파일 공유를 계속 사용할 수 있게 합니다.

### LibreNostr 0.6.0–0.7.0이 내장 Tor로 relay 연결을 라우팅 {#librenostr-060070-routes-relays-through-built-in-tor}

[LibreNostr](https://github.com/Lwb89dev/librenostr)는 relay와 개인정보 설정을 구성할 수 있는 Android Nostr 클라이언트입니다. [버전 0.6.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.0)은 ARM64에 Arti 기반 Tor 엔진을 내장하고, 선택한 Direct, 모두 Tor 사용, 또는 `.onion` 전용 모드를 relay WebSocket, HTTP 요청, 미디어, 업로드, 웹 페이지에 적용합니다. 엄격한 Tor 모드는 Tor를 사용할 수 없으면 차단 상태로 실패하며 요청을 조용히 직접 보내지 않습니다. 모드를 바꾸면 relay 소켓이 새 경로로 다시 연결됩니다.

[버전 0.6.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.2)는 공개 팔로우 목록으로 구성한 기기 내 web-of-trust 필터를 추가하고, 추가로 도달할 수 있는 팔로우 대상 수를 기준으로 보조 relay를 선택합니다. 이어서 [버전 0.7.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.7.0)은 프로필 및 개수 조회가 끝나기 전에 노트와 알림을 보여 주고, 느린 relay 조회에 상한을 두며, 대화를 열 때마다 DM 받은편지함 전체를 복호화하는 것을 멈춥니다. 이 릴리스들은 함께 클라이언트가 연결할 수 있는 곳과 느린 relay가 인터페이스를 붙잡아 둘 수 있는 시간을 모두 바꿉니다.

개발자가 서명한 [첫 안정판 릴리스 1.0.0](https://primal.net/e/4eeba660b6b789288954290497de89fe3222bfc955214647ead5d63e6031d927)은 피드, 해시태그, 프로필, 장문 읽기, 알림, 메시지를 위한 이동 가능한 열을 갖춘, 프로필별로 저장되는 태블릿 덱을 추가합니다. 가로 방향 태블릿에서는 이 레이아웃을 사용하고, 휴대전화는 기존 인터페이스를 유지합니다. 검색에는 OR, 제외, 미디어 필터, 제대로 작동하는 날짜 범위가 추가되며, relay의 정밀 결과보다 먼저 캐시된 프로필을 반환하고, 거부된 전문 검색 요청은 즉시 건너뜁니다. 해시태그는 시간순으로 정렬되고, 페이징은 충분한 relay 응답을 기다리며, 사용하지 않는 피드는 구독을 해제합니다.

[같은 릴리스](https://primal.net/e/4eeba660b6b789288954290497de89fe3222bfc955214647ead5d63e6031d927)는 편집 중에 기존의 공개 및 암호화된 음소거 목록과 북마크 항목을 하나의 변경으로 대체하지 않고 보존합니다. 계정 간 북마크와 알림을 격리하고, 보조 작성자 relay를 공개 읽기로 제한해 비공개 요청과 relay 인증이 그 relay로 가지 않게 합니다. 또한 오래된 프로필 응답이 더 새로운 메타데이터를 대체하지 못하게 하고, 알림 페이징과 배지를 수리하며, 새 항목이 도착해도 이전 피드 항목을 유지하고, 답장 실행 취소 카운트다운, 중복 게시, 쿼리 문자열이 있는 미디어 URL, 채팅을 읽음으로 표시한 뒤의 읽지 않은 수를 수정합니다. [버전 1.0.1](https://primal.net/e/630becb73dbe7ba7c76a2d1970f1d7262a5afc33b02fc8002bef611cf638deab)은 새 레이아웃에서 태블릿 덱 시작 시 발생하던 충돌을 수정합니다.

### Newlay 0.3.45가 대형 relay 조회를 닫지 않고 스트리밍 {#newlay-0345-streams-large-relay-queries-instead-of-closing-them}

[Newlay](https://code.relay.tools/opensauce/newlay)는 Android에서 호스팅되는 Nostr relay이자 관련 로컬 서비스입니다. [서명된 0.3.45 릴리스 공지](https://primal.net/e/b8380ae1bf30492129727ec59e27e2ae8a4cf9ad08e7361826a9ba8be88a227a)에 따르면 대형 조회 결과는 이제 클라이언트 연결을 닫는 대신 배압을 적용해 스트리밍됩니다. 내장 Git 호스트는 푸시 후 대체된 팩을 정리하며, Cordn 암호화 메시징 코디네이터는 크기가 큰 클라이언트 요청을 받아들이고 탐침 요청이 시간 초과되면 중단 프레임을 보냅니다.

[이 릴리스](https://primal.net/e/b8380ae1bf30492129727ec59e27e2ae8a4cf9ad08e7361826a9ba8be88a227a)는 Android 운영자에게 event, 저장소, 주소, 관리에 대한 실시간 상태 카드도 제공하며, 16 KB 메모리 페이지를 쓰는 기기에 맞춰 네이티브 암호화 라이브러리를 정렬합니다. relay와 코디네이터 변경은 이전 스토어 버전인 0.3.39 이후 여러 릴리스에 걸쳐 있으며, 0.3.45는 이를 패키지로 묶은 체크포인트입니다.

### ngit-grasp 3.0.5가 Git 푸시와 relay 동기화를 계속 진행시킴 {#ngit-grasp-305-keeps-git-pushes-and-relay-sync-moving}

[ngit-grasp](https://gitworkshop.dev/danconwaydev.com/ngit-grasp)는 서명된 저장소 협업을 위한 자체 호스팅 Nostr relay이자 Git 서버입니다. [서명된 3.0.5 릴리스 공지](https://primal.net/e/6ff00b9230e4523e6f14aaf6e5088f91e5696be38b9304a4e1cef384e3318d41)에 따르면 느린 기록 조정 작업이 공유 실시간 동기화 액터에서 분리되어, 이전 event를 확인하는 동안에도 relay 구독이 시작될 수 있습니다. 속도 제한, 불완전한 기록 조회, 메일함 읽기, 신원 조회에 대해 각각 따로 재시도 간격을 늘리므로, 문제가 있는 relay 하나가 더 이상 재시도 용량을 독점하지 않습니다.

[같은 릴리스](https://primal.net/e/6ff00b9230e4523e6f14aaf6e5088f91e5696be38b9304a4e1cef384e3318d41)는 로컬 event 목록과 대조해 이미 저장된 기록을 다시 가져오지 않으며, 불완전한 구독은 그 범위를 검증된 것으로 취급하기 전에 닫습니다. Git 측면에서는 백그라운드 상태 승격이 이미 적용한 푸시를 수락하고, 변경된 ref에 대한 충돌 보호를 유지하며, 업로드 중 Git 진행 출력을 비워 푸시가 멈추지 않게 합니다. 저장소가 relay에서는 살아 있는 것처럼 보이는데 Git 전송은 여전히 확정적인 결과를 기다리고 있을 수 있으므로 이러한 세부 사항이 중요합니다.

### Armada 0.63.0이 signer 유형에 관계없이 푸시 알림을 전달 {#armada-0630-carries-push-alerts-across-signer-types}

[Armada](https://github.com/soapbox-pub/armada)는 암호화된 커뮤니티, 채널, 다이렉트 메시지를 위한 Nostr 클라이언트입니다. 지난주의 미디어 개인정보 릴리스에 이어, [서명된 0.63.0 공지](https://primal.net/e/34021b55504d74c5d04f55dbfea87f31168a7c4582f35113d7ec063894d19e56)는 다른 계정 유형뿐 아니라 확장 프로그램 및 원격 signer 로그인에서도 앱이 닫혀 있는 동안 작동하는 새 브라우저 푸시 경로를 설명합니다. Armada를 내장한 호스트 앱인 Tenna의 사용자도 백그라운드 알림을 받게 됩니다.

[이 릴리스](https://primal.net/e/34021b55504d74c5d04f55dbfea87f31168a7c4582f35113d7ec063894d19e56)는 긴 커뮤니티 채널에서 이전 메시지를 더 빠르게 불러오며, 새 메시지를 위해 전체 기록을 다시 읽지 않습니다. 다이렉트 메시지 입력 중 표시는 더 적은 relay 연결을 사용합니다. 데스크톱 업데이트에는 재시작 안내가 추가되며, 0.50.0보다 오래된 버전에서의 직접 업그레이드는 더 이상 지원되지 않습니다.

서명된 [0.63.1 후속 릴리스](https://primal.net/e/af3ff711c1c1daa4d6a621dc5add0615fc5d37fbb1de31395cb79dcdf820aaf1)는 폴더 가져오기와 순서 변경이 가능한 편집 가능 이모지 팩을 추가하고, 불러온 기록 밖의 인용 메시지를 가져오며, relay에서 호스팅되는 답장을 상호 운용 가능하게 만듭니다. Android 재연결 트래픽을 줄이고, 긴 연결 끊김 후에도 이전 알림을 반복하지 않고 따라잡으며, 가입 전 멘션을 제외하고, 편집하지 않은 그룹 필드와 비공개 서버 목록 항목을 보존합니다. relay에서 호스팅되는 그룹의 삭제에는 이제 메시지 작성자나 관리자가 필요합니다. 서버 끌어 옮기기, 잘못된 relay 정보 처리, 저장소 구독도 수정됩니다.

[버전 0.63.2](https://primal.net/e/ad0f6ad1a7730a400e8257c494c53ef14597c55a24e01b05dd2b2301c7d3aa36)는 메시지 Markdown을 중첩 인용과 목록, 가로줄, 코드 펜스, 밑줄형 제목, 링크나 멘션에 걸친 서식까지 확장합니다. Tenor와 Giphy 페이지 링크는 GIF로 재생됩니다. 읽음 상태 동기화는 더 적은 데이터를 전송하고, 재연결은 불필요한 다운로드와 로그인을 피하며, Android 백그라운드 알림은 대규모 설정 업데이트가 몰려들 때 relay 동기화를 일시 중지합니다.

### deed 0.3.0–0.3.2가 Zig Nostr 게시를 더 안정적으로 만듦 {#deed-030032-makes-zig-nostr-publishing-steadier}

[deed](https://github.com/zig-nostr/deed)는 Nostr event를 읽고 게시하기 위한 Zig 명령줄 도구입니다. [9월 24일 버전 0.3.2](https://github.com/zig-nostr/deed/releases/tag/v0.3.2)는 에이전트 스킬을 추가하고 relay ping 기한을 수정합니다. 앞선 [0.3.1](https://github.com/zig-nostr/deed/releases/tag/v0.3.1) 및 [0.3.0](https://github.com/zig-nostr/deed/releases/tag/v0.3.0) 릴리스는 성능과 게시 안정성을 개선합니다. 세 태그는 하나의 초기 도구 계열을 이룹니다. 눈에 보이는 Nostr상의 이점은 이 CLI를 사용하는 스크립트를 위한 더 안정적인 relay 연결과 event 게시 경로입니다.

### Cordn 0.5.1이 코디네이터가 실패해도 다른 그룹을 계속 움직이게 함 {#cordn-051-keeps-other-groups-moving-when-a-coordinator-fails}

[Cordn](https://github.com/Cordn-msg/cordn)은 Nostr 신원과 relay를 사용해 대화 코디네이터를 찾는 MLS 암호화 그룹 메신저입니다. [서명된 0.5.1 클라이언트 릴리스](https://primal.net/e/23f7498e2e405e05c4d3075ccc522c753d80f37b954a81ff8ecb3268f2dc7dc6)는 지난주의 오프라인 대기열 작업에 이어 코디네이터와 outbox 스케줄링을 분리합니다. 사용할 수 없는 코디네이터가 더 이상 관련 없는 그룹의 전송을 지연시키지 않습니다. 확인된 relay 힌트는 탐색 후에도 유지되고, 그룹 문서가 이를 기기 간에 전달하며, 지속성 있는 대기 중 게시 기록이 멈춘 전송을 복구합니다. 다중 기기 복구는 현재 설정을 읽는 동안 기록 체인 조회와 공백 조회를 병행합니다.

[이 릴리스](https://primal.net/e/23f7498e2e405e05c4d3075ccc522c753d80f37b954a81ff8ecb3268f2dc7dc6)는 끌어다 놓은 파일 첨부, 고정된 그룹, 미리보기와 알림의 프로필 이름, 코디네이터 레이블도 추가합니다. 첫 번째 읽지 않은 메시지 위치 지정, 읽지 않은 수 카운터, 중복 알림, 미디어 및 시스템 메시지 미리보기, 캡션이 있는 미디어에 붙은 답장, 이미지 확대 제어를 수리합니다. 네이티브 다운로드는 다른 이름으로 저장 선택기를 사용합니다. 늦게 나타나는 signer 때문에 더 이상 지원되지 않는 암호화라는 잘못된 경고가 뜨지 않으며, 계정 전환이 더 이상 백그라운드 초기 데이터 채우기와 경합하지 않습니다.

### Nymbot 1.0.7이 로컬 문서 처리와 암호화된 채팅 공유를 추가 {#nymbot-107-adds-local-document-handling-and-encrypted-chat-sharing}

[Nymbot](https://zapstore.dev/apps/ai.nymbot)은 암호화된 gift-wrap Nostr 메시지로 접근하는 어시스턴트입니다. [개발자가 서명한 1.0.7 릴리스](https://primal.net/e/affd11e97fb3438965780aa01732e8d0e0f9b2162b87ab0f3019dff93449673e)는 기기에서 문서를 읽고, 파일이 너무 커서 통째로 보낼 수 없을 때 관련 구절을 골라내며, 사용한 페이지를 표시합니다. 대화는 나중에 접근 권한을 철회할 수 있는 종단 간 암호화 링크로 공유할 수 있습니다. Python 및 JavaScript 답변은 로컬에서 실행할 수 있으며, 그 출력은 대화로 돌아옵니다.

[같은 릴리스](https://primal.net/e/affd11e97fb3438965780aa01732e8d0e0f9b2162b87ab0f3019dff93449673e)는 제출 전에 가격을 보여 주는 출처 기반 리서치, 이미지 편집, 메시지별 모델 선택, 채팅 및 봇별 지출 상한을 추가합니다. MCP로 연결된 외부 도구는 데이터를 변경하기 전에 확인을 요청합니다. 저장소 실행은 검토를 위해 변경을 일시 중지하고, CI 결과를 표시하며, 바쁜 게이트웨이 이후에 재개할 수 있습니다. 추천 답변, 고정된 공지, 접힌 출처 목록, 검색 가능한 모델 선택기가 업데이트를 마무리합니다. 이러한 내용은 개발자 릴리스 노트에서 나온 것이며, Compass는 앱의 개인정보 보호를 독립적으로 감사하지 않았습니다.

### 0xchat 1.5.6이 서명 및 메시지 인증 수정을 출시 {#0xchat-156-ships-its-signing-and-message-authentication-fixes}

[0xchat](https://github.com/0xchat-app/0xchat-app-main)은 비공개 채팅, 외부 서명, 지갑 기능을 갖춘 Nostr 메신저입니다. [버전 1.5.6](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.6-release)은 [지난주 소스 병합으로 다룬](/en/newsletters/2026-09-23-newsletter/#0xchat-merges-fixes-for-signing-message-authentication-and-redirect-flaws) 보안 수정을 출시하며, 여기에는 gift-wrap 인증, 신뢰할 수 있는 인프라 설정, 내장 페이지 서명에 대한 동의가 포함됩니다. 또한 Tor 프록시 우회 경로를 막고, onion이 아닌 호스트의 TLS 인증서를 검증하며, 릴리스 빌드가 잠재적으로 민감한 자격 증명과 지갑 자료를 기기 콘솔에 기록하지 않도록 합니다. 사용자가 선택한 개발자 로그는 계속 오류를 기록합니다.

[이 릴리스](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.6-release)는 relay 재연결 간격을 3초에서 5분까지 늘리고, 재연결 후 구독을 수리하며, relay가 연결 중일 때 대기열에 들어간 요청을 전달합니다. 계정 전환 시 중복된 relay 리스너가 더 이상 누적되지 않고, 로그인이 실패해도 이미 활성화된 계정이 유지되며, 외부 signer 연결이 실행 간에 유지됩니다. 실패한 전송은 이제 오류를 표시하고 보내지 못한 텍스트나 복구 가능한 토큰 공유 상태를 보존합니다. 시작 시 키 복호화와 업로드 해싱은 UI 스레드 밖에서 수행되며, 채팅 및 동영상 캐시는 반복 렌더링과 다운로드를 피합니다. 이 릴리스는 Play 서명 Android APK와 소스에서 빌드한 Windows 설치 프로그램을 포함해 SHA-256 체크섬이 있는 Android 및 데스크톱 자산을 제공합니다.

### Nostr Mail Client 0.17.0이 메일함 동작을 relay로부터 숨김 {#nostr-mail-client-0170-hides-mailbox-actions-from-relays}

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client)는 기존 이메일 전달을 지원하면서 Nostr를 통해 이메일을 주고받습니다. [지난주의 수신자별 전송 및 미디어 개인정보 릴리스](/en/newsletters/2026-09-23-newsletter/#nostr-mail-client-0160-adds-per-recipient-delivery-choices)에 이어, [버전 0.17.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0)은 읽음, 보관, 폴더, 레이블 상태와 그 시점을 relay로부터 숨기고, 발신자에게 알리지 않고 메일을 삭제할 수 있게 합니다. 이전 클라이언트는 새 상태나 삭제를 볼 수 없으므로 이 릴리스는 모든 기기를 함께 업데이트해야 합니다. 또한 32 KB보다 큰 메일에서 Bcc 수신자를 보호하고, 로컬 연락처 별칭이 발신 메시지에 들어가지 않게 하며, Amber QR 로그인을 수리하고, 공개 메일을 수신자의 읽기 relay에 게시합니다.

[이 릴리스](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0)는 발신자, 제목, 첨부 파일 규칙을 갖춘 색상 폴더와 레이블, 답장 및 전달 인용, 붙여넣은 인라인 이미지, 첨부 파일 미리보기와 이름 변경, 메일 목록의 범위 선택을 추가합니다. 전달 시 원본 이미지와 첨부 파일이 유지되고, 답장 인용은 접힌 상태로 시작하며, 웹 편집기에는 컨텍스트 메뉴가 추가됩니다. HTML 표와 인라인 이미지가 더 정확하게 렌더링되고, 일반 텍스트 링크가 작동하며, 예약 발송은 최대 5년 후의 날짜까지 지원합니다. 주소록의 이름과 사진이 인터페이스 전반에 표시되며, 테마 색상은 시스템, 추천, 사용자 지정 팔레트를 제공합니다.

같은 [릴리스](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0)는 파일에서 선택한 배경을 로컬에 두고 링크된 배경을 캐시하는데, 여기에는 명시적인 마이그레이션 비용이 따릅니다. 네이티브 플랫폼의 이전 파일 배경은 다시 추가해야 합니다. 기본 relay/미디어 추천을 변경하고, 온보딩과 업데이트 공지 중에 Nostr 앱 탐색을 추가하며, 다른 클라이언트가 기록한 낯선 설정을 보존하고, 중단된 메일 저장소 생성과 Linux 패키징을 수리합니다. 시작 실패 시 이제 빈 화면 대신 세부 정보와 미리 채워진 보고서가 표시됩니다.

### Nostr WoT 0.8.7이 인증을 목적지에 묶음 {#nostr-wot-087-binds-authentication-to-the-destination}

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension)는 Nostr 서명과 신뢰 도구를 결합한 브라우저 확장 프로그램입니다. [버전 0.8.7](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7)은 [NIP-98](/ko/topics/nip-98/) 서명 HTTP 인증에 대해 정확한 URL, 쿼리, 메서드, 계정, 요청 출처를 기준으로 동의를 요구합니다. 이전의 포괄적 승인은 새로 동의를 받아야 합니다. [NIP-42](/ko/topics/nip-42/) relay 인증은 계정에 묶인 별도의 권한 체계를 가지며, 사이트별 거부가 공유된 relay 허용보다 우선합니다. 인증 요청은 검증된 최상위 브라우저 출처에서 와야 하며, 승인이나 잠금 해제를 기다리는 동안에는 계정 및 접근 확인이 다시 실행됩니다.

[이 릴리스](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7)는 원격 [NIP-46](/ko/topics/nip-46/) 서명과 승인된 event 전체를 검증해, 반환된 서명이 내용이나 목적지를 몰래 바꿔치기할 수 없게 합니다. 지갑 프로비저닝과 주소 변경에는 본문에 묶인 인증, 일회용 백엔드 챌린지, 별도의 트랜잭션 토큰이 사용되며, 일반 웹사이트 서명으로는 그러한 내부 지갑 토큰을 발급할 수 없습니다. 호환되는 백엔드가 먼저 배포되어야 하며, 클라이언트는 폐기된 엔드포인트로의 다운그레이드를 거부합니다. Nostr Wallet Connect 결제도 반환된 결제 프리이미지를 요청한 인보이스 해시와 대조해 검증하며, 불일치는 결과를 알 수 없는 것으로 취급합니다.

[요청 인터페이스](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7)에서 사용자는 원시 event 전체를 검사하고, 사이트 그룹에서 특정 요청을 고르고, 웹사이트로의 반환을 승인하지 않고도 비공개 메시지를 로컬에서 볼 수 있습니다. 로컬 미리보기는 30초 후 스스로 가려집니다. 들어오는 요청은 선택되지 않은 상태로 남고, 일반 일괄 승인에서는 인증이 제외됩니다. 이 확장 프로그램은 사이트별 relay 권한과 모든 사이트 relay 권한을 분리하고, 검증된 프로필 캐시에 한도를 두며, 타임스탬프가 같은 replaceable event는 더 낮은 event ID를 기준으로 결정하고, 홈 팝업 게시물 읽기를 로컬에 둡니다. Chrome과 Firefox는 각각 따로 검증된 패키지와 순차적인 안정판 제출 워크플로를 받습니다. 그 워크플로가 현재 스토어에서 사용 가능함을 입증하지는 않습니다.

### Iris의 공유 런타임이 relay와 피어 기록을 일관되게 유지 {#iriss-shared-runtime-keeps-relay-and-peer-history-consistent}

[nostr-pubsub](https://github.com/mmalmi/nostr-pubsub)는 영구 event 저장소와 발신 게시 대기열을 갖춘 공유 Nostr event 런타임을 제공합니다. [버전 0.5.7–0.5.13](https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13)은 정확한 구독을 일괄 처리하고, 재연결 후 다시 실행하며, 로컬, relay, 피어 증거를 구별해 유지하고, 지속성 저장소가 실패하면 불완전한 기록을 보고합니다. 완료된 조회는 수신된 모든 event의 수락 처리가 끝날 때까지 기다립니다. 기본 relay 일괄 처리에는 일반적인 서버와의 호환성을 위해 이제 최대 20개의 OR 필터가 들어가며, 피어 일괄 처리는 독립적인 매칭과 취소를 유지합니다.

[Hashtree의 런타임 업데이트](https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13)는 워커 전용 네트워킹을 그 공유 런타임, 영구 event 색인, 발신 대기열로 대체해 event와 캐시된 파일이 하나의 FIPS 노드를 공유할 수 있게 합니다. [FIPS TypeScript 0.0.44–0.0.45](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.45)는 완전한 시그널링 레코드를 담을 만큼 용량이 충분한 경로를 선택하고, 핸드셰이크 기한 안에 유실된 세션 설정을 복구하며, 명시적인 라우팅 거부 후에만 WebRTC 응답을 재시도합니다. 더 큰 프레임 WebSocket 경로에는 호환되는 네이티브 피어가 필요하며, 0.0.44 노트는 네이티브 FIPS 0.4.85를 먼저 배포하도록 요구합니다.

[Iris Kit 0.2.5](https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.5)는 계정 키와 오프라인 읽기를 보존하면서 영구적인 일반 event 애플리케이션 클라이언트와 전송 방식에 중립적인 [NIP-46](/ko/topics/nip-46/) 서명을 추가합니다. [버전 0.2.6](https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.6)은 이미 검증된 완전한 event ID를 워커나 네이티브 백엔드에서 즉시 반환하며, 접두사 조회와 replaceable event 조회는 여전히 최신 값을 고르기 전에 기록을 기다립니다. 이는 라이브러리 릴리스이며, 노트가 모든 Iris 애플리케이션에 배포되었음을 입증하지는 않습니다.

[Iris Meet의 9월 30일 소스 업데이트](https://github.com/irislib/meet/commit/9bebb074895fd34574c3a92056612cf3891de74b)는 NDK 통합을 영구 게시/구독 인프라와 공유 신원 signer로 대체합니다. 이 패치는 오프라인 신원 복원, NIP-07 서명, 회의실 격리에 대한 테스트를 추가합니다. 기존 [회의 앱](https://github.com/irislib/meet)은 암호화된 시그널링에 Nostr를, 오디오와 영상에 WebRTC를 사용합니다. 이는 기본 브랜치의 구현 진척이며, 저장소에는 이 특정 업데이트가 라이브 사이트에 반영되었음을 입증하는 태그된 릴리스가 없습니다.

### Chama가 등록 취소와 백그라운드 알림을 전파 {#chama-propagates-listing-cancellation-and-background-alerts}

[Chama](https://github.com/jesuspirate/chama)는 커뮤니티 거래와 비공개 대화에 서명된 event를 사용합니다. [버전 6.4.14–6.4.16](https://github.com/jesuspirate/chama/releases/tag/v6.4.16)은 등록 항목을 로컬에서 삭제하기 전에 서명된 취소를 게시하므로, 다른 클라이언트도 캐시된 같은 제안을 내릴 수 있습니다. 수신자 깨우기 tag는 이제 발신자의 알림 설정과 무관하게 event에 붙으며, 알림 서버는 서명된 event 기준으로 중복을 제거하므로 가입 직후의 채팅도 깨우기를 발생시킬 수 있습니다. 백그라운드 작업은 저장된 커서부터 영향을 받은 거래를 다시 처리하고, 실패한 체인을 격리하며, 알림 텍스트를 로컬에서 복호화합니다. 이 릴리스는 동반 감시 서비스를 다시 배포해야 합니다.

[묶음으로 나온 릴리스](https://github.com/jesuspirate/chama/releases/tag/v6.4.16)는 참가자 갱신을 서명된 event 시각에 적용하고, 자리가 만료된 뒤에 이루어진 자금 잠금을 격리하며, 저장된 무기명 노트에 대한 복구 수단을 제공합니다. 청구 게시는 가져오기나 결제가 확인될 때까지 기다립니다. 등록 항목 필터는 커뮤니티 범위가 달라도 열람자의 통화를 유지하며, 거래 헤더는 확정된 참여 금액을 사용합니다. 이러한 변경은 Nostr에 연결된 두 클라이언트가 같은 event 기록에서 추론하는 내용을 일치시킵니다.

### Earthly 0.1.12가 재사용 가능한 지도 구성을 추가 {#earthly-0112-adds-reusable-map-configurations}

[Earthly](https://github.com/zeSchlausKwab/earthly)는 서명된 게시와 암호화된 공유를 지원하는 [Nostr 협업 지도 편집기](https://github.com/zeSchlausKwab/earthly/blob/v0.1.12/README.md)입니다. [버전 0.1.12](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.12)는 공개 Google My Maps를 위한 재사용 가능한 GMapper 구성, 개발자가 만든 Maplet 탐색, 구성의 비공개 저장 또는 공개 게시, 출처가 표시되는 도형 복사를 추가합니다. 같은 릴리스는 암호화된 연결 공유, 드래그 앤 드롭으로 엔티티 추가, 모바일 채팅 탐색도 추가합니다. Google 내보내기 가용성과 브라우저 CORS가 가져오기를 제한하고, 다운로드한 실행형 Maplet은 Tauri에서 여전히 사용할 수 없으며, 실제 Android 기기에서의 업그레이드 확인은 아직 남아 있습니다.

[구성 작업](https://github.com/zeSchlausKwab/earthly/pull/29)은 기존 게시 주소와 환경설정을 마이그레이션하고, 구성 업데이트에 대한 검토 또는 철회를 추가했습니다. 초기 Android 워크플로는 컴파일 전에 실패했으며, [도구 수정](https://github.com/zeSchlausKwab/earthly/pull/30)이 이후 태그된 릴리스를 준비했습니다.

### Mostro 0.19.0이 1세대 전송을 폐기 {#mostro-0190-retires-its-first-generation-transport}

[Mostro](https://github.com/MostroP2P/mostro)는 Nostr를 통해 P2P 거래를 조율합니다. [버전 0.19.0](https://github.com/MostroP2P/mostro/releases/tag/v0.19.0)은 이제 [1세대 gift-wrap 전송의 제거](https://github.com/MostroP2P/mostro/pull/1004)를 출시하므로, 클라이언트는 더 새로운 프로토콜을 사용해야 합니다. 기존의 주문 생성 및 분쟁 개시 타임스탬프 tag는 저장된 값을 바꾸지 않고 [`published_at`으로 이름이 바뀌며](https://github.com/MostroP2P/mostro/pull/1000), 이를 감싸는 event의 `created_at`은 계속 서명 시각을 나타냅니다. 복원 응답은 상대방의 거래 키를 반환하고, 수락된 생성/수락 작업은 거래 키를 인식하며, relay 게시는 첫 번째 긍정적 relay 확인 시점에 완료됩니다. 같은 릴리스는 보증금 기한과 취소를 업데이트하고, 거래가 해결되면 분쟁을 종료하며, 해결 담당자에게 알리고, 중계되는 가격의 오래됨 정도에 한도를 둡니다.

Mostro의 [거래 키 수락 수정](https://github.com/MostroP2P/mostro/pull/1006)은 처음 소개하는 주문이나 분쟁이 커밋되는 즉시 키를 인식합니다. 첫 접촉에 더 엄격한 작업 증명을 요구하는 노드는 이전에는 주기적인 알려진 키 갱신 전까지 정당한 후속 메시지를 버릴 수 있었으며, 기본값처럼 기준이 같은 경우에는 영향이 없었습니다. [분쟁 트랜잭션](https://github.com/MostroP2P/mostro/pull/923)은 주문 상태 전환과 분쟁 행을 원자적으로 커밋해 상태 불일치 실패를 막습니다. [종료 알림](https://github.com/MostroP2P/mostro/pull/945)은 사용자들이 분쟁을 해결하면 배정된 해결 담당자에게 최선 노력 방식의 비공개 메시지를 보내며, 기존의 replaceable event는 오프라인 대체 수단으로 남습니다.

### SCRUTINY Lens가 보안 연구를 Nostr로 가져옴 {#scrutiny-lens-brings-security-research-onto-nostr}

9월 29일에 첫 공개 릴리스로 나온 [SCRUTINY Lens v0.1.0](https://github.com/crocs-muni/scrutiny-lens/releases/tag/v0.1.0)은 Nostr를 통해 게시되는 보안 메타데이터를 위한 브라우저 클라이언트입니다. 분석가는 CVE, 패키지 또는 인증서 식별자로 검색하고, event 기록과 철회를 살펴보며, 주제 그래프에서 관계를 탐색할 수 있습니다. 브라우저는 event 서명과 식별자를 검증합니다. 선택적인 AI 검색과 설명은 사용자가 고른 엔드포인트를 사용하며, 앱은 인용된 출처를 기반 event와 대조해 확인합니다. [릴리스 노트](https://github.com/crocs-muni/scrutiny-lens/releases/tag/v0.1.0)는 relay의 한계를 명시적으로 설명하고, 여전히 형제 저장소가 필요한 로컬 빌드 의존성을 밝힙니다.

### Mangatsu와 Noteds가 Android에 도착 {#mangatsu-and-noteds-reach-android}

[Mangatsu v0.1.11](https://github.com/imattau/Mangatsu/releases/tag/v0.1.11)은 이번 주 이 만화 리더 겸 게시 도구의 첫 Android 릴리스 계열에 속합니다. [소스](https://github.com/imattau/Mangatsu/commit/543d6d3dde3bffe293b7336d0fb6f4c82532fe13)는 외부 signer에게 Nostr 작업 승인을 요청하는 Android 인터페이스인 [NIP-55](/ko/topics/nip-55/)를 통한 Amber 로그인을 추가합니다. 만화와 챕터는 Nostr event이며, 페이지는 Blossom 서버에 저장됩니다. 리더는 암호화된 저장 라이브러리와 오프라인 읽기도 지원합니다. 이후 커밋은 signer 호출과 relay 목록 갱신을 다룹니다.

[Noteds v0.1.2](https://github.com/imattau/noteds/releases/tag/v0.1.2)는 Tauri를 통해 Nostr 안내 광고 마켓플레이스를 Android로 가져옵니다. [Android signer 통합](https://github.com/imattau/noteds/commit/c9294999134196e9d98c011440c7ca0ed5fcc398)은 Android NIP-55 서명을 사용합니다. 이 앱은 등록 항목과 메시지를 Nostr로 게시하고, 카테고리, 지리적 지역, 선택적인 브라우저 임베딩으로 로컬 검색 그래프를 구축합니다. 최신 소스는 근처 검색을 위한 네이티브 위치 접근을 수정합니다. 두 프로젝트 모두 초기 릴리스이며, GitHub 릴리스 페이지에 자세한 노트가 없으므로 이러한 기능은 태그된 README와 구현 커밋에서 나온 것입니다.

### Statim이 Nostr DM을 다른 네트워크와 결합 {#statim-combines-nostr-dms-with-other-networks}

[Statim v0.4.0](https://github.com/alaibe/statim/releases/tag/v0.4.0)은 9월 23일의 초기 릴리스에 이어 나왔습니다. [태그된 소스](https://github.com/alaibe/statim/blob/v0.4.0/README.md)는 XMTP, Status, Telegram, Matrix와 함께 NIP-17 Nostr DM을 지원하는 메신저를 설명합니다. 계정은 로컬에 보관된 복구 문구에서 시작하며, 각 네트워크가 서로 다른 개인정보 보호 특성을 제공하므로 대화마다 해당 프로토콜이 표시됩니다. Android에는 현재 Telegram 통합이 없습니다. 이는 프로젝트가 문서화한 기능이며, 독립적으로 테스트된 보장이나 앱 스토어 제공 여부에 대한 확인이 아닙니다.

## 개발 중 {#in-development}

### Amethyst가 암호화 그룹 상호 운용성을 수리 {#amethyst-repairs-encrypted-group-interoperability}

[Amethyst](https://github.com/vitorpamplona/amethyst)는 Marmot 암호화 그룹을 지원하는 Android Nostr 클라이언트입니다. White Noise는 또 다른 Marmot 메신저이며, [White Noise 클라이언트와 함께 테스트한 상호 운용성 묶음](https://github.com/vitorpamplona/amethyst/pull/4245)은 두 클라이언트가 한 대화를 공유할 때 드러난 그룹 관리, 삭제 문구, 기타 동작을 다룹니다. 더 구체적인 수정으로는 [반응과 삭제를 Marmot 그룹 안에서 전송](https://github.com/vitorpamplona/amethyst/pull/4233)해 별도의 [NIP-17](/ko/topics/nip-17/) gift-wrap 비공개 메시지로 보내지 않게 하는 것과, [재시작 후 다른 클라이언트의 편집을 적용](https://github.com/vitorpamplona/amethyst/pull/4240)하는 것이 있습니다. 이는 소스 병합이며, PR에 기술된 테스트는 공개된 클라이언트 간 릴리스보다 범위가 좁습니다.

별도의 [Cordn 그룹 런타임 및 인터페이스 병합](https://github.com/vitorpamplona/amethyst/pull/4201)은 코디네이터 서버를 통한 또 다른 암호화 그룹 경로를 추가합니다. Cordn은 Marmot과 다르므로, 두 변경을 하나의 전송 마이그레이션으로 읽어서는 안 됩니다.

Amethyst는 또한 [Geode relay와 Quartz 클라이언트의 HTTP relay 명령](https://github.com/vitorpamplona/amethyst/pull/4231)을 자체 [NIP-FE](/ko/topics/nip-fe/) 제안에 따라 병합했으며, replaceable 프로필 및 목록 event를 위한 [백업 충돌 검토 인터페이스](https://github.com/vitorpamplona/amethyst/pull/4174)도 병합했습니다. NIP-FE는 프로젝트 제안 용어입니다. 백업 흐름은 사용자가 대체를 수락하기 전에 버전을 비교할 수 있게 하고 로컬 상태가 조용히 덮어쓰이는 것을 막습니다.

Amethyst는 Armada와 Accordion이 사용하는 별도의 암호화 커뮤니티 프로토콜인 Concord도 개발합니다. [적합성 묶음](https://github.com/vitorpamplona/amethyst/pull/4262)은 분할된 커뮤니티 목록, 고정 증명, 키 교체 및 해산 기록을 추가하며, 이어서 [사라지는 메시지와 직접 초대](https://github.com/vitorpamplona/amethyst/pull/4264)가 뒤따릅니다. 초대는 수락될 때까지 비공개 받은편지함에 머물며, 초대를 받는 것만으로는 커뮤니티의 relay에 연결하지 않습니다. 같은 변경은 다른 작성자의 삭제가 메시지를 제거할 수 있게 하던 작성자 비교 오류를 바로잡습니다. [클라이언트 간 수정](https://github.com/vitorpamplona/amethyst/pull/4265)은 서명되지 않은 rumor 직렬화, 누락된 초대 필드, relay가 확인한 커뮤니티 생성, 재시작 없는 가입을 수리하며, 보고된 에뮬레이터 테스트에는 실제 Armada 및 Accordion 피어가 참여했습니다.

이후의 [비공개 채널 구현](https://github.com/vitorpamplona/amethyst/pull/4277)은 관련 접근 권한이 철회되면 채널 키를 교체하고, 생성, 비공개 전환, 공개 전환, 키 재발급 제어를 추가합니다. 또한 등급을 확인하는 협력적 강퇴를 추가하고, 메시지 첨부 파일이 상위 메시지와 함께 만료되게 합니다. WebXDC 업데이트는 별도의 채널 버퍼에 들어갈 수 있지만, Amethyst에는 여전히 WebXDC 애플리케이션 호스트가 없습니다. 이 후속 묶음은 유선 형식 테스트와 단위 테스트를 보고할 뿐 기기나 실제 relay에서의 실행은 없으므로, 앞선 상호 운용성 결과가 새로 추가된 모든 제어를 보증하지는 않습니다.

Quartz의 MLS 엔진은 이제 [건너뛴 메시지 세대 비밀 값을 재시작 후에도 보존](https://github.com/vitorpamplona/amethyst/pull/4271)해, 저장된 상태를 복원한 뒤에도 순서가 뒤바뀐 메시지를 복호화할 수 있게 합니다. [보존되는 이전 epoch 네 개](https://github.com/vitorpamplona/amethyst/pull/4272)는 호출자가 늦게 도착한 애플리케이션 메시지를 인증하고, 인증된 데이터를 유지하며, 이미 소비된 세대가 다시 열리지 않게 합니다. [비밀 트리 업데이트](https://github.com/vitorpamplona/amethyst/pull/4275)는 ts-mls 방식 상태에서 확장되지 않은 노드 비밀 값을 불러오며, [발신자별 오래된 세대 오류](https://github.com/vitorpamplona/amethyst/pull/4270)는 클라이언트 자신의 ratchet 충돌과 다른 멤버의 재전송을 구별합니다. PR은 Marmot의 기존 보존 epoch 대체 경로가 별개로 남아 있다고 명시하므로, 이는 엔진 기능일 뿐 모든 Amethyst 메시지 경로가 이를 사용한다는 증거는 아닙니다.

[Quartz tag 판독기 감사](https://github.com/vitorpamplona/amethyst/pull/4267)는 평문으로 게시될 수 있던 비공개 geohash 항목과, `nsec`의 개인 키를 공개 키로 취급하던 파서를 수정합니다. 또한 리포스트 주소, 채널 숨김 대상, 라이브 룸 루트 tag, addressable 민트 event를 수리합니다. 더 이상 쓰이지 않는 `ForkTag` 판독기가 제거되어 Quartz 사용자에게 소스 API 변경이 생기며, 기존 SQLite 민트 행에는 여전히 별도의 마이그레이션이 필요합니다. [추가 event 모델](https://github.com/vitorpamplona/amethyst/pull/4282)은 Buzz의 프로젝트 컨테이너, 아티팩트 수정본, 팀 제안을 다루고, [동영상 보기 및 암호화된 푸시 제어 모델](https://github.com/vitorpamplona/amethyst/pull/4266)은 Divine의 스키마를 따릅니다. 이러한 추가는 파싱과 구성 지원을 확립할 뿐, 완전한 클라이언트 인터페이스나 번호가 매겨진 채택된 NIP를 의미하지는 않습니다.

이 클라이언트는 또한 Android 14 이상에서 피드와 전체 화면 뷰어에 [Ultra HDR 사진을 렌더링](https://github.com/vitorpamplona/amethyst/pull/4284)합니다. Android 15 이상에서는 피드의 밝기 상승이 일반 범위의 두 배로 제한되고, 전체 화면에서는 디스플레이의 전체 범위를 쓸 수 있습니다. 보고된 테스트 기기는 더 새로운 Android API를 실행했으므로 Android 14와 15는 테스트되지 않았습니다. [공유 UI 및 업로드 포트 병합](https://github.com/vitorpamplona/amethyst/pull/4278)은 140개 화면을 Android/데스크톱 공통 코드로 옮기고 Android 미디어 작업을 UI 스레드 밖으로 옮깁니다. 이 작업의 감사는 메타데이터 제거 오류 보고도 복원하므로, 이 리팩터링은 단순한 파일 이동 이상입니다.

### Divine이 다이렉트 메시지에 암호화된 동영상을 추가 {#divine-adds-encrypted-video-to-direct-messages}

[Divine](https://github.com/divinevideo/divine-mobile)은 Nostr 동영상 클라이언트입니다. [NIP-17](/ko/topics/nip-17/)은 발신자를 relay로부터 숨기는 암호화된 gift wrap에 비공개 메시지를 담습니다. Divine의 [병합된 동영상 메시지 작업](https://github.com/divinevideo/divine-mobile/pull/9486)은 첨부된 동영상을 기기에서 암호화하고, 암호문을 업로드하며, 복호화 키를 그 비공개 메시지 안에 담아 보냅니다. 수신자는 파일을 검증하고 복호화해 재생하거나 저장할 수 있습니다. 별도의 [기록 복원 수정](https://github.com/divinevideo/divine-mobile/pull/9446)은 다른 relay가 아직 응답할 수 있을 때 모호한 relay 거부 때문에 복구가 조기에 끝나지 않도록 합니다.

Divine의 [폐기된 모더레이션 키 수정](https://github.com/divinevideo/divine-mobile/pull/9603)은 모더레이션 레이블 해석에서 폐기된 키를 거부하고, 신고가 접수될 때 현재의 신고 수신자를 선택합니다. 폐기된 키로 보내진 대기 중인 신고는 빌드에 고정된 키로 전환되며, 해결되지 않은 대화는 쓸 수 없는 상태로 남습니다. 이 변경은 미성년자가 읽을 수 있는 과거 스레드를 결정할 때 폐기된 키의 보관 주체도 구별하며, 보관 주체 업데이트에는 여전히 애플리케이션 릴리스가 필요합니다. [삭제된 댓글 캐시 처리](https://github.com/divinevideo/divine-mobile/pull/9677)는 성공적으로 삭제된 최근 댓글이 스레드를 다시 불러올 때 다시 나타나지 않게 합니다.

제작자를 위해 [실시간 색상 마스크 녹화 모드](https://github.com/divinevideo/divine-mobile/pull/9598)는 촬영 전에 대체 배경을 미리 보여 주며, [흰 벽 마스킹](https://github.com/divinevideo/divine-mobile/pull/9701)은 동영상 플러그인을 통해 밝기에 반응하는 마스킹을 추가합니다. [단어별 자막](https://github.com/divinevideo/divine-mobile/pull/9652)은 인식된 단어 타이밍을 보존하고, 서버가 전체 큐만 제공할 때는 근사 타이밍을 사용합니다. [스톱모션 이어 찍기](https://github.com/divinevideo/divine-mobile/pull/9698)는 기존 구성의 속도에 맞춰 새 정지 화면을 덧붙이며, [분리된 클립 되돌리기](https://github.com/divinevideo/divine-mobile/pull/9645), [그룹화된 글꼴 선택](https://github.com/divinevideo/divine-mobile/pull/9654), [속도 사전 설정](https://github.com/divinevideo/divine-mobile/pull/9601)은 Nostr event 형식을 바꾸지 않고 편집 제어를 추가합니다.

[정사각형 내보내기 정렬](https://github.com/divinevideo/divine-mobile/pull/9694)과 그 [작은 클립 후속 수정](https://github.com/divinevideo/divine-mobile/pull/9703)은 해상도가 섞인 클립에서도 텍스트와 스티커를 제자리에 유지합니다. [타사 HLS 재생](https://github.com/divinevideo/divine-mobile/pull/9664)은 가져온 재생 목록을 반복해서 미리 버퍼링하는 대신 루프 경계에서 되감아 Android 힙 충돌을 피하며, 이 루프는 다시 시작할 때마다 잠시 멈출 수 있습니다. [계정 환경설정 다시 불러오기](https://github.com/divinevideo/divine-mobile/pull/9680)는 계정 전환 시 계정에 묶인 필터를 기본값으로 유지하면서 디버그 로그인 어서션의 일부를 수정합니다. 별도의 모더레이션 레이블 새로 고침 문제는 여전히 열려 있으므로, 이 PR이 모든 로그인 오류가 해결되었다고 주장하지는 않습니다.

### Buzz가 relay의 채널 및 신원 제어를 확장 {#buzz-extends-its-relays-channel-and-identity-controls}

[Buzz](https://github.com/block/buzz)는 자체 relay와 클라이언트를 갖춘 Nostr 기반 업무 공간입니다. [병합된 채널 아티팩트 구현](https://github.com/block/buzz/pull/7919)은 편집 가능한 레코드에 하나의 채널 홈과 수정본 체인을 부여하며, 충돌하는 편집이 둘 다 헤드가 될 수는 없습니다. 프로젝트의 [NIP-AR](/ko/topics/nip-ar/) 레이블은 자체 제안과 구현을 가리키며, 확립된 Nostr 표준이 아닙니다.

보호된 HTTP 수신 경로를 위해 또 다른 [병합된 변경](https://github.com/block/buzz/pull/7264)은 연합 신원 어서션을 [NIP-98](/ko/topics/nip-98/) 인증으로 증명된 같은 키와 짝짓습니다. NIP-98은 서명된 HTTP 인증 event를 정의하며, Buzz의 [NIP-FI](/ko/topics/nip-fi/) 어서션은 프로젝트 명세입니다. Buzz는 또한 [비밀 키 백업 봉투를 위한 HPKE 암호화](https://github.com/block/buzz/pull/7849)를 병합했습니다. 이 PR은 소스 수준의 보안 작업을 확립하며, 모든 클라이언트로의 배포는 아직 확인되지 않았습니다.

[Buzz 데스크톱 0.5.26](https://github.com/block/buzz/releases/tag/desktop-v0.5.26)에는 채널 아티팩트 작업, 네이티브 HPKE 비밀 키 백업 암호화, 데스크톱 relay 관리 콘솔이 포함됩니다. 공유 변경 사항은 목록에 없는 프로젝트 채널 요청을 수리하고, 사이드바 섹션, 정렬, 별표, 음소거를 기기 간에 동기화하며, 긴 스레드 읽기에 한도를 두고, Blossom 신원 어서션을 강화합니다. [저장소 전체 노트](https://github.com/block/buzz/releases/tag/desktop-v0.5.26)는 relay 신원 페어링, 동반 멘션 전달, 설정 가능한 푸시 URL, 원자적 관리 삭제, 모바일 문맥별 이름을 별도로 나열합니다. 데스크톱 릴리스는 데스크톱/공유 배포를 확립할 뿐, 그 모바일 변경이 모바일 빌드로 출시되었음을 입증하지는 않습니다.

Buzz의 [WebSocket NIP-FI 강제 적용](https://github.com/block/buzz/pull/7224)은 프레임을 수락하기 전에 연합 신원 어서션을 확인한 뒤, 그 Nostr 키가 클라이언트의 신원을 relay에 증명하는 [NIP-42](/ko/topics/nip-42/)로 인증된 키와 일치하도록 요구합니다. 세션은 토큰 만료, 최대 어서션 수명, 설정된 연결 수명 중 가장 이른 시점에 만료되며, 만료 후에는 새로운 효과를 받아들이지 않습니다. 이 프로젝트 고유의 NIP-FI 모드는 기본적으로 꺼져 있습니다. 이미 수락된 오디오 커밋과 구독 설정은 여전히 멈춘 의존성을 기다릴 수 있으므로, 이 변경이 보편적으로 제한된 연결 해제 시간을 확립하지는 않습니다.

[소유자 삭제 준비](https://github.com/block/buzz/pull/7830)는 운영자가 증명한 요청을 목록에 묶인 자동 승인을 거쳐 기존 삭제 실행기로 넘깁니다. [relay 후속 작업](https://github.com/block/buzz/pull/7969)은 같은 요청을 재시도하면 현재 상태를 반환하게 하고, 삭제가 완료될 때까지 소유자의 활성 할당량을 예약합니다. 영구적으로 보존되는 호스트 툼스톤은 커뮤니티 20개라는 평생 상한에 포함됩니다. 이는 소스 수준의 관리 변경이며, 후속 작업은 relay와 드레인 실행기가 가동될 때까지 운영자에게 삭제를 비활성화해 두라고 안내합니다. 이와 별도로 [파티션 카탈로그 감사](https://github.com/block/buzz/pull/6515)는 새 event 및 전달 로그 파티션을 만들기 전에 포괄 파티션과 다루지 않은 달을 감지해, 서비스 안전성과 감사 최신성을 운영자에게 드러냅니다.

Buzz 모바일은 이제 표시 이름이 같은 사람과 에이전트를 구별합니다. [신원 이름 해석기](https://github.com/block/buzz/pull/7894)는 에이전트를 소유자 기준으로 한정하고 필요할 때만 짧은 키 접미사를 붙이며, [대화 통합](https://github.com/block/buzz/pull/7895)은 작성자, 멘션, 멤버십 알림에 그 이름을 사용합니다. [목록, 검색, Pulse](https://github.com/block/buzz/pull/7896)는 대화 밖에서도 같은 동작을 완성합니다. 눈에 보이는 한정 표시는 로컬 레이블만 바꾸며, 선택된 멘션은 신원의 원래 유선 이름을 유지합니다.

### Conduit가 relay 수락 후 결제를 진행 {#conduit-advances-checkout-after-relay-acceptance}

[Conduit](https://github.com/Conduit-BTC/conduit-mono)는 판매자에게 비공개 주문 메시지를 보내는 Nostr 마켓플레이스입니다. [점진적 relay 게시](https://github.com/Conduit-BTC/conduit-mono/pull/483)는 첫 번째 긍정적 relay 확인과 모든 relay 시도의 완료를 구별하며, [결제 후속 작업](https://github.com/Conduit-BTC/conduit-mono/pull/488)은 진행하기 전에 그 첫 확인을 저장합니다. relay의 수락은 서명된 주문이 relay에 도달했다는 뜻일 뿐, 판매자가 그것을 읽거나 처리했다는 증거는 아닙니다.

Conduit는 또한 [복구 가능한 원격 signer 세션](https://github.com/Conduit-BTC/conduit-mono/pull/529)과 [트랜잭션 방식의 signer-relay 협상](https://github.com/Conduit-BTC/conduit-mono/pull/533)을 병합했습니다. [NIP-46](/ko/topics/nip-46/)은 애플리케이션이 별도의 signer가 보유한 키에 서명을 요청할 수 있게 합니다. 이 변경들은 전송이 수리되는 동안 사용자의 계정 작업 공간을 유지하고, 재개하기 전에 정확한 계정을 검증합니다. 이 PR들은 소스 동작을 확립할 뿐, 출시된 결제 빌드를 의미하지는 않습니다.

Conduit의 [순위 기반 상품 검색 병합](https://github.com/Conduit-BTC/conduit-mono/pull/575)은 kind 30402 상품에 대해 일반 [NIP-50](/ko/topics/nip-50/) 전문 검색 쿼리 하나를 보내고, 서명 검사, 수정본 조정, 로컬 자격 필터링을 거치는 동안 relay의 관련성 순서를 유지합니다. 카드는 정확한 상품의 백그라운드 읽기가 끝나기 전에 나타날 수 있으며, 더 새로운 서명된 삭제가 계속 우선합니다. 새로 고침과 재시도는 광범위한 카탈로그 탐색을 시작하지 않고 검색과 정확한 상품 읽기 범위 안에 머뭅니다. 결과 100개 상한 뒤에 로컬 필터링이 이어지면 자격 있는 일치 항목을 놓칠 수 있으므로, 부분적으로 빈 응답은 복구 수단을 제공하며 상품이 없다는 증거가 아닙니다.

### Elisym이 Nostr 커머스 결제를 구축 {#elisym-builds-a-nostr-commerce-checkout}

[Elisym](https://github.com/elisymlabs/elisym)은 상품에 서명하고 비공개 주문 및 영수증 메시지를 Nostr로 전달하는 커머스 도구 모음을 개발하고 있습니다. [병합된 커머스 패키지](https://github.com/elisymlabs/elisym/pull/120)는 제안 검증과 gift-wrap 주문 event를 정의합니다. [결제 인터페이스](https://github.com/elisymlabs/elisym/pull/131)는 제안 검토, 지갑 결제, 배송 상태를 처리하며, [자체 호스팅 판매자 노드](https://github.com/elisymlabs/elisym/pull/133)는 스토어 쪽을 패키지로 묶습니다. 프로젝트는 kind `30490`을 임시로 부르며 10월의 최소 구현 범위를 설명합니다. 이 소스 병합들은 새로 등장하는 통합을 확립할 뿐, 채택된 Nostr 커머스 표준이나 완전한 공개 출시가 입증된 것은 아닙니다.

Elisym의 [에이전트 결제 도구](https://github.com/elisymlabs/elisym/pull/136)는 Nostr로 광고되는 상품을 위한 `buy_product`와 `get_order`를 추가합니다. 첫 번째 호출은 주문하지 않고 견적을 반환하며, 두 번째 호출은 같은 에이전트와 네트워크에 대해 일회용 견적과 경고를 수락합니다. 주문 상태는 에이전트의 로컬 파일 백엔드에 지속적으로 보관됩니다. [Tempo 결제 지원](https://github.com/elisymlabs/elisym/pull/137)은 판매자 검증과 배송을 갖춘 브라우저 지갑 결제 경로를 추가합니다. 전송된 트랜잭션 해시는 결과가 확정될 때까지 시도를 살아 있는 상태로 유지해, 브로드캐스트가 아직 정산될 수 있는 동안 미결제 결과가 나오지 않게 합니다.

[이후의 결제 수정](https://github.com/elisymlabs/elisym/pull/139)은 브라우저 지갑이 탐색 중 즉시 자신을 알릴 때도 서명된 상품 결제가 초기화될 수 있게 합니다. 이 소스 변경은 세션 선언을 그 콜백이 실행되기 전으로 옮기며, 병합만으로 호스팅된 배포가 검증되지는 않습니다.

### nostter가 signer 확인과 event 조회를 개선 {#nostter-improves-signer-checks-and-event-retrieval}

[nostter](https://github.com/SnowCait/nostter)는 Nostr 소셜 클라이언트입니다. [병합된 signer 기능 변경](https://github.com/SnowCait/nostter/pull/2573)은 팔로우 및 반응 동작을 제공하기 전에 사용 가능한 signer가 있는지 확인합니다. [새 고정 tag](https://github.com/SnowCait/nostter/pull/2611)는 추측하지 않고 작성자의 키와 알려진 relay 힌트를 담으며, [replaceable event 캐시 정렬](https://github.com/SnowCait/nostter/pull/2608)은 [NIP-01](/ko/topics/nip-01/)의 타임스탬프 및 event ID 동점 처리 규칙을 따릅니다. NIP-01은 클라이언트가 replaceable event 중 하나를 고르는 방법을 포함해 핵심 Nostr event 규칙을 정의합니다.

### Pensieve가 격리된 아카이브 조정을 준비 {#pensieve-prepares-isolated-archive-reconciliation}

[Pensieve](https://github.com/andotherstuff/pensieve)는 Nostr 아카이브 및 복구 도구입니다. [병합된 격리 negentropy 런타임](https://github.com/andotherstuff/pensieve/pull/60)은 동기화에 한도가 있는 워커와 지속성 있는 완료 동작을 제공합니다. 이 기능은 선택형이며, PR은 프로덕션 서비스나 설정이 활성화되지 않았다고 명시합니다. 이는 더 안전한 복구 경로를 위한 기초 작업이지, 실행 중인 배포의 증거가 아닙니다.

### ContextVM이 relay 간 중복 호출을 방지 {#contextvm-avoids-duplicate-calls-across-relays}

[ContextVM의 TypeScript SDK](https://github.com/ContextVM/sdk)는 도구 및 리소스 요청을 Nostr event로 전달합니다. [병합된 수신 중복 제거 수정](https://github.com/ContextVM/sdk/pull/103)은 여러 relay나 재연결로 같은 평문 요청이 다시 전달되더라도 event ID로 하나의 요청임을 인식하며, 기존의 래핑된 메시지 경로와 동작을 맞춥니다. PR에 따르면 수정 전에는 멱등성이 없는 도구 하나가 한 번의 호출에 세 번 실행되었습니다. 동반된 [리소스 알림 변경](https://github.com/ContextVM/sdk/pull/101)은 구독한 클라이언트에게만 업데이트를 보내며, 구독 없이 초기화된 세션은 더 이상 이를 받지 않습니다.

### Cyberspace가 DECK-0003 객체 규칙을 개정 {#cyberspace-revises-the-deck-0003-object-rules}

[Cyberspace](https://github.com/arkin0x/cyberspace)는 구조화된 Nostr 객체와 암호화된 영역 가방을 위한 DECK-0003 형식을 개발하며, 지난호에서 다뤘듯 Amethyst가 이를 구현하기 시작했습니다. 새로운 [부품 및 숨김 객체 규칙](https://github.com/arkin0x/cyberspace/pull/36)과 [가방 참조](https://github.com/arkin0x/cyberspace/pull/38)는 가방이 모든 부품을 포함하는 대신 별도로 게시된 객체를 참조할 수 있게 합니다. 이후의 [정정](https://github.com/arkin0x/cyberspace/pull/40)은 relay가 대체 후 이전 버전을 버릴 수 있으므로 event ID 참조로는 addressable event의 이전 버전을 확실히 고정할 수 없다고 말합니다. 독자는 정정된 좌표 참조 규칙을 사용해야 하며, 앞선 병합의 문구는 대체되었습니다.

### Wisp가 Nostr 댓글에 대한 답장을 수정 {#wisp-fixes-replies-to-nostr-comments}

[Wisp](https://github.com/barrydeen/wisp)는 relay 라우팅과 지갑 기능을 갖춘 Nostr 클라이언트입니다. 지난주에 출시된 [NIP-22](/ko/topics/nip-22/) 댓글 지원에 이어, [병합된 후속 작업](https://github.com/barrydeen/wisp/pull/667)은 NIP-22 댓글에 대한 답장도 적절한 상위 및 루트 참조를 갖춘 댓글 event가 되게 합니다. 이전 경로는 항상 일반 노트를 게시했습니다. NIP-22는 댓글이 다양한 Nostr 콘텐츠 유형에 붙을 수 있게 합니다. 이 수정은 노트에 버전 변경만 적힌 Wisp 1.2.5 태그 이후에 병합되었으므로, 아직 릴리스가 확인되지 않은 소스 수준의 진척입니다.

### Cordn이 코디네이터 위치를 두 번째 기기로 전달 {#cordn-sends-coordinator-locations-to-a-second-device}

[Cordn](https://github.com/Cordn-msg/cordn)은 Nostr를 통한 암호화 그룹 메시징을 조율합니다. [병합된 다중 기기 명세 변경](https://github.com/Cordn-msg/cordn/pull/9)은 복제되는 그룹 문서에 그룹의 코디네이터 relay 힌트를 담습니다. 그러면 새로 초기화된 기기가 기본 relay에 없는 코디네이터도 찾을 수 있으므로, 백로그와 실시간 메시지를 가져올 수 없는 그룹에 가입한 것처럼 보이는 일이 없어집니다. 이는 지난주 Cordn 오프라인 대기열 릴리스에 이은 프로토콜 문서 작업이며, 새 클라이언트 릴리스가 아닙니다.

### Nostr Atlas가 확인 가능한 신원을 위한 디렉터리를 공개 {#nostr-atlas-opens-a-directory-for-checkable-identities}

[Nostr Atlas](https://nostr-atlas.web.app)는 외부 계정에 대한 클레임과 함께 Nostr 프로필을 보여 주는 새 디렉터리입니다. [병합된 사이트 게시](https://github.com/saiy2k/nostr-components/pull/148)는 디렉터리를 프로젝트의 컴포넌트 데모와 분리하며, 사이트는 공개적으로 응답합니다. [클레임 흐름 병합](https://github.com/saiy2k/nostr-components/pull/144)은 X 계정 소유자가 브라우저 signer로 서명된 [NIP-39](/ko/topics/nip-39/) 증명을 게시할 수 있게 하며, [프로필 보강](https://github.com/saiy2k/nostr-components/pull/146)은 증명이 검증된 뒤에만 kind-0 Nostr 메타데이터를 읽습니다. NIP-39는 Nostr 키를 다른 온라인 신원과 연결하기 위한 증명 방식을 정의하며, relay 확인만으로는 클레임이 검증된 것으로 표시되지 않습니다.

### nostr-java가 미디어 호스팅 도구를 추가하고 tag 위치를 보존 {#nostr-java-adds-media-hosting-tools-and-preserves-tag-positions}

[nostr-java](https://github.com/tcheeric/nostr-java)는 Nostr 애플리케이션을 위한 Java 라이브러리이자 MCP 도구 모음입니다. [병합된 Blossom 도구](https://github.com/tcheeric/nostr-java/pull/557)는 호출자가 해시로 주소가 지정되는 미디어를 업로드, 검색, 나열, 삭제하고 사용자의 서버 목록을 관리할 수 있게 합니다. 별도의 [게시 수정](https://github.com/tcheeric/nostr-java/pull/558)은 빈 tag 값을 제자리에 유지합니다. Nostr tag는 위치 기반이므로, 빈 relay 힌트를 빼 버리면 표식이 잘못된 필드로 밀려나 게시된 event가 승인된 미리보기와 달라질 수 있습니다.

### Zap Cooking이 계정 기록 복구 방식을 변경 {#zap-cooking-changes-how-account-history-can-be-recovered}

[Zap Cooking](https://github.com/zapcooking/frontend)은 레시피 공유 Nostr 클라이언트입니다. [병합된 Lazarus 복구 작업](https://github.com/zapcooking/frontend/pull/753)은 [NIP-78](/ko/topics/nip-78/) 애플리케이션 전용 데이터 event에 기반한 백업을, relay가 보존한 replaceable event의 이전 버전을 스캔해 덮어쓰인 팔로우, 음소거, 프로필을 감지하는 방식으로 대체합니다. Lazarus는 여전히 초안 프로토콜입니다. 복구는 이전 버전을 보존한 relay에 달려 있으며, 병합된 웹 클라이언트 PR이 잃어버린 모든 event를 복구할 수 있다는 보장은 아닙니다.

이 클라이언트는 또한 노트와 답장을 위한 [선택적 NIP-13 작업 증명 제어](https://github.com/zapcooking/frontend/pull/743)와, [첨부 파일 모델](https://github.com/zapcooking/frontend/pull/752)을 통해 미리보기와 게시 사이에서 미디어 순서와 [NIP-92](/ko/topics/nip-92/) 설명을 일관되게 유지하는 변경을 병합했습니다. [NIP-13](/ko/topics/nip-13/)은 발신자가 게시 전에 event에 로컬 연산을 들이게 하며, NIP-92는 미디어 메타데이터를 event tag로 전달합니다.

Zap Cooking의 [NIP-05 클레임 수정](https://github.com/zapcooking/frontend/pull/763)은 정확한 요청 본문에 대한 [NIP-98](/ko/topics/nip-98/) 인증을 요구하고, 이름을 주장하는 공개 키와 다른 signer를 거부합니다. 이전에는 이 공개 엔드포인트가 인증되지 않은 클레임을 받아들여 다른 멤버의 이름을 대체할 수 있었습니다. 멤버십 등급은 이제 기존 멤버십 기록에서 가져오며, 원격 signer 사용자는 클레임할 때 서명 요청을 받습니다. 신뢰할 수 있는 별도의 서버 측 등록 경로는 바뀌지 않습니다.

[음소거 목록 수리](https://github.com/zapcooking/frontend/pull/764)는 프로필의 음소거 동작이 kind 10000 목록 전체를 공개 키 tag만으로 대체하지 않게 합니다. 이전 경로는 단어, 해시태그, 스레드 항목과 암호화된 내용을 지웠으며, 한 화면에서는 복호화된 비공개 음소거 키를 공개적으로 재게시할 수 있었습니다. 새 경로는 relay의 사본을 읽고, 관련 없는 tag와 암호문을 보존하며, 그 읽기를 할 수 없으면 게시를 거부합니다. 비공개 음소거를 제거하려면 signer를 통한 복호화와 재암호화가 필요합니다.

### Opal이 Omarchy에 원격 서명을 도입 {#opal-brings-remote-signing-to-omarchy}

[Opal](https://github.com/derekross/opal)은 Omarchy Linux 환경을 위해 만든 데스크톱 Nostr signer입니다. [9월 28일 버전 0.3.3](https://github.com/derekross/opal/releases/tag/v0.3.3)은 첫 공개 계열에 이어 [NIP-46](/ko/topics/nip-46/) 원격 서명 지원, 로컬 키링, 연결된 앱의 요청을 위한 권한 인터페이스를 제공합니다. NIP-46은 별도의 클라이언트가 작업 승인을 요청하는 동안 계정 키를 signer에 둡니다. 이는 특정 플랫폼용 signer의 초기 릴리스이며, 더 넓은 데스크톱 지원을 주장하는 것이 아닙니다.

### WatchTower가 NIP-86 relay 제어판을 공개 {#watchtower-opens-a-nip-86-relay-control-panel}

[WatchTower](https://github.com/iqbqioza/watchtower)는 인증된 relay 관리 요청을 위한 프로토콜인 NIP-86을 통해 relay를 관리하는 새로 공개된 패널입니다. [공개 인스턴스](https://watchtower.nostrfy.org)가 응답하므로, 운영자는 인터페이스를 살펴볼 수 있습니다. 저장소는 9월 22일에 만들어졌습니다. 접속 가능한 사이트가 있다고 해서 인가 흐름이 독립적으로 감사되었거나 모든 relay 구현과 작동한다는 것이 입증되지는 않습니다.

### Hubstr Blossom이 개인 미디어 원본 서버를 공개 {#hubstr-blossom-opens-a-personal-media-origin}

새로 공개된 [Hubstr Blossom 서버](https://github.com/johninnis/hubstr-blossom)는 Nostr 클라이언트가 이미지, 동영상, 파일을 자체 호스팅 Blossom 엔드포인트에 업로드한 뒤 그 URL을 event에 넣을 수 있게 합니다. README는 로컬 콘텐츠 해시 저장소, SQLite 색인, 변경을 위한 서명된 kind-24242 인증, 그리고 업로드, 미러링, 목록, 삭제를 위한 다양한 Blossom 작업을 문서화합니다. 공개 읽기를 통해 다른 클라이언트는 업로드 권한 없이도 게시된 미디어를 렌더링할 수 있습니다.

[서버의 문서화된 옵션](https://github.com/johninnis/hubstr-blossom)은 공유 미디어를 설명하는 [NIP-94](/ko/topics/nip-94/) event를 위한 파일 메타데이터도 추출합니다. 서버는 EXIF 메타데이터 없이 이미지를 다시 인코딩할 수 있으며, 기본적으로 사설 네트워크 대상에 대한 미러 요청을 차단합니다. 이는 배포 안내를 갖춘 새로 공개된 구현이며, 광범위한 프로덕션 도입의 증거는 아닙니다.

[Hubstr Relay](https://github.com/johninnis/hubstr-relay)는 9월 24일에 초기 소스를 공개했습니다. 개인용 SQLite event 캐시와 공개 relay를 결합한 것으로, 인증되지 않은 독자는 허용된 공개 event를 보고, NIP-42로 인증된 테넌트는 자신의 캐시를 읽을 수 있습니다. NIP-17 gift wrap은 게스트 독자에게 계속 제공되지 않습니다. [9월 25일 업데이트](https://github.com/johninnis/hubstr-relay/commit/0ae1a551ac50da0b7097105b76591dbc4d6cc023)는 NIP-86 pubkey 목록 메서드가 반환하는 레코드를 바로잡습니다.

### Meshstr가 허가가 필요 없는 relay 메시를 실험 {#meshstr-experiments-with-a-permissionless-relay-mesh}

[Meshstr](https://gitlab.pocketlabs.dev/meshstr/meshstr)는 Nostr relay들이 피어 예산을 협상하고 서명된 사용량 영수증을 교환하기 위한 알파 단계 설계입니다. 첫 구현에는 9월 27일에 추가된 [Nostr relay인 strfry를 위한 쓰기 정책 브리지](https://gitlab.pocketlabs.dev/meshstr/meshstr/-/commit/6d609fc99f)가 포함되며, 다음 날 소켓 수정이 이어졌습니다. 저장소는 DIDComm 협상과, 피어가 전체 목록을 교환하지 않고 event 집합을 비교할 수 있게 하는 [NIP-77](/ko/topics/nip-77/) 조정, 그리고 합의된 예산을 초과한 피어에 대한 검증 가능한 보고를 설명합니다.

이러한 [프로젝트 규칙](https://gitlab.pocketlabs.dev/meshstr/meshstr)은 제안일 뿐, 채택된 NIP나 입증된 공개 relay 네트워크가 아닙니다. 이번 주의 구체적인 진척은 relay의 쓰기 정책을 제안된 메시 회계와 연결하는 코드 경로가 공개되었다는 것입니다.

### Dossier가 공개 Nostr 기록이 드러낼 수 있는 것을 보여 줌 {#dossier-shows-what-a-public-nostr-history-can-reveal}

[Dossier](https://github.com/satanrayshe/dossier)는 개인의 Nostr 및 Lightning 흔적을 브라우저에서 스스로 점검하는 새 도구이며, [공개 데모](https://satanrayshe.github.io/dossier/)를 제공합니다. 눈에 보이는 프로필 링크, zap 흔적, 게시 시각, 이전 [NIP-04](/ko/topics/nip-04/) 암호화 다이렉트 메시지의 메타데이터, 사진 EXIF 같은 미디어 메타데이터를 수집하며, 누군가 삭제하려 했던 event를 아직 제공하는 relay가 어디인지도 보여 줄 수 있습니다. [NIP-07](/ko/topics/nip-07/) signer 지원을 통해 사용자는 개인 키를 페이지에 붙여넣지 않고 정리 작업을 승인할 수 있습니다.

프로젝트의 [문서화된 한계](https://github.com/satanrayshe/dossier)가 중요합니다. 스캔은 도달한 relay만 볼 수 있으며, 삭제 요청은 다른 곳에 보관된 사본을 지울 수 없습니다. 저장소는 9월 27일에 등장했고 태그된 릴리스가 없습니다. 데모와 소스는 초기 단계의 도구를 확립할 뿐, 누군가의 과거 활동 전체를 담은 목록이 아닙니다.

### Marmot MDK가 투표, 사용자 지정 이모지, 계정 메타데이터를 확장 {#marmot-mdk-extends-polls-custom-emoji-and-account-metadata}

[Marmot MDK](https://github.com/marmot-protocol/mdk)는 암호화된 Nostr 그룹 메시징을 위한 런타임과 바인딩을 제공합니다. 이후의 MDK 소스 병합은 전체 집계와 같은 유효 응답 규칙을 사용하는 [페이지 단위의 투표자별 투표 선택](https://github.com/marmot-protocol/mdk/pull/2094)을 노출합니다. [선택적인 애플리케이션 소유 그룹 구성 요소](https://github.com/marmot-protocol/mdk/pull/1929)는 호스트에 메시지 보존 정책이 적용되어도 유지되고 새 멤버의 Welcome에 전달되는, 관리자가 제어하는 설정을 제공합니다. [태그된 전송과 미디어 반응](https://github.com/marmot-protocol/mdk/pull/2105)은 사용자 지정 이모지 메타데이터를 런타임과 바인딩 전반에 전달하고, epoch 변경 후에도 첨부된 반응 이미지의 복호화 자료를 유지하며, 위조된 첨부 tag를 거부합니다. 이 변경은 C 업로드 요청 구조체를 확장하므로, C 사용자는 헤더에 맞춰 다시 빌드해야 합니다.

[수렴 정정](https://github.com/marmot-protocol/mdk/pull/2093)은 정식 브랜치가 선택되지 않았을 때 실시간 상태를 시도하지 않고 메시지를 무효화하는 대신 대기 상태로 유지합니다. 함께 이루어진 [도달할 수 없는 경로 정리](https://github.com/marmot-protocol/mdk/pull/2095)는 해결되지 않은 스테이징 커밋을 보존된 재시도 동작으로 보냅니다. [암호화된 미디어 읽기](https://github.com/marmot-protocol/mdk/pull/2097)는 HTTP 읽기 시간 제한을 재개 가능한 본문의 유휴 처리에 맞춰 멈춘 대용량 전송을 다루지만, 대기 중인 수신 APK 기기 수락 테스트가 통과했다고 주장하지는 않습니다. [시작 단계 표식](https://github.com/marmot-protocol/mdk/pull/2098)은 어떤 계정 열기 단계에서 시간 초과가 발생했는지 보여 주어 진단 증거를 더하지만, 근본적인 시작 지연이 해결되었다고 주장하지는 않습니다.

로컬 에이전트 커넥터는 또한 kind 0 업데이트를 게시할 때 [기존 프로필 메타데이터를 병합](https://github.com/marmot-protocol/mdk/pull/1969)해, 요청에서 빠진 필드를 보존합니다. [그룹 프로필 업데이트](https://github.com/marmot-protocol/mdk/pull/2096)는 기존의 현재 관리자 인가 경로를 통해 그룹 이름과 설명의 변경을 노출합니다. 소켓 인증은 여전히 로컬 API 전체에 대한 권한을 부여하며, 이 병합은 주체별 권한 부여를 추가하지 않습니다. 이 소스 변경들은 태그된 0.11.0 릴리스 이후에 이루어졌습니다.

### rust-nostr가 relay COUNT 응답을 요청과 대응시킴 {#rust-nostr-correlates-relay-count-replies}

Nostr 애플리케이션을 위한 Rust 라이브러리이자 SDK인 [rust-nostr](https://github.com/rust-nostr/nostr)가 [요청에 대응되는 COUNT 응답과 더 명확한 대기자 오류](https://github.com/nostrdevkit/nostr/pull/1478)를 병합했습니다. SDK는 COUNT를 보내기 전에 구독하고 일치하는 응답만 받아들이므로, 유실되거나 닫힌 수신자가 정당한 0으로 보이는 일을 막습니다. 또한 게시 확인과 relay 인증에 대한 수신자 오류를 보존해, 호출자가 누락된 확인과 명시적 거부를 구별할 수 있게 합니다. 공개 메서드 시그니처는 바뀌지 않습니다.

### ZapTracker가 Nostr 네트워크 및 인용 지표를 추가 {#zaptracker-adds-nostr-network-and-quote-metrics}

[ZapTracker](https://github.com/pratik227/zap_dashboard)는 Nostr 참여와 지갑 활동을 위한 제작자 대시보드입니다. [네트워크 대시보드 병합](https://github.com/pratik227/zap_dashboard/pull/133)은 Lightning 네트워크 통계를 nostr.watch의 온라인 Nostr relay 데이터와 NIP-11 문서의 기능 정보로 대체합니다. [인용 지표 변경](https://github.com/pratik227/zap_dashboard/pull/135)은 좋아요, 리포스트, 북마크, zap과 함께 `q` tag를 담은 kind 1 event를 집계합니다. 이를 통해 제작자는 콘텐츠 순위와 참여 차트에서 인용을 볼 수 있으며, 이는 아직 병합된 소스 수준의 증거입니다.

### LaWallet NWC가 카드 충전을 카드 지갑으로 라우팅 {#lawallet-nwc-routes-card-top-ups-to-the-card-wallet}

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc)는 Nostr Wallet Connect를 통해 Lightning 지갑을 애플리케이션에 연결합니다. [BoltCard 충전 병합](https://github.com/lawalletio/lawallet-nwc/pull/316)은 카드 지갑의 NWC `make_invoice` 메서드로 인보이스를 생성하는 LUD-19 결제 링크를 알립니다. 차단되었거나, 비활성화되었거나, 페어링되지 않은 카드는 결제 링크를 알리지 않으며, 이 경로는 충전을 소유자의 별도 Lightning 주소로 돌리지 않습니다. [후속 작업](https://github.com/lawalletio/lawallet-nwc/pull/319)은 에뮬레이터에서도 같은 링크를 노출하고, LNURL 송금에 수신자가 허용한 결제자 메모를 담습니다.

### 새 khatru relay가 소유자 모더레이션 제어를 제공 {#a-new-khatru-relay-exposes-owner-moderation-controls}

[nostr-relay-khatru](https://github.com/rzazo24/nostr-relay-khatru)는 중단된 HiveScope 전용 구현에서 파생된 범용 relay로, 9월 29일에 초기 소스를 공개했습니다. [공개 인스턴스](https://relay.hivescope.xyz)는 이 저장소를 명시하고 인증, event 만료, 보호된 event, 개수 집계, 조정, relay 관리를 알리는 NIP-11 문서를 제공합니다. [9월 30일 구현](https://github.com/rzazo24/nostr-relay-khatru/commit/a6ef7cff9c4f833a6a2f72957d45935c736a0c51)은 소유자 패널에 모더레이션 제어를 추가합니다. 공개 메타데이터는 배포된 엔드포인트를 확인해 줄 뿐, 알려진 모든 메서드가 테스트를 통과했음을 확인해 주지는 않습니다.

### 로컬 web-of-trust 빌더가 언팔로우를 추적 {#a-local-web-of-trust-builder-tracks-unfollows}

[etemiz/wot](https://github.com/etemiz/wot/commit/212fe268dd781c73adad51329be235abc8fd37db)는 9월 30일에 Nostr web-of-trust 크롤러를 공개했습니다. 팔로우 목록과 NIP-65 relay 목록을 읽고, 설정 가능한 루트에서 신뢰도를 계산하며, relay 정책, 피드, 스팸 필터를 위해 점수를 LMDB에 기록합니다. [프로젝트 문서](https://github.com/etemiz/wot)는 그 절충을 설명합니다. 실시간 업데이트는 신뢰도를 높이고, 예약된 전체 크롤링은 신뢰도 감소와 언팔로우를 반영합니다. 점수는 선택한 루트에 따라 달라집니다. 이는 새로 공개된 소스이며, 태그된 릴리스나 프로덕션 배포에 대한 주장은 없습니다.

### Moyu가 Marmot 업무 공간 클라이언트를 공개 {#moyu-opens-a-marmot-workspace-client}

[Moyu](https://github.com/tsgx1990/moyu)는 [Marmot](/ko/topics/marmot/) 기반 Rust 업무 공간 채팅 클라이언트의 소스를 공개했으며, 명령줄, 터미널, 데스크톱 인터페이스를 갖추고 있습니다. [9월 30일 변경](https://github.com/tsgx1990/moyu/blob/88a20d247510d1cc46ca955564aa395d26ae8e89/CHANGELOG.md)은 로컬에 기록된 멤버십 변경을 사용해 이전 가입 요청이 제거된 멤버를 다시 받아들이지 못하게 하고, 초대 코드가 7일 후 만료되게 하며, 관리자가 이를 철회할 수 있게 합니다. 터미널 출력은 다른 멤버가 보낸 제어 문자와 텍스트 방향 재정의를 걸러 냅니다. 고정된 MDK 포크는 Blossom 첨부 파일 전송을 설정된 SOCKS5 프록시로 라우팅하며, 호스트 이름 해석도 그 프록시가 수행합니다. 0.3.0 변경 사항은 공개 소스에 있지만, 아직 공개 릴리스 태그나 릴리스 항목은 없습니다.

## 프로토콜 및 명세 작업 {#protocol-and-spec-work}

### NIP-39가 신원 증명을 Bluesky와 Discord로 확장 {#nip-39-extends-identity-proofs-to-bluesky-and-discord}

[NIP-39](/ko/topics/nip-39/)는 Nostr 계정이 다른 플랫폼의 신원을 통제하고 있다는 증명을 가리킬 수 있게 합니다. [9월 27일 병합된 변경](https://github.com/nostr-protocol/nips/pull/2486)은 새 증명에 권장 문장 하나를 제시하고, 계정의 npub을 포함하는 이전 증명은 문구가 다르더라도 받아들이라고 검증자에게 안내합니다. 또한 Bluesky 게시물과 Discord 메시지를 증명 위치로 문서화합니다. Discord 클레임은 해당 메시지가 게시된 서버를 읽을 수 있는 사람만 확인할 수 있습니다.

### NIP-86이 relay 관리자를 위한 초대 코드 관리를 추가 {#nip-86-adds-invite-code-management-for-relay-administrators}

Compass는 7월 8일 호에서 열려 있던 [NIP-86 초대 제안](https://github.com/nostr-protocol/nips/pull/2408)을 다뤘으며, 이 제안이 이제 병합되었습니다. [NIP-86](/ko/topics/nip-86/)은 표준 relay 관리 API를 정의하며, [NIP-43](/ko/topics/nip-43/)은 제한된 relay가 멤버십을 알리고 가입 요청을 처리하는 방법을 정의합니다. 9월 24일 병합은 `listclaims`, `createclaim`, `deleteclaim`을 추가해 관리자가 relay가 받아들이는 초대 코드를 나열, 발급, 철회할 수 있게 합니다. 이는 가입한 멤버에게 역할을 부여할 수 있는 초대를 위한 관리 경로를 운영자에게 제공하며, 모든 relay가 이 메서드를 지원해야 하는 것은 아닙니다.

지난주 [NIP-86 기사](/en/newsletters/2026-09-23-newsletter/#nip-86-adds-clear-and-list-methods-for-relay-management)에 대한 정정입니다. [병합된 명세](https://github.com/nostr-protocol/nips/blob/5b9920982ae1f4061328c1b09a90360da28d13c8/86.md)가 추가한 메서드는 `unallowevent`, `unbanevent`, `listallowedevents`, `listdisallowedkinds`입니다. 앞선 기사는 오래된 제안 설명에 있던 이름을 나열했습니다. 처음 두 메서드는 event 수준의 허용 또는 차단 결정을 되돌리며, 나머지는 허용된 event와 허용되지 않은 kind를 조회합니다.

### NIP-51이 즐겨찾는 팔로우 세트를 사용되지 않는 event kind로 이동 {#nip-51-moves-favorite-follow-sets-to-an-unused-event-kind}

[NIP-51](/ko/topics/nip-51/)은 사용자가 즐겨찾는 팔로우 세트 목록을 포함해 공개 및 비공개 목록을 정의합니다. Compass는 7월 22일 호에서 [kind 충돌 제안](https://github.com/nostr-protocol/nips/pull/2417)을 다뤘으며, 이 제안이 이제 병합되었습니다. 9월 27일 정정은 이전 번호가 이미 사용 중이었기 때문에 그 즐겨찾기 목록에 kind `10021`을 할당합니다. `a` tag는 여전히 kind `30000` 팔로우 세트를 가리킵니다. 이 변경은 명세의 번호 충돌을 해결할 뿐, 사람을 팔로우하는 새로운 방법을 만들지는 않습니다.

### NIP-51이 스레드별 숨긴 답장을 제안 {#nip-51-proposes-hidden-replies-for-each-thread}

[열린 NIP-51 제안](https://github.com/nostr-protocol/nips/pull/2489)은 스레드 작성자가 공개 숨긴 답장 세트를 게시하고, 협력하는 클라이언트가 이를 토글 뒤에 표시하도록 하자는 내용입니다. 스레드마다 하나의 addressable kind-30027 event를 사용하며, 루트 ID를 `d` tag로, 답장을 `e` tag로 지정합니다. 루트 작성자가 서명한 세트만 적용됩니다. 루트를 목록에 넣으면 클라이언트에게 다른 작성자의 답장을 숨기고 답장 작성기 제공을 멈추도록 요청하지만, 답장은 여전히 relay에 게시될 수 있습니다. 스레드별 형식은 편집 충돌을 같은 대화 안으로 제한합니다. 작성자는 Nostrich에 구현이 있다고 보고하지만 공개 소스 검토로는 이를 확인하지 못했으며, 제안은 세트 형식이 여전히 논의 중인 채로 병합되지 않았습니다.


### NIP-DB가 키로 주소가 지정되는 서비스를 위한 검증된 도메인 이름을 제안 {#nip-db-proposes-verified-domain-names-for-key-addressed-services}

9월 28일에 제출된 [열린 NIP-DB 제안](https://github.com/nostr-protocol/nips/pull/2487)은 일반 인터넷 도메인을, 노드를 Nostr 공개 키로 주소 지정하는 암호화 메시인 [FIPS](/ko/topics/fips/) 같은 키 주소 네트워크에서 그 도메인을 제공하는 키에 바인딩하는 Nostr event를 설명합니다. 도메인 소유자는 DNS TXT 레코드나 클레임과 함께 전달되는 DNSSEC 증명으로 바인딩을 확립할 수 있으며, 클라이언트는 이후 오프라인 사용을 위해 검증된 결과를 고정합니다. 누구나 Nostr event에서 다른 사람의 도메인을 주장할 수 있으므로, 제안은 검증되지 않은 클레임을 통한 이름 해석을 명시적으로 금지합니다. [fips-pub-domains](https://github.com/fr34aky/fips-pub-domains)는 작성자의 참조 구현이지만, event kind 번호와 일부 오버레이 관련 문구는 아직 검토 중입니다. 보고된 종단 간 테스트는 작성자의 증거일 뿐, 이 제안이 채택된 NIP라는 주장이 아닙니다.

### 비공개 피드 초안이 암호화된 수신자 그룹을 탐구 {#a-private-feed-draft-explores-encrypted-groups-of-recipients}

9월 29일에 열린 [새 다중 수신자 봉투 제안](https://github.com/nostr-protocol/nips/pull/2488)은 의도한 수신자가 event의 보이는 tag에 일반 공개 키를 드러내지 않고도 event를 찾을 수 있는 비공개 노트, 답장, 연결을 구상합니다. 공유 비밀 값에서 도출된 불투명한 쌍별 별칭 tag와 임시 event kind를 제안하며, 다른 Nostr event를 수백 명의 독자를 위해 감싸는 방법도 포함합니다. 이를 통해 작은 비공개 피드는 모든 멤버에게 메시지를 따로 보내는 것보다 더 직접적인 조회 경로를 얻을 수 있습니다.

[제안 작성자](https://github.com/nostr-protocol/nips/pull/2488)는 이것이 진행 중인 작업이라고 명시합니다. 초안에는 입증된 구현이나 보안 검토가 없으며, kind 할당과 바이트 수준의 서명 규칙이 아직 열려 있습니다.

### Blossom 제안이 다른 사람도 미러링된 미디어를 알릴 수 있게 함 {#a-blossom-proposal-lets-other-people-announce-mirrored-media}

[열린 NIP 제안](https://github.com/nostr-protocol/nips/pull/2478)은 다른 작성자의 Blossom blob을 미러링한 사람이 Nostr를 통해 그 사본을 알리는 방법을 설명합니다. 그러면 원래 서버가 blob을 잃었을 때 클라이언트가 사본을 찾을 수 있습니다. 논의에서는 공지된 서버 힌트가 오래되었을 때 미러의 현재 BUD-03 서버 목록을 확인하는 방안도 제기되었습니다. 이는 제안된 탐색 경로이며, 클라이언트나 아카이브 relay가 이미 대체 저장소를 제공한다는 보장이 아닙니다.

### 도로 event 보고가 공유 Nostr 형식을 모색 {#road-event-reports-seek-a-shared-nostr-format}

[열린 Road Event Reports 제안](https://github.com/nostr-protocol/nips/pull/2479)은 포트홀, 도로 폐쇄, 카메라, 기타 도로 상황에 대한 보고와 확인을 설명합니다. 위치 tag와, relay에 event 제공을 멈출 시점을 알려 주는 [NIP-40](/ko/topics/nip-40/)의 만료 타임스탬프를 사용하므로, 보고가 무기한 유효한 상태로 남을 필요가 없습니다. 작성자는 공개 relay에서 수집한 event 표본과 도로 상황 보고를 위한 기존 [Roadstr 클라이언트](https://github.com/jooray/roadstr)를 바탕으로 수정했지만, 초안에는 여전히 압축 인코딩 문제가 열려 있으며 제안된 NIP 번호는 채택되지 않았습니다.

### Marmot이 다중 기기 조율을 재검토 {#marmot-revisits-multi-device-coordination}

[Marmot의 다중 기기 재설계](https://github.com/marmot-protocol/marmot/pull/427)는 구현되지 않은 External Commit 초안을 초기 피드백을 위한 비규범적 안내로 대체합니다. 새 방향은 기존 기기가 새 기기를 승인하고, 대화에 참여시키고, 나중에 기기를 제거하는 방식을 탐구하며, 열린 질문을 계속 드러내 둡니다. 어떤 구현도 채택하지 않았으므로 제거된 초안이 예약했던 ID는 해제됩니다. 이 아이디어 문서는 새 ID나 유선 형식을 할당하지 않으며, 구현된 다중 기기 기능이 아닙니다.

## Nostr의 여섯 번의 9월 {#six-years-of-nostr-septembers}

9월의 마지막 호는 Nostr가 스케치에서 더 큰 규모의 상호 운용 가능한 도구 모음으로 옮겨 온 과정을 되짚어 볼 기회입니다. [2021년 승차 매칭 프로토타입](https://github.com/arcbtc/buber/commit/7a66d400f2)은 서명된 event로 서비스를 조율했습니다. 5년이 지난 지금, [신원 증명 문구](https://github.com/nostr-protocol/nips/commit/0046368a7)와 [목록 kind 충돌](https://github.com/nostr-protocol/nips/commit/6631b3eb1)이 유지관리자들이 해결하고 있는 종류의 세부 사항입니다. 그 사이에 클라이언트는 대화, 미디어, 복구를 일반 사용자가 쓸 수 있는 방식으로 보여 주는 법을 익혔습니다. 아래의 날짜가 있는 출처들은 그 진전의 단계를 보여 줍니다. 모든 실험이 출시되었다거나 각각의 오래된 설계가 여전히 권장된다는 것을 입증하지는 않습니다.

### 2021년 9월: 쓸모 있는 형태를 갖춘 초기 실험 {#september-2021-early-experiments-with-useful-shapes}

[9월 4일 BUber 커밋](https://github.com/arcbtc/buber/commit/7a66d400f2)은 Nostr event를 사용한 택시 매칭 개념을 탐구했습니다. 서명되어 relay로 전달되는 요청이 서비스 전체를 하나의 서버에 맡기지 않고도 사람들을 조율할 수 있음을 보여 주었습니다. 이 소스는 개념일 뿐이며, 출시된 승차 서비스를 입증하지는 않습니다.

같은 달 하순, [Loquaz의 9월 23일 소스](https://github.com/emeceve/loquaz/commit/d885d93d22)는 데스크톱 채팅 프로토타입을 선보였습니다. relay 메시지를 일반 애플리케이션처럼 느껴지게 하려는 또 하나의 초기 시도였습니다. 이 소스가 완성된 종단 간 암호화나 프로덕션 메신저를 입증하지는 않으며, 오래 이어진 흐름은 단순한 event 위에 쓸 만한 대화 인터페이스를 찾는 노력입니다. BUber는 승차 매칭을, Loquaz는 채팅을 시험했으며, 둘 다 공통 클라이언트 패턴이 자리 잡기 전에 서명된 event를 사용했습니다. 이러한 시도는 이후 클라이언트가 거듭 마주할 두 가지 문제, 즉 relay를 통한 조율과 event를 쓸 만한 대화로 보여 주는 문제를 펼쳐 놓았습니다.

### 2022년 9월: 채팅과 위임된 동작이 명세에 들어옴 {#september-2022-chat-and-delegated-actions-enter-the-specifications}

[9월 10일 NIP-28 변경](https://github.com/nostr-protocol/nips/commit/3423a6dfb)은 클라이언트가 함께 해석할 수 있는 메시지와 메타데이터를 갖춘 공개 채팅 채널을 설명했습니다. [NIP-28](/ko/topics/nip-28/)은 공유된 방을 명시적인 프로토콜 주제로 만들고 클라이언트에게 공통 채널 규약을 제공했습니다.

9월 23일, [NIP-26](/ko/topics/nip-26/)의 [위임 서명 문서](https://github.com/nostr-protocol/nips/commit/b62aa418d)는 한 키가 다른 키에게 제한된 event에 서명하도록 권한을 부여하는 방법을 문서화했습니다. 이는 2022년의 중요한 설계 질문, 즉 모든 애플리케이션에 주 키를 넘기지 않고 Nostr 신원을 사용하는 방법을 담고 있었습니다. [NIP-26은 현재 unrecommended로 표시되어 있으므로](https://github.com/nostr-protocol/nips/blob/master/26.md), 이는 실험의 기록이지 새로운 통합을 위한 조언이 아닙니다. 이후의 상태는 서명 모델이 어떻게 변해 왔는지 보여 줍니다. 제안된 답이 폐기되더라도 명세는 유용한 문제 정의를 보존할 수 있습니다.

### 2023년 9월: relay 탐색과 메타데이터를 중심으로 성숙해 가는 클라이언트 {#september-2023-clients-grow-up-around-relay-discovery-and-metadata}

Damus는 Nostr 소셜 클라이언트입니다. [9월 21일 변경 기록](https://github.com/damus-io/damus/blob/master/CHANGELOG.md#16-18---2023-09-21)에는 로컬 Nostr 데이터베이스, 검색, 해시태그 탐색에 대한 작업이 기록되어 있습니다. 이러한 변경은 휴대전화에서 바쁜 소셜 피드를 더 쉽게 탐색하고 복구할 수 있게 했습니다. 날짜가 있는 변경 기록은 해당 클라이언트 릴리스의 증거일 뿐, 이후 Damus의 모든 기능에 대한 증거는 아닙니다.

프로토콜 세부 사항도 움직이고 있었습니다. [9월 26일 변경](https://github.com/nostr-protocol/nips/commit/44c21c9d8)은 [NIP-24](/ko/topics/nip-24/)의 선택적 프로필 메타데이터 필드를 명확히 했고, [NIP-65의 9월 29일 변경](https://github.com/nostr-protocol/nips/commit/3b5d3ca67)은 relay URI 정규화와 중복 제거를 다뤘습니다. [NIP-65](/ko/topics/nip-65/)는 클라이언트가 읽기와 쓰기에 사용하는 relay를 게시하는 방법을 알려 주며, URI를 일관되게 처리하면 문자열이 무해한 방식으로 다르더라도 그 목록이 같은 relay를 가리키게 됩니다. 이 작은 규약은 클라이언트 설계를 신뢰할 수 있는 탐색 쪽으로 이끌었습니다. 누군가의 event를 찾으려면 그것이 어디에 게시되는지 알아야 하기 때문입니다.

### 2024년 9월: 게시물이 더 풍부한 맥락을 얻음 {#september-2024-posts-acquire-richer-context}

[Damus의 9월 22일 릴리스 노트](https://github.com/damus-io/damus/blob/master/CHANGELOG.md#1101---2024-09-22)는 [NIP-84](/ko/topics/nip-84/) 하이라이트와 댓글 지원을 설명했습니다. NIP-84는 독자가 장문 자료의 한 구절을 인용하고 논의할 수 있는 방법을 제공합니다. 이 클라이언트 작업은 프로토콜 아이디어가 사람들이 읽는 동안 사용할 수 있는 것이 되어 가는 과정을 보여 줍니다.

한편 [NIP-34](/ko/topics/nip-34/)는 Nostr를 통한 git 협업에서 이슈 제목과 레이블을 다듬는 [9월 20일 변경](https://github.com/nostr-protocol/nips/commit/ea36ec9ed)을 받았고, [NIP-73](/ko/topics/nip-73/)은 같은 날 외부 콘텐츠 식별자를 다듬는 [변경](https://github.com/nostr-protocol/nips/commit/79786bb7b)을 받았습니다. 이는 별개의 명세 변경입니다. 하나는 저장소의 이슈가 구조를 유지하도록 돕고, 다른 하나는 event가 Nostr 밖의 자료를 참조할 수 있게 합니다. 둘 다 콘텐츠가 커뮤니티, 저장소, 다른 매체 사이를 오갈 때 클라이언트가 보존할 수 있는 의미를 넓힙니다.

### 2025년 9월: 접근 제어와 결제 맥락이 더 정밀해짐 {#september-2025-access-controls-and-payment-context-become-more-precise}

[9월 6일 NIP-42 개정](https://github.com/nostr-protocol/nips/commit/4c5d5fff9)은 다중 사용자 relay 인증을 다뤘습니다. [NIP-42](/ko/topics/nip-42/)는 relay가 클라이언트에게 어떤 Nostr 키가 요청하는지 증명하도록 요구할 수 있게 하며, 이 업데이트는 같은 연결로 둘 이상의 인증된 계정을 지원하는 서비스에 중요했습니다.

[9월 15일 NIP-47 업데이트](https://github.com/nostr-protocol/nips/commit/400d975da)는 Nostr Wallet Connect 요청에 선택적 결제 메타데이터를 추가했습니다. [NIP-47](/ko/topics/nip-47/)은 앱이 Nostr를 통해 지갑에 작업을 요청할 수 있게 합니다. 더 많은 맥락은 지갑 상호 작용을 이해하기 쉽게 만들 수 있지만, 메타데이터가 결제자 정보를 드러낼 수 있으므로 클라이언트와 지갑은 여전히 이를 민감한 정보로 다뤄야 합니다. 이 변경은 상호 운용성 작업이 이제 요청이 전달될 수 있는지뿐 아니라 수신자가 무엇을 알게 되는지까지 포함하게 되었음을 보여 줍니다.

### 2026년 9월: 상호 운용성 세부 사항이 공개 신원과 만남 {#september-2026-interoperability-details-meet-public-identity}

올해 9월, [병합된 NIP-51 변경](https://github.com/nostr-protocol/nips/commit/6631b3eb1)은 팔로우 세트 event kind를 충돌에서 벗어나게 옮겼습니다. [NIP-51](/ko/topics/nip-51/)은 사람이 관리하고 공유할 수 있는 목록을 정의하며, 고유한 event kind는 클라이언트가 목록 유형을 서로 구별할 수 있게 합니다. 이전 Compass 호에서 이 제안을 다뤘으며, 9월의 병합은 상태 변화입니다.

두 번째로 [병합된 NIP-39 변경](https://github.com/nostr-protocol/nips/commit/0046368a7)은 증명 문구를 명확히 하고 외부 계정을 Nostr 신원과 연결하는 방법을 더 추가했습니다. [NIP-39](/ko/topics/nip-39/)는 중앙 신원 등록소가 아니라 확인 가능한 신원 클레임에 관한 것입니다. 두 병합은 함께, 현재의 프로토콜 작업이 독립적인 클라이언트들이 같은 신원 및 목록 event를 올바르게 해석하는지를 좌우하는 작은 세부 사항에 집중하고 있음을 보여 줍니다. 또한 새로운 event 범주를 고안하는 데서 기존 범주의 모호함을 줄이는 쪽으로의 전환도 보여 줍니다.

여섯 번의 9월을 거치며 드러나는 흐름은 [서명된 event가 애플리케이션 요청을 기술할 수 있음](https://github.com/arcbtc/buber/commit/7a66d400f2)을 증명하던 단계에서, [클라이언트가 사람에 대한 클레임을 어떻게 검증하는지](https://github.com/nostr-protocol/nips/commit/0046368a7)를 묻는 단계로의 진전입니다. 오래된 프로토타입이 중요한 이유는 이후의 명세와 클라이언트가 답해야 했던 질문, 즉 누가 서명하는지, event를 어디서 찾는지, 그것이 무엇을 의미하는지, 그리고 누군가 그것을 신뢰해야 할지 어떻게 아는지를 드러내기 때문입니다. 작고 정밀한 프로토콜 정정이 새로운 인터페이스만큼 중요할 수 있는 이유도 여기에 있습니다.

