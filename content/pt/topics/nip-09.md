---
title: 'NIP-09: Solicitação de exclusão de eventos'
date: 2026-02-25
draft: false
categories:
- Moderation
- Protocol
translationOf: /en/topics/nip-09.md
translationDate: '2026-03-07'
---

O NIP-09 define uma forma de os autores solicitarem a exclusão de eventos que publicaram anteriormente. É um sinal de exclusão do lado relay, não uma função de exclusão em toda a rede.

## Como funciona

Os usuários publicam eventos kind 5 contendo referências a eventos que desejam excluir. Os relays que suportam NIP-09 devem parar de servir eventos correspondentes do mesmo autor e podem removê-los do armazenamento.

A exclusão é um pedido, não uma garantia. As relays podem ignorar solicitações de exclusão e os eventos já podem ter sido propagados para relays que não suportam exclusão. Os usuários não devem confiar no NIP-09 para remoção de conteúdo sensível à privacidade.

## Por que é importante

O NIP-09 oferece aos clientes e ao relays uma maneira comum de expressar "este evento não deve mais aparecer", o que é útil para postagens acidentais, sobreposição de estado de carteira e fluxos de trabalho de moderação. Mas o autor só pode solicitar a exclusão de seus próprios eventos. Não é um mecanismo de remoção de uso geral para conteúdo de terceiros.

## Compensações

O ponto fraco é a propagação. Depois que um evento for espelhado em vários relays, a exclusão se tornará o melhor esforço. Alguns relays irão excluí-lo, alguns irão marcá-lo e alguns continuarão servindo-o indefinidamente. Os clientes que apresentam a exclusão como definitiva estão exagerando o que o protocolo garante.

Outra questão prática são as referências. Os usuários e aplicativos ainda podem manter o evento excluído localmente ou citá-lo em outro lugar, mesmo depois que um relay compatível parar de exibi-lo.

---

**Fontes primárias:**
- [Especificação NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Mencionado em:**
- [Boletim informativo nº 11: Aprofundamento do NIP-60](/pt/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)
- [Boletim informativo nº 12: Notícias](/pt/newsletters/2026-03-04-newsletter/#news)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
- [NIP-60: Carteira Cashu](/pt/topics/nip-60/)
