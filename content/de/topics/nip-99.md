---
title: "NIP-99: Kleinanzeigen"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 definiert adressierbare Kleinanzeigen-Events für Waren, Dienstleistungen, Jobs, Vermietungen und andere Angebote. Es gibt Marketplace-Apps ein einfacheres Event-Modell als die ältere [NIP-15](/de/topics/nip-15/) Marketplace-Spezifikation, weshalb viele aktuelle Commerce-Clients stattdessen auf NIP-99 aufbauen.

## Wie es funktioniert

Aktive Listings verwenden kind `30402`, während Entwürfe oder inaktive Listings kind `30403` verwenden. Der pubkey des Autors ist der Verkäufer oder Ersteller des Angebots. Das Feld `content` trägt die menschenlesbare Beschreibung in Markdown, und die Tags enthalten strukturierte Felder wie Titel, Zusammenfassung, Preis, Ort und Status.

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

Das Event ist adressierbar, daher kann ein Verkäufer das Listing aktualisieren und dabei dasselbe Identitätstupel aus pubkey, kind und `d`-Tag beibehalten. Das macht Listing-Revisionen für Clients sauberer, als für jede Preis- oder Statusänderung eine brandneue unveränderliche Notiz zu veröffentlichen.

## Warum es wichtig ist

Die Stärke von NIP-99 liegt darin, dass es Raum für verschiedene Marketplace-Designs lässt und dennoch die Kernform eines Listings standardisiert. Ein Client kann sich auf lokale Kleinanzeigen konzentrieren, ein anderer auf Abonnements und ein weiterer auf globale Produktkataloge. Wenn sie sich alle auf dieselbe Event-Struktur einigen, können Verkäufer einmal publizieren und trotzdem eine gewisse Sichtbarkeit über mehrere Clients hinweg erhalten.

Diese Flexibilität erklärt auch, warum aktuelle Marketplace-Projekte es bevorzugen. Die Spezifikation ist strukturiert genug, um Suche und Darstellung zu unterstützen, zwingt aber nicht jede App in denselben Escrow-, Versand- oder Zahlungsablauf.

## Hinweise zur Implementierung

- `price`-Tags können einmalige oder wiederkehrende Zahlungen beschreiben, indem ein optionales Frequenzfeld hinzugefügt wird.
- `t`-Tags dienen als Kategorien oder Suchbegriffe.
- `image`-Tags erlauben Clients das Rendern von Galerieansichten, ohne den Markdown-Body parsen zu müssen.
- Ein Listing kann mit `e`- oder `a`-Tags auf verwandte Events oder Dokumente verweisen, wenn ein Marketplace reichhaltigeren Produktkontext möchte.

## Implementierungen

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr-Marketplace mit NIP-99-Listings und agentenseitigen MCP-Endpunkten
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Lebensmittel-Marketplace auf derselben Listing-Schicht mit gemischten Zahlungsoptionen

---

**Primärquellen:**
- [NIP-99 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - MCP-Commerce-Endpunkte auf Basis von NIP-99-Listings
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Abonnement- und Multi-Merchant-Checkout auf Basis von Marketplace-Listings

**Erwähnt in:**
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/de/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**Siehe auch:**
- [NIP-15: Marketplace Offers](/de/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/de/topics/nip-47/)
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
