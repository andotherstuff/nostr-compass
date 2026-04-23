---
title: "TollGate: Pay-per-use Internet Over Nostr and Cashu"
date: 2026-04-22
translationOf: /en/topics/tollgate.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocols
---

TollGate ist ein Protokoll, um Netzwerkzugang gegen kleine, häufige Zahlungen mit Bearer-Assets zu verkaufen. Ein Gerät, das Konnektivität kontrollieren kann, etwa ein WiFi-Router, ein Ethernet-Switch oder ein Bluetooth-Tether, agiert als TollGate, bewirbt Preise, akzeptiert [Cashu](/de/topics/cashu/) ecash-Tokens und verwaltet Sessions. Kunden bezahlen exakt die Minuten oder Megabytes, die sie verbrauchen. Es gibt keine Accounts, keine Subscriptions und kein KYC.

## Funktionsweise

TollGate trennt die Verantwortlichkeiten in drei Schichten. Die Protocol Layer definiert Event-Formen und Payment-Semantik. Die Interface Layer definiert, wie Kunde und Gate diese Events austauschen. Die Medium Layer beschreibt den physischen Link, über den der bezahlte Traffic läuft. Ein funktionierendes TollGate kombiniert je eine Spezifikation aus jeder Schicht, und einige Interfaces laufen über Nostr-Relays, andere über plain HTTP.

Auf der Protocol Layer definiert [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) drei Basis-Events: ein Advertisement-Kind, das Preise und akzeptierte Mints auflistet, ein Session-Kind, das verfolgt, wie viel der Kunde bezahlt und verbraucht hat, und ein Notice-Kind für Out-of-Band-Messaging. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) legt Cashu-Zahlungen darüber, sodass ein Kunde ecash-Tokens von jedem Mint einlösen kann, den das TollGate bewirbt, und dafür Session-Guthaben erhält.

Auf der Interface Layer definieren [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) bis HTTP-03 die HTTP-Oberfläche für Geräte auf restriktiven Betriebssystemen, die nicht leicht WebSocket-Verbindungen zu beliebigen Relays öffnen können, und [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) definiert den Nostr-Relay-Transport für Clients, die das können. Auf der Medium Layer beschreibt [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md), wie ein Captive-Portal-WiFi-Setup zahlende Kunden identifiziert und routet.

Weil das Payment-Asset ein Bearer-Token und kein Credential ist, benötigt der Kunde keinen vorherigen Internetzugang, um es zu erzeugen. Ein Cashu-Token in einer lokalen Wallet reicht aus, um die erste Minute Konnektivität zu kaufen. Danach kann der Kunde bei Bedarf mit weiteren Tokens aufladen. TollGates können außerdem selbst Uplink voneinander kaufen, sodass die Reichweite über einen einzelnen Betreiber hinausgeht.

## Warum das wichtig ist

Konventionelles Bezahl-WiFi beruht auf Accounts, Captive Portals und Zahlungskarten, die jeweils Reibung und Datenspuren erzeugen. Das Modell von TollGate macht Konnektivität zu einer Ware, die jeder Router an jeden zahlenden Kunden verkaufen kann, ohne zu wissen, wer dieser ist. Die Abstraktion erlaubt unabhängigen Betreibern, eigene Preise zu setzen, eigene bevorzugte Mints zu akzeptieren und über Reichweite und Qualität zu konkurrieren statt über Lock-in.

Der [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) ist der erste getaggte Snapshot dieser Spezifikationen. Er standardisiert noch nicht jedes Detail, fixiert aber genug der Oberfläche, damit Router-Firmware, Client-Wallets und Multi-Hop-Reseller gegen eine stabile Referenz bauen können.

---

**Primärquellen:**
- [TollGate v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01: Base Events](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02: Cashu payments](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 through HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [TollGate repository](https://github.com/OpenTollGate/tollgate)

**Erwähnt in:**
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [Cashu](/de/topics/cashu/)
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
