---
title: "NIP-73: Identificatori di contenuti esterni"
date: 2026-02-04
draft: false
translationOf: /en/topics/nip-73.md
translationDate: 2026-11-05
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 definisce un modo standard per fare riferimento a contenuti esterni all'interno degli eventi Nostr. Usa tag `i` per l'identificatore stesso e tag `k` per il tipo di identificatore, così i client possono raggruppare le discussioni attorno allo stesso libro, sito web, episodio di podcast, luogo, hashtag od oggetto blockchain. La [specifica attuale](https://github.com/nostr-protocol/nips/blob/master/73.md) è contrassegnata come bozza e opzionale.

## Come funziona {#how-it-works}

Un evento che usa NIP-73 include un tag `i` con un identificatore esterno normalizzato e un tag `k` che indica la famiglia dell'identificatore. I client possono interrogare i relay per un singolo soggetto esatto tramite `i` o per un'intera famiglia tramite `k`. NIP-73 non aggiunge alcun kind di evento proprio. Sono commenti, recensioni e altri eventi a portare i tag.

Frammento di tag, non un evento completo:

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

Una pagina web inserisce il proprio URL normalizzato in `i` e imposta `k` su `web`. La specifica copre diverse famiglie di identificatori, tra cui:

- URL web normalizzati senza frammento
- ISBN per i libri
- ISAN per i film
- DOI
- geohash e codici ISO 3166 di paesi o suddivisioni
- GUID di feed, episodi ed editori di podcast
- hashtag
- identificatori di transazioni e indirizzi blockchain

## Regole di normalizzazione {#normalization-rules}

La corrispondenza dipende da stringhe identiche, quindi la specifica stabilisce un'unica forma scritta per ciascuna famiglia. Esempi tratti dalla specifica:

- i geohash usano `geo:<value>` e devono essere in minuscolo
- i codici di paesi e suddivisioni usano `iso3166:<code>` e devono essere in maiuscolo
- gli ISBN omettono i trattini
- i DOI sono in minuscolo
- gli URL web eliminano i frammenti
- gli hash delle transazioni blockchain usano esadecimale minuscolo

La normalizzazione stabilisce come si scrive un singolo identificatore. Non unisce gli alias. Gli ISBN specifici di un'edizione e gli URL che si normalizzano in stringhe diverse restano identificatori separati, quindi la discussione su uno stesso libro o articolo può comunque distribuirsi su più valori `i`.

## Suggerimenti URL {#url-hints}

Un tag `i` può includere un suggerimento URL opzionale come terzo elemento dell'array, ovvero il secondo valore dopo il nome del tag. Un client privo di un renderer personalizzato per quel tipo di identificatore può usare il suggerimento come link di ripiego.

Frammento di tag: `["i", "isbn:9780765382030", "<url-hint>"]`

Il suggerimento è scelto dall'autore. Non fa parte dell'identità, non prova alcuna proprietà e non indica un sito canonico.

## Fiducia e contesto {#trust-and-context}

Due eventi con lo stesso identificatore finiscono nella stessa conversazione, e l'identificatore condiviso non stabilisce nulla di più. Un evento firmato identifica il proprio autore. Non autentica il libro, il sito o l'editore del podcast a cui fa riferimento, e non mostra chi li controlla.

Il significato di un tag `i` dipende dall'evento. Nei commenti [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md), `I`/`K` maiuscoli indicano l'ambito radice e `i`/`k` minuscoli indicano il genitore. Questa struttura di thread deriva da NIP-22, e NIP-73 non definisce alcun kind di commento. [NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) usa `i` per le identità esterne nei profili, quindi non tutti i tag `i` sono soggetti NIP-73.

Anche le asserzioni attendibili di [NIP-85](/it/topics/nip-85/) possono avere come destinazione identificatori NIP-73 come libri, siti web, hashtag e luoghi.

## Implementazioni {#implementations}

Il file [nip73.rs al commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) di rust-nostr analizza i prefissi noti trasformandoli in un `ExternalContentId` tipizzato e converte un eventuale suggerimento in un URL tipizzato. Scrive il terzo elemento del tag solo quando esiste un suggerimento. I suoi test mantengono gli ISBN con i trattini: il parser rimuove il prefisso e memorizza il resto senza applicare la normalizzazione della specifica, quindi il parsing tipizzato non garantisce stringhe canoniche. Esclude gli ID di catena dalla famiglia, mappando `ethereum:100:tx:<hash>` su `ethereum:tx`. Quella revisione non ha una variante `iso3166` per i paesi.

Il file [DisplayExternalId.kt al commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) di Amethyst indirizza gli identificatori geohash, hashtag e URL verso visualizzazioni dedicate e mostra gli altri tipi supportati come chip di ambito generico. Un URL apre il percorso di thread dell'app dedicato a quella pagina. Con le anteprime disattivate, il rendering normale mostra un semplice chip con il link e non richiede alcuna anteprima. Con le anteprime attivate, il recupero di un'anteprima mancante può contattare il sito di destinazione. Nessuno dei due file mostra come si comporta una versione rilasciata.

---

**Fonti primarie:**
- [Specifica NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Aggiunge i codici ISO 3166 di paesi e suddivisioni
- [rust-nostr nip73.rs al commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [Amethyst DisplayExternalId.kt al commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**Menzionato in:**
- [Newsletter #47: Approfondimento NIP](/it/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [Newsletter #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [Newsletter #37: agosto 2025](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [Newsletter #8: Aggiornamenti NIP](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: Approfondimento NIP-85](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #36: Commenti (NIP-22)](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [Newsletter #38: Approfondimento NIP](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [Newsletter #40: filtri podcast-medium di NIP-73](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [Newsletter #42: contenuti esterni di settembre 2024](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**Vedi anche:**
- [NIP-31: Gestione dei kind di evento sconosciuti](/it/topics/nip-31/)
- [NIP-22: Commento](/it/topics/nip-22/)
- [NIP-39: Identità esterne nei profili](/it/topics/nip-39/)
- [NIP-85: Asserzioni attendibili](/it/topics/nip-85/)
