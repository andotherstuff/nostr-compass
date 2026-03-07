---
title: Quartz
date: 2025-12-31
draft: false
categories:
- Library
- Development
translationOf: /en/topics/quartz.md
translationDate: '2026-03-07'
---

Quartz é uma biblioteca Kotlin Multiplataforma Nostr desenvolvida por Vitor Pamplona. É o protocolo compartilhado e a camada de dados por trás do avanço da Amethyst em direção ao Android, desktop e, eventualmente, iOS a partir de uma base de código.

## Como funciona

Quartz fornece funcionalidade central do Nostr como uma biblioteca compartilhada:

- **Manipulação de eventos**: análise, validação e criação de eventos Nostr
- **Criptografia**: assinatura Secp256k1, criptografia NIP-44, gerenciamento de chaves
- **Comunicação de relay**: gerenciamento de conexões, ordenação de mensagens, tratamento de assinaturas
- **Suporte NIP**: Implementação de NIPs comuns, incluindo NIP-06, NIP-19, NIP-44 e mais

## Por que é importante

Quartz transfere a lógica pesada de protocolo de um único aplicativo para uma biblioteca reutilizável. Isso é importante porque o manuseio do relay, a análise de eventos, a criptografia e as regras de armazenamento tornam-se mais fáceis de compartilhar entre clientes, em vez de serem reimplementadas por plataforma.

O resultado concreto já apareceu no trabalho desktop da Ametista. O refator apoiado por concessão moveu o código compartilhado para módulos Kotlin Multiplataforma, como `commonMain`, `jvmAndroid` e `jvmMain`, tornando o suporte de desktop um problema de biblioteca e módulo em vez de uma reescrita completa.

## Arquitetura

A biblioteca usa uma estrutura modular de conjunto de fontes:
- `commonMain`: Código compartilhado para todas as plataformas
- `jvmAndroid`: Código compartilhado entre JVM e Android
- `androidMain`: implementações específicas do Android
- `jvmMain`: implementações JVM de desktop
- `iosMain`: implementações específicas para iOS

## Status atual

Em dezembro de 2025, o OpenSats anunciou o financiamento para Quartz em sua décima quarta onda de bolsas Nostr. O repositório existe como uma biblioteca independente, mas grande parte do progresso visível até agora chegou por meio de PRs Amethyst que convertem módulos de aplicativos em código multiplataforma e rastreiam a paridade de recursos entre os destinos.

---

**Fontes primárias:**
- [Repositório Quartz](https://github.com/vitorpamplona/quartz)
- [Quartz no Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Repositório de Ametista](https://github.com/vitorpamplona/amethyst)
- [Décima quarta onda de concessões Nostr do OpenSats](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)

**Mencionado em:**
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Boletim informativo nº 3: Notícias](/pt/newsletters/2025-12-31-newsletter/#news)
- [Boletim informativo nº 3: Mudanças notáveis na ametista](/pt/newsletters/2025-12-31-newsletter/#amethyst-android)

**Veja também:**
- [Protocolo Blossom](/pt/topics/blossom/)
