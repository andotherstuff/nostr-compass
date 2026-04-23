---
title: "NIP-5A: 정적 웹사이트"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Hosting
---

NIP-5A는 Nostr 키페어 아래에서 정적 웹사이트를 호스팅하는 방법을 정의합니다. 사이트 작성자는 URL 경로를 SHA256 콘텐츠 해시에 매핑하는 서명된 manifest 이벤트를 게시하고, 호스트 서버는 그 manifest를 해석해 Blossom storage에서 사이트 파일을 제공합니다.

## 작동 방식

이 명세는 두 가지 이벤트 kind를 사용합니다. Kind `15128`은 루트 사이트 manifest이며 pubkey당 하나만 존재하고 해당 키의 기본 웹사이트 역할을 합니다. Kind `35128`은 `d` 태그로 식별되는 named site manifest이며 서브도메인처럼 동작합니다. 각 manifest는 절대 URL 경로를 제공해야 할 파일의 SHA256 해시와 매핑하는 `path` 태그를 포함합니다.

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

호스트 서버는 HTTP 요청을 받고, 서브도메인에서 작성자의 pubkey를 추출하고, 작성자의 relay 목록에서 사이트 manifest를 가져오며, 요청된 경로를 콘텐츠 해시로 해석한 뒤, `server` 태그에 나열된 Blossom 서버에서 일치하는 blob을 내려받습니다.

## URL 해석

루트 사이트는 npub을 서브도메인으로 사용합니다. named site는 raw pubkey의 50자 base36 인코딩 뒤에 `d` 태그 값을 붙여 하나의 DNS label로 사용합니다. DNS label은 63자 제한이 있고 base36 pubkey가 항상 50자를 쓰므로, named site 식별자는 13자로 제한됩니다.

## 구현체

- [nsite](https://github.com/lez/nsite) - NIP-5A manifest를 해석하고 파일을 제공하는 호스트 서버
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - 사이트 manifest를 만들고 게시하는 UI

---

**주요 출처:**
- [NIP-5A Specification](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - 원래 제안과 병합
- [nsite](https://github.com/lez/nsite) - 참조 호스트 구현
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - 게시 및 관리 UI

**언급된 뉴스레터:**
- [Newsletter #16: NIP-5A merges](/ko/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/ko/newsletters/2026-04-01-newsletter/)
- [Newsletter #19: NIP-5D applets proposal](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [Blossom](/ko/topics/blossom/)
- [NIP-65: 릴레이 목록 메타데이터](/ko/topics/nip-65/)
- [NIP-96: HTTP File Storage](/ko/topics/nip-96/)
