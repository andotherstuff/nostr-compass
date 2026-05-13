---
title: "NIP-78: App-spezifische Daten"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-78.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Data Storage
---

NIP-78 definiert einen Standard-Event-Kind, mit dem Anwendungen beliebige Daten im Namen eines Nutzers über Nostr-Events speichern können, um geräteübergreifende Zustandssynchronisation ohne zentralen Server zu ermöglichen.

## Funktionsweise

Der zentrale Event-Kind ist 30078, ein parametrisiertes ersetzbares Event. Der `d`-Tag ist eine anwendungsdefinierte Bezeichner-Zeichenfolge, die den Speicherslot auf eine bestimmte Anwendung und einen bestimmten Zweck beschränkt.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

Eine Anwendung veröffentlicht ein 30078-Event mit einem eindeutigen `d`-Tag (zum Beispiel `tamagostrich-pet-state` oder `amethyst-settings`) und dem JSON- oder Textinhalt, der gespeichert werden soll. Da 30078 ersetzbar und durch den `d`-Tag bereichert ist, bedeutet das Aktualisieren des gespeicherten Zustands, ein neues Event mit demselben `d`-Tag zu veröffentlichen; der Relay behält nur die neueste Version.

## Geräteübergreifende Synchronisation

Jeder Client, der den öffentlichen Schlüssel eines Nutzers und den `d`-Tag der Anwendung kennt, kann den aktuellen Zustand aus dem Relay-Set des Nutzers abrufen und auf jedem Gerät rekonstruieren. Die Daten gehören dem Nutzer, weil sie in Events leben, die mit seinem Schlüsselpaar signiert und auf Relays aus seiner [NIP-65](/de/topics/nip-65/)-Relay-Liste gespeichert sind.

## Private vs. öffentliche Daten

Für private Anwendungsdaten kann das Inhaltsfeld mit [NIP-44](/de/topics/nip-44/) verschlüsselt werden, bevor es veröffentlicht wird, sodass der Relay nur Chiffretext speichert, den nur der Schlüsselinhaber entschlüsseln kann. Öffentliche Anwendungsdaten können unverschlüsselt gespeichert werden, damit andere Clients sie lesen und anzeigen können.

## Inhaltsformat

NIP-78 lässt das Inhaltsformat bewusst offen; Anwendungen wählen ihr eigenes Schema. Die gängige Konvention ist, `d`-Tags mit dem Anwendungsnamen zu präfixieren, um Kollisionen zwischen Apps zu verhindern, die denselben Relay nutzen.

## Implementierungen

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — Haustier-Zustandssynchronisation über Geräte hinweg via `tamagostrich-pet-state` kind:30078-Events
- [Wisp](https://github.com/barrydeen/wisp-android) — kind:30078-Wallet-Backup und geräteübergreifende Sicherheitseinstellungssynchronisation; Outbox-Abonnements zu einer einzelnen REQ mit NIP-78-Autorenfilter zusammengeführt
- [NosPress](https://github.com/nostrapps/nospress) — CMS-Orchestrierungszustand in NIP-78-Events gespeichert
- Mehrere Nostr-Client-Einstellungssynchronisationsimplementierungen (Amethyst, andere)

---

**Primäre Quellen:**
- [NIP-78-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — Produktionsimplementierung

**Erwähnt in:**
- [Newsletter #22: NIP-78 Deep Dive](/de/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [Newsletter #22: Tamagostrich](/de/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**Siehe auch:**
- [NIP-51: Listen](/de/topics/nip-51/)
- [NIP-44: Versionierte Verschlüsselung](/de/topics/nip-44/)
- [NIP-65: Relay-Listen-Metadaten](/de/topics/nip-65/)
