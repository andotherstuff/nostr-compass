---
title: "Buzz NIP-FA: Gefedereerde identiteitsadapter"
date: 2026-10-21
draft: false
categories: ["NIPs"]
translationOf: /en/topics/nip-fa.md
translationDate: 2026-11-05
---

Buzz NIP-FA is een optionele conceptspecificatie van het Buzz-project. Ze valt buiten de geaccepteerde NIPs van de officiële nostr-protocol/nips-repository.

Ze definieert een providerneutraal HTTP-contract tussen een Nostr-client en een zakelijke identiteitsadapter. Na een login in de browser houdt de adapter een sessie voor de gebruiker bij. De adapter geeft projectlokale Buzz NIP-FI-asserties uit die de gebruiker aan een Nostr-sleutel koppelen. De client bewijst met [NIP-98](/nl/topics/nip-98/) dat hij die sleutel beheert. De [operator kiest de levensduur van elke assertie](https://github.com/block/buzz/pull/8934). Die levensduur moet binnen de maximum_assertion_age van de uitgever blijven die de relay accepteert, en exp mag niet later liggen dan het verlopen van de adaptersessie. De gekozen levensduur bepaalt hoe lang een ingetrokken sleutel na een herstart van de relay nog opnieuw verbinding zou kunnen maken. Clients mogen een assertie niet uitsluitend vanwege de levensduur weigeren. NIP-FI en de officiële NIPs blijven ongewijzigd. Bij het inloggen worden een S256-overdrachtschallenge en een loopback-callback op `127.0.0.1` of `[::1]` gebruikt, die een eenmalige code ontvangt. Upstream-systemen zoals OIDC of SAML blijven achter de adapter. Hoe je vindt welke relays een zakelijke identiteit vereisen, wordt aan andere specificaties overgelaten.

Primaire bron: de [NIP-FA-specificatie](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md) in de Buzz-repository.

## Agentcredentials {#agent-credentials}

Buzz heeft een [NIP-FA-concept voor door de eigenaar geautoriseerde agentcredentials](https://github.com/block/buzz/pull/9015) gemerged. Het concept definieert toekennings-, assertie- en intrekkingsroutes voor agents die een eigenaar via NIP-OA heeft geautoriseerd. Een toekenning komt voort uit een RFC 8693-tokenuitwisseling die de sessie van de eigenaar koppelt aan een [NIP-98](/nl/topics/nip-98/)-bewijs van de agent. Om een assertie te krijgen, presenteert de agent de toekenning als Bearer-token samen met zijn eigen bewijs. Clients controleren de `iss` van de assertie tegen de uitgever van de toekenning. Agentbewijzen zijn eenmalig en horen uitsluitend bij de toekennings- en assertieroutes. Intrekking verloopt via de sessie van de eigenaar, zonder agentbewijs. Ze trekt de agentsleutel en de bijbehorende toekenningen in en verbreekt de verbinding van de agent. Het adapterbeleid bepaalt hoe lang een toekenning geldig is. Niet-ondersteunde autorisatievoorwaarden worden geweigerd, en een ingetrokken sleutel kan zich niet opnieuw inschrijven. NIP-FA is een Buzz-specificatie en geen geaccepteerde NIP. De merge bestaat alleen in de broncode. Er wordt niet beweerd dat de functie in productie actief is, in een uitgebrachte build zit of interoperabel is.

## Primaire bronnen {#primary-sources}

- [Buzz NIP-FA: Gefedereerde identiteitsadapter](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)

- [Routes voor door de eigenaar geautoriseerde agentcredentials](https://github.com/block/buzz/pull/9015)

## Vermeld in {#mentioned-in}

- [Nieuwsbrief #47: Buzz-agentcredentials](/nl/newsletters/2026-11-04-newsletter/#buzz-defines-owner-authorized-agent-credential-routes)


- [Nieuwsbrief 45](/en/newsletters/2026-10-21-newsletter/#buzz)
