---
title: "NIP-38: Gebruikersstatussen"
date: 2026-08-26
translationOf: /en/topics/nip-38.md
translationDate: 2026-08-26
draft: false
description: "Definieert kortlevende gebruikersstatus-events, inclusief de categorieën voor algemene en muziekstatus."
---

NIP-38 definieert adresseerbare kind 30315-events voor korte gebruikersstatussen. Een `d`-tag identificeert de statuscategorie, zoals `general` of `music`, terwijl optionele `r`- en `p`-tags naar een URL kunnen verwijzen of een artiest kunnen identificeren. Clients kunnen de `expiration`-tag van het event gebruiken om verouderde statussen niet langer te tonen.

## Hoe het werkt

Een gebruiker publiceert een kind 30315-event met de statustekst in `content`. Het event is adresseerbaar op pubkey, kind en `d`-tag, dus een nieuwer event in dezelfde categorie vervangt het oudere. Een leeg contentveld wist die status.

---

**Primaire bronnen:**
- [NIP-38-specificatie](https://github.com/nostr-protocol/nips/blob/master/38.md) - Gebruikersstatussen

**Vermeld in:**
- [Newsletter #37: NoorNote v1.3.6: profielstatussen en advertenties](/nl/newsletters/2026-08-26-newsletter/#noornote-v136-profielstatussen-en-advertenties)
