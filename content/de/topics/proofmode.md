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

[ProofMode](https://proofmode.org/) ist ein Open-Source-Toolkit für Medien-Provenienz, entwickelt von Guardian Project, WITNESS und Okthanks, das verifizierbare Authentizitäts- und Chain-of-Custody-Daten an Fotos und Videos im Moment der Aufnahme anfügt. Es ist nicht Nostr-spezifisch; Nostr-Clients, die ProofMode-Daten mitführen, integrieren einen bestehenden externen Standard und keine neue Protokollschicht.

## Funktionsweise

Die Capture-Komponente von ProofMode bettet Provenienz-Metadaten direkt in Mediendateien während der Aufnahme ein und unterstützt dieselben interoperablen Standards, die von der Content Authenticity Initiative (CAI), Content Credentials (CR) und C2PA verwendet werden. Eine separate Verify-Komponente prüft Audio-, Bild- und Videodateien auf Anzeichen von KI-Generierung oder nachträglicher Bearbeitung in diesen Metadaten, und eine Preserve-Komponente übernimmt die redundante, dezentralisierte Web-Speicherung der zugrunde liegenden Nachweisdaten für die Langzeitarchivierung. Ein Develop SDK ermöglicht es Apps, Aufnahme und Verifikation zu integrieren, ohne das Provenienzformat selbst aufzubauen.

## Warum es wichtig ist

Für einen Nostr-Video- oder -Bild-Client bedeutet das Mitführen von ProofMode-Daten, dass ein Betrachter eine externe, plattformübergreifende Möglichkeit hat zu prüfen, ob ein Medienstück wie behauptet aufgenommen wurde und seitdem nicht stillschweigend verändert wurde, ohne sich auf den veröffentlichenden Client oder Relay als Vertrauensquelle zu verlassen. Diese Unterscheidung ist am wichtigsten für eine heruntergeladene oder neu kodierte Kopie eines Clips: Provenienzdaten, die den Download und etwaiges Wasserzeichen überleben, das ein Client anwendet, machen die Attestierung auch noch überprüfbar, nachdem die Datei die App verlassen hat, die sie erzeugt hat.

## Implementierungen

- [Divine](https://github.com/divinevideo/divine-mobile) - Kurzvideo-Nostr-Client; führt ProofMode-Provenienzdaten durch wasserzeichenmarkierte Clip-Downloads

---

**Primärquellen:**
- [ProofMode](https://proofmode.org/)

**Erwähnt in:**
- [Newsletter #17](/de/newsletters/2026-04-29-newsletter/)
- [Newsletter #31: Divine Mobile 1.0.16 ships a deeper video editor, at-rest encryption, and ProofMode provenance](/de/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**Siehe auch:**
- [Blossom](/de/topics/blossom/)
