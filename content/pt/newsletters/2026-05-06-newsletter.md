---
title: 'Nostr Compass #21'
date: 2026-05-06
publishDate: 2026-05-06
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-06-newsletter.md
translationDate: 2026-05-13
---

Bem-vindo ao Nostr Compass, o seu guia semanal sobre Nostr.

**Esta semana:** O Marmot Protocol lança o MDK 0.8.0 com os primeiros primitivos de notificação MIP-05, pacotes de chaves NIP-51 endereçáveis e uma revisão de segurança reforçada. O LaWallet NWC lança v0.10.0, o maior lançamento desde o financiamento OpenSats, trazendo um painel de administração completo, carteira para o utilizador, registo de atividade de ponta a ponta e o novo esquema LightningAddress 1→N e NWCConnection. O Amethyst realiza um sprint de estabilização do Nests com eliminação de falhas de áudio durante a renovação JWT, subscrições de dados de chave com consciência do ciclo de vida, reconexão keep-alive de relay e um indicador animado do participante que está a falar. O ngit lança v2.4.2 e v2.4.3 corrigindo a deteção de servidores GRASP para submissões de PR e a filtragem de eventos de estado multi-remote. O GRAIN lança v0.5.4 com reforço de produção e uma correção silenciosa de perda de dados. O Mostro Core lança v0.10.1 com artefactos de lançamento assinados com PGP. O Clave lança v0.2.0 com suporte a múltiplas contas no iOS.

## Principais histórias

### MDK 0.8.0 adiciona primitivos de notificação MIP-05 e pacotes de chaves endereçáveis

O MDK, a biblioteca central em Rust do protocolo Marmot, lançou v0.8.0 a 4 de maio. Este lançamento inclui os primeiros blocos de construção de notificação MIP-05, move os pacotes de chaves MIP-00 para eventos endereçáveis para que o pacote de chaves de um utilizador possa ser substituído no lugar, melhora a compatibilidade de grupos com versões mistas, expande a cobertura UniFFI para bindings móveis e reforça os caminhos de validação em torno de ações administrativas, commits, armazenamento, limites de encriptação e tratamento de replays. Os primitivos MIP-05 incluem helpers de índice de folha adicionados na PR #235, que fornecem aos clientes downstream informação suficiente para entregar notificações push por destinatário sem revelar a estrutura do grupo. A PR #273 restaura a publicação de mdk-core no crates.io, e a PR #269 expõe o módulo test_util por trás de uma funcionalidade Cargo test-utils para que suites de testes de clientes externos possam partilhar o harness de testes do Marmot.

### LaWallet NWC v0.10.0 lança o monorepo completo e a carteira para utilizador

O LaWallet NWC, a implementação NIP-47 Nostr Wallet Connect da equipa LaWallet, lançou v0.10.0 a 30 de abril. Este é o maior lançamento desde que o projeto recebeu financiamento OpenSats. Inclui o monorepo completo, o painel de administração completo, uma carteira para utilizador, um registo de atividade de ponta a ponta, branding dinâmico e o novo esquema LightningAddress 1→N e NWCConnection. A carteira voltada para o utilizador lançada na PR #191 cobre integração, início, envio/receção, digitalização, moedas, um feed de atividade e uma cache offline.

### Amethyst estabiliza o Nests com keep-alive, resiliência JWT e subscrições de ciclo de vida

O Amethyst, o cliente Android rico em funcionalidades, continuou o trabalho nas salas de áudio NIP-53 Nests com um sprint de estabilização focado nos modos de falha que quebravam chamadas em produção. A correção de falhas de áudio na PR #2733 sobrepõe a nova aquisição de credenciais com o stream ativo durante a renovação JWT. Um novo mecanismo keep-alive na PR #2730 reconecta relays desligados sem necessitar de ação manual do utilizador, e a PR #2728 substitui o KeyDataSourceSubscription legado pelo LifecycleAwareKeyDataSourceSubscription. A PR #2724 adiciona um indicador de anel exterior animado que destaca o participante que está a falar em sessões com múltiplos oradores.

