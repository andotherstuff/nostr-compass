---
title: 'Nostr Compass #18'
date: 2026-04-15
translationOf: /en/newsletters/2026-04-15-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [Amethyst](https://github.com/vitorpamplona/amethyst)가 데스크톱 Tor 지원, JNI 바인딩이 포함된 커스텀 C secp256k1 구현, [NIP-AC](/ko/topics/nip-ac/) 음성 및 영상 통화를 위한 완전한 WebRTC 호출 시스템, [Marmot](/ko/topics/marmot/)용 RFC 9420 MLS 준수, 그리고 멀티 지갑 NWC를 포함해 29개의 PR을 병합했습니다. [nstrfy](https://github.com/vcavallo/nstrfy-android)는 kind `7741` 이벤트를 사용해 Firebase를 Nostr 릴레이로 대체하는 Android 푸시 알림 앱으로 출시되었습니다. [HAMSTR](https://github.com/LibertyFarmer/hamstr)는 Reticulum mesh networking을 추가해 인터넷 연결 없이 LoRa radio 위로 Nostr 이벤트를 전달할 수 있게 했습니다. [Bloom](https://github.com/nostrnative/bloom)은 [Blossom](/ko/topics/blossom/) 미디어 서버와 Nostr relay를 한데 묶은 데스크톱 앱 v0.1.0을 출시했습니다. [WaveFunc](https://github.com/zeSchlausKwab/wavefunc)는 Nostr 기반 인터넷 라디오 디렉터리이자 플레이어인 v0.1.0으로 데뷔했습니다. [Botburrow](https://github.com/marmot-protocol/botburrow)는 [Marmot](/ko/topics/marmot/) 암호화 그룹 채팅용 self-hosted bot 플랫폼으로 개발을 시작했습니다. [Snort](https://github.com/v0l/snort)는 보안 감사, batched WASM 검증, 재작성된 메시징 시스템이 포함된 v0.5.0부터 v0.5.3까지를 배포했습니다. 이번 주 NIP 심층 분석은 [NIP-29](/ko/topics/nip-29/)와 [NIP-90](/ko/topics/nip-90/)을 다룹니다.

## Top Stories

### Amethyst merges desktop Tor, C secp256k1, WebRTC calls, and multi-wallet NWC

vitorpamplona가 유지 관리하는 Android 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)는 이번 주 암호화, 네트워킹, 통화, 지갑 인프라 전반에 걸쳐 29개의 PR을 병합했습니다.

[PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381)은 이번 주 가장 큰 변경으로, fail-closed 설계를 가진 내장 kmp-tor daemon을 통해 데스크톱 Tor 지원을 추가합니다. Tor가 켜져 있으면 모든 relay 연결이 내장 Tor 프로세스를 통해 라우팅되고, Tor가 시작되지 않으면 앱은 연결을 거부합니다. 이제 privacy routing은 Android와 데스크톱 빌드 사이에서 기능 parity를 갖추며, Tor 통합에는 130개가 넘는 unit test가 붙었습니다.

[PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374)는 서명 검증용 JNI 바인딩이 포함된 커스텀 C secp256k1 구현을 추가합니다. 이 구현은 GLV decomposition, wNAF (windowed Non-Adjacent Form) point encoding, 그리고 x86_64와 ARM64 양쪽의 하드웨어 가속 SHA-256을 사용합니다. 결과적으로 Schnorr signature 검증이 이전 pure Kotlin 경로보다 2배에서 3배 빨라졌습니다. 이어지는 PR들([PR #2188](https://github.com/vitorpamplona/amethyst/pull/2188), [PR #2195](https://github.com/vitorpamplona/amethyst/pull/2195), [PR #2204](https://github.com/vitorpamplona/amethyst/pull/2204))은 fused multiply-reduce 연산, field element 저장용 LongArray를 대체하는 전용 Fe4 struct, 플랫폼별 intrinsic을 추가해 Android에서 약 28%의 추가 개선을 목표로 합니다.

[PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202)는 pure Kotlin MLS 구현을 RFC 9420에 맞추어 갱신하며, [Marmot](/ko/topics/marmot/) 프로토콜 통합을 위해 reuse guard 검사, ciphertext 연산의 additional authenticated data (AAD), ciphertext sample derivation, commit 처리 수정, thread safety를 추가합니다. [지난주 다룬 Kotlin MLS 작업](/en/newsletters/2026-04-08-newsletter/)을 바탕으로, 이 작업은 [Quartz](/ko/topics/quartz/)를 완전한 MLS 명세 준수에 더 가깝게 밀어 붙입니다.

[PR #2203](https://github.com/vitorpamplona/amethyst/pull/2203)부터 [PR #2211](https://github.com/vitorpamplona/amethyst/pull/2211)까지 이어지는 WebRTC PR 묶음은 [NIP-AC](/ko/topics/nip-ac/)용 완전한 음성 및 영상 통화 시스템을 추가합니다. 구현 범위에는 연결이 끊겼을 때의 ICE restart, 런타임 camera 전환, 자동 재연결이 포함된 network monitoring, 설정 가능한 통화 옵션(resolution, bitrate, TURN server 선택), Android 14+ 백그라운드 제한 대응용 foreground service 수정, 그리고 통화 state machine 전반의 thread safety가 포함됩니다.

[PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988)는 멀티 지갑 [NIP-47](/ko/topics/nip-47/) (Nostr Wallet Connect) 지원을 추가합니다. 이제 사용자는 하나의 계정에 여러 NWC 지갑을 연결하고, 각 지갑의 잔액 카드를 보고, 기본 지갑을 선택하고, 예전 단일 지갑 구성에서 마이그레이션할 수 있습니다.

[PR #2189](https://github.com/vitorpamplona/amethyst/pull/2189)는 품질 슬라이더가 있는 GIF-to-MP4 변환을 추가해 3MB GIF를 약 159KB MP4로 줄입니다. 같은 주에 post composer에는 자동 언어 감지와 제안 사전 계산 병렬화가 포함된 AI tone suggestion도 들어왔습니다.

### nstrfy launches Nostr-native push notifications for Android

[nstrfy](https://github.com/vcavallo/nstrfy-android)는 4월 13일 [v1.0.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.0.0)부터 [v1.2.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.2.0)까지 세 개의 릴리스와 함께 출시되었습니다. 이 앱은 ntfy-android의 fork로, HTTP transport를 Nostr로 교체했습니다. 서버를 polling해 푸시 알림을 받는 대신, nstrfy는 설정 가능한 릴레이에서 kind `7741` 이벤트를 subscribe하고 이를 네이티브 Android notification으로 표시합니다.

알림 모델은 평문 payload와 [NIP-44](/ko/topics/nip-44/) 암호화 payload를 모두 지원합니다. 암호화가 켜져 있으면 nstrfy는 [Amber](https://github.com/greenart7c3/Amber)를 통해 [NIP-55](/ko/topics/nip-55/)로 서명하거나 로컬 nsec을 사용합니다. 주제별 subscription을 통해 사용자는 topic별 발신자 allowlist와 npub whitelist를 구성할 수 있어 승인된 발신자만 특정 topic의 알림을 발생시킬 수 있습니다. 앱은 [NIP-65](/ko/topics/nip-65/)를 사용해 사용자 프로필에서 relay 목록을 가져오고, [NIP-40](/ko/topics/nip-40/) 이벤트 만료도 존중합니다. 전체 ntfy 알림 어휘, 즉 URL tap-to-open, priority level, custom icon, action button을 지원하므로 대부분의 ntfy 스타일 알림은 거의 그대로 옮겨집니다. 사용자 검색은 brainstorm.world의 [Web of Trust](/ko/topics/web-of-trust/) 데이터를 통한 NIP-50 기반입니다.

[nstrfy.sh](https://github.com/vcavallo/nstrfy.sh) 동반 프로젝트는 browser에서 전송과 수신을 할 수 있는 bash CLI와 [nstrfy.sh](https://nstrfy.sh) 호스팅 웹 클라이언트를 함께 제공합니다. NIP-07 signer도 지원합니다. 네이티브 앱은 [Zapstore](https://zapstore.dev/apps/io.nstrfy.android)에서 받을 수 있습니다.

### HAMSTR adds Reticulum for Nostr over LoRa mesh

[HAMSTR](https://github.com/LibertyFarmer/hamstr)는 ham radio 위로 Nostr 이벤트와 Lightning zap을 보내는 프로젝트로, 4월 12일 [PR #10](https://github.com/LibertyFarmer/hamstr/pull/10)을 병합해 [Reticulum](https://reticulum.network/) mesh networking을 transport backend로 추가했습니다. Reticulum은 LoRa, HF, VHF/UHF radio, serial link, TCP/IP 위에서 동작하는 암호화 mesh 프로토콜입니다. 이 추가로 HAMSTR는 인터넷 인프라가 전혀 없는 상태에서도 RNode hardware 장치 mesh를 통해 Nostr 이벤트를 중계할 수 있게 됩니다.

기존 AX.25 Packet Radio와 VARA HF transport도 그대로 유지되므로, 운영자는 자신의 환경에 맞는 radio link를 선택할 수 있습니다. HAMSTR의 zero-knowledge 서버 아키텍처는 relay가 개인 키를 보지 못하게 하며, [NIP-57](/ko/topics/nip-57/) zap 준수 덕분에 offline Lightning zap이 Amethyst와 Primal 같은 클라이언트에 올바르게 표시됩니다. Reticulum transport용 설정 가이드는 [RETICULUM.MD](https://github.com/LibertyFarmer/hamstr/blob/master/RETICULUM.MD)에 포함되어 있습니다. 같은 주에 [PR #11](https://github.com/LibertyFarmer/hamstr/pull/11)은 프론트엔드를 Svelte 5와 TailwindCSS v4로 옮겼습니다.

## Shipping This Week

### Bloom v0.1.0 ships self-hosted Blossom server and relay

[Bloom](https://github.com/nostrnative/bloom)은 4월 9일 첫 릴리스인 [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0)을 배포했습니다. Tauri v2 (Rust backend)와 React 19로 구축된 Bloom은 전체 [Blossom](/ko/topics/blossom/) 프로토콜 미디어 서버(BUD-00부터 BUD-10까지)와 Nostr relay를 하나의 데스크톱 애플리케이션으로 묶어 macOS, Windows, Linux에서 실행합니다. Android와 iOS 빌드도 계획되어 있습니다. 사용자는 SHA-256 content addressing, [NIP-94](/ko/topics/nip-94/) 파일 메타데이터 지원, `blossom://` URI 해석을 갖춘 sovereign file storage를 별도의 서버 인프라 관리 없이 사용할 수 있습니다. 릴리스에는 16개의 플랫폼별 binary asset이 포함됩니다.

### WaveFunc v0.1.0 and v0.1.1 launch Nostr internet radio

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc)는 4월 13일 [v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0)과 [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1)을 배포하며 Nostr 기반 인터넷 라디오 디렉터리이자 플레이어로 출범했습니다. 커스텀 event kind가 데이터 모델을 정의합니다. 라디오 방송국 목록용 kind `31237`, 즐겨찾기 목록용 kind `30078`, 라이브 채팅용 kind `1311`, 방송국 댓글용 kind `1111`입니다. Khatru relay backend는 SQLite 저장과 Bluge full-text search를 제공하며 [NIP-50](/ko/topics/nip-50/)을 지원합니다.

WaveFunc는 [NIP-60](/ko/topics/nip-60/) Cashu wallet과 nutzap 지원을 포함해 출시되었고, NDK에서 applesauce-core로 마이그레이션했습니다. [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1)은 genre carousel, Lightning donation popover, 인증 사용자용 방송국 관리, Zapstore listing을 추가합니다. Tauri v2 데스크톱 빌드는 system tray 통합, media key 지원, autostart, deep linking을 얻었습니다. 빌드는 [wavefunc.live](https://wavefunc.live)에서 macOS, Windows, Linux, Android용으로 제공됩니다.

### Snort ships v0.5.0 through v0.5.3 with security hardening and performance overhaul

[Snort](https://github.com/v0l/snort)는 React 기반 Nostr 웹 클라이언트로, [v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0)부터 [v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3)까지 세 개의 릴리스를 배포했습니다. 핵심인 v0.5.0은 실제 Schnorr signature 검증, 위조 relay 메시지에 대한 [NIP-46](/ko/topics/nip-46/) 보호 강화, 개선된 PIN 암호화, 검증되지 않은 [NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md) delegation 신뢰 제거를 포함한 포괄적 보안 감사를 제공합니다. 성능 측면에서는 batched WASM signature 검증, lazy-loaded route, batch loading과 chunking이 포함된 재작성된 priority profile loader, worker-relay 최적화가 들어갔습니다. 같은 릴리스는 [NIP-90](/ko/topics/nip-90/) DVM을 위한 kind `7000` payment-required invoice 표시도 추가했습니다. [PR #620](https://github.com/v0l/snort/pull/620)은 메시징 시스템을 성능 중심으로 재설계해 worker relay에 gift wrap을 영속화하고 O(n²) 채팅 목록 계산을 단일 pass Map 기반 접근으로 바꿨습니다.

### Primal Android ships 3.0.21 and redesigns feed layout

[Primal Android](https://github.com/PrimalHQ/primal-android-app)는 poll zap 투표, wallet multi-account sharing, remote signer와 wallet service의 auto-reconnect 버그 수정을 포함한 [v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21)을 배포했습니다. 이어서 일곱 개의 PR이 병합됐습니다. [PR #1008](https://github.com/PrimalHQ/primal-android-app/pull/1008)은 main screen layout을 통합하고, [PR #1010](https://github.com/PrimalHQ/primal-android-app/pull/1010)은 더 큰 avatar와 content indentation을 가진 새 feed card 디자인을 도입하며, [PR #1009](https://github.com/PrimalHQ/primal-android-app/pull/1009)은 media feed card에 video 지원과 portrait layout을 추가하고, [PR #1012](https://github.com/PrimalHQ/primal-android-app/pull/1012)는 빠른 답글용 compact text field를 도입하며, [PR #1013](https://github.com/PrimalHQ/primal-android-app/pull/1013)은 app bar를 재설계합니다.

### Nostria v3.1.19 through v3.1.21 add local AI image generation

[Nostria](https://github.com/nostria-app/nostria)는 [v3.1.19](https://github.com/nostria-app/nostria/releases/tag/v3.1.19)부터 [v3.1.21](https://github.com/nostria-app/nostria/releases/tag/v3.1.21)까지 세 개의 릴리스를 80개가 넘는 커밋과 함께 배포했습니다. 핵심 추가 사항은 WebGPU 가속을 사용하는 Janus Pro 기반 로컬 이미지 생성으로, 사용자가 외부 API 없이 장치에서 이미지를 생성할 수 있게 합니다. 이 릴리스들은 cloud image generation, multimodal chat, ONNX runtime 지원, AI prompt library, AI cache 관리도 추가합니다. 클라이언트 쪽에서는 새로운 dialog 시스템, note editor overhaul, music embed 개선, signer login flow 변경이 포함됐습니다. [뉴스레터 #17](/en/newsletters/2026-04-08-newsletter/)은 local signer 지원이 포함된 v3.1.18 native mobile 릴리스를 다뤘습니다.

### TubeStr v1.0.3 ships feed and studio updates

[TubeStr](https://github.com/Tubestr/tubestr-v2)는 Nostr 위에 구축된 private family video sharing 앱으로, 4월 13일 [v1.0.3](https://github.com/Tubestr/tubestr-v2/releases/tag/v1.0.3)을 배포했습니다. 이 릴리스는 feed와 studio 개선을 포함합니다. [PR #3](https://github.com/Tubestr/tubestr-v2/pull/3)은 onboarding screen을 전면 개편하고, [PR #2](https://github.com/Tubestr/tubestr-v2/pull/2)는 video export 오류를 수정합니다. 이 앱은 가족 간 암호화 미디어 공유를 위해 NDK와 MDK ([Marmot](/ko/topics/marmot/) Development Kit)를 사용하며, 미디어 저장을 위한 [Blossom](/ko/topics/blossom/) 통합도 계획 중입니다. TubeStr는 [Zapstore](https://zapstore.dev)에서 받을 수 있습니다.

## In Development

### Botburrow begins development as Marmot bot platform

[Botburrow](https://github.com/marmot-protocol/botburrow)는 Marmot 팀의 새 프로젝트로, 4월 3일 시작됐습니다. 이는 self-hosted bot 관리 플랫폼으로, 각 bot은 자체 Nostr identity를 갖고 [Marmot](/ko/topics/marmot/) MLS 암호화 그룹 채팅에 Welcome 메시지로 참여하며, end-to-end encrypted 메시지를 주고받습니다. Rails 8.1로 구축된 dashboard는 하나의 whitenoise-rs daemon (`wnd`)과 Unix socket을 통해 통신합니다.

Botburrow는 꽤 큰 scripting 및 운영 계층을 노출합니다. command, trigger, scheduled action이 커스텀 Ruby 코드를 실행하고, script는 `wnd`를 통해 profile, group membership, pending invite를 검사할 수 있으며, dashboard에는 실제 그룹 안에서 bot을 메시징하는 live chat view가 포함됩니다. 각 bot은 config, 캐시 데이터, 생성 결과물을 위한 자체 file storage도 가집니다. [멀티 아키텍처 Docker image](https://github.com/marmot-protocol/botburrow/commit/2ed012078eaab3c5b92dff16b87865c2e353bd80)는 Umbrel과 Start9에서 zero-config self-hosting을 목표로 합니다. README의 [trust model section](https://github.com/marmot-protocol/botburrow/commit/c8ef8c306af247560b1952878206d854cde3fe20)은 보안 경계를 문서화합니다.

### Nostr Archives adds trending feeds relay and entity resolution

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api)는 [nostrarchives.com](https://nostrarchives.com)의 Nostr archival 및 analytics 플랫폼으로, [API](https://github.com/barrydeen/nostrarchives-api) (Rust)와 [frontend](https://github.com/barrydeen/nostrarchives-frontend) (Next.js 16) 양쪽에서 꾸준한 개발을 이어갔습니다. API 쪽에서는 [PR #118](https://github.com/barrydeen/nostrarchives-api/pull/118)이 client leaderboard에 time-range filtering을 추가했고, [PR #117](https://github.com/barrydeen/nostrarchives-api/pull/117)은 reply 이벤트에 engagement counter를 추가했습니다. 프론트엔드에서는 [PR #85](https://github.com/barrydeen/nostrarchives-frontend/pull/85)가 URL path에서 Nostr entity를 직접 해석하고, [PR #86](https://github.com/barrydeen/nostrarchives-frontend/pull/86)은 API 문서 페이지를 추가합니다. 이 플랫폼은 NIP-50 search relay, trending feeds relay(`wss://feeds.nostrarchives.com`), 미래 시각 이벤트용 scheduler relay, kinds 0, 3, 10002용 indexer relay까지 네 개의 relay 서비스를 운영합니다.

### Damus fixes favorites timeline

[Damus](https://github.com/damus-io/damus)는 iOS 클라이언트로, [PR #3708](https://github.com/damus-io/damus/pull/3708)을 병합해 `subscribe_to_favorites()` 함수를 in-place filtering, deduplication rebuilding, persisted tab selection 방식으로 재작성했습니다.

### Nostur adds private zaps and custom emoji viewing

[Nostur](https://github.com/nostur-com/nostur-ios-public)는 이번 주 10개의 커밋을 푸시하며 private zap 지원, custom emoji 보기, animated `.webp` 렌더링 수정, voice message audio format 감지를 추가했습니다.

### Amber ships v6.0.1 through v6.0.3 with WebDAV backup and relay reconnection fixes

[Amber](https://github.com/greenart7c3/Amber)는 Android [NIP-55](/ko/topics/nip-55/) signer 앱으로, 이번 주 세 개의 릴리스를 배포했습니다. [v6.0.1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.1)은 두 개의 새 backup 옵션(WebDAV와 Google Drive 공유), relay 재연결용 exponential backoff, Quartz 라이브러리 1.08.0 업데이트, 앱 업데이트와 profile 이벤트에 대한 event validation 수정을 포함합니다. [v6.0.2](https://github.com/greenart7c3/Amber/releases/tag/v6.0.2)는 seed word 사용 시 account index 옵션을 추가하고, 시작 시 relay가 offline인 경우 relay 재연결 문제를 고칩니다. [v6.0.3](https://github.com/greenart7c3/Amber/releases/tag/v6.0.3)은 intent 수신 시 비어 있는 request ID 문제에 대한 추가 수정을 담습니다.

### Plektos v0.6.0 redesigns with Ditto themes

[Plektos](https://github.com/derekross/plektos)는 인터랙티브 맵 위에 구축된 [NIP-52](/ko/topics/nip-52/) 기반 분산 meetup 및 이벤트 플랫폼으로, 4월 14일 [v0.6.0](https://github.com/derekross/plektos/commit/7a691cdf089ceb7a8582dd5c0ee026830f2cdc77)과 [v0.6.1](https://github.com/derekross/plektos/commit/3a6474ae380522d8ee1b3526423fcfc3328fd879)을 배포했습니다. 이 업데이트는 custom background image 업로드, avatar shape 설정, UI overhaul이 포함된 Ditto 스타일 community theme를 추가합니다. [PR #6](https://github.com/derekross/plektos/pull/6)은 보안, 아키텍처, UX 결과를 포함한 전체 코드 리뷰를 반영합니다. Plektos는 프로토콜 통합에 Nostrify를, 원격 로그인에 [NIP-46](/ko/topics/nip-46/)을, 티켓 결제에 zaps를 사용합니다. Android 빌드는 Zapstore에서 받을 수 있습니다.

### Shadow adds Nostr OS API and Cashu wallet app

[Shadow](https://github.com/justinmoon/shadow)는 Justin Moon의 앱 runtime 플랫폼으로, 이틀 동안 30개가 넘는 커밋을 푸시했습니다. [Commit 88cbda5](https://github.com/justinmoon/shadow/commit/88cbda5131814d2730a2d892029932136db005df)는 Shadow runtime 안에서 실행되는 Cashu wallet 앱을 추가합니다. [Commit 865c415](https://github.com/justinmoon/shadow/commit/865c415)는 podcast player 데모를 더합니다. runtime은 `Shadow.os.nostr`와 `Shadow.os.audio`를 1급 OS 수준 API로 노출하며, Pixel runtime 레인은 루팅된 Android 장치에서 GPU compositing이 포함된 Wayland compositor를 실행합니다. 기여자 k0sti의 [PR #1](https://github.com/justinmoon/shadow/pull/1)과 [PR #2](https://github.com/justinmoon/shadow/pull/2)는 데스크톱 Linux font loading과 XDG state directory 처리를 수정합니다. 아직 정식 릴리스는 없습니다.

### Lief fixes Amber login and adds Zapstore

[Lief](https://gitlab.com/chad.curtis/lief)는 다른 Nostr 사용자에게 장문 편지를 작성하고 보내는 앱으로, 4월 12일 build `v2026.04.12`를 배포했습니다. 이 업데이트는 Android에서 [Amber](https://github.com/greenart7c3/Amber) signer 로그인 문제를 고치고, signer nudge 흐름을 단순화하며, nostrify 의존성을 업그레이드하고, Zapstore 통합을 추가합니다.

### Espy overhauls color picker and fixes Amber login

[Espy](https://gitlab.com/chad.curtis/espy)는 사용자가 현실 장면에서 3개에서 6개의 색 팔레트를 공유하는 Nostr 소셜 앱으로, 4월 12일 build `v2026.04.12`를 배포했습니다. 이 업데이트는 grayscale toggle을 대체하는 curved saturation arc가 포함된 color picker overhaul, hue ring flicker 수정, Easter egg 캐릭터(Alchemist와 Astrologer) 추가를 포함합니다. PNG asset 압축으로 703KB를 줄였습니다. 이 릴리스는 또한 [Amber](https://github.com/greenart7c3/Amber) signer 로그인 문제를 고치고, signer nudge 흐름을 단순화하며, nostrify 의존성을 올리고, Zapstore 통합을 더합니다.

### Jumble adds per-feed kind filters and articles tab

[Jumble](https://github.com/CodyTseng/jumble)은 이번 주 13개의 커밋을 푸시하며 per-feed kind filtering, Articles 탭, privacy-preserving 옵션이 있는 notification read status sync, avatar 숨김 모드, account switching race condition 수정을 추가했습니다.

### Primal Web ships 8 version bumps

[Primal Web](https://github.com/PrimalHQ/primal-web-app)는 1주일 동안 21개 커밋과 함께 3.0.93부터 3.0.101까지 버전을 배포했습니다. 작업은 live stream chat 개선, mention 경계 수정, bookmark pagination, duplicate like 방지, relay proxy 수리에 집중됐습니다.

## Protocol and Spec Work

### NIP Updates

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항입니다:

**Merged:**

- **[NIP-34](/ko/topics/nip-34/) (Git Stuff): Add `nostr://` clone URLs** ([PR #2312](https://github.com/nostr-protocol/nips/pull/2312)): [NIP-34](/ko/topics/nip-34/)는 브랜치, 태그, relay 위치, maintainer pubkey를 나열하는 kind `30617` 저장소 공지로 git 저장소를 Nostr 위에 호스팅하는 방법을 정의합니다. 지금까지 이 명세에는 저장소를 참조하는 공식 URL scheme이 없었습니다. 이 PR은 `git-remote-nostr` helper와 함께 동작하는 `nostr://` clone URL 형식을 추가합니다. 따라서 `git clone nostr://npub1.../relay.ngit.dev/ngit` 같은 형식으로 npub 또는 [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md) 주소를 해석하고, 저장소 relay 위치를 발견하며, 저장소 데이터를 가져올 수 있습니다. 세 가지 URL 패턴이 정의됩니다. 직접 addressable event 참조용 `nostr://<naddr>`, 사람이 읽을 수 있는 저장소 참조용 `nostr://<npub|nip05>/<identifier>`, 그리고 클라이언트가 relay hint가 필요할 때의 `nostr://<npub|nip05>/<relay-hint>/<identifier>`입니다. relay hint와 identifier는 모두 RFC 3986에 따라 percent-encoding됩니다. 이 형식은 이미 Shakespeare, ngit의 git-remote-nostr helper, GitWorkshop.dev, NostrHub.io가 구현하거나 표시하고 있습니다. PR은 또한 저장소 식별자를 위한 `d` 태그 형식을 더 엄격히 해 `nostr://` URL이 유효한 URI를 생성하도록 만듭니다.

**Open PRs and Discussions:**

- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): 유료 콘텐츠 접근을 위해 콘텐츠 제작자가 payment gateway, pricing model, subscription rule을 선언할 수 있는 새 kind `10164` replaceable event를 제안합니다. 현재 Nostr에서 결제 게이트 콘텐츠를 지원하려면 각 클라이언트가 자체 결제 흐름을 구현해야 하며, 제작자가 "이 콘텐츠는 gateway Y를 통해 X sats"라고 표준 방식으로 선언할 수 없습니다. 제안된 이벤트는 payment gateway descriptor를 Nostr 이벤트에 직접 내장해, 클라이언트가 하나의 replaceable event에서 제작자의 허용 결제 방식, 가격 tier, subscription 옵션을 발견할 수 있게 합니다. 이로써 결제 표현을 특정 제공자와 분리하므로 제작자는 각 클라이언트가 제공자별로 별도 통합을 구현하지 않아도 Lightning, Cashu, fiat gateway를 함께 받을 수 있습니다.

- **NIP-XX: Relay Self-Declaration Manifest and Retention Horizon** ([PR #2314](https://github.com/nostr-protocol/nips/pull/2314)): relay transparency를 위한 두 개의 wire protocol primitive를 제안합니다. 첫 번째는 relay 운영자가 endpoint(clearnet, Tor, I2P), retention window, write policy, 지원 NIP를 선언하는 gossip 가능한 replaceable event kind `10100`입니다. HTTP로만 제공되고 Nostr 자체로는 발견할 수 없는 [NIP-11](/ko/topics/nip-11/) relay information document와 달리, kind `10100` manifest는 다른 이벤트처럼 Nostr event 네트워크를 통해 전파됩니다. NIP-11 `pubkey` 필드를 통한 TOFU key binding으로 spoofing을 막습니다. 두 번째는 `HORIZON`이라는 새 relay-to-client 메시지 `[["HORIZON", <sub_id>, <earliest_timestamp>]]`로, `EOSE` 전에 전송됩니다. 클라이언트의 subscription time range가 릴레이 retention window를 넘어가면, 릴레이는 자신이 보유한 가장 이른 타임스탬프를 알려 줍니다. 이렇게 하면 "결과 없음"이라는 침묵 대신 "timestamp X부터의 데이터만 있다"는 명시적 경계가 생깁니다. 동기는 2026년 2월 NIP-11의 `retention` 필드가 거의 쓰이지 않는 HTTP 전용 전달 모델 때문에 제거된 데 있습니다. 참조 구현은 nostr-rs-relay 0.9.0 위에서 90일 pruning으로 동작합니다.

- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): 특정 수신자와 암호화된 위치 데이터를 공유하기 위한 kind `20411`(ephemeral 범위)을 제안합니다. Google Maps와 Apple Find My 같은 중앙화 위치 공유 서비스는 실시간 이동 정보를 중앙 권한자에게 맡기게 만듭니다. 이 NIP는 privacy-first 대안을 정의합니다. 이벤트 content에는 수신자 pubkey를 key로 하고, configurable precision의 geohash를 담은 [NIP-44](/ko/topics/nip-44/) 암호화 payload를 value로 하는 JSON map이 들어갑니다. precision 5면 도시 수준, precision 8이면 거리 수준입니다. 여러 수신자를 하나의 이벤트 안에서 수신자별 암호화로 처리하므로, 각자는 자기 payload만 복호화할 수 있습니다. `ttl` 태그는 권장 보존 시간(초)을 지정하고, ephemeral kind 범위(`20000`-`20999`)는 릴레이가 이를 무기한 저장하지 말아야 함을 시사합니다. `p` 태그는 content 복호화 없이도 관련 이벤트를 필터링하게 합니다.

- **[NIP-5C](/ko/topics/nip-5c/) (Scrolls): WASM programs update** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): WebAssembly 프로그램 게시와 실행 명세 개발을 계속 이어갑니다. 이 명세는 WASM binary를 Nostr 이벤트로 게시하고 발견하기 위한 규약을 정의합니다. Scroll은 클라이언트가 relay에서 내려받아 sandboxed runtime에서 실행할 수 있는 self-contained 프로그램으로, Nostr를 실행 가능한 코드의 배포 네트워크로 바꿉니다. 이 PR은 이벤트 형식과 runtime interface를 다듬습니다. [데모 앱](https://nprogram.netlify.app/)은 브라우저 안에서 실행되는 scroll을 보여 주며, 어떤 클라이언트든 가져와 실행할 수 있는 예제 프로그램이 Nostr 이벤트로 게시돼 있습니다. 이 개념은 [NIP-5A](/ko/topics/nip-5a/)가 HTML 페이지를 제공하는 데서 더 나아가, 같은 relay 인프라를 통해 상호작용 프로그램까지 배포하려는 것입니다.

- **[NIP-44](/ko/topics/nip-44/) large payload support** ([PR #1907](https://github.com/nostr-protocol/nips/pull/1907)): 현재 65,535바이트 제한보다 더 큰 payload를 다룰 수 있도록 [NIP-44](/ko/topics/nip-44/) versioned encryption을 확장하는 제안입니다. 이 변경은 하위 호환적입니다. 큰 메시지가 필요 없는 구현체는 이를 완전히 무시해도 됩니다. 실제 동기는 [NIP-46](/ko/topics/nip-46/) 원격 서명에서 큰 kind `3` contact list를 다뤄야 하는 경우입니다. 사용자의 follow list는 JSON 직렬화 시 암호화 크기 한도를 넘길 수 있으므로, 이 변경이 없으면 remote signer는 큰 contact list 응답을 암호화할 수 없고 우회책이나 잘라내기가 필요해집니다.

- **[NIP-C7](/ko/topics/nip-c7/): Restrict kind 9 to chat views** ([PR #2310](https://github.com/nostr-protocol/nips/pull/2310)): [NIP-C7](/ko/topics/nip-c7/)는 kind `9`를 경량 채팅 메시지로 정의합니다. 이는 [NIP-29](/ko/topics/nip-29/) 그룹 채팅이나 [NIP-53](/ko/topics/nip-53/) 라이브 액티비티 스트림 같은 채팅 맥락의 실시간 대화를 위한 짧은 텍스트 노트입니다. 이 PR은 클라이언트가 순서 있는 이벤트 흐름을 "chat view"로 렌더링할 때 kind `9` 이벤트만 가져와야 한다는 요구를 추가합니다. 이렇게 하면 kind `1` 노트나 kind `30023` article 같은 다른 콘텐츠가 채팅 타임라인에 섞여 들어가 문맥이 깨지는 일을 막습니다. 다른 콘텐츠는 여전히 [NIP-18](/ko/topics/nip-18/) repost 규약에 따라 kind `9` 메시지 안에서 인용할 수 있습니다. 동기는 일반 피드에 kind `9` 메시지가 나타나면 문맥 없이 짧은 답변 조각처럼 보인다는 커뮤니티 논의입니다.

## NIP Deep Dive: NIP-29 (Relay-based Groups)

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)은 릴레이 자체가 그룹 멤버십과 moderation을 관리하는 그룹 메시징 모델을 정의합니다. 그룹은 특정 릴레이 위에 존재하며 임의 문자열 ID로 식별되고, 누가 그룹에 쓸 수 있는지는 릴레이가 강제합니다. 이는 [Marmot](/ko/topics/marmot/)의 client-side MLS 암호화나 [NIP-17](/ko/topics/nip-17/) 그룹 채팅의 gift-wrapped DM 아키텍처와는 다릅니다. NIP-29에서는 릴레이가 권한 주체이고, 메시지는 릴레이 운영자가 읽을 수 있으며, moderation도 릴레이 수준에서 이뤄집니다.

그룹은 `<host>'<group-id>` 형식으로 식별됩니다. 예를 들어 `groups.nostr.com'abcdef`입니다. 특수 그룹 ID `_`는 릴레이 전체 토론용 최상위 그룹으로 예약되어 있습니다. 그룹에 보내는 모든 사용자 이벤트는 그룹 ID를 담은 `h` 태그를 가집니다:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744675200,
  "kind": 9,
  "tags": [
    ["h", "abcdef"],
    ["previous", "a1b2c3d4", "e5f67890", "12345678"]
  ],
  "content": "Has anyone tested the new relay config?",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

`previous` 태그는 tamper-detection 메커니즘입니다. 클라이언트는 같은 릴레이에서 최근 50개 메시지 안에서 본 이벤트의 처음 8개 hex 문자(4바이트)를 포함합니다. 릴레이는 데이터베이스에 없는 이벤트를 가리키는 `previous` 참조가 들어간 이벤트를 거부하므로, 그룹이 다른 릴레이 포크로 문맥 없이 재브로드캐스트되는 일을 감지할 수 있습니다. 완전한 chain of custody는 아니지만, 맥락 밖 재유포를 눈에 띄게 만듭니다.

그룹 멤버십은 `9000`-`9020` 범위의 moderation event kind로 관리됩니다. 사용자는 kind `9021` 가입 요청을 게시해 그룹에 들어가며, 릴레이는 정책에 따라 이를 수락하거나 거부합니다:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "f1a2b3c4d5e6f7890123456789abcdef0123456789abcdef1234567890abcdef",
  "created_at": 1744675200,
  "kind": 9021,
  "tags": [
    ["h", "abcdef"],
    ["code", "invite-xyz-123"]
  ],
  "content": "I'd like to join the dev discussion group.",
  "sig": "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff"
}
```

선택적인 `code` 태그는 관리자가 kind `9009` 이벤트로 만든 invite code와 연결됩니다. 사용자가 떠날 때는 kind `9022`를 게시하고, 릴레이는 자동으로 kind `9001` removal을 발행합니다. 관리자는 역할이 포함된 사용자 추가(kind `9000`), 사용자 제거(kind `9001`), 그룹 메타데이터 편집(kind `9002`), 이벤트 삭제(kind `9005`)를 할 수 있습니다. 역할 시스템은 유연합니다. 역할은 임의 레이블이며, 각 역할의 권한은 프로토콜이 아니라 릴레이 정책이 정합니다. 릴레이는 그룹 설정을 addressable event로 게시합니다. 메타데이터용 kind `39000`, admin 목록용 kind `39001`, member 목록용 kind `39002`, 역할과 capability용 kind `39003`입니다.

그룹은 public(누구나 읽고 멤버만 쓰기), closed(멤버만 읽고 쓰기), fully open 상태를 가질 수 있습니다. 가시성과 쓰기 접근 설정은 kind `9002` 메타데이터 편집 이벤트의 `public`, `open`, `visible`, `unrestricted` 플래그로 직교적으로 제어됩니다. 하나의 릴레이는 멤버십과 moderation이 서로 독립적인 여러 그룹을 동시에 호스팅할 수 있습니다.

이 명세는 채팅 메시지만이 아니라 그룹 안의 어떤 event kind도 허용합니다. 장문 글([NIP-23](/ko/topics/nip-23/)), 캘린더 이벤트([NIP-52](/ko/topics/nip-52/)), 라이브 스트림([NIP-53](/ko/topics/nip-53/)), 마켓 listing까지 모두 `h` 태그를 달고 그룹 맥락에 참여할 수 있습니다. 그래서 NIP-29 그룹은 서로 다른 콘텐츠 타입이 같은 namespace 안에 공존하는 Discord 서버나 Slack workspace처럼 동작합니다.

[Flotilla](https://gitea.coracle.social/coracle/flotilla)는 가장 활발히 개발되는 NIP-29 클라이언트이며, [v1.7.0](/en/newsletters/2026-04-01-newsletter/)에서 voice room, email login, proof-of-work DM을 추가했습니다. [Coracle](https://github.com/coracle-social/coracle)도 NIP-29 그룹을 지원합니다. 릴레이 측에서는 [groups.fiatjaf.com](https://github.com/fiatjaf/relay29)이 fiatjaf의 참조 구현입니다. [OpenSats](/en/newsletters/2026-04-08-newsletter/)의 지원을 받은 Kotlin Multiplatform NIP-29 클라이언트 [Nostrord](https://github.com/Nostrord/nostrord)는 Discord 스타일 moderation과 threading을 갖춘 초기 개발 단계에 있습니다.

[Marmot](/ko/topics/marmot/) 같은 암호화 대안과 비교한 tradeoff는 분명합니다. NIP-29 그룹은 릴레이 운영자가 읽을 수 있습니다. end-to-end encryption도, forward secrecy도, post-compromise security도 없습니다. 콘텐츠 무결성과 멤버십 강제는 릴레이가 신뢰 당사자입니다. 그 대가로 단순함을 얻습니다. 관리할 key material도 없고, 장치 간 state sync도 없고, MLS handshake 협상도 없습니다. 릴레이 운영자가 그룹을 띄우고, 사용자가 참여하며, 메시지가 흐릅니다. 공개 커뮤니티, 개발 채널, 열려 있는 토론 공간에는 이 릴레이 신뢰 모델이 용도와 맞습니다. 릴레이가 콘텐츠를 읽지 못해야 하는 private messaging에는 NIP-17이나 Marmot이 더 적절합니다.

## NIP Deep Dive: NIP-90 (Data Vending Machines)

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)은 Nostr 위의 온디맨드 계산 프로토콜을 정의합니다. 고객이 작업 요청을 게시하면, 서비스 제공자가 이를 수행하기 위해 경쟁하고, 결과는 Nostr 이벤트로 전달됩니다. 명세는 이를 "money in, data out"이라고 설명하며, 고객이 누가 결과를 만들었는지보다 어떤 결과가 나왔는지에 관심을 갖는 데이터 처리 시장으로 Nostr를 다룹니다.

이 프로토콜은 작업 요청용 kinds `5000`-`5999`, 결과용 `6000`-`6999`, 피드백용 kind `7000`을 예약합니다. 결과 kind는 항상 요청 kind보다 1000 큽니다. kind `5001` 요청은 kind `6001` 결과를 만듭니다. 다음은 텍스트 요약을 요청하는 예시입니다:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744675200,
  "kind": 5001,
  "tags": [
    ["i", "https://example.com/article.txt", "url"],
    ["output", "text/plain"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol"],
    ["bid", "5000"],
    ["param", "lang", "en"],
    ["param", "max_tokens", "280"]
  ],
  "content": "",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

`i` 태그는 타입 마커와 함께 입력 데이터를 지정합니다. 정의된 입력 타입은 네 가지입니다. `url`(이 URL에서 데이터를 가져와 처리), `event`(Nostr 이벤트를 입력으로 사용), `job`(이전 작업의 출력에 이어서 처리), `text`(인라인 텍스트)입니다. `bid` 태그는 millisats 단위 최대 지불 금액을 설정합니다. `param` 태그는 작업 종류별 파라미터를 담고, `output` 태그는 기대하는 응답 형식을 지정합니다.

서비스 제공자는 이 요청을 받아 결과를 게시합니다:

```json
{
  "id": "d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744675260,
  "kind": 6001,
  "tags": [
    ["request", "{\"id\":\"c3d4e5...\",\"kind\":5001,...}"],
    ["e", "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2", "wss://relay.damus.io"],
    ["i", "https://example.com/article.txt", "url"],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["amount", "5000", "lnbc50n1pj..."]
  ],
  "content": "The article discusses three protocol changes proposed for the next quarter...",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

결과는 원본 요청 이벤트를 태그하고, 입력을 참조용으로 포함하며, 고객 pubkey를 지정하고, 선택적으로 `amount` 태그에 Lightning invoice를 넣을 수 있습니다. 고객은 pubkey를 확인해 결과가 특정 서비스 제공자에게서 왔는지 검증할 수 있습니다.

작업 피드백(kind `7000`)은 작업이 진행되는 동안 상태 업데이트를 제공합니다. 서비스 제공자는 `payment-required`, `processing`, `error`, `success` 같은 상태 값을 가진 피드백 이벤트를 발행할 수 있습니다. 덕분에 고객은 오래 걸리는 작업의 진행 상태를 실시간으로 볼 수 있습니다:

```json
{
  "id": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744675230,
  "kind": 7000,
  "tags": [
    ["status", "payment-required"],
    ["e", "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2", "wss://relay.damus.io"],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["amount", "5000", "lnbc50n1pj..."]
  ],
  "content": "",
  "sig": "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff"
}
```

작업 체이닝도 가능합니다. 고객은 입력 타입을 `job`으로 두고 이전 작업의 event ID를 참조할 수 있습니다. 하위 작업을 맡은 서비스 제공자는 상위 작업 결과를 기다린 뒤 이를 처리합니다. 이렇게 하면 오디오 전사(kind `5002`), 전사 요약(kind `5001`), 요약 번역(kind `5003`) 같은 조합 가능한 파이프라인을 만들 수 있습니다. 각 단계는 서로 다른 서비스 제공자가 맡을 수 있습니다.

프라이버시를 위해 고객은 서비스 제공자의 pubkey로 [NIP-04](/ko/topics/nip-04/) 암호화를 사용해 `i`와 `param` 태그를 암호화할 수 있습니다. 이 경우 암호문은 `content` 필드에 들어가고 `encrypted` 태그가 추가됩니다. 이렇게 하면 릴레이와 다른 서비스 제공자는 입력 데이터와 파라미터를 볼 수 없지만, 고객은 미리 특정 제공자를 선택해야 합니다.

구체적인 작업 요청 타입은 [별도 저장소](https://github.com/nostr-protocol/data-vending-machines/tree/master/kinds)에 정의되어 있습니다. 현재는 text generation(kind `5050`), summarization(kind `5001`), translation(kind `5002`), speech-to-text(kind `5003`), image generation(kind `5100`), content recommendation(kind `5300`) 등이 있습니다.

[Snort](https://github.com/v0l/snort)는 [뉴스레터 #17](/en/newsletters/2026-04-08-newsletter/)에서 다룬 kind `7000` payment-required invoice 표시를 추가해, DVM이 결제 요구로 응답할 때 feed 안에 Lightning invoice를 직접 렌더링합니다. [noStrudel](https://github.com/hzrd149/nostrudel)에는 사용 가능한 서비스 제공자를 둘러보는 DVM explorer가 있습니다. 제공자 쪽에서는 [DVMDash](https://github.com/dtdannen/dvmdash) 같은 프로젝트가 네트워크 전반의 DVM 활동을 추적하고, 여러 AI 중심 서비스가 NIP-90 프로토콜을 통해 text generation, image creation, content moderation을 제공합니다. [NIP-89](/ko/topics/nip-89/) (Recommended Application Handlers)는 서비스 제공자가 자신의 capability를 발견 가능한 Nostr 이벤트로 게시할 수 있게 해 NIP-90을 보완합니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 전할 소식이 있다면 Nostr에서 DM을 보내거나 [nostrcompass.org](https://nostrcompass.org)에서 찾아 주세요.
