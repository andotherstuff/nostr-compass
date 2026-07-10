---
title: "NIP-F4: Podcasts"
date: 2026-06-03
draft: false
translationOf: /en/topics/nip-f4.md
translationDate: 2026-07-01
categories:
  - NIPs
  - Protocol
  - Media
---

NIP-F4 define como clientes Nostr referenciam, exibem e interagem socialmente com episódios de podcast. Mesclado em 2026-05-28 após dois anos e três meses em rascunho, a especificação usa eventos de kind 54 para episódios e é projetada em torno da pilha existente de podcasting via RSS como uma camada complementar.

## Como funciona

Um evento de episódio de podcast kind 54 carrega uma tag `title`, uma tag `image` opcional, uma tag `description`, uma ou mais tags `imeta` para o arquivo de áudio (URL, tipo mime, hash, duração, bitrate, código de idioma, URLs de fallback, flag de serviço NIP-96), tags de tópico `t` e uma tag `alt` NIP-31 para exibição de fallback.

A escolha de projeto que carrega o peso é a tag `i`, que carrega o GUID RSS do episódio no formato `podcast:item:guid:<guid>`. Isso permite:

- Que um cliente Nostr exiba um evento kind 54 e o linke de volta ao mesmo episódio em qualquer app de podcast compatível com RSS
- Que um cliente Nostr compatível com RSS exponha episódios de um podcast existente como eventos kind 54 sem forçar o podcaster a migrar de hospedagem
- Encadeamento de comentários entre protocolos via as tags `<podcast:socialInteract>` e `<podcast:chat>` do Podcasting 2.0

## Coexistência com RSS

O debate de dois anos na thread do PR (com o coautor do Podcasting 2.0 Dave Jones, Alex Gleason, fiatjaf, Mike Terenzio, Pablo F7z e Jeff Gardner) se resolveu em coexistência. O Nostr fornece a camada social e de descoberta, enquanto o RSS mantém a fonte da verdade para o arquivo de áudio e os metadados do feed. O Nostr não duplica a camada de distribuição do RSS.

Isso contrasta com tentativas anteriores de substituir o RSS (JSONFeed, RSS 3.0, APIs proprietárias de podcast). O namespace do Podcasting 2.0 já suporta `<podcast:socialInteract>` referenciando eventos Nostr por note ID, então um feed RSS pode declarar sua thread de discussão Nostr companheira sem exigir que o Nostr espelhe o próprio feed.

## Exemplo de evento

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["imeta", "url https://podcast.example.com/audio/ep42.mp3", "m audio/mpeg", "x b2e0a7a82ac9f3f3a71f1d9a78c381d5be9d1cf19dce258765c17c8a76287c93", "duration 4523", "bitrate 192000", "l en ISO-639-1"],
    ["i", "podcast:item:guid:9b2a4c7d-1e3f-4a5b-8c9d-0e1f2a3b4c5d"],
    ["t", "podcasting"],
    ["alt", "Podcast episode: Why RSS Won (43 min)"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

## Implementações

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Tela dedicada de podcast com lista de episódios e player embutido (primeira implementação em cliente relevante, maio de 2026)
- [Wavlake](https://wavlake.com) - Maior plataforma nativa Nostr para música e podcasting, com expectativa de alinhamento ao kind 54 para conteúdo de podcast
- [Fountain](https://fountain.fm) - App de podcast Bitcoin, com expectativa de fazer a ponte entre RSS e NIP-F4

## Questões em aberto

A especificação mesclada mantém várias questões de projeto para as implementações convergirem:

- Pubkeys por criador são recomendadas mas não obrigatórias, então plataformas como o Wavlake, que publicam muitos criadores sob uma única pubkey, permanecem válidas
- Comentários e discussão por episódio usam o encadeamento genérico do NIP-22 e notas kind 1 da linha do tempo em vez de um kind dedicado de comentário de episódio
- Metadados por podcast (host, rede, idioma, licença) vivem seja nos metadados kind 0 do publicador, seja em um registro kind 54 separado de nível de podcast

---

**Fontes primárias:**
- [Especificação NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - Proposta original, mesclada em 2026-05-28 após dois anos de discussão
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Primeira implementação em cliente relevante

**Mencionado em:**
- [Newsletter #25: Atualizações de NIPs e Deep Dive](/pt/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)
- [Newsletter #27: Amethyst v1.12.0 traz carteiras Cashu, nutzaps, um driver CLINK e auto-recuperação Tor](/pt/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Veja também:**
- [NIP-22 (Comentários)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Tags alt)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (Metadados de Arquivo)](/pt/topics/nip-94/)
- [NIP-96 (Armazenamento de Arquivo HTTP)](/pt/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
