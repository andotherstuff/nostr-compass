---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2025-12-31
draft: false
categories:
  - Biblioteca
  - Desenvolvimento
---

Quartz é uma biblioteca Kotlin Multiplatform para Nostr desenvolvida por Vitor Pamplona. Originalmente extraída do cliente Android Amethyst, Quartz fornece implementações reutilizáveis do protocolo Nostr para plataformas JVM, Android, iOS e Linux.

## Como Funciona

Quartz fornece funcionalidade central do Nostr como uma biblioteca compartilhada:

- **Manipulação de Eventos**: Análise, validação e criação de eventos Nostr
- **Criptografia**: Assinatura Secp256k1, criptografia NIP-44, gerenciamento de chaves
- **Comunicação com Relays**: Gerenciamento de conexões, ordenação de mensagens, manipulação de assinaturas
- **Suporte a NIPs**: Implementação de NIPs comuns incluindo NIP-06, NIP-19, NIP-44, e mais

## Recursos Principais

- **Kotlin Multiplatform**: Uma única base de código compila para múltiplos alvos
- **Plataformas Alvo**: Android, JVM, iOS (ARM64, Simulador), Linux
- **Otimizado para Performance**: Processamento eficiente de eventos e operações criptográficas
- **Integração com Blossom**: Suporte para upload de mídia via protocolo Blossom
- **OpenTimestamp**: Port completo em Kotlin para verificação de carimbos de tempo

## Arquitetura

A biblioteca usa uma estrutura modular de conjuntos de fontes:
- `commonMain`: Código compartilhado para todas as plataformas
- `jvmAndroid`: Código compartilhado entre JVM e Android
- `androidMain`: Implementações específicas do Android
- `jvmMain`: Implementações JVM para desktop
- `iosMain`: Implementações específicas do iOS

## Subsídio da OpenSats

Em dezembro de 2025, a OpenSats anunciou financiamento para Quartz como parte de sua décima quarta onda de subsídios Nostr. O subsídio apoia o desenvolvimento contínuo para habilitar Amethyst no iOS através da mesma abordagem Kotlin Multiplatform que já alimenta as versões Android e desktop.

---

**Fontes principais:**
- [Quartz no Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Repositório do Amethyst](https://github.com/vitorpamplona/amethyst)

**Mencionado em:**
- [Newsletter #3: Resumo de Dezembro](/pt/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: Notícias](/pt/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Mudanças Notáveis do Amethyst](/pt/newsletters/2025-12-31-newsletter/#amethyst-android)

**Veja também:**
- [Protocolo Blossom](/pt/topics/blossom/)
