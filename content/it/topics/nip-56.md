---
title: "NIP-56: Segnalazione"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---
NIP-56 definisce eventi di segnalazione kind `1984`. Permettono a utenti e app di pubblicare segnali di moderazione su account, note e blob senza richiedere un'unica autorità di moderazione condivisa.

## Come funziona

Una segnalazione deve includere un tag `p` per la pubkey segnalata. Se la segnalazione riguarda un evento specifico, deve includere anche un tag `e` per quell'evento. Il tipo di segnalazione appare come terzo valore nel tag `p`, `e` o `x` pertinente.

## Categorie di segnalazione

- **nudity**: contenuto per adulti
- **malware**: virus, trojan, ransomware e payload simili
- **profanity**: linguaggio offensivo e incitamento all'odio
- **illegal**: contenuto che potrebbe violare la legge
- **spam**: messaggi ripetitivi indesiderati
- **impersonation**: false rivendicazioni di identità
- **other**: violazioni che non rientrano nelle categorie sopra

Le segnalazioni di blob usano tag `x` con l'hash del blob e possono includere un tag `server` che punta all'endpoint di hosting. Questo rende NIP-56 usabile per la moderazione dei media, non solo di note e profili.

## Modello di sicurezza e fiducia

Le segnalazioni sono segnali, non verdetti. I client possono pesarle usando fiducia sociale, liste di moderazione o ruoli espliciti di moderatore. Anche i relay possono leggerle, ma la specifica mette in guardia contro una moderazione completamente automatica perché le segnalazioni sono facili da manipolare.

Una classificazione aggiuntiva può essere inserita con i tag `l` e `L` di NIP-32, utile quando un client vuole un vocabolario di moderazione più fine rispetto ai sette tipi base di segnalazione.

---

**Fonti principali:**
- [Specifica NIP-56](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Citato in:**
- [Newsletter #10: Project Updates](/en/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-prep)

**Vedi anche:**
- [NIP-22: Comment](/it/topics/nip-22/)
