---
title: "NIP-36: Sensible Inhalte"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-36.md
translationDate: 2026-10-15
---

NIP-36 definiert ein optionales `content-warning`-tag mit einer optionalen Begründung. Clients können es verwenden, um ein event auszublenden, bis der Leser es einblendet. Das event bleibt öffentlich.

## Implementierungen

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) liest das tag und seine Begründung aus. [Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) berücksichtigt die Einstellung des Lesers für sensible Inhalte und bietet eine Aktion zum Einblenden an. [noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) prüft die Warnungseinstellungen und den Aufklappzustand, bevor die Warnung angezeigt wird.

---

**Primärquellen:**
- [NIP-36-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/36.md)

**Erwähnt in:**
- [Newsletter #44: Inhaltswarnungen vor der Anzeige](/de/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**Siehe auch:**
- [NIP-32: Kennzeichnung](/de/topics/nip-32/)
