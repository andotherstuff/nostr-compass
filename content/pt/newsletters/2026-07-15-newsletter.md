---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
draft: false
type: newsletters
translationOf: /en/newsletters/2026-07-15-newsletter.md
translationDate: 2026-07-15
description: "Vector v0.4.0 aposenta Marmot para chats em grupo em favor do protocolo aberto Concord e lança Concord v2 dias depois, Amethyst faz merge da sua própria implementação limpa de Concord, Sonar se separa do Bitchat com um alpha multiplataforma e uma especificação de pacotes de stickers, Divine Mobile 1.0.16 traz criptografia em repouso e procedência ProofMode, Bitchat 1.7.0 adiciona voz push-to-talk ao vivo, e MDK v0.9.4 limita o login com assinante externo."
---

Bem-vindos de volta ao Nostr Compass, seu guia semanal sobre Nostr.

**Esta semana:** [Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later) aposenta [Marmot](/pt/topics/marmot/) como transporte padrão para Chats em Grupo em favor de [Concord](/pt/topics/concord-protocol/), um protocolo de comunidade aberto com licença MIT também usado pelo Armada da Soapbox, e lança Concord v2 quatro dias depois com um seletor de comandos com barra para bots, um temporizador de autodestruição e badges NIP-58. [Amethyst faz merge da sua própria implementação limpa de Concord, compatível a nível de protocolo](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities), na mesma semana. [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) se separa do Bitchat com um alpha multiplataforma e é a fonte de especificação citada para a proposta de kinds de pacotes de stickers desta semana. [Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance) traz um editor de vídeo mais profundo, criptografia em repouso e procedência ProofMode que sobrevive a downloads de clipes com marca d'água. [Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh) adiciona voz push-to-talk ao vivo para DMs e push-to-talk assinado na malha pública. [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) limita o login com assinante externo e adiciona persistência de rascunhos, continuando seu passe de endurecimento na mesma semana em que Vector se afasta da especificação para chat em grupo.

