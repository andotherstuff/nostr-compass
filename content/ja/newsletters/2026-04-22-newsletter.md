---
title: 'Nostr Compass #19'
date: 2026-04-22
translationOf: /en/newsletters/2026-04-22-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [Amethyst](https://github.com/vitorpamplona/amethyst)は、[Marmot](/ja/topics/marmot/)準拠、[NIP-72](/ja/topics/nip-72/) community、[NIP-75](/ja/topics/nip-75/) zap goals、MoQベースaudio roomをまとめて進めました。[TollGate](https://github.com/OpenTollGate/tollgate)は、NostrとCashu上のpay-per-use internet access仕様をv0.1.0として固め、[nostream](https://github.com/Cameri/nostream)は[NIP-45](/ja/topics/nip-45/)、[NIP-62](/ja/topics/nip-62/)、compression、query hardening、完全な[NIP-11](/ja/topics/nip-11/) parityを進めました。Forgeswornは、signing、identity、paid API discoveryのstackを一気に公開しました。ShockWalletは、NostrネイティブなLightning wallet同期を押し進め、Formstr suiteはsecurity hardeningとRRULE supportを中心に26 PRをマージしました。StableKraft、Keep、topaz、WoT Relay、Flotilla、NipLockも今週の出荷に並びます。今週のdeep diveは[NIP-72](/ja/topics/nip-72/)と[NIP-57](/ja/topics/nip-57/)です。

## Top Stories

### Amethyst ships Marmot MIP compliance, NIP-72 communities, zap goals, and MoQ audio rooms

[Amethyst](https://github.com/vitorpamplona/amethyst)は今週57本のPRをマージし、[Marmot](/ja/topics/marmot/) encrypted groupの準拠作業、community support、live stream向けzap goals、Media over QUICベースaudio roomをまとめて押し進めました。[PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462)は埋め込み[MDK](https://github.com/marmot-protocol/mdk)をMIP-01とMIP-05 wire formatへ合わせ、VarInt encodingとMDK test vectorによるround-trip validationを追加しました。[PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435)はMIP-00 KeyPackage Relay List supportを加え、[PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436)はWhite Noiseとのcross-client testingで見つかったadmin gateとmedia handlingの差分を埋めました。[PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466)と[PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471)はMLS commit framingとouter-layer復号の正しさを修正し、[PR #2477](https://github.com/vitorpamplona/amethyst/pull/2477)と[PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493)はさらにcommit pathとmessage encryptionの整合性を詰め、reference vectorに対するcryptography validatorを追加しました。[PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488)は、Marmot/MLS group操作をscriptableに扱えるCLIの`amy`も出荷しています。

community側では、[PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468)がkind `34550`定義の作成、moderator追加、relay hint設定、`a`タグによる投稿、kind `4549` approval event管理を含む[NIP-72](/ja/topics/nip-72/) supportを追加しました。絵文字では[PR #2458](https://github.com/vitorpamplona/amethyst/pull/2458)と[PR #2473](https://github.com/vitorpamplona/amethyst/pull/2473)がemoji set supportと完全なNIP-30 emoji-pack管理UIを追加しました。live surfaceでは、[PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469)が[NIP-53](/ja/topics/nip-53/) Live Activities画面へ[NIP-75](/ja/topics/nip-75/) zap goalsを統合し、goal header、progress bar、one-tap zap、top-zappers leaderboardを導入しました。[PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486)は専用のLive Streams feed、[PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491)はproof-of-agreementとevent builder、[PR #2461](https://github.com/vitorpamplona/amethyst/pull/2461)はfeed内lowest-resolution HLS、picture-in-picture、full-screen時の自動解像度選択を追加しています。

もっとも野心的なのはreal-time audioです。[PR #2494](https://github.com/vitorpamplona/amethyst/pull/2494)は[Media over QUIC](https://datatracker.ietf.org/group/moq/about/) transport clientとaudio room supportを追加しました。MoQのpub-sub modelは、WebSocket relayよりライブ音声に向いており、trackやpriorityごとのsubscriptionを可能にします。[PR #2487](https://github.com/vitorpamplona/amethyst/pull/2487)のPublic Chats画面と組み合わせると、Amethystはpublic audio roomとMarmot encrypted messagingを並行して持つことになります。[PR #2485](https://github.com/vitorpamplona/amethyst/pull/2485)と[PR #2490](https://github.com/vitorpamplona/amethyst/pull/2490)はFollow Packs discovery feedとonboarding統合を追加し、[PR #1983](https://github.com/vitorpamplona/amethyst/pull/1983)はMarmot DMやmentionのためのalways-on notification serviceを導入し、[PR #2480](https://github.com/vitorpamplona/amethyst/pull/2480)はadaptive cache sizing付きHLS video cachingを加えました。

### TollGate v0.1.0 stabilizes pay-per-use internet over Nostr and Cashu

[TollGate](https://github.com/OpenTollGate/tollgate)は4月21日に[v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)を出し、pay-per-use network access向け仕様群に最初のtag付きsnapshotを与えました。WiFi router、Ethernet switch、Bluetooth tetherのような接続制御デバイスが価格を広告し、[Cashu](/ja/topics/cashu/) ecash tokenを受け取り、sessionを管理できます。数satsを持つlocal Cashu walletがあれば、accountもsubscriptionもKYCもなく、その場で次の1分または1MBの接続を買えます。

releaseは3層構造を固定しています。[TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)はAdvertisement、Session、Noticeの3つの基本event shapeを定義し、[TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)はCashu payment layerを追加して、gateが広告する任意mintからcustomerがtokenを償還できるようにします。上位のinterface layerでは[HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md)からHTTP-03が制限的OS向けplain HTTP surfaceを定義し、[NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)がWebSocketを張れるclient向けのNostr transportを定義します。medium layerでは[WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)がcaptive portal routingを扱います。payment assetがcredentialではなくbearer tokenなので、customerは事前ネット接続なしで最初の接続を購入でき、TollGate同士がuplinkを買い合うmulti-hop構成も可能です。詳しくは新しい[TollGate topic page](/ja/topics/tollgate/)にまとめました。

### nostream merges 53 PRs for NIP-45, NIP-62, compression, and query hardening

[nostream](https://github.com/Cameri/nostream)は、TypeScript relay implementationとして今週53本のPRをマージしました。feature面では、[PR #522](https://github.com/Cameri/nostream/pull/522)が[NIP-45](/ja/topics/nip-45/) `COUNT` supportを追加し、[PR #544](https://github.com/Cameri/nostream/pull/544)が[NIP-62](/ja/topics/nip-62/) right-to-vanishをadvertised feature listへ加え、[PR #548](https://github.com/Cameri/nostream/pull/548)は最近のtag-case conventionに沿って`#A`から`#Z`のuppercase tag filterを受け入れるようにし、[PR #514](https://github.com/Cameri/nostream/pull/514)はevent import/exportにgzipとxz compressionを追加しました。

query performanceとcorrectnessも強化されています。[PR #534](https://github.com/Cameri/nostream/pull/534)はbenchmark harnessとfilter-to-SQL translationの最適化を導入し、[PR #524](https://github.com/Cameri/nostream/pull/524)はwhitelist/blacklist pubkeyのprefix match bugをexact-matchへ修正し、[PR #553](https://github.com/Cameri/nostream/pull/553)は同一`created_at`時のconcurrent insert raceを避けるdeterministic tie-breakerを`upsertMany`へ追加しました。[PR #493](https://github.com/Cameri/nostream/pull/493)は`X-Forwarded-For`をtrusted proxyだけに限定し、[PR #557](https://github.com/Cameri/nostream/pull/557)はretention、authentication hint、optional field整理を含めて完全な[NIP-11](/ja/topics/nip-11/) parityを達成しました。

## Shipping This Week

### Primal Android ships Explore tab, NIP-05 verification, and audio player

[Primal Android](https://github.com/PrimalHQ/primal-android-app)は先週のfeed redesignに続き11本のPRを積みました。[PR #1021](https://github.com/PrimalHQ/primal-android-app/pull/1021)はpopular user、follow pack、curated feedを軸にしたExplore tabを導入し、[PR #1015](https://github.com/PrimalHQ/primal-android-app/pull/1015)はPrimalのAdvanced Search DSLから初期値を作るfeed editorを追加しました。[PR #994](https://github.com/PrimalHQ/primal-android-app/pull/994)はprofile向け[NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md) verification UIを追加し、[PR #997](https://github.com/PrimalHQ/primal-android-app/pull/997)はin-feed audio playerを埋め込み、audio attachmentをその場で再生できるようにしています。[PR #1018](https://github.com/PrimalHQ/primal-android-app/pull/1018)はwallet QR scanner経由の[NIP-46](/ja/topics/nip-46/) nostr-connect pairingも追加しました。

### strfry adds Prometheus write-path metrics and fixes NIP-42 AUTH envelope

[strfry](https://github.com/hoytech/strfry)はoperator向け改善をまとめて出しました。[PR #194](https://github.com/hoytech/strfry/pull/194)は専用Prometheus write-path metrics exporterとconnection gaugeを追加し、[PR #197](https://github.com/hoytech/strfry/pull/197)はconnectionごとのup/down bytesとcompression ratioをlogへ出すようにしました。[PR #192](https://github.com/hoytech/strfry/pull/192)はfilter tag limitをruntime-configurable optionへ昇格させ、[PR #201](https://github.com/hoytech/strfry/pull/201)は[NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH failure responseを`NOTICE`からNIP準拠の`OK` envelopeへ修正しました。

### Shopstr hardens storefront security across 13 PRs

[Shopstr](https://github.com/shopstr-eng/shopstr)は今週13本のPRをマージし、storefront security fixが大半を占めました。[PR #434](https://github.com/shopstr-eng/shopstr/pull/434)はseller-to-visitor script executionを許していたstored JavaScript holeを閉じ、[PR #417](https://github.com/shopstr-eng/shopstr/pull/417)はreflected XSSを防ぐためstorefront policy HTML renderingをescapeし、[PR #418](https://github.com/shopstr-eng/shopstr/pull/418)は未認証cached-event deletion APIを閉じました。[PR #433](https://github.com/shopstr-eng/shopstr/pull/433)、[PR #419](https://github.com/shopstr-eng/shopstr/pull/419)、[PR #435](https://github.com/shopstr-eng/shopstr/pull/435)、[PR #414](https://github.com/shopstr-eng/shopstr/pull/414)も認証とSSRF関連の穴を塞いでいます。機能面では、[PR #421](https://github.com/shopstr-eng/shopstr/pull/421)がfailed relay publish queueのreplay safetyを改善し、[PR #425](https://github.com/shopstr-eng/shopstr/pull/425)がwallet event fetchを修復し、[PR #392](https://github.com/shopstr-eng/shopstr/pull/392)がcheckout前にstored cart discountを再検証するようにしました。

### Nostria v3.1.26 through v3.1.28 add background music playback on Android

[Nostria](https://github.com/nostria-app/nostria)は今週[v3.1.22](https://github.com/nostria-app/nostria/releases/tag/v3.1.22)から[v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28)まで6リリースを出しました。中心は[v3.1.26](https://github.com/nostria-app/nostria/releases/tag/v3.1.26)のAndroid background music playbackで、audio再生中にappが生き続け、notification barやlock screenからmedia controlを行えます。続く[v3.1.27](https://github.com/nostria-app/nostria/releases/tag/v3.1.27)と[v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28)はこの新しいmedia-service surfaceをhardeningしました。[Newsletter #18](/ja/newsletters/2026-04-15-newsletter/)では、その直前のlocal image generation releaseを扱っています。

### Wisp v0.18.0-beta adds Normie Mode, For You feed, and NIP-29 group config

[Wisp](https://github.com/barrydeen/wisp)は4月16日に[v0.18.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.18.0-beta)を出しました。[PR #462](https://github.com/barrydeen/wisp/pull/462)は法定通貨建て表示を増やすNormie Modeを追加し、[PR #464](https://github.com/barrydeen/wisp/pull/464)はtopic pickerとfirst-post coach付きのonboarding刷新を行い、[PR #469](https://github.com/barrydeen/wisp/pull/469)はextended follow、trending event、followed hashtagを混ぜるFor You feedを加えました。protocol面では[PR #471](https://github.com/barrydeen/wisp/pull/471)が[NIP-29](/ja/topics/nip-29/) group configurationを実装し、[PR #478](https://github.com/barrydeen/wisp/pull/478)が[NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH完了前にgroup `9021`、`9007`、`9009`を送らないよう順序を修正し、[PR #481](https://github.com/barrydeen/wisp/pull/481)はmentionされたpubkeyの[NIP-65](/ja/topics/nip-65/) inbox relayへnoteをbroadcastするようにしました。

### NoorNote v0.8.4 adds Scheduled Posts and live stream zapping

[NoorNote](https://github.com/77elements/noornote)は[v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4)と[v0.8.5](https://github.com/77elements/noornote/releases/tag/v0.8.5)を出しました。v0.8.4の中心はScheduled Posts add-onで、appは署名済みイベントをNoorNote運営relayへ渡し、指定時刻に公開させます。秘密鍵は端末外へ出ません。同じreleaseは[NIP-53](/ja/topics/nip-53/)経由でstream chat overlayへsatsが現れるone-tap live stream zapも追加し、fiat-rate APIが一時停止してもwallet balanceを表示し続けるようにしました。v0.8.5では長いAndroid scrollでpostが重複するtimeline deduplication bugが修正されています。

### topaz v0.0.2 ships a Nostr relay for Android

[topaz](https://github.com/fiatjaf/topaz)は、[fiatjaf](https://github.com/fiatjaf)によるAndroid phone上で動く新しいNostr relayで、2026-04-17に[v0.0.2](https://github.com/fiatjaf/topaz/releases/tag/v0.0.2)を公開しました。現段階ではscopeは狭く、インストール可能なAndroid packageとして動作するrelayを提供することが主眼です。

### StableKraft v1.0.0 ships the first stable music-and-podcast PWA release

[StableKraft](https://github.com/ChadFarrow/stablekraft-app)は、podcast feed由来のmusicを発見、整理、再生するNext.js PWAで、authとsocial featureにNostr、V4V paymentにLightningを使います。2026-04-18に[v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0)へ到達しました。同週には、[15-minute OPML cacheとillegal XML stripping](https://github.com/ChadFarrow/stablekraft-app/commit/7ac90f6)でfeed ingestionを改善し、[follow-up fix](https://github.com/ChadFarrow/stablekraft-app/commit/fbf337b)でnightly reparse windowを720時間から24時間へ縮め、新規feedのself-healを速めています。

### NipLock ships a NIP-17-based password manager

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd)は、credentialを[NIP-17](/ja/topics/nip-17/) gift-wrapped DMとして保存し、device間で同期するpassword managerです。各password entryは自分の鍵から自分自身へのNIP-17 DMであり、同じ鍵で認証した任意deviceへ同じイベントが複製されます。署名はraw `nsec`、[nos2x](https://github.com/fiatjaf/nos2x)のようなbrowser extension、または[NIP-46](/ja/topics/nip-46/)経由の[Amber](https://github.com/greenart7c3/Amber)で行えます。

### flotilla-budabit polishes its NIP-34 repo surface

Budabit communityによる[Flotilla](https://gitea.coracle.social/coracle/flotilla) fork、[flotilla-budabit](https://github.com/Pleb5/flotilla-budabit)は、NIP-34 git-over-nostr workflow周辺のfixをまとめて出しました。repo discussion controlの復元、detail pageでのsticky repo tab保持、saved GRASP relayからのrepo announcement読み込み、maintainer適用patch statusの同期などが含まれます。upstream Flotillaと近い状態を保ちながら、Budabit contributor向けrepo viewを優先しています。

### rx-nostr 3.7.2 through 3.7.4 add default verifier and optional constructor args

[rx-nostr](https://github.com/penpenpng/rx-nostr)は、RxJSベースのNostr libraryで、[3.7.2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.2)、[3.7.3](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.3)、[3.7.4](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.4)を出しました。[PR #192](https://github.com/penpenpng/rx-nostr/pull/192)はdefault Schnorr verifierを追加し、paired releaseの[crypto@3.1.6](https://github.com/penpenpng/rx-nostr/releases/tag/crypto%403.1.6)が`@noble/curves`利用bugを修正しました。[PR #195](https://github.com/penpenpng/rx-nostr/pull/195)は`createRxNostr()`の引数をoptionalにし、zero-configでのquick integrationを可能にしています。

### Keep Android v1.0.0 ships with reproducible builds and zero trackers

[Keep](https://github.com/privkeyio/keep-android)は、Nostrネイティブなpassword and secret managerで、hardening PRの積み上げの後、4月21日に[v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0)を出しました。[PR #241](https://github.com/privkeyio/keep-android/pull/241)はpinnedかつverifiedなtoolchainを使うreproducible build recipeを追加し、[PR #248](https://github.com/privkeyio/keep-android/pull/248)はGoogle ML KitをZXingへ置き換えてGoogle Play Services依存を外し、[PR #252](https://github.com/privkeyio/keep-android/pull/252)はv1.0.0 buildのtrackerがゼロであることを示す[Exodus Privacy scan](https://reports.exodus-privacy.eu.org/en/)を公開しました。[PR #256](https://github.com/privkeyio/keep-android/pull/256)はZapstore配布向け`zapstore.yaml` manifestも追加しています。

### Flotilla 1.7.3 and 1.7.4 add kind-9 wrapping for richer NIP-29 rooms

[Flotilla](https://gitea.coracle.social/coracle/flotilla)は、hodlbodによる[NIP-29](/ja/topics/nip-29/) groups clientで、[1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3)と[1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)を出しました。中心となるprotocol changeは、calendar eventやpollのようなnon-chat contentをkind `9`で包むことです。これにより、それらをgroupへ送ったときroom contextが保たれます。同じrelease lineではpoll、Aegis URL schemeによる[NIP-46](/ja/topics/nip-46/) login、space inviteのnative share、room mention、mobile clipboard image paste、draft、video in call、feed pagination改善も入りました。

### WoT Relay v0.2.1 migrates eventstore to LMDB

[WoT Relay](https://github.com/bitvora/wot-relay)は、bitvoraによるweb-of-trust filtered relayで、2026-04-22に[v0.2.1](https://github.com/bitvora/wot-relay/releases/tag/v0.2.1)を出しました。[PR #97](https://github.com/bitvora/wot-relay/pull/97)はeventstoreを[LMDB](http://www.lmdb.tech/)へ移行し、初期trust graph構築時にupstream read budgetを使い切らないようWoT bootstrap fetchを調整し、[PR #99](https://github.com/bitvora/wot-relay/pull/99)は`golang.org/x/crypto`をv0.45.0へ上げ、[PR #100](https://github.com/bitvora/wot-relay/pull/100)はreleaseに合わせてadvertised [NIP-11](/ja/topics/nip-11/) software URLとversion stringを更新しました。

### Formstr suite: Pollerama security pass, Forms i18n, Calendar RRULE support

Formstr suiteは今週26本のPRをマージし、Pollerama、Forms、Nostr Calendar全体で明確なsecurityテーマが見えました。[Pollerama](https://pollerama.fun)では、[PR #182](https://github.com/formstr-hq/nostr-polls/pull/182)がlogout時のcached DM失効、[PR #175](https://github.com/formstr-hq/nostr-polls/pull/175)がsecure browser storageへのlocal key移動、[PR #171](https://github.com/formstr-hq/nostr-polls/pull/171)がkind `0` profile contentの`JSON.parse`防御を行い、product面では[PR #186](https://github.com/formstr-hq/nostr-polls/pull/186)がHTTPS deep linking、[PR #169](https://github.com/formstr-hq/nostr-polls/pull/169)がpoll result上のauthor名clickable化を追加しました。

[Formstr](https://formstr.app)側では、[PR #475](https://github.com/formstr-hq/nostr-forms/pull/475)がaudio/video URL support、[PR #439](https://github.com/formstr-hq/nostr-forms/pull/439)がi18n、[PR #466](https://github.com/formstr-hq/nostr-forms/pull/466)がGoogle Forms importer、[PR #463](https://github.com/formstr-hq/nostr-forms/pull/463)がsensitive key logのconsole出力削除を行いました。[Nostr Calendar by Formstr](https://calendar.formstr.app)は同日に[v1.3.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.3.0)と[v1.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.0)を出し、[PR #107](https://github.com/formstr-hq/nostr-calendar/pull/107)で複数およびcustom RRULE support、[PR #101](https://github.com/formstr-hq/nostr-calendar/pull/101)でRFC 5545に従うfloating RRULE dateのUTC解釈、[PR #97](https://github.com/formstr-hq/nostr-calendar/pull/97)でshared event追加、[PR #86](https://github.com/formstr-hq/nostr-calendar/pull/86)でlist-level notification preference、[PR #112](https://github.com/formstr-hq/nostr-calendar/pull/112)でlogin/loading path再設計を行いました。3つのprojectはすべて[NIP-52](/ja/topics/nip-52/) eventを基盤にしています。

### Also shipped: notedeck, nostr.blue, cliprelay, Captain's Log

大きな見出し機能はないものの、複数clientが小刻みなreleaseを出しました。[notedeck](https://github.com/damus-io/notedeck)は[v0.10.0-beta.4](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.4)でcolumn renderingとrelay pool fixを出し、[nostr.blue v0.8.6](https://github.com/patrickulrich/nostr.blue/releases/tag/v0.8.6)はDioxus 0.7.5を取り込み、native audio bridgeを`manganis::ffi` pluginへ変えてAndroid buildを復旧しました。[cliprelay](https://github.com/tajava2006/cliprelay)はDesktop v0.0.3とAndroid v0.0.4を出し、clipboard sync loopを引き締め、32-bit Android variantを落としました。[Captain's Log](https://github.com/nodetec/comet)は、sync relayのliveness detectionを含む3つのalpha buildを公開しています。

## In Development

### whitenoise-rs refactors to session-scoped account views

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)は、[Marmot](/ja/topics/marmot/) clientのRust daemonとして、global singletonからaccountごとの`AccountSession` viewへ移る15本のPRをマージしました。[PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743)が`AccountSession`と`AccountManager`の土台を置き、[PR #753](https://github.com/marmot-protocol/whitenoise-rs/pull/753)がscoped relay handleを追加し、続くphaseでdraftとsetting、message operation、group read/write、membership、push notification、key-package read、group creationを順に移し、[PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770)でevent dispatchまでsession所有へ移しました。目標は、shared monolithを副作用の漏れにくいper-account surfaceへ分解することです。

### White Noise app adds block/unblock UI, leave-group, and offline notices

[White Noise](https://github.com/marmot-protocol/whitenoise)は、missingだったgroup lifecycle controlを追加しました。[PR #578](https://github.com/marmot-protocol/whitenoise/pull/578)はblock/unblock UIを出し、[PR #571](https://github.com/marmot-protocol/whitenoise/pull/571)と[PR #572](https://github.com/marmot-protocol/whitenoise/pull/572)はRust側の`clear_chat`、`delete_chat`、`leave_and_delete_group`をappへ結び、[PR #569](https://github.com/marmot-protocol/whitenoise/pull/569)と[PR #576](https://github.com/marmot-protocol/whitenoise/pull/576)はchatとsettings画面へoffline noticeを追加しました。[PR #585](https://github.com/marmot-protocol/whitenoise/pull/585)は「全key package削除」を「legacy key package削除」へ狭め、migration時にcurrent keyまで消えないようにしています。

### MDK adds mixed-version invite support and SelfUpdate convergence

[MDK](https://github.com/marmot-protocol/mdk)は7本のPRをマージしました。[PR #261](https://github.com/marmot-protocol/mdk/pull/261)はinvitee capabilityのLCDとして`RequiredCapabilities`を計算し、AmethystとWhite Noise間のmixed-version inviteを可能にしました。[PR #264](https://github.com/marmot-protocol/mdk/pull/264)はSelfUpdate wire formatを実装間で収束させ、[PR #262](https://github.com/marmot-protocol/mdk/pull/262)はmalformed inviteeがstray stateを残さないようkey package parse順を修正し、[PR #256](https://github.com/marmot-protocol/mdk/pull/256)と[PR #259](https://github.com/marmot-protocol/mdk/pull/259)はrobustnessを強化し、[PR #265](https://github.com/marmot-protocol/mdk/pull/265)は`group_required_proposals` accessorを公開しました。

### nostter adds NIP-44 encryption across people lists, bookmarks, and mutes

[nostter](https://github.com/SnowCait/nostter)は10本のPRをマージしました。[PR #2088](https://github.com/SnowCait/nostter/pull/2088)はmute listへ、[PR #2089](https://github.com/SnowCait/nostter/pull/2089)はbookmarkへ、[PR #2090](https://github.com/SnowCait/nostter/pull/2090)はpeople listへ[NIP-44](/ja/topics/nip-44/) encryptionを追加し、適用可能な箇所では[NIP-04](/ja/topics/nip-04/)から移行しました。[PR #2087](https://github.com/SnowCait/nostter/pull/2087)は、encrypted kind-10000 flowが安定したためlegacy kind-30000 mute migration pathを削除しています。

### zap.cooking ships Nourish scoring and a reusable comment thread

[zap.cooking](https://github.com/zapcooking/frontend)は今週20本のPRをマージしました。中心機能は新しいNourish recipe scoring moduleで、[PR #317](https://github.com/zapcooking/frontend/pull/317)と[PR #319](https://github.com/zapcooking/frontend/pull/319)がrecipeを栄養軸で評価します。同時に[PR #299](https://github.com/zapcooking/frontend/pull/299)から[PR #302](https://github.com/zapcooking/frontend/pull/302)までの4段階refactorでComments moduleが再利用可能な`CommentThread`へ抽出されました。加えてrecipe scaling、media upload button統一、profile Replies tabも入りました。

### ridestr extracts shared rider coordinator

[ridestr](https://github.com/variablefate/ridestr)は10本のPRをマージし、Compose screenをfocused componentへ分割しつつ、rider/driver protocol logicを共有`:common` coordinator moduleへ抽出しました（[PR #70](https://github.com/variablefate/ridestr/pull/70)）。[PR #60](https://github.com/variablefate/ridestr/pull/60)はRoadflare側向けkind `3189` driver-ping receiverを追加しています。

### Blossom drafts a BUD-01 Sunset header for blob expiration

[Blossom](https://github.com/hzrd149/blossom)は、SHA-256 hashでkey付けされたHTTP blob storage protocolで、[PR #99](https://github.com/hzrd149/blossom/pull/99)を開き、BUD-01へ`Sunset` headerを追加する案を提示しました。serverはこのheaderでblobがいつ配信終了になるかを未来timestampとして広告でき、clientは404へ当たる前にretention制限を把握できます。標準[RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) semanticsを使い、serverは助言として長めに保持しても、best-effortで宣言通り期限を守ってもよい設計です。

## New Projects

### Forgesworn publishes a 29-repo cryptographic toolkit for Nostr

[Forgesworn](https://github.com/forgesworn)は、5日間で29本のopen-source repositoryを公開し、signing、identity、attestation、web of trust、paid API discoveryをまとめたstackを提示しました。signing stackの中心は、1つのmaster secretから無制限のunlinkable Nostr identityを導く[nsec-tree](https://github.com/forgesworn/nsec-tree)と、Tor default-onのRaspberry Pi向け[NIP-46](/ja/topics/nip-46/) remote signerである[Heartwood](https://github.com/forgesworn/heartwood)です。[Sapwood](https://github.com/forgesworn/sapwood)はHeartwoodのweb management UIで、[heartwood-esp32](https://github.com/forgesworn/heartwood-esp32)はHeltec WiFi LoRa 32 board上の同種token logic実験です。[nsec-tree-cli](https://github.com/forgesworn/nsec-tree-cli)はoffline-first operation向けにderivation、proof、Shamir recovery flowを公開します。

identityとtrustでは、[Signet](https://github.com/forgesworn/signet)が[v1.6.0](https://github.com/forgesworn/signet/releases/tag/v1.6.0)へ到達し、QR pairing flowとsession pubkey pinningを備えたdecentralized identity verification protocolを提供します。[nostr-attestations](https://github.com/forgesworn/nostr-attestations)は、credential、endorsement、vouch、provenance、licensing、trustを1つのkind `31000`イベントへ統合し、[nostr-veil](https://github.com/forgesworn/nostr-veil)は[NIP-85](/ja/topics/nip-85/) assertionをsecp256k1上のLSAG ring signatureで支えるprivacy-preserving web of trustを構築します。monetization側では、[toll-booth](https://github.com/forgesworn/toll-booth)がExpress、Hono、Deno、Bun、Cloudflare Workers向けL402 middlewareを提供し、[toll-booth-dvm](https://github.com/forgesworn/toll-booth-dvm)がそれを[NIP-90](/ja/topics/nip-90/) DVMとして公開し、[toll-booth-announce](https://github.com/forgesworn/toll-booth-announce)がkind `31402`のHTTP 402 service discoveryへつなぎます。全体はTypeScript中心、zero-dependency志向で、[anvil](https://github.com/forgesworn/anvil)というbash-only supply-chain-hardened release toolで出荷されています。

### ShockWallet ships Nostr-native Lightning wallet sync and multi-node connections

[ShockWallet](https://github.com/shocknet/wallet2)は、self-custodial Lightning nodeとの接続transportとしてNostrを使うLightning walletです。appは1つ以上の[Lightning.Pub](https://github.com/shocknet/Lightning.Pub) nodeと`nprofile`経由でpairし、walletとnodeの間でpayment authorizationをend-to-endで署名します。[PR #608](https://github.com/shocknet/wallet2/pull/608)はchannels dashboard UIを改善し、[PR #606](https://github.com/shocknet/wallet2/pull/606)は新規PUB user向けadmin-invite-link QR flowを追加し、[PR #607](https://github.com/shocknet/wallet2/pull/607)はmetrics dashboardの可読性を上げました。

ShockWalletは、multi-device wallet state syncに[NIP-78](/ja/topics/nip-01/) application-specific data eventを使います。これによりdesktop browserとphoneのwallet viewをcentralized sync serverなしで一致させます。これは[NIP-47](/ja/topics/nip-47/)のさらに下の層にあり、NIP-47が既存walletへ支払いを依頼するinterfaceであるのに対し、ShockWalletはwallet自身のaccount/session transportとしてNostrを使っています。並行して、teamはwallet-to-app connection向けsession pairing protocolの[CLINK](https://github.com/shocknet/CLINK)も進めています。

### Nostrability issues migrate to git over Nostr after GitHub censorship

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues)は、elsatによるNostr client/relay interop trackerで、GitHub organizationが停止された後、issue workflowをgit over Nostrへ移しています。issue trackerは現在GitWorkshop/ngit上にあり、既存issueも引き継がれ、今後のinterop reportをNostrネイティブなinfrastructure内で扱えるようになりました。

### nowhere encodes full websites into URL fragments and routes orders through Nostr

[nowhere](https://github.com/5t34k/nowhere)は、site全体をURL fragmentにserializeし、dictionary substitutionとraw DEFLATEで圧縮し、base64urlで符号化する新しいAGPL-3.0 projectです。HTTPではfragmentがserverへ送られないため、pageを配るhostは中身を見ず、site自体もserverへ保存されません。projectはevent、fundraiser、store、petition、message、drop、art、forumの8種類を用意し、creatorによる署名とURL単位のpassword encryptionもサポートします。store、forum、petitionではlive communicationが必要で、その通信はephemeral keyと[NIP-44](/ja/topics/nip-44/) encryptionを使ってNostr relay越しに流れます。[nowhr.xyz](https://nowhr.xyz/install) readerにより、短いstore URLはprintable QR codeとしても実用的です。

### Small new surfaces: relayk.it and Brainstorm Search

[relayk.it](https://relayk.it)はSoapbox teamの[sam](https://nostr.com/sam@relayk.it)が作った、[Shakespeare](https://shakespeare.diy)ベースのrelay discovery clientで、完全にbrowser内で動作します。[Brainstorm Search](https://brainstorm.world)は、network全体のcontent surfacingに焦点を当てたsingle-page Nostr search UIとして公開されました。

## Protocol and Spec Work

### NIP Updates

[NIPs repository](https://github.com/nostr-protocol/nips)での最近のproposalとdiscussionです。

**Open PRs and Discussions:**

- **[NIP-67](/ja/topics/nip-67/): EOSE Completeness Hint**（[PR #2317](https://github.com/nostr-protocol/nips/pull/2317)）：relayがfilterに一致する保存済みイベントをすべて返し切ったかどうかを示す、任意の3番目要素を`EOSE`へ追加する提案です。relay上限によって途中で切られたのか、本当に全部なのかをclientが区別できるようにします。
- **NIP-5D: Nostr Applets**（[PR #2303](https://github.com/nostr-protocol/nips/pull/2303)）：[NIP-5A](/ja/topics/nip-5a/)の静的websiteと、進行中の[NIP-5C](/ja/topics/nip-5c/)のWASM scrollの中間にあたる、sandboxed iframe/WebViewで動くinteractive applet配布の提案です。
- **NIP-29: Subgroups spec**（[PR #2319](https://github.com/nostr-protocol/nips/pull/2319)）：1つのgroup内に複数parallel channelを持てるsubgroup hierarchyを追加し、旧client向けの単一`h`タグ形を保つ案です。
- **NIP-29: Explicit role permissions on kind 39003**（[PR #2316](https://github.com/nostr-protocol/nips/pull/2316)）：kind `39003` role eventへ明示permission schemaを導入し、`moderator`のようなroleがrelayごとに別意味になる問題を減らす提案です。
- **NIP-11: access_control field for gated-relay discovery**（[PR #2318](https://github.com/nostr-protocol/nips/pull/2318)）：relayのgating modeとaccess request endpointを示す`access_control` objectを追加する案です。
- **NIP-63a: Minimal Payment Gateway Descriptor**（[PR #2315](https://github.com/nostr-protocol/nips/pull/2315)）：先週扱ったkind `10164` payment gateway descriptorのfield layout調整が続いています。
- **NIP-XX: Agent Reputation Attestations (Kind 30085)**（[PR #2320](https://github.com/nostr-protocol/nips/pull/2320)）：Nostr上のautonomous agentやserviceについて、reliabilityやhonest advertisingを署名付きで評価するkind `30085` addressable eventを提案します。
- **NIP-TPLD: Transient Private Location Data**（[PR #2309](https://github.com/nostr-protocol/nips/pull/2309)）：kind `20411`、recipientごとの[NIP-44](/ja/topics/nip-44/) encryption、`ttl` tag semanticsの議論が続いています。
- **marmot-ts 0.5.0 release PR**（[PR #70](https://github.com/marmot-protocol/marmot-ts/pull/70)）：TypeScript Marmot clientのbreaking change群をまとめたrelease PRで、legacy kind `443`と新kind `30443`両対応、constructorとstorage layerの見直しが含まれます。

## NIP Deep Dive: NIP-72 (Moderated Communities)

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md)は、topic-based communityをNostr上で扱うためのモデルです。relayがmembershipとmoderationのauthorityになる[NIP-29](/ja/topics/nip-29/)とは異なり、NIP-72 communityは通常のNostr eventとして存在し、関係するkindを運べるrelayならどこでも配信できます。誰でも投稿でき、認識済みmoderatorが承認した投稿だけがcommunity feedに表示されます。

communityはkind `34550`のaddressable eventで定義されます。`d`タグが安定slugになり、`name`、`description`、`image`、`rules`タグが表示用metadataを持ち、`p`タグに`moderator` markerを付けてmoderator pubkeyを列挙します。`relay`タグには`author`、`requests`、`approvals`といったmarkerを付けて、どこへどの種別のイベントを出すべきかのhintを載せられます。ユーザーはkind `1` noteやkind `30023` articleなど任意の通常イベントへ、community coordinateである`34550:<creator_pubkey>:<slug>`を値に持つ`a`タグを追加して投稿します。その投稿はそれ単体でも有効なNostr eventですが、community-aware clientは認識済みmoderatorのapprovalが付いたものだけをcommunity feedへ出します。

approvalはmoderatorが公開する別個のkind `4549`イベントです。そこにはsubmissionを指す`e`タグ、投稿者を指す`p`タグ、communityを指す`a`タグが入り、`content`にはstringifyされたsubmission eventがcache copyとして埋め込まれます。これにより、元投稿が後で消されても承認済みpostをrenderできます。approval modelの利点は3つあります。moderation判断が透明でaudit可能であること、同じ投稿が複数communityで承認され得ること、そしてkind `34550`からmoderatorが外されれば、そのmoderatorの古いapprovalがread layerで無効化されることです。NIP-72は、spamをwireに流したくないclosed spaceより、curated front page的なpublic topic communityに向いています。

## NIP Deep Dive: NIP-57 (Zaps)

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)は、Lightning paymentをNostr identityやeventへ結び付け、かつ検証可能な支払いreceiptをrelayへ戻す方法を定義します。senderが誰で、いくらを、誰へ、どの対象のために支払ったかをNostr clientが検証可能な形で見られるようにする仕様で、LNURL、Lightning、Nostrの3層をまたいでいます。

flowには4つのactorがいます。senderのclientは、recipientのkind `0` profile metadataの`lud06`または`lud16`、またはzap対象イベントの`zap`タグからLNURL endpointを見つけます。そのclientは意図した支払いを記述するkind `9734` zap requestを署名し、relayではなくrecipientのLNURL callbackへ送ります。recipient側のLNURL serverはrequestを検証し、description hashがrequest eventの文字列表現へコミットするLightning invoiceを返し、senderが支払うとsenderが指定したrelay setへkind `9735` zap receiptを公開します。zap requestには`p`タグ、任意の`e`または`a`タグ、`amount`、`relays`、任意のmessageを入れる`content`、対象kindを示す`k`タグが入ります。zap receiptには`description`タグ内のrequest全文、`bolt11`、`preimage`が入り、recipientのLNURL responseでadvertiseされた`nostrPubkey`でwallet serverが署名します。

clientがkind `9735` receiptをzapとして表示するなら、4点を検証すべきです。receipt署名がLNURL `nostrPubkey`と一致すること、`bolt11`金額が埋め込みrequestの`amount`と一致すること、invoiceのdescription hashがstringified requestへコミットしていること、`preimage`がinvoiceの`payment_hash`へハッシュされることです。これをしないzap count集計は簡単に偽造されます。private zapでは`content`を暗号化して`anon`タグを付け、anonymous zapではephemeral keypairまで新しく生成します。NIP-57はさらに[NIP-75](/ja/topics/nip-75/) zap goalの土台にもなっており、[Amethyst](https://github.com/vitorpamplona/amethyst)の[PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469)はこの週、[NIP-53](/ja/topics/nip-53/) Live Activities画面でgoal progressとtop-zapper leaderboardを描画するようにしました。付録で定義されるzap splitにより、1回のzapを複数recipientへweight付きで分配することもできます。

---

今週は以上です。何か作っているものがある、または共有したい更新がある場合は、NostrでDMを送るか、[nostrcompass.org](https://nostrcompass.org)で見つけてください。
