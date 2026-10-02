---
title: "NIP-26: Firma delegata degli event"
date: 2026-09-30
translationOf: /en/topics/nip-26.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Identity
---

NIP-26 documenta un modo con cui una chiave Nostr può autorizzare un’altra chiave a firmare un insieme limitato di event. La sua specifica attuale è contrassegnata come **draft** e **unrecommended**, quindi documenta un progetto precedente e non costituisce un consiglio per una nuova integrazione.

## Come funziona

La chiave dell’account firma un token di delega che indica la chiave delegata e le condizioni. Le condizioni possono limitare i kind degli event e gli orari `created_at`. La chiave delegata firma l’event con la propria chiave e allega il token in un tag `delegation`. Un lettore deve verificare sia la firma dell’event sia il token di delega rispetto a quelle condizioni. I relay che supportano lo schema possono anche effettuare ricerche per delegante.

Il modello consente a un’applicazione di pubblicare senza custodire la chiave di firma principale dell’account. I suoi requisiti aggiuntivi di convalida e di ricerca sui relay spiegano perché le implementazioni non possono considerare una normale firma di event come prova sufficiente di un’identità delegata. La [specifica attuale](https://github.com/nostr-protocol/nips/blob/master/26.md) contrassegna esplicitamente l’approccio come non raccomandato.

---

**Fonti primarie:**
- [Specifica di NIP-26 e stato attuale](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [Testo sulla firma delegata di settembre 2022](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**Citato in:**
- [Newsletter #42: settembre 2022](/it/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
