---
title: 'Nostr Compass #20'
date: 2026-04-29
publishDate: 2026-04-29
draft: false
type: newsletters
translationOf: /en/newsletters/2026-04-29-newsletter.md
translationDate: 2026-07-01
description: 'GitWorkshop는 브라우저 내 PR 병합 버튼, 저장소 팔로우, 대역폭 효율적인 git 탐색기, git-over-Nostr용 인라인 코드 리뷰 코멘트를 출시했습니다; Routstrd는 Nostr 프로바이더 공지와 Cashu 결제를 이용한 로컬 추론 라우터를 시작했습니다; 릴리스에는 ngit v2.4.2, Wisp v1.0.0, grain v0.5.2와 v0.5.3, Mostro Core v0.10.0, Mostro Mobile v1.2.5, marmot-ts v0.5.0, CruxCoach v0.1.3, Meiso v1.3.0, NoorNote, Nostria, Nostr Calendar, nos2x-fox, applesauce, nostr-double-ratchet가 포함됩니다; 미출시 작업은 Amethyst Nests, nostream NIP-65/NWC, FIPS Nostr 기반 udp:nat 부트스트랩, strfry 관측성, Sprout 소유자 증명, Zap Cooking 레시피 팩을 다룹니다; 새로 추적된 프로젝트에는 Nostrord, Clave, Treasures, smesh, Surveil, Fundstr, Nod City, deploy-nsite-to-pages, null--nostr가 포함됩니다; 월말 회고는 2021년부터 2026년까지의 Nostr 4월을 다룹니다.'
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr에 대한 주간 가이드입니다.

