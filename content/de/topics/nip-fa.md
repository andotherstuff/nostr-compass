---
title: "Buzz NIP-FA: Föderierter Identitätsadapter"
date: 2026-10-21
draft: false
categories: ["NIPs"]
translationOf: /en/topics/nip-fa.md
translationDate: 2026-11-05
---

Buzz NIP-FA ist eine optionale Spezifikation des Buzz-Projekts im Entwurfsstadium. Sie gehört nicht zu den akzeptierten NIPs des offiziellen Repositorys nostr-protocol/nips.

Sie definiert einen anbieterneutralen HTTP-Vertrag zwischen einem Nostr-Client und einem Enterprise-Identitätsadapter. Nach einer Anmeldung im Browser hält der Adapter eine Sitzung für den Nutzer. Er stellt projektlokale Buzz-NIP-FI-Assertions aus, die den Nutzer an einen Nostr-Schlüssel binden. Dass der Client diesen Schlüssel kontrolliert, weist er mit [NIP-98](/de/topics/nip-98/) nach. Der [Betreiber wählt die Lebensdauer jeder Assertion](https://github.com/block/buzz/pull/8934). Sie muss das vom Relay akzeptierte maximum_assertion_age des Ausstellers einhalten, und exp darf den Ablauf der Adaptersitzung nicht überschreiten. Die gewählte Lebensdauer begrenzt, wie lange sich ein widerrufener Schlüssel nach einem Neustart des Relays noch erneut verbinden könnte, und Clients dürfen eine Assertion nicht allein wegen ihrer Lebensdauer ablehnen. NIP-FI und die offiziellen NIPs bleiben unverändert. Die Anmeldung verwendet eine S256-Handoff-Challenge und einen Loopback-Callback auf `127.0.0.1` oder `[::1]`, der einen Einmalcode empfängt. Vorgelagerte Systeme wie OIDC oder SAML bleiben hinter dem Adapter. Wie sich ermitteln lässt, welche Relays eine Enterprise-Identität verlangen, bleibt anderen Spezifikationen überlassen.

Primärquelle: die [NIP-FA-Spezifikation](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md) im Buzz-Repository.

## Agenten-Anmeldedaten {#agent-credentials}

Buzz hat einen [NIP-FA-Entwurf für vom Eigentümer autorisierte Agenten-Anmeldedaten](https://github.com/block/buzz/pull/9015) gemergt. Er definiert Routen für Grant, Assertion und Widerruf für Agenten, die ein Eigentümer über NIP-OA autorisiert hat. Ein Grant entsteht aus einem Token-Austausch nach RFC 8693, der die Sitzung des Eigentümers mit einem [NIP-98](/de/topics/nip-98/)-Nachweis des Agenten verknüpft. Für eine Assertion legt der Agent den Grant als Bearer-Token zusammen mit seinem eigenen Nachweis vor, und Clients prüfen das `iss` der Assertion gegen den Aussteller des Grants. Agentennachweise sind nur einmal verwendbar und gehören ausschließlich zu den Grant- und Assertion-Routen. Der Widerruf läuft über die Sitzung des Eigentümers ohne Agentennachweis. Er widerruft den Agentenschlüssel und dessen Grants und trennt die Verbindung des Agenten. Die Richtlinie des Adapters bestimmt die Lebensdauer eines Grants. Nicht unterstützte Autorisierungsbedingungen werden abgelehnt, und ein widerrufener Schlüssel kann sich nicht erneut registrieren. NIP-FA ist eine Buzz-Spezifikation, kein akzeptiertes NIP. Der Merge betrifft nur den Quellcode. Eine Aktivierung in Produktion, ein veröffentlichter Build oder Interoperabilität werden nicht behauptet.

## Primärquellen {#primary-sources}

- [Buzz NIP-FA: Föderierter Identitätsadapter](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)

- [Routen für vom Eigentümer autorisierte Agenten-Anmeldedaten](https://github.com/block/buzz/pull/9015)

## Erwähnt in {#mentioned-in}

- [Newsletter #47: Buzz-Agenten-Anmeldedaten](/de/newsletters/2026-11-04-newsletter/#buzz-defines-owner-authorized-agent-credential-routes)


- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