### ngit v2.4.2 e v2.4.3 corrigem deteção de servidores GRASP e eventos de estado multi-remote

O ngit, a ferramenta de linha de comando e plugin git para colaboração NIP-34, lançou v2.4.2 a 28 de abril e v2.4.3 a 1 de maio. O v2.4.2 corrige uma discrepância de normalização de URL onde repo_grasps continha nomes de host normalizados mas a comparação era feita com URLs de clone completos. O v2.4.3 corrige uma ambiguidade de evento de estado que surgiu quando um repositório tem múltiplos remotes nostr:// com o mesmo identificador.

### GRAIN v0.5.4 traz reforço de produção e uma correção silenciosa de perda de dados

O GRAIN, o relay Nostr e biblioteca de cliente baseados em Go, lançou v0.5.4 a 30 de abril. O lançamento consolida seis correções acumuladas desde v0.5.3, incluindo um bug silencioso de perda de dados no arranque rápido Docker que anteriormente descartava eventos quando o contentor reiniciava, e um bug de correção da camada de armazenamento nas leituras de eventos endereçáveis.

### Mostro Core v0.10.1 adiciona artefactos de lançamento assinados com PGP

O Mostro Core, a biblioteca Rust que fornece funcionalidade peer-to-peer para o daemon Mostro, lançou v0.10.1 a 28 de abril. O novo lançamento adiciona artefactos de lançamento assinados com PGP e um fluxo de verificação de lançamento para que os empacotadores downstream possam confirmar a proveniência dos artefactos.

## Lançamentos

### Clave v0.2.0 lança multi-conta no iOS com assinatura NIP-46 (Nostr Connect)

O Clave, a app iOS de assinatura remota NIP-46, lançou v0.2.0 a 5 de maio. A maior atualização introduz suporte a múltiplas contas: o Clave pode agora ter até quatro contas num único dispositivo, com um seletor de um toque e isolamento por conta. A PR #23 adiciona a canalização iOS para multi-conta, e a PR #22 adiciona um campo signer_pubkey à carga APNs para que o dispositivo saiba a que conta pertence um pedido de assinatura remota.

### Wisp lança trabalho de estabilidade v1.0.3 → v1.0.5

O Wisp, o cliente Android, lançou v1.0.3, v1.0.4 e v1.0.5 a 4 de maio com trabalho de estabilidade. A PR #506 adiciona Thumbhash para pré-visualizações de imagens desfocadas enquanto o media completo carrega, e a PR #514 reduz o engasgamento ao mudar de separadores inferiores.

### Amber 6.1.0-pre1 lança correções de layout e estabilidade

O Amber, a app Android de assinatura para NIP-55 e NIP-46, lançou v6.1.0-pre1 com uma passagem de layout no fluxo de conexão de nova app e várias correções de falhas. A PR #416 corrige o layout do ActivityStatsBar e problemas de overflow de texto.

### Routstr Core v0.4.3 melhora pagamento, reembolso e relatórios de utilização

O Routstr Core lançou v0.4.3 como pré-lançamento a 1 de maio com melhorias no tratamento de pagamentos e reembolsos, rastreamento de custos e relatórios de utilização.

### Nostria v3.1.37 a v3.1.41 adiciona marcadores Web e um tema automático

O Nostria, o cliente Nostr multiplataforma, lançou v3.1.37 a v3.1.41 adicionando suporte a marcadores Web NIP-B0, um tema automático que segue as definições do dispositivo e visualização de PDF na app.

### NoorNote v0.8.9 corrige ecrã vazio no primeiro lançamento no desktop

O NoorNote lançou v0.8.9 a 28 de abril corrigindo um bug de ecrã vazio no primeiro lançamento da app desktop.

### Kubo v0.3.4 a v0.4.1 lança plataforma de vídeo Nostr segura para crianças com controlos parentais e curadoria de feed Web of Trust

