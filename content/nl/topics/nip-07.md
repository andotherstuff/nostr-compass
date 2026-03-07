---
title: "NIP-07: Browser Extension Signer"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 definieert een standaardinterface waarmee browserextensies signing-mogelijkheden kunnen bieden aan webgebaseerde Nostr-clients, zodat private keys in de extensie blijven in plaats van aan websites blootgesteld te worden.

## Hoe het werkt

Browserextensies injecteren een `window.nostr` object dat webapps kunnen gebruiken:

```javascript
// Get public key
const pubkey = await window.nostr.getPublicKey();

// Sign an event
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Encrypt (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Decrypt (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 methods (modern, if supported)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Beveiligingsmodel

- **Sleutelisolatie**: Private keys verlaten de extensie nooit
- **Goedkeuring door de gebruiker**: Extensies kunnen voor elk signing-verzoek om bevestiging vragen
- **Domeincontrole**: Extensies kunnen beperken welke sites signatures mogen aanvragen

NIP-07 verbetert key custody, maar neemt het vertrouwen in de extensie zelf niet weg. Een kwaadaardige of gecompromitteerde extensie kan nog steeds het verkeerde signeren, metadata lekken of permissies te ruim toekennen.

## Interop-opmerkingen

Het lastigste deel van NIP-07 is niet de vorm van de API. Het is de variatie in capabilities. Sommige extensies ondersteunen alleen `getPublicKey()` en `signEvent()`. Andere bieden ook `nip04`, `nip44` of nieuwere optionele methoden aan. Webapps hebben feature detection en redelijke fallbacks nodig, in plaats van ervan uit te gaan dat elke injected signer zich hetzelfde gedraagt.

De UX rond gebruikersgoedkeuring verandert ook het gedrag. Een site die stilletjes toegang op de achtergrond verwacht, werkt misschien met de ene extensie en voelt kapot aan met een andere die bij elk verzoek om bevestiging vraagt. Goede NIP-07 apps behandelen signing als een interactieve permissiegrens.

## Implementatiestatus

Populaire NIP-07 extensies zijn onder meer:
- **Alby** - Lightning wallet met Nostr-signing
- **nos2x** - Lichtgewicht Nostr-signer
- **Flamingo** - Nostr-extensie met veel functies

## Beperkingen

- Alleen browser, geen mobiele ondersteuning
- Vereist installatie van een extensie
- Elke extensie heeft een andere UX voor goedkeuringen

Voor signing tussen apparaten of op mobiel passen NIP-46 en NIP-55 meestal beter.

---

**Primaire bronnen:**
- [NIP-07-specificatie](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - `peekPublicKey()`-voorstel

**Vermeld in:**
- [Nieuwsbrief #7: NIP-updates](/en/newsletters/2026-01-28-newsletter/#nip-updates)
- [Nieuwsbrief #8: Nieuws](/en/newsletters/2026-02-04-newsletter/#news)
- [Nieuwsbrief #11: Nieuws](/en/newsletters/2026-02-25-newsletter/#news)

**Zie ook:**
- [NIP-04: Encrypted Direct Messages (verouderd)](/nl/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/nl/topics/nip-44/)
- [NIP-46: Nostr Connect](/nl/topics/nip-46/)
- [NIP-55: Android Signer Applications](/nl/topics/nip-55/)
