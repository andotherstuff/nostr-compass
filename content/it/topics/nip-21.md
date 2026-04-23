---
title: "NIP-21: Schema URI nostr:"
date: 2026-04-22
translationOf: /en/topics/nip-21.md
translationDate: 2026-04-23
draft: false
categories:
  - Protocol
  - Interoperability
---

NIP-21 definisce lo schema URI `nostr:`, un modo standard con cui applicazioni, siti web e sistemi operativi possono registrare l'interesse ad aprire identificatori Nostr come `npub`, `nprofile`, `nevent` e `naddr` tramite il client Nostr che l'utente ha impostato come gestore.

## Come Funziona

Un URI `nostr:` consiste nel prefisso dello schema seguito da uno qualsiasi degli identificatori bech32 di [NIP-19](/it/topics/nip-19/), tranne `nsec`. I client e i sistemi operativi trattano lo schema come fanno con `mailto:` o `tel:`: registrarsi come gestore permette all'utente di fare clic su un link `nostr:` in qualunque punto del sistema e aprirlo nel client Nostr di sua scelta.

Esempi dalla specifica:

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` punta a un profilo utente
- `nostr:nprofile1...` punta a un profilo utente con relay hint inclusi
- `nostr:nevent1...` punta a un event specifico con relay hint
- `nostr:naddr1...` punta a un event replaceable parametrizzato, come un articolo long-form

## Collegare Pagine HTML a Entità Nostr

NIP-21 specifica anche due convenzioni `<link>` utili per le pagine web che corrispondono a entità Nostr. Una pagina che serve lo stesso contenuto di un event Nostr, per esempio un post di blog renderizzato da un articolo `kind:30023` di [NIP-23](/it/topics/nip-23/), può includere un `<link rel="alternate">` che punta all'URI Nostr. Una pagina profilo può includere un `<link rel="me">` o `<link rel="author">` che punta a un `nprofile` per dichiarare l'autorialità basata su Nostr.

## Perché È Importante

Lo schema è il livello di interoperabilità che permette a qualunque identificatore Nostr di diventare un link funzionante fuori dall'interfaccia di un singolo client. Estensioni del browser, gestori del sistema operativo mobile e shell desktop possono tutti instradare gli URI `nostr:` verso il client installato dall'utente, rendendo possibile condividere un profilo o un event incollando un URI ovunque senza perdere la possibilità di aprirlo in modo nativo per Nostr.

## Implementazioni

Il supporto agli URI `nostr:` è diffuso in tutto l'ecosistema dei client, inclusi i principali client Nostr web, mobile e desktop. Estensioni del browser come [nos2x](https://github.com/fiatjaf/nos2x) e [Alby](https://github.com/getAlby/lightning-browser-extension) gestiscono la registrazione dell'URI nei browser desktop.

---

**Fonti primarie:**

- [Specifica NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)

**Menzionato in:**

- [Newsletter #19: Nostrability migra a NIP-34](/en/newsletters/2026-04-22-newsletter/#nostrability-migrates-to-nip-34-and-opens-19-per-nip-interop-trackers)

**Vedi anche:**

- [NIP-19: Entità codificate Bech32](/it/topics/nip-19/)
- [NIP-23: Contenuti long-form](/it/topics/nip-23/)
