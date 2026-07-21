---
title: "ProofMode"
date: 2026-07-15
translationOf: /en/topics/proofmode.md
translationDate: 2026-07-15
draft: false
categories:
  - Media
  - Provenance
---

[ProofMode](https://proofmode.org/) è un toolkit open-source per la provenienza dei media, sviluppato da Guardian Project, WITNESS e Okthanks, che associa dati verificabili di autenticità e catena di custodia a foto e video al momento della cattura. Non è specifico per Nostr; i client Nostr che trasportano dati ProofMode integrano uno standard esterno già esistente anziché un nuovo livello di protocollo.

## Come funziona

Il componente Capture di ProofMode incorpora metadati di provenienza direttamente nei file multimediali durante la cattura, supportando gli stessi standard interoperabili utilizzati dalla Content Authenticity Initiative (CAI), Content Credentials (CR) e C2PA. Un componente Verify separato ispeziona file audio, immagine e video per verificare quei metadati alla ricerca di segni di generazione tramite IA o modifiche successive, e un componente Preserve gestisce l'archiviazione ridondante e decentralizzata dei dati di prova sottostanti per la conservazione a lungo termine. Un SDK Develop consente alle app di integrare cattura e verifica senza costruire autonomamente il formato di provenienza.

## Perché è importante

Per un client Nostr di video o immagini, trasportare dati ProofMode significa che chi guarda dispone di un metodo esterno e multipiattaforma per verificare se un contenuto multimediale è stato catturato come dichiarato e non è stato alterato silenziosamente da allora, senza fare affidamento sul client di pubblicazione o sul relay come fonte di fiducia. Questa distinzione conta soprattutto per una copia scaricata o ricodificata di un clip: i dati di provenienza che sopravvivono al download e a qualsiasi watermarking applicato dal client sono ciò che rende l'attestazione ancora verificabile dopo che il file ha lasciato l'app che lo ha prodotto.

## Implementazioni

- [Divine](https://github.com/divinevideo/divine-mobile) - client Nostr di video brevi; trasporta i dati di provenienza ProofMode attraverso i download di clip con watermark

---

**Fonti primarie:**
- [ProofMode](https://proofmode.org/)

**Menzionato in:**
- [Newsletter #17](/it/newsletters/2026-04-29-newsletter/)
- [Newsletter #31: Divine Mobile 1.0.16 distribuisce un editor video più avanzato, cifratura at-rest e provenienza ProofMode](/it/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**Vedi anche:**
- [Blossom](/it/topics/blossom/)
