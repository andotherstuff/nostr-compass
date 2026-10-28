---
title: "Nostr Compass #46"
date: 2026-10-28
publishDate: 2026-10-28
translationOf: /en/newsletters/2026-10-28-newsletter.md
translationDate: 2026-10-28
draft: false
type: newsletters
description: "Mostro가 서명된 신원 재바인딩을 추가하고, Amethyst 1.20.0이 비공개 Marmot 그룹 투표와 암호화된 설정 동기화를 도입했으며, swift-nostr 0.9.0이 출시되었습니다. 또한 여섯 번의 Nostr 10월을 되돌아봅니다."
---

이번 주에는 **Mostro**가 [서명된 신원 재바인딩](https://github.com/MostroP2P/mostro/pull/1035)을 추가했습니다. **Amethyst**는 Marmot 그룹에 [비공개 투표](https://github.com/vitorpamplona/amethyst/pull/4630)를, 기기 간에는 [암호화된 설정 동기화](https://github.com/vitorpamplona/amethyst/pull/4613)를 도입했습니다. **swift-nostr**는 [공개 키가 서명자의 공개 키와 일치하지 않는 event에는 서명을 거부하는 검사](https://github.com/yysskk/swift-nostr/pull/239)를 출시했습니다. 마지막으로 2021–2026년, 여섯 해에 걸친 Nostr의 10월을 돌아보며 마무리합니다.

## 주요 소식 {#top-stories}

[commands-review]: https://github.com/nostr-protocol/nips/pull/2462 "Proposed previously, now merged"
[marmot-devices-review]: https://github.com/marmot-protocol/marmot/pull/442 "Proposed previously, now merged"
[cd-installed-merge]: https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157

### Mostro {#mostro}

Nostr로 조율되는 P2P 거래소 데몬인 [Mostro](https://github.com/MostroP2P/mostro)가 [0.20.1을 릴리스했습니다](https://github.com/MostroP2P/mostro/releases/tag/v0.20.1). 이번 버전은 [서명된 신원 재바인딩](https://github.com/MostroP2P/mostro/pull/1035)을 추가했는데, 이는 [지난주 호](/en/newsletters/2026-10-21-newsletter/#mostro)에서 아직 구현되지 않았다고 설명했던 기능입니다. 또한 이전에는 소스에만 있던 평판 내보내기 기능도 함께 제공합니다. 바인딩된 신원은 노드와 새 신원을 명시한 일회용 승인에 서명하며, 이 승인은 최대 1시간 동안만 유효합니다. 데몬은 event ID를 기록한 뒤 compare-and-swap 방식으로 전환하므로, 서명이 실패하거나 경쟁에서 지더라도 아무것도 바뀌지 않습니다. 운영자는 인증 토큰과 사유를 요구하는, 감사 기록이 남는 루프백 전용 RPC도 사용할 수 있습니다. 재바인딩을 해도 이미 발급된 증명은 취소되지 않습니다.

이후 병합된 변경 사항은 릴리스에 포함된 것으로 확인되지 않았습니다. [옵트인 방식의 고정 USD 페그 제공자](https://github.com/MostroP2P/mostro/pull/1083)는 운영자가 활성화한 경우에만 Nostr `mostro-rates` 피드에 USDT, USDC, DOC를 추가합니다. 네트워크 제공자나 중계된 코인 시세가 이 기능을 암묵적으로 활성화하지는 않습니다. [후속 변경](https://github.com/MostroP2P/mostro/pull/1091)은 제공자와 그 설정 키의 이름을 `pegged`로 바꾸어, 릴리스되지 않았던 `stablecoins` 키를 대체합니다. 아울러 BTC, LBTC, RBTC를 sats 기준 1:1 고정 비율로 산정하고, 그 환율을 kind 30078 event로 게시합니다. 이렇게 설정된 페그 가정이 페그나 결제를 보장하지는 않습니다. 실시간 페그 확인은 이 메커니즘의 범위 밖에 있습니다. 이 제공자는 기본적으로 꺼져 있습니다. 주문은 여전히 허용 통화 설정에 따라 제한되며, 클라이언트, protocol-book, 페그 가드 작업은 별도로 진행됩니다. [이제 본드 타임락이 에스크로와 별도로 동작합니다](https://github.com/MostroP2P/mostro/pull/1085). 게시되는 주문 만료 시간에는 상한이 적용되고, 오더북의 주문 수락 기간은 본드가 만료되기 전에 닫힙니다. 기존의 144블록 메이커 본드는 업그레이드 시 만료되므로 해당 주문은 다시 생성해야 합니다. 진행 중인 거래와 Cashu 모드는 영향을 받지 않지만, 일부 운영자 설정에서는 본드 타임락을 조정할 때까지 데몬이 시작되지 않습니다.

### Nostr WoT 확장 프로그램 {#nostr-wot-extension}

웹 오브 트러스트 기능을 갖춘 브라우저 서명 도구인 [Nostr WoT 확장 프로그램](https://github.com/nostr-wot/nostr-wot-extension)이 [0.8.15](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.15)를 릴리스했습니다. 이 버전에는 사용자가 직접 굴린 주사위나 던진 동전에서 얻은 256비트 엔트로피로 복구 키를 생성하는 옵션이 추가되었습니다. 이 과정은 복구 문구를 표시하지 않는 격리된 탭에서 진행되며, 주사위 결과는 SHA-256으로 해시하고 동전 던지기 결과는 원시 비트로 그대로 사용합니다. 이제 relay에 연결할 수 없으면 온보딩이 시간 초과로 종료됩니다. [버전 0.8.16](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.16)은 [relay 인증(NIP-42)](/ko/topics/nip-42/)에 대한 상시 승인을 추가했습니다. 덕분에 사용자는 한 사이트의 모든 relay, 또는 연결된 모든 사이트에 대해 AUTH를 한 번만 승인할 수 있습니다([relay 인증 구현](https://github.com/nostr-wot/nostr-wot-extension/pull/47)). relay나 사이트에 대한 거부 설정은 이러한 승인보다 우선하며, 대기 중인 요청이 처리되기 전에 철회 여부를 다시 확인합니다. 넓은 범위의 승인은 항상 사용자가 명시적으로 선택해야 하며, [HTTP Auth(NIP-98)](/ko/topics/nip-98/)에는 결코 적용되지 않습니다. 대기열 상한은 5개로 유지되므로, 이를 넘는 요청은 여전히 실패한 뒤 재시도됩니다. [버전 0.8.18](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.18)은 가져오기와 복구를 키 형식을 감지하고 신원을 미리 보여 주는 하나의 흐름으로 통합했습니다. 호환되는 Nosskey 복구에서는 동일한 신원, 기존 계정, 원래의 패스키가 그대로 유지됩니다.

별도의 개발자용 SDK인 [nostr-wot-sdk](https://github.com/nostr-wot/nostr-wot-sdk)는 안정화된 identity 1.1 지원을 담은 [3.0.1](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%403.0.1)을 릴리스했습니다. Nosskey를 통한 경우를 포함해 패스키로 복구하면 원래의 pubkey가 유지되며, 이제 제공자, 복구, 서명 코드가 하나의 구현을 공유합니다([SDK 복구 및 제공자 소스](https://github.com/nostr-wot/nostr-wot-sdk/pull/22)). 지원 중단된 포워더 패키지도 여전히 작동하지만, 통합 개발자는 유지 관리되는 진입점으로 옮겨야 합니다.

### Amethyst {#amethyst}

Android 및 데스크톱용 Nostr 클라이언트인 [Amethyst](https://github.com/vitorpamplona/amethyst)가 [버전 1.20.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.20.0)을 릴리스했으며, 여기에는 [비공개 투표를 비롯한 Marmot 암호화 그룹 기능](https://github.com/vitorpamplona/amethyst/pull/4630)이 포함되었습니다. 구체적으로는 교체 가능한 비공개 투표, 암호화된 사용자 지정 이모지, 관리자에 의한 메시지 삭제 및 신고 기능, 그룹의 현재 epoch에 고정된 미디어가 있습니다. 작성자는 리뷰 이후 클라이언트 간 상호 운용성 검사를 다시 실행하지 않았으며, Android에서 이 변경 사항을 수동으로 테스트하지도 않았습니다. 같은 epoch 번호를 공유하는 경쟁 브랜치들의 캐시 키 문제는 아직 남아 있고, 암호화된 미디어 키가 사라지는 메시지보다 오래 남을 수 있습니다. [설정 동기화](https://github.com/vitorpamplona/amethyst/pull/4613)는 앱 설정 여섯 그룹을 암호화된 [NIP-78](/ko/topics/nip-78/) 데이터로 저장합니다. 키, 서명자, 지갑, 알림, 덱, 읽음 표시는 각 기기에 그대로 남습니다. 설정을 처음 수정하면 여섯 그룹이 모두 게시됩니다. 읽기 전용 계정은 설정을 로컬에만 보관하며, 서명 가능한 기기 두 대에서의 동작은 검증되지 않았습니다.

데스크톱 시스템 알림은 [알림 필터를 따르며](https://github.com/vitorpamplona/amethyst/pull/4650), 일회용 외부 gift wrap과 음소거된 DM은 건너뜁니다. [255바이트를 넘는 신뢰할 수 없는 `d` tag](https://github.com/vitorpamplona/amethyst/pull/4616)도 더 이상 오류를 일으키지 않습니다. [kind 조회](https://github.com/vitorpamplona/amethyst/pull/4600)는 연결된 relay와 계정의 검색 relay에만 질의하며, 각각 최대 200개의 event를 가져옵니다. 앱은 [Quartz의 Kite JSON 처리 방식을 사용해](https://github.com/vitorpamplona/amethyst/pull/4595) 프레임, event, 필터, 그리고 [NIP-46](/ko/topics/nip-46/) 및 [NIP-55](/ko/topics/nip-55/) 메시지를 다룹니다. 다만 이 두 프로토콜을 통한 서명은 기기에서 검증되지 않았습니다. 이후의 [라이브러리 분리](https://github.com/vitorpamplona/amethyst/pull/4654)를 통해 다른 클라이언트에도 필요할 Marmot 및 cordn 프로토콜 규칙이 공유 라이브러리로 옮겨졌습니다.

1.20.0 이후 병합되었으나 아직 릴리스되지 않은 소스는 [앱의 Marmot 수신 경로를 공유 라이브러리 위에서 실행합니다](https://github.com/vitorpamplona/amethyst/pull/4672). 복호화된 모든 메시지는 멱등적으로 저장됩니다. 참여 시점에 기준선을 기록하므로 첫 멤버십 변경에도 해당 행이 표시됩니다. 커밋보다 먼저 도착한 kind 445 메시지는 보류되었다가 나중에 다시 처리되며, 관리자 캐치업 과정에서는 대기 중이던 탈퇴가 커밋됩니다. `amy cordn migrate export`는 가져오기를 하거나 새 재개 명령을 실행할 때까지 기존 설치본의 세션 명령을 비활성화합니다. 작성자는 로컬 체크아웃을 대상으로 루프백 amy 테스트와 라이브러리 테스트를 실행했습니다. 하지만 실제 앱의 수신 경로를 수동으로 시험하거나 Marmot 상호 운용성 테스트 모음을 실행하지는 않았습니다. [호환성을 깨는 업데이트](https://github.com/vitorpamplona/amethyst/pull/4659)는 제안 단계인 [NIP-5D napplet 형식](/ko/topics/nip-5d/)을 변경하여, napplet 매니페스트 해시를 기존의 경로 집계 대신 하나의 `/index.html` 아티팩트로 읽도록 했습니다. 따라서 레거시 번들은 다시 게시해야 합니다. 사용할 수 없는 필수 NAP 도메인은 fail-closed 방식으로 차단되고, 선택적 도메인은 없는 상태로 유지됩니다. 아이콘은 해시 및 디코더 검사를 거치고, 저장소는 매니페스트 kind, 아티팩트, 스냅샷별로 분할되며, 리소스 blob은 정규 base64를 사용합니다. 기기 수동 테스트, 클라이언트 간 테스트, 실제 relay 게시는 수행되지 않았습니다.

[외부 서명자에서 발생한 거부](https://github.com/vitorpamplona/amethyst/pull/4669)가 이제 보호 처리가 없던 코루틴 전반에서 처리되므로, 더 이상 앱이 충돌하지 않습니다. [PressStr 전자책, 잡지, 개별 호](https://github.com/vitorpamplona/amethyst/pull/4662)(kind 33953, 34609, 39731)도 이제 렌더링됩니다. PDF는 앱 내 리더에서 열리고, EPUB은 시스템 핸들러로 넘겨집니다. 카드에는 파일 형식과 크기가 표시되고, 미리 보기만을 위해 대용량 PDF를 내려받는 일은 없으며, 개별 호는 해당 잡지의 작성자에게서만 가져옵니다. 작성자는 이 변경 사항에 대한 Android 기기 테스트를 보고하지 않았습니다. 리치 미리 보기가 꺼져 있으면 [인보이스와 LNURL이 결제 버튼 없이 복사 가능한 간결한 라벨로 표시되며](https://github.com/vitorpamplona/amethyst/pull/4663), 인보이스 카드에는 이제 만료 시간이 표시됩니다. `amy gift wrap`는 [이제 seal과 wrap의 시각을 서로 다른 무작위 시각으로 설정하며](https://github.com/vitorpamplona/amethyst/pull/4661), 각각 최대 이틀 전까지 거슬러 올라갑니다. `--no-backdate`는 이 동작을 끕니다. 일반 DM 경로는 Quartz에서 별도로 수정됩니다. 데스크톱에서는 [각 동영상 카드가 자체 재생을 관리하므로](https://github.com/vitorpamplona/amethyst/pull/4660), 같은 URL을 가진 카드들이 더 이상 서로의 동영상을 가로채지 않습니다. 작성자는 이를 macOS에서 테스트했지만, 콜드 캐시 상태에서는 테스트하지 않았습니다. [제안된 Windows 링크 수정](https://github.com/vitorpamplona/amethyst/pull/4666)은 rundll32를 전체 경로로 호출해 링크를 열고, AWT로 폴백합니다. 근본 원인은 재현되지 않았으므로, 이는 확인된 수정이 아니라 유력한 수정입니다.

### Myco, 암호화된 napplet 저장소와 서명된 업데이트 알림 추가 {#myco-adds-encrypted-napplet-storage-and-signed-update-notices}

Nostr napplet을 위한 Android 호스트인 Myco가 0.12.0과 [0.12.1](https://github.com/Origami74/myco/releases/tag/v0.12.1)을 출시했습니다. 이제 napplet은 런타임을 통해 [NIP-44](/ko/topics/nip-44/) [자기 자신에게 암호화한 데이터](https://github.com/Origami74/myco/pull/152)를 저장할 수 있습니다. 하지만 relay, outbox, mesh 읽기 권한을 가진 앱은 평문을 볼 수 있으므로, 이 데이터는 앱별로 격리되지 않습니다. 이전에 Amber로 로그인한 사용자는 새로운 암호화 및 복호화 권한을 부여하려면 다시 로그인해야 합니다. 업데이트 알림은 고정된(pinned) 게시자가 서명하며, 이미 0.12를 실행 중인 기기에만 전달됩니다. 온라인 상태에서 Myco는 Zapstore를 매일 확인하고 Circle도 확인할 수 있으며, 메시 전용 모드에서는 Circle에만 문의합니다. 이 방식은 [초기의 일시 중지 방식](https://github.com/Origami74/myco/pull/151)을 대체합니다. 명시적으로 선택한 로컬 Blossom 레일은 서버 없이 파일을 기기에 보관하며, 앱당 하루 최대 64 MiB까지 지원합니다. 승인된 기본 서버로의 업로드가 실패한 경우에도 로컬 사본이 보관됩니다. 두 경로 모두 EXIF 메타데이터를 제거하지 않습니다. 이번 릴리스들은 Android TV 지원과, 사용자가 직접 파일을 선택하는 NAPFS 파일 선택기도 추가합니다.

## 태그 릴리스 {#tagged-releases}

### Monostr {#monostr}

Android용 Nostr 소셜 클라이언트인 [Monostr](https://github.com/schmidt1024/monostr)가 최신 버전인 [0.26.0](https://github.com/schmidt1024/monostr/releases/tag/v0.26.0)을 릴리스했습니다. 이제 최대 2분 길이의 동영상은 기기에서 압축되며, 위치 메타데이터도 제거됩니다. 탐색, 검색, 온보딩 화면에서는 선별된 팔로우 목록을 제공합니다. 스레드와 알림에는 이제 [NIP-22](/ko/topics/nip-22/) 댓글로 전송된 Fediverse 답글도 표시됩니다.

[0.25.0](https://github.com/schmidt1024/monostr/releases/tag/v0.25.0)의 기능도 그대로 유지됩니다. 답글의 상위 글이 없으면 앱은 답글의 relay 힌트와 상위 글 작성자의 relay를 검색하는데, 이는 사용자 자신의 목록에 없는 relay에 잠시 연결된다는 뜻입니다. 또한 기기의 네트워크가 바뀔 때마다 relay와 실시간 메시지 구독이 다시 연결됩니다.

### Sidecar {#sidecar}

Nostr 브라우저 확장 프로그램이자 서명 도구인 [Sidecar](https://github.com/dmnyc/sidecar)가 [1.16.3을 릴리스했습니다](https://github.com/dmnyc/sidecar/releases/tag/v1.16.3). 이제 작성기와 하이라이트 도구는 [계정 자체의 relay에 게시하고 event를 수신 확인한 relay만 집계한 뒤](https://github.com/dmnyc/sidecar/pull/545), 해당 relay로 연결되는 링크를 제공합니다. 수신 확인은 relay가 event를 받아들였다는 뜻일 뿐, 이를 계속 보관한다는 뜻은 아닙니다. 확장 작성기는 더 이상 설정의 기본 relay로 폴백하지 않습니다. 각 relay에는 개별적으로 12초의 제한 시간이 적용됩니다. 모든 relay에서 실패한 게시만 새 소켓으로 한 번 재시도됩니다. [투표 결과](https://github.com/dmnyc/sidecar/pull/544) 기능은 투표를 찾기 위해 공개 relay 네 곳에도 질의합니다. 태그 이후 병합된 변경 사항은 일반적인 relay 밖에 제출된 투표를 수집하기 위해 [relay를 하나 더 추가합니다](https://github.com/dmnyc/sidecar/pull/550). 실제 진행 중인 한 투표에서는 이 변경으로 집계가 21표에서 23표로 늘었습니다. 이는 투표 한 건의 결과일 뿐이며, 네트워크 전반에서의 집계 완전성에 대해서는 아무것도 말해 주지 않습니다. 집계는 여전히 1인당 투표 하나만 인정하고, 투표 마감 이후에 제출된 투표는 무시합니다. 앞서 나온 [1.16.1](https://github.com/dmnyc/sidecar/releases/tag/v1.16.1)은 상시 서명 승인을 이를 승인한 계정과 사이트로 제한하고, event에 d tag가 있는 경우에는 단일 addressable 레코드로 제한합니다. 승인은 암호화나 복호화에는 결코 적용되지 않습니다. 프로필, 팔로우 목록, 음소거 목록, relay 목록은 어떤 승인에도 포함되지 않습니다. 삭제, zap 요청, relay AUTH, 지갑 제어도 제외됩니다. 잠긴 확장 프로그램은 여전히 PIN을 요구합니다. 승인을 철회하거나 사이트 정보를 지우면 해당 승인과 승인 유효 기간이 함께 지워집니다.

별도의 [열린 pull request](https://github.com/dmnyc/sidecar/pull/552)는 CLINK offer 결제가 zap으로 집계되도록 하는 변경입니다. 이 변경은 changelog의 Unreleased 항목에 올라가 있으며, Debits는 구현하지 않습니다. offer 패널은 payer_data를 포함한 서명된 kind 9734 zap 요청을 전달하게 되며, 이를 통해 서비스가 kind 9735 영수증을 게시할 수 있게 됩니다. 영수증은 먼저 offer의 relay로, 그다음 수신자의 relay로 전송되며, 중복이 제거되고 최대 6개로 제한됩니다. 결제자의 relay는 사용되지 않습니다. offer가 code 3과 함께 디코딩 가능한 후속 offer로 응답하면, Sidecar는 새 요청과 새 서명으로 이를 한 번 따라가게 됩니다. 수신자의 프로필에는 결코 쓰지 않습니다. 이 변경 사항은 마감 시점까지 병합되지 않은 상태였습니다.

### Roadbeacon {#roadbeacon}

Roadbeacon은 이전에 Roadstr라는 이름을 썼던 위치 보고 클라이언트로, 독립적인 Roadstr 앱과는 별개입니다. 이 클라이언트는 새 event 형식을 갖춘 새 패키지로서 [새 이름으로 0.4.0을 출시했습니다](https://github.com/jooray/roadbeacon/releases/tag/v0.4.0). 이제 보고와 투표에는 상호운용 가능한 공유 kind 1315와 1316이 쓰이고, 좌표에는 정확히 재구성할 수 있는 정수 프레임이 사용되며, 웹 버전은 서명을 검증합니다. 이 패키지는 데이터를 마이그레이션하지 않고 기존 패키지와 나란히 설치됩니다. 이전 event는 relay에서 여전히 유효하지만, 새 클라이언트는 이를 읽을 수 없습니다.

### Jumble {#jumble}

Nostr 웹 클라이언트인 [Jumble](https://github.com/CodyTseng/jumble)이 [v26.10.1을 출시했습니다](https://github.com/CodyTseng/jumble/releases/tag/v26.10.1). 새 기능으로는 장문 아티클 편집기, 기기 간에 동기화되는 뮤트 단어, 시스템 알림, 그룹 및 Git 콘텐츠용 리더가 있습니다. 최근 호에서 다룬 게시 대기(pending-post) 및 레이아웃 변경 사항도 이번 릴리스에 포함되어 배포됩니다.

릴리스 이후 병합된 커밋은 [선택적인 NIP-22 답글 설정](https://github.com/CodyTseng/jumble/commit/ea798677d366ff750ac556d31c5628fe47ebd275)을 추가합니다. 이 설정은 기본적으로 꺼져 있으며 로컬 환경설정으로 저장됩니다. 설정을 켜면 kind 1 텍스트 노트에 대한 답글이 kind 1111 댓글로 전송됩니다. 기존 kind 1111 스레드는 루트를 그대로 유지하고, 다른 kind나 외부 콘텐츠에 대한 댓글도 kind 1111로 유지됩니다. 설정이 꺼져 있으면 답글은 기존 kind 1 동작을 따릅니다. 앱은 일부 클라이언트에서 이러한 댓글이 표시되지 않을 수 있다고 경고합니다.

### nostr-idb {#nostr-idb}

브라우저의 IndexedDB에 Nostr event를 캐시하는 라이브러리인 [nostr-idb](https://github.com/hzrd149/nostr-idb)가 [쿼리 수정 사항을 담은 5.1.1을 출시했습니다](https://github.com/hzrd149/nostr-idb/releases/tag/v5.1.1). 이제 교체 가능(replaceable) event와 주소 지정 가능(addressable) event에서도 정확한 ID 조회가 작동하며, 대기 중인 쓰기와 구독 기록을 포함한 모든 대상에 모든 필터 제약 조건과 필터별 limit이 적용됩니다. 캐시 정리(pruning)와 타임스탬프가 0인 event 관련 문제도 수정되었습니다. 메모리 내 캐시 크기인 `maxMemoryEvents`의 기본값은 `maxEvents`이며, 0으로 설정하면 캐시가 꺼집니다.

### Manent {#manent}

Nostr를 통해 동기화되는 암호화 노트북인 [Manent](https://github.com/dtonon/manent)가 [음성 메모 기능을 갖춘 3.0.0을 출시했습니다](https://github.com/dtonon/manent/releases/tag/v3.0.0). 녹음은 다른 노트와 마찬가지로 암호화된 상태로 동기화되며, 앱이 모델을 내려받은 뒤에는 Whisper로 오프라인에서 전사본이 생성됩니다. 앞서 소스 작업으로 다룬 relay 인증 복구 기능도 이번 릴리스에 포함되었습니다. 이 기능은 이제 Nostr Development Kit 라이브러리인 NDK의 0.10.1 버전을 통해 제공됩니다.

### NoorNote {#noornote}

데스크톱 및 웹 Nostr 클라이언트인 [NoorNote](https://github.com/77elements/noornote)가 노트와 다이렉트 메시지를 대상으로 하는 [기기 로컬 전문 검색을 갖춘 1.9.2를 출시했으며](https://github.com/77elements/noornote/releases/tag/v1.9.2), 캐시 전용 모드도 함께 제공합니다. [1.9.3 버전](https://github.com/77elements/noornote/releases/tag/v1.9.3)은 1.9.2에서 발생한 투명 유리(transparent-glass) 회귀로 읽기 어려워졌던 드롭다운, 메뉴, 토스트를 다시 읽을 수 있게 복원합니다. 이전에는 소스에만 있던 미래 타임스탬프 필터도 이번 릴리스들에 포함됩니다. 이제 로드에 실패한 프로필은 누락이 확인될 때까지 로딩 상태로 유지됩니다.

### Earthly {#earthly}

Nostr 지도 저작 클라이언트인 Earthly가 [relay 및 결제 수정 사항을 담은 0.1.22를 출시했습니다](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.22). 이제 relay 인증은 활성 계정에 연결됩니다. 복구된 구독과 카운트는 사용할 수 없는 카운트와 실제 0을 구분하며, 지도 리비전이 바뀌어도 카운트를 유지합니다. zap 합계는 실제 zap 영수증을 기준으로 산출되고, 앱은 지출하기 전에 지갑 동기화가 끝날 때까지 기다립니다. 실제 Nostr Wallet Connect 결제와 mint 결제는 아직 테스트되지 않았습니다([릴리스 통합](https://github.com/zeSchlausKwab/earthly/pull/36)).

### Chama {#chama}

Nostr event 기반 에스크로 거래 클라이언트인 [Chama](https://github.com/jesuspirate/chama)가 [6.4.31을 출시했으며](https://github.com/jesuspirate/chama/releases/tag/v6.4.31), 이 버전은 자금을 투입하기 전에 시드 백업을 확인합니다. 이 기기의 온체인 거래 키가 서명된 CREATE, JOIN 또는 예치 조건에 들어가기 전에, relay는 이 기기가 열었던(복호화했던) 서명된 시드 백업을 반환해야 합니다. 백업이 없거나, 폐기되었거나, 충돌하면 거래가 중단됩니다. 재시도할 때는 새 시드 없이 저장된 백업을 정확히 그대로 다시 전송합니다. 이 재조회는 그 시점의 가용성을 보여줄 뿐, 지속성을 보여주지는 않습니다. 이제 여러 단위로 구성된 리스팅은 수량 주문을 사용합니다. [6.4.30 버전](https://github.com/jesuspirate/chama/releases/tag/v6.4.30)은 구매자가 서명한 조건이 서명된 리스팅과 일치할 때만 스토어프론트 주문을 집계하고, 서명된 CREATE의 날짜가 2026년 12월 1일 또는 그 이후인 거래에서는 뒤늦게 도착한 외부인 event를 차단합니다. 그보다 이전 거래는 기존 만료 동작을 유지합니다([거래 만료 및 스토어프론트 검증](https://github.com/jesuspirate/chama/pull/77)).

저희 소스 기준 시점까지 병합되지 않은 열린 pull request는 [identity당 하나의 지갑 시드 백업](https://github.com/jesuspirate/chama/pull/92)을 허용하게 됩니다. 시작 시에는 페이지 내 큐와 Web Locks로 최초 생성을 직렬화한 다음, relay 상태를 다시 읽게 됩니다. 서로 다른 브라우저 사이에서는 그 재조회에만 의존합니다. 분산 잠금과 기존에 충돌하는 백업의 복구는 이 변경의 범위에 포함되지 않습니다. 저희는 어떤 자금 경로도 테스트하지 않았습니다.

### Linky {#linky}

Nostr를 통해 동기화되는 Cashu 지갑인 [Linky](https://github.com/linky-fit/linky)가 [26.10.7 버전](https://github.com/linky-fit/linky/releases/tag/linky-v26.10.7)과 [Android 26.10.8 빌드](https://github.com/linky-fit/linky/releases/tag/linky-v26.10.8)에서 플래그로 제어되는 실험적 온체인 전송 기능을 추가했습니다. 설정된 인간 운영자가 수수료를 받고 24시간 이내에 송금 및 수신 요청을 처리하므로, 전송은 원자적이지도 않고 신뢰가 필요 없는(trustless) 방식도 아닙니다. [조정 변경 사항](https://github.com/linky-fit/linky/pull/637)은 커스텀 Nostr 앱 메시지, [NIP-78](/ko/topics/nip-78/) 운영자 설정, 그리고 새로운 링크 동기화 범위를 사용합니다. 이 범위는 운영자의 대기 중인 ecash 송금을 동기화하여, 운영자의 다른 기기가 같은 송금을 두 번 지불하거나 환불하거나 정산하지 못하도록 합니다. 수신은 사용자의 지갑이 일치하는 Cashu 금액을 받았을 때에만 완료됩니다. 운영자와 사용자는 [NIP-65](/ko/topics/nip-65/) relay 목록이나 DM 인박스 목록이 아닌 권장 relay에서만 서로를 찾습니다. 따라서 공유 relay를 모두 잃으면 조정이 끊길 수 있습니다.

### LaWallet {#lawallet}

Nostr Wallet Connect 기반 지갑 및 계정 서비스인 [LaWallet](https://github.com/lawalletio/lawallet-nwc)이 [2.9.0 버전](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.9.0)과 [Android 1.2.0 베타](https://github.com/lawalletio/android-wallet/releases/tag/v1.2.0)를 출시했으며, 두 버전 모두 새 Nostr 로그인으로 옮겨 가는 NFC 카드 보조 복구 기능을 추가했습니다([네이티브 복구 흐름](https://github.com/lawalletio/android-wallet/pull/1)). 복구하려면 새로 수행되고 암호학적으로 검증된 카드 탭과, 15분 동안 유효한 일회용 복구 QR 코드가 필요합니다. 자산은 단일 트랜잭션으로 이동하고, 역할은 이전되지 않으며, 기존 OAuth 권한 부여는 취소되고, 기존 로그인은 빈 상태로 남습니다. 카드 복구는 기본적으로 켜져 있습니다. 계정 보유자는 보안 설정에서 이를 비활성화하고 아직 사용되지 않은 코드를 취소할 수 있습니다. 이제 연결할 수 없는 지갑은 잔액이 0으로 표시되지만, 이것이 지갑이 비어 있다는 뜻은 아닙니다. Android 베타는 보고 엔드포인트가 있는 빌드에서 이전에 옵트아웃했더라도 Sentry 오류 보고를 강제로 켭니다. 로컬 빌드와 F-Droid 빌드에는 엔드포인트가 없습니다.

태그 이후 병합된 소스에서는 잔액이 결제 금액을 충당할 경우 [카드 콜백이 NWC 정산 전에 OK를 반환할 수 있으므로](https://github.com/lawalletio/lawallet-nwc/pull/385), POS 시스템은 자체 인보이스를 직접 확인해야 합니다. [고정 결제 한도](https://github.com/lawalletio/lawallet-nwc/pull/388)가 잔액 기반 한도를 대체합니다. 저희 소스 기준 시점까지 병합되지 않은 열린 pull request는 설정된 제공자 또는 Nosskey 복구를 통해 다른 앱의 호환 패스키로 로그인할 수 있게 하며, 만료되는 임시 세션을 발급하기 전에 계정을 확인하게 됩니다([#386](https://github.com/lawalletio/lawallet-nwc/pull/386)). 제공자는 개인 키를 가져오지 않고도 서명할 수 있으며, 키 가져오기는 별도의 확인을 거치는 선택 사항입니다. 이 pull request의 스크린샷은 시뮬레이션된 데모 응답을 보여 줄 뿐, 실제 교차 출처(cross-origin) 로그인의 증거는 아닙니다.

역시 릴리스 포함 여부가 확인되지 않은 또 다른 병합은 NWC 및 Lightning 주소 콜백이 [make_invoice 오류 하나만으로 사용자의 원격 지갑을 교체하는 것](https://github.com/lawalletio/lawallet-nwc/pull/389)을 막습니다. 대신 활성 상태 및 잔액 확인을 거쳐 지갑을 유지하고 503을 반환할 수 있습니다. 서비스는 잔액과 보호 자금 상태도 기억하며, 복원(Restore) 옵션을 추가합니다. 다만 임계값과 알 수 없는 과거 이력 때문에 보호할 수 있는 범위가 제한되므로, 모든 자금의 안전을 보장하지는 않습니다. 배포가 이루어졌다거나 사용자 계정이 복원되었다고 주장하지는 않습니다.

### KithMoot {#kithmoot}

방 채팅과 통화를 위한 Nostr 기반 앱인 [KithMoot](https://github.com/forgesworn/kithmoot)은 이제 게시자의 공개 서비스 없이도 작동합니다. 10월 21일부터 23일 사이에 게시자는 [공개 회의 코드, 공유 TURN 서비스, 파일 업로드, 저장된 파일 읽기를 종료했습니다](https://github.com/forgesworn/kithmoot/pull/535). 초대 링크가 회의 코드를 대체합니다. 공개 파일은 기본적으로 Yakihonne를 사용하며 처음 보낼 때 안내가 표시되지만, 사용자는 자신의 서버를 직접 선택할 수 있습니다. 통화는 여전히 먼저 직접 연결을 시도합니다. 반면 IP 숨기기(Hide IP)는 작동하는 TURN 서버가 필요하며 절대 직접 연결로 대체되지 않습니다. 데스크톱 0.1.102와 Android 0.6.106에서는 [Cloudflare의 공개 STUN이 게시자의 STUN을 대체하며](https://github.com/forgesworn/kithmoot/pull/548), 사용자는 자신의 STUN을 설정할 수 있습니다. [서버에서 제공되던 백업 사본은 삭제되었지만](https://github.com/forgesworn/kithmoot/pull/543), [오프라인 암호화 사본은 남아 있습니다](https://github.com/forgesworn/kithmoot/pull/545). [데스크톱 0.1.109와 Android 0.6.121](https://github.com/forgesworn/kithmoot/pull/596)은 기기 자격 증명이 만료되면 초안을 유지한 채 채팅을 차단하고, 선택적인 디렉터리 조회와는 [별도로 사용자 자신의 프로필 이름을 읽습니다](https://github.com/forgesworn/kithmoot/pull/594). 일반 통화 엔진은 실험적인 [realtime SDK 프리뷰](https://github.com/forgesworn/kithmoot/pull/561)로 전환되지 않았으며, [MLS 그룹 후보](https://github.com/forgesworn/kithmoot/pull/583)는 기본적으로 꺼진 상태로 유지됩니다.

[데스크톱 0.1.110](https://github.com/forgesworn/kithmoot/releases/tag/v0.1.110)은 데스크톱과 웹에서 이미지, 오디오, 비디오, PDF를 위한 [샌드박스 첨부 파일 뷰어](https://github.com/forgesworn/kithmoot/pull/597)를 추가합니다. 데스크톱에서 이 뷰어들은 Node 접근, 애플리케이션 저장소, 외부 네트워크 접근이 모두 없는 전용 비영속 Electron 렌더러에서 실행됩니다. 스트리밍에는 제한이 적용되며, 뷰어는 닫히거나 메시지가 철회될 때 정리됩니다. pull request의 WebKit 실행과, 패키지 빌드를 대상으로 추가로 진행한 악성 SVG(hostile-SVG) 실행은 멈춰 버렸기 때문에 검증되었다고 주장하지 않으며, 이 중 어느 것도 보안 인증이 아닙니다. macOS 빌드는 공증(notarize)되었지만, Windows는 여전히 서명되지 않은 프리뷰입니다.

0.1.110에 포함된 것으로 확인되지 않은 이후의 병합은 절전 해제 후와 전송 전에 [만료된 기기 자격 증명을 실제 시계 시간(wall-clock) 기준으로 갱신하며](https://github.com/forgesworn/kithmoot/pull/605), 서명자가 응답하는 동안 초안을 유지합니다. 이 변경은 한 테스터의 자격 증명이 절전 중인 노트북에서 밤사이 만료된 일에 따른 것입니다. 응답이 끝내 돌아오지 않는 서명자 요청은 여전히 갱신을 열린 상태로 붙잡아 두며, Android에는 이와 별개로 해결되지 않은 갱신 공백이 있습니다. 저희 소스 기준 시점까지 병합되지 않은 열린 pull request는 [다른 사람의 연결 돕기(Help other people connect)를 일시 중지하게 됩니다](https://github.com/forgesworn/kithmoot/pull/606). 작성자에 따르면 앱이 미디어를 실어 나르지 않는 피어 지원 쌍을 수락할 수 있고, 이로 인해 포워더나 TURN으로의 대체가 막혀 소리가 나지 않는 통화가 남을 수 있습니다. 라이브러리 기본값은 변경되지 않은 채 유지됩니다.

### Marmot TS {#marmot-ts}

Marmot 암호화 그룹 메시징 프로토콜용 TypeScript 라이브러리인 [marmot-ts](https://github.com/marmot-protocol/marmot-ts)가 호환성을 깨는 변경 사항을 포함한 [v0.8.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/v0.8.0)과 [v0.9.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/v0.9.0)을 출시했습니다. 암호화 미디어 V2는 소스 바인딩을 추가하고 재시작 후 지연된 미디어를 복호화합니다. Blossom 업로드 디스크립터, 대상, 암호문은 서명 전에 검증됩니다. 저장된 그룹은 페이지 단위로 백필되며, 불확실한 커밋은 재시도합니다. 이제 앱은 실패하거나 시간 초과된 읽기를 거부하는 어댑터를 갖춘 영속적인 ingest 저장소와 rewind 저장소를 직접 제공해야 합니다. 레거시 V1 그룹은 다시 생성해야 하며, V1 헬퍼는 기록 조회용으로만 남아 있습니다.

이후 병합된 소스는 [key-package, 초대, 기록 감시자에 선택적인 AbortSignal을 제공합니다](https://github.com/marmot-protocol/marmot-ts/commit/bce57044f91251040807b1c0fd7a739046ee2f4e). 이 감시자들의 리스너는 저장소 읽기가 아직 대기 중이더라도 반환, 예외 발생 또는 폐기 시점에 즉시 정리됩니다. 소비자가 일시 중지된 동안 도착한 변경 사항은 래치되었다가 하나의 업데이트로 병합됩니다. 기반 백엔드 읽기는 취소 후에도 계속 진행됩니다. 쿼리 실패는 여전히 reject되며, 이 변경이 런타임 상호운용성을 보증하지는 않습니다.

### Nostr 메일 클라이언트 {#nostr-mail-client}

Nostr 기반 메일 클라이언트인 [nostr-mail-client](https://github.com/nogringo/nostr-mail-client)가 [v0.19.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.19.0)을 출시했습니다. 이 버전은 원격 서명자의 auth_url 승인을 포함하여 bunker, nsec, ncryptsec을 위한 단일 로그인 흐름을 제공합니다. 이제 다시 로그인하지 않아도 DM, 인박스, 아웃박스, 비공개 relay 목록의 변경 사항을 반영하고, 동기화 중 메일 알림의 중복을 제거하며, 이메일 서명을 암호화된 형태로 기기 간에 동기화합니다. 25 MB 한도를 넘는 이메일 첨부 파일은 안내와 함께 폐기되며, Nostr 전용 주소는 이메일에서 보낸 답장을 받을 수 없습니다.

### Napplet 적합성 CLI {#napplet-conformance-cli}

napplet(서명된 Nostr event로 배포되는 웹 앱)을 위한 웹 패키지 및 도구인 [napplet/web](https://github.com/napplet/web)은 이제 지난 호에서 다룬 검증 작업을 버전이 지정된 [@napplet/conformance-cli 0.4.0](https://github.com/napplet/web/releases/tag/%40napplet/conformance-cli%400.4.0)으로 제공합니다. 헤드리스 실행 전에 CLI는 매니페스트의 event ID, 서명, 정확한 원시 HTML 해시를 확인하며, 런타임 바인딩, 네임스페이스, 설치 실패를 napplet 오류와 구분하여 보고합니다. 내장 폴백은 RESOURCE와 GAMEPAD만 다루므로, 커스텀 호스트는 소스 및 스냅샷 입력을 명시적으로 전달해야 합니다.

[Napplet의 deploy 명령은 이제 기본적으로 Zapstore 리스팅을 준비하며](https://github.com/napplet/web/pull/265), 선택된 각 빌드의 스크린샷을 캡처하고 kind 32267 Software Application event를 준비합니다. `--no-screenshot`와 `--no-zapstore`는 이 단계들을 비활성화합니다. 메타데이터를 준비하는 것이 릴리스를 게시하는 것은 아니며, 이 변경은 패키지 릴리스나 에셋 event를 추가하지 않습니다.

### napplet-soy {#napplet-soy}

[napplet-soy](https://github.com/soytec/napplet-soy)는 napplet을 빌드하고 게시하기 위한 워크스페이스로, soyli 명령줄 도구에 [v0.31.2](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.2)와 [v0.31.3](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.3) 태그를 붙였습니다. 이 태그들은 Studio 배포가 아닙니다. Git 전달이 확인되면 게시 과정은 정확한 조상 관계와 대상, 그리고 현재 리비전을 확인한 후 포함된 Git 협업([NIP-34](/ko/topics/nip-34/)) 제안을 병합됨으로 표시하며, 재개 시에는 미리 서명된 상태를 재사용합니다. 더 새로운 제안 리비전은 열린 상태로 유지됩니다. 또한 어떤 커밋을 포함하는 태그가 있다고 해서 대상 브랜치가 그 커밋을 병합했다는 증거로 간주하지 않습니다. 이 태그들의 기반이 되는 소스는 통합된 Manage 워크스페이스에 초기 Cashu 지갑([NIP-60](/ko/topics/nip-60/)) 보기를 추가하고, 탭을 전환해도 실행 중인 napplet이 계속 동작하도록 유지합니다. 이전 버전인 [v0.31.1](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.1)의 업데이터는 변하지 않는 GitHub 저장소 ID를 추적하므로, 설치본은 Soytec으로 이전한 후에도 계정과 프로젝트를 그대로 유지합니다. 이전 업데이터가 설치된 경우에는 설치 프로그램을 한 번 실행해야 합니다.

[NIP-60 Cashu 지갑](https://github.com/soytec/napplet-soy/pull/39)은 [NIP-61](/ko/topics/nip-61/) nutzap을 수령하며, 준비된 mint 출력과 서명된 relay 업데이트를 실행 전에 먼저 저장합니다. 따라서 결과가 불확실한 요청도 결제를 반복하지 않고 복구할 수 있습니다. 지갑은 계정별로 격리되어 있고 브라우저 탭들이 동시에 지출할 수 없습니다. 다만 테스트에는 가짜 mint가 사용되었으며, 실제 자금으로의 상호운용성은 검증되지 않았습니다. [이제 기여 페이지에서 작성자를 대상으로 한 zap을 지원하며](https://github.com/soytec/napplet-soy/pull/42), 선택한 릴리스나 제안에 서명한 작성자에게 지불합니다.

[soyli v0.31.4](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.4) 태그에는 작성자 기여 이력과 zap, 그리고 [NIP-5D 준비 상태, 오디오 및 테스트 관련 변경 사항](https://github.com/soytec/napplet-soy/pull/43)이 기록되어 있습니다. 도메인 호출은 더 이상 셸이 준비 완료를 보고할 때까지 기다리지 않습니다. 공유 호스트는 iframe 격리를 완화하지 않으면서, napplet이 NAPMEDIA를 통해 소유하는 오디오를 조정합니다. 이 태그 역시 Studio 배포가 아닙니다. 설정된 검사 중 다섯 개는 통과했고 다섯 개는 건너뛰었습니다. 완전한 적합성은 여전히 입증되지 않았으며, 수정된 앱들은 재게시를 기다리고 있습니다.

### Pakstr {#pakstr}

[Pakstr](https://git.nostrdev.com/stuff/pakstr)는 Android 앱을 빌드하여 Nostr에 게시하는 명령줄 도구로, [v0.29.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.29.1) 태그를 붙였습니다. 게시하기 전에 [APK가 v2 또는 v3 서명 블록에서 주장하는 서명자 인증서를 읽고](https://git.nostrdev.com/stuff/pakstr/commit/4dbdbec3bec10bef3f96c42a8324e0fc1a10d5c5), 그 SHA-256을 예상되는 사이드카 및 신원 증명과 대조합니다([게시 검토](https://git.nostrdev.com/stuff/pakstr/pulls/108)). 서명되지 않았거나 형식이 잘못되었거나 인증서가 여러 개인 APK는 거부됩니다. 오래된 사이드카는 다시 빌드할 때 제거되며, 유효하지 않은 게시용 nsec는 빌드 전에 실패 처리됩니다. 파서는 APK 서명 자체를 검증하지 않고 이를 Android와 apksigner에 맡깁니다. 그래서 오래되었거나 서명되지 않았거나 잘못된 인증서를 사용한 빌드는 잡아내지만, 빌드가 위조되지 않았음을 증명할 수는 없습니다. ZIP64, 다중 서명자, 키 순환은 지원되지 않습니다.

### MDK {#mdk}

Marmot 암호화 그룹을 위한 SDK이자 런타임인 MDK가 [안정 버전 v0.14.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.14.0)을 출시했습니다. 이 버전은 미디어 파일 핸드오프와 저장소, 순서가 보장된 오프라인 따라잡기, 팔로우 목록 보존, 원시 SQLCipher 키 재설정(rekeying)을 제공하며, MLS와 와이어 포맷은 변경되지 않았습니다. [0.14.0 릴리스 가이드](https://github.com/marmot-protocol/mdk/blob/v0.14.0/docs/release/0.14.0.md)와 [0.14.0 통합 가이드](https://github.com/marmot-protocol/mdk/blob/v0.14.0/docs/integration/0.14.0.md)는 앱이 바인딩, 네이티브 라이브러리, 헤더를 서로 일치하는 세트로 함께 배포하도록 요구하며, [MarmotKit 0.14.0](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-v0.14.0)이 이를 Apple과 Android용으로 패키징합니다. Apple 플랫폼에서는 바이너리가 원시 정적 XCFramework입니다. 따라서 앱은 이를 일치하는 Swift 바인딩과 짝지어 사용하고, 그 PrivacyInfo.xcprivacy 리소스를 앱이 지정하는 래퍼 제품에 복사해야 합니다. 릴리스의 아카이브 검사를 통과했다고 해서 App Store 내보내기가 성공한다는 것이 입증되지는 않습니다. 데이터베이스와 저장소는 단방향으로 마이그레이션되며, 이 과정에서 모든 페이지의 키가 한 번씩 재설정됩니다. 다운그레이드는 여전히 지원되지 않습니다. 계정 미디어와 핸드오프 데이터는 백업에서 제외해야 합니다. WN 에이전트는 여전히 프리릴리스 상태이며, crate들은 crates.io에 올라가 있지 않습니다. 알려진 제한 사항도 남아 있습니다. 다섯 에포크보다 더 늦게 도착한 기록은 아무런 알림 없이 복호화할 수 없게 됩니다. 에포크가 진행되는 사이 전송 중에 유실된 미디어 문제는 수정되지 않았으며, 그룹 컨텍스트 순서와 관련된 호환성 문제도 여전히 남아 있습니다.

태그 조상 관계를 보면 이 안정 태그에는 동기화 및 미디어 관련 변경 다섯 건도 포함되어 있습니다. [그룹 구독을 갱신할 때 변경된 REQ 배치 패밀리만 다시 묶습니다](https://github.com/marmot-protocol/mdk/pull/2583). 실패한 패밀리는 다음 동기화를 위해 활성 경로를 유지하며, 부분 커밋은 여전히 동기화 실패로 보고합니다. [전송 전 갱신이 실패하더라도 메시지 전송과 그룹 변경은 계속 영속 큐에 들어갑니다](https://github.com/marmot-protocol/mdk/pull/2567). 단, 완료 상태는 CompletionUnknown으로 남을 수 있습니다. [연결할 수 없는 relay의 REQ는 재연결될 때까지 같은 ID로 이행해야 할 상태로 남으므로](https://github.com/marmot-protocol/mdk/pull/2572), 저하된 커버리지는 완전한 기록이 아닙니다. [온보딩 복구 승인은 모든 탐색 소스를 기다리며](https://github.com/marmot-protocol/mdk/pull/2545), 선언된 소스가 시간 초과되면 RetryableFailure를 반환합니다. [옵트인 방식의 계정별 미디어 보존](https://github.com/marmot-protocol/mdk/pull/2541)은 영구 보관(Keep forever)부터 30일까지 설정할 수 있습니다. 이 기능은 마지막 조회 시점이 아니라 수신 시점 또는 마지막 명시적 재다운로드 시점을 기준으로 미디어를 정리하며, 메시지 기록은 삭제하지 않습니다. 호스트는 새로운 FFI 값인 CleanedBySetting을 처리해야 합니다.

태그 이후에 병합된 소스에서는 아직 어떤 릴리스도 포함한다고 밝히지 않은 다중 기기 및 푸시 작업이 이어졌습니다. [가입 후 기록 요청은 커밋과 재시작을 거쳐도 유지되어](https://github.com/marmot-protocol/mdk/pull/2635) Welcome과 실시간 메시지 사이의 공백을 메웁니다. [계정별로 멤버를 집계하면서](https://github.com/marmot-protocol/mdk/pull/2634) 두 번째 기기가 가입하거나 탈퇴할 때 특정 사람에 대한 잘못된 알림이 더 이상 표시되지 않습니다. 또한 [Welcome 처리는 형제 기기를 위한 전달을 무시하되](https://github.com/marmot-protocol/mdk/pull/2633), 가입을 실패시키거나 키를 소비하지는 않습니다. 푸시의 경우 MDK는 [커밋 후 소유자가 서명한 레코드와 툼스톤을 가십으로 전파하는데](https://github.com/marmot-protocol/mdk/pull/2620), 여기에는 [새 푸시 가십 저장소](https://github.com/marmot-protocol/mdk/pull/2617)가 사용됩니다. 아울러 [멤버 추가 후 토큰을 다시 공유하고](https://github.com/marmot-protocol/mdk/pull/2613) [수신자의 모든 기기에 알림을 보냅니다](https://github.com/marmot-protocol/mdk/pull/2609). 다만 발신자 자신의 기기는 여전히 알림을 받지 못합니다. [트리거마다 새로 생성되는 무작위 패딩](https://github.com/marmot-protocol/mdk/pull/2608) 덕분에 중복 제거 때문에 깨우기 신호가 억제되는 일이 없습니다. [KeyPackage 게시는 계정 자체의 relay 목록을 채택하며](https://github.com/marmot-protocol/mdk/pull/2594), 목록이 불완전하거나 사용 가능한 relay가 없으면 저장된 목록을 보존한 채 실패합니다. [유형이 지정된 오래된 에포크(stale-epoch) 및 미해결(unsettled) 미디어 상태](https://github.com/marmot-protocol/mdk/pull/2312)는 다시 업로드해야 하는지, 아니면 동기화 후 재전송해야 하는지를 앱에 알려 줍니다. [전송 상태 변경은 즉시 전달되고, 바이트 진행률은 일괄 처리됩니다](https://github.com/marmot-protocol/mdk/pull/2311).

더 새로운 계정-기기 소스는 이후 릴리스를 향한 진척일 뿐, 안정 버전 0.15가 아닙니다. 테스트 전용으로 표시된 10월 28일자 나이틀리 빌드 세 개는 커밋 b8d0a49에 고정되어 있습니다. 이 커밋은 이후의 병합보다 앞선 것이므로, 해당 에셋에는 그 내용이 모두 포함되어 있지 않습니다. MDK는 [기기별로 호환되는 KeyPackage를 선택하며](https://github.com/marmot-protocol/mdk/pull/2649), 이는 계정당 최근 기기 최대 20대까지 적용됩니다. [로그아웃하면 이 기기의 게시 슬롯만 철회됩니다](https://github.com/marmot-protocol/mdk/pull/2654). [새 패키지는 30일 1시간 동안 유효하며, 게시 후 6~7일 사이에 갱신됩니다](https://github.com/marmot-protocol/mdk/pull/2643). 탐색 과정은 모든 기기를 찾으려 하지만, relay 장애로 일부가 누락될 수 있습니다. 다시 초대하면 도움이 될 수 있으나 자동 복구는 보장되지 않습니다. [인증된 리프별 기능 검사](https://github.com/marmot-protocol/mdk/pull/2645)가 계정별 캐시를 대체합니다. 모든 창립 멤버가 지원하는 경우 [새 그룹은 account-devices 컴포넌트 0x800d를 요구하며](https://github.com/marmot-protocol/mdk/pull/2656), [업그레이드된 기기는 이제 이를 지원한다고 알립니다](https://github.com/marmot-protocol/mdk/pull/2659). 이러한 그룹은 해당 컴포넌트가 없는 이전 기기를 거부하며, 기존 그룹은 변경되지 않습니다. 이 요구 사항이 적용되면 MDK는 [컴포넌트 데이터, 지원되지 않는 리프, 계정당 20개를 초과하는 리프, 그리고 요구 사항을 제거하려는 시도를 거부합니다](https://github.com/marmot-protocol/mdk/pull/2637). 레거시 그룹과 이를 요구하지 않는 그룹은 그대로 둡니다. 이와 별도로 MDK는 [스키마에 데이터가 없는 앱 컴포넌트에 대해서는 호스트가 제공한 초기 데이터를 거부하며](https://github.com/marmot-protocol/mdk/pull/2662), 이 거부는 어떤 그룹, Welcome, event도 생성되기 전에 이루어집니다.

0x800d 그룹에서 엔진은 [부모 상태를 고려한 커밋 분류와 함께 자기 계정 추가 및 제거 권한](https://github.com/marmot-protocol/mdk/pull/2650)을 갖추게 됩니다. 이를 통해 자기 업데이트, 자기 제거, 동일 계정, 관리자 커밋을 구분하며, 동일 계정 권한을 행사하려면 값 기반(by-value) 제안이 필요합니다. [일치하는 Welcome 처리는 동일 계정 Welcome을 수락하되](https://github.com/marmot-protocol/mdk/pull/2646), 해당 그룹에서만, 그리고 컴포넌트 상태와 서명 검사를 마친 후에만 수락합니다. 다른 그룹에서는 여전히 활성 관리자가 필요합니다. [자기 계정 추가 및 제거 전송 의도는 스케줄러에서 공정한 차례를 받지만](https://github.com/marmot-protocol/mdk/pull/2655), 앱 API는 아직 동일 계정 전송 의도를 노출하지 않습니다. [이제 기기 자신의 리프 제거가 해당 기기의 로컬 멤버십을 결정하므로](https://github.com/marmot-protocol/mdk/pull/2640), 형제 기기가 존재한다는 이유로 제거된 기기의 멤버 작업이 유지되는 일은 더 이상 없습니다.

푸시 가십에는 [레코드와 툼스톤의 8바이트 다이제스트 접두사를 담아 영속적으로 큐에 저장되는 kind 447 공지](https://github.com/marmot-protocol/mdk/pull/2648)가 추가됩니다. 이 공지는 가입 시, 레코드 변경 시, 그리고 7일 단위의 메시지 주기에 맞춰 전송됩니다. 피어는 순위가 매겨지고 시차를 둔 응답을 통해 [누락된 소유자 서명 레코드를 복구하며](https://github.com/marmot-protocol/mdk/pull/2658), 여기에는 중복 억제와 리프당 24시간 제한이 적용됩니다. 복구 과정에서 [잘라내기와 취소는 더 이상 새로운 손실을 만들어 내지 않습니다](https://github.com/marmot-protocol/mdk/pull/2673). 진전 없이 24회 시도하면 해당 의무는 불완전 기록 경고 뒤에 보류됩니다. [커버리지 원장](https://github.com/marmot-protocol/mdk/pull/2667)은 섀도 기록기로만 동작합니다. 한편 [시간 분할 스윕](https://github.com/marmot-protocol/mdk/pull/2665)은 가장 오래된 슬라이스부터 재개하지만, 아직 프로덕션 스케줄러는 없습니다. [옵트인 감사 파일은 만료되며](https://github.com/marmot-protocol/mdk/pull/2664), 그 시점은 마지막 쓰기 후 30일이고 정리는 시작 시와 매시간 수행됩니다. 실제 삭제는 하루 늦게 이루어질 수 있으며, 별도의 키 공개 보안 로그는 이 만료 대상에서 제외됩니다.

[페어링 crate](https://github.com/marmot-protocol/mdk/pull/2670)는 임시 X25519, 커밋먼트(commitment), 사용자가 양쪽 화면에서 확인하는 이모지 7개 비교, 그리고 ConfirmedLink로 끝나는 HMAC 확인을 사용합니다. 이 crate의 와이어 어댑터는 전송 계층만 다루며, 사양이 마련될 때까지 기본적으로 꺼져 있습니다. UI와 Welcome 및 그룹 링크 후속 작업은 완료되지 않았고, 이 구현의 상호운용성은 여전히 검증되지 않았습니다. [기기 명단 0x800e 소스](https://github.com/marmot-protocol/mdk/pull/2666)는 숨겨진 단일 계정 그룹에 diff 업데이트를 적용합니다. 그러나 0x800e를 알리려면 테스트 정책 재정의가 필요하므로, 프로덕션 빌드는 아직 기기 그룹을 생성하거나 가입할 수 없습니다.

다른 MDK 제안들은 아직 열려 있습니다. 그중 하나는 [NIP-67](/ko/topics/nip-67/) [완료를 완전한 커버리지의 증거로 취급하는 것](https://github.com/marmot-protocol/mdk/pull/2674)을 중단하자는 것으로, 일정이 잡히지 않은 스윕은 완전성을 보장하지 않기 때문입니다. 다른 제안들은 [체크포인트 재생](https://github.com/marmot-protocol/mdk/pull/2671), [자동 재가입](https://github.com/marmot-protocol/mdk/pull/2661), [기존 그룹에서의 0x800d 활성화](https://github.com/marmot-protocol/mdk/pull/2668)를 추가하려는 것입니다. 이전에 제출된 네이티브 API 제안 세 건도 새로 상태를 확인한 결과 여전히 열려 있습니다. [과거 첨부 파일 복구](https://github.com/marmot-protocol/mdk/pull/2614)는 소스 슬롯을 검사하고 인증된 다이제스트와 만료를 확인한 후, 검증된 바이트를 비공개 임대(leased) 파일에 기록하게 됩니다. 이 과정에서 타임라인은 네트워크를 사용하지 않는 상태로 유지되며, 전달된 사본은 취소할 수 없는 스냅샷입니다. [필터 전체 채팅 선택 핸들](https://github.com/marmot-protocol/mdk/pull/2592)은 로드된 페이지를 넘어 필터와 일치하는 모든 채팅을 포괄하되, 이후에 도착하는 항목은 제외하게 됩니다. 그리고 [wn-agent 그룹 생성을 위한 창립 관리자 선택](https://github.com/marmot-protocol/mdk/pull/2587)은 초대된 창립 관리자를 선택하고, 업로드 전에 비멤버를 거부하게 됩니다.

### nosfry {#nosfry}

Rust로 작성된 Nostr relay인 nosfry가 네이티브 에디션과 Workers/SQL 에디션용 [nosfry v0.2.0](https://github.com/qntx/nosfry/releases/tag/v0.2.0)을 출시했습니다. 이 버전에는 v0.1 시점에는 릴리스되지 않았던 기능들이 담겨 있습니다. [NIP-09](/ko/topics/nip-09/) 삭제, [NIP-40](/ko/topics/nip-40/) 만료, NIP-42 AUTH 및 [NIP-70](/ko/topics/nip-70/) 보호 event, [NIP-45](/ko/topics/nip-45/) COUNT, [NIP-77](/ko/topics/nip-77/) Negentropy 동기화, [NIP-62](/ko/topics/nip-62/) 소멸(vanish) 요청, 그리고 [NIP-86](/ko/topics/nip-86/) 관리자 API가 그것입니다. 또한 아웃바운드 예산과 쓰기 정책을 갖춘 제한된 구독을 추가하고, permessage-deflate가 기본적으로 켜져 있다고 설명합니다. 성능 및 적합성에 관한 주장은 독립적으로 재현되지 않았으며, 모든 구현과 상호운용된다고 주장하지도 않습니다.

0.3 태그 이후인 10월 25일에 보안 강화 변경 네 건이 병합되었으며, 이들은 릴리스된 바이너리에 포함되어 있지 않습니다. Worker 연결 및 속도 제한 버킷은 IPv6를 /64 단위로 집계하는 반면, NIP-86 IP 차단 목록은 여전히 정확한 주소 단위로 일치 여부를 판단합니다([#78](https://github.com/qntx/nosfry/pull/78)). NEG-OPEN 스캔은 수집 중에 1024개 레코드 단위로 전역 동기화 메모리 예산을 차감합니다([#73](https://github.com/qntx/nosfry/pull/73)). 동일 타임스탬프 동점 그룹은 쿼리 제한으로 크기가 제한된 힙을 유지합니다([#72](https://github.com/qntx/nosfry/pull/72)). NIP-86 모더레이션 스냅샷은 요청 시점에 캡처된 상태 그대로 저장된 데이터 읽기와 실시간 전달에 적용됩니다. 따라서 열려 있는 요청에는 새 차단이 즉시 반영되지 않습니다([#68](https://github.com/qntx/nosfry/pull/68)).

역시 아직 릴리스되지 않은 추가 병합은 [라이터를 64 MiB 바이트 예산으로 제한하고](https://github.com/qntx/nosfry/pull/79), 게시 백로그를 더 큰 트랜잭션으로 처리하되 각 트랜잭션의 상한을 수행된 작업량으로 정합니다. 이때 영속적인 LMDB 동기화는 그대로 유지합니다. 프로젝트의 벤치마크 수치는 자체 프로브 변형에서 나온 것이며, 저희가 측정한 결과가 아닙니다.

### nostream {#nostream}

TypeScript 기반 Nostr relay인 nostream이 [nostream 3.7.0](https://github.com/cameri/nostream/releases/tag/nostream%403.7.0)과 [nostream 3.8.0](https://github.com/cameri/nostream/releases/tag/nostream%403.8.0)을 출시했습니다. 3.7.0 버전에는 앞서 소스에만 반영되어 있다고 전해 드린 관리자 작업, 감사 로그, 서명된 webhook, 메트릭이 포함되어 배포됩니다. 유료 쓰기를 위한 옵트인 방식의 수명 주기도 추가되었고, LNbits 1 이상에서의 ISO 시간 파싱과 만료 처리도 수정되었습니다. 정적 미러링은 제거되었습니다. 관련 설정은 이제 NIP-77 동기화로 대체되어 경고와 함께 무시됩니다. 3.7.0 컨테이너 이미지는 Docker 태그에 허용되지 않는 `@` 문자가 들어 있어 게시에 실패했으며, 3.8.0은 태그를 수정하고 실패한 이미지 빌드를 다시 실행하는 기능을 추가했습니다. 3.8.0 버전은 또한 관리자 API와 콘솔에 pubkey 및 kind 목록, IP 및 속도 제한 우회 제어 기능을 더하고, 상위 게시자, IP, 속도 제한 적중에 대한 통계도 제공합니다. 속도 제한 전략을 바꾸거나 업그레이드할 때 발생하던 Redis 키 충돌도 이번에 수정되었습니다. 다만 소스만으로는 이제 이미지가 정상적으로 게시되는지 확인할 수 없으며, 실제로 배포된 과금 기능이 있다고 주장하지도 않습니다.

이와 별도로 `rewrite/main` 브랜치에서 진행 중인 Rust 재작성 작업은 [740ef69](https://github.com/Cameri/nostream/commit/740ef699fb04f3f54bd82a9d012e27c04dabb480)에서 실제 클라이언트에 응답하는 첫 wire 코어를 병합했고, [2b2287f](https://github.com/Cameri/nostream/blob/2b2287f8acc43b1e0b3039c745c88a03268831aa/crates/nostream-relay/src/strategies/mod.rs) 시점에는 전략 레지스트리가 남은 14개의 전략 분기를 구현합니다. 기본값이 아닌 이 프로토타입은 TypeScript `main` 및 안정 버전인 3.x 릴리스와 분리되어 있으며, 리뷰와 CI 결과는 작성자가 제시한 것입니다. [NIP-43](/ko/topics/nip-43/)과 [NIP-56](/ko/topics/nip-56/) 처리는 기본적으로 꺼져 있습니다. vanish 요청은 여전히 동시에 진행되는 게시와의 경쟁에서 밀릴 수 있으므로, vanish가 프라이버시를 보장하지는 않습니다. 접근 및 신원 관련 코드를 수동으로 리뷰해 달라는 작성자의 요청은 여전히 유효합니다.

### swift-nostr {#swift-nostr}

Swift용 Nostr SDK인 swift-nostr가 10월 27일 [0.9.0](https://github.com/yysskk/swift-nostr/releases/tag/0.9.0)을 공개했습니다. 이번 릴리스에는 타입이 지정된 키, event ID, URL, 타임스탬프, 좌표, 구독 ID가 추가되었습니다. 로컬이든 원격이든 어떤 서명자로도 서명할 수 있는 EventTemplate, 타입이 지정된 오류, 풀이 소유하는 구독, 그리고 풀이나 정확히 지정한 relay 또는 NIP-65 outbox를 거쳐 라우팅하는 RelayRoute도 함께 들어갔습니다. Event.verify는 이제 잘못된 서명에 대해 오류를 던지므로, 0.8에서 옮겨 오려면 소스 코드를 수정해야 합니다. 앞서 나온 [0.8.0](https://github.com/yysskk/swift-nostr/releases/tag/0.8.0)은 보안 강화 릴리스였습니다. 릴리스 노트에 따르면 이 버전은 교체 가능한 event, gift-wrap 발신자, NIP-46 및 NWC 응답을 검증하고, 여러 relay에서 온 중복 응답을 제거하며, 서명자가 수행하거나 공유 키를 사용하는 NIP-44 암호화를 추가했고, 호환성을 깨는 변경으로 zap 검사를 더 엄격하게 했습니다. 이는 작성자의 주장이며 감사 결과가 아닙니다.

앞서 다룬 0.8 이후의 수정 사항들은 이제 0.9.0에 포함되어 배포됩니다. 서명자는 [자신의 것과 다른 공개 키를 가진 event를 거부하며](https://github.com/yysskk/swift-nostr/pull/239), [구독을 해지할 때 CLOSE를 보내려고 연결이 끊긴 relay를 여는 일도 더 이상 없습니다](https://github.com/yysskk/swift-nostr/pull/238). 핵심 전송 호출은 notConnected를 던지고 구독 시에는 명시적으로 연결합니다. 하지만 NWC와 NIP-46 전송 계층은 새 요청이 들어오면 여전히 끊긴 relay에 다시 연결합니다. NWC 및 원격 서명자 호출은 [타입이 지정된 오류와 즉시 취소를 지원하게 되었지만](https://github.com/yysskk/swift-nostr/pull/247), 이미 전송된 요청은 여전히 처리될 수 있습니다. NWC 알림 및 인증 챌린지 스트림은 [relay가 종료되면 함께 끝나고](https://github.com/yysskk/swift-nostr/pull/242), 연결 대기는 [모든 relay 스트림이 끝나면 실패하며](https://github.com/yysskk/swift-nostr/pull/244), [필터의 tag 쿼리는 한 번만 저장되어](https://github.com/yysskk/swift-nostr/pull/241) tag마다 JSON 키가 하나씩만 생깁니다. 범용 [WalletConnectRequest](https://github.com/yysskk/swift-nostr/pull/232)는 일반적인 result_type 및 오류 검사를 거치는 단일 응답 방식의 사용자 정의 [NIP-47](/ko/topics/nip-47/) 메서드를 지원하며, multi_pay는 별도로 유지됩니다. 확장 가능한 [RemoteSignerMethod](https://github.com/yysskk/swift-nostr/pull/229)는 기본 제공 범위를 넘어서는 NIP-46 메서드를 호출하고 결과 문자열을 반환합니다. 두 경우 모두 지갑이나 서명자가 해당 메서드를 지원해야 합니다. [EventTemplate과 signer.sign 조합](https://github.com/yysskk/swift-nostr/pull/214) 덕분에 원격 NIP-46 서명자도 zap 요청처럼 예전에는 로컬 EventSigner가 필요했던 헬퍼를 사용할 수 있으며, 이에 맞춰 [여러 데이터 모델](https://github.com/yysskk/swift-nostr/pull/215)과 [NIP-29](/ko/topics/nip-29/) 및 [NIP-98 빌더](https://github.com/yysskk/swift-nostr/pull/216)도 함께 변경되었습니다. 이 변경은 API를 바꿀 뿐 wire 형식은 바꾸지 않습니다.

0.9.0 태그 이후에 병합된 코드는 해당 릴리스에 포함되지 않습니다. 이제 [호출자가 전송을 취소해도 정상 상태의 relay는 유지되며](https://github.com/yysskk/swift-nostr/pull/257), [DM 열기 및 결과 타입이 단순해지고 rumor 작성자가 서명자에 결합되었습니다](https://github.com/yysskk/swift-nostr/pull/260). [FileAttachment는 암호화된 파일 메타데이터를 통합합니다](https://github.com/yysskk/swift-nostr/pull/261). [setSigner와 removeSigner로 이루어진 단일 쌍](https://github.com/yysskk/swift-nostr/pull/262)은 뒤늦게 반영되는 오래된 원격 설정이 로그아웃을 되돌리는 일을 막습니다. removeSigner는 AUTH 응답을 중단시키지만, 이미 전송된 원격 요청을 철회하지는 않습니다. [재연결 및 중복 제거 설정에는 각각 전용 구성 타입이 생겼습니다](https://github.com/yysskk/swift-nostr/pull/263).

### haps {#haps}

Nostr 키로 서명된 소프트웨어용 설치 프로그램인 haps가 [haps v0.1.22](https://github.com/mmalmi/haps/releases/tag/v0.1.22)를 출시했습니다. 이번 버전은 [haps v0.1.18](https://github.com/mmalmi/haps/releases/tag/v0.1.18)을 기반으로 합니다. v0.1.18은 Linux와 macOS 소스 빌드를 비공개 홈 디렉터리와 쓰기 가능한 체크아웃 안에서 실행했으며, 네트워크 접근은 기본적으로 꺼져 있었습니다. 명시적인 allow-build-network 및 allow-host-build 옵션으로 이 동작을 재정의할 수 있습니다. Windows 소스 빌드에는 host-build가 필요합니다. 설치된 앱은 여전히 샌드박스 밖에 있습니다. [haps v0.1.19](https://github.com/mmalmi/haps/releases/tag/v0.1.19)는 고정된 소스와 빌드 레시피를 빌드된 페이로드 해시에 연결하는 단일 감사 및 설치 확인 절차를 추가했습니다. 따라서 이와 일치하는 게시자 바이너리는 검토를 거친 해당 빌드의 정책에 따라 설치할 수 있습니다. 신뢰된 검토를 재사용하는 것은 또 하나의 독립적인 감사로 간주되지 않습니다. 변경 불가능한 서명된 카탈로그에서 설치할 때에도 여전히 감사가 필요하며, 게시된 경고가 있으면 기본값이 No인 별도의 동의가 필요합니다. 0.1.22 버전은 [제한된 조회와 게시자 측 소스 완전성 검사](https://github.com/mmalmi/haps/commit/606a1cd25ef8ff9f454adb0d89acb5d4c9605a35)를 추가했습니다. 이제 조회는 짧은 마감 시간을 공유하고, 클라이언트는 [첫 번째 relay가 연결되면 쿼리를 시작하며](https://github.com/mmalmi/haps/commit/f58d7fa30e149c8f0e500bd7cd59da7e834cc61c), 스냅샷 검색은 단일 3초 예산 안에서 찾은 검증된 결과를 반환합니다. 게시 과정은 소스 ref를 변경하기 전에 요건을 충족하는 번들 git 헬퍼, 고정된 동반 바이너리와 일치하는 별도 설치 헬퍼, 또는 complete-blob-dag-v1을 알리는 헬퍼 중 하나를 찾지 못하면 실행을 거부합니다. 기본 의존성 검토 범위, symlink 및 크기 보호 장치, 제한된 재시도는 그대로 유지되며, 이는 새로운 독립 감사가 아닙니다. 콜드 설치가 한 번 성공했다고 해서 간헐적인 전송 시간 초과가 해결되었다는 것을 보여 주지는 않으며, 고정된 헬퍼 번들은 여전히 호스트 툴체인에 의존합니다.

### Swarm, NIP-98 인증으로 관리자 API 보호 {#swarm-protects-its-admin-api-with-nip-98-authentication}

Nostr와 연동되는 게시 및 관리 서버인 Swarm이 [v0.2.0을 출시했으며](https://github.com/HiveTalk/swarm/releases/tag/v0.2.0), 이 버전은 기존 대시보드 쿠키와 함께 [관리자 API용 NIP-98 HTTP 인증](https://github.com/HiveTalk/swarm/pull/59)을 제공합니다. 서버는 kind 27235 event의 서명, 과거 5분부터 미래 1분까지의 타임스탬프 허용 범위, HTTP 메서드와 경로 및 쿼리, 운영자가 고정한 pubkey, 그리고 선택적 페이로드 해시를 확인합니다. 전달된 호스트(forwarded host)를 받아들이는 것은 앞단에 신뢰할 수 있는 프록시가 있다는 전제를 깔고 있습니다. 이전에 공개되어 있던 `/environment` 엔드포인트는 이제 관리자 인증을 요구합니다.

릴리스 포함 여부가 확인되지 않은 이후의 병합은 연결된 팀 구성원의 kind 1 노트를 대상으로 [X로의 옵트인 크로스포스팅](https://github.com/HiveTalk/swarm/pull/67)을 추가합니다. 예약된 노트와 WebSocket으로 도착한 노트는 같은 경로를 거칩니다. `e` tag가 있는 답글은 건너뛰고, 과거 노트를 소급해 게시하지 않으며, 중복은 event ID 기준으로 제거됩니다. CMS 측은 NIP-98 인증을 사용합니다. 게시는 로컬 OAuth나 신뢰된 위임 서비스에 의존하므로, 탈중앙화된 방식도 아니고 신뢰가 필요 없는 방식도 아닙니다. 실제 운영 중인 X 서비스로의 게시는 아직 테스트되지 않았습니다.

### fips2go, 검증된 메시 도메인으로의 직접 링크 활성화 {#fips2go-turns-on-direct-links-to-verified-mesh-domains}

Nostr 광고(advert)를 통해 피어와 도메인 클레임을 찾는 Android 메시 클라이언트 fips2go가 0.9.6부터 [0.10.0](https://github.com/fr34aky/fips2go/releases/tag/v0.10.0)까지의 버전을 출시했습니다. 0.10 버전은 가장 최근에 검증된 도메인 최대 두 곳의 서버로 향하는 [직접 링크를 기본적으로 켭니다](https://github.com/fr34aky/fips2go/pull/91). 이때 DNSSEC 또는 여러 리졸버를 통해 고정된 도메인만 대상으로 삼습니다. 이러한 링크는 휴대전화의 공인 IP 주소와 온라인 시간대를 해당 서버에 노출하고 어떤 서버를 선택했는지를 공개 relay에 드러내지만, 사용자는 이 기능을 끌 수 있습니다. 특정 서버와 포트에 대해 이미 고정된 TXT 레코드는 이제 새로운 Nostr 클레임 없이 해석되는 반면, 새 서버, 변경된 포트, 포트가 없는 레코드는 여전히 대기합니다. 네트워크 전환으로 새 VPN 경로가 필요하지만 구성은 바뀌지 않은 경우, 앱은 터널만 교체하고 노드, 링크, 세션은 유지합니다. 핫스팟 변경, 그 밖의 구성 변경, 실패 시 대체 동작에서는 여전히 노드를 다시 구축합니다.

### fips-pub-domains, 클레임을 가져오기 전에 고정된 조회에 응답 {#fips-pub-domains-answers-pinned-lookups-before-fetching-claims}

공개 도메인을 메시 주소에 연결하는 Nostr 서명 바인딩을 해석하는 fips-pub-domains가 [0.2.9](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.9)와 [0.2.10](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.10)을 출시했습니다. 특정 서버와 포트에 대해 고정된 TXT 레코드는 이제 동일한 고정 정책 아래에서 백그라운드 클레임 가져오기가 끝나기 전에 응답할 수 있으며, 새 서버나 포트는 여전히 클레임을 기다립니다. 데스크톱 시작 시와 네트워크 변경 후에는 리졸버가 고정된 서버를 최대 16개까지 미리 준비(warm-up)하며, 이 과정에서 해당 서버와 라우팅 노드에 온라인 상태가 드러납니다. 첫 20초 백오프 동안에는 3초마다 재시도하고, 서버가 응답하면 일찍 종료합니다.

이 태그들 이후에 병합된 두 가지 변경 사항은 아직 릴리스되지 않았습니다. [하나는 `fips-ca` ServiceClaim 역할을 추가합니다](https://github.com/fr34aky/fips-pub-domains/pull/29). 이 역할은 포트가 없고 자체 DNSSEC 체인과 증명(attestation)을 가지며 `fips-dns`와 분리되어 있지만, 새 PKI를 도입하거나 DNS 바인딩 정책을 바꾸지는 않습니다. [다른 하나는 CLI verify 및 zone 명령을 추가합니다](https://github.com/fr34aky/fips-pub-domains/pull/30). 이 명령들은 고정(pin) 파일을 읽기만 하고 쓰지는 않습니다. 이 코드에서 증명은 자신의 이전 증인(witness)만 담고 있으며, 다른 역할 항목은 다시 검증됩니다. require-previous 옵션은 누락된 데이터를 거부하지만, 장애와 존재하지 않는 레코드를 구별하지는 못합니다.

### Codr {#codr}

White Noise 암호화 채팅으로 데스크톱 코딩 세션을 제어하는 브리지인 [Codr v0.8.0](https://github.com/tidley/codr/releases/tag/v0.8.0)은 채팅에서 확인을 거치고 10분 이내에 이루어져야 하는 워커 업데이트 기능을 추가했습니다. 이 업데이트는 고정된 유지관리자의 ngit 레코드와 체크섬이 검증된 Blossom 바이트를 가져오며, GitHub로 대체하는 경로는 없습니다. 커넥터나 저장소 코호트 변경은 거부하고, 시작에 실패하면 이전 실행 파일을 복원합니다. 지금까지 이 업데이트는 테스트 픽스처를 대상으로만 실행되었습니다. 이제 파일과 미디어는 작업 중인 세션을 중단시키지 않고 전달되며, 최대 25 MiB, 첨부 파일 4개까지 가능합니다. 선택 사항인 Gemini 전사 기능은 복호화된 음성 메모를 Google로 보내며 기본적으로 꺼져 있습니다. 0.4부터 0.7까지의 릴리스는 휴대전화에서 입력한 텍스트를 작업 중인 세션에 전달하고, /cancel과 프로젝트, 에이전트, 모델 메뉴를 추가했으며, MDK 0.14로 전환했습니다. 0.13에서의 마이그레이션은 한 방향으로만 가능하며 백업과 승인이 필요합니다.

[옵트인 방식의 소유자 전용 제어 채팅](https://github.com/tidley/codr/pull/7)(`control_chat=true`, 기본값은 꺼짐)은 다음 워커 시작 시 그룹을 생성합니다. `/new`는 채팅이 연결되기 전에 프로젝트 세션을 시작합니다. 생성 여부가 불확실한 경우에는 자동으로 재시도하지 않습니다.

저희 소스 기준 시점까지 병합되지 않은 열린 pull request는 [새 코딩 세션을 위한 그룹 생성](https://github.com/tidley/codr/pull/18) 과정에서 아직 기록되지 않은 대화 기록(transcript)을 빈 것으로 취급하도록 할 것입니다. 유효하지 않거나 모호한 대화 기록은 여전히 거부될 것입니다. 이 변경은 첫 프롬프트 이전의 새 `/new` 세션에 대한 휴대전화 초대를 복원하며, 세션 승인 방식은 바꾸지 않을 것입니다.

### nostr-media {#nostr-media}

Nostr 미디어 호스팅용 WordPress 플러그인인 [nostr-media 0.17](https://github.com/fabianfabian/nostr-media/releases/tag/0.17)은 Blossom 미러링을 강화했습니다. 이제 [미러 URL을 가져오기 전에 서명된 kind 24242 해시 권한 부여를 확인하여](https://github.com/fabianfabian/nostr-media/commit/f29e15e387a41c0d43b97d5b8643e287ccae88d4), 권한이 없는 요청은 다운로드 없이 거부합니다. 가져오기에는 공개 HTTP(S) 호스트만 허용하고 리디렉션을 검증하는 WordPress의 안전한 HTTP API를 사용하며, 상한은 20초, 리디렉션 3회, 128 MiB입니다. 다운로드된 바이트는 여전히 해시를 계산해 확인합니다. Authorization, X-SHA-256, X-Content-Type 헤더는 대소문자를 구분하지 않고 일치시킵니다. 서버 측 요청 위조 방어는 WordPress 안전 API의 강도를 넘어서지 못합니다.

### NosTube {#nostube}

Nostr 기반 동영상 사이트인 [NosTube](https://github.com/flox1an/nostube)가 침해된 인증 기관에 대한 신뢰를 제거하기 위해 [서버 0.1.25](https://github.com/flox1an/nostube/releases/tag/server-v0.1.25)와 [데스크톱 0.2.51](https://github.com/flox1an/nostube/releases/tag/v0.2.51)을 출시했습니다. 서버의 Rust relay는 더 이상 WebSocket 또는 HTTPS 연결에서 해당 인증 기관을 신뢰하지 않으며, 이미지 빌드에는 이제 고정된 Debian 시스템 CA 번들이 필요합니다. 데스크톱 릴리스는 TLS 계층과 almond 사이드카에 동일한 완화 조치를 적용합니다. 이러한 보안 관련 주장은 릴리스 노트에 근거한 것입니다. 이후 나온 서버 0.1.27의 노트는 오래된 libbrotli1이 포함되어 있으므로 해당 이미지를 사용하지 말라고(DO NOT USE) 밝히며 0.1.28을 안내하지만, 저희는 0.1.28이 출시되었는지 확인하지 못했습니다.

### bitchat {#bitchat}

Bluetooth 메시와 Nostr 위에서 동작하는 메신저 [bitchat](https://github.com/permissionlesstech/bitchat)이 Nostr 위치 채팅(geochat)의 성능 개선과 DM rumor의 타임스탬프 범위 제한을 담은 [1.8.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.8.0)을 출시했습니다. 이제 앱은 닉네임이 아닌 발신자 ID로 사용자 자신의 메시지를 인식합니다([발신자 식별 수정](https://github.com/permissionlesstech/bitchat/pull/1793)). 비공개 그룹은 생성자를 고정하며, 메시 피어 ID는 geohash DM에 포함되지 않습니다. 성능 수치는 프로젝트가 자체적으로 제시한 것이며 저희가 재현하지는 않았습니다.

소스 마감 시점까지 병합되지 않은 열린 pull request 하나는 가장 가까운 relay 다섯 개와 공유 백업 다섯 개를 경유해 라우팅하고 경로당 연결 수를 10개로 제한함으로써, relay 장애 중에도 지역 기반 채팅의 연결을 유지하도록 할 예정입니다([#1822](https://github.com/permissionlesstech/bitchat/pull/1822)). relay 디렉터리가 로드되기 전에는 메시지가 대기열에 쌓이고, 구독과 대기 중인 쓰기 작업은 신원 변경 없이 이전됩니다. 검증은 작성자 본인이 수행한 것입니다. Android 측 연동 변경은 별도의 pull request로 진행됩니다.

역시 병합되지 않은 또 다른 열린 pull request는 Nostr 전송 계층이 아닌 자체 `LIVE_VIDEO_V1` 형식을 사용해 [iOS 및 macOS Bluetooth 메시를 통한 실시간 영상](https://github.com/permissionlesstech/bitchat/pull/1827) 기능을 추가하려 합니다. 공개 프레임에는 서명이 붙고 최신성 검사가 이루어집니다. DM 프레임은 Noise 암호화 안에서 전송되며, 녹화본은 메시지로 전송됩니다. 작성자는 Android에서 iPhone으로 보낸 스트림이 수신되었다고 보고합니다. iPhone에서의 송신, iOS 기기 간 영상 송수신, DM 실시간 영상은 테스트되지 않았습니다.

### ngit {#ngit}

Nostr 위에서 Git 협업을 지원하는 명령줄 도구 [ngit](https://github.com/DanConwayDev/ngit-cli)이 [v3.0.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v3.0.4)를 출시했습니다. 이제 relay 연결은 물론 Android의 HTTPS 연결도 침해된 인증 기관을 더 이상 신뢰하지 않습니다. 대화형 프롬프트는 빈 입력을 방지하며, 명령은 오프라인 필터를 준수합니다. 원격 추적 업데이트는 아직 게시되지 않은 커밋을 보존합니다. 진단 메시지 역시 소스가 없는 경우와 쿼리가 결과를 반환하지 않은 경우를 구분합니다.

### Hasheus {#hasheus}

이전에 verify라는 이름이었던 파일 검증 도구가 이제 [Hasheus](https://github.com/tinfoilhash/hasheus)가 되었으며 [2.0.0](https://github.com/tinfoilhash/hasheus/releases/tag/v2.0.0)을 출시했습니다. 이 도구는 Nostr에 게시된 해시와 파일을 대조하며, 이제 신뢰하는 검증자로부터 설명과 URL을 가져오고 대용량 파일은 청크 단위로 해싱합니다. 검증 완료 배너는 게시된 바로 그 파일에서만 표시됩니다. 잘못된 형식의 프로필도 처리하고, 중복된 검증자를 제거하며, relay가 누락되면 오류를 반환합니다. 체크섬이 일치한다는 것은 파일 자체를 확인해 줄 뿐, 게시자가 그 파일에 대해 내세우는 주장까지 확인해 주지는 않습니다.

### Alby JS SDK {#alby-js-sdk}

[Alby의 JavaScript SDK](https://github.com/getAlby/js-sdk)가 [9.0.0](https://github.com/getAlby/js-sdk/releases/tag/v9.0.0)을 출시했습니다. 이제 NWC 클라이언트는 게시하는 각 요청마다 relay의 OK를 고정된 5초 동안 기다리고, OK가 도착하지 않으면 Nip47PublishTimeoutError로 실패합니다. 메서드별 응답 타임아웃은 변경되지 않았습니다. 복호화에 실패한 응답은 이제 reject되며, relay의 실패 메시지 텍스트는 보존됩니다([요청 오류 처리](https://github.com/getAlby/js-sdk/pull/597)). 호환성을 깨는 변경으로는 더 이상 사용되지 않는 multi_* 메서드가 제거되었으며, Nip47SingleMethod를 사용하는 코드는 Nip47Method로 옮겨야 합니다. relay OK는 relay가 요청을 수락했다는 뜻일 뿐, 결제가 성공했다는 의미는 아닙니다.

### Alby Hub {#alby-hub}

Nostr Wallet Connect를 통해 지갑을 제공하는 자체 호스팅 Lightning 노드 [Alby Hub](https://github.com/getAlby/hub)가 [1.24.4](https://github.com/getAlby/hub/releases/tag/v1.24.4)를 출시했습니다. 이번 패치는 허브의 NWC 지갑 서비스가 의존하는 네이티브 LDK 및 Go TLS 연결에서 침해된 인증 기관에 대한 신뢰를 제거합니다. CLN hold-invoice 플러그인의 시작 문제도 수정했습니다.

### Orchard {#orchard}

Flatpak 소프트웨어 카탈로그인 [Orchard](https://github.com/Letdown2491/orchard)가 [0.3.0](https://github.com/Letdown2491/orchard/releases/tag/v0.3.0)을 출시했습니다. 이번 릴리스는 [소프트웨어 릴리스 상호운용성](https://github.com/Letdown2491/orchard/pull/4)을 [NIP-82](/ko/topics/nip-82/), 그리고 ngit 또는 다른 NIP-82 도구를 통한 게시용 [Flatpak 에셋 준비](https://github.com/Letdown2491/orchard/pull/5)와 연결합니다. NIP-82는 아직 번호가 할당되거나 채택되지 않은 제안 단계의 소프트웨어 카탈로그 사양이므로, Orchard는 앞으로 바뀔 수 있는 초안을 구현하고 있는 셈입니다.

### Bell {#bell}

Nostr 대화를 모아 보여 주는 Android 애그리게이터 [Bell](https://njump.me/nevent1qvzqqqr4dupzpynsnxlt28xupkyf02qln9da4wuv3cg00gf7l3cu39hv6qdr3k9kqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpdljffezmc9dgwal6akc90mk3dye9gektu8s2cfptj37xrrt476wf42080)은 여러 계정의 답글과 인용을 하나의 시간순 목록으로 모읍니다. [0.1.0 릴리스 노트](https://njump.me/nevent1qvzqqqr4dupzpynsnxlt28xupkyf02qln9da4wuv3cg00gf7l3cu39hv6qdr3k9kqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzq0s4r2rh63clk2e97sr8kfx7874dequvnhdcf562ag28pwjxg3fmvvs3al)에 따르면 좋아요, zap, 단순 리포스트, 일반 멘션은 제외되며, 계정은 Amber로 서명하거나 보기 전용으로 유지됩니다. [0.6.0](https://njump.me/nevent1qvzqqqr4dupzpynsnxlt28xupkyf02qln9da4wuv3cg00gf7l3cu39hv6qdr3k9kqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqh7w3wy9773f599y90vm5c32xkr8uea57gvp3ce08x85254z06xvfrc5f8)부터 0.9.0까지의 릴리스에서는 계정별 뮤트 규칙과, 여러 항목을 선택해 읽음 처리할 수 있는 읽지 않은 항목 전용 보기가 추가되었습니다. 해당 릴리스 노트에 따르면 복구 시 서명된 답글과 반응을 원본 그대로 유지하며 자동으로 중복을 만들지 않습니다. [0.10.0](https://njump.me/nevent1qqsdu5x6ca9npnef9kfmcavpf6qelacc86rvcufa35mf67kdxm6f36qzyzf8pxd7k5wdcrvgj75plx2mm2acerss77snalr3eztwe5q68rvtvqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk09q3d2)과 [0.10.1](https://njump.me/nevent1qqsyv7r8a0e82ltdhawfctcwrk5n5a9lejaart2q3hxkquqfqqzxdgszyzf8pxd7k5wdcrvgj75plx2mm2acerss77snalr3eztwe5q68rvtvqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk8kg3j4)에서는 사용자가 개별 게시물을 기기에서 숨길 수 있으며, 실행 취소와 복원도 지원합니다. 숨기기는 relay에서 아무것도 삭제하지 않으며, 새 답글은 계속 표시됩니다. 스팸 신고는 게시물과 그 작성자를 모두 대상으로 하고, 명시적으로 선택한 계정에서 공개적으로 전송되며, 비공개 차단 역할을 하지 않습니다. [0.11.0](https://njump.me/nevent1qqsytpz6d4ctsfvpzrdgx23m7542y8wzjnn0qsctk4p5pp2hnwyugrszyzf8pxd7k5wdcrvgj75plx2mm2acerss77snalr3eztwe5q68rvtvqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkjh2y3n)은 사용자가 원본 게시물과 보낼 계정을 확인한 뒤 리포스트하는 기능을 추가합니다. 답글, 반응, 리포스트를 누가 할지는 계정 아바타로 고릅니다. 리포스트를 게시할 수 있게 되었다고 해서 단순 리포스트 알림까지 모아 보여 주게 된 것은 아닙니다. 캐시된 스레드는 불완전한 상태로 남을 수 있습니다. 선택적으로 켜는 백그라운드 수신은 Android의 전원 및 네트워크 규칙에 좌우되며, 상시 동작이나 즉각적인 전달을 보장하지 않습니다.

### SkateSpots {#skatespots}

[SkateSpots](https://njump.me/nevent1qvzqqqr4dupzqg88e9f588nx7wyz4wt0ura23w3yd4hmztqrkr95utwyvgachjepqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpas2cx4mzh73kytt49479xdtrs2q37llm848e0zhvs0y72296sv8c7ad0x)는 스케이트 스폿과 매장을 담은 커뮤니티 지도입니다. 버전 1.7.4에서는 종단 간 암호화 커뮤니티 채팅이 추가되었는데, 여기서는 커뮤니티 봇이 새 기기를 자동으로 승인하며 관리자도 승인할 수 있습니다. [1.7.0](https://njump.me/nevent1qvzqqqr4dupzqg88e9f588nx7wyz4wt0ura23w3yd4hmztqrkr95utwyvgachjepqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzq50n30vvchf923kmne5vj0ptk7ful6qldk37xva9x2ap2879e4rmaep40k)은 커뮤니티 relay를 스폿과 매장에 대한 권위 있는 소스로 삼았습니다. [1.7.3](https://njump.me/nevent1qvzqqqr4dupzqg88e9f588nx7wyz4wt0ura23w3yd4hmztqrkr95utwyvgachjepqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp8g4ah0nqaj796uuw0me3ck37azyjxp8gs9e3munfd7v5542snvp5wm656)은 이전 릴리스에서 도입된 비공개 크루 채팅의 Android 초대 QR 코드를 수정했습니다. [1.7.8](https://njump.me/nevent1qqsppdcrel94afrsluvt0gz4s2k079yvmne776w0juak38js857zsdszyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkuwx9gn), [1.7.10](https://njump.me/nevent1qqspp0kr4x4c6m5fw5glqtdv7r08jseq70mp8n224qqp6rzmm2rt5yszyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetke6cpl5), [1.7.15](https://njump.me/nevent1qqsq375v0ucwszn7s6wdatn2c9fgyxrcalmt7yazedav5zypt5d4pkqzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkj0vmg9), [1.7.19](https://njump.me/nevent1qqsr7xkz9evx70q47nzqr5wlsfs7cpzxaxy2ymzhxh4h9thy2s62n9qzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkgrmthk), [1.7.20](https://njump.me/nevent1qqsxn8f0az09eg75tnsc7kxlf3spwe4vfvh633te9k3mcsf3nhl3thszyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkqddtl9), [1.7.21](https://njump.me/nevent1qqsr9wdhzwznntvkcjzphdy0249esazdgg7k0spz370lw9mzj8jwsggzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk7dgt33), [1.7.22](https://njump.me/nevent1qqspx5m53qxctceqmva3dkynkswukl6zrwl4gr6mu3r0zucdwt96muqzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk977zdf) 릴리스는 이 크루 채팅을 확장합니다. 커뮤니티 채팅의 봇 승인과 달리 크루 채팅에서는 기존 크루 멤버가 QR로 새 기기를 승인하고, 멤버와 기기를 제거할 수 있으며, 창립자를 승격하면 관리자 tag가 다시 게시됩니다. 반응, 삭제 tombstone, 읽음 확인은 암호화된 MLS 제어 메시지로 전송됩니다. tombstone은 relay에서의 완전 삭제가 아니며, 자동 읽음 확인은 무음 서명자(silent signer)에서만 전송됩니다. 백그라운드 감시자는 관리자 키가 아니라 언제나 멤버 본인의 키를 사용하며, 가입 요청을 약 1분마다 [NIP-17](/ko/topics/nip-17/) DM이나 벨 알림으로 바꿔 줍니다. Amber 사용자의 경우 가입 알림은 벨을 열 때까지 대기하는 반면 무음 서명자는 이를 미리 불러올 수 있으므로, Amber가 백그라운드에서 프롬프트를 띄우는 일은 없습니다. 읽지 않은 항목 수는 대기 중인 NIP-17 봉투(envelope) ID를 복호화하지 않은 채 사용하고, 사용자가 직접 보낸 사본은 제외하며, 대화 주제를 드러내거나 확인해 주지 않습니다. 즉각적이거나 지속적인 백그라운드 전달은 보장되지 않습니다. 1.7.19부터 1.7.22까지의 릴리스는 명령 팔레트가 열려 있는 동안에만 실행되는 전역 데이터셋 검색도 추가했으며, 지도와 레이어 상태를 기억합니다. 저희는 이 변경 사항을 독자적으로 기기에서 테스트하거나 보안 감사하지 않았습니다.

### Emanator {#emanator}

멀티 계정 Nostr 클라이언트인 [Emanator](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqannu7pfrkl3daywutspdhdfp3ct4wyk0njcs69nlhufh6gm36a724p5x6)는 1.5.0부터 [NIP-17](/ko/topics/nip-17/) 비공개 대화를 새로 시작할 수 있습니다. 이전 릴리스에서는 기존 스레드에 답장만 할 수 있었습니다. 사용자는 메시징이 활성화된 발신 계정을 고른 뒤, 이름이나 [NIP-05](/ko/topics/nip-05/)로 연락처를 검색하거나 npub 또는 nprofile을 붙여 넣습니다. 기존 대화는 재사용되며, 수신자가 DM 수신함을 등록해 두지 않았다면 앱은 최선형(best-effort) 전달과 함께 레거시 옵션을 제공합니다. [1.4.1](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpx8h9aamsmuvu7fzkhc9n8v37m9rcnyhrc60sjuwrgftk8hhns02ahkkqn) 기준입니다. 재시도 시 이미 수락된 서명된 event는 그대로 유지됩니다. 어떤 relay도 수락하지 않은 오래된 event만 다시 서명하고 날짜를 갱신할 수 있습니다.

### Feather {#feather}

지난 #45호에서 0.9 시리즈 시점에 다뤘던 Android Nostr 클라이언트 Feather가 그 이후 [1.8.4](https://njump.me/nevent1qvzqqqr4dupzqmjxss3dld622uu8q25gywum9qtg4w4cv4064jmg20xsac2aam5nqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqqguewyhvswx5qkcn29ckc7mjsendh0wtc2u6n6l8wzvnvup0wt8y6q9ww)에 이르렀습니다. 1.x 릴리스 노트에 따르면 저장소가 공지한 relay를 통해 NIP-34 이슈를 네이티브로 탐색하고 제출하는 기능이 추가되었습니다. 서명된 작업은 이제 기기 내 outbox에서 대기하며, WorkManager가 이를 백그라운드에서 전달하면서 답글보다 상위 글을 먼저 보냅니다. [1.8.0](https://njump.me/nevent1qvzqqqr4dupzqmjxss3dld622uu8q25gywum9qtg4w4cv4064jmg20xsac2aam5nqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqny0jdx2y7gaxdwcmexndm6rk2qgtkxz3zq3cucdlxvdyl92sp532mdl79)은 초안 저장과 오프라인 전달을 지원하는 kind 20 사진 게시물을 추가했고, 1.8.4는 신고가 성공한 뒤 선택적으로 뮤트하는 기능을 추가했습니다. [1.7.0](https://njump.me/nevent1qvzqqqr4dupzqmjxss3dld622uu8q25gywum9qtg4w4cv4064jmg20xsac2aam5nqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp2qa3hycyvc8g7c7wt3a2zl06uneuu5xt8w38q87xqd4pq9uq89udwewmd) 이후로 번역은 별도의 Offline Translator 앱과 그 언어 팩을 통해 이루어지며, 클라우드 대체 경로는 없습니다.

### OUTKAST {#outkast}

Android Nostr 클라이언트인 [OUTKAST](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqg4n7egyu8slmmx6gtmus5stgf6fdsxr43rp9fz57ftv4ru5ettxrc4nc3)는 2.2.1에서 기기 내 Network 탐색 기능을 추가했습니다. 이 기능은 내가 팔로우하는 사람들이 최근 48시간 동안 좋아요를 누르거나 리포스트한, 팔로우하지 않는 계정의 노트를 보여 줍니다. 릴리스 노트에 따르면 순위는 반응, 답글, zap을 (sat 금액이 아닌) 횟수로 집계한 다음 친구 수와 최신성을 가중해 매기며, 순위 서버는 없습니다. 40개 이상의 계정을 팔로우하면 노트 하나에 최소 두 명의 친구가 관여해야 합니다. 결과는 노트 100개에서 멈추고 이전 페이지는 제공되지 않습니다. 릴리스 노트는 선택한 사람이나 목록으로 구성하는 사용자 지정 피드와, 편집본을 메타데이터 없는 JPEG로 저장하되 수정하지 않은 원본은 손대지 않고 업로드하는 사진 편집기도 설명합니다.

### CustID {#custid}

Nostr 서명 앱 [CustID](https://njump.me/nevent1qvzqqqr4dupzpw5cfkeqauh4qfmq3grjpaqd8l3n97mpcs94a4s0x946ypqgzv0fqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp6736dd3jl2ucdqs85ycw8yj9veluh4ug8jqwu3y0wfr06up4s7y8cfupa)는 0.2.2-beta부터 생체 인증으로 보호된 신원에 대한 NIP-46 ASK 요청에 생체 인증 승인을 요구합니다. 다만 최근에 인증을 마쳤다면 이 프롬프트를 대신할 수 있습니다. 이전 승인을 포함해 기억된 승인 및 거부 규칙은 이제 NIP-46과 NIP-55 모두에서 별도 알림 없이 적용됩니다. 자동 승인을 켜면 먼저 확인 경고가 표시되며, 이를 취소하면 아무것도 바뀌지 않습니다. 이번 베타는 자신이 게시하는 event에 [NIP-89](/ko/topics/nip-89/) client tag도 추가합니다. 이 tag는 기본으로 켜져 있어 어떤 앱이 event를 게시했는지 독자에게 보여 주며, Privacy 설정에서 끌 수 있습니다.

### Nostr Vault {#nostr-vault}

Nostr 클라이언트인 [Nostr Vault](https://njump.me/nevent1qvzqqqr4dupzqcdl0y9jp990kq6ftj0px6k0v9d7plxv9ju4kkk0khmvemlp3vrzqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpdeavwf9zysh2zcmlx7hevu7h3nk6nvtzlk05zsajkvewvt84z3zj929ve)는 3.0.0에서 선택적으로 켜는 FIPS 기기 연결을 추가했습니다. 주소나 QR 코드로 페어링하며, 덕분에 집에 있는 Mac이나 여분의 휴대폰이 vault 역할을 할 수 있습니다. vault는 노트와 기록을 동기화하고, 기존 사진을 메시를 통해 가져오며, 메시가 활성화된 뒤에는 재부팅 후 relay와 함께 시작됩니다. 공개 미디어를 게시하려면 여전히 공개 미디어 서버가 필요합니다. 이번 릴리스는 팔로우와 가입 과정에서 발생하던 계정 간 경쟁 상태도 수정했습니다. 또한 게시 성공을 알리기 전에 사용자 본인의 쓰기 relay가 게시물을 확인 응답할 때까지 기다리며, 낯선 사람이 보낸 DM은 Requests 뒤에 둡니다.

### Holoboard {#holoboard}

[Holoboard](https://njump.me/nevent1qvzqqqr4dupzpu0ekzvk6nl3ha6708jvepthez0tvvlxss2u07hhfnch5palsz7cqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzq0j3gw5m0602kdr606fgapm3c5f4sk230ahxxr8ryvdhusrlen4cwsqg0s)는 사람들이 비용을 지불하고 게시물을 올리는 보드입니다. 이번에 Android 1.1.0을 출시했으며, 이와 함께 웹사이트와 백엔드에는 결제로 마무리되는 안내형 Add to board 흐름이 추가되었습니다. 게스트는 텍스트와 링크, 또는 기존 Nostr 게시물을 제출할 수 있습니다. 준비된 인보이스는 같은 기기의 같은 브라우저 프로필에서 이어서 진행할 수 있으며, 인보이스 QR은 계정이나 연결된 지갑 없이도 계속 이용할 수 있습니다. APK 자체는 런처 아이콘과 스플래시 화면만 새로 바꿀 뿐이므로, 보드 관련 변경 사항은 이에 대응하는 웹사이트와 백엔드에 달려 있습니다. 이메일이나 비밀번호로 로그인하는 방식은 없습니다.

### Hopp {#hopp}

value-for-value 부스트를 지원하는 팟캐스트 앱 [Hopp](https://njump.me/nevent1qvzqqqr4dupzpx7mjedrw4lzxd5ekk4tmr79t0qvrayw88zdtt9vd5mm9ay0y9s7qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk7ks3v4gvr2ffqsedrlgm44xy9dlcq3clvptw4rwglrm9dm8stu2jp6t6)은 #45호에서 다룬 0.2.x의 신원 및 결제 작업에서 한 걸음 더 나아갔습니다. 0.3.0 버전은 Hopp 서버 없이 Nostr를 통한 암호화된 기기 간 동기화 및 복원 기능을 추가했습니다. 대상은 구독, 진행 상황, 즐겨찾기, Up Next, 청취 습관, 다운로드 설정입니다. 복원 시 기존 라이브러리는 그대로 유지되며, 상태 화면에서 relay 상태와 대기 중인 상태를 확인할 수 있습니다. 릴리스 노트에 따르면 결과를 알 수 없는 부스트 분배분은 중복 재시도로부터 보호되며, 이제 예산에 Release Boosting과 Boost2Unlock이 반영됩니다.

### Nostrautica {#nostrautica}

행사 동반 앱인 [Nostrautica](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp23s4qefknu9dzeefgkxuegzd0dsml4zs2gj0sppmqvcmeh7mp5q279sgs)는 [0.15.1](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpgrrf3n4vaeafhqhl7msnkvvscw6np9cup4e6pgm3f4x3yrz9mkxd24hwd)에서 오프라인 행사 팩을 추가했습니다. 이 팩은 신호가 약한 행사장을 대비해 참가자, 참가자 간 매칭, 강연, 행사 페이지, 게시물, 프로필 사진을 저장합니다. 채팅에는 멘션 이름 표시와 수정 및 삭제 기능이 추가되었고, 전송 대기 중인 메시지는 재시도하거나 폐기할 수 있습니다. 0.16.0 버전은 Marmot 그룹 메시징 라이브러리인 MarmotKit 0.14로 전환하여, 더 적은 그룹 relay 연결로 오프라인 동안 놓친 내용을 따라잡을 수 있게 했습니다. 또한 보존 기간 정리 과정에서도 읽지 않은 메시지를 유지합니다. 저장소 마이그레이션은 단방향이므로, 이후에는 이전 앱 버전이 지원되지 않습니다. 릴리스 노트는 White Noise 메신저나 웹과의 상호운용성에는 변화가 없다고 밝히고 있습니다.

### Staircase {#staircase}

relay.tools가 만든 Nostr 그룹 채팅 앱 [Staircase](https://njump.me/nevent1qvzqqqr4dupzqlxr9zsgmke2lhuln0nhhml5eq6gnluhjuscyltz3f2z7v4zglqwqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpw255ly0xpmr7vqxvn3t45z0clzu2nljrgjcrml9jpquvvyzd44ux0dqpc)는 0.1.25에서 Frequent 알림 모드를 추가했습니다. 이 모드는 대략 5분 또는 10분마다 확인한 뒤 연결을 끊습니다. 기기가 딥 슬립 상태일 때는 Android 스케줄링이 시점을 결정하므로, 백그라운드 전달은 즉각적이지도 않고 보장되지도 않습니다. Periodic 및 Frequent 모드는 네트워크가 복구되면 범위가 제한된 확인을 한 번 실행하며, 그 빈도는 최대 2분에 한 번입니다. Instant 모드는 변경되지 않았습니다. 그룹 가입 상태는 요청이 처리되거나 만료되면 대기를 멈추지만, 둘 중 어느 쪽인지는 알려 주지 않습니다. 사용자 지정 coordinator relay는 게시된 목록으로 덮어쓰이지 않고 계속 사용자가 제어합니다.

## 개발 중 {#in-development}

### Coracle {#coracle}

Nostr 웹 클라이언트 [Coracle](https://github.com/coracle-social/coracle)은 master 브랜치에 [라우팅 수정](https://github.com/coracle-social/coracle/pull/685)을 병합했습니다. 이제 Lists나 Groups 같은 메뉴 항목을 클릭했을 때 같은 모달이 이미 맨 위에 열려 있으면 아무 동작도 하지 않습니다. 이전에는 클릭할 때마다 동일한 패널이 하나씩 더 쌓였습니다. Escape 키를 누르면 이 패널들이 하나씩 닫혔습니다. 서로 다른 모달과 일반적인 페이지 이동은 이전과 같이 작동합니다. 이는 병합된 소스 코드이며 특정 릴리스에 묶여 있지 않습니다.

### nostter {#nostter}

Nostr 웹 클라이언트 [nostter](https://github.com/SnowCait/nostter)는 zap 흐름에 대한 수정 5건을 병합했습니다. 이제 [Nostr Wallet Connect pay_invoice 응답](https://github.com/SnowCait/nostter/pull/2746)은 올바른 결과 유형과 유효한 preimage를 갖추고 error 필드가 null이거나 생략된 경우에만 성공으로 간주됩니다. 형식이 잘못된 응답은 거부됩니다. [전용 rx-nostr 클라이언트](https://github.com/SnowCait/nostter/pull/2747)는 설정이 실패하더라도 항상 해제됩니다. 지갑 응답 없이 10초가 지나면 실패가 아니라 알 수 없는 결과로 처리됩니다. [인보이스 및 서명 오류](https://github.com/SnowCait/nostter/pull/2748)는 인라인으로 표시되고 재시도를 위해 금액과 코멘트를 유지하며, 인보이스 실패는 NWC 실패와 구분되어 보고됩니다. 반복해서 zap할 수 있도록 [zap 버튼은 활성 상태로 유지됩니다](https://github.com/SnowCait/nostter/pull/2750). 버튼의 주황색 표시는 QR 인보이스가 표시될 때에도 나타나는데, 이것이 수동 결제가 완료되었음을 확인해 주는 것은 아닙니다. [대화 상자를 다시 열면](https://github.com/SnowCait/nostter/pull/2752) 유휴 상태일 때에만 초기화됩니다. 인보이스나 서명이 도착한 뒤 대화 상자를 닫으면 새 NWC 결제는 중단되지만, 이미 제출된 결제는 계속 진행됩니다.

아직 [열려 있는 pull request](https://github.com/SnowCait/nostter/pull/2753)는 결과를 알 수 없는 상황 이후 QR 대체 경로로 결제하기 전에 지갑 내역을 확인하라는 경고를 표시하고, 지갑 자동 실행을 막는 내용을 담고 있습니다. 타임아웃이 발생했다고 해서 지갑이 결제 금액을 청구하지 않았다는 뜻은 아닙니다.

### Pollerama {#pollerama}

투표 및 피드 클라이언트인 [Pollerama](https://github.com/formstr-hq/nostr-polls)는 [relay별 요청 큐](https://github.com/formstr-hq/nostr-polls/pull/258)를 병합했습니다. 이 큐는 동시에 실행되는 요청 수를 조정하고, relay가 속도 제한을 걸면 백오프하며, 지나치게 큰 필터를 분할하고 relay URL을 정규화합니다. Mine packs 화면은 이제 상시 구독을 유지하므로, 느린 relay 응답도 여전히 표시됩니다. 앱에 알려진 재요청 문제는 아직 해결되지 않았으며, 다이렉트 메시지는 이번 변경과 함께 테스트되지 않았습니다.

### Grimoire {#grimoire}

Nostr 소셜 클라이언트 [Grimoire](https://github.com/purrgrammer/grimoire)는 [다이렉트 메시지 동기화 수정](https://github.com/purrgrammer/grimoire/pull/352)을 병합했습니다. 기록 커서는 과거의 일부 지점까지만 도달한 병합 relay 페이지에서 더 이상 전진하지 않습니다. 또한 중단 가드가 있어, 로그아웃으로 메시지와 읽음 표시가 지워진 뒤 복호화 패스가 이를 다시 채우는 일을 막습니다. 중단된 백필은 커서를 옮기거나 기록을 모두 소진한 것으로 표시하기 전에 멈춥니다. 남은 공백도 있습니다. 응답한 relay 하나만으로도 다른 relay가 누락된 상태에서 기록이 소진된 것으로 표시될 수 있으며, signer가 영구적으로 거부하더라도 여전히 커서가 전진합니다.

### nostr-vpn {#nostr-vpn}

피어 탐색에 Nostr 키를 사용하는 VPN인 [nostr-vpn](https://github.com/mmalmi/nostr-vpn)은 [모바일 재연결 수정](https://github.com/mmalmi/nostr-vpn/pull/77)을 병합했습니다. 이제 탐색 프로브를 보낼 시점이 이미 되었을 때, 클라이언트는 알려진 피어로 향하는 소진된 경로를 다시 활성화합니다. 이 동작은 최근에 아무것도 수신되지 않았고 연결된 경로나 대기 중인 경로가 없을 때에만 이루어지며, 최대 300초에 한 번으로 제한됩니다. 정상 경로와 대기 중인 경로는 건드리지 않으며, 와이어 포맷은 변경되지 않았습니다. 작성자는 이 수정을 셀룰러 네트워크가 아니라 격리된 네이티브 fixture에서 테스트했습니다. 병합된 두 번째 변경은 진단 출력에서 등록용 join secret과 가공되지 않은 데몬 상태를 제외하여 [doctor 번들에서 네트워크 join secret을 제거합니다](https://github.com/mmalmi/nostr-vpn/pull/97). Nostr 개인 키는 이미 그곳에서 가려져 있었습니다. 이 변경 이전에 공유된 번들은 계속 노출된 상태이므로, 번들을 공유한 적이 있는 사람은 해당 join secret을 교체해야 합니다.

관련된 여러 변경 사항은 아직 열려 있는 제안 단계이며, 병합되거나 릴리스되지 않았습니다. 저장된 비밀 정보와 관련해, 한 제안은 기존 마이그레이션 경로를 통해 [네트워크 join secret을 플랫폼 비밀 저장소에 보관](https://github.com/mmalmi/nostr-vpn/pull/120)하도록 합니다. 다른 제안은 [Windows 머신 sidecar secret에 대한 접근을 SYSTEM과 Administrators로 제한](https://github.com/mmalmi/nostr-vpn/pull/101)하는 것으로, Nostr 노드 키를 담고 있는 DPAPI 파일이 대상입니다. 이 제한은 다음번에 파일이 기록될 때에만 적용되며, 파일 생성과 ACL 적용 사이에는 짧은 공백이 있습니다. 사용자 지정 설정 경로는 대상에 포함되지 않으며, 작성자는 다중 사용자 Windows 머신에서 테스트하지 않았습니다. 서명된 멤버십과 관련해서는, 한 제안이 [roster 스냅샷이 더 이상 디스크와 일치하지 않는 가입 승인을 거부](https://github.com/mmalmi/nostr-vpn/pull/117)하도록 합니다. 그러면 관리자는 동시에 승인된 기기를 유지한 채 다시 불러와 재시도하게 됩니다. 또 다른 제안은 [관리자 시계 오차를 5분까지 허용하고 설정된 join signer를 항상 요구](https://github.com/mmalmi/nostr-vpn/pull/111)하는 것으로, 로컬 관리자 목록이 비어 있을 때에도 마찬가지이며 요청 secret에 대한 바인딩은 유지됩니다. 세 번째 제안은 [타임스탬프가 같은 roster 사이의 동률을 아티팩트 해시로 판정](https://github.com/mmalmi/nostr-vpn/pull/109)합니다. 두 roster를 모두 보는 피어들은 동일한 하나의 roster를 선택하게 되며, 각 roster는 자체 멤버십 내용을 그대로 유지합니다. 마지막 제안은 [딥 링크 가입 요청과 유료 exit provider에 대해 확인을 요구](https://github.com/mmalmi/nostr-vpn/pull/110)합니다. macOS와 Linux에서는 가입 링크가 명시적인 Add-device 단계를 기다리게 됩니다. macOS는 유료 provider 링크도 확인을 받을 때까지 보류합니다. 두 플랫폼 중 어디에서도 네이티브로 실행하는 모습은 시연되지 않았습니다. 모든 테스트 결과는 작성자가 보고한 것입니다.

### Buzz {#buzz}

데스크톱 및 모바일 클라이언트를 갖춘 커뮤니티 relay인 [Buzz](https://github.com/block/buzz)는 그룹 및 에이전트 관련 작업을 병합했습니다. 에이전트는 이 프로젝트의 [NIP-FI](/ko/topics/nip-fi/) [JWT 사양](https://github.com/block/buzz/pull/8401)에 따라 인증할 수 있으며, 이 사양은 발급자가 주장하는 사람 소유자를 검증합니다. 해당 소유자를 거부하거나 연결을 끊으면 그 소유자의 에이전트 세션이 종료되며, 소유자의 커뮤니티 멤버십을 근거로 에이전트를 받아들일 수도 있습니다. Huddle은 또한 현재 사용자나 Huddle 소유자의 [검증된 managed-agent 레코드를 받아들이며](https://github.com/block/buzz/pull/8544), 이는 [NIP-OA](/ko/topics/nip-oa/) 소유자 증명(owner-attestation) 봇 역할에 더해지는 방식입니다. 이 대체 경로는 호환성 정책이며, 알 수 없는 제3자 레코드는 신뢰하지 않습니다. 신원 증명도 아닙니다. 두 사양 모두 채택된 NIP가 아닙니다.

[오픈 공지 채널](https://github.com/block/buzz/pull/8143)은 `join_role=guest`를 통해 읽기 전용 게스트를 받아들일 수 있습니다. [목록에 표시되지 않는 오픈 채널](https://github.com/block/buzz/pull/8579)은 비회원의 탐색에서는 숨겨지지만, 채널 ID를 가진 사람이라면 누구나 읽을 수 있습니다. 입장 승인 event는 [최대 100명의 멤버를 추가할 수 있으며](https://github.com/block/buzz/pull/8575), 일부만 성공할 수도 있습니다. 지난주 열려 있는 제안으로 소개한 [채널 설정 수정](https://github.com/block/buzz/pull/8516)이 이제 병합되었습니다. 변경 사항은 관련 요청 및 알림과 함께 하나의 트랜잭션으로 커밋됩니다. 공개에서 비공개로의 전환이 실패하면 완전히 롤백되므로, 제거된 멤버가 그 롤백을 통해 다시 나타나는 일이 방지됩니다. 모바일에서는 [푸시 설정 실패](https://github.com/block/buzz/pull/8610)가 더 이상 앱을 망가뜨리지 않습니다. 앱은 제한된 횟수만큼 재시도하고 수동 복구 수단을 제공하며, 테스트는 모의 채널로 이루어졌고 APNs 기기 동작은 검증되지 않았습니다. [동기화된 음소거 설정 때문에 시작 화면이 비어 버리는 문제도 더 이상 발생하지 않으며](https://github.com/block/buzz/pull/8608), 이제 실제 DM 푸시 구독과 대조하여 확인합니다. 이 수정은 iPhone 로그 하나에 근거합니다. relay 메시에서는 하트비트 없이 5분이 지나면 [죽은 피어 레코드가 만료되며](https://github.com/block/buzz/pull/8503), 살아 있는 연결은 예외입니다.

더 최근에 병합된 내용은 릴리스에 포함되었는지 확인되지 않았습니다. [kind 9000 멤버십 추가](https://github.com/block/buzz/pull/8606)는 이제 roster 쓰기와 함께 커밋됩니다. 변경이 실패하면 둘 다 저장되지 않으며, 동일한 서명된 event로 재시도할 수 있습니다. kind 9001, 9021, 9022에는 기존의 공백이 그대로 남아 있습니다. [NIP-FI 섀도 모드 진단](https://github.com/block/buzz/pull/8634)은 이제 거부되었을 경우에 대해 검증된 Nostr 키와 고정된 비공개 사유를 기록하며, 토큰이나 클레임은 기록하지 않습니다. 이로 인해 입장 승인이나 집행 방식이 달라지지는 않습니다. 채택된 NIP에 속하지 않는 프로젝트 문서인 Buzz 자체의 [NIP-AP](/ko/topics/nip-ap/) [에이전트 사양](https://github.com/block/buzz/pull/8631)은 이제 settings에 클라이언트가 정의한 `agentType`를 요구합니다. 다른 유형의 settings로 실행하려 하면 거부되고, 필드가 없으면 기존의 레거시 의미가 유지되며, 유형을 바꾸면 이전 유형의 중첩된 settings가 폐기될 수 있습니다. [단독 에이전트 선택](https://github.com/block/buzz/pull/8616)은 가장 최신의 kind 30177 managed-agent 정책이 잘못된 형식일 경우 fail-closed 방식으로 동작합니다. 이전 데이터는 계속 제외됩니다. 에이전트는 소유자가 관리하는 이름으로 표시되며, 아트워크와 메시지 작성자는 여전히 프로필을 사용합니다.

모바일에서는 [호스팅 에이전트 생성, 목록 조회, 삭제](https://github.com/block/buzz/pull/8626) 기능이 NIP-OA 소유자 증명과 kind 30177 등록을 사용하며, 동일한 신원을 유지하는 영속적 재시도를 지원하고 비공개 지침은 보안 저장소에 보관합니다. 빌드 시점의 호스팅 게이트가 App Store 빌드와 내부 빌드에서 꺼져 있으므로, 이것이 일반 공개를 뜻하지는 않습니다. [호스팅 iOS 초대 콜드 스타트](https://github.com/block/buzz/pull/8617)는 초대 의도를 유지하고, 일치하는 키를 가져오며, 백업에서 복구합니다. 주요 경로는 작성자만 테스트했으며, 멤버십 대체 엔드포인트와 신규 가입은 아직 해결되지 않았습니다. [푸시 등록 복구](https://github.com/block/buzz/pull/8629)는 지수 백오프로 대기한 뒤, 401로 거부된 저장 요청을 범위가 제한된 새 challenge와 App Attest 키로 교체합니다. 400 또는 일시적 오류 이후에는 의도를 유지하고, 일반적인 404는 평소대로 처리합니다. 이 복구 기능은 실제 기기에서 확인되지 않았습니다. 사용자가 가입하지 않은 공개 채널로 연결되는 [메시지 링크](https://github.com/block/buzz/pull/8518)는 kind 39000 메타데이터를 가져와 읽기 전용으로 열리며, 비공개 채널과 DM의 접근 제한은 변경되지 않습니다. 재연결 중에는 링크가 대기열에 쌓이며, 느린 조회 하나가 이후 링크를 최대 8초까지 지연시킬 수 있습니다.

소스 기준 시점에 열려 있던 여러 pull request가 아직 병합되지 않은 상태였습니다. 기본적으로 비활성화된 `buzz_v1` capability는 클라이언트 측 읽음 상태를 [호출자 전용 NIP-98 사이드바, 읽음 상태 및 커버리지 API](https://github.com/block/buzz/pull/8639)로 대체하고, 사람별 리비전과 relay 전용 kind 24300 무효화 핑도 추가하게 됩니다. 이 capability가 없는 relay는 [NIP-RS](/ko/topics/nip-rs/)를 계속 사용하며, 대규모 데이터베이스는 먼저 인덱스를 동시(concurrent) 방식으로 구축해야 합니다. [스레드 요약](https://github.com/block/buzz/pull/8635)은 최신 답글 1,000개만 스캔하고 최근 작성자 10명을 반환하며, 실시간 업데이트는 pod당 초당 최대 한 번만 보내게 됩니다. 따라서 과거 참여자를 모두 나열하지는 않습니다. 반응에 대한 에이전트 응답은 마지막으로 유효한 [NIP-25](/ko/topics/nip-25/) `e` tag를 사용해 [반응 대상 메시지 아래에 스레드로 달리고](https://github.com/block/buzz/pull/8642), 필요하면 기존 앵커로 대체(fallback)하게 됩니다. Hermes 기반 에이전트에는 [채널과 DM에 게시하기 위한 에이전트 범위 MCP 셸](https://github.com/block/buzz/pull/8643)이 제공됩니다. 이 셸은 브리지 없이는 실행을 거부하고 자격 증명을 가리지만, 설치, 재시작, 실제 게시는 검증되지 않았습니다. [ACP 어댑터 수정](https://github.com/block/buzz/pull/8625)은 v1과 v2 초기화 이름을 모두 보내고, 안정 버전인 v1로 대체하며, 검증된 메이저 버전을 고정하게 됩니다. 이는 에이전트 전송 계층을 고치는 것으로, Nostr 프로토콜 변경이 아닙니다. 모바일 [소리 내어 읽기](https://github.com/block/buzz/pull/8637)는 휴대폰의 텍스트 음성 변환 엔진을 사용하며 코드, 링크, 첨부 파일은 건너뜁니다. 음성이 어디에서 처리되는지는 사용자가 선택한 엔진에 따라 결정됩니다. 독립형 [relay 부하 생성기](https://github.com/block/buzz/pull/8636)는 사람과 NIP-OA 에이전트를 시뮬레이션하고, 정해진 오류 및 지연 시간 한도를 넘는 실행을 실패로 처리하게 됩니다. relay 코드는 전혀 바꾸지 않으며, 프로덕션 규모를 입증하지도 않습니다.

### Mosaico {#mosaico}

[relay 기반 그룹(NIP-29)](/ko/topics/nip-29/)에서 에이전트를 조율하는 데몬인 [Mosaico](https://github.com/pablof7z/mosaico)가 [하트비트 기반 프레즌스](https://github.com/pablof7z/mosaico/pull/847)를 병합했습니다. 이제 에이전트는 90초 뒤로 설정되고 30초마다 갱신되는 [만료 타임스탬프(NIP-40)](/ko/topics/nip-40/)가 붙은 상태 event를 게시하는 동안에만 채널에 있는 것으로 간주됩니다. 로컬에서 실행 중인 프로세스만으로는 더 이상 프레즌스로 인정되지 않습니다. 에이전트가 오프라인인 동안에도 멤버십은 유지되므로 다시 활동을 이어 갈 수 있습니다. [재구축된 그룹 읽기 모델](https://github.com/pablof7z/mosaico/pull/845)은 relay가 바뀔 때마다 한 번씩 정규(canonical) 도착 커서와 함께 구성됩니다. 그래서 광범위한 그룹 구독이 교체되어도 채팅이 더는 유실되지 않습니다.

이후 병합된 세 건은 릴리스에 포함되었는지 확인되지 않았습니다. [교체 구독](https://github.com/pablof7z/mosaico/pull/854)은 이제 새 REQ ID를 사용하며, 기존 구독이 닫히기 전에 먼저 열립니다. 폐기된 프로필은 지연 시간에 민감한 경로 밖에서 게시되고, 채널을 떠나는 에이전트는 NIP-29 멤버 자격을 유지한 채 프레즌스를 철회합니다. 이를 뒷받침하는 프로브는 작성자가 수행한 것이며, 저희가 측정한 결과가 아닙니다. [선점(claim-first) 재시도 집계](https://github.com/pablof7z/mosaico/pull/851)는 스키마 27에 영속적으로 저장되며 relay 재생(replay) 후에도 유지됩니다. 단일 직렬 타이머에서 30초부터 1시간까지 지수적으로 백오프하고, 10회 실패하면 포기합니다. 누락된 event는 삭제로 취급되지 않습니다. 또한 보존 윈도가 4,096개 항목을 담기 때문에 모든 event의 전달이 보장되지는 않습니다. [그룹 전용 스냅샷](https://github.com/pablof7z/mosaico/pull/852)은 이제 그룹 소비자를 깨우며, 타임스탬프가 같은 교체 event는 [NIP-01](/ko/topics/nip-01/)의 규정대로 가장 낮은 event ID를 유지합니다. 콘텐츠만 바뀐 경우에는 여전히 일반 소비자를 깨웁니다. 누락된 부모에 대한 범위 한정 대체 처리는 다음 그룹 변경이나 15초 타임아웃까지 기다릴 수 있습니다.

### Sonar {#sonar}

Nostr, MLS 암호화, Bluetooth Low Energy 메시를 결합한 메신저 [Sonar](https://github.com/hedwig-corp/bitchat-to-sonar)가 [셀룰러 연결 환경의 시작 문제 수정](https://github.com/hedwig-corp/bitchat-to-sonar/pull/665)을 병합했습니다. 이 PR은 첫 화면 렌더링이 느린 원인을 스토어 잠금을 쥐고 있는 푸시 relay 연결(attach)에서 찾아냈습니다. Android에서는 로컬 노드가 이미 열려 있으면 시작 과정에서 해당 잠금을 건너뜁니다. 콜드 스타트 전에 푸시 등록이 노드를 연 경우가 그 예입니다. iOS에서는 앱이 렌더링할 수 있도록, 앱이 알림 서비스 확장에 연결 및 드레인(drain) 작업을 멈추라고 지시합니다.

### Shopstr {#shopstr}

Nostr 마켓플레이스 [Shopstr](https://github.com/shopstr-eng/shopstr)가 [지난주에 제안된](/en/newsletters/2026-10-21-newsletter/#shopstr) [리스팅 삭제 지원](https://github.com/shopstr-eng/shopstr/commit/2e11d0b6d7b8d5d3007c5393882a77dc2f0721e2)을 병합했습니다. 이제 판매자가 서명한 [event 삭제 요청(NIP-09)](/ko/topics/nip-09/)은 캐시에서 리스팅을 제거하고 툼스톤으로 처리합니다. 따라서 삭제된 상품은 캐시에서 다시 나타나거나 구매될 수 없으며, 그보다 새로운 재등록은 계속 표시됩니다. 그래도 일부 삭제는 여전히 누락됩니다. 리스팅보다 먼저 도착한 삭제는 무시되고, `k` tag가 없는 이전 요청은 relay 쿼리와 일치하지 않으며, 과거 삭제는 소급 반영(backfill)되지 않습니다. relay가 삭제된 event를 계속 보관할 수도 있습니다. 이와 별개로, [형식이 잘못된 gift wrap 메시지](https://github.com/shopstr-eng/shopstr/pull/614)가 더 이상 주문(Orders) 및 내 리스팅(My Listings) 화면을 멈추게 하지 않습니다. [판매자는 이제 자신의 주문을 볼 수 있으며](https://github.com/shopstr-eng/shopstr/pull/652), 다른 사용자는 여전히 403을 받습니다.

소스 기준 시점에 병합되지 않은 열린 pull request 세 건은 주문 무결성을 목표로 합니다. [#665](https://github.com/shopstr-eng/shopstr/pull/665)는 NIP-98 등록을 통해 각 주문의 참여자를 한 번만 기록하게 됩니다. 구매자는 인증 정보에서, 판매자는 서명된 리스팅에서 가져오며, 이후의 쓰기로는 이를 바꿀 수 없습니다. 등록이 실패해도 체크아웃은 중단되지 않으며, 새로 생긴 미해결 주문을 tag로부터 추측하지도 않습니다. 레거시 주문은 제한된 기준 시점까지만 적용되며, 주문 ID별로 상태를 저장하는 방식의 허점은 수정되지 않은 채 남습니다. #665에 의존하는 [#666](https://github.com/shopstr-eng/shopstr/pull/666)은 gift wrap([NIP-59](/ko/topics/nip-59/))된 주문 상태 메시지를 인증된 아무 발신자의 것이 아니라, 해당 주문에 기록된 구매자나 판매자가 보낸 경우에만 적용하게 됩니다. 미해결 주문은 대기 상태로 남습니다. 구매자의 결제 후 확인은 판매자 확인으로 간주되지 않으며, 위조된 메시지는 주문 상태를 바꾸지 않고 채팅으로만 남습니다. [#664](https://github.com/shopstr-eng/shopstr/pull/664)는 에스크로 등록과 판정을 위해 네트워크 keyset 조회 없이 Cashu v2 keyset 토큰 메타데이터를 읽고, proof 합계를 바로잡게 됩니다. 주문 생성 시의 토큰 디코딩은 여전히 별도의 수정이 필요합니다.

### Conduit {#conduit}

구매자 앱과 판매자 앱이 짝을 이루는 Nostr 마켓플레이스 [Conduit](https://github.com/Conduit-BTC/conduit-mono)이 [단일 암호화 계정 레코드](https://github.com/Conduit-BTC/conduit-mono/pull/711)를 병합했습니다. 이제 지갑 메타데이터, 시드, 네이티브 신원, 주소, 환경설정, 설정 진행 상황이 하나의 [임의 커스텀 앱 데이터(NIP-78)](/ko/topics/nip-78/) 레코드에 저장됩니다. 이 레코드는 [버전이 지정된 암호화 페이로드(NIP-44)](/ko/topics/nip-44/)로 암호화되고 서명, 소유자, 파생 신원이 검증되며, signer가 승인하면 두 앱 모두 이를 찾을 수 있습니다. 이번 전환은 하위 호환되지 않습니다. 이전 백업 및 복구 경로는 무시되고, 레거시 백업은 자동 마이그레이션 없이 그대로 남습니다. 그 밖의 병합으로는 로컬 브라우저 저장소에 보관되는 [기존 nsec을 이용한 로그인](https://github.com/Conduit-BTC/conduit-mono/pull/646)이 추가되었습니다. 상품군을 편집할 때는 [서명된 정확한 배송 조건](https://github.com/Conduit-BTC/conduit-mono/pull/647)이 요구되며, [체크아웃 복구 데이터는 IndexedDB로 옮겨져](https://github.com/Conduit-BTC/conduit-mono/pull/708) 저장 완료로 표시하기 전에 다시 읽어 확인합니다.

Conduit은 또한 [NWC SDK 8.1.1로 이전](https://github.com/Conduit-BTC/conduit-mono/pull/740)하여 이 SDK의 금액 검증, 횟수가 제한된 연결 시도, 닫힌 풀 처리, 진행 중 응답 관련 수정 사항을 들여왔습니다. Conduit의 지갑 선택, 암호화, 결제 정책은 바뀌지 않았습니다. 앱 배포 여부는 아직 확인되지 않았습니다. 초안 pull request 두 건은 소스 기준 시점까지 병합되지 않았습니다. [결제 활성화](https://github.com/Conduit-BTC/conduit-mono/pull/743)는 재시도로 초기화되지 않는 고정된 2분 실행 윈도 안에서 결제 상태를 영속 저장하고, 다시 읽어 확인한 뒤 전달하게 됩니다. Nostr 영수증, 비공개 계정 복구, 재고 또는 주문 이행 변경에는 각각 별도의 서명된 증거가 필요하게 됩니다. 이후 24시간 동안 보관되는 영수증이 결제 권한을 복원하지는 않으며, 실제 자금을 투입한 검증, 기기 검증, 메인테이너 검증은 아직 끝나지 않았습니다. [이벤트 전용 상품](https://github.com/Conduit-BTC/conduit-mono/pull/741)은 `conduit_event_only` 확장을 사용해 [NIP-99](/ko/topics/nip-99/) kind 30402 리스팅을 숨김으로 표시하게 됩니다. 이런 상품은 일반 카탈로그와 체크아웃에서 제외되며, 승인된 정확한 이벤트 회차 할당이 필요합니다. 숨겨진 서명 데이터는 여전히 공개 상태이고, 다른 클라이언트는 표준 숨김 플래그만 지원합니다.

### LNbits {#lnbits}

Lightning 지갑 및 계정 서버인 [LNbits](https://github.com/lnbits/lnbits)가 [Nostr 알림을 NIP-17 비공개 메시지로 보내는 옵션](https://github.com/lnbits/lnbits/pull/4260)을 병합했습니다. 관리자는 레거시 [NIP-04](/ko/topics/nip-04/) 암호화 메시지와 [NIP-17](/ko/topics/nip-17/) 비공개 다이렉트 메시지 중에서 고를 수 있으며, 새 설정의 기본값은 NIP-17 비공개 다이렉트 메시지입니다. NIP-17을 쓸 때 서버는 수신자의 DM 수신함 relay 목록을 조회합니다. 이때 NIP-05 relay를 탐색 힌트로 사용하고, 목록이 없으면 전송 대상으로도 사용합니다. 빈 목록이 게시되어 있으면 전송은 실패합니다. 각 전송은 30초로 제한되고 최소 하나의 수신함 relay가 수락해야 하며, NIP-04로 대체되는 일은 결코 없습니다.

### Zeus {#zeus}

모바일 Bitcoin 및 Lightning 지갑인 [Zeus](https://github.com/ZeusLN/zeus)는 [결제 후 새로 고침이 실패할 때의 Nostr Wallet Connect 예산 집계 수정](https://github.com/ZeusLN/zeus/pull/5389)을 [v13.2.4-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.2.4-rc1) 프리릴리스에 포함했습니다. [Nostr Wallet Connect make_invoice가 자체 인보이스를 반환하도록 한](https://github.com/ZeusLN/zeus/pull/5316) 이전 수정도 함께 들어갔습니다. 수정 전에는 [NIP-47](/ko/topics/nip-47/) 송금 후 새로 고침 오류가 나면 예산 집계를 건너뛰었고, 성공했을 수도 있는 결제에 대해 오류를 반환했습니다. 이제는 preimage가 반환되면 기존 fallback 경로를 통해 예산에서 차감됩니다. 타임아웃이 발생하면 결제가 목록에 없더라도 해당 금액을 대기 중인 지출로 묶어 둡니다. 진행 중인 LND 결제를 포함해 다른 허점은 남아 있을 수 있습니다. 뒤이어 나온 [v13.2.4-rc2](https://github.com/ZeusLN/zeus/releases/tag/v13.2.4-rc2)에는 의존성 업데이트만 담겼습니다.

그 후 더 새로운 수정 두 건이 소스에 병합되었으나, 어느 릴리스 후보에도 포함되었는지 확인되지 않았습니다. [기본 만료 시간 수정](https://github.com/ZeusLN/zeus/pull/5394)은 인보이스에 만료 필드가 없을 때 로컬 BOLT11 디코더가 사양상 기본 만료 시간인 3600초를 적용하도록 합니다. 이런 인보이스는 그동안 만료되지 않는 것으로 취급되었습니다. 그 결과 만료된 인보이스 결제를 막는 검사가 적용되지 않았고, `NostrConnectUtils`의 NWC 인보이스 검증에도 같은 허점이 있었습니다. [지갑 단위 백업 수정](https://github.com/ZeusLN/zeus/pull/5191)은 ecash 지갑마다 Nostr 민트 백업 타임스탬프를 따로 초기화합니다. 이 수정 전에는 다른 ecash 지갑과 같은 세션에서 시드로 복구된 지갑이 그 지갑의 타임스탬프를 물려받을 수 있었습니다. 그러면 자신의 더 오래된 relay 백업을 낡은 것으로 보고 버린 뒤 빈 민트 목록을 저장할 수 있었고, 이 때문에 자동 복원이 꺼졌습니다. 지갑 전환 후에 완료되는 백업은 여전히 잘못된 지갑에 타임스탬프를 기록할 수 있습니다. 이미 영향을 받은 지갑은 저장된 빈 목록을 그대로 유지하므로, Mint sync에서 수동 복원을 하거나 민트 URL을 다시 추가해야 합니다. 해당 지갑의 ecash는 민트에 그대로 남아 있습니다. 두 pull request 모두 기기 테스트는 하지 않았다고 밝히고 있습니다.

### npub.cash {#npubcash}

[npub.cash](https://github.com/cashubtc/npubcash-server)는 Nostr 신원 앞으로 오는 Lightning 결제를 받아 Cashu ecash로 변환합니다. 이 프로젝트는 [zap 영수증을 지불자가 요청한 relay에 게시하는 서버 변경](https://github.com/cashubtc/npubcash-server/pull/67)을 병합했습니다. 서버는 이미 zap 요청에 명시된 relay를 파싱하고 있었지만, 결제 완료 영수증을 게시할 때는 이를 무시했습니다. 이제 요청에 relay가 하나 이상 명시되어 있으면 영수증이 해당 relay로 전송됩니다. relay 목록이 없거나 비어 있는 요청은 여전히 설정된 기본 relay를 사용합니다.

### eHagaki {#ehagaki}

임베드 가능한 Web Component로도 제공되는 Nostr 웹 클라이언트 [eHagaki](https://github.com/Lokuyow/ehagaki)가 [1.31.0](https://github.com/Lokuyow/ehagaki/releases/tag/v1.31.0)과 [1.31.1](https://github.com/Lokuyow/ehagaki/releases/tag/v1.31.1)을 출시했습니다. 1.31.0 버전은 리포스트([NIP-18](/ko/topics/nip-18/)), 반응([NIP-25](/ko/topics/nip-25/)), 업로드된 미디어 관리를 추가했습니다. 또한 event가 외부 signer로 넘어가기 전에 아웃박스 라우팅(NIP-65)을 확정하며, 게시물 기록과 캐시를 로컬 Citrine relay에 보관할 수 있습니다. 이 버전의 IndexedDB 마이그레이션은 로컬에 표시되는 게시물 기록을 초기화하지만, 초안과 저장된 삭제 요청은 유지합니다. relay에 보관된 기록은 다시 가져올 수 있으나, 로컬에만 있는 게시물은 업그레이드 전에 백업하거나 내보내야 합니다. 1.31.1 버전은 Blossom의 kind 10063과 함께 kind 10096을 통해 [NIP-96](/ko/topics/nip-96/) 업로드 서버를 동기화하고, 사용 가능한 일부 relay 설정을 유지하며, 업로드 서버 목록 및 미디어 서버 동기화 수정을 포함합니다. 선언된 읽기 relay를 통한 [업로드 서버 목록 가져오기](https://github.com/Lokuyow/ehagaki/pull/366)는 다른 relay에서 타임아웃이 나더라도 유효하게 서명된 최신 목록을 유지합니다. 목록이 하나도 도착하지 않으면 설정은 바뀌지 않습니다. [미디어 서버 동기화](https://github.com/Lokuyow/ehagaki/pull/364)는 Blossom과 [NIP-96](/ko/topics/nip-96/) 기본 설정을 따로 처리하며, 조회에 실패한 뒤에는 결코 축소된 목록을 게시하지 않습니다.

병합된 다른 안정성 수정 사항들도 아직 릴리스 포함 여부가 확인되지 않았습니다. 401 또는 403 응답을 받은 뒤에는 사용자가 [미디어 화면에서 yabu.me 또는 nostrcheck.me NIP-96 서버에 가입할 수 있습니다](https://github.com/Lokuyow/ehagaki/pull/374). NIP-98 서명은 실제 POST URL과 본문 해시를 포괄하며, 계정이나 대상이 바뀌면 요청이 취소됩니다. 이중 전송은 가드가 막고, 결과를 알 수 없는 요청은 다시 보내지 않습니다. eHagaki는 비밀번호를 절대 대신 제공하지 않으며, 초대 코드나 결제 단계는 제공자의 공식 사이트에서 진행됩니다. [대용량 Blossom 파일 목록](https://github.com/Lokuyow/ehagaki/pull/363)은 크기가 제한된 로컬 스냅샷에서 한 번에 24개 항목씩 페이지를 나누어 보여 줍니다. 8 MiB 또는 10,000개 항목을 초과하는 응답은 거부하고, 계정·세션·서버가 바뀌면 스냅샷을 폐기합니다. 목록 끝에 도달했다는 것은 스냅샷을 모두 소진했다는 뜻이지, 서버에 더 이상 파일이 없다는 뜻은 아닙니다. [NIP-46 원격 서명자 복구](https://github.com/Lokuyow/ehagaki/pull/355)는 연결을 다시 구성하고, 대기 중이던 이전 요청은 30초가 지나면 재전송하지 않고 명시적으로 거부합니다. [Primal의 Blossom 서버로 보내는 업로드](https://github.com/Lokuyow/ehagaki/pull/367)는 이미 서명된 기존 인증 정보를 패딩이 포함된 표준 Base64로 인코딩하며, 다른 서버에는 계속 Base64URL을 사용합니다.

더 최근에 병합된 변경 사항 두 가지도 릴리스 포함 여부가 확인되지 않았습니다. 이제 [게시](https://github.com/Lokuyow/ehagaki/pull/393) 과정은 범위가 제한되고 검증된 relay 요청 대기를 공유하며, 전송과 진행 상황을 세션에 묶어 둡니다. 이를 통해 여러 개의 개별 타이머를 대체합니다. 처음으로 유효한 relay 확인 응답이 오면 성공으로 간주하며, 나머지 relay로의 전송은 그대로 계속됩니다. 진행 표시는 모든 relay에 전달되었다고 주장하지 않습니다. 계정을 전환하거나 로그아웃하면 백그라운드 전송이 중단됩니다. 게시물 기록에서는 요청 시 3초 제한 안에서 [관련 답글, 반응, 삭제를 새로 고칠 수 있습니다](https://github.com/Lokuyow/ehagaki/pull/391). 일부 요청이 시간 초과되더라도 이미 받은 결과는 유지되며, 삭제가 도착하지 않았다고 해서 삭제가 존재하지 않는다는 증거로 취급하지는 않습니다.

### Formstr Drive {#formstr-drive}

Nostr와 Blossom 기반의 암호화 파일 공유 앱인 Formstr Drive는 앞서 공개 제안 단계로 소개했던 [DriveKey 복구 작업을 병합했습니다](https://github.com/formstr-hq/formstr-drive/commit/e7f8c00583dc746e4a69b9ce4c97f8c3e1af851f). 앱은 통합 키링을 쓰기 전에 접근 가능한 모든 relay를 읽으므로, 이전 키들은 보이게 되는 대로 하나로 수렴합니다. 새 키는 앱 relay 4개 중 2개가 아무것도 반환하지 않고 기록이나 버전도 없을 때에만 생성됩니다. 응답하지 않는 쓰기 relay 때문에 이전 키가 한동안 여전히 보이지 않을 수 있습니다. 또한 이전 빌드는 새 JSON 형식을 읽지 못합니다.

프로젝트는 [계정마다 복호화된 파일, 공유, 폴더, outbox를 분리해 유지하도록 했습니다](https://github.com/formstr-hq/formstr-drive/pull/85). 계정을 전환하면 이전 계정에서 대기 중이던 서명과 가져오기가 차단됩니다. 다만 스테이징된 blob이 참조되지 않은 채 남을 수 있습니다. [이제 새 계정은 업로드 서버를 명시적으로 선택해야 하며](https://github.com/formstr-hq/formstr-drive/pull/88), 사용자 모르게 다른 서버로 자동 전환되는 일은 없습니다. 기존의 자동 기본값은 그대로 유지됩니다. 서버는 여전히 pubkey, 업로드 시점, 암호화된 바이트를 볼 수 있습니다. [중복 경고는 이제 같은 서버와 같은 폴더에 현재 존재하는 동일한 바이트가 있을 때에만 표시됩니다](https://github.com/formstr-hq/formstr-drive/pull/89). 계정 분리와 중복 확인 처리에 대한 Android 경로는 테스트되지 않았으며, 이 중 어느 것도 릴리스에 포함되었는지 확인하지 못했습니다.

### diVine {#divine}

Nostr용 짧은 동영상 클라이언트인 diVine은 메시징, 계정, 챌린지 관련 변경 사항을 병합했습니다. 초기 베타 릴리스에는 일반적인 내용의 노트만 있어, 이 중 어느 것도 배포된 빌드에 포함되었다고 확인되지 않았습니다. [필드별로 암호화된 계정 스냅샷](https://github.com/divinevideo/divine-mobile/pull/10413)은 환경설정, 배지 결정, 닫기(dismissal) 기록을 동기화합니다. 대기 중인 변경 사항은 로컬에서 재시도하고, 읽기가 불완전하면 안전하지 않은 게시를 차단합니다. DM 읽음 표시는 기존 프로토콜을 유지하고, 알림 읽음 처리는 서버 API를 사용하며, 모두 읽음으로 표시하려면 연결이 필요합니다. OS 권한, 자격 증명, 연령 동의는 기기에만 남습니다.

DM에서는 [메시지가 안전하게 대기열에 들어가면 작성기와 공유 시트가 닫힙니다](https://github.com/divinevideo/divine-mobile/pull/10500). 앱이 종료된 상태에서는 백그라운드 전송이 실행되지 않으며, 전송은 relay 확인 응답을 받은 뒤에만 완료로 집계됩니다. [실패한 재시도는 일관되게 시도 횟수 한도에 포함됩니다](https://github.com/divinevideo/divine-mobile/pull/10346). [형식이 잘못된 레거시 NIP-04 메시지는 폐기되고 원장에 기록됩니다](https://github.com/divinevideo/divine-mobile/pull/10522). 하지만 이미 저장된 빈 말풍선은 남아 있으며, 외부 서명자 및 다른 기기와의 호환성은 확인되지 않았습니다. [신뢰하는 발신자가 보낸 동영상 DM의 선택적 흐림 미리보기](https://github.com/divinevideo/divine-mobile/pull/10437)는 기본적으로 꺼져 있고, 켜더라도 항상 콘텐츠 경고와 함께 흐리게 표시됩니다. 동영상 자체는 그래도 다운로드되므로 흐림 처리가 네트워크 프라이버시를 제공하지는 않습니다. 그룹에서는 [멤버를 차단하면 그 멤버의 메시지만 숨겨지며](https://github.com/divinevideo/divine-mobile/pull/10156), 상대방은 여전히 내 메시지를 받는다는 경고가 표시됩니다. 방을 나간 상태는 저장되어 계속 유지됩니다. 새 그룹 생성은 기본적으로 꺼진 플래그 뒤에 그대로 남아 있습니다. 이 변경 사항들은 기존 그룹에 적용되며, 신뢰 및 안전(trust-and-safety) 검토는 아직 대기 중입니다.

이전에 공개 상태였던 기능 두 가지도 병합되었습니다. [수신한 DM 동영상 캐싱](https://github.com/divinevideo/divine-mobile/commit/25f9b7b8783ce11d70fc965936d1939b50f5f198)은 복호화된 파일을 계정별로 최대 30일 또는 300 MB까지 보관합니다. 신뢰하는 채팅과 팔로우한 사용자의 동영상은 자동으로 불러오므로 시청 시점이 미디어 호스트에 드러납니다. 모르는 사람의 동영상은 탭해야 불러옵니다. 서버에서 콘텐츠가 내려가더라도 캐시된 바이트가 즉시 무효화되지는 않으며, 캐시는 그보다 일찍 제거될 수도 있습니다. [사용자 이름 소유자 조회](https://github.com/divinevideo/divine-mobile/commit/489231071520bd066636384f4dd2a8e6d88f3f96)는 Divine 핸들 검색의 첫 페이지에 대해 이름 서버의 NIP-05 디렉터리를 확인하고, 활성 상태인 소유자만 고정합니다. 조회한 이름은 서버 로그에 남으며, 이는 일반적인 NIP-05 검증이 아닙니다.

[사람 목록(People lists)이 정식 출시 단계로 전환되며](https://github.com/divinevideo/divine-mobile/pull/10415), 이는 [탐색과 관리를 통합한 작업](https://github.com/divinevideo/divine-mobile/pull/9742)을 기반으로 합니다. 프로필 지원(support) 링크는 기본으로 켜져 있습니다. 편집기는 모든 relay에서 엄격한 원본 kind 0 읽기가 끝날 때까지 기다려, 숨겨진 제공자와 저장되지 않은 편집 내용을 보존합니다. 스토어 배포 채널을 통한 앱 빌드 승격과 백엔드 롤아웃은 아직 이루어지지 않았습니다. [클라이언트 표시 tag는 재시도와 메타데이터 편집 시 현재 NIP-89 설정을 따릅니다](https://github.com/divinevideo/divine-mobile/pull/10387). 서명 전에 다른 클라이언트의 client tag를 제거하지만, 이미 서명된 예약 게시물은 절대 변경되지 않습니다. 기본적으로 꺼져 있는 [인증된 외부 단축 링크](https://github.com/divinevideo/divine-mobile/pull/10507)는 정확한 NIP-98 POST와 본문을 2초 안에 서명하며, 실패하면 정식(canonical) URL로 대체됩니다. DM과 Nostr event에는 항상 정식 URL이 유지됩니다. 게이트웨이 생성 기능은 꺼진 상태로 배포되어 있으며, 앞으로 거쳐야 할 롤아웃 관문이 남아 있습니다.

크리에이터는 [명시적인 tag로 공개 동영상의 재사용을 허용할 수 있습니다](https://github.com/divinevideo/divine-mobile/pull/10467). 이 기능은 기본적으로 꺼져 있고, 변경 금지(no-derivatives) 라이선스 오디오가 쓰인 경우에는 게시 시점에 꺼진 상태로 고정됩니다. 이는 클라이언트 관례일 뿐 DRM이 아닙니다. 테스트 전용 챌린지 작업은 특수 테스트 빌드에서 [서명된 프로토콜 기반](https://github.com/divinevideo/divine-mobile/pull/10374), [규칙 및 동의 확인을 포함한 참가작 서명](https://github.com/divinevideo/divine-mobile/pull/10503), [계정별 영구 저장소](https://github.com/divinevideo/divine-mobile/pull/10509), [네이티브 검토 및 철회 흐름](https://github.com/divinevideo/divine-mobile/pull/10515)을 다룹니다. relay 확인 응답이 주최자 승인을 의미하지는 않습니다. 프로덕션 탐색 기능은 비활성화되어 있습니다. 백엔드 전달, 실제 계정을 사용한 인수 테스트, 클라이언트 간 릴리스 순서는 아직 남은 과제입니다.

더 최근에 병합된 변경 사항들도 릴리스 포함 여부가 확인되지 않았습니다. 수신자의 kind 10050 DM 수신함을 읽을 수 없는 경우, [NIP-17 보류 전송 대기열](https://github.com/divinevideo/divine-mobile/pull/10531)은 이제 relay가 이미 수락한 수신자용 gift wrap의 ID를 재사용합니다. 이렇게 해서 재시도 전반에 걸쳐 해당 wrap의 식별자가 유지됩니다. 재시도 중에 수신함을 찾으면 클라이언트는 공지된 relay에 다시 게시할 수 있습니다. 끝내 수신함이 나타나지 않으면 수락된 사본으로 확정하고, 이를 보관하는 일은 relay에 맡깁니다. 메시지는 여전히 실패(Failed)로 표시될 수 있습니다. 수신자에게 전달되었는지, 수신자가 읽었는지는 여전히 입증되지 않았으며, 반응과 삭제의 재시도는 이번 변경 범위에 포함되지 않습니다. [공개 알림 미리 불러오기와 시간대 새로 고침](https://github.com/divinevideo/divine-mobile/pull/10460)은 크기가 제한된 썸네일 캐시와 공유 SQLite 인덱스를 사용하며, DM과 캠페인은 제외합니다. 이 기능에는 일반적인 네이티브 릴리스와 함께 조율된 서비스 변경이 필요하며, 백그라운드 실행은 보장되지 않습니다. 동영상 편집기에는 [전환 효과 5가지](https://github.com/divinevideo/divine-mobile/pull/10543)가 추가되어 총 20가지가 되었고, 미리보기와 내보내기 모두에서 네이티브로 렌더링됩니다. 동작 줄이기 설정에서는 의도적으로 미리보기 타일을 제한합니다. 플래시 간격은 디졸브로 대체될 수 있습니다. 네이티브 구현을 실제 환경에서 테스트하지는 않았습니다.

소스 기준 시점에 병합되지 않은 공개 풀 리퀘스트가 4건 있었습니다. 앞선 정보 스티커 작업 위에 쌓인 [소셜 동영상 스티커](https://github.com/divinevideo/divine-mobile/pull/10540)는 멘션(`p`), 해시태그(`t`), 링크(`r`) 메타데이터를 담은 작고 평평한 구조의 스티커 tag를 기록하게 됩니다. 플레이어는 탭할 수 있는 영역을 겹쳐 표시하고, 외부 링크를 열기 전에 경고하게 됩니다. 다른 클라이언트는 이 tag를 구현하지 않는 한 동영상에 입혀진 스티커만 보게 되며, 이 tag는 승인된 NIP가 아닙니다. [플래그로 제한된 Concord 채팅](https://github.com/divinevideo/divine-mobile/pull/10536)의 멘션은 신원 정보를 인증된 암호화 메시지 안에 유지하게 됩니다. 앱 내 알림은 사용자가 열어 본 방에서, 팔로우하고 있고 차단하지 않은 발신자에게서만 오며, 최대 50행까지 표시되고 읽음 상태가 저장됩니다. OS 푸시 알림이나 공개 채팅 롤아웃으로 이어지지는 않으며, 신원 충돌, 재전송(replay), 차단 확인은 범위가 한정된 테스트로만 검증되어 있습니다. [NIP-17 rumor tag](https://github.com/divinevideo/divine-mobile/pull/10534) 변경은 반응 작성자를 실제 kind와 함께 한 번만 지정하고, 래핑된 삭제에서는 오해를 부르는 `p` tag를 제거하게 됩니다. gift wrap은 이미 올바른 수신자에게 주소가 지정되어 보내지고 있었으므로, 이 변경이 수신자 정보 유출을 고치는 것은 아닙니다. 이미 대기열에 들어간 rumor는 그대로 유지됩니다. 다른 클라이언트에서의 동작은 테스트되지 않았고, 방 분류(room-filing)와 관련된 절충점도 남아 있습니다. [다음 네이티브 빌드](https://github.com/divinevideo/divine-mobile/pull/10532)는 기존 단축 링크 공유를 기본으로 켜게 되며, 웹 버전은 계속 꺼진 상태로 둡니다. 비활성화, 로그아웃, 오류 경로에서는 전체 정식 URL을 유지합니다. 스토어 배포, 서비스 준비 상태, 기기 확인은 입증되지 않았습니다.

### rust-nostr {#rust-nostr}

Rust로 작성된 Nostr 프로토콜 라이브러리 모음인 rust-nostr는 [구독 재발행 방식에 대한 호환성을 깨는 변경](https://github.com/nostrdevkit/nostr/pull/1495)을 병합했습니다. 이제 `SubscriptionData`는 각 relay의 현재 EOSE 상태를 보여 줍니다. 재발행 시에는 연결이 끊긴 상태에서도 CLOSE와 저장된 필터의 REQ를 하나의 원자적 단계로 대기열에 넣습니다. 이는 대기열에 들어가는 방식을 보장할 뿐, 두 프레임이 모두 relay에 도달한다는 것까지 보장하지는 않습니다. 알림 공백에서 복구할 때 더 이상 구독을 조용히 누락하거나 중복 요청을 보내지 않습니다. 그래도 이전 REQ에서 늦게 도착한 EOSE 메시지나 event가 새 REQ와 겹칠 수 있는데, 전송 구간(wire)에는 이를 구분할 수단이 전혀 없기 때문입니다. 이는 병합된 소스이며, 릴리스에 포함되었는지는 확인하지 못했습니다.

### nostr-sdk-ffi {#nostr-sdk-ffi}

다른 언어에서 rust-nostr의 SDK를 사용할 수 있게 해 주는 바인딩인 nostr-sdk-ffi는 [NIP-44 v2 대화 키에 대한 원시 접근](https://github.com/nostrdevkit/nostr-sdk-ffi/pull/96)을 병합했습니다. 덕분에 Concord 호스트는 더 이상 자체 ECDH 및 HKDF 코드를 번들로 포함할 필요가 없습니다. 이 기능은 기존 도출 로직을 얇게 감쌀 뿐이며, 새로운 암호 기법을 추가하지 않습니다. 작성자는 Python 빌드와 함께, 양쪽에서 동일한 키를 얻은 왕복 테스트 결과를 보고했지만 전용 단위 테스트는 추가하지 않았습니다. 이는 병합된 소스일 뿐입니다.

### NDK {#ndk}

Dart용 Nostr 개발 키트인 NDK는 호환성을 깨는 프리릴리스인 [0.11.0-dev.2](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.2)를 게시했습니다. 이는 안정 버전 0.11.0이 아니며, JavaScript NDK와는 관련이 없습니다. 이번 릴리스에는 [NIP-49](/ko/topics/nip-49/) [비밀번호로 암호화된 ncryptsec 키와 샘플 UI](https://github.com/relaystr/ndk/pull/896)가 추가되었습니다. 릴리스 노트에 따르면 복호화 시 logN의 범위를 제한하고, 알 수 없는 보안 바이트를 거부하며, 도출된 버퍼를 0으로 초기화합니다. 이러한 주장은 노트와 병합된 소스에 근거한 것이며, 독립적인 감사나 테스트 벡터 실행 결과는 확인하지 못했습니다. [이제 요청은 연결 또는 전송 실패 정보를 담은 notSent 결과를 보고하며](https://github.com/relaystr/ndk/pull/911), 연결할 수 없는 relay에 대한 요청은 응답할 수 있는 relay나 필터가 더 이상 남지 않으면 시간 초과를 기다리지 않고 종료됩니다. [브로드캐스트는 event를 전송 중으로 표시하기 전에 서명자가 있는지 확인하고](https://github.com/relaystr/ndk/pull/908), [zap 요청 ID는 저장된 created_at을 사용합니다](https://github.com/relaystr/ndk/pull/907). 또한 [NIP-11](/ko/topics/nip-11/) [relay 메타데이터는 공유 캐시를 통해 필요할 때 가져오므로](https://github.com/relaystr/ndk/pull/887) 더 이상 매번 동기화를 막지 않습니다.

이번 프리릴리스에는 이전에 소스로만 존재하던 변경 사항도 포함되어 있습니다. [relay URL이 중복된 NIP-65 목록이 이제 올바르게 병합되어](https://github.com/relaystr/ndk/pull/914) 읽기와 쓰기 표시를 합치고 outbox 쓰기 relay 집합을 보존합니다. 작성자는 단 한 차례의 관찰에서 프로필 932개 가운데 잘못 읽힌 목록 5개를 확인했습니다. [선택 사항인 BUD-06 업로드 사전 확인](https://github.com/relaystr/ndk/pull/902)은 업로드 자체의 인증 정보를 사용해 서버가 blob을 수락할지 묻고, 그 상태와 이유를 보고합니다. 실제 업로드가 거부될 때도 이제 같은 방식으로 보고합니다. 404는 지원 여부를 알 수 없다는 뜻이며, 확인을 통과했다고 해서 업로드 성공이 보장되지는 않습니다. [NIP-77 조정(reconciliation) 시간 초과에 대한 호환성을 깨는 변경](https://github.com/relaystr/ndk/pull/888)은 단일 시간 초과를 열기 시간 초과와 유휴 시간 초과로 나누고, 타입이 지정된 오류를 제공합니다. 인증을 기다리는 시간은 여기서 제외됩니다. 전체 기한이 없으므로 계속 진행되는 동기화는 무한히 실행될 수 있습니다. 이 변경이 실제 relay에서 검증되었는지도 확인하지 못했습니다.

Open pull request들은 [네거티브 캐싱을 포함한 식별자 키 기반 NIP-05 캐싱](https://github.com/relaystr/ndk/pull/937), [NIP-77용 ID와 타임스탬프를 반환하는 캐시 API](https://github.com/relaystr/ndk/pull/933), [WebSocket 준비 상태 처리](https://github.com/relaystr/ndk/pull/932), [전체 NIP-11 필드](https://github.com/relaystr/ndk/pull/931), [연결이 거부되었을 때의 완료 처리](https://github.com/relaystr/ndk/pull/930)를 제안합니다. 최근 상태 확인에서도 여전히 열려 있는 또 다른 제안은 [브라우저 및 Flutter 플랫폼 passkey](https://github.com/relaystr/ndk/pull/909)로 계정을 생성하고 복구하려는 것입니다. 이 제안은 파생 키 모드와 저장 키 모드, 그리고 명시적인 레거시 메타데이터를 갖춘 초안 단계의 passkey 신원 설계를 따릅니다. 알 수 없는 핸들은 거부되며 결코 새 계정으로 취급되지 않습니다. 또한 저장된 등록 정보를 유지하기 전에 복구를 독립적으로 검증해야 합니다. 작성자는 모든 passkey 제공자에 걸친 상호운용성이 아직 검증되지 않았다고 밝힙니다.

### Applesauce {#applesauce}

Nostr용 TypeScript 라이브러리 모음인 Applesauce에는 changeset을 동반한 새 소스 변경이 있으며, 이에 대응하는 릴리스가 있다고 주장하지는 않습니다. [독립형 메시징 클라이언트와 명시적 relay 인증](https://github.com/hzrd149/applesauce/commit/a4f50406cdd625534a486b7d47369d59d004a24f)은 고정된 계정을 위한 NIP-04 및 NIP-17 클라이언트를 추가합니다. 이 클라이언트는 명시적인 NIP-42 인증 요청을 보내고, 미리 준비된 서명된 전송을 재시도합니다. [범위가 지정된 래핑 대화와 rumor 저장소](https://github.com/hzrd149/applesauce/commit/056038ed7108c3f113035a06011a5f7acdf8365f)는 서명자나 네트워크 작업을 시작하지 않고 kind 14 rumor와 스레드 모델을 노출합니다. 복호화는 기본적으로 꺼져 있습니다. 래핑된 전송에는 보낸 사람을 포함한 모든 참여자의 kind 10050 relay가 필요하며, relay의 수락이 상대방의 수신을 의미하지는 않습니다. [제한된 복호화 콘텐츠 캐시 복원](https://github.com/hzrd149/applesauce/commit/d6ac42102747feb72372ac5970ce2743e4b685ca)은 기본 동시성이 8이며, 1로 설정하지 않으면 event 순서가 바뀔 수 있습니다. 이러한 평문 캐시의 범위 지정과 암호화는 앱이 직접 해야 합니다. 그 뒤를 이어 [NDR 전송 계층과 별도의 Cordn 코디네이터 클라이언트](https://github.com/hzrd149/applesauce/commit/907a9591de867899aa7c84de1c4aa40628307a17)가 추가되었습니다. NDR은 자체적인 별도 ratchet 상태를 영구 저장해야 하며, Submitted는 상대방의 수신이 아니라 로컬 인계를 의미합니다. Cordn은 전송만 담당하고, 예제에서는 보류된 상태이며, MLS를 구현하지 않습니다. [창별 Kehto ContextVM 통합](https://github.com/hzrd149/applesauce/commit/24ad6e9650e20cc92950c3fccbc0ac0263f6d443)은 각 napplet 창에 임시 ContextVM 신원을 부여하지만, 계정 인증이나 결제는 포함하지 않습니다. [앱이 소유하는 지속형 입금과 nutzap 복구](https://github.com/hzrd149/applesauce/commit/cd483f5a610bf6fe8be7719ae5bb0dd0638c3296)가 도입되면서, 새로운 지갑 입금과 상환에는 이를 사용하는 애플리케이션이 제공하는 복구 저장소와 mint의 NUT-09 복원이 필요합니다. 저널에는 사용 가능한 proof, secret, blinding factor가 영구 저장되므로, 저널을 암호화하고 계정별로 범위를 지정해야 합니다. 재개(resume)는 명시적으로 호출될 때만 실행됩니다. 재개 시에는 서명된 ID를 재사용하며, relay가 수락을 확인할 때까지 저널을 유지합니다. 취소해도 인보이스가 무효화되지는 않습니다. [동기식 지갑 상태를 갖춘 일괄 타임라인 스냅샷](https://github.com/hzrd149/applesauce/commit/1042bc595c35cb6199a76776daab482916beda57)은 타임라인 업데이트를 16ms 단위 구간으로 묶으며, 지갑 토큰 상태는 동기식으로 유지됩니다. [COUNT 요청 스케줄러](https://github.com/hzrd149/applesauce/commit/564643fd648f5456387b54b3c8eddb79f165f46b)는 [지난주에 제안되었으며](https://github.com/hzrd149/applesauce/pull/106), 이제 병합되었습니다. 이 스케줄러는 동시성 상한 8에서 시작해 첫 번째 rate limit 또는 전송 오류가 발생할 때까지 상한을 두 배씩 늘립니다. 오류가 발생할 때마다 상한을 절반으로 줄이고 cooldown을 추가합니다. 타임아웃은 상한을 낮추지 않은 채 CountFailure로 나타납니다. 지연 시간은 relay 선택의 참고로만 쓰입니다. relay 세 개로 수행한 벤치마크는 일반적인 성능 주장을 뒷받침하기에 여전히 부족합니다.

### eventstore {#eventstore}

Nostr event용 저장소 백엔드를 모은 fiatjaf의 라이브러리 [eventstore](https://github.com/fiatjaf/eventstore)가 두 가지 쿼리 수정을 병합했습니다. 이를 포함한 태그 릴리스는 확인되지 않았습니다. 이제 모든 백엔드가 [NIP-01](/ko/topics/nip-01/)의 [빈 필터 목록](https://github.com/fiatjaf/eventstore/pull/79) 규칙을 따릅니다. 비어 있는 ids, authors, kinds 또는 tag 목록은 아무것도 일치시키지 않으며, 누락된(nil) tag 목록은 여전히 아무런 제한도 두지 않습니다. [LMDB event 카운팅 수정](https://github.com/fiatjaf/eventstore/pull/78)은 일치 항목을 찾은 뒤 HyperLogLog 커서를 앞으로 이동시킵니다. 따라서 카운트가 더 이상 끝없이 멈춰 있지 않습니다. 또한 필터에 author, kind, tag 조건이 없으면 카운팅에서 해당 검사를 더 이상 적용하지 않습니다. 이전에는 이 검사 때문에 0이 반환되었습니다.

### zsp {#zsp}

Android 앱을 Nostr에 게시하기 위한 Zapstore의 명령줄 도구 zsp가 [버전 2.0.0을 출시했습니다](https://github.com/zapstore/zsp/releases/tag/v2.0.0). [해당 태그의 README](https://github.com/zapstore/zsp/blob/v2.0.0/README.md)는 사람이 C1 서명 인증서의 소유권을 증명하는 마법사와, 에이전트에게 게시 지침을 제공하는 `zsp skill` 명령을 안내합니다. README는 에이전트에게 keystore나 그 비밀번호, 어떤 개인 키도 제공하지 못하도록 금지하므로, 증명은 사람의 몫으로 남습니다. 이번 릴리스는 또한 [JKS와 PKCS12 keystore를 내용으로 감지하므로](https://github.com/zapstore/zsp/commit/f767a1c4c98ba7130dd355f8da95afde6eeb8e08), .jks 또는 .keystore라는 이름의 PKCS12 저장소도 마법사와 게시 경로 모두에서 로드됩니다. 이 버전으로 게시하는 것은 테스트하지 않았습니다.

### nsite-gateway {#nsite-gateway}

Nostr에 게시된 정적 웹사이트를 제공하는 nsite-gateway가 [버전 3.6.6을 출시했습니다](https://github.com/hzrd149/nsite-gateway/releases/tag/v3.6.6). [소스 변경](https://github.com/hzrd149/nsite-gateway/commit/e7bbff215e23c0f3d9e23ee0ca14f5a2fb5e62dd)은 Applesauce 7로 업그레이드하고 event 만료 기능을 복원합니다. 이전 버전은 업스트림의 타이머 클램핑 버그를 피하려고 만료 관리자를 비활성화된 것으로 의도적으로 교체해 두었습니다. 그 때문에 만료된 사이트 event가 게이트웨이 저장소에 무기한 살아 있을 수 있었습니다. 업스트림 수정이 적용되면서 게이트웨이는 다시 일반 event 저장소를 사용합니다. 여기서 만료는 게이트웨이가 보관하고 제공하는 대상을 결정할 뿐이며, relay나 제3자 캐시에서 event를 삭제하지는 않습니다. 배포된 게이트웨이는 테스트하지 않았습니다.

### 44billion {#44billion}

Nostr 앱 런처인 44billion이 [권한을 기억하는 방식을 변경했습니다](https://github.com/44Billion/44billion/commit/4eb2cd9beecd8bb209dc7db47e99f338aacc5ac9). 저장된 권한 부여는 이제 앱, 권한 이름, event kind, 범위에 묶입니다. 와일드카드인 kind -1 권한 부여는 더 이상 특정 kind를 승인하지 않습니다. 범위는 번역된 레이블이 있는 등록된 kind와 범위 쌍에 대해서만 세분화됩니다. 알 수 없는 범위는 kind 전체를 대상으로 하는 빈 범위로 대체되며, 레지스트리는 비어 있는 상태로 시작합니다. IndexedDB 스키마 버전 5는 시작 시 버전 4의 권한 부여를 의도적으로 초기화하고 지원되지 않는 범위 지정 권한 부여를 제거하지만, 다른 앱 데이터는 유지합니다. 맞춤형 개인 암호화 API에는 승인된 표준이 아닌 NIP-44 v3 방식의 헬퍼가 포함되어 있습니다. 이는 소스 변경이며, 확인된 릴리스나 배포는 없습니다.

더 최신 소스에는 [앱 데이터 접근 설정](https://github.com/44Billion/44billion/commit/9800ff204c3994c269b3dc7acdba8614a1819997)이 추가되었습니다. 이 설정은 기억된 권한 부여를 앱별로 묶어 보여 주며, 사용자는 새로고침 없이 개별 권한 부여 하나 또는 앱 전체를 철회할 수 있습니다. 철회는 향후의 보호된 요청에만 영향을 줍니다. 이미 저장되거나 복사된 데이터는 삭제되지 않으며, 이미 진행 중인 작업은 중단되지 않을 수 있습니다. [Blossom 에셋 캐시 변경](https://github.com/44Billion/44billion/commit/9bc2265a125a302ba61b09d13f52b2a8615218a9)은 본문 전체의 SHA-256이 일치하고 그에 맞는 검증 완료 마커가 저장된 뒤에만 캐시된 에셋을 완전한 것으로 취급합니다. 이전 캐시의 임시 청크는 다시 검증되며, 스트리밍은 더 이상 잘못된 최종 청크를 보고하지 않습니다. 그렇다고 검증 전에 어떤 바이트도 노출되지 않는다는 뜻은 아니며, 새로운 바이너리 릴리스도 없습니다.

### Blossom Servers {#blossom-servers}

Blossom Servers 디렉터리는 각 서버 URL에 대해 [커뮤니티 기능 보고서를 추가했으며](https://github.com/hzrd149/blossomservers/commit/b3546fb745c0859094157b0eb20e9b29fc2443a9), 각 보고서에는 작성한 기여자가 표시됩니다. 수동 주장과 브라우저 관찰 결과는 별도로 관리됩니다. 수동 주장은 90일, 브라우저 관찰 결과는 24시간이 지나면 필터에서 제외됩니다. 검사는 HTTP 응답과 서버가 알리는 메서드, 그리고 인증 및 결제 챌린지를 살펴봅니다. 익명 브라우저 검사는 아무것도 업로드하지 않은 채 68바이트 PNG에 대한 메타데이터를 제시하는 HEAD 요청을 보냅니다. 따라서 200 응답이 실제 업로드가 작동함을 증명하지는 않습니다. 토론 로딩에는 이제 범위가 지정되며, 이전에 암시되던 운영자 권한 대신 기여자 표시가 사용됩니다. 보고서는 누가 서버를 운영하는지에 대한 증거가 아닙니다. 전 세계적인 가동 시간이나 BUD의 완전한 준수 여부에 대해서도 아무것도 알려 주지 않으며, 기여자끼리 의견이 다르거나 기여자가 틀릴 수도 있습니다. 배포나 릴리스는 확인하지 않았습니다.

더 최신 소스는 [설정 가능한 앱 relay와 조회 relay를 추가하고](https://github.com/hzrd149/blossomservers/commit/9ff8112963d68dee9c92d698740e47a23df7caf1), NIP-65를 통해 계정과 outbox를 읽습니다. 기존의 공개 kind 10086 조회 목록이 있으면 그것이 우선합니다. 저장 시에는 공개 목록이 이미 있는 경우에만 이를 갱신하며, 그렇지 않으면 로컬에만 남습니다. 로컬 게시 기록은 최소 한 개의 relay가 event를 확인 응답한 뒤에만 갱신됩니다. 다만 이것이 모든 relay가 event를 받았다는 뜻은 아닙니다. 릴리스나 배포는 확인되지 않았습니다.

### Ditto {#ditto}

Soapbox의 Nostr 클라이언트인 Ditto는 트랜스코딩된 동영상을 iOS에서 재생할 수 있도록 [결함이 있는 WebCodecs 인코더가 생성한 H.264 메타데이터를 수정했습니다](https://gitlab.com/soapbox-pub/ditto/-/commit/1c30cbac). 이 수정은 avcC 레코드에서 중복된 SPS 및 PPS NAL 헤더 바이트와 잘못된 예약 비트를 감지합니다. 그리고 Mediabunny muxer가 MP4 메타데이터를 쓰기 전에 이를 복구하며, 올바른 형식이거나 인식되지 않는 레코드는 그대로 둡니다. 버전 2.45.1이 출시되었지만, 이 버전에 해당 수정이 포함되어 있는지는 확인하지 않았고 실제 iOS 기기에서 재생을 테스트하지도 않았습니다. 이 변경은 모든 코덱이나 동영상이 아니라 이 H.264 결함을 대상으로 합니다.

### Amber 데스크톱 서명기와 Android NIP-46 수정 {#amber-desktop-signer-and-android-nip-46-fix}

Android Nostr 서명기인 Amber는 10월 27일 Compose 기반 데스크톱 NIP-46 서명기(Windows/macOS/Linux)의 소스를 병합했습니다. 이 서명기는 Android의 앱별 및 kind별 권한 모델을 그대로 따릅니다([커밋](https://github.com/greenart7c3/Amber/commit/1c12bb17e72d5b4ad46753062c1681d4af64adeb)). NIP-55는 계속 Android 전용입니다. 데스크톱 코드는 여러 계정을 지원하고, 앱별 relay와 기록을 갖춘 nostrconnect/bunker 연결도 지원하며, Tor와 트레이 알림 기능도 갖추었습니다. 키는 필수 Argon2id 패스프레이즈로 보호되는 암호화된 PKCS12 저장소에 보관되며, 계정별 데이터베이스도 암호화됩니다. 데스크톱 패키징이나 런타임 동작은 확인하지 않았습니다.

데스크톱 서명기가 아닌 Android 앱에 병합된 별도의 변경은 [계정이 로그아웃한 뒤 NIP-46 relay 구독과 연결 필터를 새로 고칩니다](https://github.com/greenart7c3/Amber/commit/2fbb1ee7bea7d5df574db5ca70b73841e8ba500d). 그 결과 Amber는 삭제된 계정의 키에 대한 수신 대기를 중단합니다. 민감한 정보가 가려진 잠금 화면 알림에는 이제 요청 설명도 표시됩니다. 이로써 알림은 더 유용해지지만, 프라이버시가 강화되지는 않습니다. 두 Android 변경 중 어느 하나라도 포함한 새 안정 릴리스는 확인되지 않았습니다.

### noStrudel napplet 인텐트와 동기화된 앱 데이터 {#nostrudel-napplet-intents-and-synced-app-data}

noStrudel 웹 클라이언트가 여러 소스 변경을 병합했으며, 확인된 태그나 배포는 없습니다. napplet 간 인텐트는 카탈로그와 z/i 매니페스트 선언을 통해 해석됩니다. 수락된 페이로드는 대상 프레임이 로드된 뒤 런타임이 증명한 발신자 ID와 함께 전달됩니다. 지원되지 않는 인텐트는 거부되며, 명시적 대상 핸들러는 사용자 확인이 필요합니다([커밋](https://github.com/hzrd149/nostrudel/commit/e0211136e71dac6de2bb8af2c0d9e291b02df9ba)). 설치된 napplet과 기본 핸들러는 NIP-44로 암호화된 kind 30078 앱 데이터에 3-way 병합 방식으로 계정별로 동기화됩니다([커밋](https://github.com/hzrd149/nostrudel/commit/887a6194c8cbab9ce6d780eb62961714777f72f5)). 선택된 [NIP-66](/ko/topics/nip-66/) relay 모니터는 암호화된 NIP-78 앱 데이터를 통해 동기화됩니다([커밋](https://github.com/hzrd149/nostrudel/commit/5a20096f4bcdfbd7ff86b4676cd5653d637ea4bf)). NIP-17 메시지는 캐시된 gift wrap을 불러오고, 세션당 한 번 DM relay에서 30일 분량을 대조합니다. 지원되는 경우에는 NIP-77을 사용하며, 그보다 오래된 기록은 요청 시 가져옵니다([커밋](https://github.com/hzrd149/nostrudel/commit/ce95080547485fb403c68f71ce6ad0404f42d230)).

### Nostr Feedz 보관 처리 {#nostr-feedz-archived}

RSS와 Nostr 장문 콘텐츠 및 동영상을 결합했던 Nostr Feedz는 이제 README에 보관 처리되어 더 이상 유지 관리되지 않는다고 명시하고 있습니다([커밋](https://github.com/PlebOne/Nostr-Feedz/commit/3b6f6967e532e1f0f4a3503354737cebc3350895)). 이 공지는 개발을 이어 가는 포크로 PrivKey의 [Readstr](https://github.com/privkeyio/readstr)를 안내합니다. 이는 유지 관리 상태의 변경입니다. GitHub에서 저장소가 보관됨으로 표시되는지, 계정과 데이터가 이전되는지는 확인하지 않았습니다.

### Zap Cooking의 보호된 목록, 서명기 수정, passkey 가입 {#zap-cooking-guarded-lists-signer-fixes-and-passkey-signup}

Nostr 레시피 공유 클라이언트인 Zap Cooking은 대규모 웹 소스 변경을 병합했으며, 배포나 릴리스는 확인되지 않았습니다. 저장된 kind 30001 목록에 쓸 때는 이제 먼저 읽기를 수행하며, 쓰기는 계정별로 직렬화됩니다. 쓰기 과정에서는 가장 최신의 완전한 기준본에 있는 외부 tag와 암호화된 콘텐츠를 보존합니다. relay 목록을 알 수 없거나 quorum이 부족하면 쓰기를 거부합니다([#869](https://github.com/zapcooking/frontend/pull/869)). quorum을 충족하려면 목록을 지원하는 EOSE 응답이 최소 두 개 있어야 하고, 여기에 더해 목록을 지원하는 사용자 쓰기 relay의 절반이 필요합니다. nostr.wine의 빈 응답으로는 목록이 없다는 것을 증명할 수 없습니다([#878](https://github.com/zapcooking/frontend/pull/878)). 사용자 지정 컬렉션도 같은 보호된 쓰기 경로를 공유하며, 대기열에 있던 이전 작업은 새로운 보호 조건 아래에서 다시 실행됩니다([#885](https://github.com/zapcooking/frontend/pull/885)). 또한 집계된 빈 EOSE만으로는 더 이상 목록이 비어 있는 것으로 표시되지 않습니다([#872](https://github.com/zapcooking/frontend/pull/872)).

명시적인 인증 방식을 도입하여 서명기 클래스를 혼동하게 만들던 프로덕션 minification 버그를 수정했습니다. 이에 따라 NIP-46과 [NIP-07](/ko/topics/nip-07/) 암호화가 오래된 로컬 키가 아닌 활성 서명기를 사용합니다. NIP-46에서는 relay 지갑 백업이 계속 차단됩니다([#896](https://github.com/zapcooking/frontend/pull/896)). 저장이나 반응에서 시작된 로그인은 로그인 후 해당 동작을 재개합니다. 대기 중인 zap은 금액과 대상을 유지하지만, 여전히 Send를 눌러야 합니다. 서명기가 거부하면 낯선 키로 몰래 다시 서명하지 않고 오류를 표시합니다([#867](https://github.com/zapcooking/frontend/pull/867)).

가입 시 신원은 로컬에서 생성되며, passkey로 암호화된 볼트 동기화가 기본으로 켜져 있습니다. 동기화가 꺼져 있거나 업로드가 실패하면 백업 키가 필요하고, Google Drive는 복원 전용입니다([#893](https://github.com/zapcooking/frontend/pull/893)). 프롬프트 한 번으로 끝나는 WebAuthn PRF 설정에서는 이후 볼트 복호화가 성공해 볼트를 확인하고 평문 키를 제거할 때까지 볼트가 미확인 상태로 남고, 평문 nsec도 브라우저에 남습니다([#907](https://github.com/zapcooking/frontend/pull/907)). 이 프롬프트를 가입 과정까지 확장하는 방식은 인증이 아닌 서명되지 않은 등록에 의존합니다. 새로 발급된 서버 챌린지를 가진 사람이라면 누구나 검증을 통과하는 등록을 위조할 수 있으며, credential ID를 아는 공격자는 미확인 항목(TTL 30일)을 교체해 실제 사용자의 동기화를 막을 수 있습니다([#911](https://github.com/zapcooking/frontend/pull/911)). 이는 문서화된 트레이드오프이며 보안 보장이 아닙니다.

노트 링크는 관측된 relay 힌트를 최대 세 개까지 담은 [NIP-19](/ko/topics/nip-19/) nevent로 인코딩됩니다. 덕분에 클라이언트가 복제본이 적은 event를 찾기 쉬워지지만, 가용성이 보장되지는 않습니다([#873](https://github.com/zapcooking/frontend/pull/873)). 프로필의 Replies에는 event를 루트로 하는 [NIP-22](/ko/topics/nip-22/) kind 1111 댓글이 포함되며([#877](https://github.com/zapcooking/frontend/pull/877)), 좌표 파서 수정으로 URL d-tag를 가진 레시피가 팩과 플랜에 계속 남게 됩니다([#888](https://github.com/zapcooking/frontend/pull/888)). 코드 작성자가 직접 수행한 감사에서 query-pubkey 우회 문제가 발견되어 프리미엄 레시피 페이월 실험은 종료되었으며, 기존 kind 35000 게시물은 저장된 콘텐츠로 읽을 수 있습니다([#862](https://github.com/zapcooking/frontend/pull/862)).

아직 병합되지 않은 공개 제안 하나가 뮤트 목록을 대상으로 합니다([#921](https://github.com/zapcooking/frontend/pull/921)). 이 제안에서는 뮤트 목록을 가져올 수 없었던 경우가, 가져오기에 성공해 목록을 반환하거나 목록이 없다고 반환한 경우와 구분된 채로 유지됩니다. 가져올 수 없었던 결과를 빈 목록으로 5분간 캐시하던 동작도 중단됩니다. 파싱 실패는 재시도되고, 비공개 뮤트의 복호화가 실패하면 경고가 표시됩니다. 알림 벨을 열면 목록을 다시 불러오게 됩니다. 목표는 아무 표시 없이 오래된 상태로 남은 빈 뮤트 목록 때문에 뮤트된 작성자가 알림에 들어오는 일을 막는 것입니다. 모든 실패 상황에서 콘텐츠를 차단하도록 만드는 변경은 아니며, 배포되지도 않았습니다.

### Lumilumi NWC zap 결제 {#lumilumi-nwc-zap-payments}

Nostr 웹 클라이언트인 Lumilumi에는 Nostr Wallet Connect(NIP-47)를 통해 탭 한 번으로 zap 인보이스를 결제하도록 하는 초안 pull request가 있습니다([#1120](https://github.com/TsukemonoGit/lumilumi/pull/1120)). 지출용 연결 URI는 로컬에만 저장되며, 평문 kind 30078 설정 백업에서는 제외됩니다. 지갑이 nip44_v2를 알리면 요청에 NIP-44를 사용하고, 그렇지 않으면 NIP-04로 대체합니다. 작성자는 실제 결제 없이 모의 지갑으로 동작을 확인했으며, 이 초안은 저희 소스 기준 시점에 병합되지 않은 상태였습니다.

### Wisp 식별자 검색 {#wisp-identifier-search}

저희 소스 기준 시점에 병합되지 않은 Wisp Nostr 클라이언트의 공개 pull request는, 검색이 [NIP-50](/ko/topics/nip-50/) 텍스트 쿼리로 넘어가기 전에 붙여 넣은 NIP-19 및 NIP-05 식별자, hex 키, 웹 엔티티 링크를 인식하도록 합니다([#681](https://github.com/barrydeen/wisp/pull/681)). 조회에는 relay 힌트와 로컬 캐시가 사용됩니다. 검색은 쿼리한 relay들로부터 최대 15초 한도까지 EOSE를 기다리는 동안 결과를 스트리밍하므로, 느린 relay가 더 이상 누락되지 않습니다. 작성자는 실제 기기가 아닌 에뮬레이터에서만 테스트했다고 보고합니다.

### Zapstore Android TV 지원 {#zapstore-android-tv-support}

Nostr 기반 앱 스토어인 Zapstore에는 Android TV를 위한 v2 공개 pull request가 있으며, 저희 소스 기준 시점에는 병합되지 않았습니다([#407](https://github.com/zapstore/zapstore/pull/407)). 이 변경은 32비트 ABI를 매칭하고 리모컨만으로 조작하는 Leanback 포커스를 지원하며, 설치 권한 화면을 사용할 수 없을 때의 대체 경로도 제공합니다. Arti가 없는 32비트 빌드는 Direct 전용 연결임을 명시적으로 표시하는 반면, Arti가 빠진 64비트 빌드는 fail closed 방식으로 동작합니다. TV 빌드는 배포용이 아닌 테스트용 로컬 디버그 서명자를 사용합니다. 작성자가 수행한 단 한 번의 TV 테스트에서는 공개 번들을 사용할 수 없었기 때문에 로컬에서 빌드한 relay를 사용했습니다.

### strfry 보안 강화 및 NIP-11 제안 {#strfry-hardening-and-nip-11-proposals}

C++로 작성된 Nostr relay인 strfry에는 저희 소스 기준 시점에 병합되지 않은 제안이 두 건 있습니다. [#281](https://github.com/hoytech/strfry/pull/281)은 JSON 깊이, 압축 해제된 페이로드, 큐, 메트릭 레이블에 상한을 두고, 빈 negentropy 필터로 인한 크래시를 수정하며, 긴 tag에 대한 인덱스를 해싱하는 방식으로 relay 감사 결과 SF-01부터 SF-13까지에 대응합니다. DB 형식 4로 전환되므로, 도입하는 측은 데이터를 내보낸 뒤 다시 가져와야 합니다. 통과한 테스트는 작성자 본인의 것입니다. 초안 [#278](https://github.com/hoytech/strfry/pull/278)은 실제로 적용되는 [NIP-11](/ko/topics/nip-11/) limitations와 선택 사항인 fees 및 payments_url만 알리도록 합니다. payment_required의 기본값은 false이며, 설정된 가격이 결제를 구현하지는 않습니다.

### nostrcheck-server Bark 결제 {#nostrcheck-server-bark-payments}

Nostr 미디어 호스팅 서버인 nostrcheck-server에는 barkd(Bark) 결제 제공자를 추가하는 초안 pull request가 있습니다([#62](https://github.com/quentintaranpino/nostrcheck-server/pull/62)). 이 변경은 barkd의 REST API를 통해 Lightning 인보이스를 생성하고, 선택적으로 402 응답에 파일별 X-Ark BIP-321 URI를 첨부하며, 같은 Lightning 인보이스를 대체 수단으로 제공합니다. 같은 Ark 서버에 있는 지갑은 Ark로 결제하고 그 밖의 지갑은 Lightning을 사용하며, 정산된 결제 한 건으로 파일 잠금이 한 번 해제됩니다. 테스트에는 모의 barkd가 사용되며, 이 변경은 공개 상태인 BUD-07 pull request #61에 의존합니다. 저희 소스 기준 시점에 병합되지 않았고, share.yabu.me에서 제공되는 기능도 아닙니다.

### mattn nostr-relay 유료 쓰기 {#mattn-nostr-relay-paid-writes}

저희 소스 기준 시점에 병합되지 않은 mattn의 nostr-relay 초안 pull request는 Bark 지갑을 통한 선택적 유료 쓰기 기능을 추가하며, 이 기능은 기본적으로 꺼져 있습니다([#37](https://github.com/mattn/nostr-relay/pull/37)). pubkey는 선택적인 kind 필터와 함께 barkd를 통해 쓰기 수수료를 선불로 지불하게 되며, 크레딧이 없는 작성자는 결제 URL이 담긴 restricted: 응답을 받습니다. 충전에는 BIP-321 URI 또는 NWC를 통해 Ark나 Lightning이 사용되며, 수수료는 NIP-11에 명시됩니다. 테스트에는 모의 데몬이 사용되며, 이 기능을 트리 안에 둘지 훅 뒤에 둘지는 아직 정해지지 않았습니다.

### ContextVM 재연결 재전송 방지 {#contextvm-reconnect-replay-guard}

Nostr 위에서 MCP를 전달하는 ContextVM에는 relay 재연결 이후의 중복 실행을 막기 위한 TypeScript SDK용 공개 pull request가 있습니다([#113](https://github.com/ContextVM/sdk/pull/113)). 서버 전송 계층은 닫힐 때까지 검증된 event ID를 보관하고, 크기가 제한된 별도의 envelope 캐시가 다시 래핑된 중복을 차단합니다. 메모리 사용량은 전송 계층의 수명 동안 고유한 검증 event가 늘어날수록 증가합니다. 이 수정은 저희 소스 기준 시점에 병합되지 않았으며, 릴리스된 패키지에도 포함되어 있지 않습니다.

### Kehto 셸 미디어 재생 및 승인 {#kehto-shell-media-playback-and-approvals}

Nostr napplet용 웹 셸인 Kehto는 [10월 28일에 NAP-MEDIA 재생 기능을 병합했습니다](https://github.com/kehto/web/pull/354). 이제 Paja와 playground 호스트는 정책을 거쳐 동작하는 오디오 및 비디오 플레이어를 공유합니다. 이 플레이어는 유한한 URL 및 Blossom 소스에는 브라우저 코덱을 사용하며, MediaSource가 해당 코덱을 지원하는 경우 라이브 HTTPS MP3 또는 ADTS AAC 스트림을 응답이 끝나기 전부터 재생합니다. 세션 권한은 엔드포인트, 소스 창, ACL에 묶인 상태로 유지됩니다. 권한이 철회되거나 해제되면 Blob URL이 폐기되고, 재생이 멈추며, 스트림이 취소됩니다. 호스트 전용 ResourceService.openStream 메서드는 기존의 엔드포인트 출처 권한 부여와 정책을 사용하며, 리소스 와이어 메시지를 새로 추가하지 않습니다. terminal delivery도 그대로 남아 있습니다. 기존 sendCommand 별칭도 계속 작동합니다. 이와 별도로, 감지 가능한 2인자 콜백은 경고와 함께 계속 작동합니다. 단일 인자 레거시 콜백은 command 객체로 옮겨 갑니다. 브라우저 리졸버는 HTTPS가 아닌 URL, 자격 증명, 사설 IP 리터럴을 거부합니다. 리디렉션과 리퍼러도 비활성화합니다. DNS를 검사할 수는 없으므로 조회 시점의 사설 주소 보호는 보장하지 않습니다. 프로덕션 리졸버에는 DNS 시점 검사가 필요하며, 브라우저 기본값은 CORS와 사설 네트워크 보호에 의존합니다. HLS, DASH, 라이브 Ogg, Nostr 소스, 큐, 영속 저장, 포커스 시 자동 재개는 여전히 지원되지 않습니다. 작성자는 155개의 Chromium 테스트와, 수정하지 않은 Funclet 아티팩트로 112초간 라디오를 재생한 결과를 보고했으며, 저희는 이를 다시 실행하지 않았습니다. 이는 소스 수준의 작업일 뿐입니다. 배포된 Napplet 0.32 패키지에는 일부 초안 타입이 빠져 있습니다. NAP-MEDIA는 여전히 초안이며, 릴리스 기준의 적합성은 아직 주장되지 않았습니다.

병합된 두 번째 변경은 [서명 및 게시 승인을 버전별로 적용되도록 합니다](https://github.com/kehto/web/pull/357). 각 승인은 검증된 게시자, 아티팩트 해시, 활성 서명자에 묶입니다. 승인은 철회할 수 있으며, 서명 전용 승인과 게시 전용 승인은 따로 구분됩니다. 기존 권한이 사용자 모르게 상향되는 일은 없습니다. 변경 가능한 개발용 URL에 대한 동의는 해당 로드 동안에만 유효하며, 엔드포인트나 계정이 바뀌면 대기 중인 요청은 거부됩니다. NAP-LINK는 호스트 모달에서 명시적으로 클릭한 뒤에만 noopener를 사용해 링크를 엽니다. 이 변경은 외부 CVM 라디오 소스 전반에 대해 테스트했다고 주장하지 않으며, 소스 병합만으로 npm 릴리스가 확인되는 것도 아닙니다.

### Pact {#pact}

에이전트 관계와 운영자 동의를 위한 Nostr 프로토콜인 [Pact](https://github.com/bobodread876/pact/pull/17)는 이제 Nostr Wallet Connect 응답을 인증합니다. 각 결과에는 지갑의 서명이 있어야 하고 해당 요청을 참조해야 하며, Pact는 결과 유형과 결제 해시를 확인하고 반환된 preimage가 있으면 그것도 함께 확인합니다. 상환 처리에는 원자적 원장 쓰기와 함께 요청 소비 및 재시도에 대한 보호 장치가 추가되었고, 동의 위조 경로도 추가로 차단되었습니다. [MCP 결제에 상한을 두는 후속 변경](https://github.com/bobodread876/pact/pull/18)은 `PACT_MCP_ALLOW_PAYMENTS=1`가 설정되지 않는 한 MCP 결제를 꺼 두며, 기본 1,000 sat 상한을 명시된 금액과 BOLT11 금액 양쪽에 대해 확인합니다. 비공개 inbox 창은 이제 wrap 200개에서 멈추고, 잘림이 발생했음을 표시합니다. 작성자의 테스트는 모의 객체에 의존합니다.

### nostr.watch {#nostrwatch}

Nostr relay 모니터인 [nostr.watch](https://github.com/sandwichfarm/nostr-watch/pull/961)는 명시적인 FIPS 탐색 및 전송 지원을 추가했으며, 오버레이 조회가 더 이상 공개 DNS-over-HTTPS로 넘어가지 않습니다. 모니터에는 FIPS 데몬이나 프록시가 포함되어 있지 않고 익명성도 제공되지 않으므로, DNS와 IPv6 라우팅은 여전히 호스트가 제공합니다. [더 엄격해진 npub 검사](https://github.com/sandwichfarm/nostr-watch/pull/964)는 파싱된 `.fips` 호스트 이름 안에 있는 npub만 허용합니다. [자동 NIP-11 및 NIP-05 프로브는 앱이 소유한 ServiceWorker로 옮겨졌으며](https://github.com/sandwichfarm/nostr-watch/pull/959), 이로써 관찰된 확장 프로그램 주도 탐색 경로에서 소유 탭 컨텍스트가 제거되었습니다. 이는 통제된 확장 프로그램 fixture를 사용해 기본 Firefox 155에서 확인되었습니다. [적합성 테스트 모음](https://github.com/sandwichfarm/nostr-watch/pull/960)에는 범위가 제한된 NIP-01 검사 15개와, 독립적인 연결을 지원하는 대화 계층이 들어 있습니다. 작성자가 보고한 것은 테스트 통과와 격리된 메시 실행 결과이며, 공개 relay 감사나 브라우저 보안 감사는 아닙니다.

### Bitcredit Core {#bitcredit-core}

Nostr를 사용하는 P2P 신용 및 어음 프로토콜인 [Bitcredit Core](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1060)는 이제 블록 작업이 로컬에 무엇이든 저장하거나 그 효과를 발생시키기 전에 쓰기 relay가 하나 이상 연결되어 있는지 확인합니다. 복구 시에도 깔끔하게 다시 초기화됩니다. 지난주 공개 상태라고 전했던 [후보 체인 검증](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1059)은 그 뒤 병합되었으므로, 체인은 저장되기 전에 검증과 준비를 거칩니다. 이러한 단계는 로컬 상태가 불일치할 가능성을 줄여 줍니다. 다만 relay가 연결되어 있다고 해서 relay들이 event를 수락하거나 정산이 완료된다고 보장할 수는 없으며, 그 확인만으로 로컬 저장의 내구성이 확보되지도 않습니다.

릴리스 포함 여부가 확인되지 않은 더 최근의 병합은 [신원 서비스에 트랜잭션 관리자를 추가합니다](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1063). 이제 신원 블록, 상태, 이메일 확인은 Nostr로 무엇이든 전파되기 전에 원자적으로 커밋되며, 새 테스트는 커밋이 실패했을 때 아무것도 전송되지 않는지 확인합니다. 이는 신원 서비스에만 적용됩니다. 어음 및 회사 데이터 저장에는 이러한 원자적 커밋이 없으며, relay 수락과 정산도 여전히 보장되지 않습니다.

### MLS-KMP와 Marmot 호환성 {#mls-kmp-and-marmot-compatibility}

marmot-kmp 아래에 있는 Kotlin MLS 라이브러리인 [MLS-KMP](https://github.com/vitorpamplona/mls-kmp/pull/9)는 앞서 다른 MLS 구현과 맞추기 위해 여러 와이어 동작을 수정했습니다. 그 결과 1.2.0을 쓰는 멤버와 그 새 코드를 쓰는 멤버는 나열된 경우에서 서로 어긋나므로, 그룹은 함께 업그레이드해야 합니다. 저장된 상태는 버전 10으로 바뀌었고, 이전 릴리스에서는 이를 복원할 수 없습니다. 다운스트림 Marmot 호환성 작업은 비차단(non-blocking)입니다. 그 테스트는 해당 변경의 작성 환경에서 실행되지 않았으며, Marmot은 여전히 `authorizeProposal`와 GREASE에 맞게 조정되어야 합니다. 이보다 앞선 [app-components 변경](https://github.com/vitorpamplona/mls-kmp/pull/7)은 Marmot이 MDK v0.14를 따르는 데 필요한 구성 요소를 강제합니다. Amethyst에서의 도입 여부는 저희가 확인하지 않았습니다.

릴리스된 1.3.0에 포함된다고 주장되지 않은 더 최근의 병합 소스는 [야간 상호운용성 러너의 컴파일을 복구하고](https://github.com/vitorpamplona/mls-kmp/pull/14) 스크립트별로 통과, 실패, 건너뜀을 보고합니다. 따라서 라이브 러너가 한 번도 실행되지 않았다는 저희의 이전 언급은 더 이상 맞지 않습니다. 작성자들은 실행이 정상적으로 이루어졌다고 보고하지만, 변경이 열린 시점에 최종 실행은 아직 진행 중이었고 저희는 최종 CI 결과를 다시 확인하지 않았습니다. OpenMLS 작업은 계속 비차단으로 남아 있으며, 지원되지 않거나 panic이 발생하는 시나리오 22개를 건너뛰고 ciphersuite 0x0001만 다루므로 상호운용성을 인증하지 않습니다. 이 변경은 보존된 그룹 ID에 의한 ReInit PSK 조회, epoch 0 중간 transcript, 첫 epoch의 무작위 secret, external commit 재개 PSK 처리도 수정합니다. epoch 0 transcript의 경우 코드가 이제 OpenMLS와 맞추기 위해 RFC 9420 11절을 따릅니다. 그래서 epoch 0으로의 외부 참여는 1.3.0 및 그 이전 릴리스와 달라지고, 저장된 이전 그룹은 첫 commit 전까지 기존 해시를 유지합니다. 원래 엔진은 첫 epoch secret을 0에서 도출했습니다. 이후 commit에는 새로운 UpdatePath가 포함되므로 작성자들은 익스플로잇을 찾지 못했지만, 이 수정이 모든 보안 문제가 해결되었음을 보여 주지는 않습니다.

### Obelisk Relay {#obelisk-relay}

[Obelisk Relay](https://github.com/obelisk-app/obelisk-relay/commit/d575c071729eb5230e73b95d2e2d9db219d5c00b)는 비공개 NIP-29 그룹에 관한 수정을 기본 브랜치에 병합했습니다. 전역 relay 관리자는 이전에도 비공개 그룹에 REQ를 보낼 수 있었지만, event 가시성 필터가 해당 event를 여전히 거부했습니다. 이제 relay 관리자는 그 event를 읽을 수 있으며, 멤버 접근 검사는 그대로 유지됩니다. relay 비공개 그룹은 종단 간 암호화되지 않으며, 이 변경은 서버 관리자의 가시성을 명시적으로 드러냅니다. 이 수정은 개발자와 운영자를 위해 병합된 소스 작업입니다.

### Plume {#plume}

Rust와 Tauri 기반 데스크톱 클라이언트인 [Plume](https://github.com/cpkb-bluezoo/plume/commit/2e962efb73bf7ef82d5394dc96240d3fb136a428)은 relay마다 재연결 기능을 갖춘 지속형 WebSocket 하나를 유지하도록 하는 변경 사항을 병합했습니다. 피드, 프로필, 게시, 다이렉트 메시지 작업이 모두 이 연결을 공유합니다. 구독과 event ID는 이 연결 위에서 다중화됩니다. 재연결 시도에는 백오프가 적용되며, 앱이 종료되면 연결이 닫힙니다. 이 변경 전에는 작업마다 새 소켓을 열었고, 그 소켓은 이후 해제되지 않은 채 누수되었습니다. 검토된 이 변경은 병합된 소스 작업이며, 여기서 확인된 성능 측정치는 없습니다. 무손실 복구나 전달 보장을 약속하는 것도 아닙니다.

### Hashtree {#hashtree}

Hashtree의 [TypeScript 런타임 0.5.22](https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.22)는 브라우저 provider가 서명된 현재 공개 peer 공지를 최대 256개까지 IndexedDB에 보관할 수 있게 하며, 이 공지는 신원과 앱 단위로 범위가 지정됩니다. provider는 네트워크 탐색 전에 이를 다시 불러올 수 있습니다. 일반 peer REQ는 기존 허용 규칙이 허락하는 범위에서 이 캐시를 재생할 수 있고, 비공개 탐색은 별도의 소유자 범위에 계속 분리되어 있습니다. 이와 별개로, 병합된 [Rust 어댑터 변경](https://github.com/mmalmi/hashtree/pull/4)은 중단된 인덱스 읽기를 취소하므로 명령이 더 이상 전송 타임아웃 시간을 끝까지 기다리지 않습니다. 해당 pull request는 hashtree-nostr-pubsub 0.2.87이 게시되었다고 보고하며, 이 패키지는 TypeScript 런타임과 별도로 버전이 관리됩니다. 소스에만 반영된 Rust 클라이언트 커밋들은 [읽기용으로 레거시, 읽기, 쓰기 Blossom origin을 결합](https://github.com/mmalmi/hashtree/commit/cc1c73c1733bd14673bad6c87eae6829330b25cf)하고, 소스별로 [유형이 지정된 요청 단계 연결 재설정에 대한 1회 재시도](https://github.com/mmalmi/hashtree/commit/57b30cfdfac3c745c1c3c7083459eb2512ad1ef1)를 추가하며, 부분 응답은 캐시하지 않습니다. Mac에서 한 번 수행한 콜드 설치만으로는 간헐적인 전송 타임아웃이 해결되었다고 입증되지 않습니다.

### nostr-pubsub {#nostr-pubsub}

[nostr-pubsub TS 0.5.20](https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.20)은 서명된 event를 담는 크기 제한 저장소를 유지하면서, 일반 Nostr REQ를 위한 IndexedDB 영속화, 탭 간 원자적 트랜잭션, 만료 처리, 로컬 재생을 추가합니다. 같은 소스는 이와 별도로 원자적 스냅샷과 배타적 writer lease를 갖춘 선택적 네이티브 Rust 파일 저장소 API도 설명하는데, 이는 TypeScript 패키지와는 별개입니다. [영속 event 저장소 구현](https://github.com/mmalmi/nostr-pubsub/commit/0ee66735e248d9b635caa3f44bdf8b23daf59b0d)에서는 다시 불러올 때 서명과 NIP-01 replaceable event의 승자를 재검사하고, ephemeral event와 현재 시각보다 5분 넘게 앞선 타임스탬프는 거부합니다. 저장소는 결코 암묵적으로 열리지 않으며, 공개 공지 범위는 호출자가 선택합니다. FIPS는 네트워크 탐색 전에 서명된 kind 37195 공지를 복원하며, 그 경우에도 최신성, 스키마, 네임스페이스를 검사합니다. 익명 또는 비공개 탐색 캐시는 공개 재생과 분리된 상태로 유지되어야 하며, 네트워크에서 데이터를 가져오는 라우터를 재생 소스로 사용해서는 안 됩니다. 보존 범위가 제한되어 있으므로, 이것이 무기한 오프라인 부트스트랩을 제공하지는 않습니다.

### FIPS-TS {#fips-ts}

[FIPS-TS 런타임 0.0.57](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.57)은 애플리케이션이 소유하는 영속 탐색 provider를 받아들이며, 이 provider는 기존 인터페이스를 통해 서명된 kind 37195 공지를 게시하고 구독합니다. provider가 주입되면 전송 계층은 Nostr relay 클라이언트를 열지 않고 빈 relay 목록을 허용하며, 종료 시에는 대기 중인 구독을 모두 정리합니다. provider의 수명과 복원된 저장소는 호출자가 책임집니다. 네임스페이스, 서명, 만료 검사는 여전히 적용됩니다. peer 인가도 계속 필요합니다. 새로운 인증 라우팅과 WebRTC 시그널링에는 여전히 도달 가능한 FIPS carrier가 필요하므로, 캐시된 공지가 오프라인 부트스트랩을 보장하지는 않습니다.

### Flotilla {#flotilla}

Flotilla는 소스 변경 세 건을 병합했습니다. [채팅으로 공유](https://gitea.coracle.social/coracle/flotilla/pulls/847) 기능으로 사용자는 독립 노트와 NIP-22 댓글을 어떤 방이나 대화에든 공유할 수 있습니다. 대화 안에서 인용하더라도 이제는 인용된 작성자가 p-tag에 추가되거나 멤버십이 분기되지 않습니다. [중단된 업로드 재개](https://gitea.coracle.social/coracle/flotilla/pulls/849) 변경은 초안에서 첨부 파일 업로드를 복원하고, 오류를 표시하여 사용자가 실패한 업로드에서 복구할 수 있게 합니다. 압축에 실패하면 원본 파일로 대체되며, 이때 원본 파일의 메타데이터가 남아 있을 수 있습니다. [저장된 읽음 표시 대기](https://gitea.coracle.social/coracle/flotilla/pulls/846) 변경은 저장된 읽음 상태가 로드될 때까지 페이지 읽음 표시 기록을 보류하므로, 시작 시점의 초기 읽음 업데이트가 유실되지 않습니다.

### following.space {#followingspace}

[following.space](https://github.com/callebtc/following.space)에 대한 열린 pull request는 소스 기준 시점에 아직 병합되지 않았으며, 병합되면 [follow pack 생성, 편집, 삭제를 복원](https://github.com/callebtc/following.space/pull/25)하고 pack 구성원을 팔로우하는 기능도 되살리게 됩니다. 계정 및 outbox relay 탐색에는 Applesauce를 사용하고, pack은 `naddr` 주소로 공유하게 됩니다. 브라우저 확장 signer, 메모리에만 보관되는 secret, bunker signer를 지원합니다. 코드와 작성자가 설명한 테스트만으로는 배포된 서비스나 모든 signer와의 호환성이 입증되지 않습니다.

### Routstr {#routstr}

Routstr의 pull request 세 건은 소스 기준 시점에 열려 있었으며 병합되지 않은 상태였습니다. 핵심 서비스에서는 [provider 상태 탐색](https://github.com/Routstr/routstr-core/pull/885)이 비전역 주소로 해석되는 공지 URL과 리디렉션을 거부하면서도 onion 프록시 처리는 유지하게 됩니다. 작성자들은 서버 측 요청 위조(SSRF) 노출과 테스트를 설명하지만, 이는 배포된 수정 사항도 아니고 확인된 익스플로잇도 아닙니다. SDK에서는 [URL에 대한 provider 귀속](https://github.com/Routstr/routstr-sdk/pull/123)이 kind 38421 event에 서명한 키를 따르게 됩니다. content에 기재된 pubkey는 검증되지 않은 상태로 남습니다. 작성자가 기본 relay에서 확인한 event 81개 중 content 기반 provider 목록을 가진 것은 하나도 없었으므로, 알려진 URL이 악용되었다거나 이제 모든 provider가 안전하다는 주장은 없습니다. [모델 경로 자동 고정](https://github.com/Routstr/routstr-sdk/pull/125)은 내장 상수 대신 신뢰할 수 있는 addressable kind 38427 event의 서명된 스냅샷을 사용하도록 전환됩니다. SDK는 마지막으로 유효했던 스냅샷과 롤백 워터마크를 보관하게 되며, 빈 스냅샷은 킬 스위치 역할을 하게 됩니다. 이 변경은 사용자 정의 어댑터 API의 호환성을 깨뜨립니다. 게시된 정책 event는 아직 없으며, 롤아웃은 여전히 운영자가 수행해야 하는 단계입니다.

### SatSigner {#satsigner}

SatSigner에 대한 열린 pull request는 소스 기준 시점에 병합되지 않았으며, [Nostr relay, 캐시, 동기화 계층을 재작업](https://github.com/satsigner/satsigner/pull/687)합니다. event를 찾지 못한 경우(relay의 저장된 event 종료 응답)는 타임아웃 및 relay가 아예 없는 경우와 구분하여 처리하게 됩니다. 오래된 캐시 콘텐츠에는 표시가 붙게 됩니다. event는 처리 과정에서 커서가 진행되기 전에 먼저 저장되며, gift-wrap rumor ID는 검증됩니다. 신원을 제거하면 해당 신원의 Nostr 테이블이 삭제되지만, kind 0 동기화가 로컬 프로필 편집 내용을 덮어쓸 수 있습니다. 이 위에 쌓인 [후속 변경](https://github.com/satsigner/satsigner/pull/688)은 민감 정보를 가린 진단 정보, Nostr 피드에서 탭하여 불러오는 동영상 포스터(플레이어는 최대 3개), 그리고 relay 풀을 해체하지 않고 앱 재개 시 밀린 내용을 따라잡는 기능을 추가하게 됩니다. 장애를 주입하는 relay 테스트도 함께 추가합니다. 새 네이티브 동영상 모듈은 앱을 다시 빌드해야 하며, 기기 검증은 아직 대기 중입니다. 두 변경 모두 출시되지 않았고 런타임 검사를 통과하지도 않았습니다.

### Bray {#bray}

[Bray 3.5.4](https://github.com/forgesworn/bray/releases/tag/v3.5.4)는 NIP-46 bunker 클라이언트와 데몬에 NIP-42 relay 인증을 추가합니다. 이제 AUTH를 요구하는 비공개 relay를 사용해 bunker 앞으로 온 메시지를 읽을 수 있습니다. 이후의 소스 변경이 이 태그에 포함되었는지는 확인되지 않았습니다.

이후 병합된 소스에서 Bray의 MCP 서버는 signer가 구성되지 않았거나 BRAY_READ_ONLY가 강제된 경우 [읽기 전용으로 시작](https://github.com/forgesworn/bray/pull/139)하며, 이 결정은 어떤 secret도 열기 전에 내려집니다. 이 모드에서는 지갑이 로드되지 않고 서명, 암호화, 복호화가 거부되며, 전체 261개 도구 중 조회 도구인 111개만 사용할 수 있습니다. CLI와 SDK는 여전히 signer를 필요로 하며, 구성되었지만 비어 있는 secret 파일은 여전히 오류로 처리됩니다. 새 attestation은 [이제부터](https://github.com/forgesworn/bray/pull/140) nip-va를 대체하여 [NIP-32](/ko/topics/nip-32/) attestation label 네임스페이스를 사용합니다. 기존 #l 타입 쿼리는 이전 label과 새 label을 모두 찾으며, signet-protocol은 자체 2.5.5 사본을 유지합니다. 이는 공식 NIP 채택이 아니며, 모든 중첩 라이브러리가 마이그레이션되었다는 의미도 아닙니다. 두 변경 모두 3.5.4에 포함된 것으로 확인되지 않았습니다.

### Alby 브라우저 확장 {#alby-browser-extension}

[Alby Lightning 브라우저 확장](https://github.com/getAlby/lightning-browser-extension)에 대한 열린 pull request는 소스 기준 시점에 병합되지 않았으며, 병합되면 [권한 헬퍼가 기억된 차단 항목을 단일 읽기로 거부](https://github.com/getAlby/lightning-browser-extension/pull/3644)하게 됩니다. 이로써 거부 항목을 제거하는 과정에서 Nostr 핸들러가 확인 요청 없이 동작할 수 있었던 경쟁 상태가 해소됩니다. BTC와 Liquid에 해당하는 동일한 차단 항목 경로는 현재 도달할 수 없습니다. 이는 배포된 수정 사항이 아니며, 확인된 익스플로잇도 없습니다.

### MintRadar relay 쓰기 정책 {#mintradar-relay-write-policy}

[MintRadar 소스](https://github.com/hroomnik007/MintRadar/commit/6fd6c8185c053e63610d9b4820e1656552885d85)는 프로젝트의 Nostr relay에 운영자 쓰기 정책을 추가합니다. 이 정책은 공개 kind 38172 공지와 kind 38000 리뷰를 event당 직렬화된 JSON 기준 16,384자, 그리고 IPv6 /64당 시간당 120개로 제한하며, 압축 표기된 IPv6 접두사는 정규 형식으로 변환됩니다. 트래픽이 많은 소스에는 시간당 3,000개의 소프트 상한이 적용되고, 시간당 6,000개의 절대 상한은 모든 소스에 걸쳐 수락된 event만 집계합니다. 특권 키에는 제한이 없습니다. 새 연결은 분당 120개, 버스트 60개로 제한됩니다. 이는 코드와 운영자 구성일 뿐이며, 프로덕션 롤아웃이나 완전한 서비스 거부 공격 방어를 입증하지는 않습니다.

## 새 프로젝트 {#new-projects}

### bosstro {#bosstro}

[Bosstro](https://github.com/MostroP2P/bosstro/blob/24bfd318f3e0d9d971e82a04daf12d0f035df2ab/README.md)는 Mostro 분쟁 해결자를 위한 새로운 Android 클라이언트입니다. MVP 소스가 공개되었으며, Mostro의 Rust 코어 위에 Flutter 프런트엔드를 얹은 구조입니다. 해결자는 노드 키가 아닌 전용 해결자 키로만 서명하며, 노드는 각 해결자에게 읽기 또는 읽기-쓰기 권한을 부여합니다. 권한을 받은 해결자는 분쟁을 맡고, 이미지와 PDF를 포함하는 구매자와 판매자 간 암호화 채팅에 참여하며, 구매자에게 지급하거나 판매자에게 환불할 수 있습니다. 키는 Android Keystore 기반 저장소에 보관되지만, Linux 및 웹 개발 빌드에는 이러한 보호 장치가 없습니다. 게시된 체크섬이 게시자가 누구인지를 입증하지는 않습니다.

### cordn-kmp {#cordn-kmp}

[cordn-kmp](https://github.com/vitorpamplona/cordn-kmp/commit/dcc0508fd818c1b6bc373b2a7d85742a2ec3dc1b)는 Quartz와 mls-kmp를 기반으로 JVM, Android, iOS, macOS, Linux를 지원하는 새로운 Kotlin Multiplatform Cordn 구현체입니다. 헤드리스 CordnGroupManager는 Nostr 위의 MCP 코디네이터를 통해 그룹 생성, 초대, 참여, 전송, 따라잡기를 수행하며, 이는 Marmot의 relay 전달 방식과는 다른 모델입니다. 영속화는 프런트엔드가 직접 제공하며, README의 ts-mls 상호 운용성 주장은 작성자가 제시한 것입니다.

이후 이 프로젝트는 [1.1.0](https://github.com/vitorpamplona/cordn-kmp/releases/tag/v1.1.0)을 게시했습니다. 이 버전은 정식 릴리스된 Quartz 2.4.0을 대상으로 빌드되므로, 빌드 플래그 뒤에서 미출시 Quartz의 로컬 체크아웃이 필요했던 이전 요구 사항은 태그된 릴리스에 더 이상 적용되지 않습니다. [1.2.0](https://github.com/vitorpamplona/cordn-kmp/releases/tag/v1.2.0)은 [공개 메서드 CordnExposure.differsFromMarmot()를 제거](https://github.com/vitorpamplona/cordn-kmp/pull/5)하고, 다른 바인딩과의 비교는 프런트엔드에 맡깁니다. 마이너 버전 번호임에도 이는 호환성을 깨는 API 변경입니다. 한 제안에서는 이 버전을 2.0.0으로 불렀으나, 실제 릴리스는 1.2.0을 사용합니다.

### emosphere {#emosphere}

[EmoSphere](https://github.com/Vojta01/emosphere/blob/dfabe1862c57493dbfa9b9881d26b30c1c272762/README.md)는 이제 소스가 공개된 Nostr 기분 지도이며, README는 버전 0.5.1을 설명합니다. 각 기기는 자체 키를 생성하고, 감정과 강도, 선택적인 짧은 메모, 사용자가 끌 수 있는 대략적인 위치를 담은 서명된 kind 1074 event를 게시합니다. 게시물은 시간 재생 기능이 있는 세계 지도와 팔로우 피드에 표시됩니다. 이러한 신호는 공개적이고 가명 기반이므로, relay는 기분과 위치를 읽고 시간이 지남에 따라 이를 하나의 키에 연결할 수 있습니다. Android는 키를 보안 저장소에 보관하는 반면, 웹 버전은 localStorage를 사용합니다.

### matrix-appservice-nostr {#matrix-appservice-nostr}

[matrix-appservice-nostr](https://github.com/Haven-Organization/matrix-appservice-nostr/blob/2f46b9cfcd7265db38d6a7a2c13552ab2a2aa4cc/README.md)는 Nostr relay와 짝을 이루는 Matrix 애플리케이션 서비스의 프로토타입 소스입니다. Matrix 사용자는 Nostr 신원을 생성하거나 가져올 수 있고, Matrix 방에서 게시, 팔로우, 답글, 반응, DM을 할 수 있으며, 브리지 도메인의 NIP-05 핸들을 사용합니다. 콘텐츠와 미디어는 Matrix 백엔드에 머무르며, relay는 저장된 원본으로부터 event를 재구성합니다. 키는 구성된 secret으로 AES-GCM 암호화되거나 NIP-46을 통해 원격으로 보관됩니다. 사용자는 운영자를 신뢰해야 하며, Matrix redaction(콘텐츠 삭제)은 브리지에 있는 사본만 제거합니다.

[더 최근의 커밋 7건](https://github.com/Haven-Organization/matrix-appservice-nostr/compare/a23289b2fcb42511066b47f1839e52a0184a98fa...b0cd64433ffa0ab6026635de2901a6e0a2146101)은 [섀도 Nostr 신원](https://github.com/Haven-Organization/matrix-appservice-nostr/commit/081ac30dbc8ae56f31ff8cb06f2b70cefb6b2a09)을 추가합니다. 브리지는 외부와 상호작용하는 허용된 Matrix 사용자를 위해 이 신원을 자동으로 생성하며, 그 프로필은 Matrix 프로필을 미러링합니다. 전체 프로필을 생성하면 기존 계정이 그 자리에서 업그레이드되며 동일한 키가 유지됩니다. 브리지 관리자는 외부 사용자나 홈서버에 전체 또는 섀도 접근 권한을 부여하거나, 방 범위의 수동적 답글, 반응, 투표 권한을 부여할 수 있습니다. 특정 사용자에 대한 허용이나 차단은 홈서버 규칙보다 우선하고, 홈서버 규칙은 방 규칙보다 우선합니다. 전체 권한은 프로필 생성을 허용하지만 프로필을 자동으로 게시하지는 않습니다. 접근 권한을 철회해도 키, 기록, 방은 유지되지만, 더 이상 허용되지 않는 곳에서는 외부 게시가 중단됩니다. 가져온 신원은 미러링된 프로필로 결코 덮어써지지 않습니다. 이러한 검사에는 코드와 테스트가 있지만 런타임 상호 운용성이나 보안 검증은 없으며, 운영자의 키 처리에 대한 신뢰는 여전히 필요합니다. 스티커는 이제 이미지로 전송됩니다.

### nostr-scrutiny {#nostr-scrutiny}

[Nostr Scrutiny](https://github.com/rzazo24/nostr-scrutiny/blob/2f2c38aa67eb7db72113bcf1ba00c55e99bc7e2e/README.md)는 Amethyst, Damus, Nostrich, Primal, Quill 등 다섯 개 Nostr 클라이언트를 비교하는 10월 24일 자 소스와 팩트 시트를 공개합니다. 각 시트는 클라이언트의 앱 스토어 개인정보 보호 주장과 공개된 코드를 다룹니다. 브라우저로 처음 방문했을 때 관찰되는 네트워크 요청도 함께 담겨 있습니다. 정적인 일반 HTML로 만들어진 이 사이트는 자체(퍼스트 파티) 추적이 없다고 밝힙니다. 이 시트들은 날짜가 명시된 사실 목록이며, 보안 인증이나 암호학적 감사가 아닙니다. 공개된 이해 상충 사항으로, 작성자는 Quill도 개발하고 있습니다.

### v2 {#v2}

[Solid Chat v2](https://github.com/solid-chat/v2/blob/da8b577a98167235f4452cbc97ca5fdb918b5cea/README.md)는 새로 공개된 클라이언트 소스입니다. 하나의 did:nostr 키로 NIP-98 HTTP 인증을 사용해 Solid pod 방에 글을 쓰고, NIP-17 gift wrap 방식의 DM도 보냅니다. 서명은 NIP-07, NIP-46 또는 로컬 nsec를 통해 이루어지며, NIP-44 암호화와 kind 1059 래핑을 사용합니다. 방은 평문이며 각 pod의 ACL로만 보호됩니다. 암호화된 DM 미디어는 Blossom에 업로드되고, 프로필 조회는 nostr.social 디렉터리로 전송됩니다. 로컬 nsec는 localStorage에 저장되므로 외부 서명기를 쓰는 편이 더 안전합니다.

### witchat {#witchat}

[Witchat](https://github.com/BarefootJoey/witchat/blob/905f17d322752554e077a5a0e774555c38417e50/README.md)은 Windows와 Linux용 비공식 bitchat 클라이언트의 소스입니다. 근처의 Bluetooth 메시로 채팅하며, 서로 즐겨찾기한 사용자 사이에서는 Nostr gift wrap으로 대체 전송합니다. Nostr의 공개 geohash 채널에도 참여하는데, 메시지에는 kind 20000 event를, 접속 상태(presence)에는 kind 20001을 사용합니다. bitchat 전송 계층과의 상호 운용성은 작성자의 주장이며, Windows 바이너리는 서명되지 않았습니다. Nostr relay는 IP 주소와 채널 메타데이터를 볼 수 있습니다. 근거리 브로드캐스트는 현재 Bluetooth로만 전달됩니다.

### wn-notify {#wn-notify}

[wn-notify](https://github.com/jooray/wn-notify/blob/ba21270edace90c0d6dde7fde7c3b1e3fb5c6201/README.md)는 표준 라이브러리만 사용하는 비공식 Python CLI입니다. marmot.agent-control.v2 Unix 소켓으로 로컬 wn-agent를 거쳐 White Noise 그룹에 메시지와 파일을 보냅니다. 키, MLS 상태, relay는 커넥터가 보유합니다. CLI는 final_sent와 메시지 ID를 확인합니다. 결과를 알 수 없으면 unknown으로 처리해 0이 아닌 종료 코드를 반환합니다. 스스로는 절대 재시도하지 않으므로, 수동 재시도를 위해 멱등성 키를 보존합니다. 확인 응답은 relay에 게시되었음을 확인할 뿐, 누군가 메시지를 읽었음을 확인하지는 않습니다. 테스트된 버전은 wn-agent 0.13.0뿐입니다.

### xmradar {#xmradar}

[XMRadar](https://github.com/KYC-rip/xmradar/blob/537309555c511e2f5f257fe7e471b0ff2c91ac4f/README.md)는 웹 게시물과 X 아티클을 Nostr로 복사하는 브라우저 확장 프로그램입니다. 모든 게시는 외부 NIP-07 서명기를 통해 승인됩니다. [릴리스 0.2.0](https://github.com/KYC-rip/xmradar/releases/tag/v0.2.0)에는 X에서 Nostr 신원을 가진 작성자에게 Monero 팁을 보내는 기능이 추가되었습니다.

[구현](https://github.com/KYC-rip/xmradar/commit/213d4b1a6604fe07af4c1991a1c8159a7bcc4abc)을 보면, kind 9042 영수증은 사용자가 팁을 보냈다고 밝히고 확인한 뒤에만 게시됩니다. 영수증에는 양측 참여자의 npub, 금액, 주소가 공개됩니다. 거래 ID, 거래 키, 결제 증명은 포함되지 않습니다. 소액의 무작위 piconero 금액을 사용하므로 수신자의 지갑이 결제를 대조해 kind 9044 확인을 게시할 수 있습니다. 이 확인은 수신자가 서명한 것이며 독립적인 온체인 증명이 아닙니다. 인터페이스는 수신자가 확인한 팁과 미확인 주장을 구분해 보여 줍니다. 사용자 자신이 보낸 팁은 30분 동안 대기 상태로 남습니다. 미확인 주장은 지불자당 한 번만, 현재 주소로 보낸 가장 작은 영수증 기준으로 집계됩니다. 이러한 주장은 위조될 수 있습니다. 합계는 게시물별이 아니라 작성자별로 관리됩니다. [NIP-A3](/ko/topics/nip-a3/)와 [NIP-39](/ko/topics/nip-39/) X 증명을 통한 주소 탐색은 기본적으로 꺼져 있습니다. 이 기능을 켜면 사용자가 어떤 신원을 조회하는지 relay와 X가 볼 수 있습니다.

### agent-inbox {#agent-inbox}

[agent-inbox](https://github.com/ec175/agent-inbox/commit/88fa9da299c3013a0c6a2c88abf0223945229bfa)는 AI 에이전트들이 Nostr에서 짧은 핸들로 서로 연락할 수 있게 해 주는 새 도구입니다. 단일 Python 파일로 NIP-44 v2 암호화를 적용한 표준 NIP-17 gift wrap을 보내고, 공개 게시판에 글을 올릴 수도 있습니다. 공식 테스트 벡터에서 가져온 픽스처도 포함되어 있습니다. 핸들은 공개 키 접미사를 잘라 낸 것일 뿐, 인증된 신원이 아닙니다. README는 순수 Python 암호화 구현이 상수 시간(constant-time)으로 동작하지 않는다고 경고합니다. 저희는 이 구현을 감사하지 않았습니다. 그래도 어떤 NIP-17 클라이언트든 에이전트의 npub로 메시지를 보낼 수 있습니다.

### CarryChat {#carrychat}

[CarryChat](https://github.com/kemal-arslan/carrychat/commit/64437892165b41070d93acb9b6815dc97168b5a1)은 사용 가능한 경로를 가리지 않고 크기가 제한된 메시지 번들을 옮기는 새로운 저장 후 전달(store-and-forward) 메신저입니다. 인터넷 전송은 Nostr가 맡고, 오프라인 상황은 Bluetooth LE 같은 로컬 링크와 단순 파일 교환이 담당합니다. 소스에는 Nostr 전송 계층과 그에 대한 테스트가 들어 있습니다. README는 이 버전을 초기 0.2 릴리스라고 부르며, 실제 하드웨어에서의 LoRa 현장 테스트는 아직 끝나지 않았다고 밝힙니다. 저희는 기기에서 테스트하지 않았습니다.

[최근 커밋 13개](https://github.com/kemal-arslan/carrychat/compare/64437892165b41070d93acb9b6815dc97168b5a1...311f1765e72079c7b70cf8d1c55865dc781cc2ad)는 [311f176](https://github.com/kemal-arslan/carrychat/commit/311f1765e72079c7b70cf8d1c55865dc781cc2ad)까지 이어지며, 로드맵의 자리 표시자를 실제로 동작하는 소스로 대체합니다. 대상은 Wi-Fi Direct, MeshCore 무선 어댑터, Reticulum 링크, NFC 연락처 카드, 오디오 전송이며, Kotlin, Rust, UI 코드가 포함됩니다. 오디오로 수신할 때 수신 측은 연락처 카드 서명을 검증하고 일반 메시지 프레임은 받아들이지만, 파일 청크는 거부합니다. NFC로는 메시지가 아니라 연락처 카드만 교환합니다. 이는 앞선 0.2.0 릴리스 이후의 소스 개발이며, 새로 검증된 바이너리가 아닙니다. README에 따르면 MeshCore와 LoRa, Reticulum, Wi-Fi Direct, NFC는 아직 현장 테스트나 휴대폰 두 대를 이용한 테스트를 거치지 않았습니다. 이번 변경은 하드웨어 호환성, 익명성, 보안에 대해 아무런 주장도 하지 않습니다. 고주파 오디오는 하드웨어에 따라 달라지므로 어디서나 들리지 않는 것은 아닙니다. Nostr는 로컬 링크와 함께 여전히 인터넷 relay 전송 수단 중 하나로 남아 있습니다.

### Cosign과 Marble {#cosign-and-marble}

[Cosign](https://github.com/sybenx/cosign/commit/c42da802f4d526c5c3c2b08593fcba267f3097c9)은 Nostr 서명 키를 FROST 임계값 지분(threshold share)으로 분할하는 새로운 베타 프로토콜이자 라이브러리입니다. 사용자의 기기는 서버와 함께 서명할 수 있지만, 서버만으로는 서명할 수 없습니다. 종이 백업 지분은 README에 설명된 복구 및 지분 갱신 흐름을 지원합니다. 다만 이 흐름은 보안 검증을 거치지 않았습니다. Android 및 브라우저 클라이언트인 [Marble](https://github.com/sybenx/marble/commit/d5b50d760c6d4f093120d1d955918430d8360bf6)은 피드와 서명에 Cosign을 사용합니다. 기반 FROST 라이브러리는 감사를 받았지만, Cosign 자체 프로토콜은 독립적인 검토를 받은 적이 없습니다.

[최신 소스](https://github.com/sybenx/marble/commit/ebd110f907d3569a8a9b3e385394c5a55b5582ec)에서 Marble 브라우저 클라이언트는 전송되지 않은 노트를 로그인된 계정에 연결합니다. 게시 전에는 다른 탭이나 원격 세션에서 로그인이 종료되었는지 감지합니다. 로그아웃된 클라이언트에서 요청이 오면 Signed out이 표시됩니다. [즉시 검색](https://github.com/sybenx/marble/commit/029d8b0f918a9783910aef15f6fe1f160d9c6707)은 일반 웹이 아니라 Ditto와 relay에 질의합니다. 특정 작성자의 게시물을 검색할 때는 relay에 요청하기 전에 이미 불러온 게시물부터 확인합니다. 스팸으로 의심되는 항목은 펼칠 수 있는 안내 뒤로 접힙니다. Not Spam 재정의는 해당 브라우저에서만, 그리고 해당 작성자에게만 적용됩니다. 이러한 검색 보조 기능이 보안 검토를 거쳤다는 증거가 되지는 않습니다.

[Cosign 0.12.7](https://github.com/sybenx/cosign/releases/tag/v0.12.7)에서는 서버가 보낸 구성원 목록 병합만 허용되므로, 종이 백업 지분이 다른 역할로 승격될 수 없습니다. epoch 동기화 후에는 갱신되지 않은 서버가 뒤처진 것으로 표시됩니다. 유효하지 않은 부분 결과는 거부되며, 자동 복구는 계속 비활성화되어 있습니다. 이제 복호화 부분 결과에는 Chaum-Pedersen 증명이 포함되고, 부분 결과를 결합하기 전에 이 증명을 검사합니다. 이전 클라이언트는 이 증명을 무시합니다. Marble의 Android 부분에는 다음 빌드에서 반영됩니다. 이러한 보안 설명은 릴리스 작성자가 제공한 것이며, 저희는 암호 구현을 감사하지 않았습니다.

[0.12.7 태그 이후 커밋된 Android NIP-55 소스](https://github.com/sybenx/cosign/commit/e53941f699e9e77ed430015e416daa723c95204f)는 첫 연결 시점의 경쟁 상태를 수정합니다. 이 문제는 서버의 승인이 아직 relay를 통해 도착하는 중일 때 발생합니다. 이제 공개 키 조회에는 즉시 응답합니다. 서명과 복호화는 UI 스레드 밖에서 대기합니다. 재시도는 새로 승인된 연결이 revoked 응답을 받은 경우에만, 한 번 이루어집니다. 코드는 연결할 수 없는 서버와 거부로 응답하는 서버도 구분합니다. 이 후속 소스 수정이 0.12.7 태그나 현재 Marble 바이너리에 반영되었는지는 확인되지 않았습니다.

### Dream Nests {#dream-nests}

[Dream Nests](https://github.com/2three1y/dreamnests/commit/0edc7af86c326452a020ba0b7124c55f5a0413b5)는 실시간 Nostr 오디오 방을 모아 보여 주는 새로운 읽기 전용 디렉터리입니다. Nests 방과 라이브 활동 event를 각각의 채팅과 함께 가져옵니다. 이 웹 앱은 스크린 리더를 위해 제목 구조와 polite 라이브 리전 알림을 사용하며, 짧은 이어콘(earcon)으로 소리 신호를 줍니다. 공개 HLS 스트림은 듣기 전용으로 재생됩니다. Nests 방은 Nests에서 열리고, Corny Chat과 HiveTalk 방은 각자의 사이트에서 열립니다. 따라서 발언은 해당 앱 안에서만 이루어집니다. 마이크 표시는 실제 음성 활동 감지가 아니라 presence 메타데이터를 기반으로 합니다. 저희는 기기에서 접근성을 테스트하지 않았습니다. 저장소에는 공개 라이브 URL이 기재되어 있습니다.

### fips-pub-pki {#fips-pub-pki}

[fips-pub-pki](https://github.com/fr34aky/fips-pub-pki/commit/bd0ea8a16a24eb14d92563cd8d470afad172c83a)는 서명된 Nostr 인증서를 위한 새로운 소스입니다. 도메인이 하위 발급자에게 권한을 위임할 수 있으며, 오프라인 경로 검증을 지원합니다. 신뢰 앵커는 자매 프로젝트인 fips-pub-domains에서 가져옵니다. 이 프로젝트는 DNSSEC 클레임을 핀 및 증인(witness)과 결합합니다. 검증기는 DNS에 전혀 질의하지 않습니다. 인증서 폐기는 relay에서 event를 삭제하는 방식이 아니라 만료와 명시적 표시로 처리됩니다. README에 따르면 공개 도메인과 휴대폰을 이용한 실제 메시 테스트는 아직 끝나지 않았습니다. 제출된 NIP도, 등록된 kind도 없으므로 이는 실험 단계이며 TLS를 대체하는 것이 아닙니다.

### Magnetar {#magnetar}

[Magnetar](https://github.com/awake-devel/magnetar/commit/b519486d6ed3a1e6f41c4e7faa5c587e9362caf1)는 [NIP-35](/ko/topics/nip-35/) 토렌트 event를 위한 새로운 검색 스택입니다. 크롤러 및 검색 백엔드와 로컬 SQLite 캐시를 유지하는 Android 앱으로 구성됩니다. 팔로우 관계로 게시자 신뢰도를 산정하고, 스웜이 살아 있는지도 확인합니다. 첫 0.1 프리릴리스에는 크롤러 코드와 함께 Android와 서버 양쪽의 테스트가 들어 있습니다. 작성자는 자동화 테스트와 에뮬레이터로만 검증했으며, 실제 휴대폰에서는 검증하지 않았습니다. 팔로우 기반 신뢰도가 토렌트의 합법성이나 안전성을 보장하지는 못합니다. 백엔드 역시 권위 있는 색인이 아닙니다.

### Magnitude Relay {#magnitude-relay}

[Magnitude Relay](https://github.com/VectorPrivacy/magnitude-relay/commit/92f2440d96a3bf3a6c86691b146ebd6fef7b9f10)는 VectorPrivacy가 만든 새로운 Rust 기반 Nostr relay입니다. Vector의 gift wrap DM과 Concord 트래픽에 맞게 조정되었으며, NIP-77 동기화와 입력 중 표시 기능을 갖추고 있습니다. 운영자들에 따르면 이 relay는 기존 Vector 엔드포인트 두 곳에서 strfry를 대체했습니다. 저장소에는 적대적 테스트 및 벤치마크 하네스가 포함되어 있습니다. 그러나 공개된 속도 수치는 작성자가 직접 실행한 결과이며 독립적으로 재현되지 않았습니다.

그 뒤 운영자를 위한 [Docker 및 Compose 패키징](https://github.com/VectorPrivacy/magnitude-relay/pull/1)이 병합되었습니다. 비특권 사용자로 실행되며, 데이터 볼륨과 로컬 전용 바인드, 헬스체크를 갖춥니다. 풀 리퀘스트에 적힌 프로덕션 및 가져오기 관련 관찰 내용은 작성자가 제공한 것입니다. arm64는 테스트되지 않았습니다. 패키징만으로 프로토콜 준수 여부가 입증되지는 않습니다.

[최신 소스](https://github.com/VectorPrivacy/magnitude-relay/commit/af1b354c5f465d4bf7772ef8fa8f0eaf35a7aabe)는 IP당 새 연결 수를 기본적으로 버스트 300회, 이후 분당 60회로 제한합니다. 한도를 0으로 설정하면 제한이 꺼지며, 루프백은 제한 대상에서 제외됩니다. 프록시의 실제 IP 헤더는 localhost에서 온 경우에만 신뢰합니다. 거부된 연결에는 WebSocket이 열리기 전에 HTTP 429가 반환됩니다. 공개 relay의 거부 내역은 집계 형태로만 보고되고, IP별 세부 정보는 관리자 소켓에서만 확인할 수 있습니다. 대량 NIP-77 동기화에서는 임시(ephemeral) event와 600초 이내에 만료되는 event가 제외됩니다. 실시간 전달에서는 수명이 짧은 event도 여전히 전달됩니다. 신뢰 링크가 바뀌면 relay는 중복되는 gift wrap 가시성 탐색을 건너뜁니다. 그래도 gift wrap 자체는 계속 동기화됩니다. 이는 측정된 프로덕션 벤치마크가 없는 소스 변경입니다.

### nostr_doctor {#nostr_doctor}

[nostr_doctor](https://github.com/nogringo/nostr-doctor/commit/348efc1dd32c213badf34c6ba529707b952bd658)는 CLI와 Flutter 프런트엔드를 갖춘 새로운 Dart 라이브러리입니다. 클라이언트가 계정의 데이터를 찾을 수 있는지 점검합니다. 프로필 메타데이터와 NIP-65 relay 목록부터 시작하며, 비공개 DM relay와 임시 저장 글(drafts), Blossom 서버와 nutzap 설정까지 살펴봅니다. relay 목록을 찾을 수 있는지 점검할 때는 교체 가능한(replaceable) 목록을 조회해 봅니다. 저희는 이 진단 도구를 소스 수준에서 검토했으며, 앱 릴리스는 검증하지 않았습니다. 점검 결과는 도구가 질의한 relay의 상황만 반영하며, 전체 네트워크에서의 가용성을 보여 주지는 않습니다.

### nostr-indexer-relay {#nostr-indexer-relay}

[nostr-indexer-relay](https://github.com/nogringo/nostr-indexer-relay/commit/f75e4415f24f629935f7e6b3567232e2c6dbf80a)는 NIP-65 relay 목록만 저장하는 새로운 Go 기반 relay입니다. 크롤러는 이 목록에 적힌 relay를 찾아내고 NIP-77 지원 여부를 확인합니다. 또한 negentropy를 통해 현재 동작 중인 다른 인덱서와 동기화합니다. 공개 조회 페이지와 관리자 인터페이스가 포함되어 있으며, 스스로를 초기 단계라고 소개합니다. 이 도구는 relay 목록 전용 색인일 뿐, Nostr 아카이브나 범용 콘텐츠 relay가 아닙니다.

### nostr2gh {#nostr2gh}

[nostr2gh](https://github.com/kravens/nostr2gh/commit/ec189b10d48d0f9f0c0e8a464c930263b2275c95)는 NIP-34 패치 및 풀 리퀘스트 event와 그 업데이트를 Nostr에서 GitHub로 옮기는 새로운 브리지입니다. 전달은 화이트리스트에 등록된 릴레이어를 통해 이루어집니다. 기여자가 가져올 수 있는(fetchable) 위치에 브랜치를 푸시하고 Nostr event에 서명하면, 정상적인 GitHub 계정을 가진 친구가 대신 PR을 엽니다. 이 도구는 GitHub에 접근할 수 없는 기여자를 돕습니다. 그렇다고 차단을 자동으로 우회해 주지는 않으며, 신뢰할 수 없는 패치를 자동으로 실행해도 된다는 허가가 되지도 않습니다.

### Relay Radio {#relay-radio}

[Relay Radio](https://github.com/2three1y/relayradio/commit/3993e7226de616ac9a2768a5d50a271535449806)는 실시간 Nostr 피드를 이어콘과 브라우저 텍스트 음성 변환(TTS)으로 들려주는 새로운 읽기 전용 웹 앱입니다. 스크린 리더 사용자를 위해 선택적으로 polite 라이브 리전도 제공합니다. 청취자는 큐레이션된 글로벌 방송국과 자신이 팔로우하는 사람들로 구성된 방송국 중에서 고를 수 있습니다. 방송에는 노트, 답글, 리포스트, 반응, zap이 포함됩니다. 이 앱이 청취자를 대신해 글을 게시하거나 결제하는 일은 없습니다. 콘텐츠 필터링은 최선의 노력 수준이므로, 소리 내어 읽히는 내용이 모두 안전하다고 보장할 수는 없습니다.

### Hibiki {#hibiki}

[Hibiki](https://github.com/ChiefmonkeyArt/torii-hibiki/commit/3820208896df7ba28a06a2cfa38fefc1a753f9d1)는 Torii용 독립형 피드 napplet이며, 소스에서는 버전 0.2.1을 처음으로 동작하는 피드라고 부릅니다. 공개 게시물과 미디어는 노드가 가져오고, 사용자의 취향에 기반한 순위 지정은 브라우저에서 실행됩니다. 피드는 직접적인 네트워크 접근이 없는 샌드박스 iframe에서 실행되며, 서명된 스팸 평판은 참고용 조언으로만 취급합니다. 저희는 프라이버시 경계를 독자적으로 검증하지 않았습니다.

버전 0.2.6까지 병합된 소스에는 [인라인 답글과 추출형 뉴스 요약](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/8)이 추가되었고, 이제 좋아요가 게시물 순위를 다시 매기지 않습니다. 태그된 릴리스는 아직 확인되지 않았습니다. Watch 플레이어의 미리보기 지원으로 [미리보기 프레임](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/9)이 추가됩니다. 프로필 페이지와 함께 [zap](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/11) 기능도 도입됩니다. 노드는 각 인보이스의 금액과 description hash를 확인합니다. 모든 결제에는 소유자의 확인이 필요하며, 결제자는 WebLN 또는 QR 코드를 사용합니다. 노드는 자금도 키도 보관하지 않습니다. Primal 주소의 인보이스에는 description hash가 없기 때문에, [후속 변경](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/12)에서는 금액이 정확히 일치하면 이를 수락합니다. 이러한 인보이스에는 bound:false 플래그가 붙고, 소유자에게는 지갑이 확인하지 않을 수 있다는 경고가 표시됩니다. 이 방식은 인보이스와 zap 요청 사이의 연결을 약화시키며, 이를 유효한 [NIP-57](/ko/topics/nip-57/) 확인으로 만들어 주지는 않습니다. 지갑의 5xx 오류와 타임아웃은 한 번 재시도되며 LNURL 사유가 표시됩니다. 작성자는 실제 지갑으로 종단 간 zap에 성공했다고 보고하지 않았습니다.

### wax {#wax}

[wax](https://github.com/modus-lisp/wax/commit/0b48716cfce52be990e0ef43fcecb2c5fa899b44)는 BIP-39 시드에서 역할 키를 파생하고 모든 요청을 정책 가드에 통과시키는 새로운 Common Lisp 서명기로, 승인 콜백이나 허용 목록이 허락하지 않는 한 기본적으로 거부합니다. 호출자별 엔벨로프 시퀀스가 재전송(replay) 공격을 막습니다. 메서드 이름은 NIP-46과 비슷하지만, 코어는 네트워크 전송 계층을 제공하지 않습니다. 저희는 이 서명기에 대한 보안 감사를 수행하지 않았습니다.

### WhatZaps {#whatzaps}

[WhatZaps](https://github.com/nostr-wot/whatsapp-zaps/commit/ab86552a5178c9c1b55dd917084f4e3cf223ea89)는 Nostr WoT 확장 프로그램의 WebLN 지원을 이용해 WhatsApp 연락처에 Lightning으로 결제하는 새로운 브라우저 확장 프로그램입니다. 연락처를 Nostr 프로필에 매핑하고 상대의 결제 주소를 확인하며, 결제 전에는 항상 명시적인 확인을 요청합니다. /zap 명령은 채팅 메시지로 전송되지 않으며, 반응 또는 버튼 경로로 결제할 때는 아무것도 게시되지 않습니다. 이는 신원 조회에 Nostr를 사용하는 Lightning 결제일 뿐, 서명된 [NIP-57](/ko/topics/nip-57/) zap 영수증이 아닙니다. 저희는 브라우저 메시지 매칭 기능을 테스트하지 않았습니다.

### Agora 암호화 투표 {#agora-encrypted-polls}

[Agora](https://github.com/maxgfr/agora/commit/85d83f49dcb3ed138c4118bced60d1a2f48fb01b)는 암호화된 그룹 투표를 위한 브라우저 프로토타입입니다. 구성원 보증(vouching)과 블라인드 투표 티켓을 결합하고, Nostr relay와 WebRTC를 통해 트래픽을 전달합니다. [README](https://github.com/maxgfr/agora/blob/85d83f49dcb3ed138c4118bced60d1a2f48fb01b/README.md)는 이 설계를 '실제 사람 한 명당 한 표'로 설명합니다. 그러나 이는 티켓을 위조할 수 있는 티켓 발급자를 신뢰해야 하고, 사회적 신뢰의 한 형태인 보증에도 의존합니다. 이 설계는 강압 저항성을 제공하지 않습니다. relay는 타이밍과 IP 주소를 볼 수 있으며, 결과는 클라이언트가 어떤 event를 수신하는지에 따라 달라집니다. 이 프로젝트는 이전의 ghobs91/Agora 채팅 프로젝트와 관련이 없습니다.

### Cinderous SDK {#cinderous-sdk}

[Cinderous SDK](https://github.com/VaalRL/cinderous-sdk/commit/59314a6c2dffb85224c6262348a707f6acc4eb83) v0.83.0은 새로운 소스 프로토타입입니다. 기기마다 고유한 키를 할당하고, Nostr와 WebRTC를 통해 Git과 유사한 이력으로 문서를 동기화하며, 필요할 때는 relay로 대체합니다. relay는 호출자가 선택하고 배포하며, SDK에는 기본 공개 relay가 포함되어 있지 않습니다. 암호화에는 Double Ratchet을 사용하는 실험적인 CinderEK 방식이 쓰이는데, 이 방식은 외부 감사를 받은 적이 없습니다. 하이브리드 키 교환을 사용한다고 해서 secp256k1 서명이 양자 내성을 갖게 되는 것은 아니며, [README](https://github.com/VaalRL/cinderous-sdk/blob/59314a6c2dffb85224c6262348a707f6acc4eb83/README.md)는 이 SDK가 프로덕션 환경에서 사용할 준비가 되지 않았다고 설명합니다.

### evil-napplets {#evil-napplets}

[evil-napplets](https://github.com/napplet/evil/commit/7311b6298e7b64e595d8b566f226a26cad1cfee5)는 초안 NIP-5D의 불투명 출처(opaque-origin) 모델에서 napplet을 실행하는 호스트를 테스트하기 위해 공격 단계(attack ladder) 레벨 02부터 08까지를 추가했습니다. 악성 napplet은 기능(capability) 경계와 브리지 경계를 탐색하고, 호스트가 무엇을 허용했는지 보고합니다. 기본값은 시연 모드이며, 능동 모드는 명시적으로 활성화해야 합니다. 능동 테스트는 테스터가 탐색 권한을 가진 호스트를 대상으로만 실행해야 합니다. 이 테스트 모음은 레드팀용 픽스처이므로, 이를 통과한 호스트라 해도 안전하다는 것이 입증된 것은 아닙니다. 다른 앱 아키텍처를 대상으로 하는 evil-napps와는 별개의 프로젝트입니다.

### evil-napps {#evil-napps}

[evil-napps](https://github.com/sandwichfarm/evil-napps/commit/f0746e4cb958bbcb01806e2354809472b63a943a)는 NAPP 런처의 권한 경계를 탐색하는, 소스 형태로 제공되는 새로운 테스트 모음입니다. 런처 브리지와 앱에 노출되는 NIP-07 서명기를 다룹니다. SharedDB 저장소도 범위에 포함됩니다. NAPP 번들은 메타데이터와 인덱스 파일을 짝지은 구성으로, NIP-5D napplet이 사용하는 단일 HTML 산출물과는 형식이 다릅니다. [README](https://github.com/sandwichfarm/evil-napps/blob/f0746e4cb958bbcb01806e2354809472b63a943a/README.md)에 따르면 이 테스트 모음은 기본적으로 시연 모드로 실행되며, 능동 탐색은 명시적으로 요청된 경우에만 실행합니다. 테스트와 하네스를 통과했다고 해서 런처가 인증되는 것은 아닙니다.

### Feedstr {#feedstr}

[Feedstr](https://github.com/0n4t3/Feedstr/commit/3fe44eca46106488585d0d1554509f5d3e498f39)는 피드, 읽음 상태, 즐겨찾기를 Nostr를 통해 암호화된 형태로 동기화하는 새로운 Rust RSS 리더입니다. 개별 피드마다 동기화를 끌 수 있습니다. OPML 가져오기와 내보내기를 지원하며 [NIP-23](/ko/topics/nip-23/) 장문 아티클도 처리합니다. 저장소에는 core, Android, 웹, Flatpak 소스 트리가 있습니다. [README](https://github.com/0n4t3/Feedstr/blob/3fe44eca46106488585d0d1554509f5d3e498f39/README.md)에는 이 소프트웨어가 거의 테스트되지 않아 사용을 권장하지 않으며, 설치 및 사용 안내는 곧 제공될 예정이라고 적혀 있습니다.

### NKIP 예치 영수증 툴킷 {#nkip-deposit-receipt-toolkit}

[KYC-rip/nkip-0001](https://github.com/KYC-rip/nkip-0001/commit/6d6a9489db72626794e7e2b88a18846ea19a10e2)은 XBToshi가 유지 관리하는 새로운 TypeScript 툴킷으로, NKIP-0001 예치 영수증을 다룹니다. NKIP-0001은 애플리케이션 영수증 형식이며, 채택된 Nostr NIP가 아닙니다. 이 툴킷은 Ed25519로 서명된 예치 영수증과 솔트를 적용한 커밋먼트, Nostr 증인(witness) event, 그리고 NIP-44 암호화를 통한 솔트 복구를 처리합니다. 보호 효과는 증인이 관측될 때까지 애플리케이션이 예치 주소를 공개하지 않는지에 달려 있습니다. SDK는 주문을 통제하지 않으며 지급을 보장하지도 않습니다. 자세한 내용은 [README](https://github.com/KYC-rip/nkip-0001/blob/6d6a9489db72626794e7e2b88a18846ea19a10e2/README.md)에서 확인할 수 있습니다.

### nostr-parse {#nostr-parse}

[nostr-parse](https://github.com/VectorPrivacy/nostr-parse/commit/703f07cd7177b2b52977aa6deaa6f11a696d4914)는 VectorPrivacy가 만든, 서명된 Nostr event용 새로운 Rust 파서입니다. 엄격한 7개 필드 event 구조를 강제하고 음이 아닌 정수를 요구하며, kind를 u16 범위로 제한하고 hex 필드를 검사하며 이스케이프된 문자열을 검증합니다. 오류는 오프셋과 함께 보고됩니다. 호출자는 압축된 소유(owned) 할당이나 입력을 참조하는 차용(borrowed) span을 생성할 수 있으며, `parse_unsigned`는 서명되지 않은 NIP-59 rumor를 받아들입니다. 파싱 과정에서는 event ID를 다시 계산하지 않고 Schnorr 서명도 검증하지 않습니다. 따라서 이러한 검사는 여전히 호출자가 직접 수행해야 합니다.

### cl-deposits {#cl-deposits}

[cl-deposits](https://github.com/modus-lisp/cl-deposits/commit/3d74564de6be0d25efec3ce6ad76a4fc691dc676)는 Bitcoin Deposits의 새로운 Common Lisp 구현입니다. 이 설계에서는 운영자가 서명되고 쿼럼이 공동 서명한 해시 체인 원장을 Nostr 상에서 운영하며, 이 원장은 Taproot 준비금으로 뒷받침됩니다. 저장소에는 소스와 함께 검사 테스트가 포함된 devnet이 들어 있습니다. README와 [ROADMAP](https://github.com/modus-lisp/cl-deposits/blob/3d74564de6be0d25efec3ce6ad76a4fc691dc676/ROADMAP.md)에 따르면, 작성자는 참조 픽스처를 재실행하고 signet devnet을 운영했으며 deposits-rust와의 상호 운용성을 양방향으로 테스트했습니다. 또한 작성자는 Lightning 수신 경로가 동작한다고 보고하며, 다음 작업으로 결제 InvoiceLock과 Fulfill을 꼽고 있습니다. 사용자는 운영자, 공동 서명 쿼럼, 그리고 준비금에 관한 가정에 의존하게 됩니다.

### Streets {#streets}

타임라인, 알림, 검색을 나란히 보여 주는 컬럼 기반 Nostr 웹 클라이언트 [Streets](https://streets.eyemono.moe)가 기본 반응 이모지를 계정의 NIP-78 덱 문서(kind 30078)에 저장하는 [변경 사항](https://github.com/eyemono-moe/streets/commit/6b31a7c97cc6801cf392ab61c4de4af7d3286233)을 병합했습니다. 이제 다시 로그인하거나 다른 기기에서 로그인한 뒤에도 이모지를 다시 고를 필요가 없습니다. 이전에는 이 선택이 기기의 localStorage에만 저장되었습니다. 덱 문서는 NIP-44로 암호화되므로, 기기 간 동기화를 하려면 암호화를 지원하는 확장 프로그램이나 서명기로 로그인해야 합니다. 다른 로그인 방식에서는 설정이 해당 기기에만 유지됩니다. 계정에 저장된 반응이 없으면 기존 기기 값을 사용하므로 설정이 하트로 초기화되지 않습니다. 저장된 값이 유효하지 않으면 덱의 나머지 부분은 버리지 않고 그 값만 삭제합니다. 이 변경은 소스에 반영되어 있으며, 1.22.0 릴리스 노트는 아직 초안 상태입니다.

### Labradorite {#labradorite}

Labradorite는 페어링된 Linux 컴퓨터의 코딩 에이전트 세션을 제어하는 Android 앱으로, [0.1.0](https://njump.me/nevent1qqsdqkdh6z32nysms5exwtw76n0vp3h2zzxtchh4sfcrywe5tz5gd0czyp6hjpmdntls5n8aa7n7ypzlyjrv0ewch33ml3452wtjx0smhl93jqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkylssg9)과 [0.2.0](https://njump.me/nevent1qqs9pra62cxllt9uggf38lqxsmv7np34f4jjfyr6zath3d4ffn0hlxszyp6hjpmdntls5n8aa7n7ypzlyjrv0ewch33ml3452wtjx0smhl93jqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkn9vmwk)을 공개했습니다. 휴대폰은 제어 인터페이스 역할만 합니다. 에이전트는 컴퓨터의 데몬이 실행하며, 이 데몬은 일반 Nostr relay를 통해 Marmot MLS 메시지를 주고받고 세션마다 하나의 그룹을 사용합니다. 데몬은 기본적으로 비어 있는 허용 목록에 등록된 npub만 받아들입니다([소스](https://gitworkshop.dev/npub1w4uswmv6lu9yel005l3qgheysmr7tk9uvwluddznju3nuxalevvs2d0jr5/relay.ngit.dev/nostr-agents)). 버전 0.1.0은 승인된 세션을 시작하거나 재개하고, 텍스트와 도구 호출, diff를 스트리밍하며, 승인 요청과 질문을 처리합니다. Git 제어와 읽기 전용 파일 탐색 기능도 제공합니다. 버전 0.2.0은 후속 요청을 별도의 턴으로 대기열에 넣고, 사용자가 휴대폰에서 이를 취소할 수 있게 합니다. 또한 데몬이 재시작되어도 대기 중인 작업을 유지하며, 재연결 후에는 놓친 이력을 다시 재생합니다. 이는 게시자의 주장이며, 저희는 보안을 독자적으로 감사하지 않았습니다.

### Nomisma {#nomisma}

Nomisma는 [프로토타입 베타](https://github.com/Lwb89dev/nomisma/tree/46ed9b3190ab93d1acea511677c6d4d18de931b5) 단계의 Android 공동 지출 장부로, 비공개 Nostr 메시지를 통해 두 참여자를 페어링합니다. 잔액만 추적할 뿐 돈을 이동하거나 정산하지는 않습니다. [버전 0.1.3](https://njump.me/nevent1qqszafzumepzzcw68g652k3m47v473y4jac9mhan5fpk344qd0w0m4szypjgcr6nqtr47wpc9fxjepdys2uj0nrpk2pg5pu5udkxe3ukm6r2vqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetknw8e4p)은 페어링된 기기를 자동으로 재연결하고, 저장된 변경 사항을 점점 늘어나는 지연 간격으로 재시도하며, NIP-42 relay 인증을 추가합니다. 누락된 작업도 다시 전송합니다. 두 기기는 작성자별 벡터 클록이 일치한 뒤에야 항목, 결제자, 분할 내역의 SHA-256 지문을 비교합니다. 기본 relay가 변경되었기 때문에 두 기기 모두 0.1.3을 사용하고 relay 설정이 일치해야 합니다. 체크포인트는 15분짜리 NIP-40 만료 기한과 함께 gift wrap 처리됩니다. 이는 relay에 삭제를 요청할 뿐 실제 삭제를 보장하지는 않습니다. 릴리스 노트에는 네이티브 라이브러리 로딩, Schnorr 인자 순서, NIP-44 키 파생에 대한 수정이 보고되어 있으며, 저희는 보안을 독자적으로 감사하지 않았습니다. 사용자 서명은 Amber를 통해 이루어지지만, 기기에는 임시 키도 존재합니다. APK 서명 인증서에 관한 배포 노트의 내용이 서로 상충하므로, 여기서는 업그레이드 호환성에 대해 판단하지 않았습니다.

### Onyx {#onyx}

[Onyx](https://gitworkshop.dev/npub1vx40p5mkcwyrg2gnthf343y39tf0zqxl56ajvql2m9q3rxremynsfp37lu/relay.ngit.dev/onyx)는 검증된 정식 릴리스가 아니라 소스 형태로 제공되는 비공개 일기 프로토타입입니다. 날짜가 붙은 Markdown 파일을 기기에 원본 데이터(source of truth)로 보관하고, 이를 암호화된 kind 30078 event로 relay에 백업합니다. 솔트를 적용한 d-tag를 사용하므로 항목 날짜가 직접 노출되지 않습니다. 복원하려면 별도의 로컬 암호화 키가 필요하므로 사용자는 이 키를 반드시 백업해야 합니다. npub만으로는 일기를 복원할 수 없기 때문입니다. 10월 27일 패치는 게시 전에 요청 필드의 무결성을 확인하는 가드를 추가합니다. 즉, 서명기가 반환한 event의 kind, content, pubkey, tags, 타임스탬프가 요청과 일치해야 합니다. 이 패치는 또한 잘못된 작성자의 다운로드를 거부하고, 더 최신의 로컬 편집 내용을 유지하며, 복원 중에는 데이터를 원자적으로 교체합니다. event 작성자와 타임스탬프는 여전히 공개됩니다. 암호화 명령에 전달된 평문이 로컬 프로세스 검사에 잠시 노출될 수 있으며, 항목을 삭제해도 relay에 있는 사본은 지워지지 않습니다.

### Zzub {#zzub}

[Zzub 0.0.41](https://njump.me/nevent1qqs2rzmlu7hwflagzswk3q6e20nrzp6gcq5rgk4uu2a9kcuuzlhmfyszyrts65qfz5ztnyk3swyz9teyt40kkwskhqkez7kt0yjvaas76jkwuqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkfm8t9z)은 Buzz에서 포크된 커뮤니티 클라이언트입니다. 게시자의 짧은 노트에 따르면, 이번 버전에는 시간대를 지원하는 캘린더 RSVP, 프로필 zap, [NIP-58](/ko/topics/nip-58/) 배지 표시, 그리고 진행 중인 회의에 참여하는 huddle 버튼이 추가되었습니다. 에이전트 제어에는 재시작 옵션과 예산 면제 목록 편집 기능, 새로운 작업 카드 유형이 추가됩니다. 이제 시작 시 캐시된 채널을 사용합니다.

## 프로토콜 및 사양 작업 {#protocol-and-spec-work}

### NIP-CD, 일반 텍스트로 호출하는 명령 정의 {#nip-cd-defines-commands-invoked-as-plain-text}

처음에는 Commands라는 제목이었다가 현재 Slash Commands로 제목이 바뀐 [NIP-CD 사양](/ko/topics/nip-cd/)이 [10월 21일 NIPs 저장소에 병합되었습니다](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)([제안 검토][commands-review]). 실행자(executor)는 트리거, 제목, 설명, 타입이 지정된 위치 인자, 범위(scope)를 나열한 kind 31992 event로 명령을 알립니다. 사용자는 event content의 시작 부분에 일반 텍스트로 명령을 호출하며, 필요하면 실행자의 npub로 한정할 수도 있습니다. 따라서 명령 전용 tag나 클라이언트 지원이 필요하지 않습니다. 한정자 없이 트리거만 쓰면 여러 실행자와 일치할 수 있습니다. 클라이언트는 자동 완성을 제공할 수 있지만, 이를 필수로 요구할 수는 없습니다.

### Marmot, 계정당 다중 기기 채택 {#marmot-adopts-multiple-devices-per-account}

Nostr용 MLS 기반 암호화 그룹 메시징 프로토콜인 [Marmot](/ko/topics/marmot/)은 10월 26일, 이전 초안에서 수정된 형태로 [다중 기기 계정 규칙을 병합했습니다](https://github.com/marmot-protocol/marmot/commit/be923c9cad997176cc155d5d851d40d28e19cc6b)([제안 검토][marmot-devices-review]). 초대자는 하나의 Commit에서 한 계정당 최대 20개의 KeyPackage를 추가할 수 있습니다. 각 기기는 평생 유지되는 무작위 게시 슬롯을 정확히 하나 보유하며, MLS 상태나 비공개 KeyPackage를 절대 복사하지 않습니다. 패키지의 유효 기간은 30일로 하고 7일마다 갱신하는 것이 권장됩니다. 초대자는 적격한 각 기기에 개별 Welcome을 보내며, 계정을 제거하면 그 계정의 모든 leaf가 제거됩니다.

### Marmot, 구성원이 자기 계정의 leaf를 직접 관리하도록 허용 {#marmot-lets-members-manage-their-own-accounts-leaves}

Marmot은 데이터를 전혀 담지 않는 `marmot.group.account-devices.v1`(ID 0x800d)라는 [동일 계정 멤버십 구성 요소를 채택했습니다](https://github.com/marmot-protocol/marmot/pull/443). 그룹 협상에서 이 구성 요소가 요구되면, 구성원은 관리자 권한 없이도 자기 계정에 대한 Add와 Remove를 commit할 수 있습니다. 이 구성 요소에서 구성원은 committer 자신의 leaf를 제거하거나 다른 계정을 제거할 수 없으며, 해당 계정의 관리자 지위도 바뀌지 않습니다. 기존 그룹은 이 구성 요소를 활성화하고 그 지원 불변 조건을 충족해야 합니다.

### Marmot 푸시 트리거에 새 패딩 적용 {#marmot-push-triggers-gain-fresh-padding}

10월 26일 병합된 변경에 따라 Marmot은 [이제 모든 푸시 트리거에 새 패딩을 요구합니다](https://github.com/marmot-protocol/marmot/pull/445). 각 kind 446 트리거는 1,084바이트 크기의 새 CSPRNG 패딩 청크를 최소 하나 포함하므로, 32청크 예산 안에 들어갈 수 있는 실제 암호화 토큰은 최대 31개입니다. 새 패딩이 없으면 동일한 토큰 바이트 때문에 콘텐츠 해시 기반 중복 제거가 이후의 정당한 알림을 억제할 수 있습니다. 서버는 모든 청크를 해시하며, 패딩을 감지할 수 없다는 이유로 구조적으로 유효한 트리거를 거부해서는 안 됩니다. 패딩은 relay와 관찰자에게 토큰 개수를 숨기지만, 복호화를 수행하는 알림 서버는 여전히 이를 볼 수 있습니다.

### Marmot, 신규 구성원을 위한 푸시 토큰 복구 추가 {#marmot-adds-push-token-repair-for-new-members}

Marmot은 10월 26일 [신규 구성원을 위한 푸시 토큰 복구를 병합했으며](https://github.com/marmot-protocol/marmot/pull/447), [후속 변경에서 최종 문구를 명확히 했습니다](https://github.com/marmot-protocol/marmot/blob/e8e09c822ca1a3874d2bd01c1f332d91e70bc97c/features/push-notifications.md). 참여자를 추가하는 Commit의 소유자는 활성 kind 448 토큰 스냅샷과 kind 449 제거 tombstone을 보내는 것이 권장됩니다. kind 447 공지에 선택적으로 지문 집합을 넣으면 피어는 누락된 레코드만 보낼 수 있습니다. 순위가 가장 높은 상위 세 leaf가 시차를 둔 타이머에 따라 응답하며, 공지하는 leaf마다 24시간 속도 제한이 적용됩니다. relay를 통해 전달된 서명 레코드와 보존된 제거 tombstone은 소유자가 오프라인인 동안에도 누락된 토큰 상태를 복구합니다.

### 패스키에 보관된 Nostr 키에 관한 제안 {#proposal-for-passkey-held-nostr-keys}

[패스키에 보관된 Nostr 키에 관한 제안](https://github.com/nostr-protocol/nips/pull/2519)은 패스키를 Nostr 키와 함께 사용하기 위한 기존 방식인 Nosskey를 바탕으로 합니다. 태그가 붙은 핸들은 PRF/HKDF로 파생된 신원과 저장된 키를 구분하며, 암호화된 kind 31778 relay 레코드는 신뢰 당사자(relying party), 작성자, 자격 증명을 서로 결합합니다. 메타데이터가 없거나 알 수 없는 경우에도 새 신원이 암묵적으로 생성되어서는 안 됩니다. 신뢰 당사자 출처(origin) 인가는 여전히 적용되며, 기존 Nosskey 데이터에는 명시적인 마이그레이션 리더가 필요합니다. 파생된 신원은 별도로 백업하지 않으면 패스키와 함께 사라집니다.

### NIP-05 식별자의 DNS 위임 제안 {#proposal-for-dns-delegation-of-nip-05-identifiers}

[NIP-05 DNS 기반 식별자](/ko/topics/nip-05/)를 위한 병합되지 않은 [DNS 위임 제안](https://github.com/nostr-protocol/nips/pull/2527)은 원래의 HTTPS 조회가 404 또는 410을 반환할 때에만 적용되는 대체 경로를 추가합니다. 이때 클라이언트는 HTTPS 제공자를 가리키는 `_nip05` TXT 레코드를 읽습니다. 시간 초과, TLS 또는 CORS 실패, 리디렉션, 키 불일치는 결코 대체 경로를 작동시키지 않으며, DNS에는 키가 저장되지 않습니다. DNSSEC는 권장되지만 선택 사항이므로, 서명되지 않은 DNS에서는 제공자의 TLS만으로 원래 도메인의 인가를 독립적으로 인증할 수 없습니다. 이전 클라이언트는 위임 전용 식별자를 확인(resolve)할 수 없습니다.

### NIP-82로 제안된 소프트웨어 애플리케이션 카탈로그 {#software-application-catalog-proposed-as-nip-82}

[소프트웨어 애플리케이션 카탈로그 제안](https://github.com/nostr-protocol/nips/pull/2526)은 열려 있고 아직 병합되지 않은 해당 풀 리퀘스트에서 NIP-82를 제안 번호로 사용하고 있으며, 이 번호는 할당되거나 채택되지 않았습니다. 이 제안은 앱(32267), 릴리스(30063), 에셋(3063), 큐레이션(30267), 인증서 소유권 증명(30509), 카탈로그 relay 목록(10067)에 대한 kind를 한데 묶습니다. 에셋은 파일 해시와 함께 플랫폼과 런타임을 식별합니다. Android 에셋에는 서명 인증서 해시가 추가됩니다. 증명 서명은 게시자가 해당 인증서를 제어한다는 사실을 보여 주지만, 리더는 여전히 인증서의 만료와 폐기 여부를 확인해야 합니다.

### NIP-A3 결제 대상으로 제안된 BIP 321 URI {#bip-321-uris-proposed-as-nip-a3-payment-targets}

병합되지 않은 [bip321 결제 유형 추가 제안](https://github.com/nostr-protocol/nips/pull/2522)은 이 유형을 [NIP-A3 결제 대상](/ko/topics/nip-a3/)에 더해, kind 10133 event가 완전한 `bitcoin:` URI를 정적이고 재사용 가능한 결제 지침으로 담을 수 있게 합니다. 대상이 재사용되므로 이 제안은 금액과 일회성 BOLT11 `lightning` 인보이스 매개변수를 허용하지 않습니다. 금액은 지불자가 정하고, 결제 방식은 지갑이 지원하는 것 중에서 고르며, Lightning 주소 대체 경로는 유지됩니다.

### BIP 321 대상을 통해 지불되는 zap 제안 {#proposal-for-zaps-paid-through-bip-321-targets}

[BIP 321 대상을 통해 지불되는 zap에 관한 제안](https://github.com/nostr-protocol/nips/pull/2521)에서는 송신자가 수신자의 재사용 가능한 NIP-A3 bip321 대상으로 Ark(오프체인 Bitcoin 프로토콜), Lightning 또는 온체인을 통해 지불한 뒤 kind 9740 zap을 게시합니다. 영수증 키 보유자는 kind 9741로 정산을 확인합니다. 두 kind 번호는 모두 아직 임시값입니다. 결제 참조는 [NIP-44 버전 관리 암호화](/ko/topics/nip-44/)를 사용해 수신자가 사용하기로 선택한 영수증 키를 대상으로 암호화되며, 오직 그 키만 결제를 확인할 수 있습니다. 제3자는 결제 세부 정보를 검증할 수 없으므로, 확인은 수신자의 서명을 신뢰하는 데 달려 있습니다. 이 제안은 [NIP-57 Lightning zap](/ko/topics/nip-57/)을 대체하지 않습니다.

### Nostr Wallet Connect용으로 제안된 Ark 결제 {#ark-payments-proposed-for-nostr-wallet-connect}

병합되지 않은 [Ark 확장 제안](https://github.com/nostr-wallet-connect/nwc/pull/11)은 앱이 원격 지갑을 제어할 수 있게 하는 NIP-47 프로토콜인 [Nostr Wallet Connect](/ko/topics/nip-47/)를 위한 것으로, 새 메서드 없이 기존 BIP 321 지불 및 수신 지원에 Ark 지침을 추가하고 `lookup_payment`에 Ark 결제 레코드를 추가합니다. 지갑은 해당 주소 버전과 네트워크를 지원하고 동일한 Ark 서버를 공유할 때에만 이 지침을 사용합니다. 그렇지 않으면 다른 URI 지침을 시도합니다. 금액은 밀리사토시 반올림 없이 정수 사토시여야 하며, 레코드는 서버가 공동 서명한 결제와 수신자가 수령하여 사용할 수 있는 자금을 구분합니다.

### Blossom 서버용으로 제안된 Ark 결제 헤더 {#ark-payment-header-proposed-for-blossom-servers}

[Ark 결제 헤더 제안](https://github.com/hzrd149/blossom/pull/116)은 HTTP 서버에 미디어 blob을 저장하기 위한 프로토콜인 [Blossom](/ko/topics/blossom/)에서 BUD-07 HTTP 402 결제 필요 응답에 `X-Ark`를 추가합니다. 이 헤더에는 요청마다 새로 생성되는 Ark 주소와 금액을 담은 BIP 321 URI가 들어갑니다. 선택적으로, 이 URI는 같은 결제를 Lightning 인보이스 형태로도 담습니다. 증명을 위해 클라이언트는 정산 후 지불한 Ark 주소와 함께 재시도합니다. 대체 경로를 사용한 클라이언트는 Lightning preimage와 함께 재시도합니다. HEAD 요청은 증명과 함께 재시도되지 않으며, 클라이언트는 GET 또는 PUT으로 넘어갑니다.

### 노트 내 자산 언급을 위한 캐시태그 제안 {#cashtag-proposal-for-asset-mentions-in-notes}

[캐시태그 제안](https://github.com/nostr-protocol/nips/pull/2528)은 `$` 뒤에 2~6개의 ASCII 영문자가 오는 형태를 선택적으로 토큰화하는 방식을 정의하며, 코드, URL, Nostr 참조는 제외합니다. 티커만으로는 자산을 고유하게 식별할 수 없으므로, 단일 cashtag tag가 표시 모드를 설정하고 작성자가 선택한 자산 ID를 첨부할 수 있습니다. 리더는 심볼이 체인 및 주소와 일치하는지 확인하고, 불일치는 라벨을 바꾸지 않은 채 표시만 합니다. 선택적인 `t` tag(형식: `$ticker`)를 사용하면 표준 relay 검색이 가능합니다.

### Napplet 게임패드 사양 철회 {#napplet-gamepad-specification-withdrawn}

Napplet 사양이 게시되는 NAPs 저장소는 10월 27일 [게임패드 사양 제거를 병합했습니다](https://github.com/napplet/naps/pull/129). 이 변경은 NAP-GAMEPAD.md를 삭제하고 이전의 채택을 되돌립니다. 현재 채택된 게임패드 NAP는 없습니다.

### Cyberspace 높이 tag, 그룹 tag와의 충돌 회피 {#cyberspace-height-tags-avoid-group-tag-collisions}

Nostr 기반 공간 프로토콜인 Cyberspace는 DECK이라고 부르는 자체 사양 여러 개를 병합했습니다. 이는 프로젝트 사양이며 공식 NIP가 아닙니다. 이제 사양은 [bag과 chat의 높이 tag 이름을 `h`에서 `H`로 변경합니다](https://github.com/arkin0x/cyberspace/pull/73). 소문자 tag가 NIP-29 그룹 tag와 충돌하여 event가 거부되거나 잘못 분류되었습니다. 리더는 레거시 `h`로 대체하는데, 이는 `H`가 없을 때에만 해당합니다. 이 변경은 프로젝트 사양만 바꿉니다. NIP-29를 수정하거나 배포된 클라이언트 간의 상호 운용성을 입증하는 것은 아닙니다.

### Cyberspace 숨겨진 오디오 {#cyberspace-hidden-audio}

[DECK-0007은 숨겨진 오디오를 정의합니다](https://github.com/arkin0x/cyberspace/pull/79). 숨겨진 오디오는 암호화된 Blossom 파일로, 서명된 bag 또는 chest 안에 있는 서명되지 않은 rumor가 이를 참조합니다. 따라서 오디오를 숨긴 사람은 재생 가능한 별도의 서명된 공개 게시물을 통해 귀속되지 않습니다. 배치할 때마다 새 키와 암호문을 사용하지만, 누구든 여전히 키를 공유할 수 있습니다. 이 사양은 암호화가 발견자의 프라이버시를 보장한다거나 URL 규칙이 모든 SSRF를 차단한다고 주장하지 않으며, 리더 지원은 아직 진행 중입니다.

### Cyberspace 공개 모델과 애니메이션 {#cyberspace-public-models-and-animation}

[이제 아이템은 bob 및 spin 애니메이션과 함께 공개 SNO 모델을 참조할 수 있으며](https://github.com/arkin0x/cyberspace/pull/74), 모델이 유효하지 않거나 사용할 수 없을 때에는 기존 렌더링으로 대체됩니다. 라이브 모델은 변경되거나 사라질 수 있으며, 폭넓은 채택을 주장하지는 않습니다.

### Cyberspace 아이템, chat, 댓글 사양 {#cyberspace-item-chat-and-comment-specifications}

[선택 사항인 DECK 0004부터 0006까지](https://github.com/arkin0x/cyberspace/pull/67)는 아이템, chest, 리스팅, 암호화된 로컬 chat, 봉인된 댓글에 대한 기존 코드를 합성 테스트 벡터와 함께 문서화합니다. 여러 문제가 아직 해결되지 않은 상태입니다. bag과 chest의 서명 방식이 서로 다르며, 봉인된 댓글은 공개 tag를 통해 부모 ID와 kind를 노출합니다. 보유자는 리스팅을 재정의할 수 있습니다. chat에는 재전송(replay) 및 컨텍스트 바인딩 측면의 공백이 있으며, chest 참조는 구현되지 않았습니다. 이 문서화는 어떤 보안 문제도 수정하지 않으며, 배포에 해당하지도 않습니다.

### 다중 작성자 event 제안 {#multi-author-events-proposal}

서명된 장문 기사인 [Multi-Author Nostr Events as a Soft Fork](https://njump.me/nevent1qqszlhx6hpwf0th2mk760n7cxqdknglwshgprpupsk4tj0nkr2n66wgzypzcxhpk7swe0x7gz2vrpuh4myjk9af584h7mht0xz48jjq8xrexuxjg87j)는 ID 해시가 여러 작성자 pubkey를 포괄하고 각 작성자가 동일한 ID에 서명하는 event를 제안합니다. 이전 클라이언트에는 새 형식의 데이터와 조회 힌트 역할을 하는 Q tag를 담은 secp256k1 호환 래퍼가 보이게 됩니다. 피어는 연결마다 새 형식을 협상하게 됩니다. 이 기사는 작성자가 앞서 내놓은 양자 내성(post-quantum) 제안을 일반화한 것으로, 그 제안은 미래의 키를 공동 작성자 한 명으로 추가하는 방식입니다. 이는 번호가 부여되지 않은 제안이며, 승인된 NIP가 아닙니다. 공동 작성된 naddr의 교체와 바이너리 전송은 여전히 미해결 질문으로 남아 있습니다.

### Buzz NIP-AR 동기화 구독, 라이브 head 전에 완전한 스냅샷 전송 {#buzz-nip-ar-sync-subscriptions-send-a-complete-snapshot-before-live-heads}

열려 있는 Buzz 풀 리퀘스트 하나가 [NIP-AR](/ko/topics/nip-ar/) WebSocket 동기화 구독을 제안합니다([#8522](https://github.com/block/buzz/pull/8522)). relay는 REPEATABLE READ에서 읽은 일관된 아티팩트 집합을 보내고, 그 집합이 완전해진 뒤에만 EOSE를 내보낸 다음 라이브 current head를 스트리밍하게 됩니다. 라이브 Redis 등록은 초기 읽기보다 먼저 이루어집니다. Redis 연결 끊김이나 지연이 발생하면 구독이 CLOSED로 종료되고 재동기화가 필요하며, 접근 권한 변경, redaction, 큐 가득 참의 경우도 마찬가지입니다. 구독은 최대 4,096개의 아티팩트로 제한되며, 이 변경은 저희 소스 기준 시점에 병합되지 않았고 프로덕션에서 사용할 수 없었습니다.

### HTTP를 통한 Buzz NIP-AR 아티팩트 증분 읽기 {#buzz-nip-ar-incremental-artifact-reads-over-http}

별도의 열려 있는 Buzz 풀 리퀘스트는 NIP-AR 아티팩트에 대한 증분 HTTP 읽기를 추가합니다([#8523](https://github.com/block/buzz/pull/8523)). 클라이언트는 데이터베이스 수정 타임스탬프와 안정적인 ID를 기준으로 120초의 겹침 구간을 두고 페이지를 넘기며, 현재 리비전 또는 제거 정보를 받습니다. 클라이언트는 알려진 ID를 복구할 수 있습니다. 결과는 최종 일관성 모델을 따릅니다. 이 제안은 완전한 스냅샷을 약속하지 않으며, 아티팩트가 없다고 해서 삭제되었거나 접근 권한을 잃었다는 의미는 아닙니다. 최신 리비전을 받으려면 멤버십이 있거나, 목록에 공개되지 않은 개방형 채널의 경우 명시적인 #h 범위가 필요하며, 목록 공개 상태가 바뀌면 증분 진행 상황이 초기화됩니다. 기능 게이트인 BUZZ_ARTIFACT_INCREMENTAL_ENABLED는 꺼져 있으며, 모든 writer와 마이그레이션(현재 0074~0076)이 갖춰져 있어야 합니다. 이 120초 지연은 운영상의 가정입니다. 저희 소스 기준 시점에 이 변경은 여전히 열려 있었습니다.

### 위임된 메트릭 리더를 위한 NIP-AM 초안 문서 {#draft-nip-am-text-for-delegated-metric-readers}

Buzz의 초안 문서 풀 리퀘스트 하나는 런타임 인가를 변경하지 않은 채 [NIP-AM](/ko/topics/nip-am/) 메트릭에 대한 위임된 리더를 명시합니다([#8582](https://github.com/block/buzz/pull/8582)). agent가 소유자에게 암호화한 kind 44200 event는 그대로 유지되며, agent는 활성 grant마다 별도의 NIP-44 사본을 내보내고, 각 사본은 소유자가 작성한 정확한 grant event ID에 결합됩니다. 제안된 grant kind 30180과 리더 수 상한은 아직 미해결 질문이며, 이력, 철회, 공개적 연결(linkage)도 마찬가지입니다. 서명된 철회가 있더라도 수신자가 이미 보유한 사본을 지울 수는 없으며, 이 초안은 저희 소스 기준 시점에 병합되지 않았습니다.

### DECK-0003, 부모가 배치하는 객체를 직접 담을 수 있도록 허용 {#deck-0003-lets-a-parent-carry-the-objects-it-places}

열려 있는 Cyberspace 풀 리퀘스트 하나가 인라인 SNO 객체 페이로드의 루트 테이블인 DECK-0003 §1.10을 제안합니다([#81](https://github.com/arkin0x/cyberspace/pull/81)). 부모의 사본에 항목이 존재하면, 그 항목이 유효하지 않더라도 네트워크 가져오기 없이 우선 적용됩니다. 각 항목은 작성자 pubkey로 범위가 한정되며, 크기 및 깊이 제한과 순환 제한이 적용됩니다. 이전 리더는 누락된 객체를 가져오고 자리 표시자를 표시합니다. 이 제안은 이 변경을 기다리며 보류된 구현들을 설명하고 있으며, 이 변경은 저희 소스 기준 시점에 병합되지 않았습니다.

### DECK-0004, 파생된 방 키를 사용하는 높이 기반 문 정의 {#deck-0004-defines-height-bound-doors-with-derived-room-keys}

열려 있는 Cyberspace pull request 하나가 외형(looks)과 문(doors)에 관한 DECK-0004 §3.6 및 §3.7을 추가합니다([#82](https://github.com/arkin0x/cyberspace/pull/82)). 문은 높이에 묶여 있으며, room key는 SHA-256(domain separator ‖ location key ‖ door secret)이고 방의 bag은 이 키로 암호화됩니다. 방에는 여러 개의 문이나 중첩된 문이 있을 수 있으며, 새 잠금을 설정하면 키가 교체됩니다. 첫 구현이 나오기 전까지 이 문서에는 test vector가 없으며, 저희 소스 마감 시점까지 병합되지 않았습니다.

### nostream NIP-11 피어링 광고 확장 {#nostream-nip-11-peering-advertisement-extension}

열려 있는 nostream pull request는 relay의 NIP-11 문서에 피어링 섹션을 추가하려 합니다([#999](https://github.com/cameri/nostream/pull/999)). 이 섹션은 시간 범위와 정산 조건이 붙은 피드 kind를 광고하며, 연락 엔드포인트와 피어링 작업증명(proof-of-work)도 함께 제시합니다. `enabled: false`만이 이 섹션을 비활성화하며, 조건이 비어 있으면 정산 없는(settlement-free) 피어링을 뜻합니다. 광고된 제안이 곧 수락된 피어인 것은 아닙니다. 이 변경은 피어 합의나 유료 연합(federation)을 구현하지 않습니다. 저희 소스 마감 시점까지 병합되지 않은 상태였습니다.

### NIP-CD, 선택적 설치 명령 목록 추가 {#nip-cd-adds-optional-installed-command-lists}

NIP-CD의 후속 변경이 [10월 27일 NIPs 기본 브랜치에 병합되었으며](https://github.com/nostr-protocol/nips/pull/2525) ([병합][cd-installed-merge]), 이제 사양 제목은 Slash Commands입니다. 이 변경은 [NIP-51](/ko/topics/nip-51/)을 따르는 선택적 kind 10992 목록을 정의합니다. 사용자는 이 목록에 kind 31992 명령 정의를 가리키는 address tag를 보관하며, 각 정의는 executor pubkey와 d 값으로 식별되고 선택적으로 relay 힌트를 포함할 수 있습니다. 사용자는 이 목록을 유지할 수 있으며, 클라이언트는 자동완성과 렌더링된 칩에 이를 사용하는 것이 권장됩니다. 이 목록은 표시 및 발견에 관한 선호 설정입니다. executor에게 권한을 부여하지 않으며, 일반 텍스트 호출은 이 목록 없이도 여전히 작동하고, 명령 전용 tag나 필수 클라이언트 지원도 필요하지 않습니다. NIP-CD는 여전히 선택적 초안이며, 이번 병합만으로는 어떤 클라이언트가 이 목록을 채택했는지 알 수 없습니다.

### Marmot, 계정 기기에 대한 공정 준비 규칙 범위 축소 {#marmot-narrows-its-fair-preparation-rule-for-account-devices}

Marmot은 계정 기기를 요구하는 그룹의 스케줄링 규칙에 대한 [수정을 10월 28일 병합했습니다](https://github.com/marmot-protocol/marmot/pull/450). 제한된 수렴 패스가 Stable에 도달한 뒤에는, 대기열의 인바운드 작업만으로 또 다른 패스를 강제할 수 있게 되기 전에, 관리자가 승인한 대기 중 intent 하나 또는 같은 계정에서 나온 허용된 intent 하나가 준비 시도 기회를 얻습니다. SelfUpdate와 Leave는 이 추가 공정성 보장에서 제외되지만, 어떤 멤버든 여전히 이를 commit할 수 있습니다. 이 변경은 승인된 모든 intent를 포괄하던 이전 문구를 바로잡으며, 계정 기기를 요구하지 않는 그룹은 기존 스케줄링을 유지합니다. 와이어 형식 변경은 없습니다. 또한 준비 시도가 유효하거나 수락되거나 정식(canonical)인 Commit을 보장하지는 않습니다.

### Marmot, 계정 그룹용 숨겨진 기기 명부 제안 {#marmot-proposes-a-hidden-device-roster-for-account-groups}

아직 병합되지 않은 열린 Marmot 제안 하나는 모든 leaf가 하나의 계정에 속하는 숨겨진 그룹을 위해 ID가 0x800e인 [device-roster-v1 컴포넌트를 추가하려 합니다](https://github.com/marmot-protocol/marmot/pull/452). 그룹은 생성 시점부터 명부를 지니거나, 아예 지니지 않습니다. 명부는 기기, 거부된 슬롯, 거부된 KeyPackage, leaf map을 기록하며, 후보 부모(candidate parent)에 적용되는 명시적이고 순서에 무관한 diff 업데이트를 사용하는 최초의 컴포넌트입니다. 제거된 슬롯은 형제 기기가 그 슬롯을 제거할 수 없는 그룹에 대해 leaf map을 유지할 수 있습니다. 기기는 자신이 직접 생성했거나, 확인된 링크로 인증된 Welcome을 통해 참여한 경우에만 기기 그룹을 신뢰합니다. 따라서 0x800e 표시만으로는 어떤 신뢰도 부여되지 않습니다. 창립 Add는 확인된 링크에서 나온 정확한 KeyPackage를 지정합니다. 탈취된 연결 기기는 제거될 때까지 명부를 편집할 수 있습니다. 기기 상한은 기기에 적용됩니다. leaf map 레코드와 거부 레코드에는 항목별 크기 제한이 있지만 레코드 수 상한은 없습니다. 명부 데이터는 결코 다른 계정으로 복사되지 않으며, 그룹은 채팅, 개수 표시, 알림, 대상 목록에서 계속 숨겨집니다. 본문에 따르면 MDK는 새로운 일반 UI 없이 명부 바이트를 테스트 스위치 뒤에 두고 있습니다.

### Marmot, 계정 기기 활성화 실패 시 더 명확한 피드백 제안 {#marmot-proposes-clearer-feedback-when-account-device-activation-fails}

역시 병합되지 않은 또 다른 열린 Marmot 제안은 계정 기기와 관련해 [클라이언트가 활성화 실패를 설명할 수 있게 하려 합니다](https://github.com/marmot-protocol/marmot/pull/453). 클라이언트는 어떤 그룹이 계정 기기를 활성화할 수 없다고 보고할 수 있습니다. 다만 이러한 그룹 수준 피드백으로는 활성화를 가로막는 멤버나 기기를 지목할 수 없습니다. 활성 관리자가 아닌 멤버는 자신에게 관리자 지위가 없다는 사실만 알게 됩니다. 브랜치 선택이 유실되거나 재생성된 활성화 검사가 실패하면, 사용자는 새로 요청해야 합니다. 클라이언트는 활성화를 자동으로 재시도하지 않습니다. 활성화에는 승인된 클라이언트에서 나온 사용자의 새로운 요청이 필요하다는 기존 규칙은 그대로입니다. 이는 초안 상태의 규범 문서이며, 구현되거나 배포된 동작을 보여주는 것은 아닙니다.

### Marmot, 새 기기 페어링을 위한 이모지 검증 제안 {#marmot-proposes-emoji-verification-for-pairing-new-devices}

병합되지 않은 한 열린 Marmot 제안은 X25519, HKDF, HMAC을 사용하며 Matrix m.sas.v1을 본뜬 교환을 통해 [새 기기를 페어링하는 방식을 설명합니다](https://github.com/marmot-protocol/marmot/pull/454). 사용자는 양쪽 화면에 표시된, 레이블이 붙은 이모지 7개를 비교하며 코드를 읽거나 입력하지 않습니다. 계정 키를 보유한다고 해서 기기가 인증되는 경우는 결코 없습니다. 서명되지 않은 rumor 다섯 개(Request, Answer, Reveal, Confirm, Cancel)는 계정 pubkey 앞으로 wrap되며, 계정, 세션, 새 KeyPackageRef, 기존 기기 슬롯, 새로 생성한 키를 결속합니다. 먼저 확인하는 쪽은 기존 기기이며, 확인된 KeyPackageRef만을 정확히 추가합니다. 새 기기는 검증을 마친 후에만 확인하며, 확인된 교환으로 인증된 그룹 ID에 대한 Welcome만 수락합니다. kind 452부터 456까지가 제안되었고, 457부터 489까지는 예약되어 있습니다. 계정 키 보유자는 확인 이후에도 여전히 Cancel을 위조해 서비스를 거부할 수 있습니다. 시간당 Answer 제한은 재시작 후에는 유지되지 않습니다. relay는 wrap 버스트와 계정 주소를 볼 수 있으며, 일부 병합 및 Welcome 사례는 아직 보류되어 있습니다. 구현체는 이 형식들을 기본적으로 꺼 두며, 작성자가 제공한 known-answer vector 두 개는 독립적인 보안 감사나 상호운용성 감사가 아닙니다.

### NIP-5D napplet 제안, 미디어 및 소스 필드 강화 {#nip-5d-napplet-proposal-tightens-media-and-source-fields}

[열린 NIP-5D napplet 제안](https://github.com/nostr-protocol/nips/pull/2303)은 앞서 소개한 바 있습니다. 이 제안의 10월 28일 변경 사항이 이제 NIPs 기본 브랜치가 아닌 제안 브랜치에 병합되어, 10월 17일에 도입된 선택적 미디어 및 소스 필드를 개정했습니다. 스크린샷 및 미리보기 tag는 이제 [NIP-92](/ko/topics/nip-92/) key-value 필드를 재사용하며, 필수인 소문자 SHA-256 x 값 하나와 선택적인 m, dim, size, alt, duration으로 구성됩니다. 읽는 측은 렌더링하기 전에 해시를 검증하고 실제 형식을 디코딩해야 합니다. 유효한 m 필드가 있다면, 디코딩된 형식도 그 MIME 타입과 일치해야 합니다. x가 없거나 중복되었거나 잘못된 항목은 무시됩니다. 잘못된 선택 필드는 사용 가능한 다른 미디어를 버리지 않은 채 제외되며, 미리보기가 여러 개이면 무시됩니다. source-commit은 정확한 전체 Git ID로 확인(resolve)되어야 하고, HTTPS 소스 아카이브는 바이트 수준에서 SHA-256이 정확히 일치해야 합니다. 중복되거나 형식이 잘못된 소스 필드는 무시되며, 사용할 수 없는 소스 데이터 때문에 HTML 재생이 막혀서는 안 됩니다. 커밋이나 아카이브가 일치한다고 해서 재현 가능한 빌드가 증명되는 것은 아니며, 클라이언트 적합성(conformance)도 주장되지 않습니다.

## Nostr의 여섯 번의 10월 {#six-years-of-nostr-octobers}

여섯 번의 10월에 걸쳐, 날짜가 기록된 Nostr의 변경 사항은 메시지 프레이밍에서 출발해 그 위에 구축된 애플리케이션으로 점점 바깥을 향해 나아갔습니다. 2021년에 기본 사양은 [클라이언트 메시지를 최상위 JSON 배열로 프레이밍하도록 확정했습니다](https://github.com/nostr-protocol/nostr/commit/69509f40cd6a4d5c14a7c402b04495a1de5ab2c2). 이후의 10월들에는 클라이언트 검색과 Lightning 인보이스, 타임스탬프 증거와 작업 요청, 미디어 변형과 ecash 지갑, 그리고 코드 협업과 비공개 메시지 메타데이터가 차례로 등장했습니다. 같은 달들에 이루어진 다른 변경은 눈에 보이는 relay 상태부터 별도의 서명자 키와 지갑 페어링에 이르기까지, 신원과 연결을 프로그램 사이에서 옮기기 쉽게 만들었습니다. 올해 10월에는 같은 문서가 [빈 필터 목록이 무엇과 일치하는지 정의했습니다](https://github.com/nostr-protocol/nips/commit/37db639582d857e12468dcccd99b2c7f1d657da9). 그 결과 동일한 JSON을 읽는 relay들은 이제 그것이 어떤 event를 선택하는지에 관해 공통 규칙을 갖게 되었습니다.

### 2021년 10월: 전송을 모호함 없이 만들기 {#october-2021-making-the-transport-unambiguous}

10월 4일, 기본 프로토콜 사양인 [NIP-01](/ko/topics/nip-01/)이 [클라이언트 메시지가 최상위 JSON 배열이 되도록 개정되었습니다](https://github.com/nostr-protocol/nostr/commit/69509f40cd6a4d5c14a7c402b04495a1de5ab2c2). 비공식적으로 쓰이던 EVENT, REQ, CLOSE 접두사는 각 배열의 첫 번째 요소가 되었습니다. 고정된 `/ws` 경로 요구 사항도 삭제되어, 어떤 WebSocket 엔드포인트든 사용할 수 있게 되었습니다. 이는 이미 코드가 뒷받침하고 있던 사양을 명확히 한 것이었습니다. 독립적으로 작성된 클라이언트들이 더 정교한 무언가를 상호운용하려면, 그보다 먼저 정확한 프레이밍이 필요합니다.

10월 23일에는 [relay에서 클라이언트로 가는 방향에 명시적인 EVENT 및 NOTICE 메시지가 생겼습니다](https://github.com/nostr-protocol/nostr/commit/97786e31423b45239306323a9a297188d20dbf21). relay의 EVENT는 기존 REQ 구독의 식별자를 담기 때문에, 하나의 연결로 여러 구독을 실행하는 클라이언트가 결과를 요청과 대응시킬 수 있습니다. NOTICE는 사람이 읽을 수 있는 텍스트를 담습니다. 이처럼 작은 어휘는 여러 차례 독립적으로 구현하기에 실용적이며, 이는 별도로 운영되는 relay들에 잘 맞습니다.

[10월 23일자 NIP-01 텍스트](https://github.com/nostr-protocol/nostr/blob/97786e31423b45239306323a9a297188d20dbf21/nips/01.md)는 서명이 무엇을 포괄하는지도 보여줍니다. event의 ID는 맨 앞의 0, 작성자의 공개 키, 타임스탬프, kind, tag, content를 담은 압축된 UTF-8 JSON 배열의 다이제스트이며, 작성자는 secp256k1 곡선 위의 Schnorr 서명으로 그 다이제스트에 서명합니다. WebSocket 봉투와 구독 식별자는 그 서명된 데이터 바깥에 있습니다. 이 텍스트에 따르면, 동일한 서명된 event가 다시 서명되지 않고도 서로 다른 구독이나 서로 다른 연결을 통해 도착할 수 있습니다. REQ는 먼저 일치하는 저장된 event를 반환한 다음, 클라이언트가 CLOSE를 보내거나, 소켓을 닫거나, 구독 ID를 새 REQ에 재사용할 때까지 실시간 상태로 유지됩니다. 하나의 필터 안의 조건은 모두 충족되어야 하지만, 하나의 REQ에 들어 있는 여러 필터는 그중 어느 하나라도 만족하는 event와 일치합니다. 그 버전의 필터 이름은 오늘날의 것과 다릅니다. NOTICE 동작은 명시되지 않았으며, relay가 event를 얼마나 오래 보관하는지나 쿼리가 event를 모두 반환하는지에 대해서도 아무것도 보장되지 않았습니다. 5년 뒤, 같은 사양은 REQ 안의 필터가 무엇을 의미하는지라는 문제로 다시 돌아오게 됩니다.

### 2022년 10월: 휴대폰에서 쓸 수 있게 된 피드 {#october-2022-a-feed-becomes-usable-on-a-phone}

10월 8일, iOS용 Nostr 클라이언트인 Damus가 [해시태그, 프로필, event 검색을 추가했습니다](https://github.com/damus-io/damus/commit/2c4c392b76d9ad92b28e71d6d578bdb42c2ac3de). 이 변경은 검색 결과 뷰와 스레드 모델을 수정하여, 독자가 들어오는 텍스트를 스크롤하는 것에 더해 서명된 신원이나 특정 event로 바로 이동할 수 있게 했습니다. 이 검색은 클라이언트 자체의 탐색 기능 안에서 작동했으며, relay 측 전문 검색은 아니었습니다.

8일 뒤, Damus는 [relay 설정 화면의 단순한 행들을 각 연결의 상태를 보여주는 뷰로 교체했습니다](https://github.com/damus-io/damus/commit/e5e0fb2db279a5a2763d39b15d5fff20bec26fdd). 색깔 점은 클라이언트의 relay 풀 상태를 읽어 표시합니다. 초록색은 연결됨, 노란색은 연결 중 또는 재연결 중을 뜻하며, 빨간색은 그 밖의 모든 상태를, 회색은 첫 판독 이전을 나타냅니다. 뷰는 화면에 나타날 때 새로 고쳐지고, 그 뒤로는 2초마다 새로 고쳐집니다. 이미 있던 스와이프 삭제 기능은 새 뷰로 옮겨졌습니다. 점이 보이게 되면서 멈춘 피드를 더 이상 작성자의 침묵으로 해석할 필요가 없어졌습니다. 독자가 여러 독립적인 연결 가운데 어느 것이 연결되어 있고 어느 것이 재시도 중인지 볼 수 있었기 때문입니다. 초록색 점이 보여주는 것은 열린 소켓입니다. relay가 event를 수락했거나 보관했다는 사실을 보여주지는 않습니다. 쿼리가 relay에 있는 모든 것을 반환했다는 사실도 보여주지 않습니다. 이 커밋은 병합된 소스에 구현을 기록한 것입니다. 이 소스 변경으로 App Store 출시 날짜가 확정되지는 않습니다.

10월 19일, Damus는 게시물, 채팅, 다이렉트 메시지에서 쓰이는 [BOLT11 Lightning 인보이스 파서와 인보이스 위젯을 추가했습니다](https://github.com/damus-io/damus/commit/c6ab1de63926ff7f6e29a260e3e7f2473855c9c7). 위젯에는 인보이스 설명과 사토시 단위 금액이 표시되며, Pay 버튼은 `lightning:` URI를 iOS를 통해 설치된 처리기로 넘깁니다. 서명된 게시물을 보여주는 것은 소셜 클라이언트이고, 결제는 별도의 지갑이 합니다. 이 위젯은 이후의 zap 영수증 규약보다 먼저 나왔으므로, 표준화된 zap이 아니라 인보이스를 표시하는 기능입니다.

### 2023년 10월: 증거와 작업 요청을 담게 된 event {#october-2023-events-carry-evidence-and-requests-for-work}

10월 11일, event에 관한 증거를 Bitcoin에 고정하는 [NIP-03](/ko/topics/nip-03/) OpenTimestamps 증명이 [event의 `ots` 필드에서 별도의 kind 1040 event로 옮겨졌습니다](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e). 그 event는 `e` tag로 원본을 지정하고, 최소 하나의 Bitcoin 증명을 포함한 전체 base64 OpenTimestamps 파일을 content에 담습니다. 참조된 event id 자체가 증명이 입증하는 다이제스트이므로, 검증자는 해당 event가 증명된 시각까지 존재했다는 사실을 알 수 있습니다. 그 시각은 작성자의 `created_at`가 아니라 Bitcoin에서 나옵니다. 이 증명은 event의 시점을 확정할 뿐, 그 content에 대해서는 아무런 주장도 하지 않습니다.

10월 12일에는 타임스탬프 변경과 별개로 [NIP-06](/ko/topics/nip-06/) 키 파생에 [test vector 두 개가 추가되었습니다](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b). 니모닉은 복구 시드를 인코딩하는 단어의 나열입니다. 이 vector들은 12단어 니모닉 하나와 24단어 니모닉 하나를 다루며, 각각에 대해 16진수 형식과 nsec 및 npub 인코딩으로 된 예상 개인 키와 공개 키를 제시합니다. NIP-06은 이미 BIP-39를 사용해 니모닉을 이진 시드로 바꾸고 BIP-32 경로 `m/44'/1237'/<account>'/0/0`를 사용해 키를 파생했으며, 계정 0을 기본적인 단일 키 선택지로 삼고 있었습니다. 10월에 추가된 것은 니모닉 복구나 새로운 파생 알고리즘이 아니라 known answer였습니다. 이제 클라이언트는 자신의 파생과 인코딩이 문서화된 신원을 재현하는지 확인할 수 있습니다. vector와 일치하면 구현체들을 서로 비교할 수 있게 됩니다. 그렇다고 특정 구현체가 인증되는 것은 아니며, 모든 지갑과 클라이언트의 가져오기 결과가 일치한다는 것이 증명되는 것도 아닙니다. 시드를 도난으로부터 보호하는 일은 이 vector들이 다루지 않는 별개의 문제입니다.

10월 29일, data vending machine 표준인 [NIP-90](/ko/topics/nip-90/)이 [고정된 job kind와 함께 NIPs 저장소에 병합되었습니다](https://github.com/nostr-protocol/nips/commit/7a2de8ab25ceaa35376e6b7457f08b5bffde70b3). 이 표준은 kind 5000부터 5999까지를 job 요청용으로 예약했으며, 각 결과 kind는 요청 kind에 1000을 더한 값으로 정했습니다. 피드백에는 kind 7000이 쓰였습니다. 요청은 텍스트, URL 또는 이전 job을 가리킬 수 있습니다. 기대하는 출력을 지정하고 선택적인 입찰가(bid)를 제시하는 것도 가능합니다. 따라서 작업은 특정 벤더의 API 바깥에 있는, 어떤 제공자든 응답할 수 있는 서명된 event 안에 존재합니다. 이전 초안에서는 kind 68001과 68002를 사용했었습니다.

### 2024년 10월: 미디어 대체 버전과 이식 가능한 이캐시 {#october-2024-media-alternatives-and-portable-ecash}

10월 15일, [NIP-71](/ko/topics/nip-71/) 동영상 event가 [동영상 변형(variant)에 `imeta` tag를 채택했습니다](https://github.com/nostr-protocol/nips/commit/1cda2dcc594538ea14b88aec7f1f784e06a31bbf). 당시의 addressable kind 34235와 34236에서는 각 변형의 URL, 크기, MIME 타입, 미리보기 이미지, fallback이 하나의 tag 안에 함께 담겼습니다. 해상도를 고르는 클라이언트는 어떤 썸네일과 fallback이 그 해상도에 속하는지 알아야 하는데, 평면화된 메타데이터로는 이를 표현할 수 없었습니다. 이 kind 번호들은 과거의 것입니다. 현재 NIP-71은 kind 21과 22를 사용합니다.

열흘 뒤, 둘 다 이전 초안에서 도입되었던 [NIP-60](/ko/topics/nip-60/) Cashu 지갑과 [NIP-61](/ko/topics/nip-61/) nutzap이 [사양으로 함께 병합되었습니다](https://github.com/nostr-protocol/nips/commit/ba46b23d95b186c9a8fedabf8324af2ae40e8ce4). 이 둘은 mint가 토큰을 발행하는 이캐시 프로토콜인 Cashu를 기반으로 합니다. NIP-60은 암호화된 지갑 proof를 relay에 보관하므로, 호환되는 애플리케이션들이 동일한 지갑 상태에 접근할 수 있습니다. NIP-61에서는 수신자의 kind 10019 event가 신뢰하는 mint, relay, 잠금 키(locking key)를 나열하고, 송신자의 kind 9321 event는 수신자가 상환(redeem)할 수 있도록 그 키에 잠긴 proof를 담습니다. 사용자는 여전히 토큰을 발행하는 mint에 의존하며, 애플리케이션은 같은 proof가 두 번 상환되지 않도록 방어해야 합니다.

10월 29일, 별도의 서비스가 사용자를 대신해 서명하는 키를 보유하는 방식인 [NIP-46](/ko/topics/nip-46/) 원격 서명이 [`bunker://` 연결 문자열에 원격 signer의 공개 키가 담기도록 개정되었습니다](https://github.com/nostr-protocol/nips/commit/f1e8d2c4f764d66996c0c1fb2eeabfbc0c7b2528). 사용자의 신원은 별도로 얻습니다. [개정된 본문](https://github.com/nostr-protocol/nips/blob/f1e8d2c4f764d66996c0c1fb2eeabfbc0c7b2528/46.md)은 클라이언트가 두 키를 구분하고 연결 후 `get_public_key`를 호출하도록 요구합니다. 클라이언트는 이 대화를 위해 자체 키쌍을 생성하고 암호화된 요청을 signer의 키 앞으로 보내며, `sign_event`는 사용자의 키로 서명된 event를 반환합니다. 두 키는 같을 수도 있지만 반드시 같아야 하는 것은 아닙니다. 연결 문자열의 키는 signer 서비스만을 식별합니다. 사용자의 계정은 `get_public_key`가 반환하는 공개 키입니다. NIP-60이 나흘 전에 공유 지갑 상태를 다루었다면, 이번 개정은 그와는 별개의 관심사인 signer 신원을 다룹니다. 해당 커밋 시점의 예시는 여전히 당시 NIP-46이 규정한 암호화 전송 방식을 사용합니다. 또한 이 변경은 원격 signer를 신뢰가 필요 없는 존재로 만들지도 않고, 누가 사용자의 키를 보유하는지 증명하지도 않습니다.

### 2025년 10월: 협업 업데이트와 비공개 메시지 메타데이터 {#october-2025-collaboration-updates-and-private-message-metadata}

10월 8일, [NIP-47](/ko/topics/nip-47/) Nostr Wallet Connect에 [앱과 지갑을 페어링하기 위한 딥 링크가 추가되었습니다](https://github.com/nostr-protocol/nips/commit/2ace01cf1ad0a68dae6217111c9286e3de759923). 지갑은 `nostrnwc://connect` 또는 앱 전용 `nostrnwc+{app_name}://connect`를 등록할 수 있으며, 요청하는 앱은 URI 인코딩된 아이콘, 자신의 이름, 콜백 스킴을 붙여 그 링크를 엽니다. 지갑이 연결을 생성하고 나면 `value` 파라미터에 페어링 코드, 즉 `nostr+walletconnect://` URI를 담아 콜백을 엽니다. Damus가 iOS를 통해 인보이스를 지갑에 넘긴 지 3년 만에, 한 휴대폰 안에서의 페어링이 더 이상 같은 화면에 표시된 QR 코드를 스캔하거나 앱 사이에서 긴 문자열을 복사하는 일을 뜻하지 않아도 되게 되었습니다. 이 추가 사항은 이 인계 과정만을 다룹니다. 결제 방식은 전혀 바꾸지 않으며, 그 자체로는 아무것도 결제하지 않습니다. 두 앱 모두 핸들러를 구현해야 하며, 사양 문서가 모든 지갑이 이를 구현했다는 증거가 되지는 않습니다. 지출 한도, 동의 화면, 어떤 앱이 콜백 스킴을 안전하게 소유할 수 있는지에 대한 문제도 이것으로 해결되지 않습니다.

10월 16일, [NIP-34](/ko/topics/nip-34/) git 협업에 기존 patch event와 나란히 [kind 1618 pull request event와 kind 1619 update event가 추가되었습니다](https://github.com/nostr-protocol/nips/commit/6e6b9877b32b44e84c0f3c3d412d688cf86761b0). Pull request는 커밋 tip과 clone 위치를 지정하고, update는 그 tip을 이동시킵니다. Patch는 60 kB 미만이 권장되며, 그보다 큰 제출물에는 pull request가 권장됩니다. 이로써 더 큰 제출물의 권장 경로가 event 안에 담긴 patch 본문에서 커밋에 대한 서명된 참조로 옮겨갔으며, 더 작은 변경은 여전히 patch로 전달될 수 있습니다. Nostr는 조율과 서명된 참조를 전달하고, 그 참조가 가리키는 커밋 객체는 여전히 Git 서버가 제공합니다.

10월 27일, [NIP-59](/ko/topics/nip-59/) gift wrap에 [seal과 gift wrap의 타임스탬프를 각각 독립적으로 무작위화하라는 지침이 추가되었습니다](https://github.com/nostr-protocol/nips/commit/bcaad2957d0e9cec20e4265298d2788be87d3190). 이는 만료 tag를 추가하는 경우에 해당합니다. Gift wrap은 메시지를 이 두 겹으로 감싸는데, 각 층에 고유한 무작위 타임스탬프를 부여하면 층 간 타이밍이 상관될 수 있는 정도가 줄어듭니다. 여기서 관심은 콘텐츠 암호화에서, 메타데이터 상관관계가 드러낼 수 있는 정보를 제한하는 쪽으로 옮겨갔습니다. 암호화는 메시지 자체를 숨기지만 봉투 주변의 타이밍과 기타 메타데이터는 여전히 관찰 가능하며, 이들이 얼마나 쉽게 연결될 수 있는지는 구현상의 선택에 달려 있습니다. 이 지침은 새로운 암호화를 추가하지 않으며, 참여자를 익명으로 만들어 주지도 않습니다.

### 2026년 10월: 공유된 쿼리 의미와 텍스트로 호출되는 서비스 {#october-2026-shared-query-meanings-and-text-triggered-services}

10월 5일, [NIP-92](/ko/topics/nip-92/) 미디어 첨부가 [`imeta` tag를 kind 0 프로필로 확장했습니다](https://github.com/nostr-protocol/nips/commit/a79e21d90fce5465b50ef385dd368bba99ec4a0b). 이에 따라 프로필은 fallback URL, blurhash(흐린 미리보기를 압축적으로 인코딩한 값), 크기, 대체 텍스트 및 기타 첨부 메타데이터로 자신의 `picture`와 `banner`를 기술할 수 있게 되었습니다. NIP-92는 이 변경 이전부터 존재했습니다. 새로운 점은 2024년에 NIP-71이 동영상 변형에 적용했던 묶음형 메타데이터가 이제 프로필 이미지에까지 적용된다는 것입니다. 대응 관계는 정확히 일치해야 성립합니다. Tag는 그 URL이 picture 또는 banner URL과 같을 때에만 적용되고, 클라이언트는 어느 쪽과도 일치하지 않는 tag를 무시해야 하며(SHOULD), 기본 URL이 실패하면 fallback을 시도해야 합니다(SHOULD). 새 kind 0 event는 이전 프로필을 대체하므로, 게시자는 변경되지 않은 이미지의 메타데이터를 그대로 이어서 포함하고 더 이상 쓰이지 않는 이미지의 tag는 제거해야 합니다(SHOULD). 그래야 오래된 대체 텍스트나 크기 정보가 다른 사진을 슬그머니 기술하는 일이 생기지 않습니다. 이 갱신 규칙은 새 필드만큼이나 중요합니다. `imeta` tag는 이미지가 계속 이용 가능하거나 더 빨리 로드된다는 것을 보장하지 않습니다. 어떤 프라이버시 보호도 제공하지 않으며, 클라이언트가 모든 필드를 렌더링해야 하는 것도 아닙니다.

10월 17일, [NIP-01이 명확히 정리되어 필터 안의 빈 목록은 어떤 event와도 일치하지 않게 되었으며](https://github.com/nostr-protocol/nips/commit/37db639582d857e12468dcccd99b2c7f1d657da9), 이는 해당 속성을 아예 생략하는 것과는 다릅니다. [후속 변경에서는 일관되지 않은 "하나 이상" 문구를 제거하고, 클라이언트가 일치할 수 없는 목록을 보내지 않도록 권장했습니다](https://github.com/nostr-protocol/nips/commit/0b5532c0355ab27f447e071a93c09cf3a2b4aad5). 2021년 10월에 이 문서는 REQ의 JSON 메시지 프레이밍에 대해 합의했습니다. REQ 메시지는 배열이고, 각 필터는 그 안에 있는 JSON 객체입니다. 이번 10월에는 그러한 필터 안의 빈 목록이 무엇을 의미하는지를 확정하여 필터 의미론을 정리했습니다. 같은 프레임을 동일하게 파싱하는 relay들이라도 서로 다른 결과를 반환할 수 있었기 때문입니다.

10월 21일, [당시 Commands라는 제목이었던 NIP-CD가 제안 단계에서 병합된 초안 사양으로 넘어갔습니다](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4). 이 사양은 슬래시 명령을 기술합니다. Kind 31992 event가 명령을 정의하며, 호출은 event content의 첫 글자에서 시작하는 일반 텍스트이므로 클라이언트가 이를 보내는 데 특별한 지원이 필요하지 않습니다. 별도 브랜치의 [이전 커밋](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)과 함께 진행된 [후속 제안](https://github.com/nostr-protocol/nips/pull/2525)은 [10월 27일에 병합되었습니다](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157). 이 제안은 사양의 제목을 Slash Commands로 바꾸고, 클라이언트가 자동 완성과 렌더링에 사용해야 하는 선택적 kind 10992 설치 명령 목록을 추가했습니다. 이 목록은 사용자 선호를 기록할 뿐이며, 실행자에게 권한을 부여하거나 일반 텍스트 호출을 제한하지 않습니다. NIP-90 job은 구조화된 요청 event와 결과 event를 사용하는 반면, 명령은 일반 텍스트로 읽을 수 있는 형태로 남습니다.
