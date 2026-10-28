---
title: 'Buzz-Entwurf NIP-OA: Eigentümer-Attestierung'
date: 2026-10-28
translationOf: /en/topics/nip-oa.md
translationDate: 2026-10-28
draft: false
---

**Status:** Dies ist ein Entwurfsvorschlag speziell für das Buzz-Projekt. NIP-OA ist kein akzeptierter offizieller NIP. Die Bezeichnung stammt aus der Dokumentation des Buzz-Projekts, und das offizielle NIPs-Repository hat sie weder vergeben noch genehmigt.

## Zweck

NIP-OA definiert ein optionales `auth`-Tag, mit dem ein Eigentümerschlüssel einen Agentenschlüssel zur Veröffentlichung von Events autorisieren kann. Der Agentenschlüssel bleibt der Autor des Events. Ein gültiges Tag gilt nur als Nachweis der Autorisierung und erlaubt es dem Agenten nicht, sich als Eigentümer auszugeben.

## Mechanismus

Der Eigentümer signiert mit einer Schnorr-Signatur einen domänengetrennten Hash, der den pubkey des Agenten an eine exakte Bedingungszeichenkette bindet. Bedingungen können eine bestimmte Event-kind verlangen und Grenzen für den selbst deklarierten Wert `created_at` festlegen. Der Agent kann das Tag in seinen Events wiederverwenden, solange jedes Event die Bedingungen erfüllt. Verifizierer validieren zuerst das Kern-Event und prüfen dann die Signatur des Eigentümers sowie jede einzelne Bedingung.

## Grenzen

Eine leere Bedingungszeichenkette fügt keine Einschränkungen hinzu. Zeitstempel-Klauseln beschränken ein Feld, das der Agent kontrolliert, und bieten daher keinen Ablauf nach realer Uhrzeit. Wer Aktualität benötigt, muss sie separat prüfen. Die öffentliche Veröffentlichung des Tags verknüpft die Schlüssel von Eigentümer und Agent.

## Primärquellen

- [Buzz-Entwurf NIP-OA: Eigentümer-Attestierung (fixierte Revision)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-OA.md)

## Siehe auch

- [NIP-01](/de/topics/nip-01/)

**Erwähnt in:**

- [Newsletter #46: Buzz](/de/newsletters/2026-10-28-newsletter/#buzz)
