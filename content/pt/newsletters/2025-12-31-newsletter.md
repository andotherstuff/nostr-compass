---
title: 'Nostr Compass #3'
date: 2025-12-31
publishDate: 2025-12-31
translationOf: /en/newsletters/2025-12-31-newsletter.md
translationDate: 2025-12-31
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal do ecossistema do protocolo Nostr.

**Esta semana:** Ao encerrar 2025, olhamos para trás para cinco anos de marcos de dezembro na evolução do Nostr. Desde o primeiro lançamento do cliente de fiatjaf em dezembro de 2020, passando pela doação fundamental de Jack Dorsey de 14 BTC em dezembro de 2022, até a proliferação de NIP-55 signer este mês e a aceleração de cache de 162x do NDK, dezembro consistentemente marcou pontos de virada para o protocolo. Esta edição especial traça a história técnica através de cada dezembro, documentando o crescimento do protocolo de dois relays experimentais para mais de 2.500 nós em 50 países. Além disso: O módulo desktop do Amethyst toma forma através do Quartz, Notedeck ganha mensagens, Citrine hospeda aplicações web, e NIP-54 corrige a internacionalização para scripts não latinos.

## Resumo de Dezembro: Cinco Anos de Dezembros do Nostr

Nostr completa cinco anos este ano. fiatjaf iniciou o protocolo em 7 de novembro de 2020, e cada dezembro desde então marcou uma fase distinta em sua evolução: de prova de conceito a movimento global a ecossistema de produção. Este é um retrospectivo técnico de dezembro de 2020 até dezembro de 2025, os anos formativos que estabeleceram a fundação do Nostr e catalisaram seu momento de explosão.

### Dezembro 2020: Gênese

