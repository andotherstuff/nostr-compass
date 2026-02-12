---
title: 'Nostr Compass #9'
date: 2026-02-11
translationOf: /en/newsletters/2026-02-11-newsletter.md
translationDate: 2026-02-12
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** Mostro lança seu primeiro beta público após três anos de desenvolvimento, trazendo negociação P2P de Bitcoin para mobile via Nostr. OpenSats concede sua décima sexta onda de grants Bitcoin, com Minibits Wallet recebendo renovação de grant. **Zapstore alcança o lançamento estável 1.0**, marcando a maturação da loja de apps Android descentralizada. Coracle 0.6.29 adiciona tópicos e comentários em highlights. Igloo Desktop v1.0.3 entrega endurecimento de segurança com assinatura de limiar Frostr. Amber v4.1.2-pre1 migra a arquitetura Flow. Angor alcança v0.2.5 com UI de financiamento renovada e configuração de servidor de imagens NIP-96. NostrPress surge como ferramenta que converte perfis Nostr em blogs estáticos. Antiprimal entrega gateway compatível com padrões que faz bridge do servidor de cache proprietário do Primal a NIPs padrão do Nostr. Primal Android faz merge de 18 PRs expandindo infraestrutura NWC com suporte a carteira dupla, logging de auditoria e o método `lookup_invoice`. diVine entrega feeds de vídeo API-first. O SDK TypeScript do Marmot separa seu app de chat de referência em repositório independente e começa migração a ts-mls v2. O repositório de NIPs faz merge de contagem aproximada HyperLogLog no NIP-45 e extrai tags de identidade do kind 0. Propostas de vitorpamplona começam a sistematicamente reduzir eventos de metadados kind 0. Novas propostas de protocolo incluem Nostr Relay Connect (traversal de NAT) e Nostr Web Tokens (claims web assinados). Os deep dives cobrem a contagem aproximada HyperLogLog do NIP-45 e o protocolo de armazenamento de arquivos HTTP do NIP-96, agora depreciado em favor do Blossom, enquanto projetos navegam a transição entre os dois padrões de mídia.

## Notícias

### Mostro Lança Primeiro Beta Público

