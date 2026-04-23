---
title: 'Protocolo Marmot'
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
translationOf: /en/topics/marmot.md
translationDate: 2026-04-22
---

Marmot é um protocolo para mensagens de grupo com criptografia end-to-end no Nostr. Ele combina a identidade e a rede de relays do Nostr com MLS para gerenciamento de chaves de grupo, forward secrecy e segurança pós-comprometimento.

## Como funciona

Marmot usa Nostr para identidade, transporte por relay e distribuição de eventos, e então adiciona MLS por cima para mudanças de associação ao grupo e criptografia de mensagens. Diferente da [NIP-17](/pt/topics/nip-17/), que se concentra em mensagens um a um, Marmot foi construído para grupos em que membros entram, saem ou rotacionam chaves ao longo do tempo.

## Por que importa

MLS dá ao Marmot propriedades que os esquemas de mensagem direta do Nostr não oferecem sozinhos: evolução do estado do grupo, semântica de remoção de membros e recuperação após comprometimento por meio de atualizações posteriores de chave.

Essa divisão de trabalho é o ponto útil. Nostr resolve identidade e transporte em uma rede aberta. MLS resolve acordo autenticado de chaves de grupo. Marmot é a camada de cola entre os dois.

## Status de implementação

O protocolo continua experimental, mas agora tem múltiplas implementações e uso ativo em aplicações. [MDK](https://github.com/marmot-protocol/mdk) é a principal stack de referência em Rust, [marmot-ts](https://github.com/marmot-protocol/marmot-ts) leva o modelo para TypeScript, e aplicações como [White Noise](https://github.com/marmot-protocol/whitenoise), [Amethyst](https://github.com/vitorpamplona/amethyst), Pika e Vector têm usado componentes compatíveis com Marmot.

O trabalho recente tem se concentrado em hardening e interop. Correções guiadas por auditoria chegaram no início de 2026, e o MIP-03 introduziu resolução determinística de commits para que clientes possam convergir quando mudanças concorrentes de estado de grupo competem entre relays.

Em abril de 2026, o Amethyst alinhou seu MDK embarcado com os formatos wire de MIP-01 e MIP-05: o [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) adicionou codificação VarInt para prefixos de comprimento no estilo TLS e validação round-trip contra vetores de teste do MDK, o [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) adicionou suporte à MIP-00 KeyPackage Relay List, e o [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) fechou lacunas restantes de admin gate e tratamento de mídia identificadas por testes cross-client contra o White Noise. O [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) corrigiu o framing de commits MLS para que bytes de welcome criptografados coincidam com a saída do mdk-core, e o [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) corrigiu um bug de descriptografia da camada externa que causava divergência de estado entre co-admins. O [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) adiciona validação abrangente da criptografia de commits MLS, e o [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) lança `amy`, uma interface CLI para operações de grupo Marmot e MLS dirigida pela implementação do Amethyst.

O MDK recebeu o [PR #261](https://github.com/marmot-protocol/mdk/pull/261) para computar `RequiredCapabilities` de um grupo como o LCD das capabilities dos convidados, destravando invites entre versões mistas de Amethyst e White Noise, o [PR #262](https://github.com/marmot-protocol/mdk/pull/262) para fazer parse de key packages dos convidados antes de persistir o signer do criador, o [PR #264](https://github.com/marmot-protocol/mdk/pull/264) para convergir o formato wire de SelfUpdate entre implementações, e o [PR #265](https://github.com/marmot-protocol/mdk/pull/265) para expor um accessor `group_required_proposals`.

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) está no meio de uma refatoração em múltiplas fases, saindo de singletons globais para views por conta com `AccountSession`: o [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) estabeleceu a base de `AccountSession` e `AccountManager`, e fases seguintes migraram handles de relay, drafts e settings, operações de mensagem, leitura e escrita de grupo, membership, push notifications, leituras de key package, criação de grupo e, com o [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770), dispatch de eventos com escopo de sessão. O [marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) migra o cliente TypeScript para key packages endereçáveis kind `30443`.

---

**Fontes primárias:**
- [Repositório do protocolo Marmot](https://github.com/marmot-protocol/marmot)
- [Protocolo MLS](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit (MDK)](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [Cliente White Noise](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - alinhamento wire de MIP-01 e MIP-05
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - CLI Amy

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/)
- [Newsletter #1: Lançamentos](/pt/newsletters/2025-12-17-newsletter/)
- [Newsletter #4](/pt/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/pt/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/pt/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: conformidade MIP no Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: trabalho de interop no MDK](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: refatoracao por sessao no whitenoise-rs](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [MLS: Message Layer Security](/pt/topics/mls/)
- [MIP-05: Push notifications com preservação de privacidade](/pt/topics/mip-05/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
