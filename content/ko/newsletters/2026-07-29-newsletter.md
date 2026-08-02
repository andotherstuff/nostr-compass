---
title: "Nostr Compass #33"
date: 2026-07-29
publishDate: 2026-07-29
translationOf: /en/newsletters/2026-07-29-newsletter.md
translationDate: 2026-08-02
draft: false
type: newsletters
description: "Amethyst 1.13.1은 1.13.0이 Nostr 앱을 도입한 뒤 인증된 그룹 및 Blossom 접근을 추가하고, Mosaico는 Nostr를 통해 코딩 에이전트 상태를 공유하며, Nostrology는 NIP-65 relay 리스트의 집중도를 지도화한다."
---

Nostr에 대한 주간 가이드, [Nostr Compass](https://github.com/andotherstuff/nostr-compass)에 다시 오신 것을 환영합니다.

**이번 주:** [Amethyst 1.13.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1)은 버전 1.13.0의 Nostr 앱 출시를 이어 NIP-29 호스트 relay 인증과 인증된 Blossom 다운로드 재시도를 추가했습니다. [Code Call](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.68)은 휴대전화에서 원격 코딩 세션을 계속 진행하게 하고, [GitWorkshop](https://github.com/DanConwayDev/gitworkshop)은 maintainer와 저장소 동기화를 조정하며, [Mosaico](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2)는 코딩 에이전트에 공유 Nostr 인식 레이어를 제공합니다. [Nostrology](https://dev.nostrolo.gy/relays)는 프로필이 발행한 relay 리스트에서 읽기와 쓰기 역할을 어떻게 나누는지 지도화합니다. [Mafrend](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0), [Hanami](https://github.com/Letdown2491/hanami-android/releases/tag/v0.1.0), [Cordn](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.2.1)의 Android 릴리스가 태그 릴리스를 이끌고, [FIPS는 OpenWrt 접근 레이어를 추가했으며](https://github.com/jmcorgan/fips/pull/126) [열린 PR은 FreeBSD 포트를 제안합니다](https://github.com/jmcorgan/fips/pull/129). 프로토콜 보도는 NIPs, BUDs, NAPs, Marmot, Gamma Markets, Concord, NWC를 다루며, [Nostr의 여섯 번의 7월](https://github.com/nostr-protocol/nips/commits/master/)은 초기 도메인 조회부터 relay 그룹 상태까지 7월의 변화를 추적합니다.
## 주요 소식

### Amethyst 1.13.1이 Nostr 앱 출시에 이어 인증된 그룹 및 Blossom 접근을 추가하다

Android 및 멀티플랫폼 Nostr 클라이언트용으로 7월 28일 출시된 [Amethyst 1.13.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0)은 격리된 키 없는 브라우저 프로세스 안에서 napplet과 NIP-5A nsite를 엽니다. 동의를 거치는 `window.nostr` bridge는 활성 계정을 통해 서명하고 선택한 capability를 사용할 수 있으며, 사이트별 및 계정별 권한 화면에서 사용자는 해당 허용을 검토하거나 취소할 수 있습니다. 즐겨찾는 앱은 계정 사이에 cookie, 로그인 상태, 허용을 공유하지 않고도 하단 bar에 고정할 수 있습니다.

같은 [1.13.0 릴리스](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0)는 Concord 커뮤니티, NIP-29 relay 그룹, Buzz 그룹 채팅, wiki 페이지, RSS 피드와 함께 Git 저장소 tree, issue, pull request를 추가합니다. 이 화면들을 통해 사용자는 같은 Nostr 신원 아래에서 코드, 커뮤니티, 발행, 소셜 보기를 오갈 수 있습니다.

[버전 1.13.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0)은 결제와 신원 기능도 넓혔습니다. Amethyst는 BOLT12 offer를 만들고 결제하며, 원격 서명자 계정을 자동으로 시작하고, Blossom fallback 서버를 추가하고, badge, 커뮤니티, relay 그룹을 위한 Web of Trust 제어를 확장할 수 있습니다. 7월 29일의 [1.13.1 후속 릴리스](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1)는 [CORD-02 해산 seal](https://github.com/vitorpamplona/amethyst/pull/3767), kind `9008` [그룹 및 채널 삭제](https://github.com/vitorpamplona/amethyst/pull/3779), [NIP-29 호스트 relay 인증](https://github.com/vitorpamplona/amethyst/pull/3788), 제한된 Blossom 다운로드를 위한 인증된 [BUD-01 재시도](https://github.com/vitorpamplona/amethyst/pull/3789)를 추가합니다.

### Code Call 0.2.68이 0.2.66의 따라잡기 기능에 이어 worker 폴더 브라우저를 추가하다

컴퓨터 측 코딩 세션을 위한 Android remote인 [Code Call 0.2.68](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.68)은 특수한 workspace 리스트를 worker 디렉터리를 root로 삼는 폴더 브라우저로 교체합니다. 사용자는 허용된 중첩 폴더에 들어가 OpenCode 세션용 폴더 하나를 선택하고 상위 폴더로 돌아갈 수 있으며, [버전 0.2.67](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.67)은 세션이 생성될 때 이 브라우저를 엽니다.

앞선 [0.2.66 릴리스](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.66)는 routing된 worker에게 휴대전화의 최신 메시지부터 간결한 따라잡기 요약을 요청할 수 있습니다. 같은 주의 다른 릴리스는 [여러 세션을 독립적으로 유지하고](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.51), [예상된 발신자](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.56)의 답변만 받으며, 백그라운드 전달을 위해 받은편지함을 [설정된 모든 worker relay](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.59)에 연결해 둡니다. 요청과 답변은 [NIP-17(비공개 직접 메시지)](/ko/topics/nip-17/) 안에서 이동하며, 로컬에서 암호화된 [Blossom](/ko/topics/blossom/) 첨부 파일은 [복호화 후에도 원래 파일 형식을 유지합니다](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.55).

### GitWorkshop이 maintainer를 조정하고 저장소 동기화를 독립적으로 유지하다

[GitWorkshop의 7월 27일 서명 릴리스](https://primal.net/e/869e01f9a74d98f468a66f3b83865d198a82cc718c1db36324398b1b88a17c60)는 [NIP-55(Android 서명자 애플리케이션)](/ko/topics/nip-55/)을 통한 Android 로그인을 브라우저 기반 [NIP-34(`git` 관련)](/ko/topics/nip-34/) forge에 추가합니다. [소스 저장소](https://github.com/DanConwayDev/gitworkshop)는 이제 lead maintainer를 재귀적으로 조정하고, 각 maintainer의 relay hint를 보존하며, 저장소 동기화를 초대 수락과 독립적으로 유지합니다. 저장소 간 work item 참조는 여러 저장소의 관련 작업을 연결하고, GRASP는 전송을 초대 전달과 결합하지 않은 채 저장소 데이터를 선택한 Git endpoint로 복사합니다. 개발자가 서명한 [3.1.1 업데이트](https://primal.net/e/01d0939e9960cb82f1f7aba6f1900af2c61ce384e38352221bf9d5878116ae2d)는 Android 서명자 intent 전달, 재귀적 maintainer 해석, 경로를 보존하는 저장소 링크를 수정합니다.

### Mosaico 0.1.2가 코딩 에이전트의 Nostr 상태 공유를 지원하다

[Mosaico 0.1.2](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2)는 Claude Code, Codex, Goose, Hermes, OpenCode, Grok의 코딩 에이전트 세션이 [NIP-29(Relay 기반 그룹)](/ko/topics/nip-29/)을 통해 짧은 상태 업데이트를 발행할 수 있게 합니다. 세션은 transcript나 context를 공유하지 않고도 여러 호스트에서 관련된 활성 작업을 찾을 수 있습니다.

이름이 있는 Codex 프로필 탐색과 Goose의 Top Of Mind 보기는 양쪽 harness 안에서 그 공유 상태를 드러냅니다([PR #618](https://github.com/pablof7z/mosaico/pull/618), [PR #619](https://github.com/pablof7z/mosaico/pull/619)). 이 릴리스는 호스팅된 에이전트가 공개 인식 레이어에 참여하는 기능을 복구하며, 이제 설정에는 명시적인 relay 선택이 필요합니다([PR #626](https://github.com/pablof7z/mosaico/pull/626), [PR #629](https://github.com/pablof7z/mosaico/pull/629)). Mosaico는 인식 레이어이며 에이전트 호스트, orchestrator, transcript 병합기가 아닙니다.

### Nostrology가 발행된 NIP-65 이벤트에서 relay 리스트 집중도를 지도화하다

[Nostrology의 relay 관측소](https://dev.nostrolo.gy/relays)는 각 프로필의 최신 [NIP-65(Relay 리스트 메타데이터)](/ko/topics/nip-65/) kind `10002` 이벤트에서 dataset을 만들며 [발행된 명세](https://github.com/nostr-protocol/nips/blob/master/65.md)를 따릅니다. 읽기, 쓰기, 결합 relay 역할을 구분하고, 각 프로필이 나열한 relay 수를 chart로 나타내며, 기반 count를 정렬 가능한 table로 공개합니다. 7월 29일 발행 검토 시점에 이 페이지에는 서로 다른 relay URL 값 34,430개가 있었고, relay를 정확히 하나 나열한 프로필은 520,468개로 묶였으며, 세 개를 나열한 프로필은 150,657개, 네 개는 60,710개였습니다.

같은 [Nostrology snapshot](https://dev.nostrolo.gy/relays)은 `relay.momostr.pink`에 298,859개 프로필, `relay.damus.io`에 287,181개, `nos.lol`에 279,468개, `relay.primal.net`에 225,336개가 겹쳐 집중된 모습을 보여 줍니다. 이 수치는 가용성이 아니라 발행된 relay 리스트 항목을 측정합니다. raw table에는 잘못된 URL과 로컬 주소가 포함될 수 있으며, [NIP-65 명세](https://github.com/nostr-protocol/nips/blob/master/65.md)는 routing 메타데이터를 정의할 뿐 relay 상태를 검사하지 않습니다. 이 관측소는 나열된 relay를 가동 중인 relay로 취급하지 않으면서 채택과 데이터 품질 문제를 드러냅니다.

## 태그 릴리스

### Kairos 0.1.1이 알림과 로컬 Astraea 지시를 추가하다

[Kairos 0.1.1](https://primal.net/e/ffb054280008dc3ba488d5d3a2cbfec6c4123489a874683545a29a466682fd90)은 마감일 알림, Astraea에 보내는 명시적 로컬 지시, 더 엄격한 relay 및 URL 처리를 추가합니다. [0.1.0 서명 릴리스](https://primal.net/e/6e02430844abdabf5421bbf5745a09ef2870e4ade93f56627ee14ba8db58a00a)는 [오프라인 우선 작업 관리자](https://github.com/Lwb89dev/kairos)를 도입했으며, 선택적 동기화 레이어는 [NIP-44(암호화된 Payload)](/ko/topics/nip-44/)로 암호화한 record를 사용자가 선택한 relay에 기록합니다. Kairos는 결정론적 작업 coordinate와 암호화된 tombstone을 [NIP-09(이벤트 삭제 요청)](/ko/topics/nip-09/) 삭제 요청과 함께 사용하며, 로컬 전용 작업은 디바이스를 떠나지 않습니다.

### Bray 2.3.0이 CLI에 범용 gift wrapping과 로컬 Blossom 테스트 표면을 제공하다

Nostr SDK이자 command-line toolkit인 [Bray 2.3.0](https://github.com/forgesworn/bray/releases/tag/v2.3.0)은 [NIP-59(Gift Wrap)](/ko/topics/nip-59/)을 통해 임의의 이벤트를 gift-wrap하고 unwrap할 수 있으며, bunker가 키를 보관할 때 서명은 [NIP-46(Nostr Connect)](/ko/topics/nip-46/)을 통해 routing됩니다. [PR #75](https://github.com/forgesworn/bray/pull/75)는 함께 제공되는 테스트 relay에 [NIP-42(Relay에 대한 클라이언트 인증)](/ko/topics/nip-42/) challenge를 추가하고 남은 Blossom 클라이언트 명령을 공개합니다. [PR #77](https://github.com/forgesworn/bray/pull/77)은 서명된 인가가 각 upload 또는 deletion을 하나의 blob에 결합하는 in-memory BUD-01/02 서버를 추가하고, [PR #76](https://github.com/forgesworn/bray/pull/76)은 이름이 있는 event kind, 축약 tag, 호출자가 이미 보유한 이벤트의 다운로드를 피하는 [NIP-77](/ko/topics/nip-77/) ID 조정 flag를 추가합니다.

### Buzz Desktop 0.5.0이 초대, 검색, relay 신원 업데이트를 강화하다

지난주 Armada 및 Buzz workspace 보도에 이어, [Buzz Desktop 0.5.0](https://github.com/block/buzz/releases/tag/v0.5.0)은 사용 횟수가 제한된 초대 링크([PR #3141](https://github.com/block/buzz/pull/3141))와 작성자, 채널, 시간 범위 검색 filter([PR #2871](https://github.com/block/buzz/pull/2871))를 추가합니다. [PR #2862](https://github.com/block/buzz/pull/2862)는 데스크톱 앱의 네이티브 network 레이어를 통해 가입 정책을 가져오며, [PR #2607](https://github.com/block/buzz/pull/2607)은 persona 이름 변경이 relay에 도달한 뒤 에이전트의 신원 record를 다시 발행합니다. 이 릴리스는 [NIP-44 원격 서비스 거부 권고](https://github.com/block/buzz/pull/3135)를 반영해 Nostr dependency도 업데이트하고, 로컬 저장소 복구, thread 위치, relay 재연결, Linux 및 Windows runtime 경로를 수정합니다.

### Shosho 1.0.0이 라이브 스트리밍 marketplace를 확장하다

[Shosho 1.0.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.0.0)은 설정 가능한 relay 검색으로 사용자가 찾을 수 있는 creator, 라이브 세션, clip, product를 중심으로 라이브 스트리밍 marketplace를 재설계합니다. 통합 알림 피드는 이제 mention, reaction, repost, zap을 모으고 피드를 떠나지 않은 채 답글을 지원합니다. 시청자는 라이브 스트림이나 replay에서 clip을 발행할 수 있으며, 이 릴리스는 thread 채팅, clip 답글, 프로필 loading, network 사용도 개선합니다.

### Mafrend v1.0이 Android의 장소 기반 Nostr 채팅을 미리 선보이다

[Mafrend v1.0](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0)은 계획 중인 장소 기반 Nostr 채팅 앱의 첫 공개 Android alpha입니다. [프로젝트 페이지](https://mafrend.com)는 기능이 아직 활발히 개발 중이라고 표시하며, 각 지도 위치를 한 장소를 둘러싼 대화용 전용 채팅방으로 설명합니다. 공개 릴리스 저장소에는 설치 가능한 Zapstore package가 있고, main 앱은 비공개로 남아 있습니다.

### Hanami 0.1.0이 Blossom 서버에 서명자가 중재하는 Android 경로를 제공하다

[Hanami 0.1.0](https://github.com/Letdown2491/hanami-android/releases/tag/v0.1.0)은 [Blossom](/ko/topics/blossom/) 서버용 Android companion으로, 사용자가 휴대전화에서 로그인하고 upload 및 download할 수 있게 합니다. 앱은 승인을 중재하는 서명에 [NIP-55(Android 서명자 애플리케이션)](/ko/topics/nip-55/)을 사용하고, 서버 세션에는 네이티브 [NIP-98(HTTP 인증)](/ko/topics/nip-98/) handshake를 사용합니다. Hanami는 web shell과 signing bridge를 선택한 서버 origin에 고정해 자격 증명을 서명자에 남겨 두고, 서버의 기존 web interface가 애플리케이션 경험을 제공합니다. 첫 공개 릴리스에는 Android 8 이상, 접근 가능한 Hanami 서버, 호환 서명자 앱이 필요합니다.

### Cordn이 Android에서 Nostr 신원 기반 그룹 채팅을 출시하다

비공개 그룹 메시징 클라이언트 Cordn은 이제 Android 사용자에게 Nostr 신원 onboarding, [NIP-05(Nostr 키를 DNS 기반 인터넷 식별자에 매핑)](/ko/topics/nip-05/)을 통한 프로필 링크, Cordn 목적지를 앱에서 여는 검증된 링크를 제공합니다. [7월 24일 발행된 0.2.1 릴리스](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.2.1)는 기존 web client와 함께 이 네이티브 계열을 도입합니다. 메시지는 그룹 암호화 프로토콜 [MLS](/ko/topics/mls/)와 coordinator 보조 전달을 사용하므로, 그룹은 이메일 주소나 전화번호 없이 순서가 보존된 암호화 대화를 유지합니다.

### Nostur 1.30.1이 1.30.0의 공유 기능 확장에 이어 thread와 중복 게시물을 수정하다

iPhone, iPad, Mac용 Nostr 클라이언트 [Nostur 1.30.1](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.1)은 새 layout을 방해하던 펼치기 및 접기 오류 없이 중첩된 답글 thread를 탐색할 수 있게 합니다. media upload callback이 반복될 때를 포함해 같은 draft가 두 번 발행되는 문제도 막습니다. 이 릴리스는 사라지는 직접 메시지와 media를 Nostr로 보내는 share sheet 경로를 추가한 [1.30.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.0)에 이어져, 앱이 새로운 메시징 및 발행 경로와 일상적인 thread 및 게시 흐름의 수정 사항을 함께 제공합니다.

### Formstr Drive 0.0.2가 Nostr 파일 메타데이터와 Blossom blob을 결합하다

Nostr 네이티브 파일 관리자인 [Formstr Drive 0.0.2](https://github.com/formstr-hq/formstr-drive/releases/tag/v0.0.2)는 앱 내 preview와 office 문서를 Nostr Docs에서 여는 선택지를 제공합니다. 내부적으로는 대용량 파일을 조각낸 [Blossom](/ko/topics/blossom/) blob으로 저장하고 사용자가 파일을 제거하면 원격 blob을 삭제합니다. 로컬 relay는 앱의 Nostr 메타데이터를 가까이 보관하고 Blossom은 파일 데이터를 보관하여, 파일 정리와 큰 byte 자체를 분리합니다.

### NoorNote 1.3.1

웹, 데스크톱, Android용 Nostr 클라이언트 [NoorNote 1.3.1](https://github.com/77elements/noornote/releases/tag/v1.3.1)은 사라지는 메시지 timer를 추가하고 새로 만든 계정에 작동하는 기본 DM relay를 설정합니다. 표지 이미지가 없는 글로벌 article을 걸러 내고 repost 알림을 article reader로 보냅니다. 앞선 [1.3.0 릴리스](https://github.com/77elements/noornote/releases/tag/v1.3.0)는 [NIP-53(라이브 활동)](/ko/topics/nip-53/) card, [NIP-68(사진 우선 피드)](/ko/topics/nip-68/) person tag, [NIP-78(애플리케이션 데이터)](/ko/topics/nip-78/) soft mute, note의 relay-seen 상태를 추가했습니다.

### algia 0.0.133

Nostr용 Go command-line 클라이언트 [algia 0.0.133](https://github.com/mattn/algia/releases/tag/v0.0.133)은 [0.0.132](https://github.com/mattn/algia/releases/tag/v0.0.132)에 이어지며, 앞선 릴리스는 [NIP-29(Relay 기반 그룹)](/ko/topics/nip-29/) listing, timeline, posting, reaction, deletion, join 및 leave 흐름을 추가했습니다. 같은 릴리스는 인증이 필요하도록 설정된 relay에 [NIP-42(Relay에 대한 클라이언트 인증)](/ko/topics/nip-42/) 사전 인증도 추가했습니다. 이어 버전 0.0.133은 일반, 채널, 그룹 posting 명령에 로컬 이미지 upload를 추가하고, 생성된 URL과 [NIP-92(미디어 첨부)](/ko/topics/nip-92/) tag를 각 이벤트에 붙입니다. 이미지 전용 게시물도 작동하며, 그룹 게시물은 기본적으로 그룹의 relay media store를 대상으로 하고 다른 게시물은 설정된 file server를 사용합니다.

### swift-nostr 0.7.0

Apple 플랫폼의 Swift 애플리케이션용 Nostr 라이브러리 [swift-nostr 0.7.0](https://github.com/yysskk/swift-nostr/releases/tag/0.7.0)은 하나의 [NIP-46 원격 서명자](/ko/topics/nip-46/)가 signing abstraction을 통해 모든 클라이언트 기능을 구동할 수 있게 합니다. 이 릴리스는 그룹 가입, posting, moderation 흐름을 포함한 [NIP-98(HTTP 인증)](/ko/topics/nip-98/) 및 [NIP-29(Relay 기반 그룹)](/ko/topics/nip-29/) 지원을 추가합니다. 또한 공식 vector에 따라 [NIP-44(버전 관리형 암호화 페이로드)](/ko/topics/nip-44/) padding을 검증해, 비표준 padding에 대해 유효한 MAC을 담은 payload를 거부합니다.

### lawallet-nwc 2.0.0

[LaWallet NWC 2.0.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.0.0)은 Nostr 연결 지갑이자 [NIP-47(Nostr Wallet Connect)](/ko/topics/nip-47/) 서비스로, WebAuthn PRF 확장으로 브라우저에서 Nostr 서명 키를 파생하는 passkey 로그인을 추가합니다. 서버는 그 secret을 받지 않으며 같은 passkey로 동기화된 다른 디바이스에서 같은 키를 복구할 수 있습니다. 이제 계정은 여러 Nostr pubkey를 연결하고 병합할 수 있고, 선택적 listener service는 wallet-connect 이벤트를 relay하고 endpoint에 접근할 수 없을 때 webhook 전달을 재시도합니다.

### MDK 0.9.10

[MDK 0.9.10](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.10)은 [Marmot 프로토콜](/ko/topics/marmot/)의 Rust 구현으로, transport가 비활성 상태인 동안 pending send를 유지하고, inbound 전달이 lag, panic, closure 이후 복구되도록 [relay 알림 forwarding을 감독합니다](https://github.com/marmot-protocol/mdk/pull/1157). [PR #1159](https://github.com/marmot-protocol/mdk/pull/1159)는 내구성 있고 페이지를 나눈 대화 기록과 로컬 에이전트용 전체 답글 context를 추가하며, [PR #1167](https://github.com/marmot-protocol/mdk/pull/1167)은 대체 이벤트를 생성하는 대신 현재 서명된 KeyPackage 이벤트를 다시 발행합니다. 이 릴리스는 수동 채팅 순서도 보존하고, 최종 그룹 해산을 지원하며, Web of Trust 순위 검색, relay 정책 API, 언어 binding을 확장합니다.

### pakstr 0.3.1

[pakstr 0.3.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.3.1)은 웹 팀이 앱 shell을 다시 build하지 않고도 Android용 Nostr 클라이언트를 packaging할 때 runtime 설정과 API proxy를 제공할 수 있게 합니다. [같은 날의 릴리스 계열](https://git.nostrdev.com/stuff/pakstr/releases)은 0.3.x runtime 설정 작업에 앞서 Amber 서명자 bridge, [NIP-44(암호화된 Payload)](/ko/topics/nip-44/) 암호화 및 복호화, 수정된 Android permission injection을 추가했습니다. scaffold는 bundle된 web asset을 로컬에 유지하면서 배포별 설정을 runtime에 받고, proxy는 감싸진 앱에 일반 relay 연결과 함께 API 요청용으로 제어된 경로를 제공합니다.

### Ditto 2.34.2

사용자 정의 가능한 Nostr 소셜 클라이언트 [Ditto 2.34.2](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.34.2)는 custom emoji, 만료, 선택적 link preview를 포함해 사용자 상태를 feed, detail page, quote embed의 card로 렌더링합니다. 댓글이 있는 zap은 이제 참조한 게시물 아래에 답글로 나타납니다. 이 릴리스는 [2.34.1의 선택적 프로필 globe button](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.34.1)도 [NIP-5A(웹사이트 manifest)](/ko/topics/nip-5a/) root site를 발행한 소유자를 위해 유지하고, homepage navigation, live stream 검색, 외부 링크 처리, 깨진 custom emoji를 수정합니다.

### Earthly 0.0.9

Nostr 위에 구축된 협업 지도 편집기 [Earthly 0.0.9](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.0.9)은 이제 지도 entity drawer가 닫히거나 다시 열리거나 새로 고침될 때도 like를 계속 표시합니다. [NIP-57(Lightning zap)](/ko/topics/nip-57/) 흐름은 유효한 zap-request JSON을 전송하므로, Lightning 제공자는 로컬 개발 중에도 공개적으로 접근 가능한 relay에 검증된 receipt를 발행할 수 있습니다. 생성된 invoice는 entity surface가 바뀌어도 표시되며, 앱은 검증된 receipt가 도착한 뒤 확인을 보여 줍니다.

## 개발 중

### Keep이 kind 범위 NIP-44 v3 서명을 추가하고 승인 정책을 강화하다

Keep은 [NIP-44(암호화된 Payload)](/ko/topics/nip-44/) v3 암호화 및 복호화 요청을 두 [NIP-55(Android 서명자 애플리케이션)](/ko/topics/nip-55/) transport와 [NIP-46(Nostr Connect)](/ko/topics/nip-46/) bunker 모두에 전달하는 Android 서명자 변경 다섯 건을 병합했습니다. [PR #451](https://github.com/privkeyio/keep-android/pull/451), [#452](https://github.com/privkeyio/keep-android/pull/452), [#453](https://github.com/privkeyio/keep-android/pull/453)은 v3 grant를 v2와 분리하고, event kind로 범위를 제한하며, 누락되거나 유효하지 않은 kind를 거부하고, 알림에서 연 승인 요청을 보존합니다. [PR #454](https://github.com/privkeyio/keep-android/pull/454)와 [#455](https://github.com/privkeyio/keep-android/pull/455)는 Basic signing 정책을 Auto로 취급하는 것을 중단하고 전역 선택을 core 소유 암호화 store로 옮깁니다. Keep maintainer들은 최신 Android 태그 릴리스 뒤에 다섯 변경을 모두 병합했습니다.

### Routstrd가 인증되지 않은 노출 뒤에 기본 network bind를 변경하다

Routstrd [PR #56](https://github.com/Routstr/routstrd/pull/56)은 로컬 Nostr inference router의 기본 bind 주소를 모든 network interface에서 `127.0.0.1`로 바꿉니다. 이전 기본값은 인증되지 않은 wallet balance, history, access, send, refund, API key, provider, client, usage, daemon stop endpoint를 해당 port에 접근할 수 있는 모든 host에 노출했습니다. 운영자는 여전히 로컬이 아닌 bind를 명시적으로 설정할 수 있지만, 병합된 변경은 신규 배포를 기본적으로 로컬 전용으로 만들며 아직 태그 릴리스에는 포함되지 않았습니다.

### Imwald Android가 오프라인 발행 상태를 명확히 하다

Android Nostr 클라이언트 Imwald Android는 이제 설정된 모든 target이 로컬일 때만 로컬 relay의 acknowledgement를 완료된 발행으로 취급합니다. [오프라인 발행 및 outbox 수정](https://git.imwald.eu/silberengel/imwald-android/commit/f4de9f61df35110c77d2e5f99d764c0df176962b)은 로컬 relay가 이벤트를 수락했지만 설정된 원격 relay가 아직 수락하지 않았을 때 원격 전달을 pending 상태로 유지하므로, 발행 report가 디바이스 로컬 저장소와 relay 전달을 구분합니다.

### FIPS가 OpenWrt 접근 레이어를 추가하고 FreeBSD 포트는 계속 검토 중이다

Nostr 네이티브 Free Internetworking Peering System은 이제 [병합된 PR #126](https://github.com/jmcorgan/fips/pull/126)을 통해 OpenWrt router가 개방형 `!FIPS` 접근 network를 노출할 수 있게 합니다. 병행하는 아직 열린 [FreeBSD PR #129](https://github.com/jmcorgan/fips/pull/129)는 daemon, TUN data path, `.fips` 이름 해석, service management, native package build의 포팅을 제안합니다. OpenWrt 병합은 현재 접근 범위를 넓히고, FreeBSD 작업은 병합될 경우 이를 또 다른 범용 운영체제로 확장할 것입니다.

7월 26일의 [FIPS 프로젝트 업데이트](https://primal.net/e/d0afe733f75e909341ab7f39834883968df097472238a474df3a3346c5d38f51)는 공개 UDP overlay에 300개 넘는 node가 있고 더 넓은 mesh는 2,000개 node에 근접한다고 보고했습니다. [FIPS 저장소](https://github.com/jmcorgan/fips)는 같은 주에 동시 network 테스트, rekey 연속성, hop limit 동작, firewall 검사, NAT lab 격리를 강화했습니다. 저장소 작업은 network가 성장하는 동안 운영자가 이러한 동작을 재현 가능하게 검사할 수 있게 합니다.

### Zap Cooking이 게시물을 예약하고 scanner 요청을 결합하다

Nostr 레시피 공유 및 식사 계획 앱 Zap Cooking은 이제 예약 게시물을 암호화 저장소에 보관하고 주기적 relay sweep을 통해 예정 시각에 발행할 수 있습니다([PR #566](https://github.com/zapcooking/frontend/pull/566), [PR #569](https://github.com/zapcooking/frontend/pull/569)). 따라서 사용자는 서명되지 않은 게시물 content를 scheduler database에 노출하지 않고 예약 발행을 사용할 수 있습니다.

냉장고 scanner는 이제 [NIP-98](/ko/topics/nip-98/) HTTP 인증으로 정확한 요청 body를 인증하므로, membership 검사는 body에 제공된 pubkey 대신 scan 요청에 서명한 키를 기준으로 합니다([PR #599](https://github.com/zapcooking/frontend/pull/599)).

### Citrine이 Android 디바이스를 관리 가능한 relay로 바꾸다

Android에서 호스팅되는 Nostr relay Citrine은 이제 저장한 이벤트를 외부 relay로 전송할 수 있어, 운영자가 로컬 기록을 rebroadcast할 방법을 제공합니다([PR #179](https://github.com/greenart7c3/Citrine/pull/179)). 또한 호환 클라이언트가 relay를 관리할 수 있도록 [NIP-86(Relay 관리 API)](/ko/topics/nip-86/) 명령을 추가합니다([PR #150](https://github.com/greenart7c3/Citrine/pull/150)).

그룹 운영자는 [NIP-29](/ko/topics/nip-29/) relay 기반 그룹을 [PR #178](https://github.com/greenart7c3/Citrine/pull/178)에서 Amber 서명을 통해 관리할 수 있으며, [PR #174](https://github.com/greenart7c3/Citrine/pull/174)는 재시작을 거쳐도 Tor 기반 relay 설정과 lifecycle 상태를 일치시킵니다.

### Wired가 브라우저에서 완전한 대화를 복구하다

브라우저 기반 Nostr 클라이언트 Wired는 이제 고정된 폭이나 결과 limit에서 멈추지 않고 feed root, 답글, 참조 이벤트를 끝까지 따라갑니다([PR #148](https://github.com/smolgrrr/Wired/pull/148), [PR #147](https://github.com/smolgrrr/Wired/pull/147), [PR #146](https://github.com/smolgrrr/Wired/pull/146)). 따라서 사용자는 관련 이벤트가 자신의 relay에서 제공될 때 더 깊은 thread와 feed context를 복구할 수 있습니다.

브라우저는 참조 이벤트의 relay hint도 보존하고 아직 누락된 context에만 사용하여, 설정된 relay가 보유하지 않은 대화를 복원합니다([PR #145](https://github.com/smolgrrr/Wired/pull/145), [PR #144](https://github.com/smolgrrr/Wired/pull/144)). 불완전한 검색은 완료된 snapshot과 구분되므로, 부분 응답이 이전에 cache된 보기를 덮어쓰지 않습니다.

## 프로토콜 및 명세 작업

### NIPs: NIP-34 호스팅 경계, 그룹 이전, 세 개의 진행 중인 초안

이번 주 명세 변경 두 건이 병합되었습니다. [NIP-34 commit 6d2979b](https://github.com/nostr-protocol/nips/commit/6d2979b3f503a8539c983efbcdcf901bbcf9ed23)은 `kind:1618` pull request 설명에서 GRASP 호스팅 지침을 제거해 호스팅과 fallback 동작을 event contract 밖에 둡니다. [NIP-29 commit db5fe3d](https://github.com/nostr-protocol/nips/commit/db5fe3de8c5d1443b634c9bbf66ecb004f337057)은 relay 그룹 메타데이터가 다른 relay로 이전하는 방식과 클라이언트가 유효한 이전을 독립적으로 계속되는 fork와 구분하는 방식을 정의합니다.

[PR #2424](https://github.com/nostr-protocol/nips/pull/2424)는 상호적인 `kind:10045` key set 선언을 제안합니다. 상호성 요건은 한 신원이 다른 키를 일방적으로 연결하는 것을 막게 됩니다. [PR #2421](https://github.com/nostr-protocol/nips/pull/2421)은 수신자가 운영하는 receipt server에 의존하지 않고도 클라이언트가 target, amount, offer, 정산된 payment를 기준으로 검증할 수 있는 BOLT12 zap intent와 payer proof를 제안합니다.

[PR #2425](https://github.com/nostr-protocol/nips/pull/2425)는 NIP-B0 bookmark가 web URL과 함께 `nostr:` 같은 비 HTTP scheme을 유지할 수 있도록 제안합니다. 이 변경이 채택되면 이미 web address를 담는 같은 비공개 또는 공개 bookmark 리스트 안에 네이티브 Nostr 식별자, payment request, 다른 application scheme이 온전히 보존됩니다.

### Mill이 cloud 계정 키 backup 초안을 구현하다

Mill은 Google OIDC 계정 식별자와 고엔트로피 passphrase를 결합해 일회용 backup 키를 파생하는 구현을 [발표했습니다](https://primal.net/e/6362d9b00662fa64200530f8a29ae547521bac0a1e3c9379ef9086eac7d2030b). 이 [cloud 계정 키 backup 초안](https://github.com/0ceanSlim/nostr-mill/blob/main/docs/nip-cloud-key-backup.md)의 [참조 구현](https://github.com/0ceanSlim/nostr-mill/blob/main/src/nipbackup.js)은 사용자의 실제 키를 [NIP-49(비공개 키 암호화)](/ko/topics/nip-49/) `ncryptsec`로 암호화한 뒤, 설정된 relay의 잠정적 매개변수화 교체 가능 kind `30049` 이벤트에 저장합니다. 프로젝트는 [backup 흐름을 main에 병합했지만](https://github.com/0ceanSlim/nostr-mill/commit/eeb4b9114d02114b703a6823ad36ca8063b224da), v1.0.0 이후 릴리스에는 아직 포함되지 않았고 운영자가 전용 `backupRelays`를 제공하지 않으면 backup 흐름도 비활성 상태입니다. 버전이 지정된 relay set은 잠정적이며, 초안은 발행된 ciphertext가 오프라인 passphrase 추측에 계속 노출된다고 경고합니다. 독자는 이 설계를 고엔트로피 passphrase에 의존하는 구현된 실험으로 취급해야 합니다.

### BUDs: Blossom 서버가 알 수 없는 upload를 byte로 식별할 수 있다

[BUD-02 PR #110](https://github.com/hzrd149/blossom/pull/110)은 uploader가 `Content-Type`을 생략하거나 `application/octet-stream`을 보낼 때 서버 측 MIME 탐지를 권장하자는 제안입니다. Blossom 서버는 유지 관리되는 file type library로 첫 byte를 검사하고, 클라이언트가 제공한 구체적인 type은 보존하며, 탐지에 실패하면 일반 binary type으로 fallback합니다. 이 방식은 모든 upload에 byte sniffing을 의무화하지 않으면서 이미지, audio, video, 에이전트가 만든 파일을 렌더링 가능한 상태로 유지합니다.

### NAPs: 규약이 번호가 붙은 track을 대체하며 capture 및 filesystem contract가 발전하다

[PR #87](https://github.com/napplet/naps/pull/87)은 번호가 붙은 cross-napplet protocol track을 제거하고 runtime capability를 이름이 있는 contract 아래에 유지하며, application message는 `napplet:<archetype>/<intent>` convention URI로 수렴시킵니다. 병합된 [topic 신원 변경](https://github.com/napplet/naps/pull/89)은 안정적이고 query가 없는 convention path를 메시지별 payload data와 분리하고, [PR #90](https://github.com/napplet/naps/pull/90)은 그 전치 규칙을 discovery 및 handler 메타데이터에 적용합니다.

두 NAP 초안은 신뢰된 shell 경계를 확장합니다. [NAP-CAPTURE PR #94](https://github.com/napplet/naps/pull/94)는 microphone 동의, 플랫폼 permission, limit, retention, teardown을 runtime에 유지하면서 범위가 제한된 media artifact를 sandbox된 napplet에 반환합니다. [NAP-FS PR #88](https://github.com/napplet/naps/pull/88)은 이에 대응하는 virtual filesystem 제안으로, 제한 없는 host path 대신 정책에 결합된 handle을 사용합니다.

### Marmot: 명세가 최종 그룹 상태를 정의하다

[Marmot PR #409](https://github.com/marmot-protocol/marmot/pull/409)는 MLS 자체에 그룹 삭제 연산이 없으므로 인증되고 되돌릴 수 없는 `Disbanded` 상태를 추가합니다. 권한 있는 admin commit은 그룹을 `Active`에서 벗어나게 하고, 과거 branch, message, Welcome이 그룹을 되살리지 못하게 하며, 기존 그룹이 해산할 수 있기 전에 명시적 호환 경로를 제공합니다. 앞선 [명세 issue 정리](https://github.com/marmot-protocol/marmot/pull/408)는 그룹 상태 권한, convergence, key package, acknowledgement, media rule, registry 문구, 추적된 명세 issue 200개도 조정했습니다.

### Gamma Markets: 공개 명세 변경이 반영되지 않았다

[Gamma Markets 명세 저장소](https://github.com/GammaMarkets/market-spec)는 7월 21일부터 7월 28일까지 공개 commit이나 pull request 활동을 기록하지 않았습니다. 발행된 order, settlement, market data 문서가 현재 기준으로 유지됩니다. 변경 없음 항목은 주간 명세 점검에서 Gamma를 계속 표시합니다.

### Concord: 하나의 plane 안에서 읽기 및 쓰기 capability가 나뉠 수 있다

[Concord PR #12](https://github.com/concord-protocol/concord/pull/12)는 모든 reader가 writer여서는 안 되는 plane을 위한 열린 초안으로 남아 있습니다. Control Plane을 분리된 read 및 write stream capability로 옮기고, 제한된 write channel, invite, rekey scope를 구상합니다. 초안에서 write key는 spam gate이고, 서명된 내부 actor와 roster 검사는 계속 권한을 담당합니다.

### NWC: 하나의 wallet method가 BOLT11과 BOLT12 사이에서 선택할 수 있다

[NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2)는 BIP-321 payment URI를 위한 선택적 `pay` 및 `receive` method를 제안합니다. wallet service는 지원을 알리고, URI에서 호환되는 BOLT11 invoice 또는 BOLT12 offer 하나를 선택하며, 결제 전에 일치하지 않는 Bitcoin network를 거부하고, 사용한 instruction type을 보고할 수 있습니다. 이 제안은 NWC core 밖에 남으므로 BIP-321 또는 BOLT12를 지원하지 않는 wallet은 이를 구현할 필요가 없습니다.

## Nostr의 여섯 번의 7월

이번 7월의 역사는 읽을 수 있는 식별자, relay filtering, 휴대 가능한 application data, privacy, interoperability라는 반복되는 Nostr 문제를 따라갑니다. 6년에 걸쳐 각 레이어는 좁은 범위의 수정을 공유 인프라로 바꿉니다. 이름은 프로필이 되고, filter는 application contract가 되며, relay가 운반하는 상태는 note에서 live room과 group으로 확장됩니다. [첫 NIP-05 구현](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599)에서 시작해 [이번 달의 주소 지정 가능 discovery 병합](https://github.com/nostr-protocol/nips/commit/2f4b09335c54a993d483bc220195e3f4a33df1ec)에서 끝난 뒤, 이러한 주제를 발전시킨 7월의 변경을 살펴봅니다.

### 2021년 7월

2021년 7월 19일, [nostr-tools commit 1ce00bd](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599)은 `nip05.js` module을 추가하고 package를 버전 0.5.0으로 올렸습니다. `keyFromDomain` function은 `_nostrkey.<domain>`에 대한 DNS TXT 요청을 만들고, 순환하는 DNS-over-HTTPS 제공자 8곳 중 하나에 binary query를 게시한 뒤, 응답에서 첫 번째 키를 반환했습니다. 따라서 브라우저 클라이언트는 DNS resolver를 운영하거나 하나의 hard-coded 제공자에 의존하지 않고도 사람이 관리하는 도메인을 public key로 변환할 수 있었습니다.

이 첫 접근법은 조회 문제는 해결했지만 도메인 안의 이름은 지원하지 않았고, 신뢰 경계는 DNS와 선택한 resolver에 놓였습니다. 현대 [NIP-05 명세](https://github.com/nostr-protocol/nips/blob/master/05.md)는 discovery를 `/.well-known/nostr.json`으로 옮겼으며, 여기서 도메인은 로컬 이름을 pubkey에 매핑하고 relay hint를 붙일 수 있습니다. 2021년 코드는 당시의 설계 압력을 기록합니다. public key는 휴대 가능했지만, 사람들은 여전히 읽고 검증하고 클라이언트 사이에서 옮길 수 있는 식별자가 필요했습니다.

### 2022년 7월

7월 10일, [NIP-12 commit 3771186](https://github.com/nostr-protocol/nips/commit/3771186c0351656a675576051b75d253f26c0f0b)은 일반 relay query를 한 글자 tag로 제한했습니다. 이 결정은 relay가 임의의 모든 메타데이터 key를 index할 필요 없이 `#r`, `#g`, `#t` 같은 filter를 URL 참조, geohash, hashtag에 유용하게 만들었습니다. 열흘 뒤 첫 [NIP-20 web comment 초안](https://github.com/nostr-protocol/nips/commit/9f9a864ce1e1ebfdcfdd4835cd60807440f038e8)은 이 query model을 직접 사용했습니다. kind `34` comment가 정규화된 webpage URL을 `r` tag에 담아, 사이트와 독립 클라이언트가 relay에서 같은 토론을 복구할 수 있게 했습니다.

Relay 정책과 소셜 feedback이 뒤따랐습니다. 최초 [NIP-22 commit](https://github.com/nostr-protocol/nips/commit/f51ce9dc0efaf61f39a76e112c310a9f58af1c87)은 `created_at` timestamp가 그럴듯하지 않게 오래된 이벤트를 relay가 거부할 수 있게 했고, [commit 8bef0e9](https://github.com/nostr-protocol/nips/commit/8bef0e9d79ebb4b11f8fd2bea11dc8f1668bc9d0)은 같은 정책에 미래 timestamp를 추가했습니다. 7월 30일 [NIP-25 commit dcbd504](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)은 kind `7` reaction을 target `e` 및 `p` tag와 함께 정의했습니다. 다음 commit은 부정 reaction에 `-`를 할당했고, [commit 6903ff5](https://github.com/nostr-protocol/nips/commit/6903ff5b2c395a550a26069f6e2b5460ae1fdca6)은 `+`를 명시적 일반 like로 만들었습니다. 이 commit들은 초안을 채택한 클라이언트를 위해 relay timestamp 거부, tag 기반 검색, web comment, reaction tag를 함께 규정했습니다.

### 2023년 7월

2023년 7월에는 조정 범위가 짧은 note를 넘어섰습니다. [NIP-37 분실 키 초안](https://github.com/nostr-protocol/nips/commit/e057fa01ca3928a32bdc0e9a44c27f946f267041)은 되돌릴 수 없는 키 폐기, social recovery threshold, 미리 commit한 대체 키를 탐구하면서 그 결과를 보편적 key rotation이라고 부르기를 명시적으로 거부했습니다. 닷새 뒤 [NIP-53](https://github.com/nostr-protocol/nips/commit/141197c564d97073f0293e3b2f367f0b6b3619c2)은 주소 지정 가능한 kind `30311` live activity와 kind `1311` chat message를 도입해, stream, stage, live room에 host, participant, status, conversation을 위한 공유 event model을 제공했습니다.

애플리케이션은 작업과 상거래도 알리기 시작했습니다. 첫 [Data Vending Machine 초안](https://github.com/nostr-protocol/nips/commit/67e950a2009e81df1b8c91b0a2ade0596e83f168)은 transcription, summarization, translation 같은 작업을 위한 kind `68001` job request, kind `68002` result, bid, expiration, chaining, 경쟁 provider를 설명했습니다. 7월 13일 [classified listing 초안](https://github.com/nostr-protocol/nips/commit/451c06a3c572a13afe45c1d80616f8e6dd9bb1de)은 title, summary, price, location, status 메타데이터를 가진 주소 지정 가능한 kind `30402` offer를 추가했습니다. 이 초안들은 나중에 NIP-90과 NIP-99가 되었지만, 7월 형태에서 이미 request 또는 listing을 이를 표시하는 서버와 분리했습니다.

Payment routing도 조합 가능해졌습니다. 7월 31일의 [NIP-57 zap split 병합](https://github.com/nostr-protocol/nips/commit/5d63b1570c490007252b10e757f7f68ef1f4b717)은 단일 `zap` destination을 수신자 pubkey 및 relay hint의 가중치 리스트로 바꿨습니다. 클라이언트는 하나의 zap을 여러 협업자에게 나누고, 일부 weight가 있을 때 weight가 없는 수신자를 제외하며, 결제 전에 split을 표시할 수 있었습니다. 이 변경은 가중치가 있는 zap 수신자와 relay hint를 위한 서명된 event 표현을 표준화하여, 호환 클라이언트가 결제 전에 split을 제시할 수 있게 했습니다.

### 2024년 7월

7월 4일, [NIP-29 commit c60ca88](https://github.com/nostr-protocol/nips/commit/c60ca888efbdc9b8fa4bbfbace372409d0b2161a)는 그룹을 생성하는 `kind:9007` relay moderation action을 추가했습니다. 엿새 뒤 [NIP-70](https://github.com/nostr-protocol/nips/commit/ae1906ec7943a6bd756f05d2cd2fb2a041398921)은 protected event를 정의했습니다. `-` tag는 이벤트의 인증된 작성자에게서 온 발행만 수락하라고 relay에 알립니다. 한 변경은 relay에 명시적 그룹 상태 전이를 제공했고, 다른 변경은 작성자가 제3자가 유효하게 서명된 이벤트를 relay에 replay하는 것을 막게 했습니다.

7월 16일, 하나의 [Cashu 명세 commit](https://github.com/nostr-protocol/nips/commit/506b38916ab67a37b2d98b46b62cf0c0c5fde5a4)은 NIP-60 wallet과 NIP-61 nutzap을 함께 도입했습니다. NIP-60은 kind `37375`에 wallet 메타데이터를, 암호화된 kind `7375` 이벤트에 사용하지 않은 proof를, kind `7376`에 선택적 transaction history를 넣었습니다. NIP-61은 수신자의 kind `10019` mint 및 relay preference를 P2PK로 잠긴 kind `7337` nutzap과 짝지었습니다. Wallet 상태와 bearer token은 이제 relay를 통해 이동할 수 있었지만, redemption은 여전히 Cashu mint proof와 double claim을 세심하게 방지하는 데 의존했습니다.

7월 말의 편집 두 건은 결정론적 상태를 강화했습니다. [NIP-01 commit 9c54549](https://github.com/nostr-protocol/nips/commit/9c54549f1842245b842d8a66f3bade744da24189)은 같은 `created_at` timestamp 뒤의 tie-breaker로 event ID를 요구해, 클라이언트가 같은 결과 집합을 같은 방식으로 정렬할 수 있게 했습니다. [NIP-09 삭제 병합](https://github.com/nostr-protocol/nips/commit/722ac7a58695a365be0dbb6eccb33ccd7890a8c7)은 kind `5` 요청이 event ID 또는 주소 지정 가능한 coordinate를 대상으로 할 수 있고 relay가 삭제해야 할 kind를 식별하는 `k` tag를 포함해야 한다고 명확히 했습니다. 두 변경은 올바른 구현 두 개가 서로 다르게 판단할 수 있는 지점을 줄였습니다.

### 2025년 7월

Ecash discovery는 7월 16일 자체 social directory를 얻었습니다. [NIP-87 commit 1afb6da](https://github.com/nostr-protocol/nips/commit/1afb6da049e57dd628ef46a3b0f90300653a66ee)은 kind `38172` Cashu mint record, kind `38173` Fedimint record, relay hint와 함께 이 record를 가리킬 수 있는 kind `38000` recommendation을 정의했습니다. Wallet은 mint에 연결하기 전에 신뢰하는 작성자의 recommendation을 query할 수 있었고, 명세는 filter 없는 글로벌 discovery가 사용자를 악의적 운영자로 유도할 수 있다고 경고했습니다.

일주일 뒤 한 초안은 음성 메시지를 위한 휴대 가능한 Nostr event record를 규정했습니다. 첫 [NIP-A0 commit](https://github.com/nostr-protocol/nips/commit/e50f37a527ace39cc3057827d52295c6b6de1112)은 음성 메시지 root에 kind `1222`, 답글에 kind `1244`를 할당하고 audio URL과 media 메타데이터를 담았습니다. 7월 27일의 [format 후속 변경](https://github.com/nostr-protocol/nips/commit/4984b057c20397eae919ee5e463bc8a5d3fb2dc0)은 Ogg container의 Opus를 권장하고 압축 waveform을 표준화했습니다. 클라이언트는 하나의 recorder, host, waveform 표현에 합의하지 않고도 짧은 audio를 교환할 수 있었습니다.

이어 비공개 메시징과 wallet 연결은 읽음 추적, 암호화 선택, 결제 진행 상황을 위한 프로토콜 상태를 추가했습니다. [NIP-17 commit 3d76da3](https://github.com/nostr-protocol/nips/commit/3d76da368e157934e056d95b3b3d8d6eaa105b09)은 교체 가능한 kind `30016` record를 정의했으며, 순서가 있는 `seen` tag를 통해 클라이언트가 읽은 메시지와 놓쳤을 수 있는 공백을 구분하게 했습니다. 7월 31일 [NIP-47 암호화 협상](https://github.com/nostr-protocol/nips/commit/f30a43bd37e08516923b96dd0d860122c9ffe04e)은 wallet service가 NIP-44 v2 또는 legacy NIP-04를 알릴 수 있게 했고, [transaction 상태 commit](https://github.com/nostr-protocol/nips/commit/0595d438aaa163dd33ed00748026698a411a0861)은 `pending`, `settled`, `accepted`, `expired`, `failed` 상태를 추가했습니다. 전달, 암호화, 결제 진행 상황은 로컬 추론이 아니라 명시적 프로토콜 데이터가 되었습니다.

### 2026년 7월

이번 7월은 일반 web address를 relay query와 연결하며 시작했습니다. [주소 지정 가능 discovery commit 2f4b093](https://github.com/nostr-protocol/nips/commit/2f4b09335c54a993d483bc220195e3f4a33df1ec)은 응답에 Nostr filter와 relay 리스트가 들어가는 `/.well-known/nostr.json?ad=<path>` 조회를 정의합니다. 일반 브라우저는 원래 URL을 HTML로 계속 열 수 있고, Nostr 클라이언트는 해당 `/.well-known/nostr.json?ad=<path>` endpoint에 filter 및 relay 리스트를 query해 주소를 group, nsite, feed, event 또는 다른 네이티브 객체로 해석할 수 있습니다. 이 패턴은 2021년의 도메인 대 키 문제를 더 넓은 레이어에서 다시 다룹니다. 하나의 사람이 읽을 수 있는 URL이 이제 신원과 query를 모두 가리킬 수 있습니다.

이어 NIP-29는 평면 relay 그룹에서 구조화된 공간으로 성장했습니다. 7월 16일 [하위 그룹 commit](https://github.com/nostr-protocol/nips/commit/223ddb3b0c282f2a133adb9f4a9c098a31b36937)은 parent 및 순서가 있는 child 관계를 추가했고, 인접한 commit은 invite code suffix, banner, 순서가 있는 pin snapshot, 주소 지정 가능한 event pin을 추가했습니다. 7월 22일 [이전 및 fork 명확화](https://github.com/nostr-protocol/nips/commit/db5fe3de8c5d1443b634c9bbf66ecb004f337057)은 메타데이터가 그룹을 다른 relay로 정당하게 옮기는 시점과 여전히 활성인 branch가 독립 fork가 되는 시점을 정의했습니다. 그룹 식별자는 단순하게 유지됐고 hierarchy, presentation, relay 변경은 명시적 상태가 되었습니다.

더 작은 편집 두 건은 구현 경계를 명확히 했습니다. [NIP-46 commit f0af204](https://github.com/nostr-protocol/nips/commit/f0af20484c5e0d12e2d1936f87c5a6681a08daff)는 클라이언트가 조용히 timeout할 때까지 두는 대신 원격 서명자가 알 수 없거나 지원하지 않는 method에 오류를 반환하도록 요구합니다. [NIP-34 commit 6d2979b](https://github.com/nostr-protocol/nips/commit/6d2979b3f503a8539c983efbcdcf901bbcf9ed23)은 pull request event 설명에서 GRASP 전용 호스팅 지침을 제거합니다. 하나는 caller에 terminal response를 제공하고, 다른 하나는 휴대 가능한 git event가 하나의 server protocol을 암묵적으로 상속하지 않게 합니다.

---

[Nostr Compass 프로젝트](https://github.com/andotherstuff/nostr-compass)를 통해 프로젝트나 소식을 공유하려면 NIP-17 DM을 보내 주세요.
