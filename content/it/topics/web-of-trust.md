---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2025-12-31
draft: false
categories:
  - Fiducia
  - Grafo Sociale
---

Web of Trust (WoT) è un modello di fiducia decentralizzato dove la reputazione e l'affidabilità derivano dalle relazioni del grafo sociale piuttosto che da autorità centrali.

## Come Funziona

In Nostr, Web of Trust sfrutta il grafo dei follow (liste contatti NIP-02) e gli eventi di segnalazione per calcolare punteggi di fiducia:

1. **Costruzione del Grafo**: Un grafo diretto viene costruito da pubkey, eventi e le loro relazioni (follow, silenziati, segnalazioni)
2. **Assegnazione dei Pesi**: Pesi iniziali vengono assegnati a pubkey note come affidabili (es. quelle con identificatori NIP-05 verificati)
3. **Propagazione Iterativa**: I punteggi di fiducia fluiscono attraverso la rete usando algoritmi simili a PageRank
4. **Resistenza Sybil**: Se un attaccante crea molti account falsi, la fiducia passata a loro viene divisa per il numero di falsi

## Proprietà Chiave

- **Decentralizzato**: Nessuna autorità centrale determina la reputazione
- **Personalizzato**: La fiducia può essere calcolata dalla prospettiva di ogni utente in base a chi segue
- **Resistente ai Sybil**: Le farm di bot non possono facilmente manipolare il sistema a causa della diluizione della fiducia
- **Componibile**: Può essere applicato al filtraggio spam, moderazione dei contenuti, ammissione ai relay e directory di pagamento

## Applicazioni in Nostr

- **Filtraggio Spam**: I relay possono usare WoT per filtrare contenuti a bassa fiducia
- **Scoperta di Contenuti**: Mostrare contenuti da account di cui la tua rete si fida
- **Directory di Pagamento**: Ricerca di indirizzi Lightning con prevenzione dell'impersonificazione
- **Politiche dei Relay**: I relay WoT accettano solo note da pubkey affidabili
- **Moderazione Decentralizzata**: Le comunità possono curare in base ai punteggi di fiducia

## Implementazioni

Diversi progetti implementano Web of Trust per Nostr:
- **Nostr.Band Trust Rank**: Punteggio in stile PageRank per la rete
- **WoT Relays**: Relay che filtrano per distanza sociale
- **DCoSL**: Protocollo per sistemi di reputazione decentralizzati
- **Noswot**: Punteggio di fiducia basato su follow e segnalazioni

---

**Fonti principali:**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [Protocollo DCoSL](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Menzionato in:**
- [Newsletter #3: Riepilogo di Dicembre](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [NIP-02: Lista dei Seguiti](/it/topics/nip-02/)
