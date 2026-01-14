---
title: "NIP-71: Video Events"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 definieert event kinds voor videocontent op Nostr, wat het delen van video's met goede metadata-ondersteuning mogelijk maakt. De specificatie behandelt zowel reguliere video events als adresseerbare video events, waarbij de laatste in januari 2026 werden toegevoegd om creators in staat te stellen videometadata bij te werken zonder opnieuw te publiceren.

## Event Kinds

NIP-71 definieert vier event kinds verdeeld in twee categorieën gebaseerd op beeldverhouding en adresseerbaarheid.

Reguliere video-events gebruiken kind 21 voor horizontale (landschap) video's en kind 22 voor verticale (portret/shorts) video's. Dit zijn standaard Nostr-events met onveranderlijke content na publicatie.

Adresseerbare video-events gebruiken kind 34235 voor horizontale video's en kind 34236 voor verticale video's. Dit zijn geparametriseerd vervangbare events geidentificeerd door de combinatie van pubkey, kind, en `d`-tag. Het publiceren van een nieuw event met dezelfde identificatoren vervangt de vorige versie, wat metadata-updates mogelijk maakt.

## Structuur

Een volledig adresseerbaar video-event bevat identificatievelden, metadatatags, en de videocontentreferentie.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

De `d`-tag biedt een unieke identificator binnen je video's van die kind, zodat je meerdere adresseerbare video's kunt hebben door verschillende `d`-waarden te gebruiken. De `title`- en `summary`-tags bieden de videotitel en een korte beschrijving voor weergave in clients. De `url`-tag wijst naar het daadwerkelijke videobestand, terwijl `thumb` een voorbeeldafbeelding biedt. De `duration`-tag specificeert de lengte in seconden, en `dim` specificeert optioneel de videodimensies.

De `origin`-tag houdt het bronplatform bij wanneer content van andere diensten wordt geimporteerd. Dit behoudt herkomst bij het migreren van video's van YouTube, Vimeo, of andere platformen naar Nostr-hosting.

Het `content`-veld kan een uitgebreide beschrijving, volledige transcriptie, of aanvullende tekst bevatten die bij de video hoort.

## Waarom Adresseerbare Events Belangrijk Zijn

Reguliere video-events (kinds 21 en 22) zijn onveranderlijk na publicatie. Als je een video publiceert en later een typefout in de titel opmerkt, de thumbnail wilt bijwerken, of de hosting-URL moet wijzigen omdat je naar een andere videodienst bent gemigreerd, kun je het originele event niet aanpassen. Je enige optie is een nieuw event te publiceren met een nieuwe ID, wat bestaande verwijzingen breekt en engagementmetrics verliest.

Adresseerbare video-events lossen dit probleem op door het event vervangbaar te maken. De combinatie van je pubkey, de event kind, en de `d`-tag identificeert je video uniek. Wanneer je een nieuw event publiceert met dezelfde identificatoren, vervangen relays de oude versie met de nieuwe. Clients die je video ophalen krijgen altijd de nieuwste metadata.

Dit is bijzonder waardevol voor het corrigeren van metadatafouten na publicatie, het bijwerken van thumbnails naarmate je branding verbetert, het migreren van videohosting-URL's bij het wisselen van providers, en het importeren van content van stopgezette platformen zoals Vine terwijl herkomst behouden blijft via de `origin`-tag.

## Implementaties

Adresseerbare video-events (kinds 34235 en 34236) zijn momenteel geimplementeerd in Amethyst en nostrvine. Beide clients kunnen adresseerbare video-events maken, weergeven en bijwerken.

---

**Primaire bronnen:**
- [NIP-71 Specificatie](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Adresseerbare video events update

**Vermeld in:**
- [Nieuwsbrief #5: NIP Updates](/nl/newsletters/2026-01-13-newsletter/#nip-updates)

**Zie ook:**
- [NIP-94: Bestandmetadata](/nl/topics/nip-94/)
