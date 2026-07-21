---
title: "ProofMode"
date: 2026-07-15
draft: false
translationOf: /en/topics/proofmode.md
translationDate: 2026-07-15
categories:
  - Media
  - Provenance
---

[ProofMode](https://proofmode.org/) is een opensource gereedschapskist voor mediaherkomst, gebouwd door Guardian Project, WITNESS en Okthanks, die verifieerbare gegevens over echtheid en beheersketen aan foto's en video hangt op het moment van opname. Het is niet Nostr-specifiek; Nostr-clients die ProofMode-gegevens meedragen, integreren een bestaande externe standaard in plaats van een nieuwe protocollaag.

## Hoe het werkt

De Capture-component van ProofMode sluit herkomstmetadata tijdens de opname direct in mediabestanden in en ondersteunt dezelfde interoperabele standaarden die de Content Authenticity Initiative (CAI), Content Credentials (CR) en C2PA gebruiken. Een aparte Verify-component inspecteert audio-, afbeeldings- en videobestanden om die metadata te controleren op sporen van AI-generatie of latere bewerking, en een Preserve-component regelt redundante opslag op het gedecentraliseerde web van de onderliggende bewijsgegevens voor archivering op lange termijn. Een Develop-SDK laat apps opname en verificatie integreren zonder het herkomstformaat zelf te bouwen.

## Waarom het van belang is

Voor een Nostr-video- of afbeeldingsclient betekent het meedragen van ProofMode-gegevens dat een kijker een externe, platformoverstijgende manier heeft om te controleren of een stuk media is opgenomen zoals beweerd en sindsdien niet stilzwijgend is gewijzigd, zonder de publicerende client of relay als bron van vertrouwen te nemen. Dat onderscheid weegt het zwaarst bij een gedownloade of opnieuw gecodeerde kopie van een clip: herkomstgegevens die de download en elk watermerk dat een client aanbrengt overleven, zijn wat de verklaring nog controleerbaar houdt nadat het bestand de app heeft verlaten die het maakte.

## Implementaties

- [Divine](https://github.com/divinevideo/divine-mobile) - Nostr-client voor korte video's; draagt ProofMode-herkomstgegevens mee door downloads van clips met watermerk

---

**Primaire bronnen:**
- [ProofMode](https://proofmode.org/)

**Genoemd in:**
- [Newsletter #17](/nl/newsletters/2026-04-29-newsletter/)
- [Newsletter #31: Divine Mobile 1.0.16 levert een diepere video-editor, versleuteling in rust en ProofMode-herkomst](/nl/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**Zie ook:**
- [Blossom](/nl/topics/blossom/)
