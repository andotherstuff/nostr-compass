---
title: "CLINK: Common Lightning Interface for Nostr Keys"
date: 2026-06-17
draft: false
translationOf: /en/topics/clink.md
translationDate: 2026-07-01
categories:
  - Payments
  - Lightning
---

CLINK (Common Lightning Interface for Nostr Keys) ist ein vorgeschlagenes Zahlungsanforderungsformat, mit dem ein Absender jede Nostr-Schlüssel-Identität über eine einzige noffer-Schnittstelle bezahlen kann. Ein CLINK-noffer kodiert den öffentlichen Nostr-Schlüssel des Empfängers zusammen mit ausreichend Routing-Metadaten, damit die Wallet des Absenders eine Lightning-Zahlung, eine On-Chain-Zahlung oder ein zukünftiges Abrechnungsprimitiv konstruieren kann, das an den Empfänger aufgelöst wird. Der Empfänger veröffentlicht einen noffer pro Identität, und Absender bezahlen ihn, ohne zu wissen, ob die empfangende Wallet über Lightning, On-Chain oder eine andere Schiene abrechnet.

## Wie es funktioniert

Ein CLINK-noffer ist eine strukturierte Zahlungsanforderung, die die Wallet des Absenders in eine konkrete Zahlungsanweisung dekodiert. Der noffer enthält:

- Den öffentlichen Nostr-Schlüssel des Empfängers als kanonische Identitätswurzel
- Einen oder mehrere Zahlungsendpunkte (Lightning-Node-URI, Hinweis zur Ableitung einer On-Chain-Adresse, zukünftige Schienen)
- Optionale Metadaten für die Zahlung (Memo, Betrag, Ablaufdatum)
- Eine Signatur des Empfängers, die den noffer an seine Nostr-Identität bindet

Eine sendende Wallet, die CLINK unterstützt, liest den noffer, wählt die Schiene, die sie bedienen kann (eine reine Lightning-Wallet bezahlt den Lightning-Endpunkt, eine Multi-Schienen-Wallet wählt den günstigsten Pfad), und übermittelt die Zahlung. Die Wallet des Empfängers bestätigt den Empfang, indem sie das entsprechende Abschluss-event veröffentlicht oder abruft, wobei der öffentliche Nostr-Schlüssel als dauerhafte Identität über alle Schienen hinweg fungiert.

## Warum eine Nostr-Schlüssel-Schnittstelle

LNURL und BOLT-12 existieren bereits als Lightning-Zahlungsanforderungsformate, und Bitcoin verfügt über ein bekanntes Adressformat für die On-Chain-Abwicklung. CLINK ersetzt keines von beiden. Es fügt eine an Nostr-Schlüsseln verankerte Schicht hinzu, damit ein Absender einen Empfänger über seine Nostr-Identität adressieren und die Wallet auflösen lassen kann, welche zugrunde liegende Schiene verwendet wird. Ein Nutzer, der den Lightning-Anbieter wechselt, eine neue Mint eröffnet oder seine On-Chain-Wallet migriert, veröffentlicht seinen noffer mit demselben Nostr-Schlüssel erneut, und Absender müssen ihre Adressbücher nicht aktualisieren.

Für Zeus Pay (das für jedes Konto einen CLINK-noffer generiert) bedeutet dies, dass ein Absender jeden Zeus-Nutzer allein über den Nostr-Schlüssel bezahlen kann. Für den On-Chain-zap-Treiber von Amethyst bestätigt die CLINK-Verifikationszustandsmaschine, dass der signierte noffer on chain mit dem in der zap-Anfrage angegebenen Nostr pubkey übereinstimmt, und schließt so einen Fälschungspfad gegen unsignierte On-Chain-zaps.

## Implementierungen

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) liefert Unterstützung für CLINK-noffer-Zahlungen, wobei Zeus Pay für jedes Konto einen CLINK-noffer generiert, sodass ein Absender jeden Zeus-Nutzer allein über den Nostr-Schlüssel bezahlen kann
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) liefert einen CLINK-Treiber für die On-Chain-zap-Verifikation mit einer Verifikationszustandsmaschine und einem Reverify-Treiber ([PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039), [PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177), [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182))

---

**Primärquellen:**
- [Zeus v13.1.0-rc1 Release Notes](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - Auslieferung des CLINK-noffer
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - NIP-BC On-Chain-zaps-Verifikationszustandsmaschine und Reverify-Treiber
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - Implementierung von CLINK (Common Lightning Interface for Nostr Keys)
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - kotlinx-serialization-Unterstützung für CLINK-Protokoll-DTOs hinzugefügt

**Erwähnt in:**
- [Newsletter #27: Amethyst v1.12.0 liefert Cashu-Wallets, nutzaps, einen CLINK-Treiber und Tor-Selbstheilung](/de/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #27: Zeus v13.1.0-rc1 liefert CLINK-noffers und warteschlangenloses NWC](/de/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**Siehe auch:**
- [NIP-57: Zaps](/de/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/de/topics/nip-47/)
