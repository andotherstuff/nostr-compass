---
title: "NIP-68: Feed incentrati sulle immagini"
date: 2026-07-29
translationOf: /en/topics/nip-68.md
translationDate: 2026-07-29
draft: false
categories:
  - Media
  - Protocol
---

NIP-68 definisce event indirizzabili per le immagini. Offre ai client un modo portabile per pubblicare metadati, didascalie, etichette e riferimenti ai file delle immagini, mantenendo l'event separato dall'archiviazione dei blob.

## Come funziona

Un event immagine usa kind `20`, include un tag `title` e contiene una descrizione in `content`. Il tag `imeta` descrive ogni immagine con campi come `url`, `m` per il tipo MIME, `dim` per le dimensioni, il testo `alt` e un hash SHA-256 facoltativo. Più tag `imeta` consentono a un event di rappresentare un insieme di immagini.

L'event può includere tag `p` per le persone raffigurate o accreditate, tag `t` per gli argomenti e normali riferimenti Nostr. Può includere anche tag per tipo di media, hash, posizione e avviso sui contenuti, così che i client possano filtrare e visualizzare i post con immagini in modo coerente.

NIP-68 non prescrive un backend di archiviazione. I client possono fare riferimento a normali URL HTTPS o a un sistema con indirizzamento basato sul contenuto, come Blossom, purché pubblichino metadati `imeta` sufficienti affinché un altro client possa visualizzare e verificare l'immagine.

## Implementazioni

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0) ha aggiunto i tag NIP-68 per le immagini alle funzionalità del client dedicate alle immagini.

---

**Fonti primarie:**
- [Specifica NIP-68](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**Menzionato in:**
- [Newsletter #33: Rilasci taggati](/it/newsletters/2026-07-29-newsletter/#tagged-releases)

**Vedi anche:**
- [Protocollo Blossom](/it/topics/blossom/)
- [NIP-94: Metadati dei file](/it/topics/nip-94/)
