---
title: "NIP-84: Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-03-07
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 definieert kind 9802-"highlight"-events waarmee gebruikers passages kunnen markeren en delen die ze waardevol vinden uit long-form content op Nostr.

## Hoe het werkt

Het `.content`-veld bevat de gemarkeerde tekst. Events verwijzen naar hun bronmateriaal met `a`- of `e`-tags voor Nostr-native content, of `r`-tags voor externe URL's (clients moeten trackingparameters verwijderen). Optionele `p`-tags schrijven de oorspronkelijke auteurs toe, en een optionele `context`-tag geeft omringende tekst wanneer de highlight deel uitmaakt van een grotere passage.

Voor niet-tekstuele media kan de highlight-content leeg zijn. Dat geeft clients een manier om naar een audio- of videohighlight te verwijzen terwijl de bronverwijzing in tags blijft staan.

## Citaathighlights

Gebruikers kunnen een `comment`-tag toevoegen om citaathighlights te maken, die renderen als quoted reposts. Dit voorkomt dubbele vermeldingen in microbloggingclients. Binnen comments vereisen `p`-tagvermeldingen een "mention"-attribuut om ze te onderscheiden van auteur- of redacteurtoeschrijvingen, en `r`-tag-URL's gebruiken een "source"-attribuut voor bronverwijzingen.

## Waarom het belangrijk is

NIP-84 scheidt de gemarkeerde passage van de omringende discussie. Een client kan de geselecteerde tekst als primair object renderen en commentaar vervolgens behandelen als optionele metadata, in plaats van beide te vermengen in een gewone note.

Dat is nuttig voor lees- en onderzoekstools omdat het het exacte fragment bewaart. Twee lezers kunnen commentaar geven op hetzelfde artikel en toch portable highlight-events maken die andere clients begrijpen.

## Interop-opmerkingen

Attributietags zijn belangrijker dan ze lijken. Een `p`-tag met een rol als `author` of `editor` vertelt clients wie het bronmateriaal heeft gemaakt, terwijl een `mention`-rol binnen een quote comment iets anders betekent. Als clients die gevallen op één hoop gooien, kunnen ze de gemarkeerde bron verkeerd labelen of onterecht meldingen naar mensen sturen.

---

**Primaire bronnen:**
- [NIP-84 Specification](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Vermeld in:**
- [Nieuwsbrief #10: Releases](/en/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**Zie ook:**
- [NIP-94: File Metadata](/nl/topics/nip-94/)
