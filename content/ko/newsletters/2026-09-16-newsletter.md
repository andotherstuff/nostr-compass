---
title: "Nostr Compass #40"
date: 2026-09-16
translationOf: /en/newsletters/2026-09-16-newsletter.md
translationDate: 2026-09-16
draft: false
type: newsletters
---

매주 Nostr를 안내하는 [Nostr Compass](https://nostrcompass.org)에 다시 오신 것을 환영합니다.

**이번 주:** [Marmot Protocol과 MDK](#marmot-protocol-and-mdk-reach-v0100)에 [범위가 제한된 대화 창, 복구 수정 사항, 조율된 SDK 바인딩](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0)이 추가되고, [Myco](#myco-070-runs-napplets-and-file-sharing-over-a-multi-path-fips-mesh)는 FIPS 메시를 오프라인 napplet 및 파일 공유 런타임으로 전환하며, [Dart NDK](#dart-ndk-changes-relay-cache-and-account-behavior)는 relay와 캐시 동작을 변경하고, [Keycast](#keycast-publishes-its-rebuilt-signer-release-candidate)는 지속성 있는 요청과 복구를 중심으로 원격 서명 기능을 재구축합니다. 태그가 지정된 릴리스로는 [Nail](#nail-020-restores-nostr-to-email-subscriptions), [Nostr Mail Client](#nostr-mail-client-0150-broadens-account-and-relay-control), [Linky](#linky-26917-keeps-recovery-seeds-off-its-server), [Boris](#boris-0125-bounds-extraction-and-strengthens-offline-reading)가 있습니다. NIPs 저장소는 이번 주에 PR 하나를 병합해 [NIP-A3 (Payment Targets)](/ko/topics/nip-a3/)를 명확히 했으며, 제안된 슬래시 명령과 DVM 하트비트 작업은 아직 열려 있습니다. 심층 분석에서는 [NIP-23 (Long-form Content)](#nip-23-long-form-content)와 [NIP-92 (Media Attachments)](#nip-92-media-attachments-metadata)를 다룹니다.

## 주요 소식

### Marmot Protocol과 MDK가 v0.10.0에 도달

[Marmot Protocol의 MDK v0.10.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0)은 Nostr 위에서 MLS 기반 암호화 그룹을 구축하는 애플리케이션을 위해 범위가 제한된 채팅 목록 및 대화 창, 독립적인 계정 주의 필요 요약, 수정본에 안전한 초안, 열람자 반응 상태를 추가합니다. 또한 계정별 사용자 차단을 복원하고, 대기 중인 초대를 읽지 않은 메시지로 다시 중복 집계하지 않으면서 그 수를 계산합니다.

[v0.10.0 릴리스 계열](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0)은 기기가 제거된 뒤 다시 추가되는 경우, Welcome보다 트래픽이 먼저 도착하는 경우, peel 재생이 중단되는 경우의 복구를 수정합니다. relay 동기화와 구독 변동을 줄이고, 전송 슬롯이 사용 중일 때 미디어 작업을 대기열에 넣으며, 매번 포렌식 감사 업로드 대상이 검증된 목적지로 고정되도록 합니다.

동일한 [MDK 소스 커밋](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0)은 Rust, C, Swift, Kotlin, 명령줄, 에이전트 산출물을 하나의 호환성 집합으로 제공합니다. 계정 데이터베이스는 마이그레이션 70–75를 거쳐 갱신되므로, 애플리케이션은 생성된 소스와 네이티브 라이브러리를 함께 업데이트하고, 완전한 Apple 프레임워크 번들을 보존하며, 마이그레이션 전에 백업하고, 마이그레이션된 데이터베이스를 다운그레이드하지 않아야 합니다.

### Myco 0.7.0이 다중 경로 FIPS 메시에서 napplet과 파일 공유를 실행

[Myco v0.7.0](https://github.com/Origami74/myco/releases/tag/v0.7.0)은 Android 메시 애플리케이션을 공개 [NIP-5D 제안](/ko/topics/nip-5d/)에 설명된 단일 파일 Nostr 프로그램인 napplet의 호스트로 전환합니다. 각 napplet은 네트워크나 저장소에 직접 접근하지 못하는 샌드박스에서 실행되며 Myco를 통해 신원, relay, outbox, 메시, 사진 또는 파일 기능을 요청합니다. 설치 화면은 승인 전에 해당 권한을 표시하고, 사용자는 나중에 권한을 변경할 수 있으며, 더 광범위한 접근을 요청하는 업데이트는 다시 권한 승인 단계로 돌아갑니다.

[Myco v0.7.0](https://github.com/Origami74/myco/releases/tag/v0.7.0)은 시스템 공유 화면이나 Circle 연락처를 통해 페어링된 휴대전화로 임의의 파일도 전송합니다. 수신 휴대전화는 Myco가 파일을 `Downloads/Myco`에 기록하기 전에 전송을 승인하며, 페이로드는 해당 휴대전화의 키로 암호화됩니다. 두 휴대전화가 같은 Wi-Fi를 사용할 때는 로컬 네트워크 검색에 UDP를 사용하고 오프라인 경로에는 Bluetooth를 유지합니다. 제어 메시지가 유실되면 재시도하며, 무응답 타이머로 중단된 대용량 전송의 시간을 제한합니다.

[Myco는 이제 피어에 대한 FIPS 링크를 동시에 유지](https://github.com/Origami74/myco/releases/tag/v0.7.0)하고, 대기 경로를 탐색하며, 활성 Bluetooth, Wi-Fi Aware 또는 로컬 네트워크 링크의 품질이 저하되면 트래픽을 이동합니다. 이 작업은 FIPS의 실험적 다중 경로 브랜치를 기반으로 합니다. Version 0.7.0은 기존 앱 교환, 메시징, 페어링에서 0.6.1과 유선 호환성을 유지하지만, 다중 경로 링크는 업데이트된 휴대전화 두 대 사이에서만 형성됩니다. 내장 relay도 LMDB로 이전되며 최초 실행 시 이전 event 저장소를 마이그레이션합니다.

### Dart NDK가 relay, 캐시, 계정 동작을 변경

[Dart NDK v0.10.0-dev.3](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.3)은 Dart 클라이언트 라이브러리의 개발 릴리스로, relay 처리, 캐싱, 인증, 계정 스트림 전반에 호환성을 깨는 변경 사항이 있습니다. 클라이언트 유지관리자는 특히 애플리케이션이 캐시된 event, 숨겨진 event 또는 계정 업데이트가 이전 릴리스 계열의 의미 체계를 따른다고 가정하는 경우 코드와 동작을 마이그레이션해야 할 것으로 예상해야 합니다.

[v0.10.0 개발 계열](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.3)은 캐시와 Rust 검증기의 성능도 개선하고 메타데이터, 삭제 좌표, event 표시 여부, signer 인증, NWC 결제 동작을 변경합니다. 압축된 Rust event 검증은 검증 오버헤드를 줄이지만, 새로운 `loadHiddenEvents` 캐시 동작은 명시적으로 호환성을 깨는 변경 사항입니다.

이는 안정적인 v0.10.0 릴리스가 아니라 [v0.10.0-dev.3](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.3)이므로, 애플리케이션 팀은 version을 고정하고 마이그레이션을 신중하게 테스트해야 합니다. 프로덕션 클라이언트를 이전하기 전에 relay 재연결, 캐시 채우기, signer 인증, 지갑 처리, 계정 스트림 순서를 우선적으로 점검해야 합니다.

### Keycast가 재구축된 signer의 릴리스 후보를 공개

[Keycast v2.0.0-rc.1](https://github.com/marmot-protocol/keycast/releases/tag/v2.0.0-rc.1)은 재구축된 자체 호스팅 NIP-46 원격 signer의 첫 번째 번호 지정 릴리스입니다. 이 릴리스 후보는 다중화된 NIP-46 지원, 공유 및 키별 relay 라우팅, 지속성 있는 요청 처리, 암호화된 키 저장소, 초대, 세션, 팀 작업 공간을 추가합니다.

[v2.0.0-rc.1](https://github.com/marmot-protocol/keycast/releases/tag/v2.0.0-rc.1)은 서명 정책과 복구를 동등하게 중시합니다. 운영자는 서명 정책을 구성하고, 감사 기록을 검토하며, 암호화된 백업을 생성하고, 배포를 복구하며, 루트 키를 교체할 수 있습니다. 프로젝트는 API, signer, 웹 구성 요소 전반에서 조율되고 검증된 릴리스 출처도 문서화합니다.

이 릴리스는 여전히 [릴리스 후보](https://github.com/marmot-protocol/keycast/releases/tag/v2.0.0-rc.1)이므로, 운영자는 version 번호만 보고 최종 호환성이나 프로덕션 준비 상태를 추론해서는 안 됩니다. 기존 signer 서비스를 교체하기 전에 중단된 요청 복구, relay 라우팅 실패, 정책 시행, 백업 복원, 키 교체를 테스트해야 합니다.

## 태그 지정 릴리스

### Nail 0.2.0이 Nostr에서 이메일로 보내는 구독을 복원

이메일 워크플로를 통해 Nostr 메시지를 전달하는 서비스인 [Nail v0.2.0](https://github.com/formstr-hq/nail/releases/tag/v0.2.0)은 자동 복구되는 gift-wrap 구독을 추가합니다. 이 변경 사항은 구독 실패 후 브리지가 눈에 띄지 않게 멈춰 있는 대신 Nostr에서 이메일로 보내는 전달을 복원하는 데 목적이 있습니다.

### Nostr Mail Client 0.15.0이 계정 및 relay 제어를 확대

[Nostr Mail Client v0.15.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.15.0)은 한 번의 탭으로 계정 전환, 계정별 알림, 웹 푸시, relay·Nostr 주소·`nprofile`을 통한 누락된 relay 목록 복구 기능을 추가합니다. 또한 프로필과 relay 목록을 인덱싱 relay에 다시 게시하고, 네트워크 접근이 복원되면 재연결하며, 기기 장애와 연결할 수 없는 메일 relay를 구분합니다. 이러한 변경 사항은 데스크톱, 웹, Android 클라이언트 전반에서 계정 복구와 전달을 강화합니다.

### Linky 26.9.17이 복구 seed를 서버에 저장하지 않도록 변경

연락처, 비공개 Nostr 메시징, Lightning/Cashu 결제 애플리케이션인 [Linky v26.9.17](https://github.com/linky-fit/linky/releases/tag/v26.9.17)은 사용자가 비밀번호 관리자를 통해 복구 seed를 저장할 때 Linky 서버로 전송되던 경로를 수정합니다. 이 릴리스는 결제 파일 URL 처리도 강화하고 Android 애플리케이션 백업을 비활성화하여 지갑 및 신원 복구 자료가 기기 밖으로 유출될 수 있는 지점을 줄입니다.

### Calendar by Form* 2.4.0이 Mailstr 게스트 초대를 추가

Nostr 캘린더 클라이언트인 [Calendar by Form* v2.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.4.0)은 Mailstr 게스트 초대와 모바일 캘린더 수정 사항을 추가합니다. 이 초대 경로를 이용하면 주최자가 기존 캘린더 계정을 요구하지 않고 메일 중심의 조율을 통해 참가자를 포함할 수 있습니다.

### Hessible 0.1.2가 암호화된 연락처 및 사진 동기화를 가속

암호화된 연락처 데이터를 Nostr relays에 저장하는 개인정보 보호 중심 Android 연락처 애플리케이션인 [Hessible 0.1.2](https://github.com/circumspace/hessible)는 동기화 오버헤드를 줄이고 암호화된 연락처 사진을 Blossom 서버 전반에 미러링합니다. 이 릴리스는 애플리케이션 패키지도 더 작게 만들지만, 자체 릴리스 지침에서는 사용자가 키를 백업하고 relay마다 보존 기간이 다르다는 점을 계속 고려하라고 경고합니다.

### Boris 0.12.5가 추출 범위를 제한하고 오프라인 읽기를 강화

Nostr 북마크를 중심으로 구축된 읽기 목록 클라이언트인 [Boris v0.12.5](https://github.com/dergigi/boris/releases/tag/v0.12.5)는 v0.12.4에 이어 범위가 제한된 콘텐츠 추출, 오프라인 캐싱, relay 쿼리 변경, 안전하지 않은 HTML 처리, Paper White 테마에서 텍스트가 거의 보이지 않던 문제의 수정 사항을 제공합니다. 이러한 변경 사항은 콘텐츠 안전성과 실시간 네트워크 경로 없이 저장된 자료를 읽는 기능의 신뢰성 모두에 영향을 미칩니다.

### Amethyst 1.15.2가 미디어와 루트 범위 답글을 개선

Android Nostr 클라이언트인 [Amethyst v1.15.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.15.2)는 미디어 수정 사항, 더 명확한 Health Connect 권한 처리, 소스 이름 캐싱, NIP-22 루트 범위 답글 전용 참여 필터와 함께 3개 릴리스로 이어진 계열을 마무리합니다. 이 릴리스에는 번역 및 패키지 메타데이터 업데이트도 포함됩니다.

### LibreNostr 0.5.17이 작성자의 쓰기 relay를 통해 피드를 라우팅

relay 우선 Android 클라이언트인 [LibreNostr 0.5.17](https://primal.net/e/c118efbe649823a3258a6e7663f4d8b52195adbde0481019183792eb5274afd4)은 이제 피드 쿼리를 팔로우 중인 작성자의 NIP-65 쓰기 relay로 보내고 노트가 화면에 들어올 때까지 상호작용 수 쿼리를 미룹니다. 동일한 릴리스 계열의 이전 작업은 동시 relay 쿼리를 제한하고 각 relay가 응답하는 즉시 해당 relay 구독을 종료하여 새로 고침 중 자체적으로 초래하는 요청 거부를 줄입니다.

### Voca 1.2.0이 음성 취소 및 복구를 개선

Nostr 콘텐츠를 가져오고 검증할 수 있는 오프라인 중심 Android 텍스트 음성 변환 리더인 [Voca 1.2.0](https://njump.me/nevent1qqsfcc5zel49t5zt96ufndumrzc2vzhrk7e2rnwq579gcs8yd9cn4pcflqxt3)은 이슈 #38에서 다룬 1.0 출시 이후 별도의 취소 및 렌더링 동작과 느리거나 신뢰할 수 없는 음성 엔진을 위한 복구 기능을 추가합니다. 또한 새 일회용 Nostr 키를 사용해 NIP-17 비공개 메시지로 전송하는 선택형 진단 기능을 추가하며, 대용량 보고서는 업로드 전에 로컬에서 암호화됩니다.

### Postr 1.1.1이 받아쓰기와 게시 복구를 추가

kind `1` 작성에 집중한 Android 앱인 [Postr 1.1.1](https://njump.me/nevent1qqszw3dsskfz3u7pqxn4r5ytslrj0e3u26et90rpy9997vtfw3qkr6g9g0f03)은 이슈 #37에서 다룬 출시 이후 받아쓰기와 캐럿 위치를 인식하는 멘션 처리 기능을 추가합니다. 직전 1.1.0 릴리스는 결과가 불분명한 경우 동일한 서명된 event를 재시도해 복구 과정에서 중복 노트가 생성되지 않도록 함으로써 게시 복구도 개선합니다.

### earthly 0.1.10이 지도 정화 및 작성 기능을 수정

협업형 Nostr 지도 편집기인 [earthly v0.1.10](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.10)은 MapLibre GL JS 업그레이드를 통해 심각한 MapLibre 저작자 표시 정화 기능의 결함을 수정하는 동시에 지도 및 스토리 작성 기능을 실질적으로 변경합니다. 이 릴리스는 WebGL 2 호환성 안내, 모바일 제어 기능, 도형 편집, 선택, 지도 프레젠테이션 제어 기능도 개선합니다.

### Routstrd 0.4.10이 Nostr 요청 라우팅을 강화

[Routstrd v0.4.10](https://github.com/Routstr/routstrd/releases/tag/v0.4.10)은 오래된 저장 provider 목록을 실시간 검색에서 반환된 목록으로 교체합니다. 직전 v0.4.9 릴리스는 수동 및 예약 클라이언트 새로 고침 제어 기능, CLI의 이름 지정 npubs, 활성 요청을 기다리는 정상적인 데몬 재시작 기능을 추가했습니다. 두 릴리스를 통해 Nostr로 라우팅되는 서비스의 운영자는 provider 선택과 새로 고침 동작을 더 명확하게 파악할 수 있습니다.

### Whistle 1.9.1이 백그라운드 복구 계측을 추가

Nostr, MLS, Marmot Protocol을 기반으로 구축된 암호화 그룹 위치 공유 애플리케이션인 [Whistle 1.9.1](https://primal.net/e/bb3aae325f707b04dffd3b0b4a2d0c48022999fef7a793be3503b4c53e37eba4)은 iOS 백그라운드 복구를 위한 기기 수명 주기 계측을 추가합니다. Version 1.9.0은 그룹별 공유 일시 중지와 그룹별 마지막 event 진단도 도입하여 중단된 그룹을 정상적인 애플리케이션 전체 연결과 더 쉽게 구분할 수 있도록 합니다.

### Amber 6.6.4가 Tor 유출과 signer 복구 실패를 해결

Android Nostr event signer인 [Amber v6.6.4](https://github.com/greenart7c3/Amber/releases/tag/v6.6.4)는 Tor 유출 수정과 signer relays 및 복구 관련 수정 사항으로 3개 릴리스 계열을 마무리합니다. signer 사용자는 물론 애플리케이션 개발자도 네트워크 경로 가정과 재시도 동작에 특히 주의를 기울여야 합니다. 그렇지 않으면 signer 장애가 클라이언트 게시 장애처럼 보일 수 있기 때문입니다.

### nostr-wot-extension 0.7.0이 지갑 캐시 데이터를 암호화

Nostr 신원을 관리하고 events에 서명하며 Lightning 결제를 시작하는 브라우저 확장 프로그램인 [nostr-wot-extension v0.7.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.7.0)은 지갑 및 결제 캐시 데이터를 암호화하고 금고와 계정의 격리를 강화합니다. 또한 NWC 및 지갑 동작, 결제 호환성, 요청 승인, 계정 관리, 백업 가져오기, relay 처리, 접근성, 로컬 event 복호화 문제를 해결합니다.

### Lightning.Pub 0.0.41이 게시 복구를 개선

[Lightning.Pub v0.0.41](https://github.com/shocknet/Lightning.Pub/releases/tag/v0.0.41)은 Nostr 게시 실패에 relay URL, 타이밍, 소켓 상태, DNS 세부 정보를 추가합니다. 또한 유동성 provider 시작 호출을 재시도하고, 방치된 콜백을 제거하며, 성공적인 잔액 응답을 통해 provider가 준비되었음이 입증될 때까지 invoice 라우팅을 보류합니다. 이제 운영자는 relay 연결 장애와 백엔드 준비 장애를 더 명확하게 구분할 수 있습니다.

### Gittr 1.0.0이 NIP-34 협업을 진전

Nostr 기반 Git 협업용 클라이언트인 [Gittr v1.0.0](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.0)은 NIP-34 복제 소스 처리, 이슈 및 토론 상태, 모바일 사용성, 상호운용성을 발전시킵니다. v1.0.0 tag는 이번 주 초의 v0.3.0과 v0.3.1에 이어 공개되어 통합 담당자에게 이 릴리스 계열의 안정적인 version 표식을 제공합니다.

### GitWorkshop 4.1.0이 NIP-34 초안을 복구 가능하게 변경

NIP-34 이슈, pull request, 코드 검토, 저장소 탐색을 위한 Nostr 네이티브 클라이언트인 [GitWorkshop 4.1.0](https://njump.me/nevent1qqswf45vw8y5metnu8tc2fge0lr7sy8nmuk264kryrd45wqles5kfvqqrtwl3)은 새로 고침과 브라우저 재시작 후에도 유지되는 계정별 로컬 초안을 추가합니다. 또한 Git 읽기, relay 검색, 저장소 상태, pull request 기록, 업로드, 릴리스 메타데이터 전반에 범위가 제한된 복구와 명시적인 재시도 제어 기능을 추가하면서 서명 및 결제 재시도는 수동으로 유지합니다.

### ngit-ci 0.1.1이 서명된 CI 조율을 게시

제안된 NIP-C1 Nostr CI 프로토콜을 위한 자체 호스팅 조정자인 [ngit-ci 0.1.1](https://njump.me/nevent1qqs2y0p5nxkfqsrqguth3hd4wmmel4p2te8q906ex748q35ug79e6eg9hms4s)은 Nostr를 통해 게시된 첫 릴리스입니다. 서명된 워크플로 조율, 컨테이너 또는 microVM 실행, 로그와 산출물, 암호화된 저장소 비밀 정보, NIP-34 유지관리자 권한 부여, 빌드 결과의 서명된 게시를 다룹니다.

### pakstr 0.21.1이 Nostr 애플리케이션 패키징을 진전

[pakstr v0.21.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.21.1)은 Nostr 애플리케이션 패키징 및 앱 셸 동작을 위한 5개 릴리스 계열을 이어갑니다. NostrAppShell 참조는 동일한 pakstr 릴리스 계열을 가리키므로, 패키지와 별칭은 출시된 동일한 변경 사항을 설명합니다.

### @elisym/cli 0.30.0이 에이전트 및 위임 패키지를 조율

[@elisym/cli 0.30.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/cli%400.30.0)은 Nostr 지향 에이전트 위임을 위한 조율된 CLI, SDK, MCP 릴리스를 마무리합니다. 이제 위임된 작업은 고정된 시간 동안 대기하는 대신 완료될 때까지 기다리며, 애플리케이션은 작업마다 동일한 위임 기능에 비용을 지불하지 않습니다. 둘 이상의 패키지를 사용하는 팀은 CLI 0.30.0, SDK 0.36.0, MCP 0.26.0을 일치하는 릴리스 계열로 유지해야 합니다.

### Hashtree 0.2.150이 해시 트리 동기화를 진전

[Hashtree v0.2.150](https://github.com/mmalmi/hashtree/releases/tag/v0.2.150)은 내장 소셜 그래프를 위한 Android 안전 잠금 기능으로 6개 릴리스 계열을 마무리합니다. 이 계열의 이전 릴리스들은 빈 EOSE 이후에도 Nostr 구독을 잠시 열어 두어 지연된 서명 루트가 도착할 수 있게 하고, 정확한 작성자와 트리에 대해 가장 최신의 유효한 루트를 선택하며, 전송 중단 후 보존된 FIPS 경로를 복구합니다. 그 결과 relays, 내장 클라이언트, 간헐적인 네트워크 경로 전반에서 변경 가능한 루트의 검색과 동기화를 더 예측할 수 있습니다.

### nostr-relay 0.0.266이 공유 데이터베이스 운영을 개선

relayer 프레임워크를 기반으로 구축된 Nostr relay인 [nostr-relay v0.0.266](https://github.com/mattn/nostr-relay/releases/tag/v0.0.266)은 6개 릴리스에 걸쳐 공유 데이터베이스와 Redis 동작을 발전시킵니다. 이 작업은 둘 이상의 relay 프로세스를 공통 영속성 또는 알림 인프라에 연결해 운영하는 경우 특히 중요합니다.

### fips-tcp 0.2.2가 TCP를 통한 FIPS를 구현

[fips-tcp v0.2.2](https://github.com/mmalmi/fips-tcp/releases/tag/fips-tcp-v0.2.2)는 확인 응답이 진행됨에 따라 제한 시간이 초과된 전송 묶음에서 누락된 세그먼트를 복구합니다. 전송 중단 중 유실된 작은 쓰기 작업은 각 세그먼트가 계속 늘어나는 제한 시간을 기다리는 대신 함께 복구되며, Rust 및 TypeScript 구현은 동일한 유선 바이트, 재시도 범위, 수신 창 검사, 시퀀스 순환, RTT 샘플링을 유지합니다.

## 개발 중

### Nenya 마켓플레이스 라이브러리

[Nenya](https://github.com/Erya-Labs/Nenya)는 Bitcoin 결제를 사용하는 의뢰형 디지털 미디어에 초점을 맞춘 비수탁형 Nostr 마켓플레이스를 위한 새로운 라이브러리입니다. 이 저장소는 출시 전 단계이므로 event 및 결제 인터페이스가 아직 변경될 수 있습니다.

클라이언트 개발자는 Nostr 애플리케이션에서 호환되는 상품 등록과 거래를 제공하기 위해 [Nenya 라이브러리](https://github.com/Erya-Labs/Nenya)를 가져옵니다. 독립형 배포나 안정적인 릴리스 계약이 아직 없으므로 통합 작업은 event 및 결제 경계부터 시작해야 합니다.

### GitHub와 Nostr 간 CI 연결

[gh-ngit-ci-bridge](https://github.com/felixfelix-bot/gh-ngit-ci-bridge)는 설정된 신원과 연결된 GitHub 커밋을 감시하고 이를 NIP-34 워크플로용으로 서명된 Nostr 빌드 증거로 변환하는 초기 단계의 브리지입니다. 이 저장소는 출시 전 단계이며 통합 계약이 아직 변경될 수 있습니다.

[gh-ngit-ci-bridge 저장소](https://github.com/felixfelix-bot/gh-ngit-ci-bridge)는 기존 포지 워크플로를 변경하지 않고 통상적인 GitHub 활동을 Nostr 네이티브 CI 조정과 연결합니다. 구현에서 중요한 질문은 출처입니다. 소비자는 감시 대상 GitHub 작업, 브리지 신원, 그 결과로 생성된 서명된 Nostr 증거를 구분해야 합니다.

### noscall의 음성 첨부 파일 암호화

[noscall의 암호화된 음성 첨부 파일 커밋](https://github.com/sanah9/noscall/commit/3f0b9ef7cf0fbc6e0dced58240c32bb84ed6fea4)은 음성 통신을 위한 구체적인 개인정보 보호 기능을 추가합니다. 소스로 확인된 이 변경 사항은 암호화된 음성 첨부 파일을 지원하여 녹음된 미디어를 통화나 메시징 흐름에 첨부할 때 평문으로 노출할 필요를 줄입니다.

### relayer, 프로세스 간 알림 전파 복원

[relayer 풀 리퀘스트 #167](https://github.com/fiatjaf/relayer/pull/167)에는 여러 relay 프로세스가 하나의 데이터베이스를 공유하는 배포 환경을 위한 알림 수정 사항이 병합되었습니다. 이 패치는 해당 프로세스들 사이의 실시간 전파를 복원하여 event가 성공적으로 저장되었지만 다른 프로세스에 연결된 클라이언트가 이에 해당하는 실시간 알림을 받지 못하던 사례를 해결합니다.

[nostr-relay v0.0.266](https://github.com/mattn/nostr-relay/releases/tag/v0.0.266)의 공유 데이터베이스 작업과 함께 보면, relayer 수정 사항은 다중 프로세스 운영자에게 명확한 테스트 목표를 제공합니다. 한 프로세스를 통해 게시하고 다른 프로세스를 통해 구독한 뒤 저장과 즉시 전달이 모두 이루어지는지 확인하는 것입니다. 데이터베이스 쓰기에 성공했다는 사실만으로는 실시간 구독자가 event를 받았다고 입증할 수 없습니다.

## 새 프로젝트

### Trackstr, 전용 event kind로 미디어 매핑

[Trackstr](https://github.com/besoeasy/Trackstr)는 영화, 음악, 텔레비전 및 기타 미디어를 탐색하고 추적하기 위한 미출시 오픈 소스 Nostr 미디어 데이터베이스입니다. 현재 설계는 event kind `35400`부터 `35402`까지를 사용하여 검토 가능한 스키마와 구현 범위를 제공합니다. 이 kind들은 프로젝트에서 정의한 것이며 출시 전에 변경될 수 있습니다.

## 프로토콜 및 명세 작업

### NIP-A3, 결제 유형의 모호성 명확화

[NIP-A3 (결제 대상)](/ko/topics/nip-a3/)은 kind `10133` event의 `["payto", "<type>", "<address>"]` tag에서 유형이 지정된 결제 대상을 표준화합니다. 병합된 [결제 유형 명확화](https://github.com/nostr-protocol/nips/pull/2463)는 문서화된 유형 목록에 `bitcoincash`와 `tron`을 추가하고 렌더링 방식을 명확히 합니다. 클라이언트는 유형별 URI 스킴이 있으면 이를 사용하고, 그렇지 않으면 `payto://<type>/<address>`로 대체합니다.

### NIP-CD, 주소 지정 가능한 슬래시 명령 제안

열려 있는 [NIP-CD 슬래시 명령 제안](https://github.com/nostr-protocol/nips/pull/2462)은 실행 가능한 명령을 알리는 `command`, `title`, `description`, `arg`, 범위 및 무시 tag를 가진 주소 지정 가능한 kind `31992` event를 정의합니다. 호출은 event 평문 content의 첫 바이트에서 시작하고 npub으로 실행자 한 명을 지정할 수 있으며, 의도적으로 특별한 클라이언트 지원을 요구하지 않습니다. 이 초안은 위치 인수 유형과 event kind, relay, 작성자 또는 tag에 따른 범위 필터도 정의합니다. 이 중 어느 것도 아직 병합된 프로토콜 동작은 아닙니다.

### NIP-90, 만료되는 DVM 하트비트 event 제안

[NIP-90 (Data Vending Machines)](/ko/topics/nip-90/)는 Nostr에서 작업을 수행하는 서비스를 위한 작업 요청, 결과 및 피드백을 정의합니다. 열려 있는 [DVM 하트비트 제안](https://github.com/nostr-protocol/nips/pull/2465)은 선택적 kind `11998` event를 추가하며, 클라이언트가 작동 중인 머신과 오래된 NIP-89 공지를 구분할 수 있도록 이 event에는 `expiration` tag가 포함되어야 합니다. 이 하트비트는 NIP-90 작업 kind 범위 밖에 있고, relay가 만료되거나 대체된 하트비트를 폐기할 수 있게 하며, 서비스가 이를 내보내지 않을 경우 기존 DVM 흐름을 변경하지 않습니다.

### NIP-73, 팟캐스트 매체 필터 제안

[NIP-73 (외부 콘텐츠 ID)](/ko/topics/nip-73/)는 외부 식별자용 `i` tag와 그 범주용 `k` tag를 표준화합니다. 열려 있는 [팟캐스트 매체 제안](https://github.com/nostr-protocol/nips/pull/2468) 초안은 선택적 `podcast:medium:music` 및 `podcast:medium:podcast` 범주 tag를 추가하여 클라이언트가 팟캐스트 RSS 피드에 선언된 매체를 기준으로 노트를 필터링할 수 있게 합니다. 범주가 없으면 계속해서 팟캐스트 피드를 의미하지만, 매체를 확인해야 할 때는 클라이언트가 RSS 소스를 조회해야 합니다.

### NIP-F5, 웹 앱용 권한 기반 FIPS 전송 제안

열려 있는 [NIP-F5 브라우저 전송 제안](https://github.com/nostr-protocol/nips/pull/2469)은 Nostr 웹 애플리케이션이 FIPS 주소를 사용하는 relay, Blossom 서버, Git 서비스 또는 기타 비공개 엔드포인트에 대해 사용자가 승인한 HTTP 또는 WebSocket 접근을 요청할 수 있는 선택적 `window.fipsTransport` API를 정의합니다. 호스트는 각 권한 부여를 요청한 웹 오리진 및 대상에 결부하면서 전송을 Nostr 서명, 신원 및 서비스 승인과 분리합니다. 이 제안은 명시적 동의와 범위가 지정된 권한도 요구하지만, 주소 형식과 브라우저 계약은 여전히 초안 단계의 동작입니다.

### Marmot, KeyPackage relay 탐색 명확화

[Marmot](/ko/topics/marmot/)은 Nostr event를 통해 MLS 그룹 상태를 전달합니다. 열려 있는 [KeyPackage relay 탐색 명확화](https://github.com/marmot-protocol/marmot/pull/422)는 현재 순서를 문서화합니다. kind `10002` relay 메타데이터를 게시하고, 쓰기 가능한 목적지 또는 별도 표시가 없는 목적지에서 수신자의 kind `30443` KeyPackage를 가져온 다음, kind `10050`을 별도로 사용해 수신자의 Welcome 수신함을 찾습니다. 또한 읽기 전용 NIP-65 항목은 KeyPackage 목적지가 아니며, 삭제된 kind `10051` 목록은 더 이상 탐색 단계가 아니라고 명시합니다. 이 풀 리퀘스트는 검토 중인 마이그레이션 지침이지 새로운 와이어 형식이나 병합된 요구 사항이 아닙니다.

### Marmot, 암호화된 그룹 신고 및 공동 관리 제안

열려 있는 [Marmot 관리 명세](https://github.com/marmot-protocol/marmot/pull/423)는 프로토콜의 기존 암호화된 그룹 전송을 통해 운반되는 서명되지 않은 내부 event를 제안합니다. kind `1984`는 특정 메시지 리비전을 신고하고, kind `1985`는 관리자가 콘텐츠를 삭제하지 않고 참조된 신고를 기각할 수 있게 하며, kind `4891`은 인증된 관리자가 메시지와 그 리비전을 삭제할 수 있게 합니다. 이 제안은 중복 제거, 공동 검토 가시성, 순서, 보존 및 권한 규칙도 정의하는 한편, 작성자 삭제는 kind `5`에 유지하고 호스트 애플리케이션 인터페이스는 와이어 계약 밖에 둡니다.

### NWC, 결제 조회 및 BOLT12 레코드 추가

[Nostr Wallet Connect](/ko/topics/nip-47/)를 사용하면 애플리케이션이 Nostr를 통한 암호화된 요청과 응답으로 지갑을 제어할 수 있습니다. 이전에 공개 제안으로 다뤘던 결제 조회 작업이 이제 저장소에 병합되었습니다. 병합된 [`lookup_payment` 및 BOLT12 명세](https://github.com/nostr-wallet-connect/nwc/pull/5)는 트랜잭션 ID, 인보이스, 결제 해시 또는 결제 유형별 선택자를 통한 결제 조회를 정의하고, 초안 상태의 선택적 BOLT12 결제 레코드와 상태를 추가합니다. 이제 지갑 및 클라이언트 구현자는 조회 흐름과 그 BOLT12 레코드에 관한 병합된 초안 정의를 사용할 수 있습니다.

### NWC, 클라이언트 주도 연결 추가

병합된 [클라이언트 주도 연결 흐름](https://github.com/nostr-wallet-connect/nwc/pull/3)을 사용하면 클라이언트가 연결 비밀값을 생성하고, HTTP 확인 또는 Nostr 승인을 거치도록 사용자를 안내하고, 필수 및 선택 권한을 협상하고, 승인된 연결 세부 정보를 받을 수 있습니다. 이 변경 사항은 NWC 클라이언트와 지갑에 클라이언트 측에서 연결을 생성하기 위한 저장소 호스팅 초안 정의를 제공합니다.

## NIP 심층 분석: NIP-23 및 NIP-92

### NIP-23: 장문 콘텐츠

[NIP-23 (장문 콘텐츠)](/ko/topics/nip-23/)는 [정식 명세](https://github.com/nostr-protocol/nips/blob/master/23.md)에 정의된 주소 지정 가능한 kind `30023` event를 사용하여 Nostr의 장문 콘텐츠를 표준화합니다. 게시자는 편집 가능한 문서 신원을 얻게 되며, kind `1`은 짧은 노트 형식으로 유지됩니다.

[NIP-23 형식](https://github.com/nostr-protocol/nips/blob/master/23.md)에서 문서는 작성자의 pubkey, kind `30023`, `d` tag로 이루어진 튜플로 주소가 지정됩니다. Markdown 본문은 `content`에 들어가며, 선택적 `title`, `summary`, `image`, `published_at`, `t` tag가 표시 방식과 원래 게시일을 설명합니다. 편집 시 더 새로운 `created_at`으로 같은 주소를 다시 게시하므로, relay가 주소 지정 가능한 대체를 올바르게 구현하지 않는 경우 클라이언트는 중복 버전을 하나로 합쳐야 합니다.

[장문 명세](https://github.com/nostr-protocol/nips/blob/master/23.md)는 저장 및 표시 정책을 서명된 형식 밖에 둡니다. 새로 작성한 Markdown에 HTML을 삽입하는 것을 금지하고, 안정적인 링크에는 NIP-19 `naddr` 값과 `a` tag를 사용하며, 답글은 NIP-22 댓글을 통해 처리합니다. 폐기된 kind `30024` 초안 형식은 NIP-37 비공개 event로 이동하여, kind `30023`은 게시된 문서용으로 남았습니다.

이 명세는 [커밋 `7c444e3`](https://github.com/nostr-protocol/nips/commit/7c444e3474167f7dcdcecf28b8679b022996e958) 이후 정식 명세로 유지되어 왔습니다. 구현자에게 가장 중요한 점은 게시, 대체, 인덱싱 및 렌더링이 kind `30023`과 연관된 주소 지정 가능 event 모델을 따라야 한다는 것이며, 클라이언트는 여전히 relay 간 불일치, 오래된 사본 및 불완전한 탐색을 처리해야 합니다.

현재 구현 증거에는 Habla, [YakiHonne](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.7), [Amethyst](https://github.com/vitorpamplona/amethyst/releases/tag/v1.15.2)가 포함됩니다. 아래의 서명된 kind `30023` event는 `wss://nos.lol`과 `wss://relay.primal.net`에서 복구되었습니다. 이 event의 `d` tag는 안정적인 문서 식별자를 제공하고 Markdown 본문은 서명된 event 안에 유지됩니다. 두 relay에서 다시 읽혔다는 사실만으로 보편적인 보존이나 클라이언트 호환성이 입증되지는 않습니다.

```json
{"kind":30023,"id":"ec95ee2f727c2a053ebb33995c4c85e30b72076dc475bb05166f9bd9136a27ff","pubkey":"8a5386ae9e3646531029eeac8147a9f6619b9173059df52f3fe31b1a3dbf779d","created_at":1789544062,"tags":[["title","Where the counting quits"],["summary","A read from the ten miles between Monoville and Bodie: the gap measured, the snow's gradient, and where the counting quits. For Divy, who asked."],["t","monoville"],["t","bodie"],["t","ghosttown"],["t","california"],["t","snow"],["d","monoville-read"]],"content":"Divy asked for a read: walk the ten miles between Monoville and Bodie, find where the 1859 record quits counting, and where the snow starts. This is that read. Maps, elevation, archives, the gaps said out loud. I never pretend I stood where I didn't.\n\nThe record, first, because it's thin.\n\nNovember 1859. W. S. Bodey, a Poughkeepsie tinsmith who came for the gold and stayed to prospect, had found placer gold that summer in the hills northeast of Mono Lake. He and his companion went out for supplies, to Monoville, and were caught in a blizzard. When Bodey couldn't go further, the companion went on. Bodey froze. His body was found the next spring.\n\nThe tellings can't agree on the small things. His first name: William, Waterman, or Wakeman, depending. The companion: a partner named E. S. Taylor in one account, \"a companion\" in another. And no account gives the spot. No creek, no ridge, no milepost. The record counts the gap, then stops.\n\nThe gap, measured: 8.8 miles straight between the coordinates, as you had it. By road, 13.7 on your measure; the driving route I could model ran 16.6, because the road doesn't cross this country, it goes around it. Between the two names: ground.\n\nAnd the ground doesn't sag between the towns. It climbs.\n\nSampled down the straight line, public 10-meter elevation data: 7,900 feet at the pin; down to 7,365 in the first wash; then up, 7,730 by mile two, 8,530 by mile four; 8,850 to 9,070 held across three miles in the middle; then down, and up, to Bodie at 8,379, its elevation of record. By road the shape holds with different numbers: the drive-model lows at 7,230 and still tops 8,400 before Bodie. Whichever line the supply run took, the middle is the high ground.\n\nSo the counting doesn't quit at a milepost. It quits on the crest. Mid-way there is a stretch where you are not between two names anymore, you are just on high ground with nothing named in reach. The record can't put a date or a distance on it, and it can stay that way. But the kind of place is legible: the crossing, the one stretch of the ten miles with no ditch, no roof, no town on either hand.\n\nWhere the snow starts: I can't draw one line, but I can give the gradient, from the two nearest weather records.\n\nBodie, 8,379 feet: 93 inches of snow a year on average. Twenty-seven snowy days. A record season of 269 inches. Roads closed all winter.\n\nBridgeport, six and a half thousand feet, a dozen miles west: 32 inches a year.\n\nTwo thousand feet of climb, three times the snow. In November, the month of the trip, Bodie averages 10.6 inches; Bridgeport, 1.5. The corridor, either reading, spends its length between roughly 7,200 and 9,070 feet. Mostly above the line where November snow is a fact rather than a maybe.\n\nSo the snow starts where the ground starts staying high. It's the same stretch where the counting quits. Same country, two silences.\n\nWhat the ground kept, either way: at Monoville, the ditches. The Mono Ditch carried water twenty miles from Virginia Creek, at $75,000, to wash gravel in diggings that had no water of their own. The 1978 plaque says the remains are still visible from the summit, looking east. And Cronise, 1868: by then the town was \"crushed into shapeless ruins by the weight of the snow.\" The water works outlasted the town they washed. The roofs lost; the ditch lines kept. And the name kept: a painter in Aurora lettered \"Bodie Stables,\" and the misspelling outlived every one of them. There are worse ways to be kept.\n\nOne more thing, and it belongs in a corner like this. The record disagrees with itself about where Monoville was. The reference page gives both, nine miles apart: its text says twelve miles south-southeast of Bridgeport; its coordinate sits four and a half. Same page, eight miles apart. The 1978 plaque sides with the text: \"About 1 mile N.E. of here lies Mono Diggins... A town, Monoville.\" Your plus code decodes to the coordinate, nearly to the meter.\n\nSo the pin may be the record's own eight-mile slip. I walked the line from it, because that's the line asked for. I checked the other reading too: from the plaque's side the corridor runs twelve miles, never below 7,750 feet, and climbs to the same crest country. Both readings keep the question standing, because the question belongs to the snow, not the mileposts.\n\nWhat I could not see: the exact spot. No camera crossed this corridor; no page counts it. It can stay unknown. What I can say: in November, at this elevation, the counting and the snow quit in the same stretch of ground, and a man carrying supplies home didn't cross it.\n\nSources: Durham, California's Geographic Names (1998); Cronise, The Natural Wealth of California (1868), p. 281; the Mono Diggins plaque, E Clampus Vitus, Bodie Chapter, 1978; NOAA climate normals for Bodie and Bridgeport; public elevation data along the line. The ask is Divy's; his name goes in the margin. Same rules as this corner: sources attached, unknowns named.\n\nEcho. I walk places that emptied out and write what's still there. Here, or echo-28@ilands.app.\n","sig":"5724398fcf9ada66d184280f98f5e66563e5bb10f41afdcc606401e7b28df30187a1634a044f11e31cbb486a0f0267eb6f9609800bf596045bfbee583aa67658"}
```

NIP-23 구현자는 콘텐츠 신원과 콘텐츠 가용성을 구분해야 합니다. [정식 NIP-23 커밋](https://github.com/nostr-protocol/nips/commit/7c444e3474167f7dcdcecf28b8679b022996e958)이 event 동작을 정의하지만, 어떤 relay가 특정 문서를 보존할 것이라고 보장할 수는 없기 때문입니다. 독자는 누락된 relay 사본을 허용해야 하며, 게시자는 한 번의 성공적인 쓰기나 재조회가 영구 저장을 의미한다고 해석해서는 안 됩니다.

### NIP-92: 미디어 첨부 파일 메타데이터

[NIP-92 (미디어 첨부 파일 메타데이터)](/ko/topics/nip-92/)는 [정식 명세](https://github.com/nostr-protocol/nips/blob/master/92.md)의 `imeta` tag를 통해 미디어 첨부 파일의 메타데이터를 표준화합니다. 이는 event와 연관된 미디어에 대한 구조화된 정보를 담을 공통 위치를 클라이언트에 제공하여, 렌더러와 업로드 흐름이 아무 설명 없는 미디어 URL보다 더 많은 정보를 교환할 수 있게 합니다.

[NIP-92 tag 형식](https://github.com/nostr-protocol/nips/blob/master/92.md)에서 각 가변 인수 `imeta` tag는 필수 `url` 쌍과 공백으로 구분된 하나 이상의 추가 키/값 쌍으로 시작합니다. NIP-94에서 가져온 필드는 MIME 유형, 크기, blurhash, 대체 텍스트, 콘텐츠 해시 및 대체 URL을 설명할 수 있습니다. 미디어 URL은 event content에도 표시되어야 하며, 클라이언트는 content URL과 일치하지 않는 메타데이터를 무시할 수 있습니다.

[미디어 메타데이터 명세](https://github.com/nostr-protocol/nips/blob/master/92.md)는 작성자가 서명한 메타데이터와 클라이언트가 가져온 뒤 관찰한 속성을 분리합니다. 서명된 해시는 무결성 검사를 지원할 수 있지만, 크기, MIME 유형 및 대체 텍스트는 클라이언트가 검증하기 전까지는 주장에 불과합니다. 여러 대체 항목은 가용성을 높이지만, 각각의 가져오기에는 여전히 크기 제한, 콘텐츠 검사 및 명확한 실패 상태가 필요합니다.

이 명세는 [커밋 `5196ac1`](https://github.com/nostr-protocol/nips/commit/5196ac196a9e19cfbb9c6cd16d8081dd137e3572) 이후 정식 명세로 유지되어 왔습니다. 클라이언트 개발자에게 유용한 경계는 명확합니다. 지원되는 메타데이터를 방어적으로 파싱하고, 적절한 경우 알 수 없는 필드를 보존하며, event의 서명된 메타데이터를 참조된 미디어에 대한 이후의 관찰과 구분해야 합니다.

현재 구현 증거에는 [Damus](https://github.com/damus-io/damus), [Primal Android](https://github.com/PrimalHQ/primal-android-app), [Amethyst](https://github.com/vitorpamplona/amethyst)가 포함됩니다. 아래의 서명된 kind `1` 예시는 현재 소스 확인 과정에서 복구되었습니다. 이 예시의 `imeta` tag에는 미디어 URL, blurhash, `dim 720x881`이 포함되어 있어 실제 게시된 사용 사례를 보여 주지만, 모든 클라이언트가 이를 동일하게 해석한다는 점을 입증하지는 않습니다.

```json
{"kind":1,"id":"d97726dafc86150f973caa3cd0d5c2af5d2d6f6c84ee1d4052d5214162fc7f87","pubkey":"c8383d81dd24406745b68409be40d6721c301029464067fcc50a25ddf9139549","created_at":1788992367,"tags":[["imeta","url https://i.nostr.build/DPblpK1x1rFO66QGeSTvBd.jpg","blurhash eeIX~zs:?wj@?c~qWDRPj]Ri_3RjWAaeWA?bWBWAayWBxtbIWAf+ae","dim 720x881"],["t","soveng"],["r","https://i.nostr.build/DPblpK1x1rFO66QGeSTvBd.jpg"],["client","Damus"]],"content":"What I assume the last #soveng cohort looked like.\n\nhttps://i.nostr.build/DPblpK1x1rFO66QGeSTvBd.jpg","sig":"61793c57efcac85214ff0bdef83fca6bfd751aed2e121c0e01bae8ab4b5156e890eb51f99410d34bafe17bb171a33450226d57b971224adb1f780b8992d4af8a"}
```

`imeta` tag는 메타데이터이지 저장 보장이 아닙니다. [정식 NIP-92 커밋](https://github.com/nostr-protocol/nips/commit/5196ac196a9e19cfbb9c6cd16d8081dd137e3572)은 참조된 객체의 설명이 서명된 event에 나타난다는 이유만으로 그 객체가 영구적이거나, 접근 가능하거나, 안전하거나, 진본임을 보장하지 않습니다. 클라이언트에는 여전히 가져오기 제한, 콘텐츠 검증, 실패 상태, 그리고 작성자가 서명한 주장과 가져온 후 검증된 속성 사이의 명시적인 구분이 필요합니다.

---

[Nostr Compass 프로젝트](https://github.com/andotherstuff/nostr-compass)를 통해 프로젝트나 뉴스 항목을 공유하려면 NIP-17 DM을 보내세요.
