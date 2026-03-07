---
title: "NIP-24: Campi metadata extra"
date: 2025-12-17
translationOf: /en/topics/nip-24/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---
NIP-24 definisce campi opzionali aggiuntivi per i metadata utente kind 0 oltre a name, about e picture di base.

## Campi metadata extra

- **display_name**: Un nome alternativo, più grande e con caratteri più ricchi di `name`
- **website**: Un URL web collegato all'autore dell'evento
- **banner**: URL di un'immagine larga (~1024x768) per la visualizzazione opzionale sullo sfondo
- **bot**: Boolean che indica che il contenuto è interamente o parzialmente automatizzato
- **birthday**: Oggetto con campi opzionali year, month e day

La specifica segna anche due campi più vecchi come deprecati: `displayName` dovrebbe diventare `display_name`, e `username` dovrebbe diventare `name`. I client li vedono ancora in circolazione, quindi un parser tollerante aiuta con la compatibilità all'indietro anche se chi scrive non dovrebbe emetterli.

## Tag standard

NIP-24 standardizza anche tag general-purpose:
- `r`: Riferimento URL web
- `i`: Identificatore esterno
- `title`: Nome per vari tipi di evento
- `t`: Hashtag (deve essere in minuscolo)

## Perché è importante

NIP-24 riguarda soprattutto la convergenza. Questi campi e tag comparivano già in vari client, quindi la specifica assegna loro nomi e significati coerenti. Questo riduce piccole ma fastidiose incompatibilità, per esempio quando i client non concordano se un banner debba stare sotto `banner` o sotto una chiave specifica di un'app.

Un punto pratico per chi implementa è che kind 0 resta un hot path nella maggior parte dei client. I metadata extra devono restare leggeri. Se un campo richiede un proprio pattern di fetch o un ciclo di aggiornamento indipendente, probabilmente appartiene a un kind di evento separato invece di gonfiare i metadata del profilo.

---

**Fonti primarie:**
- [Specifica NIP-24](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Citato in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-01: Basic Protocol](/it/topics/nip-01/)
