---
title: "NIP-A4: Messaggi Pubblici"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4 definisce i messaggi pubblici (kind 24) progettati per schermate di notifica, con ampio supporto client come obiettivo.

## Come Funziona

A differenza delle conversazioni threaded, questi messaggi non hanno concetto di cronologia chat o catene di messaggi. Sono semplici messaggi one-off destinati ad apparire nel feed notifiche di un destinatario.

## Struttura

- Usa tag `q` (citazioni) invece di tag `e` per evitare complicazioni di threading
- Nessuno stato conversazione o cronologia
- Progettato per semplici notifiche pubbliche

## Casi d'Uso

- Riconoscimenti pubblici o shoutout
- Messaggi broadcast a un utente
- Notifiche che non necessitano threading delle risposte

---

**Fonti primarie:**
- [PR NIP-A4](https://github.com/nostr-protocol/nips/pull/1988)

**Menzionato in:**
- [Newsletter #2: Aggiornamenti NIP](/it/newsletters/2025-12-24-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-01: Protocollo Base](/it/topics/nip-01/)
- [NIP-10: Threading Note di Testo](/it/topics/nip-10/)