O primeiro mês completo de existência do Nostr viu fiatjaf lançar [Branle](https://github.com/fiatjaf/branle), o primeiro cliente do protocolo, construído com Quasar (Vue.js) e absurd-sql para armazenamento local. fiatjaf já havia estabelecido a arquitetura central: usuários identificados por chaves públicas secp256k1, todas as postagens assinadas criptograficamente, relays servindo como armazenamento simples que não se comunicam entre si. Um ou dois relays experimentais serviam um punhado de primeiros adotantes coordenando no grupo do Telegram [@nostr_protocol](https://t.me/nostr_protocol), que foi lançado em 16 de novembro. A [documentação original](https://fiatjaf.com/nostr.html) descrevia "o protocolo aberto mais simples que é capaz de criar uma rede social global resistente à censura", uma premissa que levaria mais dois anos para ser provada.

### Dezembro 2021: Desenvolvimento Inicial

Em 31 de dezembro de 2021, Nostr chegou à [primeira página do Hacker News](https://news.ycombinator.com/item?id=29749061) com 110 pontos e 138 comentários, submetido por Cameri. Isso marcou a primeira exposição significativa do protocolo à comunidade mais ampla de desenvolvedores. A rede funcionava com aproximadamente sete relays com menos de 1.000 usuários. Branle recebeu atualizações incluindo importação de chave privada (31 de dezembro) e suporte multi-relay. Um cliente de linha de comando, noscl, fornecia interação baseada em terminal. As especificações do protocolo existiam na documentação de fiatjaf, embora o [repositório formal de NIPs](https://github.com/nostr-protocol/nips) não fosse criado até maio de 2022. O protocolo era, como fiatjaf descreveu, "um trabalho em progresso".

### Dezembro 2022: O Ponto de Virada

Dezembro de 2022 transformou Nostr de um experimento de nicho em um movimento mainstream. O catalisador veio em 15 de dezembro, quando Jack Dorsey doou [14.17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding) (~$245.000-$250.000) para fiatjaf após descobrir o protocolo e declarar que era "100 por cento o que queríamos do Bluesky, mas não foi desenvolvido por uma empresa". Em 16 de dezembro, fiatjaf anunciou a divisão de fundos com o desenvolvedor do Damus William Casarin (jb55), e Dorsey verificou sua conta Nostr (npub: `npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`). O financiamento legitimou o projeto da noite para o dia.

Na mesma semana, o caos do Twitter acelerou a adoção. De 14 a 15 de dezembro houve suspensões de jornalistas proeminentes do New York Times, CNN e Washington Post. Em 18 de dezembro, o Twitter [anunciou banimentos](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/) de contas promovendo Nostr, Mastodon e outras plataformas. A política foi revertida no dia seguinte após reação negativa. O êxodo levou os usuários a explorar alternativas.

O desenvolvimento do protocolo acelerou. Em 16 de dezembro, [NIP-19](/pt/topics/nip-19/) foi mesclado ([#57](https://github.com/nostr-protocol/nips/pull/57)), introduzindo identificadores codificados em bech32 (npub, nsec, note, nprofile, nevent) que tornavam as chaves legíveis por humanos e distinguíveis. O repositório de NIPs registrou mais de 36 commits naquele mês, incluindo atualizações de NIP-40 e NIP-07. Os clientes proliferaram: Damus preencheu seu beta TestFlight em horas, Astral bifurcou Branle para criação de perfis, Snort foi lançado como um cliente web "rápido e resistente à censura", e Vitor Pamplona começou o desenvolvimento do Amethyst. Alby v1.22.1 "Kemble's Cascade of Stars" foi lançado em 22 de dezembro com suporte a NIP-19. Até 7 de dezembro, Nostr tinha aproximadamente 800 usuários com perfis; quando Damus chegou à App Store em 31 de janeiro de 2023, as comportas se abriram, impulsionando o crescimento para mais de 315.000 usuários até junho de 2023.

### Dezembro 2023: Maturação do Ecossistema

Dezembro de 2023 marcou um ponto de inflexão crítico para a segurança do protocolo Nostr. Em 20 de dezembro, a [revisão 3 do NIP-44 foi mesclada](https://github.com/nostr-protocol/nips/pull/746) após uma auditoria de segurança independente da Cure53 (NOS-01) que identificou 10 problemas nas implementações TypeScript, Go e Rust, incluindo ataques de timing e preocupações de forward secrecy. A especificação atualizada substituiu a criptografia defeituosa do [NIP-04](/pt/topics/nip-04/) por ChaCha20 e HMAC-SHA256, estabelecendo a fundação criptográfica que agora sustenta os DMs privados do [NIP-17](/pt/topics/nip-17/) e o gift wrapping do [NIP-59](/pt/topics/nip-59/). Na mesma semana, [OpenSats anunciou sua quarta onda de grants](https://opensats.org/blog/nostr-grants-december-2023) em 21 de dezembro, financiando sete projetos incluindo Lume, noStrudel, ZapThreads, e uma auditoria independente do NIP-44. Isso seguiu a [primeira onda em julho de 2023](https://opensats.org/blog/nostr-grants-july-2023) que havia financiado Damus, Coracle, Iris, e outros, trazendo a alocação total do Fundo Nostr para aproximadamente $3,4 milhões através de 39 grants.

O mês também expôs tensões de sustentabilidade no ecossistema. Em 28 de dezembro, William Casarin (jb55) [postou no Stacker News](https://stacker.news/items/368863) que 2024 seria "provavelmente o último ano do Damus", citando que "clientes nostr não geram dinheiro" após as restrições da Apple sobre zaps in-app limitarem severamente o potencial de receita. A equipe do Damus havia anteriormente rejeitado financiamento de VC. Enquanto isso, [Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1) foi lançado em 26 de dezembro, estendendo [NIP-47](/pt/topics/nip-47/) com métodos `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, e `get_info`, preparando o terreno para as integrações de wallets que se tornariam padrão em todos os clientes.

### Dezembro 2024: Avanço do Protocolo

Dezembro de 2024 abriu com o [lançamento Alpha do Notedeck](https://damus.io/notedeck/) em 30 de novembro, o cliente desktop baseado em Rust da equipe Damus com uma interface multi-coluna com suporte para múltiplas contas. Construído para Linux, macOS e Windows (Android planejado para 2025), Notedeck foi inicialmente enviado para assinantes do Damus Purple e representou uma expansão estratégica além do iOS. Duas semanas depois, [OpenSats anunciou sua nona onda de grants](https://opensats.org/blog/9th-wave-of-nostr-grants) em 16 de dezembro, financiando AlgoRelay (o primeiro relay algorítmico para feeds personalizados), Pokey (app Android com mesh Bluetooth para internet restrita), Nostr Safebox (armazenamento de tokens Cashu com [NIP-60](/pt/topics/nip-60/)), e LumiLumi (cliente web leve e acessível), levando a alocação total do Fundo Nostr para aproximadamente $9 milhões, um aumento de 67% ano a ano.

O mês viu maturação significativa de clientes em todo o ecossistema. [Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0) chegou em 23 de dezembro com suporte a File Metadata ([NIP-92](/pt/topics/nip-92/)/[NIP-94](/pt/topics/nip-94/)), integração Blossom, e busca em relay com [NIP-50](/pt/topics/nip-50/). [Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0) foi lançado em 12 de dezembro com onboarding reformulado e integração nostr-editor. O desenvolvimento do protocolo permaneceu ativo com 30 pull requests submetidos entre 9 e 22 de dezembro (10 mesclados), incluindo reescritas do [NIP-46](/pt/topics/nip-46/) para usar apenas criptografia NIP-44 e trabalho contínuo no [NIP-104](/pt/topics/nip-104/) para criptografia double ratchet no nível do Signal. Estatísticas de rede mostraram mais de 224.000 eventos diários de pubkeys confiáveis, crescimento de 4x ano a ano em novos perfis com listas de contatos, e um aumento de 50% em eventos de escrita pública.

### Dezembro 2025: Expansão do Ecossistema

Dezembro de 2025 trouxe maturação contínua do protocolo e expansão do ecossistema. Em 21 de dezembro, [OpenSats anunciou sua décima quarta onda de grants Nostr](https://opensats.org/blog/fourteenth-wave-of-nostr-grants), financiando três projetos: YakiHonne (um cliente multiplataforma com portal de criadores para conteúdo de formato longo e integração de pagamentos Cashu/Nutzaps), Quartz (biblioteca Kotlin Multiplatform de Vitor Pamplona que alimenta Amethyst e permitirá uma versão iOS), e Nostr Feedz (integração bidirecional RSS-para-Nostr por PlebOne). Renovações de grants foram para Dart NDK e nostr-relay de Mattn.

A evolução do protocolo continuou com [NIP-BE](/pt/topics/nip-be/) (mensagens Bluetooth Low Energy, [#1979](https://github.com/nostr-protocol/nips/pull/1979)) mesclado em novembro, habilitando sincronização offline de dispositivos. [NIP-A4](/pt/topics/nip-a4/) (Mensagens Públicas, kind 24, [#1988](https://github.com/nostr-protocol/nips/pull/1988)) chegou mais tarde no mês, definindo mensagens de tela de notificação que usam tags `q` para evitar complicações de threading. [NIP-29](/pt/topics/nip-29/) recebeu grande clarificação ([#2106](https://github.com/nostr-protocol/nips/pull/2106)), introduzindo a tag `hidden` para grupos verdadeiramente privados e não descobríveis. A especificação do [NIP-55](/pt/topics/nip-55/) também viu refinamento ([#2166](https://github.com/nostr-protocol/nips/pull/2166)), abordando um erro comum de implementação onde desenvolvedores chamavam `get_public_key` de processos em segundo plano.

No lado do cliente, [Primal Android se tornou um signer NIP-55 completo](/pt/newsletters/2025-12-24-newsletter/#news) através de oito PRs mesclados implementando `LocalSignerContentProvider`, juntando-se a Amber e Aegis como opções de assinatura no Android. A [biblioteca NDK alcançou consultas de cache 162x mais rápidas](/pt/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes) (de ~3.690ms para ~22ms) eliminando escritas duplicadas e buscas desnecessárias de cache LRU ([PR #371](https://github.com/nostr-dev-kit/ndk/pull/371), [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)). Shopstr introduziu [Zapsnags](/pt/newsletters/2025-12-24-newsletter/#news) para vendas relâmpago via zaps. White Noise lançou notificações push que preservam a privacidade com [MIP-05](/pt/topics/mip-05/). Veja [Newsletter #1](/pt/newsletters/2025-12-17-newsletter/) e [Newsletter #2](/pt/newsletters/2025-12-24-newsletter/) para cobertura completa.

---

Cinco anos atrás, fiatjaf lançou Branle para um punhado de usuários através de dois relays experimentais. Hoje, o protocolo suporta mais de 140 clientes, mais de 2.500 relays em 50 países, e uma crescente rede de confiança ligando centenas de milhares de keypairs. O padrão de dezembro de grandes lançamentos continuou este mês com mensagens Bluetooth, proliferação de signers no Android, e grants de infraestrutura sinalizando investimento sustentado em ferramentas multiplataforma.

## Notícias

**Amethyst Desktop Toma Forma** - O grant do Quartz da décima quarta onda do OpenSats já está produzindo resultados. [PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625) cria um módulo `:desktopApp` completo para Amethyst usando Compose Multiplatform, com telas de login e feed global funcionais no Desktop JVM. A arquitetura converte o módulo `:commons` para Kotlin Multiplatform com uma estrutura de source set limpa (`commonMain`, `jvmAndroid`, `androidMain`, `jvmMain`), permitindo componentes de UI compartilhados entre Android e desktop enquanto deixa decisões específicas de plataforma para cada target. Isso estabelece a fundação para a eventual versão iOS através da mesma abordagem Kotlin Multiplatform.

**Amethyst Respostas de Voz** - Uma entrega de Natal de davotoula: [PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622) adiciona telas dedicadas de resposta de voz com visualização de forma de onda, suporte para regravar, seleção de servidor de mídia, e indicadores de progresso de upload. Usuários agora podem responder tanto a mensagens de voz raiz quanto a respostas de voz com áudio.

**Notedeck Adiciona Mensagens** - Notedeck, o cliente desktop do Damus, ganhou um recurso de mensagens em [PR #1223](https://github.com/damus-io/notedeck/pull/1223), expandindo além da navegação do timeline para comunicação direta.

**Citrine Hospeda Aplicações Web** - Citrine agora pode [hospedar aplicações web](https://github.com/greenart7c3/Citrine/pull/81), transformando seu telefone em um servidor web Nostr local-first. Um [PR #85](https://github.com/greenart7c3/Citrine/pull/85) separado adiciona reconexão automática e broadcasting de eventos quando a conectividade de rede retorna, com cobertura de testes abrangente através dos níveis de API do Android.

**Registro de Kits de Desenvolvimento Nostrability** - O rastreador de [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264) mantém um registro curado de SDKs, bibliotecas e ferramentas de desenvolvimento através de linguagens (TypeScript, Rust, Python, Go, Dart, Swift, e mais). Se você é novo no desenvolvimento Nostr, este é um ponto de partida útil para encontrar o toolkit certo para seu stack.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

- **[NIP-54](/pt/topics/nip-54/)** - Correção crítica de internacionalização para normalização de d-tag wiki ([#2177](https://github.com/nostr-protocol/nips/pull/2177)). Regras anteriores convertiam todos os caracteres não ASCII para `-`, quebrando suporte para japonês, chinês, árabe, cirílico e outros scripts. A especificação atualizada preserva letras UTF-8, aplica minúsculas apenas a caracteres com variantes de maiúsculas, e inclui exemplos abrangentes: `"ウィキペディア"` permanece `"ウィキペディア"`, `"Москва"` se torna `"москва"`, e scripts mistos como `"日本語 Article"` normalizam para `"日本語-article"`.

## Lançamentos

**Zapstore 1.0-rc1** - A loja de aplicativos sem permissões baseada em Nostr lança o [primeiro release candidate](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1) de sua nova arquitetura, apresentando uma atualização completa de UI, gerenciador de pacotes reescrito com melhor tratamento de erros, App Stacks para descoberta curada, telas de perfil redesenhadas, verificação de atualizações em segundo plano, e rolagem infinita em listas de lançamentos.

**KeyChat v1.38.1** - O app de mensagens criptografadas baseado em MLS [adiciona suporte UnifiedPush](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489) para notificações push de Android e Linux, mais autenticação biométrica para operações de privacidade. Disponível para Android, Windows, macOS e Linux.

**Alby Go v2.0.0** - O companheiro de wallet Lightning móvel [lança um redesign visual](https://github.com/getAlby/go/releases/tag/v2.0.0) com novo logo, paleta de cores atualizada, agenda de endereços redesenhada, e teclado de entrada de valores melhorado. BTC Map agora é acessível da tela inicial, e descrições de transações aparecem em notificações.

**nak v0.17.4** - A ferramenta de linha de comando Nostr de fiatjaf [lançada](https://github.com/fiatjaf/nak/releases/tag/v0.17.4), seguindo a correção de restrição LMDB Linux da v0.17.3 da semana passada.

## Mudanças notáveis de código e documentação

*Pull requests abertos e trabalho em estágio inicial que vale a pena acompanhar.*

### Damus (iOS)

[NIP-19 relay hints](https://github.com/damus-io/damus/pull/3477) implementa consumo de relay hints para busca de eventos. Quando usuários abrem links nevent, nprofile ou naddr, Damus agora extrai relay hints dos dados TLV bech32 e se conecta a relays efêmeros para buscar conteúdo que não está no pool de relays do usuário. A implementação inclui limpeza com contagem de referências para prevenir condições de corrida durante buscas concorrentes. [Detecção de URL de imagem](https://github.com/damus-io/damus/pull/3474) converte automaticamente URLs de imagem coladas em miniaturas de preview no compositor, com badge de posição de carrossel para múltiplas imagens. [Conversão de colagem npub](https://github.com/damus-io/damus/pull/3473) transforma strings npub/nprofile coladas em links de menção com resolução de perfil assíncrona.

### Amethyst (Android)

[Payment targets](https://github.com/vitorpamplona/amethyst/pull/1627) adiciona uma interface de evento para splits de zap NIP-57, permitindo que posts especifiquem múltiplos destinatários que compartilham zaps recebidos (útil para colaborações, divisão de receita, ou dar gorjetas tanto para criadores de conteúdo quanto para as ferramentas que eles usam). [Documentação de paridade de recursos Quartz](https://github.com/vitorpamplona/amethyst/pull/1624) adiciona uma tabela detalhada rastreando quais recursos estão implementados através dos targets Android, Desktop JVM e iOS, notando que iOS está faltando criptografia central (`Secp256k1Instance`), serialização JSON e estruturas de dados.

### Notedeck (Desktop)

[Reconstrução de filtro de timeline](https://github.com/damus-io/notedeck/pull/1226) corrige um bug onde contas deixadas de seguir continuavam aparecendo em feeds. Filtros de timeline eram construídos uma vez da lista de contatos e nunca atualizados; a correção adiciona rastreamento de `contact_list_timestamp` e um método `invalidate()` para acionar reconstruções quando o estado de seguimento muda.

### Citrine (Android Relay)

[ContentProvider API](https://github.com/greenart7c3/Citrine/pull/86) expõe o banco de dados de eventos do relay local para outros apps Android via `ContentResolver`. Diferente da interface WebSocket (que requer que apps mantenham uma conexão persistente e falem o protocolo relay Nostr), ContentProvider oferece acesso direto síncrono ao banco de dados através do mecanismo IPC nativo do Android. Apps externos podem consultar eventos por ID, pubkey, kind ou intervalo de datas, inserir novos eventos com validação, e deletar eventos sem gerenciar conexões de socket.

### rust-nostr (Library)

[Suporte NIP-40 em nível de relay](https://github.com/rust-nostr/nostr/pull/1183) adiciona tratamento de expiração no nível do relay builder. Eventos expirados agora são rejeitados antes do armazenamento e filtrados antes de enviar para clientes, eliminando a necessidade de cada implementação de banco de dados tratar verificações de expiração independentemente.

### nak (CLI)

[Blossom mirror](https://github.com/fiatjaf/nak/pull/91) implementa funcionalidade de espelhamento de blobs para a ferramenta de linha de comando.

### Mostro (P2P Trading)

[Dev fee audit events](https://github.com/MostroP2P/mostro/pull/559) adiciona trilhas de auditoria transparentes para pagamentos ao fundo de desenvolvimento através de eventos Nostr kind 8383. A implementação publica eventos de auditoria não bloqueantes após pagamentos de fees bem-sucedidos, incluindo detalhes de ordem e hashes de pagamento enquanto exclui pubkeys de comprador/vendedor por privacidade.

### MDK (Marmot Development Kit)

Três correções de auditoria de segurança chegaram: [Verificação de autor](https://github.com/marmot-protocol/mdk/pull/40) força que pubkeys de rumor correspondam às credenciais do remetente MLS, prevenindo ataques de impersonação. [KeyPackage identity binding](https://github.com/marmot-protocol/mdk/pull/41) verifica que a identidade da credencial corresponda aos assinantes de eventos. [Validação de atualização de admin](https://github.com/marmot-protocol/mdk/pull/42) previne conjuntos de admin vazios e atribuições de admin a não membros.

### Shopstr (Marketplace)

[HODL invoice escrow](https://github.com/shopstr-eng/shopstr/pull/217) implementa um sistema de pagamento que minimiza confiança para bens físicos. A arquitetura usa `makeHoldInvoice` do Alby para bloquear fundos do comprador em sua própria wallet, com liquidação acionada apenas após verificação de inventário do comerciante. O protocolo de handshake flui através de DMs criptografados [NIP-17](/pt/topics/nip-17/): comprador envia solicitação de pedido, comerciante responde com HODL invoice, comprador paga (fundos bloqueados), comerciante confirma estoque e envio, então a liquidação libera os fundos. Suporte de carrinho multi-comerciante divide pagamentos entre vendedores.

### Jumble (Web Client)

[Modo de descoberta por relay](https://github.com/CodyTseng/jumble/pull/713) adiciona um toggle para ocultar posts de usuários seguidos em relays específicos, habilitando feeds de descoberta baseados em idioma (ex., nostr.band/lang/*). O recurso filtra posts onde o pubkey do autor aparece na lista de seguidos do usuário, persistindo o estado do toggle por URL de relay no localStorage.

### White Noise (Encrypted Messaging)

[Retry de upload de mídia](https://github.com/marmot-protocol/whitenoise/pull/937) adiciona opções de retry para uploads falhos. [Avisos de edição de perfil](https://github.com/marmot-protocol/whitenoise/pull/927) alerta usuários sobre mudanças de perfil. No backend, [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422) corrige uma condição de corrida na criação de AccountGroup.

### npub.cash (Lightning Address Service)

[Reescrita v3](https://github.com/cashubtc/npubcash-server/pull/40) migra para Bun para o monorepo e servidor, adiciona suporte SQLite, remove compatibilidade v1, implementa LUD-21, e adiciona atualizações de mint quote em tempo real.

### nostr-java (Library)

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1) lança refatorações de tratamento WebSocket e robustez de testes melhorada através de [dois PRs](https://github.com/tcheeric/nostr-java/pull/499).

### NIPs Repository

[Migração NIP-54 para Djot](https://github.com/nostr-protocol/nips/pull/2180) propõe uma mudança separada para a especificação wiki: mudar o formato de conteúdo de Asciidoc para Djot, uma linguagem de marcação leve com sintaxe mais limpa. O PR introduz links de estilo referência para wikilinks, tornando referências cruzadas entre artigos wiki mais legíveis na forma fonte. [NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179) introduz governança de multi-assinatura threshold para grupos Nostr usando FROST (Flexible Round-Optimized Schnorr Threshold signatures). Um Quorum é um nsec compartilhado entre membros através de um esquema T-de-N onde membros podem representar a si mesmos ou delegar a um conselho de representantes. Quando o conselho muda, o nsec antigo se torna obsoleto e um novo é distribuído—o ato final de qualquer conselho é assinar o evento de transição de governança. A especificação define membresía (pública ou privada), eleições e enquetes (votos populares, votos de desconfiança), "leis" opcionais em linguagem natural, e crucialmente, ontologias de quorum onde quorums podem ser membros de outros quorums, habilitando estruturas hierárquicas como localidades se juntando a corpos regionais. Casos de uso abrangem desenvolvimento de código fonte, conselhos de empresas, HOAs, e comunidades moderadas.

---

Isso é tudo por esta semana e este ano. Construindo algo? Tem notícias para compartilhar? Quer que cubramos seu projeto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via NIP-17 DM</a> ou encontre-nos no Nostr.
