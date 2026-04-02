---
title: "Bitcredit"
date: 2026-03-25
translationOf: /en/topics/bitcredit.md
translationDate: 2026-04-01
draft: false
categories:
  - Finance
  - Commerce
  - Infrastructure
---

Bitcredit ist ein E-Bill-Handelsfinanzsystem für Unternehmen. Die öffentliche Website präsentiert Bitcredit Core als Software zum Ausstellen, Indossieren, Bezahlen und Verwalten elektronischer Wechsel, während das Open-Source-Core-Repository eine Nostr-Transportschicht neben der Geschäftslogik und den Persistenz-Crates implementiert.

## Funktionsweise

Bitcredit modelliert Handelskredite als elektronische Wechsel (E-Bills). Ein Käufer stellt einen E-Bill mit einem zukünftigen Fälligkeitsdatum aus, der Inhaber kann ihn an ein anderes Unternehmen indossieren, und der letzte Inhaber kann bei Fälligkeit die Zahlung anfordern.

Die Bitcredit-Website beschreibt auch einen Mint-basierten Liquiditätspfad. Anstatt auf die Fälligkeit zu warten, kann ein Inhaber ein Angebot von einem Bitcredit-Mint anfordern, sofort Ecash erhalten und dieses dann verwenden, um Lieferanten oder Mitarbeiter zu bezahlen.

## Implementierungshinweise

Das `Bitcredit-Core`-Repository teilt das System in mehrere Rust-Crates auf. `bcr-ebill-core` behandelt das Datenmodell, `bcr-ebill-api` enthält die Geschäftslogik, `bcr-ebill-persistence` übernimmt die Speicherung, und `bcr-ebill-transport` stellt die Netzwerk-Transport-API mit einer Nostr-Implementierung bereit.

Diese Architektur ist wichtig, weil Bitcredit nicht nur eine Website oder ein Wallet-Flow ist. Es ist ein Geschäftsdokumentsystem mit Transport-, Zustands- und Abwicklungslogik, die in wiederverwendbare Komponenten aufgeteilt ist, einschließlich eines WASM-Einstiegspunkts für Web-Deployments.

## Aktuelle Arbeit

Compass berichtete erstmals im März 2026 über Bitcredit, als `v0.5.3` API-Felder für Rechnungszahlungsaktionen und Rechnungsstatus hinzufügte und die Behandlung von Signieradressen für anonyme Unterzeichner korrigierte. Das folgende Release `v0.5.4` setzte diese API-Arbeit fort, indem es `BitcreditBillResult` anpasste, Zahlungs- und Akzeptanzstatus verfeinerte und eine explizitere Behandlung optionaler Felder hinzufügte.

Diese Änderungen sind klein im Vergleich zum breiteren Bitcredit-Konzept, zeigen aber, wohin sich die Implementierung bewegt: sauberere Frontend-Ergonomie, klarerer Rechnungslebenszyklus-Status und bessere Behandlung anonymer oder Inhaber-basierter Signierflows.

---

**Primärquellen:**
- [Bitcredit-Website](https://www.bit.cr/)
- [Bitcredit: How it works](https://www.bit.cr/how-it-works)
- [Bitcredit-Core-Repository](https://github.com/BitcreditProtocol/Bitcredit-Core)
- [Bitcredit-Core-Dokumentationsindex](https://github.com/BitcreditProtocol/Bitcredit-Core/blob/master/docs/index.md)
- [Bitcredit v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)
- [Bitcredit v0.5.4](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.4)
- [PR #846: Improve Status Flags and Add Payment Actions](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)
- [PR #849: Fix signing address and signatory for anon signers](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)

**Erwähnt in:**
- [Newsletter #13: Bitcredit v0.5.3](/en/newsletters/2026-03-11-newsletter/#bitcredit-v053)
