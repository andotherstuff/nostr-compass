---
title: "Nostr Compass #38"
date: 2026-09-02
publishDate: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
description: "Voca 1.0이 오프라인 음성 변환 앱에 검증된 Nostr 읽기를 도입하고, nostream이 relay 측 작업 라우팅과 인증을 확장하며, Napstr가 Tor 기반 오디오 카탈로그를 게시하고, MDK 0.9.17이 그룹 유지 비용을 줄이며, 핵심 NIP에 페이지네이션 힌트와 하이라이트 tag가 병합되고 NWC에 거래 합계가 추가되며, NIP 심층 분석은 재게시와 리액션을 설명합니다."
---

[Nostr Compass](https://nostrcompass.org)에 다시 오신 것을 환영합니다. Nostr의 주간 안내서입니다.

**이번 주:** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0이 기사 내용을 소리 내어 읽어 주는 오프라인 Android 리더에 검증된 Nostr 노트와 장문 구독을 도입하고, [nostream](https://github.com/cameri/nostream)이 relay 측 작업 라우팅과 인증된 운영을 확장하며, [NDK for Dart](https://github.com/relaystr/ndk)가 negentropy와 다중 relay 요청 수명을 고치고, [Divine Mobile](https://github.com/divinevideo/divine-mobile)이 wrap된 메시지 삭제와 서명을 결정론적으로 만들며, [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay)가 기본적으로 gift wrap inbox를 보호하고, [Amethyst](https://github.com/vitorpamplona/amethyst)가 이동 가능한 하이라이트를 출시하며, [Mostro](https://github.com/MostroP2P/mostro)가 spam 게이트 전에 서명된 주문을 검증합니다. [Napstr](https://github.com/lnbits/napstr)는 Nostr를 통해 오디오 카탈로그와 seeder heartbeat를 게시하면서 Tor로 파일을 전송합니다. 릴리스는 [MDK](https://github.com/marmot-protocol/mdk)와 [pakstr](https://git.nostrdev.com/stuff/pakstr)를 다룹니다. 프로토콜 작업에서는 [NIPs 저장소](https://github.com/nostr-protocol/nips)에 [NIP-67](/ko/topics/nip-67/) 페이지네이션 힌트와 [NIP-84](/ko/topics/nip-84/) 하이라이트 tag 방식을 병합하고, [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc)에 거래 합계를 추가합니다. NIP 심층 분석은 재게시와 리액션의 event 형태와 현재 구현을 따라갑니다.

## 주요 소식

### Voca 1.0이 검증된 Nostr 노트와 구독을 Android에서 소리 내어 읽다

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)는 기사, PDF, Markdown 파일, Nostr 노트를 휴대폰 자체의 음성 변환 목소리로 읽으며 현재 읽는 문장을 페이지에서 계속 강조하는 오프라인 Android 리더입니다. 자체 [프로젝트 키](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu)로 [2026-08-27에 게시된](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) [1.0 릴리스](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)는 Nostr를 일급 소스로 만듭니다. 노트 주소, event 식별자, npub, 프로필, 또는 내부에 Nostr 엔티티가 있는 일반 웹 링크를 붙여 넣으면 앱이 참조를 해독하고 relay에서 서명된 event를 가져와 그 주위에 만들어진 웹 페이지가 아니라 작성자의 글을 읽습니다.

두 가지 검증된 동작이 Nostr 통합을 규정하며, 둘 다 [Voca의 서명된 1.0 공지](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)에 설명되어 있습니다. 첫째, 가져온 모든 event는 저장되기 전에 다시 계산한 id와 BIP-340 Schnorr 서명을 대조해 검사됩니다. 이때 부트스트랩 relay, 작성자의 [NIP-65](/ko/topics/nip-65/) relay 목록, 즉 작성자가 읽고 쓰는 relay를 나열하는 서명된 replaceable kind `10002` event, 그리고 참조 자체에 담긴 힌트를 사용합니다. 따라서 relay가 응답을 거부할 수는 있어도 작성자의 말을 바꿀 수는 없습니다. 둘째, 작성자의 npub을 추가하면 그 작성자의 [NIP-23](/ko/topics/nip-23/) 장문 기사, 즉 제목·요약·이미지가 있는 addressable kind `30023` 게시물이 RSS 및 Atom 피드와 함께 기기 내 하나의 inbox에 들어갑니다. [2026-08-28에 발표](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca)되고 2026-08-29에 [Zapstore](https://zapstore.dev)에 게시된 1.1.0 업데이트는 문장 단위 스크롤의 타이밍을 맞추고, 긴 문서를 부드럽게 처리하며, 수동 스크롤·크기 변경·프로세스 재시작·업그레이드 뒤에도 홈 화면 위젯을 복구합니다.


### nostream이 relay 측 DVM 라우팅과 인증된 운영을 확장

[8월 19일의 작업 수집 기능](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes) 이후, TypeScript relay 구현체 [nostream](https://github.com/cameri/nostream)은 [NIP-89 애플리케이션 handler event를 저장하고 제공합니다](https://github.com/cameri/nostream/pull/737). [NIP-89](/ko/topics/nip-89/)(애플리케이션 handler 탐색)는 kind `31989` 추천과 kind `31990` handler 정보를 사용합니다. 둘 다 이미 parameterized-replaceable 범위에 있으므로, 클라이언트가 이 kind들을 질의하면 `d` tag가 충돌할 때 대체본을 받을 수 있습니다. relay는 자체 worker의 handler 정보를 게시하지 않습니다.

대기 중인 [NIP-90](/ko/topics/nip-90/)(data vending machine) 작업은 이제 [worker 프로세스에 도달하고 결과 event로 돌아옵니다](https://github.com/cameri/nostream/pull/734). 성공하면 relay가 자체 키로 kind 6000-6999 결과에 서명합니다. 시간 초과나 worker 충돌이 발생하면 작업을 제출된 상태로 남기지 않고 실패로 표시합니다.

인증된 세션과 관리자 HTTP 호출은 서로 다른 경계에 있습니다. [NIP-42](/ko/topics/nip-42/)(relay에 대한 클라이언트 인증)는 [socket마다 인증된 pubkey를 추적](https://github.com/cameri/nostream/pull/716)하고, 클라이언트가 event를 게시하기 전에 AUTH를 요구할 수 있으며, [NIP-11](/ko/topics/nip-11/)(relay 정보) 문서에서 이 요구 사항을 알립니다. 두 제어 기능은 기본적으로 꺼져 있습니다. 별도로 [관리자 API 경로는 NIP-98 서명 HTTP 인가를 받을 수 있습니다](https://github.com/cameri/nostream/pull/730). [NIP-98](/ko/topics/nip-98/)(서명된 event를 이용한 HTTP 인증)는 운영자가 이를 활성화하고 허용할 pubkey를 지정할 때까지 꺼져 있습니다.

### NDK for Dart가 negentropy, 다중 relay 요청 수명, 서명 검증을 수정

Nostr용 Dart 개발 키트 [NDK](https://github.com/relaystr/ndk)에서 [NIP-77](/ko/topics/nip-77/)(negentropy 집합 조정)을 실행하면 오류 없이 잘못된 have 및 need 집합이 반환되었습니다. codec이 [negentropy](/ko/topics/negentropy/) 프로토콜 v1을 사용하지 않았기 때문입니다. [v1 인코딩 수정](https://github.com/relaystr/ndk/pull/722)은 이제 relay가 가진 id와 여전히 필요한 id를 반환합니다.

서로 다른 relay에 보낸 동일한 필터가 [하나의 요청으로 합쳐지고 있었습니다](https://github.com/relaystr/ndk/pull/705). 같은 필터를 가진 요청도 대상 relay나 수명이 다르면 이제 서로 구분되므로, 짧은 질의가 다른 relay의 event를 결과에 섞거나 살아 있는 subscription을 멈춘 채로 두지 않습니다.

같은 키트는 [서명을 한 번 검증하고 그 결과를 유지합니다](https://github.com/relaystr/ndk/pull/726). 나중에 중복으로 전달되어도 다시 검사하는 비용을 쓰거나 저장된 검증 완료 event를 덮어쓰지 않습니다.

### Divine Mobile이 wrap된 다이렉트 메시지 삭제와 서명을 결정론적으로 만들다

메시지를 대상으로 한 wrap된 [NIP-09](/ko/topics/nip-09/)(event 삭제 요청) kind `5` event가 Nostr를 통해 게시하는 모바일 짧은 동영상 클라이언트 [Divine Mobile](https://github.com/divinevideo/divine-mobile)에서 적용되지 않았습니다. 이제 클라이언트는 리액션이 아닌 것은 이미 처리됐다고 보는 대신 [각 삭제를 지목된 메시지에 대조해 처리합니다](https://github.com/divinevideo/divine-mobile/pull/8174). 첫 번째 요청이 아직 진행 중일 때 보낸 두 번째 [모두에게서 삭제 요청](https://github.com/divinevideo/divine-mobile/pull/8164)은 예전에는 오류도, wire의 kind `5`도 없이 사라졌지만, 이제 동시 삭제 요청이 각각 게시됩니다.

앞서 다룬 1.0.22 릴리스 이후에도 동일한 1:1 [NIP-17](/ko/topics/nip-17/)(gift wrap된 비공개 DM) 텍스트를 1초 안에 두 번 보내면 [하나의 rumor id가 만들어져](https://github.com/divinevideo/divine-mobile/pull/8163) 두 번째 전송이 사라졌습니다. 이제 각 전송은 [NIP-59](/ko/topics/nip-59/)(gift wrap) rumor 안에 token을 담아 id가 달라집니다.

kind `4` 또는 kind `5` event에 이미 서명한 호출자는 [그 서명을 유지합니다](https://github.com/divinevideo/divine-mobile/pull/8173). 예전처럼 나중에 client tag가 추가되어 id가 바뀌고 relay가 event를 유효하지 않다고 거부하지 않습니다.

### Conduit Relay가 NIP-42로 보호되는 inbox를 강화

Kind `1059` gift wrap은 수신자 한 명을 위해 저장됩니다. 이 wrap을 수신자 보호 inbox에 보관하는 Go relay [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay)는 [enforce 모드를 기본값으로 사용합니다](https://github.com/Conduit-BTC/conduit-relay/pull/8). kind `1059` 질의는 해당 수신자로서 [NIP-42](/ko/topics/nip-42/) 인증을 제시해야 하며, 그렇지 않으면 relay가 요청을 거부합니다. 이 wrap을 대상으로 한 여러 kind 혼합 필터, wildcard, count, [negentropy](/ko/topics/negentropy/)는 `restricted`이므로 다른 AUTH가 이를 타인의 inbox 전체를 가져오는 수단으로 바꿀 수 없습니다.

같은 [보호 inbox 병합](https://github.com/Conduit-BTC/conduit-relay/pull/8)은 전송된 AUTH event에 정규 event id가 있어야 한다고 요구하며, 그 밖에 유효한 NIP-42 event는 `content`가 비어 있는지와 관계없이 허용합니다. Challenge-only는 읽기를 막지 않으면서 AUTH를 계속 제공하고, disabled는 제한 없이 허용합니다. 라이브러리 기본값은 enforce입니다.

### Amethyst가 NIP-84 하이라이트를 출시하고 relay 관련 실패 경로 두 곳을 수정

지난주의 [Blossom 인가 작업](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads)에 이어 Android Nostr 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)는 [NIP-84](/ko/topics/nip-84/)(이동 가능한 하이라이트)를 포함한 [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0)을 출시했습니다. 선택한 구절은 composer, 하이라이트 피드, 또는 앱으로의 공유를 통해 kind `9802` event가 됩니다.

릴리스는 [NIP-29](/ko/topics/nip-29/) 채널 삭제 및 보관 제어([PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812))를 추가하고, 클라이언트가 이미 만드는 트래픽으로 relay 동작을 측정한 뒤 [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) probe를 streaming, 읽기, 쓰기, URL 검사로 확장합니다([PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836), [PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)). Amethyst는 SharedKeyCache 해시 충돌 취약점도 제거하고 메시지 인증 코드를 일정한 시간에 비교하며([PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)), 연결 시점의 AUTH 전달이 사라질 수 있는 race를 고치고([PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)), subscription 상태 잠금을 분산해 ANR 병목을 없애며([PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)), 첫 번째 필터만이 아니라 모든 subscription 필터를 비교합니다([PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)).

[Newsletter #36은 이 relay 인증, 백업, 공개 채팅 변경을 앞서 다뤘고](/en/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow), 이제 v1.14.0이 이를 함께 출시했습니다. Concord soft ban은 감사에서 발견된 권한 공백을 닫습니다([PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)). relay 인증은 권한 흐름을 다시 설계했고([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)), 시간 초과 대신 challenge 해결을 기다리며([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)), 새 계정의 기본값을 인증으로 정하고([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), 계정의 일반적인 집합 밖에 있는 relay에서도 그 설정을 지키며([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)), 재연결 뒤에도 세션 권한을 유지합니다([PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)). 안내형 최초 실행 및 설정 흐름은 키 백업을 찾기 쉽게 만들고([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)), Cashu proof backfill과 기록 페이지 나누기는 지갑 잔액이 잘리는 일을 막으며([PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)), 공개 채팅을 음소거할 수 있게 합니다([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)).

그 tag 이후, kind `30392`부터 `30395`까지의 [신뢰 목록](https://github.com/vitorpamplona/amethyst/pull/3983)은 [NIP-50](/ko/topics/nip-50/)(전체 텍스트 검색)에 제목만 색인되므로, 본문에 이름이 나온 목록을 구성원의 16진수 id까지 색인하지 않고 찾을 수 있습니다. [NIP-47](/ko/topics/nip-47/)(Nostr Wallet Connect)을 통해 도착한 지갑 거부는 이제 [탭이 아무 동작도 하지 않은 것처럼 보이는 대신 오류를 표시합니다](https://github.com/vitorpamplona/amethyst/pull/3987). `QUOTA_EXCEEDED`, `RESTRICTED`, 지갑이 응답하지 않을 때의 시간 초과도 포함됩니다.

### Mostro가 비용이 큰 작업 전에 서명된 주문을 검증하고 주문 감사 event를 보존

[v0.18.1의 Cashu escrow 기반](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon) 이후, Nostr를 통해 주문을 조율하는 피어 투 피어 거래 daemon [Mostro](https://github.com/MostroP2P/mostro)는 [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5)를 tag했습니다. 이 버전은 전송의 기본값을 [NIP-44](/ko/topics/nip-44/)(페이로드 암호화)로 정하고 gift wrap은 명시적인 선택 사항으로 유지합니다.

릴리스는 대기 상태 시간 초과를 기록된 인수 시점에 고정해 maker bond가 잘못된 시계 때문에 삭감되지 않게 하고([PR #879](https://github.com/MostroP2P/mostro/pull/879)), 결제 완료된 각 주문의 구매자 지급을 최대 한 번만 실행하며([PR #881](https://github.com/MostroP2P/mostro/pull/881)), 그 지급을 한계가 있고 차단하지 않는 `send_payment` 대기로 처리합니다([PR #883](https://github.com/MostroP2P/mostro/pull/883)). 시간 초과 삭감의 승자에게 지급하려던 변경([PR #875](https://github.com/MostroP2P/mostro/pull/875))은 같은 tag가 출시되기 전에 되돌려졌습니다([PR #885](https://github.com/MostroP2P/mostro/pull/885)). Mostro는 변경되지 않은 대기 주문서를 매시간 그리고 시작할 때 다시 게시하는 일도 중단하고([PR #888](https://github.com/MostroP2P/mostro/pull/888)), kind `38386` 분쟁 event에 이후 정렬을 위한 `created_at` tag를 넣습니다([PR #878](https://github.com/MostroP2P/mostro/pull/878)).

그 tag 이후에는 [서명 검사가 spam 게이트보다 먼저 실행됩니다](https://github.com/MostroP2P/mostro/pull/892). event id는 `sig`를 확정하지 않으므로, 깨진 서명이 붙은 피해자의 kind `14` 복사본이 재생 방지 자리를 차지하고 유효한 메시지를 조용히 버리게 할 수 있었습니다. 이제 daemon은 먼저 검증하고, 경고한 뒤 계속하는 대신 유효하지 않은 wrap을 버립니다.

kind `8383` 수수료 감사 event에는 15일의 [NIP-40](/ko/topics/nip-40/)(만료 타임스탬프)이 들어 있었습니다. 이제 공개 결제 기록이라는 역할에 맞게 [1년 만료를 유지합니다](https://github.com/MostroP2P/mostro/pull/924). Cashu가 활성화된 노드에서 주문을 인수하면 [Nostr를 통해 판매자에게 2-of-3 escrow를 잠그도록 요청](https://github.com/MostroP2P/mostro/pull/830)하고, 대기 주문 event를 게시하며, Lightning hold invoice 생성은 건너뜁니다. 이로써 요청 경로는 완성되지만, 그것만으로 모든 escrow 또는 시장 남용 사례가 해결되지는 않습니다.

### Napstr가 Nostr에 오디오 카탈로그를 게시하고 Tor로 파일을 전송

[Napstr](https://github.com/lnbits/napstr)는 Nostr에 검색 가능한 카탈로그와 활성 seeder를 게시한 뒤 직접 IP 대체 경로 없이 번들 Tor 프로세스로 파일을 전송하는 데스크톱 오디오 공유 클라이언트입니다. [버전 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0)은 프로필과 카탈로그 메타데이터를 공개로 유지하고, 요청·전송 자격 증명·파일 내용·피어 IP 주소는 relay에 올리지 않습니다.

탐색은 [Napstr 저장소](https://github.com/lnbits/napstr)에 정의된 두 addressable event kind를 사용합니다. kind `30421` 카탈로그 항목은 SHA-256 digest, 공개 basename, 크기, 오디오 형식으로 파일을 지정하고, 작성자는 해당 좌표를 삭제 표시로 대체해 파일을 철회합니다. kind `30422` 가용성 heartbeat는 10분 뒤 만료되며 작성자가 seed할 준비가 된 파일 id를 나열하므로, 만료되지 않은 heartbeat에 해당 digest가 아직 있을 때만 카탈로그 행이 활성 상태입니다.

공개 대화는 relay 소유 그룹 대신 [NIP-C7](/ko/topics/nip-c7/)(kind 9 채팅 메시지)을 사용합니다. [Napstr 저장소](https://github.com/lnbits/napstr)는 공유 공개 방과 파일 digest를 키로 삼는 트랙별 토론을 정의합니다. 이 메시지는 서명되어 공개됩니다. onion 주소, 전송 자격 증명, 파일 바이트는 담지 않습니다.

다운로드는 [NIP-17](/ko/topics/nip-17/)(gift wrap된 비공개 DM) 협상으로 시작합니다. [Napstr 저장소](https://github.com/lnbits/napstr)는 요청, 제안, 거절을 kind `14` rumor 안에 wrap하므로 relay는 임시 v3 onion 호스트 이름이나 수락된 제안이 반환하는 일회용 capability를 볼 수 없습니다. 이어 번들 Tor가 해당 onion을 통해 바이트를 옮기고, 전체 SHA-256 digest를 검증하며, 파일을 재생할 수 있게 되기 전에 오디오를 다시 검증합니다.

[v0.1.7과 v0.2.0 비교](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0)는 오디오북 모음과 선택적인 Android 동반 앱 Napstrfy를 추가합니다. kind `30423` manifest는 일반 카탈로그 파일로 유지되는 순서 있는 장을 나열하므로, 모음을 무시하는 클라이언트도 각 장을 가져올 수 있습니다. Napstr는 이를 위해 기존 내용을 파괴하지 않는 로컬 Audiobooks 폴더를 만듭니다. Napstrfy는 일회용 QR 코드로 실행 중인 데스크톱과 pair한 뒤, 데스크톱 비밀 키를 받지 않고도 데스크톱의 기존 Nostr 및 Tor 서비스를 통해 검색하고 다운로드를 요청합니다.

같은 [비교](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0)는 완료되지 않는 동반 앱 handshake에 시간 초과를 적용합니다. seeder는 바이트를 제공하기 전에 공유 파일을 복사하고 hash하며, 들어오는 데이터를 비공개 임시 파일에 쓰고, 오디오북 목적지를 실제 Napstr 폴더의 하위 경로로 제한하며, 전송 중 그 목적지가 바뀌면 중단합니다.

## 릴리스

### MDK v0.9.17: 최신 KeyPackage, 구성원 활동, 지속적 전송

[Newsletter #37은 MDK 0.9.14와 0.9.15를 다뤘습니다](/en/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles). 여기에는 [MDK 저장소](https://github.com/marmot-protocol/mdk)가 가장 오래된 KeyPackage부터 선택하던 방식에서 유효한 현재 프로필의 최신 package를 선택하도록 바꾼 것, epoch 차이 복구 게이트, 계정 정리, 탐색 relay와 운영 relay의 분리가 포함됩니다. 이 수정은 뒤이은 두 릴리스의 기반으로 남으므로, 사용할 수 있는 package를 이미 게시한 구성원을 오래된 package가 더는 막지 않습니다.

[구성원 및 관리자 event는 이제 새 메시지처럼 채팅 목록을 앞으로 옮깁니다](https://github.com/marmot-protocol/mdk/pull/1551). 사람이 참여하거나 나가거나 역할을 바꾸면 미리 보기 텍스트, 순서, 읽지 않은 수, 읽음 표시가 갱신되고, 로컬 시스템 actor는 Nostr 프로필로 취급되지 않습니다. 재연결과 재시작은 [재시도하는 지속적 발신 텍스트에 하나의 전송 신원을 재사용하므로](https://github.com/marmot-protocol/mdk/pull/1516), 같은 그룹 메시지가 두 번 게시되지 않습니다.

그 뒤의 두 릴리스는 큰 그룹을 건강하게 유지하는 비용에 집중합니다. [버전 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16)은 [high-water mark가 아니라 현재 epoch에서 epoch 차이를 측정](https://github.com/marmot-protocol/mdk/pull/1559)하고, 거부된 수신 event를 계속 가져올 수 있게 하며([PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)), replay rollback 범위를 정규 그룹 상태로 제한하고([PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)), UniFFI binding 위에 macro로 생성한 C ABI인 [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545)를 도입해 host가 engine을 직접 내장할 수 있게 합니다. 이어 [버전 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17)은 pass마다 구성원을 도는 대신 [한 번의 구성원 순회로 pass 승인 scan을 합치고](https://github.com/marmot-protocol/mdk/pull/1617), [전체 기록 graph를 seed하지 않고 그룹 상태의 경합 여부를 탐지하며](https://github.com/marmot-protocol/mdk/pull/1620), [지연 peel sweep의 유휴 poll 비용을 줄이고](https://github.com/marmot-protocol/mdk/pull/1621), [첫 pass가 빠뜨린 세 projection 지점에 일괄 component 읽기를 적용합니다](https://github.com/marmot-protocol/mdk/pull/1622). 대응하는 [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17)과 [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) artifact는 같은 commit에서 빌드되므로, 내장하는 쪽도 비용이 낮아진 유지 경로를 함께 받습니다.


### pakstr v0.16.0: 게시할 때 kind-32267 식별자 표시

[지난주의 0.13.0부터 0.15.0까지 Zapstore 게시 pipeline](/en/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit) 이후, 웹 앱을 서명된 Android APK로 package하고 Nostr 키로 게시하는 CLI [pakstr](https://git.nostrdev.com/stuff/pakstr)는 조회하거나 게시하거나 대체한 [kind `32267` 애플리케이션 event id를 log에 남깁니다](https://git.nostrdev.com/stuff/pakstr/pulls/67). 오래된 목록 메타데이터로 인해 다시 게시할 때 [버전 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0)은 이전 id와 새 id를 모두 출력하므로, 게시자는 relay에서 어떤 목록 event가 활성 상태인지 확인할 수 있습니다.

같은 [식별자 log](https://git.nostrdev.com/stuff/pakstr/pulls/67)는 대체하기 전에 조회에서 찾은 id를 기록하고, 이어 도착한 event의 id를 기록하므로, 아무 변경 없이 재사용하면 같은 id가 반복해서 나타납니다. 이것이 [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0)에 tag된 변경입니다. Content-Digest, 업로드 전 게시, 게시자 검증 동작은 이미 이전 tag에서 출시되었습니다.

## 미출시 변경 사항

### Zap Cooking이 bunker relay의 범위를 제한하고 유료 endpoint에 서명

Nostr 장문 event를 기반으로 만든 레시피 사이트 [Zap Cooking](https://github.com/zapcooking/frontend)에서 bunker 세션을 다시 불러오면, 예전에는 암호화된 [NIP-46](/ko/topics/nip-46/)(relay를 통한 원격 서명) 대화를 페이지가 이미 쓰는 모든 relay에 게시했습니다. 이제 [signer 트래픽을 bunker 자체 relay로 제한](https://github.com/zapcooking/frontend/pull/633)하며, 이 제한은 세션 복원과 signer가 시작하는 연결 흐름인 nostrconnect pair에 적용되어 bunker URL 로그인 경로와 일치합니다. 잘못 저장된 기록에서 빈 relay 집합을 설치하는 것은 거부하므로, 레시피만 host하는 relay는 같은 pubkey가 활성 bunker 세션을 유지한다는 사실을 더는 알 수 없습니다.

[서명된 HTTP 인증](https://github.com/zapcooking/frontend/pull/630)은 이제 [NIP-98](/ko/topics/nip-98/)(서명된 Nostr event를 이용한 HTTP 인증)에 따라 유료 요리 도우미 채팅, 요리책 소개, 접근 제한 레시피 업데이트를 보호합니다. 서버는 요청 본문을 한 번 읽고 정확히 그 페이로드를 대조해 서명을 검증하며, 본문에 제공된 공개 키 대신 검증된 auth event에서 신원을 가져옵니다. 채팅 미리 보기는 header 없이도 계속 작동하지만, header가 있으면서 서명이 유효하지 않으면 거부되고 요리책 소개에는 항상 서명이 필요합니다. 접근 제한 레시피를 업데이트하려면 검증된 키가 저장된 작성자와 일치해야 합니다. 그 밖의 사람에게는 레시피가 없다고 알려 endpoint가 어떤 유료 기록이 있는지 확인해 주지 않습니다.

### nostrord가 wrap된 DM과 공유 event 링크를 수정

지난주의 [v2.9.0](/en/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media) 이후, relay host 커뮤니티용 크로스플랫폼 클라이언트 [nostrord](https://github.com/nostrord/nostrord)는 한 기기에서 보낸 [NIP-17](/ko/topics/nip-17/)(gift wrap된 비공개 DM)이 같은 계정의 다른 기기에 도달하도록 전달 문제를 수정했습니다. [보낸 사람의 자체 사본을 독립적으로 게시](https://github.com/nostrord/nostrord/pull/295)하면 수신자 wrap이 첫 relay에서 수락됐다는 이유로 다른 기기가 가져올 사본이 누락되지 않습니다. 같은 변경은 [NIP-42](/ko/topics/nip-42/)(relay에 대한 클라이언트 인증)가 완료된 뒤 wrap을 다시 보내며, 첫 relay가 수락하면 전송 성공으로 표시해 host 하나의 실패가 나머지를 멈추지 않게 합니다. [NIP-59](/ko/topics/nip-59/)(gift wrap) 복호화에 실패해 보류된 [gift wrap 재시도](https://github.com/nostrord/nostrord/pull/297)는 이제 timer에 따라 실행되므로, 계속 연결된 bunker가 그 메시지를 누락된 채로 남겨 두지 않습니다... [잘림]

[NIP-C7](/ko/topics/nip-c7/)(kind `9` 채팅 메시지) 답글은 `q` tag 옆에서 부모를 선두 [NIP-19](/ko/topics/nip-19/)(bech32로 인코딩된 엔티티) `nevent` 포인터로 반복합니다. 본문을 열 때 해당 포인터가 답글 부모를 지목한다면 [선두 부모 포인터를 제거](https://github.com/nostrord/nostrord/pull/292)하여 행이 답글 인용 하나로 렌더링되게 합니다. 본문 중간의 포인터나 본문 전체인 포인터는 계속 인용 카드로 렌더링됩니다. [인용된 event 링크는 이제 `nevent`를 인코딩](https://github.com/nostrord/nostrord/pull/293)하면서 작성자, kind, 인용을 읽은 relay를 포함하므로, DM으로 공유한 [NIP-29](/ko/topics/nip-29/)(relay 관리 그룹) event를 다른 클라이언트가 조회 힌트 없는 맨 note 식별자 대신 가져올 수 있습니다.

## NIP 업데이트 및 프로토콜 사양 작업

### Nostr 구현 가능성

이번 주 핵심 [NIPs 저장소](https://github.com/nostr-protocol/nips)에 사양 변경 두 건이 병합되었습니다.

[NIP-67](/ko/topics/nip-67/)은 클라이언트가 페이지네이션을 계속할지 알 수 있도록 relay가 `EOSE`(저장된 event의 끝) 메시지에 붙일 수 있는 힌트를 정의합니다. [병합된 `"auth"` 힌트](https://github.com/nostr-protocol/nips/pull/2371)는 `finish`와 `more`에 세 번째 값을 더합니다. relay는 사용자가 인증하면 저장된 event가 더 보일 수 있음을 이제 알릴 수 있고, 힌트를 담은 `EOSE`보다 먼저 [NIP-42](/ko/topics/nip-42/)(relay 인증) `AUTH` challenge를 보내야 합니다. [함께 추가된 NIP-42 내용](https://github.com/nostr-protocol/nips/pull/2371)은 클라이언트 측에서 같은 흐름을 정의하므로, `auth`가 있는 `EOSE`를 받은 클라이언트에는 응답에 필요한 challenge가 이미 있습니다.

[NIP-84](/ko/topics/nip-84/)(이동 가능한 하이라이트, 위에서 Amethyst가 지원을 출시한 kind `9802` event)는 [tag 방식 업데이트를 병합했습니다](https://github.com/nostr-protocol/nips/pull/2454). 이제 하이라이트는 Nostr event용 `a`/`e` tag와 그 밖의 모든 대상용 `r` tag 외에도 [NIP-73](/ko/topics/nip-73/)(외부 콘텐츠 식별자)에 따른 구조화된 `i` tag로 출처를 표시할 수 있습니다. 인용 하이라이트를 인용 재게시처럼 렌더링하라는 요구도 MUST에서 SHOULD로 바뀌었습니다.

### Nostr Wallet Connect

`list_transactions` 응답은 현재 페이지가 반환한 행 수가 아니라 요청과 일치하는 거래 수를 보고할 수 있습니다. [NWC 확장 저장소](https://github.com/nostr-wallet-connect/nwc)의 NWC-05(지갑 기록 확장)에 [병합된 선택적 `total_count`](https://github.com/nostr-wallet-connect/nwc/pull/4)는 [NIP-47](/ko/topics/nip-47/)(Nostr를 통한 암호화된 원격 지갑 제어)과 함께 쓰이는 응답에 이 필드를 추가합니다.

[`total_count`를 추가한 commit](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67)은 이를 선택적 정수, 즉 요청 필터와 일치하는 전체 거래 수로 문서화합니다.

[페이지네이션을 합계에서 제외한 commit](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e)은 이 합계가 페이지네이션을 제외한다고 밝히므로, 모든 페이지에 걸쳐 일치하는 거래를 셉니다.

## NIP 심층 분석: 재게시와 리액션

연락처는 기존 노트를 자신의 follower에게 다시 보여 줄 수 있고, 답글을 쓰지 않고도 간결한 좋아요, 싫어요, 이모지를 붙일 수 있습니다. [NIP-18](/ko/topics/nip-18/)(재게시)은 그 재배포를 자체 서명 event로 게시합니다. [NIP-25](/ko/topics/nip-25/)(리액션)는 간결한 반응을 별도의 서명 event로 게시합니다. 둘 다 [정규 재게시 사양](https://github.com/nostr-protocol/nips/blob/master/18.md)과 [정규 리액션 사양](https://github.com/nostr-protocol/nips/blob/master/25.md)에서 `draft` `optional` 파일로 남아 있습니다. NIPs 저장소에 있고 클라이언트가 구현했지만, 여전히 최종본이 아니라고 표시되어 있습니다.

### 재게시(NIP-18)

클라이언트가 kind 6 event를 쓰면 follower는 누군가 이미 게시한 kind 1 텍스트 노트를 가리키는 서명된 포인터를 받습니다. [재게시 사양](https://github.com/nostr-protocol/nips/blob/master/18.md)은 `kind`를 6으로 정하고, 해당 노트의 문자열화한 JSON을 `content`에 넣으며, 빈 `content`는 허용하지만 권장하지 않습니다. 또한 값이 노트의 `id`이고 세 번째 항목이 노트를 가져올 수 있는 relay URL인 `e` tag를 요구하며, 원래 작성자의 `pubkey`가 있는 `p` tag도 event에 포함해야 한다고 규정합니다(SHOULD). [NIP-70](/ko/topics/nip-70/)(보호된 event) event를 재게시할 때는 보호된 페이로드가 새 event로 복사되지 않도록 `content`를 비워 두어야 합니다(SHOULD).

인용은 kind 6 wrapper가 아니라 다른 event 안의 인용입니다. 클라이언트가 [NIP-21](/ko/topics/nip-21/)(`nostr:` URI) `nevent`, `note`, `naddr`를 언급할 때는 그 언급을 `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]` 형태의 `q` tag로 바꿔야 합니다. [인용 재게시 tag](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts)는 이런 인용을 답글 thread에서 분리하고, 클라이언트가 게시물의 인용을 가져와 셀 수 있게 합니다.

Kind 6은 kind 1 노트용으로 예약되어 있습니다. kind 16 일반 재게시는 kind 1을 제외한 모든 event kind를 wrap할 수 있습니다. 안쪽 event의 문자열화한 kind를 값으로 하는 `k` tag를 포함해야 합니다(SHOULD). 안쪽 event가 replaceable이면 일반 재게시는 `kind:pubkey:d-tag` 좌표가 있는 `a` tag를 추가해야 합니다(SHOULD). 그 `a` tag가 없으면 재게시는 특정 버전 하나를 대상으로 하며 `content`에는 그 버전의 전체 JSON 문자열이 들어 있어야 합니다. [일반 재게시 규칙](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts)은 장문, addressable, 그 밖의 노트가 아닌 event가 kind 1인 것처럼 게시되는 일을 막습니다.

다음 kind 6 event는 조립 시점에 `wss://relay.damus.io`에서 복구한 실제 재게시입니다([event 열기](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)).

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

`kind`는 6이고, `e` tag는 재게시된 노트를 가리키며, `p` tag는 그 노트의 작성자를 식별하고, `content`에는 원래 kind 1 event가 문자열화한 JSON으로 들어 있습니다. relay에서 복구한 이 event에는 [NIP-18 사양](https://github.com/nostr-protocol/nips/blob/master/18.md)이 필수라고 표시한 relay 힌트가 없습니다. 이는 독자와 클라이언트가 실제 event를 검증하고 필드를 빠뜨리는 제작자를 허용해야 하는 이유를 보여 줍니다.

### 리액션(NIP-25)

게시물은 서명된 좋아요, 싫어요, 이모지를 답글 thread에 넣지 않고 모을 수 있습니다. [리액션 사양](https://github.com/nostr-protocol/nips/blob/master/25.md)은 그 표시를 kind 7 event로 정의하며, `content`에는 리액션 값이 반드시 들어가야 합니다(MUST). `+` 또는 빈 문자열은 좋아요나 추천으로 읽어야 합니다(MUST). `-`는 싫어요나 비추천으로 읽어야 합니다(MUST). 이모지 또는 [NIP-30](/ko/topics/nip-30/)(사용자 지정 이모지) shortcode는 좋아요나 싫어요로 읽어서는 안 되며(SHOULD NOT), 클라이언트는 해당 이모지를 게시물에 표시할 수 있습니다(MAY).

대상은 `content`에서 추론하지 않고 tag에 둡니다. 대상 event `id`로 설정된 `e` tag가 반드시 있어야 하며(MUST), 그 tag에는 relay 힌트를 포함해야 합니다(SHOULD). 추가 `e` tag는 권장하지 않으며, 있다면 대상 `id`가 마지막이어야 합니다. 대상 작성자의 `p` tag가 있어야 하며(SHOULD), `p` tag가 여러 개면 마지막이어야 합니다. addressable 대상에는 `kind:pubkey:d-tag` 좌표가 있는 `a` tag도 있어야 합니다(SHOULD). `e` 및 `a` tag에는 relay와 pubkey 힌트를 포함해야 하고(SHOULD), `p` tag에는 relay 힌트를 포함해야 하며(SHOULD), `k` tag에는 리액션 대상 event의 문자열화한 kind를 넣을 수 있습니다(MAY). [이 tag 규칙](https://github.com/nostr-protocol/nips/blob/master/25.md#tags)을 통해 클라이언트는 리액션 event만으로 대상을 가져오고 작성자에게 알릴 수 있습니다.

클라이언트는 `content`에 단일 `:shortcode:`를 넣고 그 shortcode를 이미지 URL에 대응시키는 `emoji` tag 하나를 넣을 수 있으며(MAY), 이는 [사용자 지정 이모지 리액션 규칙](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction)을 따릅니다. 대상이 Nostr 고유 event가 아니면 리액션은 kind 17이어야 하고(MUST), [외부 콘텐츠 리액션 규칙](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions)처럼 [NIP-73](/ko/topics/nip-73/)(외부 콘텐츠 id) `k`와 `i` tag를 담아야 합니다(MUST). kind 17은 웹사이트, 팟캐스트 에피소드, 그 밖의 외부 객체에 대한 리액션입니다. kind 7 event 간 리액션도 아니고 재게시도 아닙니다.

다음 kind 7 event는 조립 시점에 `wss://relay.damus.io`에서 복구한 실제 리액션입니다([event 열기](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)).

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

`content`는 `+`이며, [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md)의 일반적인 좋아요입니다. `e` tag는 리액션 대상 event를 지정하고, `a` tag는 addressable 좌표를 추가하며, `p` tag는 작성자를 식별하고, 선택적인 `k` tag는 대상의 kind를 문자열로 기록합니다.

### 현재 클라이언트 구현

Android Nostr 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)는 현재 프로토콜 계층에 [재게시 event 유형](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt)과 [리액션 event 유형](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt)을 정의합니다.

웹 Nostr 클라이언트 [Snort](https://github.com/v0l/snort)는 [인용 링크 tag 처리를 포함하는 NIP-18 helper](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts)를 구현하고 [NIP-25 event 리액션 tag를 생성합니다](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

Mastodon 서버와 Nostr relay를 겸하는 [Ditto](https://github.com/soapbox-pub/ditto)는 [addressable 대상에 `k` tag와 `a` 좌표가 있는 kind 16 일반 재게시를 게시](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx)하고, [마지막 `e` tag를 대상 event로 취급해 kind 7 리액션 의미를 적용합니다](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### 함께 작동하는 방식

kind 6 또는 kind 16 event는 기존 event의 JSON을 포함하거나 replaceable 좌표를 가리켜 재게시자의 follower 피드에 기존 event를 다시 배포합니다. `q` tag는 다른 event 안의 인용을 표시하므로, [인용 재게시 절](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts)이 구분한 대로 thread 재구성 과정에서 인용 event를 답글로 취급하지 않고 인용을 셀 수 있습니다. kind 7 event는 원래 event를 그대로 두고 리액션 값과 대상 tag만 붙이며, 이는 [리액션 사양](https://github.com/nostr-protocol/nips/blob/master/25.md)의 계약입니다. 따라서 하나의 pubkey를 가져오는 클라이언트는 해당 pubkey의 재게시를 새로운 kind 6 또는 16 event로 보고, 그 pubkey의 의견을 다른 사람의 게시물에 붙은 kind 7 event로 봅니다.

---

[Nostr Compass 프로젝트](https://github.com/andotherstuff/nostr-compass)를 통해 프로젝트나 소식을 공유하려면 NIP-17 DM을 보내주세요.
