---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
translationOf: /en/topics/nip-59.md
translationDate: 2026-03-11
draft: false
categories:
  - Privacy
  - Protocol
---
NIP-59 definisce gift wrap, un modo per incapsulare un evento così che relay e osservatori esterni non apprendano il vero mittente dall'evento esterno che ricevono.

## Struttura

Un evento wrapped con gift wrap ha tre livelli:

1. **Rumor** - L'evento di destinazione senza firma.
2. **Seal** (kind `13`) - Il rumor cifrato per il destinatario e firmato dal vero mittente.
3. **Gift Wrap** (kind `1059`) - Il seal cifrato di nuovo e firmato da una chiave casuale usa e getta.

Il seal deve avere tag vuoti. Il gift wrap esterno di solito porta il tag `p` del destinatario così che i relay possano instradarlo.

## Cosa nasconde

Gift wrap nasconde il mittente a relay e osservatori di rete perché l'evento esterno è firmato da una chiave disposable. Il destinatario, però, può comunque decifrare il seal interno e capire quale chiave a lungo termine lo ha firmato. Quindi il guadagno in privacy è la protezione dei metadata sul livello di trasporto, non l'anonimato rispetto al destinatario.

La specifica raccomanda anche di randomizzare i timestamp del wrapper e, quando possibile, di usare relay che richiedono autenticazione e servono gli eventi wrapped solo al destinatario previsto. Senza questo comportamento dei relay, i metadata del destinatario possono comunque trapelare.

## Note operative

Gift wrap non è di per sé un protocollo di messaggistica. Altri protocolli, come i sistemi di messaggistica privata, lo usano come elemento costruttivo.

I relay possono scegliere di non conservare a lungo gli eventi wrapped perché non hanno utilità pubblica. La specifica consente anche proof-of-work sul wrapper esterno quando le implementazioni vogliono una resistenza allo spam aggiuntiva.

## Casi d'uso

- Messaggi diretti privati (NIP-17)
- Note solo per amici (proposta NIP-FR)
- Payload per notifiche push (proposta NIP-9a)
- Qualsiasi scenario che richieda privacy del mittente rispetto alla rete

---

**Fonti primarie:**
- [NIP-59 Specification](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Citato in:**
- [Newsletter #8: NIP Deep Dive](/it/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-59-gift-wrap)
- [Newsletter #1: News](/it/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: NIP Updates](/it/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #15: Open PRs](/it/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Vedi anche:**
- [NIP-17: Private Direct Messages](/it/topics/nip-17/)
