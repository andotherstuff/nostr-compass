---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
translationOf: /en/topics/nip-be.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE legt fest, wie Nostr-Anwendungen über Bluetooth Low Energy kommunizieren und synchronisieren können. Dadurch können offline-fähige Apps Daten zwischen nahegelegenen Geräten austauschen, ohne Internetverbindung zu benötigen.

## Funktionsweise

NIP-BE verwendet normale Nostr-Nachrichtenrahmen über BLE weiter, statt ein eigenes Event-Modell zu erfinden. Geräte kündigen einen BLE-Service plus eine Geräte-UUID an, vergleichen ihre UUIDs beim Aufeinandertreffen und entscheiden dann deterministisch, welche Seite zum GATT-Server und welche zum GATT-Client wird.

Der GATT-Service folgt grob dem Aufbau eines Nordic-UART-Dienstes mit einer Write-Characteristic und einer Read- oder Notify-Characteristic. Das hält den Transport einfach genug für eingeschränkte mobile Stacks und kann trotzdem normale Nostr-Nachrichten übertragen.

## Nachrichtenrahmen

BLE hat kleine Payload-Limits, daher komprimiert NIP-BE Nachrichten mit DEFLATE, teilt sie in indizierte Chunks auf und sendet immer nur eine Nachricht gleichzeitig. Die Spezifikation begrenzt Nachrichten auf 64 KB. Das zeigt klar, dass dieser Transport für Synchronisierung und lokale Weitergabe gedacht ist, nicht für große Massenübertragungen.

## Synchronisationsmodell

Nachdem eine Verbindung steht, nutzen Peers einen Half-Duplex-Sync-Flow auf Basis von Negentropy-Nachrichten aus [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md), etwa `NEG-OPEN`, `NEG-MSG`, `EVENT` und `EOSE`. Diese Entscheidung ist wichtig, weil Implementierungen vorhandene Relay-Sync-Logik wiederverwenden können, statt einen nur für BLE gedachten Replikationsalgorithmus zu bauen.

Die Half-Duplex-Regel spiegelt außerdem die Realität instabiler BLE-Verbindungen wider. Kurze, unterbrochene Verbindungen auf kurze Distanz funktionieren besser, wenn jede Seite genau weiß, wann sie an der Reihe ist.

## Warum das wichtig ist

NIP-BE gibt Nostr-Anwendungen einen Weg zu lokalem Networking. Zwei Telefone können Notizen oder Relay-Zustand direkt synchronisieren, wenn sie nah genug beieinander sind, auch wenn keines von beiden funktionierendes Internet hat. Dadurch wird BLE für Zensurresistenz, Katastrophenszenarien und soziale Apps mit schlechter Konnektivität interessant.

Die Grenzen sind genauso wichtig: BLE bietet geringe Bandbreite, Verbindungen sind kurzlebig und große Historien passen schlecht dazu. In der Praxis eignet sich NIP-BE am besten für inkrementelle Synchronisierung und die Verbreitung von Nachrichten in der Nähe, nicht für vollständige Archiv-Replikation.

---

**Primärquellen:**
- [NIP-BE Specification](https://github.com/nostr-protocol/nips/blob/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)

**Erwähnt in:**
- [Newsletter #1: News](/de/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
