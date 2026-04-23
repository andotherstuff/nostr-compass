---
title: "NIP-05: Domain-Verifizierung"
date: 2026-02-04
description: "NIP-05 ermöglicht menschenlesbare Identifikatoren für Nostr-Pubkeys durch Domain-Verifizierung."
translationOf: /en/topics/nip-05.md
translationDate: 2026-03-07
draft: false
categories:
  - Identity
  - Discovery
---

NIP-05 ordnet Nostr-Public Keys menschenlesbaren Internet-Identifikatoren wie `user@example.com` zu. Es gibt Nutzern einen DNS-gestützten Identitätshinweis, den Clients über HTTPS verifizieren können.

## Wie es funktioniert

Ein Nutzer beansprucht einen Identifikator, indem er seinen Profil-Metadaten ein `nip05`-Feld hinzufügt. Der Identifikator folgt dem Format `name@domain`. Clients verifizieren diesen Anspruch, indem sie `https://domain/.well-known/nostr.json` abrufen und prüfen, ob der Name auf den Pubkey des Nutzers zeigt.

Die JSON-Datei unter dem well-known-Pfad enthält ein `names`-Objekt, das lokale Namen auf Hex-Pubkeys abbildet:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Wenn die Verifizierung erfolgreich ist, können Clients den Identifikator anstelle des npub oder zusätzlich dazu anzeigen. Manche Clients zeigen einen Verifizierungsindikator, andere geben den Identifikator als einfachen Text aus und überlassen die Vertrauensentscheidung dem Leser.

## Vertrauensmodell

NIP-05 ist kein globales Benutzernamen-Register. Es beweist die Kontrolle über einen Domain-Namen und einen Webserver-Pfad, nicht die rechtliche Identität oder eine langfristig stabile Kontinuität. Wenn ein Domain-Betreiber die Zuordnung später ändert, verifizieren Clients die neue Zuordnung, sofern sie keinen früheren Zustand gespeichert halten.

Dadurch ist NIP-05 für Auffindbarkeit und Reputation nützlich, aber schwächer, als viele Nutzer annehmen. Ein guter Client sollte es als verifizierte Domain-Kontrolle behandeln, nicht als Beweis dafür, dass eine Person oder Organisation wirklich die behauptete ist.

## Relay-Hinweise

Die `nostr.json`-Datei kann optional ein `relays`-Objekt enthalten, das Pubkeys auf Arrays von Relay-URLs abbildet. Das hilft Clients dabei herauszufinden, wo sich die Events eines bestimmten Nutzers finden lassen.

## Interop-Hinweise

Die Kleinschreibungs-Anforderung ist wichtiger, als es auf den ersten Blick wirkt. Gemischte Groß- und Kleinschreibung bei Namen oder Pubkeys kann in einer Implementierung funktionieren und in einer anderen scheitern, deshalb sollten aktuelle Clients mit kleingeschriebenen Namen und kleingeschriebenen Hex-Schlüsseln in `nostr.json` rechnen.

Ein weiteres praktisches Detail ist der spezielle Name `_`. Damit kann eine Domain die nackte Identifikatorform wie `_@example.com` oder einfach `example.com` für Clients abbilden, die das unterstützen. Nicht jeder Client stellt diese Form gleich dar, daher bekommen Nutzer mit expliziten `name@domain`-Identifikatoren weiter die konsistentesten Ergebnisse.

## Implementierungsstatus

Die meisten großen Clients unterstützen NIP-05-Verifizierung:
- Damus, Amethyst und Primal zeigen verifizierte Identifikatoren an
- Viele Relay-Dienste bieten NIP-05-Identifikatoren als Funktion an
- Es gibt zahlreiche kostenlose und kostenpflichtige NIP-05-Anbieter

---

**Primärquellen:**
- [NIP-05 Specification](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [PR #2208](https://github.com/nostr-protocol/nips/pull/2208) - lowercase requirement for names and hex keys

**Erwähnt in:**
- [Newsletter #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
- [NIP-65: Relay List Metadata](/de/topics/nip-65/)