**이번 주:** [GitWorkshop](#gitworkshop-ships-in-browser-pr-merge-repository-following-and-a-bandwidth-efficient-git-explorer)은 브라우저 내 PR 병합 버튼, Stars 및 저장소 팔로우, 대역폭 효율적인 git 탐색기, kind `1111` 인라인 리뷰 코멘트, 암호화된 다중 기기 알림 상태를 통해 git-over-Nostr를 더 완전한 코드 리뷰 표면으로 만듭니다. [Routstrd](#routstrd-launches-a-local-router-for-inference-over-nostr)는 Nostr kind `38421` 공지를 통해 모델 프로바이더를 발견하고 Cashu로 결제하는 로컬 데몬을 출시합니다. 태그된 릴리스에는 [ngit v2.4.2](#ngit-v242-fixes-grasp-relay-detection-for-pr-submissions), [Wisp v1.0.0](#wisp-v100-graduates-from-beta), [grain v0.5.2와 v0.5.3](#grain-v052-fixes-websocket-lockup-v053-continues-polish), [Mostro Core v0.10.0 및 Mostro Mobile v1.2.5](#mostro-core-v0100-and-mostro-mobile-v125-adopt-nip-59-dual-key-gift-wrap), [marmot-ts v0.5.0](#marmot-ts-v050-ships-addressable-keypackages), [CruxCoach v0.1.3](#cruxcoach-v013-ships-encrypted-climbing-data-backup-with-nostr-and-blossom), [Meiso v1.3.0](#meiso-v130-adds-subtasks-blossom-attachments-and-nip-89-tagging), NoorNote, Nostria, Nostr Calendar, nos2x-fox, applesauce, nostr-double-ratchet 등이 포함됩니다. 미출시 변경 사항은 [Amethyst Nests](#amethyst-advances-nests-audio-rooms-with-moq-interop-testing), [nostream NIP-65 및 NWC](#nostream-adds-nip-65-relay-list-support-and-nwc-payments), [FIPS Nostr 기반 udp:nat 부트스트랩](#fips-adds-nostr-based-udpnat-bootstrap), [strfry 관측성](#strfry-adds-per-connection-observability), [Sprout 소유자 증명](#sprout-adds-owner-attestation-and-multi-workspace-support), [Zap Cooking 레시피 팩](#zap-cooking-adds-recipe-packs-delete-requests-and-bunker-login)을 다룹니다. 새로 추적된 프로젝트에는 [Nostrord](#nostrord-a-nip-29-client-built-with-kotlin-multiplatform-and-wasm), [Clave](#clave-brings-nip-46-remote-signing-to-ios-via-apns), Treasures, smesh, Surveil, Fundstr, Nod City, deploy-nsite-to-pages, null--nostr가 포함됩니다. 그리고 월말 회고는 2021년부터 2026년까지 여섯 번의 Nostr 4월을 되짚어봅니다.

## 주요 소식

### GitWorkshop, 브라우저 내 PR 병합, 저장소 팔로우, 대역폭 효율적인 git 탐색기 출시

[GitWorkshop](https://gitworkshop.dev)은 Dan Conway가 [NIP-34](/ko/topics/nip-34/) git-over-Nostr용으로 만든 웹 기반 협업 계층으로, 이번 주에 개발자들이 GitHub 또는 GitLab에서 기대하는 워크플로우에 훨씬 가까워지면서도 코멘트, 저장소 목록, 알림을 서명된 Nostr 이벤트 내부에 유지하는 주요 릴리스를 출시했습니다.

가장 큰 추가 기능은 GRASP 릴레이를 사용하는 저장소를 위해 오랫동안 기다려온 브라우저 내 PR 병합 버튼입니다. 이 릴리스는 또한 반응과 [NIP-51](/ko/topics/nip-51/) 리스트를 기반으로 구축된 Stars 및 저장소 팔로우를 추가하며, 고정된 저장소 세트는 kind `10617` 이벤트로 게시되어 순서가 지정된 `a` 태그를 통해 kind `30617` 저장소 공지를 가리킵니다. 이제 프로필 페이지에 이식 가능한 저장소 목록을 표시할 수 있습니다.

대역폭 효율적인 git 탐색기가 이전의 브라우저 내 얕은 clone을 대체합니다. 새로운 탐색기는 GRASP가 구축된 기본 git 클라이언트/서버 프로토콜에 의존하므로, 브라우저가 전체 팩을 가져오도록 강제하지 않고도 큰 저장소를 처리할 수 있습니다. 검색은 이제 사용자명과 저장소 메타데이터를 다루며, [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)과 네트워크 전체에서 저장소 공지를 발견하고 동기화하는 `ngit-indexer` 릴레이 구현으로 구동됩니다. 브라우저 내 저장소 생성 워크플로우가 발견 및 온보딩 경로를 마무리합니다.

리뷰 도구는 Files Changed 탭, 패치별 diff 뷰어, 그리고 실험적인 새 프리미티브 세트를 중심으로 재구축되었습니다. 인라인 코드 리뷰 코멘트는 kind `1111`을 사용하며, [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md)를 기반으로 합니다: 각 코멘트는 파일 경로(`f` 태그), 커밋 SHA(`c` 태그), 선택된 라인 범위(`line` 태그)를 가리키므로 클라이언트가 diff의 올바른 위치에 코멘트를 렌더링할 수 있습니다. 두 번째 계층의 실험적 프리미티브는 작성자와 저장소 관리자가 권한을 부여하며 [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) 레이블을 사용합니다: 제출 후 Issue 또는 PR 제목 변경, 제출 후 해시태그 추가, 편집 가능한 요약을 위해 PR 또는 Issue의 상단에 버전 관리된 CoverNote 고정, 인라인 코드 논의 서브스레드를 해결됨으로 표시. Verdict 이벤트와 `suggestion` 블록은 여전히 초안 상태이며 아직 출시되지 않았습니다.

기기 간 알림 상태도 Nostr를 통해 동기화되지만, 프라이버시를 보존하는 방식으로 이루어집니다. GitWorkshop은 전용 알림 keypair를 생성하고, 그 nsec를 암호화한 다음 kind `30078` 이벤트 안에 저장합니다. 알림 nsec는 실제 알림 상태 이벤트에 서명합니다. 이 간접 참조는 사용자의 메인 signer가 읽기 또는 아카이브 작업마다 빈번한 암호화 및 복호화 요청으로 스팸을 받는 것을 방지하고, 외부 관찰자가 사용자가 알림 상태를 만지는 시점을 쉽게 볼 수 없도록 합니다. 사용자는 기기 간에 읽기 및 아카이브 상태를 동기화할 수 있으며, 릴레이는 암호화된 blob만 볼 수 있습니다.

### Routstrd, Nostr를 통한 추론을 위한 로컬 라우터 출시

[Routstrd](https://github.com/routstr/routstrd)는 로컬 도구에 OpenAI 호환 엔드포인트를 제공하고 각 요청을 경쟁하는 [Routstr](https://routstr.com) 프로바이더로 라우팅하는 새로운 TypeScript 데몬입니다. 데몬은 Routstr의 RIP-02 사양에 정의된 Nostr kind `38421` 공지를 통해 프로바이더를 발견합니다. 그런 다음 RIP-06 하에서 가격, 신뢰, 최근 성능으로 프로바이더 점수를 매기고 각 요청을 현재 최고의 옵션으로 보냅니다.

결제는 cocod가 관리하고 Lightning으로 자금을 조달하는 로컬 Cashu 지갑을 통해 실행됩니다. 이는 클라이언트에게 sats 단위 정산 경로를 제공하는 동시에 Nostr 릴레이를 통한 프로바이더 발견을 공개적이고 무허가 상태로 유지합니다. 세션 중 프로바이더가 실패하면 Routstrd는 다음 순위 노드로 대체할 수 있습니다. 설치 경로는 `bun install -g routstrd`이며, 지갑과 릴레이 설정을 위해 `routstrd onboard`가 뒤따릅니다.

더 넓은 [Routstr org](https://github.com/routstr)는 데몬, Python 노드 소프트웨어(`routstr-core`), 채팅 UI, 프로토콜 사양을 유지 관리합니다. 사용자에게 로컬 포트는 안정적인 인터페이스가 됩니다: 기존 OpenAI 호환 도구가 Routstrd를 가리키고, 데몬이 프로바이더 발견, 라우팅, 결제를 처리합니다.

## 태그된 릴리스

### ngit v2.4.2, PR 제출을 위한 GRASP 서버 감지 수정

[ngit](https://codeberg.org/DanConwayDev/ngit-cli)은 저장소 GRASP 서버 감지 수정 사항을 포함한 [v2.4.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.2)를 출시하여, 제안이 PR kind를 사용할 때 PR 제출이 정상 경로를 유지하도록 했습니다. ngit는 현재 대부분의 변경 사항에 대해 크지 않은 한 `Patch` kind를 기본으로 사용하며, 관리자는 기본값을 변경하기 위해 노력하고 있습니다. 이번 주 초에 출시된 [v2.4.1](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.1)은 저장소의 지정된 git 서버에서 열려 있는 PR의 git 데이터를 사용할 수 없을 때 clone과 fetch 중 발생하는 `fatal` 오류를 수정했습니다.

### Wisp v1.0.0, 베타 졸업

[Wisp](https://github.com/barrydeen/wisp)는 릴레이 라우팅, 프라이버시, 작은 네이티브 UI에 초점을 맞춘 Kotlin 및 Jetpack Compose Android 클라이언트로, [v1.0.0](https://github.com/barrydeen/wisp/releases/tag/v1.0.0)을 출시하고 이어서 [v1.0.2](https://github.com/barrydeen/wisp/releases/tag/v1.0.2)를 출시했습니다. 1.0.0 마일스톤은 [Newsletter #19](/ko/newsletters/2026-04-22-newsletter/#wisp-v0180-beta-adds-normie-mode-for-you-feed-and-nip-29-group-config)에서 다룬 Normie Mode 법정화폐 표시 토글, For You 피드, [NIP-29](/ko/topics/nip-29/) 릴레이 기반 그룹 구성, [NIP-65](/ko/topics/nip-65/) 릴레이 리스트 브로드캐스팅을 모읍니다. v1.0.2는 Android 15 16 KB 페이지 크기 지원, 드로어 시트의 QR 스캔 탭, 인라인 비디오 컨트롤용 다운로드 버튼, 알림 리스트 성능 수정을 추가합니다.

### grain v0.5.2, WebSocket 잠금 수정; v0.5.3, 다듬기 계속

0ceanSlim의 Go 릴레이인 [grain](https://github.com/0ceanSlim/grain)은 v0.5.0에서 도입된 WebSocket 잠금에 대한 중요한 핫픽스로 [v0.5.2](https://github.com/0ceanSlim/grain/releases/tag/v0.5.2)를 릴리스한 다음 [v0.5.3](https://github.com/0ceanSlim/grain/releases/tag/v0.5.3)을 이어서 출시했습니다. 잠금은 일부 필터 및 WebSocket 경로에서 연결이 멈추게 했으므로 v0.5.1 또는 v0.5.0 운영자는 업그레이드해야 합니다. grain은 모든 주요 Nostr 이벤트 카테고리를 추적하고, NIP-11 릴레이 정보를 노출하며, 화이트리스트/블랙리스트 접근 제어, kind별 요율 제한, 웹 대시보드, v0.5.x 라인에 추가된 Go 클라이언트 라이브러리를 지원합니다.

### Mostro Core v0.10.0 및 Mostro Mobile v1.2.5, NIP-59 이중 키 gift wrap 채택

[Mostro Core v0.10.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.10.0)은 분리된 identity 및 거래 키를 갖춘 새로운 [NIP-59](/ko/topics/nip-59/) gift-wrap 모듈을 추가합니다. 이전 전송 코드는 거래 identity와 gift wrapping 모두에 단일 identity 키를 사용했습니다. v0.10.0은 안정적인 거래 identity를 임시 wrapping 키로부터 분리하므로, 각 거래는 거래 프로토콜에 필요한 identity를 보존하면서 새로운 전송 키를 사용할 수 있습니다. 데몬 통합은 [Mostro PR #718](https://github.com/MostroP2P/mostro/pull/718)을 통해 이루어지며, [mostro-cli PR #165](https://github.com/MostroP2P/mostro-cli/pull/165)는 동일한 마이그레이션을 커맨드라인 클라이언트에 적용합니다.

[Mostro Mobile v1.2.5](https://github.com/MostroP2P/mobile/releases/tag/v1.2.5)는 프로토콜 작업과 함께 출시됩니다. [PR #581](https://github.com/MostroP2P/mobile/pull/581)은 taker가 maker의 계정 나이로 offer를 필터링할 수 있게 하여, 사용자에게 주문서에서 새로 생성된 maker 계정을 피할 방법을 제공합니다. [PR #580](https://github.com/MostroP2P/mobile/pull/580)은 취소된 주문 세부 정보의 역할 레이블을 수정하고, [PR #576](https://github.com/MostroP2P/mobile/pull/576)은 협조적 취소 버튼을 정리합니다.

### marmot-ts v0.5.0, 주소 지정 가능한 KeyPackages 출시

[marmot-ts](https://github.com/marmot-protocol/marmot-ts)는 TypeScript [Marmot](/ko/topics/marmot/) 클라이언트의 첫 번째 계획된 breaking change 릴리스인 [@internet-privacy/marmot-ts@0.5.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/%40internet-privacy%2Fmarmot-ts%400.5.0)을 출시했습니다. [PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68)은 주소 지정 가능한 KeyPackage 지원을 추가합니다: `KeyPackageManager`는 이제 레거시 kind `443` 및 새로운 kind `30443` KeyPackage 이벤트를 모두 처리할 수 있습니다. 이 릴리스는 `KeyPackageStore`와 group-state 저장소 클래스를 제거하고, `KeyPackageManager` 및 `MarmotGroup`에 전달되는 제네릭 key-value 저장소로 대체합니다. 또한 초대 및 그룹 관리를 `MarmotClient.invites` 및 `MarmotClient.groups`로 이동하므로, 직접 임베드하는 사용자는 업그레이드 전에 생성자 및 저장소를 변경해야 합니다.

### CruxCoach v0.1.3, Nostr와 Blossom을 사용한 암호화된 클라이밍 데이터 백업 출시

[CruxCoach](https://codeberg.org/CruxCoach/CruxCoach)는 Kilter Board 클라이머를 위한 새로운 오픈소스 Android 앱입니다. Kilter Board는 홀드가 Bluetooth를 통해 켜져 경로를 표시하는 인터랙티브 트레이닝 벽입니다. 앱은 4월 14일에 출시되었고 4월 26일에 [v0.1.3](https://codeberg.org/CruxCoach/CruxCoach/releases/tag/v0.1.3)에 도달했습니다.

v0.1.3은 선택적 암호화된 클라우드 백업을 추가합니다. 사용자의 CruxCoach 계정은 Nostr keypair이며, private 키는 로컬 백업 암호화 키의 입력 역할도 합니다. 앱은 기기에서 클라이밍 데이터를 암호화하고 암호문을 Blossom 저장 서버(`blossom.primal.net` 및 `nostr.download`)에 미러링합니다. 원격 삭제 작업은 Blossom 정리 경로를 호출합니다. 백업 외에도 CruxCoach는 Amber 지원을 위한 [NIP-46](/ko/topics/nip-46/) 원격 서명, 앱 내 개발자 연락을 위한 [NIP-17](/ko/topics/nip-17/) private DM, 릴레이 검색을 위한 [NIP-65](/ko/topics/nip-65/) 릴레이 리스트, Nostr 플러밍을 위한 Vitor Pamplona의 [Quartz](https://github.com/vitorpamplona/quartz) 라이브러리를 사용합니다. 사용자는 Zapstore 또는 직접 Codeberg APK를 통해 설치할 수 있습니다.

### Meiso v1.3.0, subtask, Blossom 첨부 파일, NIP-89 태깅 추가

[Meiso](https://github.com/higedamc/meiso)는 [NIP-44](/ko/topics/nip-44/) 암호화된 kind `30078` 애플리케이션 데이터로 Nostr 릴레이에 작업을 저장하는 Android용 미니멀리스트 Flutter 작업 관리자입니다. 4월 6일에 출시된 [v1.3.0](https://github.com/higedamc/meiso/releases/tag/v1.3.0)은 부모/자식 관계가 있는 subtask, blocks/blocked-by/related-to/duplicate-of를 위한 작업 링크, Blossom 및 [NIP-96](/ko/topics/nip-96/) HTTP 파일 업로드 엔드포인트를 통한 이미지 첨부 파일, 게시된 이벤트의 [NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md) 권장 애플리케이션 `client` 태그, Go 커맨드라인 동기화 도구를 추가합니다. v1.3.0은 또한 콜드 스타트 릴레이 동작 및 Amber 클라이언트 재사용을 수정합니다.

### NoorNote, Nostria, Nostr Calendar, nos2x-fox 및 라이브러리 릴리스

[NoorNote](https://github.com/77elements/noornote)는 [v0.8.7](https://github.com/77elements/noornote/releases/tag/v0.8.7), [v0.8.8](https://github.com/77elements/noornote/releases/tag/v0.8.8), [v0.8.9](https://github.com/77elements/noornote/releases/tag/v0.8.9)를 게시했습니다. 이러한 릴리스는 인용된 리포스트에서 이미지 및 비디오 클릭 처리를 수정하고, 롱폼 기사 이미지에 대한 lightbox 지원을 추가하며, 빈 데스크톱 시작 화면을 수정합니다. [Nostria](https://github.com/nostria-app/nostria)는 [v3.1.29](https://github.com/nostria-app/nostria/releases/tag/v3.1.29), [v3.1.30](https://github.com/nostria-app/nostria/releases/tag/v3.1.30), [v3.1.31](https://github.com/nostria-app/nostria/releases/tag/v3.1.31)을 출시하여 article-editor 이미지 압축, 지갑 USD 토글, 프로모션 카드 컨트롤, PDF 지원, 모바일 레이아웃 다듬기를 추가했습니다.

[Nostr Calendar v1.4.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.1)은 캘린더 이벤트 게시를 캘린더 리스트 관리에서 분리하고 초대 추적을 수정합니다. [nos2x-fox v1.19.0](https://github.com/diegogurpegui/nos2x-fox/releases/tag/v1.19.0)은 Firefox NIP-07 브라우저 서명 grant에 대한 사용자 정의 인증 시간 프레임을 추가합니다. [nostr-double-ratchet v0.0.97](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.97)은 새로운 바이너리를 출시합니다. [nostr-wot-sdk 0.9.0](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%400.9.0)은 기본적으로 `NostrSessionProvider`를 마운트하며, [nostr-tools PR #535](https://github.com/nbd-wtf/nostr-tools/pull/535)는 NIP-47 wallet-connect 문자열에 대한 다중 릴레이 파싱 지원을 추가합니다.

주 후반에는 [Amber v6.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre1)이 더 나은 새 앱 연결 레이아웃, signer 대화 상자 수정, 개선된 알림 권한 처리, 재구성된 계정 선택을 포함한 사전 릴리스를 출시했습니다. [nostr-vpn v0.3.14](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.14)는 macOS Apple Silicon, Linux 및 Windows 아티팩트로 새 빌드를 출시했습니다. [Bitcredit Core v0.5.7-hotfix-1 및 v0.5.8](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.8)은 고아 블록 검증 문제에 대한 연속 수정을 출시했습니다. [Surveil v0.1.6](https://gitlab.com/chad.curtis/surveil/-/tags/v0.1.6)은 모바일 UI 다듬기와 개편된 About 페이지를 가져왔습니다. 프로젝트 자체는 [아래](#surveil-a-magic-the-gathering-deck-builder-on-nostr)에서 소개됩니다.

### applesauce 6.0.0, 레거시 이벤트 팩토리 제거 및 Blossom URI 파싱 추가

hzrd149의 TypeScript Nostr 툴킷인 [applesauce](https://github.com/hzrd149/applesauce)는 monorepo 전반에 걸쳐 6.0.0 릴리스 열차를 출시했습니다. [applesauce-core@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.0.0)은 레거시 `EventFactory` 클래스와 이전의 `buildEvent`, `modifyEvent`, `createEvent` 헬퍼를 제거하고, 호출자를 `applesauce-core/factories` 및 `applesauce-common`의 새로운 팩토리 클래스로 안내합니다. 또한 IP 주소 및 로컬호스트 처리를 링크 파싱에 추가하고, BUD-10 Blossom URI 정규 표현식, `timeoutWithIgnore`, `combineLatestBy`, `combineLatestByIndex`, `combineLatestByKey`와 같은 새로운 observable 헬퍼를 추가합니다.

패키지 수준 릴리스는 Nostr 특정 부분을 채웁니다. [applesauce-content@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-content%406.0.0)은 텍스트 및 Markdown용 BUD-10 Blossom URI 노드를 추가하여, 렌더러에 콘텐츠에서 Blossom 참조를 파싱할 수 있는 일급 방법을 제공합니다. [applesauce-actions@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-actions%406.0.0)은 릴레이, 사용자, 항목을 다루는 NIP-51 리스트를 위한 기본 팩토리 클래스를 추가하여 리스트 구성을 덜 임시적으로 만듭니다. [applesauce-wallet-connect@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet-connect%406.0.0)은 `WalletConnect.connectURI`를 노출하므로 앱이 기존 NIP-47 wallet-connect URI에 직접 액세스할 수 있습니다.

## 미출시 변경 사항

### Amethyst, MoQ 상호 운용성 테스트로 Nests 오디오 룸 진전

[Amethyst](https://github.com/vitorpamplona/amethyst)는 지난주의 [Media over QUIC](https://datatracker.ietf.org/group/moq/about/) 오디오 룸 스택을 기반으로 이번 주에 여러 Nests 중심 PR을 병합했습니다. [PR #2622](https://github.com/vitorpamplona/amethyst/pull/2622)는 Amethyst MoQ 클라이언트를 참조 웹 구현에 대해 훈련하는 교차 클라이언트 상호 운용성 하네스를 추가합니다. 목표는 사용자가 부딪히기 전에 Android/브라우저 wire 레벨 차이를 잡는 것입니다. [PR #2625](https://github.com/vitorpamplona/amethyst/pull/2625)는 picture-in-picture 스피커 포커스와 연결 상태를 개선하는 반면, [PR #2620](https://github.com/vitorpamplona/amethyst/pull/2620)은 참가자 그리드에서 아바타, 음소거 상태, 말하는 상태를 명확하게 합니다. 주 후반에는 [PR #2634](https://github.com/vitorpamplona/amethyst/pull/2634)가 전체 화면 Nest 뷰에서 IME 패딩과 창 인셋을 수정하고 [PR #2635](https://github.com/vitorpamplona/amethyst/pull/2635)는 Nests 피드에 존재 기반 신선도 필터링을 추가합니다. 별도로, [PR #2627](https://github.com/vitorpamplona/amethyst/pull/2627)은 Amethyst의 사용자 정의 C secp256k1 구현을 제거하고 `libschnorr256k1`으로 마이그레이션합니다.

### nostream, NIP-65 릴레이 리스트 지원 및 NWC 결제 추가

[nostream](https://github.com/Cameri/nostream)은 지난주의 53개 PR 릴레이 스프린트 이후 세 개의 주목할 만한 PR을 병합했습니다. [NIP-65](/ko/topics/nip-65/) 릴레이 리스트 메타데이터 지원은 [PR #585](https://github.com/Cameri/nostream/pull/585)에 도착하여, 릴레이가 kind `10002` 릴레이 리스트 이벤트를 인덱싱하고 제공할 수 있습니다. Nostr Wallet Connect 결제 프로세서는 [PR #539](https://github.com/Cameri/nostream/pull/539)에서 이어져 pay-to-relay 경로를 추가합니다. 연결 정리는 [PR #438](https://github.com/Cameri/nostream/pull/438)에서 개선되며, 활성 구독이 있는 소켓이 회수되지 않아 장기 실행 인스턴스에서 구독 수가 드리프트되는 죽은 연결 버그를 수정합니다.

### FIPS, Nostr 기반 udp:nat 부트스트랩 추가

[FIPS](https://github.com/jmcorgan/fips)는 [Newsletter #6](/ko/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking) 및 [Newsletter #10](/ko/newsletters/2026-03-25-newsletter/#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples)에서 이전에 다루었던 Free Internetworking Peering System으로, Nostr 기반 `udp:nat` 부트스트랩과 함께 [PR #53](https://github.com/jmcorgan/fips/pull/53)을 병합했습니다. 이 변경은 노드가 Nostr 광고를 게시하고, 암호화된 offer/answer 시그널링을 교환하며, STUN을 통해 공용 주소를 발견하고, UDP 홀 펀칭을 수행하며, 펀치된 소켓을 일반 FIPS 전송 스택으로 넘길 수 있게 합니다. 구현은 신호 페이로드 identity를 실제 Nostr 발신자에게 바인딩하고, 인박스 조회를 위해 구성된 DM 및 광고 릴레이를 쿼리하며, 실패한 채택된 순회 핸드오프를 롤백하여 고아 UDP 전송이 활성 상태로 남지 않도록 합니다. 이것이 canonical 저장소인 `jmcorgan/fips`에서 추적할 Nostr 공지 및 NAT 순회 작업입니다.

### strfry, 연결별 관측성 추가

[strfry](https://github.com/hoytech/strfry)는 [PR #214](https://github.com/hoytech/strfry/pull/214)를 병합하여 연결별 관측성과 Prometheus를 통해 내보낼 수 있는 연결 수준 메트릭을 추가했습니다. [PR #204](https://github.com/hoytech/strfry/pull/204)는 Prometheus 레이블을 정규화하고, [PR #215](https://github.com/hoytech/strfry/pull/215)는 strfry 위에 구축된 Namecoin identity 프로젝트를 다루는 Community Integrations 섹션을 문서에 추가합니다.

### Sprout, Owner Attestation 및 다중 워크스페이스 지원 추가

Block의 Nostr 클라이언트인 [Sprout](https://github.com/block/sprout)는 NIP-OA(Owner Attestation)를 구현하는 [PR #406](https://github.com/block/sprout/pull/406)을 병합했습니다. 이 기능은 자율 에이전트에게 특정 인간 pubkey가 그 행동을 승인했다는 암호학적 증명을 제공합니다. [PR #409](https://github.com/block/sprout/pull/409)는 데스크톱 앱에 다중 워크스페이스 지원을 추가하고, [PR #411](https://github.com/block/sprout/pull/411)은 모바일 작성에 `#channel` 자동완성을 추가하며, [PR #410](https://github.com/block/sprout/pull/410)은 활성 채널 메시지를 드롭할 수 있는 race window를 닫습니다. [PR #413](https://github.com/block/sprout/pull/413)은 기기 간 읽기 상태 동기화를 위한 NIP-RS를 도입하고, 후속 [PR #420](https://github.com/block/sprout/pull/420) 및 [PR #422](https://github.com/block/sprout/pull/422)는 그 읽기 상태를 모바일 미확인 배지에 연결합니다.

### Zap Cooking, 레시피 팩, 삭제 요청, bunker 로그인 추가

[Zap Cooking](https://github.com/zapcooking/frontend)은 생산적인 레시피 게시 작업 주간을 병합했습니다. 사용자 자신의 Recipe Pack에 대한 [NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md) 삭제 요청은 [PR #367](https://github.com/zapcooking/frontend/pull/367)에 도착합니다. 게시 신뢰성은 모든 새 레시피를 garden 릴레이로 강제하고 공유 레시피 세트에 대한 재시도 큐를 추가하는 [PR #366](https://github.com/zapcooking/frontend/pull/366)을 통해 개선됩니다. 원클릭 저자 팩 게시는 [PR #365](https://github.com/zapcooking/frontend/pull/365)에 도착하고, [PR #331](https://github.com/zapcooking/frontend/pull/331)은 [NIP-46](/ko/topics/nip-46/) bunker 로그인 지원을 추가합니다.

### Whitenoise-rs, 로컬 데이터베이스 암호화

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)는 [PR #758](https://github.com/marmot-protocol/whitenoise-rs/pull/758)을 병합하여 온디스크 Whitenoise 데이터베이스에 SQLCipher 암호화를 추가했습니다. 이는 Marmot 데몬 스택에 대한 오랫동안 지속된 정지 상태 보안 격차를 좁힙니다. [PR #775](https://github.com/marmot-protocol/whitenoise-rs/pull/775)는 그룹 필수 기능을 노출하고, [PR #772](https://github.com/marmot-protocol/whitenoise-rs/pull/772)는 그룹 미디어 작업을 세션 소유 `MediaOps`로 마이그레이션하며, [PR #773](https://github.com/marmot-protocol/whitenoise-rs/pull/773)은 session-ops 리팩터의 일부로 `SharedServices` 홀더를 추출합니다. 모바일 측에서는 [whitenoise PR #577](https://github.com/marmot-protocol/whitenoise/pull/577)이 Android 포그라운드 서비스에 대한 부팅 자동 재시작을 활성화하여 기기 재부팅 후 데몬이 다시 돌아오지 않는 경우를 수정합니다.

## 새로 추적 및 발견됨

### Nostrord: Kotlin Multiplatform과 WASM으로 구축된 NIP-29 클라이언트

[Nostrord](https://github.com/nostrord/nostrord)는 Discord 대체 사용 사례를 대상으로 하는 새로운 [NIP-29](/ko/topics/nip-29/) 그룹 채팅 클라이언트입니다. 그룹은 릴레이 강제 멤버십, 역할, 조정, 접근 제어와 함께 Nostr 릴레이에 상주하므로 그룹 상태는 선택한 NIP-29 릴레이에 의해 호스팅됩니다. 클라이언트 개발자는 해당 그룹에 대한 별도의 애플리케이션 데이터베이스를 제어하지 않습니다. 웹 앱은 [web.nostrord.com](https://web.nostrord.com)에서 실행되며 WebAssembly로 컴파일되는 Kotlin Multiplatform으로 구축되고, 네이티브 Android, iOS, 데스크톱 빌드가 개발 중입니다. Nostrord는 [OpenSats](https://opensats.org) grant 수령자이며 Flotilla, Chachi, 0xChat가 사용하는 동일한 NIP-29 릴레이와 상호 운용됩니다.

### Clave, APNs를 통해 iOS에 NIP-46 원격 서명 도입

[Clave](https://github.com/DocNR/clave)는 앱이 열려 있지 않을 때 Nostr 이벤트에 서명하는 베타 상태의 iOS 원격 signer입니다. private 키는 iPhone Keychain에 유지됩니다. 클라이언트가 [NIP-46](/ko/topics/nip-46/) 원격 서명 요청을 보내면 서버 측 프록시가 Apple Push Notification을 전달하여 최대 30초 동안 Notification Service Extension을 깨웁니다. 그 확장은 [NIP-44](/ko/topics/nip-44/) 암호화로 요청을 복호화하고 Keychain 키로 서명한 다음 응답을 게시합니다. 기기 토큰 등록은 토큰 하이재킹을 방지하기 위해 [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) HTTP Auth를 사용합니다. Clave는 `bunker://` 및 `nostrconnect://` 페어링, 클라이언트별 신뢰 수준, kind별 오버라이드를 지원하며 Nostur 및 noStrudel에서 테스트되었습니다.

### Treasures: Nostr 상의 분산 지오캐싱

[Treasures](https://gitlab.com/chad.curtis/treasures)는 캐시와 발견이 서명된 Nostr 이벤트인 지오캐싱 플랫폼입니다. 캐시 작성자는 GPS 좌표와 함께 kind `37516` 주소 지정 가능한 이벤트를 게시합니다. 발견자는 물리적 캐시에 부착된 QR 코드를 스캔하여 발견을 기록합니다. 코드는 작성자 pubkey, 캐시 `d` 태그, 물리적 방문의 증거로 사용되는 검증 private 키를 인코딩합니다. [NIP-57](/ko/topics/nip-57/) zap은 발견자에서 캐시 작성자로 흐를 수 있으며, 라이브 앱은 [treasures.to](https://treasures.to)에 있습니다.

### smesh v0.5.1: 자체 호스팅 Nostr 릴레이, 클라이언트, signer를 하나의 스택으로

[smesh](https://git.smesh.lol/smesh/smesh)는 mleku가 Go와 TinyGo에서 파생한 사용자 정의 언어인 Moxie로 작성된 자체 호스팅 Nostr 스택입니다. 이 스택은 HTTP, WebSocket, AUTH, 검색, Blossom 지원을 갖춘 네이티브 릴레이 바이너리, ES 모듈로 컴파일된 웹 클라이언트인 `sm3sh`, NIP-07 브라우저 서명과 NIP-04 및 NIP-44 암호화 지원을 갖춘 브라우저 signer 확장을 제공합니다. 최근 작업에는 v0.5.0의 MLS(RFC 9420) 그룹 메시징, 릴레이 동기화를 위한 negentropy 집합 조정, Web of Trust 그래프 엔진이 포함됩니다. 코드는 mleku의 자체 호스팅 forge인 `git.smesh.lol`에 있으며 그의 자체 `git-web` 도구로 구축되었습니다. 관련 [gitea-nostr-auth](https://git.smesh.lol/smesh/gitea-nostr-auth) 저장소는 Gitea용 OAuth2/OIDC 브리지입니다: 사용자는 NIP-07 브라우저 signer로 인증하고, 브리지는 NIP-65를 통해 릴레이를 발견하며, Gitea는 표준 OIDC identity claim을 받습니다.

### Surveil: Nostr 상의 Magic: The Gathering 덱 빌더

[Surveil](https://gitlab.com/chad.curtis/surveil)은 Magic: The Gathering 플레이어를 위한 Nostr 클라이언트로, 사용자가 카드를 검색하고, 덱을 만들고, Android에서 온디바이스 ML Kit OCR로 종이 카드를 스캔하고, 네트워크 전체에 덱을 공유할 수 있게 합니다. 덱은 kind `37381` 주소 지정 가능한 이벤트로 게시되며, 덱 이벤트 사양은 프로젝트의 `NIP.md`에 문서화되어 있습니다. 소셜 계층은 표준 Nostr 프리미티브로 구축됩니다: 각 덱으로 범위가 지정된 NIP-22(kind `1111`) 스레드 코멘트, NIP-25(kind `7`) 반응, 플레이어 홈용 [NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md)(kind `30078`) 프로필 데이터, kind `3` 팔로우 피드, 원본 덱으로 다시 연결되는 `a` 태그를 가진 fork. [v0.1.6](https://gitlab.com/chad.curtis/surveil/-/tags/v0.1.6)은 이번 주에 모바일 UI 다듬기, 라이프 카운터 개선, 개편된 About 페이지, 덱 히어로 배너의 릴레이 pill과 함께 출시되었습니다. 웹 앱은 정적 HTML이 제공되는 어디에서나 실행되고, Android 빌드는 [Zapstore](https://zapstore.dev)를 통해 배송되며, kind `37381` 이벤트는 Magic 덱으로 [Ditto](https://about.ditto.pub/reference)에서도 네이티브로 인덱싱됩니다. 저장소는 GitLab의 [chad.curtis/surveil](https://gitlab.com/chad.curtis/surveil)에 있습니다.

### 작은 추가 항목: Fundstr, Nod City, deploy-nsite-to-pages, null--nostr

[Fundstr](https://github.com/ritty65/Fundstr)는 일회성 및 반복 pledge를 위해 Cashu ecash를 사용하는 Nostr 상의 크리에이터 자금 조달 플랫폼으로, 크리에이터 tier 정의와 Nostr DM을 갖추고 있습니다. [Nod City](https://nod.city)는 리뷰가 서명된 Nostr 이벤트이고 리뷰어가 zap을 받을 수 있는 Bitcoin 서비스 리뷰 사이트입니다. 공개 소스 저장소는 발견되지 않았습니다. [deploy-nsite-to-pages](https://github.com/Origami74/deploy-nsite-to-pages)는 `nsyte download`를 사용하여 nsite를 GitHub Pages에 미러링하는 GitHub Action이며, 루트 kind `15128` 및 명명된 kind `35128` nsite를 지원합니다. 이번 주 NIP-34 데이터에서도 발견된 [null--nostr](https://github.com/tami1A84/null--nostr)는 최근 OpenSats 웨이브에서 Nurunuru로 다룬 클라이언트입니다. MLS 그룹 메시징, Amber, NIP-50 검색, NIP-70 보호된 게시물, ProofMode 배지, Zapstore 배포를 지원합니다.

FIPS는 Compass의 새 프로젝트가 아닙니다. [Newsletter #6](/ko/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking) 및 [Newsletter #10](/ko/newsletters/2026-03-25-newsletter/#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples)에서 다루었습니다. 데이터베이스는 이제 올바른 canonical 저장소인 [jmcorgan/fips](https://github.com/jmcorgan/fips)를 가리키며, 이번 주의 NIP-34 발견은 또한 `fips` 및 `awesome-fips`와 같은 관련 git-over-Nostr 미러를 표면화했습니다.

## 프로토콜 작업

### NIP 업데이트

[NIPs repository](https://github.com/nostr-protocol/nips)의 최근 제안 및 논의:

**이번 주 병합됨:**

- **NIP-34 git repositories: remove unused refs tag extension** ([PR #2325](https://github.com/nostr-protocol/nips/pull/2325)): 정의되었지만 사용되지 않은 [NIP-34](/ko/topics/nip-34/)의 `refs` 태그 확장을 제거합니다. 이 정리는 git-over-Nostr 도구에 대한 구현 모호성을 줄입니다.

- **NIP-34 git repositories: remove incorrect NIP-09 claim** ([PR #2326](https://github.com/nostr-protocol/nips/pull/2326)): [NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md) 삭제 이벤트가 저장소 상태를 재설정할 수 있다는 잘못된 주장을 제거합니다. NIP-09 삭제는 저장소 상태 머신이 아니라 클라이언트 측 이벤트 삭제 요청입니다. 이 수정은 NIP-34 구현자가 삭제 힌트를 권위 있는 저장소 재설정으로 취급하는 것을 방지합니다.

**열려 있고 구현 주도 작업:**

- **GitWorkshop kind `1111` 인라인 리뷰 코멘트**: 인라인 코드 리뷰 코멘트 kind는 GitWorkshop의 `NIP.md`에 문서화되어 있으며 현재 활발히 사용되고 있지만, 아직 공식 NIP로 제안되지 않았습니다. Verdict 이벤트(kind `7321`)와 `suggestion` 블록은 여전히 초안 상태이며 아직 출시되지 않았습니다. GitWorkshop 및 ngit의 구현 피드백에 따라 이 형태가 독립형 git-review NIP가 될지 아니면 NIP-34 위에 계층화된 애플리케이션 관례로 남을지가 결정됩니다.

- **Nostr mail core 및 Nostrmon**: 이번 주에 두 개의 새로운 커스텀 NIP 초안이 순환되었습니다. [Nostr mail core](https://njump.me/57d11cdf2f9ed73f7f39d6a7a6012ee3d642584ab11887f96a031f7d00fd9697)는 RFC 2822 이메일 콘텐츠에 대해 kind `1301`을 제안하며, 프라이빗 전달을 위해 NIP-59로 wrap되고 NIP-05로 해결된 브리지 pubkey를 통해 레거시 이메일에 브리지됩니다. [Nostrmon](https://njump.me/5e9a8cee19d464f5f0322518ac9ccaf2399c69da6572346b4fb12d36acb17a27)은 지역, 지도, 생물, NPC, 플레이어 저장, 아이템을 위한 주소 지정 가능한 이벤트 kind를 스케치합니다. 둘 다 병합된 NIP가 아니라 커스텀 초안으로 남아 있습니다.

- **NIP-67: EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)): 이 제안은 `EOSE`에 긍정적 완결성 마커를 추가하는 반복을 계속하여, 릴레이가 완결성 주장을 하지 않는 레거시 `EOSE` 사례와 "저장된 이벤트가 완전히 전달됨"을 구별할 수 있게 합니다.

## 여섯 번의 Nostr 4월

4월은 Nostr 개발 경로의 깨끗한 단면을 제공합니다: 2021년의 프로토콜 문서, 2022년의 초기 클라이언트 작업, 2023년의 Damus 이후 애플리케이션 웨이브, 2024년의 프라이빗 메시징 및 git-over-Nostr 작업, 2025년의 Blossom 및 릴레이 리스트 정리, 2026년의 채택 중심 클라이언트 grant.

### 2021년 4월: NIPs 저장소 이전의 프로토콜 문서

Fiatjaf는 2020년 11월 20일에 원본 Nostr 기사 ["Notes and Other Stuff Transmitted by Relays"](https://fiatjaf.com/nostr.html)를 게시했습니다. 그 첫 번째 텍스트는 이미 프로토콜을 정의하는 핵심 형태를 포함하고 있었습니다: 사용자는 키로 이벤트에 서명하고, 릴레이에 게시하며, 선택한 릴레이에서 읽습니다. [`nostr-protocol/nostr` 커밋 로그](https://github.com/nostr-protocol/nostr/commits?since=2021-04-01&until=2021-04-30)는 4월 1일에서 4월 30일 사이에 커밋이 없음을 보여줍니다. 활동은 양쪽에 자리잡고 있습니다: 2021년 3월 커밋은 초기 "nostwitter" 링크와 `kind` 필터를 추가했고, 2021년 5월은 NIP-02를 재활용하고 NIP 저자를 추가했습니다.

2021년 4월에는 공개 클라이언트 시장이 없었고, 눈에 보이는 릴레이 네트워크도 없었으며, NIPs 저장소도 없었습니다. 프로토콜은 여전히 작은 문서와 몇 가지 실험으로 존재했습니다. Nostr는 아직 소셜 네트워크나 개발 플랫폼이 되지 않았습니다. 첫 번째 지속적인 기여자 웨이브를 기다리는 릴레이/키/이벤트 모델이었습니다.

### 2022년 4월: NIP는 여전히 메인 저장소에 있었음

2022년 4월은 NIP가 메인 `nostr-protocol/nostr` 저장소에서 이동하기 전 마지막 달이었습니다. 분리가 아직 일어나지 않았기 때문에 전용 [`nostr-protocol/nips`](https://github.com/nostr-protocol/nips) 저장소는 4월 pull request 이력이 없습니다. 메인 저장소에서는 세 개의 4월 커밋이 들어왔습니다: 4월 8일 goswami1999의 ["Update readme to add nip12"](https://github.com/nostr-protocol/nostr/commit/bae286312a233b971bee5429adda7aff41747eb8), 4월 25일 jb55의 ["add kinds list"](https://github.com/nostr-protocol/nostr/commit/4b9e9d123273ba8a5c70d77df46922070c11c11d), 4월 28일 steliosrammos의 ["add js formatting to sample code"](https://github.com/nostr-protocol/nostr/commit/759997657f07e0344064228ffe5e93febe85d367).

클라이언트 작업도 형태를 갖추기 시작했습니다. 2022년 4월의 Damus 커밋은 초기 채팅방 동작, 프로필 처리, 앱 아이콘을 추가했고, nostr-tools는 초기 클라이언트 및 실험을 위한 JavaScript 라이브러리 경로가 되고 있었습니다. 프로토콜 측면에서는 NIP-12 제네릭 태그 쿼리가 태그 검색에 문서화된 자리를 제공했고, kinds 리스트는 Nostr를 레지스트리 모델로 이동시켰으며, 더 나은 JavaScript 예제는 클라이언트 및 라이브러리 작성자가 사양을 구현하기 더 쉽게 만들었습니다. 5월 1일에 fiatjaf는 NIP를 전용 저장소로 이동시켰습니다. 2022년 4월은 원래의 단일 저장소 시대의 마지막 달이었습니다.

### 2023년 4월: Damus 이후 애플리케이션 확장

2023년 4월은 2023년 1월 31일에 Damus가 iOS App Store에서 출시된 지 3개월 후, 그리고 Jack Dorsey가 Nostr 공개 키를 게시한 후에 왔습니다. 네트워크는 첫 번째 주요 공개 성장 웨이브를 막 흡수했습니다. Damus, Snort, Iris, Coracle, Amethyst와 같은 클라이언트가 활발했으며, 릴레이 운영자는 더 큰 소셜 그래프가 대역폭, 스팸, 검색, 조정 가정에 미치는 영향을 배우고 있었습니다.

2023년 4월에는 병합된 NIPs PR이 하나 있었습니다: 4월 17일에 병합된 [PR #456](https://github.com/nostr-protocol/nips/pull/456)은 NIP-21 URI 처리에 NIP-19 bech32 엔티티 링크를 추가했습니다. 주변 커밋은 프로토콜 작업 배후의 애플리케이션 압력을 보여줍니다. 2023년 4월은 [NIP-45 COUNT](https://github.com/nostr-protocol/nips/commit/8b39976e78f90fe766ad7149e250777cddacbb5e), 이벤트별 zap 마커, [NIP-15 marketplace](https://github.com/nostr-protocol/nips/commit/bf0a0da6a48b96467172414d8e41dc72b0ca379c), NIP-26 delete delegation 시맨틱, NIP-94 파일 메타데이터, NIP-47 wallet-connect 오류 처리, [NIP-30 커스텀 이모지](https://github.com/nostr-protocol/nips/commit/e91ce3409e1ce8267fc07a21784d2538621267c3) 작업을 보았습니다. 기여자 목록은 fiatjaf, staab, pablof7z, Semisol, CodyTseng, sethforprivacy, mikedilger, AsaiToshiya, alexgleason, martindsq, frbittencourt, arkin0x을 포함하도록 넓어졌습니다.

Damus, Snort, Iris, Coracle, Amethyst는 더 이상 사양을 둘러싼 데모가 아니었습니다. 그들은 온보딩, 피드, 스팸, zap, 미디어, 릴레이 선택을 다루는 프로덕션 클라이언트였습니다. 2023년 4월의 프로토콜 작업은 그러한 클라이언트가 만든 백로그처럼 읽힙니다: zap, 마켓플레이스, 파일 메타데이터, 카운팅, 이모지, identity 링크가 모두 사양을 단순한 노트와 팔로우 이상으로 밀어붙였습니다.

### 2024년 4월: 프라이빗 메시징, git-over-Nostr, 유지 관리자 지원

2024년 4월에는 두 개의 NIP PR 병합이 있었습니다. 4월 10일에 병합된 [PR #1167](https://github.com/nostr-protocol/nips/pull/1167)은 클라이언트와 signer가 요청된 및 승인된 작업에 대한 정확한 언어가 필요한 [NIP-46](/ko/topics/nip-46/) 원격 서명의 혼란스러운 용어를 수정했습니다. 4월 17일에 병합된 [PR #1108](https://github.com/nostr-protocol/nips/pull/1108)은 status 이벤트, 명확화, 선택적 유지 관리자, 저장소 식별자, 발견 가능성 태그로 [NIP-34](/ko/topics/nip-34/) git 저장소를 확장했습니다. 이 단계는 git-over-Nostr를 ngit와 나중의 GitWorkshop에 더 실용적으로 만들었습니다.

[NIP-17](https://github.com/nostr-protocol/nips/commit/df30012430c88d49fb5b124992b04d5c61b6338b)은 이전에 NIP-24였으며, 4월 24일에 프라이빗 DM과 소규모 그룹 채팅을 위한 sealed gift-wrapped 메시지로 도착했습니다. 클라이언트 및 라이브러리 작업이 함께 진행되었습니다: Amethyst, Primal, Gossip, nostr-tools, NDK, rust-nostr가 모두 같은 기간에 활발했습니다.

OpenSats는 또한 2024년 4월에 Nostr 개발자에 대한 장기 지원을 발표했습니다: 4월 9일 [PabloF7z](https://opensats.org/blog/pablofz7-receives-lts-grant), 4월 12일 [Stuart Bowman](https://opensats.org/blog/stuart-bowman-receives-lts-grant), 4월 15일 [hzrd149](https://opensats.org/blog/hzrd149-receives-lts-grant). 이러한 grant는 자금을 고립된 프로젝트 grant에서 릴레이, 라이브러리, 클라이언트 인프라의 지속적인 유지 관리로 이동시켰습니다.

### 2025년 4월: 밀도 있는 NIP 정리 및 Blossom 공식화

2025년 4월은 이 회고에서 가장 밀도 있는 프로토콜 달로, 16개의 병합된 NIPs PR이 있었습니다. 이 달은 NIP-73에 블록체인 트랜잭션 및 주소를 추가하는 [PR #1846](https://github.com/nostr-protocol/nips/pull/1846), 표준화된 태그 테이블에 NIP-C0 태그를 추가하는 [PR #1865](https://github.com/nostr-protocol/nips/pull/1865)로 시작했습니다. 계속해서 [PR #1801](https://github.com/nostr-protocol/nips/pull/1801) 및 [PR #1889](https://github.com/nostr-protocol/nips/pull/1889)는 kind `10002` 릴레이 리스트 재게시 가이드를 개선했고, [PR #1879](https://github.com/nostr-protocol/nips/pull/1879)는 [NIP-65](/ko/topics/nip-65/)를 축소하고 명확하게 했습니다.

[PR #1822](https://github.com/nostr-protocol/nips/pull/1822)는 Blossom 상호작용을 위한 NIP-B7을 추가하여, 1년 이상의 비공식 관행 이후 Nostr 클라이언트와 Blossom 서버에 canonical 조정 계층을 제공했습니다. [PR #1051](https://github.com/nostr-protocol/nips/pull/1051)은 위임 이벤트 서명 사양인 [NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md)을 폐지했습니다. NIP-26은 안전하게 구현하기 어려웠으며 NIP-46과 다른 signer 패턴이 성숙해지면서 덜 매력적으로 되었습니다.

이 달의 나머지는 정리와 애플리케이션 확장을 결합했습니다: [PR #1882](https://github.com/nostr-protocol/nips/pull/1882)는 [NIP-11](/ko/topics/nip-11/)에 개인 정보 보호 정책 및 서비스 약관 필드를 추가했고, [PR #1849](https://github.com/nostr-protocol/nips/pull/1849)는 NIP-B0 하의 kind `39701` 웹 북마크를 확장했으며, [PR #1891](https://github.com/nostr-protocol/nips/pull/1891)은 그 북마크 kind를 README에 추가했고, [PR #1895](https://github.com/nostr-protocol/nips/pull/1895)는 NIP-B0 표준화된 태그를 추가했습니다. OpenSats는 4월 16일에 [Eleventh Wave of Nostr Grants](https://opensats.org/blog/eleventh-wave-of-nostr-grants)를 발표하여 Swae, HAMSTR, Vertex, Nostr Double Ratchet, Nostr Game Engine을 지원했습니다. Primal, Coracle, noStrudel, nostr-tools, NDK, rust-nostr도 이 기간에 출시되고 있었으므로, 프로토콜 정리는 활발한 클라이언트 및 라이브러리 작업 옆에 자리잡았습니다.

### 2026년 4월: NIP-34 강화, 배지, 채택 중심 grant

이 이슈가 마무리되는 달인 2026년 4월에는 네 개의 병합된 NIPs PR이 있었습니다. 첫 번째는 4월 1일에 병합된 [PR #2276](https://github.com/nostr-protocol/nips/pull/2276)으로, [NIP-58](https://github.com/nostr-protocol/nips/blob/master/58.md) 프로필 배지를 kind `10008`로 변경하고 kind `30008` 배지 세트를 추가하여, 배지 할당 및 배지 컬렉션을 더 조합 가능하게 만들었습니다. 두 번째 git-over-Nostr 사용성 변경은 4월 10일에 병합된 [PR #2312](https://github.com/nostr-protocol/nips/pull/2312)에 도착하여 [NIP-34](/ko/topics/nip-34/)에 `nostr://` clone URL 시맨틱을 추가했습니다. 4월 25일 정리인 [PR #2325](https://github.com/nostr-protocol/nips/pull/2325) 및 [PR #2326](https://github.com/nostr-protocol/nips/pull/2326)은 사용되지 않고 잘못된 NIP-34 언어를 제거했습니다.

관련 커밋은 같은 표면을 다듬습니다. 4월 22일에 fiatjaf는 NIP-51에 Blossom 서버 리스트를 추가하고 Flotilla의 PUT 스타일 동작에 맞게 NIP-29 메타데이터 편집을 조정했습니다. 4월 26일에 그는 명확성을 위해 NIP-5A의 이름을 변경했습니다. 2026년 4월은 이미 사용 중인 프로토콜 표면을 구현하기 쉽고 잘못 읽기 어렵게 만드는 데 초점을 맞췄습니다.

OpenSats는 4월 8일에 [Sixteenth Wave of Nostr Grants](https://opensats.org/blog/sixteenth-wave-of-nostr-grants)를 발표하여 Amethyst Desktop, Nostr Mail, Nostrord, Nurunuru(null--nostr), HAMSTR 갱신을 지원했습니다: 데스크톱 클라이언트, 이메일과 유사한 메시징, 그룹 UX, 일본어 온보딩, 오프그리드 연결.

---

*Nostr Compass #20을 읽어주셔서 감사합니다. 팁, 수정 사항 또는 다루어야 할 새 프로젝트가 있으시면 [Nostr에서 DM을 보내주세요](https://nostr.com).*
