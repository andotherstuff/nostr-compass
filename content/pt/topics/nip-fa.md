---
title: "Buzz NIP-FA: Adaptador de identidade federada"
date: 2026-10-21
draft: false
categories: ["NIPs"]
translationOf: /en/topics/nip-fa.md
translationDate: 2026-11-05
---

A Buzz NIP-FA é uma especificação rascunho e opcional do projeto Buzz. Ela fica fora das NIPs aceitas do repositório oficial nostr-protocol/nips.

Ela define um contrato HTTP neutro em relação a provedores entre um cliente Nostr e um adaptador de identidade corporativa. Após um login no navegador, o adaptador mantém uma sessão para o usuário. Ele emite asserções Buzz NIP-FI locais ao projeto que vinculam o usuário a uma chave Nostr, cujo controle o cliente prova com a [NIP-98](/pt/topics/nip-98/). O [operador escolhe o tempo de vida de cada asserção](https://github.com/block/buzz/pull/8934), que deve respeitar o maximum_assertion_age do emissor aceito pelo relay, e o exp não pode exceder a expiração da sessão do adaptador. O tempo de vida escolhido limita por quanto tempo uma chave revogada ainda poderia se reconectar após uma reinicialização do relay, e os clientes não devem rejeitar uma asserção apenas por causa do seu tempo de vida. A NIP-FI e as NIPs oficiais não mudam. O login usa um desafio de handoff S256 e um callback de loopback em `127.0.0.1` ou `[::1]` que recebe um código de uso único. Sistemas upstream como OIDC ou SAML ficam atrás do adaptador. Descobrir quais relays exigem identidade corporativa fica a cargo de outras especificações.

Fonte primária: a [especificação NIP-FA](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md) no repositório do Buzz.

## Credenciais de agentes {#agent-credentials}

O Buzz mergeou um [rascunho da NIP-FA para credenciais de agentes autorizadas pelo dono](https://github.com/block/buzz/pull/9015), definindo rotas de concessão, asserção e revogação para agentes que um dono autorizou por meio da NIP-OA. Uma concessão vem de uma troca de tokens RFC 8693 que combina a sessão do dono com uma prova [NIP-98](/pt/topics/nip-98/) do agente. Para uma asserção, o agente apresenta a concessão como token Bearer junto com sua própria prova, e os clientes verificam o `iss` da asserção contra o emissor da concessão. As provas de agentes são de uso único e pertencem apenas às rotas de concessão e de asserção. A revogação roda na sessão do dono sem prova do agente; ela revoga a chave do agente e suas concessões e desconecta o agente. A política do adaptador decide o tempo de vida da concessão. Condições de autorização não suportadas são recusadas, e uma chave revogada não pode se inscrever novamente. A NIP-FA é uma especificação do Buzz, não uma NIP aceita. O merge está apenas no código-fonte, sem alegação de ativação em produção, de build lançado ou de interoperabilidade.

## Fontes primárias {#primary-sources}

- [Buzz NIP-FA: Adaptador de identidade federada](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)

- [Rotas de credenciais de agentes autorizadas pelo dono](https://github.com/block/buzz/pull/9015)

## Mencionado em {#mentioned-in}

- [Newsletter #47: Credenciais de agentes do Buzz](/pt/newsletters/2026-11-04-newsletter/#buzz-defines-owner-authorized-agent-credential-routes)


- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
