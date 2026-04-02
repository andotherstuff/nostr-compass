---
title: 'Nostr Compass #16'
date: 2026-04-01
translationOf: /en/newsletters/2026-04-01-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [Amethyst](https://github.com/vitorpamplona/amethyst)가 고정 노트, [NIP-86](/ko/topics/nip-86/)을 통한 relay 관리, [NIP-62](/ko/topics/nip-62/) Request to Vanish 지원이 포함된 [v1.07.0](#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish)을 출시했습니다. [NIP-5A](#nip-5a-merges-bringing-static-websites-to-nostr) (Static Websites)가 NIPs 저장소에 병합되어 [Blossom](/ko/topics/blossom/) 스토리지를 사용해 Nostr 키페어 아래 웹사이트를 호스팅하는 방법을 정의합니다. [Flotilla](https://gitea.coracle.social/coracle/flotilla)는 음성 방, 이메일/비밀번호 로그인, proof-of-work DM이 포함된 [v1.7.0](#flotilla-v170-adds-voice-rooms-and-email-login)을 출시했습니다. [White Noise](https://github.com/marmot-protocol/whitenoise)는 [v2026.3.23](#white-noise-fixes-relay-churn-and-expands-client-controls)에서 relay churn을 수정했고, [nospeak](https://github.com/psic4t/nospeak)는 가입 없는 암호화 메신저로 [1.0.0](#nospeak-launches-as-a-10-private-messenger)을 출시했습니다. [Nymchat](https://github.com/Spl0itable/NYM)는 [Marmot](#nymchat-ships-marmot-powered-group-chats)를 채택해 MLS 암호화 그룹 채팅과 NIP-17 대체 경로를 제공합니다. [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)는 비공개 캘린더 목록과 ICS 가져오기가 포함된 [v1.0.0](#calendar-by-form-v100)에 도달했고, [Amber](https://github.com/greenart7c3/Amber)는 [니모닉 복구와 NIP-42 relay 인증 화이트리스트](#amber-v502-through-v504)를 추가했으며, [Marmot 사양](#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications)은 KeyPackages를 주소 지정 가능 이벤트로 옮기고 MIP-05 푸시 알림 형식을 더 엄격하게 했습니다.

## 뉴스

### Amethyst ships pinned notes, relay management, and Request to Vanish

vitorpamplona가 유지 관리하는 Android 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)가 3일 동안 [v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0)부터 [v1.07.5](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.5)까지 여섯 개의 릴리스를 배포했습니다. 핵심 기능은 여섯 개의 프로토콜 표면에 걸쳐 있습니다. 고정 노트, 전용 투표 피드 화면, relay에 전체 이벤트 삭제를 요청하는 [NIP-62](/ko/topics/nip-62/) (Request to Vanish) 지원, 클라이언트 내부에서의 [NIP-86](/ko/topics/nip-86/) (Relay Management API), relay 정보 화면의 [NIP-66](/ko/topics/nip-66/) (Relay Discovery and Liveness Monitoring) 평가, 그리고 [NIP-43](/ko/topics/nip-43/) (Relay Access Metadata and Requests) 멤버 정보 표시입니다.

[NIP-86](/ko/topics/nip-86/)은 relay 운영자를 위한 JSON-RPC 인터페이스를 정의하여, 클라이언트가 pubkey 차단, pubkey 허용, 차단된 사용자 목록 조회 같은 관리 명령을 표준화된 API로 보낼 수 있게 합니다. Amethyst는 이제 이를 relay 관리 UI에 직접 노출하므로, 자신의 relay를 운영하는 사용자가 게시에 사용하는 동일한 클라이언트에서 relay를 관리할 수 있습니다. [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039)는 차단/허용 pubkey를 위한 기존 16진수 입력 대화상자를 대화형 사용자 검색 대화상자로 교체합니다.

