---
title: "Domínios públicos do FIPS"
date: 2026-09-30
translationOf: /en/topics/fips-pub-domains.md
translationDate: 2026-10-02
draft: false
categories:
  - Protocol
  - Networking
  - Identity
---

O fips-pub-domains é uma implementação inicial para resolver nomes de domínio conhecidos da internet para serviços da malha [FIPS](/pt/topics/fips/). Ele publica reivindicações Nostr assinadas, mas uma assinatura prova apenas quem fez a reivindicação. O cliente também precisa verificar evidências de DNS ou DNSSEC, uma testemunha confiável ou um vínculo previamente fixado antes de tratar o autor da reivindicação como dono do domínio.

## Verificação e uso offline

A [primeira versão](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0) adicionou a reivindicação, o daemon de resolução e a integração com Android. A [versão 0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0) pode anexar uma prova DNSSEC a uma reivindicação, permitindo que um cliente que enxerga apenas um relay da malha verifique um domínio assinado ainda não visto contra as chaves raiz do DNS. Ela também oferece suporte a mais de um servidor verificado por domínio. A [versão 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1) corrigiu a unidade de servidor empacotada e passou a executá-la sem root; instalações existentes precisam da unidade substituta.

As [notas de teste](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md) do projeto descrevem casos com dois nós e com relay apenas na malha. São testes relatados pelo mantenedor, e não evidência de uma implantação mais ampla. Sua [proposta de NIP-DB](https://github.com/nostr-protocol/nips/pull/2487) está aberta, e os números de kinds de event do rascunho são marcadores provisórios, e não kinds Nostr atribuídos.

---

**Fontes primárias:**
- [Repositório e README](https://github.com/fr34aky/fips-pub-domains)
- [Versões 0.1.0–0.2.1](https://github.com/fr34aky/fips-pub-domains/releases)
- [NIP-DB proposto](https://github.com/nostr-protocol/nips/pull/2487)
- [Notas de teste](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Mencionado em:**
- [Newsletter #42: fips-pub-domains](/pt/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**Veja também:**
- [FIPS](/pt/topics/fips/)
