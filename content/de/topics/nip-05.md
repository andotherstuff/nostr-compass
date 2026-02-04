---
title: "NIP-05 (Domain-Verifizierung)"
date: 2026-02-04
description: "NIP-05 ermöglicht menschenlesbare Identifikatoren für Nostr-pubkeys durch Domain-Verifizierung."
---

NIP-05 ordnet Nostr-öffentliche Schlüssel menschenlesbaren Internet-Identifikatoren wie `user@example.com` zu. Dies bietet eine Möglichkeit, Identität durch Domain-Besitz zu verifizieren, ohne auf eine zentrale Autorität vertrauen zu müssen.

## Funktionsweise

Ein Benutzer beansprucht einen Identifikator, indem er ein `nip05`-Feld zu seinen Profil-Metadaten hinzufügt. Der Identifikator folgt dem Format `name@domain`. Clients verifizieren den Anspruch, indem sie `https://domain/.well-known/nostr.json` abrufen und prüfen, ob der Name dem pubkey des Benutzers zugeordnet ist.

Die JSON-Datei unter dem well-known-Pfad enthält ein `names`-Objekt, das lokale Namen auf Hex-pubkeys abbildet:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Bei erfolgreicher Verifizierung können Clients den Identifikator anstelle des npub oder daneben anzeigen. Einige Clients zeigen ein Häkchen oder einen anderen Indikator für verifizierte Identifikatoren.

## Relay-Hinweise

Die `nostr.json`-Datei kann optional ein `relays`-Objekt enthalten, das pubkeys auf Arrays von Relay-URLs abbildet. Dies hilft Clients zu entdecken, wo Events eines bestimmten Benutzers zu finden sind.

## Implementierungen

Die meisten großen Clients unterstützen NIP-05-Verifizierung:
- Damus, Amethyst, Primal zeigen verifizierte Identifikatoren an
- Viele Relay-Dienste bieten NIP-05-Identifikatoren als Feature
- Zahlreiche kostenlose und kostenpflichtige NIP-05-Anbieter existieren

## Primäre Quellen

- [NIP-05 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/05.md)

## Erwähnt in

- [Newsletter #8 (2026-02-04)](/de/newsletters/2026-02-04-newsletter/) - PR erfordert Kleinschreibung für Hex-Schlüssel und Namen
