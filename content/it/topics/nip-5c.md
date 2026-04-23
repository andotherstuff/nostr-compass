---
title: "NIP-5C: Scrolls (Programmi WASM)"
date: 2026-04-08
translationOf: /en/topics/nip-5c.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Applications
---

NIP-5C, in precedenza NIP-A5, definisce convenzioni per pubblicare, scoprire ed eseguire programmi WebAssembly ("scrolls") su Nostr. I binari WASM vengono memorizzati come eventi Nostr, permettendo a qualunque client di recuperarli ed eseguirli in un runtime sandboxed.

## Come funziona

Gli sviluppatori pubblicano programmi WASM come eventi Nostr che contengono il binario compilato. I client scoprono questi programmi con query Nostr standard, scaricano il binario WASM dall'evento e lo eseguono in un runtime WebAssembly sandboxed. La sandbox impedisce agli scroll di accedere direttamente al sistema host, limitandoli alle capacità che il runtime espone esplicitamente.

## Casi d'uso

- **Calcolo portabile**: eseguire programmi su qualunque client che supporti l'esecuzione WASM
- **Distribuzione decentralizzata di app**: pubblicare e scoprire applicazioni senza app store
- **Strumenti componibili**: concatenare scroll per workflow complessi

## Demo

Una [demo app](https://nprogram.netlify.app/) mostra scroll in esecuzione nel browser, con programmi di esempio pubblicati come eventi Nostr.

---

**Fonti primarie:**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - proposta Scrolls (programmi WASM)

**Menzionato in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)
- [Newsletter #19: proposta di applet NIP-5D](/en/newsletters/2026-04-22-newsletter/)

**Vedi anche:**
- [NIP-5D (Web Applets)](/it/topics/nip-5d/)
- [NIP-5A (Siti Web statici)](/it/topics/nip-5a/)
