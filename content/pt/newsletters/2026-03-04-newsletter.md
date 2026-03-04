---
title: 'Nostr Compass #12'
date: 2026-03-04
translationOf: /en/newsletters/2026-03-04-newsletter.md
translationDate: 2026-03-04
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** O [Marmot Development Kit](https://github.com/marmot-protocol/mdk) lança sua [primeira versão pública](#marmot-development-kit-lança-primeira-versão-pública) com mídia criptografada e bindings multi-linguagem. [Nostrability](https://github.com/nostrability/outbox) publica [benchmarks do modelo outbox](#modelo-outbox-sob-o-microscópio) em 14 algoritmos de seleção de relay. [Wisp](https://github.com/barrydeen/wisp) vai do [primeiro alpha ao beta](#wisp-sai-do-alpha-para-o-beta) em oito dias com Tor e assinatura [NIP-55](/pt/topics/nip-55/) (Android Signer Application). [NIP-91](#atualizações-de-nips) (filtros AND) é mergeado. [Vector v0.3.1](#vector-v031) entrega sincronização negentropy com ganhos de desempenho de 15x. Esta edição também inclui a retrospectiva Cinco Anos de Fevereiros do Nostr, traçando o protocolo desde uma reescrita de spec servindo três relays, passando pela explosão do Damus na App Store, até redes mesh e propostas de agentes de IA.

## Notícias

### Modelo Outbox Sob o Microscópio

[Nostrability](https://github.com/nostrability/outbox) publicou uma série de benchmarks do modelo outbox testando quão bem diferentes algoritmos de seleção de relay recuperam eventos da rede descentralizada de relays. O projeto mergeou 16 PRs e 76 commits em dez dias, produzindo o que pode ser a análise empírica mais completa de estratégias de implementação do [NIP-65](/pt/topics/nip-65/) (Relay List Metadata) até hoje.

Os benchmarks testam 14 algoritmos de seleção de relay contra listas de follows reais em 15 clientes e bibliotecas em cinco linguagens. Uma abordagem de linha de base consultando apenas relays populares recupera aproximadamente 26% dos eventos. Set-cover guloso com Thompson Sampling alcança 80-90% de recall. Adicionar uma variante sensível a latência usando desconto hiperbólico e rastreamento de latência de relay EWMA elevou a completude de 62-80% para 72-96% na marca de 2 segundos em seis perfis de teste.

A filtragem de relays inativos do [NIP-66](/pt/topics/nip-66/) (Relay Monitoring) provou ser consequente. Pré-filtrar candidatos de relay contra dados de atividade do [nostr.watch](https://nostr.watch) removeu 40-64% dos relays inativos e dobrou as taxas de sucesso de relay de 30% para 75-85%. Tempos de carregamento de feed caíram 39% (de 40 segundos para 24 segundos em 10 perfis). Uma simulação de corrida EOSE descobriu que esperar pelo EOSE mais um período de graça de 200ms melhorou a completude em comparação com parar no primeiro relay a terminar.

Para clientes que não conseguem reescrever completamente seu roteamento de relay, uma abordagem de "enriquecimento outbox híbrido" adiciona consultas outbox por autor sobre os relays hardcoded existentes do app. Esse híbrido alcançou 80% de recall de eventos de um ano contra os 26% da linha de base, oferecendo um caminho de migração para clientes com arquiteturas de relay legadas.

### ContextVM Abre NIP de MCP e Lança Gift Wraps Efêmeros

[ContextVM](https://contextvm.org), o protocolo fazendo ponte entre o Nostr e o [Model Context Protocol](https://modelcontextprotocol.io/), abriu duas propostas no [repositório de NIPs](https://github.com/nostr-protocol/nips) esta semana. O [PR #2246](https://github.com/nostr-protocol/nips/pull/2246) formaliza CVM como uma convenção para transportar mensagens MCP JSON-RPC sobre Nostr usando eventos efêmeros kind 25910. O [PR #2245](https://github.com/nostr-protocol/nips/pull/2245) estende o [NIP-59](/pt/topics/nip-59/) (Gift Wrap) com um kind efêmero (21059) que segue a semântica efêmera do [NIP-01](/pt/topics/nip-01/) (Basic Protocol Flow), permitindo que relays descartem mensagens encapsuladas após a entrega.

A convenção de gift wrap efêmero foi lançada como [CEP-19](https://docs.contextvm.org/spec/ceps/cep-19/) na família de lançamento ContextVM SDK v0.6.x. A [implementação do SDK](https://github.com/ContextVM/sdk) adiciona um enum `GiftWrapMode` com três configurações: OPTIONAL (aceita ambos os kinds e auto-detecta capacidade do par), EPHEMERAL (apenas kind 21059) e PERSISTENT (apenas kind 1059). Para chamadas de ferramentas de IA, o modo efêmero evita armazenar tráfego intermediário de requisição-resposta nos relays, reduzindo tanto custos de armazenamento quanto exposição de privacidade.

Novos servidores MCP públicos apareceram na rede de operadores independentes, incluindo um servidor de consulta Wolfram Alpha. A equipe ContextVM publicou CEP-15 (esquema de ferramentas comuns) e CEP-17 (publicação de lista de relays de servidor) junto com o ciclo de lançamento v0.6.x.

### Marmot Development Kit Lança Primeira Versão Pública

[MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit), a biblioteca Rust que alimenta mensagens criptografadas com [Marmot](/pt/topics/mls/) em [Pika](https://github.com/sledtools/pika) e [White Noise](https://github.com/marmot-protocol/whitenoise), lançou [v0.6.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.6.0) como sua primeira versão pública. Mais de 200 PRs foram mergeados nesta versão, com seis novos contribuidores.

O lançamento inclui suporte a mídia criptografada (MIP-04) com derivação de seed HKDF (MIP-01 v2), resolução determinística de corrida de commits (MIP-03), armazenamento local criptografado, validação de autorização de admin para commits e propostas Marmot, e suporte GREASE para extensibilidade do protocolo. Bindings são fornecidos para Kotlin, Python, Ruby e Windows junto com compilação cruzada para Android. A biblioteca atualiza para OpenMLS 0.8.0 com correções de avisos de segurança e um tipo `Secret<T>` que zeroiza valores sensíveis na memória.

Uma mudança de protocolo complementar ([MIP-03](https://github.com/marmot-protocol/marmot/pull/48)) substituiu a criptografia [NIP-44](/pt/topics/nip-44/) (Encrypted Payloads) por ChaCha20-Poly1305 para mensagens kind 445. NIP-44 exigia entrada de string UTF-8 conforme sua especificação, tornando impossível passar bytes brutos de mensagem Marmot através de bibliotecas Nostr TypeScript padrão. A substituição deriva chaves diretamente do segredo exportador do Marmot. Essa mudança que quebra compatibilidade exigiu atualizações coordenadas em toda a [spec core](https://github.com/marmot-protocol/marmot/pull/48), [MDK](https://github.com/marmot-protocol/mdk/pull/208) e [TypeScript SDK](https://github.com/marmot-protocol/marmot-ts/pull/54).

[marmot-ts](https://github.com/marmot-protocol/marmot-ts), a implementação TypeScript mantida por hzrd149, mergeou quatro PRs com mudanças que quebram a API. Uma [atualização omnibus](https://github.com/marmot-protocol/marmot-ts/pull/52) adicionou um gerenciador de pacote de chaves para ciclo de vida criar/publicar/rotacionar, um método conveniente `sendChatMessage`, pré-visualização de convite sem entrar (`readInviteGroupInfo`), auto-atualização para rotações de sigilo futuro e logging de debug estruturado. APIs de descriptografia de grupo foram renomeadas de `readGroupMessage` para `decryptGroupMessage` com variantes de resultado mais ricas (processed/skipped/rejected/unreadable). gzuuus contribuiu limpeza de exemplos com suporte a relay NIP-65 e tratamento de pacote de chaves de último recurso conforme MIP-00.

O [White Noise CLI](https://github.com/marmot-protocol/whitenoise-rs) (`wn`), o backend Rust que alimenta tanto o app mobile quanto o novo TUI, mergeou 16 PRs em dez dias. O tratamento do ciclo de vida do assinador ganhou segurança contra cancelamento através de um scope guard RAII ([PR #538](https://github.com/marmot-protocol/whitenoise-rs/pull/538)), corrigindo uma classe de bugs onde operações abortadas podiam vazar estado do assinador. O login agora bloqueia quando listas de relay obrigatórias (kind 10002/10050/10051) estão ausentes ([PR #515](https://github.com/marmot-protocol/whitenoise-rs/pull/515)), e assinaturas de giftwrap recorrem a relays [NIP-65](/pt/topics/nip-65/) quando listas de inbox estão ausentes ([PR #518](https://github.com/marmot-protocol/whitenoise-rs/pull/518)). Um modo debug ([PR #528](https://github.com/marmot-protocol/whitenoise-rs/pull/528)) expõe consultas ao banco de dados e inspeção da árvore de ratchet MLS como saída JSON. Outras correções trataram recuperação de assinatura após re-registro do assinador, timing de catch-up de mensagens de boas-vindas, validação de filtro de relay e limites de raio de busca de usuários.

O Marmot teve expansão significativa além da stack Rust core esta semana. [White Noise TUI](https://github.com/marmot-protocol/wn-tui), uma interface baseada em terminal para a stack de mensagens White Noise, foi lançado em 3 de março. Ele encapsula o CLI `wn` como um subprocesso e renderiza sua saída JSON através de uma arquitetura unidirecional inspirada em Elm, fornecendo navegação entre múltiplas conversas com indicadores de não lidos, criação de grupo e busca de membros, streaming de mensagens em tempo real e reações com emoji pelo terminal.

[DavidGershony](https://github.com/DavidGershony) publicou uma stack Marmot completa em C# espelhando a arquitetura em camadas do ferramental Rust. [dotnet-mls](https://github.com/DavidGershony/dotnet-mls) implementa primitivas criptográficas MLS RFC 9420 em C#. [marmot-cs](https://github.com/DavidGershony/marmot-cs) constrói sobre isso para adicionar transporte por relay Nostr, funcionando como equivalente em C# do MDK. [OpenChat](https://github.com/DavidGershony/openChat), um app desktop multiplataforma construído com .NET 9 e Avalonia UI, une ambos em um cliente de chat funcional com DMs NIP-44, criptografia de grupo Marmot, assinatura remota [NIP-46](/pt/topics/nip-46/) (Nostr Connect) e indicadores de status multi-relay.

[MDK PWA Reference](https://github.com/zerosats/mdk-pwa-reference) fornece um template Progressive Web App para construir aplicações criptografadas com Marmot, com suporte experimental para participação de agentes de IA em chats de grupo e pagamentos Bitcoin via infraestrutura de carteira Arkade.

### Wisp Sai do Alpha para o Beta

[Wisp](https://github.com/barrydeen/wisp) é um novo cliente Nostr para Android que foi do [primeiro alpha](https://github.com/barrydeen/wisp/releases/tag/v0.1.0-alpha) em 24 de fevereiro ao [v0.3.4-beta](https://github.com/barrydeen/wisp/releases/tag/v0.3.4-beta) em 3 de março, produzindo 19 lançamentos, 115 PRs mergeados e 276 commits em oito dias.

A trajetória de recursos cobre terreno que a maioria dos clientes leva meses para alcançar. A v0.1.0 foi lançada com suporte ao modelo de relay outbox/inbox e fluxos de onboarding. Na v0.1.3, o cliente tinha assinatura baseada em intent [NIP-55](/pt/topics/nip-55/) para Amber, um proxy SOCKS5 Tor embutido para conectividade de relay `.onion`, e [NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect). A v0.2.0 graduou para beta com filtragem de lista de mute e suporte a emoji personalizado, enquanto a v0.2.4 adicionou overlays de aviso de conteúdo. A série v0.3.x introduziu proof-of-work [NIP-13](/pt/topics/nip-13/) para notas, mineração PoW em background com configurações persistentes, armazenamento de relay `.onion` e notificações de mute de thread.

Tradução no dispositivo via Google ML Kit roda localmente sem acesso à rede após o download inicial do modelo. Uma visualização interativa de grafo social usa uma simulação de física velocity Verlet a aproximadamente 30fps com navegação pinch-to-zoom e inspeção de perfil.

## Lançamentos

### Vector v0.3.1

[Vector](https://github.com/VectorPrivacy/Vector), o app de mensagens criptografadas com Marmot, lançou [v0.3.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.1) com melhorias de gerenciamento de grupo e trabalho de desempenho. Grupos multi-admin, convites em massa, convite por npub e avatares de grupo expandem os recursos de colaboração. Notificações em background no Android agora suportam ações inline de Responder e Marcar como Lido.

Sincronização determinística baseada em [negentropy](/pt/topics/negentropy/) recupera histórico completo de conversas incluindo mensagens perdidas durante períodos offline. Voz-para-texto reconstruído com aceleração GPU no Android. O tratamento de anexos de arquivo foi reformulado com progresso de download, estados de retry, zip-e-envio de diretório e indicadores de progresso ao vivo em toda parte. O desempenho melhorou mais de 15x em tempo de inicialização, processamento de imagem, reprodução de áudio e responsividade geral da UI. O tamanho de instalação do app caiu mais de um terço, com o frontend reduzido aproximadamente pela metade. Suporte a Android ARM de 32 bits foi adicionado.

### Alby Hub v1.21.5

[Alby Hub](https://github.com/getAlby/hub), o nó Lightning auto-custodial com suporte a Nostr Wallet Connect ([NIP-47](/pt/topics/nip-47/)), lançou [v1.21.5](https://github.com/getAlby/hub/releases/tag/v1.21.5). Um segundo relay foi adicionado à configuração NWC padrão, melhorando a confiabilidade durante reinicializações de relay. Uma correção para dados de zap inválidos na lista de transações resolve um problema de exibição com eventos [NIP-57](/pt/topics/nip-57/) (Lightning Zaps) malformados. Novas entradas na app store incluem Alby CLI e LNVPS.

### nospeak v0.12.x

[nospeak](https://github.com/psic4t/nospeak), o cliente Nostr de mensagens baseado em texto, lançou três versões durante o período. [v0.12.0](https://github.com/psic4t/nospeak/releases/tag/v0.12.0) adicionou bloqueio de app por PIN com teclado de 4 dígitos e mais de 15 novas traduções de idiomas incluindo bengali, tailandês, vietnamita, hindi, árabe, hebraico, urdu, turco, japonês, chinês, coreano, holandês, polonês, russo e persa com suporte RTL. [v0.12.1](https://github.com/psic4t/nospeak/releases/tag/v0.12.1) introduziu um tema Cypher com fundos preto puro e acentos ciano, além de geração de poster de vídeo para Android. [v0.12.2](https://github.com/psic4t/nospeak/releases/tag/v0.12.2) adicionou exportação de chat e Ver Perfil nos menus de contato.

### Citrine v2.0.0-pre2

[Citrine](https://github.com/greenart7c3/Citrine), o relay pessoal Android de greenart7c3, lançou [v2.0.0-pre2](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre2) com melhorias de desempenho de relay através de novos índices de banco de dados e coroutines Kotlin reestruturadas. Cada app web hospedado agora inicia em sua própria porta. Busca full-text e uma tela de eventos redesenhada com expansão de eventos completam as mudanças.

### NoorNote v0.5.x

[NoorNote](https://github.com/77elements/noornote), uma aplicação de anotações baseada no Nostr, lançou 8 versões de [v0.5.0](https://github.com/77elements/noornote/releases/tag/v0.5.0) até [v0.5.7](https://github.com/77elements/noornote/releases/tag/v0.5.7). O lançamento da v0.5.0 no Android adicionou suporte ao assinador Amber [NIP-55](/pt/topics/nip-55/) e publicação de notas [NIP-71](/pt/topics/nip-71/) (Video Events). Uma página de boas-vindas redesenhada na v0.5.1 incluiu pré-visualizações de timeline pública e reduziu o APK para 15 MB. O Relay Browser na v0.5.2 permite que usuários naveguem em timelines públicas de relays via URLs compartilháveis, junto com download de mídia e reações de emoji personalizado [NIP-30](/pt/topics/nip-30/). Lançamentos subsequentes até a v0.5.7 trataram condições de corrida de sincronização no sistema de compartilhamento de notas colaborativas "tribes".

### NosCall v0.5.1

[NosCall](https://github.com/sanah9/noscall), o app de chamadas de voz e vídeo no Nostr, lançou [v0.5.1](https://github.com/sanah9/noscall/releases/tag/v0.5.1-release) com suporte a mensagens de voz, uma experiência desktop otimizada com entrada de grupo, favoritos de contato no desktop, notas e filtragem de contatos, opções de exportação e limpeza de dados, e suporte a acessibilidade de tamanho de fonte do sistema.

### Shosho v0.13.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), o app de transmissão ao vivo no Nostr, lançou [v0.13.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.13.0) com downloads de replay em MP4 nos menus de cartão de stream e [NIP-05](/pt/topics/nip-05/) (DNS-Based Verification) para perfis. O publisher RTMP migrou para a Expo Modules API. O desempenho de streaming em conexões de menor largura de banda melhorou, e crashes em dispositivos mais antigos e streaming iOS para [Zap.Stream](https://zap.stream) foram corrigidos.

### nostr-java v2.0.0

[nostr-java](https://github.com/tcheeric/nostr-java) lançou [v2.0.0](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.0) com tamanhos de buffer WebSocket configuráveis, permitindo que aplicações lidem com eventos Nostr maiores sem truncamento. O major version bump reflete mudanças que quebram compatibilidade na API de conexão.

### Prism 1.1.0

[Prism](https://github.com/hardran3/Prism) lançou [1.1.0](https://github.com/hardran3/Prism/releases/tag/1.1.0) com suporte a conteúdo de formato longo (artigos kind 30023) e um editor Markdown para composição diretamente no app, seguido por um lançamento de correção [1.1.1](https://github.com/hardran3/Prism/releases/tag/1.1.1).

### Angor v0.2.6

[Angor](https://github.com/block-core/angor), a plataforma de crowdfunding Bitcoin, lançou [v0.2.6](https://github.com/block-core/angor/releases/tag/v0.2.6) com integração Boltz e um fluxo de investimento em 1 clique. Tanto os tipos investir quanto financiar projeto funcionam de ponta a ponta na testnet. A equipe nota que a UI está aproximadamente 70% completa.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado:**

- **[NIP-91: AND Operator for Filters](https://github.com/nostr-protocol/nips/pull/1365)**: Adiciona semântica de filtro AND para arrays de tags em assinaturas de relay. Atualmente, especificar múltiplos valores em um filtro de tag (por exemplo, múltiplas tags `p`) corresponde a eventos contendo qualquer um deles. NIP-91 permite que clientes exijam eventos correspondendo a todos os valores de tag especificados simultaneamente, reduzindo largura de banda e habilitando operações de índice mais rápidas. Múltiplas implementações de relay já existem incluindo nostr-rs-relay, satellite-node, worker-relay e applesauce. Anteriormente numerado NIP-119.

- **[NIP-30: Emoji Set Address in Tags](https://github.com/nostr-protocol/nips/pull/2247)**: Tags de emoji personalizado no [NIP-30](/pt/topics/nip-30/) agora podem incluir um endereço opcional de conjunto de emoji. Clicar em um emoji em um cliente pode abrir o conjunto ao qual pertence para favoritar ou navegar. Originado do cliente [Chachi](https://github.com/purrgrammer/chachi).

- **[NIP-29: Add unallowpubkey and unbanpubkey](https://github.com/nostr-protocol/nips/pull/2111)**: Dois novos comandos de admin para chat de grupo [NIP-29](/pt/topics/nip-29/). `unallowpubkey` remove uma pubkey da lista de permitidos sem bani-la. `unbanpubkey` levanta um banimento sem re-adicionar a pubkey à lista de membros. Anteriormente, a única forma de remover alguém da lista de permitidos também bania a pessoa, e desbanir exigia re-adicionar o usuário como membro.

**PRs Abertos e Discussões:**

- **[NIP-A7: Spells](https://github.com/nostr-protocol/nips/pull/2244)** (aberto 27 fev): Proposto por purrgrammer, spells são consultas Nostr salvas e portáteis publicadas como eventos kind 777. Um spell codifica um filtro REQ ou COUNT em tags estruturadas (`k` para kinds, `authors` para pubkeys, `tag` para filtros de tags arbitrários) com variáveis de runtime: `$me` resolve para a pubkey do usuário logado, `$contacts` expande para a lista de follows kind 3 do usuário. Timestamps relativos (`7d`, `2w`, `1mo`) permitem que spells definam janelas de tempo rolantes sem datas hardcoded. Já implementado em [nak](https://github.com/fiatjaf/nak) e [Grimoire](https://github.com/purrgrammer/grimoire), spells permitem que usuários criem, compartilhem e se inscrevam em feeds curados que viajam entre clientes.

- **[NIP-59: Ephemeral Gift Wrap (kind 21059)](https://github.com/nostr-protocol/nips/pull/2245)** (aberto 27 fev): Adiciona uma variante efêmera dos gift wraps [NIP-59](/pt/topics/nip-59/). O kind 21059 segue a semântica efêmera do NIP-01, então relays descartam eventos após a entrega. Proposto por ContextVM para transporte MCP onde persistência de mensagens é desnecessária.

- **[ContextVM: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)** (aberto 27 fev): Especifica como transportar mensagens Model Context Protocol sobre Nostr usando eventos efêmeros kind 25910 com tags `p` e `e` para endereçamento e correlação. Intencionalmente fino, delegando detalhes de protocolo à [spec ContextVM](https://docs.contextvm.org).

- **[NIP-29: Audio/Video Live Spaces](https://github.com/nostr-protocol/nips/pull/2238)** (aberto 25 fev, rascunho): Rascunho de fiatjaf estendendo grupos [NIP-29](/pt/topics/nip-29/) com áudio e vídeo ao vivo. A proposta adiciona tags opcionais `livekit` e `no-text` a eventos de metadados de grupo. Quando um usuário quer entrar em um espaço de voz, o cliente solicita um JWT do relay em `/.well-known/nip29/livekit/{groupId}`. O relay verifica a associação ao grupo e emite um token com a pubkey hex do usuário como claim `sub`, que é passado ao [LiveKit](https://livekit.io/) para transporte de mídia. O acesso à sala de voz herda o modelo de permissão existente do grupo, então regras de associação do lado do relay governam quem pode falar. Sendo testado no Pyramid e Chachi.

- **[Collaborative Event Ownership](https://github.com/nostr-protocol/nips/pull/2235)** (aberto 24 fev): pablof7z propõe um evento ponteiro (kind 39382) que declara um espaço colaborativo listando pubkeys de co-proprietários em tags `p` e um kind de evento alvo em uma tag `k`. Qualquer proprietário listado pode publicar eventos desse kind com a mesma tag `d`, e clientes resolvem o estado atual consultando todos os proprietários e pegando o evento mais recente. A atribuição de co-autoria só aparece quando uma tag `a` verificável referencia de volta o ponteiro e o autor aparece em suas tags `p`, prevenindo reivindicações falsificadas. Isso habilita páginas wiki compartilhadas e recursos co-autorados sem atribuir controle a um único par de chaves.

- **[NIP-09: Cascading Deletion of Reposts](https://github.com/nostr-protocol/nips/pull/2234)** (aberto 24 fev): Quando um autor original deleta uma nota, relays também devem deletar quaisquer reposts kind 6 ou kind 16 que a referenciam. Motivado por preocupações de privacidade: reposts podem preservar informações acidentalmente vazadas após o autor deletar a fonte. A mudança é apenas do lado do relay, não exigindo modificações nos clientes.

- **[NIP-07: peekPublicKey](https://github.com/nostr-protocol/nips/pull/2233)** (aberto 23 fev): Adiciona um método `peekPublicKey()` a extensões de navegador [NIP-07](/pt/topics/nip-07/). Diferente de `getPublicKey()`, retorna a pubkey atual sem solicitar confirmação do usuário, habilitando auto-login silencioso quando o usuário tem auto-login habilitado.

- **[NIP-BB: Book](https://github.com/nostr-protocol/nips/pull/2248)** (aberto 28 fev, rascunho): Define quatro kinds de evento endereçáveis (30300-30303) para publicação estruturada de livros no Nostr. Um evento Cover contém metadados raiz incluindo título, imagem de capa, licença via labels [NIP-32](/pt/topics/nip-32/) (Labeling) e código de idioma. Um evento Index mapeia cada capítulo à sua posição usando indexação fracionária base62, que permite aos autores inserir novos capítulos entre existentes sem renumerar. Eventos Chapter agem como cabeçalhos estruturais com imagens opcionais, enquanto eventos Episode carregam a prosa real limitada a 30.000 caracteres com tags de imagem posicionadas. Resenhas usam Zaps em eventos Cover com a descrição do Zap como texto da resenha.

- **[NIP-54: Switch from Asciidoc to Djot](https://github.com/nostr-protocol/nips/pull/2242)** (aberto 26 fev): Após a [correção de internacionalização de d-tag](/pt/newsletters/2025-12-31-newsletter/) em dezembro, este PR propõe substituir o formato de marcação Asciidoc do wiki [NIP-54](/pt/topics/nip-54/) por [Djot](https://djot.net/), adicionando uma seção de justificativa e exemplos de wikilink para scripts não-latinos.

- **[NIP-66: Defensive Measures](https://github.com/nostr-protocol/nips/pull/2240)** (aberto 26 fev): Baseado nos aprendizados dos benchmarks [nostrability/outbox](#modelo-outbox-sob-o-microscópio), adiciona chamadas explícitas para casos limite do [NIP-66](/pt/topics/nip-66/). Um [PR #2241](https://github.com/nostr-protocol/nips/pull/2241) complementar define tags de saída para SSL, geolocalização, rede e verificações de conectividade.

- **NIP-C1: Cryptographic Identity Proofs** (entrada wiki, kind 30817): Propõe eventos kind 30509 que vinculam criptograficamente certificados de assinatura APK a perfis Nostr. A prova funciona assinando uma mensagem canônica contendo a pubkey Nostr com a chave privada do certificado (suportando ECDSA, RSA PKCS1v15, Ed25519 e outros algoritmos padrão), depois publicando a assinatura em um evento kind 30509 assinado com a chave Nostr. Verificadores podem confirmar que a pessoa que controla o certificado de assinatura de um app Android também controla a pubkey Nostr que afirma publicá-lo. Provas expiram após um ano por padrão e podem ser explicitamente revogadas. Implementado no ferramental [Zapstore](https://github.com/zapstore/zapstore).

- **NIP-31402: SARA Revenue Share Offering Registry** (entrada wiki, kind 30817): Define eventos endereçáveis kind 31402 para publicar ofertas de Simple Autonomous Revenue Agreement (SARA) em relays Nostr. Emissores anunciam termos de compartilhamento de receita liquidados via Lightning incluindo percentual de pool share, gatilho de pagamento, limiar em sats, duração do termo e preço por faixas. Agentes e humanos podem descobrir ofertas em relays e se inscrever autonomamente sem uma plataforma central. O número do kind espelha o kind 30402 (L402 Service Registry, publicado pelo mesmo autor como uma entrada wiki complementar) já que SARA representa o retorno da relação de pagamento L402.

## PRs Abertos e Atualizações de Projetos

### Damus: [NIP-89](/pt/topics/nip-89/) (Recommended Application Handlers)

O [PR #3337](https://github.com/damus-io/damus/pull/3337) implementa suporte a client tag NIP-89 para [Damus](https://github.com/damus-io/damus). O app agora emite uma client tag em todos os caminhos de publicação (app principal, extensão de compartilhamento, highlighter, rascunhos) e exibe "via ClientName" ao lado de timestamps quando outros apps incluem suas tags. Um toggle de Privacidade nas configurações de Aparência permite que usuários desabilitem a emissão de tag. O [PR #3652](https://github.com/damus-io/damus/pull/3652) adiciona uma seção de Armazenamento em Configurações com um gráfico de pizza interativo detalhando uso de disco do cache NostrDB e Kingfisher com suporte a exportação.

Em aberto: [PR #3657](https://github.com/damus-io/damus/pull/3657) adiciona fallback de relay [NIP-65](/pt/topics/nip-65/) para notas citadas. Quando um `nevent` inline inclui uma pubkey de autor mas nenhuma dica de relay e a nota está ausente do pool do usuário, Damus busca a lista de relays kind 10002 do autor e tenta novamente a partir de seus relays de escrita.

### Amethyst: [NIP-39](/pt/topics/nip-39/) (External Identities), NIP-C0, [NIP-66](/pt/topics/nip-66/)

[Amethyst](https://github.com/vitorpamplona/amethyst) mergeou uma onda de implementações de NIPs em 28 PRs. Reivindicações de identidade externa agora publicam como eventos dedicados kind 10011 sob [NIP-39](/pt/topics/nip-39/) ([PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747)), separando identidade social de metadados kind 0 com fallback retrocompatível. Suporte a trechos de código via NIP-C0 ([PR #1744](https://github.com/vitorpamplona/amethyst/pull/1744)) adiciona eventos kind 1337 com acessores para linguagem, extensão, runtime, licença e dependências. A implementação de monitoramento de relay [NIP-66](/pt/topics/nip-66/) ([PR #1742](https://github.com/vitorpamplona/amethyst/pull/1742)) cobre ambos os kinds de evento com parsing completo de tags para métricas RTT, tipo de rede, NIPs suportados e geohash.

DMs criptografadas chegaram ao Amethyst Desktop ([PR #1710](https://github.com/vitorpamplona/amethyst/pull/1710)) com um layout de chat em painéis divididos suportando tanto [NIP-04](/pt/topics/nip-04/) (Encrypted Direct Messages) quanto [NIP-17](/pt/topics/nip-17/) (Private Direct Messages). Uma nova tela de feed de relay ([PR #1733](https://github.com/vitorpamplona/amethyst/pull/1733)) permite que usuários naveguem posts de um relay específico com funcionalidade de follow/unfollow. Em aberto: verificação NIP-05 resistente a censura ([PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)) adiciona um caminho de verificação paralelo para identificadores `.bit` que resolve contra a blockchain Namecoin em vez de HTTP DNS. Quando Amethyst detecta um sufixo `.bit` em um campo NIP-05, consulta um servidor ElectrumX-NMC pelo histórico de transações do nome, faz parsing do script `NAME_UPDATE` da saída mais recente para extrair a pubkey Nostr, e rejeita nomes mais antigos que 36.000 blocos (janela de expiração do Namecoin). Conexões ElectrumX roteiam através de SOCKS5 quando Tor está habilitado, com seleção dinâmica de servidor entre endpoints clearnet e `.onion`. Um cache LRU com TTL de uma hora previne consultas repetidas à blockchain.

### Notedeck: Arquitetura Outbox

O [PR #1303](https://github.com/damus-io/notedeck/pull/1303) migra o [Notedeck](https://github.com/damus-io/notedeck) de gerenciamento ad-hoc de pool de relays para um modelo outbox centralizado com assinaturas com escopo de conta. O módulo Messages agora publica uma lista de relay DM padrão se nenhuma existir e roteia DMs para relays preferidos dos destinatários conforme kind 10050.

### Pika: Perfis por Grupo e Feed Tutorial

[Pika](https://github.com/sledtools/pika), o app de mensagens criptografadas com Marmot disponível para iOS e Android com build desktop, ganhou perfis por grupo ([PR #368](https://github.com/sledtools/pika/pull/368)). Usuários agora podem definir um nome de exibição e foto separados para cada chat de grupo, junto com uma bio personalizada. Esses perfis publicam como eventos kind 0 criptografados dentro do grupo Marmot, invisíveis para qualquer pessoa fora dele, com fallback para o perfil Nostr global do usuário quando nenhum perfil específico do grupo está definido. Quando novos membros entram, o admin retransmite todos os perfis de grupo armazenados e cada membro republica o seu próprio no commit. Fotos de perfil são criptografadas com Marmot-media antes do upload Blossom. O PR inclui 16 novos testes unitários e expõe o recurso tanto através de um comando CLI (`update-group-profile`) quanto da UI.

Um novo web app `pika-news` ([PR #401](https://github.com/sledtools/pika/pull/401)) monitora os PRs do próprio GitHub do Pika e gera automaticamente tutoriais passo a passo de walkthroughs a partir de diffs de PRs, publicando-os como páginas renderizadas no servidor com autenticação [NIP-07](/pt/topics/nip-07/). Usuários podem discutir tutoriais específicos em tempo real através de chat autenticado por Nostr.

### diVine: Widgets Embutíveis e Respostas em Vídeo

[diVine](https://github.com/divinevideo/divine-mobile), a plataforma de compartilhamento de vídeo nativa do Nostr, mergeou 132 PRs em dez dias. Widgets embutíveis via iframe ([PR #1843](https://github.com/divinevideo/divine-mobile/pull/1843)) fornecem uma página `/embed?npub=...` autocontida que renderiza o perfil de um usuário e seus vídeos mais recentes. Funcionalidade de resposta em vídeo ([PR #1915](https://github.com/divinevideo/divine-mobile/pull/1915)), protegida por feature flag, usa comentários Kind 1111 ([NIP-22](/pt/topics/nip-22/)) com metadados imeta [NIP-92](/pt/topics/nip-92/) (Media Attachments). Filtros de conteúdo em três vias inspirados no Bluesky ([PR #1797](https://github.com/divinevideo/divine-mobile/pull/1797)) oferecem controles Mostrar/Avisar/Ocultar em 17 categorias de aviso de conteúdo [NIP-32](/pt/topics/nip-32/).

### strfry: Validação de Filtro REQ

O [PR #163](https://github.com/hoytech/strfry/pull/163) adiciona validação configurável de filtro REQ ao [strfry](https://github.com/hoytech/strfry), o relay Nostr C++. Operadores podem definir máximo de filtros por REQ, presença obrigatória de autor ou tag, whitelists de kinds permitidos e limites de kinds por filtro. O recurso visa deployments de relay NWC que precisam de enforcement estrito de filtros. Em aberto: [PR #173](https://github.com/hoytech/strfry/pull/173) adiciona compressão zstd opcional para payloads de evento no momento da ingestão.

### rust-nostr: [NIP-62](/pt/topics/nip-62/) Request to Vanish

[rust-nostr](https://github.com/rust-nostr/nostr), a biblioteca de protocolo Nostr em Rust, adicionou suporte a [NIP-62](/pt/topics/nip-62/) (Request to Vanish) em todos os três backends de banco de dados: [LMDB](https://github.com/rust-nostr/nostr/pull/1268), [SQLite](https://github.com/rust-nostr/nostr/pull/1270) e [in-memory](https://github.com/rust-nostr/nostr/pull/1272). A implementação LMDB inclui opções configuráveis para habilitar ou desabilitar enforcement de [NIP-09](/pt/topics/nip-09/) e NIP-62 por deployment.

### NDK: Eventos Colaborativos e Timeout NIP-46

[NDK](https://github.com/nostr-dev-kit/ndk), o Nostr Development Kit para JavaScript/TypeScript, mergeou o [PR #380](https://github.com/nostr-dev-kit/ndk/pull/380) introduzindo `NDKCollaborativeEvent` para documentos colaborativos multi-autor usando um evento ponteiro endereçável (kind 39382) que define autores autorizados. Um timeout configurável para `NDKNip46Signer` ([PR #381](https://github.com/nostr-dev-kit/ndk/pull/381)) previne que operações de assinatura remota [NIP-46](/pt/topics/nip-46/) fiquem penduradas indefinidamente quando um bunker não responde.

### TENEX: Categorização de Agentes e Gating por Pubkey

[TENEX](https://github.com/tenex-chat/tenex), a plataforma de orquestração de agentes de IA nativa do Nostr, mergeou dois PRs relacionados a segurança. Categorização de agentes baseada em papéis TIP-01 ([PR #91](https://github.com/tenex-chat/tenex/pull/91)) mapeia categorias de agente (principal, orchestrator, worker, advisor, auditor) para restrições automatizadas de ferramentas via um mapa de ferramentas negadas. Gating de pubkey na porta de entrada ([PR #87](https://github.com/tenex-chat/tenex/pull/87)) garante que apenas eventos de pubkeys na whitelist ou assinados pelo backend sejam roteados junto com agentes conhecidos; pubkeys desconhecidas são silenciosamente descartadas com spans OpenTelemetry para auditoria.

### Zap Cooking: Painel de Membros

[Zap Cooking](https://github.com/zapcooking/frontend), a plataforma de compartilhamento de receitas baseada no Nostr, mergeou 25 PRs e 85 commits em dez dias. Um painel de membros ([PR #228](https://github.com/zapcooking/frontend/pull/228)) mostra status de assinatura com datas de expiração e opções de gerenciar/upgrade, reabilita gates de recursos para as faixas Sous Chef e Zappy com verificações tanto no lado do cliente quanto no servidor, e padroniza nomenclatura de faixas em 26 arquivos. Carregamento de mensagens de grupo em duas fases ([PR #227](https://github.com/zapcooking/frontend/pull/227)) fornece uma busca inicial rápida de 3 dias para exibição instantânea seguida de um backfill em background de 40 dias.

O armazenamento de mnemônica de carteira foi movido de criptografia derivada de pubkey para encrypt-to-self [NIP-44](/pt/topics/nip-44/) ([PR #224](https://github.com/zapcooking/frontend/pull/224)), corrigindo uma vulnerabilidade onde o esquema antigo derivava sua chave de `SHA-256(pubkey)`, que é efetivamente não criptografado já que pubkeys são públicas. Carteiras existentes são migradas silenciosamente no primeiro carregamento. Chat de grupo [NIP-29](/pt/topics/nip-29/) ganhou indicadores de não lidos com badges de ponto vermelho e acesso somente por convite com códigos de convite kind 9009 ([PR #213](https://github.com/zapcooking/frontend/pull/213)). Pré-visualizações de links e embeds de eventos Nostr agora renderizam em DMs e mensagens de grupo ([PR #218](https://github.com/zapcooking/frontend/pull/218)). Uma seção de backup Nostr em Configurações ([PR #210](https://github.com/zapcooking/frontend/pull/210)) armazena follows e listas de mute via armazenamento criptografado [NIP-78](/pt/topics/nip-78/) (Application-specific Data) com versionamento rotativo de 3 slots. O desempenho de inicialização melhorou através de serviços de notificação diferidos, renderização DOM lazy via IntersectionObserver (reduzindo nós DOM de ~15.000 para ~3.000 em um feed de 200 eventos) e TTLs estendidos de cache outbox ([PR #208](https://github.com/zapcooking/frontend/pull/208)). Um modal de impressão de receita personalizável ([PR #205](https://github.com/zapcooking/frontend/pull/205)) permite que usuários alternem quais seções incluir com pré-visualização ao vivo. Integração com [Branta SDK](https://github.com/BrantaOps/branta-core) ([PR #222](https://github.com/zapcooking/frontend/pull/222)) adiciona proteções de verificação para requisições POST e GET.

### Keep: Migração de Estado Orientada por Rust

[Keep](https://github.com/privkeyio/keep-android), o gerenciador de chaves privadas baseado no Nostr para Android, mergeou o [PR #178](https://github.com/privkeyio/keep-android/pull/178), deletando quatro stores de configuração Kotlin em favor de estado compartilhado orientado por Rust da camada keep-mobile. Um loop de polling de 10 segundos foi substituído por `KeepStateCallback` push-based do Rust. O [PR #179](https://github.com/privkeyio/keep-android/pull/179) adiciona backup e restauração criptografados com proteção por passphrase.

### Mostro Mobile: Criptografia de Chat de Disputa

[Mostro Mobile](https://github.com/MostroP2P/mobile), o cliente mobile para a plataforma de trading P2P de Bitcoin Mostro, lançou uma migração em duas fases da criptografia de chat de disputa. O primeiro passo ([PR #495](https://github.com/MostroP2P/mobile/pull/495)) troca de encapsulamento específico do mostro para criptografia de chave compartilhada derivada da pubkey do admin. Construindo sobre isso, o [PR #501](https://github.com/MostroP2P/mobile/pull/501) unifica o modelo de mensagem com `NostrEvent` e armazena eventos gift wrap criptografados em disco, consistente com o padrão de chat peer-to-peer. Uma correção de assinatura BIP-340 ([PR #496](https://github.com/MostroP2P/mobile/pull/496)) sobrescreve a dependência bip340 para 0.2.0, resolvendo um bug de padding `bigToBytes()` que causava 1-2% das assinaturas Schnorr serem inválidas e 100% de falha para chaves cuja chave pública começa com `0x00`. Detalhes do Pedido agora mostra labels de status legíveis em vez de valores brutos do protocolo, localizados em inglês, espanhol, italiano e francês ([PR #502](https://github.com/MostroP2P/mobile/pull/502)). HalCash foi adicionado e SEPA removido como método de pagamento ([PR #493](https://github.com/MostroP2P/mobile/pull/493)), já que transferências SEPA podem exceder 24 horas (SEPA Instant permanece).

No lado do servidor, [Mostro](https://github.com/MostroP2P/mostro) corrigiu a restauração de sessão de disputa para incluir o campo do iniciador ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) e agora fecha automaticamente disputas ativas quando um vendedor libera fundos, publicando um evento Nostr de liquidação para que clientes admin vejam a resolução ([PR #606](https://github.com/MostroP2P/mostro/pull/606)).

## Cinco Anos de Fevereiros do Nostr

[A newsletter do mês passado](/pt/newsletters/2026-01-28-newsletter/#cinco-anos-de-janeiros-do-nostr) traçou os marcos de janeiro do Nostr desde o desenvolvimento inicial, passando pela explosão do Damus, até a infraestrutura de segurança em 2026. Esta retrospectiva cobre o que aconteceu em cada fevereiro de 2021 a 2026.

### Fevereiro de 2021: A Reescrita

Três meses após sua existência, o fevereiro do Nostr produziu a mudança inicial mais consequente do protocolo. Em 14-15 de fevereiro, fiatjaf [reescreveu o NIP-01](https://github.com/nostr-protocol/nostr/commit/33a1a70), substituindo o formato de mensagem original pelo modelo EVENT/REQ/CLOSE que o protocolo ainda usa. Antes dessa reescrita, clientes e relays se comunicavam através de uma estrutura mais simples. Separar publicação de evento (EVENT) de gerenciamento de assinatura (REQ/CLOSE) habilitou filtragem do lado do relay que se provaria essencial para escalar.

[NIP-04](/pt/topics/nip-04/) chegou no mesmo mês, adicionando mensagens diretas criptografadas usando segredos compartilhados derivados de troca de chaves Diffie-Hellman sobre secp256k1. Sua criptografia era básica (AES-256-CBC) e seria depois substituída pela criptografia auditada do [NIP-44](/pt/topics/nip-44/), mas deu aos poucos usuários iniciais seu primeiro canal de comunicação privada no protocolo.

O ferramental expandiu com [noscl](https://github.com/fiatjaf/noscl), um cliente de linha de comando em Go para interação com relays pelo terminal, e futurepaul iniciou [nostr-rs](https://github.com/futurepaul/nostr-rs), uma implementação inicial em Rust. A rede inteira rodava em dois ou três relays, coordenada através de um [grupo no Telegram](https://t.me/nostr_protocol), com aproximadamente sete contribuidores ativos.

### Fevereiro de 2022: Ganhando Tração

O [post no Hacker News](https://news.ycombinator.com/item?id=29749061) de 31 de dezembro de 2021 continuou atraindo desenvolvedores em fevereiro. O repositório [nostr-protocol/nostr](https://github.com/nostr-protocol/nostr) (o [repositório formal de NIPs](https://github.com/nostr-protocol/nips) não existiria até maio de 2022) recebeu seis pull requests em fevereiro, incluindo NIP-13 (Proof of Work) de vinliao, NIP-14 (Reputation) de fiatjaf, NIP-15 (Resource Relations) de Cameri e [NIP-17](https://github.com/nostr-protocol/nostr/pull/75) (Git Updates Over Nostr) de melvincarvalho. O número do NIP seria depois reatribuído para Private Direct Messages; colaboração git no Nostr continuou separadamente através do que se tornou [gitworkshop.dev](https://gitworkshop.dev).

O [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) de Greg Heartsfield foi o cavalo de batalha do mês com 34 commits e três lançamentos. A versão 0.5.0 em 12 de fevereiro adicionou limites de publicação para usuários verificados por [NIP-05](/pt/topics/nip-05/). As versões 0.5.1 e 0.5.2 seguiram nas duas semanas seguintes, e o relay lidou com a maior parte do tráfego da rede sozinho.

Robert C. Martin (Uncle Bob) estava construindo [more-speech](https://github.com/unclebob/more-speech), um cliente desktop em Clojure, registrando 69 commits entre 18 de janeiro e o final de fevereiro. Seu envolvimento trouxe atenção da comunidade mais ampla de engenharia de software. A extensão de navegador [nos2x](https://github.com/fiatjaf/nos2x) de fiatjaf lançou suporte a descriptografia [NIP-04](/pt/topics/nip-04/) e políticas de preferência de relay em fevereiro, implementando a interface `window.nostr` ([NIP-07](/pt/topics/nip-07/)) que clientes web ainda usam para delegação de chaves.

[Branle](https://github.com/fiatjaf/branle), ainda o cliente web principal, ganhou registro de handler do protocolo `web+nostr` em 13 de fevereiro, uma tentativa inicial de deep linking entre aplicações Nostr. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) aprimorou a validação NIP-05. [go-nostr](https://github.com/nbd-wtf/go-nostr) adicionou suporte a DM criptografada NIP-04 e parsing NIP-12 (Generic Tag Queries) em 11 commits. A rede operava com aproximadamente 7-15 relays com uma base de usuários ativos provavelmente na casa das baixas centenas. Damus e Nostream ainda não existiam e não apareceriam até abril de 2022.

### Fevereiro de 2023: Atenção Internacional

Fevereiro de 2023 trouxe ao Nostr sua maior onda de atenção pública. [Damus](https://github.com/damus-io/damus), o cliente iOS de William Casarin, havia sido [aprovado na App Store da Apple em 31 de janeiro](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store) após repetidas rejeições. Em 1º de fevereiro alcançou o top 10 em Redes Sociais nos EUA. Dois dias depois, em 2 de fevereiro, a [Apple removeu o Damus da App Store da China](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) supostamente a pedido da Administração do Ciberespaço da China.

Grandes veículos incluindo TechCrunch e CoinDesk cobriram a remoção, amplificando a conscientização tanto do app quanto do protocolo. Chaves públicas únicas com metadados no nostr.directory ultrapassaram 300.000 em 3 de fevereiro. Todos os relays eram operados por entusiastas pagando do próprio bolso, e a infraestrutura se esforçou para lidar com a carga. Aproximadamente 289 relays eram rastreados no início de fevereiro, número que continuou crescendo.

O [repositório de NIPs](https://github.com/nostr-protocol/nips) registrou 29 pull requests mergeados naquele mês, a maior contagem de um único mês na história do protocolo até aquele ponto. [NIP-57](https://github.com/nostr-protocol/nips/pull/224) (Lightning Zaps) e [NIP-23](https://github.com/nostr-protocol/nips/pull/220) (Long-form Content) ambos foram mergeados em 13 de fevereiro, adicionando micropagamentos Bitcoin e expandindo o Nostr além de posts curtos em um único dia. [NIP-65](/pt/topics/nip-65/) (Relay List Metadata) havia sido mergeado uma semana antes, em 7 de fevereiro, habilitando o modelo outbox que se seguiu. [NIP-46](/pt/topics/nip-46/) (Nostr Connect) e [NIP-58](/pt/topics/nip-58/) (Badges) também foram aprovados antes do fim do mês.

A Human Rights Foundation [concedeu US$50.000 a William Casarin para desenvolvimento do Nostr e Damus](https://hrf.org/devfund2023q1) em 21 de fevereiro, uma das primeiras bolsas institucionais para um projeto Nostr. A OpenSats ainda não havia lançado seu fundo Nostr (isso viria em [julho de 2023](https://opensats.org/blog/nostr-grants-july-2023)).

### Fevereiro de 2024: Durabilidade do Protocolo

Fevereiro de 2024 mudou o foco de crescimento para durabilidade do protocolo. [NIP-17](/pt/topics/nip-17/) (Private Direct Messages), aberto desde julho anterior, estava trabalhando em direção a uma substituição para a envelhecida criptografia [NIP-04](/pt/topics/nip-04/) usando criptografia auditada do [NIP-44](/pt/topics/nip-44/) e gift wrapping [NIP-59](/pt/topics/nip-59/). NIP-04 vazava metadados para operadores de relay, que podiam ver pares remetente-destinatário. NIP-17 esconde a identidade do remetente atrás de pares de chaves descartáveis e foi mergeado na primavera seguinte após uma rodada final de revisão em março.

[NIP-29](/pt/topics/nip-29/) (Simple Groups) [foi mergeado em 28 de fevereiro](https://github.com/nostr-protocol/nips/pull/566) após meses de discussão, definindo como relays podem hospedar chats de grupo moderados com papéis de admin e controle de acesso. [NIP-92](/pt/topics/nip-92/) (tags imeta) foi mergeado em 1º de fevereiro, padronizando como clientes anexam dimensões de imagem e pré-visualizações blurhash a eventos de mídia.

Em 16 de fevereiro, o repositório de NIPs adicionou [BREAKING.md](https://github.com/nostr-protocol/nips/commit/62c48eff), um arquivo rastreando mudanças incompatíveis com versões anteriores na especificação do protocolo. Sua criação reconheceu que o Nostr havia alcançado um nível de maturidade onde mudanças que quebram compatibilidade precisavam de documentação formal.

Vinte e dois pull requests foram mergeados naquele mês. [npub.cash](https://github.com/cashubtc/npubcash-server) foi lançado como serviço de endereço Lightning permitindo que qualquer npub receba pagamentos sem rodar um servidor. Um [artigo acadêmico](https://arxiv.org/abs/2402.05709) publicado em 8 de fevereiro descobriu que 95% dos relays de uso gratuito não conseguiam cobrir custos operacionais através de doações, com 35% dos relays pagos cobrando taxas de admissão abaixo de 1.000 sats (aproximadamente US$0,45 na época).

### Fevereiro de 2025: Crescimento de Infraestrutura

Fevereiro de 2025 produziu 28 pull requests mergeados no repositório de NIPs. Um NIP de [Direito ao Desaparecimento](/pt/topics/nip-62/) foi mergeado em 19 de fevereiro, definindo como usuários podem solicitar a exclusão de seus dados dos relays em resposta a questões regulatórias sobre portabilidade de dados e controle do usuário.

[NIP-60](/pt/topics/nip-60/) (Cashu Wallet) e NIP-61 (Nutzaps) receberam atualizações de simplificação, otimizando o formato de armazenamento de tokens ecash. Um rollout de q-tag (quote tag) continuou em múltiplos NIPs, padronizando como eventos referenciam outros eventos para citação e threading.

Lançamentos de clientes marcaram progresso constante. [Notedeck](https://github.com/damus-io/notedeck) v0.3.0 alpha foi lançado no último dia de janeiro, com adoção continuando em fevereiro. Primal v2.1 seguiu em 7 de fevereiro, e [GRAIN](https://github.com/0ceanSlim/grain) v0.3.0, uma implementação de relay em Go, foi lançado em 21 de fevereiro.

NOSTRLDN v5 reuniu a comunidade Nostr de Londres para seu quinto meetup. Uma ponte DVMCP conectou as Data Vending Machines do Nostr ([NIP-90](/pt/topics/nip-90/)) com o Model Context Protocol, prefigurando o trabalho de integração de agentes de IA que chegaria no mês seguinte.

### Fevereiro de 2026: Além das Redes Sociais

*A atividade de fevereiro de 2026 é extraída das edições do Nostr Compass [#8](/pt/newsletters/2026-02-04-newsletter/) a [#11](/pt/newsletters/2026-02-25-newsletter/).*

Fevereiro de 2026 produziu a mais ampla gama de desenvolvimento na camada de aplicação em qualquer mês do Nostr. [Mostro](https://github.com/MostroP2P/mostro) lançou seu [primeiro beta público](/pt/newsletters/2026-02-11-newsletter/#mostro-lança-primeiro-beta-público) para trading descentralizado peer-to-peer de Bitcoin, e [Zapstore](https://github.com/zapstore/zapstore) alcançou a [versão 1.0 estável](/pt/newsletters/2026-02-11-newsletter/#zapstore-v100) após meses em teste de release candidate. [White Noise v0.3.0](/pt/newsletters/2026-02-25-newsletter/#white-noise-v030) entregou mensagens em tempo real criptografadas com [Marmot](/pt/topics/mls/) com suporte ao assinador Amber e mais de 160 melhorias mergeadas.

Propostas concorrentes de agentes de IA de pablof7z (NIP-AE para fluxos de trabalho de agentes, NIP-AD para anúncios de servidores MCP) e joelklabo (AI Agent Messages) chegaram junto com uma [proposta de Coordenação de Agentes DVM](/pt/newsletters/2026-02-25-newsletter/#atualizações-de-nips) estendendo [NIP-90](/pt/topics/nip-90/). [ContextVM](/pt/newsletters/2026-02-25-newsletter/#contextvm-mcp-sobre-nostr) lançou melhorias no SDK conectando o Model Context Protocol ao transporte Nostr. [Burrow](/pt/newsletters/2026-02-25-newsletter/#burrow-mensagens-mls-para-agentes-de-ia) adicionou mensagens criptografadas com [Marmot](/pt/topics/mls/) tanto para agentes de IA quanto humanos, estendendo a identidade e infraestrutura de relay do Nostr para comunicação máquina-a-máquina.

[FIPS](/pt/newsletters/2026-02-25-newsletter/#fips-redes-mesh-nativas-do-nostr) lançou uma implementação Rust funcional de redes mesh nativas do Nostr, usando pares de chaves secp256k1 como identidades de nó com roteamento agnóstico de transporte sobre UDP, Ethernet, Bluetooth ou rádio LoRa. Seu design mostrou que o modelo de chaves do Nostr se estende além das redes sociais para infraestrutura de rede física.

A [OpenSats anunciou sua décima quinta onda de bolsas Nostr](https://opensats.org/blog/fifteenth-wave-of-nostr-grants), financiando projetos incluindo ContextVM e Nostube. Mudanças de protocolo incluíram suporte a hold invoice do [NIP-47](/pt/topics/nip-47/) para Nostr Wallet Connect e HyperLogLog do [NIP-45](/pt/topics/nip-45/) (Counting Results) para estimativa de contagem do lado do relay. A descobribilidade de provedores de serviço do [NIP-85](/pt/topics/nip-85/) (Trusted Assertions) para pontuação de [Web of Trust](/pt/topics/web-of-trust/) também foi mergeada. [rust-nostr](https://github.com/rust-nostr/nostr) iniciou um redesign completo de API enquanto Nostria 3.0 e [Frostr](https://github.com/FROSTR-ORG) (iOS TestFlight) ambos foram lançados. A camada de cache local do [Blossom](/pt/topics/blossom/) tratou a disponibilidade de mídia entre relays.

### Olhando para Frente

Cinco fevereiros de história do protocolo mostram uma progressão consistente de trabalho fundacional para diversificação na camada de aplicação, com o influxo de usuários de 2023 como ponto de virada. Em 2021, sete contribuidores trabalhavam em três relays. Em 2026, o mesmo protocolo suportava redes mesh e propostas de agentes autônomos rodando em infraestrutura de produção.

---

É isso por esta semana. Construindo algo ou tem novidades para compartilhar? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via [NIP-17](/pt/topics/nip-17/) DM</a> ou nos encontre no Nostr.
