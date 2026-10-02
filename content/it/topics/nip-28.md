---
title: "NIP-28: Chat pubblica"
date: 2026-09-30
translationOf: /en/topics/nip-28.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Social
---

NIP-28 descrive canali di chat pubblici, messaggi nei canali e moderazione lato client sotto forma di event Nostr. La specifica attuale è contrassegnata come **draft** e **unrecommended** e indirizza gli implementatori verso NIP-29 per gli attuali gruppi basati sui relay.

## Modello degli event

Il kind `40` crea un canale; il kind `41` ne aggiorna i metadati; il kind `42` trasporta un messaggio. I kind `43` e `44` permettono a un utente di nascondere un messaggio o silenziare un altro utente nel proprio client. I tag dei messaggi fanno riferimento all’event di creazione del canale e possono identificare il messaggio a cui si risponde. I relay non sono tenuti ad applicare queste scelte lato client di occultamento e silenziamento.

La [modifica alla specifica di settembre 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb) ha reso una stanza di chat pubblica un oggetto condiviso del protocollo. Questo ruolo storico resta utile da comprendere anche se la [specifica attuale](https://github.com/nostr-protocol/nips/blob/master/28.md) raccomanda un percorso diverso per le nuove implementazioni.

---

**Fonti primarie:**
- [Specifica di NIP-28 e stato attuale](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [Modifica sulla chat pubblica di settembre 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**Citato in:**
- [Newsletter #42: settembre 2022](/it/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**Vedi anche:**
- [NIP-29: Gruppi basati sui relay](/it/topics/nip-29/)
