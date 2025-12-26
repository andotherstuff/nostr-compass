---
title: "BUD-03: Lista de Servidores do Usuário"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
translationOf: /en/topics/bud-03.md
translationDate: 2025-12-26
---

BUD-03 define como usuários publicam seus servidores Blossom preferidos, permitindo que clientes descubram onde fazer upload e recuperar arquivos de mídia de um usuário.

## Como Funciona

Usuários publicam um evento kind 10063 listando seus servidores Blossom. Clientes podem então:
- Fazer upload de mídia para os servidores preferidos do usuário
- Descobrir onde encontrar os blobs de um usuário dado sua pubkey

Isso permite descoberta baseada em autor como alternativa a incorporar URLs de servidor diretamente no conteúdo.

---

**Fontes primárias:**
- [Especificação BUD-03](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**Veja também:**
- [Protocolo Blossom](/pt/topics/blossom/)
- [NIP-51: Listas](/pt/topics/nip-51/)
