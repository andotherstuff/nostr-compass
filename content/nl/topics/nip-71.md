---
title: "NIP-71: Video Events"
date: 2026-01-13
translationOf: /en/topics/nip-71.md
translationDate: 2026-03-11
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 definieert event kinds voor videocontent op Nostr, zodat video's met goede metadata-ondersteuning gedeeld kunnen worden. De specificatie behandelt zowel reguliere video events als adresseerbare video events. Die laatste werden in januari 2026 toegevoegd, zodat makers videometadata kunnen bijwerken zonder opnieuw te publiceren.

## Event Kinds

NIP-71 definieert vier event kinds, verdeeld in twee categorieën op basis van beeldverhouding en adresseerbaarheid.

Reguliere video events gebruiken kind 21 voor horizontale (landscape) video's en kind 22 voor verticale (portrait/shorts) video's. Dit zijn standaard Nostr-events waarvan de content na publicatie onveranderlijk is.

Adresseerbare video events gebruiken kind 34235 voor horizontale video's en kind 34236 voor verticale video's. Dit zijn parameterized replaceable events, geïdentificeerd door de combinatie van pubkey, kind en `d` tag. Als je een nieuw event publiceert met dezelfde identificatoren, vervangt dat de vorige versie, wat metadata-updates mogelijk maakt.

## Structuur

Een volledig adresseerbaar video event bevat identificatievelden, metadata tags en de verwijzing naar de videocontent.

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

De `d` tag geeft een unieke identificator binnen je video's van dat kind, zodat je meerdere adresseerbare video's kunt hebben door verschillende `d`-waarden te gebruiken. De `title` en `summary` tags geven de videotitel en een korte beschrijving voor weergave in clients. De `url` tag verwijst naar het videobestand zelf, terwijl `thumb` een previewafbeelding levert. De `duration` tag geeft de lengte in seconden aan, en `dim` geeft optioneel de videodimensies op.

De `origin` tag houdt het bronplatform bij wanneer content uit andere diensten wordt geïmporteerd. Zo blijft de herkomst behouden wanneer video's van YouTube, Vimeo of andere platforms naar Nostr-hosting worden gemigreerd.

Het `content` veld kan een uitgebreide beschrijving, volledig transcript of andere aanvullende tekst bevatten die bij de video hoort.

## Waarom Adresseerbare Events Belangrijk Zijn

Reguliere video events (kinds 21 en 22) zijn na publicatie onveranderlijk. Als je een video publiceert en later een typefout in de titel ontdekt, de thumbnail wilt bijwerken, of de hosting-URL moet wijzigen omdat je naar een andere videodienst bent verhuisd, kun je het oorspronkelijke event niet aanpassen. Je enige optie is een nieuw event met een nieuwe ID te publiceren, wat bestaande verwijzingen breekt en engagement-metrics verliest.

Adresseerbare video events lossen dit probleem op door het event replaceable te maken. De combinatie van je pubkey, het event kind en de `d` tag identificeert je video uniek. Wanneer je een nieuw event publiceert met dezelfde identificatoren, vervangen relays de oude versie door de nieuwe. Clients die je video ophalen, krijgen altijd de nieuwste metadata.

Dit is vooral waardevol voor het corrigeren van metadatafouten na publicatie, het bijwerken van thumbnails terwijl je branding verbetert, het migreren van video-hosting-URL's bij een wissel van provider en het importeren van content van verdwenen platforms zoals Vine, terwijl de herkomst via de `origin` tag behouden blijft.

Een extra voordeel is stabiel linken. Andere events kunnen naar dezelfde adresseerbare video blijven verwijzen terwijl de maker presentatiedetails eromheen bijwerkt. Dat is netter dan comments en verwijzingen te versnipperen over meerdere onveranderlijke reposts.

## Afwegingen

Replaceability helpt bij het onderhouden van metadata, maar het betekent ook dat clients moeten bepalen hoeveel historische staat ze bewaren. Als een maker de titel of summary na publicatie wijzigt, wordt het nieuwste event canoniek, ook al kunnen oudere clients nog de vorige versie hebben geïndexeerd.

Kinds 21 en 22 blijven relevant voor toepassingen die een onveranderlijk publicatieregister willen. NIP-71 dwingt niet elke video-workflow in het replaceable model.

## Implementaties

Adresseerbare video events (kinds 34235 en 34236) zijn momenteel geïmplementeerd in Amethyst en nostrvine. Beide clients kunnen adresseerbare video events maken, weergeven en bijwerken.

---

**Primaire bronnen:**
- [NIP-71 Specificatie](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Update voor adresseerbare video events

**Vermeld in:**
- [Nieuwsbrief #5: NIP Updates](/nl/newsletters/2026-01-13-newsletter/#nip-updates)
- [Nieuwsbrief #12: NoorNote](/nl/newsletters/2026-03-04-newsletter/)

**Zie ook:**
- [NIP-94: File Metadata](/nl/topics/nip-94/)
