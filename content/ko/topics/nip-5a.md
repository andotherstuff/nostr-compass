---
title: "NIP-5A: 정적 웹사이트"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-01
draft: false
categories:
  - 프로토콜
  - 호스팅
---

NIP-5A는 Nostr 키페어 하에서 정적 웹사이트를 호스팅하는 방법을 정의합니다. 사이트 저자는 URL 경로를 SHA256 콘텐츠 해시에 매핑하는 서명된 매니페스트 이벤트를 게시하며, 호스트 서버는 해당 매니페스트를 해석하여 Blossom 스토리지에서 사이트 파일을 제공합니다.

## 작동 방식

이 사양은 두 가지 이벤트 kind를 사용합니다. Kind `15128`은 루트 사이트 매니페스트로, pubkey당 하나씩 해당 키의 기본 웹사이트 역할을 합니다. Kind `35128`은 `d` 태그로 식별되는 명명된 사이트 매니페스트로, 서브도메인처럼 작동합니다. 각 매니페스트는 절대 URL 경로를 제공할 파일의 SHA256 해시에 매핑하는 `path` 태그를 포함합니다.

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

호스트 서버는 HTTP 요청을 수신하고, 서브도메인에서 저자의 pubkey를 추출하며, 저자의 relay 목록에서 사이트 매니페스트를 가져온 다음, 요청된 경로를 콘텐츠 해시로 해석하고, `server` 태그에 나열된 Blossom 서버에서 일치하는 blob을 다운로드합니다.

## URL 해석

루트 사이트는 npub을 서브도메인으로 사용합니다. 명명된 사이트는 원시 pubkey의 50자 base36 인코딩 뒤에 `d` 태그 값을 하나의 DNS 레이블로 사용합니다. DNS 레이블이 63자로 제한되고 base36 pubkey가 항상 50자를 사용하므로, 명명된 사이트 식별자는 13자로 제한됩니다.

## 구현체

- [nsite](https://github.com/lez/nsite) - NIP-5A 매니페스트를 해석하고 파일을 제공하는 호스트 서버
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - 사이트 매니페스트 빌드 및 게시를 위한 UI

---

**주요 출처:**
- [NIP-5A 사양](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - 원본 제안 및 병합
- [nsite](https://github.com/lez/nsite) - 참조 호스트 구현
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - 게시 및 관리 UI

**언급된 곳:**
- [뉴스레터 #16: NIP-5A 병합](/ko/newsletters/2026-04-01-newsletter/#nip-5a-merges-bringing-static-websites-to-nostr)
- [뉴스레터 #16: NIP 심층 분석](/ko/newsletters/2026-04-01-newsletter/#nip-deep-dive-nip-5a-static-websites)

**같이 보기:**
- [Blossom](/ko/topics/blossom/)
- [NIP-65: Relay List Metadata](/ko/topics/nip-65/)
- [NIP-96: HTTP File Storage](/ko/topics/nip-96/)
