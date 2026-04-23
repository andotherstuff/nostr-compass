---
title: "NIP-5A: Static Websites"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Hosting
---

NIP-5A definiert, wie statische Websites unter Nostr-Keypairs gehostet werden. Site-Autoren veröffentlichen signierte Manifest-Events, die URL-Pfade auf SHA256-Content-Hashes abbilden, und Host-Server lösen diese Manifeste auf, um die Dateien der Site aus Blossom-Storage auszuliefern.

## Funktionsweise

Die Spezifikation verwendet zwei Event-Kinds. Kind `15128` ist ein Root-Site-Manifest, eines pro pubkey, das als Standard-Website für diesen Schlüssel dient. Kind `35128` ist ein benanntes Site-Manifest, identifiziert durch ein `d`-Tag, das wie eine Subdomain fungiert. Jedes Manifest enthält `path`-Tags, die absolute URL-Pfade auf SHA256-Hashes der auszuliefernden Dateien abbilden.

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

Ein Host-Server empfängt eine HTTP-Anfrage, extrahiert den pubkey des Autors aus der Subdomain, ruft das Site-Manifest aus der Relay-Liste des Autors ab, löst den angeforderten Pfad in einen Content-Hash auf und lädt den passenden Blob vom Blossom-Server oder den Servern herunter, die in den `server`-Tags aufgeführt sind.

## URL-Auflösung

Root-Sites verwenden den npub als Subdomain. Benannte Sites verwenden eine 50-Zeichen-Base36-Kodierung des rohen pubkey gefolgt vom `d`-Tag-Wert, alles in einem einzigen DNS-Label. Weil DNS-Labels auf 63 Zeichen begrenzt sind und die Base36-pubkey-Kodierung immer 50 Zeichen nutzt, sind Bezeichner für benannte Sites auf 13 Zeichen begrenzt.

## Implementierungen

- [nsite](https://github.com/lez/nsite) - Host-Server, der NIP-5A-Manifeste auflöst und Dateien ausliefert
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - UI zum Erstellen und Veröffentlichen von Site-Manifesten

---

**Primärquellen:**
- [NIP-5A Specification](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - Original proposal and merge
- [nsite](https://github.com/lez/nsite) - Reference host implementation
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - Publishing and management UI

**Erwähnt in:**
- [Newsletter #16: NIP-5A merges](/de/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/de/newsletters/2026-04-01-newsletter/)
- [Newsletter #19: NIP-5D applets proposal](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [Blossom](/de/topics/blossom/)
- [NIP-65: Relay List Metadata](/de/topics/nip-65/)
- [NIP-96: HTTP File Storage](/de/topics/nip-96/)
