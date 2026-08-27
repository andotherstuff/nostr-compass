---
title: "Nostr Compass #30"
date: 2026-07-08
publishDate: 2026-07-08
translationOf: /en/newsletters/2026-07-08-newsletter.md
translationDate: 2026-08-27
draft: false
type: newsletters
description: "Marmot 명세가 채택 상태로 바뀌고 MDK가 MarmotKit 바인딩과 암호화 그룹 아바타를 담은 v0.9.0~v0.9.3을 출시했습니다. Mostro는 NIP-44 기반 Transport v2를, Bitchat은 NIP-13 작업증명과 mesh-to-Nostr gateway를, rust-nostr는 gift wrap 및 비공개 DM builder용 NIP-40 만료 기능을 추가했습니다."
---

주간 Nostr 가이드 Nostr Compass에 다시 오신 것을 환영합니다.

**이번 주:** [Marmot 명세가 채택 상태로 전환](#marmot-marks-the-spec-adopted-and-mdk-cuts-v09x)되어 42개 파일이 갱신됐고, MDK는 암호화 그룹 아바타, 외부 signer 지원, MarmotKit iOS·Android 바인딩을 담은 v0.9.0~v0.9.3을 내놓았습니다. [Mostro는 Transport v2를 출시](#mostro-v0180-and-mobile-v130-ship-transport-v2-on-nip-44)해 mostrod v0.18.0과 Mobile v1.3.0에서 스팸 방지 gate와 마이그레이션 공존 기간을 갖춘 NIP-44 DM을 지원합니다. [Bitchat 1.6.0은 NIP-13 작업증명](#bitchat-160-adds-nip-13-proof-of-work-and-an-opt-in-mesh-to-nostr-gateway), 한 대의 온라인 휴대폰으로 군중 전체를 연결하는 선택형 mesh-to-Nostr gateway, prekey bundle, 전이적 검증, 생성자 관리형 암호화 비공개 그룹을 추가했습니다. [Amber](#amber-v623-scopes-profile-subscriptions-and-adds-a-tor-status-notification)는 계정별 profile subscription과 NIP-65 우선 조회, 재시작 동작이 있는 실시간 Tor 상태 알림을 제공합니다. rust-nostr에는 gift wrap과 비공개 DM builder의 NIP-40 만료가, Amethyst에는 Negentropy sync 강화와 NIP-50 검색이 들어갔습니다.

빠른 이동: [rust-nostr](#rust-nostr-adds-nip-40-expiration-to-gift-wrap-and-private-dm-builders), [Amethyst](#amethyst-spends-the-week-hardening-negentropy-sync-and-adding-nip-50-search), [Nostrord](#nostrord-v200-and-v210-fold-the-relay-pool-and-heal-zombie-websockets), [Ngit](#ngit-v262-stops-duplicate-pr-status-events-on-default-branch-push), [Jumble](#jumble-v2671-makes-blossom-the-default-upload-service-in-a-dm-focused-cut), [Applesauce](#applesauce-signers-622-drops-an-nbunksec-dependency), [Bray](#bray-v1330-cli-picks-up-a-bunker-profile-persona-and-tor-outbound), [Deepmarks](#deepmarks-100-hardens-the-nostr-bookmarking-surface), [Bitcredit](#bitcredit-core-v0513-unencrypts-block-metadata-on-the-nostr-wire), [Coop Mobile](#coop-mobile-v023-and-v024), [Granary](#granary-v110-adds-nip-71-video-event-support), [nostr-relay](#nostr-relay-v00244-adds-a-firestore-backend), [Manent](#manent-v140-fixes-nip-42-auth-and-adds-media-clipboard-flows), [Routstrd](#routstrd-v037-makes-the-nostr-event-store-the-persistent-source-of-truth), [Nymchat](#nymchat-101-launches-as-a-progressive-web-app-on-nip-17), [21Meetup](#21meetup-110-launches-nostr-signed-attendance-badges), [SafeBox](#safebox-publishes-a-phase-3-progress-report-and-a-freebsd-jail-runbook), [NIP-51/37](#merged-nip-51-and-nip-37-align-the-kind-10013-name), [NIP-AD](#open-nip-ad-nostr-web-addresses-via-well-known-lookup), [NIP-86 claim](#open-nip-86-claim-management-for-invite-codes), [role color](#open-role-color-as-h-s-l-tuple), [NIP-80](#open-nip-80-hardware-attested-media-provenance), [NIP-01 pagination](#open-nip-01-pagination-hardening), [NIP-13 심층 분석](#nip-deep-dive-nip-13-proof-of-work), [NIP-40 심층 분석](#nip-deep-dive-nip-40-expiration-timestamp).

---

## 주요 소식

### Marmot, 명세를 채택 상태로 전환하고 MDK v0.9.x 출시

[Marmot protocol 저장소](https://github.com/marmot-protocol/marmot)는 7월 3일 [PR #170](https://github.com/marmot-protocol/marmot/pull/170)을 병합해 42개 파일의 `Status: draft for internal review` 및 `experimental draft`를 `Status: adopted`로 바꿨습니다. README 제목은 작업 중인 저장소라는 표현에서 채택된 “Marmot Protocol”로 바뀌었고, MIP 시대 문서는 폐기된 구버전으로 재정리됐습니다. “Review Status”는 현행 명세 편집을 위한 “Review Guidance”가 됐으며, 전반의 `v2` 표현도 “this spec”과 “under this spec”으로 바뀌었습니다. 비규범 문서인 `implementation-model.md`와 multi-device 기능 문서만 의도대로 draft 상태를 유지합니다.

같은 저장소의 [PR #171](https://github.com/marmot-protocol/marmot/pull/171)은 admin policy, membership, role change의 불변조건을 정렬했습니다. Remove가 admin을 하나도 남기지 않는 상태를 만들 수 없다는 cross-component 검사는 모든 결과 epoch의 속성으로 명시됐고, admin-policy update가 없는 commit은 이전 epoch의 admin 집합을 기준으로 평가합니다. Convergence의 후보 branch에서 “validates”는 이제 결과 epoch의 cross-component 검사까지 포함한 전체 commit 유효성을 뜻합니다. 대체된 commit에서 나온 상태 알림은 branch 선택이 바뀔 때 반드시 철회되어, 패배한 rename이 성공한 system message처럼 보이던 문제를 명세 수준에서 막습니다. `member-departure.md`의 새 “Realizing removal” 절은 마지막 leaf를 제거한 canonical commit을 기본 입력으로 삼고, 해당 commit을 적용하지 못한 client를 위한 fallback도 규정합니다.

하위 프로젝트인 [MDK workspace](https://github.com/marmot-protocol/mdk)는 7월 6일 [v0.9.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.0)을 출시한 뒤 이틀 동안 [v0.9.1](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.1), [v0.9.2](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.2), [v0.9.3](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.3)을 잇달아 내놓았습니다. v0.9.0은 새 SQLite database 생성 시 오래된 keyring entry를 교체하고 storage layer 전체에 mutate 전 검증 원칙을 적용합니다. v0.9.1의 [PR #732](https://github.com/marmot-protocol/mdk/pull/732)는 모든 outbound connection을 하나의 host-safety dial 관문으로 통과시켜 call site별 검증 차이를 없앴습니다. v0.9.3의 [PR #771](https://github.com/marmot-protocol/mdk/pull/771)은 `download_group_image`와 `image_hash_hex`를 통해 암호화 그룹 아바타를 uniffi binding에 노출합니다. 외부 signer와 MarmotKit의 iOS·Android binding도 이 릴리스 흐름에 포함됐습니다.

후속 변경으로 [Marmot PR #236](https://github.com/marmot-protocol/marmot/pull/236)과 [MDK PR #781](https://github.com/marmot-protocol/mdk/pull/781)도 반영됐습니다.

### Mostro v0.18.0과 Mobile v1.3.0, NIP-44 기반 Transport v2 출시

Mostro는 Nostr event 위에서 order book, escrow, dispute resolution을 운영하는 peer-to-peer Bitcoin 거래 protocol이며, client는 암호화 DM으로 daemon인 `mostrod`와 통신합니다. [Mostro v0.18.0](https://github.com/MostroP2P/mostro/releases/tag/v0.18.0)은 기존 Transport v1에서 Transport v2로 옮겨 [NIP-44](/ko/topics/nip-44/) DM, server-side dual receive, 스팸 방지 gate를 도입했습니다. [PR #776](https://github.com/MostroP2P/mostro/pull/776)은 Phase 1 wire 변경, [PR #780](https://github.com/MostroP2P/mostro/pull/780)은 protocol v2의 Phase 2 anti-spam gate, [PR #785](https://github.com/MostroP2P/mostro/pull/785)은 활성 transport에 inner protocol version을 맞춰 v1과 v2 client가 공존하게 하는 변경입니다. [PR #782](https://github.com/MostroP2P/mostro/pull/782)은 NIP-33 info tag 이름도 바로잡았습니다.

전환 과정의 추가 수정은 [PR #783](https://github.com/MostroP2P/mostro/pull/783), [PR #778](https://github.com/MostroP2P/mostro/pull/778), [PR #779](https://github.com/MostroP2P/mostro/pull/779)에 담겼습니다.

[Mostro Mobile v1.3.0](https://github.com/MostroP2P/mobile/releases/tag/v1.3.0)은 client 쪽 마이그레이션입니다. [PR #613](https://github.com/MostroP2P/mobile/pull/613)은 Riverpod 3.x로 옮겼고, Phase A [PR #620](https://github.com/MostroP2P/mobile/pull/620)은 main isolate와 background isolate에 NIP-44 DM dual receive를, Phase B [PR #624](https://github.com/MostroP2P/mobile/pull/624)은 dual send를 추가했습니다. [PR #632](https://github.com/MostroP2P/mobile/pull/632)은 Riverpod 전환 뒤 dual send를 다시 적용했고 Phase C [PR #637](https://github.com/MostroP2P/mobile/pull/637)이 마이그레이션을 마무리했습니다. [PR #625](https://github.com/MostroP2P/mobile/pull/625)은 Malawi Kwacha 결제 수단을, [PR #627](https://github.com/MostroP2P/mobile/pull/627)은 KES, MZN, TZS 등 아프리카 통화 결제 수단을 추가했습니다.

### Bitchat 1.6.0, NIP-13 작업증명과 선택형 mesh-to-Nostr gateway 추가

[Bitchat 1.6.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.6.0)은 geohash channel과 DM handoff에 Nostr를 쓰는 Bluetooth mesh chat 앱입니다. [PR #1382](https://github.com/permissionlesstech/bitchat/pull/1382)는 outbound geohash channel message(kind 20000 ephemeral event)에 [NIP-13 작업증명](/ko/topics/nip-13/)을 추가합니다. 전송할 때마다 `["nonce", "<value>", "<target>"]` tag를 채굴하며 목표는 선행 0 bit 8개로, 평균 256회 hash 시도이고 M-series Mac에서 1ms 미만입니다. 검증된 PoW가 있는 inbound event는 sender별 수신 rate limit이 완화됩니다. PoW는 kind 20000에만 적용되고 presence heartbeat(kind 20001), kind-1 위치 note, DM에는 적용되지 않습니다.

[PR #1384](https://github.com/permissionlesstech/bitchat/pull/1384)는 geohash channel용 선택형 mesh-to-Nostr uplink인 gateway mode를 추가합니다. 인터넷이나 relay 연결이 없는 사용자가 보내고 mesh peer가 `.gateway` capability를 광고하면, 서명된 kind 20000 event를 새 `MessageType.nostrCarrier = 0x28` TLV envelope에 싸서 gateway 하나로 보냅니다. gateway peer는 sender 대신 Nostr에 게시하고 inbound channel traffic을 기본 TTL로 mesh에 재방송합니다. uplink는 directed multi-hop courier envelope, downlink는 broadcast를 이용합니다. sender가 event에 미리 서명하므로 gateway는 게시 여부만 결정할 뿐 저자를 위조할 수 없습니다. 재난이나 시위 현장에서 연결된 휴대폰 한 대만으로 전체 geohash channel에 Nostr uplink를 제공하려는 설계입니다.

같은 릴리스의 [PR #1381](https://github.com/permissionlesstech/bitchat/pull/1381)은 courier mail 경로에 prekey bundle을 추가해, live Noise handshake 없이 offline peer에게 forward-secret 첫 메시지를 보낼 수 있게 합니다. [PR #1380](https://github.com/permissionlesstech/bitchat/pull/1380)은 이미 검증한 사람이 Noise handshake를 마친 peer를 보증하는 전이적 검증을 추가합니다. [PR #1383](https://github.com/permissionlesstech/bitchat/pull/1383)은 생성자 관리형 암호화 비공개 mesh group을, [PR #1376](https://github.com/permissionlesstech/bitchat/pull/1376)은 `/pay` command로 Cashu ecash token을 감지·표시·상환하는 기능을 추가했습니다.

[PR #1379](https://github.com/permissionlesstech/bitchat/pull/1379), [PR #1372](https://github.com/permissionlesstech/bitchat/pull/1372), [v1.5.4](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.4), [PR #1367](https://github.com/permissionlesstech/bitchat/pull/1367)의 기반 작업도 이번 릴리스에 이어졌습니다.

---

## 태그 릴리스

### Amber v6.2.3, profile subscription 범위 조정과 Tor 상태 알림

[Amber v6.2.3](https://github.com/greenart7c3/Amber/releases/tag/v6.2.3)은 Android [NIP-46](/ko/topics/nip-46/) signer의 성능과 정확성을 다듬은 릴리스입니다. [PR #492](https://github.com/greenart7c3/Amber/pull/492)은 “never”와 “always”를 포함한 profile fetch interval 설정을 추가했습니다. 계정 전환 bottom sheet에 profile image를 표시하고, profile subscription을 현재 계정으로 제한해 여러 계정을 보관한 signer가 사용하지 않는 계정까지 subscription하지 않게 했습니다. Bunker permission parsing 실패에는 명시적 오류 처리가 생겼고, main-thread keystore 및 disk read 등 StrictMode 위반도 수정됐습니다. profile metadata보다 NIP-65 relay list를 먼저 가져오며, 재시작 action이 포함된 실시간 Tor 상태 알림도 제공합니다.

해당 변경은 [PR #493](https://github.com/greenart7c3/Amber/pull/493), [PR #494](https://github.com/greenart7c3/Amber/pull/494), [PR #495](https://github.com/greenart7c3/Amber/pull/495)에서도 확인할 수 있습니다.

### Jumble v26.7.1, DM 중심 릴리스에서 Blossom을 기본 upload service로 지정

[Jumble v26.7.1](https://github.com/CodyTseng/jumble/releases/tag/v26.7.1)은 DM과 media에 초점을 둔 Nostr web client 릴리스입니다. media upload 설정을 새로 설계하고 [Blossom](/ko/topics/blossom/)을 기존 NIP-96 대신 기본 service로 삼았습니다. mobile message menu, desktop action 개선, “최신으로 이동” button, DM media long-press reaction, 실패한 outbound DM 재시도를 추가했습니다. invoice와 embed의 bubble 크기, DM scroll·정렬, emoji 삽입·복사·drag 문제를 고쳤고 upload 중 metadata 제거 시 image orientation도 보존합니다. Linux ARM64 download도 추가됐습니다.

### Applesauce signers 6.2.2, nbunksec 의존성 제거

[applesauce-signers@6.2.2](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%406.2.2)는 [commit d654349](https://github.com/hzrd149/applesauce/commit/d654349)에서 `@sandwichfarm/encoded-entities` 의존성을 내장 [nbunksec](/ko/topics/nip-46/) helper로 대체했습니다. 지난주 추가된 Applesauce [NIP-46](/ko/topics/nip-46/) bunker session encoding이 외부 encoding library 없이 동작해 downstream client의 supply-chain 노출 면적을 줄입니다.

### Ngit v2.6.2, default branch push의 중복 PR 상태 event 중단

[Ngit v2.6.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.2)는 git-over-Nostr CLI의 버그 수정 릴리스입니다. default branch로 `git push`할 때 이미 applied 상태인 PR의 merge/applied event를 중복 게시하지 않습니다. merge 감지가 git 내부 heuristic 대신 push 전 Nostr repo state, 즉 [NIP-34](/ko/topics/nip-34/) workflow의 source of truth를 읽도록 바뀌어 kind-1621 상태 event 중복을 막았습니다.

### Bray v1.33.0 CLI, bunker profile·persona·Tor outbound 추가

[Bray v1.33.0](https://github.com/forgesworn/bray/releases/tag/v1.33.0)은 Nostr SDK 겸 CLI 릴리스입니다. `bunker --profile <name>`은 안정적인 connection key와 relay fallback을, `bunker --persona <name>`은 nsec-tree 파생 identity로 여러 pubkey를 대신 서명하는 기능을 제공합니다. 설정 시 모든 HTTP fetch를 Tor SOCKS proxy로 보낼 수 있습니다. [NIP-47](/ko/topics/nip-47/) NWC wallet command, [NIP-29](/ko/topics/nip-29/) group admin write, NIP-86 admin verb, [NIP-65](/ko/topics/nip-65/) outbox helper도 추가됐습니다. `--jsonl`, `--csv`, `--tsv`, generic NIP-01 `req`, 임의 event 생성, `publish-raw`, 일회성 NIP-46 `bunker sign`도 지원합니다.

### Deepmarks 1.0.0, Nostr bookmark 보안 강화

[Deepmarks 1.0.0](https://github.com/ostermayer/deepmarks-public/releases/tag/v1.0.0)은 공개 Nostr bookmark service의 보안 강화 milestone입니다. bracket가 붙은 IPv6 literal을 public으로 잘못 분류해 `[::1]`, `[fd00::1]`, IPv4-mapped 주소가 내부 target에 닿던 중대한 SSRF 우회를 고쳤습니다. 이제 bracket를 제거하고 IPv4-mapped·compatible IPv6를 embedded v4로 접은 뒤 private range를 검사합니다. 외부 relay에서 들어온 `kind:0` profile은 sink에서 signature를 검증해 악성 relay의 `nip05`·`lud16` 위조를 막고 bookmark URL scheme도 제한합니다.

### Bitcredit Core v0.5.13, Nostr wire의 block metadata 비암호화

[Bitcredit Core v0.5.13](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.13)은 credit-bill protocol의 공개 Nostr event에서 block metadata 암호화 layer를 제거합니다. block id, hash, signature는 평문이고 block data만 bill key로 암호화됩니다. 새 앱은 이전 chain을 처리하지만 이전 앱은 새 chain을 처리하지 못합니다. bill chain fetch 함수와 optimistic relay threshold 게시도 추가돼, 기본 한 relay가 수락하면 나머지 relay 전송은 비동기로 진행됩니다.

### Coop Mobile v0.2.3과 v0.2.4

[Coop Mobile](https://git.reya.su/reya/coop-mobile)은 7월 4일 [v0.2.3](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.3), 7월 7일 [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4)를 출시했습니다. Android [NIP-17](/ko/topics/nip-17/) DM client인 이 앱은 v0.2.3에서 inline image·link, image attachment, speech-to-text, contact 삭제 확인을 추가했습니다. v0.2.4는 멈춘 indicator를 고치고 Nostr Connect handshake를 개선했으며, 새 identity import 화면과 [NIP-49](/ko/topics/nip-49/) 암호화 private key 형식 `ncryptsec1` import를 추가했습니다.

### Granary v11.0, NIP-71 video event 지원

[Granary v11.0](https://github.com/snarfed/granary/releases/tag/v11.0)은 Bridgy Fed의 cross-network bridge를 구동하는 multi-protocol 변환 library입니다. [NIP-71](/ko/topics/nip-71/) video event(kind 21, 22, 34235, 34236)를 video attachment가 있는 ActivityStreams 1 note로 변환하며 `imeta` thumbnail, duration, `published_at`, fallback `displayName`용 `alt`를 추출합니다. API의 `sign`은 `hash_and_sign`으로 바뀌고 `verify` 실패와 잘못된 relay URL은 `ValueError`를 냅니다. private key가 없으면 `Nostr.query`가 [NIP-42](/ko/topics/nip-42/) AUTH challenge를 안전하게 건너뜁니다.

### Nostr-relay v0.0.244, Firestore backend 추가

[mattn/nostr-relay v0.0.244](https://github.com/mattn/nostr-relay/releases/tag/v0.0.244)는 [PR #12](https://github.com/mattn/nostr-relay/pull/12)로 Go relay storage layer에 Google Cloud Firestore backend를 추가해 운영자에게 managed serverless database 선택지를 제공합니다.

### Manent v1.4.0, NIP-42 AUTH 수정과 media clipboard flow 추가

[Manent v1.4.0](https://github.com/dtonon/manent/releases/tag/v1.4.0)은 [NIP-44](/ko/topics/nip-44/) 암호화, [NIP-46](/ko/topics/nip-46/)·[NIP-55](/ko/topics/nip-55/) signer, [NIP-65](/ko/topics/nip-65/) outbox, Blossom storage를 쓰는 암호화 note·file 앱입니다. 깨져 있던 [NIP-42](/ko/topics/nip-42/) relay 인증, `http://` Blossom upload, compression flow를 고쳤습니다. clipboard image 복사·붙여넣기, drag and drop, crop·rotate, video·GIF 재생, camera icon long press 동영상 촬영을 지원하며 Linux primary clipboard와 note loading·scroll도 개선했습니다.

### Routstrd v0.3.7, Nostr event store를 영속적 source of truth로 전환

[Routstrd v0.3.7](https://github.com/routstr/routstrd/releases/tag/v0.3.7)은 kind 38421 provider discovery와 kind 38425 LGTM review로 LLM request를 routing하는 분산 AI inference network의 local daemon입니다. `routstrd update`가 routstrd와 cocod binary를 받아 daemon을 정상 재시작하고, 시작 시와 21분마다 `refreshNostrEvents()`를 호출합니다. `@routstr/sdk` 0.3.15는 ProviderRegistry 대신 `DiscoveryAdapter`를 직접 쓰고 사라진 provider model을 정리하며 잘못된 210분 TTL을 없애 Nostr event store를 영속적 source of truth로 취급합니다. Xcashu refund 경로도 강화됐습니다.

이 daemon이 사용하는 메시지 기반은 [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md)와 [NIP-30](/ko/topics/nip-30/)의 관련 동작도 포함합니다.

### Nymchat 1.0.1, NIP-17 기반 Progressive Web App 출시

[Nymchat 1.0.1](https://github.com/Spl0itable/NYM)은 Nostr Ynstant Messenger라고도 불리는 PWA 및 iOS·Android messenger로 Bitchat과 bridge됩니다. geohash channel은 kind 20000, named channel은 kind 23333을 쓰며 private message와 group chat은 회전하는 ephemeral recipient key 및 compromise 후 자동 복구가 있는 [NIP-17](/ko/topics/nip-17/) gift wrap(kind 1059)을 이용합니다. 등록 없는 session keypair 또는 [NIP-07](/ko/topics/nip-07/), [NIP-46](/ko/topics/nip-46/), nsec으로 로그인할 수 있습니다. WebAuthn PRF나 PBKDF2를 사용한 password·PIN·passkey·biometric local identity 암호화도 선택할 수 있고, voice·video call signaling도 NIP-17로 전달합니다.

### 21Meetup 1.1.0, Nostr 서명 출석 badge 출시

[21Meetup 1.1.0](https://github.com/louisthecat86/Einundzwanzig-Meetup-App)은 독일 Einundzwanzig Bitcoin community의 Flutter 앱으로 NFC tag와 10초마다 바뀌는 QR code로 meetup 출석을 기록합니다. 각 badge는 organizer가 BIP-340 Schnorr로 서명한 kind 21000 Nostr event입니다. 참가자는 특정 block height의 meetup 출석을 증명하는 event를 모으며, local trust score를 P2P 거래에서 QR로 제시할 수 있습니다.

### Nostrord v2.0.0과 v2.1.0, relay pool 통합과 zombie WebSocket 복구

[Nostrord v2.0.0](https://github.com/nostrord/nostrord/releases/tag/v2.0.0)은 NIP-29, NIP-42, NIP-44, NIP-46, NIP-57, NIP-65, NIP-98을 지원하는 KMP/WASM client의 큰 릴리스입니다. 다음 날 [v2.0.1](https://github.com/nostrord/nostrord/releases/tag/v2.0.1)이 [PR #166](https://github.com/nostrord/nostrord/pull/166)으로 desktop 시작 crash를 고쳤습니다. jlink image에 SQLDelight가 요구하는 `java.sql` module이 없어 `NoClassDefFoundError`가 났던 문제입니다. 같은 PR은 optimistic send가 cache에만 남지 않고 relay로 가도록 network layer를 통과시켰습니다.

[v2.1.0](https://github.com/nostrord/nostrord/releases/tag/v2.1.0)의 “relay pool fold” [PR #176](https://github.com/nostrord/nostrord/pull/176)은 NIP-29 전용 socket과 shared pool을 통합했습니다. 하나의 reconnect scheduler가 모든 relay를 담당하고 [NIP-42](/ko/topics/nip-42/) AUTH는 retry 상한을 두며, auth-required publish는 fail closed 후 재시도합니다. request storm race를 닫고 kind-10009 fetch를 relay별 batch로 묶으며 `mux_chat` subscription이 모든 가입 group을 다루고 drop 시 스스로 복구합니다. [PR #179](https://github.com/nostrord/nostrord/pull/179)은 Android network 전환 뒤 zombie WebSocket을 감지합니다.

후속 [v2.1.1](https://github.com/nostrord/nostrord/releases/tag/v2.1.1)과 [PR #178](https://github.com/nostrord/nostrord/pull/178)도 같은 안정화 흐름을 이어갔습니다.

---

## 미출시 변경 사항

### rust-nostr, gift wrap과 비공개 DM builder에 NIP-40 만료 추가

[rust-nostr PR #1384](https://github.com/rust-nostr/nostr/pull/1384)는 `GiftWrapBuilder`와 `PrivateDirectMessageBuilder`에 `expiration` option을 추가했습니다. caller는 `Duration`을 넘기고 library는 [NIP-40](/ko/topics/nip-40/) 만료 tag를 gift wrap의 무작위 `created_at`에 더합니다. 절대 timestamp를 받으면 relay 관찰자가 duration을 빼 실제 send time을 알아낼 수 있기 때문입니다. tag는 gift wrap event에 들어가며 [NIP-59](/ko/topics/nip-59/)가 빈 tag를 요구하는 kind:13 seal에는 들어가지 않습니다. NIP-17 builder도 같은 값을 전달합니다. 이 변경은 [issue #1381](https://github.com/rust-nostr/nostr/issues/1381)을 닫았습니다.

관련 builder 정리는 [PR #1387](https://github.com/rust-nostr/nostr/pull/1387)에서도 이어졌습니다.

### Amethyst, Negentropy sync 강화와 NIP-50 검색 추가

[Amethyst main branch](https://github.com/vitorpamplona/amethyst)는 세 주제에 걸쳐 43개 PR을 병합했습니다. geode-to-strfry Negentropy sync에서 거절된 window가 무한 분할 loop를 만들던 문제를 [PR #3480](https://github.com/vitorpamplona/amethyst/pull/3480)이 backoff로 고쳤고, [PR #3475](https://github.com/vitorpamplona/amethyst/pull/3475)는 `negentropyKmp` 1.1.1로 올렸습니다. [PR #3478](https://github.com/vitorpamplona/amethyst/pull/3478)은 100만 event benchmark와 strfry parity mirror를 추가했으며 [PR #3458](https://github.com/vitorpamplona/amethyst/pull/3458), [PR #3466](https://github.com/vitorpamplona/amethyst/pull/3466)은 production benchmark와 sync 최적화를 CI에 넣었습니다. [PR #3459](https://github.com/vitorpamplona/amethyst/pull/3459)은 relay별 mutex를 lock-free concurrent collection으로 교체했습니다.

[PR #3477](https://github.com/vitorpamplona/amethyst/pull/3477)도 이 sync·benchmark 작업 묶음에 포함됩니다.

두 번째 주제는 [NIP-50](/ko/topics/nip-50/) full-text 검색입니다. [PR #3452](https://github.com/vitorpamplona/amethyst/pull/3452)는 event가 index metadata를 직접 담는 `SearchableEvent` interface를 추가했고 [PR #3464](https://github.com/vitorpamplona/amethyst/pull/3464)는 SQLite FTS 질의 전에 server-side NIP-50 extension을 제거합니다. [PR #3446](https://github.com/vitorpamplona/amethyst/pull/3446)은 기본 search relay를 중앙화했습니다.

세 번째는 niche protocol 통합입니다. Birdstar 조류 감지 kind 2473은 [PR #3473](https://github.com/vitorpamplona/amethyst/pull/3473), PS1 memory-card save kind 38192는 [PR #3482](https://github.com/vitorpamplona/amethyst/pull/3482)로 지원합니다. [PR #3450](https://github.com/vitorpamplona/amethyst/pull/3450)은 compose signature, [PR #3457](https://github.com/vitorpamplona/amethyst/pull/3457)은 desktop native notification, [PR #3432](https://github.com/vitorpamplona/amethyst/pull/3432)은 Messages privacy lock, [PR #3469](https://github.com/vitorpamplona/amethyst/pull/3469)은 `NostrServer.ingest` local write path를 추가했습니다.

### Buzz, relay 강화와 agent turn metric용 kind 44200 정의

[Buzz](https://github.com/block/buzz)는 이전 이름이 Sprout였던 프로젝트로 7월 1~7일 123개 PR을 병합했습니다. [PR #1441](https://github.com/block/buzz/pull/1441)은 NIP-AM의 영속적 암호화 agent turn metric을 kind 44200 signed event로 정의해 사용자의 relay에 보관합니다. [PR #1555](https://github.com/block/buzz/pull/1555)는 local archive, [PR #1562](https://github.com/block/buzz/pull/1562)는 atomic kind removal, [PR #1564](https://github.com/block/buzz/pull/1564)는 model name 전달을 추가했습니다.

relay 성능에서는 [PR #1453](https://github.com/block/buzz/pull/1453)이 post-commit dispatch를 지연하고 verify clone을 없앴으며, [PR #1454](https://github.com/block/buzz/pull/1454)는 ingest·fan-out DB round trip을 batch로 묶어 p99 ack를 7~16%, p999 tail을 29~53% 줄였습니다. [PR #1457](https://github.com/block/buzz/pull/1457)은 multi-filter query에 bounded concurrency를, [PR #1464](https://github.com/block/buzz/pull/1464)는 outbound WebSocket frame batching을 적용했습니다. [PR #1463](https://github.com/block/buzz/pull/1463)은 admin이 설정하고 [NIP-11](/ko/topics/nip-11/)로 제공하는 community별 icon을, [PR #1519](https://github.com/block/buzz/pull/1519)은 kind:5 기반 agent message 삭제를 추가했습니다.

relay hardening의 추가 변경은 [PR #1398](https://github.com/block/buzz/pull/1398)과 [PR #1432](https://github.com/block/buzz/pull/1432)에 담겼습니다.

### Divine Video, relay signature 검증과 NostrConnect 분리

[Divine Video mobile](https://github.com/divinevideo/divine-mobile)은 97개 PR을 병합했습니다. [PR #5774](https://github.com/divinevideo/divine-mobile/pull/5774)는 inbound relay event signature를 검증하고, [PR #5828](https://github.com/divinevideo/divine-mobile/pull/5828)은 kind-3080 deregistration event의 FCM push token을 암호화하며, [PR #5831](https://github.com/divinevideo/divine-mobile/pull/5831)은 큰 kind:5 삭제 이력을 chunk로 요청합니다. [PR #5826](https://github.com/divinevideo/divine-mobile/pull/5826)은 `nostrconnect://` flow의 `NostrConnectCoordinator`를 분리해 [NIP-46](/ko/topics/nip-46/) client-initiated bunker 경로를 정리했습니다.

관련 추적은 [issue #4741](https://github.com/divinevideo/divine-mobile/issues/4741)과 [PR #5709](https://github.com/divinevideo/divine-mobile/pull/5709)에서 이어집니다.

### Zap Cooking, NIP-46 bunker login 수정과 NIP-50 recipe 검색 추가

[Zap Cooking frontend](https://github.com/zapcooking/frontend)의 [PR #503](https://github.com/zapcooking/frontend/pull/503)은 명시적 connect handshake, authUrl 처리, 오류 표시로 bunker login hang을 고쳤습니다. [PR #495](https://github.com/zapcooking/frontend/pull/495)는 extract-recipe endpoint의 image·text upload에 NIP-98 auth를 붙였습니다. [PR #483](https://github.com/zapcooking/frontend/pull/483)은 nostrarchives search relay backend를 이용한 NIP-50 full-text recipe 검색을 추가했습니다.

같은 주간의 [PR #491](https://github.com/zapcooking/frontend/pull/491), [PR #492](https://github.com/zapcooking/frontend/pull/492), [PR #482](https://github.com/zapcooking/frontend/pull/482), [PR #494](https://github.com/zapcooking/frontend/pull/494)는 content rendering과 failure recovery를 다듬었습니다.

### swift-nostr-client v0.6.0, 첫 stable 릴리스를 향해 진전

[yysskk/swift-nostr-client](https://github.com/yysskk/swift-nostr-client)는 30개 PR과 함께 [v0.6.0](https://github.com/yysskk/swift-nostr-client/releases/tag/0.6.0)을 출시했습니다. MDK나 MarmotKit toolchain에 link하지 않는 Swift Nostr client를 위한 첫 stable API surface에 가까워졌습니다.

### Nostr Applet Protocol, NAP-OUTBOX routing과 fanout 강화

NAPS는 주로 [NAP-OUTBOX](https://github.com/napplet/naps/pull/32)를 정리했습니다. caller가 제어하는 routing과 노출되는 relay detail을 줄이고, relay hint와 resource sidecar를 담는 공통 event result 형태를 [NAP-RESOURCE](https://github.com/napplet/naps/pull/80)와 연결했습니다. outbox, inbox, relay fanout 규칙도 명시해 상호운용 모호성을 줄였습니다.

### Napplet toolchain, protocol 정렬 강화와 CLI 출시

Napplet package는 [NAP-COUNT query](https://github.com/napplet/web/pull/104), [OUTBOX runtime-owned lifecycle](https://github.com/napplet/web/pull/112), [RelayEventResult sidecar](https://github.com/napplet/web/pull/108)를 구현했습니다. CVM registry, DM error envelope, MEDIA session context, LISTS count, COMMON profile result, `htree:` RESOURCE scheme도 다듬었습니다. 새 [@napplet/cli](https://github.com/napplet/web/pull/103)는 config discovery, deploy planning, signing, Blossom upload, manifest 생성을 지원합니다. [host-injectable shim prelude](https://github.com/napplet/web/pull/127)와 [JSR 준비 작업](https://github.com/napplet/web/pull/145)도 반영됐습니다.

### primal-android, remote signer 기능 확장

[Primal Android](https://github.com/PrimalHQ/primal-android-app)는 18개 PR을 병합했습니다. [PR #1075](https://github.com/PrimalHQ/primal-android-app/pull/1075)는 remote signer 역할에 `switch_relays`와 `logout`을 구현해 NIP-46 surface를 넓혔습니다. [PR #1083](https://github.com/PrimalHQ/primal-android-app/pull/1083)은 splash-gated local migration framework, [PR #1080](https://github.com/PrimalHQ/primal-android-app/pull/1080)은 splash view-model의 note-feed prefetch를 추가했습니다.

### Wisp, multi-account switcher와 Blossom parser test 추가

[Wisp](https://github.com/barrydeen/wisp)의 [PR #604](https://github.com/barrydeen/wisp/pull/604)는 multi-account switcher와 account 추가 취소 경로를 넣었습니다. [PR #613](https://github.com/barrydeen/wisp/pull/613)은 [Blossom](/ko/topics/blossom/) server-list parser test를 추가했습니다. [PR #574](https://github.com/barrydeen/wisp/pull/574)는 iOS zap sheet, [PR #605](https://github.com/barrydeen/wisp/pull/605)는 swipe-up 거래 이력, [PR #611](https://github.com/barrydeen/wisp/pull/611)은 non-ASCII hashtag, [PR #609](https://github.com/barrydeen/wisp/pull/609)은 profile feed pagination과 inline gallery, [PR #603](https://github.com/barrydeen/wisp/pull/603)은 inline segment 앞 blank line 보존을 구현했습니다.

### TAO와 Wired, PoW signal을 21bit로 높이고 새 PoW root 표시

[smolgrrr/TAO](https://github.com/smolgrrr/TAO)와 [smolgrrr/Wired](https://github.com/smolgrrr/Wired)는 같은 commit set을 병합했습니다. [PR #84](https://github.com/smolgrrr/TAO/pull/84)는 기본 post signal PoW 목표를 선행 0 bit 21개로, [PR #80](https://github.com/smolgrrr/TAO/pull/80)은 최신 NIP-13 작업을 feed root로 표시해 raw event age 대신 timeline ranking signal로 씁니다. [PR #75](https://github.com/smolgrrr/TAO/pull/75)는 custom emoji picker, [PR #65](https://github.com/smolgrrr/TAO/pull/65)는 첫 frame video preview를 추가했습니다.

### keep-android, NIP-46 UX 개선과 TOCTOU 수정

[privkeyio/keep-android](https://github.com/privkeyio/keep-android)는 [v1.1.5](https://github.com/privkeyio/keep-android/releases/tag/v1.1.5)와 core v0.5.0을 고정한 [v1.1.6](https://github.com/privkeyio/keep-android/releases/tag/v1.1.6)을 출시했습니다. Keep은 [Issue #29](/en/newsletters/2026-07-01-newsletter/#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow)에서 CustID로 소개한 mobile identity vault입니다. v1.1.5는 [NIP-46](/ko/topics/nip-46/) challenge UX를, v1.1.6은 `set_active_share`의 check-then-set race를 고쳤습니다. [NIP-98](/ko/topics/nip-98/) 승인 화면에 URL과 method를 표시하고 RNG health check는 panic 대신 fail closed합니다. NIP-55 approval kill switch test도 추가했습니다.

### Heartwood, relay-to-serial signing bridge 출시

[forgesworn/heartwood v0.7.0](https://github.com/forgesworn/heartwood/releases/tag/v0.7.0)은 Bray serial signer 경로의 HSM-mode data plane을 연결합니다. [PR #11](https://github.com/forgesworn/heartwood/pull/11)은 bridge, [PR #13](https://github.com/forgesworn/heartwood/pull/13)은 serial-frame test와 `read_frame` payload offset 수정, [PR #14](https://github.com/forgesworn/heartwood/pull/14)은 codec를 공통 `heartwood-frame` crate로 분리한 변경입니다.

### SafeBox, Phase 3 진행 보고서와 FreeBSD jail runbook 공개

[SafeBox](https://github.com/trbouma/safebox)는 [NIP-47](/ko/topics/nip-47/) NWC, nAuth, nembed, QR·NFC relay 기반 record transfer를 결합한 private portable data vault입니다. 7월 6일의 [2026년 7월 진행 보고서](https://github.com/trbouma/safebox/blob/main/docs/PROGRESS-REPORT-2026-07.md)는 4월 이후 49개 commit, 총 1,136개 commit으로 Phase 3가 대부분 완료됐다고 기록합니다. 다음 단계는 제한된 pilot이며 NDA 하의 통신사가 health-record pilot을 검토 중이라고 밝혔습니다.

NWC mutate action은 proof race 방지를 위해 queue되고 실패한 Lightning melt는 proof를 보호합니다. 장기 NWC listener는 idle threshold 전에 refresh하며 LNURL callback은 canonical origin과 명시적 JSON·CORS를 씁니다. QR·NFC 교환은 recipient-presented, sender-presented, cross-device mode를 아우르는 통합 flow와 KEM, replay protection을 갖췄습니다. 이번 주 [`6866dae`](https://github.com/trbouma/safebox/commit/6866dae)는 [FreeBSD jail deployment 및 liboqs build runbook](https://github.com/trbouma/safebox/blob/main/docs/devops/freebsd-jail-from-scratch.md)을 추가했습니다.

배포 목표와 구조는 [FreeBSD appliance 명세](https://github.com/trbouma/safebox/blob/main/docs/devops/SAFEBOX-FREEBSD-APPLIANCE-SPEC.md)에 정리돼 있습니다.

보고서는 SafeBox의 cryptographic control과 portable record 구조를 전자 선하증권·창고증권·약속어음·인증서에 적용하는 spin-off [OpenETR](https://github.com/trbouma/openetr)도 발표했습니다. 7월 7일 [`ea612a9`](https://github.com/trbouma/openetr/commit/ea612a9)는 attestation 분리, [`ca153a3`](https://github.com/trbouma/openetr/commit/ca153a3)는 mandate와 effect 처리, [`ba84b61`](https://github.com/trbouma/openetr/commit/ba84b61)는 verifiable credential 형식 비교를 추가했습니다.

---

## Protocol 작업과 NIP 업데이트

### 병합: NIP-51과 NIP-37의 kind 10013 명칭 정렬

[PR #2404](https://github.com/nostr-protocol/nips/pull/2404)는 문구 일관성을 고칩니다. [NIP-37](/ko/topics/nip-37/)의 kind 10013 명칭 `Relay List for Private Content`를 [NIP-51](/ko/topics/nip-51/)의 `Draft relays` 절도 그대로 쓰게 됐습니다. wire 동작이나 tag semantics는 바뀌지 않지만 list event의 umbrella 명세와 private-content 후속 명세가 같은 kind를 가리킨다는 점이 분명해졌습니다.

### 공개: .well-known 조회를 이용한 NIP-AD Nostr web address

[PR #2406](https://github.com/nostr-protocol/nips/pull/2406)은 닫힌 PR #2393의 후속이며 [`AD.md`](https://github.com/nostr-protocol/nips/blob/2f4b09335c54a993d483bc220195e3f4a33df1ec/AD.md)에 전체 초안이 있습니다. NIP-AD는 web URL에 선택적 Nostr 상대 주소를 부여합니다. client가 `https://golf.com/players`를 보면 `https://golf.com/.well-known/nostr.json?ad=/players`를 요청하고, path를 `{filter, relays}`에 mapping한 JSON을 받습니다. filter는 kinds, authors, `#d`, `limit` 등을 갖춘 표준 NIP-01 filter입니다. `"limit": 1`이면 단일 event, 없으면 목록으로 해석합니다. 일반 browser에는 같은 URL이 HTML을 보여 줍니다. [NIP-29](/ko/topics/nip-29/) group name을 특정 relay의 kind 39000 event로 해석하는 사례 등이 제시됐습니다.

### 공개: invite code용 NIP-86 claim 관리

[PR #2408](https://github.com/nostr-protocol/nips/pull/2408)은 [NIP-86](/ko/topics/nip-86/)에 `listclaims`(params `[]`, [NIP-43](/ko/topics/nip-43/) invite code 배열 반환), `createclaim`(params `[claim]`), `deleteclaim`(params `[claim]`)을 추가합니다. relay admin이 role과 연결된 유료 invite code를 만들고 사용자가 kind 28935 claim event를 게시하면 bot이 role을 자동 할당하는 community onboarding flow를 relay management RPC만으로 처리할 수 있습니다.

### 공개: (h, s, l) tuple의 role color

[PR #2402](https://github.com/nostr-protocol/nips/pull/2402)는 [NIP-43](/ko/topics/nip-43/) role color를 단일 `hue`(0~360)에서 `hue`, `saturation`(0~1), `lightness`(0~1) tuple로 바꿉니다. 각 component는 빈 문자열로 client default를 쓸 수 있고 특별한 색이 아니면 hue만 제공하도록 권장합니다. NIP-86의 `createrole`과 `editrole` signature도 `[id, label, description, [h, s, l], order]`가 됩니다. client마다 같은 role을 다른 강도로 표시하던 문제를 줄입니다.

### 공개: NIP-80 hardware-attested media provenance

[PR #2409](https://github.com/nostr-protocol/nips/pull/2409)은 capture hardware에 뿌리를 둔 media provenance 형식 NIP-80을 제안합니다. camera가 촬영 순간 photo에 서명하고 content를 key로 proof를 relay에 게시해 metadata 제거, re-hosting, platform takedown 뒤에도 검증되게 합니다. kind 1080은 capture attestation, 1081은 resize·crop·recompress·redact derivation, 1082는 영구적 author-scoped revocation, 11080은 device announcement, 31080은 device endorsement, 31081은 anonymous attestation용 device set입니다. NIP-94 `x` tag, [NIP-92](/ko/topics/nip-92/) `imeta`, [NIP-65](/ko/topics/nip-65/) discovery, [Blossom](/ko/topics/blossom/)을 재사용합니다.

제안은 [NIP-5A](/ko/topics/nip-5a/)와 [NIP-03](https://github.com/nostr-protocol/nips/blob/master/03.md)의 기존 primitive도 참고하며, [OpenVeilCam](https://github.com/PrarthanaPurohit/OpenVeilCam)은 hardware-attested capture 구현 사례로 언급됩니다.

### 공개: NIP-01 pagination 강화

[PR #2407](https://github.com/nostr-protocol/nips/pull/2407)은 NIP-01에 “Pagination & limits” 절을 추가합니다. relay의 최대 `limit`은 같은 `created_at`을 가진 event 최대 개수보다 커야 합니다. 뒤로 paging하는 client는 `until = oldest`를 포함형으로 반복하고 `id`로 deduplicate해야 하며, 새 event가 없으면 끝입니다. 한 page의 oldest와 newest가 같은 timestamp면 더 큰 limit으로 그 초를 다시 요청하고, relay가 clamp해도 한 초에 갇히면 `until = oldest - 1`로 누락을 감수하거나 중단해야 합니다. 일반 paging은 작은 `limit`을 설정하면 안 되며 relay 최대값을 따라야 합니다.

---

## NIP 심층 분석: NIP-13 작업증명

[NIP-13](/ko/topics/nip-13/)은 Nostr event의 작업증명 mechanism을 정의합니다. 공개 relay에서는 누구나 keypair를 만들고 비용 없이 topic을 flood할 수 있습니다. NIP-13은 spammer가 대량으로 부담하지만 일반 사용자는 message당 한 번만 내는 계산 비용을 부여하고, relay와 client가 난이도 기준을 만족하는 event를 요구하거나 우선할 수 있게 합니다.

### 동작 원리

event author는 bit 단위 난이도를 고르고 직렬화 event의 sha256 hash인 id가 그 수 이상의 선행 0 bit를 가질 때까지 채굴합니다. id에는 `created_at`, tag, content가 들어가므로 hash space를 탐색하려면 event body를 바꿔야 합니다. NIP-13은 이를 위한 `nonce` tag를 정의합니다.

```
["nonce", "<nonce_value>", "<target_bits>"]
```

`nonce_value`는 miner가 정하는 문자열이고 `target_bits`는 약속한 난이도입니다. verifier는 event id의 실제 선행 0 bit 수를 세어 tag의 claim과 비교합니다.

무작위 sha256 output의 선행 0 bit 수는 기하분포를 따르므로 bit 하나마다 예상 작업량이 두 배가 됩니다. 8bit는 평균 256회, 20bit는 약 100만 회, 28bit는 약 2억 6,800만 회입니다. Bitchat의 8bit는 최신 hardware에서 1ms 미만이고, TAO와 Wired의 21bit는 post당 약 200만 회여서 laptop에는 빠르지만 bot farm 규모에서는 비쌉니다. NIP-13 자체는 난이도를 정하지 않으며 relay와 client가 선택합니다.

### event 예시

NIP-13으로 채굴한 최소 kind-1 note는 다음과 같습니다.

```json
{
  "id": "000000000e9d97a1ab09fc381030b346cdd7a1a8a6f27c9c88f68c8b9d0f6c8a",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1720368000,
  "kind": 1,
  "tags": [
    ["nonce", "72847", "28"]
  ],
  "content": "hello, this cost me 28 bits of PoW",
  "sig": "b1a5c9c74cff59f8a48e5c3b3d8e1c8e7e2c1d4a8e2b9f7d1c3e8b4f6a2c8d1e9f4b3c7a1d8e5b2f9c6a3d7e1b8f4c9a2d6e3b7f1c8a4d9e2b5f8c1a7d4e6b9f3c2"
}
```

`id`는 hex 0 일곱 개, 즉 nonce tag의 `target_bits`와 같은 선행 0 bit 28개로 시작합니다. miner는 목표를 만족할 때까지 `nonce_value` `72847`을 변화시켰습니다. verifier는 직렬화 event를 hash하고 선행 0 bit와 signature를 확인합니다. NIP-13은 새 field가 아니라 `nonce` tag와 id의 0 bit 제약을 추가합니다.

### 사용 사례

Bitchat 1.5.4는 kind 20000 geohash channel message에 8bit PoW를 적용해 게시 전 채굴하고 검증된 inbound PoW의 sender별 rate limit을 완화합니다. TAO와 Wired는 21bit를 기본 post signal로 쓰고 최신 PoW 활동을 feed root ranking에 반영합니다. [cagliostr](https://github.com/mattn/algia)는 relay layer에서 기준 미달 event를 거부합니다. noStrudel은 author용 client-side mining 설정을 제공하고 Damus와 Amethyst는 표시할 때 선행 0 bit를 계산합니다. Coracle은 mining과 filtering을, NDK와 nostr-tools는 library consumer용 helper를 제공합니다.

NIP-13의 핵심은 위조할 수 없다는 점입니다. `target_bits` claim은 id가 실제로 그만큼의 선행 0을 가져야 증거가 되며 위조하려면 작업을 다시 해야 합니다. 따라서 Bitchat은 spammer의 고난이도 주장도 신뢰 판단이 아니라 hash count로 검증해 rate limit 완화에 쓸 수 있습니다. PoW가 특정 pubkey나 content에 miner를 묶지는 않지만 계산 비용은 실제입니다. NIP-13은 spam 문제를 “불가능”에서 “수량화 가능”으로 바꾸고 client가 가격을 정하게 합니다.

---

## NIP 심층 분석: NIP-40 만료 timestamp

[NIP-40](/ko/topics/nip-40/)은 지정한 Unix timestamp 뒤 event가 만료된 것으로 취급하라고 relay와 client에 알리는 `expiration` tag를 정의합니다. Nostr event는 원래 영구적이고 NIP-09 delete event도 원본 보존을 막지 못합니다. NIP-40은 게시 시 event가 단명한다고 선언해 기한 뒤 relay가 제공을 중단하고 client가 표시를 멈추도록 요청합니다.

### 동작 원리

author는 event에 다음 tag를 추가합니다.

```
["expiration", "<unix_timestamp>"]
```

timestamp는 Unix 초입니다. relay는 이미 지난 event를 ingest 시 거부하거나 만료 뒤 제공을 중단할 수 있고 author의 만료를 존중해야 합니다. client도 만료 event를 숨겨야 합니다. NIP-40은 삭제를 강제하지 않고 NIP-70 protected-event semantics를 무효화하지도 않는, hint와 soft contract의 조합입니다.

tag는 event 자체, wrapped messaging이면 outer wrap에 있습니다. event는 계속 유효한 signed event라 보유한 사람이 읽을 수 있지만 relay와 client가 기한 뒤 노출하지 않으리라는 공동 기대를 만듭니다. ephemeral post, 시간 제한 공지, live-event note, 정해진 기간 뒤 남지 않아야 할 NIP-17 DM에 유용합니다.

### gift wrap과의 상호작용

이번 주 [rust-nostr PR #1384](https://github.com/rust-nostr/nostr/pull/1384)는 NIP-40과 [NIP-59](/ko/topics/nip-59/) gift wrap의 상호작용을 보여 줍니다. NIP-59는 sender 실제 key가 서명한 kind:13 “seal”과 ephemeral key가 서명한 kind:1059 “gift wrap”의 두 layer를 정의합니다. 둘의 `created_at`은 실제 전송보다 최대 48시간 전까지 무작위화되어 relay 관찰자가 실제 시간을 알 수 없습니다. seal의 tag는 비어 있어야 합니다.

따라서 expiration tag는 seal이 아니라 gift wrap에 있어야 합니다. 실제 send time에 고정하면 관찰자가 절대 만료 timestamp에서 TTL을 빼 실제 시간을 복원할 수 있습니다. rust-nostr API는 caller에게 `Duration`을 받고 내부에서 `expiration = wrap.created_at + duration`을 계산합니다. wrap의 `created_at`이 이미 무작위이므로 expiration도 같은 무작위성을 물려받아 실제 시간을 누출하지 않습니다.

### event 예시

kind-1 note의 최소 NIP-40 예시는 다음과 같습니다.

```json
{
  "id": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1720368000,
  "kind": 1,
  "tags": [
    ["expiration", "1720454400"]
  ],
  "content": "this note expires in 24 hours",
  "sig": "d2e5b8a1c4f7b0d3e6a9c2f5b8d1e4a7c0f3b6d9e2a5c8f1b4d7e0a3c6f9b2d5e8a1c4f7b0d3e6a9c2f5b8d1e4a7c0f3b6d9e2a5c8f1b4d7e0a3c6f9b2d5e8a1"
}
```

`created_at`은 게시 Unix timestamp이고 expiration은 86,400초, 즉 24시간 뒤 제공을 멈추라는 뜻입니다. NIP-40을 따르는 relay는 `1720454400` 뒤 REQ에 이 event를 반환하지 않고 client도 숨깁니다.

### 사용 사례

rust-nostr의 `GiftWrapBuilder`와 `PrivateDirectMessageBuilder`는 만료를 일급 `Duration` parameter로 제공합니다. NDK는 kind-1과 DM builder용 helper를, nostr-tools는 tag를 읽고 적용하는 `getExpiration`과 `isExpired`를 제공합니다. strfry, nostr-rs-relay, khatru 등은 운영자 정책에 따라 만료 event를 거부하거나 REQ에서 제외합니다. Damus, Amethyst, noStrudel, Coracle, Primal은 timeline에서 필터링하고 zap.stream 같은 live client는 kind-1311 chat에 NIP-40을 써 stream 종료 뒤 chat이 남지 않게 합니다.

NIP-40은 event별 opt-in이라 조정된 배포가 필요 없습니다. author는 지금 tag를 붙일 수 있고, 지원 relay는 working set이 깔끔해지며, 무시하는 relay도 이전보다 나빠지지 않습니다. 이번 rust-nostr 변경은 tag의 존재만큼 위치가 중요함을 보여 줍니다. NIP-59처럼 privacy-preserving envelope에서는 이미 timestamp가 무작위인 layer에 tag를 두고 API가 실제 timestamp의 우발적 누출을 막습니다.

---

이번 주 소식은 여기까지입니다. 만들고 있는 프로젝트나 공유할 소식이 있나요? NIP-17 DM 또는 Nostr로 연락해 주세요.
