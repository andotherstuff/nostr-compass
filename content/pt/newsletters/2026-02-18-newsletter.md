---
title: 'Nostr Compass #10'
date: 2026-02-18
translationOf: /en/newsletters/2026-02-18-newsletter.md
translationDate: 2026-02-18
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** Uma camada de cache local do Blossom toma forma à medida que projetos independentes convergem para acesso offline a mídia no Android. Alby lança um [sandbox para desenvolvedores NWC](https://sandbox.albylabs.com) para criar e testar integrações de Nostr Wallet Connect sem arriscar fundos reais. Propostas concorrentes para comunicação de agentes de IA no Nostr chegam na mesma semana de dois autores diferentes. fiatjaf remove campos não utilizados do [NIP-11](https://github.com/nostr-protocol/nips/pull/1946), eliminando políticas de retenção, códigos de país, política de privacidade e tags de preferência de comunidade que operadores de relay nunca adotaram. O [NIP-85](https://github.com/nostr-protocol/nips/pull/2223) faz merge com orientações de descoberta de provedores de serviço para Trusted Assertions. Uma nova tag `D` no [NIP-52](https://github.com/nostr-protocol/nips/pull/1752) habilita indexação temporal com granularidade de dia para eventos de calendário. Novos projetos incluem [Mapnolia](https://github.com/zeSchlausKwab/mapnolia) para distribuição descentralizada de tiles de mapa, [Pika](https://github.com/sledtools/pika) para mensagens criptografadas com MLS, [Keep](https://github.com/privkeyio/keep-android) para assinatura de limiar FROST no Android, [Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) para armazenamento endereçado por conteúdo com integração Nostr, e [Prism](https://github.com/hardran3/Prism) para compartilhar conteúdo no Nostr a partir de qualquer app Android. [Primal Android](https://github.com/PrimalHQ/primal-android-app) faz merge de 11 PRs de NWC adicionando suporte a carteira dupla e ciclo de vida automático do serviço. [Mostro Mobile](https://github.com/MostroP2P/mobile) lança [carteira Lightning embutida](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) via integração NWC. [Notedeck](https://github.com/damus-io/notedeck) se prepara para lançamento na Android App Store enquanto o HAVEN alcança [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3) com suporte a múltiplos npubs e backup em nuvem. Os deep dives desta semana cobrem o sistema de Trusted Assertions do NIP-85 para delegar cálculos de Web of Trust a provedores de serviço, e o protocolo de Eventos de Calendário do NIP-52 após sua atualização de indexação com granularidade de dia.

## Notícias

### Camada de Cache Local do Blossom Emerge

Múltiplos projetos independentes estão convergindo para o mesmo problema: acesso offline a mídia [Blossom](/pt/topics/blossom/) em dispositivos móveis.

[Morganite](https://github.com/greenart7c3/Morganite), um novo app Android de greenart7c3 (o desenvolvedor por trás do [Amber](https://github.com/greenart7c3/amber) e do [Citrine](https://github.com/greenart7c3/Citrine)), implementa cache no lado do cliente para mídia Blossom. Usuários podem acessar imagens e arquivos visualizados anteriormente sem conexão de rede.

[Aerith](https://github.com/hardran3/Aerith) lançou [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) com rotulagem de imagens, operações em massa de espelhamento/marcação/exclusão, filtragem por rótulo e tipo de arquivo, além de suporte inicial a cache local Blossom. Aerith é uma interface de gerenciamento para usuários que armazenam mídia em múltiplos servidores Blossom e precisam organizar e espelhar seus blobs.

Um novo [guia de implementação de cache local](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md) na especificação do Blossom documenta armazenamento de blobs no lado do cliente, enquanto [Prism](https://github.com/hardran3/Prism) (do mesmo desenvolvedor do Aerith) adiciona integração de upload Blossom ao seu fluxo de compartilhamento para Nostr no Android. Quatro projetos independentes convergiram para o mesmo problema esta semana: um app dedicado de cache, um gerenciador de mídia, uma especificação de referência e uma ferramenta de compartilhamento com integração Blossom, todos implementando armazenamento local persistente além do simples upload e recuperação.

### Sandbox NWC para Desenvolvedores da Alby

[Alby](https://sandbox.albylabs.com) lançou um ambiente sandbox para desenvolvedores que trabalham com [Nostr Wallet Connect (NIP-47)](/pt/topics/nip-47/). O sandbox oferece um serviço NWC hospedado onde desenvolvedores podem criar conexões de teste e enviar pagamentos simulados sem conectar a uma carteira Lightning real, enquanto observam o ciclo completo de requisição/resposta de eventos NWC em tempo real. Desenvolvedores geram uma string de conexão `nostr+walletconnect://` a partir do sandbox e a passam para o cliente. O sandbox então exibe os eventos kind 23194 de requisição e kind 23195 de resposta conforme fluem entre o cliente e o serviço de carteira.

Isso reduz a barreira para novas integrações NWC. Anteriormente, os testes exigiam uma carteira Lightning pessoal ou um serviço NWC auto-hospedado. O sandbox abstrai isso, fornecendo aos desenvolvedores um ciclo de feedback imediato para implementar os métodos `pay_invoice`, `get_balance`, `make_invoice`, `lookup_invoice` e `list_transactions` contra um endpoint NWC ativo.

### NIPs de Agentes de IA Chegam

Propostas para comunicação de agentes de IA no Nostr apareceram com poucos dias de diferença, abordando o problema sob ângulos distintos.

[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226) de joelklabo define um protocolo completo para interação de agentes de IA: kinds de evento para prompts, respostas, deltas de streaming, atualizações de status, telemetria de ferramentas, erros, cancelamentos e descoberta de capacidades. Um evento de descoberta `ai.info` (kind 31340, substituível) permite que agentes anunciem seus modelos suportados, ferramentas com schemas, suporte a streaming e limites de taxa. A proposta de joelklabo inclui correlação de execução via ID de prompt, gerenciamento de sessão, reconciliação de stream com ordenação por sequência e orientações do [NIP-59](/pt/topics/nip-59/) para privacidade de metadados.

[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220) de pablof7z adota uma abordagem diferente, definindo kinds para instanciação de agentes: definições e lições. Esses são os tipos de evento que pablof7z usa no [TENEX](https://github.com/tenex-chat/tenex), o sistema de aprendizado autônomo construído sobre Nostr. Uma proposta complementar, [NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221), também de pablof7z, define eventos para anunciar servidores do [Model Context Protocol](https://modelcontextprotocol.io/) e habilidades no Nostr. Comentários [NIP-22](/pt/topics/nip-22/) são suportados, de modo que a comunidade pode discutir e avaliar servidores MCP diretamente no Nostr.

NIP-XX cobre a comunicação completa entre agentes, enquanto NIP-AE e NIP-AD endereçam identidade e descoberta de ferramentas. Essas propostas podem convergir em um padrão unificado ou coexistir como camadas complementares.

## Lançamentos

### HAVEN v1.2.0-rc3

[HAVEN](https://github.com/bitvora/haven), o relay pessoal tudo-em-um que reúne quatro funções de relay com um servidor de mídia [Blossom](/pt/topics/blossom/), alcançou [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3). Este release candidate adiciona suporte a múltiplos npubs, permitindo que uma única instância do HAVEN sirva várias identidades Nostr. RCs anteriores adicionaram as flags `--from-cloud` e `--to-cloud` para backup em nuvem (RC2) e corrigiram um bug de dupla contagem no Web of Trust (RC1).

### Mostro Mobile v1.2.0: Carteira Lightning Embutida

[Mostro Mobile](https://github.com/MostroP2P/mobile), o cliente mobile para a exchange P2P de Bitcoin [Mostro](https://github.com/MostroP2P/mostro) ([v1.1.0 coberta na semana passada](/pt/newsletters/2026-02-11-newsletter/#mostro-lança-primeiro-beta-público)), lançou [v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) com uma carteira Lightning embutida por meio de integração completa com [NWC (NIP-47)](/pt/topics/nip-47/). Compradores e vendedores não precisam mais alternar entre apps para gerenciar invoices. O app detecta hold invoices para vendedores e as paga automaticamente pela carteira conectada, enquanto compradores recebem geração automática de invoice. O lançamento segue o [v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1) do início da semana, que adicionou suporte a múltiplos nós Mostro com um registro curado de instâncias confiáveis, busca de metadados kind 0 para exibição de nós, gerenciamento de nós personalizados por pubkey e fallback automático quando o nó selecionado fica offline.

No lado servidor, o [Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2) chegou com correções para pagamentos duplicados de taxa de desenvolvimento, limitação de taxa no endpoint RPC de validação de senha e limpeza adequada de disputas em cancelamento cooperativo.

Um novo projeto complementar, [mostro-skill](https://github.com/MostroP2P/mostro-skill), permite que agentes negociem no Mostro via Nostr.

### Aerith v0.2

[Aerith](https://github.com/hardran3/Aerith), o gerenciador de imagens [Blossom](/pt/topics/blossom/), lançou [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) com rótulos de imagem para organizar mídia, operações em massa de espelhamento/marcação/exclusão entre servidores, filtragem por rótulo e tipo de arquivo, além de suporte inicial a cache local. Veja a [seção de Notícias](#camada-de-cache-local-do-blossom-emerge) para contexto sobre a tendência mais ampla de cache local.

### Mapnolia: Tiles de Mapa Descentralizados via Nostr

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia) é um novo servidor de dados geoespaciais que divide arquivos de mapa [PMTiles](https://github.com/protomaps/PMTiles) em regiões geográficas e as anuncia via Nostr para descoberta descentralizada. Ele publica eventos substituíveis parametrizados kind 34444 em relays Nostr contendo um índice completo de fragmentos de tiles de mapa com metadados de camadas, regiões de geohash, referências de arquivos e detalhes de servidor [Blossom](/pt/topics/blossom/).

Clientes descobrem e recuperam dados de mapa pela rede Nostr em vez de servidores centralizados de tiles, com eventos de anúncio carregando metadados suficientes para solicitar apenas as regiões geográficas necessárias dos servidores Blossom listados. Mapnolia é o primeiro projeto a trazer distribuição de dados geoespaciais para o Nostr, abrindo possibilidades para aplicações de mapeamento com suporte offline.

### Pika: Mensagens Criptografadas Baseadas em Marmot

[Pika](https://github.com/sledtools/pika) é um novo app de mensagens criptografadas ponta a ponta para iOS e Android usando o protocolo [Marmot](/pt/topics/marmot/), que camada o [Messaging Layer Security (MLS)](/pt/topics/mls/) sobre relays Nostr. A arquitetura separa as responsabilidades em um núcleo Rust (`pika_core`) que gerencia o estado MLS e a criptografia/descriptografia de mensagens sobre relays Nostr, com camadas nativas finas de UI em SwiftUI (iOS) e Kotlin (Android). O estado flui unidirecionalmente: a UI despacha ações para o ator Rust, que muta o estado e emite snapshots com números de revisão de volta para a UI via bindings UniFFI e JNI.

Pika se junta a um campo crescente de mensageiros MLS-sobre-Nostr ao lado de [White Noise](https://github.com/marmot-protocol/whitenoise), [Vector](https://github.com/VectorPrivacy) e [0xchat](https://0xchat.com). Todos usam relays Nostr como camada de transporte para texto cifrado criptografado por MLS, mantendo os operadores de relay incapazes de ler o conteúdo das mensagens. Pika usa o Marmot Development Kit (MDK) para sua implementação MLS e nostr-sdk para conectividade com relays.

### Keep: Assinatura de Limiar [FROST](/pt/topics/frost/) para Android

[Keep](https://github.com/privkeyio/keep-android) é um novo aplicativo Android para assinatura de limiar [FROST](/pt/topics/frost/) onde nenhum dispositivo único detém a chave privada completa. Ele implementa [NIP-55](/pt/topics/nip-55/) (Android Signer) e [NIP-46](/pt/topics/nip-46/) (assinatura remota), de modo que clientes Nostr compatíveis podem solicitar assinaturas enquanto o material de chave permanece distribuído entre dispositivos. As configurações padrão são 2-de-3 e 3-de-5, embora qualquer limiar t-de-n seja suportado.

A cerimônia de geração distribuída de chaves (DKG) do Keep é executada sobre relays Nostr usando kinds de evento personalizados: kind 21101 para anúncios de grupo, kind 21102 para polinômios de comprometimento da rodada 1 (difundidos publicamente) e kind 21103 para compartilhamentos secretos da rodada 2 (criptografados ponto a ponto com [NIP-44](/pt/topics/nip-44/) entre participantes). O escalar da chave privada do grupo nunca é calculado ou montado em nenhum lugar durante o DKG. Cada dispositivo mantém apenas sua avaliação de polinômio, e quaisquer t compartilhamentos podem produzir uma assinatura Schnorr válida por meio de um protocolo de comprometer-depois-assinar em duas rodadas. A assinatura resultante de 64 bytes é indistinguível de uma assinatura Schnorr de signatário único. Por baixo, Keep usa o crate `frost-secp256k1-tr` da Zcash Foundation com ajuste Taproot, de modo que a chave pública do grupo funciona diretamente como um npub Nostr.

Keep se junta à família [Frostr](https://frostr.org) de projetos ao lado de [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), [Igloo para Android](https://github.com/FROSTR-ORG/igloo-android), [Frost2x](https://github.com/FROSTR-ORG/frost2x) e [Igloo para iOS](https://github.com/FROSTR-ORG/igloo-ios), expandindo as opções de gerenciamento de chaves por limiar no Nostr.

### Prism: Compartilhe Qualquer Coisa no Nostr a Partir do Android

[Prism](https://github.com/hardran3/Prism) é um novo app Android (Kotlin/Jetpack Compose, API 26+) que se registra como destino de compartilhamento do sistema, permitindo que usuários publiquem textos, URLs, imagens e vídeos no Nostr a partir de qualquer app do celular. URLs compartilhadas passam por um removedor de parâmetros de rastreamento antes de serem compostas em notas. Prism busca metadados OpenGraph para gerar pré-visualizações ricas de links e renderiza referências Nostr nativas (`note1`, `nevent1`) inline.

O mecanismo de agendamento usa uma abordagem híbrida `AlarmManager`/`WorkManager` para contornar as otimizações de bateria do Android: AlarmManager gerencia o tempo preciso de wake-up enquanto tarefas expedidas do WorkManager garantem a entrega, com retry exponencial para cenários offline. Uploads de mídia passam por servidores [Blossom](/pt/topics/blossom/) configuráveis com geração de miniaturas para imagens e frames de vídeo. Toda assinatura de eventos é delegada a assinadores externos [NIP-55](/pt/topics/nip-55/) como o [Amber](https://github.com/greenart7c3/amber), com suporte a múltiplas contas para alternar entre identidades. Prism também suporta posts de [NIP-84 (Highlights)](/pt/topics/nip-84/). Do mesmo desenvolvedor do [Aerith](#aerith-v02).

### Hashtree: Armazenamento Endereçado por Conteúdo com Integração Nostr

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) é um sistema de armazenamento de blobs endereçado por conteúdo baseado em sistema de arquivos que publica raízes Merkle no Nostr para criar endereços mutáveis npub/caminho. O sistema usa "armazenamento burro" que funciona com qualquer store chave-valor, dividindo o conteúdo em blocos de 2MB otimizados para uploads [Blossom](/pt/topics/blossom/). Ao contrário do BitTorrent, não é necessário computação ativa de prova Merkle - basta armazenar e recuperar blobs por hash.

A integração Nostr possibilita URLs remotas git como `htree://npub.../nome-do-repo` para clonar repositórios, com comandos como `htree publish mydata <hash>` para publicar hashes de conteúdo em endereços `npub.../mydata`. A CLI abrangente suporta modos de armazenamento criptografado (padrão) e público, fixação de conteúdo, envio a servidores Blossom e gerenciamento de identidades Nostr. Cada item armazenado é ou bytes brutos ou um nó de árvore, fornecendo uma base para distribuição descentralizada de conteúdo pela rede de relays do Nostr.

### Espy: Captura de Paleta de Cores no Shakespeare

[Espy](https://espy.you), construído na plataforma [Shakespeare](https://soapbox.pub/tools/shakespeare/), permite que usuários capturem paletas de cores de fotos e as compartilhem como eventos Nostr. Shakespeare é um construtor de apps com IA que autentica usuários via extensões de navegador NIP-07 e fornece conectividade integrada com relays Nostr, de modo que desenvolvedores publicam apps sem implementar seu próprio gerenciamento de chaves ou pool de relays. Espy extrai cores dominantes da câmera em cartões de paleta compartilháveis descobríveis por feeds Nostr padrão.

### Flotilla 1.6.4

[Flotilla](https://gitea.coracle.social/coracle/flotilla), o cliente Nostr semelhante ao Discord de hodlbod que organiza relays como grupos, lançou [1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4). A família de projetos Coracle migrou do GitHub para uma [instância Gitea auto-hospedada](https://gitea.coracle.social/coracle). Este lançamento adiciona notificações push via NIP-9a e um fluxo de recebimento de carteira, além de listagens classificadas e suporte a URL de espaço. Melhorias de interface incluem modais e tratamento de notificações simplificados. Silenciamento de salas e insets de área segura em mobile complementam as mudanças, junto com correções para uploads de imagem no Safari e detalhes de eventos de calendário.

### Shosho v0.12.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), o app mobile de transmissão ao vivo com integração Nostr, lançou [v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0). Este lançamento adiciona Clips de vídeo com respostas dentro do player e integração de emoji personalizado. A proteção de thread bloqueia spam de menções indiretas, e um novo recurso de compartilhamento por QR permite que usuários troquem perfis offline. Um novo modo de reprodução horizontal oferece uma experiência de visualização estilo Twitch, e a tela de navegação agora apresenta clips de criadores ao lado de transmissões ao vivo.

### Granary v10.0

[Granary](https://github.com/snarfed/granary), uma biblioteca de tradução de redes sociais que converte dados entre Nostr, Bluesky, ActivityPub e outras plataformas em um formato comum, lançou [v10.0](https://github.com/snarfed/granary/releases/tag/v10.0) com mudanças que quebram compatibilidade. O lançamento muda os IDs ActivityStreams 1 padrão do Nostr de bech32 para hex e adiciona suporte expandido ao Nostr, incluindo parsing de menções [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) e tags de artigo. Uma nova opção de saída múltipla nos conversores permite que desenvolvedores traduzam entre protocolos em lote.

### Nostr MCP Server v3.0.0

[Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server), um servidor de [Model Context Protocol](https://modelcontextprotocol.io/) que permite a agentes de IA interagirem com a rede Nostr, lançou [v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0). Este lançamento principal adiciona ações sociais (follows, reações, reposts, respostas) e gerenciamento de lista de relays com suporte a [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) mais autenticação opcional [NIP-42](/pt/topics/nip-42/). Mensagens diretas via [NIP-17](/pt/topics/nip-17/) e [NIP-44](/pt/topics/nip-44/) também são novidades. O lançamento se complementa com as [propostas de NIP para agentes de IA](#nips-de-agentes-de-ia-chegam) desta semana como ferramental prático para agentes que operam no Nostr.

### Aegis v0.3.8

[Aegis](https://github.com/ZharlieW/Aegis), o assinador Nostr multiplataforma, lançou [v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8) com suporte a UI multilíngue e um gerenciador de atualização incremental para seu navegador de apps Nostr embutido. O novo mecanismo de atualização faz diff incremental contra o estado local, mantendo o diretório interno de apps web Nostr atualizado com menor uso de largura de banda. O lançamento também introduz cache de 5 minutos para material de chave, reduzindo as idas ao banco de dados ao assinar múltiplos eventos em sequência.

### SNSTR v0.3.1

[SNSTR](https://github.com/AustinKelsay/snstr) (Secure Nostr Software Toolkit for Renegades), uma biblioteca TypeScript para o protocolo Nostr, lançou [v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1). O lançamento adiciona verificações de pacote garantindo que todos os pontos de entrada estejam incluídos nos tarballs npm, com aplicação por CI no Node e Bun. O [v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0) foi lançado na mesma semana.

### Citrine v2.0.0-pre1

[Citrine](https://github.com/greenart7c3/Citrine), o relay Nostr Android de greenart7c3, lançou [v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1) com melhorias de desempenho por meio de índices de banco de dados otimizados e melhor tratamento de coroutines Kotlin. O lançamento também aprimora o suporte para hospedagem de web apps, com cada app agora rodando em sua própria porta.

## Atualizações de Projetos

### Primal Android: Expansão da Infraestrutura NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) fez merge de 11 PRs relacionados a NWC esta semana, continuando a construção [iniciada há duas semanas](/pt/newsletters/2026-02-04-newsletter/#primal-android-entrega-criptografia-nwc). Este lote adiciona suporte a NWC para carteira dupla, início/parada automática do serviço vinculada a notificações do backend, roteamento de conexão por tipo de carteira e limpeza adequada de dados ao excluir carteira. O serviço NWC agora gerencia seu próprio ciclo de vida com base no estado de conexão da carteira, reduzindo a intervenção manual do usuário.

### Notedeck: Preparação para Android App Store

[Notedeck](https://github.com/damus-io/notedeck), o cliente Nostr multiplataforma da equipe [Damus](https://github.com/damus-io/damus), fez merge da [preparação para lançamento na Android App Store](https://github.com/damus-io/notedeck/pull/1287) esta semana. O PR adiciona um plano de conformidade UGC (Conteúdo Gerado pelo Usuário) exigido pelo Google Play, incluindo uma tela de aceitação dos Termos de Serviço, bloqueio de usuários via menus de contexto e configurações, funcionalidade [NIP-56 (Reporting)](/pt/topics/nip-56/) que publica eventos de denúncia em relays, e uma seção de configurações de Conteúdo e Segurança. Infraestrutura de build foi adicionada para geração de APKs e AABs (Android App Bundles) de lançamento assinados via novos targets Makefile. Um documento EULA estabelece requisito de idade de 17 anos e isenções de responsabilidade específicas do Nostr sobre conteúdo descentralizado. Os próprios recursos de conformidade serão entregues em PRs subsequentes; este merge estabelece as bases de documentação e assinatura.

No lado iOS do Damus, foi lançada uma correção para uma [regressão de spinner de carregamento infinito](https://github.com/damus-io/damus/pull/3593) onde o spinner persistia indefinidamente após o conteúdo ter sido carregado.

### Nostria: Relays de Descoberta e Correções de DM

[Nostria](https://github.com/nostria-app/nostria), o cliente Nostr multiplataforma focado em escala global, fez merge de 9 PRs esta semana. O mais notável adiciona [inicialização automática de Relays de Descoberta](https://github.com/nostria-app/nostria/pull/460) para busca de perfis, dando a novos usuários conectividade funcional com relays sem configuração manual. Outras correções tratam de [quebra de linha na área de texto de DM](https://github.com/nostria-app/nostria/pull/466), [preenchimento de viewport em vídeo fullscreen](https://github.com/nostria-app/nostria/pull/479), [extração de metadados de artigos em pré-visualizações de repost](https://github.com/nostria-app/nostria/pull/481) e [resolução de URI nostr: em notificações](https://github.com/nostria-app/nostria/pull/458).

### Camelus: Migração para Riverpod v3

[Camelus](https://github.com/camelus-hq/camelus), o cliente Nostr baseado em Flutter, fez merge de 5 PRs esta semana centrados em uma [migração de API para Riverpod v3](https://github.com/camelus-hq/camelus/pull/158) e [refatoração de feed genérico](https://github.com/camelus-hq/camelus/pull/159). Um [cache de notas embutidas](https://github.com/camelus-hq/camelus/pull/161) evita buscas redundantes em relays para notas citadas.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado:**

- **[NIP-85: Descoberta de Provedores de Serviço](https://github.com/nostr-protocol/nips/pull/2223)**: vitorpamplona adicionou orientações sobre descoberta pelo cliente de provedores de serviço de [NIP-85 Trusted Assertions](/pt/topics/nip-85/), incluindo dicas de relay e chaves de serviço específicas por algoritmo. Veja o [deep dive abaixo](#deep-dive-de-nip-nip-85-trusted-assertions) para cobertura completa.

- **[NIP-11: Limpeza de Informações de Relay](https://github.com/nostr-protocol/nips/pull/1946)**: fiatjaf removeu `privacy_policy`, o array `retention`, `relay_countries` e o bloco de preferências de comunidade do [NIP-11](/pt/topics/nip-11/). Operadores de relay raramente populavam esses campos e os clientes não agiam sobre eles.

- **[NIP-52: Tag de Timestamp com Granularidade de Dia](https://github.com/nostr-protocol/nips/pull/1752)**: staab adicionou uma tag `D` obrigatória ao [NIP-52](/pt/topics/nip-52/) para eventos de calendário baseados em tempo (kind 31923) representando o timestamp Unix com granularidade de dia, calculado como `floor(unix_seconds / 86400)`. Múltiplas tags `D` cobrem eventos de vários dias, habilitando indexação temporal eficiente sem precisar analisar timestamps completos.

- **[NIP-47: Simplificação](https://github.com/nostr-protocol/nips/pull/2210)**: O PR de simplificação [discutido no Compass #9](/pt/newsletters/2026-02-11-newsletter/) foi mergeado esta semana, removendo `multi_pay_invoice` e `multi_pay_keysend` do [NIP-47 (Nostr Wallet Connect)](/pt/topics/nip-47/). Veja o [Compass #8](/pt/newsletters/2026-02-04-newsletter/#deep-dive-de-nip-nip-47-nostr-wallet-connect) para o deep dive completo do protocolo NWC.

**PRs Abertos e Discussões:**

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)**: Coberto no [Compass #8](/pt/newsletters/2026-02-04-newsletter/), esta proposta de especificação de podcast gerou discussão acalorada esta semana. staab observou que já existem pelo menos três padrões concorrentes de podcast em uso, e derekross apontou para uma implementação existente de seis meses com apps e podcasts ativos. O caminho a seguir exige convergência entre implementações antes que um número de NIP possa ser atribuído.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)**: joelklabo propõe um protocolo completo de comunicação de agentes de IA com kinds de evento para prompts, respostas, streaming, telemetria de ferramentas, erros e descoberta de capacidades. Veja a [seção de Notícias](#nips-de-agentes-de-ia-chegam) para cobertura de todas as propostas de IA desta semana.

- **[NIP-PNS: Private Note Storage](https://github.com/nostr-protocol/nips/pull/1893)**: O sistema de notas privadas de jb55 define eventos kind 1080 para armazenar notas pessoais criptografadas em relays sem revelar quem as escreveu. O esquema deriva um par de chaves pseudônimo determinístico a partir do nsec do usuário via HKDF: `pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`, depois gera um par de chaves secp256k1 a partir dessa chave derivada. Uma segunda derivação produz uma chave de criptografia simétrica: `pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`. As notas internas são criptografadas com [NIP-44](/pt/topics/nip-44/) v2 usando essa chave e publicadas sob a pubkey pseudônima, de modo que relays veem eventos kind 1080 de uma identidade desvinculada da chave principal do usuário. Ao contrário dos gift wraps do [NIP-59](/pt/topics/nip-59/), o PNS não é passível de spam (a chave pseudônima é determinística, não aleatória) e não carrega metadados públicos (nenhuma tag `p` é necessária, pois não há destinatário). Esta semana, jb55 publicou descobertas da implementação do PNS no backend Rust do Notedeck (módulo `enostr::pns`). Ele identificou que a chamada `hkdf_extract` da especificação é ambígua porque o HKDF RFC 5869 tem duas fases (Extract e Expand) que produzem saída diferente, e a maioria das bibliotecas espera ambas. Ele esclareceu que `pns_nip44_key` contorna o acordo de chaves ECDH normal do NIP-44 e é usada diretamente como a chave de conversa, um detalhe que implementadores precisam saber, pois a maioria das bibliotecas NIP-44 usa ECDH por padrão. Ele também sinalizou uma variável indefinida na implementação de referência TypeScript. O PR, originalmente de abril de 2025, está agora sendo ativamente implementado.

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)**: pablof7z define quatro kinds de evento para identidade de agente no Nostr, extraídos de seu trabalho no [TENEX](https://github.com/tenex-chat/tenex). O template base é kind 4199 (Agent Definition), carregando título, descrição de papel, instruções do sistema, declarações de ferramentas e versão. Modificadores comportamentais ficam no kind 4201 (Agent Nudge), que usa as tags `only-tool`, `allow-tool` e `deny-tool` para controle de capacidades em tempo de execução. Agentes publicam o que aprendem como eventos kind 4129 (Agent Lesson), categorizados e vinculados de volta à definição pai via tags `e`, refinável por meio de threads de comentário [NIP-22](/pt/topics/nip-22/). A verificação de propriedade usa kind 14199, um evento substituível onde operadores humanos listam seus pubkeys de agente, estabelecendo uma cadeia bidirecional quando combinado com a tag `p` do perfil kind 0 do agente.

- **[NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221)**: pablof7z define eventos para anunciar servidores do [Model Context Protocol](https://modelcontextprotocol.io/) e habilidades individuais no Nostr. Anúncios de servidor MCP carregam a URL de endpoint do servidor e a versão de protocolo suportada junto com uma lista de ferramentas disponíveis com seus schemas de entrada. Comentários [NIP-22](/pt/topics/nip-22/) são suportados em anúncios de servidor, de modo que a comunidade pode discutir e avaliar servidores MCP diretamente no Nostr.

- **[NIP-73: Tag de Kind OSM](https://github.com/nostr-protocol/nips/pull/2224)**: DestBro propõe adicionar identificadores OpenStreetMap ao [NIP-73 (External Content IDs)](/pt/topics/nip-73/), que padroniza como eventos Nostr referenciam conteúdo externo como livros (ISBN), filmes (ISAN), feeds de podcast (GUID), geohashes e URLs via tags `i` e `k`. O kind OSM proposto permitiria que eventos referenciem recursos de mapa específicos (edifícios, estradas, parques) por seu ID de nó ou via OpenStreetMap, conectando conteúdo Nostr ao banco de dados geográfico aberto.

- **[NIP-XX: Variantes de Imagem Responsiva](https://github.com/nostr-protocol/nips/pull/2219)**: woikos propõe estender eventos de metadados de arquivo [NIP-94](/pt/topics/nip-94/) com tags para variantes de imagem responsiva em diferentes resoluções. Clientes poderiam selecionar a variante apropriada com base no tamanho da tela e nas condições de rede, reduzindo largura de banda para usuários de dispositivos móveis visualizando imagens de alta resolução hospedadas em servidores [Blossom](/pt/topics/blossom/).

## Deep Dive de NIP: NIP-85 (Trusted Assertions)

O [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) define um sistema para delegar cálculos custosos a provedores de serviço confiáveis que publicam resultados assinados como eventos Nostr. Pontuações de Web of Trust e métricas de engajamento exigem rastrear muitos relays e processar grandes volumes de eventos, trabalho que é impraticável em dispositivos móveis. O [merge](https://github.com/nostr-protocol/nips/pull/2223) desta semana adicionou orientações sobre o processo de descoberta de provedores pelo cliente.

**Delegação:**

Calcular a pontuação de Web of Trust de um usuário exige rastrear grafos de follows com múltiplos saltos em muitos relays, e calcular contagens precisas de seguidores significa desduplicar em toda a rede de relays. Dispositivos móveis e clientes de navegador não conseguem executar essas operações, mas os resultados são essenciais para filtragem de spam e ranqueamento de conteúdo. O NIP-85 preenche essa lacuna permitindo que usuários designem provedores confiáveis para executar os cálculos e publicar resultados como eventos Nostr padrão.

**Design do Protocolo:**

O NIP-85 usa quatro kinds de evento para asserções sobre diferentes tipos de sujeito. Asserções de usuário (kind 30382) carregam contagem de seguidores, contagens de posts/respostas/reações, volumes de zap, rank normalizado (0-100), tópicos comuns e horas ativas:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Asserções de evento (kind 30383) avaliam notas individuais com contagem de comentários, citações, reposts, reações e dados de zap:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Para eventos endereçáveis (artigos de forma longa, páginas wiki), o kind 30384 aplica as mesmas métricas de engajamento em todas as versões coletivamente. O kind 30385 avalia identificadores externos (livros, filmes, sites, locais, hashtags) referenciados via [NIP-73 (External Content IDs)](/pt/topics/nip-73/), que padroniza como eventos Nostr referenciam conteúdo externo via tags `i` e `k`:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Cada asserção é um evento endereçável substituível onde a tag `d` contém o sujeito: um pubkey, ID de evento, endereço de evento ou identificador NIP-73. Provedores de serviço assinam esses eventos com suas próprias chaves, e clientes os avaliam com base nas relações de confiança.

**Descoberta de Provedores:**

Usuários declaram quais provedores de asserção confiam publicando eventos kind 10040. Cada entrada especifica o tipo de asserção com o pubkey do provedor e dica de relay, mais variantes de algoritmo opcionais:

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

Usuários podem criptografar a lista de tags em `.content` usando [NIP-44](/pt/topics/nip-44/) para manter suas preferências de provedor privadas. Clientes constroem uma lista de provedores verificando quais provedores as contas que seguem confiam, criando uma camada de reputação descentralizada para os próprios provedores de asserção.

**Modelo de Segurança:**

Provedores devem usar chaves de serviço diferentes para algoritmos distintos, e uma chave única por usuário quando os algoritmos são personalizados, evitando correlação cruzada de consultas entre usuários. Cada chave de serviço recebe um evento de metadados kind 0 descrevendo o comportamento do algoritmo, dando aos usuários transparência sobre o que estão confiando. Eventos de asserção só devem ser atualizados quando os dados subjacentes realmente mudam, evitando tráfego desnecessário de relay e permitindo que clientes armazenem resultados em cache com segurança.

**Adoção Atual:**

O NIP-85 formaliza um padrão que já estava surgindo de forma informal. O servidor de cache do Primal computa métricas de engajamento e pontuações de Web of Trust. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal), coberto no [Compass #9](/pt/newsletters/2026-02-11-newsletter/#antiprimal-gateway-compatível-com-padrões-ao-cache-do-primal), faz bridge desses cálculos para clientes Nostr padrão usando kinds de evento NIP-85. [Nostr.band](https://nostr.band) opera o relay `wss://nip85.nostr.band` referenciado nos próprios exemplos da spec, servindo eventos de asserção para seus dados de índice de busca. No lado do cliente, [Amethyst](https://github.com/vitorpamplona/amethyst) (de autoria de vitorpamplona, que também escreveu este NIP) tem suporte experimental a Trusted Assertions em sua biblioteca `quartz`, analisando eventos de asserção e declarações de provedores de serviço. [Vertex](https://vertexlab.io) computa métricas similares de Web of Trust, mas [escolheu uma abordagem diferente](https://vertexlab.io/blog/dvms_vs_nip_85/), usando uma API direta em vez de eventos NIP-85, citando o problema de descoberta e o overhead computacional de arquiteturas baseadas em asserção. Com o NIP-85, qualquer cliente pode consumir asserções de qualquer provedor por meio de um formato de evento padrão, e provedores competem em precisão enquanto usuários escolhem em quem confiar.

## Deep Dive de NIP: NIP-52 (Eventos de Calendário)

O [NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md) define eventos de calendário no Nostr, dando aos clientes uma forma padrão de representar e descobrir ocorrências em momentos específicos ou entre momentos. O [merge da tag D](https://github.com/nostr-protocol/nips/pull/1752) desta semana adicionou indexação com granularidade de dia, completando uma peça ausente na infraestrutura de consulta da spec.

**Dois Tipos de Evento:**

O NIP-52 separa eventos de calendário em dois kinds com base na precisão temporal. Eventos baseados em data (kind 31922) representam ocorrências de dia inteiro como feriados ou festivais de vários dias. Eles usam strings de data ISO 8601 em suas tags `start` e `end` opcionais, sem consideração de fuso horário:

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

Eventos baseados em tempo (kind 31923) representam momentos específicos com timestamps Unix em suas tags `start` e `end` opcionais, mais identificadores de fuso horário IANA (`start_tzid`, `end_tzid`) para exibição. Ambos os kinds são eventos substituíveis parametrizados, de modo que organizadores atualizam detalhes publicando um novo evento com a mesma tag `d`.

**Calendários e RSVPs:**

Eventos kind 31924 definem calendários como coleções, referenciando eventos via tags `a` que apontam para eventos kind 31922 ou 31923 por suas coordenadas de endereço:

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

Usuários podem manter múltiplos calendários (pessoal, trabalho, comunidade) e clientes podem assinar calendários de pubkeys específicos. Eventos de calendário podem incluir uma tag `a` referenciando um calendário para solicitar inclusão, habilitando gerenciamento colaborativo onde múltiplos usuários contribuem com eventos para calendários que não possuem.

RSVPs usam kind 31925, onde usuários publicam seu status de presença junto com um indicador opcional de livre/ocupado:

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

Os valores válidos de `status` são "accepted", "declined", "tentative", e a tag opcional `fb` marca o usuário como livre ou ocupado naquele período. Eventos de RSVP referenciam a tag `a` do evento de calendário e carregam a tag `p` do organizador, de modo que o cliente do organizador pode agregar respostas entre relays.

**A Adição da Tag D:**

Antes do merge desta semana, clientes que consultavam eventos em um intervalo de datas precisavam buscar todos os eventos de um pubkey ou calendário e filtrar no lado do cliente. A nova tag `D` obrigatória em eventos baseados em tempo (kind 31923) contém um timestamp Unix com granularidade de dia calculado como `floor(unix_seconds / 86400)`. Eventos de vários dias carregam múltiplas tags `D`, uma por dia. Relays agora podem indexar eventos por dia e responder a consultas filtradas de forma eficiente, transformando o que era um problema de filtragem no lado do cliente em uma busca por índice no lado do relay.

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

O valor `D` de `20139` é igual a `floor(1740067200 / 86400)`, posicionando este evento em 20 de fevereiro de 2025. Clientes que consultam "todos os eventos desta semana" enviam um filtro com o intervalo `D` correspondente, e os relays retornam apenas os eventos correspondentes.

**Decisões de Design:**

O NIP-52 omite intencionalmente eventos recorrentes. A spec deixa de fora as regras de recorrência (RRULE do iCalendar) completamente, delegando essa complexidade aos clientes. Um organizador publica eventos individuais para cada ocorrência, mantendo o modelo de dados no lado do relay simples. Tags de participante carregam papéis opcionais ("host", "speaker", "attendee"), e tags de localização podem incluir tags de geohash `g` para consultas espaciais junto com endereços legíveis por humanos.

**Implementações:**

[Flockstr](https://github.com/zmeyer44/flockstr) é o principal cliente de calendário construído sobre NIP-52. [Coracle](https://gitea.coracle.social/coracle/coracle) exibe eventos de calendário em seu feed social. A adição da tag `D` esta semana habilita indexação temporal no lado do relay que ambos os clientes podem usar para reduzir largura de banda ao consultar eventos em um intervalo de datas específico.

---

É isso por esta semana. Construindo algo ou tem novidades para compartilhar? Quer que cobramos seu projeto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via [NIP-17](/pt/topics/nip-17/) DM</a> ou nos encontre no Nostr.
