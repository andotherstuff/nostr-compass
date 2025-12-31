---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocollo
  - Contenuto
---

NIP-54 definisce kind 30818 come un tipo di evento indirizzabile per creare articoli wiki e voci enciclopediche su Nostr. Consente la creazione di contenuti collaborativi e decentralizzati dove più autori possono scrivere sugli stessi argomenti.

## Come Funziona

Gli articoli wiki sono identificati da un `d` tag normalizzato (l'argomento dell'articolo). Più persone possono scrivere articoli sullo stesso soggetto, creando una base di conoscenza decentralizzata senza autorità centrale.

**Normalizzazione del D Tag:**
- Convertire tutte le lettere in minuscolo
- Convertire gli spazi in trattini
- Rimuovere punteggiatura e simboli
- Preservare i caratteri non-ASCII e i numeri

## Formato del Contenuto

Gli articoli utilizzano il markup Asciidoc con due caratteristiche speciali:

- **Wikilinks** (`[[pagina destinazione]]`) - Link ad altri articoli wiki su Nostr
- **Link Nostr** - Riferimenti a profili o eventi secondo NIP-21

## Selezione degli Articoli

Quando esistono più versioni di un articolo, i client danno priorità in base a:

1. Reazioni (NIP-25) che indicano l'approvazione della comunità
2. Liste di relay (NIP-51) per la classificazione delle fonti
3. Liste di contatti (NIP-02) che formano reti di raccomandazione

## Funzionalità Collaborative

- **Forking** - Creare versioni derivate degli articoli
- **Richieste di merge** (kind 818) - Proporre modifiche agli articoli esistenti
- **Reindirizzamenti** (kind 30819) - Puntare vecchi argomenti verso nuovi
- **Marcatori di deferenza** - Indicare le versioni preferite degli articoli

---

**Fonti primarie:**
- [Specifica NIP-54](https://github.com/nostr-protocol/nips/blob/master/54.md)

**Menzionato in:**
- [Newsletter #3: Aggiornamenti NIP](/it/newsletters/2025-12-31-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-51: Liste](/it/topics/nip-51/)
- [NIP-02: Lista dei Seguiti](/it/topics/nip-02/)
