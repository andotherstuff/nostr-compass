---
title: "NIP-38: Nutzerstatus"
date: 2026-08-26
translationOf: /en/topics/nip-38.md
translationDate: 2026-08-26
draft: false
description: "Definiert kurzlebige Nutzerstatus-Events, einschließlich der Kategorien für allgemeinen und Musik-Status."
---

NIP-38 definiert adressierbare Kind-30315-Events für kurze Nutzerstatus. Ein `d`-Tag benennt die Statuskategorie, etwa `general` oder `music`, während optionale `r`- und `p`-Tags auf eine URL verweisen oder einen Künstler identifizieren können. Clients können den `expiration`-Tag des Events nutzen, um veraltete Status nicht mehr anzuzeigen.

## Wie es funktioniert

Ein Nutzer veröffentlicht ein Kind-30315-Event mit dem Statustext in `content`. Das Event ist über Pubkey, Kind und `d`-Tag adressierbar, sodass ein neueres Event derselben Kategorie das ältere ersetzt. Ein leeres Content-Feld löscht diesen Status.

---

**Primärquellen:**
- [NIP-38-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/38.md) - Nutzerstatus

**Erwähnt in:**
- [Newsletter #37: NoorNote v1.3.6: Profilstatus und Kleinanzeigen](/de/newsletters/2026-08-26-newsletter/#noornote-v136-profilstatus-und-kleinanzeigen)
