---
title: 'TollGate: Internet pay-per-use sobre Nostr e Cashu'
date: 2026-04-22
draft: false
categories:
  - Protocols
translationOf: /en/topics/tollgate.md
translationDate: 2026-04-22
---

TollGate é um protocolo para vender acesso à rede em troca de pequenos pagamentos frequentes com ativos bearer. Um dispositivo capaz de controlar conectividade, como um roteador WiFi, um switch Ethernet ou um tether Bluetooth, atua como um TollGate que anuncia preços, aceita tokens de ecash [Cashu](/pt/topics/cashu/) e gerencia sessões. Clientes pagam exatamente pelos minutos ou megabytes que consomem. Não há contas, não há assinaturas, não há KYC.

## Como funciona

TollGate separa responsabilidades em três camadas. A camada de protocolo define os formatos de evento e a semântica de pagamento. A camada de interface define como cliente e gate trocam esses eventos. A camada de meio descreve o link físico que carrega o tráfego pago. Um TollGate funcional combina uma spec de cada camada, e algumas interfaces rodam sobre relays Nostr enquanto outras rodam sobre HTTP simples.

Na camada de protocolo, [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) define três eventos base: um kind Advertisement que lista preços e mints aceitas, um kind Session que acompanha quanto o cliente pagou e quanto consumiu, e um kind Notice para mensagens fora de banda. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) adiciona pagamentos Cashu sobre isso, para que um cliente possa resgatar tokens de ecash de qualquer mint anunciada pelo TollGate e receber crédito de sessão em troca.

Na camada de interface, [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) até HTTP-03 definem a superfície HTTP para dispositivos em sistemas operacionais restritivos que não conseguem abrir facilmente conexões WebSocket para relays arbitrários, e [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) define o transporte via relay Nostr para clientes que conseguem. Na camada de meio, [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) descreve como uma configuração WiFi com captive portal identifica e roteia clientes pagantes.

Como o ativo de pagamento é um bearer token, e não uma credencial, o cliente não precisa de acesso prévio à internet para produzi-lo. Um token Cashu em uma carteira local já basta para comprar o primeiro minuto de conectividade, e depois o cliente pode recarregar com mais tokens conforme necessário. TollGates também podem comprar uplink uns dos outros, então o alcance vai além de um único operador.

## Por que importa

WiFi pago convencional depende de contas, captive portals e cartões de pagamento, cada um criando atrito e uma trilha de dados. O modelo do TollGate transforma conectividade em uma commodity que qualquer roteador pode vender a qualquer cliente pagante sem saber quem ele é. Essa abstração permite que operadores independentes definam seus próprios preços, aceitem suas mints preferidas e concorram por cobertura e qualidade, não por lock-in.

O [release v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) é o primeiro snapshot com tag dessas especificações. Ele não padroniza todos os detalhes, mas fixa superfície suficiente para que firmware de roteadores, carteiras cliente e revendedores multi-hop comecem a construir sobre uma referência estável.

---

**Fontes primárias:**
- [TollGate v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01: eventos base](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02: pagamentos Cashu](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 até HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [Repositório TollGate](https://github.com/OpenTollGate/tollgate)

**Mencionado em:**
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [Cashu](/pt/topics/cashu/)
- [NIP-60: Carteira Cashu](/pt/topics/nip-60/)
