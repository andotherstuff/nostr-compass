---
title: "NIP-53: 라이브 액티비티"
date: 2026-04-15
translationOf: /en/topics/nip-53.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Live Streaming
---

NIP-53은 Nostr에서 라이브 스트리밍 메타데이터를 위한 표준 이벤트 형식을 정의합니다. 스트림은 kind `30311` addressable event로 공지되므로, 클라이언트는 이를 발견하고 현재 상태를 표시하며 채팅을 해당 스트림 맥락과 다시 연결할 수 있습니다.

## 작동 방식

각 스트림은 안정적인 식별자로 `d` 태그를 가진 kind `30311` 이벤트를 사용합니다. 이 이벤트에는 보통 제목과 요약 텍스트, 재생 URL을 담는 `streaming` 태그, 그리고 `status` 태그(`planned`, `live`, `ended`)가 들어갑니다. 이 이벤트는 addressable event이므로 같은 `d` 값에 대한 업데이트는 이전 메타데이터를 대체하며, 이벤트 흔적이 무한히 쌓이지 않습니다.

이벤트에는 주제 태그(`t`), 참가자 참조(`p`), 선택적인 참가자 수 필드도 포함될 수 있습니다. 라이브 채팅은 스트림을 `a` 태그로 참조하는 kind `1311` 이벤트로 전달되며, 이를 통해 채팅 메시지가 특정 라이브 액티비티 기록에 묶입니다.

## 구현체

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) - Nostr 네이티브 라이브 방송 주변의 메타데이터와 채팅 게시
- [Zap.stream](https://zap.stream/) - 스트림 탐색과 상호작용에 Nostr 이벤트 사용
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) - 인터넷 라디오 맥락에서 kind `1311` 라이브 채팅 이벤트 사용
- [Amethyst](https://github.com/vitorpamplona/amethyst)는 [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469)에서 [NIP-75](/ko/topics/nip-75/) zap goal을 Live Activities 화면에 연결했습니다. 각 라이브 스트림에 진행률 막대, 원탭 zap 버튼, 스트림의 kind `30311` 이벤트에 묶인 kind `9735` zap receipt로 계산한 top-zappers 리더보드가 표시됩니다. 이어지는 [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491)은 NIP-53 proof-of-agreement와 event builder를 추가했고, [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486)은 필터링과 탐색을 갖춘 전용 Live Streams 피드 화면을 출시했습니다.
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4)는 라이브 스트림 카드에서 원탭 zap을 추가했고, sats는 NIP-53을 통해 스트림 채팅 오버레이에 표시됩니다.

---

**주요 출처:**
- [NIP-53 명세](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - 라이브 스트림 goal 헤더와 top-zappers 리더보드
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - NIP-53 proof of agreement와 event builder

**언급된 뉴스레터:**
- [Newsletter #18: WaveFunc launch](/en/newsletters/2026-04-15-newsletter/)
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-29: 릴레이 기반 그룹](/ko/topics/nip-29/)
- [NIP-75: Zap Goals](/ko/topics/nip-75/)
- [NIP-57: Zaps](/ko/topics/nip-57/)
- [NIP-C7: 채팅 메시지](/ko/topics/nip-c7/)
