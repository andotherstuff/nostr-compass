---
title: "NIP-DB proposto: Vínculos de serviço a domínios"
date: 2026-09-30
translationOf: /en/topics/nip-db.md
translationDate: 2026-10-02
draft: false
categories:
  - Proposals
  - Networking
  - Identity
---

O NIP-DB é uma **proposta aberta** para vincular um domínio comum da internet a um serviço endereçado por chave. Seus kinds de event e sua redação continuam sujeitos a revisão; esta página não o apresenta como uma especificação Nostr aceita.

## Modelo de verificação

Uma chave de serviço pode publicar uma reivindicação assinada que nomeia o domínio e o serviço. A proposta descreve evidências opcionais de DNS ou DNSSEC, atestações de testemunhas e um registro de zona para nomes sob o domínio. Uma assinatura prova qual chave publicou uma reivindicação, mas não prova o controle do domínio. O cliente precisa verificar o vínculo com evidências de DNS, uma testemunha confiável ou uma chave previamente fixada antes de usá-lo para resolver um nome.

O [fips-pub-domains](/pt/topics/fips-pub-domains/) é a implementação de referência do autor para a malha FIPS. Seus testes documentados com dois nós e com relay apenas na malha são evidência de implementação relatada pelo mantenedor. Eles não encerram a revisão aberta da proposta nem estabelecem uma implantação mais ampla.

---

**Fontes primárias:**
- [Pull request aberto do NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Rascunho do autor e marcadores provisórios de kinds de event](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [Implementação de referência e testes](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Mencionado em:**
- [Newsletter #42: domínios públicos](/pt/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [Newsletter #42: NIP-DB proposto](/pt/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
