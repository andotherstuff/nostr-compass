---
title: "NIP-34 (Git-samenwerking)"
date: 2026-02-04
description: "NIP-34 maakt gedecentraliseerde git-repository hosting en samenwerking mogelijk via Nostr events."
---

NIP-34 definieert event kinds voor het hosten van git-repositories, patches en issues op Nostr relays. Dit maakt volledig gedecentraliseerde codesamenwerking mogelijk zonder afhankelijkheid van gecentraliseerde hostingplatforms zoals GitHub of GitLab.

## Hoe Het Werkt

Repositories worden gerepresenteerd als adresseerbare events (kind 30617) met metadata zoals naam, beschrijving en clone-URL's. De repository-eigenaar publiceert dit event om het project op Nostr te vestigen.

Patches (kind 1617) bevatten git-patch-inhoud die kan worden toegepast op een repository. Bijdragers dienen patches in als events die verwijzen naar de doelrepository. Dit weerspiegelt de e-mail-gebaseerde patch-workflow gebruikt door projecten zoals de Linux kernel.

Issues (kind 1621) functioneren als traditionele issue trackers. Ze verwijzen naar een repository en bevatten een titel en beschrijving. Reacties op issues en patches gebruiken standaard reply events.

## Event Kinds

- **30617** - Repository-aankondiging (adresseerbaar)
- **1617** - Patch-indiening
- **1621** - Issue
- **1622** - Issue-status (open/gesloten)

## Implementaties

- **ngit** - Command-line tool voor het publiceren van repos en patches naar Nostr
- **gitworkshop.dev** - Webinterface voor het browsen van Nostr-gehoste repositories
- **Notedeck** - Desktopclient met [concept-ondersteuning voor NIP-34 weergave](https://github.com/damus-io/notedeck/pull/1279)

## Primaire Bronnen

- [NIP-34 Specificatie](https://github.com/nostr-protocol/nips/blob/master/34.md)

## Vermeld In

- [Nieuwsbrief #8 (2026-02-04)](/nl/newsletters/2026-02-04-newsletter/) - Notedeck voegt NIP-34 viewer toe
