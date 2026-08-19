---
title: "Nostr Compass #36"
date: 2026-08-19
publishDate: 2026-08-19
translationOf: /en/newsletters/2026-08-19-newsletter.md
translationDate: 2026-08-19
draft: false
type: newsletters
description: "AmberとCambiumにわたる署名者セキュリティの一週間、メールブリッジのローンチ、スマートフォン上のリレー機能、暗号化コミュニティモデレーション、スレッド・暗号化ファイル・パッチに関するプロトコル作業。"
---

[Nostr Compass](https://nostrcompass.org)へようこそ。Nostrのウィークリーガイドです。

**今週:** [Amber](https://github.com/greenart7c3/Amber)はリレー認証を強化し保存済みシークレットを暗号化し、[Cambium](https://github.com/forgesworn/cambium)はリレー認証負荷下でWebサイト向けに署名し、[Citrine](https://github.com/greenart7c3/Citrine)はスマートフォンリレー上でグループと静的サイトをホストし、[Vector](https://github.com/VectorPrivacy/Vector)はスパム下でモデレーションをキューイングしミュートをデバイス間で同期し、[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar)はスレッド化メッシュ返信を追加し、[Nostria](https://github.com/nostria-app/nostria)はポッドキャストを公開し、[Nail](https://github.com/formstr-hq/nail)はメールをギフトラップイベントとしてブリッジします。リリースはMDKグループ状態、バッジミント、QR署名者ペアリング、Androidブラウザ署名、共有ウォレット接続をカバーします。プロトコル作業はコメントパッチ、暗号化ファイルメタデータ、スレッドフォーマット、Marmot再起動保証、Concordメンバーシップリストに及びます。ディープダイブ: バッジとコメント。

## トップストーリー

### Amber 6.5.0はリレー認証のconfused deputyを解消し保存シークレットを暗号化

[Amber](https://github.com/greenart7c3/Amber)はAndroid向け[NIP-55](/ja/topics/nip-55/)(Android署名者インテント)および[NIP-46](/ja/topics/nip-46/)(リレー仲介リモート署名)署名者です。[バージョン6.5.0](https://github.com/greenart7c3/Amber/releases/tag/v6.5.0)は4件の開示済みギャップを解消します: ユーザーが承認していないリレー向けにkind `22242`の[NIP-42](/ja/topics/nip-42/)(クライアント・リレー認証)イベントを任意の呼び出し元が取得できた[リレー認証におけるconfused deputy](https://github.com/greenart7c3/Amber/security/advisories/GHSA-vx4h-56qj-wcp7); [NIP-46リプレイギャップ](https://github.com/greenart7c3/Amber/security/advisories/GHSA-h9fv-9247-3582); 平文の接続シークレットとローカル鍵を[保存時にエンベロープ暗号化](https://github.com/greenart7c3/Amber/security/advisories/GHSA-5fjp-ghh8-wch8); 復号前の呼び出し元認可、フェイルクローズ権限解析、平文`ws://`警告、セキュアQR画面、ログ秘匿、ログアウト時の遅延鍵ゼロ化、オプションのロック解除デバイスKeystore利用を含む[8項目のハードニングバッチ](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8844-q5vh-9j8f)。

[バージョン6.5.1](https://github.com/greenart7c3/Amber/releases/tag/v6.5.1)は、ロック解除デバイス要件の切り替え後にKeystore鍵がローテーションした際に保存済みNIP-46シークレットを再暗号化し、権限エディタのクラッシュを修正します。[バージョン6.5.2](https://github.com/greenart7c3/Amber/releases/tag/v6.5.2)はアプリケーション一覧が描画しない列の復号を停止し、Keystoreハンドルをキャッシュし、起動時にアカウントキャッシュをウォームアップし、リレーステータス通知をデバウンスします。

[先週の6.4.0](/ja/newsletters/2026-08-12-newsletter/#amber-640-makes-every-grouped-signing-decision-explicit)はグループ化署名決定を明示的にしました。6.5.xはAmberがそもそも何を承認するかを変えます。

### Cambium 0.4.0はWebサイト向け署名とリレー認証バーストの軽減

[Cambium](https://github.com/forgesworn/cambium)はAndroid向け[NIP-55](/ja/topics/nip-55/)プロキシで、[NIP-46](/ja/topics/nip-46/)経由でHeartwoodハードウェア署名者に接続します。2日間に6リリースが出荷されました。

[バージョン0.4.0](https://github.com/forgesworn/cambium/releases/tag/v0.4.0)はWebサイト向け署名を拡張します。ページは検証済み`nostrsigner:`コールバック経由で署名を要求でき、ネイティブアプリに付与された権限を継承しないため、ブラウザタブが別アプリの承認を借用できません。同リリースは仕様の最小イベント形状を修正します: `kind`と`content`のみを持つイベントが正しく署名され、CambiumがペアのNIP-46 ID、現在のタイムスタンプ、空のタグ配列を補完してからrust-nostrに渡します。ネイティブrust-nostr計測は同変更で必須の継続的インテグレーションゲートになりました。

[バージョン0.3.6](https://github.com/forgesworn/cambium/releases/tag/v0.3.6)は仕様準拠署名者とのペアリングを修復します。Cambiumの旧rust-nostrビルドはNIP-46 `connect`呼び出しの結果として文字列`ack`のみを受け入れたため、現在の仕様が求める（Heartwoodファームウェアが行う）bunker URIシークレットのエコーで応答する署名者は予期しない応答エラーでペアリングが終了していました。rust-nostr 0.44.2から0.44.8への移行で両形式が許容され、実機と依然`ack`で応答する`nak bunker`の両方で検証されました。

0.4.1から0.4.3のリリースは負荷下の入場制御がテーマです。[バージョン0.4.1](https://github.com/forgesworn/cambium/releases/tag/v0.4.1)はリアクション、投稿、削除、暗号化にリレー認証とバックグラウンド復号より先の予約キュースロットを与え、キューイング呼び出しに上限を設け、呼び出し元がタイムアウトしたら破棄し、過負荷時はフォアグラウンド署名画面を開かず終端の利用不可結果を返します。[バージョン0.4.2](https://github.com/forgesworn/cambium/releases/tag/v0.4.2)は次のリクエスト前にタイムアウトまたは長時間アイドルのNIP-46セッションを破棄し、同一kind `22242`認証イベントの並行コピーが1つのハードウェア署名を共有できます。[バージョン0.4.3](https://github.com/forgesworn/cambium/releases/tag/v0.4.3)はハードウェアワーカーに同一IDあたり最大1つの異なる認証チャレンジのみを入場させ、認証を内部で再試行せず、タイムアウト後はIDあたり60秒のクールダウンを開きながら完全一致のキャッシュ重複には応答します。リリースノートの計測はGrapheneOS端末で[Amethyst](https://github.com/vitorpamplona/amethyst)を駆動したものです: コールドスタートバーストで33件の即時過負荷応答と13件の完了リクエスト（署名者タイムアウトなし）、認証バースト中の新規ログインは承認後1.254秒で返りました。

### Citrine 3.1.0はスマートフォンリレーをグループホストとサイトホストに

[Citrine](https://github.com/greenart7c3/Citrine)はオンデバイスAndroidリレーです。[バージョン3.1.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.1.0)はリレーがホストできるものを変える3機能を追加します。

[NIP-29](/ja/topics/nip-29/)([リレーベースのグループ仕様](https://github.com/nostr-protocol/nips/blob/master/29.md) — リレー自体がメンバーシップとモデレーション状態を保持)のサポートにより、スマートフォンがグループに参加する代わりにグループをホストできます。[NIP-86](/ja/topics/nip-86/)([リレー管理API](https://github.com/nostr-protocol/nips/blob/master/86.md) — 認証済みJSON-RPCで管理操作を公開)は設定画面とともに到着し、許可リストとBANをAPIからもアプリからも駆動できます。[NIP-5A](/ja/topics/nip-5a/) [静的Webサイト](https://github.com/nostr-protocol/nips/blob/master/5A.md)のサポートにより、リレーはWebクライアント向けにnsiteを提供し、モダン化されたブラウズ一覧はアイコン、検索、最終更新順ソート、インストール進捗、説明、デフォルトで`nsite.run`、`nos.lol`、`nostr.land`の取得用リレーセットを備えます。

モデレーション面も[同リリース](https://github.com/greenart7c3/Citrine/releases/tag/v3.1.0)で拡大しました。公開鍵のローカルBANはその作者の保存イベントのパージを提案し、設定可能な`REJECTED_KINDS`リストがオペレーターが保存したくないkindをブロックし、アクセス制御は既存リストからインポートできます。再ブロードキャストツールは保存イベントを選択リレーへ再送し、スマートフォン保持アーカイブにネットワーク再シード手段を与えます。リリースはWebSocket `permessage-deflate`拡張を削除し、クエリホットパスを絞り、Tor公開設定変更時のTor起動・停止失敗を修正し、ログをローカルDBへ移しlogcatをデバッグビルドに限定しました。

### Vector 0.4.2はスパム波を乗り越えるコミュニティモデレーション

[Vector](https://github.com/VectorPrivacy/Vector)はデスクトップおよびAndroid向け[Concord](https://github.com/concord-protocol/concord)メッセンジャーです。[バージョン0.4.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.2)は負荷下のモデレーションに焦点を当てます。

急速なBANは以前は互いに上書きしていました。現在はキューイング、スタック、単一操作として確定するため、アカウントの波をBANしてもアカウントごとではなく1回の鍵ローテーションで済みます。解散済みコミュニティへの招待受諾は理由を説明し、ユーザーが所有する全デバイスから招待を削除し、ユーザーが所有するコミュニティの解散は[バージョン0.4.3](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.3)でどこでもコミュニティ一覧から消去します。バックグラウンドキャッチアップ中に届くコミュニティメッセージは送信直後のように通知を鳴らさず、入力中インジケータは送信時刻から期限切れになり、遅延シグナルがチャンネルに残りません。

[Concord](https://github.com/concord-protocol/concord)が定義するシャード化コミュニティ一覧は、もう一方のConcordクライアントArmadaとクロスクライアントレビューを受けました。リネームは一覧を膨らませず、同点は両クライアントで同一に解決し、未変更データはリレーへ再公開されません。ミュートはDMパスから外れました: ユーザーはメッセージ履歴なしでコミュニティから直接ミュートでき、通知とバッジはチャンネルとDMに適用されメッセージ自体は表示されたままです。ピン留めメッセージはクリック可能リンク付きの共有チャンネル面になり、ピン留めメッセージの編集は表示箇所すべてで追従します。ブロックリスト、ミュート、ニックネームはユーザーのデバイス間で同期し、ピン留めチャットも同期します。バージョン0.4.3は別Nostrクライアントが同一IDでサインイン中にVectorが入力中を告知するのを止め、x64とARM64の両方で15%で凍結していたWindows上のTorブートストラップを解消します。

### SonarはNIP-C7でメッシュメッセンジャーにスレッド返信

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar)はBluetoothメッシュおよびNostrメッセンジャーです。[バージョン0.1-alpha.13.1](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.13.1)は[NIP-C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) kind `9`チャットにSignal風返信、メンション、境界付きBluetooth再アセンブリ、バックアップ上限、メッシュパス署名検証、FCMプッシュフォールバックを追加します。[バージョン0.1-alpha.13.2](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.13.2)と[0.1-alpha.13.3](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.13.3)はAndroidのチャット起動クラッシュとiOSキーボード重なりを修正します。

### Nostriaはポッドキャスト公開を開始しリレーにカウントを依頼

[Nostria](https://github.com/nostria-app/nostria)はWebクライアントです。[バージョン4.1.70](https://github.com/nostria-app/nostria/releases/tag/v4.1.70)と[4.1.71](https://github.com/nostria-app/nostria/releases/tag/v4.1.71)はプレミアム加入者向けポッドキャスト公開を追加し、エピソードは署名済みNostrイベントです。[バージョン4.1.69](https://github.com/nostria-app/nostria/releases/tag/v4.1.69)はフィードで[NIP-45](/ja/topics/nip-45/) `COUNT`をリアクション、返信、zap合計に使い、ローカライゼーションを完了します。[先週の4.1.67](/ja/newsletters/2026-08-12-newsletter/#nostria-4167-expands-encrypted-community-administration)は暗号化コミュニティ管理を拡張しました。

## タグ付きリリース

### MDK 0.9.14: より高速なグループ作成を通じたフェイルクローズグループ履歴

[MDK](https://github.com/marmot-protocol/mdk)は[Marmot](https://github.com/marmot-protocol/marmot)向けRust開発キットで、MarmotはNostr上で運ばれる暗号化グループメッセージングプロトコルです。[バージョン0.9.12](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.12)は複数のグループ状態パスを推測ではなくフェイルクローズにします。欠落フォークアンカーはハードエラー([PR #1329](https://github.com/marmot-protocol/mdk/pull/1329))、leave提案はアトミックに永続化されクラッシュが半適用の退出を残せません([PR #1360](https://github.com/marmot-protocol/mdk/pull/1360))、インシデントリプレイはマニフェストなし改行区切りJSONストリームのフォーマットを推測しません([PR #1140](https://github.com/marmot-protocol/mdk/pull/1140))。収束テストも同時に拡大し、保持履歴クロスルートリカバリ([PR #1350](https://github.com/marmot-protocol/mdk/pull/1350))、クロスアダプター収束保証([PR #1372](https://github.com/marmot-protocol/mdk/pull/1372))、一般化孤立収束キャンペーン([PR #1357](https://github.com/marmot-protocol/mdk/pull/1357))を含みます。リレー拒否診断は汎用失敗に潰されず保持されます([PR #1361](https://github.com/marmot-protocol/mdk/pull/1361))。

[バージョン0.9.13](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.13)は8月18日にストレージフォーマットv2([PR #1421](https://github.com/marmot-protocol/mdk/pull/1421))、移行レール、ライブアカウントスナップショットを置くデルタ書き込み([PR #1435](https://github.com/marmot-protocol/mdk/pull/1435))、より高速な招待キャッチアップ([PR #1444](https://github.com/marmot-protocol/mdk/pull/1444))、macOSバインディング([PR #1402](https://github.com/marmot-protocol/mdk/pull/1402))とともに着地しました。[バージョン0.9.14](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.14)は8月19日にグループ作成の磨き込み: 事前アップロード創設画像([PR #1498](https://github.com/marmot-protocol/mdk/pull/1498))、KeyPackageバッチング([PR #1494](https://github.com/marmot-protocol/mdk/pull/1494))、アトミック初期メッセージ保持([PR #1497](https://github.com/marmot-protocol/mdk/pull/1497))、アカウント所有リレーでのプロフィール公開([PR #1495](https://github.com/marmot-protocol/mdk/pull/1495))が続きました。[MarmotKit 0.9.14](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-v0.9.14)と[wn-agent 0.9.14](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.14)はコアクレートとともに出荷します。
### Divine Mobile 1.0.20: アプリを離れずにバッジをミント

[Divine Mobile](https://github.com/divinevideo/divine-mobile)はNostr経由で動画を公開・取得するショート動画クライアントです。[バージョン1.0.20](https://github.com/divinevideo/divine-mobile/releases/tag/v1.0.20)はユーザーが[NIP-58](/ja/topics/nip-58/)バッジ（本号最初のディープダイブで説明する署名付与イベント）をミントし、アプリを離れずに誰かに渡せます。プロフィールのバッジをタップすると獲得条件が説明され、定義イベントと付与イベントが別保存されるため通常未実装になりがちな仕様部分です。

[リリース](https://github.com/divinevideo/divine-mobile/releases/tag/v1.0.20)の残りはクライアント作業です: ライトテーマ、ストップモーションエディタのクロップ・回転・反転、レコーダーから1タップの下書き、動画に対するキャプションタイミング、視聴済み素材を下げる優先度のフィード、エディタ・レコーダー・プロフィールタブのスクリーンリーダー対応、低モーション処理、アカウント設定でのDivineメールとパスワード管理およびアカウントリンク・解除。削除動画はローカル状態を残し、ブックマークは永続化します。[先週の1.0.19](/ja/newsletters/2026-08-12-newsletter/#divine-mobile-1019-tightens-accounts-private-messages-and-publishing)はアカウント分離とDM検証を強化しました。バッジ発行はその上の新しい公開面です。

### ClipRelay 0.2.0: カメラで署名者をペアリング

[ClipRelay](https://github.com/tajava2006/cliprelay)はNostr経由でデバイス間クリップボードを同期します。[Androidバージョン0.2.0](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.2.0)は`nostrconnect://` QRログインを追加し、別スマートフォンの署名者アプリでサインインでき、bunker URLのカメラスキャンを追加し、シークレット含有文字列をメッセンジャー経由で貼る習慣を取り除きます。Bunker接続はハングせず60秒でタイムアウトし、Amberログイン失敗後の再試行ボタンが動作します。[デスクトップバージョン0.2.0](https://github.com/tajava2006/cliprelay/releases/tag/desktop%2Fv0.2.0)はタイムアウトとログインタブ修正を引き継ぎます。

[バージョン0.1.4](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.1.4)は短いリレー有効期限付き機密クリップボード同期、ピン留め署名者セッションリレー、ローカル合成`EOSE`ではなく実ラウンドトリップを要求する生存プローブを追加しました。[先週の0.1.3](/ja/newsletters/2026-08-12-newsletter/#cliprelay-013-restores-relay-and-signer-connections-after-idle-periods)はアイドル後の接続を復元しました。

### Bark 1.3.9: Androidで動くブラウザ署名者

[Bark](https://github.com/forgesworn/bark)は[NIP-07](/ja/topics/nip-07/)(Webページが署名や暗号化操作を要求する`window.nostr`インターフェース)を提供するブラウザ拡張です。[バージョン1.3.9](https://github.com/forgesworn/bark/releases/tag/v1.3.9)はFirefoxビルドのAndroidサポートを宣言し、アドオン一覧がスマートフォンにインストールできます。Android版Firefoxはwindows APIを実装しないため、ポップアップウィンドウを開く承認はすべて拒否されていました。承認面はフォアグラウンドタブにフォールバックし、閉じると拒否、レビュー操作で前面化、リクエスト確定後にバックグラウンドを閉じます。リリースノートはGrapheneOS上Pixel 10 Pro XL、Firefox 153.0.4での検証を記録し、Android版Chromiumは拡張サブシステムをコンパイルアウトするためChromium系AndroidブラウザではBarkを一切実行できないと明記します。

[バージョン1.3.8](https://github.com/forgesworn/bark/releases/tag/v1.3.8)は逆方向のNIP-46相互運用欠陥を修正しました。BarkはイベントをJSONオブジェクトとして送るコンパクトHeartwood署名方言をプローブし、厳密型署名者（`nak`やrust-nostrベースbunkerを含む）は解析できず黙って破棄するため署名がハングしていました。プローブはHeartwoodと自己申告した署名者にのみ送られ、他の署名者は最初の署名から標準`sign_event`呼び出しを受けます。

### Bray 3.0.0とToll Booth 6.0.0は共有ウォレット接続ライブラリへ移行

[Bray](https://github.com/forgesworn/bray)と[Toll Booth](https://github.com/forgesworn/toll-booth)はどちらも[NIP-47](/ja/topics/nip-47/) Nostr Wallet Connect（暗号化Nostrイベント経由でアプリがウォレットに支払いを要求する仕様）で支払います。[Bray 3.0.0](https://github.com/forgesworn/bray/releases/tag/v3.0.0)と[Toll Booth 6.0.0](https://github.com/forgesworn/toll-booth/releases/tag/v6.0.0)はそれぞれ[nwc-kit](https://github.com/forgesworn/nwc-kit)採用の破壊的変更を宣言し、Toll Boothは同変更でpayer資格フローを削除します。両者は2つの独立ランナー間で出力がバイト同一の再現可能ビルドを公開し、リリースノートにtarballハッシュを印字して読者がレジストリアーティファクトを検証できます。

Toll Boothパッチが3件続きました: [6.0.1](https://github.com/forgesworn/toll-booth/releases/tag/v6.0.1)は交渉デプロイホスト鍵をピン留め、[6.1.1](https://github.com/forgesworn/toll-booth/releases/tag/v6.1.1)はパッチ対象の`cashu-ts`をピン留め、[6.1.2](https://github.com/forgesworn/toll-booth/releases/tag/v6.1.2)はイメージビルドを復元します。

### NoorNote 1.3.4: 招待リンクから暗号化コミュニティに参加

[NoorNote](https://github.com/77elements/noornote)はデスクトップ、Web、Android向けNostrクライアントです。[バージョン1.3.4](https://github.com/77elements/noornote/releases/tag/v1.3.4)は暗号化ArmadaおよびConcordコミュニティをアドオンとして追加します: ユーザーは招待リンクで参加し、設定に参加コミュニティ一覧が表示され、アクティビティ通知を受け取ります。同リリースは外部引用投稿（Web記事段落を引用するハイライトノート）をグローバルまたは作者ごとに非表示にする制御を追加し、そのリポストも非表示にしつつユーザー自身のハイライトは表示を維持します。プロフィール解決も修復され、プロフィールは切り詰め公開鍵や匿名プレースホルダーとして描画されなくなりました。

[バージョン1.3.5](https://github.com/77elements/noornote/releases/tag/v1.3.5)は長文ノート用エクスパンダーとArmada招待リンク入力のレイアウト修正を追加します。[先週の1.3.2](/ja/newsletters/2026-08-12-newsletter/#noornote-132-moves-article-discovery-into-the-social-graph)は記事発見をソーシャルグラフへ移しました。コミュニティメンバーシップは別面です。

### Mostroは紛争チャットをギフトラップから移行

[Mostro](https://github.com/MostroP2P/mostro)は注文とメッセージがNostrイベントとして走るP2P取引デーモンで、[mostro-core](https://github.com/MostroP2P/mostro-core)が共有ライブラリ、[Mostro Mobile](https://github.com/MostroP2P/mobile)がクライアントです。[Mobile 1.3.2](https://github.com/MostroP2P/mobile/releases/tag/v1.3.2)は紛争チャットを[NIP-59](/ja/topics/nip-59/)ギフトラップからkind `14`チャットエンベロープへ移行し、バックログを会話ごとの永続カーソルで支えます。[mostro-core 0.14.5](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.5)はギフトラップ内のrumor識別子を直列化([PR #164](https://github.com/MostroP2P/mostro-core/pull/164))、[0.14.4](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.4)は評価平均バグを修正([PR #163](https://github.com/MostroP2P/mostro-core/pull/163))、[Mobile 1.3.1](https://github.com/MostroP2P/mobile/releases/tag/v1.3.1)は暗号化チャット添付を保持するBlossomサーバーへ切り替えます。デーモン[0.18.2](https://github.com/MostroP2P/mostro/releases/tag/v0.18.2)または[0.18.4](https://github.com/MostroP2P/mostro/releases/tag/v0.18.4)を使用してください。

### NYM 3.73.522: 暗号化グループチャットと暗号化ローカルストア

[NYM](https://github.com/Spl0itable/NYM)は独自アシスタント統合を持つNostrクライアントです。[バージョン3.73.522](https://github.com/Spl0itable/NYM/releases/tag/v3.73.522)は[3.73.521](https://github.com/Spl0itable/NYM/releases/tag/v3.73.521)が暗号化グループチャットを洗練した後にローカルSQLiteストアを暗号化し、[3.73.520](https://github.com/Spl0itable/NYM/releases/tag/v3.73.520)はコンテンツセキュリティポリシー破断と重複新着表示を修正します。

### Morganite 0.0.4: キャッシュ前にblobを検証

[Morganite](https://github.com/greenart7c3/Morganite)はAndroid向け[Blossom](/ja/topics/blossom/)サーバーで、BlossomはコンテンツSHA-256ハッシュでファイルをアドレスし、保持ホストから提供するメディアプロトコルです。[バージョン0.0.4](https://github.com/greenart7c3/Morganite/releases/tag/v0.0.4)はダウンロード中に1パスでblobハッシュを検証してからキャッシュし、受信側でコンテンツアドレッシングを意味あるものにするチェックです。リリースは保存のたびにディレクトリを再スキャンせずキャッシュサイズを増分追跡し、ブロッキングネットワーク呼び出しを入出力スレッドへ移し、MIME検出でTikaインスタンスを再利用し、ログをローカルDBに永続化します。

## 新規発見

### NailはメールをギフトラップイベントとしてNostrへ

[Nail](https://github.com/formstr-hq/nail)はFormstrチーム（[Formstr](https://github.com/formstr-hq/nostr-forms)と[nostr-calendar](https://github.com/formstr-hq/nostr-calendar)の背後）によるMITライセンスのメールブリッジ兼Webクライアントです。8月18日に[PR #7](https://github.com/formstr-hq/nail/pull/7)でローンチし、22ファイル変更でメールイベントへの`k`タグ、設定での鍵リカバリ、ウェルカムメッセージを追加しました。デプロイは[mailstr.app](https://mailstr.app)で稼働し、ブリッジ自身の`_smtp` [NIP-05](/ja/topics/nip-05/)(ドメイン名をNostr公開鍵にマップするDNS方式)レコードを提供します。

メール自体はNostrイベントです。クライアントの[constants](https://github.com/formstr-hq/nail/blob/main/client/src/lib/nostr/constants.ts)はkind `1301`メールrumorをkind `1059` [NIP-59](/ja/topics/nip-59/)ギフトラップ内に載せ、プライベートDMと同じメタデータ秘匿エンベロープで受信者へ届けます。配送リレーはkind `10050` [NIP-17](/ja/topics/nip-17/)受信箱リストとその背後のkind `10002` [NIP-65](/ja/topics/nip-65/)リレーリストから来ます。フォルダは`mail`名前空間下のkind `1985` [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md)ラベル、クライアント設定はkind `30078` [NIP-78](/ja/topics/nip-78/)アプリケーションデータイベントにあります。60,000バイト超の添付は[NIP-44](/ja/topics/nip-44/)が暗号化平文を65,535バイトに上限するためイベントではなく[Blossom](/ja/topics/blossom/)へ行きます。アドレスはドメイン上のnpubで、NIP-05レコードのないローカルドメインは存在しないメールボックスとして扱われます。

ブリッジ半分は[mailcow](https://github.com/mailcow/mailcow-dockerized)デプロイ横でパッチなしに動くNode LMTPサーバーです: Postfixが一致ドメインをブリッジへルーティングし、ブリッジはSMTP経由で返信を注入します。その設計はメールブリッジで最も難しい問い、`From`ヘッダーが何を証明するかに正直に答えます。Nailの[受信パス](https://github.com/formstr-hq/nail/blob/main/client/src/lib/mail/receive.ts)は各メッセージを4つの出所状態のいずれかに分類します: 設定ブリッジが封印し上流で検証しなかった送信者は中継拒否、ユーザー自身が封印、住所のNIP-05が封印鍵に解決、ヘッダーを裏付けるものが一切ない。最後の場合インターフェースは封印公開鍵にフォールバックし、イベントが実際に証明できる唯一のIDです。ブリッジAPI呼び出しは[NIP-98](/ja/topics/nip-98/)署名HTTPイベントで認証されます。

### Glowはパスキー派生ID下でリレーにウォレットラベルを保存

[Glow](https://breez.technology/glow/)はBreezの自己保管Lightningウォレットです。パスキーログインがNostr IDを導出し、ウォレットラベルはそのID下でリレーから一覧・保存され、部分リレーカバレッジ間でバイト同一の重複が潰されます。

## 開発中

### Amethystはリレー認証決定フローを再構築

[Amethyst](https://github.com/vitorpamplona/amethyst)はAndroid Nostrクライアントです。マージ済み作業のブロックが[NIP-42](/ja/topics/nip-42/)クライアント・リレー認証の扱いを再形成します。権限インターフェースと決定フローを再設計([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899))、認証はタイムアウトではなくチャレンジ解決を待つ([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905))、新規アカウントはデフォルトで常にリレーと認証([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931))、「常にログイン」選択がアカウント自身が使わないリレーでも尊重される([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937))。認証は[NIP-29](/ja/topics/nip-29/)グループとConcordコミュニティを参加会場として認識([PR #3906](https://github.com/vitorpamplona/amethyst/pull/3906))し、リレーホストグループが開くたび見知らぬリレーのように見えるのを防ぎます。

他2変更がプロトコル面に触れます。[NIP-13](/ja/topics/nip-13/)下のプルーフ・オブ・ワークマイニングはマイニング中に`created_at`を更新しGPUパス分析を獲得([PR #3911](https://github.com/vitorpamplona/amethyst/pull/3911))、フルスクリーンナプレットホストが入力方式インセットを処理([PR #3932](https://github.com/vitorpamplona/amethyst/pull/3932))。設定エントリ付きガイド付き初回鍵バックアップもマージ([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909))、公開チャットのミュート能力も([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939))。

### nostrordは未マージ暗号化鍵提案を実装

[nostrord](https://github.com/nostrord/nostrord)はリレースコープグループ中心のNostrチャットクライアントです。NIP-4e（メッセージ暗号化をID鍵から切り離す未マージ提案。Compassは[7月15日号](/ja/newsletters/2026-07-15-newsletter/)で最後に記述）の実装をマージしました。アカウントは自身のkind `10044`暗号化鍵を告知し、秘密半分をローカル保持し、受信DMをプロセス内復号し、bunkerやブラウザ拡張を読取パスから完全に外します([PR #261](https://github.com/nostrord/nostrord/pull/261))。kind `4454`と`4455`のデバイスペアリングが鍵を第2デバイスへ移し、自己アーカイブが新鍵宛て履歴を再公開します。送信は最初から告知鍵宛て([PR #247](https://github.com/nostrord/nostrord/pull/247))、フォローアップが交渉成功だけで鍵を渡さないペアリングを修正([PR #271](https://github.com/nostrord/nostrord/pull/271))。PRはオープン提案と乖離する箇所でデプロイ済みJumble実装に従うと述べ、この仕様の実動定義を文書ではなく出荷コードに置きます。

グループIDは同バッチで絞られました。グループ識別子はリレー内でのみ一意([PR #269](https://github.com/nostrord/nostrord/pull/269))、2リレー上の同一識別子は2グループとして扱われ([PR #272](https://github.com/nostrord/nostrord/pull/272))、スレッド投稿はフォーラム投稿として描画([PR #274](https://github.com/nostrord/nostrord/pull/274))。kind `22242`署名プロンプトを繰り返し出す接続チャーンも停止([PR #268](https://github.com/nostrord/nostrord/pull/268)) — 今週Cambiumが3リリース費やした署名者圧力と同クラスです。

### nostreamはリレーモニター追加と招待コードミント

[nostream](https://github.com/cameri/nostream)はTypeScriptリレー実装です。[NIP-66](/ja/topics/nip-66/)リレー監視イベント（他リレーの生存・能力データをモニターが告知する発見仕様）を公開するクラスタワーカーとプローブスケジューラをマージ([PR #724](https://github.com/cameri/nostream/pull/724))、設定スキーマとデフォルト([PR #689](https://github.com/cameri/nostream/pull/689))、インテグレーションテスト([PR #733](https://github.com/cameri/nostream/pull/733))。CLIツールが[NIP-43](/ja/topics/nip-43/)招待コード（入場をゲートするリレーアクセスメタデータ方式）をミント([PR #732](https://github.com/cameri/nostream/pull/732))、リレーは実装済みだった[NIP-13](/ja/topics/nip-13/)プルーフ・オブ・ワークをサポート一覧で告知([PR #680](https://github.com/cameri/nostream/pull/680))。DVMジョブは永続化移行とリポジトリを獲得([PR #727](https://github.com/cameri/nostream/pull/727))、リレーは[NIP-90](/ja/topics/nip-90/)(DVMジョブリクエスト)をトラップしジョブリポジトリ経由で記録([PR #729](https://github.com/cameri/nostream/pull/729))。

### rust-nostrはギフトラップ識別子を修正し保護リポストを拒否

[rust-nostr](https://github.com/nostrdevkit/nostr)は本号のRust・モバイルクライアント作業の大きな割合の背後にあるRustライブラリとSDKです。ギフトラップ封印暗号化前にrumor識別子を計算([PR #1444](https://github.com/nostrdevkit/nostr/pull/1444)) — 今週Mostroが自ライブラリで修正した欠陥と同クラス。ローカルリレーは[NIP-70](/ja/topics/nip-70/)保護イベントのリポストを拒否([PR #1445](https://github.com/nostrdevkit/nostr/pull/1445)) — その仕様が存在する保護。NIP-47応答解析は欠落・null amountを許容([PR #1450](https://github.com/nostrdevkit/nostr/pull/1450))。リレーURL解析を強化([PR #1451](https://github.com/nostrdevkit/nostr/pull/1451))。

### NDKはポスト量子DMを追加しGPL依存を削除

[NDK](https://github.com/relaystr/ndk)はNostr向けDart開発キットです。ML-KEM-1024（FIPS 203として標準化された格子KEM）を用いたDM向けハイブリッドポスト量子暗号をマージ([PR #713](https://github.com/relaystr/ndk/pull/713))、古典鍵合意に置き換えるのではなく並置。別変更がGPL-3.0-only Dilithium実装をML-DSA署名標準の`fips204`へ置換([PR #712](https://github.com/relaystr/ndk/pull/712))、キットを埋め込むアプリのライセンス制約を除去。接続も各1 IDへ([PR #710](https://github.com/relaystr/ndk/pull/710))。

### Nostterはブックマークリスト、プロフィールバッジ、Blossomアップロードを追加

[Nostter](https://github.com/SnowCait/nostter)はWebクライアントです。標準とレガシー両形状の[NIP-51](/ja/topics/nip-51/)ブックマークリスト([PR #2311](https://github.com/SnowCait/nostter/pull/2311))、NIP-58プロフィールバッジ処理更新([PR #2281](https://github.com/SnowCait/nostter/pull/2281))、Blossomメディアアップローダー([PR #2298](https://github.com/SnowCait/nostter/pull/2298))、メンションオートコンプリートに[NIP-05](/ja/topics/nip-05/)識別子（DNS検証名）表示([PR #2303](https://github.com/SnowCait/nostter/pull/2303))をマージしました。

### Zap Cookingは管理ルートを署名リクエストに拘束し保存ウォレット接続を暗号化

[Zap Cooking](https://github.com/zapcooking/frontend)はNostr長文イベント上のレシピサイトです。セキュリティバッチは保存Nostr Wallet Connect接続文字列をNIP-44エンベロープ内で保存時暗号化([PR #622](https://github.com/zapcooking/frontend/pull/622))、管理ルートのなりすまし可能公開鍵比較を[NIP-98](/ja/topics/nip-98/) HTTP認証（HTTPリクエストを認可するイベント署名方式）へ置換([PR #626](https://github.com/zapcooking/frontend/pull/626))、ログアウトでアカウントデータを消去し保留NIP-46レコードに上限([PR #627](https://github.com/zapcooking/frontend/pull/627))。
## プロトコルと仕様作業

### NIPs

この期間中に[nostr-protocol/nips](https://github.com/nostr-protocol/nips)へマージされたPRはありません。前号終了後に6提案がオープンし、3件はドラフト初出後の8月18日です。

[NIPs PR #2438](https://github.com/nostr-protocol/nips/pull/2438)はNIP-9A、コメントベースパッチを提案します。パッチは親としてパッチ対象イベントを参照するkind `1111`コメントで、`content`がリテラルラベル`PATCH`で始まりパッチ行が続きます。数字で始まる行は`<index> -<deleted> +<inserted> <inserted characters>`形式で対象`content`を編集し、バイトではなくUnicode文字で数え、`t`で始まる行は`title`、`description`、`subject`、`picture`など人間向けタグを置換します。設計は意図的に後方互換: 形式を理解しないクライアントは通常のラベル付きコメントとして表示し、理解するクライアントはパッチを適用してコメントを非表示にします。提案はkind `1`、`11`、`1111`、`24`、`1621`をパッチ可能と名指し、書き手と読み手の双方に過大・過多・原イベントから長期後のパッチ拒否を求め、不変イベントの一般編集チャンネル化を明示的に防ぎます。

[NIPs PR #2437](https://github.com/nostr-protocol/nips/pull/2437)は[NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)（kind `1063`イベントでアップロードファイルを記述するファイルメタデータ仕様）向けファイル暗号化を提案します。3つのオプションタグを追加: `encryption-algorithm`（列挙は`aes-gcm`のみ）、16進`decryption-key`と`decryption-nonce`。タグ意味はそれに合わせてシフトし、`m`は暗号化前MIME、`x`は暗号化ファイルハッシュ、`ox`は原本ハッシュ、任意の`thumb`、`image`、`fallback`ソースも同一鍵・nonceで暗号化。目的は公開Blossomオペレーターがバイト内容を判別できないことで、作者は[NIP-17](/ja/topics/nip-17/) DM暗号化特性をファイルメタデータへコピーし、`imeta`タグ内でも同処理が動くと位置づけます。

[NIPs PR #2436](https://github.com/nostr-protocol/nips/pull/2436)はNIP-7D（[NIP-22](/ja/topics/nip-22/) kind `1111`コメントを返信とするkind `11`スレッドイベント上のフォーラムスレッド仕様）を修正します。スレッド投稿をkind `1`ノート同様にインライン画像、リンク、[NIP-27](/ja/topics/nip-27/)参照でフォーマット可能とする節を追加し、曖昧文法の軽量マークアップDjotもサポート可能とします。論点はフォーマット未指定が eventual なMarkdownデフォルト実装を招くことで、PRは既存Djot実装squalkを指します。

[NIPs PR #2439](https://github.com/nostr-protocol/nips/pull/2439)は[NIP-86](/ja/topics/nip-86/)（リレー管理コマンド）に`assign`と`unassign`メソッドを追加し、リレー管理者がマスター鍵を共有せず別pubkeyに管理権限を付与できます。

[NIPs PR #2442](https://github.com/nostr-protocol/nips/pull/2442)は[1月号でCompassがカバーした](/ja/newsletters/2026-01-13-newsletter/)オーディオトラック提案の後継で、先のPRはクローズ済み、本PRはlightning.fmでkind `31337`トラックイベント、kind `31339`リリースオブジェクト、バンドプロフィール、トラックごと貢献者、オプション[NIP-57](/ja/topics/nip-57/) zap分割を本番出荷し販売は[NIP-99](/ja/topics/nip-99/)に留めます。相互運用契約は[lightning.fm/interop](https://lightning.fm/interop)に公開、デスクトップパブリッシャーと自己ホスト販売デーモンはオープンソースです。

### Marmot

[Marmot PR #416](https://github.com/marmot-protocol/marmot/pull/416)は8月13日マージし、プロトコルコアに耐久性と再起動契約を追加します。採択文書は決定論的収束、保持候補親素材、適用前公開、履歴欠落時フェイルクローズを既に定義していましたが、それらの境界でプロセスが中断されたときの一意ルールがありませんでした。変更は回復可能論理事実、再起動等価、公開・収束中断境界、オブザーバーアトミック遷移、欠落・破損素材処理、アプリケーション効果回復を定義し、各々にクラッシュ・再起動適合シナリオを追加します。トランザクション、ジャーナル、スナップショット、リプレイ戦略、スケジューラ、ストレージ形式は実装定義のまま、ワイヤエンコーディング変更は不要と明記。排除する具体失敗は、外部受理されたがローカル未確認の公開、または部分適用選択ブランチが、再起動後に実装依存のプロトコル結果を生むことです。

### ConcordとCORDs

[Concord PR #18](https://github.com/concord-protocol/concord/pull/18)（先週号ではオープン提案としてカバー）は8月15日マージ済み。暗号化コミュニティ一覧をkind `33302`イベントにシャードし、50メンバーシップ上限を削除、退役エントリを剪定して一覧をリレーサイズ上限内に保ちます。Vector今週のリリースノートは同点解決と未変更データ再公開停止を含むクライアント側半分を記録します。

[Concord PR #22](https://github.com/concord-protocol/concord/pull/22)はコミュニティ所有AVブローカーを提案します。CORD-02メタデータエンティティはリレー横にオプション`av_brokers`リストを持ち、他エンティティ同様エディションで進化し、CORD-07ランデブーはそのリスト（コミュニティが未公開ならメンバー自身のブローカー）から、既存ルーム鍵タイブレーク順で引きます。presence上のブローカータグは残差分割報告に読み取り有用なまま、ルーティングから降格する論点は直接的: ルーティングに使うと仲間メンバーの非信頼入力がコミュニティ自身の指示より優先されます。

[Concord PR #23](https://github.com/concord-protocol/concord/pull/23)はCORD-05で既存実装挙動を規範化します。参加永続化前にオーナー創世メタデータエディションが配送鍵下で開き、ローテーション面はコンパクション対にアンカー。PRは最初からライブ脆弱性ではなかったと述べます: Vectorのバンドル受理は配送ルートがオーナー創世を開けないバンドルを拒否し、既に保持コミュニティの招待を駐車せず、Armadaも保持コミュニティのベースを動かすバンドルを破棄。ギャップは仕様がどちらも要求していなかったため、仕様忠実クライアントが脆弱版を出荷できた点です。

[Blossomアップグレード文書](https://github.com/hzrd149/blossom)、[Nappletアプリケーション提案](https://github.com/napplet/naps)、[Gamma Markets仕様](https://github.com/GammaMarkets/market-spec)はこの期間変更なし。

## NIPディープダイブ

### バッジ (NIP-58)

[NIP-58](/ja/topics/nip-58/)は[一次仕様](https://github.com/nostr-protocol/nips/blob/master/58.md)により、1つのNostr IDが別IDへ命名トークンを付与し、受信者がプロフィール表示を制御する手段を与えます。解決する問題は、Nostr上の人物に関する記述がそれ以外は単なるノートであること — 誰が主張を発行し、何と呼ばれ、どう見えるか、主体が受け入れたかを言う構造がないことです。バッジは3つの独立署名イベントと3つの著者意図でその主張を与えます。

[仕組み](https://github.com/nostr-protocol/nips/blob/master/58.md)はアドレス可能定義、付与、表示リストから成ります。バッジ定義は発行者が公開するkind `30009`イベントで、`d`タグでアドレス可能 — 発行者は`name`、`description`、`image`、`thumb`タグを後から改訂でき、他が指す識別子は変わりません。付与は同一発行者のkind `8`イベントで、定義の`30009:<issuer-pubkey>:<d-identifier>`座標を持つ`a`タグと1つ以上の受信者`p`タグを載せます。表示リストは受信者のkind `30008`イベントで固定`d`値`profile_badges`、`a`と`e`タグペアを列挙 — `a`は定義座標、`e`は特定付与イベント。ペアとして順序付き読み取り: 一致付与のない`a`、一致定義のない`e`は無視され、半参照バッジは黙って描画されません。

[仕様](https://github.com/nostr-protocol/nips/blob/master/58.md)が拒否することにトレードオフが見えます。失効も期限もなく、付与は発行者によるその時点の永久声明で、考えを変えた発行者は付与が指す定義のみ変更可能。譲渡もなく、バッジはトークンとして流通しません。信頼発行者レジストリもなく、信頼はクライアントと読者へ — バッジの価値は見る人にとって発行者公開鍵の価値そのもの。仕様はクライアントが受信者が列挙したより少ないバッジを表示し、どの画像サイズを描画するか選ぶ余地を与え、プロフィールが第三者だけが選んだグラフィックの壁にならないようにします。

最も近い隣接仕様は[NIP-51](/ja/topics/nip-51/)([リスト仕様](https://github.com/nostr-protocol/nips/blob/master/51.md))で、比較するとバッジが3イベントを要する理由が分かります。リストは単一著者が参照をキュレート — リスト著者が主張の著者。バッジは著者を二分し、発行者が付与を、受信者が表示受諾を署名。どちらか一方だけでは可視結果を作れず、自己適用ラベルとの差です。

今週[nos.lol](https://nos.lol)と[relay.primal.net](https://relay.primal.net)から回収した稼働中kind `8`付与:

```json
{
  "id": "08504dec368939bd63849a349cab83dea0ac199a852129dbf68cf35fe5c64e96",
  "pubkey": "bef514bd58c8ceea4beb9e6b84a8d983935f7be26f49e14df68098f1ba64156e",
  "created_at": 1787051248,
  "kind": 8,
  "tags": [
    ["a", "30009:bef514bd58c8ceea4beb9e6b84a8d983935f7be26f49e14df68098f1ba64156e:blocks_orange_league"],
    ["p", "92dfa05d915196a7a09152fa3f57871debfd422e1d278ac5af266a70c3350b1f", "wss://relay.damus.io"]
  ],
  "content": "Badge awarded!",
  "sig": "5bf0218dfec5e56b47339b0b4b992cceedd2e18798fb3d47cafea51850c00827f66251e4a3e08190370e04a5e1d4d092eeb441141b7219acdd18b80290a022f8"
}
```

現在の実装は発行、表示、読取をカバーします。[Divine Mobile 1.0.20](https://github.com/divinevideo/divine-mobile/releases/tag/v1.0.20)はアプリ内でバッジをミント・付与し、読者がタップした獲得バッジを説明し、[Nostter PR #2281](https://github.com/SnowCait/nostter/pull/2281)はWebクライアントのプロフィールバッジ処理を更新し、[Amethyst](https://github.com/vitorpamplona/amethyst)は自身のクライアントタグ付き付与イベントを公開 — 上例と並ぶリレーデータに1件現れます。

### コメント (NIP-22)

[NIP-22](/ja/topics/nip-22/)は[一次仕様](https://github.com/nostr-protocol/nips/blob/master/22.md)により、短文ノートでないものへの返信向け一般コメントイベントを提供します。短文スレッドは既に[NIP-10](/ja/topics/nip-10/)があり、kind `1`と返信チェーン周りのタグ慣習が成長しました。NIP-22は動画、記事、カレンダーイベント、wikiページ、URLなど、対象kindを識別し、対象がアドレス可能でもNostrイベントでない外部リソースでも動く返信構造が必要なため存在します。

[仕組み](https://github.com/nostr-protocol/nips/blob/master/22.md)は大文字小文字の区別が要です。コメントはkind `1111`イベントで2組タグを持ちます: 大文字タグが議論のルート、小文字が直接親を記述。`E`、`A`、`I`はルートイベント、ルートアドレス可能座標、ルート外部識別子、`K`はルートkind、`P`はルート著者。小文字`e`、`a`、`i`、`k`、`p`は親について同じ事実 — トップレベルコメントでは親＝ルート、ネスト返信では別kind `1111`コメント。分割によりクライアントは大文字ルートタグ1フィルタで議論全体を取得でき、小文字親タグからネストを正しく描画。`I`/`i`変種は[NIP-73](/ja/topics/nip-73/)形式の外部識別子を載せ、Webページ、ポッドキャストエピソード、書籍へのコメントスレッド接続を可能にします。

トレードオフは主にNIP-22が吸収しないことについてです。[仕様](https://github.com/nostr-protocol/nips/blob/master/22.md)はコメントをkind `1`ノートへの返信に使わないと述べ、2つのスレッドモデルが同一オブジェクトで競合するのを防ぎ、既に動く場所ではNIP-10を残します。ネストは許可されますがルートは固定 — 深いスレッドでも中間イベントが欠けてもアンカーを失いません。kindタグが荷重部分: 対象なしでコメントを取得しても`K`/`k`から何を見ているか分かり、そのkindを描画できるか判断できます。仕様が提供しないのは順序・モデレーションモデル — 表示順、折りたたみ、非表示は完全にクライアント方針です。

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md)との比較では差は型付けにあります。NIP-10は対象がノートであると仮定しスレッド内位置を符号化; NIP-22は対象のIDとkindを明示し他は一切仮定しません。その明示型付けが本号の新提案がkind `1111`を選ぶ理由です。

今週[nos.lol](https://nos.lol)と[relay.primal.net](https://relay.primal.net)から回収した稼働中kind `1111`コメント — 動画下の別コメントへの返信:

```json
{
  "id": "c8d335f8bfea58ecd1a943d6000fb2045f4bddf4a36c67df53eb661671f7ab45",
  "pubkey": "3e911baba55ae247339cf805dd6ff49ad2cd6bee84ac44e088ce66450c49104f",
  "created_at": 1787062681,
  "kind": 1111,
  "tags": [
    ["E", "1c492f2bac17b79d66934a340fa43d8d30d0aea4c9fa329346c05573ef912d70", "", "482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839"],
    ["A", "34236:482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839:e64ba9ea157b1a315caff51dbca656ed73ce817d4494e3966adf24055a86f5c5", ""],
    ["K", "34236"],
    ["P", "482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839"],
    ["e", "7a14723b9ef999e74b1757a0fb74942cb6c121138d4ddafe096a57a67ed0a442", "", "8b69e548402afa997343d73e8088224a440f256350f6257b61acc4bb1fa4af4f"],
    ["k", "1111"],
    ["p", "8b69e548402afa997343d73e8088224a440f256350f6257b61acc4bb1fa4af4f"],
    ["client", "Divine", "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile", "wss://relay.divine.video"]
  ],
  "content": "niiice",
  "sig": "a5517fdea07647efa7ab1730fbea8df882690bba667e93ea5aeba4a73be6a49af1ee17c045535483650caf41dbbcb0897d5803fa39b59f395fd6f9bb193bb789"
}
```

大文字タグは動画と著者を保持し、小文字`e`/`k`は親コメントを指す — 仕様が述べる形状です。kind `1111`を読み書きする実装には、上イベントにクライアントタグが現れる[Divine Mobile](https://github.com/divinevideo/divine-mobile)、同リレー結果にコメントが現れる[Amethyst](https://github.com/vitorpamplona/amethyst)、今週スレッド投稿をフォーラム投稿として描画する[nostrord](https://github.com/nostrord/nostrord/pull/274)があります。[NIPs PR #2438](https://github.com/nostr-protocol/nips/pull/2438)の提案パッチ形式も同kind上に構築されます。

---

プロジェクトやニュースを共有するには[NIP-17](/ja/topics/nip-17/) DMを[Nostr Compassプロジェクト](https://github.com/andotherstuff/nostr-compass)へ送ってください。
