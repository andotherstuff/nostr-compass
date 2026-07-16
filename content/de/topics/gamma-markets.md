---
title: "Gamma Markets"
date: 2026-07-15
translationOf: /en/topics/gamma-markets.md
translationDate: 2026-07-15
draft: false
categories:
  - Commerce
  - Marketplace
  - Protocol
---

Gamma Markets ist ein Satz von E-Commerce-Konventionen, die direkt auf [NIP-99](/de/topics/nip-99/) Classified Listings aufbauen. Sie wurden gemeinschaftlich von einer Arbeitsgruppe von Nostr-Marktplatz-Entwicklern entwickelt: den Teams hinter Shopstr, Cypher, Plebeian Market und Conduit Market. Gamma Markets füllt die Versand-, Bestellablauf-, Sammlungs- und Bewertungskonventionen, die NIP-99 selbst nicht definiert.

## Funktionsweise

Gamma Markets fügt fünf Event-Kinds rund um das bestehende kind-`30402`-Listing-Event von NIP-99 hinzu, ohne dessen Form zu ändern:

- **Kind 30405** - Produktsammlungen, die mehrere Listings über `a`-Tags gruppieren
- **Kind 30406** - Versandoptionen mit länderspezifischer Preisgestaltung und optionalen gewichts- oder entfernungsbasierten Kostenregeln
- **Kind 16** - Bestellnachrichten: Erstellung (Typ 1), Zahlungsanforderungen (Typ 2), Statusaktualisierungen (Typ 3) und Versandaktualisierungen (Typ 4)
- **Kind 14** - Allgemeine Kommunikation zwischen Käufer und Händler
- **Kind 17** - Zahlungsbelege
- **Kind 31555** - Produktbewertungen, adressiert an einen bestimmten Verkäufer-pubkey und Listing-`d`-Tag

Die Zahlungspräferenzen eines Händlers werden über ein `payment_preference`-Tag in den kind-`0`-Profilmetadaten deklariert, und Clients entdecken kompatible Apps über [NIP-89](/de/topics/nip-89/)-Anwendungsempfehlungen. Die Bestellkommunikation baut auf [NIP-17](/de/topics/nip-17/) Private Messages auf, ohne ein eigenes Verschlüsselungsschema.

Die zentrale Designentscheidung der Spezifikation ist, dass nichts kaskadiert: Ein Listing, das zu einer Sammlung gehört oder eine Versandoption nutzt, referenziert diese explizit über ein `a`-Tag, anstatt die Einstellungen des übergeordneten Elements automatisch zu erben. Das ist eine bewusste Abkehr vom älteren [NIP-15](/de/topics/nip-15/)-Stall-Modell, bei dem ein Produkt stillschweigend die Währung und Versandtabelle seines Stalls erbte.

### Beispiel: Bestellerstellung (kind 16, Typ 1)

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

## Warum es wichtig ist

NIP-99 allein standardisiert nur das Listing selbst, eine signierte, adressierbare Kleinanzeige. Vor Gamma Markets erfand jeder Client, der echten E-Commerce auf NIP-99 aufbaute, seine eigenen privaten Konventionen für Versand, Checkout und Bewertungen, was bedeutete, dass zwei NIP-99-konforme Clients jeweils ein Listing korrekt darstellen konnten, aber keinen gemeinsamen Weg hatten, eine Bestellung zwischen ihnen abzuschließen. Gamma Markets schließt diese Lücke, ohne das NIP-99-Listing-Format selbst zu verändern, sodass bestehende NIP-99-Listings ohne Änderung gültig bleiben.

## Implementierungen

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr-Marktplatz, eines der vier Projekte, die die Spezifikation verfasst haben
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - Marktplatz-Protokoll, das seinen eigenen Bestellstatus- und Checkout-Ablauf im selben Designraum aufbaut

---

**Primärquellen:**
- [Gamma Markets Spezifikations-Repository](https://github.com/GammaMarkets/market-spec)
- [NIP-99 E-Commerce-Anwendungsfall-Erweiterung, PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - gemergter Link vom kanonischen NIP-99-Dokument zur Gamma-Markets-Spezifikation

**Erwähnt in:**
- [Newsletter #31: NIP Deep Dive: NIP-99 und die Gamma-Markets-Commerce-Erweiterung](/de/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**Siehe auch:**
- [NIP-99: Classified Listings](/de/topics/nip-99/)
- [NIP-15: Nostr Marketplace](/de/topics/nip-15/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
