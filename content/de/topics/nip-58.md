---
title: "NIP-58: Badges"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 definiert ein Badge-System für Nostr, das es Ausstellern ermöglicht, Badges zu erstellen und an Benutzer zu vergeben, die diese dann auf ihren Profilen anzeigen können.

## Funktionsweise

### Badge-Definition (Kind 30009)

Aussteller erstellen Badge-Definitionen als adressierbare Events:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Beigetreten vor 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Badge-Vergabe (Kind 8)

Aussteller vergeben Badges an Benutzer:

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

Benutzer wählen, welche Badges auf ihrem Profil angezeigt werden:

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

## Anwendungsfälle

- **Community-Mitgliedschaft**: Mitgliedschaft in Gruppen oder Communities nachweisen
- **Erfolge**: Beiträge oder Meilensteine anerkennen
- **Verifizierung**: Drittanbieter-Attestierungen (Mitarbeiter, Creator usw.)
- **Zugriffskontrolle**: Inhalte oder Funktionen basierend auf Badge-Besitz einschränken

## Vertrauensmodell

Der Badge-Wert hängt vollständig von der Reputation des Ausstellers ab. Jeder kann Badges erstellen, daher sollten Clients:
- Aussteller-Informationen prominent anzeigen
- Benutzern erlauben, nach vertrauenswürdigen Ausstellern zu filtern
- Badges ohne Kontext nicht als autoritativ behandeln

## Verwandt

- [NIP-51](/de/topics/nip-51/) - Listen
- [Web of Trust](/de/topics/web-of-trust/)
