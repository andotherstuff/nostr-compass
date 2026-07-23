---
title: 'Nostr Compass #32'
date: 2026-07-22
translationOf: /en/newsletters/2026-07-22-newsletter.md
translationDate: 2026-07-22
draft: false
type: newsletters
---

Bem-vindos de volta ao Nostr Compass, seu guia semanal sobre Nostr.

**Esta semana:** o [IndieSats](#indiesats-drops-its-publisher-role-and-relaunches-as-open-nostr-music-infrastructure) aposenta a custódia de chaves, sua lista branca e sua taxa obrigatória sobre receita, relançando-se como um relay aberto, um player e uma camada de descoberta onde artistas publicam sob suas próprias chaves. O [Nostrord v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) traz moderação de grupos, listas de mudo e relays onion na mesma semana em que cinco [PRs da especificação NIP-29 são mergeados](#protocol-work-and-nip-updates). O [Zapstore 1.1.0](#zapstore-110-makes-the-device-key-portable-and-adds-background-auto-updates) introduz uma chave de dispositivo portátil criptografada com backup via Amber e atualizações automáticas em segundo plano opcionais. O [kind de lista de conjuntos de seguimento favoritos](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house) é mergeado e abre um PR de renumeração em poucos dias. E o [ecossistema Iris](#the-iris-ecosystem-ships-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week) lança nostr-pubsub, o runtime de navegador fips-ts e nostr-social-graph 2.0.0 em uma única semana.

Os lançamentos etiquetados trazem [Amber v6.3.0](#amber-v630-groups-bunker-signing-approvals-and-adds-expert-list-support) com aprovações agrupadas de assinatura bunker, [Wisp v1.2.0](#wisp-v120-adds-a-multi-account-switcher-and-collapsible-reply-threads) com um alternador de múltiplas contas, [Sonar v0.1-alpha.11](#sonar-v01-alpha11-continues-the-alpha-line) continuando a linha alpha, e o novo projeto [ClipRelay v0.1.2](#cliprelay-v012-new-project-syncs-clipboards-across-devices-over-nostr-relays) sincronizando áreas de transferência através de relays Nostr.

No lado não publicado, o [nostream](#nostream-merges-seven-prs-without-cutting-a-release) faz merge da pilha de controle de acesso que o Deep Dive desta semana cobre, e o [Amethyst](#amethyst-lands-v1130-pre-release-qa-on-napplet-isolation-and-concord-authority) entrega o QA pré-lançamento da v1.13.0 em 81 PRs mergeados.

O repositório de NIPs faz merge de cinco PRs esta semana, incluindo o [bloco NIP-29](#protocol-work-and-nip-updates) e os [conjuntos de seguimento favoritos kind:10011](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house), e abre debates sobre a [simplificação do NIP-47](#protocol-work-and-nip-updates) e [asserções de confiança de relays](#protocol-work-and-nip-updates). O Deep Dive cobre [NIP-42 e NIP-43, o par de controle de acesso de relays](#nip-deep-dive-nip-42-and-nip-43).

---

## Matérias principais

### IndieSats abandona seu papel de editora e se relança como infraestrutura musical Nostr aberta

O [IndieSats](https://zapstore.dev) é uma plataforma de música baseada em Nostr que até esta semana atuava como editora: detinha chaves dos artistas, mantinha uma lista branca e cobrava uma taxa obrigatória de 2% sobre a receita. Em um [anúncio de pivô publicado em 20 de julho](https://njump.me/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u), o projeto aposentou esses três papéis de uma vez. A plataforma relançada é, em vez disso, três peças de infraestrutura aberta: um relay aberto, um player e uma camada de descoberta, com artistas publicando música sob seus próprios perfis Nostr em vez de uma identidade custodiada pela plataforma. As divisões de receita passam a ser opcionais, não mais obrigatórias, e a plataforma agora honra pedidos de exclusão kind:5 do [NIP-09](/pt/topics/nip-09/) para que artistas possam remover seu trabalho. Para um espaço que costuma falar de protocolos substituindo plataformas, este é um caso real de uma plataforma se desmontando voluntariamente em peças de protocolo.

### Nostrord v2.3.0 traz moderação de grupos, listas de mudo e relays onion

O [Nostrord](https://github.com/nostrord/nostrord), o cliente de chat em grupo para Android, iOS, web e desktop, lançou [v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) com ações de moderação de grupo conectadas em todas as interfaces ([PR #192](https://github.com/nostrord/nostrord/pull/192)), convites de grupo com consentimento e detecção entre relays ([PR #195](https://github.com/nostrord/nostrord/pull/195)), listas de mudo [NIP-51](/pt/topics/nip-51/) multiplataforma ([PR #188](https://github.com/nostrord/nostrord/pull/188)) e suporte a relays .onion via Tor. O lançamento chega na mesma semana em que a especificação [NIP-29](/pt/topics/nip-29/) subjacente mergeou cinco PRs cobrindo subgrupos, fixação de mensagens, banners e códigos de convite (detalhes na [seção de protocolo](#protocol-work-and-nip-updates) desta semana), de modo que o chat em grupo no Nostr agora tem tanto uma especificação mais profunda quanto um cliente exercitando a maior parte dela, o que encurta o ciclo de feedback para todos os outros que constroem sobre grupos de relays.

### Zapstore 1.1.0 torna a chave de dispositivo portátil e adiciona atualizações automáticas em segundo plano

O [Zapstore](https://github.com/zapstore/zapstore) é uma loja de aplicativos nativa do Nostr onde os lançamentos são assinados pelas chaves dos desenvolvedores e nenhum operador central os endossa. A [versão 1.1.0](https://github.com/zapstore/zapstore/releases/tag/1.1.0), o primeiro lançamento coberto aqui desde o início de março, fecha as duas maiores lacunas em relação às lojas de aplicativos convencionais. A primeira é atualizações: atualizações automáticas opcionais em segundo plano agora baixam via Wi-Fi e instalam silenciosamente ou de forma agendada, mantendo os aplicativos atualizados sem viagens manuais pela loja. A segunda é continuidade de identidade: a chave de dispositivo torna-se portátil, criptografada e com backup possível pelo [Amber](https://github.com/greenart7c3/Amber) via [NIP-55](/pt/topics/nip-55/), a interface de assinante do Android, de modo que um usuário trocando de telefone não recomeça mais como um dispositivo desconhecido. O lançamento também move o catálogo de aplicativos para os relays como eventos kind:10067 assinados pelo dispositivo, adiciona denúncias verificadas [NIP-56](/pt/topics/nip-56/) a partir do menu de opções para que usuários possam sinalizar aplicativos problemáticos de forma que outros clientes possam consumir, e verifica a prova C1 anexada a um lançamento antes de qualquer instalação prosseguir, reforçando o vínculo entre o que um desenvolvedor assinou e o que um dispositivo executa.

### O kind de lista de conjuntos de seguimento favoritos é mergeado e imediatamente muda de casa

Uma história de coordenação de especificação aconteceu em uma única semana. O [PR #2413](https://github.com/nostr-protocol/nips/pull/2413) foi mergeado em 15 de julho, padronizando um kind de lista substituível para conjuntos de seguimento favoritos sob o [NIP-51](/pt/topics/nip-51/) (listas): um kind dedicado onde clientes podem publicar os conjuntos curados de contas seguidas de um usuário em vez de sobrecarregar kinds de lista genéricos. Em poucos dias, descobriu-se que o kind:10011 atribuído já estava em uso em outro lugar, então um PR de acompanhamento [PR #2417](https://github.com/nostr-protocol/nips/pull/2417) está agora aberto para renumerar a lista para kind:10021. Nada foi lançado contra o kind mergeado ainda, o que faz deste o momento barato para renumerar; uma vez que clientes comecem a publicar eventos kind:10011, a colisão ficará cara de desfazer. Desenvolvedores construindo recursos que consomem listas devem acompanhar o PR de renumeração, não o texto mergeado, até que se resolva.

### O ecossistema Iris lança uma biblioteca pubsub, um runtime FIPS para navegador e um grafo social 2.0 em uma semana

Três lançamentos da órbita Iris chegaram juntos, e eles se encaixam. O [nostr-pubsub](https://github.com/mmalmi/nostr-pubsub) é uma biblioteca de publicação/assinatura neutra em transporte para eventos Nostr; seus [primeiros lançamentos rastreados, v0.1.3 a v0.5.2](https://github.com/mmalmi/nostr-pubsub/releases), entregam um transportador de relay para navegador construído sobre o SimplePool do nostr-tools, verificação de eventos na fronteira do transporte para que assinaturas inválidas nunca cheguem aos assinantes, e consultas históricas limitadas. O [fips-ts](https://github.com/mmalmi/fips-ts) traz o [FIPS](/pt/topics/fips/), o transporte ponto a ponto Noise-sobre-secp256k1 antes disponível como pilha Rust, para o navegador como um runtime TypeScript: os lançamentos [0.0.24 a 0.0.30](https://github.com/mmalmi/fips-ts/releases) adicionaram um transportador por canal de dados WebRTC, sinalização baseada em Nostr para descoberta de pares, um cache de pares recentes e um adaptador IndexedDB para armazenamento no navegador, e o runtime é compatível a nível de fio com a implementação Rust de referência. A terceira peça, [nostr-social-graph v2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0), é uma versão maior da biblioteca de grafo social: operações de roster assinadas para grafos de identidade Nostr, fluxos de aprovação de dispositivos iniciados a partir de um URI canônico de três campos, e facetas de identidade de transporte FIPS com vetores de teste Rust e TypeScript compartilhados. O enquadramento conectivo é a [Iris Stack](https://stack.iris.to/), o laboratório de integração do projeto que une essas bibliotecas com Blossom, Hashtree e mensagens criptografadas. Juntas, uma aplicação web agora pode descobrir pares via Nostr, abrir um canal FIPS criptografado até eles e manter um grafo social assinado, tudo em TypeScript.

---

## Lançamentos etiquetados

### Amber v6.3.0 agrupa aprovações de assinatura bunker e adiciona suporte a Expert List

O [Amber](https://github.com/greenart7c3/Amber) é um assinante remoto [NIP-46](/pt/topics/nip-46/) para Android. A [v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) adiciona aprovação agrupada de múltiplas requisições para assinatura bunker, de modo que um lote de pedidos de assinatura pendentes pode ser revisado e aprovado junto em vez de um prompt por vez. O lançamento também adiciona suporte aos eventos Expert List (kind 12022) e Expert Pack (kind 32022), um modo de privacidade que oculta conteúdo sensível na tela, e uma mudança para buscar a lista de relays [NIP-65](/pt/topics/nip-65/) de uma conta antes dos metadados do perfil, para que os fluxos de assinatura partam do conjunto real de relays do usuário. Isso segue a linha v6.2.x coberta na edição de 2026-07-08.

### Acompanhamento do Nostrord v2.2.0

Com a [v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) liderando a seção de Notícias desta semana, o espaço de lançamentos etiquetados anota apenas o que a matéria principal não cobre: a v2.3.0 segue os controles de DM da v2.2.0 cobertos no #31, tornando este o segundo lançamento semanal consecutivo do cliente.

### Wisp v1.2.0 adiciona alternador de múltiplas contas e threads de resposta recolhíveis

O [Wisp](https://github.com/barrydeen/wisp) é um cliente Nostr orientado à privacidade com suporte a carteira integrado. A [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) adiciona um alternador de múltiplas contas para mudar entre perfis sem novo login, threads de resposta recolhíveis para conversas longas, remoção de parâmetros de rastreamento dos links de notas antes de abri-los, e uma visualização do histórico de transações da carteira. O lançamento segue a atualização do Wisp coberta na edição de 2026-07-08.

### ClipRelay v0.1.2 (novo projeto) sincroniza áreas de transferência entre dispositivos via relays Nostr

O [ClipRelay](https://github.com/tajava2006/cliprelay) é um aplicativo multiplataforma recém-lançado (Android, macOS, Windows, Linux) que sincroniza sua área de transferência entre seus próprios dispositivos: copie em uma máquina, cole em outra. Todo o tráfego passa por relays Nostr como eventos criptografados [NIP-44](/pt/topics/nip-44/) endereçados a você mesmo, então não há servidor para rodar nem conta para criar; a chave privada fica fora do aplicativo. A [v0.1.2](https://github.com/tajava2006/cliprelay/releases) corrige uma falha sutil de sincronização em que uma máquina acordando do sono continuava publicando, mas parava silenciosamente de receber, e reforça os indicadores de status de relay que antes reportavam assinaturas mortas como saudáveis. Esta é a primeira aparição do ClipRelay na newsletter.

### Sonar v0.1-alpha.11 continua a linha alpha

O [Sonar](https://github.com/hedwig-corp/bitchat-to-sonar), matéria principal da semana passada, lançou [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11) com trabalho no motor de enlace mesh em Rust, correções de BLE e mesh, e diagnósticos de relay; um acompanhamento incremental da linha alpha coberta no #31.

### Os lançamentos menores da semana

Três lançamentos menores merecem uma linha cada: o [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release), o aplicativo de chamadas Nostr, migrou suas notificações push para UnifiedPush, mantendo a sinalização de chamadas fora da infraestrutura de push do Google; o [nostr-vpn v4.1.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.1), uma VPN mesh que usa Nostr para sinalização, lançou uma atualização no Zapstore; e dois novos aplicativos estrearam lá também: StableKraft, um agregador de música e podcasts Nostr-mais-Lightning, e Hakari, um backup Nostr criptografado para um registrador de peso.

### Amethyst entrega QA pré-lançamento v1.13.0 sobre isolamento de napplets e autoridade Concord

O [Amethyst](https://github.com/vitorpamplona/amethyst) mergeou 81 PRs esta semana antes do lançamento da v1.13.0. O [PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) é uma passada de QA pré-lançamento cobrindo isolamento de contas de napplets, correções de autoridade Concord e cerca de 30 outras correções, com mais PRs de preparação da v1.13.0 chegando até 21-07. Isso continua a cobertura do #31 sobre a implementação limpa do cliente Concord do Amethyst, reforçando o comportamento de autoridade e isolamento desse trabalho antes de seu lançamento etiquetado.

---

## Mudanças não publicadas

### nostream mergeia sete PRs sem cortar um lançamento

O [nostream](https://github.com/Cameri/nostream), a implementação de relay em TypeScript, mergeou sete PRs esta semana sem cortar um lançamento. O par principal é [PR #702](https://github.com/Cameri/nostream/pull/702) e [PR #676](https://github.com/Cameri/nostream/pull/676), que juntos dão aos operadores de relay uma pilha funcional de controle de acesso de autenticação-mais-associação; o Deep Dive de NIP desta semana percorre exatamente esse handshake.

### FIPS v0.4.1 reforça o transporte sobre o qual o ecossistema Iris constrói

O [jmcorgan/fips](https://github.com/jmcorgan/fips) lançou [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1), um lançamento de manutenção que limita o estado antipoison, corrige convergência e tratamento de MTU, e reduz o uso de CPU. Por si só isso é encanamento, mas esta semana é tecido conectivo: o runtime TypeScript para navegador [fips-ts](https://github.com/mmalmi/fips-ts) do bloco do ecossistema Iris na seção de Notícias desta edição é compatível a nível de fio com este transporte Rust, então correções aqui se propagam diretamente para aquilo com que o runtime de navegador interopera.

---

## Trabalho de protocolo e atualizações de NIP

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeados:**

- **[NIP-29](/pt/topics/nip-29/) (Grupos baseados em relay): Subgrupos** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319), mergeado em 2026-07-16): NIP-29 define grupos hospedados em relay onde associação, papéis e histórico de chat vivem em um único relay como eventos endereçáveis da série `kind:39000`, com ações de moderação carregadas por eventos de administração da série `kind:9000`. Este PR permite que um grupo se declare um subgrupo adicionando uma tag `parent` aos seus metadados, apontando para o identificador `d` de outro grupo no mesmo relay. Subgrupos são grupos comuns em todos os outros aspectos: a associação não cascateia (entrar em um pai não concede associação em nenhum filho), papéis de administrador não são herdados (a lista de administradores `kind:39001` de cada subgrupo é autoritativa para seu próprio escopo), e cada subgrupo mantém seus próprios eventos de membros `kind:9000`/`kind:9001` independentes. Relays que suportam a hierarquia a anunciam em seu documento de informações de relay NIP-11 sob um objeto `nip29` com `"subgroups": true`, para que clientes possam descobrir a capacidade antes de tentar criar comunidades aninhadas.

- **[NIP-29](/pt/topics/nip-29/): Fixação de mensagens** ([PR #2379](https://github.com/nostr-protocol/nips/pull/2379), mergeado em 2026-07-15; [PR #2416](https://github.com/nostr-protocol/nips/pull/2416), mergeado em 2026-07-17): administradores de grupo agora podem fixar mensagens dentro de um grupo baseado em relay. O mecanismo adiciona um novo evento de moderação, `kind:9010` `update-pin-list`, que carrega a lista ordenada completa de fixados como tags `e` referenciando ids de eventos comuns, e um novo evento opcional no nível do grupo, `kind:39005` *group pinned events*, que o relay regenera para espelhar a lista de fixados aceita mais recente. Como cada `kind:9010` substitui a lista inteira em vez de alternar entradas individuais, fixar, desafixar, reordenar e limpar fixados são todos expressos submetendo uma nova lista. O PR de acompanhamento #2416 estende o formato para que tags `a` também sejam aceitas na lista de fixados, permitindo que administradores fixem eventos endereçáveis (posts longos, páginas de wiki e outros conteúdos substituíveis parametrizados) junto com mensagens de chat comuns. Relays podem limitar o número de fixados, e o texto da especificação mergeado recomenda exibir os fixados na ordem em que as tags aparecem.

- **[NIP-29](/pt/topics/nip-29/): Tag banner e sufixo de código de convite** ([PR #2383](https://github.com/nostr-protocol/nips/pull/2383), mergeado em 2026-07-16; [PR #2380](https://github.com/nostr-protocol/nips/pull/2380), mergeado em 2026-07-16): duas adições de exibição e onboarding aos metadados de grupo. O PR #2383 adiciona uma tag `banner` opcional ao evento de metadados de grupo `kind:39000`, juntando-se aos campos existentes `name`, `picture` e `about` para que clientes possam renderizar uma imagem de cabeçalho para a página de um grupo. O PR #2380 define um sufixo de código de convite para links de compartilhamento de grupo: um código de convite pode ser anexado ao identificador `naddr` do grupo como `naddr1...?invite=<code>`. Como o conjunto de caracteres bech32 não inclui `?`, a porção antes do sufixo permanece um naddr válido por si só, então clientes que não entendem a extensão ainda podem resolver o grupo. Clientes que a entendem pré-preenchem a tag `code` na requisição de entrada `kind:9021`, que se combina com o evento de moderação existente `kind:9009` `create-invite` para simplificar a admissão em grupos fechados.

- **[NIP-51](/pt/topics/nip-51/) (Listas): Conjuntos de seguimento favoritos, kind:10011** ([PR #2413](https://github.com/nostr-protocol/nips/pull/2413), mergeado em 2026-07-15): NIP-51 define os kinds de lista padrão, divididos entre listas substituíveis da série `kind:10000` (uma por usuário) e conjuntos endereçáveis da série `kind:30000` (muitos por usuário, indexados pela tag `d`). Este PR adiciona `kind:10011`, *conjuntos de seguimento favoritos*, uma lista substituível padrão cujas tags `a` apontam para conjuntos de seguimento `kind:30000`. Espelho do `kind:10012` (feeds de relay), que contém tags `a` referenciando conjuntos de relays `kind:30002`, o novo kind permite que um usuário favorite conjuntos de seguimento nomeados, como listas curadas de coleções de pubkeys publicadas por si mesmo ou por outros, e faça clientes os apresentarem para seguir com um toque ou trocar de feed. Note que este número de kind já está contestado: veja o PR de renumeração aberto abaixo.

- **[NIP-46](/pt/topics/nip-46/) (Nostr Connect): Orientação sobre timeout silencioso** ([PR #2375](https://github.com/nostr-protocol/nips/pull/2375), mergeado em 2026-07-15): NIP-46 é o protocolo de assinatura remota onde um cliente envia requisições criptografadas no estilo JSON-RPC a um assinante (bunker) através de relays e aguarda uma resposta criptografada. A mudança mergeada é uma frase de comportamento de fio: requisições feitas com métodos desconhecidos ou não suportados DEVEM ser respondidas com um erro. Anteriormente, um assinante que recebesse um método que não implementava poderia nunca responder, deixando o cliente pendurado até seu próprio timeout disparar, sem como distinguir "método não suportado" de "assinante offline". A resposta de erro obrigatória permite que clientes falhem rápido e apresentem uma mensagem significativa ao usuário em vez de girar indefinidamente.

**PRs e Discussões abertos:**

- **Renumeração de kind:10011 para kind:10021** ([PR #2417](https://github.com/nostr-protocol/nips/pull/2417)): Move a lista de conjuntos de seguimento favoritos recém-mergeada de `kind:10011` para `kind:10021`, porque `10011` já está em uso em outro lugar. O PR de renumeração foi aberto poucos dias após o merge original, então clientes implementando conjuntos de seguimento favoritos devem acompanhar este PR e mirar o número final, não `10011`.

- **[NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect): Simplificação do núcleo** ([PR #2419](https://github.com/nostr-protocol/nips/pull/2419)): Propõe estreitar o NIP-47, o protocolo wallet-connect que permite a aplicativos solicitar pagamentos Lightning de uma carteira remota via Nostr, em uma especificação de núcleo menor. Funcionalidades opcionais e mais especializadas sairia do `47.md` para um repositório de extensões dedicado, [nostr-wallet-connect/nwc](https://github.com/nostr-wallet-connect/nwc), onde especificações de extensão podem evoluir independentemente do núcleo. O objetivo declarado é manter o núcleo pequeno, estável e fácil de implementar, seguindo a direção acordada em chamadas anteriores da NWC de separar uma camada mínima de wallet-connect de comportamentos opcionais mais ricos. Dado o quão amplamente o NIP-47 está implantado em carteiras e aplicativos, qualquer um que fale NWC deve acompanhar a discussão de reestruturação.

- **Trusted Relay Assertions (rascunho, sem número atribuído)** ([PR #2418](https://github.com/nostr-protocol/nips/pull/2418)): Propõe um padrão para publicar avaliações de confiança sobre relays Nostr, posicionado como a camada "o que concluímos" ao lado do [NIP-11](/pt/topics/nip-11/) (o que um relay afirma sobre si mesmo) e [NIP-66](/pt/topics/nip-66/) (o que monitores mediram). Provedores de asserções computariam pontuações de confiança a partir de métricas observadas, reputação do operador e relatórios de usuários; clientes consultariam essas asserções ao escolher a quais relays se conectar. O rascunho introduz `kind:30385` (Trusted Relay Assertion endereçável, carregando tags de pontuação, confiabilidade, qualidade, acessibilidade, operador, política e jurisdição), `kind:10385` (Trusted Provider List substituível, os provedores de asserção escolhidos pelo usuário), e reutiliza rótulos [NIP-32](/pt/topics/nip-32/) para relatórios de relay e operador. Nenhum número de NIP foi atribuído ainda; este é um rascunho em estágio inicial.

- **Operador AND para filtros ("NIP-91", proposto, número ainda não no repositório)** ([PR #2252](https://github.com/nostr-protocol/nips/pull/2252)): Sob o NIP-01, filtros de tags são apenas OR: um filtro `"#t": ["meme", "cat"]` corresponde a eventos com qualquer uma das tags. Esta proposta adiciona um modificador `&` para tags indexáveis, de modo que `"&t": ["meme", "cat"]` retorna apenas eventos carregando ambas as tags, permitindo que relays façam a interseção no servidor em vez de clientes buscarem demais e filtrarem localmente. As regras especificam que AND tem precedência sobre OR, que valores de tags usados em AND devem ser ignorados em OR por relays que suportam, e que clientes DEVEM também incluir as tags OR `#` padrão para compatibilidade com relays que não suportam a extensão (esses relays retornam o resultado OR mais amplo, que o cliente intersecta localmente). O PR é uma continuação reaberta de uma proposta anterior e lista implementações de relay incluindo uma imagem docker nostr-rs-relay, netstr e um relay worker Snort. O número NIP-91 aparece apenas na branch do PR; ainda não está no índice de NIPs do README do repositório, então trate o número como provisório.

- **Applets web Nostr ("NIP-5D", proposto, número ainda não no repositório)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Define um protocolo `postMessage` para aplicações web em sandbox ("napplets") rodando em iframes ou webviews para se comunicar com uma aplicação hospedeira ("shell"). A especificação é deliberadamente um núcleo fino: especifica o envelope de mensagem, regras de sandbox (iframes de napplets DEVEM usar `sandbox="allow-scripts"` sem `allow-same-origin`, e shells NÃO DEVEM expor `window.nostr` NIP-07 dentro do iframe), identificação do remetente via a referência de janela infalsificável `MessageEvent.source`, não `event.origin`, e negociação de capacidades baseada em manifesto. Mensagens de protocolo reais para assinatura, acesso a relays, armazenamento e comunicação entre napplets são delegadas a especificações de extensão NAP (Nostr Applet Protocol), cada uma dona de um domínio de capacidade, com assinatura e criptografia sempre mediadas pelo shell para que chaves nunca entrem no sandbox. A proposta depende da especificação de manifesto de napplet NIP-5A e é oportuna esta semana: o trabalho pré-lançamento v1.13.0 do Amethyst inclui isolamento de contas de napplets, tornando a hospedagem de napplets no lado do cliente uma área ativa de implementação. Assim como o "NIP-91" acima, o número 5D é provisório.

---

## NIP Deep Dive: NIP-42 e NIP-43

Rodar um relay que não é aberto a todos costumava significar inventar tudo por conta própria. Um operador de relay pago ou só por convite tinha que manter uma lista branca fora de banda, geralmente um arquivo de texto de pubkeys coletados por DMs, sem forma padrão de dizer a um cliente conectado "prove quem você é" e sem forma padrão de um usuário pedir admissão ou saber se era membro. Cada relay que queria leituras ou escritas restritas construía seu próprio mecanismo privado, e clientes não conseguiam interoperar com nenhum deles. O [NIP-42](/pt/topics/nip-42/) padroniza a metade de prova de identidade desse problema, e o [NIP-43](/pt/topics/nip-43/) padroniza a metade de associação. Esta semana o nostream, o relay TypeScript, mergeou o par de ponta a ponta: [PR #702](https://github.com/Cameri/nostream/pull/702) restringe leituras de kinds criptografados a destinatários autenticados, e [PR #676](https://github.com/Cameri/nostream/pull/676) adiciona estratégias de eventos de requisição de entrada e saída, ambos mergeados em 20 de julho.

### NIP-42: Autenticação de clientes para relays

O [NIP-42](/pt/topics/nip-42/) responde a uma pergunta: quem está nesta conexão? Um relay que quer restringir leituras ou escritas envia uma mensagem `AUTH` carregando uma string de desafio, no momento da conexão ou sob demanda quando uma requisição precisa de autenticação. O cliente responde com sua própria mensagem `AUTH` contendo um evento efêmero assinado, kind 22242, e o relay responde com uma mensagem `OK` exatamente como se o evento de autenticação fosse uma escrita comum. A sessão autenticada então vale pela duração da conexão, e um cliente pode autenticar vários pubkeys em uma conexão com uma sequência de mensagens `AUTH`, cada uma tratada pelo relay como autenticada.

O evento de autenticação assinado se parece com isto:

```json
{
  "id": "4ef6f2c0b1a84c9a3d0f9c58e2a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0",
  "pubkey": "c308e1f882c1f1dff2a43d4294239ddeec04e575f2d1aad1fa21ea7684e61fb5",
  "created_at": 1753195800,
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com/"],
    ["challenge", "challengestringhere"]
  ],
  "content": "",
  "sig": "8b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1"
}
```

O `pubkey` é a identidade sendo provada, já que o relay verifica a `sig` sobre o `id` do evento contra ele. O `kind` 22242 está na faixa efêmera: o evento é uma credencial no nível da conexão, e relays nunca devem armazená-lo nem transmiti-lo a outros clientes. A tag `relay` vincula a assinatura a uma URL de relay para que um evento de autenticação capturado não possa ser reutilizado contra um relay diferente, e a tag `challenge` o vincula à string de desafio específica que o relay emitiu nesta conexão, bloqueando o replay de uma autenticação capturada em uma conexão posterior. O `created_at` deve estar próximo da hora atual, dentro de uma janela de aproximadamente dez minutos, de modo que um evento de autenticação antigo expire sozinho. O campo `content` está vazio; nada está sendo publicado.

A especificação também define dois prefixos legíveis por máquina que tornam a restrição visível aos clientes. Um relay que rejeita uma assinatura porque o cliente ainda não se autenticou responde com uma mensagem `CLOSED` começando com `auth-required:`, e uma escrita rejeitada recebe um `OK` com o mesmo prefixo. Um cliente que se autenticou mas ainda não tem permissão para a ação recebe `restricted:` em vez disso. Essa distinção é sobre o que o [PR #702 do nostream](https://github.com/Cameri/nostream/pull/702) se constrói: leituras de kinds criptografados agora podem ser fechadas com `auth-required:` até que o pubkey requisitante prove ser o destinatário.

### NIP-43: Metadados e Requisições de Acesso a Relay

O [NIP-43](/pt/topics/nip-43/) responde à pergunta seguinte: agora que o relay sabe quem você é, o que você tem permissão de fazer? Onde o NIP-42 é um handshake em uma conexão ativa, o NIP-43 é um conjunto de eventos publicados que descrevem o estado de associação e permitem que usuários peçam para alterá-lo. Do lado do relay, um evento kind 13534, assinado pelo pubkey no campo `self` do [NIP-11](/pt/topics/nip-11/) do relay, lista uma tag `member` por pubkey, com argumentos de papel opcionais apontando para definições de papéis publicadas como kind 33534. Kind 8000 anuncia um membro sendo adicionado e kind 8001 anuncia uma remoção, ambos assinados pela mesma chave do relay com uma tag `p` para o membro afetado. Do lado do usuário, kind 28934 é uma requisição de entrada carregando um código de convite em uma tag `claim`, kind 28935 é um evento efêmero de código de convite que o relay gera na hora quando um usuário solicita um claim, e kind 28936 é uma requisição de saída.

Uma requisição de entrada se parece com isto:

```json
{
  "id": "9f0e1d2c3b4a59687a6b5c4d3e2f1098a7b6c5d4e3f2019a8b7c6d5e4f3021a9b8",
  "pubkey": "ee1d336e13779e4d4c527b988429d96de16088f958cbf6c074676ac9cfd9c958",
  "created_at": 1753195900,
  "kind": 28934,
  "tags": [
    ["-"],
    ["claim", "invite-code-from-operator"]
  ],
  "content": "",
  "sig": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2"
}
```

O `pubkey` é o usuário pedindo admissão, e kind 28934 marca o evento como uma requisição de entrada. A tag `-` é o marcador de evento protegido do [NIP-70](/pt/topics/nip-70/), dizendo aos relays para não aceitar este evento de ninguém além de seu autor. A tag `claim` carrega o código de convite que o usuário obteve fora de banda, e `created_at` deve ser agora, mais ou menos alguns minutos, para que uma requisição antiga não possa ser reutilizada. O relay responde ao claim com uma mensagem `OK`, reutilizando o prefixo `restricted:` do NIP-42 para falhas como um código expirado ou inválido, e deve então atualizar sua lista kind 13534 e pode publicar um evento de adição de membro kind 8000. A associação deliberadamente não é derivada de um único evento: a especificação diz que a lista assinada pelo relay não deve ser considerada exaustiva ou autoritativa, e um cliente decidindo se alguém é atualmente membro deve consultar tanto o kind 13534 do relay quanto os próprios eventos do membro. Clientes só devem enviar requisições de entrada, convite ou saída a relays que anunciam este NIP na seção `supported_nips` de seu documento NIP-11, e o [PR #676 do nostream](https://github.com/Cameri/nostream/pull/676) é a maquinaria do lado do relay que transforma esses kinds de requisição em mudanças reais de associação.

### História

O NIP-42 é o mais antigo dos dois por uma margem ampla. Ele entrou no repositório de NIPs em 2 de janeiro de 2023, no [commit c80be21c](https://github.com/nostr-protocol/nips/commit/c80be21c), onde fiatjaf simplificou drasticamente um NIP anterior de autenticação de relay redigido por semisol, colapsando um esquema de desafio mais complexo no único evento efêmero assinado que a especificação ainda usa hoje. O NIP-43 chegou muito depois, em 30 de outubro de 2025, quando o [PR #1079](https://github.com/nostr-protocol/nips/pull/1079) de hodlbod foi mergeado, adicionando metadados e requisições de acesso a relay construídos diretamente sobre o prefixo `restricted:` do NIP-42. A lacuna de dois anos e meio reflete quanto tempo o ecossistema rodou relays pagos e privados em listas brancas ad hoc antes que a camada de associação ganhasse um padrão.

### Implementações

Do lado do relay, o [nostream](https://github.com/Cameri/nostream) agora entrega ambas as metades após os merges desta semana. O [strfry](https://github.com/hoytech/strfry) implementa o NIP-42, validando eventos de autenticação kind 22242 em seu ingestor e emitindo desafios a partir de sua configuração. O [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) trata o handshake AUTH em sua camada de conexão com testes cobrindo a janela de desafio e timestamp. O [khatru](https://github.com/fiatjaf/khatru), o framework de relay em Go, rastreia o pubkey autenticado por conexão para que políticas possam restringir leituras e escritas sobre ele. Do lado do cliente, o [Amethyst](https://github.com/vitorpamplona/amethyst) assina respostas kind 22242 aos desafios de relays, incluindo autenticação por stream para suas comunidades criptografadas Concord. Os dois NIPs dividem o controle de acesso ao longo de uma linha limpa: NIP-42 é prova de identidade, com escopo de uma conexão, um desafio e alguns minutos de validade, e não diz nada sobre política. NIP-43 é política, expressa como eventos comuns de relay: quem é membro, quem foi adicionado ou removido, e como um usuário solicita essas transições. A lacuna que implementadores devem ter em mente é que nada ainda padroniza permissões mais granulares além dos metadados de papel opcionais do NIP-43, então qualquer relay fazendo mais do que uma divisão binária membro/não-membro está projetando essa camada por conta própria.

---

Isso é tudo por esta semana. Se você está construindo algo ou tem notícias para compartilhar, entre em contato via DM NIP-17 ou nos encontre no Nostr.
