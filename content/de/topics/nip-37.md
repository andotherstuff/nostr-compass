---
title: "NIP-37: Entwurfs-Wraps"
date: 2026-07-01
draft: false
translationOf: /en/topics/nip-37.md
translationDate: 2026-07-01
categories:
  - NIP
  - Drafts
  - Privacy
---

NIP-37 definiert ein verschlüsseltes Speicher-event für unsignierte Entwurfs-events beliebiger Art. Ein Nutzer, der einen Langform-Artikel verfasst, ein bevorstehendes Kalender-event erstellt oder eine Nachricht schreibt, die er später senden möchte, kann den Entwurf auf relays unter einem kind `31234`-event speichern, verschlüsselt mit seinem eigenen Schlüssel über [NIP-44](/de/topics/nip-44/). Der Entwurf ist von jedem Client wiederherstellbar, der den Schlüssel des Nutzers besitzt, und dasselbe NIP definiert ein separates `kind:10013`-Listen-event, das die relays benennt, auf denen der Nutzer seine privaten Entwürfe speichern möchte.

## Wie es funktioniert

Ein Entwurfs-Wrap ist ein parametrisiertes ersetzbares event der Art `31234`. Das unsignierte Entwurfs-event wird als JSON serialisiert, mit NIP-44 auf den eigenen öffentlichen Schlüssel des Signierers verschlüsselt und in `.content` platziert. Ein `k`-tag deklariert die Art des Entwurfs, damit ein Client Entwürfe nach event-Typ gruppieren kann. Ein `d`-tag trägt den Entwurfsbezeichner, sodass der Wrap ersetzt werden kann, während sich der Entwurf entwickelt, und ein NIP-40-`expiration`-tag wird empfohlen, damit alte Entwürfe automatisch ablaufen.

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

Ein leeres `.content`-Feld signalisiert, dass der Entwurf gelöscht wurde.

## Checkpoints

Kind `1234` definiert Checkpoints, die zu einem übergeordneten `kind:31234`-event gehören. Checkpoints tragen einen `a`-tag, der zurück auf den übergeordneten Entwurf verweist, und ermöglichen es einem Client, den Revisionsverlauf neben dem neuesten Entwurf zu speichern.

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## Relay-Liste für private Inhalte (kind 10013)

Kind `10013` ist ein ersetzbares event, dessen tags die relays auflisten, auf denen der Nutzer private Inhalte speichern möchte, einschließlich Entwurfs-Wraps. Clients, die kind `31234` veröffentlichen, SOLLTEN auf relays veröffentlichen, die im kind `10013`-event des Nutzers aufgeführt sind. Dies trennt die für öffentliche Beiträge verwendete relay-Menge (NIP-65) von der für die private Inhaltsspeicherung verwendeten relay-Menge, sodass ein Nutzer private Entwürfe an eine kleine Menge vertrauenswürdiger relays binden kann, ohne diese Menge in seiner öffentlichen Outbox offenzulegen.

## Implementierungen

- [Notedeck](https://github.com/damus-io/notedeck) - speichert private Sync-relays als kind-10013-Liste (hinzugefügt 2026-06)

---

**Primärquellen:**
- [NIP-37-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Notedeck-commit, der private Sync-relays als kind-10013 speichert](https://github.com/damus-io/notedeck) - Das Damus-Team übernimmt die Spezifikation für die Verwaltung der Desktop-Sync-relays

**Erwähnt in:**
- [Newsletter #29: Notedeck](/de/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**Siehe auch:**
- [NIP-44: Versionierte Verschlüsselung](/de/topics/nip-44/)
- [NIP-65: Relay-Listen-Metadaten](/de/topics/nip-65/)
