---
title: "Domini pubblici FIPS"
date: 2026-09-30
translationOf: /en/topics/fips-pub-domains.md
translationDate: 2026-10-02
draft: false
categories:
  - Protocol
  - Networking
  - Identity
---

fips-pub-domains è un’implementazione iniziale per risolvere nomi di dominio Internet familiari verso servizi sulla mesh [FIPS](/it/topics/fips/). Pubblica rivendicazioni Nostr firmate, ma una firma dimostra solo chi ha fatto una rivendicazione. Un client deve anche verificare prove DNS o DNSSEC, un testimone fidato o un’associazione fissata in precedenza prima di considerare il richiedente come proprietario del dominio.

## Verifica e uso offline

La [prima release](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0) ha aggiunto la rivendicazione, il demone resolver e l’integrazione Android. La [versione 0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0) può allegare una prova DNSSEC a una rivendicazione, consentendo a un client che vede solo un relay della mesh di verificare un dominio firmato mai visto prima rispetto alle chiavi della radice DNS. Supporta inoltre più di un server verificato per uno stesso dominio. La [versione 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1) ha corretto la unit del server inclusa nel pacchetto e l’ha modificata per funzionare senza root; le installazioni esistenti devono sostituire la unit.

Le [note sui test](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md) del progetto descrivono casi a due nodi e con relay solo sulla mesh. Sono test riportati dai maintainer, non prove di una diffusione più ampia. La sua [proposta NIP-DB](https://github.com/nostr-protocol/nips/pull/2487) è aperta, e i numeri dei kind degli event nella bozza sono segnaposto e non kind Nostr assegnati.

---

**Fonti primarie:**
- [Repository e README](https://github.com/fr34aky/fips-pub-domains)
- [Release 0.1.0–0.2.1](https://github.com/fr34aky/fips-pub-domains/releases)
- [Proposta NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Note sui test](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Citato in:**
- [Newsletter #42: fips-pub-domains](/it/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**Vedi anche:**
- [FIPS](/it/topics/fips/)
