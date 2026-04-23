---
title: "NIP-5A: Siti Web Statici"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Hosting
---

NIP-5A definisce come ospitare siti web statici sotto keypair Nostr. Gli autori dei siti pubblicano event manifesto firmati che mappano i percorsi URL a hash SHA256 dei contenuti, e i server host risolvono quei manifesti per servire i file del sito dallo storage Blossom.

## Come Funziona

La specifica usa due kind di event. Kind `15128` è un manifesto del sito root, uno per pubkey, che funge da sito web predefinito per quella chiave. Kind `35128` è un manifesto del sito con nome, identificato da un tag `d`, che funziona come un sottodominio. Ogni manifesto contiene tag `path` che mappano percorsi URL assoluti a hash SHA256 dei file da servire.

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

Un server host riceve una richiesta HTTP, estrae la pubkey dell'autore dal sottodominio, recupera il manifesto del sito dalla lista relay dell'autore, risolve il percorso richiesto in un hash del contenuto, e scarica il blob corrispondente dal server o dai server Blossom elencati nei tag `server`.

## Risoluzione URL

I siti root usano l'npub come sottodominio. I siti con nome usano una codifica base36 di 50 caratteri della pubkey grezza seguita dal valore del tag `d`, il tutto in una singola etichetta DNS. Poiché le etichette DNS sono limitate a 63 caratteri e la pubkey in base36 ne usa sempre 50, gli identificatori dei siti con nome sono limitati a 13 caratteri.

## Implementazioni

- [nsite](https://github.com/lez/nsite) - Server host che risolve i manifesti NIP-5A e serve i file
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - UI per costruire e pubblicare manifesti dei siti

---

**Fonti primarie:**
- [Specifica NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - Proposta originale e merge
- [nsite](https://github.com/lez/nsite) - Implementazione host di riferimento
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - UI di pubblicazione e gestione

**Menzionato in:**
- [Newsletter #16: NIP-5A viene unito](/it/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/it/newsletters/2026-04-01-newsletter/)

**Vedi anche:**
- [Blossom](/it/topics/blossom/)
- [NIP-65: Relay List Metadata](/it/topics/nip-65/)
- [NIP-96: HTTP File Storage](/it/topics/nip-96/)
