---
title: 'Nostr Compass #18'
date: 2026-04-15
translationOf: /en/newsletters/2026-04-15-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) mergeia 29 PRs, incluindo suporte a Tor no desktop, uma implementação customizada em C de secp256k1 com bindings JNI, um sistema completo de chamadas WebRTC para [NIP-AC](/pt/topics/nip-ac/), conformidade MLS com RFC 9420 para [Marmot](/pt/topics/marmot/) e suporte a múltiplas carteiras NWC. [nstrfy](https://github.com/vcavallo/nstrfy-android) estreia como app Android de push notifications nativo de Nostr usando eventos kind `7741`. [HAMSTR](https://github.com/LibertyFarmer/hamstr) adiciona rede mesh Reticulum, levando eventos Nostr a LoRa sem conexão de internet. [Bloom](https://github.com/nostrnative/bloom) lança a v0.1.0 como app desktop que empacota um servidor de mídia [Blossom](/pt/topics/blossom/) e um relay Nostr. [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) estreia com a v0.1.0 como diretório e player de rádio na internet construído sobre Nostr. [Botburrow](https://github.com/marmot-protocol/botburrow) inicia desenvolvimento como plataforma self-hosted de bots para chats em grupo criptografados com [Marmot](/pt/topics/marmot/). [Snort](https://github.com/v0l/snort) lança v0.5.0 até v0.5.3 com auditoria de segurança, verificação WASM em lote e um sistema de mensagens reescrito. [Primal Android](https://github.com/PrimalHQ/primal-android-app) redesenha seu layout de feed.

## Top Stories

### Amethyst mergeia Tor no desktop, secp256k1 em C, chamadas WebRTC e NWC com múltiplas carteiras

[Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android mantido por vitorpamplona, mergeou 29 PRs nesta semana em criptografia, networking, chamadas e infraestrutura de carteiras.

O [PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381) é a maior mudança, adicionando suporte a Tor no desktop ao embutir um daemon kmp-tor com design fail-closed. Se Tor estiver habilitado, todas as conexões com relays passam pelo processo Tor embutido, e o app se recusa a conectar se o Tor falhar ao iniciar. O roteamento com foco em privacidade agora alcança paridade entre as builds Android e desktop, com mais de 130 testes unitários cobrindo a integração Tor.

O [PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374) adiciona uma implementação customizada em C de secp256k1 com bindings JNI para verificação de assinaturas. A implementação usa decomposição GLV, codificação de pontos wNAF e SHA-256 acelerado por hardware em arquiteturas x86_64 e ARM64. O resultado é um ganho de velocidade de 2x a 3x na verificação de assinaturas Schnorr em comparação com o caminho anterior em Kotlin puro. PRs adicionais da série, [PR #2188](https://github.com/vitorpamplona/amethyst/pull/2188), [PR #2195](https://github.com/vitorpamplona/amethyst/pull/2195) e [PR #2204](https://github.com/vitorpamplona/amethyst/pull/2204), adicionam operações fused multiply-reduce, uma struct Fe4 dedicada no lugar de LongArray para armazenamento de field elements e intrinsics específicas de plataforma para um ganho estimado de 28% no Android.

O [PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202) atualiza a implementação MLS em Kotlin puro para cumprir a RFC 9420, adicionando verificações de reuse guard, additional authenticated data, derivação de amostras de ciphertext, correções no processamento de commits e thread safety para integração com o protocolo [Marmot](/pt/topics/marmot/). Em cima do [trabalho de MLS em Kotlin da semana passada](/en/newsletters/2026-04-08-newsletter/), isso aproxima o [Quartz](/pt/topics/quartz/) da conformidade completa com a spec MLS.

Uma série de PRs WebRTC, do [PR #2203](https://github.com/vitorpamplona/amethyst/pull/2203) ao [PR #2211](https://github.com/vitorpamplona/amethyst/pull/2211), adiciona um sistema completo de chamadas de voz e vídeo para [NIP-AC](/pt/topics/nip-ac/). A implementação cobre ICE restart para conexões interrompidas, troca de câmera em runtime, monitoramento de rede com reconexão automática, settings configuráveis de chamada, incluindo resolução, bitrate e seleção de servidor TURN, correção de foreground service para restrições em background do Android 14+ e thread safety em toda a máquina de estados de chamadas.

O [PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988) adiciona suporte a [NIP-47](/pt/topics/nip-47/) com múltiplas carteiras, ou Nostr Wallet Connect. Usuários agora podem conectar várias carteiras NWC a uma única conta, ver cartões de saldo de cada uma, escolher uma carteira padrão e migrar da configuração legada de carteira única.

O [PR #2189](https://github.com/vitorpamplona/amethyst/pull/2189) adiciona conversão de GIF para MP4 com slider de qualidade, comprimindo um GIF de 3 MB para cerca de 159 KB em MP4. A mesma semana também trouxe sugestões de tom no composer com detecção automática de idioma e pré-computação paralela das sugestões.

### nstrfy estreia com push notifications nativas de Nostr para Android

[nstrfy](https://github.com/vcavallo/nstrfy-android) estreou em 13 de abril com três releases, da [v1.0.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.0.0) à [v1.2.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.2.0). O app é um fork do ntfy-android em que o transporte HTTP foi substituído por Nostr. Em vez de ficar fazendo polling em um servidor por push notifications, o nstrfy assina eventos kind `7741` em relays configuráveis e os exibe como notificações nativas do Android.

O modelo de notificação suporta payloads em plaintext e payloads criptografados com [NIP-44](/pt/topics/nip-44/). Quando a criptografia está habilitada, o nstrfy usa [Amber](https://github.com/greenart7c3/Amber) para assinar via [NIP-55](/pt/topics/nip-55/) ou um nsec local. Assinaturas baseadas em tópico permitem configurar allowlists de remetentes por tópico com whitelist de npub, então apenas remetentes aprovados podem disparar notificações para um tópico específico. O app importa listas de relay do perfil do usuário usando [NIP-65](/pt/topics/nip-65/) e respeita expiração de eventos da [NIP-40](/pt/topics/nip-40/). Todo o vocabulário de notificações do ntfy é suportado, incluindo tap-to-open URLs, níveis de prioridade, ícones customizados e action buttons, então a maior parte dos alerts ao estilo ntfy se traduz diretamente. A busca de usuários é movida por NIP-50 com dados de [Web of Trust](/pt/topics/web-of-trust/) do brainstorm.world.

O projeto complementar [nstrfy.sh](https://github.com/vcavallo/nstrfy.sh) oferece tanto uma CLI em bash quanto um cliente web hospedado em [nstrfy.sh](https://nstrfy.sh) para envio e escuta a partir do navegador, com suporte a signer NIP-07. O app nativo está disponível no [Zapstore](https://zapstore.dev/apps/io.nstrfy.android).

### HAMSTR adiciona Reticulum para Nostr sobre mesh LoRa

[HAMSTR](https://github.com/LibertyFarmer/hamstr), o projeto que envia eventos Nostr e zaps Lightning por rádio amador, mergeou o [PR #10](https://github.com/LibertyFarmer/hamstr/pull/10) em 12 de abril, adicionando a rede mesh [Reticulum](https://reticulum.network/) como backend de transporte. Reticulum é um protocolo mesh criptográfico que roda sobre LoRa, HF, VHF/UHF, links seriais e TCP/IP. Com isso, o HAMSTR consegue retransmitir eventos Nostr por uma malha de dispositivos RNode sem infraestrutura de internet.

Os transportes AX.25 Packet Radio e VARA HF existentes continuam disponíveis, então operadores podem escolher o link de rádio que melhor se ajusta ao seu setup. A arquitetura de servidor zero-knowledge do HAMSTR significa que o relay nunca vê chaves privadas, e sua conformidade com [NIP-57](/pt/topics/nip-57/) garante que zaps Lightning offline apareçam corretamente em clientes como Amethyst e Primal. Um guia de setup para o transporte Reticulum está incluído em [RETICULUM.MD](https://github.com/LibertyFarmer/hamstr/blob/master/RETICULUM.MD). Na mesma semana, o [PR #11](https://github.com/LibertyFarmer/hamstr/pull/11) migrou o frontend para Svelte 5 e TailwindCSS v4.

## Shipping This Week

### Bloom v0.1.0 lança servidor Blossom self-hosted e relay

[Bloom](https://github.com/nostrnative/bloom) lançou seu primeiro release, a [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0), em 9 de abril. Construído com Tauri v2 e React 19, o Bloom empacota um servidor completo do protocolo [Blossom](/pt/topics/blossom/), de BUD-00 até BUD-10, e um relay Nostr em uma única aplicação desktop que roda em macOS, Windows e Linux, com builds Android e iOS planejadas. Usuários ganham armazenamento soberano de arquivos com endereçamento por conteúdo via SHA-256, suporte a metadados de arquivo [NIP-94](/pt/topics/nip-94/) e resolução do esquema URI `blossom://` sem precisar administrar infraestrutura de servidor. Dezesseis assets binários específicos de plataforma acompanham o release.

### WaveFunc v0.1.0 e v0.1.1 lançam rádio na internet sobre Nostr

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc) lançou a [v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0) e a [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) em 13 de abril, estreando como diretório e player de rádio na internet baseado em Nostr. Kinds de evento customizados definem o modelo de dados: kind `31237` para listagens de estações, kind `30078` para listas de favoritos, kind `1311` para chat ao vivo e kind `1111` para comentários em estações. Um backend de relay Khatru fornece armazenamento em SQLite e full-text search com Bluge, suportando [NIP-50](/pt/topics/nip-50/).

O WaveFunc vem com uma carteira [NIP-60](/pt/topics/nip-60/) Cashu e suporte a nutzaps, tendo migrado de NDK para applesauce-core. A [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) adiciona carrosséis de gênero, popover para doações via Lightning, gerenciamento de estações para usuários autenticados e listagem no Zapstore. A build desktop em Tauri v2 ganhou integração com system tray, suporte a media keys, autostart e deep linking. Há builds para macOS, Windows, Linux e Android em [wavefunc.live](https://wavefunc.live).

### Snort lança v0.5.0 até v0.5.3 com hardening de segurança e overhaul de performance

[Snort](https://github.com/v0l/snort), o cliente web Nostr em React, lançou três releases da [v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0) à [v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3). A v0.5.0 é a maior, trazendo uma auditoria de segurança abrangente com verificação real de assinaturas Schnorr, proteção reforçada em [NIP-46](/pt/topics/nip-46/) contra mensagens forjadas de relay, melhorias na criptografia de PIN e remoção da confiança em delegação [NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md) não verificada. As melhorias de desempenho incluem verificação de assinaturas em lote com WASM, rotas lazy-loaded, um carregador de perfis prioritários reescrito com batch loading e chunking e otimizações no worker relay. O release também adiciona exibição de invoice kind `7000` exigindo pagamento para DVMs da [NIP-90](/pt/topics/nip-90/). O [PR #620](https://github.com/v0l/snort/pull/620) reformulou o sistema de mensagens para performance, persistindo gift wraps no worker relay e substituindo o cálculo O(n²) da lista de chats por uma abordagem de passagem única baseada em Map.

### Primal Android lança 3.0.21 e redesenha o layout do feed

[Primal Android](https://github.com/PrimalHQ/primal-android-app) lançou a [v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21) com correções para votos de zap em enquetes, compartilhamento multi-conta de carteira e auto-reconnect do remote signer e do serviço de carteira. Sete PRs mergeadas vieram em seguida: o [PR #1008](https://github.com/PrimalHQ/primal-android-app/pull/1008) unifica o layout da tela principal, o [PR #1010](https://github.com/PrimalHQ/primal-android-app/pull/1010) implementa um novo design de card de feed com avatares maiores e indentação do conteúdo, o [PR #1009](https://github.com/PrimalHQ/primal-android-app/pull/1009) adiciona suporte a vídeo e layout retrato em cards de mídia, o [PR #1012](https://github.com/PrimalHQ/primal-android-app/pull/1012) introduz um campo de texto compacto para quick replies e o [PR #1013](https://github.com/PrimalHQ/primal-android-app/pull/1013) redesenha as app bars.

### Nostria v3.1.19 até v3.1.21 adiciona geração local de imagens com AI

[Nostria](https://github.com/nostria-app/nostria) lançou três releases da [v3.1.19](https://github.com/nostria-app/nostria/releases/tag/v3.1.19) à [v3.1.21](https://github.com/nostria-app/nostria/releases/tag/v3.1.21) com mais de 80 commits. A principal adição é geração local de imagens com Janus Pro usando aceleração WebGPU, permitindo que usuários gerem imagens no dispositivo sem API externa. Os releases também adicionam geração de imagens em nuvem, chat multimodal, suporte a ONNX runtime, uma biblioteca de prompts e gerenciamento de cache de AI. No lado do cliente, a atualização traz um novo sistema de diálogos, overhaul do editor de notas, melhorias em embeds de música e mudanças no fluxo de login com signer. A [Newsletter #17](/pt/newsletters/2026-04-08-newsletter/) cobriu o release mobile nativo v3.1.18 com suporte a signer local.

### TubeStr v1.0.3 lança atualizações no feed e no studio

[TubeStr](https://github.com/Tubestr/tubestr-v2), um app privado de compartilhamento de vídeos familiares construído sobre Nostr, lançou a [v1.0.3](https://github.com/Tubestr/tubestr-v2/releases/tag/v1.0.3) em 13 de abril. O release adiciona melhorias ao feed e ao studio. O [PR #3](https://github.com/Tubestr/tubestr-v2/pull/3) reformula as telas de onboarding e o [PR #2](https://github.com/Tubestr/tubestr-v2/pull/2) corrige um erro de exportação de vídeo. O app usa NDK e MDK, o Marmot Development Kit, para compartilhamento criptografado de mídia entre familiares, com integração [Blossom](/pt/topics/blossom/) planejada para armazenamento de mídia. O TubeStr está disponível no [Zapstore](https://zapstore.dev).

## In Development

### Botburrow começa o desenvolvimento como plataforma de bots para Marmot

[Botburrow](https://github.com/marmot-protocol/botburrow) é um novo projeto da equipe Marmot, iniciado em 3 de abril. É uma plataforma self-hosted de gerenciamento de bots em que cada bot recebe sua própria identidade Nostr, entra em chats de grupo criptografados com MLS do [Marmot](/pt/topics/marmot/) por meio de mensagens Welcome e envia e recebe mensagens end-to-end encrypted. O dashboard, construído com Rails 8.1, se comunica com um único daemon whitenoise-rs, `wnd`, por um socket Unix.

O Botburrow expõe uma camada substancial de scripts e operações: comandos, triggers e ações agendadas executam código Ruby customizado, scripts podem inspecionar perfis, membership de grupos e invites pendentes por meio do `wnd`, o dashboard inclui uma live chat view para trocar mensagens com bots em grupos reais, e cada bot tem seu próprio armazenamento de arquivos para configs, dados em cache e saída gerada. Uma [imagem Docker](https://github.com/marmot-protocol/botburrow/commit/2ed012078eaab3c5b92dff16b87865c2e353bd80) com builds multi-arch mira self-hosting sem configuração em Umbrel e Start9. Uma [seção sobre trust model](https://github.com/marmot-protocol/botburrow/commit/c8ef8c306af247560b1952878206d854cde3fe20) no README documenta as fronteiras de segurança.

### Nostr Archives adiciona relay de feeds em alta e resolução de entidades

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api), a plataforma de arquivamento e analytics em [nostrarchives.com](https://nostrarchives.com), seguiu em desenvolvimento constante em sua [API](https://github.com/barrydeen/nostrarchives-api), em Rust, e no [frontend](https://github.com/barrydeen/nostrarchives-frontend), em Next.js 16. Na API, o [PR #118](https://github.com/barrydeen/nostrarchives-api/pull/118) adiciona filtragem por intervalo de tempo ao leaderboard de clientes, e o [PR #117](https://github.com/barrydeen/nostrarchives-api/pull/117) adiciona contadores de engajamento a eventos de reply. No frontend, o [PR #85](https://github.com/barrydeen/nostrarchives-frontend/pull/85) resolve entidades Nostr diretamente a partir do path da URL, para que colar um npub ou note ID na URL faça o site renderizar o conteúdo, e o [PR #86](https://github.com/barrydeen/nostrarchives-frontend/pull/86) adiciona uma página de documentação da API. A plataforma roda quatro serviços de relay: um relay de busca NIP-50, um relay de feeds em alta, visível em `wss://feeds.nostrarchives.com`, um scheduler relay para eventos futuros e um indexer relay para kinds 0, 3 e 10002.

### Damus corrige a timeline de favoritos

[Damus](https://github.com/damus-io/damus), o cliente iOS, mergeou o [PR #3708](https://github.com/damus-io/damus/pull/3708), reescrevendo a função `subscribe_to_favorites()` com filtragem in-place, reconstrução de deduplicação e seleção persistida de abas.

### Nostur adiciona private zaps e visualização de emoji customizado

[Nostur](https://github.com/nostur-com/nostur-ios-public), o cliente iOS, publicou 10 commits nesta semana adicionando suporte a private zaps, visualização de emoji customizado, correção de renderização animada `.webp` e detecção de formato de áudio em mensagens de voz.

### Amber lança v6.0.1 até v6.0.3 com backup WebDAV e correções de reconexão a relays

[Amber](https://github.com/greenart7c3/Amber), o app signer Android da [NIP-55](/pt/topics/nip-55/), lançou três releases nesta semana. A [v6.0.1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.1) adiciona duas novas opções de backup, WebDAV e compartilhamento para Google Drive, implementa exponential backoff para reconexões com relays, atualiza a biblioteca Quartz para 1.08.0 e corrige validação de eventos de atualização do app e de perfil. A [v6.0.2](https://github.com/greenart7c3/Amber/releases/tag/v6.0.2) adiciona uma opção de índice de conta ao usar seed words e corrige a reconexão a relay quando o relay está offline no startup. A [v6.0.3](https://github.com/greenart7c3/Amber/releases/tag/v6.0.3) adiciona uma correção extra para request IDs vazios ao receber intents.

### Plektos v0.6.0 redesenha com temas Ditto

[Plektos](https://github.com/derekross/plektos), a plataforma descentralizada de meetups e eventos construída sobre [NIP-52](/pt/topics/nip-52/) com mapas interativos, lançou a [v0.6.0](https://github.com/derekross/plektos/commit/7a691cdf089ceb7a8582dd5c0ee026830f2cdc77) e a [v0.6.1](https://github.com/derekross/plektos/commit/3a6474ae380522d8ee1b3526423fcfc3328fd879) em 14 de abril. A atualização adiciona temas de comunidade ao estilo Ditto com upload de imagem de fundo, configuração do formato do avatar e overhaul de UI. O [PR #6](https://github.com/derekross/plektos/pull/6) responde a uma revisão completa de código cobrindo achados de segurança, arquitetura e UX. O Plektos usa Nostrify para integração de protocolo, [NIP-46](/pt/topics/nip-46/) para login remoto e zaps para pagamento de ingressos. A build Android está no Zapstore.

### Shadow adiciona Nostr OS API e app de carteira Cashu

[Shadow](https://github.com/justinmoon/shadow), a plataforma de runtime de apps do Justin Moon, publicou mais de 30 commits em dois dias. O [commit 88cbda5](https://github.com/justinmoon/shadow/commit/88cbda5131814d2730a2d892029932136db005df) adiciona um app de carteira Cashu rodando dentro do runtime Shadow. O [commit 865c415](https://github.com/justinmoon/shadow/commit/865c415) adiciona um demo de podcast player. O runtime expõe `Shadow.os.nostr` e `Shadow.os.audio` como APIs de nível de sistema, e a faixa Pixel do runtime roda um compositor Wayland em dispositivos Android com root e composição por GPU. Os [PR #1](https://github.com/justinmoon/shadow/pull/1) e [PR #2](https://github.com/justinmoon/shadow/pull/2), do colaborador k0sti, corrigem carregamento de fontes no desktop Linux e tratamento do diretório de estado XDG. Ainda não há release formal.

### Lief corrige login com Amber e adiciona Zapstore

[Lief](https://gitlab.com/chad.curtis/lief), um app Nostr para compor e enviar cartas long-form a outros usuários Nostr, lançou a build `v2026.04.12` em 12 de abril. A atualização corrige um problema de login com signer [Amber](https://github.com/greenart7c3/Amber) no Android, simplifica o fluxo de lembrete de signer, atualiza a dependência nostrify e adiciona integração com Zapstore.

### Espy reformula o color picker e corrige login com Amber

[Espy](https://gitlab.com/chad.curtis/espy), um app social Nostr em que usuários compartilham color moments, capturando paletas de 3 a 6 cores de cenas reais como forma de comunicação visual pré-verbal, lançou a build `v2026.04.12` em 12 de abril. A atualização reformula o color picker com um arco curvo de saturação no lugar do toggle em escala de cinza, corrige bugs de flicker no anel de matiz e adiciona personagens Easter egg, Alchemist e Astrologer. A compressão reduziu assets PNG em 703 KB. O release também corrige um problema de login com signer Amber, simplifica o fluxo de signer nudge, atualiza a dependência nostrify e adiciona integração com Zapstore.

### Jumble adiciona filtros de kind por feed e aba de artigos

[Jumble](https://github.com/CodyTseng/jumble), o cliente Nostr, publicou 13 commits nesta semana adicionando filtragem de kind por feed, uma aba Articles, sincronização de status de leitura de notificações com uma opção que preserva privacidade, um modo de ocultar avatar e correção de uma race condition na troca de conta.

### Primal Web lança 8 version bumps

[Primal Web](https://github.com/PrimalHQ/primal-web-app) lançou versões 3.0.93 até 3.0.101 em uma semana com 21 commits. O trabalho se concentrou em melhorias no chat de live stream, correções de limites de mentions, paginação de bookmarks, prevenção de likes duplicados e correções no relay proxy.

## Protocol and Spec Work

### NIP Updates

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-34](/pt/topics/nip-34/) (Git Stuff): adiciona URLs de clone `nostr://`** ([PR #2312](https://github.com/nostr-protocol/nips/pull/2312)): [NIP-34](/pt/topics/nip-34/) define como hospedar repositórios git no Nostr usando anúncios de repositório kind `30617` que listam branches, tags, localizações de relay e pubkeys de mantenedores. Até agora, a spec não tinha um esquema formal de URL para referenciar esses repositórios. Este PR adiciona um formato de clone URL `nostr://` que funciona com helpers `git-remote-nostr`, então `git clone nostr://npub1.../relay.ngit.dev/ngit` resolve o npub, ou endereço [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md), descobre as localizações de relay do repositório e busca os dados do repositório. Três padrões de URL são definidos: `nostr://<naddr>` para referências diretas a eventos endereçáveis, `nostr://<npub|nip05>/<identifier>` para referências legíveis por humanos e `nostr://<npub|nip05>/<relay-hint>/<identifier>` quando o cliente precisa de um relay hint. Tanto o relay hint quanto o identifier são percent-encoded conforme a RFC 3986. O formato já é implementado por Shakespeare e pelo helper git-remote-nostr do ngit, e exibido por GitWorkshop.dev e NostrHub.io. O PR também endurece o formato da tag `d` para identificadores de repositório, para que URLs `nostr://` produzam URIs válidas.

**Open PRs and Discussions:**

- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): propõe um novo evento replaceable kind `10164` que permite a criadores de conteúdo declarar payment gateways, modelos de preço e regras de assinatura para acesso a conteúdo pago. Hoje, conteúdo pago no Nostr exige que cada cliente implemente seu próprio fluxo de pagamento, sem forma padrão de um criador dizer que o conteúdo custa X sats via gateway Y. O evento proposto embutiria descritores de gateway diretamente em eventos Nostr, permitindo que clientes descubram métodos de pagamento aceitos, faixas de preço e opções de assinatura a partir de um único evento replaceable. Isso desacopla a apresentação de pagamento de provedores específicos, de forma que um criador poderia aceitar Lightning, Cashu ou gateways fiat sem exigir integração customizada em cada cliente.

- **NIP-XX: Relay Self-Declaration Manifest and Retention Horizon** ([PR #2314](https://github.com/nostr-protocol/nips/pull/2314)): propõe dois primitivos de wire protocol para transparência de relays. O primeiro é o kind `10100`, um evento replaceable gossipable em que operadores de relay declaram seus endpoints, em clearnet, Tor e I2P, janela de retenção, política de escrita e NIPs suportados. Diferente dos Relay Information Documents da [NIP-11](/pt/topics/nip-11/), que são entregues por HTTP e não podem ser descobertos pelo próprio Nostr, manifests kind `10100` se propagam pela rede de eventos Nostr como qualquer outro evento, com binding TOFU por meio do campo `pubkey` da NIP-11 para evitar spoofing. O segundo primitivo é `HORIZON`, uma nova mensagem relay-to-client `['HORIZON', <sub_id>, <earliest_timestamp>]` enviada antes de `EOSE`. Quando o intervalo temporal pedido por um cliente ultrapassa a janela de retenção do relay, o relay responde com o timestamp mais antigo que possui, trocando dead ends silenciosos por fronteiras temporais explícitas. A motivação é que o campo `retention` da NIP-11 foi removido em fevereiro de 2026 por falta de uso, porque a entrega apenas por HTTP falhou em distribuição. Uma implementação de referência roda no nostr-rs-relay 0.9.0 com pruning de 90 dias.

- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): propõe o kind `20411`, na faixa efêmera, para compartilhar geolocalização criptografada com destinatários específicos. Serviços centralizados de compartilhamento de localização como Google Maps e Apple Find My exigem confiar em uma autoridade central com movimentos em tempo real. Este NIP define uma alternativa privacy-first em que o conteúdo do evento contém um mapa JSON de pubkeys destinatárias para payloads criptografados com [NIP-44](/pt/topics/nip-44/), cada um contendo um geohash em nível de precisão configurável. Múltiplos destinatários são tratados em um único evento com criptografia por destinatário, então cada pessoa só pode descriptografar seu próprio payload. Uma tag `ttl` define o time-to-live sugerido em segundos, e a faixa efêmera de kinds sinaliza a relays que esses eventos não devem ser armazenados indefinidamente. As tags `p` permitem que clientes filtrem eventos relevantes sem descriptografar o conteúdo.

- **[NIP-5C](/pt/topics/nip-5c/) (Scrolls): atualização de programas WASM** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): continua o desenvolvimento da spec de publicação e execução de programas WebAssembly, que define convenções para publicar e descobrir binários WASM como eventos Nostr. Scrolls são programas autocontidos que clientes podem baixar de relays e executar em um runtime sandboxed, transformando o Nostr em uma rede de distribuição de código executável. O PR refina o formato do evento e a interface de runtime. Um [demo app](https://nprogram.netlify.app/) mostra scrolls rodando no navegador, com programas de exemplo publicados como eventos Nostr que qualquer cliente pode buscar e executar. O conceito estende a [NIP-5A](/pt/topics/nip-5a/), sites estáticos, da entrega de páginas HTML para a execução de programas interativos, tudo distribuído pela mesma infraestrutura de relays.

- **Suporte a payloads grandes na [NIP-44](/pt/topics/nip-44/)** ([PR #1907](https://github.com/nostr-protocol/nips/pull/1907)): propõe estender a criptografia versionada da NIP-44 para lidar com payloads maiores que o limite atual de 65.535 bytes. A mudança é backward compatible, então implementações que não precisam de mensagens grandes podem ignorá-la. A motivação prática é assinatura remota [NIP-46](/pt/topics/nip-46/) de listas grandes de contatos kind `3`, em que a lista de follows de um usuário pode ultrapassar o limite de tamanho quando serializada em JSON. Sem essa mudança, signers remotos não conseguem criptografar responses contendo grandes listas de contatos, forçando workarounds ou truncamento.

- **[NIP-C7](/pt/topics/nip-c7/): restringe kind 9 a views de chat** ([PR #2310](https://github.com/nostr-protocol/nips/pull/2310)): [NIP-C7](/pt/topics/nip-c7/) define o kind `9` como uma mensagem leve de chat, uma nota curta de texto destinada a conversa em tempo real em contextos de chat como grupos da [NIP-29](/pt/topics/nip-29/) e streams de live activities da [NIP-53](/pt/topics/nip-53/). Este PR adiciona o requisito de que clientes que renderizam uma chat view como stream de eventos ordenados DEVEM buscar apenas eventos kind `9`, evitando perda de contexto quando outros tipos de conteúdo, como notas kind `1` e artigos kind `30023`, se misturam à timeline do chat. Outros tipos de conteúdo ainda podem ser citados dentro de uma mensagem kind `9` seguindo reposts da [NIP-18](/pt/topics/nip-18/). A motivação vem de uma discussão comunitária sobre mensagens kind `9` aparecendo em feeds gerais sem contexto, já que mensagens de chat costumam ser respostas curtas que só fazem sentido dentro de um thread de conversa.

## NIP Deep Dive: NIP-29 (Relay-based Groups)

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md) define um modelo de mensagens em grupo em que o próprio relay gerencia membership e moderação. Grupos vivem em um relay específico, identificados por uma string aleatória de ID, e o relay impõe quem pode escrever no grupo. Essa é uma arquitetura diferente de [Marmot](/pt/topics/marmot/), com criptografia MLS do lado do cliente, ou de chats em grupo da [NIP-17](/pt/topics/nip-17/), com gift-wrapped DMs: na NIP-29, o relay é a autoridade, as mensagens podem ser lidas pelo operador do relay e a moderação acontece no nível do relay.

Um grupo é identificado pelo formato `<host>'<group-id>`, por exemplo `groups.nostr.com'abcdef`. O ID especial `_` é reservado como grupo de topo para discussão em nível de relay. Todos os eventos de usuário enviados ao grupo carregam uma tag `h` com o ID do grupo:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744675200,
  "kind": 9,
  "tags": [
    ["h", "abcdef"],
    ["previous", "a1b2c3d4", "e5f67890", "12345678"]
  ],
  "content": "Has anyone tested the new relay config?",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

A tag `previous` funciona como mecanismo de detecção de adulteração. Clientes incluem os primeiros 8 caracteres hex dos eventos recentes vistos no mesmo relay dentro das últimas 50 mensagens. Relays rejeitam eventos com referências `previous` a eventos fora do banco, o que impede replay de mensagens para uma cópia bifurcada do grupo em outro relay. Não é uma cadeia completa de custódia, mas torna rebroadcasts fora de contexto detectáveis.

A membership é gerenciada por um conjunto de kinds de moderação na faixa `9000-9020`. Um usuário entra publicando um request de entrada kind `9021`, que o relay aceita ou rejeita com base em sua política:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "f1a2b3c4d5e6f7890123456789abcdef0123456789abcdef1234567890abcdef",
  "created_at": 1744675200,
  "kind": 9021,
  "tags": [
    ["h", "abcdef"],
    ["code", "invite-xyz-123"]
  ],
  "content": "I'd like to join the dev discussion group.",
  "sig": "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff"
}
```

A tag `code` opcional se vincula a invite codes criados por admins via eventos kind `9009`. Um usuário sai publicando kind `9022`, e o relay emite automaticamente uma remoção kind `9001` em resposta. Admins podem adicionar usuários com papéis, kind `9000`, remover usuários, kind `9001`, editar metadados do grupo, kind `9002`, e apagar eventos, kind `9005`. O sistema de papéis é flexível: papéis são rótulos arbitrários, e o que cada papel pode fazer é política do relay, não algo definido pelo protocolo. O relay publica a configuração do grupo como eventos endereçáveis: kind `39000` para metadados, kind `39001` para lista de admins, kind `39002` para lista de membros e kind `39003` para papéis e capacidades.

Grupos podem ser públicos, qualquer um lê, só membros escrevem, fechados, só membros leem e escrevem, ou totalmente abertos. As settings de visibilidade e acesso de escrita são ortogonais e controladas pelas flags `public`, `open`, `visible` e `unrestricted` no evento de edição de metadados kind `9002`. Um relay pode hospedar muitos grupos simultaneamente, cada um com membership e moderação independentes.

A spec aceita qualquer kind de evento dentro de um grupo, não apenas mensagens de chat. Artigos de formato longo da [NIP-23](/pt/topics/nip-23/), eventos de calendário da [NIP-52](/pt/topics/nip-52/), lives da [NIP-53](/pt/topics/nip-53/) e listagens de mercado podem carregar uma tag `h` e participar do contexto do grupo. Isso faz grupos NIP-29 funcionarem mais como servidores do Discord ou workspaces do Slack, onde diferentes tipos de conteúdo coexistem no mesmo namespace.

[Flotilla](https://gitea.coracle.social/coracle/flotilla) é o cliente NIP-29 em desenvolvimento mais ativo, com salas de voz, login por email e DMs com proof-of-work adicionadas na [v1.7.0](/pt/newsletters/2026-04-01-newsletter/). [Coracle](https://github.com/coracle-social/coracle) também suporta grupos NIP-29. No lado de relay, [groups.fiatjaf.com](https://github.com/fiatjaf/relay29) é uma implementação de referência de fiatjaf. [Nostrord](https://github.com/Nostrord/nostrord), um cliente NIP-29 em Kotlin Multiplatform financiado pela [OpenSats](/en/newsletters/2026-04-08-newsletter/), está em desenvolvimento inicial com moderação estilo Discord e threading.

O tradeoff contra alternativas criptografadas como [Marmot](/pt/topics/marmot/) é explícito. Grupos NIP-29 podem ser lidos pelo operador do relay. Não há end-to-end encryption, nem forward secrecy, nem segurança pós-comprometimento. O relay é uma parte confiável para integridade de conteúdo e enforcement de membership. Em troca, o modelo oferece simplicidade: não há material de chave para gerenciar, nem sincronização de estado entre dispositivos, nem negociação MLS handshake. Um operador sobe um grupo, usuários entram e as mensagens fluem. Para comunidades públicas, canais de dev e espaços de discussão aberta, o modelo de confiança no relay combina com o caso de uso. Para mensagens privadas em que o relay não deve ler o conteúdo, NIP-17 ou Marmot são escolhas mais apropriadas.

## NIP Deep Dive: NIP-90 (Data Vending Machines)

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md) define um protocolo para computação on-demand sobre Nostr. Um cliente publica um request de job, provedores de serviço competem para cumpri-lo e os resultados são entregues como eventos Nostr. A spec descreve isso como money in, data out, tratando o Nostr como um mercado para processamento de dados, em que clientes se importam com o resultado, não com quem o produziu.

O protocolo reserva os kinds `5000-5999` para requests de jobs, `6000-6999` para resultados e o kind `7000` para feedback. O kind do resultado é sempre 1000 acima do kind do request: um request kind `5001` produz um resultado kind `6001`. Abaixo está um request de job pedindo sumarização de texto:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744675200,
  "kind": 5001,
  "tags": [
    ["i", "https://example.com/article.txt", "url"],
    ["output", "text/plain"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol"],
    ["bid", "5000"],
    ["param", "lang", "en"],
    ["param", "max_tokens", "280"]
  ],
  "content": "",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

A tag `i` especifica os dados de entrada com um marcador de tipo. Quatro tipos de entrada são definidos: `url`, buscar e processar dados na URL; `event`, usar um evento Nostr como entrada; `job`, encadear a partir da saída de um job anterior; e `text`, texto inline. A tag `bid` define um pagamento máximo em millisats. A tag `param` carrega parâmetros específicos do tipo de job, e a tag `output` especifica o formato de resposta esperado.

Um provedor de serviço pega o request e publica um resultado:

```json
{
  "id": "d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744675260,
  "kind": 6001,
  "tags": [
    ["request", "{\"id\":\"c3d4e5...\",\"kind\":5001,...}"],
    ["e", "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2", "wss://relay.damus.io"],
    ["i", "https://example.com/article.txt", "url"],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["amount", "5000", "lnbc50n1pj..."]
  ],
  "content": "The article discusses three protocol changes proposed for the next quarter...",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

O resultado marca o evento request original, inclui a entrada para referência, endereça a pubkey do cliente e opcionalmente inclui uma invoice Lightning na tag `amount`. O cliente pode verificar que o resultado veio de um provedor específico conferindo a pubkey.

Feedback de job, kind `7000`, fornece atualizações de status enquanto um job está em andamento. Provedores podem emitir eventos de feedback com valores de status como `payment-required`, `processing`, `error` ou `success`. Isso dá visibilidade em tempo real a jobs longos:

```json
{
  "id": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744675230,
  "kind": 7000,
  "tags": [
    ["status", "payment-required"],
    ["e", "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2", "wss://relay.damus.io"],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["amount", "5000", "lnbc50n1pj..."]
  ],
  "content": "",
  "sig": "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff"
}
```

O encadeamento de jobs permite que saídas alimentem jobs posteriores. Um cliente pode definir o tipo de entrada como `job` e referenciar o ID de evento de um job anterior. O provedor do job downstream espera o resultado upstream e então o processa. Isso cria pipelines componíveis: transcrever áudio, kind `5002`, depois resumir a transcrição, kind `5001`, e depois traduzir o resumo, kind `5003`. Cada passo pode ser cumprido por um provedor diferente.

Por privacidade, clientes podem criptografar as tags `i` e `param` usando a criptografia da [NIP-04](/pt/topics/nip-04/) com a pubkey do provedor, colocando o payload criptografado no campo `content` e adicionando uma tag `encrypted`. Isso esconde dados de entrada e parâmetros de relays e outros provedores, embora exija que o cliente selecione um provedor específico desde o início.

Tipos específicos de request de job são definidos em um [repositório separado](https://github.com/nostr-protocol/data-vending-machines/tree/master/kinds). Os tipos atuais incluem geração de texto, kind `5050`, sumarização, kind `5001`, tradução, kind `5002`, speech-to-text, kind `5003`, geração de imagens, kind `5100`, e recomendação de conteúdo, kind `5300`.

[Snort](https://github.com/v0l/snort) adicionou exibição de invoice de pagamento obrigatório kind `7000` na [Newsletter #17](/pt/newsletters/2026-04-08-newsletter/), renderizando invoices Lightning diretamente no feed quando um DVM responde com exigência de pagamento. [noStrudel](https://github.com/hzrd149/nostrudel) tem um explorador de DVM para navegar por provedores disponíveis. Do lado dos provedores, projetos como [DVMDash](https://github.com/dtdannen/dvmdash) acompanham atividade de DVM pela rede, e vários serviços focados em AI oferecem geração de texto, criação de imagens e moderação de conteúdo por meio do protocolo NIP-90. A [NIP-89](/pt/topics/nip-89/), Recommended Application Handlers, complementa a NIP-90 ao permitir que provedores publiquem suas capabilities como eventos Nostr descobríveis.

---

É isso por esta semana. Está construindo algo ou tem notícias para compartilhar? Mande DM no Nostr ou nos encontre em [nostrcompass.org](https://nostrcompass.org).
