---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-03-11
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 definieert remote signing via Nostr-relays. Een client praat met een aparte signer, vaak een bunker genoemd, zodat signing keys buiten de app kunnen blijven die de gebruiker actief gebruikt.

## Hoe Het Werkt

1. De client genereert een lokaal keypair dat alleen voor de bunkersessie wordt gebruikt.
2. De verbinding wordt opgezet met een `bunker://`- of `nostrconnect://`-URI.
3. Client en signer wisselen versleutelde kind `24133` request- en response-events uit via relays.
4. Na het verbinden roept de client `get_public_key` aan om de werkelijke user pubkey op te halen waarvoor wordt getekend.

## Verbindingsmethoden

- **bunker://** - Door de signer gestarte verbinding
- **nostrconnect://** - Door de client gestarte verbinding via QR-code of deep link

`nostrconnect://`-flows bevatten een vereiste shared secret zodat de client kan verifiëren dat de eerste response echt van de bedoelde signer kwam. Dat voorkomt eenvoudige connection spoofing.

## Ondersteunde Bewerkingen

- `sign_event` - Een willekeurig event ondertekenen
- `get_public_key` - De pubkey van de gebruiker ophalen bij de signer
- `nip04_encrypt/decrypt` - NIP-04-encryptiebewerkingen
- `nip44_encrypt/decrypt` - NIP-44-encryptiebewerkingen
- `switch_relays` - De signer vragen om een bijgewerkte relay-set

Veel implementaties gebruiken tijdens het opzetten ook permission strings zoals `sign_event:1` of `nip44_encrypt`, zodat de signer een beperkte scope kan goedkeuren in plaats van volledige toegang.

## Relay- en Vertrouwensmodel

NIP-46 verplaatst private keys uit de client, maar haalt vertrouwen niet weg bij de signer. De signer kan requests goedkeuren, weigeren of vertragen, en ziet elke bewerking die de client vraagt uit te voeren. Ook de relay-keuze is belangrijk, omdat het protocol afhangt van request- en response-delivery via relays die beide kanten kunnen bereiken.

De methode `switch_relays` bestaat zodat de signer de sessie na verloop van tijd naar een andere relay-set kan verplaatsen. Clients die die methode negeren, werken minder betrouwbaar wanneer de relay-voorkeuren van de signer veranderen.

---

**Primaire bronnen:**
- [NIP-46-specificatie](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Vermeld in:**
- [Nieuwsbrief #1: Opvallende codewijzigingen](/nl/newsletters/2025-12-17-newsletter/#amethyst-android)
- [Nieuwsbrief #3: Decemberoverzicht](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Nieuwsbrief #7: Primal Android wordt een volledige signing hub](/nl/newsletters/2026-01-07-newsletter/#primal-android-becomes-a-full-signing-hub)
- [Nieuwsbrief #15: NDK collaborative events en NIP-46-time-out](/nl/newsletters/2026-03-04-newsletter/#ndk-collaborative-events-and-nip-46-timeout)

**Zie ook:**
- [NIP-55: Android Signer](/nl/topics/nip-55/)
