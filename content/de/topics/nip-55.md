---
title: "NIP-55: Android Signer Application"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 definiert, wie Android-Apps Signing- und Verschlüsselungsoperationen von einer separaten Signer-Anwendung anfordern. Damit erhalten Android-Clients eine native Alternative zu Browser-Extensions und entfernten Bunkern.

## Funktionsweise

NIP-55 verwendet zwei Android-Mechanismen:

- **Intents** für Vordergrund-Flows mit expliziter Zustimmung des Nutzers
- **Content resolvers** für Hintergrund-Flows, nachdem der Nutzer eine dauerhafte Berechtigung erteilt hat

Der übliche Verbindungsablauf beginnt mit `get_public_key`. Der Signer gibt sowohl den pubkey des Nutzers als auch den Package-Namen des Signers zurück, und der Client soll beides cachen. `get_public_key` in Hintergrundschleifen zu wiederholen ist ein häufiger Implementierungsfehler, vor dem die Spezifikation ausdrücklich warnt.

## Wichtige Operationen

- **get_public_key** - Den pubkey des Nutzers und den Package-Namen des Signers abrufen
- **sign_event** - Ein Nostr-Event signieren
- **nip04_encrypt/decrypt** - NIP-04-Nachrichten ver- oder entschlüsseln
- **nip44_encrypt/decrypt** - NIP-44-Nachrichten ver- oder entschlüsseln
- **decrypt_zap_event** - Zap-bezogene Event-Payloads entschlüsseln

## Sicherheits- und UX-Hinweise

NIP-55 hält Keys auf dem Gerät, hängt aber weiterhin von Android-App-Grenzen und der Berechtigungsverwaltung des Signers ab. Unterstützung für Content Resolvers liefert eine deutlich glattere UX als wiederholte Intent-Prompts, aber erst nachdem der Nutzer diesem Client eine dauerhafte Freigabe erteilt hat.

Für Web-Apps auf Android ist NIP-55 weniger ergonomisch als NIP-46. Browser-basierte Flows können keine direkten Hintergrundantworten erhalten wie native Android-Apps, deshalb fallen viele Implementierungen auf Callback-URLs, Zwischenablage oder manuelles Einfügen zurück.

---

**Primärquellen:**
- [NIP-55 Specification](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Erwähnt in:**
- [Newsletter #1: Releases](/de/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/de/newsletters/2025-12-24-newsletter/)
- [Newsletter #2: NIP Updates](/de/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #4: NIP Updates](/de/newsletters/2026-01-07-newsletter/)
- [Newsletter #11: NIP Deep Dive](/de/newsletters/2026-02-25-newsletter/)
- [Newsletter #13: Samizdat v1.0.0-alpha](/en/newsletters/2026-03-11-newsletter/)

**Siehe auch:**
- [NIP-46: Nostr Connect](/de/topics/nip-46/)
