---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2025-12-31
draft: false
categories:
  - Media
  - Protocollo
---

NIP-92 consente agli utenti di allegare file multimediali agli eventi Nostr includendo URL insieme a tag di metadati in linea che descrivono tali risorse.

## Come Funziona

1. L'utente inserisce gli URL dei media direttamente nel contenuto dell'evento (ad esempio, in una nota di testo kind 1)
2. Un tag `imeta` (metadati in linea) corrispondente fornisce dettagli su ogni URL
3. I client possono sostituire gli URL imeta con anteprime arricchite basate sui metadati
4. I metadati vengono tipicamente generati automaticamente quando i file vengono caricati durante la composizione

## Il Tag imeta

Ogni tag `imeta` deve avere un `url` e almeno un altro campo. I campi supportati includono:

- `url` - L'URL del media (obbligatorio)
- `m` - Tipo MIME del file
- `dim` - Dimensioni dell'immagine (larghezza x altezza)
- `blurhash` - Blurhash per la generazione dell'anteprima
- `alt` - Testo alternativo per l'accessibilità
- `x` - Hash SHA-256 (da NIP-94)
- `fallback` - URL alternativi se quello principale fallisce

## Esempio

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Fonti primarie:**
- [Specifica NIP-92](https://github.com/nostr-protocol/nips/blob/master/92.md)

**Menzionato in:**
- [Newsletter #3: Riepilogo di Dicembre](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [NIP-94: Metadati File](/it/topics/nip-94/)
