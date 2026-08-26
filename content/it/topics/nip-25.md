---
title: "NIP-25: Reazioni"
date: 2026-07-29
translationOf: /en/topics/nip-25.md
translationDate: 2026-08-26
draft: false
categories:
  - Protocol
  - Social
---

NIP-25 definisce le reazioni come eventi kind `7`. Dà ai client una forma di evento condivisa per allegare un'emoji o un'altra breve reazione a una nota, un articolo, un annuncio o un altro evento referenziato.

## Come funziona

Un evento di reazione porta il proprio testo di reazione in `content` e referenzia l'obiettivo tramite il tag `e` dell'evento obiettivo. Quando l'obiettivo è indirizzabile, la reazione include anche il suo tag `a`. Include inoltre tag `p` per l'autore dell'evento referenziato, il che permette a relay e client di instradare le notifiche senza dedurre i destinatari dal contenuto dell'evento.

La reazione predefinita è `+`, così i client possono trattare un contenuto di reazione vuoto come risposta positiva. Altre emoji sono valori di reazione validi. La specifica permette anche `-` per una reazione negativa, che l'aggiunta di luglio 2022 ha introdotto dopo l'introduzione originale.

I client dovrebbero preservare il riferimento all'obiettivo e i tag dell'autore quando creano una reazione. Una reazione è un normale evento firmato, quindi può viaggiare tramite le consuete subscription ai relay ed essere resa da qualsiasi client che riconosca il kind `7`.

## Implementazioni

NIP-25 è ampiamente implementato da client e librerie Nostr come parte della normale interazione con le note. Il suo semplice modello di kind e tag permette ai client di mostrare conteggi, reazioni singole e notifiche senza un protocollo di trasporto separato.

---

**Fonti primarie:**
- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [Commit di introduzione](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [Aggiunta sul voto negativo](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**Menzionato in:**
- [Newsletter #33: Sei anni di luglio su Nostr](/it/newsletters/2026-07-29-newsletter/#sei-anni-di-luglio-su-nostr)
- [Newsletter #37: Marmot](/it/newsletters/2026-08-26-newsletter/#marmot)

**Vedi anche:**
- [NIP-01: Basic Protocol](/it/topics/nip-01/)
- [NIP-10: Text Note Threading](/it/topics/nip-10/)
