---
title: "Concord Protocol"
date: 2026-07-15
draft: false
translationOf: /en/topics/concord-protocol.md
translationDate: 2026-07-15
categories:
  - Protocol
  - Messaging
---

Concord는 Nostr 위에서 종단 간 암호화 커뮤니티와 채널을 위한 개방형 MIT 라이선스 프로토콜로, [CORD-01부터 CORD-07까지의 명세](https://github.com/concord-protocol/concord)로 정의됩니다. [Vector](https://github.com/VectorPrivacy/Vector)는 v0.4.0부터 그룹 채팅 기능의 기본 전송 방식으로 이를 채택하며 자체 릴리스 노트에서 "우리의 맞춤형 메시징 프로토콜"이라고 불렀지만, 명세 자체는 Vector와 별도로 공개되어 있고 이미 독립 구현들을 갖추고 있습니다.

## 작동 방식

Concord는 Discord 스타일의 커뮤니티 서버가 보통 하는 일을 아무도 신뢰할 필요가 없는 조각들로 나눕니다: relay는 회전하는 라벨로 주소가 지정된 암호화된 blob만 저장하고, 방의 키를 보유하는 것이 누군가를 구성원으로 만들며, 역할, 추방, 차단에 대한 권한은 서버가 집행하도록 신뢰하는 대신 모든 클라이언트가 로컬에서 검증하는 소유자 신원에 뿌리를 둔 서명된 명부입니다. 모든 지속 이벤트는 동일한 3계층 봉투를 탑니다: 평면 자체의 파생 스트림 키로 서명된 kind 1059 wrap이 저자의 실제 키로 서명된 seal을 담고, 그 seal은 기능 이벤트를 담은 서명되지 않은 rumor를 담습니다. 채팅 메시지 rumor는 평범한 kind 9 이벤트입니다:

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

제어, 채팅, 방명록 트래픽은 각각 자체 [NIP-59](/ko/topics/nip-59/) gift-wrap된 평면을 가지므로, 셋 모두를 보유한 relay라도 방 키 없이는 제어 메시지와 채팅 메시지, 방명록 항목을 구별할 수 없습니다. 명세는 일곱 개의 CORD 문서로 나뉩니다: 비공개 스트림(01), 커뮤니티와 멤버십(02), 채널(03), 역할(04), 초대(05), 제거된 구성원의 접근을 끊기 위한 재키잉과 재설립(06), 그리고 블라인드 토큰 브로커를 통한 오디오/비디오(07). 멤버십 자체에는 서버 측 목록이 없습니다: 평면을 복호화할 수 있는 자가 구성원이며, 누군가를 진짜로 제거한다는 것은 테이블에서 행을 삭제하는 대신 커뮤니티를 새 키 에포크로 굴려 남은 사람에게만 넘겨준다는 뜻입니다.

## Marmot과의 차이점

Concord와 [Marmot](/ko/topics/marmot/)은 서로 다른 그룹 형태를 위한 서로 다른 암호화로 Nostr 상의 암호화 그룹 메시징을 해결하며, Concord 프로젝트 자체의 비교는 그 분기점을 명확히 밝힙니다: Marmot은 순방향 비밀성과 침해 후 보안을 위해 Nostr 위에 [MLS](/ko/topics/mls/)를 얹으며, 기기별 키 패키지와 전체 그룹을 일사불란하게 전진시키는 순서 있는 커밋을 사용합니다. 그것은 강력한 보장을 얻는 대신 멤버십 변경에 따라 커지는 비용을 치르며, 가입과 탈퇴가 드문 작고 위험도 높은 그룹에 잘 맞습니다. Concord는 대신 모든 구성원에게 동일한 방 키를 주고 커밋마다 래칫하는 대신 제거 시 방 전체를 재키잉하여, MLS의 암호화 보장 일부를 내주는 대가로 커뮤니티가 수백 또는 수천 명의 캐주얼하고 이탈이 잦은 구성원으로 성장해도 저렴하게 유지되는 모델을 얻는데, 이것이 Discord 스타일 커뮤니티가 실제로 취하는 형태입니다.

## Vector가 전환한 이유

Vector 자체 [v0.4.0 릴리스 노트](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)는 Concord를 그룹 채팅을 위한 "우리의 맞춤형 메시징 프로토콜"이라고만 설명하며 그 이유를 직접 밝히지는 않습니다. 그럼에도 Concord 자체 공개 근거와의 부합은 분명합니다: Vector 같은 클라이언트의 그룹 채팅은 정확히 크고 개방적이며 멤버십이 자주 바뀌는 경우로, Marmot의 기기별 MLS 상태가 더 비싼 경로가 되는 지점이며, Concord의 비동기적이고 언제든 접을 수 있는 설계는 바로 그 경우를 위해 만들어졌습니다. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)는 그룹 채팅에서 Marmot을 은퇴시키고 Concord를 채택했으며, 기존 Marmot 그룹 기록은 전환 과정에서 이전되지 않았습니다. [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)은 4일 뒤 프라이버시 및 안정성 개선과 함께 "Concord v2"를 출시했습니다. 같은 주에 [Amethyst가 자체 클린룸 방식의 와이어 호환 Concord 구현을 병합했으며](https://github.com/vitorpamplona/amethyst/pull/3566), Soapbox의 Discord 스타일 클라이언트 [Armada](https://gitlab.com/soapbox-pub/armada)는 이미 참조 구현으로서 같은 명세 위에 Communities 기능을 구축하고 있습니다. 세 개의 독립 클라이언트가 며칠 사이에 하나의 개방형 명세로 수렴하는 것은 실제 클라이언트 간 상호 운용으로 가는 빠른 경로이며, 나머지 Nostr 그룹 채팅 클라이언트 중 얼마나 많은 수가 대신 Marmot에 머무는지와 대비해 추적할 가치가 있습니다.

## 구현

- [Vector](https://github.com/VectorPrivacy/Vector) - 단일 바이너리, 프라이버시 우선 Nostr 메신저; 첫 Concord 출시 클라이언트, v0.4.0에서
- [Armada](https://gitlab.com/soapbox-pub/armada) (Soapbox) - Discord 스타일 커뮤니티 클라이언트; 참조 구현, 백엔드는 별도의 `armada-relay` 저장소에
- [Amethyst](https://github.com/vitorpamplona/amethyst) - 기능이 풍부한 Android 및 멀티플랫폼 Nostr 클라이언트; Armada와 와이어 호환되는 클린룸 재구현 ([PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566))

---

**주요 출처:**
- [Concord 프로토콜 명세 (CORD-01부터 CORD-07)](https://github.com/concord-protocol/concord)
- [Vector v0.4.0 릴리스 노트](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Vector v0.4.1 릴리스 노트](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [Amethyst PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)

**언급된 곳:**
- [Newsletter #31: Vector v0.4.0가 그룹 채팅을 Marmot에서 Concord로 옮기고, 며칠 뒤 Amethyst가 자체 Concord 클라이언트를 출시하다](/ko/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31: Amethyst가 종단 간 암호화 커뮤니티를 위한 클린룸 Concord 구현을 출시하다](/ko/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**함께 보기:**
- [Marmot Protocol](/ko/topics/marmot/)
- [MLS (Message Layer Security)](/ko/topics/mls/)
- [NIP-46: Nostr Connect](/ko/topics/nip-46/)
