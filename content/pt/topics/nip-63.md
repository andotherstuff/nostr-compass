---
title: 'NIP-63: acesso pago/conteúdo premium'
date: 2025-12-17
draft: false
categories:
- Protocol
- Monetization
translationOf: /en/topics/nip-63.md
translationDate: '2026-03-07'
---

NIP-63 é um padrão proposto para lidar com conteúdo fechado dentro do protocolo Nostr, permitindo que os criadores exijam pagamento antes de revelar o conteúdo.

## Como funciona

Os criadores de conteúdo podem publicar eventos onde o conteúdo completo é criptografado ou escondido atrás de um acesso pago. Após a verificação do pagamento, o conteúdo é desbloqueado para o usuário pagante.

A proposta é intencionalmente sobre a superfície do protocolo para conteúdo premium, e não sobre a obrigatoriedade de uma única via de pagamento ou modelo de negócios. Isso o mantém flexível, mas também significa que carteiras, clientes e editores ainda precisam concordar sobre o fluxo de desbloqueio na prática.

## Por que é importante

Sem um formato compartilhado, cada sistema de acesso pago Nostr se torna seu próprio silo. Um NIP comum permitiria que um cliente publicasse conteúdo premium e outro cliente entendesse que o conteúdo é bloqueado, o que precisa ser pago e quando deve ser revelado.

Isso ainda não garante portabilidade. O NIP-63 ainda é uma proposta no [PR #2156](https://github.com/nostr-protocol/nips/pull/2156), portanto as implementações ainda podem divergir enquanto o design estiver em discussão.

## Casos de uso

- Artigos exclusivos para assinantes
- Conteúdo de mídia premium
- Eventos pay-per-view
- Acesso exclusivo aos criadores

## Compensações

Os metadados do Paywall podem ser públicos mesmo quando o payload premium não o é. Isso dá aos clientes informações suficientes para apresentar uma oferta, mas também significa que a existência de conteúdo pago fica visível para qualquer pessoa que possa ler o evento.

Os criadores também precisam pensar no que acontece após o desbloqueio. Depois que o texto simples é mostrado a um usuário pagante, o protocolo não pode impedir que o usuário o copie em outro lugar.

---

**Fontes primárias:**
- [Proposta NIP-63 (PR #2156)](https://github.com/nostr-protocol/nips/pull/2156)

**Mencionado em:**
- [Boletim informativo nº 1: atualizações do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)

**Veja também:**
- [NIP-57: Zaps](/pt/topics/nip-57/)
