---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2026-03-07
draft: false
categories:
  - Trust
  - Social Graph
---
Web of Trust (WoT) è un modello di fiducia decentralizzato in cui reputazione e affidabilità derivano dalle relazioni nel grafo sociale invece che da autorità centrali.

## Come funziona

In Nostr, Web of Trust di solito parte dal follow graph di [NIP-02: Follow List](/it/topics/nip-02/) e talvolta aggiunge mute, report o segnali di identità verificata. Un client o servizio sceglie una o più pubkey seed di cui già si fida, poi propaga la fiducia verso l'esterno attraverso il grafo.

1. **Costruzione del grafo**: costruire un grafo diretto di follow e segnali negativi opzionali
2. **Selezione dei seed**: partire dalle pubkey di cui l'osservatore si fida già
3. **Propagazione del punteggio**: far scorrere il rank attraverso il grafo con un algoritmo come PageRank o una sua variante
4. **Soglie e normalizzazione**: limitare la profondità del grafo, attenuare gli account con poco segnale e normalizzare il punteggio finale per visualizzazione o filtro

L'algoritmo esatto non è standardizzato. Due sistemi WoT possono essere entrambi validi pur producendo classifiche diverse perché usano seed diversi, profondità del grafo diverse, regole di decadimento diverse o trattamenti diversi di mute e report.

## Perché è importante

WoT offre a Nostr un modo per classificare e filtrare senza un servizio centrale di moderazione. Un grafo di fiducia personalizzato è più difficile da manipolare di un semplice conteggio follower perché gli account falsi hanno comunque bisogno che la fiducia fluisca verso di loro dalla rete esistente dell'osservatore.

Il lato opposto è il cold start. Se non segui nessuno, un WoT personalizzato non ha quasi alcuna base per classificare nulla. Molti prodotti risolvono questo problema distribuendo follow iniziali, default di provider fidati o punteggi precalcolati da servizi esterni.

## Applicazioni in Nostr

- **Filtro dello spam**: i relay possono usare WoT per filtrare contenuti a bassa fiducia
- **Scoperta dei contenuti**: far emergere contenuti da account di cui la tua rete si fida
- **Directory di pagamento**: lookup di indirizzi Lightning con prevenzione dell'impersonazione
- **Policy dei relay**: i relay WoT accettano solo note da pubkey fidate
- **Moderazione decentralizzata**: le comunità possono curare i contenuti in base ai punteggi di fiducia

## Note di implementazione

Poiché i calcoli WoT richiedono di esplorare grandi parti della rete, molti client non li eseguono localmente. [NIP-85: Trusted Assertions](/it/topics/nip-85/) esiste in parte per questo motivo: offre ai client un modo per consumare calcoli WoT firmati da terzi quando il calcolo locale è troppo costoso.

Le implementazioni esistenti rispondono anche a domande diverse. Un rank di fiducia globale è utile per la scoperta e la resistenza allo spam su tutta la rete. Un punteggio locale personalizzato è migliore per "mostrami gli account di cui il mio grafo si fiderebbe". Leggere un numero WoT senza sapere quale modello lo ha prodotto è una fonte comune di confusione.

---

**Fonti primarie:**
- [NIP-02: Follow List](https://github.com/nostr-protocol/nips/blob/master/02.md)
- [NIP-85: Trusted Assertions](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [Protocollo DCoSL](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Citato in:**
- [Newsletter #3: Riepilogo di dicembre](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [NIP-02: Follow List](/it/topics/nip-02/)
