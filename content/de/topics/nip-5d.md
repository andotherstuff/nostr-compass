---
title: "NIP-5D: Nostr Web Applets"
date: 2026-04-08
translationOf: /en/topics/nip-5d.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Hosting
  - Applications
description: "Definiert ein postMessage-Protokoll, damit sandboxed Webanwendungen in iframes mit einer hostenden Nostr-Anwendung kommunizieren können."
---

NIP-5D definiert ein `postMessage`-Protokoll für sandboxed Webanwendungen, sogenannte napplets, die in iframes laufen und mit einer hostenden Anwendung, der Shell, kommunizieren. Es erweitert [NIP-5A](/de/topics/nip-5a/) (Static Websites) um eine Runtime-Kommunikationsschicht, die Web-Apps Zugang zu Nostr-Funktionalität gibt, ohne den private key des Nutzers offenzulegen.

## Funktionsweise

Eine Shell-Anwendung lädt ein napplet in einem sandboxed iframe. Das napplet kommuniziert mit der Shell über die `postMessage`-API des Browsers mithilfe eines strukturierten Nachrichtenprotokolls. Die Shell stellt dem napplet über diesen Kanal Nostr-Signing, Relay-Zugriff und User-Kontext bereit. Die iframe-Sandbox verhindert, dass das napplet direkt auf den private key des Nutzers zugreift, daher fungiert die Shell als Gatekeeper für alle Nostr-Operationen.

## Anwendungsfälle

- **Interaktive Nostr-Apps**: Apps bauen, die Nostr-Events lesen und schreiben, ohne dass Nutzer ihren nsec einfügen müssen
- **App-Marktplatz**: Interaktive Webanwendungen über Nostr-Events verteilen
- **Sandboxed Extensions**: Nostr-Clients über Third-Party-napplets um Funktionen erweitern

---

**Primärquellen:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - Nostr Web Applets proposal

**Erwähnt in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)

**Siehe auch:**
- [NIP-5A (Static Websites)](/de/topics/nip-5a/)
- [NIP-5C (Scrolls)](/de/topics/nip-5c/)
