---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-03-newsletter.md
translationDate: 2026-07-01
---

Amber 6.2.0 lança criptografia NIP-44 v3 antes da especificação. Mostro traz a fundação para escrow liquidado em Cashu em oito PRs, envolvendo o Cashu Development Kit existente como um segundo backend de liquidação junto com Lightning. NIP-F4 podcasts foi mesclado após 27 meses de debate. fiatjaf abre uma proposta contestada de desacoplamento de chave NIP-17 que reabre o argumento arquitetural bunker-versus-Marmot. Amethyst traz labeling de hashtag NIP-32, uma tela dedicada de podcast e zaps onchain em 52 PRs não lançados.

## Matérias principais

### Amber 6.2.0: criptografia NIP-44 v3 lançada

[Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0), lançado em 1º de junho, adiciona [suporte a criptografia NIP-44 v3](https://github.com/greenart7c3/Amber/pull/448) com uma tela dedicada de aprovação, preview de intent, preview de bunker, log de histórico e auto-rejeição para requisições inválidas. A release também registra [autoridades ContentProvider NIP-44 v3](https://github.com/greenart7c3/Amber/commit/8b93340) para que outros apps Android possam solicitar criptografia v3 junto com o caminho v2 existente. NIP-44 em si é a especificação de payload criptografado versionada usada por DMs privadas [NIP-17](/pt/topics/nip-17/), tráfego bunker NIP-46, e outras primitivas Nostr; v3 no Amber é opt-in junto com v2, sinalizada por um método de signer separado para que clientes do lado receptor possam negociar o algoritmo explicitamente. O PR correspondente nos NIPs ainda não chegou, então o Amber está lançando v3 antes do consenso de protocolo, com o formato de fio e autoridade ContentProvider registrados para integração de cliente downstream.

Sessões NIP-46 agora auto-aceitam requisições de ping na conexão, removendo o prompt na primeira ida-e-volta após pareamento. O método de signer `sign_message` foi removido inteiramente após ter sido descontinuado e não usado.

Como o Amber é o signer Android dominante, cada cliente downstream que quiser v3 tem que mirar no formato de fio do Amber até o PR dos NIPs chegar. Isso dá ao Amber influência implícita sobre a especificação final v3 até que o protocolo alcance. A troca é real: v3 em produção permite ao Amber coletar feedback de implementação para o eventual NIP, ao custo de um ponto de referência de implementação única temporário que outros clientes agora têm que igualar.

### Mostro: integração de escrow Cashu via CDK

grunch trouxe oito PRs em MostroP2P esta semana integrando as primitivas P2PK multisig existentes do Cashu (NUT-10 e NUT-11) como um segundo backend de liquidação junto com Lightning no câmbio P2P Bitcoin coordenado por Nostr. As primitivas criptográficas são do Cashu; o trabalho é scaffolding de integração e uma nova trait de backend de escrow. [Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0), lançado em 30 de maio, adiciona os [tipos de protocolo para escrow multisig 2-de-3](https://github.com/MostroP2P/mostro-core/pull/150), assinaturas P_M por prova, e permite eventos de escrow através da validação de resposta. A arquitetura está documentada no [PR #756](https://github.com/MostroP2P/mostro/pull/756) e usa chaves de trade por ordem esclarecidas no [PR #757](https://github.com/MostroP2P/mostro/pull/757).

A implementação foi lançada em seis PRs subsequentes ao longo de um único dia. [F2 (PR #758)](https://github.com/MostroP2P/mostro/pull/758) adicionou a configuração, o modo de escrow e o boot condicional. A próxima fatia, [F3 (PR #760)](https://github.com/MostroP2P/mostro/pull/760), definiu uma trait `EscrowBackend` com uma implementação Lightning e um stub Cashu, permitindo ao Mostro trocar backends de liquidação sem mudar a máquina de estado de ordem. [F4 (PR #759)](https://github.com/MostroP2P/mostro/pull/759) envolveu o [CDK](https://github.com/cashubtc/cdk) (o Cashu Development Kit) para operações de mint e carteira. Trabalho de banco de dados no [F5 (PR #761)](https://github.com/MostroP2P/mostro/pull/761) adicionou locks de escrow compare-and-swap e queries active-locked. [F6 (PR #762)](https://github.com/MostroP2P/mostro/pull/762) construiu um mint containerizado em um job CI dedicado para teste de escrow ponta-a-ponta. O fluxo do Mostro já usa DMs gift-wrapped NIP-59 para coordenação de ordem sobre o relay, então o escrow Cashu se encaixa como uma segunda opção de liquidação junto com Lightning sem tocar no protocolo de fio.

## Releases

### ngit v2.5.0: fallback GRASP e fetches git lazy

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0) muda o comportamento padrão de `git push pr/<branch>` e `ngit send` para produzir um kind PR para novas propostas quando o repositório tem pelo menos um servidor GRASP registrado. Anteriormente isso só era disparado para commits grandes acima de 60 KB ou commits contendo submódulos. Quando um PR não pode ser empurrado para os servidores GRASP do repositório, ngit agora recorre ao roteamento GRASP-06 através dos servidores declarados. A flag `ngit send --git-server` ou `git push -o git-server=<url>` permite aos contribuidores mirar em uma URL git customizada ou servidor GRASP explicitamente.

Republicações `ngit init` agora preservam tags desconhecidas de anúncios existentes, para que tags adicionadas por uma versão futura do ngit ou ferramenta de terceiros sobrevivam à republicação. Um aviso amarelo lista as tags carregadas, e `--clean` as remove sob demanda. `ngit pr apply`, `ngit pr checkout` e `ngit pr list` consultam servidores git de forma lazy e compartilham um único helper de fetch, para que o checkout não faça mais fetch incondicionalmente quando o commit já está local. `ngit pr checkout` também tenta URLs de clone fornecidas pelo submitter do evento PR como fallback quando os servidores git declarados do repo não carregam o tip do PR, correspondendo ao comportamento existente em `ngit pr apply`. ngit é a implementação de referência [NIP-34](/pt/topics/nip-34/) para colaboração git sobre Nostr, e v2.5.0 torna GRASP o caminho de primeira classe para novos contribuidores.

### Jumble v26.5.7: remoção de EXIF e contagens de zap validadas

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7) adiciona duas mudanças que afetam a privacidade do usuário e a integridade de dados diretamente. Localização EXIF e identificadores de câmera agora são removidos de uploads de imagem antes que deixem o cliente, fechando uma superfície de longa data de vazamento de metadados que afetava cada imagem postada do Jumble. Contagens de zap agora são computadas apenas a partir de recibos criptograficamente validados, corrigindo contagens infladas de eventos de zap malformados que haviam permitido a atacantes exagerar totais de zap em notas. A release também adiciona verificação de identidade do remetente para DMs [NIP-17](/pt/topics/nip-17/), fechando uma superfície de spoofing onde um remetente podia forjar sua `pubkey` no seal.

### nostr-calendar v1.6.0: RSVP e tratamento de participantes duplicados

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0) traz o fluxo de RSVP do Formstr ([PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)) e evita participantes duplicados em convites de evento ([PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168)). A opção `waitForAll` na função de publish agora tem padrão false para que a UI não bloqueie em relays lentos ([PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170)). [PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157) lançou os dois rascunhos de proposta NIP do Formstr para agendamento de compromissos e reservas.

### Sprout 0.3.6: Sprout × mesh-llm e seções de canal

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6) é o destaque de uma sequência de seis releases de v0.3.1 a v0.3.6 esta semana. Integração in-process Sprout × mesh-llm chega no [PR #798](https://github.com/block/sprout/pull/798), permitindo ao Sprout servir e consumir nós mesh-llm através de admissão de relay. Seções de canal definidas pelo usuário sincronizam entre dispositivos via Nostr no [PR #792](https://github.com/block/sprout/pull/792), e seções de canal chegam ao mobile com sync de relay no [PR #800](https://github.com/block/sprout/pull/800). Notificações conscientes de thread com controles mutáveis de follow e mute chegam no [PR #761](https://github.com/block/sprout/pull/761).

Anexos de tipo de arquivo arbitrário com cards de download chegaram no [PR #810](https://github.com/block/sprout/pull/810), expandindo o Sprout além de anexos apenas de imagem. Mobile ganhou uma aba de feed social Pulse ([PR #772](https://github.com/block/sprout/pull/772)) e polimento Pulse em superfícies de feed, compose e filter ([PR #796](https://github.com/block/sprout/pull/796)).

### NostrBotKit v0.5.0: chat de grupo Marmot em um framework de bot Rust

[NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md), lançado em 24 de maio no Codeberg, adiciona suporte a [Marmot](/pt/topics/marmot/) (MLS-sobre-Nostr, [NIP-104](https://github.com/nostr-protocol/nips/pull/2014)) ao framework de bot Rust auto-hospedado. Quando `marmot: true` está definido, o bot publica seus key packages MLS (kind 443, 30443, 10051), aceita convites de grupo automaticamente e escuta mensagens em grupos aos quais aderiu. Dois novos tipos de comando, `dm_marmot` e `dm_marmot_npub`, permitem aos bots enviar mensagens para grupos Marmot nomeados ou chats Marmot 1:1 via cron jobs ou webhooks. Para evitar loops de feedback com outros bots, bots NostrBotKit só respondem a mensagens explicitamente endereçadas a eles via `/command` ou `@botname/command`. Anexos criptografados usando MIP-04 são auto-descriptografados e re-uploadados via Blossom ou NIP-96, e o banco de dados de estado MLS é criptografado com uma chave derivada da chave privada do bot. NostrBotKit é o primeiro framework Rust a lançar suporte a bot NIP-104, abrindo implantação de bot criptografado por Marmot para um perfil de operador diferente do caminho TypeScript existente.

### noscrypt v0.1.14: release de biblioteca de criptografia assinada

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14) é uma release de segurança da biblioteca de criptografia C usada por vários clientes Nostr para primitivas secp256k1, NIP-04 e NIP-44. A release vem com [downloads assinados por PGP](https://www.vaughnnugent.com/resources/software/modules/noscrypt) verificáveis contra a chave pública do mantenedor. Clientes downstream que empacotam noscrypt devem validar a assinatura antes de integrar.

### Chama v1.3.0: novo escrow P2P Nostr-native com Fedimint

[Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0), lançado em 1º de junho, é o destaque de uma sequência de quatro releases para um novo cliente de escrow P2P Nostr-native que usa ecash Fedimint e compartilhamento de segredo Shamir 2-de-3 para liquidação. O projeto está em [getchama.app](https://getchama.app) e roda sem servidor. v1.3.0 introduz "heal that sticks" (re-broadcast bem-sucedido e healing de trade que sobrevivem a reinicializações de sessão) e correspondência pay-rail, onde Chamas orientados a EUA apresentam trilhos de pagamento dos EUA primeiro. Base de storefront multi-unidade chegou em [v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11) (schema multi-unidade) e [v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12) (contador de estoque de storefront + fortalecimento de recuperação nativo de bridge Fedimint). Chama se junta a Mostro e Shopstr na categoria marketplace Nostr, distinguido por sua arquitetura sem servidor e liquidação de escrow baseada em Fedimint.

## Mudanças não lançadas

### Amethyst: labeling de hashtag NIP-32, tela de podcast, faixas de música

Amethyst fez merge de 52 PRs e 411 commits esta semana sem cortar uma tag de release. A maior adição funcional é [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111), que implementa labeling de hashtag [NIP-32](/pt/topics/nip-32/) e um feed de hashtag baseado em label usando eventos kind 1985 com namespace `L` e tags de label `l`. Isso substitui o mecanismo frágil de correspondência de texto `#tag` por um modelo de descoberta baseado em labeler onde usuários podem seguir npubs de labelers específicos da forma como seguem criadores de conteúdo. [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) adiciona uma tela dedicada de podcast com lista de episódios e player inline, chegando dias após o merge da especificação de podcast [NIP-F4](/pt/topics/nip-f4/). [PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071) adiciona um feed de Software Apps com filtragem de lista de follow, e [PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067) adiciona suporte a faixas de música e playlists via conjuntos [NIP-51](/pt/topics/nip-51/).

Signers efêmeros para uploads de post anônimos chegam no [PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123), permitindo aos usuários postar anonimamente sem expor sua chave de identidade aos serviços de upload. Um watchdog de auto-cura Tor com testes de integração contra Arti v2.3.0 chega no [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053), fortalecendo o roteamento Tor do Amethyst durante interrupções transientes de rede. Zaps onchain e um filtro NIP-05 para usuários retornando do Gemini chegam no [PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052), ampliando a superfície de zap além do Lightning para pagamentos Bitcoin onchain.

### Shopstr: validação de URL de preview OpenGraph

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504) valida URLs de preview OpenGraph antes de renderizá-las em listagens de marketplace, fechando uma potencial superfície XSS onde vendedores maliciosos podiam embutir conteúdo com script via metadados OG forjados. Lojas hospedadas no Shopstr exibem previews OG para links externos, e URLs não validadas permitiam a um atacante injetar conteúdo arbitrário na UI da loja.

## Atualizações NIP e trabalho de especificação de protocolo

### NIP-F4 (Podcasts) mesclado após dois anos

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093) foi mesclado em 28 de maio, dois anos e três meses após fiatjaf abrir o rascunho original. NIP-F4 define episódios de podcast como eventos kind 54 com tags `imeta` para metadados de arquivo de áudio (URL, mime type, código de idioma ISO, URLs de fallback, flag de serviço NIP-96, bitrate, duração), uma tag `title`, tags opcionais `image` e `description`, e tags `t` para labels de tópico. A especificação deliberadamente mantém RSS como a fonte de verdade: episódios podem carregar uma tag `i` referenciando o GUID de podcast RSS, permitindo aos clientes Nostr linkar para feeds de podcast existentes sem duplicar hospedagem de áudio. O longo debate na thread do PR (com o co-autor do podcast-namespace Dave Jones, Alex Gleason e Mike Terenzio) chegou a um modelo de coexistência onde Nostr fornece a camada social em cima do RSS enquanto RSS mantém a camada de distribuição. O [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) do Amethyst com tela de podcast chega dias após o merge da especificação, e o trabalho de picker GIF do Jumble também inclui scaffolding inicial de anexo de podcast.

### Desacoplamento de chave NIP-17 (PR #2361)

fiatjaf abriu [PR #2361](https://github.com/nostr-protocol/nips/pull/2361) em 1º de junho, propondo que NIP-17 separe a chave de identidade da chave de criptografia. Destinatários anunciam sua chave de criptografia em um novo evento kind 10044, e remetentes usam essa chave anunciada (quando presente) para o seal interno do gift-wrap, recorrendo à chave de identidade do destinatário apenas quando o anúncio está ausente. O PR também adiciona uma tag `n` ao seal carregando a pubkey de criptografia do remetente, para que receptores possam derivar a chave de conversa correta sem descriptografia por tentativa contra cada chave aposentada. A motivação declarada é UX de bunker: sob o design atual, um usuário bunker deve fazer round-trip de cada DM recebida através do signer para descriptografar, já que a chave de criptografia é a chave de identidade detida pelo signer. Desacoplar permite ao cliente deter a chave de criptografia localmente enquanto mantém a chave de identidade no bunker para assinaturas.

A proposta atraiu a revisão mais contestada da semana. Cody Tseng (Jumble) a apoia como o caminho mais fácil para interop de DM cross-client. Vitor Pamplona (Amethyst) objeta em dois pontos: adiciona um novo segredo de descriptografia de longa vida fora do bunker, e clientes que não a lançarem falharão silenciosamente em descriptografar mensagens de clientes que lançarem, sem caminho de degradação porque a quebra é na camada do seal. Pamplona argumenta que o problema já é resolvido corretamente pelos key packages e rotação de época do [Marmot](/pt/topics/marmot/), e que retroencaixar a separação de chave na especificação base NIP-17 cria o tipo de falha de interop que o Marmot levou dois anos para engenhar em torno. A contra-argumentação do fiatjaf tem três partes: o desacoplamento é opcional por destinatário, a correção n-tag aborda a preocupação de descriptografia por tentativa, e a alternativa é manter a UX de bunker quebrada enquanto o Telegram consome o caso de uso de mensageria. A thread permanece aberta sem uma decisão de merge e é a discussão NIP mais observada do trimestre.

### NIP-Silent Payments fluxo de pagamento (PR #2362)

[silentius-satoshi abriu PR #2362](https://github.com/nostr-protocol/nips/pull/2362) em 1º de junho como companheiro ao rascunho NIP mais amplo [Nostr Silent Payments (PR #2355)](https://github.com/nostr-protocol/nips/pull/2355). O NIP de fluxo de pagamento define kind 8352 para notificações de recibo de silent payment (entregues via gift wrap [NIP-59](/pt/topics/nip-59/) para que o link de recibo não seja publicamente observável) e kind 10353 para um cache UTXO criptografado que sincroniza entre dispositivos para a mesma carteira Silent Payments. O par junto permite a um pagador sinalizar um pagamento para um endereço Silent Payments usando primitivas nativas do Nostr sem expor o link on-chain na camada aberta de relay.

### NIP-PIP Perfect IP Packets (PR #2364)

[RandyMcMillan abriu PR #2364](https://github.com/nostr-protocol/nips/pull/2364) em 1º de junho como rascunho. Introduz um transporte de árvore de pacotes com três novos kinds endereçáveis: 39078 carrega o manifest, 39079 carrega fatias individuais, e 39080 carrega solicitações de reparo. A especificação define um formato de fio onde arquivos grandes são quebrados em fatias endereçáveis, com manifests descrevendo a árvore de fatias e solicitações de reparo permitindo aos receptores pedir fatias faltantes. Status de rascunho inicial se aplica, e a proposta ainda não atraiu revisão do mantenedor.

### NIP-29 espaços live de áudio/vídeo (PR #2238)

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238) foi mesclado em 28 de maio, estendendo grupos baseados em relay [NIP-29](/pt/topics/nip-29/) com suporte a espaço live de áudio e vídeo. Grupos agora podem referenciar uma sessão live-space ativa, permitindo que eventos de atividade live estilo [NIP-53](/pt/topics/nip-53/) se ancorem em um contexto de grupo NIP-29.

### NIP-71 vídeo múltiplas faixas de áudio (PR #2255)

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255) foi mesclado em 28 de maio, adicionando tags `imeta` de faixa de áudio a eventos de vídeo NIP-71. O novo formato carrega URL, hash, mime type, tag de idioma (com ISO-639-1 mais flag de versão original), URLs de fallback, sinal de serviço NIP-96, bitrate e duração. Isso habilita streaming apenas de áudio (video podcasts), troca de resolução com áudio estável, múltiplas faixas de idioma, e armazenamento reduzido quando servidores não embutem áudio diretamente em arquivos de vídeo. Clientes devem verificar a disponibilidade de faixa de áudio antes de assumir comportamento de faixa única.

### NIP-59 gift wrap efêmero (PR #2245)

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245) foi mesclado em 28 de maio, adicionando kind 21059 como contraparte efêmera ao gift wrap kind 1059 existente. A semântica corresponde ao wrap NIP-59 padrão mas segue regras de evento efêmero por NIP-01 (relays os descartam após broadcast e não os persistem). Isso permite aos apps escolher persistência baseada em requisitos: indicadores de digitação e pings de presença se beneficiam de efêmero, enquanto histórico de DM precisa de persistência.

### NIP-78 kind específico de aplicação (PR #2292)

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292) foi mesclado em 28 de maio, reclassificando dados específicos de aplicação NIP-78 como um kind endereçável normal, removendo a faixa separada anterior. Isso simplifica a semântica de substituibilidade e alinha NIP-78 com o modelo de evento endereçável usado por outros NIPs de estado de aplicação.

### Esclarecimentos NIP-85 (PR #2304)

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304) foi mesclado em 28 de maio com pequenas melhorias na linguagem em torno de múltiplas chaves e relays por provedor de serviço em Trusted Assertions [NIP-85](/pt/topics/nip-85/), esclarecendo o caminho de rotação de chave de operador para serviços de asserção de relay.

### NIP-01 one-liner de gerenciamento de conexão de relay (PR #2307)

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307) foi mesclado em 28 de maio, adicionando uma única sentença ao NIP-01 sobre como clientes devem lidar com tempos de vida de conexão de relay. A correção aborda uma lacuna de longa data onde clientes divergiam sobre manter conexões WebSocket abertas após fetching, levando a perda silenciosa de mensagem em relays que descartam conexões ociosas.

