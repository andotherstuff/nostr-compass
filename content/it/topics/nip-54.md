---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Content
---
NIP-54 definisce la kind `30818` per articoli in stile wiki su Nostr. Più autori possono pubblicare voci sullo stesso argomento, quindi i client hanno bisogno di euristiche di ranking e fiducia invece di una singola pagina canonica.

## Come funziona

Gli articoli wiki sono identificati da un tag `d` normalizzato che rappresenta l'argomento. Più persone possono pubblicare voci con lo stesso argomento normalizzato, creando una wiki aperta senza un redattore centrale.

**Normalizzazione del tag D:**
- Lettere minuscole per i caratteri che hanno varianti maiuscole e minuscole
- Conversione degli spazi bianchi in trattini
- Rimozione di punteggiatura e simboli
- Riduzione dei trattini ripetuti e rimozione dei trattini iniziali o finali
- Conservazione di lettere e numeri non ASCII

Questa regola di normalizzazione conta per l'interoperabilità. Se due client normalizzano lo stesso titolo in modo diverso, interrogheranno argomenti differenti e frammenteranno l'insieme degli articoli.

## Formato del contenuto

La specifica unificata usa markup Asciidoc con due funzionalità aggiuntive:

- **Wikilink** (`[[target page]]`) - Link ad altri articoli wiki su Nostr
- **Link Nostr** - Riferimenti a profili o eventi secondo NIP-21

È stato proposto un passaggio a Djot, ma fino a marzo 2026 non ha sostituito Asciidoc nel NIP canonico.

## Selezione degli articoli

Quando esistono più versioni di un articolo, i client possono dare priorità in base a:

1. Reazioni (NIP-25) che indicano approvazione della comunità
2. Liste di relay (NIP-51) per il ranking delle fonti
3. Liste contatti (NIP-02) che formano reti di raccomandazione

In pratica, questo significa che NIP-54 non è solo un formato di contenuto. È anche un problema di policy lato client. Due client possono mostrare articoli "migliori" diversi per lo stesso argomento pur restando entrambi conformi alla specifica.

## Funzionalità collaborative

- **Forking** - Crea versioni derivate degli articoli
- **Merge request** (kind 818) - Propone modifiche ad articoli esistenti
- **Redirect** (kind 30819) - Punta vecchi argomenti verso quelli nuovi
- **Marcatori di deferenza** - Indicano versioni preferite degli articoli

I fork e i marcatori di deferenza permettono agli autori di riconoscere versioni migliori senza eliminare il proprio lavoro. Questo conta in una rete dove le revisioni precedenti possono restare disponibili su molti relay.

---

**Fonti principali:**
- [Specifica NIP-54](https://github.com/nostr-protocol/nips/blob/master/54.md)
- [PR #2177: Internationalized d-tag normalization](https://github.com/nostr-protocol/nips/pull/2177)

**Citato in:**
- [Newsletter #3: NIP Updates](/en/newsletters/2025-12-31-newsletter/#nip-updates)
- [Newsletter #15: Open PRs](/en/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Vedi anche:**
- [NIP-51: Lists](/it/topics/nip-51/)
- [NIP-02: Follow List](/it/topics/nip-02/)
