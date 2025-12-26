---
title: "NIP-40: Timestamp de Expiração"
date: 2025-12-17
draft: false
categories:
  - Protocol
translationOf: /en/topics/nip-40.md
translationDate: 2025-12-26
---

NIP-40 define uma tag de expiração que informa aos relays quando um evento deve ser deletado.

## Estrutura

Eventos incluem uma tag `expiration` com um timestamp Unix:

```json
["expiration", "1734567890"]
```

Após esse tempo, os relays devem deletar o evento e recusar servi-lo.

## Casos de Uso

- Conteúdo efêmero que deve desaparecer após um tempo definido
- Ofertas ou anúncios por tempo limitado
- Expiração de listagens em marketplaces (ex: Shopstr)
- Redução de requisitos de armazenamento dos relays

## Considerações

- Relays não são obrigados a honrar expiração (mas a maioria o faz)
- Clientes não devem depender de expiração para deleção de conteúdo crítico de segurança
- Uma vez que o conteúdo é buscado por outro cliente, ele pode ser armazenado em cache ou republicado

---

**Fontes primárias:**
- [Especificação NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
