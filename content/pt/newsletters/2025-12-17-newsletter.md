---
title: 'Nostr Compass #1'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
translationOf: /en/newsletters/2025-12-17-newsletter.md
translationDate: 2025-12-26
---

Bem-vindo ao Nostr Compass, um boletim semanal dedicado ao ecossistema do protocolo Nostr. Nossa missão é manter desenvolvedores, operadores de relays e construtores informados sobre desenvolvimentos importantes em toda a rede. Documentamos a evolução do protocolo com precisão técnica, neutralidade e profundidade, cobrindo desde propostas de NIP até lançamentos de clientes e melhores práticas de implementação.

O Nostr Compass é inspirado no [Bitcoin Optech](https://bitcoinops.org/), cujo trabalho dedicado ao longo dos anos avançando o conhecimento técnico do Bitcoin estabeleceu o padrão para boletins focados em protocolos. Somos gratos pelo exemplo deles e esperamos trazer o mesmo rigor ao ecossistema Nostr.

Esta edição inaugural estabelece nosso formato semanal. Toda quarta-feira traremos atualizações de NIP, notas de lançamento, destaques de desenvolvimento e orientação técnica. Seja você construindo um cliente, operando um relay ou contribuindo para o protocolo, o Nostr Compass pretende ser sua fonte confiável sobre o que está acontecendo no ecossistema.

## O que é Nostr?

*Como esta é nossa primeira edição, começamos com uma introdução sobre como o Nostr funciona. Leitores regulares podem [pular para frente](#notícias).*

Nostr (Notes and Other Stuff Transmitted by Relays) é um protocolo descentralizado para redes sociais e mensagens. Diferente das plataformas tradicionais, o Nostr não tem servidor central, nenhuma empresa o controla e não tem ponto único de falha. Os usuários possuem sua identidade através de pares de chaves criptográficas, e o conteúdo flui através de servidores relay independentes que qualquer pessoa pode executar.

**Como funciona:** Os usuários geram um par de chaves (uma chave privada chamada nsec e uma chave pública chamada npub). A chave privada assina mensagens chamadas "eventos", e a chave pública serve como sua identidade. Os eventos são enviados para relays, que os armazenam e encaminham para outros usuários. Como você controla suas chaves, pode trocar entre clientes ou relays sem perder sua identidade ou seguidores.

**Por que importa:** O Nostr fornece resistência à censura através da diversidade de relays (se um relay te banir, outros ainda podem servir seu conteúdo), portabilidade (sua identidade funciona em qualquer app Nostr) e interoperabilidade (todos os clientes Nostr falam o mesmo protocolo). Não há algoritmo decidindo o que você vê, sem anúncios e sem coleta de dados.

**O ecossistema hoje:** O Nostr suporta microblogging (como Twitter/X), conteúdo longo (como Medium), mensagens diretas, marketplaces, streaming ao vivo e mais. Os clientes incluem Damus (iOS), Amethyst (Android), Primal, Coracle e dezenas de outros. A integração com Lightning Network permite pagamentos instantâneos através de "zaps". O protocolo continua a evoluir através de NIPs (Nostr Implementation Possibilities), especificações impulsionadas pela comunidade que estendem a funcionalidade.

## Notícias {#news}

**NIP-BE Merged: Suporte Bluetooth Low Energy** - Uma nova capacidade significativa [chegou ao protocolo](https://github.com/nostr-protocol/nips/pull/1979). [NIP-BE](/pt/topics/nip-be/) especifica como aplicações Nostr podem se comunicar e sincronizar sobre Bluetooth Low Energy. Isso permite que apps capazes de funcionar offline sincronizem dados entre dispositivos próximos sem conectividade com internet. A especificação adapta padrões de relay WebSocket às restrições do BLE, usando compressão DEFLATE e mensagens fragmentadas para lidar com os pequenos tamanhos de MTU do BLE (20-256 bytes). Os dispositivos negociam papéis baseados na comparação de UUID, com o UUID mais alto se tornando o servidor GATT.

**MIP-05: Notificações Push que Preservam Privacidade** - O [Protocolo Marmot](/pt/topics/marmot/) publicou [MIP-05](/pt/topics/mip-05/) ([especificação](https://github.com/marmot-protocol/mips/blob/main/mip-05.md)), uma especificação para notificações push que mantêm a privacidade. Sistemas push tradicionais exigem que servidores conheçam tokens de dispositivo e identidades de usuário; MIP-05 resolve isso encriptando tokens de dispositivo com ECDH+HKDF e ChaCha20-Poly1305, usando chaves efêmeras para prevenir correlação. Um protocolo gossip de três eventos (kinds 447-449) sincroniza tokens encriptados entre membros do grupo, e as notificações usam gift wrapping [NIP-59](/pt/topics/nip-59/) com tokens chamariz para esconder tamanhos de grupo. Isso permite que WhiteNoise e outros clientes Marmot entreguem notificações oportunas sem comprometer a privacidade do usuário.

**Blossom BUD-10: Novo Esquema URI** - O protocolo de mídia [Blossom](/pt/topics/blossom/) está ganhando um esquema URI personalizado via [BUD-10](/pt/topics/bud-10/) ([especificação](https://github.com/hzrd149/blossom/blob/master/buds/10.md)). O novo formato `blossom:<sha256>.ext` incorpora hash de arquivo, extensão, tamanho, múltiplas dicas de servidor e pubkeys de autor para descoberta de servidor [BUD-03](/pt/topics/bud-03/). Isso torna links de blob mais resilientes que URLs HTTP estáticas ao permitir fallback automático entre servidores.

**Atualizações do Marketplace Shopstr** - O marketplace nativo Nostr [implementou Nostr Wallet Connect](https://github.com/shopstr-eng/shopstr/pull/202) ([NIP-47](/pt/topics/nip-47/)) para pagamentos, [adicionou expiração de listagens](https://github.com/shopstr-eng/shopstr/pull/203) usando [NIP-40](/pt/topics/nip-40/), e introduziu [códigos de desconto](https://github.com/shopstr-eng/shopstr/pull/210) para vendedores.

## Atualizações de NIP {#nip-updates}

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Novos NIPs:**
- **[NIP-BE](/pt/topics/nip-be/)** - Mensagens Bluetooth Low Energy e sincronização de dispositivos ([#1979](https://github.com/nostr-protocol/nips/pull/1979))
- **[NIP-63](/pt/topics/nip-63/)** - Padrão de Paywall/Conteúdo Premium para lidar com conteúdo restrito dentro do protocolo ([#2156](https://github.com/nostr-protocol/nips/pull/2156))

**Mudanças Significativas:**
- **[NIP-24](/pt/topics/nip-24/)** - Adicionado array opcional `languages` aos metadados de usuário Kind 0, permitindo que usuários especifiquem múltiplos idiomas preferidos usando tags IETF BCP 47 para melhor descoberta de conteúdo e correspondência de relay ([#2159](https://github.com/nostr-protocol/nips/pull/2159))
- **[NIP-69](/pt/topics/nip-69/)** - Adicionado suporte de expiração de ordem para trading P2P com tags `expires_at` e `expiration` ([#2118](https://github.com/nostr-protocol/nips/pull/2118))
- **[NIP-59](/pt/topics/nip-59/)** - Eventos gift wrap agora podem ser deletados via requisições NIP-09/NIP-62 ([#2131](https://github.com/nostr-protocol/nips/pull/2131))
- **[NIP-51](/pt/topics/nip-51/)** - Removidas tags de hashtag e URL de marcadores genéricos; hashtags agora usam kind 30015 ([#2133](https://github.com/nostr-protocol/nips/pull/2133))
- **[NIP-18](/pt/topics/nip-18/)** - Melhorados reposts genéricos para eventos substituíveis com suporte a tag `a` ([#2132](https://github.com/nostr-protocol/nips/pull/2132))
- **[NIP-17](/pt/topics/nip-17/)** - Redação refinada e adicionado suporte a reação kind 7 para DMs ([#2098](https://github.com/nostr-protocol/nips/pull/2098))
- **[NIP-11](/pt/topics/nip-11/)** - Adicionado campo `self` para identificação de chave pública do relay ([#1764](https://github.com/nostr-protocol/nips/pull/1764))

## Aprofundamento em NIP: NIP-01 e NIP-19 {#nip-deep-dive-nip-01-and-nip-19}

Para esta edição inaugural, cobrimos dois NIPs fundamentais que todo desenvolvedor Nostr deve entender. Consulte nossas páginas de tópicos para [NIP-01](/pt/topics/nip-01/) e [NIP-19](/pt/topics/nip-19/).

### NIP-01: Protocolo Básico

[NIP-01](/pt/topics/nip-01/) define o protocolo central. Tudo no Nostr é construído sobre esta especificação.

**Eventos** são o único tipo de objeto. Cada evento contém:
- `id`: Hash SHA256 do evento serializado (o identificador único do evento)
- `pubkey`: A chave pública do criador (hex de 32 bytes, secp256k1)
- `created_at`: Timestamp Unix
- `kind`: Inteiro categorizando o tipo de evento
- `tags`: Array de arrays para metadados
- `content`: O payload (interpretação depende do kind)
- `sig`: Assinatura Schnorr provando que a pubkey criou este evento

**Kinds** determinam como relays armazenam eventos:
- Eventos regulares (1, 2, 4-44, 1000-9999): Armazenados normalmente, todas as versões mantidas
- Eventos substituíveis (0, 3, 10000-19999): Apenas o mais recente por pubkey é mantido
- Eventos efêmeros (20000-29999): Não armazenados, apenas encaminhados para assinantes
- Eventos endereçáveis (30000-39999): Mais recente por combinação pubkey + kind + d-tag

Kind 0 são metadados de usuário (perfil), kind 1 é uma nota de texto (o post básico), kind 3 é a lista de seguidos.

**Kind 1: Notas de Texto** são o coração do Nostr social. Um evento kind 1 é um post curto, similar a um tweet. O campo `content` contém o texto da mensagem (texto puro, embora clientes frequentemente renderizem markdown). Tags permitem respostas, menções e referências:

```json
{
  "id": "<32-byte-hex>",
  "pubkey": "<32-byte-hex>",
  "created_at": 1734480000,
  "kind": 1,
  "content": "Olá Nostr! Confira o trabalho do @jb55 no Damus.",
  "tags": [
    ["e", "<replied-to-event-id>", "wss://relay.example.com", "reply"],
    ["p", "<jb55-pubkey>"]
  ],
  "sig": "<64-byte-hex>"
}
```

A tag `e` com marcador "reply" indica que isso é uma resposta (veja [NIP-10](/pt/topics/nip-10/) para convenções de threading). A tag `p` menciona um usuário, permitindo que clientes o notifiquem e renderizem seu nome ao invés da pubkey crua. Clientes buscam o evento kind 0 do usuário mencionado para obter seu nome de exibição e foto.

Para construir uma timeline, um cliente se inscreve em eventos kind 1 de pubkeys seguidas: `["REQ", "feed", {"kinds": [1], "authors": ["<pubkey1>", "<pubkey2>", ...], "limit": 50}]`. O relay retorna notas correspondentes, e o cliente as renderiza cronologicamente.

**Eventos endereçáveis** (30000-39999) funcionam como eventos substituíveis mas usam uma tag `d` como identificador adicional. O relay mantém apenas a versão mais recente de cada combinação pubkey + kind + d-tag. Isso permite artigos editáveis, listagens de produtos, ou qualquer caso onde você precisa de múltiplos itens substituíveis por usuário.

**Tags** são arrays onde o primeiro elemento é o nome da tag. Tags padrão de uma única letra (`e`, `p`, `a`, `d`, `t`) são indexadas por relays para consultas eficientes. Por exemplo, `["e", "<event-id>"]` referencia outro evento, `["p", "<pubkey>"]` referencia um usuário.

**Comunicação Cliente-Relay** usa conexões WebSocket com arrays JSON como mensagens. O primeiro elemento identifica o tipo de mensagem.

De cliente para relay:
- `["EVENT", <event>]` - Publica um evento no relay
- `["REQ", <sub-id>, <filter>, ...]` - Inscreve-se em eventos correspondentes ao(s) filtro(s)
- `["CLOSE", <sub-id>]` - Encerra uma inscrição

De relay para cliente:
- `["EVENT", <sub-id>, <event>]` - Entrega um evento correspondente à sua inscrição
- `["EOSE", <sub-id>]` - "Fim de eventos armazenados" - o relay enviou todos os correspondentes históricos e agora só enviará novos eventos conforme chegarem
- `["OK", <event-id>, <true|false>, <message>]` - Confirma se um evento foi aceito ou rejeitado (e por quê)
- `["NOTICE", <message>]` - Mensagem legível por humanos do relay

O fluxo de inscrição: cliente envia `REQ` com um ID de inscrição e filtro, relay responde com mensagens `EVENT` correspondentes, então envia `EOSE` para sinalizar que está em dia com o histórico. Após `EOSE`, qualquer nova mensagem `EVENT` é em tempo real. Cliente envia `CLOSE` quando terminar.

**Filtros** especificam quais eventos recuperar. Um objeto filtro pode incluir: `ids` (IDs de evento), `authors` (pubkeys), `kinds` (tipos de evento), `#e`/`#p`/`#t` (valores de tag), `since`/`until` (timestamps), e `limit` (máximo de resultados). Todas as condições dentro de um filtro usam lógica AND. Você pode incluir múltiplos filtros em um `REQ`, e eles se combinam com lógica OR - útil para buscar diferentes tipos de evento em uma inscrição.

### NIP-19: Identificadores Codificados em Bech32

[NIP-19](/pt/topics/nip-19/) define os formatos amigáveis para humanos que você vê em todo lugar no Nostr: npub, nsec, note e mais. Estes não são usados no protocolo em si (que usa hex), mas são essenciais para compartilhamento e exibição.

**Por que bech32?** Chaves hex brutas são propensas a erros ao copiar e difíceis de distinguir visualmente. A codificação bech32 adiciona um prefixo legível por humanos e checksum. Você pode distinguir imediatamente um `npub` (chave pública) de um `nsec` (chave privada) ou `note` (ID de evento).

**Formatos básicos** codificam valores brutos de 32 bytes:
- `npub` - Chave pública (sua identidade, segura para compartilhar)
- `nsec` - Chave privada (manter em segredo, usada para assinar)
- `note` - ID de evento (referencia um evento específico)

Exemplo: A pubkey hex `3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d` se torna `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

**Identificadores compartilháveis** incluem metadados usando codificação TLV (Type-Length-Value):
- `nprofile` - Perfil com dicas de relay (ajuda clientes a encontrar o usuário)
- `nevent` - Evento com dicas de relay, pubkey do autor e kind
- `naddr` - Referência de evento endereçável (pubkey + kind + d-tag + relays)

Estes resolvem um problema-chave: se alguém compartilha um ID de nota, como você sabe qual relay o tem? Um `nevent` agrupa o ID do evento com relays sugeridos, tornando o compartilhamento mais confiável.

**Importante:** Nunca use formatos bech32 no protocolo em si. Eventos, mensagens de relay e respostas NIP-05 devem usar hex. Bech32 é puramente para interfaces humanas: exibição, copiar/colar, códigos QR e URLs.

## Lançamentos {#releases}

**Amber v4.0.4** - O app assinador Android corrige um NullPointerException, melhora performance na tela de atividade e adiciona traduções para alguns tipos de evento. O lançamento anterior v4.0.3 adicionou UI renovada de encriptação/decriptação, exportação/importação de contas, tratamento de relay por conta, suporte a ping bunker e relatório de crashes. [Lançamento](https://github.com/greenart7c3/Amber/releases/tag/v4.0.4)

**Coracle 0.6.28** - Lançamento de correção de bugs para o cliente web. Corrigidos feeds de tópicos, tratamento de imagens quando imgproxy está desabilitado, e linkificação de fontes de destaque que não são links. [Lançamento](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.6.2** - O cliente de comunidades estilo Discord corrige scroll modal e problemas de estilo. Lançamentos anteriores neste ciclo adicionaram badges e sons opcionais para notificações, renderização de links melhorada, escaneamento de código QR para links de convite e configuração de carteira simplificada. [Lançamento](https://github.com/coracle-social/flotilla/releases/tag/1.6.2)

**nak v0.17.2** - A ferramenta de linha de comando Nostr adicionou um novo comando `nip` para consulta rápida de referência NIP, além de correções para tratamento de repositório git e processamento de eventos stdin. [Lançamento](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**White Noise v0.2.1** - Lançamento maior para o app de mensagens encriptadas baseado em MLS adicionando compartilhamento de imagens via Blossom, sincronização em background, notificações push, localização em 8 idiomas e gerenciamento de membros de grupo. [Lançamento](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - Lançamento com novas funcionalidades introduzindo listas/packs de seguidos, novos filtros de timeline, galeria de imagens e compressão de vídeo H.265 (arquivos 50% menores). Migração completa para Kotlin Multiplatform. [Lançamento](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - Atualização do bot de trading P2P com suporte a expiração de ordem NIP-69 e respostas melhoradas de histórico de trades. [Lançamento](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

**Nosflare v8.9.26** - Relay Nostr serverless construído na infraestrutura Cloudflare. Este lançamento entrega um hotfix crítico abordando um bug que poderia causar falhas de websocket, garantindo conexões mais estáveis para usuários e aplicações que dependem do relay. [Lançamento](https://github.com/Spl0itable/nosflare/releases/tag/v8.9.26)

**Noscall v0.4.1** - App de chamadas de áudio e vídeo seguras baseado em Nostr. Este lançamento melhora a UI pop-up na página Me e corrige vários problemas conhecidos, resultando em melhor estabilidade e confiabilidade de chamadas. [Lançamento](https://github.com/sanah9/noscall/releases/tag/v0.4.1-release)

**Gitplaza v0.25.0** - Cliente de desktop Nostr focado em atividade relacionada a Git. Este lançamento introduz um filtro de kind avançado para o feed de inbox, inclui zaps regulares em filtros e simplifica a formatação de texto de abas. Melhorias de performance otimizam o carregamento da árvore de comentários, reduzem consultas desnecessárias ao banco de dados e usam branches de comentários em cache para exibição mais rápida. [Lançamento](https://codeberg.org/dluvian/gitplaza/releases/tag/v0.25.0)

## Mudanças notáveis de código e documentação {#notable-code-and-documentation-changes}

### Damus (iOS) {#damus}

Foco em estabilidade com correções de crash e UI: [correção de pulo de cursor](https://github.com/damus-io/damus/pull/3377) para a view de composição, [redesign da interface NostrDB](https://github.com/damus-io/damus/pull/3366) usando tipos `~Copyable` do Swift para segurança de transações, [estabilidade de UI de threads](https://github.com/damus-io/damus/pull/3341) corrigindo reinstanciação da barra de ações, [congelamento de lista de silenciados](https://github.com/damus-io/damus/pull/3346) por ciclos de AttributeGraph, e [crash de perfil](https://github.com/damus-io/damus/pull/3334) por limpeza de transação entre threads. Também adicionou diretrizes [AGENTS.md](https://github.com/damus-io/damus/pull/3293) para agentes de código IA.

### Notedeck (Desktop/Mobile) {#notedeck}

[Armazenamento seguro de chaves](https://github.com/damus-io/notedeck/pull/1191) move nsec para o armazenamento seguro do SO com migração automática. [Filtragem de notas futuras](https://github.com/damus-io/notedeck/pull/1201) esconde eventos datados 24+ horas à frente (anti-spam). [Cópia de nevent](https://github.com/damus-io/notedeck/pull/1183) agora inclui dicas de relay. Também: [adição rápida de coluna de perfil](https://github.com/damus-io/notedeck/pull/1212), [navegação por teclado](https://github.com/damus-io/notedeck/pull/1208), [otimização de carregamento de mídia](https://github.com/damus-io/notedeck/pull/1210).

### Amethyst (Android) {#amethyst}

Suporte a [assinatura remota NIP-46](https://github.com/vitorpamplona/amethyst/pull/1555) para Nostr Connect. [Organização de marcadores](https://github.com/vitorpamplona/amethyst/pull/1586) com gerenciamento de lista pública/privada. [Correção de compatibilidade strfry](https://github.com/vitorpamplona/amethyst/pull/1596) para casos extremos de parsing de info de relay.

### Primal (Android) {#primal-android}

[Deep links de Nostr Connect](https://github.com/PrimalHQ/primal-android-app/pull/788) para URLs `nostrconnect://`. [Login remoto](https://github.com/PrimalHQ/primal-android-app/pull/787) via scan de QR para conexões bunker. [Correção de condição de corrida de conexão](https://github.com/PrimalHQ/primal-android-app/pull/783).

### White Noise (Mensagens Encriptadas) {#white-noise}

[Correção de retenção de dados do app](https://github.com/marmot-protocol/whitenoise/pull/890) desabilita auto-backup do Android para privacidade. [Comportamento de scroll do chat](https://github.com/marmot-protocol/whitenoise/pull/861) preserva posição ao ler histórico.

### Zeus (Carteira Lightning) {#zeus}

[Pagamentos paralelos NIP-47](https://github.com/ZeusLN/zeus/pull/3407) para melhor throughput de zaps em lote.

## Melhores Práticas para Desenvolvedores

**Valide Eventos Auth Defensivamente** - go-nostr corrigiu um [panic na validação NIP-42](https://github.com/nbd-wtf/go-nostr/pull/182) quando a tag relay estava faltando. Sempre verifique as tags requeridas antes de acessá-las, mesmo em fluxos auth onde você espera eventos bem formados.

**Limite Taxa por Estado de Autenticação** - khatru adicionou [limitação de taxa baseada em NIP-42](https://github.com/fiatjaf/khatru/pull/57), permitindo que relays apliquem limites diferentes para conexões autenticadas vs anônimas. Considere limites escalonados baseados em status auth ao invés de restrições gerais.

**Use Paginação por Cursor para Listas** - Blossom [substituiu paginação baseada em data](https://github.com/hzrd149/blossom/pull/65) com paginação baseada em cursor no endpoint `/list`. Paginação baseada em data quebra quando itens compartilham timestamps; cursores fornecem iteração confiável.

**Validação de Schema para Tipos de Evento** - O projeto [nostrability/schemata](https://github.com/nostrability/schemata) fornece schemas JSON para validar eventos compatíveis com NIP. Considere integrar validação de schema em desenvolvimento para capturar eventos malformados antes que cheguem aos relays.

---

Isso é tudo por esta semana. Construindo algo? Tem notícias para compartilhar? Quer que a gente cubra seu projeto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via NIP-17 DM</a> ou nos encontre no Nostr.
