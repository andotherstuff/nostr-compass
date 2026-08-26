---
title: "Nostr Compass #37"
date: 2026-08-26
publishDate: 2026-08-26
translationOf: /en/newsletters/2026-08-26-newsletter.md
translationDate: 2026-08-26
draft: false
type: newsletters
description: "Shopstr와 Routstr가 저장된 비밀값과 relay 기반 탐색을 강화하고, Postr와 Infans가 출시되며, pakstr가 Zapstore 배포를 명시화하고, Nostr의 여섯 번의 8월이 조용한 프로토콜 코어에서 실제 클라이언트까지 댓글 스레드의 흐름을 따라갑니다."
---

[Nostr Compass](https://nostrcompass.org)에 다시 오신 것을 환영합니다. Nostr의 주간 안내서입니다.

**이번 주:** [Shopstr](https://github.com/shopstr-eng/shopstr)가 원격 signer와 지갑 비밀값을 브라우저 저장소 밖에 두고, [Routstr SDK](https://github.com/Routstr/routstr-sdk)가 relay에서 온 공급자 탐색 결과를 검증하며, [Postr](https://gitworkshop.dev/npub1qwkd5wzftcxquuhtkcg0xn9ed7evksluuppf7qdmdh34ywe9uncs5uqfvl/relay.ngit.dev/postr)가 작은 Android 작성 앱으로 출시되고, [Infans](https://github.com/TurkeyNostr/infans)가 육아 기록과 공동 양육자 동기화를 암호화하며, [walls.rip](https://walls.rip/comms)가 PGP로 암호화된 채팅을 공개 Nostr relay로 실어 나르고, [pakstr](https://git.nostrdev.com/stuff/pakstr)가 Zapstore 배포를 명시화합니다. [nostr-tools](https://github.com/nbd-wtf/nostr-tools)는 gift wrap의 rumor를 해당 seal에 묶습니다. 릴리스는 subscription 격리, 프로필 상태, relay 단위 탈퇴 표시를 다룹니다. 프로토콜 작업은 댓글 스레드의 실제 적용, wallet connect의 수수료 상한과 결제 조회 초안, napplet 디스플레이 요청, 동일 계정에서의 실험적 등록까지 이어집니다. 이번 호는 [Nostr의 여섯 번의 8월](#nostr의-여섯-번의-8월)로 마무리합니다.

## 주요 소식

### Postr가 작은 Android 작성 앱으로 출시

[Postr](https://gitworkshop.dev/npub1qwkd5wzftcxquuhtkcg0xn9ed7evksluuppf7qdmdh34ywe9uncs5uqfvl/relay.ngit.dev/postr)는 kind 1 노트를 위해 의도적으로 작게 만든 Android 작성 앱입니다. 개인 키 보관은 [Amber](https://github.com/greenart7c3/Amber), 즉 Android [NIP-55](/ko/topics/nip-55/)(로컬 signer)와 NIP-46 signer에 남습니다. 버전 1.0.0은 연결 끊김과 프로세스 종료를 견디는 지속적인 outbox, 계정별 비공개 초안, 검증된 해시와 범위가 제한된 업로드 인가를 갖춘 [Blossom](/ko/topics/blossom/) 첨부를 제공합니다.

게시는 Postr가 동일한 서명 이벤트를 다시 읽어 서명을 확인한 뒤에 성공으로 처리됩니다. 재시도는 같은 event id를 유지합니다. 배포는 작성자의 [NIP-65](/ko/topics/nip-65/)(relay 목록) 쓰기 relay와 암호화된 부트스트랩 relay, 또는 계정별 사용자 지정 목록을 사용합니다. 서명된 [NIP-34](/ko/topics/nip-34/)(git over Nostr) [저장소 공지](https://njump.me/nevent1qqsqxdwxa8k5e0ftf6j6q5ucs3u94ezgjqmyzwznqt99pyxxw23c74spz3mhxue69uhhyetvv9ujumn8d96zuer9wcx4nr0m)와 이에 대응하는 [kind 0 프로젝트 프로필](https://njump.me/nevent1qqs24gy97frkjkma8ys3rwc3jj8f0qrrmsxjwe39jxrhuemztrygr8qpz3mhxue69uhhyetvv9ujumn8d96zuer9wcspcsat)이 `relay.ngit.dev`에 게시됩니다. 피드, 분석, 광고, 키 저장은 앱 밖에 남습니다.

### Infans가 Nostr에서 육아 기록과 공동 양육자 동기화를 암호화

공동 양육자는 수유, 수면, 성장 기록을 각자의 휴대폰에 두고 육아 데이터 업체 없이 공유할 수 있습니다. [Infans](https://github.com/TurkeyNostr/infans)는 로컬 Room 데이터베이스를 유일한 기준으로 삼고, 백업과 파트너 동기화를 위해 암호화된 kind 30078 [NIP-78](/ko/topics/nip-78/)(애플리케이션별 데이터) 이벤트를 게시하는 Android 육아 기록 앱입니다. 저장소는 로컬 암호 방식을 [NIP-44](/ko/topics/nip-44/)(페이로드 암호화)로 표기하지만, 구현은 AES-256-GCM을 사용하고 NIP-44 v2는 ChaCha20과 HMAC-SHA256을 요구합니다. 따라서 로컬 모드 페이로드를 NIP-44 호환으로 소개해서는 안 됩니다.

[파트너 동기화](https://github.com/TurkeyNostr/infans/blob/main/README.md)는 d-tag `baby-tracker-sync`를 쓰고, 자체 백업은 `baby-tracker-backup`을 씁니다. 비동기 메모는 파트너 페이로드 안에서 전달됩니다. 문서화된 Amber [NIP-55](/ko/topics/nip-55/)(로컬 signer) 경로는 서명과 암호화를 signer에 위임하지만, 저장소는 모든 백업과 파트너 동기화 경로가 NIP-44 v2 암호문을 만든다는 것을 보이는 상호운용 테스트를 제공하지 않습니다. 저장소는 의료기기 주장도, 제3자 보안 검토도 제시하지 않습니다.

### walls.rip의 Ghost Chat이 PGP 암호화 채팅을 공개 Nostr relay로 가져오다

[walls.rip](https://walls.rip/comms)은 익명 통신 도구 모음이며, Ghost Chat 모드는 브라우저에서 OpenPGP 신원을 생성하거나 가져옵니다. [오픈소스 클라이언트](https://github.com/KYC-rip/walls-rip/tree/cf40bda32df5f106007631b21afc3cd193ac0cda/src/components/ghostChat)는 각 메시지를 수신자의 PGP 공개 키로 암호화합니다. 읽을 수 있는 대화는 기기의 로컬 세션 저장소에 남고, 애플리케이션에는 채팅 계정도 중앙 메시지 데이터베이스도 없습니다.

전송은 실제 Nostr이지만 의도적으로 앱 전용입니다. Ghost Chat은 [armored 암호문을 kind 1 이벤트로 게시](https://github.com/KYC-rip/walls-rip/blob/cf40bda32df5f106007631b21afc3cd193ac0cda/src/utils/nostrService.ts)해 기본 relay 다섯 곳으로 보내고, 각 이벤트에 수신자의 PGP 지문에서 파생된 안정적인 방 tag를 붙입니다. 이는 개발자에게 relay를 검열에 강한 메시지 전송 수단으로 쓰는 구체적인 예를 주면서, 동시에 분산 전달만으로는 메타데이터가 보호되지 않고 NIP-17 다이렉트 메시지와 상호운용되지도 않는 이유를 보여줍니다.

### pakstr 0.13.0부터 0.15.0까지가 Zapstore 배포를 명시화

7월의 [0.3.1 패키징 및 Amber 작업](/ko/newsletters/2026-07-29-newsletter/#pakstr-031) 이후, [pakstr](https://git.nostrdev.com/stuff/pakstr)는 웹 자산 폴더를 서명된 Android APK로 바꾸고 Nostr 키로 Zapstore에 게시하는 CLI입니다. [0.13.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.0)은 릴리스 버전 자동 부여를 추가합니다. 이어지는 0.13.1부터 0.13.3은 Blossom 게시를 고칩니다. [인가가 base64url을 쓰게 되고](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.1), [업로드가 Content-Digest를 갖고](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.2), [Zapstore 애플리케이션 이벤트가 Blossom 업로드보다 먼저 게시됩니다](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.3).

[0.14.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.14.0)은 게시가 진행되기 전에 Zapstore 발행자를 검증합니다. [0.15.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.15.0)은 목록 메타데이터를 kind 32267 애플리케이션 이벤트에 쓰고 릴리스 노트를 kind 30063 릴리스 이벤트의 content에 넣습니다. 그래서 패키징된 앱의 Zapstore 기록은 별도의 수동 등재 단계 없이 이름, 요약, 노트를 담을 수 있습니다.

### Heterodyne이 이동 가능한 페르소나와 암호화된 소셜 통신을 규격화

[Heterodyne](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5)은 이동 가능한 페르소나, 인증된 통신, 자기 기기 제어, 소셜 상호작용을 위한 규격 우선 프로토콜 계열입니다. [현재 README](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5)는 기존 네 계층을 조합합니다. 서명된 Nostr 이벤트, 지속 저장을 위한 [Radicle](https://radicle.xyz)(피어 투 피어 git), 암호화된 개별·그룹 대화를 위한 [Marmot](/ko/topics/marmot/)(Nostr 위의 MLS 그룹 메시징), 그리고 신원 회전을 위한 [KERI](https://arxiv.org/abs/1907.02143)(Key Event Receipt Infrastructure) key-event log입니다. 페르소나는 콜드 루트 Nostr npub과 승인된 KERI log의 조합으로 기술되며, 일상적인 서명은 회전하는 epoch 키를 쓰고 Radicle 노드 신원은 이중 증명으로 위임됩니다.

이 계열은 그 작업을 [독립적으로 버전이 매겨지는 네 개의 0.x 초안](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5)으로 나눕니다. Core는 신원, key-event log 검증, 정규화된 Nostr 바이트열, Radicle 저장소 기반을 담당하고, Comms는 Nostr 고유 envelope, 프라이버시 등급, 게시, Marmot 대화를 담당하며, Social은 공개 팔로우, 상호작용, 목록을 담당합니다. 자기 기기 등록과 권한 부여를 담당하는 Control은 미완성이며 완료되었다고 주장할 수 없습니다. 이 문서들은 1.0 전에 깨질 수 있는 초안으로 남아 있고, 이번 호는 Heterodyne 클라이언트 릴리스가 나오기 전에 이 계열을 소개합니다.

## 릴리스

### Nostr Java v2.0.8: subscription 격리와 이동 가능한 NIP-44

이벤트 다섯 개를 가진 relay에 대한 gift wrap 질의가 0개, 2개, 6개를 무작위로 돌려주고 있었습니다. relay와 통신하고 Nostr 페이로드를 암호화하는 Java 라이브러리 [Nostr Java](https://github.com/tcheeric/nostr-java)가 들어오는 모든 프레임을 연결의 모든 listener에게 전달했기 때문입니다. [버전 2.0.8](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8)은 `EVENT`, `EOSE`, `CLOSED`를 해당 프레임이 지목한 subscription으로 보내므로, 한 질의의 저장 이벤트 종료 신호가 다른 질의를 닫는 일은 더 이상 없습니다. `NOTICE`, `OK`, `AUTH` 같은 연결 범위 프레임은 여전히 모든 listener에 도달합니다.

같은 [릴리스](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8)의 [NIP-44](/ko/topics/nip-44/)(페이로드 암호화)는 프로세스에 등록된 JCE provider를 더 이상 필요로 하지 않습니다. 예전에는 해당 JVM에서 키를 생성한 뒤에야 암호화가 동작했고, 그 부수 효과로 BouncyCastle이 등록되었습니다. 또한 "BC"라는 이름의 provider를 추가해도 아무 일도 일어나지 않는 Android에서는 실패했습니다. 이제 두 cipher 경로 모두 BouncyCastle의 경량 ChaCha20 엔진을 쓰고, 키 생성이 프로세스 전역 JCE 상태를 바꾸지도 않습니다. provider 등록을 라이브러리에 의존했던 호출자는 직접 등록해야 합니다. 이로써 닫히는 이슈가 [NIP-44의 JCE provider 의존](https://github.com/tcheeric/nostr-java/issues/537)입니다.

### NoorNote v1.3.6: 프로필 상태와 분류 광고

[NoorNote](https://github.com/77elements/noornote)는 데스크톱, 웹, Android용 Nostr 클라이언트입니다. [1.3.4가 암호화된 커뮤니티 가입을 추가](/ko/newsletters/2026-08-19-newsletter/#noornote-134-joining-encrypted-communities-from-an-invite-link)한 지 한 주 뒤, [버전 1.3.6](https://github.com/77elements/noornote/releases/tag/v1.3.6)은 프로필의 [NIP-05](/ko/topics/nip-05/)(도메인 검증) 이름 아래에 [NIP-38](/ko/topics/nip-38/)(사용자 상태)을 보여줍니다. 한 줄짜리 일반 상태나 음악 상태를 담고 선택적으로 만료되는 kind `30315` addressable 이벤트입니다. 그 줄을 누르면 보는 사람 자신의 상태가 설정됩니다.

[NIP-99](/ko/topics/nip-99/)(kind `30402` 마켓플레이스 제안)의 [분류 광고](https://github.com/77elements/noornote/releases/tag/v1.3.6)가 이제 앱 전체에서 렌더링되므로, 마켓플레이스 애드온은 사고팔 때만 필요합니다. 프로필의 비공개 별칭 메모도 경고용 주황색으로, 채워진 메모 아이콘과 주황색 아바타 링과 함께 표시됩니다.

### nostrord v2.9.0: relay 단위 그룹 상태와 미디어

한 호스트에서 [NIP-29](/ko/topics/nip-29/)(relay 관리 그룹) 그룹을 떠나면 예전에는 다른 모든 relay에서 같은 그룹 id가 억제되었습니다. relay 호스팅 커뮤니티용 크로스플랫폼 클라이언트 [nostrord](https://github.com/nostrord/nostrord)가 탈퇴와 삭제 표시를 맨 id로 키를 잡았기 때문입니다. [relay 단위로 범위가 정해진 탈퇴·삭제 표시](https://github.com/nostrord/nostrord/pull/253)는 그 억제를 만들어 낸 호스트에 남기므로, 두 relay에서 id를 공유하는 그룹이 한 쌍으로 함께 탈퇴되거나 버려지지 않습니다. 이미 구성원이라는 이유로 relay가 거절하는 가입은 이제 성공으로 처리되어 로컬 표시를 지웁니다. 이는 이전에는 흡수 상태였습니다. 자기 복구가 한 칸을 지우는 동안 콜드 스타트가 다른 칸을 되살렸던 것입니다.

[버전 2.9.0](https://github.com/nostrord/nostrord/releases/tag/v2.9.0)은 다른 클라이언트가 `![alt](url)`로 쓰는 [markdown 이미지 임베드](https://github.com/nostrord/nostrord/pull/254)도 렌더링해서, 이미 감지된 URL 주위에 markdown 기호를 보여주지 않습니다. 다이렉트 메시지는 [NIP-17](/ko/topics/nip-17/)(gift wrap된 비공개 DM)의 [kind `15` 파일 rumor](https://github.com/nostrord/nostrord/pull/275)를 지원하므로, Jumble에서 보낸 암호화 첨부가 내려받아지고 복호화되어 표시되며, 보내는 첨부는 업로드 전에 암호화됩니다. 이 태그는 이제 [지난주에 다룬 NIP-4e 암호 키 작업](/ko/newsletters/2026-08-19-newsletter/#nostrord-implements-an-unmerged-encryption-key-proposal)을 실제로 담고 있습니다. 제안은 아직 병합되지 않았고, nostrord는 초안과 다른 부분에서는 실제 배포된 Jumble의 동작을 따른다고 말합니다.

## 미출시 변경 사항

### Shopstr가 원격 signer와 지갑 비밀값을 브라우저 저장소 밖에 두다

[Shopstr](https://github.com/shopstr-eng/shopstr)는 [NIP-99](/ko/topics/nip-99/) 분류 광고를 위한 웹 마켓플레이스입니다. [지난달의 결제 정합성 작업](/ko/newsletters/2026-07-22-newsletter/#shopstr-binds-payment-validation-to-signed-receipts-and-server-side-prices) 이후, [직렬화된 bunker signer 비밀값을 `localStorage`에 쓰는 것을 중단했습니다](https://github.com/shopstr-eng/shopstr/pull/437). [NIP-46](/ko/topics/nip-46/)(원격 서명) bunker 페이로드에는 살아 있는 `bunker://` URL과 생성된 앱 개인 키가 들어 있었기 때문에, Shopstr origin의 어떤 스크립트든 원격 서명 세션을 이어받을 수 있었습니다. 이제 bunker 데이터는 현재 세션 동안 메모리에 남고, 남아 있던 bunker 페이로드는 발견되면 제거되며, bunker가 아닌 signer 유형은 이전 저장 동작을 유지합니다.

대응하는 [NWC 변경](https://github.com/shopstr-eng/shopstr/pull/436)은 [NIP-47](/ko/topics/nip-47/)(wallet connect) 자격 증명에 같은 처리를 합니다. Shopstr는 지갑 동작에 쓰이는 비밀값을 포함한 `nostr+walletconnect://` 문자열 전체를 일반 브라우저 데이터로 저장하고 결제 시 재사용했습니다. 이제 연결 문자열과 지갑 메타데이터는 메모리에 남고, 오래된 저장 사본은 로컬 데이터를 읽을 때 삭제됩니다. 활성 세션 중 이미 Shopstr origin에서 실행되는 스크립트는 메모리의 그 값들을 여전히 볼 수 있습니다.

### Routstr가 relay에서 온 공급자 탐색 결과를 검증

예전에는 악의적인 relay 하나가 Routstr 클라이언트가 신뢰하는 추론 공급자를 정할 수 있었습니다. [Routstr SDK](https://github.com/Routstr/routstr-sdk)는 Nostr에서 AI 공급자를 찾아 Cashu로 지불하는 마켓플레이스 Routstr의 TypeScript 라이브러리입니다. [이번 주 탐색 수정](https://github.com/Routstr/routstr-sdk/pull/47)은 relay가 전달한 모든 공급자 공지, 모델 목록, 리뷰(kind 38421, 38423, 38425)를 소비자가 보기 전에 검증하므로, 신뢰된 pubkey를 내세우면서 쓰레기 서명을 담은 리뷰는 더 이상 순위에 들어가지 않습니다.

[아주 먼 미래의 타임스탬프](https://github.com/Routstr/routstr-sdk/pull/47)는 "최신 리뷰" 선정 전에 버려집니다. 로컬 시계보다 15분 이상 앞선 이벤트는 실시간 경로와 영속 저장소를 읽을 때 제거되므로, 위조된 `created_at`이 재시작을 넘나들며 올바르게 서명된 리뷰를 앞지를 수 없습니다. 신뢰할 수 있는 리뷰를 얻을 수 없으면 리뷰 게이트는 닫힌 상태로 실패하고, 리뷰가 도착할 때까지 리뷰 없는 공급자를 지불 순위에서 제외합니다. 운영자는 여전히 공급자를 수동으로 활성화할 수 있습니다.

### nostr-tools가 gift wrap의 rumor를 해당 seal에 묶다

[NIP-59](/ko/topics/nip-59/)(gift wrap) 이벤트를 풀 때 예전에는 wrap을 복호화하고 seal을 복호화한 뒤, seal이 누구에게서 왔는지 확인하지 않고 안쪽 rumor를 반환했습니다. [nostr-tools](https://github.com/nbd-wtf/nostr-tools)는 Nostr 프로토콜 도우미를 모은 JavaScript 라이브러리입니다. [이번 주 unwrap 수정](https://github.com/nbd-wtf/nostr-tools/pull/545)은 wrap이 kind 1059여야 하고, seal이 유효한 서명을 가진 kind 13이어야 하며, rumor의 `pubkey`가 seal의 `pubkey`와 같아야 한다고 요구합니다. seal을 복호화하는 것 자체가 이미 `seal.pubkey`에 대한 통제를 증명합니다. 마지막 확인이 없으면 누구든 다른 사람을 작성자로 지목한 rumor를 seal할 수 있고, 클라이언트가 그 메시지를 그 피해자에게 귀속시키게 만들 수 있습니다.

[NIP-17](/ko/topics/nip-17/)(gift wrap된 비공개 DM)은 같은 unwrap 경로를 쓰므로 이 결속은 비공개 DM에도 적용됩니다. [일괄 unwrap](https://github.com/nbd-wtf/nostr-tools/pull/545)은 이제 그 확인을 통과하지 못한 wrap에서 예외를 던지지 않고 건너뜁니다. gift wrap은 요청하지 않아도 오는 것이고, 적대적인 이벤트 하나가 relay 질의의 나머지를 버리게 만들 수 있기 때문입니다.

### Haven이 서명된 relay 관리와 로컬 노트 브라우저를 추가

[Haven](https://github.com/barrydeen/haven)은 자체 호스팅 Nostr relay이자 Blossom 미디어 서버입니다. 새로 병합된 [관리 콘솔](https://github.com/barrydeen/haven/pull/135)은 각 relay 엔드포인트에서 NIP-86 관리 호출을 제공하며, 모든 요청은 설정된 소유자의 NIP-98 이벤트로 인증됩니다. 운영자는 relay에 서명 키를 주지 않고도 차단, 허용 목록, kind 규칙, relay 이름, 저장된 미디어를 관리할 수 있습니다. 읽기 전용 노트 브라우저는 암호화된 kind를 불투명하게 유지하고 원격 미디어는 클릭 후에만 불러오므로, 운영자의 IP 주소를 외부 호스트에 알리는 자동 요청을 피합니다.

같은 [Haven 변경](https://github.com/barrydeen/haven/pull/135)은 지속적인 트래픽 그래프를 추가하고, 기본 LMDB에서 저장된 이벤트를 세는 작업이 끝없이 돌며 CPU 코어를 점유하고 이후 통계 호출을 막던 문제를 고칩니다. Haven은 이제 종료가 보장되는 곳에서는 백엔드 카운터를 쓰고, 그렇지 않으면 한계가 정해진 이벤트 순회를 씁니다. 프로젝트는 이벤트 페이지네이션, 삭제, 지표 영속화, 소유자 확인, URL에 묶인 요청 서명에 대한 첫 23개 테스트를 추가했습니다.

### Amethyst가 Blossom 인가를 이미지 로딩 스레드에서 떼어내다

Android Nostr 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)는 [OkHttp dispatcher 스레드에서 Blossom 읽기 인가를 기다리는 것을 중단했습니다](https://github.com/vitorpamplona/amethyst/pull/3991). interceptor는 이제 네트워크 스레드에서 벗어나 서명을 시작하고, 이미지 fetcher는 호스트별로 공유되는 하나의 서명을 기다린 뒤 보호된 blob 요청을 재시도합니다. 따라서 인가가 필요한 이미지가 몰려도 signer가 응답하는 동안 호스트별 연결 슬롯을 모두 차지하지 않습니다.

같은 [Amethyst 패치](https://github.com/vitorpamplona/amethyst/pull/3991)는 토큰 인코딩을 BUD-11에 맞춥니다. 패딩 없는 Base64url, `server` 범위, blob 전용 `x` tag 없음으로, 토큰 하나가 같은 호스트의 여러 blob을 담당할 수 있습니다. 새 동시성 테스트는 캐싱, 만료, 서명된 재시도, 하나의 서명을 공유하는 열여섯 개의 동시 호출자를 검사합니다.

## 프로토콜 및 사양 작업

### NIP

Snort와 Ditto는 이제 일반 텍스트 답글에 [NIP-22](/ko/topics/nip-22/)(댓글 스레드)를 사용해 호환 경로를 유지하면서 kind 1111로 수렴하고 있습니다. 이것이 프로토콜 전반의 단일 답글 kind를 정하는 것은 아닙니다. [6월 수정](/ko/newsletters/2026-06-24-newsletter/#kind-1111-as-reply-to-kind-1-notes)이 kind 1 노트에 NIP-22를 쓰는 금지를 없앤 뒤, [NIP-30](/ko/topics/nip-30/)(사용자 지정 이모지)에 대한 [병합된 추가](https://github.com/nostr-protocol/nips/pull/2448)가 kind `1111`을 `emoji` tag를 담을 수 있는 이벤트 목록에 넣었고, `content`의 짧은 코드가 그 tag로 해석됩니다. 웹 Nostr 클라이언트 [Snort](https://github.com/v0l/snort)는 이제 [모든 답글을 kind 1111로 씁니다](https://github.com/v0l/snort/commit/420ed60e2ff43bd373f2583e171a77002ec9f3a0). 대문자 `E`/`A` 루트 범위 tag로 그 댓글을 불러오고, 오래된 노트에 대해서는 선택적인 [NIP-10](/ko/topics/nip-10/)(kind 1 답글 tag) 경로도 받아들입니다. Mastodon 서버와 Nostr relay를 겸하는 [Ditto](https://github.com/soapbox-pub/ditto)는 [모든 답글을 NIP-22 댓글로 게시](https://github.com/soapbox-pub/ditto/commit/8a0ffc6e3a5d9202ffc452fa0de8ae33b5883384)하며, 텍스트는 kind `1111`, 음성은 kind `1244`로 하고 기존 kind 1 답글도 계속 렌더링합니다. NIP-10만 이해하는 클라이언트는 새 형태를 보지 못합니다. 최상위 게시물은 여전히 kind 1입니다.

[NIP-47](/ko/topics/nip-47/)(Nostr Wallet Connect)의 `pay_invoice` 요청에는 현재 클라이언트가 라우팅 수수료 상한을 지정할 표준 방법이 없습니다. [열린 수수료 상한 제안](https://github.com/nostr-protocol/nips/pull/2444)은 `pay_invoice`에 밀리사토시 단위의 선택적 `max_fee` 매개변수를 추가합니다. 예산을 지키는 지갑은 라우팅 비용이 `amount + max_fee`를 넘는 결제를 보내서는 안 되며(MUST NOT), 인출도 결제 시도도 없는 상태로 정의된 `FEE_LIMIT_EXCEEDED`를 반환해야 합니다(MUST). 이를 지원하는 구현은 클라이언트가 대조할 수 있도록 응답에 `fees_paid`를 포함해야 합니다(MUST). 수수료 한도를 지원하지 않는 구현은 알 수 없는 매개변수를 무시하며, 클라이언트는 `fees_paid` 필드가 없는 것을 상한이 적용되지 않았을 수 있다는 신호로 받아들여야 합니다. 이 변경은 이벤트 kind를 추가하지 않고 병합될 때까지 제안으로 남습니다.

[열린 NIP-32 언어 라벨 제안](https://github.com/nostr-protocol/nips/pull/2451)은 작성자가 선언하는 본문 언어를 위해 `["l", "<BCP-47>", "lang"]`을 표준화합니다. 한 글자 `l` tag는 이미 relay에서 색인 가능하므로, 클라이언트는 relay 업그레이드나 다운로드 후의 믿을 수 없는 언어 감지 없이 `{"#l":["ja"]}`로 일본어 피드를 요청할 수 있습니다. 초안은 NIP-66 relay 보고서, NIP-68 이미지 메타데이터, NIP-71 오디오 트랙의 언어 예시도 같은 이름공간으로 옮깁니다. 라벨은 검증되지 않은 작성자의 주장으로 남고, 이 변경은 병합되지 않았습니다.

### Nostr Wallet Connect

시간 초과, 재연결, 놓친 알림 뒤에 wallet connect 클라이언트는 어떤 Bitcoin 결제 프로토콜이 만들었는지 모르는 상태로 결제 기록 하나를 요청할 방법이 필요합니다. [NWC 확장 저장소](https://github.com/nostr-wallet-connect/nwc)의 [열린 결제 조회 초안](https://github.com/nostr-wallet-connect/nwc/pull/5)은 NIP-47 코어와 나란히 선택적인 NWC-09 `lookup_payment`을 정의합니다. 요청은 정확히 하나의 선택자를 씁니다. 지갑 범위에서 안정적인 `transaction_id`, `lookup_invoice`가 이미 쓰는 BOLT11 호환 `payment_hash` 및/또는 `invoice` 필드, 또는 `payment_type`과 다른 확장이 정의한 타입 지정 `lookup` 객체입니다. 성공한 결과는 공통 envelope(`transaction_id`, `type`, `state`, `payment_type`, msat 단위 `amount`, 타임스탬프, 선택적 `fees_paid`와 `metadata`, 그리고 구분된 `details` 객체)을 반환하며 해당 연결에서 보이는 기록 정확히 하나로 해석되어야 합니다(MUST). 지갑은 접근할 수 없는 기록이 존재하는지 드러내서는 안 되며(MUST NOT), 보이는 기록 여러 개에 일치하는 선택자는 `MULTIPLE_MATCHES`를 반환합니다. 상태는 `pending`, `accepted`, `settled`, `failed`, `expired`, `canceled`입니다. 같은 제안은 그 envelope을 재사용하는 NWC-12 BOLT12 offer와 결제 세부 정보도 추가합니다. 두 문서 모두 아직 초안입니다.

### NAP

[열린 NAP-DISPLAY 초안](https://github.com/napplet/naps/pull/97)은 napplet이 호스트에게 사용이 허용된 픽셀 디스플레이를 물어볼 수 있게 합니다. 이는 따로 진행 중인 [병합되지 않은 NIP-5D 웹 애플릿 제안](/ko/topics/nip-5d/)에 기반하며, 그 제안은 Newsletter #17이 소개했고 병합된 NIP 집합 밖에 남아 있습니다. 초안은 `display.list`를 정의해 논리적 너비와 높이, 런타임이 고르는 유형(`lcd`, `eink`, `led-matrix`, `other`)을 담은 불투명하고 안정적인 식별자를 반환하게 하고, `display.push`는 좌표로 지정된 3바이트 sRGB 픽셀의 비어 있지 않은 배치를 제출하게 합니다. 런타임 탐색은 논리 RGB를 기기 고유의 색 깊이, 방향, 갱신 주기에 대응시키며 갱신을 회전, 재배열, 양자화, 디더링, 병합할 수 있습니다(MAY). 셸 정책은 napplet이 어떤 디스플레이를 열거나 쓸 수 있는지 통제하며 배치를 거부, 속도 제한, 상한 설정할 수 있습니다(MAY). 픽셀을 적용하기 전에 런타임은 배치 전체를 검증하므로, 실패한 push는 기기에서 아무것도 바꾸지 않습니다. 성공은 배치가 받아들여졌다는 뜻이며, 하드웨어 갱신이 끝났다는 뜻은 아닙니다.

### Marmot

[열린 Marmot 실험](https://github.com/marmot-protocol/marmot/pull/417)은 동일 계정 등록에 대해 철회된 External Commit 초안을 한계가 정해진 Commit 형태로 대체합니다. Nostr 위의 MLS 그룹 메시징 프로토콜 [Marmot](/ko/topics/marmot/)은 그 초안에서 데이터 없는 구성 요소 `0x800d`(`marmot.same-account-membership.v1`)를 협상된 동작 표시로 지정합니다. 그것이 요구되는 동안, 현재 leaf는 인라인 동일 계정 Add를 정확히 하나 또는 인라인 형제 Remove를 하나에서 넷까지 작성할 수 있으며, 각각 일반 UpdatePath와 통상적인 수렴 우선순위를 갖고, 모든 Commit은 한 계정당 최대 다섯 개의 현재 leaf를 남겨야 합니다(MUST). 페어링은 스폰서가 표시하는 짧은 수명의 QR(`marmot-pairing-v1:`)을 쓰며, 그 비밀값이 전달 수단과 무관한 채널에서 HKDF-SHA256과 ChaCha20-Poly1305에 공급됩니다. 로컬 전용 kind `453` 증명은 세션을 공유 계정 키에 묶고 relay로 전달되지 않습니다. 일치하는 Welcome 뒤에 참여자의 첫 애플리케이션 페이로드는 Welcome과 GroupInfo 다이제스트에 묶인, 렌더링되지 않는 kind `452` 확인입니다. 그래서 바이트 단위로 동일한 Welcome을 KeyPackage를 다시 소비하지 않고 복구할 수 있습니다. 페어링된 스폰서는 그 분기에서 참여자의 신뢰 기점이며 전역 확정성을 증명하지 않습니다. 함께 있는 계정 동기화 문서는 탐색적이고 상호운용되지 않습니다. 이 실험은 채택된 기본 프로필에 포함되지 않습니다.

## Nostr의 여섯 번의 8월

8월들은 하나의 상호운용성 문제를 따라갑니다. 클라이언트가 대상을 어떻게 지목하고 그것에 반응을 붙이는가입니다. [최초의 프로토콜 저장소](https://github.com/nostr-protocol/nostr)는 2021년 8월 커밋을 기록하지 않았고, 서명된 이벤트의 핵심은 멈춰 있었습니다. 그다음 [NIP-25](/ko/topics/nip-25/)(리액션)가 2022년에 kind 1 전용 칸을 떠났습니다. 일반 replaceable 기록은 2023년에 빈 식별자를 가진 `naddr`과 `a` 좌표를 얻었고, 2024년에는 별도의 [parameterized-replaceable 분류가 addressable event로 이름이 바뀌었습니다](https://github.com/nostr-protocol/nips/commit/ca3c52e3e74f0a4679f1c6c0d9ac6461ea748d2d). wire format은 바뀌지 않았습니다. 리액션은 2025년에 외부 미디어로 옮겨갔습니다. [NIP-22](/ko/topics/nip-22/)(댓글 스레드) kind 1111은 2026년에 실제로 쓰는 클라이언트에 도달했습니다. 이 흐름은 멈춰 있던 프로토콜 문서에서, 노트와 replaceable 기록과 네트워크 밖 객체를 가로질러 작동하는 공통의 답글·리액션 어휘로 이어집니다.

### 2021년 8월

최초 프로토콜 저장소의 [2021년 8월 커밋 구간](https://api.github.com/repos/nostr-protocol/nostr/commits?since=2021-08-01T00:00:00Z&until=2021-08-31T23:59:59Z)은 비어 있습니다. 그 활동 없는 달 직전의 변경은 6월 18일 NIP-05 초안으로, 공개 키를 가리키는 사람이 읽을 수 있는 포인터로 DNS 도메인 식별자를 추가했습니다. [NIP-05](/ko/topics/nip-05/)(도메인 식별자)는 나중에 well-known JSON 파일로 옮겨갔지만, 2021년 중반에는 아직 DNS TXT 조회였습니다. 8월은 그 식별자 작업을 확장하지도, 새로운 이벤트 kind나 relay 메시지를 추가하지도 않았습니다.

같은 빈 구간이 사양 옆에 이미 존재하던 도구들에도 나타납니다. 2021년 1월에 만들어진 명령줄 클라이언트 [noscl](https://github.com/fiatjaf/noscl/commits?since=2021-08-01&until=2021-09-01)은 8월 커밋을 기록하지 않았고, [go-nostr](https://github.com/nbd-wtf/go-nostr/commits?since=2021-08-01&until=2021-09-01)와 [nostr-tools](https://github.com/nbd-wtf/nostr-tools/commits?since=2021-08-01&until=2021-09-01)도 마찬가지였습니다. 프로토콜 활동은 연말에야 다시 시작되어, 저장소가 [NIP-09](/ko/topics/nip-09/)(이벤트 삭제 요청)를 배정하고 DNS 방식을 well-known JSON 식별자 파일로 대체했습니다. 2021년 8월은 6월의 식별자 초안과 12월의 삭제 및 well-known JSON 작업 사이의 활동 없는 단계이며, 그 사이 [서명된 이벤트와 relay 모델](https://fiatjaf.com/nostr.html)은 쓰인 대로 유지되었습니다.

### 2022년 8월

8월 19일, [NIP-25 수정](https://github.com/nostr-protocol/nips/commit/7af2540c6e392d5cb789c743b1dd237294388649)이 kind 7 리액션의 대상을 kind 1 텍스트 노트에서 다른 노트로 확장했습니다. kind 7 이벤트와 `+`/`-` 관례는 이미 초안에 있었습니다. 그 상호운용성 변경은 좋아요, 싫어요, 이모지가 프로필, 팔로우 목록, 또는 같은 `e`와 `p` tag를 재사용하는 이후의 어떤 이벤트 kind에도 붙을 수 있게 했습니다.

현재의 [NIP-25 사양](https://github.com/nostr-protocol/nips/blob/master/25.md)은 그 일반화를 유지합니다. 리액션은 다른 이벤트에 대한 사용자 반응을 나타내며, addressable 대상은 `kind:pubkey:d-tag` 좌표를 담은 `a` tag도 받습니다. Android 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst/blob/main/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt)는 리액션 builder에서 그 계약을 구현합니다. builder는 어떤 이벤트든 받고 `e`, `p`, `k` tag를 쓰며, 대상이 addressable event일 때 `a` tag를 더합니다. 이로써 리액션 대상은 kind 1을 넘어 일반화되었고, 이후 8월의 변경들이 안정적인 좌표와 댓글 문맥 tag를 더했습니다.

relay 소프트웨어도 tag 규칙을 저장 동작으로 옮기고 있었습니다. 8월 17일, nostr-rs-relay는 [16진수처럼 보이는 모든 tag 값을 이진 색인 키로 취급하는 것을 멈췄습니다](https://github.com/scsibug/nostr-rs-relay/commit/035cf34673ae23407bda6656eef505b3178482ab). 그 최적화를 한 글자 tag와 소문자 16진 값으로 제한해, 필터가 맞출 수 없는 형태로 디코딩하는 대신 일반 텍스트 tag를 보존했습니다. 그래서 그 달은 상호운용성의 두 면을 함께 묶었습니다. 사양은 상호작용이 가리킬 수 있는 대상을 넓혔고, relay는 그 대상 tag를 색인하고 가져오는 방식을 바로잡았습니다.

### 2023년 8월

8월 24일, [NIP-19](/ko/topics/nip-19/)(bech32 식별자)는 [parameterized가 아닌 replaceable event를 naddr로 인코딩하는 방법을 정의했습니다](https://github.com/nostr-protocol/nips/commit/208dee210249f84496ddfa823542d023e23b3edb). 식별자 필드인 `d` tag는 메타데이터와 연락처 목록처럼 pubkey와 kind만으로 대체되는 kind에서 빈 문자열이 되었습니다. 닷새 뒤, [NIP-01](/ko/topics/nip-01/)(기본 이벤트 및 relay 프로토콜)이 [대응하는 a-tag 형식을 추가했습니다](https://github.com/nostr-protocol/nips/commit/e50bf508d9014cfb19bfa8a5c4ec88dc4788d490). 끝에 콜론이 붙고 식별자가 없는 `kind:pubkey:`입니다. 이제 클라이언트는 다음 대체가 무효로 만들 특정 event id를 기다리지 않고 replaceable 기록을 가리킬 수 있었습니다.

[현재의 NIP-19 본문](https://github.com/nostr-protocol/nips/blob/master/19.md)은 그러한 replaceable event에 빈 문자열을 쓰라고 구현자에게 여전히 안내합니다. JavaScript 식별자 라이브러리 [nostr-tools](https://github.com/nbd-wtf/nostr-tools/blob/master/nip19.ts)는 그 필드를 `naddrEncode`로 인코딩하므로, 호출자는 빈 식별자를 넘겨 공유 가능한 좌표를 만들 수 있습니다. 2023년 8월의 작업은 replaceable 상태를, 기반 이벤트가 대체된 뒤에도 댓글이나 리액션, 공유 링크가 지목할 수 있는 것으로 바꿨습니다. 다음 8월은 관련된 parameterized-replaceable 분류의 용어를 표준화했고, 이후의 댓글 tag는 그 좌표 문법을 `A`와 `a`로 재사용했습니다.

같은 시기에 비공개 페이로드도 이동 가능해지고 있었습니다. 8월 24일, rust-nostr는 [JavaScript 바인딩에 NIP-44 암호화·복호화 함수를 추가](https://github.com/nostrdevkit/nostr/commit/39e581d398d926ff37a6b57a1c6d5fceae270d77)해, 버전이 붙은 conversation key 방식을 네이티브 Rust 호출자와 나란히 웹 애플리케이션에도 열었습니다. 8월 22일, Amethyst는 [NIP-44 암호화를 메시징 이벤트 형식에서 분리](https://github.com/vitorpamplona/amethyst/commit/fa4257ad7d7afa76ccb368b4cf6cadefa39461ba)해, 내용을 어떻게 암호화하는지와 애플리케이션이 그것을 어떻게 전송하는지 사이의 프로토콜 분리를 반영했습니다. 안정적인 좌표는 공개 객체를 참조하기 쉽게 했고, 재사용 가능한 암호화 API는 비공개 내용을 하나의 메시지 kind에 묶지 않고 구현들 사이에서 옮기기 쉽게 했습니다.

같은 달은 인접한 키 격리, 인터페이스, 교육 작업에 대한 자금도 가져왔습니다. [8월 17일 OpenSats 지원금 라운드](https://github.com/OpenSats/website/commit/acd33f11b7529c34a846e8c4b4a6c63e7187f970)는 Nostr Fund 지원금을 Amber, 공동의 Nostr 인터페이스 설계, Nostr 활용 사례 교육에 배정했습니다. Amber의 지원금은 NIP-46을 통해 서명 키를 전용 Android 애플리케이션에 두는 데 집중했고, 설계와 교육 지원금은 온보딩과 재사용 가능한 애플리케이션 패턴을 다뤘습니다. 더 넓은 Nostr 체계는 사양 커밋, 키 격리, 인터페이스 작업, 그리고 공동 기반으로 자금이 지원된 개발자 교육을 통해 전진하고 있었습니다.

### 2024년 8월

8월 20일, 사양들은 NIP-01과 장문 기사, 라이브 활동, 목록, 캘린더, 분류 광고를 포함한 열여섯 개의 다른 문서에서 ["parameterized replaceable event"를 "addressable event"로 이름을 바꿨습니다](https://github.com/nostr-protocol/nips/commit/ca3c52e3e74f0a4679f1c6c0d9ac6461ea748d2d). wire format은 바뀌지 않았습니다. `kind:pubkey:d-tag`가 좌표로 남았습니다. 바뀐 것은 그 좌표를 이미 쓰던 모든 사양이 이제 같은 단어로 그것을 부른다는 점입니다.

그 어휘가 현재 구현들이 담고 있는 것입니다. [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)은 addressable event를 kind, pubkey, `d` tag별 최신 기록으로 저장합니다. [NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)는 naddr을 "a nostr addressable event coordinate"라고 부릅니다. 위에서 인용한 Amethyst의 리액션 경로는 `a` tag를 쓰기 전에 대상을 `AddressableEvent`로 타입 지정합니다. 2023년의 좌표 확장과 2024년의 용어 변경은 모두 `kind:pubkey:d-tag` 좌표 문법을 쓰고, NIP-01은 일반 replaceable event와 addressable event의 구분을 계속 유지합니다. 그래서 이후의 댓글은 지금 어떤 event id가 그 주소를 차지하는지 신경 쓰지 않고 대문자 `A`로 addressable 논의를 가져올 수 있습니다.

저장 프로토콜도 명시적 식별자에 대한 같은 선호를 적용하고 있었습니다. 8월 27일, Blossom의 BUD-04는 [하나의 인가 이벤트가 여러 blob 해시 `x` tag를 담을 수 있게 했습니다](https://github.com/hzrd149/blossom/commit/4325aa79891cb4d68448ce16e5fa5519058eae4b). 그래서 클라이언트는 해시들이 하나의 객체를 가리키는 척하지 않고도 한계가 정해진 업로드, 미러, 삭제 묶음을 인가할 수 있었습니다. 나흘 뒤, 프로젝트는 [blob descriptor를 명확히 하고 예시를 추가했습니다](https://github.com/hzrd149/blossom/commit/95eb92e70768b0a2d5bab3dc42a5e3418f9055ec). Nostr 이벤트가 내용 주소 기반 미디어 작업을 조율하는 동안 바이트는 미디어 서버에 남아, 서명된 인가와 저장 전송이 분리되었습니다.

8월 29일, 원격 서명은 불완전한 relay 집합에 더 관대해졌습니다. go-nostr는 NIP-46 클라이언트를 바꿔 [고장 난 relay 하나가 다른 설정된 relay를 통해 보내는 요청을 막지 못하게 했습니다](https://github.com/nbd-wtf/go-nostr/commit/5edb54efee52f469fe62180c20d2876fe9c72910). relay 연결과 게시 시도는 독립적으로 실행되고, 어느 연결이든 성공하면 호출이 진행됩니다. 8월 19일, OpenSats는 [Amethyst 제작자 Vitor Pamplona에 대한 장기 지원도 발표](https://github.com/OpenSats/website/commit/b0ac18552a80c662b6ca33381abeed5c3d833a4c)했고, 여기에는 NIP-17 비공개 메시지, 크로스플랫폼 라이브러리, outbox 모델 작업이 포함됩니다. 프로토콜 어휘, 견고한 전송, 프라이버시 작업, 지속적인 유지보수 자금이 같은 목표로 모이고 있었습니다. 기기를 넘나들고 고르지 않은 relay 상황에서도 계속 작동할 수 있는 클라이언트입니다.

### 2025년 8월

8월 22일, [NIP-25가 외부 콘텐츠 리액션을 얻었습니다](https://github.com/nostr-protocol/nips/pull/2020). 네이티브 Nostr 이벤트가 아닌 것에 대한 리액션은 kind 17이어야 하고 [NIP-73](/ko/topics/nip-73/)(외부 콘텐츠 식별자)의 `k`와 `i` tag를 담아야 하며, 이전의 웹사이트 `r` tag를 대체합니다. 병합된 본문의 예시는 웹 URL(`k=web`)과 프로그램 GUID 및 항목 GUID로 식별되는 팟캐스트 에피소드이고, Fountain URL이 힌트로 붙습니다. 리액션은 2022년에 kind 1을 떠났습니다. 이제는 Nostr 이벤트 집합 자체를 떠났습니다.

2025년 8월 15일에 게시된 [Fountain 1.3](https://blog.fountain.fm/p/1-3)은 사양 병합 전에 그 좋아요를 출시했고, 다른 팟캐스트 앱이 읽을 수 있도록 Nostr로 작동한다고 밝혔습니다. 오늘의 [NIP-25 문서](https://github.com/nostr-protocol/nips/blob/master/25.md)는 여전히 Fountain의 팟캐스트 GUID 예시를 씁니다. 2025년 8월까지 리액션 좌표는, 댓글이 나중에 외부 루트에 쓰는 것과 같은 식별자 문법으로 팟캐스트 에피소드나 웹 페이지를 지목할 수 있게 되었습니다.

### 2026년 8월

이번 8월은 일반 답글을 쓰는 클라이언트에 댓글 스레드를 들여왔습니다. 나중에 병합된 [6월 수정](/ko/newsletters/2026-06-24-newsletter/#kind-1111-as-reply-to-kind-1-notes)은 짧은 노트에 NIP-22 댓글을 쓰지 말라고 클라이언트에 지시했던 줄을 없앴습니다. 이어 [NIP-30](/ko/topics/nip-30/)(사용자 지정 이모지)이 노트, 리액션, 사용자 상태와 나란히 [kind 1111을 추가](https://github.com/nostr-protocol/nips/pull/2448)해, 댓글도 그 다른 kind들이 이미 쓰던 같은 이모지 tag를 담을 수 있게 되었습니다. 사양 작업은 허용입니다. 클라이언트 작업은 실제 적용입니다.

웹 클라이언트 [Snort](https://github.com/v0l/snort/commit/420ed60e2ff43bd373f2583e171a77002ec9f3a0)는 이제 kind 1 대상에 대해 기본으로 NIP-22 댓글을 게시하고, 대문자 `E`/`A` 루트 tag로 스레드를 구독하며, 알림에서 kind 1111을 받아들입니다. 커뮤니티 웹 클라이언트 [Ditto](https://github.com/soapbox-pub/ditto/commit/8a0ffc6e3a5d9202ffc452fa0de8ae33b5883384)는 kind 1 노트에 대한 답글까지 포함해 모든 답글을 NIP-22 댓글로 게시하며, 텍스트는 kind 1111, 음성은 1244로 하면서 [NIP-10](/ko/topics/nip-10/)(노트 스레드) 답글도 계속 읽습니다. 여섯 해의 이동은 그 기본값에서 보입니다. 2022년은 리액션을 일반화했고, 2023년과 2024년은 좌표에 이름을 붙였으며, 2025년은 리액션을 네트워크 밖으로 향하게 했고, 2026년은 댓글을 그 같은 대상들에 대한 공통 답글 이벤트로 만들었습니다.

비공개 그룹 기반은 복구를 상호운용성 요건으로 정의하고 있었습니다. Marmot의 [8월 13일 지속성 및 재시작 계약](https://github.com/marmot-protocol/marmot/commit/4a2bc65f8db5866cec3b2a127dedb37818eaf207)은 어떤 로컬 MLS 및 게시 상태가 재시작을 견뎌야 하는지 규정하고, 클라이언트가 그룹 작업을 계속하기 전에 보존된 상태를 대조하도록 요구합니다. 이는 8월의 흐름을 대상을 지목하는 것 너머로 넓힙니다. 성숙한 클라이언트는 중단 뒤에 안전하게 이어가기에 충분한 암호 및 전달 상태도 보존해야 합니다. 공통 이벤트 형태는 구현이 그것을 쓰는 데 필요한 상태를 복구할 수 있을 때만 쓸모가 있습니다.

---

[Nostr Compass 프로젝트](https://github.com/andotherstuff/nostr-compass)를 통해 프로젝트나 소식을 공유하려면 [NIP-17](/ko/topics/nip-17/) DM을 보내주세요.