[Mostro](https://github.com/MostroP2P/mostro), a exchange peer-to-peer de Bitcoin construída sobre Nostr, lançou seu [app mobile v1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0), o primeiro beta público do projeto após três anos de desenvolvimento. O app permite que usuários negociem Bitcoin diretamente usando Nostr na coordenação de ordens, com Lightning na liquidação e nenhum intermediário custodial.

O lançamento introduz notificações push com confiabilidade em background melhorada no Android, sistema opcional de logging que permite capturar e compartilhar dados de diagnóstico quando surgem problemas, atualizações de relay mais suaves usando inicialização aditiva, e refinamentos de UI da Fase 2 com suporte a internacionalização. O app está disponível na [Zapstore](https://zapstore.dev) e como [download direto do GitHub](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0).

Mostro se junta a Shopstr e Plebeian Market como aplicação de comércio nativa do Nostr, com a distinção de que foca em coordenação de troca fiat-Bitcoin. O [daemon Mostro](https://github.com/MostroP2P/mostro) subjacente lida com correspondência de ordens e resolução de disputas através de relays Nostr.

### Décima Sexta Onda de Grants Bitcoin da OpenSats

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants) anunciou grants a 17 projetos open-source. O destaque relevante ao Nostr: [Minibits Wallet](https://github.com/minibits-cash/minibits_wallet), a carteira Android [Cashu](/pt/topics/cashu/) com suporte a eventos de carteira [NIP-60](/pt/topics/nip-60/) e integração de nutzap, recebeu grant de renovação. Minibits usa eventos Nostr no armazenamento de estado de tokens ecash, tornando backups de carteira portáveis entre dispositivos através de sincronização via relay.

### NostrPress: Perfil Nostr em Blog Estático

[NostrPress](https://github.com/besoeasy/NostrPress) ([blog.besoeasy.com](https://blog.besoeasy.com)) é ferramenta nova que converte perfil Nostr em blog completamente estático implantável em qualquer lugar. Usuários publicam artigos no Nostr através de qualquer cliente, e o NostrPress gera site independente a partir desses eventos, completo com hospedagem local de mídia e feeds RSS.

Construído com templates Nunjucks e JavaScript, o NostrPress produz sites sem lock-in de plataforma. A saída gerada é HTML/CSS puro que pode ser hospedado em qualquer servidor de arquivos estáticos, GitHub Pages, Netlify ou VPS pessoal. A ferramenta se junta a [Npub.pro](https://github.com/nostrband/nostrsite) e [Servus](https://github.com/servus-social/servus) como opções na conversão de conteúdo Nostr em sites tradicionais.

### Antiprimal: Gateway Compatível com Padrões ao Cache do Primal

[antiprimal](https://gitlab.com/soapbox-pub/antiprimal) ([antiprimal.net](https://antiprimal.net)), novo projeto de Alex Gleason e a equipe Soapbox, é gateway WebSocket que faz bridge do servidor de cache proprietário do Primal a mensagens padrão do protocolo Nostr. Primal oferece recursos como estatísticas de eventos, busca de conteúdo e cálculos de Web of Trust através de `wss://cache.primal.net/v1`, mas acessar estes requer formato de mensagem proprietário com campo `cache` não-padrão que aplicações Nostr padrão não conseguem usar. Antiprimal traduz requisições NIP padrão ao formato do Primal e converte as respostas de volta.

O gateway suporta consultas COUNT [NIP-45](/pt/topics/nip-45/) (reações, respostas, reposts, contagens de zap, contagens de seguidores), busca [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md), informações de relay [NIP-11](/pt/topics/nip-11/) e [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) Trusted Assertions com dados pré-computados de Web of Trust do Primal. Bot complementar publica eventos NIP-85 kind 30382 (estatísticas de usuário) e kind 30383 (engajamento de eventos) em relays configuráveis. O projeto é construído com TypeScript no Bun e usa a biblioteca Nostrify. Criado em 6 de fevereiro, tem 53 commits nos primeiros três dias de desenvolvimento e está ao vivo em antiprimal.net.

### Ikaros: Gateway de Mensagens de Agentes de IA com Signal e Nostr

[Ikaros](https://gitlab.com/soapbox-pub/ikaros), novo projeto da equipe Soapbox, é gateway de mensagens que permite agentes de IA se comunicarem através de DMs criptografadas tanto do Signal quanto do Nostr. A bridge usa o [Agent Client Protocol](https://agentclientprotocol.org) (ACP) na conexão de qualquer assistente de codificação IA compatível com ACP a redes de mensagens reais. Três pull requests constituem a construção inicial do projeto nesta semana.

O [PR #1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1) implementa adaptador completo de DM criptografada [NIP-04](/pt/topics/nip-04/) com suporte a envio/recebimento, buffer de resposta com flush explícito na conclusão, formatos de chave privada `nsec` e hex, publicação multi-relay com reconexão automática e assistente de configuração interativo. O adaptador usa nostr-tools v2.23.0 e atualiza o ACP SDK a v0.14.1.

O [PR #2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2) corrige descarte silencioso de mensagens causado por condição de corrida na atualização de sessão: notificações recebidas antes de registro no mapa eram silenciosamente perdidas, e a correção armazena essas notificações em buffer até que o registro seja concluído. O [PR #3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3) adiciona metadados de nome/UUID de usuário e grupo do Signal nas interações com agentes, de modo que o agente de IA saiba com quem está falando e em qual grupo. O projeto abre novo espaço de design: agentes de IA endereçáveis via DMs Nostr que podem ser alcançados do Signal, ou vice-versa.

### Campanha de Redução do Kind 0

vitorpamplona abriu série de PRs nesta semana propondo extração sistemática de dados de eventos kind 0 (metadados de usuário) em kinds de evento dedicados. A campanha aborda problema crescente: eventos kind 0 acumularam campos ao longo do tempo que a maioria dos aplicativos não usa, inflando o tamanho de cada busca de perfil.

O [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) (mergeado) move tags de identidade (tags `i`) do kind 0 a novo kind 10011, já que a adoção dessas tags foi mínima. O [PR #2213](https://github.com/nostr-protocol/nips/pull/2213) propõe mover verificação [NIP-05](/pt/topics/nip-05/) ao kind 10008, o que permitiria que usuários tivessem múltiplos identificadores NIP-05 e possibilitaria filtrar eventos por endereço NIP-05. O [PR #2217](https://github.com/nostr-protocol/nips/pull/2217) propõe extrair endereços Lightning (lud06/lud16) em novo kind, impedindo que todos os usuários de kind 0 carreguem campos relacionados a zap que só importam em aplicações com integração Lightning.

As propostas reacenderam a discussão sobre a questão mais ampla da estrutura do kind 0, incluindo o [PR #1770](https://github.com/nostr-protocol/nips/pull/1770), a proposta de longa data que substitui JSON stringificado no conteúdo do kind 0 por tags estruturadas.

### Suporte a NIP-70 em Relays é Crítico na Segurança de Mensagens Criptografadas

A implementação White Noise do protocolo [Marmot](/pt/topics/marmot/) [identificou lacuna crítica](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html) no suporte de relays ao [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) (Eventos Protegidos) e [NIP-42](/pt/topics/nip-42/) (Autenticação). Testes revelaram que relays públicos importantes incluindo Damus, Primal e nos.lol rejeitam eventos protegidos diretamente com erros `blocked: event marked as protected` em vez de iniciar o desafio de autenticação obrigatório.

Isso quebra recurso de segurança chave: NIP-70 permite exclusão segura de KeyPackages MLS gastos, prevenindo ataques "coletar agora, descriptografar depois". Sem suporte de relay, protocolos de mensagens criptografadas não conseguem proteger usuários contra comprometimento futuro de chaves. White Noise desabilitou NIP-70 por padrão em resposta, mantendo flag opcional com relays compatíveis.

**Chamado à ação de operadores de relay:** Implementem o fluxo completo de autenticação NIP-42. Ao receber eventos protegidos, desafiem os remetentes a provar propriedade e então aceitem escritas validadas. Rejeitar eventos protegidos sem autenticação quebra garantias de segurança do protocolo das quais aplicações de mensagens criptografadas dependem.

## Lançamentos

### Coracle 0.6.29

[Coracle](https://github.com/coracle-social/coracle) ([coracle.social](https://coracle.social)), o cliente web de hodlbod, lançou [0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29). O lançamento adiciona exibição de tópicos e comentários em highlights kind 9802. Novo item de navegação de listas dá acesso rápido a listas curadas pelo usuário a partir da UI principal. Internamente, Coracle atualizou a nova versão do Welshman, a biblioteca Nostr compartilhada que alimenta o gerenciamento de relay e tratamento de eventos do Coracle. A lista padrão de relays foi atualizada, e o rastreamento de erros Glitchtip foi removido do codebase.

### Igloo Desktop v1.0.3

[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), o assinador de limiar baseado em [FROST](/pt/topics/frost/) e aplicação de gerenciamento de chaves, lançou [v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3) com extenso endurecimento de segurança. O lançamento introduz validação IPC, isolamento Electron e verificações de relay com proteção contra SSRF (server-side request forgery). Novo fluxo de onboarding e importação de shares simplifica a distribuição de chaves, o planejamento de relay agora inclui normalização e merge de prioridade, e arquitetura de API Electron baseada em preload melhora a barreira de segurança entre o renderer e o processo principal. Sistema de keep-alive do assinador mantém estabilidade de sessão de assinatura de limiar, e melhorias de UX de recuperação reduzem a fricção de restauração de chaves.

### Amber v4.1.2-pre1

[Amber](https://github.com/greenart7c3/Amber), o assinador de eventos Android, lançou [v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1) corrigindo a exibição ausente de pontuação de confiança de relay introduzida na v4.1.1, resolvendo problemas de parsing JSON em requisições de encrypt/decrypt não-Nostr, e migrando o modelo de conta de LiveData a Flow com gerenciamento de estado mais previsível. O lançamento muda segredos do bunker a UUIDs completos e atualiza ao Gradle plugin 9.

### Mostro Mobile v1.1.0 e Daemon v0.16.1

Veja a [seção de Notícias acima](#mostro-lança-primeiro-beta-público) com cobertura completa do lançamento mobile. No lado servidor, o [daemon Mostro](https://github.com/MostroP2P/mostro) lançou [v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1), adicionando publicação automática de metadados NIP-01 kind 0 na inicialização ([PR #575](https://github.com/MostroP2P/mostro/pull/575)), de modo que o daemon agora anuncia sua identidade na rede quando fica online. A documentação de cálculo de taxas de desenvolvimento foi igualmente corrigida ([PR #571](https://github.com/MostroP2P/mostro/pull/571)).

### Angor v0.2.5

[Angor](https://github.com/block-core/angor) ([angor.io](https://angor.io)), o protocolo descentralizado de financiamento P2P construído sobre Bitcoin e Nostr, lançou [v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5) com três PRs mergeados. O [PR #649](https://github.com/block-core/angor/pull/649) redesenha a seção de gerenciamento de Fundos (V2), substituindo o layout anterior por nova interface que rastreia UTXOs individuais e posições de investimento. O [PR #651](https://github.com/block-core/angor/pull/651) reformula o InvoiceView com estilos de botão atualizados, diálogos fecháveis, novo comando "Copiar Endereço", suporte a cancelamento no monitoramento de endereço e tratamento melhorado de fluxo de investimento. O [PR #652](https://github.com/block-core/angor/pull/652) adiciona servidores de imagem [NIP-96](/pt/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) configuráveis nas configurações, permitindo que usuários escolham qual endpoint de upload de mídia lida com suas imagens de projeto e documentação. A versão [v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4) foi lançada na semana anterior.

### Ridestr v0.2.2 e v0.2.3

[Ridestr](https://github.com/variablefate/ridestr), a plataforma descentralizada de compartilhamento de caronas [coberta na semana passada](/pt/newsletters/2026-02-04-newsletter/#ridestr-v020-roadflare-release), continuou iteração rápida com [v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2) (Bridge Payment Hotfix) e [v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3) após o v0.2.0 "RoadFlare Release". O hotfix v0.2.2 corrige bug onde pagamentos bridge [Cashu](/pt/topics/cashu/) cross-mint estavam auto-cancelando corridas enquanto o pagamento ainda estava processando ou eventualmente teria sucesso, prevenindo cancelamento prematuro de corridas em liquidações mais lentas. Corrige igualmente flickering de UI e hitboxes de toque quebradas no botão "minha localização". A versão v0.2.3 entrega correções de bugs adicionais. Ambos os lançamentos incluem APKs separados, Ridestr (app do passageiro) e Drivestr (app do motorista).

### Nostr PHP 1.9.4

[Nostr PHP](https://github.com/nostrver-se/nostr-php) ([nostr-php.dev](https://nostr-php.dev)), a biblioteca helper PHP do protocolo Nostr, lançou [1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4) adicionando propriedade `timeout` configurável à classe de requisição ([PR #106](https://github.com/nostrver-se/nostr-php/pull/106)). Isso permite que desenvolvedores definam durações de timeout personalizadas em conexões de relay e requisições de mensagem, prevenindo travamentos indefinidos quando relay não responde ou demora a responder.

### Zapstore v1.0.0

[Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0) ([zapstore.dev](https://zapstore.dev)), a loja de apps Android sem permissão construída sobre Nostr, **alcançou seu marco de lançamento estável 1.0** nesta semana após meses de release candidates.

O lançamento 1.0 inclui melhorias críticas de estabilidade: tratamento de estado do botão de instalação que garante que Excluir apareça imediatamente após a instalação ser concluída, mensagens de erro amigáveis com detalhes técnicos expansíveis, e botão "Reportar problema" que envia DMs criptografadas via Nostr usando chaves efêmeras. Entrega ainda nova tela de atualizações com polling e rastreamento em lote, melhor watchdog de download em transferências travadas, limites dinâmicos de downloads concorrentes baseados em desempenho do dispositivo, sincronização mais frequente de pacotes instalados e lógica de comparação de versão aprimorada. A equipe corrigiu problema crítico do flutter_secure_storage e melhorou o tratamento de casos extremos do gerenciador de pacotes.

O marco representa a maturação da primeira plataforma dedicada de distribuição de apps do Nostr, permitindo que desenvolvedores publiquem aplicações Android diretamente a usuários sem gatekeeping de loja de apps centralizada.

### ZSP v0.3.1

[ZSP](https://github.com/zapstore/zsp), a ferramenta CLI Go da equipe [Zapstore](https://github.com/zapstore/zapstore) que substitui as ferramentas de publicação anteriores do Zapstore na assinatura e upload de apps Android a relays Nostr, lançou [v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1). ZSP lida com aquisição de APK do GitHub, GitLab, Codeberg, F-Droid ou arquivos locais, depois analisa metadados, assina eventos Nostr (via chave privada, bunker [NIP-46](/pt/topics/nip-46/) ou extensão de navegador [NIP-07](/pt/topics/nip-07/)), e faz upload de artefatos a servidores [Blossom](/pt/topics/blossom/). A versão adiciona modo offline completo na vinculação de keystore sem conexão de rede, headers `Content-Digest` em uploads Blossom em conformidade com o protocolo, detecção corrigida de APK arm64-v8a de repositórios F-Droid, correções de parâmetros trailing de query do GitLab, e suporte completo a arquivo `.env` na configuração.

### Damus iOS 1.17

[Damus](https://github.com/damus-io/damus), o cliente iOS Nostr, atualizou a versão 1.17 ([PR #3606](https://github.com/damus-io/damus/pull/3606)). O lançamento corrige problema no RelayPool onde conexões fechavam após liberação de lease efêmero ([PR #3605](https://github.com/damus-io/damus/pull/3605)), o que podia causar queda inesperada de subscrições. Resolve ainda bug onde a timeline de favoritos não exibia eventos ao alternar entre abas ([PR #3603](https://github.com/damus-io/damus/pull/3603)).

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak), o canivete suíço Nostr CLI, lançou [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) com três correções de estabilidade: prevenindo panic quando tags de desafio AUTH são nil ou curtas demais, verificando erros de dateparser antes de usar o valor analisado, e lidando com URLs de mint Cashu que não possuem separador `://`.

### Mi: Relay Local no Navegador

[Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git) ([mi.shakespeare.wtf](https://mi.shakespeare.wtf)), novo MiniApp do [Shakespeare](https://shakespeare.wtf), é relay local no navegador que arquiva eventos Nostr do usuário em IndexedDB. Mi busca perfis (kind 0), listas de contatos (kind 3), listas de relay (kind 10002) e eventos de carteira de relays conectados e os armazena localmente, dando aos usuários acesso offline aos seus próprios dados. Construído com React e nostr-tools 2.15.0.

### Agora v1.0.2

[Agora](https://gitlab.com/soapbox-pub/agora) ([agora.spot](https://agora.spot)), plataforma descentralizada de ativismo e arrecadação de fundos da equipe Soapbox, lançou [v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2) com APK Android disponível em instalação direta. Esta é a primeira menção do Agora no Compass, que foi lançado em 17 de janeiro com declaração de missão: "Junte-se ao movimento global pela liberdade. Envie apoio a ativistas no campo internacionalmente e participe de ações locais."

A plataforma é centrada em mapa-múndi onde usuários navegam por país, criam "ações" geolocalizadas (protestos, campanhas, organização comunitária) e as discutem através de comentários em thread. Todo o conteúdo se propaga através de relays Nostr, de modo que nenhum servidor central pode ser derrubado ao silenciar a coordenação. Agora suporta múltiplos idiomas com paridade de tradução obrigatória via CI, integra servidores de mídia [Blossom](/pt/topics/blossom/) em uploads, e inclui busca, navegação por hashtag com alternância global/regional, perfis de usuário e sistemas de reação. O lançamento v1.0.2 é a build Android atual, disponível como download direto de APK.

### xonos v0.1.6

[xonos](https://codeberg.org/xonos/xonos), o cliente Nostr 3D experimental construído com o motor de jogo Bevy, lançou [v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6). xonos renderiza eventos Nostr em ambiente espacial 3D com capacidades de text-to-speech, explorando como dados de protocolos sociais podem funcionar fora de interfaces 2D convencionais.

## Atualizações de Projetos

### Primal Android Expande Infraestrutura NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) fez merge de 18 PRs nesta semana, continuando a construção NWC [iniciada na semana passada](/pt/newsletters/2026-02-04-newsletter/#primal-android-entrega-criptografia-nwc). O [PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883) adiciona suporte a conexões NWC em ambas as carteiras (Spark e externa), e o [PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879) implementa o método NWC `lookup_invoice` na verificação de status de pagamento.

O [PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880) adiciona logging de auditoria de requisição-resposta NWC na depuração de interações de carteira. O [PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877) traz suporte multi-conta ao `PrimalNwcService`, permitindo que usuários com múltiplos perfis mantenham conexões de carteira separadas. O [PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882) implementa limpeza periódica de reservas de orçamento expiradas, prevenindo que reservas de pagamento obsoletas bloqueiem operações de carteira.

Trabalho de UI inclui redesign de tela de upgrade de carteira ([PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)), FAQ de upgrade de carteira ([PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)), configuração de endereço Lightning durante onboarding ([PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)) e correção de transações de zap aparecendo como pagamentos regulares em tipos não-Lightning ([PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887)).

### diVine Entrega Feeds de Vídeo API-First

[diVine](https://github.com/divinevideo/divine-mobile), o cliente de vídeos curtos, fez merge de 19 PRs nesta semana, movendo a arquitetura API-first. O [PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468) introduz feeds de vídeo API-first, e o [PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466) adiciona endpoints de API de trending, recentes e home. O [PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433) indexa controladores de vídeo específicos na renderização eficiente de feeds.

Tratamento de perfil melhorou com o [PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440) implementando padrão cache-plus-fresh na visualização de outros perfis, reduzindo tempos de carregamento enquanto garante atualização dos dados. A equipe entregou correções de notificação ([PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)), refatoração de fluxo de comentários ([PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)) e swipe de abas na tela de Notificações ([PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388)).

### White Noise: Unificação de Keyring e Busca de Usuário

O backend [White Noise](https://github.com/marmot-protocol/whitenoise-rs) do protocolo [Marmot](/pt/topics/marmot/) fez merge de 4 PRs nesta semana. Dois PRs melhoraram tratamento de keyring: o [PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468) torna o identificador de serviço de keyring configurável via `WhitenoiseConfig`, e o [PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475) unifica a implementação em crate única `keyring-core` com stores nativos de plataforma, substituindo código fragmentado específico de plataforma. Separadamente, o [PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470) adiciona funcionalidade de busca de usuário.

### Marmot TS Extrai App de Chat de Referência

O SDK TypeScript do [Marmot](/pt/topics/marmot/) ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) fez merge do [PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40), removendo a aplicação de chat de referência embutida e separando-a em repositório independente: [marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat). O novo repositório, criado em 6 de fevereiro, é implementação de referência do SDK TypeScript do Marmot com seu próprio pipeline de CI, visualização de chat com abas e sistema de build independente. A separação permite que o SDK foque em questões de biblioteca enquanto o app de chat itera em UX independentemente.

PR aberto ([#41](https://github.com/marmot-protocol/marmot-ts/pull/41)) migra o marmot-ts a ts-mls v2.0.0, trazendo API redesenhada com objetos de contexto unificados, novos utilitários de tratamento de mensagem (criação de evento, leitura, desserialização), helpers de metadados de key package e suporte a eventos de exclusão.

### Atualizações do Alby Hub

[Alby Hub](https://github.com/getAlby/hub) fez merge de 5 PRs nesta semana. O [PR #2049](https://github.com/getAlby/hub/pull/2049) adiciona CLI Alby à interface da loja de apps. O [PR #2033](https://github.com/getAlby/hub/pull/2033) corrige tratamento de dados de zap inválidos na lista de transações, e o [PR #2046](https://github.com/getAlby/hub/pull/2046) remove o método `ListTransactions` não utilizado da interface LNClient.

### Notedeck Entrega Dashboard e Agentium

[Notedeck](https://github.com/damus-io/notedeck), o cliente Nostr cross-platform da Damus, fez merge de 6 PRs nesta semana. O [PR #1247](https://github.com/damus-io/notedeck/pull/1247) adiciona app de dashboard inicial. O [PR #1293](https://github.com/damus-io/notedeck/pull/1293) introduz Agentium, ambiente de desenvolvimento multi-agente que transforma o assistente de IA Dave em sistema com modos de IA duais e gerenciamento de agentes baseado em cenas. O [PR #1276](https://github.com/damus-io/notedeck/pull/1276) adiciona compositor de mensagem multilinha com keybindings estilo Signal, e o [PR #1278](https://github.com/damus-io/notedeck/pull/1278) entrega melhorias de desempenho de mídia. PRs abertos de destaque incluem [infraestrutura outbox](https://github.com/damus-io/notedeck/pull/1288) e [planejamento de Git App](https://github.com/damus-io/notedeck/pull/1289) [NIP-34](/pt/topics/nip-34/).

### Agora Entrega Grande Reformulação de UI

[Agora](https://gitlab.com/soapbox-pub/agora) fez merge de 7 PRs nesta semana junto com seu lançamento v1.0.2. O [PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106) é o maior, fechando 11 tarefas de UI em configurações, edição de perfil, interações de mapa, resultados de busca, filtragem de comentários e gerenciamento de servidor Blossom. O merge desabilitou botões de reação de usuários não autenticados (que antes recebiam falhas silenciosas ao tentar reagir a posts no mapa), corrigiu panning de mapa na date-line e adicionou texto em negrito nos resultados de busca.

O [PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108) adiciona contagem de comentários sob posts de feed e em páginas de thread. O [PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107) traz retry automático em falhas de carregamento de eventos com botão de reload explícito quando retries se esgotam. O [PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104) muda navegação de hashtag ao escopo global por padrão, já que o escopo anterior por país frequentemente retornava zero resultados.

O [PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109) adiciona etapa de CI que verifica paridade de tradução em todos os idiomas, falhando a build se qualquer chave estiver sem valor. O [PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110) recorta notas grandes em feeds ao preservar ritmo de scroll, e o [PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111) corrige problema de zoom em iOS mobile ao comentar em ações causado por tamanhos de fonte pequenos.

### Clawstr Entrega CLI e Botões de Lightning Zap

[Clawstr](https://gitlab.com/soapbox-pub/clawstr), a plataforma inspirada no Reddit onde agentes de IA criam e gerenciam comunidades no Nostr, fez merge de 3 PRs nesta semana. O [PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11) substitui todos os comandos nak manuais nas definições de habilidades do agente de IA pelo novo pacote `@clawstr/cli` (`npx -y @clawstr/cli@latest`), removendo construção manual de eventos JSON em favor de comandos CLI e adicionando operações de carteira (init, balance, zap, npc) e busca de texto completo [NIP-50](/pt/topics/nip-50/).

O [PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13) adiciona página de documentação "For Humans" e componente `ProfileZapDialog`. O botão de zap aparece em páginas de perfil quando usuário tem endereço Lightning configurado e funciona sem login, usando LNURL-pay diretamente com valores pré-definidos de sats e exibição de QR code. O [PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12) documenta o comando `wallet sync`, explicando como pagamentos em endereços Lightning são retidos pelo NPC até que agentes explicitamente sincronizem suas carteiras.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado:**

- **[NIP-45: Resposta HyperLogLog de Relay](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45 (Contagem de Eventos)](/pt/topics/nip-45/) agora suporta contagem aproximada HyperLogLog (HLL). Relays podem retornar valores de registros HLL de 256 bytes junto com respostas COUNT. Ao fazer merge desses registros de múltiplos relays, aplicações computam cardinalidade aproximada sem baixar conjuntos completos de eventos. O caso de uso principal são contagens de seguidores e reações sem depender de relay único como fonte autoritativa. Até dois eventos de reação consomem mais largura de banda que o payload HLL de 256 bytes. Aplicações podem aplicar correções HyperLogLog++ em cardinalidades pequenas.

- **[NIP-39: Tags de Identidade Movidas do Kind 0](https://github.com/nostr-protocol/nips/pull/2216)** - As tags de claim de identidade [NIP-39](/pt/topics/nip-39/) (tags `i`) foram extraídas de eventos de metadados kind 0 a novo kind 10011 dedicado. A razão: quase nenhum cliente suporta essas tags, que adicionam tamanho a cada busca de kind 0 sem fornecer valor. Primeiro de série de PRs de extração do kind 0 de vitorpamplona (veja [seção de Notícias](#campanha-de-redução-do-kind-0)).

**PRs Abertos e Discussões:**

- **[NIP-XX: Nostr Relay Connect (NRC)](https://github.com/nostr-protocol/nips/pull/2214)** - woikos propõe protocolo de acesso a relays Nostr através de tunelamento criptografado via relay rendezvous público. O mecanismo permite acesso a relays atrás de NAT ou firewalls, incluindo relays pessoais rodando em servidores domésticos ou dispositivos móveis. O tunelamento usa eventos kind 24891/24892 com criptografia [NIP-44](/pt/topics/nip-44/) através de relay rendezvous que não pode descriptografar o tráfego. Aplicação prática: qualquer cliente Nostr pode expor armazenamento local (IndexedDB, SQLite) como endpoint de relay na sincronização entre dispositivos. Semânticas padrão NIP-01 (REQ, EVENT, CLOSE, COUNT) passam pelo túnel de forma transparente. Existem referências em Go (ORLY Relay) e TypeScript (Smesh).

- **[Nostr Web Tokens (NWT)](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btc propõe Nostr Web Tokens, formato de evento Nostr que transmite claims assinados entre partes web, inspirado em JSON Web Tokens (JWTs). NWT pode representar tanto [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (HTTP Auth) quanto [eventos de autorização Blossom](/pt/topics/blossom/), dando flexibilidade em como e por quanto tempo tokens permanecem válidos. Biblioteca de referência em Go está disponível. Explicação em [vídeo](https://github.com/pippellia-btc/nostr-web-tokens) e [comparação detalhada](https://github.com/pippellia-btc/nostr-web-tokens#comparisons) com NIP-98 e Blossom Auth estão linkadas no PR.

- **[Simplificação do NIP-47](https://github.com/nostr-protocol/nips/pull/2210)** - rolznz propõe remover os métodos `multi_` do [NIP-47 (Nostr Wallet Connect)](/pt/topics/nip-47/), que eram complexos de implementar e não ganharam adoção. O PR reduz duplicação em tratamento de criptografia e compatibilidade retroativa, limpando a spec após a [adição de hold invoice da semana passada](/pt/newsletters/2026-02-04-newsletter/#atualizações-de-nips).

- **[NIP-05: Mover ao Kind de Evento Próprio](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplona propõe mover verificação NIP-05 do kind 0 ao novo kind 10008, permitindo múltiplos identificadores NIP-05 por usuário e filtragem por endereço NIP-05. Parte da campanha de redução do kind 0.

- **[NIP-57: Endereços Lightning do Kind 0](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplona propõe extrair lud06/lud16 (endereços Lightning) do kind 0 em kind de evento dedicado conforme [NIP-57](/pt/topics/nip-57/), continuando o esforço de redução do kind 0.

- **[Hiperpersonalização de Perfil](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjaf propõe capacidades estendidas de personalização de perfil além do que o kind 0 atualmente suporta.

## Deep Dive de NIP: NIP-45 (Contagem de Eventos) e HyperLogLog

[NIP-45](/pt/topics/nip-45/) ([spec](https://github.com/nostr-protocol/nips/blob/master/45.md)) define como aplicações podem pedir a relays a contagem de eventos que correspondem a filtro sem transferir os eventos em si. O merge do [suporte a HyperLogLog](https://github.com/nostr-protocol/nips/pull/1561) nesta semana adiciona estrutura de dados probabilística que resolve problema fundamental: como contar coisas em múltiplos relays independentes.

**O Problema:**

Contar eventos em relay único é simples: envie requisição COUNT, receba número de volta. Contar pela rede é mais difícil. Se o relay A reporta 50 reações e o relay B reporta 40, o total não é 90 porque muitos eventos existem em ambos os relays. Baixar todos os eventos e deduplicar seria a alternativa, mas aplicações não conseguem fazer isso em escala.

**HyperLogLog:**

HyperLogLog (HLL) é algoritmo probabilístico que estima o número de elementos distintos em conjunto usando quantidade fixa de memória. A versão do NIP-45 usa 256 registros de um byte cada, consumindo exatamente 256 bytes independente de quantos eventos são contados. O algoritmo funciona examinando a representação binária de cada ID de evento e rastreando a posição dos zeros iniciais. Eventos cujos IDs começam com muitos zeros são estatisticamente raros, e sua ocorrência indica conjunto grande.

**Como Funciona no NIP-45:**

Relay respondendo a requisição COUNT pode incluir campo `hll` contendo valores de registro codificados em base64:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

A aplicação coleta valores HLL de múltiplos relays e faz merge deles tomando o valor máximo em cada posição de registro. O HLL mergeado representa a união de todos os conjuntos de eventos entre relays, tratando deduplicação automaticamente. A estimativa final de cardinalidade é computada a partir dos registros mergeados.

**Precisão:**

Com 256 registros, o erro padrão é aproximadamente 5,2%. Contagem verdadeira de 1.000 tipicamente produz estimativa entre 948 e 1.052. Em contagens maiores, o erro relativo permanece constante: contagem verdadeira de 100.000 será estimada em aproximadamente 94.800-105.200. Correções HyperLogLog++ melhoram a precisão em cardinalidades pequenas (abaixo de ~200), onde o algoritmo básico tende a superestimar.

**Por Que Importa:**

Métricas sociais (contagens de seguidores, reações, reposts) são recurso central de aplicações de mídia social. A alternativa ao HLL é consultar relay único "confiável" (centralizando a contagem) ou baixar todos os eventos de todos os relays (desperdiçando largura de banda). HLL permite obter boa contagem aproximada de múltiplos relays com overhead total de 256 bytes por relay, independente da contagem real. Até dois eventos de reação consomem mais largura de banda que payload HLL completo.

A spec fixa o número de registros em 256 por interoperabilidade. Todos os relays produzem valores HLL que podem ser mergeados, independente de qual software de relay executam. Essa padronização permite que aplicações implementem suporte HLL uma vez e se beneficiem de cada relay que o suporta.

**Status Atual:**

O PR foi aberto por fiatjaf e esteve em discussão por vários meses antes de ser mergeado nesta semana. Relays precisarão adicionar computação HLL aos seus handlers COUNT. Aplicações precisarão adicionar merge HLL à sua lógica de agregação de contagem.

## Deep Dive de NIP: NIP-96 (Armazenamento de Arquivos HTTP) e a Transição ao Blossom

[NIP-96](/pt/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) definiu como aplicações Nostr fazem upload, download e gerenciam arquivos em servidores de mídia HTTP. Agora marcado como "não recomendado" em favor do [Blossom](/pt/topics/blossom/) (hospedagem de mídia baseada em BUD), o NIP-96 permanece relevante nesta semana porque Angor v0.2.5 [adicionou configuração de servidor NIP-96](#angor-v025) e ZSP v0.3.1 [faz upload a servidores Blossom](#zsp-v031), ilustrando transição de protocolo em andamento.

**Como o NIP-96 Funciona:**

A aplicação descobre as capacidades de servidor de arquivos buscando `/.well-known/nostr/nip96.json`, que retorna a URL da API, tipos de conteúdo suportados, limites de tamanho e transformações de mídia disponíveis:

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

O upload consiste em POST `multipart/form-data` à URL da API com header de autorização [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (evento Nostr assinado provando a identidade de quem faz o upload). O servidor retorna estrutura de metadados de arquivo [NIP-94](/pt/topics/nip-94/) contendo a URL do arquivo, hashes SHA-256 originais e transformados, tipo MIME e dimensões:

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

Downloads usam requisições GET a `<api_url>/<sha256-hash>`, com parâmetros de query opcionais em transformações do lado do servidor como redimensionamento de imagem. Exclusão usa DELETE com auth NIP-98, e somente quem fez o upload original pode excluir seus arquivos. Endpoint de listagem de arquivos retorna resultados paginados dos uploads de dado usuário.

Usuários publicam eventos kind 10096 declarando seus servidores de upload preferidos, permitindo que aplicações selecionem automaticamente o servidor correto sem configuração manual.

**Por Que Foi Depreciado:**

NIP-96 vinculava URLs de arquivo a servidores específicos. Se `files.example.com` caísse, toda nota Nostr referenciando as URLs daquele servidor perdia sua mídia. O servidor era o endereço, e o endereço era frágil.

[Blossom](/pt/topics/blossom/) (Blobs Stored Simply on Mediaservers) inverte isso tornando o hash SHA-256 do conteúdo do arquivo o identificador canônico. URL Blossom se parece com `https://blossom.example/<sha256>.png`, mas qualquer servidor Blossom hospedando o mesmo arquivo o serve no mesmo caminho de hash. Se servidor desaparece, a aplicação consulta outro servidor pelo mesmo hash. Endereçamento por conteúdo torna os dados portáveis entre servidores por padrão.

Blossom simplifica a API. NIP-96 usava uploads multipart form com respostas JSON, políticas de transformação e endpoint de descoberta. Blossom usa PUT simples em uploads, GET em downloads e eventos Nostr assinados (não headers HTTP) na autorização. A especificação do Blossom é dividida em documentos modulares: BUD-01 cobre protocolo de servidor, autorização e recuperação, BUD-02 cobre upload de blob, BUD-03 cobre servidores de usuários, e BUD-04 cobre espelhamento entre servidores.

A depreciação aconteceu em setembro de 2025 via [PR #2047](https://github.com/nostr-protocol/nips/pull/2047), que marcou NIP-96 como "não recomendado" no índice de NIPs.

**A Transição na Prática:**

Servidores como nostr.build e void.cat suportavam NIP-96 e adicionaram ou migraram a endpoints Blossom. As aplicações estão em vários estágios: o lançamento v0.2.5 do Angor adicionou configuração de servidor NIP-96 em imagens de projeto, enquanto o lançamento v0.3.1 do ZSP faz upload de artefatos exclusivamente a servidores Blossom com headers `Content-Digest` em conformidade com o protocolo. Amethyst e Primal suportam uploads Blossom. A coexistência provavelmente continuará até que os softwares NIP-96 restantes completem sua migração.

**O Que Permanece:**

Eventos de preferência de servidor kind 10096 continuam úteis na seleção de servidor Blossom. Metadados de arquivo NIP-94 (eventos kind 1063) ainda descrevem propriedades de arquivo independente de qual protocolo de upload os criou. O hashing SHA-256 que NIP-96 usava em URLs de download se tornou a base do endereçamento por conteúdo do Blossom. O design do NIP-96 informou o que o Blossom simplificou: a lição foi que hospedagem de mídia em rede descentralizada requer armazenamento endereçado por conteúdo ao nível da resistência à censura da camada de relay.

---

É isso por esta semana. Compartilhe notícias, sugira cobertura de projeto ou envie feedback via <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">DM NIP-17</a>, ou nos encontre no Nostr.
