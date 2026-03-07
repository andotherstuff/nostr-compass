---
title: 'NIP-BE: Bluetooth de baixa energia'
date: 2025-12-17
draft: false
categories:
- Protocol
- Connectivity
translationOf: /en/topics/nip-be.md
translationDate: '2026-03-07'
---

O NIP-BE especifica como os aplicativos Nostr podem se comunicar e sincronizar via Bluetooth Low Energy, permitindo que aplicativos com capacidade off-line sincronizem dados entre dispositivos próximos sem conectividade com a Internet.

## Como funciona

O NIP-BE reutiliza frames de mensagens Nostr normais sobre BLE em vez de inventar um modelo de evento separado. Os dispositivos anunciam um serviço BLE mais um UUID do dispositivo, comparam os UUIDs quando eles se encontram e decidem deterministicamente qual lado se torna o servidor GATT e qual lado se torna o cliente GATT.

O serviço GATT usa uma forma de estilo UART nórdico com uma característica de gravação e uma característica de leitura/notificação. Isso mantém o transporte simples o suficiente para pilhas móveis restritas, ao mesmo tempo que transporta mensagens Nostr comuns.

## Enquadramento de mensagem

BLE tem pequenos limites de payload, então o NIP-BE compacta mensagens com DEFLATE, divide-as em partes indexadas e envia apenas uma mensagem por vez. A especificação limita as mensagens a 64 KB, o que é um lembrete útil de que esse transporte é para sincronização e propagação local, não para transferência em massa.

## Modelo de sincronização

Depois que uma conexão é estabelecida, os peers usam um fluxo de sincronização half-duplex baseado em mensagens de negentropia [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md), como `NEG-OPEN`, `NEG-MSG`, `EVENT` e `EOSE`. Essa escolha de design é importante porque permite que as implementações reutilizem a lógica de sincronização relay existente em vez de construir um algoritmo de replicação somente BLE.

A regra half-duplex também reflete a realidade dos links BLE instáveis. Conexões intermitentes de curto alcance funcionam melhor quando cada lado sabe exatamente de quem é a vez de falar.

## Por que é importante

O NIP-BE oferece aos aplicativos Nostr um caminho para redes locais. Dois telefones podem sincronizar notas ou estado relay diretamente quando estão próximos um do outro, mesmo que nenhum deles tenha internet funcionando. Isso torna o BLE útil para resistência à censura, cenários de desastres e aplicativos sociais de baixa conectividade.

As restrições são igualmente importantes: a largura de banda do BLE é baixa, as conexões têm vida curta e grandes históricos não se ajustam bem. Na prática, o NIP-BE é melhor para sincronização incremental e propagação de mensagens próximas, e não para replicação completa de arquivamento.

---

**Fontes primárias:**
- [Especificação NIP-BE](https://github.com/nostr-protocol/nips/blob/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)

**Mencionado em:**
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
