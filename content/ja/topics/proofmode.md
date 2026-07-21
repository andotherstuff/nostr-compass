---
title: "ProofMode"
date: 2026-07-15
translationOf: /en/topics/proofmode.md
translationDate: 2026-07-15
draft: false
categories:
  - Media
  - Provenance
---

[ProofMode](https://proofmode.org/)は、Guardian Project、WITNESS、Okthanksによって作られたオープンソースのmedia-provenanceツールキットで、撮影の瞬間に写真や動画へ検証可能な真正性とchain-of-custodyのデータを付与します。Nostr固有のものではありません。ProofModeデータを運ぶNostr clientは、新しいプロトコル層ではなく、既存の外部標準を統合しているのです。

## 仕組み

ProofModeのCaptureコンポーネントは、撮影中にprovenance metadataをmediaファイルへ直接埋め込み、Content Authenticity Initiative(CAI)、Content Credentials(CR)、C2PAが使うのと同じ相互運用可能な標準をサポートします。別のVerifyコンポーネントは、audio、画像、動画ファイルを検査して、そのmetadataにAI生成や後からの編集の痕跡がないかをチェックし、Preserveコンポーネントは、長期アーカイブのために、基盤となるproofデータの冗長で分散型ウェブのストレージを扱います。Develop SDKにより、アプリはprovenanceフォーマットを自前で構築することなく、撮影と検証を統合できます。

## なぜ重要か

Nostrの動画または画像clientにとって、ProofModeデータを運ぶことは、視聴者が、公開元のclientやrelayを信頼の拠り所とせずに、あるmediaが主張どおりに撮影され、それ以降ひそかに改変されていないかを確認する、外部的でクロスプラットフォームな手段を持つことを意味します。その違いが最も効いてくるのは、clipのダウンロードまたは再エンコードされたコピーの場合です。ダウンロードと、clientが適用する任意のwatermarkingを生き延びるprovenanceデータこそが、ファイルがそれを生成したアプリを離れた後も、その証明を検証可能なままにするものです。

## 実装

- [Divine](https://github.com/divinevideo/divine-mobile) - short-videoなNostr client。watermarkされたclipのダウンロードを通じてProofMode provenanceデータを運ぶ

---

**Primary sources:**
- [ProofMode](https://proofmode.org/)

**Mentioned in:**
- [Newsletter #17](/ja/newsletters/2026-04-29-newsletter/)
- [Newsletter #31: Divine Mobile 1.0.16 ships a deeper video editor, at-rest encryption, and ProofMode provenance](/ja/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**See also:**
- [Blossom](/ja/topics/blossom/)
