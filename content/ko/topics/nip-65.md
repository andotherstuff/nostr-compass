---
title: "NIP-65: Relay List Metadata"
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65는 사용자가 읽기 및 쓰기에 선호하는 relay를 광고하는 kind 10002 event를 정의합니다. 이 메타데이터는 다른 사용자와 클라이언트가 분산된 relay 네트워크에서 귀하의 콘텐츠를 찾는 데 도움이 되며, 부하를 분산하고 검열 저항성을 향상시키는 "outbox 모델"을 가능하게 합니다.

## 구조

relay 목록은 사용자가 광고하려는 각 relay에 대한 `r` 태그를 포함하는 교체 가능한 event(kind 10002)입니다. 이 event는 동일한 pubkey의 이전 relay 목록을 대체합니다.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

각 `r` 태그는 relay WebSocket URL과 사용자가 해당 relay와 어떻게 상호 작용하는지를 나타내는 선택적 마커를 포함합니다. `read` 마커는 사용자가 이 relay에서 event를 소비한다는 것을 의미하므로, 다른 사람들은 사용자에게 도달하기 위해 거기에 게시해야 합니다. `write` 마커는 사용자가 이 relay에 게시한다는 것을 의미하므로, 다른 사람들은 사용자의 콘텐츠를 보기 위해 거기에서 구독해야 합니다. 마커를 생략하면 읽기와 쓰기 모두를 나타냅니다.

relay 목록 event의 `content` 필드는 비어 있습니다.

## Outbox 모델

NIP-65는 "outbox 모델"이라고 불리는 탈중앙화된 콘텐츠 배포 패턴을 가능하게 합니다. 모든 사람이 동일한 중앙 relay에 게시하고 읽는 대신, 사용자는 자신이 선호하는 relay에 게시하고 클라이언트는 각 사용자의 콘텐츠를 어디서 찾을 수 있는지 동적으로 발견합니다.

Alice가 Bob의 게시물을 찾으려면, 그녀의 클라이언트는 먼저 어떤 relay에서든 Bob의 kind 10002 event를 가져옵니다. 그런 다음 Bob이 게시하는 곳이므로 `write`로 표시된 relay를 추출합니다. 그녀의 클라이언트는 Bob의 event를 위해 해당 relay에서 구독합니다. Alice가 Bob에게 다이렉트 메시지를 보내려면, 그녀의 클라이언트는 대신 그의 `read` relay를 찾아 거기에 메시지를 게시합니다.

outbox 모델을 따르는 클라이언트는 팔로우하는 사용자의 NIP-65 event에 나열된 relay에 대한 연결을 유지합니다. 새로운 계정을 발견하면 동적으로 새 relay에 연결합니다. 여러 팔로우하는 사용자의 목록에 나타나는 relay는 연결하면 사용자의 소셜 그래프를 더 많이 제공하므로 우선순위가 높아집니다.

이 아키텍처는 단일 relay가 모든 사람의 콘텐츠를 저장하거나 제공할 필요가 없기 때문에 검열 저항성을 향상시킵니다. 하나의 relay가 오프라인이 되거나 사용자를 차단해도 콘텐츠는 나열된 다른 relay에서 계속 사용할 수 있습니다.

## Relay 힌트와의 관계

NIP-65는 다른 NIP 전반에서 발견되는 relay 힌트를 보완합니다. `["p", "pubkey", "wss://hint.relay"]`로 누군가를 태그하면, 힌트는 클라이언트에게 해당 특정 참조를 어디서 찾아야 하는지 알려줍니다. NIP-65는 권위 있는 사용자 제어 선호 relay 목록을 제공하고, 힌트는 더 빠른 발견을 위해 개별 event에 포함된 바로가기를 제공합니다.

## 모범 사례

오래된 항목이 더 이상 작동하지 않는 relay를 가리키면 당신을 찾기 어려워지므로 relay 목록을 최신 상태로 유지하세요. 중복성을 위해 최소 2~3개의 relay를 포함하여 하나의 relay가 오프라인이 되어도 콘텐츠가 다른 relay를 통해 계속 접근 가능하도록 하세요.

너무 많은 relay를 나열하는 것은 피하세요. 10개 또는 15개의 relay를 나열하면 귀하의 콘텐츠를 가져오려는 모든 클라이언트가 모든 relay에 연결해야 하므로 경험이 느려지고 네트워크 전반의 부하가 증가합니다. 잘 선택된 3~5개의 relay로 구성된 집중된 목록이 모든 사람에게 부담을 주는 완전한 목록보다 더 나은 서비스를 제공합니다.

범용 relay와 사용하는 전문 relay를 혼합하세요. 예를 들어 `wss://relay.damus.io`와 같은 인기 있는 범용 relay, 지리적 지역에 초점을 맞춘 relay, 그리고 참여하는 특정 커뮤니티를 위한 relay를 나열할 수 있습니다.

---

**주요 출처:**
- [NIP-65 사양](https://github.com/nostr-protocol/nips/blob/master/65.md)

**언급된 곳:**
- [Newsletter #5: NIP 심층 분석](/ko/newsletters/2026-01-13-newsletter/#nip-65-relay-list-metadata)

**참고:**
- [NIP-11: Relay 정보](/ko/topics/nip-11/)
