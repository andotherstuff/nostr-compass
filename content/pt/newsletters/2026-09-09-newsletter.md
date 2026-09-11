---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
translationOf: /en/newsletters/2026-09-09-newsletter.md
translationDate: 2026-09-11
draft: false
type: newsletters
description: "O Nostr Compass #39 acompanha fluxos de trabalho git assinados, publicação pelo navegador, transmissões ao vivo auto-hospedadas, consentimento de relays comunitários, eventos privados, lançamentos focados e o contrato de links NIP-21/NIP-27."
---

Bem-vindo de volta ao [Nostr Compass](https://nostrcompass.org), seu guia semanal sobre Nostr.

**Esta semana:** [ngit e GitWorkshop](https://ngit.dev/v3) trazem fluxos de trabalho git assinados para o Nostr e o [Blossom](/pt/topics/blossom/), o [nsite-clay](https://github.com/jooray/nsite-clay) torna a publicação pelo navegador recuperável, e o [Wingman App](https://github.com/OtherStuffAI/wm-app) une navegação, assinatura local, autenticação e arquivos. [Shosho e Livelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) conectam transmissões auto-hospedadas ao Nostr, o [Communitator](https://github.com/dyne/communitator) torna modelos de relay inspecionáveis antes da assinatura, o [cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) publica horários de agendamento, e o [Plektos](https://github.com/derekross/plektos/pull/16) criptografa eventos privados. Lançamentos etiquetados adicionam trabalho de recuperação e privacidade no [Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4), [Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27), [LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) e [SkateSpots](https://zapstore.dev/apps/org.skatespots.app). O trabalho de desenvolvimento abrange renderização de [NIP-27](/pt/topics/nip-27/), preferências de relay assinadas no [Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397), destinos de pagamento [NIP-A3](/pt/topics/nip-a3/) e espelhos Blossom. Mudanças mescladas no [repositório de NIPs](https://github.com/nostr-protocol/nips) esclarecem assinaturas somente ao vivo e dados de aplicativo autenticados. Nosso mergulho profundo explica como os links [NIP-21](/pt/topics/nip-21/) e as referências NIP-27 transportam perfis e eventos Nostr entre aplicativos.

## Principais Notícias

### Fluxos de trabalho git assinados trazem CI, repositórios privados e lançamentos para o Nostr

O [lançamento v3 de 8 de setembro](https://ngit.dev/v3) reúne ngit, GitWorkshop, ngit-grasp e ngit-ci em um único fluxo de trabalho assinado. O [ngit](https://ngit.dev/ngit.git) transporta branches, patches e pull requests como eventos [NIP-34](/pt/topics/nip-34/), enquanto o [GitWorkshop](https://ngit.dev/gitworkshop.git) fornece a interface de revisão. O lançamento adiciona o ngit-ci 0.1, um serviço de integração contínua auto-hospedado cujas instruções e resultados trafegam como eventos Nostr assinados, permitindo que as verificações rodem em hardware controlado pelo mantenedor junto à revisão de código.

O mesmo lançamento dá ao [ngit-grasp v3](https://ngit.dev/ngit-grasp.git) repositórios privados por meio da extensão de repositório privado GRASP-08 e torna explícita a autoridade do mantenedor. Registros de lançamento assinados podem apontar para ativos no [Blossom](/pt/topics/blossom/), mantendo tanto os metadados de lançamento quanto os arquivos endereçados por conteúdo fora de uma forge hospedada. O [novo site de documentação](https://ngit.dev/v3) reúne os componentes de cliente, repositório privado, CI e web.

### nsite-clay torna a publicação pelo navegador recuperável

Uma [correção de prompt do signatário de 31 de agosto](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8), a [recuperação de publicação](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0) e os [controles de edição de 2 de setembro](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7) fazem do [nsite-clay](https://github.com/jooray/nsite-clay) uma ferramenta de publicação no navegador para um site de página única. O usuário edita o modelo de objeto de documento no local, serializa o resultado, envia-o como um blob [Blossom](/pt/topics/blossom/) endereçado por conteúdo e republica o manifesto [NIP-5A](/pt/topics/nip-5a/) do site. Nenhum build local ou servidor é necessário.

O [publicador no navegador](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html) agora torna a publicação com falha recuperável e reduz os prompts repetidos do signatário, enquanto o [guia de edição](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html) documenta o ciclo. O resultado continua sendo um site NIP-5A comum para os gateways existentes.

### Wingman App une navegação, assinatura e arquivos

O trabalho de setembro adiciona [seletores de arquivos](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec), [publicação de perfil](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704), [restauração segura de signatário e sessão](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6) e [builds móveis testados](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac) ao [Wingman App](https://github.com/OtherStuffAI/wm-app). Seu shell Flutter injeta um provedor [NIP-07](/pt/topics/nip-07/) nas páginas abertas dentro do aplicativo, enquanto o Flight Deck e o Drive baseado em Tower fornecem uma superfície de trabalho e um espaço de arquivos ao lado do navegador.

O Wingman assina requisições HTTP autenticadas usando [NIP-98](/pt/topics/nip-98/). A [implementação da requisição](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs) constrói o evento que um servidor verifica antes de responder, dando a uma identidade instalada um caminho de aprovação consistente para ações de relay, assinatura em aplicativos web e arquivos.

### Shosho lança os streams auto-hospedados do Livelier

O [Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) foi lançado em 1º de setembro com suporte ao [Livelier](https://github.com/r0d8lsh0p/livelier), cuja [atualização de atribuição de 31 de agosto](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc) identifica a fonte da bridge e do Owncast nos perfis intermediados. O Livelier observa o diretório público do Owncast, verifica se uma transmissão de vídeo está ao vivo e então publica um evento endereçável `kind:30311` da [NIP-53](/pt/topics/nip-53/). A descoberta trafega pelo Nostr enquanto o vídeo permanece no servidor do streamer.

O chat atravessa a bridge como eventos `kind:1311`. O [design da bridge](https://github.com/r0d8lsh0p/livelier) abre uma conexão do lado da fonte apenas enquanto um leitor Nostr estiver inscrito, rotula as identidades derivadas e envia o chat transitório para um relay que o exclui após três horas. O relay de descoberta aceita escritas de eventos ao vivo apenas da chave da bridge; o relay de chat usa [autenticação NIP-42](/pt/topics/nip-42/) e [sinalizadores de evento protegido da NIP-70](/pt/topics/nip-70/).

### Communitator torna os templates de relay inspecionáveis antes da assinatura

A [série de lançamento de 31 de agosto](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c) dá ao [Communitator](https://github.com/dyne/communitator) templates canônicos para listas de relays de kind `10002`, servidores Blossom de kind `10063` e caixas de entrada de mensagens privadas de kind `10050`. Antes que um assinante se conecte, a aplicação mostra endpoints normalizados, permissões de leitura/escrita, kinds de eventos, relays de publicação fixos e destinos.

O [fluxo delimitado de assinatura e publicação](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501) separa a conexão da aplicação. Cada evento é assinado separadamente, uma execução usa no máximo quatro conexões WebSocket e um destino só conta após um `OK` positivo da [NIP-01](/pt/topics/nip-01/). Os resultados distinguem entrega completa, parcial, com falha e cancelada. Os templates compartilhados permanecem recomendações não confiáveis; a [superfície de consentimento](https://github.com/dyne/communitator#security-and-consent) explica a observabilidade de relays e de rede.

### cal.emre.xyz publica disponibilidade de compromissos via NIP-52

O repositório público foi aberto em um [commit inicial de 2 de setembro](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743), seguido de um [anúncio assinado do handler em 3 de setembro](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac) para o [cal.emre.xyz](https://cal.emre.xyz). Um anfitrião publica a disponibilidade como um evento `kind:31923` da [NIP-52](/pt/topics/nip-52/); um convidado publica um RSVP `kind:31925`.

Ele lê os eventos do anfitrião e os RSVPs de ocupação aceitos a partir dos relays, exclui intervalos de tempo sobrepostos e mantém os eventos Nostr como o registro de agendamento sem copiá-los para um banco de dados separado. Os anfitriões podem assinar com [NIP-07](/pt/topics/nip-07/), [NIP-46](/pt/topics/nip-46/) ou uma chave local; os convidados podem gerar uma chave separada. Seu [repositório](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) também expõe o `naddr` resultante e os links de calendário, com e-mail desativado por padrão.

### Plektos torna eventos privados um único canal criptografado

A [implementação de eventos privados de 2 de setembro](https://github.com/derekross/plektos/pull/12) faz de cada encontro do [Plektos](https://github.com/derekross/plektos) um canal privado dentro de uma comunidade criptografada do [Concord](/pt/topics/concord-protocol/). A lista de convidados, o quadro de RSVPs, a lista de inscrições, a thread, as contribuições, as imagens de capa, as edições e as exclusões são criptografados juntos; um convite carrega apenas a chave daquele evento e nenhum evento de calendário em texto claro é publicado.

A [auditoria de ciclo de vida de 6 de setembro](https://github.com/derekross/plektos/pull/14) ancora o id da definição do evento para busca direta quando existem mais de 500 wraps, mantendo um fallback paginado. Os pacotes de convite expiram 30 dias após o término de um evento e podem ser desativados, mas alguém que já obteve uma chave de canal pode retê-la. Um [reparo separado de segurança do parser](https://github.com/derekross/plektos/pull/16) faz com que identificadores [NIP-19](/pt/topics/nip-19/) malformados em type-length-value (TLV) falhem em vez de travar o parser.

## Lançamentos Marcados

### Vector 0.4.4 torna a recuperação de comunidades criptografadas mais segura

O [Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) foi lançado em 31 de agosto com correções de recuperação de comunidades, rotação de chaves, moderação e roteamento de respostas. A refundação fecha uma comunidade invadida para o caminho de convite usado pelos atacantes; a substituição de membros sobrepõe o estado local desatualizado; e um único membro inalcançável não congela mais a lista de membros. Rotações vazias são rejeitadas, promoções preservam os membros online e as operações se recusam a executar quando os membros necessários não podem ser alcançados.

O [lançamento](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) também persiste exclusões e banimentos de moderadores, recriptografa o livro de visitas após uma mudança de senha, vincula respostas de notificação à sua conversa após a reinicialização e usa apenas caminhos multiplayer verificados. Estes são controles de recuperação, não revogação de chaves já obtidas.

### Primal Android 3.5.27 verifica a identidade do assinante e da carteira

O [Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) foi lançado em 3 de setembro após a [verificação de identidade do assinante](https://github.com/PrimalHQ/primal-android-app/pull/1108) e a [autenticação de requisições de carteira](https://github.com/PrimalHQ/primal-android-app/pull/1105) serem mescladas em 31 de agosto. A assinatura local rejeita uma requisição cuja identidade não corresponde à conta mantida, e as requisições [NIP-47](/pt/topics/nip-47/) recebidas são autenticadas antes do processamento. O roteamento de zap-polls também envia votos ao autor da enquete quando ela aparece em uma resposta.

### GRAIN 0.8.0-rc2 encerra um caminho de evento reconhecido, mas não armazenado

O [GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) foi lançado em 7 de setembro, depois que uma falha de armazenamento permitia retornar `OK` antes que o gravador assíncrono do banco de dados LMDB percebesse a capacidade de armazenamento esgotada. O relay agora emite avisos aos 80 e 95 por cento, recusa novos eventos aos 97 por cento mantendo espaço para exclusões e relata falhas do gravador após a aceitação. A retenção percorre dos eventos mais antigos para os mais recentes, o encerramento trata mensagens tardias e filtros inválidos não descartam mais os irmãos válidos.

A [versão](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) também confirma anúncios de monitores do kind `10166` e relatórios de relays do kind `30166`, remove relatórios desatualizados, mantém os relays configurados como reserva e informa limites ao vivo e autenticação no [NIP-11](/pt/topics/nip-11/) em vez de zeros estáticos.

### LibreNostr 0.5.0–0.5.2 faz o roteamento Tor falhar de forma fechada

O [LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) foi lançado em 7 de setembro com um modo Orbot que roteia relays, zaps, uploads, mídia, reprodução e pré-visualizações por uma única porta SOCKS, além de uma correção para uma falha na tela de zaps. Se o Orbot ou o proxy não estiver disponível, as conexões são interrompidas em vez de vazar para uma rota direta. A [versão 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1) impede que buscas lentas de [NIP-50](/pt/topics/nip-50/) atrasem os resultados locais; a [0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2) substitui o layout recursivo de threads e corrige a ordenação de threads.

O [comportamento fail-closed](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) se aplica a todas as superfícies de rede listadas pela versão, e é necessário reiniciar, pois esses clientes são de longa duração. As versões de correção preservam essa escolha enquanto limitam falhas não relacionadas de busca, profundidade de pilha e layout.

### SkateSpots adiciona um caminho de relay no dispositivo

A [versão assinada de 8 de setembro na Zapstore](https://zapstore.dev/apps/org.skatespots.app) adiciona um relay Citrine opcional ao SkateSpots. Spots, crews, mensagens e dados do mapa podem ser carregados localmente; as publicações entram em fila offline; e o telefone mantém uma cópia local. O conteúdo existente de stash e mensagens permanece criptografado de ponta a ponta. As verificações de pagamento exigem valores de invoice e recibos de zap emitidos pelo provedor antes de conceder acesso ou contabilizar contribuições.

O [relay local](https://zapstore.dev/apps/org.skatespots.app) é uma opção de armazenamento e continuidade, não um substituto para todos os relays remotos. Ele permite que um skatista continue trabalhando durante um período desconectado e depois reconcilie a atividade assinada, enquanto as mudanças de pagamento impedem que um recibo autoassinado se torne prova de liquidação.

### Whistle 1.8.15 corrige a recuperação do ciclo de vida de grupos criptografados

O [Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) foi lançado em 3 de setembro, depois que uma correção de ciclo de vida no Android impediu que detentores de estado no nível de rota destruíssem as assinaturas de relays e as atualizações de localização válidas para todo o aplicativo. Suas notas de versão também descrevem o estado de conexão atualizado após bloqueio ou modo de espera e um backlog de 501 eventos recuperado no caso observado.

O [bug](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) vinculava a propriedade de um serviço de longa duração a uma tela de curta duração. Manter viva a instância com escopo de activity e verificar o socket antes de uma leitura única torna menos provável que a navegação comum do Android e a suspensão em segundo plano pareçam um grupo vazio.

### TWENTY ONE Companion 1.12.0 separa DMs criptografadas do chat legado

O [TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) foi lançado em 5 de setembro com DMs em gift wrap do [NIP-17](/pt/topics/nip-17/). A caixa de entrada criptografada é separada do chat de espaços mais antigo, que permanece distinto porque essas mensagens nunca foram criptografadas e não podem ser migradas. PDFs e vídeos são suportados, sujeitos à política do relay, e ocultações pessoais sincronizam sem se tornar banimentos de moderador.

A [separação visível](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) faz parte do modelo de segurança. Chamar o histórico antigo de caixa de entrada segura deturparia sua procedência, enquanto migrá-lo silenciosamente sugeriria uma criptografia que não existia quando ele foi escrito.

### ZapStore 1.1.2 valida ids de eventos e rotação de certificados

O [ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) foi lançado em 4 de setembro com validação de id de evento do NIP-01: o cliente recalcula o id de um evento recebido e rejeita divergências antes de usá-lo. A versão também identifica pacotes instalados fora da ZapStore. No servidor, a [retenção de hash de certificado](https://github.com/zapstore/relay/pull/8) preserva tags `apk_certificate_hash` repetidas para que a rotação da chave de assinatura do Android possa manter uma linhagem aprovada.

A [verificação de id de evento](https://github.com/zapstore/zapstore/releases/tag/1.1.2) impede que um relay ou cache altere tags ou conteúdo mantendo o id antigo. O indicador de origem da instalação fornece procedência separada quando um pacote Android com o mesmo application id veio de outro canal.

### Amber 6.6.1 mantém as respostas do assinante atribuíveis

O [Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) foi lançado em 4 de setembro, depois que o processamento de permissões foi corrigido para tolerar um `kind` opcional ausente, e as solicitações de assinatura rejeitadas passaram a retornar seu id de solicitação original. Os aplicativos chamadores podem associar uma rejeição à operação enviada. A versão também atualiza os padrões de assinante remoto e adiciona um relay indexador.

Juntas, essas [correções](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) preservam a atribuição em ambas as direções: um registro de permissão permanece utilizável quando um campo opcional está ausente, e uma recusa permanece vinculada à solicitação que a causou. As mudanças nos relays padrão afetam a descoberta, mas não substituem a decisão de autorização local do assinante.

## Em Desenvolvimento

### Zap Cooking renderiza referências NIP-27 com dicas de relay

[A fusão de 4 de setembro](https://github.com/zapcooking/frontend/pull/665) faz o [Zap Cooking](https://github.com/zapcooking/frontend) renderizar referências `nostr:npub` e `nostr:nprofile` em artigos, receitas, pré-visualizações do editor e visualizações de impressão. Identificadores inválidos permanecem como texto, a resolução não é bloqueante e o editor pré-visualiza o Markdown que será assinado. Quando existem informações de relay, um `npub` simples se torna um `nprofile` com relays outbox e uma tag `p` correspondente.

Na mesma semana, corrigiu-se [leituras do kind `30023` com escopo de autor](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7), adicionaram-se [relays de busca NIP-50 verificados](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea) com desduplicação e proteções contra consultas obsoletas, e repararam-se [chamadas de carteira NIP-47](https://github.com/zapcooking/frontend/pull/705) após alterações de dependências quebrarem saldos e histórico.

### Conduit reconcilia preferências assinadas de relay e Blossom

O [Conduit](https://github.com/Conduit-BTC/conduit-mono) fundiu a [edição de preferências Blossom](https://github.com/Conduit-BTC/conduit-mono/pull/374) em 2 de setembro e a [reconciliação de preferências assinadas](https://github.com/Conduit-BTC/conduit-mono/pull/397) em 7 de setembro. Market e Merchant retêm a lista de relays kind `10002` e a declaração de inbox kind `10050` válidas mais recentes, preservam uma lista assinada utilizável quando um evento mais novo está mal formado, distinguem uma lista vazia explícita de uma consulta não disponível e não substituem relays declarados que falharam por padrões do código.

O [editor do kind `10063`](https://github.com/Conduit-BTC/conduit-mono/pull/374) permite ao usuário carregar, reordenar, revisar, assinar externamente, publicar e ler de volta uma lista ordenada de servidores de mídia HTTPS sem contatar esses servidores ou inserir um padrão não declarado.

### Alvos de pagamento NIP-A3 chegam a três clientes

De 1 a 3 de setembro, [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) e [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) implementaram alvos de pagamento NIP-A3 do kind `10133`. O Amethyst oferece uma transferência opcional apenas quando existe um alvo compatível e não a transforma em zap; o Grimoire usa um registro fixo antes de construir URIs de carteira; o Pollerama valida endereços Monero e busca a lista de relays do autor antes de consultar os alvos. Cada cliente ainda precisa de um método de pagamento permitido, uma rota de relay e uma exibição precisa.

### Ditto expande o fallback Blossom e embeds ao vivo

O [Ditto](https://github.com/soapbox-pub/ditto) fundiu [fallback e espelhamento Blossom amplos](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07) em 6 de setembro. Avatares, emblemas, banners, imagens de comunidade, emojis personalizados e ícones de aplicação agora tentam servidores declarados com o mesmo hash de blob; uploads espelhados usam um token de autorização BUD-11 padrão. Uma [alteração de 4 de setembro](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa) adicionou embeds compactos de transmissão ao vivo `kind:30311`.

## Trabalho de Protocolo e Especificação

### Nostr Implementation Possibilities

O [NIP-01](/pt/topics/nip-01/) agora esclarece [o filtro `limit: 0`](https://github.com/nostr-protocol/nips/pull/2460), fundido em 4 de setembro. Um relay MUST retornar nenhum evento armazenado, MUST enviar `EOSE` quando as consultas iniciais terminarem e MUST manter a assinatura ativa para novos eventos correspondentes. Clientes podem abrir uma assinatura somente ao vivo com um campo de filtro, mantendo o histórico local. O esclarecimento registra comportamento compatível entre várias implementações de relay e relays públicos.

O [NIP-78](/pt/topics/nip-78/) ganhou um [requisito de dados de aplicação autenticados](https://github.com/nostr-protocol/nips/pull/2458), fundido em 3 de setembro. Relays SHOULD exigir autenticação [NIP-42](/pt/topics/nip-42/) para os kinds `78` e `30078` e SHOULD servi-los apenas ao autor autenticado do evento. Isso é um SHOULD, não uma garantia de confidencialidade: clientes não podem tratar relays arbitrários como armazenamento privado. A fusão também desencoraja kinds de dados de aplicação personalizados como intercâmbio público genérico.

O [NIP-AC](/pt/topics/nip-ac/) foi aberto em 4 de setembro como uma [proposta de sinalização WebRTC](https://github.com/nostr-protocol/nips/pull/2461) explicitamente aberta. Ele usa kinds efêmeros provisórios para ping, solicitações de conexão, ofertas, respostas e candidatos ICE, endereçados com `p` e agrupados por uma tag `e` de sessão; o kind `30600` dá suporte à descoberta. Relays SHOULD transmitir e MUST NOT armazenar esses eventos de sinalização enquanto os pares se conectam diretamente. Os números permanecem provisórios, clientes SHOULD usar [listas de relays NIP-65](/pt/topics/nip-65/), e aplicações que precisam de confidencialidade SHOULD criptografar o conteúdo de ofertas, respostas e candidatos com [NIP-44](/pt/topics/nip-44/).

## Mergulho no NIP: Links URI e Referências no Texto de Eventos

Um identificador Nostr precisa de um significado transportável antes que outra aplicação possa abri-lo. O [NIP-21](/pt/topics/nip-21/) coloca um identificador [NIP-19](/pt/topics/nip-19/) após o esquema URI `nostr:`, dando a navegadores, sistemas operacionais e aplicações uma forma despachável. O [NIP-27](/pt/topics/nip-27/) define o que esse mesmo URI significa dentro do `content` legível do evento. O NIP-21 atravessa um limite de aplicação; o NIP-27 mantém uma referência de perfil ou evento em prosa assinada. Nenhum dos dois cria um kind de evento ou altera mensagens de relay; as [duas especificações](https://github.com/nostr-protocol/nips/tree/master) definem apenas comportamento de vinculação e renderização.

### Despacho de URI e semântica do NIP-19

[A gramática do NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) é `nostr:` seguida de uma entidade bech32 do NIP-19. O `nsec` é excluído porque codifica uma chave privada. Não há componente de autoridade, caminho ou consulta, portanto um link conforme é `nostr:npub1...`, e não `nostr://npub1...`. Uma plataforma ou cliente pode registrar-se como manipulador; a especificação não escolhe o aplicativo instalado nem define um fallback web.

O prefixo indica ao cliente o que decodificar. O `npub` carrega uma chave pública e o `note` um id de evento. O `nprofile` adiciona dicas de relay opcionais a um perfil; o `nevent` adiciona relays, autor e kind a um id de evento; e o `naddr` carrega o autor, o kind e o identificador `d` de um evento endereçável, com relays opcionais. Essas formas usam [campos type-length-value do NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md). As dicas restringem a descoberta, mas não provam nem a posse do relay nem o controle do autor. Todo evento obtido ainda precisa de uma recomputação do id e de uma verificação de assinatura.

A forma de perfil na [especificação do NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) é:

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

O [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) também define pontes HTML: uma página que serve um evento Nostr pode colocar seu `naddr` em `<link rel="alternate">`, e um perfil pode colocar um `nprofile` em `<link rel="me">` ou `<link rel="author">`.

### Renderização do NIP-27 e tags opcionais

O [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) aplica-se a conteúdo de evento legível, como notas do kind `1` e artigos do kind `30023`. Um editor pode exibir `@name`, mas publica `nostr:nprofile1...` na string assinada. Um leitor varre a URI, decodifica sua entidade NIP-19, busca o alvo e pode renderizar um nome, cartão, pré-visualização ou link local. Se a decodificação falhar, a URI permanece como texto comum. O conteúdo bruto não deve ser reescrito: alterá-lo muda a serialização do NIP-01, o id e a assinatura.

Referências de conteúdo e tags têm funções relacionadas, mas distintas. O [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) descreve tags `p` e `e` opcionais e a tag `q` do [NIP-18](/pt/topics/nip-18/). Um cliente pode mostrar uma referência sem criar uma notificação ou relação de thread; a descoberta de citações deve escrever tanto a URI quanto uma tag `q`. A [implementação de 4 de setembro do Zap Cooking](https://github.com/zapcooking/frontend/pull/665) segue essa divisão ao manter a URI enquanto adiciona dicas de relay e uma tag `p` correspondente. Adicionar `p` ou `q` não torna a URI privada, e o NIP-27 não tem modo de menção oculta.

O seguinte [evento do kind `1`](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a) foi recuperado de `wss://nos.lol` e verificado antes da inclusão como uma referência concreta do NIP-27. Seu `content` contém um `naddr` para um evento endereçável independente de versão. A decodificação resulta no kind `30402`, autor `91036d...310a`, o identificador `d` do workbook e uma dica `wss://nos.lol/`. As tags `q`, `p`, `t`, `zap` e `client` são escolhas do aplicativo, não requisitos do NIP-27.```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### Confiança, comportamento em falhas e implementações de clientes

Um leitor seguro encontra um token `nostr:` completo, valida bech32, decodifica NIP-19, rejeita `nsec`, ignora tipos TLV desconhecidos e deixa textos malformados ou excessivamente longos de lado. `npub` e `nprofile` levam a consultas de perfil; `note` e `nevent` identificam eventos imutáveis; `naddr` seleciona o evento endereçável válido mais recente para seu tipo, autor e tag `d`. Dicas de relay reduzem a busca, mas não ampliam a confiança. Sob as [regras de eventos do NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md), o cliente verifica o id de um `nevent` buscado e confere a assinatura de cada candidato `naddr` antes de aplicar as regras de substituição de eventos endereçáveis.

Pré-visualizações inline são uma escolha do cliente, com custos de privacidade e recursos. Buscar todas as referências revela os interesses do leitor e pode criar uma avalanche de consultas, então os clientes podem usar cache, adiar buscas até o conteúdo ficar visível, limitar a concorrência e exigir um clique para mídia desconhecida. Sob o [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md), uma pré-visualização deve permanecer distinta do texto assinado do autor atual. A falha deve aparecer como texto não resolvido ou um cartão indisponível, não tratada silenciosamente como conteúdo verificado.

A confiança também muda conforme o tipo de identificador. Um `nevent` nomeia bytes imutáveis, então o cliente pode rejeitar um evento buscado cujo id serializado difere do id solicitado. Um `naddr` nomeia uma coordenada substituível, então o cliente deve verificar cada candidato e aplicar as regras de eventos endereçáveis antes de decidir qual versão exibir. Uma dica de relay é útil para a primeira consulta em ambos os casos, mas não constitui endosso do relay nem do conteúdo retornado. A [definição TLV do NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md) fornece os dados necessários para tornar essas verificações explícitas.

O [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) define um link portátil que pode ser aberto fora do Nostr, enquanto o NIP-27 torna esse mesmo link durável dentro de texto assinado. Um cliente que implementa apenas NIP-21 pode abrir uma URI colada, mas não renderiza referências embutidas. O suporte completo a NIP-27 adiciona varredura, decodificação segura, política de busca, renderização local e uma escolha explícita sobre tags de notificação e citação. A URI compartilhada mantém essas camadas interoperáveis sem forçar os clientes a apresentá-las de forma idêntica. [Damus](https://github.com/damus-io/damus) modela referências inline como menções tipadas. Seu [código de menções](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift) mapeia `npub` e `nprofile` para referências de perfil, `note` e `nevent` para referências de evento e `naddr` para referências de endereço; [NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift) as encaminha ao destino apropriado. [Primal Android](https://github.com/PrimalHQ/primal-android-app) [analisa o esquema e formas coladas](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt), valida bech32 e extrai dicas de relay, depois [mapeia referências em modelos de conteúdo de notas](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt). [Zap Cooking](https://github.com/zapcooking/frontend/pull/665) renderiza as mesmas referências em artigos, receitas, pré-visualizações do editor e visualizações de impressão.

---

Envie uma DM NIP-17 para compartilhar um projeto ou notícia através do [projeto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
