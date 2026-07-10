---
title: "Keycast: Team-gebaseerd Nostr Remote Signing"
date: 2026-05-21
draft: false
categories:
  - Signing
  - Security
  - Teams
translationOf: /en/topics/keycast.md
translationDate: 2026-07-01
---

Keycast is een zelf-gehoste NIP-46 remote signing-server gebouwd voor teams. Het slaat Nostr private keys versleuteld op in SQLite, genereert NIP-46 bunker-verbindingsstrings en draait signer-processen die remote signing-verzoeken goedkeuren of afwijzen volgens configureerbare beleidsregels per sleutel. Het project wordt onderhouden door de Marmot Protocol-organisatie.

## Hoe het werkt

De server bestaat uit vier hoofdcomponenten: een Axum API die teambeheer en NIP-98 HTTP-auth afhandelt, een SvelteKit-webfrontend die NIP-07 gebruikt voor authenticatie, een signer manager die autorisatierijen bewaakt en per autorisatie één `signer_daemon` opstart, en een SQLite-database met migraties.

Teamleden loggen in via hun NIP-07 browserextensie. De web-app vraagt om een NIP-98 HTTP-auth event dat lokaal door de extensie wordt ondertekend, en stuurt die auth-header vervolgens naar de API. De API verifieert het event, extraheert de pubkey en controleert het teamlidmaatschap. Opgeslagen sleutels worden versleuteld met een `master.key`-bestand dat apart van de image moet worden gemount en nooit gecommit mag worden.

De signer daemon ontsleutelt bij het opstarten de opgeslagen sleutel en de bunker-sleutel, maakt verbinding met geconfigureerde relays en roept `Authorization::validate_policy` aan vóór het goedkeuren van elk NIP-46 signing-verzoek. Beleidsregels specificeren welke event-kinds een bepaalde bunker-verbinding mag ondertekenen.

## Beveiligingsaudit (mei 2026)

Een beveiligingsaudit die in mei 2026 is voltooid, adresseerde problemen rond auth, permissies, data-integriteit en dependencies. Belangrijkste wijzigingen:

- NIP-98 auth vereist nu exact één `u`-tag en één `method`-tag, verwerpt verouderde of toekomstige timestamps, en valideert de `payload`-hashes van de request-body
- `ALLOWED_PUBKEYS` wordt exact geparseerd en server-side afgedwongen; de frontend biedt `/api/config?pubkey=<hex>` zodat de browser de allowlist-status kan controleren zonder de volledige serverlijst te ontvangen
- Lege beleidsregels weigeren standaard sign/encrypt/decrypt-verzoeken; het aanmaken van beleidsregels weigert onbekende of misvormde permissieconfiguraties
- SQLite-verbindingen activeren foreign-key-afdwinging; bij het verwijderen van een team gaan permissie-join-data niet langer verloren vóór opschoning
- Server-side routebescherming dekt nu ook geneste app-routes zoals `/teams/:id`
- Webresponses stellen CSP-, frame-, content-type-, referrer-, permissions- en HSTS-headers in
- Een SQL-migratie normaliseert oude allowed-kinds permissie-JSON van `{"sign":[...]}` naar `{"allowed_kinds":[...]}` bij het opstarten

De audit vermeldt resterende punten in [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) voordat de deployment kan worden vertrouwd met echte teamsleutels.

## Deployment

Docker Compose-deployment mount `master.key` in API- en signer-containers, draait containers als een niet-root UID/GID met een alleen-lezen root-bestandssysteem, en gebruikt Caddy-labels om `/api/*` naar de API te routeren en al het overige naar de web-app. De gepubliceerde image op `ghcr.io/marmot-protocol/keycast` is getagd met `master`, `latest` en `sha-<commit>`.

---

**Primaire bronnen:**
- [Keycast Repository](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - Resultaten van de beveiligingsaudit van mei 2026

**Genoemd in:**
- [Newsletter #23: Keycast Security Audit Complete](/nl/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**Zie ook:**
- [NIP-46: Nostr Remote Signing](/nl/topics/nip-46/)
- [NIP-07: Browser Extension Signer](/nl/topics/nip-07/)
- [Marmot Protocol](/nl/topics/marmot/)
