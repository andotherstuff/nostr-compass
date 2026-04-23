---
title: 'NIP-40: Carimbo de data e hora de expiração'
date: 2025-12-17
draft: false
categories:
- Protocol
translationOf: /en/topics/nip-40.md
translationDate: '2026-03-07'
---

O NIP-40 define uma expiração tag que informa ao relays quando um evento deve ser excluído.

## Como funciona

Os eventos incluem um `expiration` tag com um carimbo de data/hora Unix:

```json
["expiration", "1734567890"]
```

Após este horário, relays deverá excluir o evento e recusar-se a atendê-lo.

## Por que é importante

- Conteúdo efêmero que deve desaparecer após um determinado tempo
- Ofertas ou anúncios por tempo limitado
- Expiração da listagem em mercados (por exemplo, Shopstr)
- Reduzindo os requisitos de armazenamento relay

A expiração é uma dica de retenção, não um sistema de revogação. Ajuda a alinhar o comportamento do relay em torno do conteúdo desatualizado, mas não garante o apagamento quando outro relay, cliente ou arquivo já tiver copiado o evento.

## Notas de confiança e segurança

- Os relays não são obrigados a honrar a expiração (mas a maioria o faz)
- Os clientes não devem confiar na expiração para exclusão de conteúdo crítico para a segurança
- Uma vez que o conteúdo é obtido por outro cliente, ele pode ser armazenado em cache ou republicado
- A expiração não esconde a existência de um evento. IDs de eventos, cotações ou cópias fora do relay ainda podem sobreviver após a passagem do carimbo de data/hora

---

**Fontes primárias:**
- [Especificação NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Mencionado em:**
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/)
- [Boletim informativo nº 3: Mudanças notáveis no código](/pt/newsletters/2025-12-31-newsletter/)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
