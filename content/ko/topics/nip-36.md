---
title: "NIP-36: 민감한 콘텐츠"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-36.md
translationDate: 2026-10-15
---

NIP-36은 사유를 선택적으로 포함할 수 있는 선택적 `content-warning` tag를 정의합니다. 클라이언트는 이를 사용해 독자가 표시를 선택할 때까지 event를 숨길 수 있습니다. event는 여전히 공개 상태로 유지됩니다.

## 구현

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt)는 tag와 그 사유를 파싱합니다. [Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte)은 독자의 민감한 콘텐츠 설정을 사용하며, 콘텐츠를 표시하는 동작을 제공합니다. [noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx)은 경고를 표시하기 전에 경고 환경설정과 펼침 상태를 확인합니다.

---

**1차 출처:**
- [NIP-36 명세](https://github.com/nostr-protocol/nips/blob/master/36.md)

**언급된 곳:**
- [뉴스레터 #44: 표시 전 콘텐츠 경고](/ko/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**함께 보기:**
- [NIP-32: 라벨링](/ko/topics/nip-32/)
