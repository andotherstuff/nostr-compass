---
title: "NIP-61: Nutzaps"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-61.md
translationDate: 2026-07-01
categories:
  - Zaps
  - Ecash
---

NIP-61 define os "nutzaps", pagamentos peer-to-peer de ecash Cashu entregues como eventos Nostr. Um remetente publica um token Cashu com bloqueio P2PK endereçado à chave Nostr do destinatário, e o destinatário o resgata na mint quando lhe for conveniente. As próprias provas carregam o valor, então um pagamento NIP-61 chega como um token autocontido que o destinatário pode resgatar no seu próprio ritmo, sem necessidade de canal Lightning ou handshake interativo.

## Como funciona

O NIP-61 se baseia em duas primitivas existentes: as carteiras Cashu do [NIP-60](/pt/topics/nip-60/) e os bloqueios P2PK do Cashu. O fluxo usa três kinds de evento.

**Recomendação de mint (kind 10019):** um evento replaceable que o destinatário publica para anunciar de quais mints aceita nutzaps e a chave pública Cashu usada para bloquear as provas para ele. Remetentes leem isso antes de enviar para que o token bloqueado seja um que o destinatário possa resgatar.

**Evento nutzap (kind 9321):** o próprio pagamento. Ele carrega as provas Cashu (bloqueadas por P2PK para a pubkey nutzap do destinatário obtida do kind 10019), a URL da mint, tags `e` e `a` opcionais identificando a nota zapada e uma tag `p` para o destinatário. O destinatário o recebe por meio das subscrições normais do Nostr, desbloqueia as provas com a chave privada correspondente e as mantém em sua carteira NIP-60 ou as derrete para Lightning.

**Info de nutzap (kind 7375):** estado em cache com o mesmo formato dos eventos de token do NIP-60, registrando as provas de nutzap já resgatadas para que a carteira não as conte em dobro em uma ressincronização.

## Tradeoffs e modelo de confiança

Um nutzap é um token de ecash autocontido. Enquanto o destinatário puder contatar a mint depois, ele poderá resgatar o pagamento. A própria mint é o custodiante confiável, o mesmo modelo de confiança do NIP-60, e essa escolha de custódia é o preço explícito por micropagamentos capazes de operar offline com finalidade instantânea. Os zaps NIP-57 exigem que o receptor rode (ou seja hospedado em) um nó Lightning com um endpoint LNURL que aceite HTLCs entrantes em tempo real. Celulares sem canal Lightning, usuários atrás de firewalls e destinatários que por acaso estão offline ficam todos fora desse modelo.

O anúncio kind 10019 é o portão de confiança da camada social. O remetente escolhe uma das mints aceitas pelo destinatário, o que mantém o caminho de resgate do destinatário previsível. Um remetente que escolhe uma mint fora do conjunto do destinatário corre o risco de um token não resgatável, então as carteiras leem o kind 10019 primeiro.

## Fluxo de trabalho

1. O destinatário publica um kind 10019 anunciando as mints aceitas e uma pubkey de nutzap
2. O remetente lê o kind 10019, cunha provas em uma das mints listadas e as bloqueia via P2PK para a pubkey nutzap do destinatário
3. O remetente publica um kind 9321 com as provas bloqueadas, a URL da mint e as tags de destino
4. O destinatário recebe o kind 9321 por meio de sua subscrição Nostr normal
5. O destinatário desbloqueia as provas usando sua chave privada de nutzap e as mantém em sua carteira NIP-60 ou as derrete para Lightning

## Exemplo de evento nutzap

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## Implementações

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) traz renderização de nutzap com visualizações de saldo por mint como parte de sua superfície de carteira NIP-60/NIP-61 ([PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075))

---

**Fontes primárias:**
- [Especificação NIP-61](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - Suporte a carteira Cashu NIP-60 e nutzap NIP-61

**Mencionado em:**
- [Newsletter #27: Amethyst v1.12.0 traz carteiras Cashu, nutzaps, um driver CLINK e auto-recuperação Tor](/pt/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Veja também:**
- [NIP-57: Zaps](/pt/topics/nip-57/)
- [NIP-60: Carteira Cashu](/pt/topics/nip-60/)
- [Cashu](/pt/topics/cashu/)
