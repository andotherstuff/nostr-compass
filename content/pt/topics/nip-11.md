---
title: 'NIP-11: Relay Information Document'
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
translationOf: /en/topics/nip-11.md
translationDate: 2026-04-22
---

NIP-11 define como relays publicam uma descrição legível por máquina sobre si mesmos, incluindo suporte declarado a features, limites e metadados do operador.

## Como funciona

Clientes buscam informações de relay fazendo um request HTTP GET para a URL WebSocket do relay com o header `Accept: application/nostr+json`. O relay retorna um documento JSON descrevendo suas capabilities.

## Campos úteis

- **name** - nome legível do relay
- **description** - para que o relay serve
- **supported_nips** - lista do suporte a NIPs declarado
- **limitation** - restrições como tamanho máximo de mensagem, auth obrigatória e afins
- **pubkey** - chave pública do operador do relay, quando fornecida
- **contact** - endereço de contato do operador

## Modelo de confiança

NIP-11 é metadado autorreportado. Ela diz o que um relay afirma sobre si mesmo, não o que ele provou em tráfego real. Isso ainda é útil para descoberta e UX, mas clientes não devem tratar `supported_nips` como verdade absoluta sem testar o comportamento.

Essa distinção importa para seleção de relay. Um relay pode anunciar busca NIP-50, exigências de autenticação ou um grande limite de mensagem, mas a resposta real só aparece quando um cliente de fato se conecta e exercita esses caminhos de código.

## Por que importa

- clientes podem checar se um relay suporta features exigidas antes de conectar
- serviços de descoberta podem indexar capabilities de relays
- usuários podem ver políticas de relay antes de publicar

## Direção recente da spec

A especificação foi enxugada ao longo do tempo. Campos opcionais antigos, como `software`, `version`, detalhes de política de privacidade e metadados de retenção, foram removidos depois de anos de adoção fraca. Isso torna documentos NIP-11 atuais menores e mais realistas, mas também significa que clientes não devem esperar metadados ricos de política vindos de relays.

O [PR #2318](https://github.com/nostr-protocol/nips/pull/2318) propõe adicionar um objeto opcional `access_control` ao relay information document, listando o modo de restrição do relay, como open, invite, payment ou allowlist, e qualquer endpoint que um cliente possa usar para pedir acesso. O campo é apenas consultivo e pretende permitir que clientes e diretórios filtrem relays restritos para fora de listas públicas de descoberta e mostrem aos usuários, de antemão, por que um relay recusa escritas.

## Implementações

- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) leva o nostream à paridade completa com informações de relay NIP-11.

---

**Fontes primárias:**
- [Especificação NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - atualização do campo de identidade do relay
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - limpeza de campos raramente usados
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - remoção de campos obsoletos
- [PR #2318](https://github.com/nostr-protocol/nips/pull/2318) - campo `access_control` para descoberta de relays restritos
- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) - paridade completa de informações de relay NIP-11

**Mencionado em:**
- [Newsletter #1: Atualizações de NIP](/pt/newsletters/2025-12-17-newsletter/)
- [Newsletter #13: Atualizações de NIP](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: Atualizações de NIP, proposta `access_control`](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-66: Relay Discovery and Liveness Monitoring](/pt/topics/nip-66/)
