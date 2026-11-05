---
title: "NIP-31: Lidando com tipos de evento desconhecidos"
date: 2026-11-04
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-31.md
translationDate: 2026-11-05
---

> **Aviso de status:** A [especificação NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md) atual se marca como `unrecommended` por ser "desnecessariamente inchada", e sua linha de status diz rascunho, não recomendada e opcional. Os relays já guardam eventos que usam essa convenção, então esta página explica como os clientes os leem. Ela não recomenda a NIP-31 para novos protocolos.

A NIP-31 define uma tag `alt` de nível superior. A tag contém um breve resumo em texto simples para kinds de evento personalizados que não foram feitos para ser lidos como notas de texto comuns.

## Como Funciona {#how-it-works}

O autor de um evento de kind personalizado adiciona uma tag `alt` com um rótulo que uma pessoa consegue ler. Clientes construídos em torno do kind 1 não precisam assinar todos os kinds que não reconhecem. Seus usuários ainda podem se deparar com um evento desses quando uma nota o referencia, e o rótulo dá algum contexto mesmo que o cliente não implemente aquele kind.

Fragmento de tag, não um evento completo:

```
["alt", "<short plaintext summary>"]
```

Um rótulo legível cobre apenas a exibição. Ele não pode registrar um voto, atender a um pedido de carteira nem executar qualquer outra ação nativa do kind. Para interações mais ricas, a especificação aponta para a [NIP-89: Handlers de aplicativos recomendados](/pt/topics/nip-89/).

## Implementações {#implementations}

No [card de evento desconhecido do noStrudel no commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), a primeira tag `alt` tem os espaços aparados e se torna o rótulo principal, com uma linha opcional `Using <client>`. Um valor ausente ou em branco gera `Unknown event (kind ...)`, e até três linhas de conteúdo aparecem por conta própria. O mesmo componente resolve a tag `client` por meio de templates de handlers NIP-89. Ele mostra um botão Open quando existe um endereço compartilhável e `Open in <client>` quando um link de handler válido é resolvido. A explicação e o despacho para o app são controles separados.

O [UnknownEventDigest.kt do Amethyst no commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) prefere conteúdo que classifica como prosa e recorre ao `alt` como alternativa. Seu parser apara os valores e pega o primeiro `alt` não vazio. Como resultado, um evento cujo primeiro `alt` está em branco pode receber aqui um rótulo diferente do que recebe no noStrudel. Ambas as descrições refletem o código-fonte nesses commits. Nenhuma delas confirma como uma versão lançada se comporta.

## Limitações {#limits}

- `alt` é uma tag, então o ID do evento e a assinatura definidos na [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) a cobrem. Uma assinatura válida mostra que o autor publicou o rótulo. Ela não mostra que o rótulo é preciso, então um resumo pode enganar.
- Tags são públicas. Um `alt` em um evento com conteúdo criptografado expõe seu resumo e pode revelar o que o conteúdo esconde.
- As duas propriedades acima vêm do envelope de evento da NIP-01. O próprio texto da NIP-31 não as estabelece como requisitos.
- Uma tag `alt` de nível superior é diferente do campo `alt` de descrição de imagem dentro de `imeta`, e os renderizadores os interpretam separadamente.

---

**Fontes primárias:**
- [Especificação NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [embedded-unknown.tsx do noStrudel no commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [UnknownEventDigest.kt do Amethyst no commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**Mencionado em:**
- [Newsletter #47: Mergulho em NIP](/pt/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**Veja também:**
- [NIP-89: Handlers de aplicativos recomendados](/pt/topics/nip-89/)
- [NIP-73: IDs de conteúdo externo](/pt/topics/nip-73/)
- [NIP-01: Descrição do fluxo básico do protocolo](/pt/topics/nip-01/)
