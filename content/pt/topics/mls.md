---
title: MLS (Message Layer Security)
date: 2025-12-31
draft: false
categories:
- Cryptography
- Protocol
- Messaging
- Privacy
translationOf: /en/topics/mls.md
translationDate: '2026-03-07'
---

Message Layer Security (MLS) é um protocolo IETF para mensagens de grupo criptografadas de ponta a ponta. Ele fornece sigilo direto e segurança pós-comprometimento para grupos que podem mudar de membro ao longo do tempo.

## Como funciona

O MLS usa uma estrutura de contrato de chave baseada em árvore chamada TreeKEM:

1. **Pacotes de Chaves**: Cada participante publica um pacote de chaves contendo sua identidade e chaves de criptografia
2. **Estado do grupo**: uma árvore de catraca mantém o estado criptográfico do grupo
3. **Commits**: os membros atualizam a árvore ao ingressar, sair ou alternar chaves
4. **Criptografia de mensagens**: o conteúdo é criptografado usando chaves derivadas do segredo do grupo compartilhado

## Por que é importante

O MLS resolve um problema que a criptografia em pares não resolve bem: manter a adesão ao grupo e o estado de criptografia coerentes à medida que os membros ingressam, saem ou alternam chaves de forma assíncrona.

Sua estrutura em árvore é o insight prático. As atualizações não exigem que cada participante renegocie em pares com todos os outros, portanto, o protocolo é muito melhor dimensionado do que esquemas ad hoc de chave de grupo.

## Padronização

- **RFC 9420** (julho de 2023): especificação do protocolo Core MLS
- **RFC 9750** (abril de 2025): arquitetura MLS para integração de sistemas

## Adoção em Nostr

Vários aplicativos Nostr usam MLS para mensagens de grupo seguras:

- **KeyChat**: aplicativo de mensagens criptografadas baseado em MLS para dispositivos móveis e desktop
- **White Noise**: Mensagens privadas usando MLS com integração do protocolo Marmot
- **Protocolo Marmot**: extensão Nostr que fornece criptografia de grupo baseada em MLS

A MLS oferece garantias de segurança de grupo mais fortes do que [NIP-04](/pt/topics/nip-04/) ou [NIP-44](/pt/topics/nip-44/) isoladamente, especialmente quando a adesão muda com frequência.

## Compensações

MLS não é um produto de mensagens completo. Os aplicativos ainda precisam de identidade, transporte, resistência a spam, armazenamento e tratamento de conflitos em torno do protocolo.

É por isso que projetos Nostr como o Marmot adicionam regras extras ao MLS. A criptografia é padronizada, mas o protocolo de aplicação envolvente ainda é importante para a interoperabilidade.

---

**Fontes primárias:**
- [RFC 9420: Protocolo MLS](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: Arquitetura MLS](https://datatracker.ietf.org/doc/rfc9750/)
- [Grupo de Trabalho IETF MLS](https://datatracker.ietf.org/wg/mls/about/)
- [Site do protocolo MLS](https://messaginglayersecurity.rocks/)

**Mencionado em:**
- [Boletim Informativo nº 3: Lançamentos](/pt/newsletters/2025-12-31-newsletter/#releases)
- [Boletim informativo nº 10](/pt/newsletters/2026-02-18-newsletter/)
- [Boletim informativo nº 12](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [Protocolo Marmot](/pt/topics/marmot/)
- [MIP-05: Notificações push para preservação de privacidade](/pt/topics/mip-05/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-44: cargas criptografadas](/pt/topics/nip-44/)
