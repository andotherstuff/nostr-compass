---
title: "CLINK: Interface Lightning Comum para Chaves Nostr"
date: 2026-06-17
draft: false
translationOf: /en/topics/clink.md
translationDate: 2026-07-01
categories:
  - Payments
  - Lightning
---

CLINK (Common Lightning Interface for Nostr Keys) é um formato proposto de solicitação de pagamento que permite ao remetente pagar qualquer identidade com chave Nostr usando uma única interface noffer. Um noffer CLINK codifica a chave pública Nostr do destinatário mais metadados de roteamento suficientes para que a carteira do remetente construa um pagamento Lightning, um pagamento on-chain ou uma primitiva de liquidação futura que resolve para o destinatário. O destinatário publica um noffer por identidade, e os remetentes o pagam sem saber se a carteira receptora liquida via Lightning, on-chain ou outro trilho.

## Como funciona

Um noffer CLINK é uma solicitação de pagamento estruturada que a carteira do remetente decodifica em uma instrução de pagamento concreta. O noffer carrega:

- A chave pública Nostr do destinatário como raiz canônica de identidade
- Um ou mais endpoints de pagamento (URI de nó Lightning, dica de derivação de endereço on-chain, trilhos futuros)
- Metadados opcionais para o pagamento (memo, valor, expiração)
- Uma assinatura do destinatário vinculando o noffer à sua identidade Nostr

Uma carteira remetente que suporta CLINK lê o noffer, escolhe o trilho que pode servir (uma carteira apenas-Lightning paga o endpoint Lightning, uma carteira multi-trilho escolhe o caminho mais barato) e envia o pagamento. A carteira do destinatário confirma o recebimento publicando ou buscando o evento de conclusão correspondente, com a chave pública Nostr atuando como identidade durável entre os trilhos.

## Por que uma interface com chave Nostr

LNURL e BOLT-12 já existem como formatos de solicitação de pagamento Lightning, e o Bitcoin possui um formato de endereço bem conhecido para liquidação on-chain. CLINK não substitui nenhum deles. Ele adiciona uma camada enraizada em chave Nostr para que um remetente possa endereçar um destinatário por sua identidade Nostr e deixar a carteira resolver qual trilho subjacente usar. Um usuário que troca de provedor Lightning, abre uma nova mint ou migra sua carteira on-chain republica seu noffer com a mesma chave Nostr, e os remetentes não precisam atualizar seus catálogos de endereços.

Para o Zeus Pay (que gera um noffer CLINK para cada conta), isso significa que um remetente pode pagar qualquer usuário Zeus apenas pela chave Nostr. Para o driver de zap on-chain do Amethyst, a máquina de estados de verificação CLINK confirma que o noffer assinado on-chain corresponde à pubkey Nostr reivindicada na solicitação de zap, fechando um caminho de falsificação contra zaps on-chain não assinados.

## Implementações

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) traz suporte a pagamentos com noffer CLINK, com o Zeus Pay gerando um noffer CLINK para cada conta para que um remetente possa pagar qualquer usuário Zeus apenas pela chave Nostr
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) traz um driver CLINK para verificação de zaps on-chain com uma máquina de estados de verificação e um driver de reverificação ([PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039), [PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177), [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182))

---

**Fontes primárias:**
- [Notas de lançamento do Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - Envio de noffer CLINK
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - Máquina de estados de verificação de zaps on-chain NIP-BC e driver de reverificação
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - Implementação do CLINK (Common Lightning Interface for Nostr Keys)
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - Adiciona suporte a kotlinx-serialization para DTOs do protocolo CLINK

**Mencionado em:**
- [Newsletter #27: Amethyst v1.12.0 traz carteiras Cashu, nutzaps, um driver CLINK e auto-recuperação Tor](/pt/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #27: Zeus v13.1.0-rc1 traz noffers CLINK e NWC sem fila](/pt/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**Veja também:**
- [NIP-57: Zaps](/pt/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
