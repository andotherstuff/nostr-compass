---
title: Protocolo Marmot
date: 2025-12-17
draft: false
categories:
- Protocol
- Privacy
- Messaging
translationOf: /en/topics/marmot.md
translationDate: '2026-03-07'
---

Marmot é um protocolo para mensagens de grupo criptografadas de ponta a ponta no Nostr. Ele combina a identidade da Nostr e a rede de relays com MLS para gerenciamento de chaves de grupo, sigilo de encaminhamento e segurança pós-comprometimento.

## Como funciona

Marmot usa Nostr para identidade, transporte relay e distribuição de eventos e, em seguida, coloca MLS no topo para alterações de membros de grupo e criptografia de mensagens. Ao contrário do [NIP-17](/pt/topics/nip-17/), que se concentra em mensagens individuais, o Marmot foi desenvolvido para grupos onde os membros ingressam, saem ou alternam chaves ao longo do tempo.

## Por que é importante

O MLS fornece ao Marmot propriedades que os esquemas de mensagem direta do Nostr não fornecem por si próprios: evolução do estado do grupo, semântica de remoção de membros e recuperação após comprometimento por meio de atualizações de chave posteriores.

Essa divisão do trabalho é o insight útil. Nostr resolve identidade e transporte em uma rede aberta. MLS resolve acordo de chave de grupo autenticado. Marmot é a camada adesiva entre eles.

## Status de implementação

O protocolo permanece experimental, mas agora possui múltiplas implementações e uso ativo de aplicativos. MDK é a principal pilha de referência do Rust, `marmot-ts` traz o modelo para TypeScript e aplicativos como White Noise, Pika e Vector têm usado componentes compatíveis com Marmot.

O trabalho recente concentrou-se no fortalecimento e na interoperabilidade. Correções orientadas por auditoria foram lançadas no início de 2026, e o MIP-03 introduziu resolução determinística de commit para que os clientes possam convergir quando mudanças simultâneas de estado de grupo ocorrerem em relays.

---

**Fontes primárias:**
- [Repositório de protocolo Marmot](https://github.com/marmot-protocol/marmot)
- [NIP-104: Bate-papos em grupo criptografados baseados em MLS](/pt/topics/nip-104/)
- [Kit de desenvolvimento Marmot](https://github.com/marmot-protocol/mdk)
- [marmota-ts](https://github.com/marmot-protocol/marmot-ts)

**Mencionado em:**
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Boletim Informativo nº 1: Lançamentos](/pt/newsletters/2025-12-17-newsletter/#releases)
- [Boletim informativo nº 4](/pt/newsletters/2026-01-07-newsletter/)
- [Boletim informativo nº 7](/pt/newsletters/2026-01-28-newsletter/)
- [Boletim Informativo nº 12](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [MLS (Message Layer Security)](/pt/topics/mls/)
- [MIP-05: Notificações push para preservação de privacidade](/pt/topics/mip-05/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
