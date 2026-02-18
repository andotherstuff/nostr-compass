---
title: "NIP-84: Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-02-18
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 definieert kind 9802-"highlight"-events waarmee gebruikers passages kunnen markeren en delen die ze waardevol vinden uit lange-vorm inhoud op Nostr.

## Hoe het werkt

Het `.content`-veld bevat de gemarkeerde tekst. Events refereren hun bronmateriaal via `a`- of `e`-tags voor Nostr-native inhoud, of `r`-tags voor externe URL's (clients dienen trackingparameters te verwijderen). Optionele `p`-tags schrijven de originele auteurs toe, en een optionele `context`-tag biedt omringende tekst wanneer de highlight een deel is van een grotere passage.

## Citaathighlights

Gebruikers kunnen een `comment`-tag toevoegen om citaathighlights te maken, die worden weergegeven als geciteerde reposts. Dit voorkomt dubbele vermeldingen in microbloggingclients. In commentaren vereisen `p`-tagvermeldingen een "mention"-attribuut om ze te onderscheiden van auteur/redacteur-attributies, en `r`-tag-URL's gebruiken een "source"-attribuut voor bronreferenties.

---

**Primaire bronnen:**
- [NIP-84-specificatie](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Vermeld in:**
- [Nieuwsbrief #10: Releases](/nl/newsletters/2026-02-18-newsletter/#prism-deel-alles-naar-nostr-vanuit-android)

**Zie ook:**
- [NIP-94: Bestandsmetadata](/nl/topics/nip-94/)
