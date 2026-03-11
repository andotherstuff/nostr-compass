---
title: "NIP-96: HTTP File Storage"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Media
---
NIP-96 definisce come i client Nostr caricano, scaricano e gestiscono file su server multimediali HTTP. Ora è contrassegnato come "unrecommended" a favore di Blossom, ma conta ancora perché server e client esistenti continuano a supportarlo durante la transizione.

## Come funziona

Un client scopre le capacità di un file server recuperando `/.well-known/nostr/nip96.json`. Quel documento pubblicizza l'URL dell'API di upload, l'eventuale URL di download, i content type supportati, i limiti di dimensione e se il server supporta trasformazioni dei media o delegated hosting.

Per l'upload, il client invia un POST `multipart/form-data` all'URL dell'API con un header di autorizzazione [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md). Il server risponde con un oggetto di metadati nella forma di NIP-94 che include l'URL del file più tag come `ox` per l'hash originale e, quando applicabile, `x` per il file trasformato che verrà effettivamente servito.

I download usano `GET <api_url>/<sha256-hash>` con parametri di query facoltativi come la larghezza dell'immagine. La cancellazione usa `DELETE` con auth NIP-98. Gli utenti pubblicano eventi kind `10096` per dichiarare i propri server di upload preferiti.

## Dettagli del modello dati

Un dettaglio utile è che NIP-96 identifica i file tramite l'hash del file originale, anche quando il server trasforma l'upload. Questo permette a un client di cancellare o riscaricare la risorsa usando lo stesso identificatore stabile, continuando però a ricevere thumbnail generate dal server o varianti ricompresse quando disponibili.

Il documento well-known supporta anche `delegated_to_url`, che permette a un relay di indirizzare i client verso un server HTTP di storage separato. Questo evitava che il software del relay dovesse implementare da sé l'intera API dei media.

## Perché è stato deprecato

NIP-96 legava gli URL dei file a server specifici. Se un server andava offline, ogni nota Nostr che faceva riferimento agli URL di quel server perdeva i suoi media. Blossom ribalta questa impostazione rendendo l'hash SHA-256 del contenuto del file l'identificatore canonico. Qualunque server Blossom che ospita lo stesso file lo serve allo stesso percorso hash, così il contenuto è portabile tra server per impostazione predefinita.

Blossom semplifica anche l'API: PUT semplice per gli upload, GET per i download, ed eventi Nostr firmati, non header HTTP, per l'autorizzazione. La deprecazione è avvenuta nel settembre 2025 tramite [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## Note di interoperabilità

Server come nostr.build e void.cat supportavano NIP-96 e hanno aggiunto o migrato verso endpoint Blossom. I client sono in fasi diverse: Angor v0.2.5 ha aggiunto la configurazione del server NIP-96, mentre ZSP v0.3.1 carica esclusivamente su server Blossom. La coesistenza continuerà finché le implementazioni NIP-96 rimanenti non completeranno la migrazione.

Gli eventi di preferenza server kind 10096 restano utili per la selezione dei server Blossom. I metadati dei file NIP-94, eventi kind 1063, descrivono le proprietà dei file indipendentemente dal protocollo di upload che li ha creati.

---

**Fonti primarie:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Menzionato in:**
- [Newsletter #9: NIP Deep Dive](/it/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-file-storage-and-the-transition-to-blossom)

**Vedi anche:**
- [Blossom Protocol](/it/topics/blossom/)
- [NIP-94: File Metadata](/it/topics/nip-94/)
