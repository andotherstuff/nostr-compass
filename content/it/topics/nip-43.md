---
title: "NIP-43: Metadati di Accesso e Richieste per i Relay"
date: 2026-03-18
translationOf: /en/topics/nip-43.md
translationDate: 2026-04-01
draft: false
categories:
  - Protocol
  - Relay
  - Access Control
---

NIP-43 definisce come i relay pubblicano informazioni sull'appartenenza e come gli utenti richiedono ammissione, inviti o rimozione dai relay con accesso limitato. Fornisce al controllo di accesso dei relay una superficie di event standardizzata invece di costringere ogni relay privato o semi-privato a inventare il proprio protocollo di adesione.

## Come Funziona

La specifica combina diversi kind di event:

- kind `13534` pubblica una lista dei membri del relay
- kind `8000` annuncia che un membro è stato aggiunto
- kind `8001` annuncia che un membro è stato rimosso
- kind `28934` permette a un utente di inviare una richiesta di adesione con un codice di reclamo
- kind `28935` permette a un relay di restituire un codice invito su richiesta
- kind `28936` permette a un utente di richiedere la revoca del proprio accesso

Lo stato di appartenenza non è intenzionalmente derivato da un singolo event. Un client potrebbe dover consultare sia gli event di appartenenza firmati dal relay che gli event dell'utente stesso prima di decidere se l'accesso è attuale.

## Perché È Importante

NIP-43 fornisce ai relay con accesso limitato un modo standard per esprimere lo stato di ammissione e appartenenza. Questo è importante per i sistemi di gruppo, le comunità solo su invito e i relay che necessitano di onboarding leggibile dalle macchine senza ricorrere a moduli web fuori banda o flussi di lavoro manuali dell'operatore.

La chiarificazione aperta nella [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) precisa un punto pratico: i relay dovrebbero mantenere un unico stato di appartenenza autoritativo per pubkey. Questo aiuta i client a evitare cronologie di replay ambigue dove un vecchio event di aggiunta o rimozione può essere interpretato erroneamente come stato attuale.

## Note sull'Interoperabilità

NIP-43 dipende dal relay che pubblicizza il supporto attraverso il suo documento [NIP-11](/it/topics/nip-11/). Le richieste di adesione, invito e uscita dovrebbero essere inviate solo ai relay che dichiarano esplicitamente di supportare questo NIP.

Poiché gli event si trovano sia nello spazio controllato dal relay che in quello controllato dall'utente, le implementazioni necessitano di regole chiare per la risoluzione dei conflitti. Ecco perché la chiarificazione sullo stato di appartenenza è più importante di quanto appaia a prima vista.

---

**Fonti primarie:**
- [Specifica NIP-43](https://github.com/nostr-protocol/nips/blob/master/43.md)
- [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) - Chiarimento sulla gestione dello stato di appartenenza

**Menzionato in:**
- [Newsletter #14: Aggiornamenti NIP](/it/newsletters/2026-03-18-newsletter/#aggiornamenti-nip)

**Vedi anche:**
- [NIP-11: Documento Informativo del Relay](/it/topics/nip-11/)
- [NIP-42: Autenticazione dei Client verso i Relay](/it/topics/nip-42/)
