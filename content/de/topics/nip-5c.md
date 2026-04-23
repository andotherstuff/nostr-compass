---
title: "NIP-5C: Scrolls (WASM Programs)"
date: 2026-04-08
translationOf: /en/topics/nip-5c.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Programs
  - WebAssembly
description: "Definiert Konventionen zum Veröffentlichen und Entdecken von WebAssembly-Programmen auf Nostr, wobei WASM-Binaries als Nostr-Events verteilt werden."
---

NIP-5C, früher NIP-A5, definiert Konventionen zum Veröffentlichen, Entdecken und Ausführen von WebAssembly-Programmen, den sogenannten Scrolls, auf Nostr. WASM-Binaries werden als Nostr-Events gespeichert, sodass jeder Client sie abrufen und in einer sandboxed Runtime ausführen kann.

## Funktionsweise

Entwickler veröffentlichen WASM-Programme als Nostr-Events, die das kompilierte Binary enthalten. Clients entdecken diese Programme über Standard-Nostr-Queries, laden das WASM-Binary aus dem Event herunter und führen es in einer sandboxed WebAssembly-Runtime aus. Die Sandbox verhindert, dass Scrolls direkt auf das Hostsystem zugreifen, und beschränkt sie auf die Fähigkeiten, die die Runtime ausdrücklich bereitstellt.

## Anwendungsfälle

- **Portable Compute**: Programme auf jedem Client ausführen, der WASM-Execution unterstützt
- **Dezentrale App-Distribution**: Anwendungen ohne App Stores veröffentlichen und entdecken
- **Komponierbare Werkzeuge**: Scrolls für komplexe Workflows miteinander verketten

## Demo

Eine [Demo-App](https://nprogram.netlify.app/) zeigt Scrolls im Browser, mit Beispielprogrammen, die als Nostr-Events veröffentlicht wurden.

---

**Primärquellen:**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - Scrolls (WASM Programs) proposal

**Erwähnt in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)
- [Newsletter #19: NIP-5D applets proposal](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-5D (Web Applets)](/de/topics/nip-5d/)
- [NIP-5A (Static Websites)](/de/topics/nip-5a/)
