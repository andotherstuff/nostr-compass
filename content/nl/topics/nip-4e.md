---
title: "NIP-4E: Versleuteling loskoppelen van identiteit"
date: 2026-07-15
draft: false
translationOf: /en/topics/nip-4e.md
translationDate: 2026-07-15
categories:
  - NIP
  - Protocol
  - Encryption
---

NIP-4E is een open concept, voorgesteld door fiatjaf, voor het delen van privégegevens tussen de eigen apparaten van een gebruiker zonder dat elk apparaat de belangrijkste Nostr-identiteitssleutel van die gebruiker bezit. Het is niet samengevoegd en blijft een `draft`/`optional` voorstel.

## Het probleem dat het aanpakt

Veel bestaande NIPs, waaronder NIP-51-lijsten en NIP-60 Cashu-wallets, versleutelen gegevens van een gebruiker naar zichzelf met de identiteitssleutel zodat die later op elk apparaat weer te lezen zijn. Dat loopt spaak wanneer de identiteitssleutel niet direct toegankelijk is, bijvoorbeeld wanneer een externe ondertekenaar wordt beschermd door FROST-drempeldelen, MuSig2 of een gehoste beveiligde enclave, omdat versleutelen en ontsleutelen dan elke keer een rondgang naar die ondertekenaar vereist. Het maakt offline versleuteling ook onmogelijk zodra de ondertekeningssleutel in een externe bunker leeft.

## Hoe het werkt

NIP-4E scheidt een "clientsleutel" per apparaat van een gedeelde "versleutelingssleutel" die niet de identiteitssleutel van de gebruiker is:

1. De eerste client die een gebruiker opzet, genereert een willekeurig versleutelingssleutelpaar en kondigt de publieke helft ervan aan in een `kind:10044`-event dat met de identiteitssleutel van de gebruiker is ondertekend.
2. Elke andere client die gegevens voor die gebruiker wil versleutelen of ontsleutelen, berekent zijn Diffie-Hellman gedeelde geheim tegen de aangekondigde versleutelingssleutel in plaats van tegen de identiteitssleutel.
3. Wanneer een tweede apparaat een nieuwe client installeert, genereert die client zijn eigen lokale "clientsleutel" en publiceert een `kind:4454`-aankondiging (ook ondertekend met de identiteitssleutel van de gebruiker) die de eerste client vraagt de versleutelingssleutel met hem te delen.
4. De oorspronkelijke client detecteert de nieuwe `kind:4454`-aankondiging, versleutelt de gedeelde versleutelingssleutel naar de sleutel van de nieuwe client met [NIP-44](/nl/topics/nip-44/), en publiceert die zodat de nieuwe client hem voortaan kan ontsleutelen en gebruiken.

Het resultaat is dat versleutelen en ontsleutelen nooit meer iets aan de ondertekenaar van de identiteitssleutel hoeven te vragen zodra een client de gedeelde versleutelingssleutel lokaal heeft, en dat een opzet met een externe ondertekenaar (FROST, MuSig2, gehoste enclave) voor identiteit kan worden gebruikt terwijl gewone versleuteling snel blijft en offline werkt.

## Waarom het van belang is

NIP-4E wordt aangehaald als de basis voor andere voorstellen die een schijfbrede of accountbrede symmetrische sleutel nodig hebben zonder voor elke versleutel/ontsleutel-aanroep van een externe ondertekenaar af te hangen, waaronder een voorstel voor een privé versleutelde schijf ([PR #2412](https://github.com/nostr-protocol/nips/pull/2412)) en een smallere, NIP-17-specifieke versie van hetzelfde idee ([PR #2361](https://github.com/nostr-protocol/nips/pull/2361)). Beide blijven open naast NIP-4E zelf, waarmee dit een actief, onbeslecht gebied van het protocol is in plaats van een afgerond bouwblok.

---

**Primaire bronnen:**
- [NIP-4E-concept, PR #1647](https://github.com/nostr-protocol/nips/pull/1647)

**Genoemd in:**
- [Newsletter #31: Open: privé versleutelde schijf breidt NIP-4E uit](/nl/newsletters/2026-07-15-newsletter/#open-private-encrypted-drive-extends-nip-4e)

**Zie ook:**
- [NIP-44: Encrypted Payloads](/nl/topics/nip-44/)
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
- [NIP-46: Nostr Connect](/nl/topics/nip-46/)
- [FROST](/nl/topics/frost/)
