---
title: "NIP-5A: Static Websites"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Hosting
---

NIP-5Aは、Nostr keypair配下でstatic websiteをホストする方法を定義します。site authorは、URL pathをSHA256 content hashへ対応付ける署名済みmanifest eventを公開し、host serverはそのmanifestを解決してBlossom storageからsiteファイルを配信します。

## 仕組み

仕様は2つのevent kindを使います。Kind `15128`はroot site manifestで、pubkeyごとに1つ、その鍵のデフォルトwebsiteになります。Kind `35128`は`d`タグで識別されるnamed site manifestで、subdomainのように振る舞います。各manifestには、絶対URL pathを配信対象ファイルのSHA256 hashへ対応付ける`path`タグが入ります。

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

host serverはHTTP requestを受け取ると、subdomainからauthorのpubkeyを取り出し、そのauthorのrelay listからsite manifestを取得し、要求pathをcontent hashへ解決し、`server`タグに列挙されたBlossom serverから対応blobをダウンロードします。

## URL解決

root siteはnpubをsubdomainとして使います。named siteは、生pubkeyの50文字base36エンコードに`d`タグ値を続けた1つのDNS labelを使います。DNS labelは63文字までで、base36 pubkeyは常に50文字なので、named site identifierは13文字までに制限されます。

## Implementations

- [nsite](https://github.com/lez/nsite) - NIP-5A manifestを解決してファイルを配信するhost server
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - site manifestを構築し公開するUI

---

**Primary sources:**
- [NIP-5A Specification](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - Original proposal and merge
- [nsite](https://github.com/lez/nsite) - Reference host implementation
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - Publishing and management UI

**Mentioned in:**
- [Newsletter #16: NIP-5A merges](/ja/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/ja/newsletters/2026-04-01-newsletter/)
- [Newsletter #19: NIP-5D applets proposal](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [Blossom](/ja/topics/blossom/)
- [NIP-65: Relay List Metadata](/ja/topics/nip-65/)
- [NIP-96: HTTP File Storage](/ja/topics/nip-96/)
