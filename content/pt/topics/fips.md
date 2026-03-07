---
title: FIPS
date: 2026-02-25
draft: false
categories:
- Protocol
- Networking
- Infrastructure
translationOf: /en/topics/fips.md
translationDate: '2026-03-07'
---

FIPS (Free Internetworking Peering System) é um protocolo de rede mesh auto-organizado que usa pares de chaves secp256k1 estilo Nostr como identidades de nó.

## Como funciona

FIPS visa fazer com que a rede ponto a ponto funcione sem servidores centrais ou autoridades de certificação. Os nós descobrem vizinhos, constroem estados de roteamento e encaminham pacotes usando apenas conhecimento local.

O design combina uma árvore geradora com dados de acessibilidade do filtro Bloom. Cada nó obtém coordenadas relativas à árvore e depois roteia avidamente em direção ao destino. Se o roteamento ganancioso falhar, a árvore ainda fornecerá um caminho alternativo.

Duas camadas de criptografia protegem o tráfego. A criptografia da camada de link (padrão Noise IK) protege a comunicação salto a salto entre vizinhos. A criptografia da camada de sessão (padrão Noise XK) fornece proteção ponta a ponta contra roteadores intermediários.

## Por que é importante

FIPS reutiliza o mesmo modelo-chave que os desenvolvedores do Nostr já entendem, mas o aplica ao roteamento de pacotes em vez de eventos sociais. Isso proporciona uma história de identidade simples: a identidade da rede é a chave criptográfica, não uma alocação de IP ou cadeia de certificados.

O design independente de transporte também é importante. O mesmo modelo de roteamento e identidade pode, em princípio, ser executado em UDP, Ethernet, Bluetooth ou LoRa, o que torna o FIPS interessante para ambientes de rede hostis ou não confiáveis.

## Status de implementação

Conforme abordado no Compass, a implementação atual do Rust já inclui transporte UDP funcional e descoberta baseada em filtro Bloom. A inicialização baseada em relay ainda é um trabalho futuro, então hoje o protocolo é mais um substrato de rede do que um substituto final do Nostr relay.

---

**Fontes primárias:**
- [Repositório FIPS](https://github.com/jmcorgan/fips)
- [Documentação do Projeto](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**Mencionado em:**
- [Boletim informativo nº 11: Notícias FIPS](/pt/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Boletim informativo nº 12](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [Protocolo Marmot](/pt/topics/marmot/)
