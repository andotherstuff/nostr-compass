---
title: "NIP-55: Android-Signer-Anwendung"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-03-11
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 definiert, wie Android-Apps Signatur- und Verschlusselungsoperationen von einer separaten Signer-Anwendung anfordern. Damit bekommen Android-Clients eine native Alternative zu Browser-Erweiterungen und entfernten Bunkern.

## Wie es funktioniert

NIP-55 verwendet zwei Android-Mechanismen:

- **Intents** fur Vordergrund-Ablaufe mit expliziter Zustimmung des Nutzers
- **Content resolvers** fur Hintergrund-Ablaufe, nachdem der Nutzer eine dauerhafte Berechtigung erteilt hat

Der ubliche Verbindungsablauf beginnt mit `get_public_key`. Der Signer gibt sowohl den Pubkey des Nutzers als auch den Package-Namen des Signers zuruck, und vom Client wird erwartet, dass er beides cached. `get_public_key` in Hintergrundschleifen zu wiederholen ist ein haufiger Implementierungsfehler, vor dem die Spezifikation ausdrucklich warnt.

## Wichtige Operationen

- **get_public_key** - Den Pubkey des Nutzers und den Package-Namen des Signers abrufen
- **sign_event** - Ein Nostr-Event signieren
- **nip04_encrypt/decrypt** - NIP-04-Nachrichten ver- oder entschlusseln
- **nip44_encrypt/decrypt** - NIP-44-Nachrichten ver- oder entschlusseln
- **decrypt_zap_event** - Zap-bezogene Event-Payloads entschlusseln

## Sicherheits- und UX-Hinweise

NIP-55 halt Schlussel auf dem Gerat, ist aber weiterhin auf Android-App-Grenzen und die Berechtigungsverwaltung des Signers angewiesen. Die Unterstutzung von Content Resolvern sorgt fur eine deutlich angenehmere UX als wiederholte Intent-Prompts, aber erst nachdem der Nutzer diesem Client eine dauerhafte Freigabe erteilt hat.

Fur Web-Apps auf Android ist NIP-55 weniger ergonomisch als NIP-46. Browser-basierte Ablaufe konnen keine direkten Hintergrundantworten erhalten wie native Android-Apps, deshalb fallen viele Implementierungen auf Callback-URLs, Zwischenablage oder manuelles Einfugen zuruck.

---

**Primarquellen:**
- [NIP-55 Specification](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Erwahnt in:**
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7: NIP Updates](/en/newsletters/2026-01-07-newsletter/#nip-updates)
- [Newsletter #11: NIP Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-55-android-signer-application)

**Siehe auch:**
- [NIP-46: Nostr Connect](/de/topics/nip-46/)
