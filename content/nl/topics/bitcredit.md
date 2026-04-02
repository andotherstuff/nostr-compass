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

Bitcredit is een e-bill handelsfinancieringssysteem voor bedrijven. De publieke site presenteert Bitcredit Core als software voor het uitgeven, endosseren, betalen en beheren van elektronische wisselbrieven, terwijl de open-source kernrepository een Nostr-transportlaag implementeert naast de bedrijfslogica- en persistentiecrates.

## Hoe Het Werkt

Bitcredit modelleert handelsfinanciering als elektronische wisselbrieven, ofwel ebills. Een koper geeft een ebill uit met een toekomstige vervaldatum, de houder kan deze endosseren aan een ander bedrijf, en de uiteindelijke houder kan betaling verzoeken bij vervaldatum.

De Bitcredit-site beschrijft ook een mint-gebaseerd liquiditeitspad. In plaats van te wachten op vervaldatum kan een houder een aanbod aanvragen bij een Bitcredit mint, direct ecash ontvangen, en dat ecash vervolgens gebruiken om leveranciers of werknemers te betalen.

## Implementatienotities

De `Bitcredit-Core` repository splitst het systeem in meerdere Rust-crates. `bcr-ebill-core` behandelt het datamodel, `bcr-ebill-api` bevat bedrijfslogica, `bcr-ebill-persistence` regelt opslag, en `bcr-ebill-transport` biedt de netwerktransport-API met een Nostr-implementatie.

Die architectuur is belangrijk omdat Bitcredit niet alleen een website of walletflow is. Het is een bedrijfsdocumentsysteem met transport-, status- en afwikkelingslogica gescheiden in herbruikbare componenten, inclusief een WASM-ingangspunt voor webdeployments.

## Recent Werk

Compass behandelde Bitcredit voor het eerst in maart 2026 toen `v0.5.3` API-velden toevoegde voor factuurbetalingsacties en factuurstatus, en signing-adresafhandeling voor anonieme ondertekenaars repareerde. De volgende release, `v0.5.4`, zette dat API-werk voort door `BitcreditBillResult` aan te passen, betalings- en acceptatiestatus te verfijnen, en meer expliciete afhandeling voor optionele velden toe te voegen.

Die wijzigingen zijn klein vergeleken met het bredere Bitcredit-concept, maar ze tonen waar de implementatie naartoe beweegt: schonere frontend-ergonomie, duidelijkere factureringslevenscyclusstatus, en betere afhandeling voor anonieme of toonderstijl-ondertekeningsflows.

---

**Primaire bronnen:**
- [Bitcredit website](https://www.bit.cr/)
- [Bitcredit: How it works](https://www.bit.cr/how-it-works)
- [Bitcredit-Core repository](https://github.com/BitcreditProtocol/Bitcredit-Core)
- [Bitcredit-Core documentatie-index](https://github.com/BitcreditProtocol/Bitcredit-Core/blob/master/docs/index.md)
- [Bitcredit v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)
- [Bitcredit v0.5.4](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.4)
- [PR #846: Improve Status Flags and Add Payment Actions](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)
- [PR #849: Fix signing address and signatory for anon signers](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)

**Vermeld in:**
- [Newsletter #13: Bitcredit v0.5.3](/en/newsletters/2026-03-11-newsletter/#bitcredit-v053)
