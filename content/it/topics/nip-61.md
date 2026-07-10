---
title: "NIP-61: Nutzap"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-61.md
translationDate: 2026-07-01
categories:
  - Zaps
  - Ecash
---

NIP-61 definisce i "nutzap", pagamenti peer-to-peer in ecash Cashu recapitati come eventi Nostr. Un mittente pubblica un token Cashu bloccato con P2PK indirizzato alla chiave Nostr del destinatario, e il destinatario lo riscatta dalla mint a suo piacimento. Le proof stesse trasportano il valore, quindi un pagamento NIP-61 arriva come un token autosufficiente che il destinatario può riscattare secondo i propri tempi, senza alcun canale Lightning o handshake interattivo richiesto.

## Come funziona

NIP-61 si basa su due primitive esistenti: i wallet Cashu di [NIP-60](/it/topics/nip-60/) e i lock P2PK di Cashu. Il flusso utilizza tre kind di evento.

**Raccomandazione della mint (kind 10019):** un evento sostituibile che il destinatario pubblica per annunciare da quali mint accetta nutzap e la chiave pubblica Cashu utilizzata per bloccare le proof a suo nome. I mittenti la leggono prima di inviare in modo che il token bloccato sia uno che il destinatario può riscattare.

**Evento nutzap (kind 9321):** il pagamento stesso. Trasporta le proof Cashu (bloccate tramite P2PK sul pubkey nutzap del destinatario indicato in kind 10019), l'URL della mint, tag opzionali `e` e `a` che identificano la nota oggetto dello zap, e un tag `p` per il destinatario. Il destinatario lo riceve tramite le normali sottoscrizioni Nostr, sblocca le proof con la chiave privata corrispondente, e le conserva nel suo wallet NIP-60 o le fonde in Lightning.

**Info nutzap (kind 7375):** stato in cache con la stessa forma degli eventi token NIP-60, che registra le proof di nutzap riscattate in modo che il wallet non le conti due volte alla risincronizzazione.

## Compromessi e modello di fiducia

Un nutzap è un token ecash autosufficiente. Finché il destinatario può contattare in un secondo momento la mint, può riscattare il pagamento. La mint stessa è il custode fidato, lo stesso modello di fiducia di NIP-60, e questa scelta di custodia è il prezzo esplicito dei micropagamenti a finalità istantanea e capaci di funzionare offline. Gli zap NIP-57 richiedono che il ricevente esegua (o sia ospitato su) un nodo Lightning con un endpoint LNURL che accetti HTLC in ingresso in tempo reale. Telefoni senza canale Lightning, utenti dietro firewall e destinatari che si trovano offline sono tutti al di fuori di quel modello.

L'annuncio kind 10019 è il varco di fiducia a livello sociale. Il mittente sceglie una delle mint accettate dal destinatario, il che mantiene prevedibile il percorso di riscatto del destinatario. Un mittente che sceglie una mint al di fuori dell'insieme del destinatario rischia un token non riscattabile, quindi i wallet leggono prima il kind 10019.

## Flusso di lavoro

1. Il destinatario pubblica un kind 10019 che annuncia le mint accettate e un pubkey nutzap
2. Il mittente legge il kind 10019, conia proof presso una delle mint elencate e le blocca tramite P2PK sul pubkey nutzap del destinatario
3. Il mittente pubblica un kind 9321 con le proof bloccate, l'URL della mint e i tag di destinazione
4. Il destinatario riceve il kind 9321 tramite la sua normale sottoscrizione Nostr
5. Il destinatario sblocca le proof usando la sua chiave privata nutzap e le conserva nel suo wallet NIP-60 o le fonde in Lightning

## Evento nutzap di esempio

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## Implementazioni

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) rilascia il rendering dei nutzap con viste del saldo per singola mint come parte della sua superficie wallet NIP-60/NIP-61 ([PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075))

---

**Fonti primarie:**
- [Specifica NIP-61](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - Supporto wallet Cashu NIP-60 e nutzap NIP-61

**Menzionato in:**
- [Newsletter #27: Amethyst v1.12.0 rilascia wallet Cashu, nutzap, un driver CLINK e Tor self-heal](/it/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Vedi anche:**
- [NIP-57: Zaps](/it/topics/nip-57/)
- [NIP-60: Wallet Cashu](/it/topics/nip-60/)
- [Cashu](/it/topics/cashu/)
