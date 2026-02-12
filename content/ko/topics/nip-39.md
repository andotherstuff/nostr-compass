---
title: "NIP-39: 프로필의 외부 신원"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39는 사용자가 `i` tag를 사용하여 Nostr 프로필에 외부 신원 주장을 첨부하는 방법을 정의합니다. 이 tag는 Nostr pubkey를 GitHub, Twitter, DNS 도메인 등 외부 플랫폼의 계정과 연결합니다.

## 작동 방식

사용자는 신원 주장을 `i` tag로 게시합니다. 각 tag에는 플랫폼 식별자와 외부 계정이 Nostr pubkey로 다시 연결되는 증명 URL이 포함되어 양방향 검증을 수립합니다:

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

클라이언트는 증명 URL을 가져와 사용자의 Nostr pubkey가 포함되어 있는지 확인하여 주장을 검증합니다. 이를 통해 중앙화된 검증 서비스 없이 신원 연결의 웹을 생성합니다.

## 최근 변경 사항

2026년 2월 기준, [PR #2216](https://github.com/nostr-protocol/nips/pull/2216)이 신원 tag를 kind 0(사용자 메타데이터) event에서 전용 kind 10011로 추출했습니다. 이 이동은 vitorpamplona의 kind 0 슬리밍 캠페인의 일부로, 낮은 채택률이 동기가 되었습니다: `i` tag 검증을 구현한 클라이언트가 거의 없었지만 모든 kind 0 가져오기에서 오버헤드가 발생했습니다. 새로운 kind 10011은 관심 있는 클라이언트가 신원 주장을 별도로 가져올 수 있게 합니다.

---

**주요 출처:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**언급된 곳:**
- [뉴스레터 #9: NIP 업데이트](/ko/newsletters/2026-02-11-newsletter/#nip-업데이트)

**참고:**
- [NIP-05: DNS 기반 검증](/ko/topics/nip-05/)
