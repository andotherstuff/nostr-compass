---
title: 'Nostr Compass #10'
date: 2026-02-18
translationOf: /en/newsletters/2026-02-18-newsletter.md
translationDate: 2026-02-18
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** 독립적인 프로젝트들이 Android 오프라인 미디어 접근 문제에 수렴하면서 Blossom 로컬 캐시 레이어가 형태를 갖춰가고 있습니다. Alby가 실제 자금 위험 없이 Nostr Wallet Connect 통합을 구축하고 테스트할 수 있는 [NWC 개발자 샌드박스](https://sandbox.albylabs.com)를 출시했습니다. AI 에이전트의 Nostr 통신을 위한 경쟁적인 제안들이 같은 주에 두 저자로부터 도착했습니다. fiatjaf가 relay 운영자들이 채택하지 않은 보존 정책, 국가 코드, 개인정보 처리방침, 커뮤니티 환경설정 tag를 제거하며 [NIP-11](https://github.com/nostr-protocol/nips/pull/1946)에서 사용되지 않는 필드를 제거했습니다. [NIP-85](https://github.com/nostr-protocol/nips/pull/2223)가 Trusted Assertions의 서비스 제공자 검색 안내를 포함하며 병합되었습니다. [NIP-52](https://github.com/nostr-protocol/nips/pull/1752)의 새로운 `D` tag가 캘린더 event의 일 단위 타임스탬프 인덱싱을 가능하게 합니다. 새 프로젝트로는 탈중앙화 지도 타일 배포를 위한 [Mapnolia](https://github.com/zeSchlausKwab/mapnolia), MLS 암호화 메시징을 위한 [Pika](https://github.com/sledtools/pika), Android용 FROST 임계값 서명을 위한 [Keep](https://github.com/privkeyio/keep-android), Nostr 통합 콘텐츠 주소 지정 저장소인 [Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree), Android 어떤 앱에서든 Nostr로 콘텐츠를 공유할 수 있는 [Prism](https://github.com/hardran3/Prism)이 있습니다. [Primal Android](https://github.com/PrimalHQ/primal-android-app)가 듀얼 지갑 지원과 자동 서비스 수명 주기를 추가하는 11개의 NWC PR을 병합했습니다. [Mostro Mobile](https://github.com/MostroP2P/mobile)이 NWC 통합을 통한 [내장 Lightning 지갑](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2)을 출시했습니다. [Notedeck](https://github.com/damus-io/notedeck)이 Android 앱 스토어 릴리스를 준비하는 동안, HAVEN은 다중 npub 지원과 클라우드 백업을 갖춘 [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3)에 도달했습니다. 이번 주 심층 분석은 Web of Trust 계산을 서비스 제공자에게 위임하는 NIP-85의 Trusted Assertions 시스템과, 일 단위 인덱싱 업데이트 이후의 NIP-52 캘린더 Events 프로토콜을 다룹니다.

## 뉴스

### Blossom 로컬 캐시 레이어 등장

여러 독립 프로젝트가 같은 문제, 즉 모바일 기기에서 [Blossom](/ko/topics/blossom/) 미디어에 오프라인으로 접근하는 문제에 수렴하고 있습니다.

[Morganite](https://github.com/greenart7c3/Morganite)는 [Amber](https://github.com/greenart7c3/amber)와 [Citrine](https://github.com/greenart7c3/Citrine)을 만든 greenart7c3의 새 Android 앱으로, Blossom 미디어를 위한 클라이언트 측 캐싱을 구현합니다. 사용자는 네트워크 연결 없이 이전에 본 이미지와 파일에 접근할 수 있습니다.

[Aerith](https://github.com/hardran3/Aerith)가 이미지 라벨링, 대량 미러/태그/삭제 작업, 라벨과 파일 유형별 필터링, 초기 로컬 Blossom 캐시 지원을 갖춘 [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2)를 출시했습니다. Aerith는 여러 Blossom 서버에 미디어를 저장하고 blob을 정리하고 미러링해야 하는 사용자를 위한 관리 인터페이스입니다.

Blossom 명세의 새로운 [로컬 캐시 구현 가이드](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)가 클라이언트 측 blob 저장소를 문서화하고, Aerith와 같은 개발자가 만든 [Prism](https://github.com/hardran3/Prism)이 Android 공유-Nostr 흐름에 Blossom 업로드 통합을 추가합니다. 이번 주 네 개의 독립 프로젝트가 같은 문제에 수렴했습니다: 전용 캐싱 앱, 미디어 관리자, 참조 명세, Blossom 통합 공유 도구가 모두 단순 업로드-검색을 넘어선 영구 로컬 저장소를 구현하고 있습니다.

### Alby NWC 개발자 샌드박스

[Alby](https://sandbox.albylabs.com)가 [Nostr Wallet Connect (NIP-47)](/ko/topics/nip-47/)로 개발하는 개발자를 위한 샌드박스 환경을 출시했습니다. 이 샌드박스는 개발자가 실제 Lightning 지갑에 연결하지 않고 테스트 연결을 생성하고 시뮬레이션 결제를 보내면서 NWC event의 전체 요청/응답 사이클을 실시간으로 관찰할 수 있는 호스팅 NWC 지갑 서비스를 제공합니다. 개발자가 샌드박스에서 `nostr+walletconnect://` 연결 문자열을 생성하여 클라이언트에 전달하면, 샌드박스가 클라이언트와 지갑 서비스 사이를 오가는 kind 23194 요청과 kind 23195 응답 event를 보여줍니다.

이로써 새로운 NWC 통합의 진입 장벽이 낮아집니다. 이전에는 테스트를 위해 개인 Lightning 지갑이나 자체 호스팅 NWC 서비스가 필요했습니다. 샌드박스는 이를 추상화하여 개발자에게 라이브 NWC 엔드포인트에 대한 `pay_invoice`, `get_balance`, `make_invoice`, `lookup_invoice`, `list_transactions` 메서드를 구현하기 위한 즉각적인 피드백 루프를 제공합니다.

### AI 에이전트 NIP 등장

Nostr에서의 AI 에이전트 통신을 위한 제안들이 며칠 간격으로 서로 다른 접근 방식으로 등장했습니다.

joelklabo의 [NIP-XX: AI 에이전트 메시지](https://github.com/nostr-protocol/nips/pull/2226)는 AI 에이전트 상호작용을 위한 완전한 프로토콜을 정의합니다: 프롬프트, 응답, 스트리밍 델타, 상태 업데이트, 도구 텔레메트리, 오류, 취소, 기능 검색을 위한 event kind들입니다. `ai.info` 검색 event (kind 31340, 교체 가능)는 에이전트가 지원하는 모델, 스키마가 있는 도구, 스트리밍 지원, 속도 제한을 알릴 수 있게 합니다. joelklabo의 제안에는 프롬프트 ID를 통한 실행 상관관계, 세션 관리, 시퀀스 순서를 갖춘 스트림 조정, 메타데이터 프라이버시를 위한 [NIP-59](/ko/topics/nip-59/) 안내가 포함됩니다.

pablof7z의 [NIP-AE: 에이전트](https://github.com/nostr-protocol/nips/pull/2220)는 다른 접근 방식을 취하며, 에이전트 인스턴스화를 위한 kind인 정의와 레슨을 정의합니다. 이는 Nostr 위에 구축된 자율 학습 시스템인 [TENEX](https://github.com/tenex-chat/tenex)에서 pablof7z가 사용하는 event 유형입니다. pablof7z의 또 다른 제안인 [NIP-AD: MCP 서버 및 스킬 공지](https://github.com/nostr-protocol/nips/pull/2221)는 Nostr에서 [Model Context Protocol](https://modelcontextprotocol.io/) 서버와 스킬을 알리는 event를 정의합니다. [NIP-22](/ko/topics/nip-22/) 댓글이 지원되므로 커뮤니티가 Nostr에서 직접 MCP 서버를 논의하고 평가할 수 있습니다.

NIP-XX는 완전한 에이전트 통신을 다루고 NIP-AE와 NIP-AD는 신원과 도구 검색을 다룹니다. 이 제안들은 통합된 표준으로 수렴되거나 보완적인 레이어로 공존할 수 있습니다.

## 릴리스

### HAVEN v1.2.0-rc3

네 가지 relay 기능과 [Blossom](/ko/topics/blossom/) 미디어 서버를 번들로 제공하는 올인원 개인 relay인 [HAVEN](https://github.com/bitvora/haven)이 [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3)에 도달했습니다. 이 릴리스 후보는 여러 npub 지원을 추가하여 단일 HAVEN 인스턴스가 여러 Nostr 신원을 서비스할 수 있게 합니다. 이전 RC들은 클라우드 백업을 위한 `--from-cloud` 및 `--to-cloud` 플래그 (RC2)와 Web of Trust 이중 카운팅 버그 수정 (RC1)을 추가했습니다.

### Mostro Mobile v1.2.0: 내장 Lightning 지갑

[Mostro](https://github.com/MostroP2P/mostro) P2P Bitcoin 거래소의 모바일 클라이언트인 [Mostro Mobile](https://github.com/MostroP2P/mobile) ([v1.1.0은 지난주 다뤘습니다](/ko/newsletters/2026-02-11-newsletter/#mostro-첫-퍼블릭-베타-출시))이 완전한 [NWC (NIP-47)](/ko/topics/nip-47/) 통합을 통한 내장 Lightning 지갑으로 [v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2)을 출시했습니다. 이제 구매자와 판매자는 인보이스를 처리하기 위해 앱을 전환할 필요가 없습니다. 앱이 판매자를 위한 홀드 인보이스를 감지하고 연결된 지갑을 통해 자동으로 결제하며, 구매자는 자동 인보이스 생성을 받습니다. 이 릴리스는 같은 주 초에 출시된 [v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1)에 이어지는 것으로, v1.1.1은 신뢰할 수 있는 인스턴스의 큐레이션 레지스트리를 갖춘 다중 Mostro 노드 지원, 노드 표시를 위한 kind 0 메타데이터 가져오기, pubkey로 사용자 지정 노드 관리, 선택한 노드가 오프라인 상태일 때 자동 폴백을 추가했습니다.

서버 측에서는 중복 개발 수수료 결제 수정, 비밀번호 검증 RPC 엔드포인트의 속도 제한, 협력적 취소 시 분쟁 정리를 포함하는 [Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2)가 출시되었습니다.

새 동반 프로젝트인 [mostro-skill](https://github.com/MostroP2P/mostro-skill)은 에이전트가 Nostr를 통해 Mostro에서 거래할 수 있게 합니다.

### Aerith v0.2

[Blossom](/ko/topics/blossom/) 이미지 관리자인 [Aerith](https://github.com/hardran3/Aerith)가 미디어 정리를 위한 이미지 라벨, 서버 전반의 대량 미러/태그/삭제 작업, 라벨과 파일 유형별 필터링, 초기 로컬 캐시 지원을 갖춘 [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2)를 출시했습니다. 더 넓은 로컬 캐시 트렌드에 대한 맥락은 [뉴스 섹션](#blossom-로컬-캐시-레이어-등장)을 참조하세요.

### Mapnolia: Nostr를 통한 탈중앙화 지도 타일

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia)는 [PMTiles](https://github.com/protomaps/PMTiles) 지도 아카이브를 지리적 영역으로 청크로 나누고 탈중앙화 검색을 위해 Nostr를 통해 알리는 새로운 지리공간 데이터 서버입니다. 레이어 메타데이터, 지오해시 영역, 파일 참조, [Blossom](/ko/topics/blossom/) 서버 세부 정보가 포함된 지도 타일 청크의 완전한 인덱스를 담은 kind 34444 매개변수화된 교체 가능 event를 Nostr relay에 게시합니다.

클라이언트는 중앙화된 타일 서버 대신 Nostr 네트워크를 통해 지도 데이터를 검색하고 가져오며, 공지 event가 나열된 Blossom 서버에서 필요한 지리적 영역만 요청하기에 충분한 메타데이터를 담고 있습니다. Mapnolia는 Nostr에 지리공간 데이터 배포를 처음으로 도입한 프로젝트로, 오프라인 지원 지도 애플리케이션의 가능성을 열어줍니다.

### Pika: Marmot 기반 암호화 메시징

[Pika](https://github.com/sledtools/pika)는 Nostr relay 위에 [메시징 레이어 보안 (MLS)](/ko/topics/mls/)을 레이어링하는 [Marmot](/ko/topics/marmot/) 프로토콜을 사용하는 iOS와 Android용 새로운 엔드투엔드 암호화 메시징 앱입니다. 아키텍처는 Nostr relay를 통해 MLS 상태 관리와 메시지 암호화/복호화를 처리하는 Rust 코어 (`pika_core`)와 SwiftUI (iOS) 및 Kotlin (Android)의 얇은 네이티브 UI 셸로 우려 사항을 분리합니다. 상태는 단방향으로 흐릅니다: UI가 Rust 액터에게 액션을 발송하면, Rust 액터가 상태를 변경하고 UniFFI와 JNI 바인딩을 통해 UI로 개정 번호가 있는 스냅샷을 내보냅니다.

Pika는 [White Noise](https://github.com/marmot-protocol/whitenoise), [Vector](https://github.com/VectorPrivacy), [0xchat](https://0xchat.com)과 함께 성장하는 MLS-on-Nostr 메신저 분야에 합류합니다. 모두 MLS 암호화된 암호문의 전송 레이어로 Nostr relay를 사용하여, relay 운영자가 메시지 내용을 읽을 수 없게 합니다. Pika는 MLS 구현에 Marmot Development Kit (MDK)를, relay 연결성에 nostr-sdk를 사용합니다.

### Keep: Android용 [FROST](/ko/topics/frost/) 임계값 서명

[Keep](https://github.com/privkeyio/keep-android)은 어떤 단일 기기도 완전한 개인 키를 보유하지 않는 [FROST](/ko/topics/frost/) 임계값 서명을 위한 새로운 Android 애플리케이션입니다. [NIP-55](/ko/topics/nip-55/) (Android 서명자)와 [NIP-46](/ko/topics/nip-46/) (원격 서명)을 구현하므로 호환 가능한 Nostr 클라이언트가 키 자료가 기기 전반에 분산된 상태로 서명을 요청할 수 있습니다. 기본 구성은 2-of-3 및 3-of-5이지만, 어떤 t-of-n 임계값도 지원됩니다.

Keep의 분산 키 생성 (DKG) 세레모니는 사용자 지정 event kind를 사용하여 Nostr relay를 통해 실행됩니다: 그룹 공지를 위한 kind 21101, 1라운드 커밋먼트 다항식을 위한 kind 21102 (공개 방송), 2라운드 비밀 공유를 위한 kind 21103 (참가자 간 [NIP-44](/ko/topics/nip-44/) 암호화 점대점). 그룹 개인 키 스칼라는 DKG 중 어디서도 계산되거나 조합되지 않습니다. 각 기기는 다항식 평가 몫만 보유하며, t개의 몫이면 2라운드 커밋-서명 프로토콜을 통해 유효한 Schnorr 서명을 생성할 수 있습니다. 결과 64바이트 서명은 단일 서명자 Schnorr 서명과 구별할 수 없습니다. 내부적으로 Keep은 Taproot 조정이 있는 Zcash 재단의 `frost-secp256k1-tr` 크레이트를 사용하므로, 그룹 공개 키가 Nostr npub으로 직접 작동합니다.

Keep은 [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), [Android용 Igloo](https://github.com/FROSTR-ORG/igloo-android), [Frost2x](https://github.com/FROSTR-ORG/frost2x), [iOS용 Igloo](https://github.com/FROSTR-ORG/igloo-ios)와 함께 [Frostr](https://frostr.org) 프로젝트 패밀리에 합류하여 Nostr에서의 임계값 키 관리 옵션을 확장합니다.

### Prism: Android에서 어디서든 Nostr로 공유

[Prism](https://github.com/hardran3/Prism)은 시스템 공유 대상으로 등록하는 새로운 Android 앱 (Kotlin/Jetpack Compose, API 26+)으로, 사용자가 폰의 어떤 앱에서든 텍스트, URL, 이미지, 동영상을 Nostr에 게시할 수 있게 합니다. 공유된 URL은 노트로 작성되기 전에 추적 파라미터 제거기를 통과합니다. Prism은 풍부한 링크 미리보기를 생성하기 위해 OpenGraph 메타데이터를 가져오고 네이티브 Nostr 참조 (`note1`, `nevent1`)를 인라인으로 렌더링합니다.

스케줄링 엔진은 Android 배터리 최적화를 우회하기 위해 하이브리드 `AlarmManager`/`WorkManager` 방식을 사용합니다: AlarmManager가 정밀한 깨우기 타이밍을 처리하고 expedited WorkManager 작업이 전달을 보장하며, 오프라인 시나리오에 대한 지수 백오프 재시도가 있습니다. 미디어 업로드는 이미지와 동영상 프레임의 썸네일 생성과 함께 구성 가능한 [Blossom](/ko/topics/blossom/) 서버를 통해 이루어집니다. 모든 event 서명은 [Amber](https://github.com/greenart7c3/amber)와 같은 [NIP-55](/ko/topics/nip-55/) 외부 서명자에게 위임되며, 신원 전환을 위한 다중 계정 지원이 있습니다. Prism은 [NIP-84 (하이라이트)](/ko/topics/nip-84/) 게시도 지원합니다. [Aerith](#aerith-v02)와 같은 개발자 작품입니다.

### Hashtree: Nostr 통합 콘텐츠 주소 지정 저장소

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree)는 Nostr에 Merkle 루트를 게시하여 변경 가능한 npub/경로 주소를 생성하는 파일시스템 기반 콘텐츠 주소 지정 blob 저장 시스템입니다. 이 시스템은 [Blossom](/ko/topics/blossom/) 업로드에 최적화된 2MB 블록으로 콘텐츠를 청크로 나누는 어떤 키-값 저장소에서도 작동하는 "덤 스토리지"를 사용합니다. BitTorrent와 달리 활성 Merkle 증명 계산이 필요 없으며, 단순히 해시로 blob을 저장하고 검색하면 됩니다.

Nostr 통합을 통해 레포지토리 클론을 위한 `htree://npub.../repo-name`과 같은 git 원격 URL이 가능하며, `htree publish mydata <hash>`와 같은 명령으로 콘텐츠 해시를 `npub.../mydata` 주소에 게시합니다. 포괄적인 CLI는 암호화 (기본값)와 공개 저장소 모드, 콘텐츠 핀닝, Blossom 서버 푸시, Nostr 신원 관리를 지원합니다. 저장된 각 항목은 원시 바이트 또는 트리 노드이며, Nostr relay 네트워크를 통한 탈중앙화 콘텐츠 배포의 기반을 제공합니다.

### Espy: Shakespeare에서의 색상 팔레트 캡처

[Shakespeare](https://soapbox.pub/tools/shakespeare/) 플랫폼 위에 구축된 [Espy](https://espy.you)는 사용자가 사진에서 색상 팔레트를 캡처하고 Nostr event로 공유할 수 있게 합니다. Shakespeare는 NIP-07 브라우저 확장을 통해 사용자를 인증하고 내장 Nostr relay 연결성을 제공하는 AI 기반 앱 빌더로, 개발자가 자체 키 관리나 relay 풀을 구현하지 않고 앱을 출시할 수 있습니다. Espy는 카메라 입력에서 지배적인 색상을 표준 Nostr 피드를 통해 검색 가능한 공유 가능한 팔레트 카드로 추출합니다.

### Flotilla 1.6.4

relay를 그룹으로 정리하는 hodlbod의 Discord 유사 Nostr 클라이언트인 [Flotilla](https://gitea.coracle.social/coracle/flotilla)가 [1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4)를 출시했습니다. Coracle 프로젝트 패밀리는 GitHub에서 자체 호스팅 [Gitea 인스턴스](https://gitea.coracle.social/coracle)로 마이그레이션했습니다. 이 릴리스는 NIP-9a를 통한 푸시 알림과 지갑 수신 흐름, 분류 목록과 공간 URL 지원을 추가합니다. 인터페이스 개선에는 정리된 모달과 알림 처리가 포함됩니다. 방 음소거와 모바일 안전 영역 인셋, Safari 이미지 업로드와 캘린더 event 세부 정보 수정이 변경 사항을 완성합니다.

### Shosho v0.12.0

Nostr 통합이 있는 모바일 라이브 스트리밍 앱인 [Shosho](https://github.com/r0d8lsh0p/shosho-releases)가 [v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0)을 출시했습니다. 이 릴리스는 인플레이어 답글과 사용자 정의 이모지 통합이 있는 동영상 Clips를 추가합니다. 스레드 보호가 간접 언급 스팸을 차단하고, 새로운 QR 공유 기능으로 사용자가 오프라인으로 프로필을 교환할 수 있습니다. 새로운 가로 재생 모드가 스트림에 Twitch 스타일 시청 경험을 제공하며, 탐색 화면이 라이브 스트림과 함께 크리에이터 클립을 제공합니다.

### Granary v10.0

Nostr, Bluesky, ActivityPub 및 기타 플랫폼 간의 데이터를 공통 형식으로 변환하는 소셜 웹 번역 라이브러리인 [Granary](https://github.com/snarfed/granary)가 주요 변경 사항과 함께 [v10.0](https://github.com/snarfed/granary/releases/tag/v10.0)을 출시했습니다. 이 릴리스는 Nostr의 기본 ActivityStreams 1 ID를 bech32에서 hex로 전환하고 [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) 언급 파싱 및 아티클 태그를 포함한 확장된 Nostr 지원을 추가합니다. 변환기 전반의 새로운 다중 출력 옵션으로 개발자가 프로토콜 간 번역을 배치로 수행할 수 있습니다.

### Nostr MCP Server v3.0.0

AI 에이전트가 Nostr 네트워크와 상호작용할 수 있게 하는 [Model Context Protocol](https://modelcontextprotocol.io/) 서버인 [Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server)가 [v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0)을 출시했습니다. 이 주요 릴리스는 소셜 액션 (팔로우, 리액션, 리포스트, 답글)과 [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) 지원 및 선택적 [NIP-42](/ko/topics/nip-42/) 인증이 있는 relay 목록 관리를 추가합니다. [NIP-17](/ko/topics/nip-17/)과 [NIP-44](/ko/topics/nip-44/)를 통한 다이렉트 메시지도 새롭게 추가되었습니다. 이 릴리스는 Nostr에서 운영하는 에이전트를 위한 실용적인 도구로서 이번 주 [AI 에이전트 NIP 제안](#ai-에이전트-nip-등장)과 짝을 이룹니다.

### Aegis v0.3.8

크로스 플랫폼 Nostr 서명자인 [Aegis](https://github.com/ZharlieW/Aegis)가 다국어 UI 지원과 내장 Nostr 앱 브라우저를 위한 점진적 업데이트 관리자를 갖춘 [v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8)을 출시했습니다. 새 업데이트 메커니즘은 로컬 상태에 대해 점진적으로 diff를 적용하여, 낮은 대역폭 사용으로 인앱 Nostr 웹 앱 디렉토리를 최신 상태로 유지합니다. 이 릴리스는 또한 연속으로 여러 event에 서명할 때 데이터베이스 왕복을 줄이기 위한 5분 키 자료 캐싱을 도입합니다.

### SNSTR v0.3.1

Nostr 프로토콜을 위한 TypeScript 라이브러리인 [SNSTR](https://github.com/AustinKelsay/snstr) (Secure Nostr Software Toolkit for Renegades)이 [v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1)을 출시했습니다. 이 릴리스는 모든 진입점이 npm tarball에 포함되도록 보장하는 패키지 검증 가드를 추가하며, Node와 Bun에 대한 CI 적용이 있습니다. [v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0)도 같은 주에 출시되었습니다.

### Citrine v2.0.0-pre1

greenart7c3의 Android Nostr relay인 [Citrine](https://github.com/greenart7c3/Citrine)이 최적화된 데이터베이스 인덱스와 개선된 Kotlin 코루틴 처리를 통한 성능 향상과 함께 [v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1)을 릴리스했습니다. 이 릴리스는 또한 웹 앱 호스팅 지원을 강화하며, 이제 각 앱이 자체 포트에서 실행됩니다.

## 프로젝트 업데이트

### Primal Android: NWC 인프라 확장

[Primal Android](https://github.com/PrimalHQ/primal-android-app)가 이번 주 11개의 NWC 관련 PR을 병합했으며, [2주 전 시작된](/ko/newsletters/2026-02-04-newsletter/#primal-android-nwc-암호화-출시) 빌드아웃을 계속하고 있습니다. 이 배치는 듀얼 지갑 NWC 지원, 백엔드 알림과 연동된 자동 서비스 시작/중지, 지갑 유형별 연결 라우팅, 지갑 삭제 시 적절한 데이터 정리를 추가합니다. NWC 서비스는 이제 지갑 연결 상태에 따라 자체 수명 주기를 관리하여 사용자의 수동 개입을 줄입니다.

### Notedeck: Android 앱 스토어 준비

Damus의 멀티 플랫폼 Nostr 클라이언트인 [Notedeck](https://github.com/damus-io/notedeck)이 이번 주 [Android 앱 스토어 릴리스 준비](https://github.com/damus-io/notedeck/pull/1287)를 병합했습니다. 이 PR은 Google Play에서 요구하는 UGC (사용자 생성 콘텐츠) 준수 계획을 추가합니다. 여기에는 서비스 약관 동의 화면, 컨텍스트 메뉴와 설정을 통한 사용자 차단, relay에 신고 event를 게시하는 [NIP-56 (신고)](/ko/topics/nip-56/) 기능, 콘텐츠 및 안전 설정 섹션이 포함됩니다. 새 Makefile 대상을 통해 서명된 릴리스 APK와 AAB (Android App Bundle)를 생성하기 위한 빌드 인프라가 추가되었습니다. EULA 문서가 17세 이상 연령 요건과 탈중앙화 콘텐츠에 관한 Nostr 특화 면책 조항을 확립합니다. 준수 기능 자체는 후속 PR에서 출시됩니다. 이 병합은 문서화와 서명 토대를 마련합니다.

Damus iOS 측에서는 콘텐츠가 로드된 후에도 스피너가 무한히 지속되는 [무한 로딩 스피너 회귀 수정](https://github.com/damus-io/damus/pull/3593)이 이루어졌습니다.

### Nostria: 검색 Relay 및 DM 수정

글로벌 규모에 집중한 크로스 플랫폼 Nostr 클라이언트인 [Nostria](https://github.com/nostria-app/nostria)가 이번 주 9개의 PR을 병합했습니다. 가장 주목할 만한 것은 프로필 검색을 위한 [검색 Relay 자동 초기화](https://github.com/nostria-app/nostria/pull/460)를 추가하여, 새 사용자가 수동 설정 없이 relay 연결성을 갖출 수 있게 합니다. 다른 수정 사항으로는 [DM 텍스트영역 줄바꿈](https://github.com/nostria-app/nostria/pull/466), [전체 화면 동영상 뷰포트 채우기](https://github.com/nostria-app/nostria/pull/479), [리포스트 미리보기의 아티클 메타데이터 추출](https://github.com/nostria-app/nostria/pull/481), [알림의 nostr: URI 해석](https://github.com/nostria-app/nostria/pull/458)이 있습니다.

### Camelus: Riverpod v3 마이그레이션

Flutter 기반 Nostr 클라이언트인 [Camelus](https://github.com/camelus-hq/camelus)가 이번 주 [Riverpod v3 API 마이그레이션](https://github.com/camelus-hq/camelus/pull/158)과 [일반 피드 리팩토링](https://github.com/camelus-hq/camelus/pull/159)을 중심으로 5개의 PR을 병합했습니다. [임베드 노트 캐시](https://github.com/camelus-hq/camelus/pull/161)가 인용 노트에 대한 중복 relay 가져오기를 방지합니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-85: 서비스 제공자 검색 가능성](https://github.com/nostr-protocol/nips/pull/2223)**: vitorpamplona가 relay 힌트와 알고리즘별 서비스 키를 포함하여 [NIP-85 Trusted Assertions](/ko/topics/nip-85/) 서비스 제공자에 대한 클라이언트 검색 안내를 추가했습니다. 전체 내용은 [아래 심층 분석](#nip-심층-분석-nip-85-trusted-assertions)을 참조하세요.

- **[NIP-11: Relay 정보 정리](https://github.com/nostr-protocol/nips/pull/1946)**: fiatjaf가 [NIP-11](/ko/topics/nip-11/)에서 `privacy_policy`, `retention` 배열, `relay_countries`, 커뮤니티 환경설정 블록을 제거했습니다. Relay 운영자들이 이 필드들을 거의 채우지 않았고 클라이언트들도 이에 반응하지 않았습니다.

- **[NIP-52: 일 단위 타임스탬프 태그](https://github.com/nostr-protocol/nips/pull/1752)**: staab가 [NIP-52](/ko/topics/nip-52/) 시간 기반 캘린더 event (kind 31923)에 `floor(unix_seconds / 86400)`으로 계산된 일 단위 Unix 타임스탬프를 나타내는 필수 `D` tag를 추가했습니다. 여러 `D` tag가 다중 일 event를 포함하여, 전체 타임스탬프를 파싱하지 않고 효율적인 시간적 인덱싱을 가능하게 합니다.

- **[NIP-47: 단순화](https://github.com/nostr-protocol/nips/pull/2210)**: [뉴스레터 #9에서 논의된](/ko/newsletters/2026-02-11-newsletter/#nip-업데이트) 단순화 PR이 이번 주 병합되어 [NIP-47 (Nostr Wallet Connect)](/ko/topics/nip-47/)에서 `multi_pay_invoice`와 `multi_pay_keysend`를 제거했습니다. 전체 NWC 프로토콜 심층 분석은 [뉴스레터 #8](/ko/newsletters/2026-02-04-newsletter/#nip-심층-분석-nip-47-nostr-wallet-connect)을 참조하세요.

**오픈 PR 및 논의:**

- **[NIP-74: 팟캐스트](https://github.com/nostr-protocol/nips/pull/2211)**: [뉴스레터 #8에서 다룬](/ko/newsletters/2026-02-04-newsletter/) 이 팟캐스트 명세 제안이 이번 주 열띤 논의를 보았습니다. staab는 이미 야생에서 경쟁하는 최소 세 개의 팟캐스트 표준이 존재한다고 언급했으며, derekross는 활성 앱과 팟캐스트가 있는 기존 6개월 된 구현을 지적했습니다. NIP 번호가 배정되기 전에 구현 간 수렴이 필요합니다.

- **[NIP-XX: AI 에이전트 메시지](https://github.com/nostr-protocol/nips/pull/2226)**: joelklabo가 프롬프트, 응답, 스트리밍, 도구 텔레메트리, 오류, 기능 검색을 위한 event kind가 있는 완전한 AI 에이전트 통신 프로토콜을 제안합니다. 이번 주 모든 AI 제안에 대한 내용은 [뉴스 섹션](#ai-에이전트-nip-등장)을 참조하세요.

- **[NIP-PNS: 개인 노트 저장소](https://github.com/nostr-protocol/nips/pull/1893)**: jb55의 개인 노트 시스템이 누가 작성했는지 드러내지 않고 relay에 암호화된 개인 노트를 저장하기 위한 kind 1080 event를 정의합니다. 이 체계는 HKDF를 통해 사용자의 nsec에서 결정론적 가명 키쌍을 유도합니다: `pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`, 그런 다음 그 유도 키에서 secp256k1 키쌍을 생성합니다. 두 번째 유도가 대칭 암호화 키를 생성합니다: `pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`. 내부 노트는 이 키로 [NIP-44](/ko/topics/nip-44/) v2로 암호화되고 가명 pubkey 하에 게시되므로, relay는 사용자의 메인 키와 연결되지 않은 신원에서 kind 1080 event를 봅니다. [NIP-59](/ko/topics/nip-59/) 선물 포장과 달리 PNS는 스팸이 불가능하며 (가명 키가 무작위가 아닌 결정론적), 공개 메타데이터를 전혀 전달하지 않습니다 (수신자가 없으므로 `p` tag가 필요 없음). 이번 주 jb55가 Notedeck의 Rust 백엔드 (`enostr::pns` 모듈)에 PNS를 구현하면서 발견한 것들을 게시했습니다. 명세의 `hkdf_extract` 호출이 RFC 5869 HKDF에 두 단계 (Extract와 Expand)가 있고 대부분의 라이브러리가 둘 다 예상하기 때문에 모호하다는 점을 확인했습니다. `pns_nip44_key`가 NIP-44의 일반적인 ECDH 키 합의를 우회하고 대화 키로 직접 사용된다고 명확히 했으며, 대부분의 NIP-44 라이브러리가 기본적으로 ECDH를 사용하므로 구현자가 알아야 할 세부 사항입니다. 참조 구현의 TypeScript에서 정의되지 않은 변수도 표시했습니다. 2025년 4월부터 있던 이 PR이 이제 적극적으로 구현되고 있습니다.

- **[NIP-AE: 에이전트](https://github.com/nostr-protocol/nips/pull/2220)**: pablof7z가 [TENEX](https://github.com/tenex-chat/tenex)에서의 작업을 바탕으로 Nostr에서의 에이전트 신원을 위한 네 가지 event kind를 정의합니다. 기본 템플릿은 kind 4199 (에이전트 정의)로, 제목, 역할 설명, 시스템 지침, 도구 선언, 버전을 담습니다. 행동 수정자는 kind 4201 (에이전트 넛지)에 있으며, 런타임 기능 제어를 위한 `only-tool`, `allow-tool`, `deny-tool` tag를 사용합니다. 에이전트는 학습한 것을 kind 4129 (에이전트 레슨) event로 게시하며, 카테고리화되고 `e` tag를 통해 부모 정의로 연결되고 [NIP-22](/ko/topics/nip-22/) 댓글 스레드를 통해 정제될 수 있습니다. 소유권 검증은 kind 14199를 사용하며, 인간 운영자가 에이전트 pubkey를 나열하는 교체 가능 event로, 에이전트의 kind 0 프로필 `p` tag와 매칭될 때 양방향 체인을 확립합니다.

- **[NIP-AD: MCP 서버 및 스킬 공지](https://github.com/nostr-protocol/nips/pull/2221)**: pablof7z가 Nostr에서 [Model Context Protocol](https://modelcontextprotocol.io/) 서버와 개별 스킬을 알리는 event를 정의합니다. MCP 서버 공지는 서버의 엔드포인트 URL과 지원되는 프로토콜 버전을 입력 스키마가 있는 사용 가능한 도구 목록과 함께 담습니다. 서버 공지에 [NIP-22](/ko/topics/nip-22/) 댓글이 지원되므로 커뮤니티가 Nostr에서 직접 MCP 서버를 논의하고 평가할 수 있습니다.

- **[NIP-73: OSM 태그 Kind](https://github.com/nostr-protocol/nips/pull/2224)**: DestBro가 `i` 및 `k` tag를 통해 책 (ISBN), 영화 (ISAN), 팟캐스트 피드 (GUID), 지오해시, URL과 같은 외부 콘텐츠를 Nostr event가 참조하는 방식을 표준화하는 [NIP-73 (외부 콘텐츠 ID)](/ko/topics/nip-73/)에 OpenStreetMap 식별자를 추가할 것을 제안합니다. 제안된 OSM kind는 event가 특정 지도 기능 (건물, 도로, 공원)을 OpenStreetMap 노드나 way ID로 참조하여 Nostr 콘텐츠를 개방형 지리 데이터베이스에 연결할 수 있게 합니다.

- **[NIP-XX: 반응형 이미지 변형](https://github.com/nostr-protocol/nips/pull/2219)**: woikos가 다양한 해상도의 반응형 이미지 변형을 위한 tag로 [NIP-94](/ko/topics/nip-94/) 파일 메타데이터 event를 확장할 것을 제안합니다. 클라이언트가 디스플레이 크기와 네트워크 상태에 따라 적절한 변형을 선택하여, [Blossom](/ko/topics/blossom/) 서버에 호스팅된 고해상도 이미지를 보는 모바일 사용자의 대역폭을 줄일 수 있습니다.

## NIP 심층 분석: NIP-85 (Trusted Assertions)

[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)는 비용이 많이 드는 계산을 신뢰할 수 있는 서비스 제공자에게 위임하고, 서비스 제공자가 서명된 결과를 Nostr event로 게시하는 시스템을 정의합니다. Web of Trust 점수와 참여도 메트릭은 여러 relay를 크롤링하고 대량의 event를 처리해야 하며, 이는 모바일 기기에서는 비실용적인 작업입니다. 이번 주 [병합](https://github.com/nostr-protocol/nips/pull/2223)은 이 제공자들의 클라이언트 검색 프로세스에 대한 안내를 추가했습니다.

**위임:**

사용자의 Web of Trust 점수를 계산하려면 여러 relay에 걸쳐 팔로우 그래프를 여러 홉 깊이로 크롤링해야 하고, 정확한 팔로워 수를 계산하려면 전체 relay 네트워크에서 중복 제거가 필요합니다. 모바일 기기와 브라우저 클라이언트는 이러한 작업을 수행할 수 없지만, 결과는 스팸 필터링과 콘텐츠 순위 매기기에 필수적입니다. NIP-85는 사용자가 신뢰할 수 있는 제공자를 지정하여 계산을 실행하고 표준 Nostr event로 결과를 게시하도록 함으로써 이 격차를 해소합니다.

**프로토콜 설계:**

NIP-85는 다양한 주체 유형에 대한 어서션을 위해 네 가지 event kind를 사용합니다. 사용자 어서션 (kind 30382)은 팔로워 수, 게시물/답글/리액션 수, zap 금액, 정규화 순위 (0-100), 공통 주제, 활동 시간을 담습니다:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Event 어서션 (kind 30383)은 댓글 수, 인용 수, 리포스트, 리액션, zap 데이터로 개별 노트를 평가합니다:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

주소 지정 가능한 event (장문 아티클, 위키 페이지)의 경우, kind 30384가 모든 버전에 걸쳐 동일한 참여도 메트릭을 집합적으로 적용합니다. Kind 30385는 `i` 및 `k` tag를 통해 외부 콘텐츠를 참조하는 방식을 표준화하는 [NIP-73 (외부 콘텐츠 ID)](/ko/topics/nip-73/)를 통해 참조된 외부 식별자 (책, 영화, 웹사이트, 위치, 해시태그)를 평가합니다:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

각 어서션은 `d` tag에 주체가 포함된 교체 가능한 주소 지정 가능 event입니다: pubkey, event ID, event 주소, 또는 NIP-73 식별자. 서비스 제공자는 자체 키로 이 event에 서명하고, 클라이언트는 신뢰 관계에 따라 평가합니다.

**제공자 검색:**

사용자는 kind 10040 event를 게시하여 신뢰하는 어서션 제공자를 선언합니다. 각 항목은 제공자 pubkey와 relay 힌트, 선택적 알고리즘 변형과 함께 어서션 유형을 지정합니다:

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

사용자는 제공자 환경설정을 비공개로 유지하기 위해 [NIP-44](/ko/topics/nip-44/)를 사용하여 `.content`의 tag 목록을 암호화할 수 있습니다. 클라이언트는 팔로우한 계정들이 신뢰하는 제공자를 확인하여 제공자 목록을 구축하며, 어서션 제공자 자체를 위한 탈중앙화 평판 레이어를 만듭니다.

**보안 모델:**

제공자는 별개의 알고리즘에 서로 다른 서비스 키를 사용해야 하며, 알고리즘이 개인화될 때는 사용자당 고유한 키를 사용해야 합니다. 이는 사용자 간 쿼리의 상호 연관을 방지합니다. 각 서비스 키는 알고리즘의 동작을 설명하는 kind 0 메타데이터 event를 받아, 사용자에게 신뢰하는 것에 대한 투명성을 제공합니다. 어서션 event는 기본 데이터가 실제로 변경될 때만 업데이트되어야 하며, 불필요한 relay 트래픽을 방지하고 클라이언트가 안심하고 결과를 캐시할 수 있게 합니다.

**현재 채택 현황:**

NIP-85는 이미 비공식적으로 등장하고 있는 패턴을 공식화합니다. Primal의 캐시 서버가 참여도 메트릭과 Web of Trust 점수를 계산합니다. [뉴스레터 #9에서 다룬](/ko/newsletters/2026-02-11-newsletter/#antiprimal-primal-캐시에-대한-표준-호환-게이트웨이) [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal)이 NIP-85 event kind를 사용하여 이 계산들을 표준 Nostr 클라이언트에 브릿지합니다. [Nostr.band](https://nostr.band)가 명세 자체 예시에서 참조된 `wss://nip85.nostr.band` relay를 운영하며, 검색 인덱스 데이터를 위한 어서션 event를 서비스합니다. 클라이언트 측에서 이 NIP을 작성한 vitorpamplona가 만든 [Amethyst](https://github.com/vitorpamplona/amethyst)가 `quartz` 라이브러리에 실험적인 Trusted Assertions 지원을 갖추고 있으며, 어서션 event와 서비스 제공자 선언을 파싱합니다. [Vertex](https://vertexlab.io)는 유사한 Web of Trust 메트릭을 계산하지만 [다른 접근 방식을 선택했습니다](https://vertexlab.io/blog/dvms_vs_nip_85/). 검색 문제와 어서션 기반 아키텍처의 계산 오버헤드를 이유로 NIP-85 event 대신 직접 API를 사용합니다. NIP-85를 통해 어떤 클라이언트든 표준 event 형식을 통해 어떤 제공자의 어서션도 소비할 수 있으며, 제공자들은 정확성으로 경쟁하면서 사용자들은 신뢰할 대상을 선택합니다.

## NIP 심층 분석: NIP-52 (캘린더 Events)

[NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md)는 Nostr에서 캘린더 event를 정의하여, 클라이언트가 특정 순간 또는 순간 사이에 발생하는 사건을 표준적인 방식으로 표현하고 검색할 수 있게 합니다. 이번 주 [D tag 병합](https://github.com/nostr-protocol/nips/pull/1752)은 일 단위 인덱싱을 추가하여 명세의 쿼리 인프라에서 빠진 부분을 완성했습니다.

**두 가지 Event 유형:**

NIP-52는 시간적 정밀도에 따라 캘린더 event를 두 가지 kind로 분리합니다. 날짜 기반 event (kind 31922)는 공휴일이나 다중 일 축제와 같은 하루 종일 지속되는 사건을 나타냅니다. `start` 및 선택적 `end` tag에 ISO 8601 날짜 문자열을 사용하며, 시간대 고려 없이:

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

시간 기반 event (kind 31923)는 `start` 및 선택적 `end` tag의 Unix 타임스탬프와 표시를 위한 IANA 시간대 식별자 (`start_tzid`, `end_tzid`)로 특정 순간을 나타냅니다. 두 kind 모두 매개변수화된 교체 가능 event이므로, 주최자가 같은 `d` tag를 사용하는 새 event를 게시하여 세부 정보를 업데이트합니다.

**캘린더와 RSVP:**

Kind 31924 event는 kind 31922 또는 31923 event를 주소 좌표로 가리키는 `a` tag를 통해 event를 참조하는 컬렉션으로 캘린더를 정의합니다:

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

사용자는 여러 캘린더 (개인, 업무, 커뮤니티)를 유지할 수 있으며 클라이언트는 특정 pubkey의 캘린더를 구독할 수 있습니다. 캘린더 event는 캘린더를 참조하는 `a` tag를 포함하여 포함 요청을 할 수 있으며, 소유하지 않은 캘린더에 여러 사용자가 event를 기여하는 협업 캘린더 관리가 가능합니다.

RSVP는 kind 31925를 사용하며, 사용자가 선택적 참여 가능/불가능 표시와 함께 참석 상태를 게시합니다:

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

유효한 `status` 값은 "accepted", "declined", "tentative"이며, 선택적 `fb` tag가 사용자를 해당 기간 동안 참여 가능 또는 불가능으로 표시합니다. RSVP event는 캘린더 event의 `a` tag를 참조하고 주최자의 `p` tag를 담으므로, 주최자의 클라이언트가 relay 전반의 응답을 집계할 수 있습니다.

**D Tag 추가:**

이번 주 병합 전에는 날짜 범위에서 event를 쿼리하는 클라이언트가 pubkey나 캘린더에서 모든 event를 가져와 클라이언트 측에서 필터링해야 했습니다. 시간 기반 event (kind 31923)의 새로운 필수 `D` tag는 `floor(unix_seconds / 86400)`으로 계산된 일 단위 Unix 타임스탬프를 담습니다. 다중 일 event는 하루당 하나씩 여러 `D` tag를 가집니다. Relay가 이제 일별로 event를 인덱싱하고 필터링된 쿼리에 효율적으로 응답할 수 있어, 클라이언트 측 필터링 문제를 relay 측 인덱스 조회로 전환합니다.

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

`D` 값 `20139`는 `floor(1740067200 / 86400)`이며, 이 event를 2025년 2월 20일에 배치합니다. "이번 주 모든 event"를 쿼리하는 클라이언트는 해당 `D` 범위가 있는 필터를 보내고, relay는 일치하는 event만 반환합니다.

**설계 결정:**

NIP-52는 의도적으로 반복 event를 생략합니다. 명세는 재발 규칙 (iCalendar의 RRULE)을 완전히 제외하여 해당 복잡성을 클라이언트에 위임합니다. 주최자가 각 발생에 대해 개별 event를 게시하여 relay 측 데이터 모델을 단순하게 유지합니다. 참가자 tag는 선택적 역할 ("host", "speaker", "attendee")을 담으며, 위치 tag는 인간이 읽을 수 있는 주소와 함께 공간 쿼리를 위한 지오해시 `g` tag를 포함할 수 있습니다.

**구현:**

[Flockstr](https://github.com/zmeyer44/flockstr)는 NIP-52 위에 구축된 주요 캘린더 클라이언트입니다. [Coracle](https://gitea.coracle.social/coracle/coracle)은 소셜 피드에 캘린더 event를 표시합니다. 이번 주 `D` tag 추가로 특정 날짜 범위의 event를 쿼리할 때 대역폭을 줄이는 relay 측 시간적 인덱싱이 가능해져, 두 클라이언트 모두 이를 활용할 수 있습니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나, 공유할 뉴스가 있거나, 프로젝트를 다뤄주길 원하신다면 <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM으로 연락하시거나</a> Nostr에서 찾아주세요.
