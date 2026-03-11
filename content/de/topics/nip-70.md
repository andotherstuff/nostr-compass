---
title: "NIP-70: Geschützte Events"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

NIP-70 definiert eine Möglichkeit für Autoren, ein Event mit dem einfachen Tag `[["-"]]` als geschützt zu markieren. Ein geschütztes Event kann nur akzeptiert werden, wenn ein Relay dieses Verhalten unterstützen will und verifiziert, dass der authentifizierte Publisher denselben pubkey hat wie der Event-Autor.

## Wie es funktioniert

Die Kernregel ist kurz. Wenn ein Event das Tag `[["-"]]` enthält, sollte ein Relay es standardmäßig ablehnen. Ein Relay, das geschützte Events unterstützen will, muss zuerst den [NIP-42](/de/topics/nip-42/) `AUTH`-Flow ausführen und bestätigen, dass der authentifizierte Client sein eigenes Event veröffentlicht.

Dadurch ist NIP-70 eine Regel über Veröffentlichungsautorität, keine Verschlüsselungsregel. Der Inhalt kann weiterhin lesbar sein. Was sich ändert, ist, wer dieses Event auf einem Relay platzieren darf, das das Tag beachtet. So können Relays halbgeschlossene Feeds und andere Kontexte unterstützen, in denen Autoren möchten, dass ein Relay Veröffentlichungen durch Dritte ablehnt.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## Auswirkungen des AUTH-Flows

Geschützte Events sind nur dann nützlich, wenn Relays die Identität des Autors beim Veröffentlichen tatsächlich durchsetzen. Deshalb hängt NIP-70 so direkt von [NIP-42](/de/topics/nip-42/) ab. Ein Relay, das `[["-"]]`-Events ohne passende Auth-Prüfung akzeptiert, behandelt das Tag als Dekoration, nicht als Richtlinie.

## Relay-Verhalten und Grenzen

NIP-70 verspricht nicht, dass Inhalte für immer eingedämmt bleiben. Jeder Empfänger kann weiterhin kopieren, was er sieht, und anderswo ein neues Event veröffentlichen. Die Spezifikation gibt Relays nur einen standardisierten Weg, die Absicht des Autors zu respektieren und direkte Wiederveröffentlichung geschützter Events abzulehnen.

Deshalb ist die anschließende Arbeit wichtig. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) erweitert die Regel auf Reposts, die geschützte Events einbetten, und schließt damit eine einfache Umgehung, bei der das ursprüngliche Event geschützt blieb, das umhüllende Event aber nicht.

## Implementierungen

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Fügt NIP-42-Auth-Unterstützung für geschützte Events hinzu
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - Lehnt Reposts ab, die geschützte Events einbetten
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - Fügt Hilfsunterstützung im Zusammenhang mit Protected-Event-Handling hinzu

---

**Primärquellen:**
- [NIP-70 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - Fügte NIP-70 zum NIPs-Repository hinzu
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - Lehnt Reposts ab, die geschützte Events einbetten
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Relay-Implementierung für NIP-42-Auth und geschützte Events

**Erwähnt in:**
- [Newsletter #13: NIP Updates](/de/newsletters/2026-03-11-newsletter/#nip-updates)
- [Newsletter #13: NIP Deep Dive](/de/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**Siehe auch:**
- [NIP-42: Client-Authentifizierung](/de/topics/nip-42/)
- [NIP-11: Relay-Informationsdokument](/de/topics/nip-11/)
