---
title: 'NIP-11: Documento de Informações do Relay'
date: 2025-12-17
draft: false
categories:
- Relay
- Protocol
translationOf: /en/topics/nip-11.md
translationDate: '2026-03-07'
---

O NIP-11 define como relays publica uma descrição legível por máquina de si mesmo, incluindo suporte a recursos reivindicados, limites e metadados do operador.

## Como funciona

Os clientes buscam informações do relay fazendo uma solicitação HTTP GET para o URL WebSocket do relay com um cabeçalho `Accept: application/nostr+json`. O relay retorna um documento JSON descrevendo suas capacidades.

## Campos úteis

- **nome** - Nome relay legível por humanos
- **descrição** - Para que serve o relay
- **supported_nips** - Lista de suporte NIP reivindicado
- **limitação** - Restrições como tamanho máximo da mensagem, autenticação necessária, etc.
- **pubkey** - Chave pública do operador de relay quando fornecida
- **contato** - Endereço de contato da operadora

## Modelo de confiança

NIP-11 são metadados auto-relatados. Ele informa o que um relay diz sobre si mesmo, não o que provou no tráfego ao vivo. Isso ainda é útil para descoberta e UX, mas os clientes não devem tratar `supported_nips` como verdade sem testar o comportamento.

Esta distinção é importante para a seleção do relay. Um relay pode anunciar pesquisa NIP-50, requisitos de autenticação ou um grande limite de mensagens, mas a resposta real só aparece quando um cliente realmente se conecta e exercita esses caminhos de código.

## Por que é importante

- Os clientes podem verificar se um relay suporta os recursos necessários antes de conectar
- Os serviços de descoberta podem indexar recursos relay
- Os usuários podem ver as políticas relay antes de publicar

## Direção de especificações recentes

A especificação foi reduzida ao longo do tempo. Campos opcionais mais antigos, como `software`, `version`, detalhes da política de privacidade e metadados de retenção foram removidos após anos de fraca adoção. Isso torna os documentos atuais do NIP-11 menores e mais realistas, mas também significa que os clientes não devem esperar metadados de políticas ricos dos relays.

---

**Fontes primárias:**
- [Especificação NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - Atualização do campo de identidade relay
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - limpeza de campos raramente usados
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - remoção de campos obsoletos

**Mencionado em:**
- [Boletim informativo nº 1: atualizações do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)

**Veja também:**
- [NIP-66: Descoberta de relay e monitoramento de atividade](/pt/topics/nip-66/)
