---
title: "NIP-51: Lijsten"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Sociaal
---

NIP-51 definieert verschillende lijsttypes voor het organiseren van referenties naar events, gebruikers en content in Nostr.

## Lijstkinds

- **Kind 10000**: Mute-lijst (gebruikers, threads of woorden om te verbergen)
- **Kind 10001**: Pin-lijst (events om op profiel uit te lichten)
- **Kind 30000**: Volgsets (gecategoriseerde volglijsten)
- **Kind 30003**: Bladwijzersets
- **Kind 30004**: Curatiesets (artikelen)
- **Kind 30005**: Videosets
- **Kind 30006**: Fotosets
- **Kind 30015**: Interessesets (hashtags)
- **Kind 30030**: Emojisets

## Structuur

Lijsten gebruiken tags om naar content te verwijzen:
- `p` tags voor pubkeys
- `e` tags voor events
- `a` tags voor adresseerbare events
- `t` tags voor hashtags
- `word` tags voor gemute woorden

## Openbaar vs Privé

Lijsten kunnen openbare tags hebben (zichtbaar voor iedereen) en versleutelde content (privé). Privé-items worden versleuteld met NIP-44 en opgeslagen in het `content` veld van het event. De encryptie gebruikt de eigen sleutels van de auteur (versleutelen naar jezelf).

Dit maakt functies mogelijk zoals openbare bladwijzers met privénotities, of een mute-lijst waarbij gemute items verborgen zijn voor anderen.

## Recente Wijzigingen

- Hashtag en URL tags verwijderd uit generieke bladwijzers; hashtags gebruiken nu kind 30015
- Kind 30006 toegevoegd voor gecureerde fotosets

---

**Primaire bronnen:**
- [NIP-51 Specificatie](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)
- [Nieuwsbrief #2: NIP Updates](/nl/newsletters/2025-12-24-newsletter/#nip-updates)

**Zie ook:**
- [NIP-02: Volglijst](/nl/topics/nip-02/)
