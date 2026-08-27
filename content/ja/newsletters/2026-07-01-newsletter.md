---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
translationOf: /en/newsletters/2026-07-01-newsletter.md
translationDate: 2026-07-01
draft: false
type: newsletters
---

Nostrの週刊ガイド、Nostr Compassへようこそ。

**今週:** [FIPS v0.4.0](#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul)はNym mixnetトランスポート、オプトインのmDNS LANディスカバリ、パケット損失下でも途切れないrekey、データプレーンの全面改修を出荷し、v0.3.0とのwire互換性を維持します。[Whitenoise Linux](#whitenoise-linux-surfaces-as-a-desktop-marmot-client)はRustとSlintで構築されたデスクトップMarmotクライアントとして登場し、メッセージエフェクトを専用kind 9イベントへ移すprotocol提案を示します。[CustID v0.1.10-beta](#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow)は、NIP-46リモートsignerとして動作し、NFCで物理アクセスのチャレンジに応答するハードウェア保護型モバイルidentity vaultとして登場します。[myco](#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh)はv0.1.0の新しいBLE L2CAPトランスポートを使い、FIPS mesh上でピアツーピアのnsite共有を開始します。[Nostr Codex Phone](#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr)は、暗号化Nostr DMを介してローカルのCodexコーディングアシスタントを操作するAndroidコントロール画面として登場します。[Amethystの未リリース版](#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section)はNIP-89アプリハンドラー解析、NIP-34向けGit Repositoriesフィード、nSiteとnapplet向けDiscoverセクションを追加します。[Notedeck](#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)は1週間でNIP-37、NIP-52、NIP-22を実装しました。[Applesauce](#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut)は12個のサブパッケージをリリースし、nbunksec NIP-46ヘルパーとCashu-ts v4 walletへの更新を行います。[Meiso v1.4.0](#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing)はaddressableなkind 35000上でShared-Key Collaborative Listsを出荷します。NIPsリポジトリではrelay rolesイベント、NIP-44の65,535バイト制限撤廃、NIP-34のfork semantics、NIP-46のclient metadata、NIP-86の`signevent`メソッドを含む5件のPRがマージされました。ディープダイブでは[NIP-86（Relay Management API）](#nip-deep-dive-nip-86-relay-management-api)と[NIP-89（Recommended Application Handlers）](#nip-deep-dive-nip-89-recommended-application-handlers)を取り上げます。

---

## トップストーリー

### FIPS v0.4.0はNym mixnetトランスポート、mDNSディスカバリ、データプレーン全面改修を出荷

[FIPS](https://github.com/jmcorgan/fips)は、中央インフラを使わずにノード同士が互いを発見しトラフィックをルーティングする、Nostr向けの非公開・自己組織型ピアツーピアmeshネットワークです。[FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0)はNym mixnetトランスポート、オプトインのmDNS LANディスカバリ、データプレーン全面改修、パケット損失下でも途切れないrekey、render-snapshot harness上に再構築した`fipstop` TUI、hot path外のobservability plane、新しいOpenWrt apkおよびNix flakeパッケージングを導入します。すべてv0.3.0とwire互換で、ローリングアップグレード中も混在meshが相互運用できます。リリースの中核はピア発見向けの2つの新トランスポートです。新しい[アウトバウンドNym mixnetトランスポート](https://github.com/jmcorgan/fips/releases/tag/v0.4.0)は、FIPSトラフィックを`nym-socks5-client` SOCKS5プロキシ経由で[Nym](https://nymtech.net/)のcover-trafficネットワークに混ぜ、リンクレベルの観測者が通信中のmesh peer同士を相関できないようにします。`examples/sidecar-nostr-mixnet-relay/`ディレクトリは、mixnet越しにend-to-endでpeer接続したFIPSリンクから到達できるNostr relayを実演します。オプトインのmDNS / DNS-SD LANディスカバリにより、同じローカルリンク上のノードはアドレス設定もSTUNも使わず、`node.discovery.lan.enabled: true`の標準service recordを通じてpeerを広告・採用できます。

データプレーンは単一ノードのスループット向上に向けて再設計されました。peerごとの暗号化と復号は受信ループ外の専用worker taskで動くため、1つの多忙なpeerがノード全体の暗号処理を直列化しません。Linux送信経路は利用可能な場合にgeneric segmentation offloadとconnected UDP socketを使い、受信hot pathは従来パケットごとに行っていたbuffer copyを避けます。macOSには、v0.3.0でLinuxに導入された`recvmmsg` batchingに対応する`recvmsg_x` batched receiveが追加されました。`fipsctl`と`fipstop`の`show_*`読み取り面全体は、control accept taskからlock-freeな`ArcSwap`へ公開されるtickごとのsnapshotを使うため、受信ループが多忙なノードでもoperator queryへ迅速に応答します。counterのみの新しい`show_metrics` query（`fipsctl stats metrics`として公開）により、hot pathへ負荷を加えずPrometheusでscrapeできます。

FMPとFSPのsession rekeyは、双方向のパケット損失や並べ替えがあっても途切れなくなりました。inbound frameはK-bit cutoverが昇格させる前にpending sessionに対して認証されるため、古いframeやspoofされたframeがrekeyを妨げません。rekey message 1の再送には上限が設けられ、link-dead heartbeatはrekeyを認識し、高遅延リンクで双方が同時に開始する競合は対称jitterでずらされます。`fipstop` TUIは、用意されたcontrol-socket出力に対して各viewの正確なtext gridとcellごとのstyleを検証するrender-snapshot harness上で再構築されました。新しいパッケージング対象も加わりました。OpenWrt 25以降向けの`.apk`はSDKなしで構築され、既存`.ipk`のcross-compileとインストール済みfilesystem payloadを再利用します。プロジェクトrootの`flake.nix`は、固定toolchainを使いNix/NixOS上で4つのbinary（`fips`、`fipsctl`、`fips-gateway`、`fipstop`）をsourceから構築します。

### Whitenoise LinuxがデスクトップMarmotクライアントとして登場

[Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git)はデスクトップ向け[Marmot](/ja/topics/marmot/)クライアントです。Nostr relay上のMLS group messagingを、すべてのsecretをpassword暗号化vaultに保管するSlint UI付きの単一Rust binaryとして提供します。

今週最も重要な論点は、Whitenoiseのメッセージエフェクトを親メッセージを参照する専用kind 9イベントとして運ぶ提案です。現在のwire formatはメッセージ本文末尾に`dmfx:sparkle`のようなmarkerを付加するため、この慣習を知らないrendererでは本文が汚れます。エフェクトを独立イベントへ移せばメッセージ本文を清潔に保てる一方、より広いMarmot stackが直面する設計上の問いも生じます。任意のrich featureを本文内の慣習で表すのか、sidecar eventで表すのかという問題です。

### CustIDがNIP-46とNFCチャレンジフローを備えたモバイルidentity vaultとして登場

[CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c)は、NostrとSISTR protocol上に構築されたモバイルidentity vault、CustIDの最初の公開betaです。CustIDは複数のNostr identityをhardware-backed secure storageに保存し、他のclient向け[NIP-46](/ja/topics/nip-46/) remote signerとして動作し、NFCとQR codeを使って物理およびオンラインのaccess challengeに応答します。

betaはNIP-46 signerとNFC challenge-response flowに必要な機能を備えています。zero-knowledge proofによるaccess flowは今後のmilestoneです。このリリースではアプリのバックグラウンド[NIP-65](/ja/topics/nip-65/) keep-alive layerも削除されました。以前はprofileごと、read relayごとにWebSocketを開き、clientが即座に破棄するkindまで取り込んでいました。現在バックグラウンドで維持されるのはsigning request通知を運ぶNIP-46 socketだけです。この修正により、CustIDを他clientのbunkerとしてスマートフォン上で実用的に動かせます。

### mycoがFIPS mesh上でピアツーピアnsite共有を開始

[myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0)は6月27日に公開され、7月1日にv0.1.0へ到達しました。mycoは近くにいる人からアプリをインストールするRust製Androidアプリです。FIPS meshが運べる任意のトランスポート（UDP、TCP、Tor、Bluetooth）を通じてピアツーピアの[nsite](/ja/topics/nip-5a/)共有を行い、完全なオフライン環境でも動作します。設計はトランスポート基盤としてFIPS、payloadとしてNIP-5Aの静的Webサイトevent formatと直接組み合わされます。nsiteとして配布されたアプリはrelayやHTTPに依存せずmesh peer間を移動できます。

v0.1.0はL2CAP Bluetooth radio pathを追加し、FIPSをインストールした2台のスマートフォンがネットワークなしでBLE越しにpeer接続できるようにします。peerごとのspeedtestと、アプリのCircle bottom sheetからNFCで開始する共有も追加されました。mycoは直接インストールできるようZapstoreでも公開されています。

### Nostr Codex PhoneがNostr越しにローカルCodex workerを操作するモバイル画面として登場

[Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone)は今週、暗号化Nostr direct messageを介してローカルのCodex coding-assistant workerを操作するAndroid clientとして登場しました。複数repository session、音声文字起こし、routed worker session、Blossom media upload、任意の音声応答をサポートします。自宅でCodex workerを動かす開発者は、スマートフォンがrelayへ接続できる場所ならどこからでもrequestを送れます。

このプロジェクトは#28で登場した[CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr)と直接の兄弟関係にあります。どちらもagentic coding workflowを暗号化DM付きNostrトランスポートへ載せ、ネットワークに穴を開けずスマートフォンから自宅のworkerへ到達するためのpairing・messaging layerとしてNostrを使います。ローカルagentのcontrol planeとしてNostrを使う方式は、定着したパターンになりつつあります。

### Coop Mobileが初のversioned buildを公開

[Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1)と[v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2)が今週、Android向け[NIP-17](/ja/topics/nip-17/)暗号化direct messaging client、Coop Mobileの最初のversioned buildとして出荷されました。2つのリリースはメッセージ解析とQR処理のcrash safetyを強化し、logout時に保存データをすべて消去します。

### AmethystがNIP-89対応UI、Git Repositoriesフィード、napplet Discoverセクションを構築

[Amethyst](https://github.com/vitorpamplona/amethyst)のmain branchは今週、複数の新しい画面を構築しました。[Git Repositoriesフィード](https://github.com/vitorpamplona/amethyst/pull/3406)は[NIP-34](/ja/topics/nip-34/) repoを閲覧可能なAndroid timeline categoryにし、communityとauthorで絞り込めます。[smart-HTTP git browser](https://github.com/vitorpamplona/amethyst/pull/3415)も組み合わされ、アプリを離れずrepoの内容とcommitを読めます。napplet hostには[NIP-89](/ja/topics/nip-89/) handler eventと[NIP-5A](/ja/topics/nip-5a/) site eventをsourceとし、curated web app、follow中のnSiteとnappletを一覧にする[Discoverセクション](https://github.com/vitorpamplona/amethyst/pull/3409)が追加されました。ノート表示はNIP-89 tagを使い、[どのNostrアプリがeventを作成したか](https://github.com/vitorpamplona/amethyst/pull/3422)を示します。同期面では、[NIP-77 negentropy support](https://github.com/vitorpamplona/amethyst/pull/3434)がstreaming reconciliationと自動的な`created_at` windowingを導入し、relay側の結果上限を回避します。これにより大規模なローカルevent setをrelayと同期し続けるための帯域を削減します。

### Buzz v0.3.38がrelay attack surfaceを強化しprovider非依存のmodel選択を追加

[Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38)は、persona、team、managed agent、NIP-OA owner attestationを署名済みNostr eventとして公開する際にBuzzが露出する[relay attack surface](https://github.com/block/buzz/pull/1369)を強化します。Buzz relayはteamのNostr identityと状態を記録する公開台帳であり、このリリースはBuzzが定義するwell-known event kindの入力検証とreplay protectionを強化します。またmodel選択を一般化し、新しいDatabricks AI Gateway v2 backendを含め、Buzzがadapterを持つ任意のproviderをteamが選べるようにします。

### NotedeckがNIP-37 private-sync relay、NIP-52 calendar、NIP-22 commentを実装

Damus teamのnative Rust desktop clientである[Notedeck](https://github.com/damus-io/notedeck)は、1週間で3つのprotocolを実装しました。private-sync relayはkind `10013`の[NIP-37](/ja/topics/nip-37/) listとして永続化され、ユーザーのprivate content relay setを公開NIP-65 outboxから分離します。`horizon` calendar paneはnostrdbから[NIP-52](/ja/topics/nip-52/) eventを読み、3 pane layoutへ再設計されました。`headway` paneはkind `1111`上の[NIP-22](/ja/topics/nip-22/) comment event modelを追加しました。これはNIP-10 reply threadingに代わる統一comment surfaceとしてNIP-22が定義するkindです。

### Applesauceが連携した6.2.x更新で12サブパッケージを出荷

signer、relay、wallet、content向けのmodular Nostr toolkitである[Applesauce](https://github.com/hzrd149/applesauce)は、サブパッケージ全体で連携した[6.2.xリリース](https://github.com/hzrd149/applesauce/releases)を行いました。signers packageには`nbunksec` import・export helperが加わり、[NIP-46](/ja/topics/nip-46/) bunker sessionをclient間で移動できるportable artifactとして扱います。wallet packageは[Cashu](/ja/topics/nip-60/) bindingを`@cashu/cashu-ts` v4へ更新し、proof amountは`Amount` value objectとなり、token decoding APIも変わりました。

---

## タグ付きリリース

### mostro-core v0.14.0

[mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0)は、[Mostro](/ja/topics/nip-69/) P2P fiat取引ネットワークの次のprotocol iterationを導入します。[v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2)に続くリリースで、新coreを採用する[mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0)と同時に出荷されました。core repositoryでは今週3件のPRがマージされ、周辺stack（mostro daemonとMostro mobile）は共有type crateのv0.14.0へ追従します。

### ngit v2.6.1

[NIP-34](/ja/topics/nip-34/) repository向け標準git-over-nostr CLIである[ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli)は、今週マージされた[NIP-34 GRASP-06 fork semantics](https://github.com/nostr-protocol/nips/pull/2395)を実装します。repo-state eventの`personal-fork` tagを`u` tagへ置き換える変更です。

### mesh-llm v0.72.0とv0.72.1

[mesh-llm](https://github.com/Mesh-LLM/mesh-llm)は、Nostrからaddress可能なJSON-RPC surfaceの背後でopen-source LLMを動かすContextVM stackのinference componentです。[v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0)と[v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1)は、大きな単一promptにおけるbatching crashを修正し、MCP bridgeをdeprecated helperから移行しました。

### Meiso v1.4.0がtask共有のMLSを置き換えるShared-Key Collaborative Listsを出荷

[Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0)は、従来のMLSベースtask共有をより単純なaddressable event設計で置き換えるShared-Key Collaborative Lists modelを導入します。各共有listはmemberへ配布する専用Nostr鍵を生成します。taskは`d=task-id`でkeyedされたkind `35000`のaddressable eventで、contentは[NIP-44](/ja/topics/nip-44/)により自己暗号化され、relayはtaskごとにLast-Write-Winsを適用します。この設計はclient実装の単純化とrelay levelのconflict resolutionと引き換えに、MLSのforward secrecyとpost-compromise securityを手放します。

### Cordn 0.3.2

[Cordn 0.3.2](https://github.com/Cordn-msg/cordn)はgroup message投稿からephemeral sender pubkeyを削除し、古い再requestに対するjoin-request flowを強化する「more-private-coordinator」系統を出荷します。Cordnは[#28のCordn Ad-hoc CVM登場](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator)で取り上げたMLSベースmessaging stackで、このリリースは対応するcoordinator側の更新です。

---

## 未リリースの変更

### diVineがローンチ後の改善として108件のPRをマージ

Vineを復活させる短尺loop video client、[diVine](https://github.com/divinevideo/divine-mobile)は、ローンチ後の大規模な改善段階にあります。今週Nostrから見える変更は、`nostrconnect://`の失敗を構造化reason codeへ移行する[NIP-46](/ja/topics/nip-46/) connect flowの安定化です。

### Zap Cookingがプロジェクト横断NIP-46修正とcomposer全面改修を継続

[Zap Cooking](https://github.com/zapcooking/frontend)は、recipeをNostr long-form eventとして公開するNostr recipe共有clientです。今週の作業は、[#28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes)で未リリース変更として取り上げたプロジェクト横断[NIP-46](/ja/topics/nip-46/)修正とcomposer全面改修を継続します。

### Conduitがlisting flowとmarketplaceの正確性を強化

[Conduit](https://github.com/Conduit-BTC/conduit-mono)は、buyer market、merchant portal、store builderの3アプリを含むNostr marketplace monorepoです。今週の作業は[#28のローンチ記事](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default)で取り上げたmarketplaceの正確性向上を継続し、前号のprotocol面の中心だった[NIP-99](/ja/topics/nip-99/) commerceの動きの上に構築されています。

### Pollerama v1.12からv1.13.1がclient tag選択、profile tab、thread上限を追加

[Pollerama](https://github.com/formstr-hq/nostr-polls)はpollとnoteに重点を置き、web of trustによるdiscoveryを強く採用するAndroid Nostr clientです。今週Zapstoreへv1.12.0、v1.13.0、v1.13.1を出荷しました。ユーザーは作成するnoteとpollへ付けるclient tagをpreset listから選ぶか、独自の値を入力できます。深くnestしたcomment・reply chainは数levelで止まり、note pageの完全なthreadへlinkします。profile pageは既定でNotesを開き、Posts tabとConversations tabに分かれます。新しくfollowしたaccountがアプリ再起動後に消えるpersistence bugが修正され、follow buttonは進捗を表示します。

### getwired.appとget-tao.appがNIP-13 confess送信flowを修正

[getwired.app](https://github.com/smolgrrr/Wired)と[get-tao.app](https://github.com/smolgrrr/TAO)は、送信時のspam抑制にNIP-13 proof-of-workを加える匿名投稿flowを共有しています。[confess送信flow](https://github.com/smolgrrr/Wired/pull/57)を修正し、PoW mining中のUXを一貫させました。

### nostuiがmention timeline tabを追加

Rust製terminal Nostr clientの[nostui](https://github.com/akiomik/nostui)は、active pubkeyをtag付けしたkind 1 eventをTUIの専用viewに表示する[mention timeline tab](https://github.com/akiomik/nostui/pull/463)を追加しました。

### HeartwoodがidentityごとのNIP-46 bunker URIとHSM mode signing bridgeを導入

[Heartwood](https://github.com/forgesworn/heartwood)は、signing keyがclientへ一切届かない[NIP-46](/ja/topics/nip-46/) signerです。clientはNIP-46で小さなrelayと通信し、relayはserial frame protocolで接続済みhardware deviceと通信し、そのdeviceが署名を実行します。今週、プロジェクトは[relay-to-serial signing bridge](https://github.com/forgesworn/heartwood/pull/11)と[identityごとのbunker connection](https://github.com/forgesworn/heartwood/pull/16)を導入しました。複数identityを保持する1台のhardware deviceが、それぞれに異なるbunker URIを公開できます。

### Nostterのauth・signer refactor

[Nostter](https://github.com/SnowCait/nostter)は今週、[auth・signer layer](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth)を再設計し、login stateを単一signalへ移し、signer dispatchをstrategy moduleへ抽出しました。NIP-07 web extension、NIP-46 remote bunker、raw nsecが同じcode pathを共有する、明確なsigner abstractionへ向かっています。

### Dart NDKがNIP-07 signerを分離しNIP-59 timestampをrandomize

[Dart NDK](https://github.com/relaystr/dart_ndk)は[NIP-07](/ja/topics/nip-07/) signerをcore packageからFlutter WebViewを含む`ndk_flutter`へ移し、暗号化messageのtiming correlationを難しくするため[NIP-59 gift-wrap timestampをrandomize](https://github.com/relaystr/dart_ndk/pull/667)しました。

### Milk MarketがNIP-23 storefront pageとSquare決済を追加

Shopstr teamのmarketplace storefrontである[Milk Market](https://github.com/shopstr-eng/milk-market)は、sellerの[NIP-23](/ja/topics/nip-23/) long-form eventを基盤に各storefrontへblog pageを追加し、編集可能なsectionとblog settingへのdirect routeを提供しました。同じ週にseller向け代替payment processorとして[Square](https://github.com/shopstr-eng/milk-market/pull/30)を追加し、支払い済みorderのshipping labelを自動購入できるようにしました。

### Calendar by FormstrがiOSアプリを出荷

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar)は今週、[PR #159 IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159)をマージし、[NIP-52](/ja/topics/nip-52/) calendar clientをiOSへ持ち込みました。[PR #197](https://github.com/formstr-hq/nostr-calendar/pull/197)はlocal timeでのcalendar date解析を修正し、[PR #201](https://github.com/formstr-hq/nostr-calendar/pull/201)は`run-tests` labelで起動するPlaywright E2E workflowを追加します。

### cagliostrがNIP-22、座標によるNIP-09、NIP-13 proof-of-workを適用

Go製relay実装の[cagliostr](https://github.com/mattn/cagliostr)は今週、3つの適用経路を強化しました。受信eventへの[設定可能なNIP-13 proof-of-work](https://github.com/mattn/cagliostr/pull/7)、replaceable eventを`a` tagで削除できる[座標によるNIP-09削除](https://github.com/mattn/cagliostr/pull/8)（event idによる削除だけでは到達できません）、過去または未来へ離れすぎたtimestampのeventを拒否する[設定可能なNIP-22 timestamp上限](https://github.com/mattn/cagliostr/pull/9)です。

---

## 新たに追跡・発見したプロジェクト

[Vanderwarker wellbeing suite](https://git.vanderwarker.family/wellbeing)は、共有publisher signing keyの下で現実世界のtelemetryをNostr eventとして公開します。5つの兄弟アプリで構成されます。[Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android)はfitness dataを`kind:30078`としてNostrへ固定するstep tracker、[Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android)は1日のスマートフォンunlock回数を公開、[Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android)は現在のmedia playbackをUser Statusとして公開、[Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android)は15分ごとにbattery level、voltage、temperatureを公開、[Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android)は日ごとのdata usageを公開します。5つすべてが6月24日から30日の間にZapstoreへ登場しました。

[ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9)は、RustとSlintで構築された暗号化・serverlessのlive location共有Androidアプリで、6月29日にリリースされました。[#28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot)で紹介した[Marmot](/ja/topics/marmot/)ベースのlocation共有アプリ[Haven](https://github.com/mehmetefeumit/Haven-App)の兄弟ですが、トランスポート構成が異なります。ntrackでは暗号化Nostr DMがlocation updateを運び、HavenではMarmot group messageを使います。

[NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell)は、Nostrアプリを構築するための初期段階のapplication shell scaffoldです。今週、最初のユーザー向け文書を公開しました。

[NIPs by Pollerama](https://nips.pollerama.fun)（repositoryは[abh3po/better-nips](https://github.com/abh3po/better-nips)、2026-06-29作成）は、[NostrHub](https://nostrhub.io)の`kind:30817` community-authored NIP向け新clientで、nostrhub.ioに代わるtrust-weighted surfaceとして位置づけられています。各`kind:30817` NIPは、完全なMarkdown描画と定義するevent kindを備えた共有可能な独自URL（`#/nip/<naddr>`）を持ちます。clientはFollowing、Web of Trust（follows-of-follows）、Globalの3 feedを提供し、それぞれtrust-weighted approvalまたは新着順でsortできます。approvalはkind `1985`上の[NIP-32](/ja/topics/nip-32/) labelとして、tag `["L","nostrhub"]`と`["l","approve","nostrhub"]`、対象NIP addressを指す`a` tag、`better-nips`を示す`client` tagを付けて公開されます。これはNostrHub自身が署名するeventと完全に同じ形状で、2つのclient間でapprovalに互換性があります。rankingではdirect followによるapprovalが、2次のfollows-of-followsによるapprovalより大きな重みを持ちます。

signing stackは[`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer)で、[NIP-07](/ja/topics/nip-07/)、[NIP-46](/ja/topics/nip-46/) bunkerとnostrconnect、[NIP-49](/ja/topics/nip-49/) ncryptsec、[NIP-55](/ja/topics/nip-55/) Android signerを網羅するlogin modalを備え、reload時にsessionを自動で再接続します。network layerは[`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay)を通ります。これはユーザーの[NIP-65](/ja/topics/nip-65/) outboxをrelay間で分割するWeb Workerで、大規模なweb of trust setが単一relayへfan outするのを防ぎます。設計上、community NIPはNostrHub、`better-nips`、将来の別clientのどこでhostされてもprotocol levelでは対等です。rankingはmoderatorによるcurationではなくsocial graphから生まれ、[#25](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling)のディープダイブで扱ったNIP-32 labeling flowと直接組み合わされます。

今週、2つの新しい[NIP-34](/ja/topics/nip-34/) repo clusterが登場しました。[Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git)はvideo中心のNostr clientです。[nostrapps.com cluster](wss://gitnostr.com)は3つの兄弟プロジェクトを公開します。[verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git)はdesktop向けnapp VM、[hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git)はcustomizable community client、[napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git)はHTML microapp specとruntimeです。このclusterは前号のlead storyで取り上げた[napplet](/ja/topics/nip-5d/)の動きと並行しています。

---

## Protocol作業とNIP更新

### マージ済み: NIP-44が65,535バイトのpayload上限を撤廃

[PR #1907](https://github.com/nostr-protocol/nips/pull/1907)は2024年9月からopenのまま、6月28日にマージされました。[NIP-44](/ja/topics/nip-44/) versioned encryption envelopeのplaintext payload上限65,535バイトを撤廃し、4 GiB（`uint32_max`）へ引き上げます。NIP-44のwire formatはpayload lengthを`uint16`でencodeし、元の仕様は相互運用のため厳密にこれを要求していました。マージされた変更はより長いlength fieldをversion byteへtag付けするため、v2実装はwire互換を保ち、v3以降の実装はより長いlengthを運べます。[NIP-17](/ja/topics/nip-17/) direct message、[NIP-59](/ja/topics/nip-59/) gift wrap、[NIP-46](/ja/topics/nip-46/) remote signer payload、その他NIP-44で暗号化したNostr messageを扱うclientは、application layerで分割せず64 KiBを超える単一eventを交換できるようになりました。

### マージ済み: NIP-86に`signevent`メソッドとRelay Rolesイベントを追加

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389)は[NIP-86](/ja/topics/nip-86/) relay management JSON-RPC APIへ`signevent`メソッドを追加し、administratorがrelay自身のpubkeyでeventに署名するようrelayへ依頼できます。対になる[PR #2390](https://github.com/nostr-protocol/nips/pull/2390)はRelay Rolesイベントを定義します。relayがadministratorとmoderatorを宣言するために公開するreplaceable eventです。2つを組み合わせると、NIP-86 clientはrelayのadmin listを調べ、帯域外のtrustなしに、認証済みrequestが現在のadminから来たことを検証できます。両変更のディープダイブは後述します。

### マージ済み: NIP-34がGRASP-06向け`personal-fork`を`u`へ置換

[PR #2395](https://github.com/nostr-protocol/nips/pull/2395)は6月24日にマージされ、repo-state event（`kind:30618`）上の[NIP-34](/ja/topics/nip-34/) `personal-fork` tagを「upstream」を表す`u` tagへ置き換え、GitWorkshop suiteが実装してきたGRASP-06 fork semanticsへwire formatを合わせます。この変更により、別のfork semantics修正を提案していた[PR #2384](https://github.com/nostr-protocol/nips/pull/2384)（`NIP-34: remove maintainers to solve expiry issues`）はcloseされました。マージされた方向をngit v2.6.xが実装するため、仕様とreference CLIが一致しました。既存の`personal-fork`使用repoは引き続き相互運用でき、新規repoとngit v2.6系統は`u` tagを公開します。

### マージ済み: NIP-46 client metadata（Amber出荷後にupstreamへ反映）

[PR #2381](https://github.com/nostr-protocol/nips/pull/2381)は6月23日にマージされ、[NIP-46](/ja/topics/nip-46/) `connect` requestへ任意のclient metadataを追加しました。signer接続時にclientが名称、icon URL、homepage URLを公開できます。[Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2)は先週metadata拡張を出荷済みで（[#28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata)で紹介）、今週upstream NIPが出荷済み実装へ追いつきました。

### オープン: epochベースの決定論的NIP-17 wrapper key

[PR #2397](https://github.com/nostr-protocol/nips/pull/2397)と[PR #2396](https://github.com/nostr-protocol/nips/pull/2396)は、収束しつつある2つのNIP-17 wrap key提案です。PR #2397は、[NIP-59](/ja/topics/nip-59/) gift wrapの作成に使うephemeral signing keyを、粗い時間epochに結びついたconversationごとのseedから決定論的に導出することを提案します。conversation keyを知る受信者は、購読すべきpubkeyを予測できます。現在の仕様はwrapごとに新しいrandom keyを要求するため、この予測は不可能です。PR #2396は対になる変更で、特定conversationのwrapをconversation keyそのもので署名し、wrap pubkeyがconversation identifierを兼ねるよう提案します。2件を合わせると、metadataを漏らさずfilter可能なNIP-17 conversationへの道筋になります。どちらもopenで議論中です。

### オープン: NIP-59のkind 13 seal eventをrelayで拒否

[PR #2399](https://github.com/nostr-protocol/nips/pull/2399)は、[NIP-59](/ja/topics/nip-59/) gift wrapのinner sealであるkind 13 eventがpublish requestのtop levelに現れた場合、relayが拒否すべきだと提案します。seal eventはwrap内でのみ意味を持ち、漏洩したsealはrecipient pubkeyを露出するためです。対になる[issue #2398](https://github.com/nostr-protocol/nips/issues/2398)はさらに進み、sealをephemeral kindとして再定義すべきだと主張します。NIP-01のephemeral kindはrelayに保存されないため、protocol levelで規則を強化し、relayごとのpolicyへの依存をなくせます。

### オープン: NIP-29 group state

[PR #2372](https://github.com/nostr-protocol/nips/pull/2372)は[NIP-29](/ja/topics/nip-29/)（relayベースgroup）へ明示的なgroup state semanticsを追加します。groupがopen、closed、public、private、archivedである意味と、state transitionがmember eventとどう関係するかを定義します。client固有だったsemanticsをrelay仕様へ取り込みます。

### オープン: NIP-34の任意multi-maintainer support

[PR #2324](https://github.com/nostr-protocol/nips/pull/2324)は、上で扱ったGRASP-06 fork semanticsのマージ済み[PR #2395](https://github.com/nostr-protocol/nips/pull/2395)に対するcompanion proposalです。[NIP-34](/ja/topics/nip-34/) repo announcement event（`kind:30617`）へ任意のmulti-maintainer supportを追加し、repositoryが繰り返し`maintainer` tagで複数のcanonical maintainer pubkeyを宣言できるようにします。宣言済みmaintainerの誰かが署名したpatchとissueをclientがofficialとして信頼でき、co-maintainerを持つNIP-34 repoがすべてを1つのpubkeyへ集約するか、protocol外の調整へ頼るしかなかった長年のgapを解消します。

### オープン: filter向けNIP-91 AND operator（提案は未マージ）

[PR #2252](https://github.com/nostr-protocol/nips/pull/2252)はNostr [filter](/ja/topics/nip-01/)向けAND operatorの提案で、以前closeされた[PR #1365](https://github.com/nostr-protocol/nips/pull/1365)で議論された設計を再提案します。[nostr-rs-relay](https://github.com/v0l/nostr-rs-relay)、applesauce、[Amethyst](https://github.com/vitorpamplona/amethyst)、worker-relayには既に実装がありますが、仕様PR自体はopenのままです。

### クローズ: pats2satsのcommerce NIP 4件

今週、Nostr上のcommerceに関する4つの提案がcloseされました。Escrow（[#2334](https://github.com/nostr-protocol/nips/pull/2334)）、Reservations（[#2335](https://github.com/nostr-protocol/nips/pull/2335)）、[NIP-99](/ja/topics/nip-99/) Marketplace Listing Extension（[#2346](https://github.com/nostr-protocol/nips/pull/2346)）、Accommodation Listing Profile（[#2333](https://github.com/nostr-protocol/nips/pull/2333)）です。同じcommerce surfaceは現在、NIP-99 marketplace listing上にorder、checkout、escrow、dispute semanticsを組み合わせるプロジェクト所有extension repository、[Gamma Market Spec](https://github.com/GammaMarkets/market-spec)へ統合されています。CompassはこのrepositoryをMarmot、Blossomと並ぶNIPs repository外のprotocol spec repoとして追跡します。今週openのPRにはclient attributionの明確化（[#11](https://github.com/GammaMarkets/market-spec/pull/11)）、product identity変更向けsupersedes tag（[#8](https://github.com/GammaMarkets/market-spec/pull/8)）、merchant review semantics（[#7](https://github.com/GammaMarkets/market-spec/pull/7)）があります。

### オープン: Bitcoin identityの連携

今週、Bitcoin identityをNostr identityへ結びつける2つの提案がopenされました。[NIP-352 Bitcoin Silent Payment Address](https://github.com/nostr-protocol/nips/pull/2392)と[Bitcoin-OTC Identity Linkage Proof](https://github.com/nostr-protocol/nips/pull/2401)です。

---

## NIPディープダイブ: NIP-86（Relay Management API）

[NIP-86](/ja/topics/nip-86/)はrelay管理向けJSON-RPC interfaceを定義し、認可済みclientが標準API越しにrelayへadministrative commandを送れるようにします。単一clientでrelay固有toolを使わず、任意のNIP-86互換relayを管理できます。今週の2件の仕様マージ（[PR #2389](https://github.com/nostr-protocol/nips/pull/2389)と[PR #2390](https://github.com/nostr-protocol/nips/pull/2390)）は、relay署名eventとrelayが宣言するadministratorの間を閉じます。

### トランスポート

NIP-86管理requestは、relayがWebSocket接続を提供するものと同じURIへのHTTP POSTで、`Content-Type: application/nostr+json+rpc`を使います。request bodyは次の形式のJSON文書です。

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

authenticationは`Authorization` header内の[NIP-98](/ja/topics/nip-98/) HTTP auth署名eventを使います。relayはmethod実行前に、署名pubkeyがadministrator listに含まれることを検証します。relayのresponseは次の形式のJSON文書です。

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### 今週以前から存在したmethod

従来のmethod setはpubkey ban（`banpubkey`、`allowpubkey`、`listbannedpubkeys`）、event ban（`banevent`、`allowevent`、`listbannedevents`）、relay metadata（`changerelayname`、`changerelaydescription`、`changerelayicon`）、許可pubkey list管理（`allowkind`、`disallowkind`、`listallowedkinds`）、relay statisticsを返す`stats` methodを扱います。標準JSON-RPC serviceに意図的に近い形状なので、clientはその上にtyped bindingを構築できます。

### 今週の変更

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389)は仕様へ`signevent`メソッドを追加します。このmethodは部分event template（kind、tags、content）を引数に取り、relay自身のpubkeyを`pubkey` fieldに持つ完全なeventへ署名して返すようrelayへ依頼します。これはrelayが自身についてprotocol levelのeventを公開するための前提です。blocked pubkey announcement、relay metadata、後述する新しいRelay Roles eventはいずれもoperator管理鍵によるrelayの署名を必要としますが、多くのrelay operatorはadministrative clientにprivate keyを保持したくありません。

[PR #2390](https://github.com/nostr-protocol/nips/pull/2390)はRelay Roles eventを定義します。relayが公開し、`signevent`を通じて自身のpubkeyで署名するparameterised replaceable event kindで、administratorとmoderatorのpubkeyを明示的なrole semantics付きで宣言します。NIP-86対応clientは追跡中の任意relayからRelay Roles eventを取得し、event tagからadmin listを構築し、帯域外trustやrelayごとの設定なしに、認証済みNIP-86 requestが現在のadminから来たことを検証できます。2つのPRがloopを閉じます。`signevent`がmechanismで、Relay Rolesがその上に構築される最初のevent kindです。

### NIP-86 requestの例

完全なNIP-86 `banpubkey` requestは次のようになります。

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

`Authorization` headerにはNIP-98署名eventを入れます。

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

署名pubkeyはrelayのadmin set（現在はrelay roles eventで宣言）に含まれていなければなりません。`u` tagはrelayのHTTPS URLと一致し、`payload` tagはJSON request bodyのSHA-256と一致しなければなりません。relayは次を返します。

```json
{
  "result": true,
  "error": null
}
```

### 実装

- [Amethyst](https://github.com/vitorpamplona/amethyst)はAndroidにNIP-86 relay management UIを搭載しています（v1.07.0以降）。
- 仕様を実装するreference relayには[strfry](https://github.com/hoytech/strfry)、[khatru](https://github.com/fiatjaf/khatru)、仕様の`Implementation Status` sectionからlinkされる複数の小規模実装があります。

実装者が`signevent`とRelay Roles変更を取り込めば、NIP-86対応clientはrelay roles eventをrelay admin listのcanonical sourceとして扱い始めます。

---

## NIPディープダイブ: NIP-89（Recommended Application Handlers）

[NIP-89](/ja/topics/nip-89/)は2つのparameterised replaceable event kindを定義します。`kind:31990`はapp developerが公開するapplication handler、`kind:31989`はユーザーが利用中のappについて公開するrecommendationです。両者により、clientは帯域外の調整なしに未知のevent kindを処理するapplicationを発見できます。例えばnativeでは扱えない`kind:30030` eventに遭遇したlong-form readerは、NIP-89 graphへhandlerを問い合わせ、対応する公開appへの「Open in...」flowをユーザーへ提示できます。NIP-89はcross-app routingという同じ問題に対する元来の基盤であり、本号に登場するnapplet・nappsの作業はこれをcomposableなNostr native appletへ拡張しています。

### Application handler event（`kind:31990`）

app developerは、appが対応するevent kindとNostr entityをappで開く方法を説明するhandler eventを1つ以上公開します。

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

`d` tagはhandlerを識別し、置き換え可能にします。各`k` tagはappが扱うevent kindを宣言します。各platform tag（`web`、`ios`、`android`など）は、呼び出し側clientがopen時に置換する[NIP-19](/ja/topics/nip-19/) encoded entityのplaceholderとして`<bech32>`を持つURL templateを示します。同じrouting patternを共有する場合、1つのhandler eventが複数の対応kindを広告できます。app discoveryをcompactに保ち、kindごとにhandler eventを1つ作る必要をなくします。

### User recommendation event（`kind:31989`）

ユーザーは、特定event kindに利用するappを宣言するrecommendationを公開します。

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

`d` tagはrecommendation対象のevent kindを持ちます。各`a` tagは`kind:31990` handler eventへのNIP-01 address pointerで、推奨relayとrecommendation対象platformを伴います。同じrecommendationに異なるplatform向けの複数appを列挙できます。

### Client tagとprivacyのtradeoff

NIP-89は、任意のpublishing appが自身の作成eventへ付けられる任意の`client` tagも定義します。

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

これによりeventを表示するclientは、そのeventが作成されたappを示し、より詳しいhandler metadataを取得し、handlerが宣言するrendering hintを尊重できます。仕様はprivacy上のcostも明記します。すべてのeventで`client` tagを発行するclientはユーザーのsoftware identityを公開し、時間の経過とともに利用patternを明らかにします。仕様はclientがユーザーへopt-outを提供することを推奨します。

Amethystの[PR #3422](https://github.com/vitorpamplona/amethyst/pull/3422)はevent表示でNIP-89の`t`、`i`、`a`、`client` tagを解析・表示し、noteを作成したappをtimeline上へ直接示します。

### 実際のdiscovery flow

未知のevent kindを受信したclientは次の手順を取ります。（1）ユーザーのfollow graphへ、event kindと一致する`d` tagを持つ`kind:31989` eventを問い合わせます。（2）推奨された各`a` tagを対応する`kind:31990` handler eventへ解決します。（3）現在のplatformに一致する`web`、`ios`、`android` URL templateを持つhandlerを選びます。（4）entityの`bech32` encodingをURL templateへ代入します。（5）生成したURLを「Open in...」の選択肢としてユーザーへ提示します。このflowはsocial filterを通ります。信頼できないrelayから任意のhandler eventを問い合わせると、悪意あるappへredirectされる可能性があります。そのため、公開されたすべてのhandlerを同等に信頼するより、ユーザーがfollowする人々から始める方が安全なdefaultです。

### NIP-89とnapplet layer

AmethystのDiscoverセクション、napplet host runtime、`client` tag表示を合わせると、Android上の完全なNIP-89 consumer surfaceになります。前号で登場したnapplet specは、NIP-89 handler eventの対象を拡張します。NostrとBlossom上でcomposableなNostr native runtimeを動かすsandboxed appletです。NIP-89がdiscovery・routing graphで、napplet runtimeはそのgraphが指せる実行対象の1つです。

---

*フィードバック、訂正、見落としたプロジェクトは[github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass)でissueを開くか、NIP-17 DMでnpub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923までお送りください。*
