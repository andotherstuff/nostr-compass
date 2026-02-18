---
title: "NIP-56: Segnalazione"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 definisce un meccanismo di segnalazione usando eventi kind 1984, permettendo agli utenti e alle applicazioni di segnalare contenuti indesiderati sulla rete Nostr.

## Come Funziona

Un utente pubblica un evento kind 1984 con un tag `p` che referenzia la pubkey segnalata. Quando si segnala una nota specifica, un tag `e` referenzia l'ID della nota. Entrambi i tag accettano un terzo parametro che specifica la categoria della violazione.

## Categorie di Segnalazione

- **nudity**: contenuti per adulti
- **malware**: virus, trojan, ransomware
- **profanity**: linguaggio offensivo e incitamento all'odio
- **illegal**: contenuti che potrebbero violare leggi
- **spam**: messaggi ripetitivi indesiderati
- **impersonation**: affermazioni fraudolente di identità
- **other**: violazioni che non rientrano nelle categorie precedenti

## Comportamento di Client e Relay

I client possono usare le segnalazioni degli utenti seguiti per decisioni di moderazione, ad esempio sfocando i contenuti quando più contatti fidati li segnalano. I relay dovrebbero evitare la moderazione automatica tramite segnalazioni per via dei rischi di manipolazione; le segnalazioni di moderatori fidati possono invece informare l'applicazione manuale. La classificazione aggiuntiva è supportata tramite i tag `l` e `L` di NIP-32.

---

**Fonti primarie:**
- [Specifica NIP-56](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Citato in:**
- [Newsletter #10: Aggiornamenti dei Progetti](/it/newsletters/2026-02-18-newsletter/#notedeck-preparazione-allapp-store-android)

**Vedi anche:**
- [NIP-22: Comment](/it/topics/nip-22/)
