---
title: "NIP-5C: Scrolls (WASM Programs)"
date: 2026-04-08
translationOf: /en/topics/nip-5c.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Applications
---

NIP-5C（旧称NIP-A5）は、Nostr上でWebAssemblyプログラム（"scrolls"）を公開し、発見し、実行するための慣例を定義します。WASM binariesはNostr eventsとして保存され、どのclientでもそれを取得してsandboxed runtimeで実行できます。

## 仕組み

開発者は、コンパイル済みbinaryを含むNostr eventsとしてWASMプログラムを公開します。clientは標準のNostr queryを通じてこれらのプログラムを発見し、イベントからWASM binaryをダウンロードし、sandboxedなWebAssembly runtimeで実行します。このsandboxにより、scrollsがhost systemへ直接アクセスすることは防がれ、runtimeが明示的に提供したcapabilityだけに制限されます。

## ユースケース

- **Portable compute**: WASM実行に対応した任意のclientでプログラムを動かす
- **分散アプリ配布**: app storeなしでアプリケーションを公開し、発見する
- **Composable tools**: scrollsをつなげて複雑なworkflowを構成する

## Demo

[demo app](https://nprogram.netlify.app/)では、scrollsがブラウザ内で動作する様子と、Nostr eventsとして公開されたexample programsを確認できます。

---

**Primary sources:**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - Scrolls (WASM Programs) proposal

**Mentioned in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)
- [Newsletter #19: NIP-5D applets proposal](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-5D（Web Applets）](/ja/topics/nip-5d/)
- [NIP-5A（Static Websites）](/ja/topics/nip-5a/)