### NIP-C7 restrição de chat kind 9 (PR #2310)

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310) foi mesclado em 28 de maio, restringindo views de chat NIP-C7 apenas a mensagens kind 9. Isso separa chat efêmero de posts de linha do tempo kind 1 em clientes que implementam superfícies de chat estilo NIP-C7.

### Simplificação NIP-55 (PR #2363)

[PR #2363](https://github.com/nostr-protocol/nips/pull/2363) por greenart7c3, aberto em 1º de junho, simplifica a especificação de aplicação signer Android. Vitor Pamplona aprovou como "Looks good" e fiatjaf perguntou se está pronto para merge. A mudança pavimenta o caminho para o registro de autoridade ContentProvider NIP-44 v3 que o Amber lançou esta semana.

### NIP-44 v3 (implementação Amber antes da especificação)

Amber lançou NIP-44 v3 em v6.2.0 com oito commits implementando o upgrade de criptografia e registro de autoridade ContentProvider, mas o PR de especificação no repositório NIPs ainda não chegou. NIP-44 em si define um formato de payload criptografado versionado usado dentro de eventos assinados; o v2 existente (em produção desde 2024) usa ECDH secp256k1, HKDF, padding, ChaCha20, HMAC-SHA256 e base64. O formato de fio v3 adiciona um novo byte de versão (0x03) antes do nonce, permitindo aos clientes receptores negociar o algoritmo explicitamente. A implementação do Amber inclui auto-rejeição para requisições v3 inválidas, uma tela dedicada de aprovação distinta das aprovações v2, e log de plaintext por direção para o histórico. Até que o PR dos NIPs seja mesclado, v3 permanece como uma extensão específica do Amber. Trate-o como um sinal olhando adiante, não como sinalização estável em todo o protocolo.

## Deep dive de NIP: NIP-32 (Labeling)

[NIP-32](/pt/topics/nip-32/) define uma forma estruturada para qualquer ator Nostr rotular eventos, pubkeys, relays, URLs ou tópicos usando eventos endereçáveis kind 1985 com um vocabulário de label com namespace. A especificação introduz duas novas tags: `L` denota um namespace de label, e `l` denota um label dentro desse namespace. Tags de alvo de label (`e`, `p`, `a`, `r` ou `t`) especificam o que está sendo rotulado. O requisito de namespace evita que múltiplos sistemas de label colidam: um label `spam` em `nip28.moderation` carrega semântica diferente de um label `spam` em `relay-report`.

A escolha de design que torna o NIP-32 útil além da moderação é que labels são asserções, não verdade a nível de protocolo. Um evento kind 1985 diz apenas que uma pubkey específica rotulou um alvo específico em um namespace específico. O modelo de confiança é delegado ao cliente: cada cliente escolhe quais labelers honrar, quais namespaces ler, e que affordance de UI dar a cada label. A mesma primitiva carrega avisos de conteúdo, atribuição de licença, tags de idioma ISO-639-1 em notas kind 1, tags geográficas ISO-3166-2, classificação de conteúdo, sugestões de moderação distribuída e pontuações de reputação.

O [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111) do Amethyst esta semana é a maior implantação até agora. Adiciona labeling de hashtag através de NIP-32 e um feed de hashtag baseado em label, permitindo aos usuários navegar por labels atribuídos por labelers confiáveis. O mecanismo anterior de correspondência de texto `#tag` que originalmente dirigia a descoberta de hashtag no Nostr permanece como fallback para notas não rotuladas. O modelo hashtag-como-label significa que a mesma nota pode ser descobrível sob múltiplos labels atribuídos por labelers diferentes, e usuários podem silenciar ou impulsionar labelers específicos sem afetar as notas subjacentes.

Auto-labeling também é suportado. Um autor pode anexar tags `L` e `l` diretamente às suas próprias notas kind 1 para declarar idioma, localização e tópico. Uma nota taggeada `["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]` se auto-identifica como inglês e pode ser filtrada por clientes conscientes de idioma sem infraestrutura de labeling de terceiros.

Exemplo de evento de label NIP-32 rotulando uma nota kind 1 como inglês e atribuindo a ela uma tag de moderação:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

O rollout do Amethyst combinado com o recente trabalho de Trusted Relay Assertions sugere que NIP-32 está se tornando o substrato padrão para qualquer padrão "asserção dirigida pelo usuário sobre um alvo" no Nostr. O próximo teste é se labelers em si desenvolvem hierarquias de confiança: se usuários seguirão npubs de labelers específicos da forma como seguem criadores de conteúdo.

## Deep dive de NIP: NIP-F4 (Podcasts)

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md) foi mesclado esta semana, dois anos e três meses após fiatjaf abrir o rascunho original (PR #1093). O prefixo F é numeração hex simples: NIP-F0 até NIP-FF usam o mesmo espaço hex de 1 byte que NIP-0A até NIP-0D, com a faixa hex superior servindo como overflow agora que a faixa decimal 01–99 está enchendo. NIP-F4 define como podcasts publicam episódios e metadados como eventos Nostr enquanto mantêm RSS como uma camada complementar para o próprio arquivo de áudio.

A escolha arquitetural central é que cada podcast é seu próprio par de chaves Nostr. A especificação abre com isso diretamente: "cada podcast é seu próprio par de chaves Nostr". Isso permite aos podcasts combinar sua presença de podcasting com uma presença normal kind 0 / kind 1 de microblogging, e permite a um podcast mudar de propriedade ao longo do tempo através de handover de chave ou assinatura compartilhada estilo MuSig2. Quatro kinds de evento carregam a camada de publicação:

- **`kind:10154`**: metadados de podcast substituíveis. Carrega tags `title`, `image`, `description`, `website` opcionais, e tags `p` opcionais marcando autores com um `role` de `host`, `cohost` ou `editor`.
- **`kind:10164`**: contra-reivindicação de autor. O exemplo na especificação usa kind `10064` (um typo aberto para correção), mas o cabeçalho e o texto ao redor o identificam como `kind:10164`. Usuários listam as pubkeys de podcast que autoriam, para que clientes possam verificar as tags `p` em `kind:10154` contra uma reivindicação equivalente do suposto autor. Sem isso, um podcast poderia falsamente marcar qualquer um como host.
- **`kind:54`**: eventos de episódio autorados pela pubkey do podcast diretamente. Tags incluem `title`, `image` opcional, `description`, e uma ou mais tags `audio`. Cada tag `audio` é `["audio", "<audio-url>", "<optional_media_type>"]`. A especificação nota "outros campos importantes a serem especificados aqui depois de mais descoberta", e a forma mesclada é deliberadamente mínima.
- **`kind:10054`**: uma lista favoritos-de-podcasts estilo [NIP-51](/pt/topics/nip-51/), permitindo aos usuários marcar quais podcasts seguem.

O debate da thread em torno do merge envolveu o co-autor do Podcasting 2.0 [Dave Jones](https://github.com/daveajones), [Alex Gleason](https://github.com/alexgleason), [Mike Terenzio](https://github.com/mterenzio), [Pablo F7z](https://github.com/pablof7z) e [staab](https://github.com/staab). Jones argumentou fortemente contra qualquer tentativa de substituir RSS: "Foi tentado muitas vezes e sempre falha", citando JSONfeed, XMPP, AMP, API do Twitter e a migração falhada do Spotify. Terenzio reformulou a proposta como uma camada social em cima do RSS, mantendo o próprio RSS como a camada de distribuição. fiatjaf concordou em recuar e deixar a proposta amadurecer: "Concordo com tudo que você disse mas ainda acho que podemos consegui-lo, vamos parar aqui por um tempo". Dois anos depois, a especificação mesclada chega mais perto de coexistência do que substituição.

Três questões de design permanecem explícitas na especificação mesclada:

- O typo de `kind:10164` (exemplo mostra `10064`) precisa ser reconciliado antes que clientes possam interoperar seguramente.
- Descoberta em nível de episódio sem linking RSS GUID é deixado aberto. A especificação mesclada não tem tag `i`, formato `podcast:item:guid`, e mecanismo de bridging RSS. Clientes que querem ponte um catálogo RSS existente em eventos kind 54 devem definir a convenção de ponte eles mesmos.
- O stub "outros campos importantes" na definição de `kind:54` deixa bitrate, duração, idioma, ponteiros de transcrição, capítulos e metadados por segmento como território aberto para propostas de acompanhamento.

O [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) do Amethyst traz uma tela dedicada de podcast com lista de episódios e player inline dias após o merge, a primeira grande implementação de cliente. Jumble lançou scaffolding inicial de anexo de podcast junto com seu picker GIF. Wavlake permanece a maior plataforma de podcast Nostr-native e precisará decidir se alinha seus eventos existentes de faixa de música kind 31337 com o modelo de episódio kind 54 do NIP-F4.

Exemplo de evento de episódio NIP-F4 kind 54, correspondendo ao conjunto mínimo de tags da especificação mesclada:

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episódio 42: Por que RSS venceu"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones e fiatjaf sobre coexistência de protocolo e a camada social."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "Neste episódio discutimos a jornada de dois anos do NIP-F4 do rascunho ao merge, e por que a coexistência com RSS acabou sendo a escolha arquitetural correta.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

O PR #1093 esteve aberto por 27 meses, bem acima da duração mediana aberta para PRs de NIP mesclados. O próximo teste para NIP-F4 é se o typo de kind 10164 é reconciliado, se convenções de descoberta de episódio e ponte RSS emergem dos implementadores, e se os principais hosts de podcast publicam sob pares de chaves por-podcast como a especificação recomenda.
