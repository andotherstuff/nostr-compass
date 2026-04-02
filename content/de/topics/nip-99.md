---
title: "NIP-99: Classified Listings"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 definiert adressierbare Kleinanzeigen-Events für Waren, Dienstleistungen, Jobs, Vermietungen und andere Angebote. Es gibt Marktplatz-Apps ein einfacheres Event-Modell als die ältere [NIP-15](/de/topics/nip-15/) Marktplatz-Spezifikation, weshalb viele aktuelle Commerce-Clients auf NIP-99 aufbauen.

## Funktionsweise

Aktive Angebote verwenden Kind `30402`, während Entwürfe oder inaktive Angebote Kind `30403` verwenden. Der Autor-Pubkey ist der Verkäufer oder Angebotsersteller. Das `content`-Feld trägt die menschenlesbare Beschreibung in Markdown, und die Tags enthalten strukturierte Felder wie Titel, Zusammenfassung, Preis, Standort und Status.

```json
{
  "id": "b3e392b11f5d4f28321cedd09303a748acfd0487aea5a7450b3481c60b6e4f87",
  "pubkey": "a695f6b60119d9521934a691347d9f78e8770b56da16bb255ee286ddf9fda919",
  "created_at": 1741699200,
  "kind": 30402,
  "tags": [
    ["d", "shopstr-handmade-wallet-001"],
    ["title", "Handmade leather wallet"],
    ["summary", "Brown bifold wallet with Bitcoin and Nostr branding"],
    ["published_at", "1741699200"],
    ["location", "Austin, TX"],
    ["price", "75000", "SAT"],
    ["status", "active"],
    ["t", "merch"],
    ["t", "bitcoin"]
  ],
  "content": "Full listing description in Markdown, shipping details, and contact terms.",
  "sig": "4a5c7e8f9012ab34cd56ef7890ab12cd34ef56ab78cd90ef12ab34cd56ef78900112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Das Event ist adressierbar, sodass ein Verkäufer das Angebot aktualisieren kann, während das gleiche Identitätstupel aus Pubkey, Kind und `d`-Tag beibehalten wird. Das macht Angebots-Revisionen für Clients sauberer, als für jede Preis- oder Statusänderung eine komplett neue unveränderliche Notiz zu veröffentlichen.

## Warum das wichtig ist

Die Stärke von NIP-99 liegt darin, dass es Raum für verschiedene Marktplatz-Designs lässt und gleichzeitig die grundlegende Angebotsstruktur standardisiert. Ein Client kann sich auf lokale Kleinanzeigen konzentrieren, ein anderer auf Abonnements und ein dritter auf globale Produktkataloge. Wenn sie sich alle auf die Event-Struktur einigen, können Verkäufer einmal veröffentlichen und trotzdem eine gewisse client-übergreifende Sichtbarkeit erhalten.

Diese Flexibilität erklärt auch, warum aktuelle Marktplatz-Projekte es bevorzugen. Die Spezifikation ist strukturiert genug für Suche und Anzeige, zwingt aber nicht jede App in einen einzigen Treuhand-, Versand- oder Zahlungsworkflow.

## Implementierungshinweise

- `price`-Tags können einmalige oder wiederkehrende Zahlungen beschreiben, indem ein optionales Frequenzfeld hinzugefügt wird.
- `t`-Tags fungieren als Kategorien oder Suchbegriffe.
- `image`-Tags erlauben Clients, Galerieansichten zu rendern, ohne den Markdown-Körper zu parsen.
- Ein Angebot kann mit `e`- oder `a`-Tags auf verwandte Events oder Dokumente verlinken, wenn ein Marktplatz reichhaltigeren Produktkontext benötigt.

## Implementierungen

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr-Marktplatz mit NIP-99-Angeboten und agenten-freundlichen MCP-Endpunkten
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Lebensmittel-Marktplatz, der auf derselben Angebotsschicht aufbaut, mit gemischten Zahlungsoptionen

---

**Primärquellen:**
- [NIP-99-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - MCP-Commerce-Endpunkte auf Basis von NIP-99-Angeboten
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Abonnement und Multi-Händler-Checkout auf Basis von Marktplatz-Angeboten

**Erwähnt in:**
- [Newsletter #13: Shopstr und Milk Market eröffnen MCP-Commerce-Oberflächen](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**Siehe auch:**
- [NIP-15: Marketplace Offers](/de/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/de/topics/nip-47/)
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
