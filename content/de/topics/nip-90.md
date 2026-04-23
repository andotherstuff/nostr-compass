---
title: "NIP-90: Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 definiert Data Vending Machines, DVMs, ein Protokoll, um bezahlte Rechenarbeit über Nostr anzufragen und auszuliefern.

## Funktionsweise

Kunden veröffentlichen Job-Request-Events im Bereich `5000-5999`. Jeder Request kann ein oder mehrere `i`-Tags für Eingaben, `param`-Tags für jobspezifische Einstellungen, ein `output`-Tag für das erwartete Format, eine `bid`-Obergrenze und Relay-Hints dafür enthalten, wo Replies erscheinen sollen. Service Provider antworten mit einem passenden Result-kind im Bereich `6000-6999`, immer `1000` höher als der Request-kind.

Results enthalten den ursprünglichen Request, den pubkey des Kunden und optional ein `amount`-Tag oder eine Invoice. Provider können außerdem kind-`7000`-Feedback-Events wie `payment-required`, `processing`, `partial`, `error` oder `success` senden. Dadurch können Clients Fortschritt anzeigen, bevor das endgültige Ergebnis ankommt.

## Zahlung und Privatsphäre

Das Protokoll lässt die Geschäftslogik bewusst offen. Ein Provider kann Zahlung verlangen, bevor die Arbeit beginnt, nach Rückgabe eines Samples oder erst nach Lieferung des vollständigen Ergebnisses. Diese Flexibilität ist wichtig, weil DVM-Jobs von günstigen Texttransformationen bis zu teurer GPU-Arbeit reichen und Provider nicht alle dasselbe Zahlungsrisiko tragen.

Wenn ein Kunde private Inputs will, kann er `i`- und `param`-Daten in verschlüsselten `content` verschieben und das Event mit einem `encrypted`-Tag plus dem `p`-Tag des Providers markieren. Das schützt Prompts oder Quellmaterial vor Relay-Beobachtern, bedeutet aber auch, dass der Kunde einen bestimmten Provider ansprechen muss, statt einen offenen Markt-Request zu broadcasten.

## Interop-Hinweise

NIP-90 unterstützt Job-Chaining über `i`-Tags mit dem Input-Typ `job`, sodass ein Result in einen späteren Request einfließen kann. Dadurch werden mehrstufige Abläufe möglich, ohne eine separate Orchestrierungsschicht zu erfinden.

Die Discovery von Providern liegt außerhalb des eigentlichen Request-Response-Zyklus. Die Spezifikation verweist auf Ankündigungen aus [NIP-89: Recommended Application Handlers](/de/topics/nip-89/), um unterstützte Job-Kinds zu bewerben. So können Clients Anbieter entdecken, bevor sie einen Request veröffentlichen.

---

**Primärquellen:**
- [NIP-90 Specification](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Erwähnt in:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/de/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: Forgesworn toll-booth-dvm](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Agent Reputation Attestations proposal](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-89: Recommended Application Handlers](/de/topics/nip-89/)