Os lançamentos etiquetados trazem [n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support) adicionando suporte a NSEC Bunker, [cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi) adicionando suporte de serviço de carteira NIP-47 em cdk, cdk-nwc e cdk-ffi, [Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import) melhorando Nostr Connect e adicionando importação ncryptsec1, [Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications) chegando ao macOS com envio programado, [Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) adicionando um interruptor mestre de DM, [Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts) endurecendo backups de chaves para o formato NIP-49, [Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding) adicionando onboarding FROST de primeiro uso, [Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications) adicionando uma carteira Cashu e notificações push baseadas em relay, [Kubo](#kubo-ships-tablet-mode-and-group-chat-photos) adicionando modo tablet e fotos em chats de grupo, e [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests) adicionando requisições auxiliares de git, diff e leitura de arquivos.

No lado não publicado, [Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards) permite que contas atribuam apelidos a contatos com cartões NIP-85 criptografados em 54 PRs mergeados, [Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug) lança a Fase 3 do My Kitchen e corrige um bug de quórum do pool NDK, [Kehto](#kehto-streams-outbox-reads-before-relay-discovery) transmite leituras de outbox antes da descoberta de relay terminar, [Wired e TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing) adicionam compartilhamento de receita de criador com NIP-57, [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) reconstrói sua caixa de entrada de pedidos do comerciante em torno de checkout efêmero como convidado, [Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002) endurece o provisionamento do criador de canal em 240 PRs mergeados, e [Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing) adota um assinante NIP-49 com múltiplas contas e pareamento QR. Recém-rastreados esta semana: [OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr), [Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles), e a seleção Discovery [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer), um assinante NIP-55 sem chaves que redireciona para um companheiro de hardware Heartwood.

O repositório de NIPs não faz merge de nada na última semana e abre seis propostas: [kind:10011 conjuntos de seguimento favoritos](#open-kind10011-favorite-follow-sets), um [drive criptografado privado que estende NIP-4E](#open-private-encrypted-drive-extends-nip-4e), [NIP-DA compartilhamento privado de dados com permissões](#open-nip-da-permissioned-private-data-sharing), [kinds de pacotes de stickers 10031 e 30031](#open-sticker-pack-kinds-10031-and-30031), [fixação de mensagens NIP-29](#open-nip-29-message-pinning-with-kind9010-and-kind39005), e uma [reestruturação da descoberta de relay NIP-66](#open-nip-66-relay-discovery-restructure). O Deep Dive cobre [NIP-99 e a extensão de comércio Gamma Markets](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension).

---

## Matérias principais

### Vector v0.4.0 move os Chats em Grupo de Marmot para Concord, e Amethyst lança seu próprio cliente Concord dias depois

[Vector](https://github.com/VectorPrivacy/Vector) é um mensageiro Nostr construído em torno de um cliente de binário único focado em privacidade para DMs e chats em grupo. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) reescreve o motor de mensagens da aplicação em uma biblioteca compartilhada `vector-core` e, no mesmo lançamento, aposenta [Marmot](/pt/topics/marmot/) (MLS-sobre-Nostr) como transporte padrão para Chats em Grupo em favor de [Concord](/pt/topics/concord-protocol/), um protocolo de comunidade criptografado de ponta a ponta; o histórico existente de grupos Marmot não é transferido, e as notas de lançamento orientam os usuários a fazer backup de qualquer dado de grupo Marmot antes de atualizar. As próprias notas de lançamento do Vector descrevem Concord como "nosso protocolo de mensagens personalizado", mas as [especificações CORD-01 a CORD-07](https://github.com/concord-protocol/concord) subjacentes são publicadas separadamente, com licença MIT, e já estão implementadas fora do Vector: o cliente estilo Discord da Soapbox, [Armada](https://gitlab.com/soapbox-pub/armada), constrói sua funcionalidade de Comunidades sobre a mesma especificação Concord, e um dia depois, [Amethyst fez merge da sua própria implementação limpa e compatível a nível de protocolo](https://github.com/vitorpamplona/amethyst/pull/3566), coberta em detalhes abaixo. O mesmo lançamento do Vector adiciona roteamento opcional por Tor para todo o tráfego, login com assinante remoto [NIP-46](/pt/topics/nip-46/) por QR ou URI bunker colada, múltiplas contas com um alternador dentro do aplicativo, e pacotes de emojis personalizados compartilhados entre clientes. A exclusão de mensagens remove uma mensagem para ambos os lados em DMs e chats em grupo, e o Vector deliberadamente mantém a chave de assinatura efêmera em vez de seguir o fluxo padrão de exclusão [NIP-17](/pt/topics/nip-17/), um desvio motivado por privacidade que o projeto destaca explicitamente nas notas de lançamento. Quatro dias depois, [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) lança **Concord v2**, descrito como trazendo melhorias importantes de privacidade e estabilidade para Comunidades mantendo as existentes funcionando, junto com um seletor de comandos com barra estilo Discord para bots com parâmetros tipados, um temporizador de autodestruição por chat, e um sistema de badges NIP-58 para caçadores de bugs. O afastamento de Marmot para chat em grupo acontece na mesma semana em que [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) abaixo continua investindo na especificação.

### Amethyst lança uma implementação limpa de Concord para comunidades criptografadas de ponta a ponta

[Amethyst](https://github.com/vitorpamplona/amethyst) é um cliente Nostr rico em funcionalidades para Android e multiplataforma. [PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566) adiciona uma implementação completa de [Concord](/pt/topics/concord-protocol/) (CORD-01 a CORD-07) cobrindo comunidades sem servidor e criptografadas de ponta a ponta: planos de controle, chat e livro de visitas envolvidos com gift-wrap sobre relay comuns, com aplicação de papéis, expulsões e banimentos enraizados no proprietário que cada cliente verifica localmente em vez de confiar em um servidor, e recriptografia para cortar o acesso de membros removidos. O código de protocolo e criptografia reside em `quartz/`, os modelos de estado e visualização em `commons/`, e as telas e navegação em `amethyst/` para Android, com verbos CLI enxutos em `cli/`; ainda não há interface desktop, já que a lógica compartilhada reside em `quartz`/`commons` para o Desktop adotar depois. A implementação é de sala limpa: construída a partir das especificações CORD públicas e constantes de protocolo observadas, sob a própria licença MIT do Amethyst, distinta do código base AGPL-3.0 do Armada. Os valores de vetores de teste do próprio Armada foram portados para os testes unitários do Quartz para confirmar que ambos os clientes realmente interoperam a nível de protocolo, dando ao Concord três implementações independentes em dias: Vector lançando primeiro, Armada como cliente de referência da Soapbox, e agora a construção a partir da especificação do Amethyst.

### Sonar se separa do Bitchat com um alpha multiplataforma e uma especificação de pacotes de stickers

[Sonar](https://sonarprivacy.xyz/) é um mensageiro e carteira com malha Bluetooth mais Nostr desenvolvido a partir do Bitchat, com DMs em grupo Marmot interoperáveis com White Noise. O código está em [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar). [v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7) adiciona janelamento de transcrição limitado estilo Signal para que o desempenho de abertura e rolagem permaneça local-first, sincroniza o estado de descoberta próxima entre pares, e corrige uploads de mídia Blossom que falhavam no tratamento de content-type e status HTTP; a precedente [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6) drenou eventos Marmot ao vivo para atualização mais rápida do chat e fechou lacunas de paridade de funcionalidades entre Android e iOS em chamadas, mensagens, carteira e push. Sonar também é a fonte de especificação citada para [PR #2410](#open-sticker-pack-kinds-10031-and-30031), que registra kinds de eventos de pacotes de stickers sob a própria especificação "Sonar Stickers" do projeto, dando a este lançamento um link direto para o trabalho de protocolo desta semana.

### Divine Mobile 1.0.16 traz um editor de vídeo mais profundo, criptografia em repouso e procedência ProofMode

[Divine](https://github.com/divinevideo/divine-mobile) é um cliente de vídeos curtos construído sobre Nostr com curadoria de feed por Web-of-Trust. [v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16), o primeiro lançamento etiquetado desde o #30, adiciona transições de clipes, reprodução reversa, um gravador de narração e marcadores de ritmo na linha do tempo ao editor de vídeo, junto com um controle de ajuste de feed que permite ao usuário deslizar para ajustar recomendações diretamente em vez de deixá-las para sinais opacos de engajamento. O lançamento também ativa criptografia em repouso para dados locais, adiciona uploads em segundo plano que sobrevivem à suspensão do aplicativo, e carrega os dados de procedência [ProofMode](/pt/topics/proofmode/) ao baixar um clipe com marca d'água para que a atestação de criação humana permaneça intacta em trânsito. Divine também inclui novas proteções para contas de menores de 16 anos e expande a localização para 17 idiomas e 284 strings traduzidas.

### Bitchat v1.7.0 adiciona voz push-to-talk ao vivo para DMs e a malha pública

[Bitchat](https://github.com/permissionlesstech/bitchat) é um aplicativo de chat com malha Bluetooth com um gateway opcional para relay Nostr. [v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0), lançado na noite em que o #30 foi publicado, adiciona voz push-to-talk ao vivo em [PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403) que transmite áudio enquanto o remetente mantém o botão pressionado e volta para uma nota de voz se o stream cair, mais push-to-talk assinado na malha pública em [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406) para que rajadas de voz ao vivo no canal compartilhado da malha carreguem autenticação do remetente. O lançamento também repara a rotação de peer-ID religando o vínculo em um reanúncio verificado, reconhecendo o mesmo par sob seu novo ID ([PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)), e mensagens diretas para um par atualmente inalcançável agora entram em fila com entrega store-and-forward em vez de falhar diretamente ([PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)). Isso continua diretamente da cobertura do #30 sobre o trabalho de [NIP-13](/pt/topics/nip-13/) proof-of-work e gateway malha-para-Nostr do v1.6.0.

### MDK v0.9.4 limita o login com assinante externo e adiciona persistência de rascunhos

[MDK](https://github.com/marmot-protocol/mdk) é o SDK de referência para o protocolo [Marmot](/pt/topics/marmot/), a camada de mensagens MLS-sobre-Nostr que o #30 cobriu marcando sua especificação como adotada. [v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4) limita os passos de diretório consultivo que um cliente percorre durante o login com assinante externo em [PR #793](https://github.com/marmot-protocol/mdk/pull/793), prevenindo um loop de tentativas sem limite quando um assinante remoto é lento ou não responde. O mesmo lançamento adiciona persistência de rascunhos de mensagens e vinculações de perfil a website em [PR #812](https://github.com/marmot-protocol/mdk/pull/812), continuando o passe de endurecimento incremental que o MDK executou desde o corte do v0.9.0.

---

## Lançamentos etiquetados

### n_cord v1.1 adiciona suporte a NSEC Bunker

[n_cord](https://github.com/0n4t3/n_cord) é um cliente de chat com tecnologia Nostr inspirado no Discord e IRC. [v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) adiciona suporte a NSEC Bunker [NIP-46](/pt/topics/nip-46/) junto com uma correção de bug no tratamento de respostas.

### cdk v0.17.3 adiciona suporte de serviço de carteira NIP-47 em cdk, cdk-nwc e cdk-ffi

[cdk](https://github.com/cashubtc/cdk) é um kit de desenvolvimento Cashu; este lançamento é apenas Bitcoin/Lightning na maioria dos aspectos, mas [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) adiciona suporte de serviço [NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect) com um crate de serviço NWC dedicado, integração de carteira, bindings FFI para `cdk-ffi`, e cobertura de testes de ponta a ponta, dando às carteiras Cashu construídas sobre cdk uma superfície padrão de Nostr Wallet Connect.

### Coop Mobile v0.2.4 melhora Nostr Connect e adiciona importação ncryptsec1

[Coop Mobile](https://git.reya.su/reya/coop-mobile) é um cliente de mensagens privadas [NIP-17](/pt/topics/nip-17/) para plataformas móveis. [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) melhora seu fluxo de [NIP-46](/pt/topics/nip-46/) Nostr Connect, corrige um indicador de carregamento que ficava permanentemente em algumas conexões, e adiciona suporte de importação para o formato de chave criptografada [NIP-49](/pt/topics/nip-49/) `ncryptsec1` junto com uma tela de importação de identidade redesenhada.

### Nmail v0.14.0 chega ao macOS com envio programado e notificações push

[Nmail](https://github.com/nogringo/nostr-mail-client) é um cliente de e-mail construído sobre Nostr; [v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) leva o aplicativo ao macOS, adiciona envio programado com uma caixa de Programados dedicada para mensagens em fila, e adiciona notificações push. O lançamento também troca a resolução de identificadores Nostr da agenda de contatos para o resolvedor [NIP-05](/pt/topics/nip-05/) do NDK no lugar de uma implementação própria.

### Nostrord v2.2.0 adiciona um interruptor mestre de DM e mensagens diretas mais ricas

[Nostrord](https://github.com/nostrord/nostrord) é um cliente de chat em grupo baseado em relay [NIP-29](/pt/topics/nip-29/) para Android, iOS, web e desktop. [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) adiciona um interruptor mestre para desabilitar todas as funcionalidades de mensagens diretas de uma vez ([PR #175](https://github.com/nostrord/nostrord/pull/175)) e lança "mensagens diretas mais ricas" ([PR #186](https://github.com/nostrord/nostrord/pull/186)), continuando da cobertura do #30 sobre o lançamento que consolidou o pool de relay e detectou WebSockets zumbi.

### Nostr WoT 0.3.86 endurece backups de chaves e prompts de assinatura

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) é uma extensão de navegador que vincula uma identidade Nostr com uma carteira Lightning. [v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) move backups de chaves criptografadas para o formato padrão [NIP-49](/pt/topics/nip-49/), faz com que prompts de assinatura mostrem o evento completo e todas as tags em vez de um resumo, verifica dados do relay contra sua assinatura, e para de expor a identidade ativa ao trocar de conta. A extensão também remove a permissão de navegador `scripting` não utilizada.

### Keep Android v1.1.8 adiciona onboarding FROST de primeiro uso

[Keep](https://github.com/privkeyio/keep-android) é um assinante Android construído sobre fragmentos de chave FROST de limiar. [v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) adiciona um fluxo de primeiro uso que explica os fragmentos de chave FROST e permite que um novo usuário escolha uma política de assinatura Manual, Básica ou Automática antes que a primeira requisição de assinatura chegue, o primeiro onboarding do lado Android para o modelo de assinatura de limiar do crate keep-mobile subjacente.

### Noscall v0.6.0 adiciona uma carteira Cashu e notificações push baseadas em relay

[Noscall](https://github.com/sanah9/noscall) é um aplicativo de chamadas de áudio e vídeo seguras construído sobre Nostr. [v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) adiciona uma carteira Cashu com escopo de conta com saldos multi-mint, envio e recebimento de ecash, e pagamento e recebimento Lightning com persistência de cotações. O lançamento também migra as notificações push do Android do Firebase Cloud Messaging para um caminho de entrega baseado em relay Nostr através do UnifiedPush, e melhora a confiabilidade de VoIP iOS e push APNs durante tentativas de login.

### Kubo lança modo tablet e fotos em chats de grupo

[Kubo](https://github.com/JeroenOnNostr/kubo) é uma plataforma de vídeo Nostr segura para crianças com curadoria de feed por Web-of-Trust. [kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) adiciona um layout de grade para tablet opcional para o feed infantil e suporte para anexar fotos a mensagens de chat em grupo, mais correções para o botão de cadastro que ficava escondido atrás do teclado virtual no Android.

### Nostr Codex Phone v0.2.9 adiciona requisições auxiliares de git/diff/leitura de arquivos

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) é uma superfície de controle móvel para um worker de assistente de codificação local que se comunica através de DMs criptografados de Nostr. [v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) adiciona ações de ferramentas OpenCode móveis incluindo requisições auxiliares de git, diff, leitura de arquivos, status e histórico, melhorias de fixação e busca de sessão, e um controle de parada de tarefa, junto com um wrapper de upload criptografado para [Blossom](/pt/topics/blossom/) que foi lançado no v0.2.8 anterior.

### GitWorkshop v3.0.3 corrige refs recém-anunciadas no explorador de repositórios, e lança sua primeira build para Android

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) é uma interface web git-sobre-Nostr para explorar e revisar repositórios NIP-34. [v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) corrige as visualizações de branches, tags, commits e exploração de código que falhavam ao resolver uma ref que um repositório anuncia depois que o explorador já a carregou, junto com limpeza de timing de workflows CI, confirmado diretamente contra a tag e o histórico de commits. Na mesma semana, GitWorkshop publicou sua primeira build nativa para Android na [Zapstore](https://zapstore.dev), começando na v3.0.0 e alcançando v3.0.3 em horas; a interface web continua sendo a interface principal, e o pacote Android traz a mesma exploração de repositórios NIP-34 para um celular pela primeira vez.

### Bitcoin-Safe chega ao Flathub, destacando seu plugin Nostr Sync & Chat

[Bitcoin-Safe](https://bitcoin-safe.org) é uma carteira Bitcoin de autocustódia construída em torno de workflows com assinantes de hardware. O projeto [publicou um pacote no Flathub](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe) esta semana, sua primeira listagem em uma loja de aplicativos Linux convencional. O lançamento no Flathub coloca o plugin Sync & Chat do Bitcoin-Safe diante de uma audiência mais ampla: o plugin usa mensagens diretas [NIP-17](/pt/topics/nip-17/), através da própria biblioteca [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat) do projeto, para sincronizar labels de carteira entre os dispositivos de um usuário e para enviar e receber PSBTs para coassinatura multisig remota entre participantes de confiança. A camada Nostr em si foi lançada antes, em [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0) (2026-06-29), que redesenhou a assinatura de transações em torno de um tipo de conexão "Compartilhar via Chat & Sync" junto com QR, USB e Bluetooth. A notícia desta semana é o empacotamento no Flathub colocando essa funcionalidade existente diante de uma audiência Linux convencional pela primeira vez.

---

## Mudanças não publicadas

### Amethyst permite que contas atribuam apelidos a contatos com cartões NIP-85 criptografados

Além da [implementação de Concord](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) coberta acima, Amethyst fez merge de 54 outros PRs na última semana. O principal entre eles é [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548), que permite a uma conta atribuir um apelido a qualquer outro usuário publicando seu próprio cartão de contato kind 30382 [NIP-85](/pt/topics/nip-85/) sobre eles. O apelido, uma nota privada, e quaisquer mapeamentos personalizados de código curto de emoji [NIP-30](/pt/topics/nip-30/) ficam dentro do conteúdo criptografado com [NIP-44](/pt/topics/nip-44/) do cartão, de modo que apenas a conta signatária pode lê-los, e os cartões sincronizam através do conjunto estendido de relay outbox da conta no login e incrementalmente depois. Feeds, chats e menções renderizam o apelido no lugar do nome de exibição público, com um cartão de apelido acessível por toque na página de perfil acima do nome real do usuário.

### Zap Cooking lança a Fase 3 do My Kitchen e corrige um bug de quórum do pool NDK

[Zap Cooking](https://github.com/zapcooking/frontend) é um aplicativo de compartilhamento de receitas e comunidade culinária construído sobre Nostr. Fez merge de 43 PRs continuando sua funcionalidade de planejamento de refeições "My Kitchen", incorporando geração de lista de compras, um seletor de receitas e uma grade de planejamento semanal nesta fase. O mesmo conjunto de mudanças corrige um bug de quórum de prontidão do pool de conexões do [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit) que podia deixar leituras de relay esperando além do ponto em que um quórum de relay já havia respondido.

### Kehto transmite leituras de outbox antes da descoberta de relay

[Kehto](https://github.com/kehto/web) é um runtime web inicial para applets Nostr [NIP-5D](/pt/topics/nip-5d/), ou "napplets". Fez merge de 26 PRs. [PR #193](https://github.com/kehto/web/pull/193) corrige leituras de outbox que anteriormente esperavam o carregamento de listas de relay [NIP-65](/pt/topics/nip-65/) terminar antes de abrir qualquer relay, de modo que um carregamento de lista de relay que nunca se resolvesse podia bloquear tanto a entrega de eventos quanto os timeouts de consulta; a correção abre hints de relay validados imediatamente e transmite resultados enquanto relay de escrita são descobertos. Uma segunda mudança ([PR #196](https://github.com/kehto/web/pull/196)) alinha a página de auditoria de identidade do projeto com NAP-SHELL, o contrato de ciclo de vida da plataforma Napplet, parte do mesmo trabalho de alinhamento de protocolo visível em outros lugares do lançamento `napplet/web` desta semana.

### Wired e TAO adicionam compartilhamento de receita de criador com NIP-57

[Wired](https://github.com/smolgrrr/Wired) e [TAO](https://github.com/smolgrrr/TAO) são clientes gêmeos de redes sociais focados em liberdade de expressão construídos sobre Nostr, compartilhando a mesma lista de PRs; ambos fizeram merge de [PR #121](https://github.com/smolgrrr/Wired/pull/121), que implementa compartilhamento de receita de criador [NIP-57](/pt/topics/nip-57/) para que zaps enviados a uma publicação possam ser divididos automaticamente para contribuidores além do autor original. Isso continua a cobertura do #30 do par elevando seu sinal de proof-of-work para 21 bits como trabalho não publicado.

### Conduit Mono reconstrói a caixa de entrada de pedidos do comerciante em torno de checkout efêmero como convidado

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) é um protocolo de marketplace adjacente às listas de classificados [NIP-99](/pt/topics/nip-99/). [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) adiciona checkout como convidado usando uma chave efêmera gerada pelo navegador: o convidado envia um pedido criptografado e um relatório de pagamento ao comerciante usando essa chave de uso único, e o comerciante faz acompanhamento fora de banda por telefone ou e-mail, de modo que o comprador nunca precisa de uma identidade de caixa de entrada durável. [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) reconstrói a caixa de entrada de pedidos do comerciante em torno de um modelo único de estado de pedido compartilhado, separando papéis de comprador e comerciante e exigindo um código de rastreamento e transportadora antes que um pedido físico ou misto possa passar para enviado. O fluxo de checkout do projeto se baseia em mensagens privadas [NIP-17](/pt/topics/nip-17/), criptografia [NIP-44](/pt/topics/nip-44/) e gift wrap [NIP-59](/pt/topics/nip-59/). O [NIP Deep Dive](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) desta semana cobre as convenções de [Gamma Markets](/pt/topics/gamma-markets/) para as quais este mesmo problema de estado de pedido aponta.

### Buzz endurece o provisionamento do criador de canal em torno de kind 39002

[Buzz](https://github.com/block/buzz) é uma plataforma de comunicação de mente coletiva que conecta agentes de IA e humanos sobre Nostr. Fez merge de 240 PRs na última semana, continuando seu arco de endurecimento da camada de relay desde a cobertura do #30 sobre métricas de turno de agente kind 44200. A correção desta semana ([PR #1830](https://github.com/block/buzz/pull/1830)) trata o criador de um canal como membro antes da lógica de provisionamento de canal kind 39002 rodar, fechando uma condição de corrida onde o próprio canal do criador podia rejeitá-lo durante a configuração.

### Nostr Docs adota um assinante NIP-49 com múltiplas contas e pareamento QR

[Nostr Docs](https://github.com/formstr-hq/nostr-docs) é um aplicativo de documentos colaborativos nativo de Nostr. Fez merge de 5 PRs, o notável ([PR #50](https://github.com/formstr-hq/nostr-docs/pull/50)) adotando o pacote `@formstr/signer` para autenticação completa [NIP-49](/pt/topics/nip-49/) com troca de múltiplas contas e pareamento QR, substituindo um caminho de assinatura próprio anterior.

### Também publicado

Correções menores de interoperabilidade de assinantes e confiabilidade aterrissaram em vários projetos rastreados na última semana sem superfície nova suficiente para seus próprios parágrafos: [ngit-cli](https://github.com/DanConwayDev/ngit-cli), um cliente de linha de comando para uma alternativa ao GitHub baseada em Nostr, lança [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3) fazendo com que `ngit init` dê orientação de configuração acionável em vez de pedir repetidamente um nsec; [Manent](https://github.com/dtonon/manent), um aplicativo privado de notas e arquivos criptografados construído sobre Nostr, lança [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1) corrigindo o login com assinante Android quebrado quando Amber retorna um pubkey hexadecimal e melhorando a rolagem do login bunker; [NoorNote](https://github.com/77elements/noornote), um cliente Nostr leve e livre de serviços Google, lança [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8) corrigindo notificações perdidas de grupos Nostrord e adicionando um interruptor de alerta de publicação própria; [Bray](https://github.com/forgesworn/bray), um servidor MCP Nostr consciente de confiança para agentes de IA e humanos, lança [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0) enviando metadados de nome de cliente em conexões bunker [NIP-46](/pt/topics/nip-46/); [Lumilumi](https://github.com/TsukemonoGit/lumilumi), um cliente web Nostr, faz cache de listas de relay [NIP-65](/pt/topics/nip-65/) em armazenamento local para fallback offline; [Earthly](https://github.com/moogmodular/earthly), um aplicativo de cidade e comunidade local baseado em Nostr, adiciona busca geográfica [NIP-50](/pt/topics/nip-50/); e [lnbits](https://github.com/lnbits/lnbits), um sistema de carteira e contas Lightning gratuito e de código aberto, lança [PR #3925](https://github.com/lnbits/lnbits/pull/3925) fazendo com que `send_nostr_dm` publique de forma não bloqueante dentro de um lançamento focado em Lightning.

---

## Recém-rastreados e descobertos

### OpenDiscord v1.0.1 se lança como um cliente estilo Discord sobre Nostr

[OpenDiscord](https://github.com/sofia-gros/open-discord) é um cliente de servidores e canais estilo Discord construído sobre Nostr com permissões baseadas em papéis e lobbies de voz WebRTC/SFU. [v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) é o primeiro lançamento com instalador etiquetado do projeto.

### Auditable Voting v0.1.140 alinha os papéis de organizador, votante e proxy de auditoria

[Auditable Voting](https://github.com/tidley/auditable-voting) é um shell de votação apenas de cliente sobre Nostr. [v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) alinha os papéis de organizador, votante e proxy de auditoria com o evento exato de definição de questionário público assinado pelo organizador, fechando uma lacuna onde um proxy de auditoria podia agir sobre contas geradas obsoletas ou estado persistido de um worker ou organizador diferente.

### Cambium v0.3.2 se pareia com Heartwood como um assinante NIP-55 sem chaves

[Cambium](https://github.com/forgesworn/cambium) é a seleção Discovery desta edição: um assinante Android [NIP-55](/pt/topics/nip-55/) que não mantém material de chave privada próprio, redirecionando cada requisição de assinatura sobre [NIP-46](/pt/topics/nip-46/) para um assinante de hardware Heartwood companheiro. O projeto compartilha a organização GitHub `forgesworn` com o projeto rastreado Bray, e o próprio Heartwood foi coberto no #30 lançando a ponte de assinatura relay-para-serial com a qual o lado Android do Cambium agora se comunica. [v0.3.2](https://github.com/forgesworn/cambium) refina a folha de aprovação para alertar ao vivo quando a identidade selecionada difere do vínculo existente do aplicativo e move as escritas do log de atividade para uma única fila não bloqueante.

### Também lançados esta semana: echoes, Dispatch e Linky

Três lançamentos a mais merecem menção esta semana. [echoes](https://github.com/Lwb89dev/echoes) é um aplicativo de notas offline-first e criptografado de ponta a ponta que sincroniza privadamente sobre Nostr. [Dispatch](https://github.com/freecritter/dispatch) é um organizador de viagens local-first onde cada salvamento é criptografado com [NIP-44](/pt/topics/nip-44/) e respaldado sobre Nostr sob uma chave dedicada e não vinculável, e seu lançamento [v0.3.0](https://github.com/freecritter/dispatch) adiciona login Amber [NIP-55](/pt/topics/nip-55/) para que o aplicativo nunca toque a chave privada do usuário diretamente. [Linky](https://github.com/hynek-jina/linky) combina contatos e DMs de Nostr com pagamentos Lightning e Cashu em um único aplicativo web progressivo.

---

## Trabalho de protocolo e atualizações de NIP

Nenhum PR foi mergeado no [repositório de NIPs](https://github.com/nostr-protocol/nips) na última semana. Seis propostas foram abertas.

### Aberta: kind:10011 conjuntos de seguimento favoritos

[PR #2413](https://github.com/nostr-protocol/nips/pull/2413), de fiatjaf, adiciona kind:10011 conjuntos de seguimento favoritos. Espelha o padrão existente onde kind:10012 (conjuntos de relay favoritos) mantém tags `a` apontando para conjuntos de relay kind:30002, estendendo o mesmo mecanismo de favoritos para conjuntos de seguimento kind:30000 para que um cliente possa marcar uma lista de seguimento curada sem substituir sua própria lista de contatos.

### Aberta: drive criptografado privado que estende NIP-4E

[PR #2412](https://github.com/nostr-protocol/nips/pull/2412), da equipe Form*, propõe um evento genérico de Metadata, kind 34578, distinguido por uma tag de identificador `d` e uma tag de subtipo `t`, junto com um sistema de arquivos criptografado privado construído sobre ele que já está implementado no próprio cliente Form* Drive, ainda experimental. Um registro de arquivo é um evento de Metadata com `t=files`: os blobs de arquivo ficam em servidores [Blossom](/pt/topics/blossom/) enquanto apenas um índice criptografado reside em relay, e cada fragmento de arquivo recebe seu próprio par de chaves efêmero com criptografia [NIP-44](/pt/topics/nip-44/) v2 derivada por HKDF. Um evento companheiro de Chave de Criptografia Desacoplada mantém uma chave simétrica por drive contra a qual os metadados de cada arquivo são descriptografados, e se baseia explicitamente em [NIP-4E](/pt/topics/nip-4e/), o rascunho de abstração de armazenamento ainda aberto de fiatjaf ([PR #1647](https://github.com/nostr-protocol/nips/pull/1647), aberto desde dezembro de 2024).

Essa única chave por drive significa que uma chave vazada expõe os metadados de cada arquivo no drive, já que os pares de chaves efêmeros por arquivo variam apenas a chave de criptografia de fragmento, e não a chave de descriptografia de metadados; nenhum caminho de rotação ou revogação existe ainda além de publicar um novo evento de Metadata alertando que eventos mais antigos podem ser perdidos. Uma segunda proposta mais estreita alcança a mesma ideia subjacente de NIP-4E por um ângulo diferente: [PR #2361](https://github.com/nostr-protocol/nips/pull/2361), de fiatjaf, desacopla chaves de identidade e criptografia dentro de mensagens [NIP-17](/pt/topics/nip-17/) especificamente, aberto desde 1 de junho. Ambos os PRs permanecem sem merge, deixando isso como um canto ativo e disputado do espaço de design. Form* diz que o cliente Drive é experimental com uma atualização em breve.

### Aberta: NIP-DA compartilhamento privado de dados com permissões

[PR #2411](https://github.com/nostr-protocol/nips/pull/2411), de JAFairweather, é um novo rascunho NIP-DA para compartilhamento privado de dados com permissões através de concessões de dados com escopo. Cada usuário mantém um registro criptografado e autoritativo por escopo em relay, e o acesso é concedido entregando privadamente a chave simétrica desse escopo dentro de um gift wrap [NIP-59](/pt/topics/nip-59/), de modo que relay armazenam apenas texto cifrado e nunca sabem quem concedeu acesso a quem; uma revogação é simplesmente uma rotação de chave, sem necessidade de reescrever a cópia de cada consumidor. O autor o posiciona como distinto dos DMs [NIP-17](/pt/topics/nip-17/) (que podem carregar um snapshot de dados mas não atualizações ao vivo ou revogação) e das listas privadas NIP-51 (que não carregam material de chave), e cita duas implementações independentes, uma biblioteca de referência em JavaScript e um CLI em Go sobre go-nostr, testadas cruzadas contra relay.damus.io, nos.lol e relay.primal.net.

### Aberta: kinds de pacotes de stickers 10031 e 30031

[PR #2410](https://github.com/nostr-protocol/nips/pull/2410), de vincenzopalazzo, registra kind 30031 (pacotes de stickers endereçáveis) e kind 10031 (a lista de pacotes de stickers de um usuário) na tabela de Event Kinds, especificados pelo formato "Sonar Stickers" que [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) lança esta semana. Os kinds ficam deliberadamente um espaço acima dos kinds de emoji personalizados [NIP-30](/pt/topics/nip-30/) 30030 e 10030 para que um cliente não confunda um pacote de stickers com um conjunto de emojis; os bytes de imagem de stickers ficam em servidores HTTPS compatíveis com [Blossom](/pt/topics/blossom/), e as referências de stickers enviados carregam um hash em texto plano para que um pacote endereçável editado não mude silenciosamente a aparência de stickers já enviados em mensagens antigas. Um PR companheiro registra os mesmos kinds no projeto separado `registry-of-kinds`.

### Aberta: fixação de mensagens NIP-29 com kind:9010 e kind:39005

[PR #2379](https://github.com/nostr-protocol/nips/pull/2379), de Anderson-Juhasc, adiciona fixação de mensagens a grupos baseados em relay [NIP-29](/pt/topics/nip-29/): kind:9010 `update-pin-list` é um evento de moderação que carrega a lista completa de eventos fixados como tags `e` em ordem de exibição, de modo que um único evento pode fixar, desfixar, reordenar ou limpar o conjunto fixado, e kind:39005 é um espelho gerado pelo relay que expõe a última lista aceita. O design substitui uma abordagem anterior de pares adicionar/remover de [PR #1163](https://github.com/nostr-protocol/nips/pull/1163) após feedback de revisão, e escolhe os números de kind 9010/39005 porque 9009 e 39003 foram reivindicados desde então por `create-invite` e papéis de grupo. Anderson-Juhasc também mantém [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages), cujo [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) é lançado nesta mesma semana.

### Aberta: reestruturação da descoberta de relay NIP-66

[PR #2241](https://github.com/nostr-protocol/nips/pull/2241), de VincenzoImp, é uma reestruturação substancial da descoberta de relay [NIP-66](/pt/topics/nip-66/). Substitui a prosa solta de "Outras tags incluem" por uma seção estruturada de Tags Indexadas, adiciona uma tag `W` espelhando o campo `attributes` do NIP-11 para filtragem de descoberta de relay, adiciona uma tag de label `l` usando namespaces padronizados (`ISO-639-1`, `ISO-3166-1`, `IANA-asn`, `IANA-tz`, `nip66.label.city`), e organiza tags de RTT, SSL/TLS, rede, geográficas, DNS e HTTP em seções dedicadas junto com uma nova tabela de Tipos de Verificação. Também corrige eventos de exemplo quebrados que tinham nomes de campo incorretos, um `kind` faltante e nomes de tipo de verificação inválidos, e fecha o [issue #2171](https://github.com/nostr-protocol/nips/issues/2171). Todas as mudanças mantêm compatibilidade retroativa já que cada tag adicionada é opcional.

---

## NIP Deep Dive: NIP-99 e a extensão de comércio Gamma Markets

[NIP-15](/pt/topics/nip-15/), a especificação original do Marketplace Nostr, é legada neste ponto: modelava um estande de comerciante (kind 30017) com produtos (kind 30018) arquivados embaixo, e os clientes que antes rodavam sobre ela, Shopstr entre eles, migraram desde então para as listas de classificados [NIP-99](/pt/topics/nip-99/) como a especificação ativa. NIP-99 em si é um único evento endereçável, kind 30402 para uma lista ativa ou kind 30403 para um rascunho, sem estande para criar primeiro. Deixa tudo além da lista indefinido: custo de frete, status do pedido, recibos, avaliações, e uma forma de agrupar várias listas sob uma única loja, exatamente as partes de NIP-15 que nunca foram transferidas. [Gamma Markets](/pt/topics/gamma-markets/) preenche essa lacuna, e é a camada de comércio moderna que vale a pena entender hoje.

### A lacuna que NIP-99 deixa aberta

O campo `content` de uma lista NIP-99 carrega uma descrição em Markdown, `price` e `location` ficam diretamente no evento, e tags `t` a tornam pesquisável como conteúdo comum de hashtag. Como é endereçável pela tupla pubkey, kind e tag `d`, um vendedor edita uma lista no lugar publicando uma nova versão com a mesma tag `d`:

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

Essa é a especificação inteira: um anúncio classificado assinado e atualizável. Cada cliente que implementa NIP-99 para e-commerce real, além de um classificado avulso, acabou inventando suas próprias convenções privadas para frete, mensagens de pedido e avaliações. Dois clientes NIP-99 podiam renderizar corretamente uma lista e ainda assim não ter uma forma compartilhada de completar um checkout entre eles.

### Gamma Markets: padronizando o que NIP-99 deixou de fora

Gamma Markets é o nome que um grupo de trabalho de desenvolvedores de marketplaces Nostr, as equipes por trás de Shopstr, Cypher, Plebeian Market e Conduit Market, deram a um conjunto compartilhado de convenções de e-commerce construídas sobre o evento kind 30402 existente de NIP-99. A especificação está linkada no documento canônico de NIP-99 via [PR #1784](https://github.com/nostr-protocol/nips/pull/1784) e mantida em seu próprio repositório, [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec).

Gamma Markets adiciona dois kinds standalone adjacentes às listas. Kind 30405 agrupa múltiplas listas em uma coleção de produtos, referenciando cada uma por uma tag `a` explícita:

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Kind 30406 define uma opção de frete com preços por país e regras opcionais de custo baseadas em peso ou distância:

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

Criação de pedidos, requisições de pagamento, atualizações de status e frete, e recibos de pagamento viajam como mensagens privadas comuns envolvidas com gift-wrap [NIP-17](/pt/topics/nip-17/), divididas em três kinds por papel, e não por reenvolver o transporte: kind 14 carrega comunicação livre entre comprador e comerciante, kind 16 carrega cada transição de estado do pedido (uma tag `type` de 1 a 4 marca criação de pedido, requisição de pagamento, atualização de status ou atualização de frete), e kind 17 carrega o recibo de pagamento do comprador. Uma mensagem de criação de pedido se parece com isso antes do gift-wrapping:

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Avaliar uma compra concluída é um kind endereçável separado, 31555, que aponta para a lista que avalia:

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

Transportar mensagens de pedido sobre NIP-17 significa que um checkout Gamma Markets usa o mesmo transporte de mensagens privadas que os clientes já têm para DMs, em vez de um kind de mensagem de pedido sob medida.

A escolha de design central da especificação é que nada herda em cascata. Uma lista que pertence a uma coleção a referencia explicitamente com uma tag `a` em vez de herdar automaticamente as opções de frete ou a descrição da coleção, e uma opção de frete que uma lista usa é referenciada da mesma forma explícita. Essa é uma reversão deliberada do modelo de estande de NIP-15, onde um produto herdava silenciosamente a moeda e a tabela de frete que seu estande pai definia. A compensação é mais marcação explícita em cada lista, em troca da configuração completa de uma lista ser sempre legível a partir do próprio evento, sem objeto pai para resolver primeiro.

### Onde isso aparece na prática

O trabalho de [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) desta semana se situa no mesmo território de mensagens de pedido que Gamma Markets padroniza: o checkout como convidado com chave efêmera de [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) e a reconstrução da caixa de entrada de pedidos do comerciante de [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) ambos resolvem o problema de estado de pedido comprador/comerciante que as mensagens kind 14, 16 e 17 de Gamma Markets formalizam; Conduit Mono roda seu próprio modelo de estado de pedido ao lado desses kinds, sem adotá-los diretamente. Shopstr, um dos quatro projetos que escreveram a especificação, também manteve sua própria plumbing de comércio em movimento na última semana: [PR #568](https://github.com/shopstr-eng/shopstr/pull/568) extrai a lógica duplicada de gift-wrap NIP-17 em um módulo compartilhado, e [PR #567](https://github.com/shopstr-eng/shopstr/pull/567) leva seu parser de autenticação HTTP [NIP-98](/pt/topics/nip-98/) a cobertura completa de testes, manutenção em exatamente as camadas de mensagens e autenticação das quais um fluxo de pedidos Gamma Markets depende para alcançar o comprador e comerciante com segurança.

NIP-15 perdeu o papel de vitrine ao padronizar um estande e um produto, e depois deixar pagamentos, frete, avaliações e status de pedido como problema do aplicativo. Gamma Markets preenche a maior parte dessa superfície faltante sem tocar a forma de lista única de NIP-99, construindo sobre a pilha de DM existente do Nostr, NIP-17, em vez de inventar uma nova camada de mensagens.

---

Isso é tudo por esta semana. Se você está construindo algo ou tem notícias para compartilhar, entre em contato via DM NIP-17 ou nos encontre no Nostr.
