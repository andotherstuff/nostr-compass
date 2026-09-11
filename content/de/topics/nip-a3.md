---
title: "NIP-A3: Zahlungsziele"
date: 2026-09-09
translationOf: /en/topics/nip-a3.md
translationDate: 2026-09-11
draft: false
categories:
  - Protocol
  - Payments
---

NIP-A3 definiert eine portable Möglichkeit für ein Nostr-Konto, Zahlungsadressen für mehrere Netzwerke und Dienste zu veröffentlichen. Ein austauschbares Event der Art `10133` trägt ein oder mehrere `payto`-Tags.

## Funktionsweise

Jedes Tag hat die Form `["payto", "<type>", "<address>"]`. Der Typ wird kleingeschrieben, zum Beispiel `bitcoin`, `lightning` oder `monero`. Clients können bekannte Formate validieren und, sofern vorhanden, eine native Zahlungs-URI darstellen; unbekannte Typen greifen auf das `payto:`-URI-Schema aus RFC 8905 zurück.

Das Event deklariert Ziele, keine abgeschlossene Zahlung und keinen Nostr-Zap. Clients entscheiden weiterhin selbst, welche Zahlungstypen sie unterstützen, wie sie eine Adresse validieren und wie deutlich sie das Ziel anzeigen, bevor sie es an ein Wallet übergeben.

## Implementierungen

- [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041) bietet eine optionale Zahlungsübergabe an, wenn ein kompatibles Ziel erkannt wird.
- [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) bildet erlaubte Zieltypen auf Zahlungs-URIs ab.
- [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) validiert Monero-Ziele und fragt die Relays des Autors ab.

---

**Primärquellen:**
- [NIP-A3-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905: Das payto-URI-Schema](https://www.rfc-editor.org/rfc/rfc8905.html)

**Erwähnt in:**
- [Newsletter Nr. 39: NIP-A3-Zahlungsziele erreichen drei Clients](/de/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**Siehe auch:**
- [NIP-47: Nostr Wallet Connect](/de/topics/nip-47/)