v1.07.2는 GIF 키보드 업로드를 추가하고, 이전 Amber 버전이 `rejected` 필드에 빈 문자열을 반환해 Amber 거부 응답을 잘못 읽던 서명 회귀를 수정했습니다([PR #2042](https://github.com/vitorpamplona/amethyst/pull/2042)). v1.07.5는 이미지 업로드 충돌을 수정합니다. 이번 주 초의 [v1.06.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.2)와 [v1.06.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.3)은 단일/복수 선택 투표를 위한 poll type 선택기, 비디오 진행 막대 drag-to-seek, 익명 게시 개선을 추가했습니다.

### NIP-5A merges, bringing static websites to Nostr

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) (Static Websites)가 [PR #1538](https://github.com/nostr-protocol/nips/pull/1538)을 통해 병합되며, Nostr 키페어 아래 정적 웹사이트를 호스팅하는 방법을 정의했습니다. 이 사양은 두 가지 이벤트 kind를 사용합니다. kind `15128`은 pubkey당 하나의 루트 사이트용이고, kind `35128`은 `d` 태그로 식별되는 이름 있는 사이트용입니다. 각 매니페스트는 URL 경로를 SHA256 해시에 매핑하며, 실제 파일이 위치한 [Blossom](/ko/topics/blossom/) 스토리지 호스트를 가리키는 선택적 `server` 태그를 가질 수 있습니다.

호스팅 모델은 다음과 같이 동작합니다. 사이트 저자가 정적 사이트를 빌드하고, 파일을 하나 이상의 Blossom 서버에 업로드한 다음, 경로를 콘텐츠 해시에 매핑하는 서명된 매니페스트 이벤트를 게시합니다. 호스트 서버는 웹 요청을 수신하고, 서브도메인에서 저자의 pubkey를 해석하며, 저자의 [NIP-65](/ko/topics/nip-65/) relay 목록에서 매니페스트를 가져와, 일치하는 blob을 Blossom에서 다운로드해 파일을 제공합니다. 사이트는 업데이트된 매니페스트에 오직 해당 키만 서명할 수 있기 때문에 저자의 통제 아래에 머뭅니다. 어떤 NIP-5A 지원 서버라도 동일한 매니페스트에서 같은 사이트를 제공할 수 있기 때문에 호스트 서버는 대체 가능합니다.

이 사양은 이미 존재하는 인프라 위에 세워졌습니다. lez가 만든 NIP-5A 참조 호스트 구현 [nsite](https://github.com/lez/nsite)와 hzrd149의 관리 UI [nsite-manager](https://github.com/hzrd149/nsite-manager)는 NIP 병합 이전부터 이미 돌아가고 있었습니다. 이번 병합은 이벤트 kind와 URL 해석 규칙을 공식화하여, 두 번째, 세 번째 구현이 겨냥할 수 있는 안정적인 목표를 제공합니다.

### White Noise fixes relay churn and expands client controls

[Marmot](/ko/topics/marmot/) 프로토콜 위에 구축된 개인 메신저 [White Noise](https://github.com/marmot-protocol/whitenoise)가 3월 25일 [v2026.3.23](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.3.23)을 출시했습니다. 핵심 작업은 relay 안정성입니다. relay 목록 게시가 quorum 로직을 사용하고 나머지는 백그라운드에서 재시도하도록 바뀌었기 때문에, 이제 로그인은 모든 relay 목록 게시가 끝날 때까지 기다리지 않고 진행됩니다. 단발성 fetch와 publish는 오래 살아남는 풀에 남아 있지 않고 범위가 한정된 임시 relay 세션을 사용하며, 복원된 세션은 시작 후 그룹 새로고침 경로를 회복하고, 앱은 [PR #495](https://github.com/marmot-protocol/whitenoise/pull/495), [PR #502](https://github.com/marmot-protocol/whitenoise/pull/502)를 통해 relay 진단과 relay 상태 점검을 노출합니다.

같은 릴리스는 대화 동작도 바꿉니다. [PR #468](https://github.com/marmot-protocol/whitenoise/pull/468)은 `q` 태그와 `nostr:nevent` 참조를 사용하는 NIP-C7 답글 스레딩을 추가하고, [PR #471](https://github.com/marmot-protocol/whitenoise/pull/471)과 [PR #512](https://github.com/marmot-protocol/whitenoise/pull/512)는 삭제된 메시지를 조용히 제거하지 않고 삭제된 자리표시자로 남겨 두며, [PR #478](https://github.com/marmot-protocol/whitenoise/pull/478)은 [NIP-44](/ko/topics/nip-44/) (Encrypted Payloads) 익명 보고를 사용하는 인앱 버그 리포트 흐름을 추가하고, [PR #486](https://github.com/marmot-protocol/whitenoise/pull/486)은 클라이언트 안에 직접 지원 채팅을 추가합니다. 같은 시기에 사용자 대면 메시지 제어도 들어왔습니다. [PR #532](https://github.com/marmot-protocol/whitenoise/pull/532)는 채팅 보관, [PR #541](https://github.com/marmot-protocol/whitenoise/pull/541)는 기간 설정이 가능한 뮤트/언뮤트, [PR #535](https://github.com/marmot-protocol/whitenoise/pull/535)는 알림 설정을 추가합니다. [PR #539](https://github.com/marmot-protocol/whitenoise/pull/539)는 준비 단계의 푸시 등록 작업으로, iOS의 APNs 등록과 Android의 Play Services 탐지를 연결해 그 위에 등록 기능을 구축할 수 있게 합니다. 백엔드 측에서는 [MDK](https://github.com/marmot-protocol/mdk)가 MIP-05 푸시 알림 프리미티브와 notification request builder를 추가했고([PR #235](https://github.com/marmot-protocol/mdk/pull/235), [PR #238](https://github.com/marmot-protocol/mdk/pull/238)), [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)는 푸시 알림 등록 영속화([PR #688](https://github.com/marmot-protocol/whitenoise-rs/pull/688)), 백그라운드 작업 취소 수정([PR #696](https://github.com/marmot-protocol/whitenoise-rs/pull/696)), 시작 시 key package 복구([PR #693](https://github.com/marmot-protocol/whitenoise-rs/pull/693))를 추가했습니다.

### Nostr VPN reaches v0.3.0 with roster sync and invite v2

[지난주 출시 보도에 이어](/ko/newsletters/2026-03-25-newsletter/#nostr-vpn-launches-as-a-tailscale-alternative), 신호에 Nostr relay를 사용하고 암호화 터널에 WireGuard를 사용하는 P2P VPN [nostr-vpn](https://github.com/mmalmi/nostr-vpn)이 빠른 릴리스 속도를 유지하며 [v0.3.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.3)까지 배포를 이어갔습니다. 버전 범프에는 두 가지 호환성 깨짐이 포함됩니다. invite 형식이 v2로 이동했고(0.3.0은 여전히 v1 invite를 가져올 수 있지만, 이전 빌드는 v2 invite를 가져올 수 없음), signaling 프로토콜에 관리자 서명 roster sync가 추가되었습니다. 버전이 섞인 피어도 메시 계층에서는 여전히 연결될 수 있지만, 이전 피어는 roster 동기화에는 참여하지 않습니다.

roster sync 추가는 관리형 네트워크를 향한 첫걸음입니다. 이제 관리자 노드는 모든 피어에 멤버십 변경을 푸시할 수 있으므로, 메시에서 장치를 추가하거나 제거할 때 각 피어가 수동으로 구성을 업데이트할 필요가 없습니다. 같은 주의 v0.2.x 릴리스들은 구체적 배포 문제를 다뤘습니다. [v0.2.22](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.22)부터 [v0.2.28](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.28)까지는 Windows 서비스 관리 수정, Android 빌드 스크립트 추가, LAN pairing 흐름 정제가 있었습니다.

### nospeak launches as a 1.0 private messenger

Nostr 기반 개인 메신저 [nospeak](https://github.com/psic4t/nospeak)가 3월 27일 [1.0.0](https://github.com/psic4t/nospeak/releases/tag/v1.0.0)을 출시했습니다. 이 프로젝트는 일대일 및 그룹 대화, 연락처 관리, 자체 호스팅 가능한 아키텍처를 포함합니다. 일대일 채팅은 [NIP-17](/ko/topics/nip-17/) (Private Direct Messages)을 사용하며, 이는 [NIP-59](/ko/topics/nip-59/) (Gift Wrap)와 [NIP-44](/ko/topics/nip-44/) (Encrypted Payloads)를 결합해 relay로부터 발신자를 숨깁니다. 미디어의 경우 파일은 Blossom 서버 업로드 전에 클라이언트 측에서 AES-256-GCM으로 암호화됩니다. 이 릴리스는 자체 호스팅을 위한 컨테이너 이미지로도 배포됩니다.

### Flotilla v1.7.0 adds voice rooms and email login

"relay를 그룹으로" 모델을 중심으로 구축된 hodlbod의 Discord 유사 [NIP-29](/ko/topics/nip-29/) (Relay-based Groups) 클라이언트 [Flotilla](https://gitea.coracle.social/coracle/flotilla)가 3월 30일과 31일 [v1.7.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0), [v1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.1)을 출시했습니다. 핵심 기능은 mplorentz가 기여한 voice room입니다. 이제 사용자는 그룹 채널 안에서 음성 통화에 참여할 수 있으며, 오디오 입력 장치를 선택하고 음성 통화에 참여할지 아니면 텍스트 채팅만 볼지를 고를 수 있는 참가 대화상자([PR #109](https://gitea.coracle.social/coracle/flotilla/pulls/109))가 제공됩니다. 이 대화상자는 이전 버전의 UX 문제를 해결합니다. 이전에는 음성 지원 룸에 들어가면 사용자가 메시지만 읽거나 방 설정만 확인하고 싶어도 마이크가 강제로 켜졌습니다.

같은 릴리스는 Nostr 키 기반 인증의 대안으로 이메일/비밀번호 로그인, DM에서의 proof-of-work, DM 편집, 재설계된 relay 온보딩 및 설정, `supported_nips`를 통한 Blossom 지원 탐지, 개선된 알림 배지, Android 푸시 알림 대체 경로, Android 파일 업로드 수정도 추가합니다. 이어지는 v1.7.1은 오프라인 signer 사용 시 pomade registration fallback 문제를 수정합니다.

Hodlbod는 또한 zooid relay를 위한 호스팅 관리자와 대시보드 [Caravel](https://gitea.coracle.social/coracle/caravel)도 구축 중이며, 초기 개발에서 이번 주 40개의 커밋을 기록했습니다.

### Nymchat ships Marmot-powered group chats

Bitchat과 브리지된 일시적 채팅 클라이언트 [Nymchat](https://github.com/Spl0itable/NYM)(NYM, Nostr Ynstant Messenger라고도 함)은 이제 모든 새 그룹 채팅이 MLS 암호화 메시징을 위해 [Marmot](/ko/topics/marmot/) 프로토콜을 사용한다고 발표했습니다. 이 통합은 key package, welcome message, group message를 위해 각각 kinds `443`, `444`, `445`를 사용하며, 순방향 비밀성, 사후 침해 보안성, 메타데이터 누출 제로를 제공합니다. 수신자가 MLS를 사용할 수 없는 경우 Nymchat은 이전 [NIP-17](/ko/topics/nip-17/) (Private Direct Messages) 그룹 채팅 경로로 대체하며, 이 역시 종단간 암호화이지만 MLS의 ratchet-tree 속성은 없습니다.

이번 주의 v3.55, v3.56 시리즈는 새 장치에서의 로딩, 나가기 동작, 알림 라우팅, 읽지 않음 배지 수 같은 그룹 채팅 엣지 케이스에 집중했습니다. 같은 주기에는 이스케이프되지 않은 HTML에서 비롯된 XSS 취약점도 수정했고, 사용자 닉네임까지 확장된 키워드 및 구문 차단 기능도 추가했습니다. 이로써 Nymchat은 [White Noise](#white-noise-fixes-relay-churn-and-expands-client-controls), [OpenChat](#openchat-v024-through-v030)과 함께 또 하나의 Marmot 클라이언트가 되었고, 동일한 프로토콜 위에서 MLS 암호화 그룹 메시지를 교환할 수 있는 앱 집합을 넓혔습니다.

## 릴리스

### Calendar by Form* v1.0.0

[NIP-52](/ko/topics/nip-52/) (Calendar Events) 기반 탈중앙화 캘린더 앱 [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)가 3월 29일 [v1.0.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.0.0)에 도달했습니다. 이 릴리스는 암호화된 Nostr 이벤트(kind `32123`)와 [NIP-44](/ko/topics/nip-44/) (Encrypted Payloads) 자기 암호화를 사용하는 비공개 캘린더 목록을 추가해, 사용자가 relay에 그룹 구조를 노출하지 않고 이벤트를 비공개 컬렉션으로 정리할 수 있게 합니다. 같은 릴리스는 다른 애플리케이션에서 캘린더 데이터를 가져오기 위한 ICS intent 처리와, 사용자 간 이벤트 공유를 위한 invitation request도 추가합니다.

### Amber v5.0.2 through v5.0.4

[NIP-55](/ko/topics/nip-55/) (Android Signer Application) 서명자 앱 [Amber](https://github.com/greenart7c3/Amber)가 세 개의 포인트 릴리스를 배포했습니다. [v5.0.2](https://github.com/greenart7c3/Amber/releases/tag/v5.0.2), [v5.0.3](https://github.com/greenart7c3/Amber/releases/tag/v5.0.3), [v5.0.4](https://github.com/greenart7c3/Amber/releases/tag/v5.0.4)입니다. 가장 눈에 띄는 추가 사항은 mnemonic recovery phrase 로그인([PR #358](https://github.com/greenart7c3/Amber/pull/358))으로, 사용자가 원시 nsec 또는 ncryptsec 문자열을 요구받지 않고 BIP39 시드 문구로 signer를 복원할 수 있게 합니다. [PR #357](https://github.com/greenart7c3/Amber/pull/357)은 [NIP-42](/ko/topics/nip-42/) relay 인증 화이트리스트를 추가해, 어떤 relay가 클라이언트 인증을 요청할 수 있는지를 사용자가 제한할 수 있게 합니다. [PR #353](https://github.com/greenart7c3/Amber/pull/353)은 decrypt 권한을 위한 암호화 범위 선택을 추가해, 포괄적 권한 대신 NIP-04 전용 또는 NIP-44 전용 decrypt 접근을 부여할 수 있게 합니다. v5.0.4는 거부 처리에서 범위 지정 encrypt/decrypt 권한을 존중하지 않던 버그를 수정하고 여러 bunker 요청 수신 시 성능을 개선합니다.

### Aegis v0.4.0

크로스 플랫폼 signer [Aegis](https://github.com/ZharlieW/Aegis)가 3월 26일 [v0.4.0](https://github.com/ZharlieW/Aegis/releases/tag/v0.4.0)을 출시했습니다. 이 릴리스는 Settings에 Full 및 Selective authorization 모드를 추가하고 여러 QR 스캔 문제를 수정합니다. 후속 커밋 [d4f799f](https://github.com/ZharlieW/Aegis/commit/d4f799fe51dd82968d54f72ac77f2de29d0cfe6b), [3313af9](https://github.com/ZharlieW/Aegis/commit/3313af92e55e449ebc98fbd91a085bd444d716e7), [3b214e4](https://github.com/ZharlieW/Aegis/commit/3b214e4176f5dbe7f18690d0996e69dd151fe00f), [e4f40b6](https://github.com/ZharlieW/Aegis/commit/e4f40b6f1f48c2dae1bb5e4246df26c26dba419e)은 같은 방향의 작업을 계속하며, 일괄 선택 제어, 재사용 가능한 batch selection 통계, set-all-groups 선택 API, 앱 권한 페이지의 권한별 사용 통계를 추가합니다.

### Schemata v0.2.7 through v0.3.0

Nostr 이벤트 kind 검증용 JSON Schema 정의 [Schemata](https://github.com/nostrability/schemata)가 21개의 병합된 PR과 함께 [v0.2.7](https://github.com/nostrability/schemata/releases/tag/v0.2.7)부터 [v0.3.0](https://github.com/nostrability/schemata/releases/tag/v0.3.0)까지 네 개의 릴리스를 배포했습니다. v0.3.0은 relay URL, 16진수 ID, MIME 타입, BOLT-11 문자열 전반의 패턴 일관성 수정([PR #126](https://github.com/nostrability/schemata/pull/126)), 중앙화된 relay URL 패턴([PR #117](https://github.com/nostrability/schemata/pull/117)), [NIP-19](/ko/topics/nip-19/) bech32 기본 타입 스키마([PR #118](https://github.com/nostrability/schemata/pull/118)), kind 777 spell 이벤트 검증([PR #125](https://github.com/nostrability/schemata/pull/125))을 포함합니다. 이제 릴리스 파이프라인은 각 릴리스 때 Nostr에 kind `1` 노트를 게시합니다([PR #120](https://github.com/nostrability/schemata/pull/120)). 즉, 프로젝트가 자신이 검증하는 프로토콜을 통해 스스로를 공지합니다. Schemata는 이제 정식 JS/TS 패키지 외에도 Rust, Go, Python, Kotlin, Java, Swift, Dart, PHP, C#/.NET, C++, Ruby, C 등 12개 이상의 언어를 지원합니다.

Schemata와 함께 팀은 동일한 검증 문제에 대해 다른 접근을 취하는 실험적 코드 생성기 [schemata-codegen](https://github.com/nostrability/schemata-codegen)도 공개했습니다. Schemata의 validator 패키지가 JSON Schema 런타임 의존성을 요구하는 반면, schemata-codegen은 스키마를 타입 지정된 네이티브 언어 구조(typed tag tuples, kind interfaces, runtime validators)로 직접 옮겨 런타임에 validator 라이브러리가 필요하지 않게 만듭니다. [codegen-vs-validators 비교 문서](https://github.com/nostrability/schemata-codegen/blob/main/CODEGEN-VS-VALIDATORS.md)는 각 접근이 적합한 시점을 설명합니다.

### BigBrotr v6.5.0 through v6.5.4

relay 분석 플랫폼 [BigBrotr](https://github.com/BigBrotr/bigbrotr)가 [v6.5.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.0)부터 [v6.5.4](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.4)까지 다섯 개 릴리스를 배포했습니다. v6.5.0은 `parse_relay_url()` 팩토리 함수를 사용해 relay URL 검증을 중앙화하고, URL 길이 검사와 경로 정제를 추가합니다. 모니터링 인프라도 수정되었습니다. 공지 이벤트는 이제 geohash 위치 태그를 포함하며([NIP-52](/ko/topics/nip-52/)를 따름), 마감 시간이 없어 무기한 멈출 수 있던 Geo/Net [NIP-66](/ko/topics/nip-66/) 메타데이터 테스트에는 타임아웃 보호가 추가되었습니다. [PR #410](https://github.com/BigBrotr/bigbrotr/pull/410)은 PostgreSQL을 16에서 18로 업그레이드하여 비동기 I/O 서브시스템과 더 나은 WAL 처리량을 relay 분석 파이프라인에 가져옵니다.

### Vertex Lab relay adds NIP-50 profile search

[npub.world](https://github.com/vertex-lab/npub.world)와 [Vertex](https://vertexlab.io/docs) Web of Trust 엔진을 만드는 [Vertex Lab](https://vertexlab.io) 팀은 `wss://relay.vertexlab.io`가 이제 프로필 쿼리에 대해 [NIP-50](/ko/topics/nip-50/) (Search)을 지원한다고 발표했습니다. NIP-50은 표준 Nostr `REQ` 필터에 `search` 필드를 확장하여, 클라이언트가 인덱싱을 지원하는 relay에 전체 텍스트 검색 쿼리를 보낼 수 있게 합니다. 이미 Web of Trust 데이터를 제공하는 relay에 프로필 검색을 추가함으로써, `relay.vertexlab.io`에 연결된 클라이언트는 별도의 검색 서비스 없이 이름이나 설명으로 사용자를 발견할 수 있습니다.

### Hashtree v0.2.17 and v0.2.18 ship WebRTC mesh and Iris Desktop

mmalmi의 콘텐츠 주소 지정 blob 저장 시스템으로 Merkle root를 Nostr에 게시하는 [Hashtree](https://github.com/mmalmi/hashtree)가 3월 31일 [v0.2.17](https://github.com/mmalmi/hashtree/releases/tag/v0.2.17)과 [v0.2.18](https://github.com/mmalmi/hashtree/releases/tag/v0.2.18)을 출시했습니다. 이 두 릴리스는 30개 커밋 질주의 정점으로, 세 가지 뚜렷한 기능을 추가합니다. 첫째, `hashtree-webrtc` 크레이트(v0.2.18에서 `hashtree-network`로 이름 변경)는 Rust CLI, 시뮬레이션 하네스, TypeScript 클라이언트 전반에 걸쳐 통합 메시 신호를 갖춘 WebRTC 기반 P2P blob 배포를 추가합니다. 둘째, 릴리스 파이프라인이 이제 Windows 아티팩트(CLI zip과 Iris 설치 프로그램)도 빌드하여 macOS, Linux, Windows까지 크로스 플랫폼 범위를 넓혔습니다. 셋째, 두 릴리스는 모두 mmalmi의 Nostr 소셜 클라이언트 Iris Desktop 0.1.0을 AppImage, .deb, Windows 설치 프로그램 자산으로 hashtree CLI와 함께 번들합니다. [Hashtree는 Blossom 호환 저장소로 출시되었을 때 뉴스레터 #10](/ko/newsletters/2026-02-18-newsletter/)에서 처음 다뤘습니다. WebRTC 계층은 중앙화된 Blossom 서버에 의존하지 않는 P2P 콘텐츠 배포를 향한 첫 단계입니다.

### Nostr Mail Client v0.7.0 through v0.7.2

Nostr 신원을 기반으로 한 Flutter 메일형 클라이언트 [Nostr Mail Client](https://github.com/nogringo/nostr-mail-client)가 3일 동안 [v0.7.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.0), [v0.7.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.1), [v0.7.2](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.2)를 배포했습니다. 사용자에게 보이는 제품 작업은 온보딩([PR #9](https://github.com/nogringo/nostr-mail-client/pull/9))과 프로필 편집([PR #10](https://github.com/nogringo/nostr-mail-client/pull/10))에 집중되어 있었으며, 이는 Nostr를 메일박스로 제시하려는 어떤 클라이언트에게도 기본 요소입니다. 이후의 포인트 릴리스는 이 작업을 새 Android 및 Linux 빌드에 패키징했습니다.

### Wisp v0.14.0 through v0.16.1

Android Nostr 클라이언트 [Wisp](https://github.com/barrydeen/wisp)가 [v0.14.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.14.0-beta)부터 [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta)까지 13개의 릴리스를 추가로 배포했습니다. 이번 주 작업에는 NIP-17 rumor JSON 수정([PR #385](https://github.com/barrydeen/wisp/pull/385)), 갤러리 카드의 repost 배지([PR #383](https://github.com/barrydeen/wisp/pull/383)), 확장 가능한 reaction 세부 정보([PR #382](https://github.com/barrydeen/wisp/pull/382)), 영구 emoji 세트([PR #381](https://github.com/barrydeen/wisp/pull/381)), 비디오 자동 재생 제어([PR #380](https://github.com/barrydeen/wisp/pull/380))가 포함됩니다. 최신 [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta)는 하이픈이 포함된 커스텀 emoji shortcode와 누락된 emoji 태그도 수정합니다.

### Primal Android 3.0.17

[Primal Android](https://github.com/PrimalHQ/primal-android-app)가 3월 24일 [3.0.17](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.17)을 출시했습니다. [PR #1000](https://github.com/PrimalHQ/primal-android-app/pull/1000)은 WalletException 타입을 NWC 응답의 에러 코드에 매핑하여, [NIP-47](/ko/topics/nip-47/) 클라이언트에 일반 오류 대신 구조화된 실패 정보를 제공합니다. [PR #995](https://github.com/PrimalHQ/primal-android-app/pull/995)는 poll zap 투표가 Top Zaps로 보이는 문제를 수정하고, [PR #998](https://github.com/PrimalHQ/primal-android-app/pull/998)은 지갑이 설정되지 않았을 때 wallet balance와 action 버튼을 숨깁니다.

### OpenChat v0.2.4 through v0.3.0

[Marmot](/ko/topics/marmot/) 스택 위에 구축된 Avalonia 기반 채팅 클라이언트 [OpenChat](https://github.com/DavidGershony/openChat)가 4일 동안 [v0.2.4](https://github.com/DavidGershony/openChat/releases/tag/v0.2.4)부터 [v0.3.0](https://github.com/DavidGershony/openChat/releases/tag/v0.3.0)까지 여섯 개의 릴리스를 배포했습니다. 커밋 로그는 "Marmot은 동작한다"에서 "누군가가 실제로 매일 사용할 수 있다" 사이의 간극을 메우는 클라이언트의 이야기를 보여줍니다. [NIP-42](/ko/topics/nip-42/) relay 인증이 도입되었고, 이어서 relay picker UI와 중복 이벤트 필터링이 추가되었습니다. 음성 메시지는 pause, resume, seek, 시간 표시를 얻었습니다. signer 경로도 강화되었습니다. Amber 연결은 업데이트된 [NIP-46](/ko/topics/nip-46/) URI 형식으로 수정되었고, WebSocket은 요청 전 자동 재연결하며, 중복 Amber 요청은 재생된 응답을 확인해 잡아냅니다. 저장 측면에서는 Linux와 macOS가 파일 기반 키를 사용하는 AES-256-GCM 보안 저장소를 얻었고, 사용자 메타데이터 fetch는 이제 [NIP-65](/ko/topics/nip-65/) relay 발견을 사용하며 결과를 로컬 데이터베이스에 캐시합니다.

### Igloo Signer 1.1

FROSTR 프로젝트의 iOS용 [FROST](/ko/topics/frost/) threshold signer [Igloo](https://github.com/FROSTR-ORG/igloo-ios-prototype)가 3월 28일 [v1.1](https://github.com/FROSTR-ORG/igloo-ios-prototype/releases/tag/v1.1)을 출시했습니다. FROST(Flexible Round-Optimized Schnorr Threshold) 서명은 다수의 signer가 집단적으로 Nostr 키페어를 제어할 수 있게 하며, t-of-n 참여자만으로도 어느 한 당사자도 전체 개인 키를 보유하지 않은 상태에서 이벤트에 서명할 수 있습니다. Igloo는 Nostr를 위한 이 접근 방식의 최초 모바일 구현 중 하나입니다.

### nak v0.19.3 and v0.19.4

fiatjaf의 커맨드라인 Nostr 도구킷 [nak](https://github.com/fiatjaf/nak)이 3월 26일과 30일 [v0.19.3](https://github.com/fiatjaf/nak/releases/tag/v0.19.3), [v0.19.4](https://github.com/fiatjaf/nak/releases/tag/v0.19.4)를 출시했습니다. 두 릴리스 모두 panic 조건을 수정합니다. [PR #118](https://github.com/fiatjaf/nak/pull/118)은 잠재적 out-of-bounds 접근을 막기 위해 `strings.Split`을 `strings.Cut`으로 대체하고, [PR #119](https://github.com/fiatjaf/nak/pull/119)은 curl flag 파싱에서 같은 종류의 panic을 방지합니다.

### Flora v0.3.0

Nostr에서 탈중앙화 화면 녹화와 공유를 위한 Chrome 확장 [Flora](https://github.com/shawnyeager/flora-extension)가 [v0.3.0](https://github.com/shawnyeager/flora-extension/releases/tag/v0.3.0)을 출시했습니다. 이 릴리스는 공개, 비공개 링크, 비공개 모드가 포함된 private encrypted video sharing을 추가합니다. 비공개 녹화본은 AES-256-GCM으로 암호화되며 [NIP-17](/ko/topics/nip-17/) (Private Direct Messages)을 통해 수신자에게 전달되므로, 녹화물이 평문 상태로 서버에 닿지 않습니다.

### YakiHonne Mobile 2.0.3

모바일 Nostr 클라이언트 [YakiHonne](https://github.com/YakiHonne/mobile-app)가 relay 리뷰와 가입 요청, 확장된 중첩 답글, 노트 자동 번역, NWC 다중 relay 지원이 포함된 [2.0.3](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.3)을 출시했습니다.

## 프로젝트 업데이트

### Zap Cooking adds zap polls and Branta payment verification

레시피 및 콘텐츠 플랫폼 [Zap Cooking](https://github.com/zapcooking/frontend)이 이번 주 상호작용 콘텐츠와 결제 흐름에 집중한 11개의 PR을 병합했습니다. [PR #277](https://github.com/zapcooking/frontend/pull/277)은 zap poll(kind 6969)을 추가하여, 사용자가 sats를 보내 투표하고 프로필 사진이 포함된 투표자 목록을 볼 수 있게 합니다. [PR #274](https://github.com/zapcooking/frontend/pull/274)는 투표 UX를 재설계해 투표 인터페이스가 피드 안에서 더 자연스럽게 놓이도록 만듭니다.

[PR #276](https://github.com/zapcooking/frontend/pull/276)은 Send Payment 흐름에 카메라 기반 QR 스캔을 추가하고, 전송 전에 결제 목적지가 합법적인지 확인하는 검증 서비스 [Branta](https://branta.pro/)를 통합합니다. Branta는 전송 전에 결제 목적지를 피싱, 주소 바꿔치기, 중간자 가로채기에 대해 검사합니다. Zap Cooking의 구현에서는 Branta 검증이 된 플랫폼 이름과 로고가 결제 흐름에 직접 나타나며, Branta 지원 QR 코드는 `branta_id`, `branta_secret` 파라미터를 담아 지갑이 스캔된 코드 자체로 목적지를 검증할 수 있게 합니다.

### diVine lays groundwork for unified search and hardens video delivery

짧은 형식의 동영상 클라이언트 [diVine](https://github.com/divinevideo/divine-mobile)는 이번 주 검색, 피드 내비게이션, 재생 복구, 업로드 동작을 강화했습니다. [PR #2540](https://github.com/divinevideo/divine-mobile/pull/2540)은 Videos, People, Tags용 그룹화된 섹션이 있는 통합 검색 화면의 기반을 마련합니다. [PR #2623](https://github.com/divinevideo/divine-mobile/pull/2623)은 profile feed, inbox, notifications, discover list, classic vines, search, composable grid feed 전반의 pagination을 공유 pagination controller 위로 옮겨 강화합니다.

비디오 전달도 여러 구체적 수정을 받았습니다. [PR #2643](https://github.com/divinevideo/divine-mobile/pull/2643)은 Divine 호스팅 파생 소스를 순서대로 재시도하고, 재생 오류를 노출하기 전에 원본 blob으로 대체하여, 한 소스의 일시적 실패가 즉시 재생을 죽이지 않게 합니다. [PR #2634](https://github.com/divinevideo/divine-mobile/pull/2634)는 capability probing이 일시적으로 실패해도 resumable upload를 Divine 소유 경로에 유지해, 짧은 네트워크 장애로 인한 업로드 실패를 줄입니다. [PR #2637](https://github.com/divinevideo/divine-mobile/pull/2637)은 또한 sensitive-content gate를 바꾸어, creator가 제공한 content warning label이 아니라 실제 경고 레이블이 있을 때만 비디오를 강하게 차단합니다.

### Shopstr adds custom storefronts and Milk Market keeps shipping marketplace work

Nostr 기반 마켓플레이스 [Shopstr](https://github.com/shopstr-eng/shopstr)가 [PR #245](https://github.com/shopstr-eng/shopstr/pull/245)를 병합해 custom storefronts를 추가했습니다. 이를 통해 판매자는 모든 목록이 같은 일반 프레젠테이션에 들어가도록 강제되는 대신, 더 뚜렷한 홈 화면을 가질 수 있습니다.

우유 전용 마켓플레이스 [Milk Market](https://github.com/shopstr-eng/milk-market)은 storefront 최적화([PR #18](https://github.com/shopstr-eng/milk-market/pull/18)), 계정 복구([PR #17](https://github.com/shopstr-eng/milk-market/pull/17)), beef split([PR #15](https://github.com/shopstr-eng/milk-market/pull/15)), MCP 도구 타이핑 수정([PR #16](https://github.com/shopstr-eng/milk-market/pull/16))을 계속 배포했습니다.

### Notedeck adds sound effects and extends its updater path toward Android

Damus 팀의 데스크톱 클라이언트 [Notedeck](https://github.com/damus-io/notedeck)가 rodio를 사용하는 UI 상호작용 사운드가 포함된 sound effects 서브시스템을 추가하는 [PR #1412](https://github.com/damus-io/notedeck/pull/1412), 그리고 CLI title flag와 접을 수 있는 session folder가 포함된 Agentium 업데이트 [PR #1399](https://github.com/damus-io/notedeck/pull/1399)를 병합했습니다. 오픈 상태인 [PR #1417](https://github.com/damus-io/notedeck/pull/1417)은 Android에서 Nostr/Zapstore를 통한 APK 자체 업데이트를 제안하며, 이는 [뉴스레터 #14에서 다룬 Notedeck의 Nostr 네이티브 업데이터 작업](/ko/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr)을 기반으로 합니다.

### Nostria adds repost relay hints and NIP-98 alignment

[Nostria](https://github.com/nostria-app/nostria)가 kind 6 및 kind 16 이벤트의 repost `e` 태그에 [NIP-18](/ko/topics/nip-18/) (Reposts) relay 힌트를 추가하는 [PR #583](https://github.com/nostria-app/nostria/pull/583), Brainstorm HTTP 인증(kind 27235)을 [NIP-98](/ko/topics/nip-98/) (HTTP Auth) 필수 태그와 맞추는 [PR #582](https://github.com/nostria-app/nostria/pull/582), Schemata 스키마 검증 테스트를 추가하는 [PR #576](https://github.com/nostria-app/nostria/pull/576)을 병합했습니다. NIP-98 변경은 Nostria가 다른 클라이언트와 동일한 HTTP 인증 형식을 사용해 외부 서비스에 인증할 수 있음을 의미합니다.

### Nostr-Doc adds desktop packaging and offline-first work

Form*의 협업 편집기 [Nostr-Doc](https://github.com/formstr-hq/nostr-docs)는 이번 주 패키징과 에디터 작업으로 분주했습니다. [커밋 fcdc00a](https://github.com/formstr-hq/nostr-docs/commit/fcdc00a564c8d76f094c586b06efce07592a60e4)는 데스크톱 앱을 추가하고, [커밋 3977a8e](https://github.com/formstr-hq/nostr-docs/commit/3977a8eb2e62b84a67de756c2776e14de8470927)는 네이티브 앱 작업을 시작하며, [커밋 413a030](https://github.com/formstr-hq/nostr-docs/commit/413a030f5b47fb8e32a5dff81bcef557ad9b5869)은 앱을 offline-first 동작 쪽으로 밀어붙입니다. 에디터 측면에서는 [커밋 1855ce8](https://github.com/formstr-hq/nostr-docs/commit/1855ce86ee83ad504e14e47d9c339baffb114786)이 Ctrl+S 저장, 저장 경고, 링크 미리보기 수정, 취소선 렌더링 수정 기능을 추가합니다.

### rust-nostr optimizes NIP-21 parsing and adds relay-side NIP-62 support

[rust-nostr](https://github.com/rust-nostr/nostr)가 여덟 개 PR을 병합했습니다. 가장 눈에 띄는 것은 [PR #1308](https://github.com/rust-nostr/nostr/pull/1308)로, `PublicKey::parse`에서 [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) URI 파싱을 표준 bech32 파싱 성능과 맞춰 최적화합니다. 이전에는 NIP-21 URI가 원시 bech32 키보다 대략 두 배 느리게 파싱되었습니다. 프로젝트에는 또한 메모리, LMDB, SQLite, 데이터베이스 테스트 백엔드 전반에 relay별 [NIP-62](/ko/topics/nip-62/) (Request to Vanish) 지원을 추가하는 네 개의 오픈 PR([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318))도 열려 있습니다.

### nostr-tools adds bunker relay control and fixes NIP-47 multi-relay parsing

[nostr-tools](https://github.com/nbd-wtf/nostr-tools)가 수동 relay 관리를 위한 `skipSwitchRelays`를 BunkerSignerParams에 추가하는 [PR #530](https://github.com/nbd-wtf/nostr-tools/pull/530), 그리고 사양이 허용하는 다중 relay를 지원하도록 [NIP-47](/ko/topics/nip-47/) (Nostr Wallet Connect) 연결 문자열 파싱을 수정하는 [PR #529](https://github.com/nbd-wtf/nostr-tools/pull/529)를 병합했습니다.

### Nostrability integrates Sherlock audit data and publishes Schemata overview

Nostr 클라이언트 상호운용성 추적기 [Nostrability](https://github.com/nostrability/nostrability)가 14개의 PR을 병합했습니다. [PR #306](https://github.com/nostrability/nostrability/pull/306)은 Sherlock 스캔 통계를 대시보드에 통합합니다. Sherlock은 Nostrability의 자동 감사 도구로, Nostr 클라이언트에 연결하고, 이들이 게시하는 이벤트를 수집하며, 각 이벤트를 Schemata JSON Schema 정의에 대조해 사양 위반을 탐지합니다. 이제 대시보드는 클라이언트별 schema fail rate([PR #315](https://github.com/nostrability/nostrability/pull/315))를 보여주어, 개발자가 자신의 클라이언트가 어떤 이벤트 kind를 잘못 생성하는지 볼 수 있습니다. [PR #323](https://github.com/nostrability/nostrability/pull/323)은 릴리스 공지가 이전 CI 단계에 의해 취소되지 않는 별도 작업으로 실행되도록 Nostr publish 워크플로를 전면 개편합니다.

elsat는 또한 3월 30일 [Schemata for nostr devs](https://njump.me/naddr1qvzqqqr4gupzq96n3hp2vfmf6z2y8uvvxl97xk86kkalnqghx4p25lzl79c76a7yqy2hwumn8ghj7un9d3shjtnyv9kh2uewd9hj7qgwwaehxw309ahx7uewd3hkctcqz4fnx4rkw3x57nrcwdn8zt22xd982jehfptsgqtrww)를 게시해, schemata, schemata-codegen, Sherlock이 어떻게 맞물리는지 설명하고 현재 커버리지 수치 65개 NIP에 걸친 179개 이벤트 kind 스키마, 154개 태그 스키마, 13개 프로토콜 메시지, 310개 샘플 이벤트를 제시했습니다.

### Nalgorithm adds digest generation and local score caching

새로운 관련도 기반 Nostr 피드 프로젝트 [Nalgorithm](https://github.com/jooray/nalgorithm)이 이번 주 공개 개발을 시작했습니다. [커밋 cf6c501](https://github.com/jooray/nalgorithm/commit/cf6c501e754ef95a1b4fecc1a76288471a101f43)은 팔로우한 계정의 게시물을 가져와 사용자 정의 선호 프롬프트로 점수를 매기는 초기 웹 앱을 마련합니다. [커밋 8e931b6](https://github.com/jooray/nalgorithm/commit/8e931b6ae85d470e73603752134ff49b7ba4bb86)은 상위 랭크 게시물을 spoken-word 요약으로 바꾸는 CLI digest 도구를 추가하고, [커밋 4cb9c63](https://github.com/jooray/nalgorithm/commit/4cb9c635489a9a3429e8d71f3861dc2a11624153)은 파일 기반 score caching과 최근 좋아요를 바탕으로 한 점진적 learned-prompt evolution을 추가합니다. [커밋 c2edfb8](https://github.com/jooray/nalgorithm/commit/c2edfb8b89fadbe0028c3f5729bda7e23b2e3c03)은 또한 실패한 배치의 fallback score를 캐시하지 않도록 바꿔, 일시적 점수 실패가 게시물 순위를 영구히 평탄화하지 않게 합니다.

### TENEX adds RAG vector store and targeted MCP startup

Telegram을 통해 AI 에이전트를 Nostr 채널에 연결하는 Nostr 네이티브 에이전트 프레임워크 [TENEX](https://github.com/tenex-chat/tenex)가 이번 주 7개의 PR을 병합했습니다. [PR #101](https://github.com/tenex-chat/tenex/pull/101)은 SQLite-vec, LanceDB, Qdrant 백엔드를 갖춘 플러그형 벡터 저장소 추상화를 추가해, 에이전트에 하나의 벡터 데이터베이스에 묶이지 않는 retrieval-augmented generation을 제공합니다. [PR #102](https://github.com/tenex-chat/tenex/pull/102)는 MCP 시작을 표적화합니다. 첫 실행 시 모든 서버를 미리 띄우는 대신, 에이전트가 실제로 사용하는 도구를 가진 MCP 서버만 시작합니다. [PR #100](https://github.com/tenex-chat/tenex/pull/100)은 Telegram 채널 바인딩이 있는 에이전트가 수신 메시지에만 응답하지 않고 능동적으로 메시지를 밀어 넣을 수 있도록 `send_message` 도구를 추가합니다. [PR #106](https://github.com/tenex-chat/tenex/pull/106)은 `.git/HEAD`를 직접 읽어 `git branch`를 실행하지 않음으로써 9GB Bun/JSC 메모리 사전 할당을 유발하던 서브프로세스 spawn을 피합니다.

### Dart NDK moves Amber signer and adds Alby Go 1-click

Flutter용 Nostr 개발 키트 [Dart NDK](https://github.com/relaystr/ndk)가 11개의 PR을 병합했습니다. [PR #525](https://github.com/relaystr/ndk/pull/525)는 Amber signer 지원을 ndk_flutter 패키지로 이동하고, [PR #552](https://github.com/relaystr/ndk/pull/552)는 샘플 앱에 Alby Go 원클릭 지갑 연결을 추가합니다. [PR #502](https://github.com/relaystr/ndk/pull/502)는 CLI용 install.sh 스크립트를 추가하고, [PR #523](https://github.com/relaystr/ndk/pull/523)은 Rust verifier 의존성을 네이티브 asset 처리로 대체하며 제거합니다.

## Protocol and Spec Work

### Marmot moves KeyPackages to addressable events and tightens push notifications

[Marmot 사양](https://github.com/marmot-protocol/marmot)은 키 재료와 그룹 멤버십 처리 방식을 바꾸는 네 개의 PR을 병합했습니다. [PR #54](https://github.com/marmot-protocol/marmot/pull/54)는 KeyPackage 이벤트를 일반 `kind:443`에서 `d` 태그를 가진 주소 지정 가능 `kind:30443`으로 마이그레이션하여, 키 회전 중 [NIP-09](/ko/topics/nip-09/) 이벤트 삭제가 필요하지 않게 합니다. 주소 지정 가능 이벤트는 제자리에서 덮어쓰므로 회전이 자기완결적이 됩니다. [PR #57](https://github.com/marmot-protocol/marmot/pull/57)은 비관리자 사용자도 SelfRemove 제안(자발적 그룹 탈퇴)을 커밋할 수 있게 하고, [PR #62](https://github.com/marmot-protocol/marmot/pull/62)는 관리자가 SelfRemove를 사용하기 전에 관리자 지위를 내려놓도록 요구해, 관리자 권한을 가진 채 사라지는 것을 막습니다.

[PR #61](https://github.com/marmot-protocol/marmot/pull/61)은 [MIP-05](/ko/topics/mip-05/) 푸시 알림 형식을 더 엄격하게 하여, 단일 blob base64 인코딩, 버전 관리, 토큰 wire 형식, x-only key 사용을 명시적으로 만듭니다. 결과적으로 사양, 클라이언트 라이브러리, 앱 백엔드 전반에서 token blob과 x-only key에 대해 하나의 정의된 wire 표현이 생깁니다. 이러한 사양 변경의 구현은 이번 주 White Noise 스택에 반영되었고, 위의 [White Noise v2026.3.23 섹션](#white-noise-fixes-relay-churn-and-expands-client-controls)에서 다뤘습니다.

### NIP Updates

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md): Static Websites** ([PR #1538](https://github.com/nostr-protocol/nips/pull/1538)): Blossom 스토리지를 사용해 Nostr 키페어 아래 정적 웹사이트를 호스팅하기 위한 kind `15128`(루트 사이트) 및 kind `35128`(이름 있는 사이트) 매니페스트 이벤트를 정의합니다. 자세한 내용은 [아래 심층 분석](#nip-deep-dive-nip-5a-static-websites)을 참조하십시오.

- **[NIP-30](/ko/topics/nip-30/) (Custom Emoji): shortcode에 하이픈 허용** ([PR #2297](https://github.com/nostr-protocol/nips/pull/2297)): shortcode 설명을 하이픈을 포함하도록 업데이트합니다. 하이픈이 들어간 shortcode는 NIP 도입 이후 실제로 사용되어 왔기 때문에, 이제 사양이 현재 사용법을 문서화합니다.

**오픈 PR 및 논의:**

- **NIP-C1: Agent TUI Messages** ([PR #2295](https://github.com/nostr-protocol/nips/pull/2295)): 에이전트가 암호화된 DM을 통해 상호작용 UI 요소를 전송하기 위한 구조화된 메시지 형식을 제안합니다. typed `text`, `buttons`, `card`, `table` payload가 포함됩니다. 초안은 모든 것을 기존 [NIP-17](/ko/topics/nip-17/) 및 [NIP-04](/ko/topics/nip-04/) 다이렉트 메시지 콘텐츠 안의 JSON으로 유지합니다. 새 이벤트 kind는 정의하지 않으며, 버튼 응답에는 단순한 callback string 형식을 사용합니다.

- **NIP-95: Hybrid Peer-to-Peer Relay Protocol** ([PR #2293](https://github.com/nostr-protocol/nips/pull/2293)): relay가 권위적 위치를 유지하면서도 WebRTC를 통해 최근 이벤트의 P2P 배포를 조정할 수 있는 하이브리드 relay 모델을 제안합니다. 초안은 `PEER_REGISTER`, `PEER_REQUEST`, `PEER_OFFER` 같은 relay 메시지를 도입하며, 안정적인 클라이언트가 Super Peer로 작동하고 relay가 시드 노드와 대체 경로 역할을 합니다.

- **NIP-B9: Zap Poll Events** ([PR #2284](https://github.com/nostr-protocol/nips/pull/2284)): [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) (Polls)이 무료 투표를 다루고 있는 현재, 오래된 NIP-69 zap poll 아이디어를 다시 꺼냅니다. 초안은 kind `6969` poll 정의와 kind `9734` zap을 투표로 사용하여, 경제적 Sybil 저항을 가진 유료 투표 시스템을 만듭니다. 이는 무료 one-key-one-vote 투표를 보완합니다.

- **NIP-AD: Super Zap** ([PR #2289](https://github.com/nostr-protocol/nips/pull/2289)): relay의 pubkey나 클라이언트의 pubkey로 전송된 zap이 특수 프로모션 노트처럼 표시되는 규약을 제안하며, 사실상 zap 영수증을 광고 표면으로 바꿉니다. relay 운영자와 클라이언트는 `lud16`이 포함된 프로필을 게시하고, 해당 영수증을 가져오며, zap 설명 안의 콘텐츠를 추출하고, 선택적으로 최소 sats 임계값을 설정해 스팸을 억제할 수 있습니다.

- **NIP-XX: Agent Reputation Attestations** ([PR #2285](https://github.com/nostr-protocol/nips/pull/2285)): Nostr 에이전트에 대한 구조화된 평판 attestations용 매개변수화된 대체 가능 이벤트로 kind `30085`를 제안합니다. 초안은 평판을 관찰자 의존적으로 만들어 단일 글로벌 점수를 피하고, 오래된 attestation이 희미해지도록 시간 감쇠를 추가하며, 증거 요구가 있는 부정 평가를 지원하고, 더 나은 Sybil 저항을 위해 단순 가중 점수와 그래프 다양성 점수를 모두 개괄합니다.

- **NIP-XX: Paid API Service Announcements** ([PR #2291](https://github.com/nostr-protocol/nips/pull/2291)): 유료 HTTP API 광고를 위한 kind `31402` 주소 지정 가능 이벤트를 제안하며, Nostr는 발견을, HTTP 402는 결제를 처리합니다. 초안은 JSON 콘텐츠 파싱 없이 relay가 결제 방식, 가격, 기능으로 필터링할 수 있도록 태그 우선 설계를 취하고, 클라이언트나 에이전트가 호출을 자동 생성할 수 있게 선택적 요청/응답 스키마도 허용합니다.

- **NIP-XX: SplitSig를 통한 LNURL-auth 기반 키 파생** ([PR #2294](https://github.com/nostr-protocol/nips/pull/2294)): LNURL-auth ECDSA 서명과 클라이언트 측 무작위 nonce를 결합해 Nostr 키페어를 파생하는 방식을 제안합니다. 파생 공식은 `nsec = SHA256(ecdsa_signature || nonce)`입니다. 서버는 LNURL-auth 핸드셰이크에 내재된 ECDSA 서명을 보지만 nonce는 보지 못하고, 브라우저는 nonce를 생성하지만 서명을 제어하지 못합니다. 어느 한 조각만으로는 nsec를 파생할 수 없습니다. 의도된 결과는 동일한 Lightning 지갑이 여러 장치에서 동일한 Nostr 키를 만들어내고, 지갑이 복구 앵커가 되며, 어떤 서버도 개인 키를 재구성할 수 없게 하는 것입니다.

- **[NIP-55](/ko/topics/nip-55/): rejected 필드 문서화** ([PR #2290](https://github.com/nostr-protocol/nips/pull/2290)): intent 기반 signer 응답의 `rejected` 필드를 문서화하여, [Amethyst의 v1.07.x 수정](#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish)이 우회해야 했던 동작을 공식화합니다.

## NIP Deep Dive: NIP-5A (Static Websites)

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)는 두 개의 이벤트 kind와 기존 blob storage 인프라를 사용해 Nostr 키페어 아래 정적 웹사이트를 호스팅하는 방법을 정의합니다. 이를 통해 서명된 이벤트가 제공 가능한 웹 페이지로 바뀝니다. [사양](https://github.com/nostr-protocol/nips/blob/master/5A.md)은 [PR #1538](https://github.com/nostr-protocol/nips/pull/1538)을 통해 3월 25일 병합되었습니다.

모델은 루트 사이트에 kind `15128`을 사용하며, pubkey당 하나입니다. 이름 있는 사이트는 `d` 태그로 식별되는 kind `35128`을 사용합니다. 각 매니페스트는 절대 URL 경로를 SHA256 해시에 매핑합니다. 다음은 루트 사이트 매니페스트 예시입니다.

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["path", "/favicon.ico", "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["description", "A static website hosted on Nostr"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

제공 흐름은 세 단계로 동작합니다. 호스트 서버가 HTTP 요청을 수신하고, 서브도메인에서 저자의 pubkey를 추출하며(루트 사이트는 npub, 이름 있는 사이트는 원시 pubkey의 base36 인코딩), [NIP-65](/ko/topics/nip-65/)를 통해 저자의 relay 목록을 가져오고, 사이트 매니페스트를 쿼리합니다. 매니페스트가 발견되면 서버는 요청된 경로를 콘텐츠 해시로 해석하고, `server` 태그에 나열된 Blossom 서버들에서 일치하는 blob을 다운로드해 반환합니다.

DNS 서브도메인 형식은 엄격하게 지정됩니다. 루트 사이트는 표준 npub을 서브도메인으로 사용합니다. 이름 있는 사이트는 원시 pubkey의 50자 base36 인코딩 뒤에 `d` 태그 값을 이어 붙여 하나의 DNS 레이블을 만듭니다. DNS 레이블은 63자로 제한되고 base36 인코딩이 항상 50자를 차지하므로, `d` 태그는 13자로 제한됩니다. 또한 사양은 `d` 태그가 `^[a-z0-9-]{1,13}$`와 일치하고 하이픈으로 끝나지 않도록 요구해, DNS 해석 모호성을 방지합니다.

콘텐츠 해시를 사용하면 동일한 사이트를 서로 다른 호스트 서버가 제공할 수 있으며, 서버를 신뢰하지 않아도 파일 무결성을 검증할 수 있습니다. 호스트 서버는 파일을 직접 저장할 필요가 없습니다. 매니페스트의 해시를 사용해 Blossom에서 필요할 때마다 가져오면 됩니다. 즉, 저자는 무엇이 제공되는지를 통제하고, Blossom 서버는 원시 파일을 저장하며, 호스트 서버는 그 둘을 연결하는 역할만 합니다. 이 세 구성 요소는 서로 독립적으로 교체될 수 있습니다.

기존 구현으로는 매니페스트를 해석하고 파일을 제공하는 호스트 서버 [nsite](https://github.com/lez/nsite), 그리고 매니페스트를 만들고 게시하는 UI [nsite-manager](https://github.com/hzrd149/nsite-manager)가 있습니다. 이 사양은 사이트 소스 코드 저장소를 링크하기 위한 `source` 태그도 추가했으며, [PR #2286](https://github.com/nostr-protocol/nips/pull/2286)에서 별도로 병합된 README 업데이트는 kind `15128`과 `35128`을 NIP kind 색인에 등록했습니다.

## NIP Deep Dive: NIP-62 (Request to Vanish)

[NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md)는 요청하는 pubkey의 모든 이벤트를 삭제해 달라는 요청으로 kind `62`를 정의합니다. [사양](https://github.com/nostr-protocol/nips/blob/master/62.md)은 법적 동기가 있습니다. 잊힐 권리 법이 있는 관할권에서, 표준화되고 서명된 삭제 요청은 relay 운영자에게 행동해야 할 명확한 신호를 제공합니다.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

이 사양은 대상 지정 vanish 요청과 전역 vanish 요청을 구분합니다. 대상 지정 요청은 어떤 relay가 동작해야 하는지 식별하는 특정 `relay` 태그를 포함합니다. 전역 요청은 relay 태그 값으로 리터럴 문자열 `ALL_RELAYS`를 사용하여, 이 이벤트를 보는 모든 relay가 해당 pubkey의 모든 이벤트를 삭제하도록 요청합니다. 이를 준수하는 relay는 삭제된 이벤트가 다시 relay 안으로 재브로드캐스트되지 않도록 보장해야 하므로, 삭제는 지속성을 가집니다.

NIP-62는 범위와 의도 모두에서 [NIP-09](/ko/topics/nip-09/) (Event Deletion)을 넘어섭니다. NIP-09는 개별 이벤트를 삭제할 수 있게 하고 relay는 따를 수도 있습니다. NIP-62는 모든 것의 삭제를 요청하며, 사양은 URL이 태그된 경우 relay가 반드시 따라야 한다고 말합니다. 또한 relay가 요청하는 pubkey를 p-tag한 [NIP-59](/ko/topics/nip-59/) (Gift Wrap) 이벤트도 삭제하도록 요청하므로, 들어오는 DM도 사용자의 자체 이벤트와 함께 정리됩니다. NIP-62 vanish 요청을 대상으로 NIP-09 삭제를 게시해도 아무 효과가 없습니다. 한 번 vanish하면, vanish 요청을 삭제해도 vanish를 되돌릴 수 없습니다.

이번 주 [Amethyst v1.07.0](#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish)은 클라이언트 측 NIP-62 지원을 출시해 사용자가 앱에서 vanish 요청을 시작할 수 있게 했습니다. relay 측에서는 [rust-nostr](https://github.com/rust-nostr/nostr)가 메모리, LMDB, SQLite, 데이터베이스 테스트 백엔드 전반에 NIP-62 지원을 추가하는 네 개의 오픈 PR([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318))을 보유하고 있습니다. 이로써 클라이언트 지원과 relay 지원 작업이 같은 주에 맞물렸습니다.

프로토콜 설계는 하나의 실용적 긴장을 드러냅니다. Nostr의 가치 제안에는 censorship resistance가 포함되며, 이는 relay가 게시를 막아서는 안 된다는 뜻입니다. 그런데 NIP-62는 relay가 특정 pubkey의 재게시를 반드시 막아야 하는 경우를 도입합니다. 이 두 속성은 요청이 자기 지시적이라는 점에서 공존합니다. 당신이 요청하는 것은 타인의 이벤트 삭제가 아니라 자신의 이벤트 삭제입니다. censorship resistance 속성은, 명시적으로 빠지겠다고 선택한 당사자 자신을 제외하고는 그대로 유지됩니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 공유할 뉴스가 있다면 <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ko/topics/nip-17/) (Private Direct Messages) DM으로 연락하시거나</a> Nostr에서 찾아주세요.
