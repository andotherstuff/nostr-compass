---
title: "Proposta NIP-DB: Associazioni tra domini e servizi"
date: 2026-09-30
translationOf: /en/topics/nip-db.md
translationDate: 2026-10-02
draft: false
categories:
  - Proposals
  - Networking
  - Identity
---

NIP-DB è una **proposta aperta** per associare un normale dominio Internet a un servizio indirizzato tramite chiave. I suoi kind di event e la sua formulazione restano soggetti a revisione; questa pagina non la presenta come una specifica Nostr accettata.

## Modello di verifica

Una chiave che serve un servizio può pubblicare una rivendicazione firmata che indica il dominio e il servizio. La proposta descrive prove DNS o DNSSEC opzionali, attestazioni di testimoni e un record di zona per i nomi sotto il dominio. Una firma dimostra quale chiave ha pubblicato una rivendicazione, ma non dimostra il controllo del dominio. Un client deve verificare l’associazione con prove DNS, un testimone fidato o una chiave fissata in precedenza prima di usarla per risolvere un nome.

[fips-pub-domains](/it/topics/fips-pub-domains/) è l’implementazione di riferimento dell’autore per la mesh FIPS. I suoi test documentati a due nodi e solo sulla mesh sono prove di implementazione riportate dal maintainer. Non chiudono la revisione aperta della proposta né dimostrano una diffusione più ampia.

---

**Fonti primarie:**
- [Pull request aperta di NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Bozza dell’autore e segnaposto dei kind degli event](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [Implementazione di riferimento e test](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Citato in:**
- [Newsletter #42: domini pubblici](/it/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [Newsletter #42: proposta NIP-DB](/it/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
