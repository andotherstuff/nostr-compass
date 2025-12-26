---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
translationOf: /en/topics/nip-be.md
translationDate: 2025-12-26
---

NIP-BE especifica como aplicações Nostr podem se comunicar e sincronizar via Bluetooth Low Energy, permitindo que apps com capacidade offline sincronizem dados entre dispositivos próximos sem conectividade com a internet.

## Estrutura GATT

Usa um Nordic UART Service com duas características:
- **Característica de escrita** - Cliente envia dados para o servidor
- **Característica de leitura** - Servidor envia dados para o cliente (via notificações)

## Enquadramento de Mensagem

BLE tem limites de payload pequenos (20-256 bytes dependendo da versão), então mensagens são:
- Comprimidas com DEFLATE
- Divididas em chunks com um índice de 2 bytes e flag de lote final
- Limitadas a tamanho máximo de 64KB

## Negociação de Papel

Dispositivos comparam UUIDs anunciados na descoberta:
- UUID maior se torna servidor GATT (papel de relay)
- UUID menor se torna cliente GATT
- UUIDs predeterminados existem para dispositivos de papel único

## Sincronização

Usa comunicação half-duplex com tipos de mensagem Nostr padrão (`EVENT`, `EOSE`, `NEG-MSG`) para coordenar sincronização de dados através de conexões intermitentes.

## Casos de Uso

- Sincronização de eventos offline entre dispositivos próximos
- Propagação de mensagens estilo mesh sem internet
- Conectividade de backup quando a rede não está disponível

---

**Fontes primárias:**
- [Especificação NIP-BE](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
