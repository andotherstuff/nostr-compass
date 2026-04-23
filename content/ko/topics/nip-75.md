---
title: "NIP-75: Zap Goals"
date: 2026-04-22
translationOf: /en/topics/nip-75.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75는 사용자가 zap을 보낼 수 있는 fundraising goal 이벤트를 정의합니다. goal은 millisatoshis 단위의 목표 금액과, 해당 goal에 대한 zap receipt를 집계할 릴레이 목록을 선언합니다. goal 이벤트를 참조하는 어떤 [NIP-57](/ko/topics/nip-57/) zap이든 진행률 계산에 포함됩니다.

## 작동 방식

zap goal은 `kind:9041` 이벤트입니다. `.content`에는 사람이 읽을 수 있는 설명이 들어갑니다. 필수 태그는 `amount`(millisats 목표치)와 `relays`(zap receipt를 집계할 릴레이 목록)입니다. 선택 태그로는 집계를 특정 시각 이후 중단하는 `closed_at`, `image`, `summary`가 있습니다. goal은 외부 URL이나 addressable event를 가리키는 `r` 또는 `a` 태그를 포함할 수 있고, NIP-57 부록 G에서 가져온 zap-split 태그를 통해 여러 beneficiary pubkey도 담을 수 있습니다.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1776500000,
  "kind": 9041,
  "tags": [
    ["relays", "wss://alicerelay.example.com", "wss://bobrelay.example.com"],
    ["amount", "210000"],
    ["image", "<image url>"],
    ["summary", "Nostrasia travel expenses"]
  ],
  "content": "Nostrasia travel expenses",
  "sig": "<128-char hex>"
}
```

클라이언트는 zap 요청 안에 goal 이벤트를 가리키는 `e` 태그를 넣어 goal에 zap을 연결합니다. goal 진행률은 goal이 지정한 릴레이들에서 해당 goal과 일치하는 zap receipt 금액을 합산한 값입니다. `closed_at`이 설정되어 있으면 그 시각 이후에 게시된 zap receipt는 집계되지 않습니다.

## 구현체

- [Amethyst](https://github.com/vitorpamplona/amethyst)는 [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469)에서 [NIP-53](/ko/topics/nip-53/) Live Activities 화면 안에 goal progress bar와 원탭 zap 버튼을 렌더링합니다.

---

**주요 출처:**
- [NIP-75 명세](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469: live stream top zappers and goal header](https://github.com/vitorpamplona/amethyst/pull/2469)

**언급된 뉴스레터:**
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive on NIP-57](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-57: Zaps](/ko/topics/nip-57/)
- [NIP-53: 라이브 액티비티](/ko/topics/nip-53/)
