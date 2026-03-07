---
title: "NIP-02: Folgeliste"
date: 2025-12-24
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-02 definiert Kind-3-Events, die die Folgeliste eines Nutzers speichern. Dieses Event ist die grundlegende Eingabe für Home-Feeds, Antwortbenachrichtigungen und viele Strategien zur Relay-Auswahl.

## Wie es funktioniert

Ein Kind-3-Event enthält `p`-Tags, die den gefolgten Pubkeys auflisten:

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

Jedes `p`-Tag hat vier Positionen: den Tag-Namen, den gefolgten Pubkey (Hex), einen optionalen Relay-URL-Hinweis und einen optionalen "petname" (einen lokalen Spitznamen). Der Relay-Hinweis sagt anderen Clients, wo sie die Events dieses Nutzers finden können. Der petname erlaubt es, Kontakten merkbare Namen zu geben, ohne sich auf deren selbst deklarierte Anzeigenamen zu verlassen.

## Ersetzbares Verhalten

Kind 3 liegt im ersetzbaren Bereich (0, 3, 10000-19999), daher behalten Relays nur die neueste Version pro Pubkey. Wenn du jemandem neu folgst, veröffentlicht dein Client ein vollständiges neues Kind 3 mit allen bisherigen Follows plus dem neuen Eintrag. Folgelisten müssen also jedes Mal vollständig sein, inkrementelle Updates funktionieren nicht.

## Warum es wichtig ist

Um einen Home-Feed zu erzeugen, laden Clients das Kind 3 des Nutzers, extrahieren alle Pubkeys aus den `p`-Tags und abonnieren dann Kind-1-Events dieser Autoren:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

Das Relay liefert passende Notes zurück, und der Client rendert sie. Die Relay-Hinweise in Kind 3 helfen Clients zu erkennen, welche Relays sie für jeden gefolgten Nutzer abfragen sollten.

Hier zeigt sich auch schnell veralteter sozialer Zustand. Wenn das neueste Kind 3 eines Nutzers auf den abgefragten Relays fehlt, kann sein Feed leer wirken, obwohl die Follows anderswo noch vorhanden sind. Clients, die Ergebnisse aus mehreren Relays zusammenführen, erholen sich meist besser als Clients, die nur einem Relay vertrauen.

## Petnames und Identitat

Das petname-Feld ermöglicht ein dezentrales Benennungsschema. Statt einfach dem Namen zu vertrauen, den ein Nutzer in seinem Profil angibt, kannst du selbst ein Label vergeben. Ein Client könnte etwa "alice (Meine Schwester)" anzeigen, wobei "alice" aus ihrem Kind-0-Profil stammt und "Meine Schwester" dein petname ist. Das liefert Kontext, den globale Benutzernamen nicht bieten können.

## Interop-Hinweise

Weil Kind-3-Events ersetzbar sind und vollständig bleiben müssen, sollten Clients unbekannte Tags beim Aktualisieren erhalten. Wenn ein anderer Client Tags hinzugefügt hat, die dein Client nicht versteht, würde blindes Überschreiben diese Daten verlieren.

Das gilt genauso für Relay-Hinweise und petnames. Sie sind optional, aber wenn sie beim Schreiben verloren gehen, verschlechtert sich die Erfahrung in anderen Clients stillschweigend. Ein sicherer Update-Pfad ist: das neueste bekannte Kind 3 laden, nur die verstandenen Tags ändern, den Rest beibehalten und dann das vollständige Event erneut veröffentlichen.

---

**Primärquellen:**
- [NIP-02 Specification](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Erwähnt in:**
- [Newsletter #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
- [NIP-10: Textnotiz-Threading](/de/topics/nip-10/)
- [NIP-65: Relay List Metadata](/de/topics/nip-65/)
