---
title: "NIP-07: Browser Extension Signer"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 definieert een standaardinterface voor browserextensies om ondertekeningscapaciteiten te bieden aan webgebaseerde Nostr-clients, waarbij privésleutels veilig in de extensie blijven in plaats van blootgesteld te worden aan websites.

## Hoe Het Werkt

Browserextensies injecteren een `window.nostr` object dat webapps kunnen gebruiken:

```javascript
// Publieke sleutel ophalen
const pubkey = await window.nostr.getPublicKey();

// Een event ondertekenen
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Versleutelen (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Ontcijferen (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 methoden (modern, indien ondersteund)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Beveiligingsmodel

- **Sleutelisolatie**: Privésleutels verlaten de extensie nooit
- **Gebruikersgoedkeuring**: Extensies kunnen bij elk ondertekeningsverzoek om bevestiging vragen
- **Domeincontrole**: Extensies kunnen beperken welke sites handtekeningen mogen aanvragen

## Implementaties

Populaire NIP-07 extensies zijn onder andere:
- **Alby** - Lightning wallet met Nostr-ondertekening
- **nos2x** - Lichtgewicht Nostr-ondertekenaar
- **Flamingo** - Feature-rijke Nostr-extensie

## Beperkingen

- Alleen browser (geen mobiele ondersteuning)
- Vereist extensie-installatie
- Elke extensie heeft andere UX voor goedkeuringen

## Alternatieven

- [NIP-46](/nl/topics/nip-46/) - Remote signing via Nostr relays
- [NIP-55](/nl/topics/nip-55/) - Android lokale ondertekenaar

## Gerelateerd

- [NIP-44](/nl/topics/nip-44/) - Moderne encryptie (vervangt NIP-04)
- [NIP-46](/nl/topics/nip-46/) - Remote Signing
