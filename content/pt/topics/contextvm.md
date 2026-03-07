---
title: ContextVM
date: 2026-02-25
draft: false
categories:
- Infrastructure
- AI
- Protocol
translationOf: /en/topics/contextvm.md
translationDate: '2026-03-07'
---

ContextVM é um protocolo e conjunto de ferramentas para transportar tráfego MCP (Model Context Protocol) através do Nostr. Ele permite que clientes e servidores MCP se encontrem e troquem mensagens assinadas sem depender de um registro central, domínios ou OAuth.

## Como funciona

O SDK ContextVM fornece transportes de cliente e servidor TypeScript para MCP sobre Nostr. Os servidores MCP existentes podem permanecer em seus transportes normais enquanto um gateway os expõe ao Nostr, e os clientes sem suporte nativo do Nostr podem se conectar por meio de uma camada de proxy.

Os relays atuam como um barramento de mensagens. Eles roteiam eventos, enquanto a assinatura e a criptografia fornecem autenticação aos endpoints e privacidade de transporte.

## Componentes

**SDK**: biblioteca TypeScript com transporte cliente/servidor, suporte a proxy e funcionalidade de gateway para conectar servidores MCP locais ao Nostr.

**CVMI**: Interface de linha de comando para descoberta de servidor e invocação de método.

**Relatr**: Serviço de pontuação de confiança que calcula pontuações personalizadas a partir da distância do gráfico social e validação do perfil.

## Por que é importante

ContextVM é uma ponte de transporte, não um substituto do próprio MCP. Isso é importante porque reduz o custo de adoção: um servidor MCP existente pode obter acessibilidade do Nostr sem reescrever seu esquema de ferramenta ou lógica de negócios.

O trabalho recente de ContextVM também impulsionou a entrega efêmera para o tráfego gift-wrapped. Isso é útil para chamadas de ferramentas e respostas intermediárias onde o armazenamento relay durável é desnecessário e pode criar exposição extra à privacidade.

## Notas de interoperabilidade

Em Fevereiro e Março de 2026, o projeto passou da implementação para a normalização. A equipe abriu propostas NIP para MCP JSON-RPC sobre Nostr e para uma variante efêmera de gift wrap. Mesmo que essas propostas mudem, elas mostram os limites do protocolo de forma mais clara: o MCP permanece na camada de aplicação, o Nostr cuida da descoberta e do transporte.

---

**Fontes primárias:**
- [Site ContextVM](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245: Efêmero Gift Wrap](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246: MCP JSON-RPC sobre Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**Mencionado em:**
- [Boletim informativo nº 11: Notícias ContextVM](/pt/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [Boletim informativo nº 12](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [NIP-90: Máquinas de venda automática de dados](/pt/topics/nip-90/)
