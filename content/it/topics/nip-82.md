---
title: "NIP-82 proposto (non assegnato): catalogo di applicazioni software"
date: 2026-06-17
lastmod: 2026-10-28
translationOf: /en/topics/nip-82.md
translationDate: 2026-10-28
draft: false
categories:
  - Proposals
  - Apps
---

Il catalogo di applicazioni software descritto in questa pagina è una proposta in fase di revisione. Non è un NIP accettato. Si trova nella [pull request #2526 di nostr-protocol/nips](https://github.com/nostr-protocol/nips/pull/2526), intitolata "Zapstore spec". Al momento dell'ultimo aggiornamento di questa pagina, quella pull request risulta aperta e non unita, e il branch master ufficiale dei NIP non contiene alcun file `82.md`. "NIP-82" è l'etichetta che la proposta attribuisce a sé stessa. Non si tratta di un numero di NIP ufficiale. Kind degli event, tag e comportamento potrebbero cambiare prima di un eventuale merge. Secondo la pull request, essa sostituisce la precedente [pull request #1336](https://github.com/nostr-protocol/nips/pull/1336).

## Kind di event proposti

La bozza suddivide un catalogo software in diversi tipi di event:

- **Kind 32267, applicazione:** un event indirizzabile che descrive un'app.
- **Kind 30063, release:** un event indirizzabile dedicato a una singola versione di quell'app. Fa riferimento agli asset di quella versione.
- **Kind 3063, asset:** un event regolare che descrive un singolo file scaricabile.
- **Kind 30267, selezione curata:** una lista indirizzabile che un curatore pubblica per raggruppare o consigliare app.
- **Kind 30509, collegamento al certificato di firma:** un event indirizzabile che collega un certificato X.509, per esempio un certificato di firma APK, alla chiave Nostr che pubblica il software, così i client sanno quali certificati controlla quel publisher. Il suo tag `d` è l'hash SHA-256 del certificato codificato in DER. Contiene una firma realizzata con la chiave privata del certificato e una scadenza espressa come timestamp Unix; facoltativamente, può contrassegnare il collegamento come revocato.
- **Kind 10067, lista di relay:** una lista sostituibile dei relay in cui si possono trovare gli event del catalogo.

## Piattaforma, integrità e validità

Gli event degli asset riportano identificatori di piattaforma e di runtime, in modo che un client possa mostrare solo i file adatti a un dispositivo. Ogni asset include anche un hash del file. Grazie a questo, un client può verificare che i byte scaricati corrispondano a ciò che il publisher ha firmato. Per i pacchetti Android, la bozza include l'impronta del certificato di firma. Prima di proporre un aggiornamento, un installer può confrontarla con il certificato di un'app già installata. Prima di installare un pacchetto Android, i client DOVREBBERO recuperare l'event kind 30509 tramite l'hash del certificato. Dovrebbero inoltre verificarne la firma del certificato rispetto al certificato incorporato nell'APK e rispetto al publisher dell'asset, e controllare che la prova non sia scaduta né revocata.

## Limiti di fiducia

Una firma valida dimostra soltanto che una determinata chiave ha pubblicato un event. Non prova che la chiave appartenga al vero sviluppatore, che il software sia sicuro o che la lista di un curatore sia affidabile. Riguardo ai publisher arbitrari, la proposta non offre alcuna garanzia. Spetta ai client e agli utenti decidere su quali chiavi di publisher e di curatori fare affidamento. Questa pagina non dichiara alcun audit di sicurezza né alcuna interoperabilità in produzione.

## Relazione con NIP-89

Gli event handler di [NIP-89](/it/topics/nip-89/) annunciano quali applicazioni sono in grado di gestire quali kind di event. Questa proposta descrive invece gli artefatti software e dove reperirli, quindi le due coprono ambiti distinti.

---

**Fonti primarie:**
- [PR #2526 di nostr-protocol/nips: Zapstore spec](https://github.com/nostr-protocol/nips/pull/2526) (aperta, non unita; sostituisce la [PR #1336](https://github.com/nostr-protocol/nips/pull/1336))

**Citato in:**
- [Newsletter #27: copertura del rilascio di Amethyst v1.12.0 (riferimento storico)](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #46: catalogo di applicazioni software proposto come NIP-82](/it/newsletters/2026-10-28-newsletter/#software-application-catalog-proposed-as-nip-82)

**Vedi anche:**
- [NIP-89: gestori di applicazioni](/it/topics/nip-89/)
