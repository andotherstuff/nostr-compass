---
title: "NIP-58: Badges"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 definiert ein Badge-System fur Nostr. Ein Event definiert das Badge, ein anderes verleiht es, und ein drittes lasst den Empfanger auswahlen, ob es im Profil angezeigt wird.

## Wie es funktioniert

### Badge-Definition (Kind 30009)

Aussteller erstellen Badge-Definitionen als adressierbare Events:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Badge-Vergabe (Kind 8)

Aussteller verleihen Badges an einen oder mehrere Nutzer:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Badge-Anzeige (Kind 30008)

Nutzer wahlen aus, welche Badges sie im Profil anzeigen:

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

In einem Profile-Badges-Event sollten Clients `a`- und `e`-Tags als geordnete Paare lesen. Ein `a`-Tag ohne das passende Award-Event oder ein `e`-Tag ohne die passende Badge-Definition sollte ignoriert werden.

## Anwendungsfalle

- **Community-Mitgliedschaft**: Zugehorigkeit zu Gruppen oder Communities anzeigen
- **Erfolge**: Beitrage oder Meilensteine anerkennen
- **Attestations**: Einer Drittpartei erlauben, fur eine Rolle oder einen Status zu bürgen
- **Access control**: Features oder Bereiche mit vom Aussteller gestutzten Badges absichern

## Vertrauensmodell

Der Wert eines Badges hangt vollstandig von der Reputation des Ausstellers ab. Jeder kann Badges erstellen, deshalb sollten Clients:

- Informationen zum Aussteller deutlich anzeigen
- Nutzern erlauben, nach vertrauenswurdigen Ausstellern zu filtern
- Badges ohne Kontext nicht als autoritativ behandeln

Badge-Vergaben sind unveranderlich und nicht ubertragbar. Das macht Badges fur Attestations und Anerkennung geeignet, aber nicht fur portable Credentials im tokenisierten Sinn.

## Implementierungshinweise

Badge-Definitionen sind adressierbare Events. Aussteller konnen Artwork oder Beschreibung also im Lauf der Zeit aktualisieren, ohne die Badge-Identitat zu andern. Das Award-Event ist der dauerhafte Nachweis, der einen Empfanger zu einem bestimmten Zeitpunkt mit dieser Definition verbindet.

Clients haben auch Spielraum bei der Darstellung. Die Spezifikation erlaubt ausdrucklich, weniger Badges zu zeigen als ein Nutzer auflistet, und eine Thumbnail-GroBe zu wahlen, die zum verfugbaren Platz passt.

---

**Primarquellen:**
- [NIP-58 Specification](https://github.com/nostr-protocol/nips/blob/master/58.md)

**Erwahnt in:**
- [Newsletter #7: Five Years of Nostr Januarys](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #15: Five Years of Nostr Februaries](/en/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [NIP-51: Lists](/de/topics/nip-51/)
- [Web of Trust](/de/topics/web-of-trust/)
