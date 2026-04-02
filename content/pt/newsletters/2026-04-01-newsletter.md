---
title: 'Nostr Compass #16'
date: 2026-04-01
translationOf: /en/newsletters/2026-04-01-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) lança [v1.07.0](#amethyst-lança-notas-fixadas-gerenciamento-de-relay-e-request-to-vanish) com notas fixadas, gerenciamento de relay via [NIP-86](/pt/topics/nip-86/) e suporte a [NIP-62](/pt/topics/nip-62/) Request to Vanish. [NIP-5A](#nip-5a-é-mergeado-trazendo-sites-estáticos-para-o-nostr) (Static Websites) é mergeado no repositório de NIPs, definindo como hospedar sites sob pares de chaves Nostr usando armazenamento [Blossom](/pt/topics/blossom/). [Flotilla](https://gitea.coracle.social/coracle/flotilla) lança [v1.7.0](#flotilla-v170-adiciona-salas-de-voz-e-login-por-email) com salas de voz, login com email e senha e DMs com proof-of-work. [White Noise](https://github.com/marmot-protocol/whitenoise) corrige churn de relays na [v2026.3.23](#white-noise-corrige-churn-de-relays-e-expande-controles-do-cliente), [nospeak](https://github.com/psic4t/nospeak) lança sua [1.0.0](#nospeak-é-lançado-como-um-mensageiro-privado-10) como mensageiro criptografado sem cadastro. [Nymchat](https://github.com/Spl0itable/NYM) [adota Marmot](#nymchat-lança-chats-de-grupo-impulsionados-por-marmot) para chats de grupo criptografados com MLS com fallback para NIP-17. [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) chega à [v1.0.0](#calendar-by-form-v100) com listas privadas de calendário e importação ICS, [Amber](https://github.com/greenart7c3/Amber) adiciona [recuperação por mnemônica e whitelist de relay auth NIP-42](#amber-v502-até-v504), e a [spec Marmot](#marmot-move-keypackages-para-eventos-endereçáveis-e-reforça-push-notifications) move KeyPackages para eventos endereçáveis enquanto reforça o formato de push notifications MIP-05.

## Notícias

### Amethyst lança notas fixadas, gerenciamento de relay e Request to Vanish

[Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android mantido por vitorpamplona, lançou seis releases em três dias, da [v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) até a [v1.07.5](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.5). O conjunto principal de recursos cobre seis superfícies de protocolo: notas fixadas, uma tela dedicada de feed de enquetes, suporte a [NIP-62](/pt/topics/nip-62/) (Request to Vanish) para solicitar exclusão completa de eventos dos relays, [NIP-86](/pt/topics/nip-86/) (Relay Management API) de dentro do cliente, avaliações [NIP-66](/pt/topics/nip-66/) (Relay Discovery and Liveness Monitoring) na tela de informações de relay, e exibição de informações de membros [NIP-43](/pt/topics/nip-43/) (Relay Access Metadata and Requests).

[NIP-86](/pt/topics/nip-86/) define uma interface JSON-RPC para operadores de relay, permitindo que clientes enviem comandos administrativos como banir pubkeys, permitir pubkeys e listar usuários banidos por uma API padronizada. O Amethyst agora expõe isso diretamente em sua UI de gerenciamento de relay, para que usuários que rodam seus próprios relays possam administrá-los a partir do mesmo cliente que usam para postar. O [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) substitui o antigo diálogo de entrada em hex para pubkeys de ban e allow por um diálogo interativo de busca de usuários.

A v1.07.2 adicionou uploads pelo teclado de GIF e corrigiu uma regressão de assinatura em que respostas de rejeição do Amber estavam sendo interpretadas incorretamente porque versões antigas do Amber retornavam uma string vazia para o campo `rejected` ([PR #2042](https://github.com/vitorpamplona/amethyst/pull/2042)). A v1.07.5 corrige um crash ao fazer upload de imagem. As releases [v1.06.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.2) e [v1.06.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.3), mais cedo na mesma semana, adicionaram um seletor de tipo de enquete para escolha única versus múltipla, drag-to-seek em barras de progresso de vídeo e melhorias em postagem anônima.

### NIP-5A é mergeado, trazendo sites estáticos para o Nostr

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) (Static Websites) foi mergeado via [PR #1538](https://github.com/nostr-protocol/nips/pull/1538), definindo como hospedar sites estáticos sob pares de chaves Nostr. A spec usa dois kinds de evento: kind `15128` para um site raiz, um por pubkey, e kind `35128` para sites nomeados identificados por uma tag `d`. Cada manifesto mapeia caminhos de URL para hashes SHA256, com tags opcionais `server` apontando para hosts de armazenamento [Blossom](/pt/topics/blossom/) onde os arquivos reais vivem.

O modelo de hospedagem funciona assim: o autor de um site constrói um site estático, faz upload dos arquivos para um ou mais servidores Blossom e então publica um evento de manifesto assinado que mapeia caminhos para hashes de conteúdo. Um servidor host recebe requisições web, resolve a pubkey do autor a partir do subdomínio, busca o manifesto na lista de relays [NIP-65](/pt/topics/nip-65/) do autor e serve os arquivos baixando os blobs correspondentes do Blossom. O site permanece sob controle do autor porque apenas aquela chave pode assinar um manifesto atualizado. O servidor host é substituível porque qualquer servidor que entenda NIP-5A pode servir o mesmo site a partir do mesmo manifesto.

A spec se apoia em infraestrutura que já existe. [nsite](https://github.com/lez/nsite), a implementação de referência do host NIP-5A construída por lez, e [nsite-manager](https://github.com/hzrd149/nsite-manager), a UI de gerenciamento do hzrd149, já estavam em funcionamento antes do merge do NIP. O merge torna oficiais os kinds de evento e as regras de resolução de URL, dando às segundas e terceiras implementações um alvo estável.

### White Noise corrige churn de relays e expande controles do cliente

[White Noise](https://github.com/marmot-protocol/whitenoise), o mensageiro privado construído sobre o protocolo [Marmot](/pt/topics/marmot/), lançou [v2026.3.23](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.3.23) em 25 de março. O trabalho principal é estabilidade de relay. O login não espera mais que toda publicação de lista de relays termine antes de avançar, porque a publicação agora usa lógica de quórum e tenta o restante em background. Fetches e publishes pontuais usam sessões efêmeras com escopo de relay em vez de permanecer no pool de longa duração, sessões restauradas recuperam seu caminho de refresh de grupo após o startup, e o app agora expõe diagnósticos de relay e inspeção de estado de relay via [PR #495](https://github.com/marmot-protocol/whitenoise/pull/495) e [PR #502](https://github.com/marmot-protocol/whitenoise/pull/502).

O mesmo release muda o comportamento das conversas. O [PR #468](https://github.com/marmot-protocol/whitenoise/pull/468) adiciona threading de respostas NIP-C7 com tags `q` e referências `nostr:nevent`, os [PR #471](https://github.com/marmot-protocol/whitenoise/pull/471) e [PR #512](https://github.com/marmot-protocol/whitenoise/pull/512) mantêm mensagens deletadas visíveis como placeholders de exclusão em vez de removê-las silenciosamente, o [PR #478](https://github.com/marmot-protocol/whitenoise/pull/478) adiciona um fluxo in-app de bug report usando relatórios anônimos [NIP-44](/pt/topics/nip-44/) (Encrypted Payloads), e o [PR #486](https://github.com/marmot-protocol/whitenoise/pull/486) adiciona chat de suporte diretamente no cliente. Controles de mensagens voltados ao usuário também chegaram na mesma janela: o [PR #532](https://github.com/marmot-protocol/whitenoise/pull/532) arquiva chats, o [PR #541](https://github.com/marmot-protocol/whitenoise/pull/541) adiciona mute e unmute com durações configuráveis, e o [PR #535](https://github.com/marmot-protocol/whitenoise/pull/535) adiciona configurações de notificação. O [PR #539](https://github.com/marmot-protocol/whitenoise/pull/539) é trabalho preparatório para registro de push, conectando registro APNs no iOS e detecção de Play Services no Android para que o registro seja construído sobre isso. No backend, o [MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit) adicionou primitivas de push notification MIP-05 e um builder de notification request ([PR #235](https://github.com/marmot-protocol/mdk/pull/235), [PR #238](https://github.com/marmot-protocol/mdk/pull/238)), enquanto [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) adicionou persistência de registro de push notification ([PR #688](https://github.com/marmot-protocol/whitenoise-rs/pull/688)), correções de cancelamento de tarefas em background ([PR #696](https://github.com/marmot-protocol/whitenoise-rs/pull/696)) e recuperação de key package no startup ([PR #693](https://github.com/marmot-protocol/whitenoise-rs/pull/693)).

### Nostr VPN chega à v0.3.0 com roster sync e invite v2

[Seguindo a cobertura do lançamento da semana passada](/pt/newsletters/2026-03-25-newsletter/#nostr-vpn-é-lançado-como-alternativa-ao-tailscale), [nostr-vpn](https://github.com/mmalmi/nostr-vpn), a VPN peer-to-peer que usa relays Nostr para sinalização e WireGuard para túneis criptografados, continuou seu ritmo rápido de releases, lançando versões até a [v0.3.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.3). O bump de versão traz duas mudanças incompatíveis: o formato de invite muda para v2 (a 0.3.0 ainda consegue importar invites v1, mas builds antigos não conseguem importar invites v2), e um roster sync assinado por admin foi adicionado ao protocolo de sinalização. Pares em versões misturadas ainda conseguem conectar-se na camada mesh, mas peers antigos não participam da sincronização de roster.

A adição de roster sync inicia o movimento em direção a uma rede gerenciada. Um nó admin agora pode enviar mudanças de associação a todos os peers, de modo que adicionar ou remover um dispositivo da mesh não exige que cada peer atualize manualmente sua configuração. As releases v0.2.x da mesma semana trataram problemas específicos de deployment: da [v0.2.22](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.22) até a [v0.2.28](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.28) corrigiram gerenciamento de serviço no Windows, adicionaram scripts de build para Android e refinaram o fluxo de LAN pairing.

### nospeak é lançado como um mensageiro privado 1.0

[nospeak](https://github.com/psic4t/nospeak), um mensageiro privado construído sobre Nostr, lançou sua [1.0.0](https://github.com/psic4t/nospeak/releases/tag/v1.0.0) em 27 de março. O projeto inclui conversas um a um e em grupo, gerenciamento de contatos e uma arquitetura self-hostable. Chats um a um usam [NIP-17](/pt/topics/nip-17/) (Private Direct Messages), que combina [NIP-59](/pt/topics/nip-59/) (Gift Wrap) com [NIP-44](/pt/topics/nip-44/) (Encrypted Payloads) para esconder o remetente dos relays. Para mídia, arquivos são criptografados do lado do cliente com AES-256-GCM antes do upload para servidores Blossom. O release também é distribuído como imagem de container para self-hosting.

### Flotilla v1.7.0 adiciona salas de voz e login por email

[Flotilla](https://gitea.coracle.social/coracle/flotilla), o cliente estilo Discord do hodlbod baseado em [NIP-29](/pt/topics/nip-29/) (Relay-based Groups) construído em torno do modelo "relays as groups", lançou [v1.7.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0) e [v1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.1) em 30 e 31 de março. O principal recurso são salas de voz, contribuídas por mplorentz. Usuários agora podem entrar em chamadas de voz dentro de canais de grupo, com um diálogo de entrada ([PR #109](https://gitea.coracle.social/coracle/flotilla/pulls/109)) que permite selecionar um dispositivo de entrada de áudio e escolher entre entrar na chamada de voz ou apenas visualizar o chat de texto. O diálogo resolve um problema de UX da iteração anterior: entrar em uma sala com voz antes forçava a ativação do microfone mesmo quando o usuário queria apenas ler mensagens ou verificar configurações da sala.

O mesmo release adiciona login com email e senha como alternativa à autenticação baseada em chave Nostr, proof-of-work em DMs, edição de DMs, onboarding e settings de relay redesenhados, detecção de suporte a Blossom via `supported_nips`, badges de notificação melhorados, fallback de push notification no Android e correções de upload de arquivos no Android. A v1.7.1 vem em seguida com uma correção para fallback de registro pomade ao usar um signer offline.

Hodlbod também está construindo [Caravel](https://gitea.coracle.social/coracle/caravel), um gerenciador de hospedagem e dashboard para relays zooid, que registrou 40 commits nesta semana em desenvolvimento inicial.

### Nymchat lança chats de grupo impulsionados por Marmot

[Nymchat](https://github.com/Spl0itable/NYM) (também conhecido como NYM, Nostr Ynstant Messenger), o cliente de chat efêmero com bridge para Bitchat, anunciou que todos os novos chats de grupo agora usam o protocolo [Marmot](/pt/topics/marmot/) para mensagens criptografadas com MLS. A integração usa kinds `443`, `444` e `445` para key packages, mensagens de welcome e mensagens de grupo, respectivamente, fornecendo forward secrecy, segurança pós-comprometimento e zero vazamento de metadados. Se um destinatário não puder usar MLS, o Nymchat faz fallback para seu caminho anterior de chat em grupo [NIP-17](/pt/topics/nip-17/) (Private Direct Messages), que ainda é end-to-end encrypted, mas não tem as propriedades de ratchet-tree do MLS.

As séries v3.55 e v3.56 desta semana se concentraram em casos de borda de chat em grupo: carregamento em novos dispositivos, comportamento de saída, roteamento de notificações e contagens de badge de não lidos. O mesmo ciclo também corrigiu uma vulnerabilidade XSS por HTML não escapado e adicionou bloqueio de palavras-chave e frases estendido a apelidos de usuários. Isso faz do Nymchat mais um cliente Marmot a se juntar a [White Noise](#white-noise-corrige-churn-de-relays-e-expande-controles-do-cliente) e [OpenChat](#openchat-v024-até-v030), ampliando o conjunto de apps que podem trocar mensagens de grupo criptografadas com MLS sobre o mesmo protocolo.

## Lançamentos

### Calendar by Form* v1.0.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), o app de calendário descentralizado construído sobre [NIP-52](/pt/topics/nip-52/) (Calendar Events), chegou à [v1.0.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.0.0) em 29 de março. O release adiciona listas privadas de calendário usando eventos Nostr criptografados (kind `32123`) com self-encryption [NIP-44](/pt/topics/nip-44/) (Encrypted Payloads), para que usuários possam organizar eventos em coleções privadas sem expor o agrupamento aos relays. O mesmo release adiciona tratamento de intent ICS para importar dados de calendário de outras aplicações e solicitações de convite para compartilhar eventos entre usuários.

### Amber v5.0.2 até v5.0.4

[Amber](https://github.com/greenart7c3/Amber), o app assinador [NIP-55](/pt/topics/nip-55/) (Android Signer Application), lançou três point releases: [v5.0.2](https://github.com/greenart7c3/Amber/releases/tag/v5.0.2), [v5.0.3](https://github.com/greenart7c3/Amber/releases/tag/v5.0.3) e [v5.0.4](https://github.com/greenart7c3/Amber/releases/tag/v5.0.4). A adição mais visível é login por frase de recuperação mnemônica ([PR #358](https://github.com/greenart7c3/Amber/pull/358)), que permite que usuários restaurem seu signer a partir de uma seed phrase BIP39 em vez de exigir a string bruta nsec ou ncryptsec. O [PR #357](https://github.com/greenart7c3/Amber/pull/357) adiciona uma whitelist de relay auth [NIP-42](/pt/topics/nip-42/), para que usuários possam restringir quais relays estão autorizados a solicitar autenticação do cliente. O [PR #353](https://github.com/greenart7c3/Amber/pull/353) adiciona seleção de escopo de criptografia para permissões de decrypt, permitindo conceder acesso apenas a NIP-04 ou apenas a NIP-44 em vez de uma permissão ampla. A v5.0.4 corrige um bug em que a rejeição não respeitava permissões com escopo de encrypt e decrypt e melhora o desempenho ao receber múltiplas requisições de bunker.

### Aegis v0.4.0

[Aegis](https://github.com/ZharlieW/Aegis), o signer multiplataforma, lançou [v0.4.0](https://github.com/ZharlieW/Aegis/releases/tag/v0.4.0) em 26 de março. O release adiciona modos de autorização Full e Selective nas Settings e corrige múltiplos problemas de leitura de QR code. Commits posteriores [d4f799f](https://github.com/ZharlieW/Aegis/commit/d4f799fe51dd82968d54f72ac77f2de29d0cfe6b), [3313af9](https://github.com/ZharlieW/Aegis/commit/3313af92e55e449ebc98fbd91a085bd444d716e7), [3b214e4](https://github.com/ZharlieW/Aegis/commit/3b214e4176f5dbe7f18690d0996e69dd151fe00f) e [e4f40b6](https://github.com/ZharlieW/Aegis/commit/e4f40b6f1f48c2dae1bb5e4246df26c26dba419e) continuam o mesmo trabalho com controles de seleção em lote, estatísticas reutilizáveis de seleção em lote, APIs set-all-groups selection e estatísticas de uso por permissão na página de permissões do app.

### Schemata v0.2.7 até v0.3.0

[Schemata](https://github.com/nostrability/schemata), as definições JSON Schema para validar kinds de evento Nostr, lançou quatro releases da [v0.2.7](https://github.com/nostrability/schemata/releases/tag/v0.2.7) até a [v0.3.0](https://github.com/nostrability/schemata/releases/tag/v0.3.0) com 21 PRs mergeados. A v0.3.0 traz correções de consistência de padrões em URLs de relay, IDs hex, tipos MIME e strings BOLT-11 ([PR #126](https://github.com/nostrability/schemata/pull/126)), centralização de padrões de URL de relay ([PR #117](https://github.com/nostrability/schemata/pull/117)), schemas de tipo base bech32 [NIP-19](/pt/topics/nip-19/) ([PR #118](https://github.com/nostrability/schemata/pull/118)), e validação para eventos spell kind 777 ([PR #125](https://github.com/nostrability/schemata/pull/125)). O pipeline de release agora publica uma nota kind `1` no Nostr a cada release ([PR #120](https://github.com/nostrability/schemata/pull/120)), então o projeto se anuncia pelo próprio protocolo que valida. O Schemata agora suporta uma dúzia de linguagens além do pacote canônico JS/TS: Rust, Go, Python, Kotlin, Java, Swift, Dart, PHP, C#/.NET, C++, Ruby e C.

Junto com o Schemata, a equipe publicou [schemata-codegen](https://github.com/nostrability/schemata-codegen), um gerador experimental de código que toma uma abordagem diferente para o mesmo problema de validação. Onde os pacotes validadores do Schemata exigem uma dependência runtime de JSON Schema, o schemata-codegen transpõe schemas diretamente para construções tipadas de linguagem nativa (typed tag tuples, kind interfaces e runtime validators), removendo a necessidade de uma biblioteca validadora em runtime. O [comparativo codegen-vs-validators](https://github.com/nostrability/schemata-codegen/blob/main/CODEGEN-VS-VALIDATORS.md) documenta quando cada abordagem faz sentido.

### BigBrotr v6.5.0 até v6.5.4

[BigBrotr](https://github.com/BigBrotr/bigbrotr), a plataforma de analytics de relay, lançou cinco releases da [v6.5.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.0) até a [v6.5.4](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.4). A v6.5.0 centraliza a validação de URL de relay com uma factory function `parse_relay_url()` e adiciona verificação de comprimento de URL e sanitização de path. A infraestrutura de monitoramento também recebeu correções: eventos de anúncio agora incluem tags de localização geohash (seguindo [NIP-52](/pt/topics/nip-52/)), e proteção por timeout foi adicionada aos testes de metadados Geo/Net [NIP-66](/pt/topics/nip-66/) que não tinham deadline e podiam travar indefinidamente. O [PR #410](https://github.com/BigBrotr/bigbrotr/pull/410) faz upgrade do PostgreSQL de 16 para 18, trazendo o subsistema de async I/O e melhor throughput de WAL para o pipeline de analytics de relay.

### Relay da Vertex Lab adiciona busca de perfil NIP-50

[Vertex Lab](https://vertexlab.io), a equipe por trás do [npub.world](https://github.com/vertex-lab/npub.world) e do motor de Web of Trust [Vertex](https://vertexlab.io/docs), anunciou que `wss://relay.vertexlab.io` agora suporta [NIP-50](/pt/topics/nip-50/) (Search) para consultas de perfil. O NIP-50 estende o filtro padrão `REQ` do Nostr com um campo `search`, permitindo que clientes enviem consultas de full-text search a relays com suporte a indexação. Adicionar busca de perfil a um relay que já serve dados de Web of Trust significa que clientes conectados ao `relay.vertexlab.io` podem descobrir usuários por nome ou descrição sem um serviço de busca separado.

### Hashtree v0.2.17 e v0.2.18 lançam mesh WebRTC e Iris Desktop

[Hashtree](https://github.com/mmalmi/hashtree), o sistema de armazenamento de blobs content-addressed do mmalmi que publica raízes de Merkle no Nostr, lançou [v0.2.17](https://github.com/mmalmi/hashtree/releases/tag/v0.2.17) e [v0.2.18](https://github.com/mmalmi/hashtree/releases/tag/v0.2.18) em 31 de março. Os dois releases encerram um sprint de 30 commits que adiciona três capacidades distintas. Primeiro, o crate `hashtree-webrtc` (renomeado para `hashtree-network` na v0.2.18) adiciona distribuição peer-to-peer de blobs via WebRTC com sinalização mesh unificada entre o CLI Rust, o simulation harness e o cliente TypeScript. Segundo, o pipeline de release agora constrói artefatos Windows (zip do CLI e instalador do Iris), levando a cobertura multiplataforma a macOS, Linux e Windows. Terceiro, ambos os releases empacotam o Iris Desktop 0.1.0, o cliente social Nostr do mmalmi, como assets AppImage, .deb e instalador Windows ao lado do CLI do Hashtree. O [Hashtree foi coberto pela primeira vez na Newsletter #10](/pt/newsletters/2026-02-18-newsletter/) quando foi lançado como um armazenamento compatível com [Blossom](/pt/topics/blossom/) baseado em filesystem. A camada WebRTC é o primeiro passo em direção à distribuição peer-to-peer de conteúdo sem depender de servidores Blossom centralizados.

### Nostr Mail Client v0.7.0 até v0.7.2

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client), o cliente Flutter em estilo email construído sobre identidades Nostr, lançou [v0.7.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.0), [v0.7.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.1) e [v0.7.2](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.2) em três dias. O trabalho de produto mais visível se concentrou em onboarding ([PR #9](https://github.com/nogringo/nostr-mail-client/pull/9)) e edição de perfil ([PR #10](https://github.com/nogringo/nostr-mail-client/pull/10)), peças básicas para qualquer cliente que tente apresentar o Nostr como uma mailbox. Os point releases posteriores empacotaram esse trabalho em novos builds Android e Linux.

### Wisp v0.14.0 até v0.16.3

[Wisp](https://github.com/barrydeen/wisp), o cliente Nostr para Android, lançou mais 13 releases da [v0.14.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.14.0-beta) até a [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta). O trabalho desta semana inclui correções de rumor JSON NIP-17 ([PR #385](https://github.com/barrydeen/wisp/pull/385)), badges de repost em cards de galeria ([PR #383](https://github.com/barrydeen/wisp/pull/383)), detalhes expansíveis de reações ([PR #382](https://github.com/barrydeen/wisp/pull/382)), conjuntos persistentes de emoji ([PR #381](https://github.com/barrydeen/wisp/pull/381)) e controles de autoplay de vídeo ([PR #380](https://github.com/barrydeen/wisp/pull/380)). A mais recente [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta) também corrige shortcodes de emoji customizado com hífens e tags de emoji ausentes.

### Primal Android 3.0.17

[Primal Android](https://github.com/PrimalHQ/primal-android-app) lançou [3.0.17](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.17) em 24 de março. O [PR #1000](https://github.com/PrimalHQ/primal-android-app/pull/1000) mapeia tipos de WalletException para códigos de erro em respostas NWC, dando a clientes [NIP-47](/pt/topics/nip-47/) informação estruturada de falha em vez de erros genéricos. O [PR #995](https://github.com/PrimalHQ/primal-android-app/pull/995) corrige votos por zap em enquetes aparecendo como Top Zaps, e o [PR #998](https://github.com/PrimalHQ/primal-android-app/pull/998) oculta o saldo da carteira e botões de ação quando nenhuma carteira está configurada.

### OpenChat v0.2.4 até v0.3.0

[OpenChat](https://github.com/DavidGershony/openChat), o cliente de chat baseado em Avalonia construído sobre a stack [Marmot](/pt/topics/marmot/), lançou seis releases da [v0.2.4](https://github.com/DavidGershony/openChat/releases/tag/v0.2.4) até a [v0.3.0](https://github.com/DavidGershony/openChat/releases/tag/v0.3.0) em quatro dias. O log de commits conta a história de um cliente preenchendo o espaço entre "Marmot funciona" e "alguém consegue realmente usar isso no dia a dia". O relay authentication [NIP-42](/pt/topics/nip-42/) chegou, seguido por uma UI de seleção de relay com filtragem de eventos duplicados. Mensagens de voz ganharam pause, resume, seek e exibição de tempo. O caminho do signer foi reforçado: conexões com Amber foram corrigidas com um formato atualizado de URI [NIP-46](/pt/topics/nip-46/), o WebSocket faz auto-reconnect antes de enviar requests, e requisições duplicadas ao Amber agora são detectadas verificando respostas replayadas. No lado de armazenamento, Linux e macOS ganharam secure storage AES-256-GCM com chaves baseadas em arquivo, e o fetch de metadados de usuário agora usa descoberta de relay [NIP-65](/pt/topics/nip-65/) e faz cache dos resultados em um banco local.

### Igloo Signer 1.1

[Igloo](https://github.com/FROSTR-ORG/igloo-ios-prototype), o signer threshold [FROST](/pt/topics/frost/) para iOS do projeto FROSTR, lançou [v1.1](https://github.com/FROSTR-ORG/igloo-ios-prototype/releases/tag/v1.1) em 28 de março. Assinaturas FROST (Flexible Round-Optimized Schnorr Threshold) permitem que um grupo de signers controle coletivamente um par de chaves Nostr, em que qualquer conjunto t-of-n de participantes pode assinar um evento sem que nenhuma parte individual detenha a chave privada completa. O Igloo é uma das primeiras implementações mobile dessa abordagem para Nostr.

### nak v0.19.3 e v0.19.4

[nak](https://github.com/fiatjaf/nak), o toolkit de linha de comando Nostr do fiatjaf, lançou [v0.19.3](https://github.com/fiatjaf/nak/releases/tag/v0.19.3) e [v0.19.4](https://github.com/fiatjaf/nak/releases/tag/v0.19.4) em 26 e 30 de março. Ambos os releases corrigem condições de panic: o [PR #118](https://github.com/fiatjaf/nak/pull/118) substitui `strings.Split` por `strings.Cut` para impedir um potencial acesso out-of-bounds, e o [PR #119](https://github.com/fiatjaf/nak/pull/119) previne a mesma classe de panic no parsing de flags do curl.

### Flora v0.3.0

[Flora](https://github.com/shawnyeager/flora-extension), uma extensão Chrome para gravação e compartilhamento descentralizado de tela no Nostr, lançou [v0.3.0](https://github.com/shawnyeager/flora-extension/releases/tag/v0.3.0). O release adiciona compartilhamento privado de vídeo criptografado com modos público, não listado e privado. Gravações privadas são criptografadas com AES-256-GCM e entregues aos destinatários via [NIP-17](/pt/topics/nip-17/) (Private Direct Messages), então a gravação nunca toca um servidor em cleartext.

### YakiHonne Mobile 2.0.3

[YakiHonne](https://github.com/YakiHonne/mobile-app), o cliente Nostr mobile, lançou [2.0.3](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.3) com avaliações de relay e pedidos de entrada, respostas aninhadas expandidas, auto-tradução de notas e suporte a múltiplos relays em NWC.

## Atualizações de Projetos

### Zap Cooking adiciona zap polls e verificação de pagamento Branta

[Zap Cooking](https://github.com/zapcooking/frontend), a plataforma de receitas e conteúdo, mergeou 11 PRs nesta semana focados em conteúdo interativo e fluxos de pagamento. O [PR #277](https://github.com/zapcooking/frontend/pull/277) adiciona zap polls (kind 6969), em que usuários votam enviando sats e podem ver listas de votantes com fotos de perfil. O [PR #274](https://github.com/zapcooking/frontend/pull/274) redesenha a UX das enquetes para que a interface de votação se encaixe mais naturalmente no feed.

O [PR #276](https://github.com/zapcooking/frontend/pull/276) adiciona leitura de QR code pela câmera ao fluxo Send Payment e integra [Branta](https://branta.pro/), um serviço de verificação que checa se um destino de pagamento é legítimo antes do envio. A Branta verifica destinos de pagamento contra phishing, troca de endereço e interceptação man-in-the-middle antes do envio. Na implementação do Zap Cooking, um nome de plataforma e logo verificados pela Branta aparecem diretamente no fluxo de pagamento, e QR codes habilitados para Branta podem carregar parâmetros `branta_id` e `branta_secret` para que a carteira possa verificar o destino a partir do próprio código escaneado.

### diVine prepara o terreno para busca unificada e reforça entrega de vídeo

[diVine](https://github.com/divinevideo/divine-mobile), o cliente de vídeo short-form, passou a semana reforçando busca, navegação de feed, recuperação de playback e comportamento de upload. O [PR #2540](https://github.com/divinevideo/divine-mobile/pull/2540) estabelece a base para uma tela de busca unificada, com seções agrupadas para Videos, People e Tags. O [PR #2623](https://github.com/divinevideo/divine-mobile/pull/2623) endurece a paginação em feeds de perfil, inbox, notificações, listas discover, classic vines, busca e feeds de grid composable ao movê-los para um controlador de paginação compartilhado.

A entrega de vídeo também recebeu várias correções concretas. O [PR #2643](https://github.com/divinevideo/divine-mobile/pull/2643) tenta novamente fontes derivadas hospedadas pela Divine em ordem e faz fallback para o blob bruto antes de exibir um erro de playback, para que falhas transitórias em uma fonte não matem o playback imediatamente. O [PR #2634](https://github.com/divinevideo/divine-mobile/pull/2634) mantém uploads resumíveis no caminho controlado pela Divine quando o probing de capacidades falha de forma transitória, reduzindo uploads quebrados por pequenas falhas de rede. O [PR #2637](https://github.com/divinevideo/divine-mobile/pull/2637) também muda a barreira de conteúdo sensível para que vídeos só sejam efetivamente bloqueados por labels reais de warning, não apenas por labels de content warning fornecidas pelo criador.

### Shopstr adiciona storefronts customizadas e Milk Market segue entregando trabalho de marketplace

[Shopstr](https://github.com/shopstr-eng/shopstr), o marketplace baseado em Nostr, mergeou o [PR #245](https://github.com/shopstr-eng/shopstr/pull/245) adicionando storefronts customizadas. Isso dá aos vendedores uma superfície de home mais distinta em vez de forçar cada listagem à mesma apresentação genérica.

[Milk Market](https://github.com/shopstr-eng/milk-market), um marketplace dedicado a leite, continuou com otimizações de storefront ([PR #18](https://github.com/shopstr-eng/milk-market/pull/18)), recuperação de conta ([PR #17](https://github.com/shopstr-eng/milk-market/pull/17)), beef splits ([PR #15](https://github.com/shopstr-eng/milk-market/pull/15)) e correções de tipagem de ferramentas MCP ([PR #16](https://github.com/shopstr-eng/milk-market/pull/16)).

### Notedeck adiciona efeitos sonoros e estende o caminho do atualizador rumo ao Android

[Notedeck](https://github.com/damus-io/notedeck), o cliente desktop da equipe Damus, mergeou o [PR #1412](https://github.com/damus-io/notedeck/pull/1412) adicionando um subsistema de efeitos sonoros com sons de interação de UI usando rodio, e o [PR #1399](https://github.com/damus-io/notedeck/pull/1399) com atualizações do Agentium incluindo uma flag de título para CLI e pastas de sessão colapsáveis. Um [PR #1417](https://github.com/damus-io/notedeck/pull/1417) aberto propõe self-update de APK via Nostr/Zapstore no Android, construindo sobre [o trabalho de atualizador nativo do Nostr do Notedeck coberto na Newsletter #14](/pt/newsletters/2026-03-18-newsletter/#notedeck-move-descoberta-de-releases-para-o-nostr).

### Nostria adiciona relay hints em reposts e alinhamento com NIP-98

[Nostria](https://github.com/nostria-app/nostria) mergeou o [PR #583](https://github.com/nostria-app/nostria/pull/583) adicionando relay hints [NIP-18](/pt/topics/nip-18/) (Reposts) a tags `e` de repost para eventos kind 6 e kind 16, o [PR #582](https://github.com/nostria-app/nostria/pull/582) alinhando auth HTTP do Brainstorm (kind 27235) às tags obrigatórias [NIP-98](/pt/topics/nip-98/) (HTTP Auth), e o [PR #576](https://github.com/nostria-app/nostria/pull/576) adicionando testes de validação de schema do Schemata. A mudança NIP-98 significa que o Nostria pode autenticar-se em serviços externos usando o mesmo formato de auth HTTP que outros clientes usam.

### Nostr-Doc adiciona empacotamento desktop e trabalho offline-first

[Nostr-Doc](https://github.com/formstr-hq/nostr-docs), o editor colaborativo da Form*, teve uma semana movimentada de empacotamento e trabalho de editor. O [commit fcdc00a](https://github.com/formstr-hq/nostr-docs/commit/fcdc00a564c8d76f094c586b06efce07592a60e4) adiciona um app desktop, o [commit 3977a8e](https://github.com/formstr-hq/nostr-docs/commit/3977a8eb2e62b84a67de756c2776e14de8470927) inicia trabalho de app nativo, e o [commit 413a030](https://github.com/formstr-hq/nostr-docs/commit/413a030f5b47fb8e32a5dff81bcef557ad9b5869) empurra o app em direção a comportamento offline-first. No lado do editor, o [commit 1855ce8](https://github.com/formstr-hq/nostr-docs/commit/1855ce86ee83ad504e14e47d9c339baffb114786) adiciona salvar com Ctrl+S, avisos de save, correções de link preview e renderização corrigida de strikethrough.

### rust-nostr otimiza parsing de NIP-21 e adiciona suporte a NIP-62 do lado do relay

[rust-nostr](https://github.com/rust-nostr/nostr) mergeou oito PRs. O mais notável é o [PR #1308](https://github.com/rust-nostr/nostr/pull/1308), que otimiza o parsing de URI [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) em `PublicKey::parse` alinhando-o ao desempenho padrão de parsing bech32. Antes disso, URIs NIP-21 levavam aproximadamente o dobro do tempo para serem parseados em relação a chaves bech32 brutas. O projeto também tem quatro PRs abertos adicionando suporte específico de relay a [NIP-62](/pt/topics/nip-62/) (Request to Vanish) nos backends memory, LMDB, SQLite e database test ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)).

### nostr-tools adiciona controle manual de relays de bunker e corrige parsing multi-relay de NIP-47

[nostr-tools](https://github.com/nbd-wtf/nostr-tools) mergeou o [PR #530](https://github.com/nbd-wtf/nostr-tools/pull/530) adicionando `skipSwitchRelays` a BunkerSignerParams para gerenciamento manual de relays, e o [PR #529](https://github.com/nbd-wtf/nostr-tools/pull/529) corrigindo o parsing de connection string [NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect) para suportar múltiplos relays como a spec permite.

### Nostrability integra dados de auditoria do Sherlock e publica visão geral do Schemata

[Nostrability](https://github.com/nostrability/nostrability), o tracker de interoperabilidade para clientes Nostr, mergeou 14 PRs. O [PR #306](https://github.com/nostrability/nostrability/pull/306) integra estatísticas de scan do Sherlock ao dashboard. Sherlock é a ferramenta automatizada de auditoria da Nostrability que se conecta a clientes Nostr, captura os eventos que eles publicam e valida cada evento contra as definições JSON Schema do Schemata para detectar violações de spec. O dashboard agora mostra taxas de falha de schema por cliente ([PR #315](https://github.com/nostrability/nostrability/pull/315)), para que desenvolvedores possam ver quais kinds de evento seu cliente implementa incorretamente. O [PR #323](https://github.com/nostrability/nostrability/pull/323) reformula o workflow de publicação no Nostr para que anúncios de release rodem como um job separado que não pode ser cancelado por etapas anteriores de CI.

elsat também publicou [Schemata for nostr devs](https://njump.me/naddr1qvzqqqr4gupzq96n3hp2vfmf6z2y8uvvxl97xk86kkalnqghx4p25lzl79c76a7yqy2hwumn8ghj7un9d3shjtnyv9kh2uewd9hj7qgwwaehxw309ahx7uewd3hkctcqz4fnx4rkw3x57nrcwdn8zt22xd982jehfptsgqtrww) em 30 de março, descrevendo como schemata, schemata-codegen e Sherlock se encaixam e fornecendo números atuais de cobertura: 179 schemas de kind de evento em 65 NIPs, 154 schemas de tags, 13 mensagens de protocolo e 310 eventos de exemplo.

### Nalgorithm adiciona geração de digest e cache local de score

[Nalgorithm](https://github.com/jooray/nalgorithm), um novo projeto de feed Nostr ranqueado por relevância, iniciou desenvolvimento público nesta semana. O [commit cf6c501](https://github.com/jooray/nalgorithm/commit/cf6c501e754ef95a1b4fecc1a76288471a101f43) estabelece o app web inicial que busca posts de follows e os pontua contra um prompt de preferência definido pelo usuário. O [commit 8e931b6](https://github.com/jooray/nalgorithm/commit/8e931b6ae85d470e73603752134ff49b7ba4bb86) adiciona uma ferramenta CLI de digest que transforma posts mais bem ranqueados em um resumo falado, enquanto o [commit 4cb9c63](https://github.com/jooray/nalgorithm/commit/4cb9c635489a9a3429e8d71f3861dc2a11624153) adiciona cache de scores em arquivo e evolução incremental do prompt aprendido a partir de likes recentes. O [commit c2edfb8](https://github.com/jooray/nalgorithm/commit/c2edfb8b89fadbe0028c3f5729bda7e23b2e3c03) também para de fazer cache de fallback scores de batches que falharam, para que uma falha transitória de scoring não achate permanentemente o ranking de um post.

### TENEX adiciona vector store para RAG e startup direcionado de MCP

[TENEX](https://github.com/tenex-chat/tenex), o framework de agentes nativo do Nostr que conecta agentes de IA a canais Nostr via Telegram, mergeou sete PRs nesta semana. O [PR #101](https://github.com/tenex-chat/tenex/pull/101) adiciona uma abstração plugável de vector store com backends SQLite-vec, LanceDB e Qdrant, dando aos agentes retrieval-augmented generation sem travar em um banco vetorial específico. O [PR #102](https://github.com/tenex-chat/tenex/pull/102) torna o startup de MCP direcionado: apenas servidores MCP cujas ferramentas um agente realmente usa são iniciados, em vez de subir todos os servidores eager no primeiro uso. O [PR #100](https://github.com/tenex-chat/tenex/pull/100) adiciona uma ferramenta `send_message` para que agentes com bindings de canal Telegram possam enviar mensagens proativamente em vez de apenas responder a mensagens recebidas. O [PR #106](https://github.com/tenex-chat/tenex/pull/106) evita um spawn de subprocesso que disparava uma pré-alocação de 9 GB de memória Bun/JSC lendo `.git/HEAD` diretamente em vez de executar `git branch`.

### Dart NDK move suporte a signer Amber e adiciona Alby Go 1-click

[Dart NDK](https://github.com/relaystr/ndk), o kit de desenvolvimento Nostr para Flutter, lançou 11 PRs mergeados. O [PR #525](https://github.com/relaystr/ndk/pull/525) move suporte ao signer Amber para o pacote ndk_flutter, e o [PR #552](https://github.com/relaystr/ndk/pull/552) adiciona conexão one-click com Alby Go na sample app. O [PR #502](https://github.com/relaystr/ndk/pull/502) adiciona um script install.sh para o CLI, e o [PR #523](https://github.com/relaystr/ndk/pull/523) remove a dependência do verificador Rust em favor de tratamento nativo de assets.

## Trabalho de Protocolo e Spec

### Marmot move KeyPackages para eventos endereçáveis e reforça push notifications

A [specificação Marmot](https://github.com/marmot-protocol/marmot) mergeou quatro PRs que mudam como o protocolo trata material de chave e associação de grupo. O [PR #54](https://github.com/marmot-protocol/marmot/pull/54) migra eventos KeyPackage de `kind:443` regular para `kind:30443` endereçável com uma tag `d`, eliminando a necessidade de deleção de eventos [NIP-09](/pt/topics/nip-09/) durante rotação de chave. Eventos endereçáveis sobrescrevem no lugar, tornando a rotação autocontida. O [PR #57](https://github.com/marmot-protocol/marmot/pull/57) permite que usuários não-admin façam commit de propostas SelfRemove (saída voluntária do grupo), e o [PR #62](https://github.com/marmot-protocol/marmot/pull/62) exige que admins renunciem ao status de admin antes de usar SelfRemove, prevenindo que um admin desapareça enquanto ainda detém privilégios elevados.

O [PR #61](https://github.com/marmot-protocol/marmot/pull/61) reforça o formato de push notification [MIP-05](/pt/topics/mip-05/), tornando explícitos a codificação base64 em blob único, versionamento, wire format de token e uso de chave x-only. O efeito é uma representação wire única e definida para blobs de token e chaves x-only em spec, bibliotecas cliente e backends de app. A implementação dessas mudanças de spec chegou à stack White Noise nesta semana e está coberta na [seção White Noise v2026.3.23 acima](#white-noise-corrige-churn-de-relays-e-expande-controles-do-cliente).

### Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado:**

- **[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md): Static Websites** ([PR #1538](https://github.com/nostr-protocol/nips/pull/1538)): Define eventos de manifesto kind `15128` (site raiz) e kind `35128` (site nomeado) para hospedar sites estáticos sob pares de chaves Nostr usando armazenamento Blossom. Veja o [deep dive abaixo](#nip-deep-dive-nip-5a-sites-estáticos).

- **[NIP-30](/pt/topics/nip-30/) (Custom Emoji): Permitir hífens em shortcodes** ([PR #2297](https://github.com/nostr-protocol/nips/pull/2297)): Atualiza a descrição de shortcode para incluir hífens. Shortcodes com hífen já são usados na prática desde a introdução do NIP, então a spec agora documenta o uso atual.

**PRs Abertos e Discussões:**

- **NIP-C1: Agent TUI Messages** ([PR #2295](https://github.com/nostr-protocol/nips/pull/2295)): Propõe um formato estruturado de mensagem para agentes enviarem elementos interativos de UI por DMs criptografadas, incluindo payloads tipados `text`, `buttons`, `card` e `table`. O rascunho mantém tudo dentro do conteúdo JSON de mensagens diretas existentes [NIP-17](/pt/topics/nip-17/) e [NIP-04](/pt/topics/nip-04/). Não define um novo kind de evento e usa um formato simples de callback string para respostas de botões.

- **NIP-95: Hybrid Peer-to-Peer Relay Protocol** ([PR #2293](https://github.com/nostr-protocol/nips/pull/2293)): Propõe um modelo híbrido de relay no qual relays permanecem autoritativos, mas também podem coordenar distribuição peer-to-peer de eventos recentes via WebRTC. O rascunho introduz mensagens de relay como `PEER_REGISTER`, `PEER_REQUEST` e `PEER_OFFER`, com clientes estáveis atuando como Super Peers e o relay agindo como seed node e fallback.

- **NIP-B9: Zap Poll Events** ([PR #2284](https://github.com/nostr-protocol/nips/pull/2284)): Reabre a antiga ideia de zap poll do NIP-69 agora que [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) (Polls) cobre enquetes gratuitas. O rascunho usa definições de enquete kind `6969` e zaps kind `9734` como votos, tornando-o um sistema de enquetes pagas com resistência econômica a Sybil. Ele complementa enquetes gratuitas one-key-one-vote.

- **NIP-AD: Super Zap** ([PR #2289](https://github.com/nostr-protocol/nips/pull/2289)): Propõe uma convenção na qual zaps enviados à pubkey de um relay ou de um cliente são exibidos como notas promocionais especializadas, transformando efetivamente recibos de zap em uma superfície de anúncio. Operadores de relay e clientes publicariam perfis com `lud16`, buscariam esses recibos, extrairiam o conteúdo embutido das descrições de zap e poderiam opcionalmente definir thresholds mínimos em sats para reduzir spam.

- **NIP-XX: Agent Reputation Attestations** ([PR #2285](https://github.com/nostr-protocol/nips/pull/2285)): Propõe kind `30085` como um evento parameterized replaceable para attestations estruturadas de reputação sobre agentes Nostr. O rascunho evita um score global único ao tornar a reputação dependente do observador, adiciona decaimento temporal para que attestations antigas percam peso, suporta avaliações negativas com exigência de evidência e esboça tanto weighted scoring simples quanto graph-diversity scoring para melhor resistência a Sybil.

- **NIP-XX: Paid API Service Announcements** ([PR #2291](https://github.com/nostr-protocol/nips/pull/2291)): Propõe eventos addressable kind `31402` para anunciar APIs HTTP pagas, com Nostr cuidando da descoberta e HTTP 402 do pagamento. O rascunho é tags-first para que relays possam filtrar por métodos de pagamento, preços e capacidades sem fazer parsing de conteúdo JSON, e permite schemas opcionais de request e response para que clientes ou agentes possam auto-gerar chamadas.

- **NIP-XX: Key Derivation from LNURL-auth via SplitSig** ([PR #2294](https://github.com/nostr-protocol/nips/pull/2294)): Propõe derivar um par de chaves Nostr de uma assinatura ECDSA de LNURL-auth combinada com um nonce aleatório do lado do cliente. A fórmula de derivação é `nsec = SHA256(ecdsa_signature || nonce)`. O servidor vê a assinatura ECDSA, inerente ao handshake LNURL-auth, mas nunca vê o nonce, e o browser gera o nonce, mas não controla a assinatura. Nenhuma das partes isoladamente consegue derivar o nsec. O resultado pretendido é que a mesma carteira Lightning produza a mesma chave Nostr entre dispositivos, com a carteira como âncora de recuperação e sem que nenhum servidor consiga reconstruir a chave privada.

- **[NIP-55](/pt/topics/nip-55/): Documentar campo rejected** ([PR #2290](https://github.com/nostr-protocol/nips/pull/2290)): Documenta o campo `rejected` para respostas de signer baseadas em intent, formalizando o comportamento que [a correção da série v1.07.x do Amethyst](#amethyst-lança-notas-fixadas-gerenciamento-de-relay-e-request-to-vanish) precisou contornar.

## NIP Deep Dive: NIP-5A (Sites estáticos)

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) define como hospedar sites estáticos sob pares de chaves Nostr, usando dois kinds de evento e infraestrutura existente de armazenamento de blobs para transformar eventos assinados em páginas web servidas. A [especificação](https://github.com/nostr-protocol/nips/blob/master/5A.md) foi mergeada em 25 de março via [PR #1538](https://github.com/nostr-protocol/nips/pull/1538).

O modelo usa kind `15128` para um site raiz, um por pubkey, e kind `35128` para sites nomeados identificados por uma tag `d`. Cada manifesto mapeia caminhos absolutos de URL para hashes SHA256. Aqui está um manifesto de site raiz:

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["path", "/favicon.ico", "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["description", "A static website hosted on Nostr"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

O fluxo de serving funciona em três etapas. Um servidor host recebe uma requisição HTTP, extrai a pubkey do autor do subdomínio, seja um npub para sites raiz ou uma pubkey codificada em base36 para sites nomeados, busca a lista de relays do autor via [NIP-65](/pt/topics/nip-65/) e consulta o manifesto do site. Quando encontra o manifesto, o servidor resolve o caminho solicitado para um hash de conteúdo, baixa o blob correspondente do servidor Blossom ou dos servidores listados nas tags `server` e o retorna.

O formato do subdomínio DNS é rigidamente especificado. Sites raiz usam o npub padrão como subdomínio. Sites nomeados usam uma codificação base36 de 50 caracteres da pubkey bruta seguida pelo valor da tag `d`, tudo em um único label DNS. Como labels DNS são limitados a 63 caracteres e a codificação base36 sempre ocupa 50, a tag `d` é limitada a 13 caracteres. A spec também exige que tags `d` correspondam a `^[a-z0-9-]{1,13}$` e não terminem com hífen, prevenindo ambiguidades de resolução DNS.

Usar hashes de conteúdo significa que o mesmo site pode ser servido por diferentes servidores host, e a integridade dos arquivos é verificável sem confiar no servidor. Um servidor host não precisa armazenar arquivos por conta própria. Ele os busca sob demanda no Blossom usando os hashes do manifesto. Isso significa que o autor controla o que é servido, o servidor Blossom armazena os arquivos brutos, e o servidor host apenas conecta os dois. Qualquer um desses três componentes pode ser substituído de forma independente.

Implementações existentes incluem [nsite](https://github.com/lez/nsite), o servidor host que resolve manifestos e serve arquivos, e [nsite-manager](https://github.com/hzrd149/nsite-manager), uma UI para construir e publicar manifestos. A spec também adicionou uma tag `source` para vincular ao repositório de código-fonte do site, e a atualização de README mergeada separadamente no [PR #2286](https://github.com/nostr-protocol/nips/pull/2286) registrou os kinds `15128` e `35128` no índice de kinds do NIP.

## NIP Deep Dive: NIP-62 (Request to Vanish)

[NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md) define kind `62` como uma requisição para que relays deletem todos os eventos da pubkey solicitante. A [especificação](https://github.com/nostr-protocol/nips/blob/master/62.md) é motivada por questões legais: em jurisdições com leis de direito ao esquecimento, ter uma requisição padronizada e assinada de deleção dá a operadores de relay um sinal claro para agir.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

A spec separa vanish requests direcionadas e globais. Uma requisição direcionada inclui tags `relay` específicas identificando quais relays devem agir. Uma requisição global usa a string literal `ALL_RELAYS` como valor da tag relay, pedindo que todo relay que veja o evento delete todos os eventos daquela pubkey. Relays que cumprem também devem garantir que eventos deletados não possam ser republicados de volta no relay, tornando a deleção sticky.

O NIP-62 vai além do [NIP-09](/pt/topics/nip-09/) (Event Deletion) em escopo e intenção. O NIP-09 permite deletar eventos individuais, e relays MAY cumprir. O NIP-62 solicita a deleção de tudo, e a spec diz que relays MUST cumprir se sua URL estiver tagueada. Ela também pede que relays deletem eventos [NIP-59](/pt/topics/nip-59/) (Gift Wrap) que tenham p-tag para a pubkey solicitante, o que significa que DMs recebidas são limpas junto com os próprios eventos do usuário. Publicar uma deleção NIP-09 contra uma vanish request NIP-62 não tem efeito: depois que você vanish, não pode un-vanish deletando a própria vanish request.

Nesta semana, o [Amethyst v1.07.0](#amethyst-lança-notas-fixadas-gerenciamento-de-relay-e-request-to-vanish) lançou suporte do lado do cliente ao NIP-62, permitindo que usuários iniciem vanish requests pelo app. Do lado do relay, [rust-nostr](https://github.com/rust-nostr/nostr) tem quatro PRs abertos adicionando suporte a NIP-62 nos backends memory, LMDB, SQLite e database test ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)). Isso coloca trabalho de suporte em cliente e relay na mesma semana.

O desenho do protocolo levanta uma tensão prática. A proposta de valor do Nostr inclui resistência à censura, significando que relays não deveriam ser capazes de impedir publicação. O NIP-62 introduz um caso em que um relay MUST impedir republicação de uma pubkey específica. As duas propriedades coexistem porque a requisição é autodirigida: você está pedindo a deleção dos seus próprios eventos, não dos eventos de outra pessoa. A propriedade de resistência à censura permanece intacta para todos, exceto para a pessoa que explicitamente optou por sair.

---

É isso por esta semana. Construindo algo ou tem novidades para compartilhar? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via [NIP-17](/pt/topics/nip-17/) (Private Direct Messages) DM</a> ou nos encontre no Nostr.
