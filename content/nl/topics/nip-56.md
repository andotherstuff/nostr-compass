---
title: "NIP-56: Rapportage"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 definieert een rapportagemechanisme via kind 1984-events, waarmee gebruikers en applicaties aanstootgevende inhoud kunnen markeren in het Nostr-netwerk.

## Hoe het werkt

Een gebruiker publiceert een kind 1984-event met een `p`-tag die verwijst naar de pubkey die wordt gerapporteerd. Bij het rapporteren van een specifieke notitie verwijst een `e`-tag naar het notitie-ID. Beide tags accepteren een derde parameter die de schendingscategorie specificeert.

## Rapportagecategorieën

- **nudity**: inhoud voor volwassenen
- **malware**: virussen, trojans, ransomware
- **profanity**: aanstootgevend taalgebruik en haatzaaien
- **illegal**: inhoud die mogelijk wetten schendt
- **spam**: ongewenste herhaalde berichten
- **impersonation**: frauduleuze identiteitsclaims
- **other**: schendingen die niet in bovenstaande categorieën passen

## Gedrag van clients en relays

Clients kunnen rapporten van gevolgde gebruikers gebruiken voor moderatiebeslissingen, zoals het vervagen van inhoud wanneer meerdere vertrouwde contacten die markeren. Relays moeten automatische moderatie via rapporten vermijden vanwege het risico op misbruik; rapporten van vertrouwde moderatoren kunnen handhaviging ondersteunen. Aanvullende classificatie wordt ondersteund via NIP-32 `l`- en `L`-tags.

---

**Primaire bronnen:**
- [NIP-56-specificatie](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Vermeld in:**
- [Nieuwsbrief #10: Projectupdates](/nl/newsletters/2026-02-18-newsletter/#notedeck-voorbereiding-voor-android-app-store)

**Zie ook:**
- [NIP-22: Commentaar](/nl/topics/nip-22/)
