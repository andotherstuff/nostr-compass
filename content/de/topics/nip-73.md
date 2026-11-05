---
title: "NIP-73: Externe Inhalts-IDs"
date: 2026-02-04
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
translationOf: /en/topics/nip-73.md
translationDate: 2026-11-05
---

NIP-73 legt ein einheitliches Verfahren fest, mit dem Nostr-Events auf externe Inhalte verweisen. Der Bezeichner selbst steht in `i`-Tags, der Bezeichnertyp in `k`-Tags. So können Clients Diskussionen zum selben Buch, zur selben Website, zur selben Podcast-Episode, zum selben Ort, zum selben Hashtag oder zum selben Blockchain-Objekt bündeln. Die [aktuelle Spezifikation](https://github.com/nostr-protocol/nips/blob/master/73.md) ist als Entwurf (draft) und optional gekennzeichnet.

## Funktionsweise {#how-it-works}

Ein Event, das NIP-73 nutzt, enthält einen `i`-Tag mit einem normalisierten externen Bezeichner und einen `k`-Tag, der die Bezeichnerfamilie benennt. Clients können Relays über `i` nach genau einem Gegenstand oder über `k` nach einer ganzen Familie abfragen. NIP-73 führt keinen eigenen Event-Kind ein. Die Tags stehen in Kommentaren, Rezensionen und anderen Events.

Tag-Fragment, kein vollständiges Event:

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

Bei einer Webseite steht ihre normalisierte URL in `i`, und `k` wird auf `web` gesetzt. Die Spezifikation deckt mehrere Bezeichnerfamilien ab, darunter:

- normalisierte Web-URLs ohne Fragment
- ISBNs für Bücher
- ISANs für Filme
- DOIs
- Geohashes und ISO-3166-Codes für Länder oder Unterteilungen
- GUIDs für Podcast-Feeds, -Episoden und -Herausgeber
- Hashtags
- Bezeichner für Blockchain-Transaktionen und -Adressen

## Normalisierungsregeln {#normalization-rules}

Der Abgleich setzt identische Zeichenketten voraus. Deshalb legt die Spezifikation für jede Familie eine einzige Schreibweise fest. Beispiele aus der Spezifikation:

- Geohashes verwenden `geo:<value>` und müssen kleingeschrieben sein
- Länder- und Unterteilungscodes verwenden `iso3166:<code>` und müssen großgeschrieben sein
- ISBNs werden ohne Bindestriche geschrieben
- DOIs werden kleingeschrieben
- bei Web-URLs entfallen Fragmente
- Blockchain-Transaktionshashes verwenden Hex in Kleinbuchstaben

Die Normalisierung legt fest, wie ein einzelner Bezeichner geschrieben wird. Aliasse führt sie nicht zusammen. Ausgabenspezifische ISBNs und URLs, die zu unterschiedlichen Zeichenketten normalisiert werden, bleiben getrennte Bezeichner. Die Diskussion über ein Buch oder einen Artikel kann sich daher weiterhin auf mehrere `i`-Werte verteilen.

## URL-Hinweise {#url-hints}

Ein `i`-Tag kann als drittes Array-Element einen optionalen URL-Hinweis enthalten. Das ist der zweite Wert nach dem Tag-Namen. Ein Client ohne eigenen Renderer für diesen Bezeichnertyp kann den Hinweis als Ersatzlink verwenden.

Tag-Fragment: `["i", "isbn:9780765382030", "<url-hint>"]`

Den Hinweis wählt der Autor. Er ist nicht Teil der Identität, beweist keine Inhaberschaft und benennt keine kanonische Website.

## Vertrauen und Kontext {#trust-and-context}

Zwei Events mit demselben Bezeichner landen in derselben Unterhaltung. Mehr begründet der gemeinsame Bezeichner nicht. Ein signiertes Event identifiziert seinen Autor. Es authentifiziert weder das Buch noch die Website oder den Podcast-Herausgeber, auf die es verweist, und es zeigt nicht, wer diese kontrolliert.

Was ein `i`-Tag bedeutet, hängt vom Event ab. In Kommentaren nach [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) markieren die großgeschriebenen `I`/`K` den Wurzelbereich und die kleingeschriebenen `i`/`k` das übergeordnete Element. Diese Thread-Struktur stammt aus NIP-22. NIP-73 definiert keinen Kommentar-Kind. [NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) verwendet `i` für externe Identitäten in Profilen. Daher ist nicht jeder `i`-Tag ein NIP-73-Gegenstand.

Auch Trusted Assertions nach [NIP-85](/de/topics/nip-85/) können sich auf NIP-73-Bezeichner beziehen, etwa auf Bücher, Websites, Hashtags und Orte.

## Implementierungen {#implementations}

In rust-nostr parst [nip73.rs im Commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) bekannte Präfixe in eine typisierte `ExternalContentId` und wandelt einen optionalen Hinweis in eine typisierte URL um. Das dritte Tag-Element wird nur geschrieben, wenn ein Hinweis vorhanden ist. Die Tests behalten ISBNs mit Bindestrichen bei: Der Parser entfernt das Präfix und speichert den Rest, ohne die Normalisierung aus der Spezifikation anzuwenden. Typisiertes Parsen garantiert also keine kanonischen Zeichenketten. Chain-IDs werden nicht in die Familie übernommen, sodass `ethereum:100:tx:<hash>` auf `ethereum:tx` abgebildet wird. Diese Revision enthält keine `iso3166`-Variante für Länder.

In Amethyst leitet [DisplayExternalId.kt im Commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) Geohash-, Hashtag- und URL-Bezeichner an eigene Anzeigen weiter und zeigt andere unterstützte Typen als generischen Bereichs-Chip an. Eine URL öffnet die app-eigene Thread-Route für diese Seite. Sind Vorschauen deaktiviert, zeigt die normale Darstellung einen einfachen Link-Chip und fordert keine Vorschau an. Sind Vorschauen aktiviert, kann beim Abrufen einer fehlenden Vorschau die Zielwebsite kontaktiert werden. Keine der beiden Dateien zeigt, wie sich eine veröffentlichte Version verhält.

---

**Primärquellen:**
- [NIP-73-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Ergänzt ISO-3166-Codes für Länder und Unterteilungen
- [rust-nostr nip73.rs im Commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [Amethyst DisplayExternalId.kt im Commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**Erwähnt in:**
- [Newsletter #47: NIP im Detail](/de/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [Newsletter #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [Newsletter #37: August 2025](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [Newsletter #8: NIP-Neuerungen](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: NIP-85 im Detail](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #36: Kommentare (NIP-22)](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [Newsletter #38: NIP im Detail](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [Newsletter #40: NIP-73-Filter für Podcast-Medien](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [Newsletter #42: Externe Inhalte, September 2024](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**Siehe auch:**
- [NIP-31: Umgang mit unbekannten Event-Kinds](/de/topics/nip-31/)
- [NIP-22: Kommentar](/de/topics/nip-22/)
- [NIP-39: Externe Identitäten in Profilen](/de/topics/nip-39/)
- [NIP-85: Vertrauenswürdige Zusicherungen](/de/topics/nip-85/)
