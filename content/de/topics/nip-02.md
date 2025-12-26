---
title: "NIP-02: Folgeliste"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-02 definiert Kind-3-Events, die Ihre Folgeliste speichern. Dieser einfache Mechanismus bildet das soziale Netzwerk, das Zeitleisten ermöglicht.

## Struktur

Ein Kind-3-Event enthält `p`-Tags, die gefolgten Pubkeys auflisten:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Jedes `p`-Tag hat vier Positionen: den Tag-Namen, den gefolgten Pubkey (Hex), einen optionalen Relay-URL-Hinweis und einen optionalen "Petname" (ein lokaler Spitzname). Der Relay-Hinweis teilt anderen Clients mit, wo sie Events dieses Benutzers finden können. Der Petname ermöglicht es Ihnen, Kontakten einprägsame Namen zuzuweisen, ohne sich auf deren selbstdeklarierte Anzeigenamen zu verlassen.

## Ersetzbares Verhalten

Kind 3 fällt in den ersetzbaren Bereich (0, 3, 10000-19999), sodass Relays nur die neueste Version pro Pubkey behalten. Wenn Sie jemandem neu folgen, veröffentlicht Ihr Client ein komplett neues Kind 3 mit allen Ihren Follows plus dem neuen. Das bedeutet, Folgelisten müssen jedes Mal vollständig sein; Sie können keine inkrementellen Updates veröffentlichen.

## Zeitleisten erstellen

Um einen Home-Feed zu erstellen, rufen Clients das Kind 3 des Benutzers ab, extrahieren alle `p`-Tag-Pubkeys und abonnieren dann Kind-1-Events von diesen Autoren:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

Das Relay gibt passende Notizen zurück, und der Client rendert sie. Die Relay-Hinweise in Kind 3 helfen Clients zu wissen, welche Relays für jeden gefolgten Benutzer abzufragen sind.

## Petnames und Identität

Das Petname-Feld ermöglicht ein dezentrales Benennungsschema. Anstatt dem Namen zu vertrauen, den ein Benutzer in seinem Profil angibt, können Sie Ihr eigenes Label vergeben. Ein Client könnte "alice (Meine Schwester)" anzeigen, wobei "alice" aus ihrem Kind-0-Profil stammt und "Meine Schwester" Ihr Petname ist. Dies bietet Kontext, den globale Benutzernamen nicht liefern können.

## Praktische Überlegungen

Da Kind-3-Events ersetzbar und vollständig sein müssen, sollten Clients unbekannte Tags beim Aktualisieren beibehalten. Wenn ein anderer Client Tags hinzugefügt hat, die Ihr Client nicht versteht, würden Sie diese Daten durch blindes Überschreiben verlieren. Hängen Sie neue Follows an, anstatt von Grund auf neu aufzubauen.

---

**Primärquellen:**
- [NIP-02 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Erwähnt in:**
- [Newsletter #2: NIP Deep Dive](/de/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
