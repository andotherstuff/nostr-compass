---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
translationOf: /en/newsletters/2026-11-04-newsletter.md
translationDate: 2026-11-05
---

이번 주 [Amethyst](/ko/newsletters/2026-11-04-newsletter/#amethyst)는 [임베드 보안 검토](https://github.com/vitorpamplona/amethyst/pull/4710)에서 나온 수정 사항을 반영해 인라인 napplet을 출시했고, [Napplets](/ko/newsletters/2026-11-04-newsletter/#napplets---web-packages)는 애플릿 신원을 문서별 포트에 묶었으며, [Marmot의 mdk](/ko/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk) 나이틀리 빌드는 그룹 메시징을 강화했습니다. 그 밖에 릴레이, 지갑, 서명 라이브러리, 새 앱에도 변화가 있었으며, 그중 상당수는 병합된 소스에만 반영되었고 아직 출시되지 않았습니다.

## 주요 소식 {#top-stories}

### Amethyst {#amethyst}

Android 클라이언트 Amethyst가 [v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0)을 출시했습니다. 이 버전은 Android 11 이상과 데스크톱에서 노트 안에 napplet을 인라인으로 실행합니다. [임베드 보안 검토](https://github.com/vitorpamplona/amethyst/pull/4710)에서 나온 수정 사항은 릴레이 접근 권한이 있는 napplet이라면 어떤 것이든 복호화된 DM을 읽을 수 있던 경로를 막습니다. 이제 복호화에는 별도의 사용자 허가가 필요하고 `nostr.signEvent`에는 서명자 권한이 필요하지만, 데스크톱 Chromium 렌더러는 여전히 샌드박스 없이 실행됩니다. [파일별 첨부 파일 암호화 변경](https://github.com/vitorpamplona/amethyst/pull/4701)으로 [NIP-17](/ko/topics/nip-17/) 비공개 다이렉트 메시지의 각 첨부 파일은 새로운 AES-GCM 키와 논스를 받습니다. 이전에는 여러 파일을 한꺼번에 보낼 때 키와 논스를 모두 재사용했습니다. 업스트림의 위험 설명은 재현된 익스플로잇 없이 코드 분석에 근거한 것이며, 이미 전송된 파일은 수정되지 않습니다.

### Marmot Protocol (mdk) {#marmot-protocol-mdk}

Nostr용 MLS 기반 암호화 메시징 키트인 Marmot의 mdk는 테스트 전용 나이틀리 프리릴리스를 게시했으며, 이 계열에는 안정 릴리스가 없습니다. 11월 2일 나이틀리에서는 그룹 내에서 [새 전송이 대기열에 있는 이전 전송 뒤에서 기다리도록](https://github.com/marmot-protocol/mdk/pull/2849) 하여 기록을 따라잡는 멤버를 위해 암호화 세대의 순서를 유지하지만, 메시지 유실을 막는다고 보장하지는 않습니다. 병합되었지만 기본값이 꺼져 있는 [유실된 Welcome 복구](https://github.com/marmot-protocol/mdk/pull/2936)는 [Marmot 하트비트 규칙](https://github.com/marmot-protocol/marmot/pull/497)을 따르며, 대상의 하트비트가 가장 최근 캐리어 게시 시점으로부터 최소 10분 이후의 활동을 보여 주면 보관해 둔 정확히 동일한 Welcome을 다시 보냅니다. 하트비트 주기나 시계 지연으로 인해 복구가 한 시간 이상 늦어질 수 있으며, 완료 시점에는 상한이 없습니다. [기기 연결 명령](https://github.com/marmot-protocol/mdk/pull/2922)은 기본값이 꺼진 dev-device-groups 기능 뒤에 남아 있으며 프로덕션에서는 비활성화되어 있습니다.

### Napplets - 웹 패키지 {#napplets---web-packages}

샌드박스된 Nostr 애플릿을 위한 웹 패키지 Napplets가 [core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0), [nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0), [shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0)을 출시했으며, 이들 버전은 [애플릿 신원을 문서별 MessagePort에 바인딩합니다](https://github.com/napplet/web/pull/302). 검증된 (dTag, artifactHash) 신원은 생성된 iframe이 보낸 hello에 전달된 포트에 묶이며, 모든 NAP 트래픽은 그 포트를 사용합니다. 탐색으로 로드된 문서는 어떤 권한도 받지 못합니다. 아직 Window 메시징을 사용하는 셸은 호환 경로가 없으므로 반드시 업그레이드해야 합니다. 이후 소스는 frame-src 'none'으로 [미리보기 프레임을 검증된 문서에 고정합니다](https://github.com/napplet/web/pull/305).

## 태그된 릴리스 {#tagged-releases}

### Marble {#marble}

Cosign 임계값 서명을 기반으로 한 베타 클라이언트 Marble은 [0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23)에서 릴레이를 피드로 읽을 수 있게 되었습니다. 주소로 연 릴레이는 자체 설명을 먼저 보여 준 뒤 게시물을 최신순으로 보여 줍니다. 즐겨찾는 릴레이는 kind 10012 목록에, 릴레이 그룹은 kind 30002 세트에 저장되며, 이는 Jumble이 사용하는 것과 같은 목록입니다. 이번 릴리스는 최근 반응 트레이와 사용자 자신의 커스텀 이모지를 갖추도록 반응 기능도 개편했습니다.

### Sidecar {#sidecar}

노트와 웹 하이라이트를 게시하는 브라우저 확장 프로그램 Sidecar는 [1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6)에서 릴레이에 저장된 지갑 백업을 삭제할 수 있게 되었습니다. 확인 절차를 거친 뒤 암호화된 사본을 빈 사본으로 교체하고 릴레이에 이를 잊어 달라고 요청하며, 연결된 지갑은 그대로 둡니다. 릴레이가 백업을 지운다는 보장은 없습니다. [v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5)부터 Sidecar는 업로드 전에 JPEG에서 EXIF, XMP, IPTC 메타데이터를 제거하며, [업로드 준비 변경](https://github.com/dmnyc/sidecar/pull/572)은 정리할 수 없는 JPEG를 모두 차단합니다.

### Haps {#haps}

Haps는 Nostr 키로 네이티브 패키지를 게시하고 설치합니다. [Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25)는 체크섬이 고정된 htree 헬퍼와 모든 아카이브를 포괄하는 SHA256SUMS 파일을 포함한 macOS, Linux, Windows 번들을 제공합니다. 0.1.24 소스는 초안 Hashtree 사양에 따라 [버전이 지정된 Hashtree 참조를 기록합니다](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8). Haps 0.1.23 이하 버전은 레거시 전환 카탈로그나 업그레이드된 설치 프로그램 또는 Cargo 빌드 없이는 새 카탈로그를 읽을 수 없습니다.

### Cosign {#cosign}

Marble 베타의 기반이 되는 임계값 서명 라이브러리 Cosign은 [0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9)에서 참여 과정에 대한 부분적인 수정을 제공합니다. 스캔한 초대자를 통한 참여에는 이제 해당 초대자의 기여분과 서로 다른 최소 두 발신자로부터 받은 조각이 필요합니다. 휴대폰 간 참여는 여전히 바인딩되지 않아 키 두 개를 가진 공격자만으로도 충분하며, 빈 복호화 부분은 여전히 증명 검증을 건너뜁니다. [0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8)에서는 멤버 목록을 작성하는 서버가 여전히 비밀값이 알려진 공유 지점을 선택할 수 있습니다. 휴대폰은 Marble 릴리스를 통해서만 수정 사항을 받습니다.

### nostream {#nostream}

PostgreSQL 기반 TypeScript 릴레이 nostream은 [3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0)에서 [아웃바운드 피어 동기화](https://github.com/cameri/nostream/pull/1043)를 추가했습니다. 워커는 각 피어의 [NIP-11](/ko/topics/nip-11/) 릴레이 정보 범위를 읽고, [NIP-42](/ko/topics/nip-42/) 클라이언트 인증으로 인증한 뒤 [NIP-77](/ko/topics/nip-77/) negentropy 동기화로 조정하며, 가져온 이벤트를 ID, 서명, 범위 기준으로 검사합니다. [피어별 제한](https://github.com/cameri/nostream/pull/1034)은 설정된 피어가 AUTH를 완료한 후에만 적용됩니다. 소스 릴리스만으로는 어떤 릴레이가 이를 배포했다고 증명되지 않습니다.

### diVine {#divine}

짧은 반복 재생 동영상 클라이언트 diVine은 상호작용형 공개 동영상 스티커를 갖춘 [안정판 Android 1.0.27](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27)을 게시했으며, iOS와 macOS 제공 여부는 확인되지 않았습니다. 병합된 [윈도 아래 재조회](https://github.com/divinevideo/divine-mobile/pull/10711)는 초기 기록 복원이 끝난 뒤에만 실행되며, 기프트 랩, [NIP-04](/ko/topics/nip-04/) 지원 중단된 암호화 DM, 삭제 이벤트를 릴레이당 메시지 100개 단위의 페이지로 읽습니다. 이 기능은 각 릴레이를 독립적으로 순회하는 반면, 기존 기록 드레인은 하나의 커서를 공유하므로 상한에 걸린 릴레이의 오래된 기록을 건너뛸 수 있습니다. 적용 범위는 제한적이며 전체 기록을 복구하지는 않습니다.

### Whistle {#whistle}

모바일 그룹 위치 공유 및 채팅 앱 Whistle은 Marmot 프로토콜 v2 기반의 첫 공개 릴리스인 [2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1)을 출시했습니다. 기존 그룹은 이전할 수 없으므로 그룹을 다시 만들어야 하고 모든 멤버가 업데이트해야 하지만, npub 신원은 유지됩니다. 스캔하여 참여하는 방식이 초대 코드와 링크를 대체합니다. 알려진 문제로, 오프라인 상태에서 보낸 채팅 메시지가 늦게 도착하거나 아예 도착하지 않을 수 있으며, 릴리스 노트는 그 원인을 MarmotKit으로 지목합니다. 위치 공유는 영향을 받지 않습니다.

## 개발 중 {#in-development}

### Quartz {#quartz}

Kotlin Multiplatform Nostr 라이브러리인 Quartz가 릴리스 2.14.0에서 [재연결 후 실시간 구독 재개](https://github.com/vitorpamplona/quartz/pull/82) 기능을 출시했다. 각 릴레이는 이미 전달된 이벤트 중 가장 최신 created_at부터 구독을 재개하며, 이 값은 기기 시계를 넘지 않도록 제한된다. gift-wrap 필터는 백데이팅을 감안해 이틀을 더 거슬러 올라간다. 장애 중에 릴레이가 저장한, 타임스탬프가 더 오래된 이벤트는 여전히 누락될 수 있다. 병합되었지만 아직 릴리스되지 않은 [개수 인식 negentropy 윈도](https://github.com/vitorpamplona/quartz/pull/85)는 선택 사항인 [NIP-45](/ko/topics/nip-45/) 이벤트 개수를 로컬 개수와 비교하며, 릴레이가 알려 주는 개수는 신뢰할 수 없는 값으로 취급한다.

### Buzz {#buzz}

Buzz는 [kind 5 및 9005 삭제를 대상의 소프트 삭제와 하나의 트랜잭션으로 커밋하는](https://github.com/block/buzz/pull/8944) 변경을 병합했다. 이에 따라 장애가 발생하더라도 삭제는 수락되고 대상은 살아 있는 상황이 더 이상 생기지 않는다. 과거에 이미 불일치 상태로 남은 행은 복구되지 않는다. 기기 간 읽음 상태를 위한 Buzz 초안인 [NIP-RS](/ko/topics/nip-rs/)의 모바일 프로필이 병합되어 [기기 간 읽음 경계를 동기화한다](https://github.com/block/buzz/pull/8998). read_state_snapshot이 없는 구형 릴레이에서는 로컬 읽음 처리는 계속 작동하지만, 기기 간 동기화는 대체 수단 없이 중단된다.

### Alby Hub {#alby-hub}

[NIP-47](/ko/topics/nip-47/) Nostr Wallet Connect 앱을 지원하는 자기 수탁형 Lightning 노드 Alby Hub가 db_migrate 또는 Postgres 마이그레이션 중에 각 테이블의 ID 카운터를 유지하도록 하는 [데이터베이스 마이그레이션 수정](https://github.com/getAlby/hub/pull/2657)을 병합했다. 이전에는 새 앱이 삭제된 앱의 ID를 재사용하여 그 앱의 트랜잭션과 격리된 잔액을 물려받을 수 있었다. 이 수정을 포함한 태그 릴리스나 배포는 확인되지 않았다. 별도의 [알림 변경](https://github.com/getAlby/hub/pull/2677)은 앱별 실패를 서로 격리하지만, 실패한 알림은 여전히 재시도 없이 버려진다.

### swift-nostr-client {#swift-nostr-client}

Swift 6 Nostr 라이브러리인 swift-nostr-client가 [RemoteSigner가 첫 명령 전에 connect 핸드셰이크를 실행하도록 하는](https://github.com/yysskk/swift-nostr/pull/287) 호환성을 깨는 변경을 병합했다. 새 설정 connectsAutomatically의 기본값은 true이며, 핸드셰이크가 실패하면 명령은 전송되지 않는다. [NIP-46](/ko/topics/nip-46/) 원격 서명 시크릿은 일회용이므로, 저장된 클라이언트 키 쌍으로 bunker 세션을 재개하는 앱은 이 값을 false로 설정해야 한다. 그렇지 않으면 첫 명령이 이미 사용된 시크릿을 제시하게 된다. 아직 태그된 릴리스는 없다.

## 새 프로젝트 {#new-projects}

### Trikey {#trikey}

휴대폰 앱과 가디언이 암호화된 Nostr 릴레이 메시지로 통신하는, 프리알파 단계이며 감사를 받지 않은 지갑 Trikey가 [릴리스 0.1.10-alpha](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf)에서 앱을 열 때 멈추는 문제를 해결했다. 이제 양쪽 모두 이미 읽은 wrap ID를 재시작 후에도 유지되는 기록으로 보관하고, 서명 검사나 복호화 전에 해당 ID를 건너뛴다. 요청과 알림에 붙는 만료 힌트는 릴레이에서의 삭제를 보장하지 않으며, 게시자의 성능 측정은 노트북에서 이루어졌다.

### Pacto {#pacto}

기존 Marmot 그룹과 NIP-17 DM을 함께 운영하는 데스크톱 커뮤니티 조직 앱 Pacto가 서명되지 않은 [v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5)를 릴리스했으며, 보낸 메시지를 1분 동안 편집할 수 있는 기능이 추가되었다. [DM 전송 수정](https://github.com/covenant-gov/pacto-app/pull/425)으로 풀에 신뢰할 수 있는 릴레이가 없으면 전송이 즉시 실패하고, 입력 중 표시는 신뢰할 수 있는 릴레이를 통해서만 전달된다. 아직 병합되지 않은 열린 풀 리퀘스트들은 [스쿼드 이벤트](https://github.com/covenant-gov/pacto-app/pull/488)와 [암호화된 스쿼드 문서](https://github.com/covenant-gov/pacto-app/pull/490)를 추가할 예정이다.

### Mialuna {#mialuna}

미디어 중심 Flutter Nostr 클라이언트 Mialuna가 사용자 본인의 스토리가 만료되면 삭제 요청을 보내는 기능을 추가한 [버전 0.19.0 릴리스 공지](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez)를 게시했다. [변경 로그 커밋](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886)에는 릴레이 삭제 요청과 Blossom 미디어 삭제가 기록되어 있으며, 로컬 키 계정에서는 이 작업이 자동으로 실행되고 Amber 또는 bunker 계정에서는 사용자가 Delete now를 선택할 때까지 대기한다. APK와 실제 기기에서의 동작은 독립적으로 확인되지 않았다. 삭제 요청은 릴레이나 서버가 데이터를 지운다는 것을 보장하지 못한다.

### whereAreYou {#whereareyou}

QR 코드나 초대 링크로 참여하는 서클 안에서 위치를 공유하는 Android 앱 whereAreYou는 좌표를 AES-256-GCM으로 암호화해 공개 릴레이로 전송한다. [멤버 서명 커밋](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e)은 서클 키 보유자가 다른 멤버로 가장해 게시하는 것을 막으며, 모든 기기가 업데이트해야 한다. [Base45 신원 백업](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc)에 대해 작성자는 QR 코드를 촬영한 사람이라면 누구나 오프라인에서 8자리 코드를 추측할 수 있다고 경고하며, 그의 추정으로는 GPU 시간 수십 분 안에 가능하다. 벤치마크는 공개되지 않았다. 해당 출처는 어떠한 보안 보증도 제시하지 않는다.

## 프로토콜 및 사양 작업 {#protocol-and-spec-work}

### Buzz, 소유자 승인 에이전트 자격 증명 경로 정의 {#buzz-defines-owner-authorized-agent-credential-routes}

Buzz가 [NIP-FA](/ko/topics/nip-fa/) [소유자 승인 에이전트 자격 증명 초안](https://github.com/block/buzz/pull/9015)을 병합했다. 이 초안은 [NIP-OA](/ko/topics/nip-oa/) 소유자 증명을 통해 승인된 에이전트를 위한 부여, 어서션, 철회 경로를 정의한다. 부여는 소유자의 세션과 에이전트의 [NIP-98](/ko/topics/nip-98/) HTTP 인증 증명을 짝짓는 RFC 8693 토큰 교환에서 발급되며, 철회 시 에이전트 연결이 끊기고 해당 키의 재등록이 차단된다. NIP-FA는 소스에만 병합된 Buzz 사양이며, 프로덕션 활성화나 상호 운용성을 주장하지 않는다.

### 양자 내성 이벤트 서명에 정확한 검증 규칙 추가 {#post-quantum-event-signatures-gain-exact-validation-rules}

오랫동안 열려 있던 양자 내성 서명 제안에 [Nostr 이벤트를 위한 정확한 ML-DSA-44 검증 규칙](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6)이 추가되었다. 키와 서명은 고정 길이를 가지며, 검증자는 빈 컨텍스트로 32바이트 원시 이벤트 ID 다이제스트에 대한 서명을 검사하고, 대체 알고리즘은 허용되지 않는다. 제안된 신원에는 [NIP-19](/ko/topics/nip-19/) bech32 인코딩이 없으며, 새 서명이 [NIP-44](/ko/topics/nip-44/) 암호화 페이로드나 [NIP-59](/ko/topics/nip-59/) gift wrap을 양자 내성으로 안전하게 만들어 주지는 않는다.

### 서명된 전제 조건 제안으로 이벤트 교체 손실 방지 {#a-proposed-signed-precondition-prevents-lost-event-replacements}

열려 있는 Buzz 풀 리퀘스트가 교체 가능 이벤트와 주소 지정 가능 이벤트를 위한 [프로젝트 로컬 NIP-CS 서명 전제 조건을 제안한다](https://github.com/block/buzz/pull/8835). 이는 공식 NIP가 아니다. 서명된 태그는 현재 헤드 ID 또는 `none`을 지정하며, 릴레이는 좌표 잠금 아래에서 이를 원자적으로 검사하여 오래된 쓰기를 false OK 또는 HTTP 409로 거부하고 아무것도 저장하지 않는다. 태그가 없는 쓰기는 이전과 동일하게 작동하며, 이 태그는 릴레이 간 compare-and-swap을 보장하지 않는다.

## NIP 심층 분석: NIP-31과 NIP-73 {#nip-deep-dive-nip-31-and-nip-73}

클라이언트는 기본적으로 이해하지 못하는 콘텐츠를 자주 만난다. [NIP-31: Dealing with Unknown Event Kinds](/ko/topics/nip-31/)는 낯선 이벤트 kind에 읽을 수 있는 레이블을 붙여 주고, [NIP-73: External Content IDs](/ko/topics/nip-73/)는 책이나 웹페이지처럼 Nostr 바깥의 대상에 이름을 붙인다. 두 규약은 서로 독립적인 기존 명세다([NIP-31 원문](https://github.com/nostr-protocol/nips/blob/master/31.md), [NIP-73 원문](https://github.com/nostr-protocol/nips/blob/master/73.md)).

### NIP-31은 비권장으로 표시되어 있다 {#nip-31-is-marked-unrecommended}

현재 [NIP-31 원문](https://github.com/nostr-protocol/nips/blob/master/31.md)은 "불필요하게 비대하다(unnecessarily bloated)"는 이유로 이 명세를 `unrecommended`로 표시하는 경고로 시작하며, 상태 줄에는 draft, unrecommended, optional이라고 적혀 있다. 이 규약을 사용하는 이벤트가 이미 릴레이에 존재하므로, 아래의 동작 방식은 클라이언트가 그런 이벤트를 읽는 방법을 설명할 뿐 새 프로토콜에 이를 권장하는 것은 아니다.

### alt 태그에 담기는 내용 {#what-an-alt-tag-carries}

[명세](https://github.com/nostr-protocol/nips/blob/master/31.md)에 따르면, 텍스트로 읽히도록 의도되지 않은 사용자 정의 kind의 작성자는 짧은 평문 요약을 담은 `alt` 태그를 추가한다. kind 1 중심 클라이언트가 다른 kind를 요청할 것으로 기대되지는 않지만, 사용자는 여전히 노트에서 그런 이벤트를 참조할 수 있고, 이때 요약이 맥락을 제공한다. 레이블만으로는 투표를 하거나 지갑 요청을 처리할 수 없다. 더 풍부한 상호작용에 대해서는 명세가 [NIP-89: Recommended Application Handlers](/ko/topics/nip-89/)를 안내한다.

`alt`는 태그이므로 [NIP-01](/ko/topics/nip-01/): [Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md)의 이벤트 ID와 서명이 이를 포괄한다. 유효한 서명은 작성자가 통제하는 요약을 인증한다. 즉 작성자가 그 레이블을 게시했음을 보여 줄 뿐 그것이 정확하다는 것은 보여 주지 않으므로, 오해를 부르는 요약이 있을 수 있다. 태그는 공개되므로, 암호화된 콘텐츠를 가진 이벤트에 붙은 `alt`는 요약을 노출하며 콘텐츠가 감추는 내용을 드러낼 수 있다. 이러한 속성은 NIP-31의 규범 텍스트가 아니라 [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) 봉투 구조에서 비롯된다. 최상위 `alt` 태그는 `imeta` 안의 이미지 설명용 `alt` 필드와도 구별되며, 렌더러는 둘을 따로 파싱한다.

### 두 클라이언트가 alt를 읽는 방식 {#how-two-clients-read-alt}

noStrudel의 [커밋 7c68acf 시점 unknown-event 카드](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)에서는 첫 번째 `alt` 태그의 앞뒤 공백을 제거해 주 레이블로 삼고, 선택적으로 `Using <client>` 줄을 붙인다. 값이 없거나 비어 있으면 `Unknown event (kind ...)`가 표시되고, 최대 세 줄의 콘텐츠가 이와 별개로 나타난다. 같은 컴포넌트는 NIP-89 핸들러 템플릿을 통해 `client` 태그를 해석하여, 공유 가능한 주소가 있으면 Open을, 유효한 핸들러 링크가 해석되면 `Open in <client>`를 표시한다. 설명 표시와 앱 연결은 별개의 컨트롤이다.

Amethyst의 [커밋 553f761 시점 UnknownEventDigest.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170)는 산문으로 분류한 콘텐츠를 우선하고, 그렇지 않으면 `alt`로 대체한다. 이 파서는 값의 앞뒤 공백을 제거하고 비어 있지 않은 첫 번째 `alt`를 취하므로, 첫 번째 `alt`가 빈 이벤트는 여기서 noStrudel과 다른 레이블을 받을 수 있다. 두 설명 모두 해당 커밋 시점의 소스를 반영한 것이며, 확인된 릴리스 동작이 아니다.

### 예시: alt 레이블이 있는 투표 {#example-a-poll-with-an-alt-label}

아래 kind 1068 투표는 wss://relay.damus.io에서 가져온 것이며, ID와 BIP340 서명은 [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) 규칙에 따라 검증된다. 범용 렌더러는 이중 언어로 된 `alt` 텍스트를 표시할 수 있고, 투표를 인식하는 클라이언트는 `option`과 `polltype` 태그를 읽는다.

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### NIP-73의 대상과 계열 {#nip-73-subjects-and-families}

[NIP-73 명세](https://github.com/nostr-protocol/nips/blob/master/73.md)(draft, optional이며 unrecommended 표시는 없음)는 외부 대상을 `i` 태그에, 그 식별자 계열을 `k` 태그에 넣어 클라이언트가 정확히 하나의 대상이나 계열 전체를 조회할 수 있게 한다. 책은 `["i", "isbn:9780765382030"]`과 `["k", "isbn"]`을 사용하고, 웹페이지는 URL을 사용하며 `k`를 `web`으로 설정한다. NIP-73은 이벤트 kind를 정의하지 않으며, 다른 이벤트가 이 태그들을 담는다.

### 정규화와 URL 힌트 {#normalization-and-url-hints}

매칭은 문자열이 동일해야 이루어지므로 [명세](https://github.com/nostr-protocol/nips/blob/master/73.md)는 계열마다 형식을 정해 둔다. URL은 프래그먼트 없이 정규화하고, ISBN은 하이픈 없이, geohash는 소문자로, ISO 3166 코드는 대문자로 쓴다. 선택적인 세 번째 배열 요소는 해당 식별자에 대해 별도의 처리 방식이 없는 클라이언트를 위한 URL 힌트를 담는다. 이 힌트는 작성자가 고르는 것이며 식별 정보의 일부가 아니다. 또한 소유권을 증명하지 않고 정식 사이트를 지정하지도 않는다.

### 공유된 식별자가 증명하지 않는 것 {#what-a-shared-identifier-does-not-prove}

[NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)에서 동일한 식별자는 대화를 하나로 묶을 뿐 그 밖의 어떤 것도 입증하지 않는다. 서명된 댓글은 댓글 작성자를 식별하지만, 책, 사이트, 팟캐스트의 발행자를 인증하거나 누가 그것을 통제하는지 보여 주지는 않는다. 별칭, 판본별 ISBN, 서로 다르게 정규화되는 URL은 하나의 대상을 여러 스레드로 나눌 수 있다. 맥락도 중요하다. [NIP-22](/ko/topics/nip-22/): [Comment](https://github.com/nostr-protocol/nips/blob/master/22.md)는 루트 범위에 대문자 `I`/`K`를, 부모에 소문자 `i`/`k`를 사용하고, [NIP-39: External Identities in Profiles](/ko/topics/nip-39/)는 프로필 신원에 `i`를 사용하므로, 모든 `i` 태그가 NIP-73 대상인 것은 아니다.

### 파서와 렌더러 코드 속 NIP-73 {#nip-73-in-parser-and-renderer-code}

rust-nostr의 [커밋 4c8099a 시점 nip73.rs](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)는 알려진 접두사를 타입이 지정된 `ExternalContentId`로 파싱하고 선택적 힌트를 타입이 지정된 URL로 변환하며, 힌트가 있을 때만 세 번째 태그 요소를 내보낸다. 이 코드의 테스트는 하이픈이 들어간 ISBN을 그대로 유지한다. 파서는 접두사를 떼어 낸 나머지를 명세의 정규화를 적용하지 않고 저장하므로, 타입 기반 파싱이 정규 문자열을 보장하지는 않는다. 또한 체인 ID를 계열과 분리하여 `ethereum:100:tx:<hash>`를 `ethereum:tx`로 매핑한다. 해당 리비전에는 `iso3166` 국가 변형이 없다.

Amethyst의 [커밋 553f761 시점 DisplayExternalId.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)는 geohash와 해시태그 식별자를 전용 표시 화면으로 보낸다. URL 식별자도 전용 표시를 받는 반면, 그 밖의 지원 타입은 범용 범위 칩으로 처리된다. URL은 해당 페이지에 대한 앱 자체의 스레드 경로를 연다. 미리보기가 꺼져 있으면 일반 렌더링에서 단순한 링크 칩을 표시하고 미리보기를 요청하지 않는다. 미리보기가 켜져 있으면 없는 미리보기를 가져오는 과정에서 대상 사이트에 접속할 수 있다. 미리보기를 끄면 일반 렌더링에서 그 요청을 피할 수 있다. 두 파일 모두 릴리스 동작을 입증하지는 않는다.

### 예시: 웹페이지에 단 댓글 {#example-a-comment-on-a-webpage}

wss://nos.lol에서 가져온 이 kind 1111 댓글은 같은 공개 Reddit 스레드 URL을 `I`/`K` 쌍과 `i`/`k` 쌍 모두에 넣고, [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md)와 NIP-73에 따라 계열로 `web`을 지정한다. ID와 서명은 검증되며, 이는 누가 댓글을 썼는지를 식별할 뿐 링크된 페이지에 대해서는 아무것도 말해 주지 않는다.

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
