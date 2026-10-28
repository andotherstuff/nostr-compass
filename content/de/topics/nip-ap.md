---
title: "Buzz NIP-AP: Agenten-Personas"
date: 2026-10-21
translationOf: /en/topics/nip-ap.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

Buzz NIP-AP ist ein Spezifikationsentwurf des Buzz-Projekts außerhalb der akzeptierten NIPs in nostr-protocol/nips.

Er definiert Persona-Events der kind 30175, also adressierbare Definitionen zum Instanziieren eines KI-Agenten, die über einen Klartext-Slug `d` identifiziert werden. Kind 30178 enthält eine Projektion des Team-Katalogs. Implementierende Relays beschränken den Zugriff auf beide kinds: Autoren lesen ihre eigenen Events, und andere Leser sehen ein Event in Abfragen, Live-Zustellung, Suche, Zählungen oder ID-Abfragen nur, wenn es `["shared", "true"]` trägt. Das Teilen eines Teams legt die eingebettete Projektion und die Anweisungen jedes Mitglieds offen, einschließlich der Mitglieder mit nicht geteilten Personas. Die Zugriffssperre steuert den Zugriff, ohne Inhalte zu verschlüsseln; der Relay-Betreiber kann sie weiterhin lesen.

Primärquelle: die [NIP-AP-Spezifikation](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md) im Buzz-Repository.

## Primärquellen

- [Buzz NIP-AP: Agenten-Personas](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## Erwähnt in

- [Newsletter #46 (2026-10-28): buzz](/de/newsletters/2026-10-28-newsletter/#buzz)

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
