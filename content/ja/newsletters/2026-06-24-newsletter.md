---
title: 'Nostr Compass #28'
date: 2026-06-24
publishDate: 2026-06-24
translationOf: /en/newsletters/2026-06-24-newsletter.md
translationDate: 2026-06-24
draft: false
type: newsletters
---

Nostrの週刊ガイド、Nostr Compassへようこそ。

**今週:** [SproutはBuzzへ改名](#sprout-rebrands-to-buzz-and-publishes-personas-teams-and-managed-agents-as-relay-events)し、persona、team、managed agentの記録をNostr relay eventとして公開し始めました。従来のbadge frontierモデルは、デバイス間の既読状態とメッセージごとの既読マーカーに置き換わります。sandwich.farmの[Napplets](#napplets-composable-nostr-apps-with-a-defined-trust-boundary)は、NostrとBlossom上で配布される組み合わせ可能なNostrアプリのためのtrust boundary protocolとして登場します。[Conduit](#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default)（購入者向けMarket、Merchant Portal、Store BuilderからなるNostr上の3アプリ構成のmarketplace monorepoで、独自のNIPおよび仕様ディレクトリをリポジトリ内に持つ）は、marketplace MVPを強化する17件のPRをマージし、デフォルトを公開relayへ切り替え、プライバシーに配慮した分析機能を追加しました。[BitBlik](#bitblik-launches-a-p2p-blik-to-lightning-exchange-protocol-over-nostr)は、暗号化されたNostr DM上で動くP2PのBLIK・Lightning交換protocolを出荷し、coordinatorが法定通貨とLightning hold invoiceの間をアトミックに決済します。[Amethyst](#amethyst-patches-follow-up-the-v1120-launch)は、先週のwallet、podcast、workoutを含むローンチに続き、Health Connect Workouts、Road Events、折りたたみ可能な返信、分類器付きrelay遅延ヘルス追跡、macOS公証の修正を追加しました。[Amber](#amber-implements-nip-46-client-metadata)は先週提案されたNIP-46 client metadata拡張を実装し、signerのリクエスト画面にネイティブアプリのアイコンとidentityを表示します。[Haven](#haven-launches-private-location-sharing-on-marmot)はMarmot暗号化メッセージングprotocol上で非公開の位置共有を開始しました。[CodeDeck](#codedeck-remote-agentic-coding-over-nostr)は暗号化Nostr relayを通じ、スマートフォンからノートPC上のClaude Codeセッションを操作可能にし、pairingを1回のQRスキャンへまとめ、さらにセッションごとのモデル選択を追加しました。[Grain](#grain-ships-a-full-nostr-client-engine)はoutbox modelを実装したimport可能なGo Nostr client libraryを出荷します。Mostro Core、WispとDark Wisp、Citrine、FIPS、Kubo（保護者が選ぶYouTubeチャンネルと必須のtrust-gated子ども向けfeed）、Pollerama（web-of-trustスコア、端末内relay engine、「知り合いかもしれない人」欄）は後続patchを出荷しました。未リリースの作業では、sandwich.farmのブラウザベースMLS coordinator、nostterのUX改善スプリント、Zap Cookingのプロジェクト横断NIP-46修正とcomposer刷新、ShopstrのCashu escrow lifecycle、divine.video、Nosturを扱います。新たな追跡対象はSocial Agents Prototype、git-over-Nostr issueをtriageするPRana、routstr-chatです。protocol面では、NIP-99にon-graph checkoutおよびescrowの提案が加わり、Conduit、BitBlik、Shopstrのcommerce作業と直接つながります。6月最後のCompassとなるため、本号は[「Nostrの6年間の6月」](#six-years-of-nostr-junes)で締めくくります。

---

## トップストーリー

### Amethyst v1.12.1からv1.12.6がv1.12.0ローンチをフォローアップ {#amethyst-patches-follow-up-the-v1120-launch}

[Amethyst](https://github.com/vitorpamplona/amethyst)は[先週のv1.12.0ローンチ](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)に続き、水曜日から金曜日までに6件のpatchを相次いで公開しました。[v1.12.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.1)はHealth Connect Workoutsと画像として共有する操作を追加し、Torの`Active`フラグを決定論的にしてbootstrap callbackがgateと競合しないようにします。[v1.12.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.2)はRoad Eventsと折りたたみ可能な返信を追加し、[v1.12.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.3)は分類器およびdashboard UIを備えたrelay遅延ヘルス追跡とmacOS公証の修正を導入しました。[v1.12.4](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.4)から[v1.12.6](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.6)まではCrowdin翻訳更新と翻訳者クレジットの自動化を出荷します。

### SproutはBuzzへ改名しpersona、team、managed agentをrelay eventとして公開 {#sprout-rebrands-to-buzz-and-publishes-personas-teams-and-managed-agents-as-relay-events}

[Sprout](/en/newsletters/2026-04-29-newsletter/#sprout-adds-owner-attestation-and-multi-workspace-support)は、Blockが開発するself-host可能なworkspaceです。人間とAI agentが同じchannelで協働し、すべてのメッセージ、reaction、workflow step、review承認、git eventが署名済みNostr eventとして記録されます。このプロジェクトは今週、[Buzz](https://github.com/block/buzz)へ改名されました。GitHubは旧`block/sprout` slugを`block/buzz`へredirectするようになりましたが、リポジトリ、ライセンス、製品方針は変わりません。過去号のSproutに関する記事はすべて同じプロジェクトを指します。

改名とともに、大規模な製品作業もマージされました。[PR #1189](https://github.com/block/buzz/pull/1189)によりpersona、team、managed agentの記録がNostr relay eventとして公開され、状態を複製せずに同じagent identityを複数のworkspaceとaudit logへ表示できます。新しいdesktop paneはprofileにNIP-OA owner attestationを表示し（[PR #1198](https://github.com/block/buzz/pull/1198)）、channel threadの未読badge frontierをメッセージごとの既読マーカーへ置き換えて、デバイス間で未読数を正確に保ちます（[PR #1178](https://github.com/block/buzz/pull/1178)）。inboxではreminder eventに著者とsourceの帰属情報が加わりました（[PR #1176](https://github.com/block/buzz/pull/1176)）。

一時channelの有効期限はデフォルトで7日になり（[PR #1182](https://github.com/block/buzz/pull/1182)）、agentごとのrelay overrideはworkspaceのデフォルトへfallbackする前に設定済みrelayを優先します（[PR #1131](https://github.com/block/buzz/pull/1131)）。Windows buildにはshell tool用の完全なGit for Windows toolchainが同梱されるようになりました（[PR #1145](https://github.com/block/buzz/pull/1145)）。

### Napplets: 明確なtrust boundaryを持つ組み合わせ可能なNostrアプリ {#napplets-composable-nostr-apps-with-a-defined-trust-boundary}

Sandwich.farmは今週、組み合わせ可能なNostr applet、すなわちnappletのprotocolとして[napplet.run](https://napplet.run)を発表しました。nappletは1つのことを行う小さなprogramで、sandbox環境で実行され、nsiteと同じevent形式を使ってNostrとBlossom上から解決されます。プロジェクトは3つのリポジトリにまたがります。[napplet/web](https://github.com/napplet/web)はweb packageを収め、今週の一斉ローンチで51件のsubpackage version tag（`@napplet/core`、`@napplet/sdk`、`@napplet/nap`、`@napplet/shim`、`@napplet/conformance`）を切りました。[napplet/naps](https://github.com/napplet/naps)は15件のPRがマージされたNAP仕様群、[kehto/web](https://github.com/kehto/web)は41件のPRがマージされたweb runtimeで、[kehto.github.io/web/playground](https://kehto.github.io/web/playground)にplaygroundがあります。対応する仕様PRはdskvr（sandwich.farm）が提出した[NIP-5D #2303](https://github.com/nostr-protocol/nips/pull/2303)です。

設計上の前提はprotocol層で定義されるtrust boundaryです。shellは署名、鍵へのアクセス、relayへの書き込みといった危険な操作を仲介し、runtimeは実装と上位UXを処理するため、nappletは可搬で使い捨て可能なまま、単一hostに囲い込まれにくくなります。napplet同士は同じshellを通じて通信でき、設計上runtimeへのlock-inはありません。著者はnappletをNMP（Pablof7z）およびTiles（Soapbox）と同じ問題への並行した取り組みとして位置づけ、Amethyst v1.12.6の[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)と[NIP-5D](/ja/topics/nip-5d/)サポートにより、ローンチ時点で少なくとも1つの実稼働clientがあると述べています。歴史的経緯として、sandwich.farmの以前の`napp.run`（NIP-07 native app prototype）とThorium forkの`dryft` browserが、棚上げされる前に現在の設計へ影響を与えました。

### Conduitがmarketplace MVPを強化しデフォルトを公開relayへ変更 {#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default}

[Conduit](https://github.com/Conduit-BTC/conduit-mono)は`Conduit-BTC`組織が[conduit.market](https://conduit.market)で提供する3アプリ構成のmarketplace monorepoです。購入者向けMarket、Merchant Portal、Store Builderを含み、リポジトリ内の`nips/`と`specs/`ディレクトリでConduit固有のNostr commerce primitiveを定義します。下層では[Conduit-BTC/conduit-relay](https://github.com/Conduit-BTC/conduit-relay)というScope-2 [khatru](https://github.com/fiatjaf/khatru)拡張が動作します。両リポジトリは今年初めに公開され、今週はmarketplace MVPを強化する17件のPRがマージされました。

出荷されたPRはmarketplaceの正確性に集中しています。出品の安全状態（[PR #110](https://github.com/Conduit-BTC/conduit-mono/pull/110)）とmerchant側の商品価格および配送zoneの強化（[PR #115](https://github.com/Conduit-BTC/conduit-mono/pull/115)）です。relay側では、[PR #102](https://github.com/Conduit-BTC/conduit-mono/pull/102)がcommerce capabilityの検出を修正し、[PR #112](https://github.com/Conduit-BTC/conduit-mono/pull/112)が第三者の安全でないrelay hintを無視し、[PR #128](https://github.com/Conduit-BTC/conduit-mono/pull/128)が新規clientのデフォルトを公開Conduit relay domainに設定します。プライバシーに配慮した分析機能は[PR #109](https://github.com/Conduit-BTC/conduit-mono/pull/109)と[PR #129](https://github.com/Conduit-BTC/conduit-mono/pull/129)で導入され、`dompurify`の更新はOSV advisoryを解消します（[PR #116](https://github.com/Conduit-BTC/conduit-mono/pull/116)）。これらは今週のより大きな[NIP-99](/ja/topics/nip-99/) commerceの動きに含まれます。[PR #2323](https://github.com/nostr-protocol/nips/pull/2323)はorder flow、escrow、disputeを扱うNIP-99 market向けon-graph checkout layerを提案し、NIP-99を完全なe-commerceへ拡張してきた[Gamma Markets Market Spec](https://github.com/GammaMarkets/market-spec)はConduitなどが構築する仕様層となり、Shopstrも同じ週にCashu escrow lifecycleを出荷しました。

### BitBlikがNostr上のP2P BLIK・Lightning交換protocolをローンチ {#bitblik-launches-a-p2p-blik-to-lightning-exchange-protocol-over-nostr}

[BitBlik](https://github.com/bit-blik/bitblik)は今週、Nostr上に構築されたP2PのBLIK ↔ Lightning交換protocolとして公開されました。BLIKはポーランドの銀行が発行する即時決済方式です。BitBlik coordinatorはtakerが支払うBLIK法定通貨とmakerが資金を提供するLightning hold invoiceの間をアトミックに決済し、取引のlifecycleはNostr上で進みます。Flutter app、CLI、coordinatorは`core` packageを共有し、GitHub monorepoの`bit-blik/bitblik`、[www.bitblik.app](https://www.bitblik.app)のweb build、Zapstore appの`app.bitblik`を通じて提供されます。

protocolはclientとcoordinator間のRPCに暗号化されたNostr DM（[NIP-44](/ja/topics/nip-44/)）を使います。offerはkind `38383`のparameterized replaceable event、RPC requestはkind `25195`、RPC responseはkind `25196`、status updateはkind `25197`として公開されます。coordinatorはtakerがBLIK codeを送信する間Lightning hold invoiceを保持し、BLIK送金が確認されるとpreimageを解放し、invoiceの決済をmakerへ送ります。

---

## タグ付きリリース

### Amber v6.2.2がNIP-46 client metadataを実装 {#amber-implements-nip-46-client-metadata}

[Amber](https://github.com/greenart7c3/Amber)はgreenart7c3が保守する主要なAndroid向け[NIP-46](/ja/topics/nip-46/) remote signerです。対応する仕様PRがマージされたのと同じ週に[v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2)を出荷しました。このリリースはrequest画面とapp一覧にnative app iconと新しいclient metadata fieldを表示し、接続のたびにclient metadataを永続化し、接続時と承認時にnative app iconと名称を取得します。この変更はDocNRによる[NIP-46 PR #2381](https://github.com/nostr-protocol/nips/pull/2381)と直接対応します。同PRはconnect requestへ任意のclient metadataを追加し、signerがrequest元の分かりやすい名称とiconを表示できるようにします。Amber v6.2.2はevent kind 30618もサポートし、Active relay画面でデフォルトrelayと接続relayを分離します。

このリリースはsignerのsecurity surfaceも強化します。復号済みNIP-46 requestおよびresponse本文はlogへ出力されなくなり、encryptおよびdecrypt payloadはciphertextとして保存され、必要時に復号されます。すべてのlogcat出力は`BuildConfig.DEBUG`の背後に置かれ、browser呼び出し元（packageがnull）は常に確認する設定へ強制され、clipboardへcopyされた`nsec`、`ncryptsec`、seed wordは機密扱いとなり一定時間後に消去されます。多層防御としてbackupとdata extractionの明示的な除外も追加されました。Active relayのnested scrollによるcrash、bunker requestの競合する重複排除による`LazyColumn`のduplicate key crash、release update確認時の`EOSE`競合も修正しています。

### HavenがMarmot上で非公開の位置共有をローンチ {#haven-launches-private-location-sharing-on-marmot}

[Haven](https://github.com/mehmetefeumit/Haven-App)は、[Marmot](/ja/topics/marmot/) protocolを使ってNostr上で動作するAndroidおよびiOS向けの非公開で検閲耐性のある位置共有appとして今週公開されました。新規プロジェクトの初回リリースとして、4日間に[v0.1.0](https://github.com/mehmetefeumit/Haven-App/releases/tag/v0.1.0)から[v0.1.4](https://github.com/mehmetefeumit/Haven-App/releases/tag/v0.1.4)まで5件を出荷しました。HavenはDartとFlutterで構築され、developer署名済みappとしてZapstoreから公開されます。Nostr向けMLSベースのend-to-end暗号化メッセージング層であるMarmotがgroup stateとciphertext配布を担い、Havenはこの形式をメッセージングから位置共有へ拡張します。各groupの暗号化stateには、そのgroupが共有に同意した位置情報updateが含まれます。

### CodeDeck: Nostr経由のremote agentic coding {#codedeck-remote-agentic-coding-over-nostr}

[CodeDeck](https://github.com/JeroenOnNostr/codedeck)は、Androidとdesktop向けのmulti-session agentic coding interfaceとして今週公開されました。Tauri v2、React 19、Rust backendで構築され、暗号化Nostr relayを通じてスマートフォンからノートPC上の[Claude Code](https://www.anthropic.com/claude-code)セッションを操作できます。同じ4日間に[v2026.06.17](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.06.17)、[v2026.6.18](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.6.18)、[v2026.6.20](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.6.20)を出荷しました。transport modelはNostrを暗号化control planeとして使います。CodeDeckを動かすスマートフォンがcommandを暗号化eventとして公開し、ノートPCの隣で動くbridgeがそれを購読し、ノートPCは同じrelayを通じてsession outputを送り返します。

v2026.06.17は`nostr-vpn` FIPS meshをappのAndroid VPN serviceとして組み込みます。これによりノートPCはどこからでも物理test phone上でappの開発buildを構築、install、起動、操作でき、test phone側に必要なsoftwareはCodeDeckだけです。v2026.6.18はpairingとmesh inviteを1回のQR scanにまとめ、v2026.6.20はセッションごとのモデル選択を追加し、各sessionを選択済みmodelで開始できるようにします。

### Grain v0.8.0-rc1が完全なNostr client engineを出荷 {#grain-ships-a-full-nostr-client-engine}

[Grain](https://github.com/0ceanSlim/grain)は0ceanSlimが保守するGo relayです。[v0.8.0-rc1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc1)を公開し、Nostr relayであると同時に、その実装を支えるimport可能なGo client libraryとなりました。v0.7.xがbrowserからrelayを運用することに重点を置いたのに対し、v0.8系は`client/core`を出荷します。これはcgoにもHTTPにも依存しないpure Goの独立したoutbox-model Nostr client engineです。engineは共有relay poolを管理し、各userのrelay listを解決し、すべてのreadとpublishを[gossip / outbox model](https://mikedilger.com/gossip-model/)に従ってroutingします。userのnoteはそのuserのoutbox relayから読み、公開した返信は親著者のinbox relayへ届きます。Grain自身のweb frontendがこのlibraryのreference consumerになったため、UIは利用可能なappであると同時に下流Goプロジェクト向けの実装例でもあります。

リリースはnative [NIP-44](/ja/topics/nip-44/)暗号化（v2とv3）、[NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) relay AUTH、[NIP-65](/ja/topics/nip-65/)、[NIP-17](/ja/topics/nip-17/)、[NIP-51](/ja/topics/nip-51/)、[NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md) relay list、[NIP-89](/ja/topics/nip-89/) client tag、[Blossom](/ja/topics/blossom/)と[NIP-96](/ja/topics/nip-96/) media supportを導入します。relay routingを独自に再実装していた下流Go appはengineを直接`import`できるようになりました。

### Mostro Core v0.13.1がProtocol v2をフォローアップ

[Mostro Core](https://github.com/MostroP2P/mostro-core)は[v0.13.1](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.1)を[先週のProtocol v2展開](/en/newsletters/2026-06-17-newsletter/#mostro-core-v0130-cuts-the-relay-middleman-with-protocol-v2)に続くリリースとして出荷し、protocolのprice feed契約に`PriceTooStale` error variantを導入しました。今週のdaemon側では、[PR #752](https://github.com/MostroP2P/mostro/pull/752)が無効なorder IDを黙って破棄せず`CantDo(NotFound)` errorとしてclientへ示し、[PR #785](https://github.com/MostroP2P/mostro/pull/785)が内部protocol versionをactive transportに追従させます。[PR #778](https://github.com/MostroP2P/mostro/pull/778)はCUPおよびMLC向けEl Toque fiat-cross providerのphase 3を導入し、[PR #782](https://github.com/MostroP2P/mostro/pull/782)は仕様に合わせて[NIP-33](https://github.com/nostr-protocol/nips/blob/master/33.md) info tagの`protocol_versions`を`protocol_version`へ改名します。

### Wisp v1.1.2とDark Wisp variant

[Wisp](https://github.com/barrydeen/wisp)はbarrydeenによるKotlinおよびJetpack Compose製Android clientです。[v1.1.2](https://github.com/barrydeen/wisp/releases/tag/v1.1.2)ではself-send wallet legを決定論的なtransaction順序内で別々に保持し（[PR #586](https://github.com/barrydeen/wisp/pull/586)）、mediaの多いnoteでも動作するようinline video playerを遅延作成し（[PR #592](https://github.com/barrydeen/wisp/pull/592)）、event relay集合の`ConcurrentModificationException`を修正し（[PR #595](https://github.com/barrydeen/wisp/pull/595)）、chat bubble内容のintrinsic measurementを修正して`SubcomposeLayout` crashを回避しました（[PR #596](https://github.com/barrydeen/wisp/pull/596)。リリースはlock外でspam scoringを行うincremental feed filterも導入します。Wisp teamは今週、ZEC、DASH、BCH、LTCのzap targetと匿名modeを追加したmulti-currency variant、Dark Wisp v1.1.0もZapstoreで公開しました。

### Citrine v3.0.1

[Citrine](https://github.com/greenart7c3/Citrine)はgreenart7c3によるAndroid local Nostr relayです。[v3.0.1](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.1)は1件の修正を出荷しました。未登録のPokey receiverを登録解除した際のcrashでrelay全体が停止しなくなります。

### FIPS v0.4.0-rc2

[FIPS](https://github.com/jmcorgan/fips)（Free Internetworking Peering System）は、v0.3.x wire formatを基にしたpackage検証用release candidateとして[v0.4.0-rc2](https://github.com/jmcorgan/fips/releases/tag/v0.4.0-rc2)をtag付けしました。v0.4.0系はpeer到達性のためのNym mixnet transportとopt-in mDNS LAN discoveryを追加し、data planeを刷新して単一nodeのthroughputを高めpacketあたりのCPU負荷を下げます。operator向けread surfaceをdata planeのhot pathから外し、負荷下でも可観測性の応答を維持し、再設計した`fipstop` TUIを出荷し、packet loss下でも途切れないようFMPとFSPのrekeyを強化します。これはrelease candidateであり、v0.4.0 stable版は暫定的に2026-06-21とされています。

### Kubo v2026.06.12とv2026.06.20がtrust-gated子ども向けfeedを固定し保護者選定YouTubeを追加

[Kubo](https://github.com/JeroenOnNostr/kubo)はJeroenOnNostrがTrust Extended Permissions Protocol（TEPP）上に構築したNostr-nativeなYouTube Kids代替appです。今週2件のリリースを出荷しました。[v2026.06.12](https://zapstore.dev/apps/com.kubo.app)（calendar versioning、派生`versionCode`は`YYYYMMDD`）はtrust-gated子ども向けfeedを必須にします。子どもが閲覧または操作できるすべてのpost、profile、reaction、repostは、保護者が許可した人物に限定されたTEPPを経由します。新規installではtrust gateが有効で始まり、onboarding時に子どものcircleが初期化されるため、初回起動からfeedが保護されます。保護者向けmanaged group chatも追加し、trust eventを家族のprivate relay集合へ送り、trust dataを読み込めない場合は未審査内容を漏らす代わりに何も表示しないfail-closed動作を取ります。

[v2026.06.20](https://zapstore.dev/apps/com.kubo.app)は保護者が選定するYouTube channelを追加します。保護者がchannelを検索して子ども向けfeedへ加えると、子どもには保護者が承認したchannelの動画だけが表示されます。HTTP fast laneとoptimistic UIにより約10秒かかっていた追加経路も置き換えました。このリリースはTrust Extended Permissionsを無効にするoptionも削除します。プロジェクトは必須trustを中心に設計されているため、toggleは常にonです。専用Support pageを追加し、group chatの`@mention`を修正してrawな`nostr:npub1…`ではなくclick可能な`@name`を表示し、mention autocompleteを加え、trust公開のgate判定をmirror flagではなく実際の適用状態に基づかせます。両リリースはdeveloper署名済みAndroid app `com.kubo.app`としてZapstoreで追跡されています。

### Pollerama v1.9.0からv1.9.4がweb-of-trustスコア、端末内relay engine、「知り合いかもしれない人」欄を追加

[Pollerama](https://github.com/formstr-hq/nostr-polls)はabh3poによるForm*系のNostr pollおよびfeed clientで、[pollerama.fun](https://pollerama.fun)で提供されています。今週Zapstoreで5件のリリースを出荷しました。v1.9.0は新しい端末内relay engineを導入します。内蔵local relayがuserの閲覧したすべてを保存し、まずlocal cacheからappへ応答するため、feed、profile、threadは即座に読み込まれ、offlineでも利用でき、背後でnetworkと同期されます。すべてのrelay traffic（readとwrite）はmain thread外でこのengineを経由し、読み込み済みのnote、profile、reaction、zapは再取得せずlocal storageから直接提供されます。

v1.9.2は、follow listをsync engineと独立してcacheすることで、HomeとNotes feed（およびFollowing・Network view）が起動時や復帰時に空になることがある問題を修正しました。DM内で共有されたnoteは、userが著者をfollowしていなくてもrelay hintから参照先noteを取得して確実に読み込みます。relay接続、cache size、sync stateを表示し、再接続またはlocal cacheの消去を行えるNetwork設定panelも追加されました。v1.9.3は起動時crashとHome feed読み込みのregressionを修正します。

v1.9.4はprofileにweb-of-trust trust score（自分がfollowする人のうち何人がこの人物もfollowしているかをnetwork chipとして表示）と、「知り合いかもしれない人」欄（web of trustから得たfollow候補を、自分のfollowのうち何人がその人物をfollowしているかで順位付け）を追加します。Network設定はweb-of-trustの規模と最終計算時刻を表示し、任意に再計算するbuttonも備えます。trust scoreとrecommendationはweb-of-trust workerがbackgroundで計算するためappをblockしません。

### その他のタグ付きリリース

[nogringo/nostr-mail-client v0.13.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.13.1)はAmber、Aegis、Primalでの[NIP-55](/ja/topics/nip-55/) signer app loginを復旧し、signer appへcontactの署名を繰り返し要求しないようにします。[Cameri/nostream v3.0.0](https://github.com/Cameri/nostream/releases/tag/v3.0.0)はweb app factoryから`unsafe-inline`を削除し、script nonceを実装します。[LaWallet NWC v1.0.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v1.0.0)は共有可能なQR linkによるcard有効化、Remote Wallet認識、Lightning Address自動発行を備えたプロジェクト初の1.0です。[Formstr Nostr Calendar v2.0.0からv2.0.2](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.0.2)はPWAを追加し、offline replaceable eventを修正し（[PR #194](https://github.com/formstr-hq/nostr-calendar/pull/194)）、signer methodをbindしてprivate formを送信可能にしました（[PR #199](https://github.com/formstr-hq/nostr-calendar/pull/199)）。[Spl0itable/NYM](https://github.com/Spl0itable/NYM)、[codeswot/ZapBook](https://github.com/codeswot/ZapBook)、[77elements/noornote](https://github.com/77elements/noornote)、[mattn/nostr-relay](https://github.com/mattn/nostr-relay)、[mattn/algia](https://github.com/mattn/algia)、[mouse484/astraea](https://github.com/mouse484/astraea)、[dergigi/boris](https://github.com/dergigi/boris)、[fiatjaf/nak](https://github.com/fiatjaf/nak)、[Spl0itable/nosflare](https://github.com/Spl0itable/nosflare)、[nostrord/nostrord](https://github.com/nostrord/nostrord)からの小規模なリリースが今週を締めくくります。

---

## 未リリースの変更

### Cordn Ad-hoc CVM: ブラウザベースのMLS coordinator

[Cordn Ad-hoc](https://github.com/sandwichfarm/cordn-adhoc-cvm)はsandwich.farmの新しいweb appで、ad-hocな[Cordn](https://github.com/Cordn-msg/cordn) group向けにbrowser tab内で動作するMLS coordinatorとして今週公開されました。この形式は独特です。browser tabが[ContextVM](/ja/topics/contextvm/) Nostr coordinator processを実行し、coordinator pubkeyを公開し、Nostr relay経由でMCP requestを受信し、MLS key package、Welcome、join request、group messageをbrowser storageへ保存します。backendはありません。appは同じpubkeyを持つ複数のcoordinatorが同時に動くことを防ぎ、raw Nostr event、decode済みrequest、instance heartbeatを確認するoperator debug logを提供します。

### SnowCait/nostterが19件のUX改善PRを出荷

[nostter](https://github.com/SnowCait/nostter)はSnowCaitのweb Nostr clientです。今週はreleaseを切らずに19件のPRをマージしました。`nostrapp.link`を`app-manager.nostter.app`へ置き換え（[PR #2234](https://github.com/SnowCait/nostter/pull/2234)）、`deck.nostter.app`を`frame-ancestors` allowlistへ追加する変更（[PR #2233](https://github.com/SnowCait/nostter/pull/2233)）により、プロジェクトのsurfaceを`nostter.app` domainへ集約します。followeeのreplaceable eventはIndexedDBへcacheされ（[PR #2231](https://github.com/SnowCait/nostter/pull/2231)）、seen-on relay stateはseen-onとviaのoptionを分離してreactivityを取り戻しました（[PR #2230](https://github.com/SnowCait/nostter/pull/2230)）。

### Zap Cookingがプロジェクト横断NIP-46 bugを修正しcomposerを刷新

[Zap Cooking](https://github.com/zapcooking/frontend)はNostr上のレシピ共有clientです。今週16件のPRをマージしました。影響範囲が最も広い変更は[PR #452](https://github.com/zapcooking/frontend/pull/452)です。Primal remote signerがeventへsigner自身のpubkeyを付けていたため、Primalを経由するすべてのclientでupload、zap、authが壊れていました。Zap Cookingはこの経路を発見してpatchしました。修正はclient内ですが、bugは[NIP-46](/ja/topics/nip-46/)全体に存在します。[PR #458](https://github.com/zapcooking/frontend/pull/458)はcountdown timer、統一されたreply・comment UI、Write・Preview tabを備えたcomposerへ再構築します。3件のSSR修正（[PR #460](https://github.com/zapcooking/frontend/pull/460)、[PR #461](https://github.com/zapcooking/frontend/pull/461)、[PR #462](https://github.com/zapcooking/frontend/pull/462)）と[PR #454](https://github.com/zapcooking/frontend/pull/454)はprofileとrecipe routeを安定化しました。explore画面はdrag scrollできる行、profile link付きavatar cursor、community向けsticky tab修正を追加します（[PR #456](https://github.com/zapcooking/frontend/pull/456)）。

### ShopstrがCashu escrow lifecycleとstorefront toolを出荷

[Shopstr](https://github.com/shopstr-eng/shopstr)は[NIP-99](/ja/topics/nip-99/) marketplaceです。今週、一連の重要なPRをマージしました。[PR #512](https://github.com/shopstr-eng/shopstr/pull/512)はmarketplace向けにend-to-endのP2PK Cashu escrow lifecycleを実装します。これは同じ週に進む[NIP-99 PR #2323](https://github.com/nostr-protocol/nips/pull/2323)（on-graph checkout layer提案）およびConduitのローンチを含む、より広範なcommerceの動きにつながります。出品企業一覧、企業詳細、storefront、seller reputationを取得するread toolは[PR #543](https://github.com/shopstr-eng/shopstr/pull/543)で導入されます。[PR #229](https://github.com/shopstr-eng/shopstr/pull/229)はprofileおよびshop画像のURL貼り付けを追加し、[PR #359](https://github.com/shopstr-eng/shopstr/pull/359)はmarketplace統計取得にtimestampを含めます。



### divine.videoのmobileおよびdesktop作業

[divine.video](https://github.com/divinevideo/divine-mobile)はrabbleによる、復元したVine archiveを備えた短尺loop video clientです。今週マージされたPRは再生と編集に集中しています。addressable videoをfeed内で重複排除し（[PR #5465](https://github.com/divinevideo/divine-mobile/pull/5465)）、local Nostr tag filterを完全一致にして偽の結果を避け（[PR #5463](https://github.com/divinevideo/divine-mobile/pull/5463)）、video editorがsticker layer付きdraftをcrashせず復元し（[PR #5474](https://github.com/divinevideo/divine-mobile/pull/5474)）、Messages badgeはfollow済みながら未返信の未読chatを数えるようになりました（[PR #5473](https://github.com/divinevideo/divine-mobile/pull/5473)）。

### NosturがNIP-46 client metadataサポートとDM更新修正を出荷

[Nostur](https://github.com/nostur-com/nostur-ios-public)はFabianによるiOS clientです。[先週の1.29.0リリース](/en/newsletters/2026-06-17-newsletter/#nostur-1290-ships-anonymous-replies-and-remote-signer-logout)に続き、canonical repoへ4件のPRをマージしました。[PR #74](https://github.com/nostur-com/nostur-ios-public/pull/74)はNIP-46 bunker connect requestへclient metadataを追加します。これはDocNRが提案し、今週Amber v6.2.2が出荷したものと同じ形式です。[PR #75](https://github.com/nostur-com/nostur-ios-public/pull/75)と[PR #76](https://github.com/nostur-com/nostur-ios-public/pull/76)はiPhoneがforegroundへ移行した後のDM refreshとforeground recovery経路を修正し、[PR #78](https://github.com/nostur-com/nostur-ios-public/pull/78)はcustom NWC設定にQR scanを追加します。

---

## 新たな追跡対象と発見

### Social Agents Prototype: human approval gateを備えたNostr-native AI agent協働

[Social Agents Prototype](https://github.com/SrulyRosenblat/social_agents_prototype_nostr)は、分散型agent間通信を探求するNostr上の実験的AI toolです。agentはnetworkへ最小単位の質問をbroadcastし、関連するagentだけが応答し、送受信されるすべてのmessageは転送前にhuman approval gateを通ります。作者はSruly Rosenblatです。このプロジェクトは今週のBuzzおよびNIP-100 SNINと同じagent協働領域にありますが、異なる形式を取ります。Social Agents Prototypeはagentをbroadcastとlistenを行うparticipantとしてモデル化し、そのすべてのmessageに人間の承認を要求します。同じ問題への複数の並行した取り組みが今週見えています。

### PRana: NIP-34 issueのworklist

DocNRによる[PRana](https://github.com/DocNR/prana)は、opt-inのgit-over-Nostr repoで正しくopenされた[NIP-34](/ja/topics/nip-34/) issueのworklistです。このtoolはgit-over-Nostr stackの1層上に位置し、参加repoからNIP-34 issue eventを取り込み、triage queueとして表示します。ローンチと同じ週に、[NIP-34 PR #2384](https://github.com/nostr-protocol/nips/pull/2384)は期限切れ問題を解決するためmaintainers tagの削除を提案しました。これはPRanaのようなtoolがrepo間でissueの権限を解決する方法に直接影響します。

### routstr-chat: Nostr上のRoutstr protocol経由でlocal LLMへアクセス

Routstr teamによる[routstr-chat](https://github.com/Routstr/routstr-chat)は、Routstr protocolを使ってNostr経由で任意のLLM modelへアクセスする完全localなchat interfaceです。Routstr protocolはNostr上で公開されたprovider announcement（kind `38421`）を通じてinference requestをroutingし、Cashuで決済します。これは[Newsletter #20](/en/newsletters/2026-04-29-newsletter/#routstrd-launches-a-local-router-for-inference-over-nostr)で扱いました。chat clientはそのprotocol上のuser-facing surfaceです。routing daemon（Routstrd）がdiscoveryとpaymentを処理し、chat appがconversation UIを提供します。

---

## Protocol作業

### NIP update

今週のNIP活動は異例に多く、2件のmergeと重要なopen proposalが相次ぎました。

#### NIP-46 client metadataをAmberとNosturが出荷

[NIP-46 PR #2381](https://github.com/nostr-protocol/nips/pull/2381)は[先週Claveが提案したもの](/en/newsletters/2026-06-17-newsletter/#clave-10-ships-to-the-app-store-with-push-woken-background-signing)で、現在は両側に実稼働実装があります。[Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2)はbunker connect requestの新しい任意field `optional_client_metadata`を読み、request画面とapp一覧にnative app iconとmetadataを表示します。[Nostur PR #74](https://github.com/nostur-com/nostur-ios-public/pull/74)はclient側で同fieldを追加します。3プロジェクトが揃うことで、bunker pairingのidentity不足が解消されます。`bunker://` pairingでもappが`nostrconnect://`で既に告知できたものと同じ`name`、`url`、`image`を運べるようになります。

#### NIP-86 signeventとrelay roleを定義する関連event

[staabによるPR #2389](https://github.com/nostr-protocol/nips/pull/2389)はrelay管理APIである[NIP-86](/ja/topics/nip-86/)へ`signevent`操作をmergeし、relay adminがrelayに代わって[NIP-43](https://github.com/nostr-protocol/nips/blob/master/43.md) eventを管理できるようにしました。関連するopen proposalの[staabによるPR #2390](https://github.com/nostr-protocol/nips/pull/2390)はrelay role eventを定義し、relayがrole定義を宣言し、adminがmemberをそのroleへassignまたはunassignできるようにします。2件のPRは組み合わせて使う設計です。NIP-86がadminに操作を与え、role eventが認可modelを与えます。

#### NIP-99: marketplace向けon-graph checkout layer

[ColabonateによるPR #2323](https://github.com/nostr-protocol/nips/pull/2323)は今週の取り組みを結ぶ最も強いhubです。この提案はdesign feedbackの依頼として提示され、[NIP-99](/ja/topics/nip-99/)とGamma Market Specのstackにある2つの不足を指摘します。1つはgraph上で完結するcheckout flow（buy now後のstate、order作成、payment、delivery確認を、どのclientでも読めるpublic addressable Nostr eventとして表現）、もう1つはweb-of-trust signalだけでは足りない取引（高額商品、初取引の相手、匿名marketplace、物理配送）向けのescrowとdispute resolutionです。この提案は、NIP-99が出品情報のclient間siloを解消したのと同様に、marketplaceのclient間siloを解消します。[Conduit](https://github.com/Conduit-BTC/conduit-mono)のローンチ（独自の`nips/`と`specs/`ディレクトリを含む）、[Shopstr PR #512](https://github.com/shopstr-eng/shopstr/pull/512)（end-to-end Cashu escrow lifecycle）、[BitBlik](https://github.com/bit-blik/bitblik)（独自のescrow primitiveを備えたP2P BLIK ↔ Lightning）、[Gamma Markets Market Spec](https://github.com/GammaMarkets/market-spec)の独立リポジトリがactive trackingへ入ったのと同じ週に登場しました。

#### NIP-34: 期限切れ問題の解決にmaintainers tagを削除

[dhalsimによるPR #2384](https://github.com/nostr-protocol/nips/pull/2384)は[NIP-34](/ja/topics/nip-34/) repository announcementからmaintainers tagを削除し、[issue #2382](https://github.com/nostr-protocol/nips/issues/2382)に対応します。maintainers tagには定義済みの有効期限semanticsがなく、下流toolはmaintainer assignmentがまだ権威を持つか判断しにくい状態でした。この変更の影響範囲は広く、flotilla-budabit patch（今週重要なpatch活動があった唯一の追跡対象NIP-34 repo）、Iris teamの8 repo構成NIP-34 distribution、BitBlikのNIP-34 mirror、新しいAmber NIP-34 mirror、DocNRのPRana issue worklist toolへ及びます。PRのcross reviewerにはDanConwayDev（ngit）、vitorpamplona（Amethyst）、TheAwiteb、chebizarroが含まれます。

#### NIP-29 group state（作業中）

[dtononによるPR #2372](https://github.com/nostr-protocol/nips/pull/2372)は[NIP-29](/ja/topics/nip-29/)向けにgroup stateという枠組みを提案し、feedbackを得るためwork in progressとして共有されています。これは[#27で扱ったNIP-29の進展](/en/newsletters/2026-06-17-newsletter/)を新しい枠組みで継続するものです。

#### NIP-79 StoriesとNIP-76 Reels Feed（いずれもanaskmh）

同じ作者による2件の短尺media仕様が今週登場しました。[PR #2386](https://github.com/nostr-protocol/nips/pull/2386)はNIP-79 Storiesを提案します。24時間後に期限切れとなる全画面の写真、動画、text slideで、個々のslideにkind `19`、複数slideのstoryを並べる順序付き`e` tagを保持するaddressable eventにkind `34237`、任意でプライバシーを保つ閲覧receiptにkind `15750`を使います。[PR #2385](https://github.com/nostr-protocol/nips/pull/2385)は短尺video Reels Feed向けのNIP-76を提案します。どちらもdivine.videoのような既存video clientが出荷するものと並行する仕様であり、その実装ではありません。

#### kind 1 noteへの返信としてのkind 1111

[zhoreeqによるPR #2358](https://github.com/nostr-protocol/nips/pull/2358)は、kind `1` noteにkind `1111`（[NIP-22](/ja/topics/nip-22/)）のcomment thread返信を使わないよう勧めていた行をNIPs群から削除します（[issue #2250](https://github.com/nostr-protocol/nips/issues/2250)）。diffは小さいものの影響は広く、NIP-22のthreaded comment形式を通常のkind 1 timeline noteに使いたいclientが、明示的にサポートされるようになります。

---

## Nostrの6年間の6月 {#six-years-of-nostr-junes}

6月の[repository history](https://github.com/nostr-protocol/nips/commits/master/)は、Nostrがprotocol黎明期から組み合わせ可能なapplication substrateへ進む過程をたどります。2021年には作業のすべてが1つのprotocol repositoryに収まっていました。2022年には標準化processと最初の本格的clientが別々のprojectになりました。2023年の公開利用の波によりrelay、payment、より豊かなidentityが急務となり、2024年は初期のsigningとmessagingの近道を置き換え、2025年はそれらの契約をprivate group、git協働、media、commerceへ広げ、2026年にはagent workspace、exchange、developer toolの一層としてNostrを使う製品が登場しました。署名済みeventがrelay間を移動できると証明する段階から、それを実装の一要素にする段階への進展です。

### 2021年6月: protocol黎明期

Nostrは誕生から約7か月でした。fiatjafの[最初のprotocol投稿](https://fiatjaf.com/nostr.html)と[`fiatjaf/nostr`](https://github.com/fiatjaf/nostr) repositoryが、公開projectのほぼ全体をなお収めていました。各変更をreviewできるdeveloperは一握りで、reference implementationはPython scriptでした。まだclient ecosystemではなく、platformにidentityを割り当てられなくてもuserがeventへ署名しrelayを選べる、という主張の段階でした。

専用のNIPs repositoryはなく、proposalとimplementation exampleは引き続き[main protocol history](https://github.com/nostr-protocol/nostr/commits?since=2021-06-01&until=2021-07-01)を共有していました。この時点では範囲が小さいことが強みで、新しい実装者はprotocolを端から端まで理解できました。一方、すべての新しい挙動が同じ小集団に依存するという代償もありました。2022年のrepository分割とclientの波が、この制約を取り除き始めます。

### 2022年6月: NIPs repositoryの成立

2022年半ばまでにNostrには十分な数の提案者が集まり、5月に作成された独立の[`nostr-protocol/nips`](https://github.com/nostr-protocol/nips) repositoryが必要になりました。約20件の仕様が基本event形式、follow list、暗号化DM、relay metadata、bech32 identifierを扱っていました。文書を元のcode repositoryから移したことでprojectのgovernanceが変わり、clientは独立して進化でき、共有wire behaviorには明示的なproposalとreviewが行われるようになりました。

AstralやAnigmaを含む最初のpublic web clientは初期版が稼働し、William Casarinの[Damus repository](https://github.com/damus-io/damus/commits?since=2022-06-01&until=2022-07-01)はTestFlight配布へ向かっていました。user baseはまだ小さくdeveloper中心でしたが、systemには2つの拡大面が生まれました。より多くの人が仕様を保守せずapplicationを構築でき、より多くの人が元のclientを所有せず仕様を改善できるようになりました。

### 2023年6月: Damus後の利用急増

2023年6月までに、DamusのApp Storeローンチ後に起きたpublic利用の波がengineering上の問題を変えていました。[Primal](https://github.com/PrimalHQ)とIrisはprotocol初期のchatを追っていない人向けに開発し、[strfry](https://github.com/hoytech/strfry)はtraffic増加に直面するoperatorへ高性能relayを提供しました。networkに必要なのは実装数の増加だけではなく、user、follow、event historyが増えても応答性を保つclientとrelayでした。

そのためprotocol作業はroutingとvalue transferへ集中しました。[NIP-65 relay list](https://github.com/nostr-protocol/nips/blob/master/65.md)は形成されつつあったoutbox modelに可搬なsource of truthを与え、[NIP-57 zap](https://github.com/nostr-protocol/nips/blob/master/57.md)はeventとidentityをLightning receiptへ接続しました。段階の変化は実用上のものでした。identityとpublishingがuserを呼び込みましたが、より大きなnetworkを1つの過負荷なpublic feed以上のものとして動かしたのは、選択的relay routingとwallet interoperabilityでした。

### 2024年6月: signer、gift wrap、messagingの刷新

2024年6月までに署名処理は個々のclientの外へ移り始めました。[NIP-46仕様](https://github.com/nostr-protocol/nips/blob/master/46.md)、[nsecBunker](https://github.com/kind-0/nsecbunkerd)、[Amber](https://github.com/greenart7c3/Amber)により、webおよびAndroid applicationはuserのsecret keyを取り込まずに署名を要求できました。これは初期の前提を逆転させます。可搬性とは各clientへnsecをcopyすることではなく、専用signerにその周囲のboundaryを適用させることになりました。

messagingも同じ理由で変わりました。[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)はNIP-44暗号化とNIP-59 gift wrappingを組み合わせ、NIP-04が露出するmetadataを減らしました。[NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)はclient自身が描画しないevent type向けのhandlerを推薦可能にしました。この環境でMLS-over-Nostrの議論も始まりました。プライバシーとapplication discoveryはclient間の契約になりつつあり、1つのclientが全機能を抱えるのではなく、private groupとevent固有applicationの基盤を整えました。

### 2025年6月: Marmot、git-over-Nostrの成熟、多様なclient

2025年6月までにMLS-over-Nostrには正式な[Marmot仕様](https://github.com/marmot-protocol/marmot)とpublic implementationの[White Noise](https://github.com/marmot-protocol/whitenoise)がありました。[NIP-34 git event](https://github.com/nostr-protocol/nips/blob/master/34.md)、ngit、GitWorkshopも利用可能なcode review flowへ成熟しました。これらのprojectは同じ設計段階にありました。relayを協調に使いつつ、text note clientをapplication全体として扱わず、機密group stateやrepository objectを専用層へ移しました。

commerceとmediaも同じ形式を取りました。[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) walletとNIP-61 nutzapはCashu stateを可搬なeventへ持ち込み、Wavlake、Divine、[NIP-99 marketplace実装](https://github.com/nostr-protocol/nips/blob/master/99.md)はmusic、video、listingに専用event kindを使いました。applicationがidentityとrelay substrateを維持しながら、domain固有のstorage、payment、moderation、presentationを導入するにつれ、Nostrは目に見える形では「social network」らしさを弱めていきました。

### 2026年6月: ローンチの多い月

2026年6月にはNostrをより大きな製品の1要素として扱うローンチが相次ぎました。[Buzz](https://github.com/block/buzz)は人間とagent向けのself-host workspace-as-relay形式を公開し、[Napplets](https://napplet.run)はNostrとBlossom上の組み合わせ可能なappにtrust boundaryを定義し、[Conduit](https://conduit.market)はmarketplace applicationと独自のprotocol文書を並べました。これらのprojectは、署名済みeventが協働を支えられるかを問う段階を過ぎています。どの作業をeventに置き、どれをblobまたはlocal stateに置き、hostがどの権限を保持すべきかを決めていました。

[BitBlik](https://www.bitblik.app)はP2Pの法定通貨・Lightning交換にNostrを使い、[CodeDeck](https://github.com/JeroenOnNostr/codedeck)は暗号化relayを通じてcoding sessionを運び、[Haven](https://github.com/mehmetefeumit/Haven-App)は通常のmessenger以外にMarmotを応用しました。[2021年のprototype repository](https://github.com/nostr-protocol/nostr)からの距離はproject数の増加だけではありません。抽象化の変化です。teamは可搬なidentity、relay discovery、暗号化、paymentを既存部品として出発点にし、その上にあるapplication固有boundaryへ設計作業を注げるようになりました。