O Kubo, uma plataforma de vídeo segura para crianças no Nostr, lançou v0.3.4 a v0.4.1 nos dias 4 e 5 de maio. Cada criança recebe um par de chaves Nostr separado e um feed centrado em vídeo onde os pais controlam limites de tempo (15 a 180 minutos diários), janelas de tempo permitidas e visibilidade de ações de publicação.

## Mudanças não lançadas

### Sprout lança Desktop v0.0.4 e v0.0.5 juntamente com autenticação de agente NIP-OA e o sidecar relay de emparelhamento

O Sprout, o cliente Nostr da Block com relay integrado, lançou Desktop v0.0.4 a 5 de maio e v0.0.5 a 6 de maio. A PR #471 conecta a autenticação de agente NIP-OA ao fluxo de adesão NIP-43 do relay para que um agente autónomo possa provar que uma chave pública humana específica autorizou as suas ações. Um novo relay sidecar efémero para emparelhamento de dispositivos NIP-AB chega na PR #467 como sprout-pair-relay.

### nostream adiciona suporte a relay Marmot e reações NIP-25

O nostream, a implementação de relay Node.js, fundiu suporte a relay do Marmot Protocol cobrindo MIPs 00 a 03 na PR #602, suporte a reações NIP-25 na PR #589 e correspondência de prefixo geohash para filtros #g na PR #586.

### strfry adiciona observabilidade por conexão e reduz o teto nofiles

O strfry, o relay Nostr em C++, fundiu 14 PRs direcionados à observabilidade. A PR #218 adiciona observabilidade de saída pendente por conexão e um limite de contrapressão configurável. A PR #224 remove alocações de heap std::function do fanout do monitor por evento.

### Damus substitui GIFs Tenor por um proxy Purple e lança UX de compactação

O Damus fundiu a PR #3737 substituindo a integração de GIF Tenor por um proxy Damus Purple.

### Primal Android melhora Explorar, alertas e o emblema verificado NIP-05

O Primal Android fundiu a PR #1043 corrigindo um emblema verificado NIP-05 que piscava para utilizadores com identificadores _@domínio.

### Alby Hub adiciona pagamentos NWC a partir de conexões de apps

O Alby Hub fundiu a PR #2267 permitindo pagamentos a partir de conexões de apps.

### routstrd-auth: um Routstrd dockerizado para equipas com autenticação NIP-98 e RBAC npub

O routstrd-auth, criado a 27 de abril, é uma variante dockerizada do Routstrd para implementações de equipas multi-utilizador com controlo de acesso baseado em funções npub e autenticação HTTP NIP-98.

### Routstrd integra Hermes para clientes daemon e modo remoto

O Routstrd fundiu a PR #22 adicionando integração com o Hermes Agent para que o ficheiro de configuração do agente seja preenchido com fornecedores de modelos e chaves API que o Routstrd descobre via Nostr.

### whitenoise-rs lança isolamento de base de dados por conta e atualizações de propostas

O whitenoise-rs fundiu a PR #796 movendo tabelas de projeção de mensagens para bases de dados por conta, e a PR #791 adiciona atualizações de propostas para que grupos possam estender funcionalidades com novos tipos de propostas.

### Angor 0.2.21 lança fluxos de app compactos juntamente com reforço do fornecedor de chaves e mudança de rede

O Angor lançou 0.2.21 a 6 de maio com melhorias de desempenho de design móvel, fluxos de app compactos e um fornecedor de chaves seguro.

## Novos projetos rastreados e descobertos

### BitMacro Signer: um bunker NIP-46 auto-hospedável com encriptação de chave do lado do cliente

O BitMacro Signer é uma ferramenta de assinatura Nostr auto-hospedável usando o modelo bunker NIP-46. As chaves são encriptadas no cliente antes do armazenamento para que o servidor nunca tenha o texto simples.

