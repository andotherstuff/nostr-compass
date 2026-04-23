---
title: "NIP-34: Git-samenwerking"
date: 2026-02-04
translationDate: 2026-03-07
translationOf: /en/topics/nip-34.md
draft: false
categories:
  - NIP
  - Development
---

NIP-34 definieert event kinds voor het hosten van git-repositories, patches en issues op Nostr relays. Dit maakt volledig gedecentraliseerde codesamenwerking mogelijk zonder afhankelijkheid van gecentraliseerde hostingplatforms zoals GitHub of GitLab.

## Hoe het werkt

Repositories worden weergegeven als adresseerbare events (kind 30617) met metadata zoals naam, beschrijving en clone-URL's. De eigenaar van de repository publiceert dit event om het project op Nostr te vestigen.

Patches (kind 1617) bevatten `git format-patch`-inhoud die op een repository kan worden toegepast. Bijdragers dienen patches in als events die verwijzen naar de doelrepository. Dit weerspiegelt de e-mailgebaseerde patch-workflow die door projecten zoals de Linux kernel wordt gebruikt.

Issues (kind 1621) werken zoals traditionele issue trackers. Pull requests gebruiken kinds 1618 en 1619, en statusupdates gebruiken 1630 tot en met 1633. Reacties op issues, patches en pull requests gebruiken [NIP-22](/nl/topics/nip-22/) comments.

## Event Kinds

- **30617** - Repository-aankondiging (adresseerbaar)
- **30618** - Repository-statusaankondiging voor branches en tags
- **1617** - Patch-indiening
- **1618** - Pull request
- **1619** - Pull request-update
- **1621** - Issue
- **1630-1633** - Open-, merged/resolved-, closed- en draft-status events

## Waarom het belangrijk is

NIP-34 splitst discovery van transport. De feitelijke repository kan nog steeds op gewone Git-servers staan, maar Nostr events bieden een relay-gedistribueerde laag voor discovery, discussie, patchuitwisseling en statustracking. Daardoor kan een project git-native tooling blijven gebruiken zonder afhankelijk te zijn van de database of API van één forge.

De `r` tag met de vroegste unieke commit is een van de belangrijkste details. Die geeft clients een manier om mirrors en forks te groeperen die dezelfde onderliggende repositorygeschiedenis vertegenwoordigen, iets wat op basis van namen alleen moeilijk af te leiden is.

## Implementatiestatus

- **ngit** - Command-line tool voor het publiceren van repos en patches naar Nostr
- **gitworkshop.dev** - Webinterface voor het bladeren door op Nostr gehoste repositories
- **Notedeck** - Desktopclient met [draft support voor NIP-34-weergave](https://github.com/damus-io/notedeck/pull/1279)

---

**Primaire bronnen:**

- [NIP-34-specificatie](https://github.com/nostr-protocol/nips/blob/master/34.md)

**Vermeld in:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Notedeck voegt een NIP-34-viewer toe
- [Newsletter #9: Notedeck](/en/newsletters/2026-02-11-newsletter/#notedeck)

**Zie ook:**
- [NIP-22: Comments](/nl/topics/nip-22/)