A descoberta de repositórios NIP-34 revelou 26 novos anúncios de repositórios esta semana, dos quais quatro se destacam:

### gnostr: uma implementação git construída diretamente sobre Nostr

O gnostr é uma implementação git construída diretamente sobre Nostr, com os seus próprios comandos de árvore de trabalho como um cliente de controlo de versão nativo do Nostr construído de raiz.

### nostr-archive: uma especificação de arquivo com endereçamento por conteúdo no Nostr e Blossom

O nostr-archive é uma especificação de rascunho e implementação de referência para arquivos com endereçamento por conteúdo no Nostr e Blossom.

### flower-cache: um servidor de cache Blossom local

O flower-cache é um servidor de cache Blossom local, útil para clientes que querem um espelho local quente do conjunto de blobs de um servidor Blossom remoto.

### micro-vpn-ansible: playbooks Ansible para implementação de VPN via NIP-34

O micro-vpn-ansible é uma pequena coleção de playbooks Ansible para implementar uma micro VPN, hospedada como repositório NIP-34.

## Trabalho de protocolo

### Atualizações NIP

- Um mercado de hashrate sem intermediário no Nostr (proposta de rascunho): Rascunho anónimo de NIP argumentando que os atuais participantes do mercado de hashrate são corretores de custódia que fazem KYC aos utilizadores. Propõe um mercado de hashrate P2P em eventos Nostr.
- Curated Feeds: uma alternativa mais simples aos feeds DVM (proposta de rascunho): Argumenta que os DVMs NIP-90 são demasiado pesados para curadoria simples de feeds; propõe eventos endereçáveis leves com listas ordenadas de IDs de eventos.
- Profile Colors: identidade visual determinística (proposta de rascunho): Novo rascunho NIP para derivar cores legíveis determinísticas de uma chave pública Nostr para identidade visual consistente entre clientes.
- NIPs Namecoin-Track: ancoragem de identidade, relays, TLS e reputação (cluster de rascunhos): Um conjunto de NIPs de rascunho movendo peças da pilha Nostr para registos ancorados no Namecoin.

## NIP em profundidade: NIP-34 (git stuff)

O NIP-34 define tipos de eventos para hospedar repositórios git, patches, pull requests, issues e estado de fusão em relays Nostr. Um repositório é anunciado como um evento endereçável de tipo 30617. Os patches usam o tipo 1617 transportando a saída git format-patch. As pull requests usam o tipo 1618. As issues usam o tipo 1621 com conteúdo markdown. Os eventos de estado movem uma thread entre Open (1630), Applied/Merged ou Resolved (1631), Closed (1632) e Draft (1633). A história NIP-34 desta semana é a mesma que o lançamento GitWorkshop v2 da semana passada: o botão de fusão de PR no browser funciona porque os servidores GRASP, o ngit e o esquema de URL clone nostr:// fecham juntos o ciclo numa forge totalmente descentralizada.

## NIP em profundidade: NIP-53 (Live Activities)

O NIP-53 define a superfície de eventos padrão para atividades ao vivo no Nostr: transmissões ao vivo, espaços de reunião persistentes, eventos de conferência agendados, presença de ouvintes e chat ao vivo. Uma transmissão ao vivo é anunciada como um evento endereçável de tipo 30311. O NIP-53 separa a sala persistente do evento agendado realizado dentro dela: um Meeting Space de tipo 30312 define uma sala, e um Conference Event de tipo 30313 representa uma reunião agendada ou em curso nessa sala. A superfície de atividades ao vivo do Nostr é intencionalmente leve: o NIP-53 anuncia a atividade, enquanto outros NIPs tratam de preocupações adjacentes como zaps (NIP-57), objetivos de zap (NIP-75) e gravações de vídeo (NIP-71).

---

Isso é tudo para esta semana. Se estiver a construir algo ou tiver notícias para partilhar, envie-nos uma DM no Nostr ou encontre-nos em nostrcompass.org.
