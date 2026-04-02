---
title: 'Nostr Compass #15'
date: 2026-03-25
translationOf: /en/newsletters/2026-03-25-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** [Primal Android](https://github.com/PrimalHQ/primal-android-app) segue seu lançamento 3.0 de carteira com [Follow Packs, enriquecimento de zap e deep links `primalconnect://`](#primal-adiciona-follow-packs-enriquecimento-de-zap-e-deep-links). [BigBrotr](https://github.com/BigBrotr/bigbrotr) publica uma [análise de vazamento de nsec](#bigbrotr-mapeia-chaves-privadas-expostas-na-rede-de-relays), escaneando 41 milhões de eventos em 1.085 relays e encontrando 16.599 chaves privadas válidas, enquanto [npub.world](https://npub.world) integra alertas de vazamento às páginas de perfil na mesma semana. Martti Malmi lança [nostr-vpn](#nostr-vpn-é-lançado-como-alternativa-ao-tailscale), uma alternativa ao Tailscale que sinaliza sobre relays Nostr e cria túneis WireGuard, com 11 releases em sete dias. A equipe do [Vector](https://github.com/VectorPrivacy/Vector) [abre o código do DOOM P2P](#doom-open-source-roda-peer-to-peer-sobre-o-nostr) sobre Nostr, [FIPS](https://github.com/jmcorgan/fips) lança [v0.2.0](#fips-v020-lança-transporte-tor-builds-reproduzíveis-e-exemplos-sidecar), e [Nostrability Schemata](https://github.com/nostrability/schemata) se expande para [seis linguagens](#nostrability-schemata-fica-multilíngue) em uma semana.

## Notícias

### Primal adiciona Follow Packs, enriquecimento de zap e deep links

[Seguindo a cobertura da versão 3.0.7 da semana passada](/pt/newsletters/2026-03-18-newsletter/), [Primal Android](https://github.com/PrimalHQ/primal-android-app) passou esta semana em trabalho pós-release em torno de onboarding, UX do composer e contexto de carteira. O onboarding redesenhado introduz Follow Packs ([PR #949](https://github.com/PrimalHQ/primal-android-app/pull/949)), um botão nativo de GIF entra no composer de notas, um serviço de enriquecimento de zap ([PR #979](https://github.com/PrimalHQ/primal-android-app/pull/979)) anota transações da carteira com contexto de zap, e um protocolo de deep linking `primalconnect://` ([PR #969](https://github.com/PrimalHQ/primal-android-app/pull/969)) habilita navegação entre apps.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) está entregando o mesmo trabalho em paralelo via TestFlight, com a troca de carteira ([PR #191](https://github.com/PrimalHQ/primal-ios-app/pull/191)), a implementação de enquetes e a refatoração do onboarding chegando na mesma janela.

### BigBrotr mapeia chaves privadas expostas na rede de relays

[BigBrotr](https://github.com/BigBrotr/bigbrotr), a plataforma de analytics de relays Nostr, publicou uma [análise detalhada de chaves privadas expostas](https://bigbrotr.com/blog/exposed-nsec-analysis/) na rede de relays. O estudo escaneou 41 milhões de eventos em 1.085 relays, procurando strings nsec válidas embutidas no conteúdo dos eventos, e encontrou 16.599 chaves privadas válidas. Esse número parece alarmante até que se filtre um bot chamado "Mr.nsec", responsável por 92% das ocorrências. Depois de remover o tráfego de bots, apenas 38 contas reais com mais de 21.000 seguidores combinados tinham chaves expostas, e nenhuma mostrava sinais de saber que suas chaves estavam públicas.

A equipe construiu um nsec-leak-checker como um serviço [NIP-90](/pt/topics/nip-90/) (Data Vending Machine), permitindo que usuários verifiquem se sua chave privada aparece em algum ponto do dataset escaneado sem revelar a chave ao verificador. [npub.world](https://npub.world) integrou os dados de vazamento na mesma semana, exibindo banners de aviso em páginas de perfil onde chaves expostas foram detectadas. A combinação dá à rede tanto uma interface programática para DVMs e agentes quanto um aviso legível por humanos para usuários comuns. O dataset subjacente também alimenta o [BigBrotr v6.4.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.4.0), que adiciona materialized views de eventos replaceable e addressable e uma correção de timeout ocioso do sincronizador.

### nostr-vpn é lançado como alternativa ao Tailscale

Martti Malmi (mmalmi), criador do Iris, construiu e lançou [nostr-vpn](https://github.com/mmalmi/nostr-vpn), uma VPN peer-to-peer que usa relays Nostr para sinalização e WireGuard (via boringtun) para túneis criptografados. A motivação foi direta: "Got annoyed by Tailscale requiring 3rd party accounts, so created Nostr VPN." A ferramenta cria redes mesh entre dispositivos usando pares de chaves Nostr como identidade, sem servidor central de coordenação.

O projeto lançou 11 releases em sete dias, da [v0.2.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.2) até a [v0.2.13](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.13). Esse sprint adicionou suporte a Windows, pareamento LAN para descoberta em rede local e um sidecar Android para dispositivos móveis. A arquitetura é simples: dois dispositivos trocam metadados de conexão por relays Nostr e depois estabelecem um túnel WireGuard direto. Nostr lida com descoberta e sinalização para travessia de NAT. WireGuard cuida do tráfego real. A identidade é um par de chaves Nostr.

Malmi também continuou avançando [nostr-double-ratchet](https://github.com/mmalmi/nostr-double-ratchet), uma biblioteca de canal de mensagens seguras ao estilo Signal, com seis releases da [v0.0.86](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.86) até a [v0.0.93](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.93) durante a mesma semana.

### DOOM open-source roda peer-to-peer sobre o Nostr

A equipe do [Vector](https://github.com/VectorPrivacy/Vector) abriu o código de uma implementação multiplayer peer-to-peer de DOOM que usa Nostr para descoberta de pares, [Marmot](/pt/topics/marmot/) para criptografia end-to-end e [Iroh](https://github.com/n0-computer/iroh), a biblioteca de rede QUIC da n0, para transporte gossip. O jogo é distribuído como um arquivo WebXDC de 4,2 MB que pode ser enviado dentro de mensagens de chat, sem exigir servidores para hospedar ou coordenar uma partida.

A abordagem técnica substitui o lockstep netcode original de 1993 por um modelo híbrido de sincronização em tempo real. Jogadores se descobrem por consultas a relays Nostr, negociam sessões por canais criptografados com Marmot e então passam o tráfego de baixa latência do jogo para a camada gossip QUIC do Iroh. A stack usa Nostr para descoberta, Marmot para criptografia e Iroh para transporte.

O Vector também entregou endurecimento de segurança nesta semana. O release adiciona um key vault endurecido em memória com proteções anti-debug e zeroize para material de chave sensível, bloqueio de usuários com filtragem completa de DMs e mensagens de grupo, e correções do canal realtime WebXDC para Mini Apps.

### FIPS v0.2.0 lança transporte Tor, builds reproduzíveis e exemplos sidecar

[FIPS](https://github.com/jmcorgan/fips), o projeto Free Internetworking Peering System e de redes mesh adjacente ao Nostr, lançou [v0.2.0](https://github.com/jmcorgan/fips/releases/tag/v0.2.0-rel). O release adiciona suporte a transporte Tor para links mesh anonimizados, builds reproduzíveis, um exemplo sidecar que se conecta por um relay Nostr, e publicação de releases Nostr no workflow de pacotes OpenWrt. O release também corrige picos de jitter pós-rekey causados por drain-window frames. O wire format mudou em relação à v0.1.0, então nós existentes em v0.1.0 não podem interoperar com a v0.2.0 sem upgrade.

### Nostrability Schemata fica multilíngue

O projeto [Nostrability Schemata](https://github.com/nostrability/schemata), que mantém definições JSON Schema para validar kinds de evento Nostr, passou de JavaScript apenas para seis linguagens em uma semana. Novos pacotes foram lançados para Rust, Go, Dart, Swift e Python, cada um fornecendo tanto um pacote de dados quanto um validador. A [v0.2.6](https://github.com/nostrability/schemata/releases/tag/v0.2.6) também adicionou 17 novos schemas de kinds de evento.

O [tracker de interoperabilidade da Nostrability](https://nostrability.github.io/nostrability/) recebeu uma reformulação em paralelo. Uma nova aba What's New publica atualizações tanto por um feed Atom quanto por um evento Nostr, o filtro por categoria de app permite que visitantes foquem em tipos específicos de cliente, e o tracker agora detecta automaticamente linguagens de programação a partir dos metadados dos repositórios GitHub. A Nostrability também agora tem seu próprio npub, tornando o projeto descobrível pelo próprio protocolo que documenta. Para autores de bibliotecas que trabalham entre linguagens, os pacotes de schema multilíngues significam que as mesmas definições de kinds de evento ficam disponíveis como imports nativos em vez de exigir que cada projeto mantenha sua própria cópia dos schemas.

## Lançamentos

### Amethyst v1.06.0 e v1.06.1

[Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android mantido por vitorpamplona, lançou [v1.06.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.0) e [v1.06.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.1) em 23 de março. O principal recurso é suporte a enquetes usando dados [NIP-85](/pt/topics/nip-85/) (Trusted Assertions) para votação ponderada, com cards redesenhados de enquete e zap poll. A nova renderização dá tanto às enquetes padrão quanto às ponderadas por zap um layout visual mais limpo. A v1.06.1 vem em seguida com correções para crashes de modificação concorrente que tratam regressões de estabilidade introduzidas no caminho de renderização das enquetes.

### Amber v5.0.0 e v5.0.1

[Amber](https://github.com/greenart7c3/Amber), o app assinador [NIP-55](/pt/topics/nip-55/) (Android Signer Application), promoveu seu trabalho recente de pre-release da série 4.1.x para estável com a [v5.0.0](https://github.com/greenart7c3/Amber/releases/tag/v5.0.0) em 18 de março. Esse release estável traz o relay-auth [NIP-42](/pt/topics/nip-42/), Tor embutido, permissões específicas por tipo de conteúdo e armazenamento criptografado de PIN cobertos na semana passada. A [v5.0.1](https://github.com/greenart7c3/Amber/releases/tag/v5.0.1) então remove a permissão de internet do flavor offline, de modo que esse build não pode mais fazer requisições de rede na camada de permissões do Android.

### Mostro v0.17.0 e Mostro Mobile v1.2.2

[Mostro](https://github.com/MostroP2P/mostro), a exchange peer-to-peer de Bitcoin construída sobre Nostr, lançou [v0.17.0](https://github.com/MostroP2P/mostro/releases/tag/v0.17.0) em 18 de março. O release do servidor continua o trabalho de disputa e reputação do ciclo v0.16.x, adicionando dados mais completos de reputação comercial para compradores e vendedores como eventos Nostr. [Mostro Mobile](https://github.com/MostroP2P/mobile), o cliente Flutter, acompanhou com a [v1.2.2](https://github.com/MostroP2P/mobile/releases/tag/v1.2.2) em 23 de março, mantendo a interface mobile sincronizada com as mudanças mais recentes do protocolo.

### Shosho v0.14.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), o app de live streaming Nostr, lançou [v0.14.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.14.0) em 19 de março com o lançamento do Shosho Shop. O release adiciona uma aba Shop em perfis, Shop em Browse e um botão In-Live Shop em lives e clips. As release notes dizem que produtos Nostr existentes aparecem automaticamente e que compradores clicam até a página do vendedor no Plebeian Market para compra. As release notes do Shosho não identificam o kind de evento de listagem, então ainda não é possível confirmar se o Shosho Shop lê as mesmas listagens classificadas [NIP-99](/pt/topics/nip-99/) que [Shopstr](https://github.com/shopstr-eng/shopstr) suporta explicitamente em seu README.

### Applesauce v5.2.0

[Applesauce](https://github.com/hzrd149/applesauce), a coleção de pacotes auxiliares do hzrd149 para construir aplicações Nostr, lançou [v5.2.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core@5.2.0) em 22 de março. O release cobre seis pacotes. O pacote SQLite corrige uma colisão de constraint UNIQUE em tags de evento que causava inserts duplicados. O pacote signers adiciona `AndroidNativeSigner`, que encapsula a interface nativa do assinador Android [NIP-55](/pt/topics/nip-55/) para que apps baseados em web-view possam usar assinatura com hardware backing sem bridge code customizado. O pacote relay adiciona um campo `challenge` aos objetos de status de relay e pool, rastreando estado de auth [NIP-42](/pt/topics/nip-42/) para que apps possam detectar quando um relay está pedindo autenticação e responder programaticamente. O pacote core ganha métodos `isEventPointerSame` e `isAddressPointerSame` para deduplicar referências de eventos, e o pacote common adiciona `user.blossomServers$` para resolver os servidores Blossom de um usuário. Applesauce alimenta noStrudel, Satellite e vários outros clientes web, então essas correções se propagam pela camada de clientes web.

### Wisp lança 16 releases em uma semana

[Wisp](https://github.com/barrydeen/wisp), o cliente Nostr para Android, lançou 16 releases da [v0.9.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.9.3-beta) até a [v0.13.1-beta](https://github.com/barrydeen/wisp/releases/tag/v0.13.1-beta) nesta semana. As adições de recursos incluem suporte a múltiplas contas, um modo zen de notificações para reduzir interrupções, rascunhos e posts agendados, filtros de conteúdo de segurança e um novo ícone de chama.

### Manent v1.2.0

[Manent](https://github.com/dtonon/manent), o app privado de notas criptografadas e armazenamento de arquivos, lançou [v1.2.0](https://github.com/dtonon/manent/releases/tag/v1.2.0) em 20 de março. O release adiciona captura de câmera diretamente do app, redimensionamento de imagem antes do upload para reduzir custos de armazenamento, e pinch-to-zoom para revisar imagens armazenadas. O Manent armazena notas e arquivos criptografados em relays Nostr usando o par de chaves do usuário, tornando o app de telefone ou desktop um cliente fino que pode reconstruir seu estado completo a partir dos dados dos relays.

### diVine 1.0.7

[diVine](https://github.com/divinevideo/divine-mobile), o cliente de vídeo short-form, lançou [1.0.7](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.7) em 21 de março com um watchdog de reprodução de vídeo que retoma automaticamente vídeos travados. Depois da infraestrutura de testes E2E e do carregamento direto de MP4 na [v1.0.6](/en/newsletters/2026-03-11-newsletter/#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import), este release mira o caminho de falha remanescente de reprodução: vídeos que param no meio do stream sem lançar erro.

### Alby Extension v3.14.2

[Alby Extension](https://github.com/getAlby/lightning-browser-extension), a extensão de navegador [NIP-07](/pt/topics/nip-07/) (Browser Extension Signer), lançou [v3.14.2](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.2) em 18 de março com exibição de QR code de endereço Lightning e suporte a assinatura Schnorr. A adição de Schnorr alinha a extensão de navegador ao esquema de assinatura secp256k1 que o Nostr usa nativamente.

### NoorNote v0.6.5 até v0.6.11

[NoorNote](https://github.com/77elements/noornote), o app de anotações, lançou sete releases da [v0.6.5](https://github.com/77elements/noornote/releases/tag/v0.6.5) até a [v0.6.11](https://github.com/77elements/noornote/releases/tag/v0.6.11). A principal adição é Follow Packs: conjuntos curados de contas que usuários podem navegar e seguir em massa, semelhantes às Twitter Lists, mas pensados para onboarding. Usuários podem criar, editar e compartilhar Follow Packs com títulos, descrições e imagens de capa personalizados. A série também atualiza a biblioteca Nostr subjacente de NDK v2 para v3, que traz melhor tratamento de conexão de relay e gerenciamento de subscriptions. Picture notes e uma experiência redesenhada de conexão de relay completam a sequência.

### nak v0.19.1 e v0.19.2

[nak](https://github.com/fiatjaf/nak), o toolkit de linha de comando Nostr do fiatjaf para interagir com relays, codificar e decodificar identificadores [NIP-19](/pt/topics/nip-19/) (Bech32-Encoded Entities), assinar eventos e consultar dados de relay, lançou [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1) e [v0.19.2](https://github.com/fiatjaf/nak/releases/tag/v0.19.2) em 17 e 20 de março. Os dois point releases seguem a adição de UI de fórum de grupo da [v0.19.0](/pt/newsletters/2026-03-18-newsletter/) da semana passada.

### Calendar by Form* v0.2.1

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), o app de calendário descentralizado construído sobre [NIP-52](/pt/topics/nip-52/) (Calendar Events), lançou [v0.2.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.1) em 20 de março. O release corrige um problema de template de notificação que afetava lembretes de eventos. O Calendar armazena eventos como eventos Nostr kind 31922 (baseados em data) e kind 31923 (baseados em hora), permitindo que qualquer cliente Nostr renderize dados de calendário se escolher suportar esses kinds. O app é construído pela equipe Formstr, que também mantém Formstr (formulários descentralizados) e Pollerama (enquetes).

### NYM v3.50 até v3.53

[NYM](https://github.com/Spl0itable/NYM), o cliente leve de chat efêmero com bridge para Bitchat, lançou 28 releases de v3.50 até v3.53. O recurso mais notável é o Nymbot, um chat bot embutido que responde a menções `@nymbot` em canais e fornece funções de status e gerenciamento de relay. Um "hardcore mode" gera um novo par de chaves para cada mensagem enviada, tornando threads de conversa desvinculáveis no nível de identidade. O tradeoff é claro: perde-se identidade persistente, mas ganha-se anonimato por mensagem. A camada de relay proxy também recebeu trabalho, com workers sharded de relay proxy para melhor conectividade, suporte a canais geohash e tolerância a clock skew para nós com relógios de sistema imprecisos.

## Atualizações de Projetos

### Ditto adiciona ponte com Bluesky e integração com Wikipedia

[Ditto](https://github.com/soapbox-pub/ditto), o cliente social Nostr customizável da equipe Soapbox, registrou mais de 300 commits nesta semana em três trilhas distintas de recursos. A primeira é uma ponte com Bluesky (19 commits) que renderiza posts do Bluesky inline como threads completas ao estilo feed, adiciona navegação lateral para uma página de descoberta do Bluesky baseada no feed oficial Discover (whats-hot), e conecta botões de ação para comentar, compartilhar, reagir e copiar links. Quando um usuário responde a um post do Bluesky dentro do Ditto, o modal de composição mostra um aviso destacando a natureza cross-protocol da interação. Reações kind 17 do [NIP-73](/pt/topics/nip-73/) (External Content IDs) impulsionam esse modelo cross-protocol: um usuário Nostr reage a um post do Bluesky, e a reação é armazenada como um evento Nostr padrão referenciando o identificador de conteúdo externo. É o mesmo padrão NIP-73 que poderia fazer ponte de reações a qualquer conteúdo externo, de posts do Bluesky a vídeos do YouTube e páginas web.

A segunda trilha é uma integração com Wikipedia (9 commits). O Ditto agora renderiza conteúdo rico de artigos da Wikipedia em páginas de detalhe em vez de previews genéricos de link, adiciona autocomplete de busca com thumbnails de artigo, e fornece uma página `/wikipedia` puxando conteúdo em destaque da API da Wikipedia. Resultados da Wikipedia e do Archive.org também aparecem no dropdown geral de autocomplete de busca. A terceira trilha é suporte à plataforma iOS via Capacitor, com script de build remoto e configuração de plataforma chegando junto a uma reformulação de UI (55 commits) que substitui headers com backdrop blur por um novo design de navegação em arco em todas as páginas do app. Os 314 commits movem o Ditto de um cliente apenas Nostr para um agregador multiprotocolo que trata Bluesky e Wikipedia como fontes de conteúdo de primeira classe ao lado do feed Nostr.

### Pika constrói um pipeline de CI para forge NIP-34

[Pika](https://github.com/sledtools/pika), o app de mensagens criptografadas baseado em Marmot, mergeou 33 PRs nesta semana focados em um forge [NIP-34](/pt/topics/nip-34/) self-hosted com CI pré-merge. O forge é uma camada de hospedagem git que recebe patches como eventos NIP-34, executa verificações de CI antes do merge e reporta status estruturado de volta por eventos Nostr. O [PR #701](https://github.com/sledtools/pika/pull/701) adiciona CI pré-merge e noturna por lanes, onde cada caminho de código (Rust, TypeScript, builds Apple) roda em sua própria lane com status pass/fail independente. O [PR #715](https://github.com/sledtools/pika/pull/715) reduz agentes de CI gerenciados para containers Incus OpenClaw para isolamento, e o [PR #733](https://github.com/sledtools/pika/pull/733) adiciona um CLI `ph forge` para interagir com o forge hospedado pela linha de comando. PRs de suporte tratam permissões de escrita no repositório para merges ([PR #736](https://github.com/sledtools/pika/pull/736)), metadados estruturados de CI com badges de status ao vivo ([PR #722](https://github.com/sledtools/pika/pull/722)), splits de nightly builds Apple ([PR #738](https://github.com/sledtools/pika/pull/738)), e correções de auth do forge e branch lookup ([PR #734](https://github.com/sledtools/pika/pull/734)). Este é um dos primeiros sistemas CI/CD funcionais construídos sobre eventos git NIP-34, levando a hospedagem de código-fonte baseada em Nostr além da simples troca de patches em direção ao workflow de merge e teste que desenvolvedores esperam de GitHub ou GitLab.

### Nostria adiciona comunidades, snippets de código e tratamento de eventos de voz

[Nostria](https://github.com/nostria-app/nostria), o cliente Nostr multiplataforma mantido por sondreb, passou esta semana expandindo a superfície do app além da filtragem Web of Trust coberta na edição #14. A principal adição é uma implementação completa do [NIP-72](/pt/topics/nip-72/) (Moderated Communities) com criação de comunidade, configuração de moderadores e relays, rastreamento de aprovação de posts com previews de imagem e uma página dedicada de comunidade com abas Posts e Moderators.

O mesmo trecho de trabalho também adiciona renderização e edição de snippets de código com um editor com syntax highlighting, suporte a resposta a eventos de voz para conversas em áudio, configurações de relay de chat para mensagens diretas, compartilhamento de canal pela Web Share API, um sistema de docking de toolbar para o media player, cadastro in-app no serviço mais recente do Brainstorm Web of Trust, fluxos de envio e recebimento de dinheiro em DMs usando NWC e invoices BOLT-11, tratamento de GIFs nativo do Nostr e um caminho mais forte de importação RSS para músicos que consegue capturar Lightning splits existentes de feeds de podcast.

### nostr-vpn em iteração rápida

Além do [lançamento inicial](#nostr-vpn-é-lançado-como-alternativa-ao-tailscale), o log de commits do [nostr-vpn](https://github.com/mmalmi/nostr-vpn) revela os problemas específicos encontrados durante deployment real. A [v0.2.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.3) até a [v0.2.5](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.5) adicionaram o script inicial de instalação e o CLI cross-platform. A [v0.2.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.6) e a [v0.2.7](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.7) trouxeram suporte a Windows, o que exigiu quoting de caminhos com UAC para escrita de configuração e atualizações de config pertencentes ao daemon. A [v0.2.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.8) até a [v0.2.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.10) corrigiram ações de serviço na GUI do Windows, tratamento de subprocessos do CLI e configuração de serviço no escopo da máquina. A [v0.2.12](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.12) substituiu descoberta LAN por timed LAN pairing, um fluxo iniciado pelo usuário em que dois dispositivos na mesma rede local se pareiam sem sinalização via relay. O padrão é típico de testes de campo em estágio inicial: cada release mira uma falha específica de deployment, a base de usuários é pequena o suficiente para iterar diariamente, e o desenvolvedor está usando a ferramenta pessoalmente entre releases.

### Comet e builds automatizados

[Comet](https://github.com/nodetec/comet) (antigo Captain's Log), a ferramenta nativa do Nostr para escrita long-form da Nodetec, produziu mais de 40 builds alpha automatizados nesta semana. O Comet é um app desktop para escrever e publicar artigos NIP-23 (Long-form Content), com armazenamento local de rascunhos, edição Markdown e publicação com um clique para o conjunto de relays do usuário. O pipeline automatizado de builds gera um release tagueado para cada commit na branch main, o que torna a contagem bruta de releases enganosa como medida de velocidade de recursos. O que os 40 builds mostram é que o app está sob desenvolvimento ativo diário, com cada commit testado, empacotado e disponibilizado para download em minutos.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips) durante a janela de 17 a 24 de março:

Nenhum merge de NIP ocorreu entre 18 e 24 de março.

**PRs Abertos e Discussões atualizados durante a janela:**

- **NIP-AA: Autonomous Agents on Nostr** ([PR #2259](https://github.com/nostr-protocol/nips/pull/2259)): Propõe convenções para agentes autônomos operando na rede Nostr. O PR define como agentes se identificam, descobrem serviços e se coordenam com outros agentes e humanos por eventos Nostr.

- **[NIP-50](/pt/topics/nip-50/) (Search): Extensões de ordenação** ([PR #2283](https://github.com/nostr-protocol/nips/pull/2283)): Adiciona parâmetros de ordenação a consultas de busca NIP-50, incluindo top, hot, zaps e new. Isso permitiria que clientes solicitassem resultados ranqueados de relays com suporte a full-text search em vez de ordenar do lado do cliente.

- **NIP-A5: WASM Programs** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Propõe uma convenção para publicar e descobrir programas WebAssembly no Nostr. Binários WASM poderiam ser distribuídos como eventos Nostr, com relays servindo como camada de descoberta para código executável portável.

- **NIP-CF: Combine Forces interoperable napps** ([PR #2277](https://github.com/nostr-protocol/nips/pull/2277)): Define uma convenção para aplicações Nostr interoperáveis ("napps") que podem compor funcionalidades entre diferentes clientes e serviços.

- **Snapshots NIP** ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279)): Propõe um mecanismo de snapshots de estado de relay, para sincronização e backup de relays.

- **Checkpoints NIP** ([PR #2278](https://github.com/nostr-protocol/nips/pull/2278)): Propõe eventos de checkpoint para marcar estado conhecido como bom de relay, complementando a proposta de snapshots.

- **[NIP-58](/pt/topics/nip-58/) (Badges): Refatoração de Badge Sets** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Reestrutura como coleções de badges são organizadas e referenciadas.

- **[NIP-11](/pt/topics/nip-11/) (Relay Information Document): Extensões** ([PR #2280](https://github.com/nostr-protocol/nips/pull/2280)): Adiciona campos extras ao relay information document para metadados de relay legíveis por máquina mais ricos.

## Cinco Anos de Marços do Nostr

[A newsletter do mês passado](/pt/newsletters/2026-03-04-newsletter/#five-years-of-nostr-februaries) cobriu como os fevereiros do Nostr progrediram desde a reescrita do NIP-01 (Basic Protocol Flow), passando pela onda do Damus na App Store, até redes mesh e propostas de agentes. Esta retrospectiva traça o que aconteceu em cada março de 2021 até 2026.

### Março de 2021: Dois Commits

Quatro meses após sua existência, o mês de março do Nostr produziu exatamente dois commits no repositório do protocolo, ambos em 4 de março. fiatjaf [adicionou links para instâncias nostwitter](https://github.com/nostr-protocol/nostr/commit/dcd8cc3), apontando visitantes iniciais para deployments funcionais, e [adicionou kind à definição básica de filtro](https://github.com/nostr-protocol/nostr/commit/54dfb46). Esse segundo commit é revelador: em março de 2021, ainda não era possível filtrar eventos Nostr por kind. O protocolo era tão primitivo assim. Dois ou três relays serviam a rede. O grupo no Telegram era o único canal de coordenação. O repositório de NIPs ainda não existia; propostas de protocolo viviam como arquivos no repositório principal do nostr. fiatjaf foi o único committer naquele mês. Toda a produção de março de 2021 daquilo que se tornaria um protocolo suportando VPNs, jogos multiplayer e redes mesh cinco anos depois cabe em um único git diff.

### Março de 2022: Construção pré-Damus

O repositório principal do protocolo recebeu zero commits em março de 2022. O desenvolvimento havia migrado inteiramente para repositórios de ferramentas. [Branle](https://github.com/fiatjaf/branle), o cliente web em Vue.js do fiatjaf e na época a principal interface Nostr, recebeu 5 commits incluindo suporte a deployment com Docker e correções de display name [NIP-05](/pt/topics/nip-05/) (DNS-Based Verification) que removiam o prefixo `_@` dos badges de verificação. O [more-speech](https://github.com/unclebob/more-speech) de Robert C. Martin, o cliente desktop em Clojure, registrou 13 ou mais commits adicionando threading, navegação por teclado e uma janela de edição. O autor de software mais famoso construindo ativamente sobre Nostr naquele mês não era um desenvolvedor cripto, mas a pessoa cujo "Clean Code" vendeu milhões de cópias, escrevendo um cliente Nostr em Clojure, uma escolha de linguagem que diz tudo sobre a comunidade inicial: eram programadores opinativos construindo para si mesmos.

A rede de relays havia se expandido para cerca de 15 relays com uma base ativa de usuários na casa das centenas. O Damus ainda não existia e só seria criado em abril de 2022. O Nostream também ainda não havia aparecido. O trabalho do mês foi infraestrutura: tornar as ferramentas existentes mais confiáveis para a pequena comunidade que já as usava diariamente.

### Março de 2023: Infraestrutura pós-explosão

Um mês após a onda do Damus na App Store e o salto acima de 300.000 chaves públicas, março de 2023 foi sobre absorver o crescimento. O [repositório de NIPs](https://github.com/nostr-protocol/nips) mergeou 28 pull requests, a segunda maior contagem mensal da história do protocolo. [NIP-51](/pt/topics/nip-51/) (Lists) foi mergeado, dando aos clientes coleções estruturadas de follows, mutes e bookmarks. [NIP-39](/pt/topics/nip-39/) (External Identities in Profiles) chegou, o NIP-78 (Application-Specific Data) forneceu um kind de armazenamento de propósito geral para apps que precisavam de estado privado, e uma reescrita do [NIP-57](/pt/topics/nip-57/) (Lightning Zaps) ([PR #392](https://github.com/nostr-protocol/nips/pull/392)) consolidou o fluxo de zap e clarificou a terminologia. O PR mais discutido do mês foi uma proposta alternativa de tratamento de mentions ([PR #381](https://github.com/nostr-protocol/nips/pull/381)) com mais de 50 comentários.

O novo projeto mais consequente foi o [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit), a biblioteca TypeScript para conexões de relay, assinatura de eventos, cache e gerenciamento de subscriptions. pablof7z fez o [commit inicial](https://github.com/nostr-dev-kit/ndk/commit/09e5e03) em 16 de março de 2023, depois o reescreveu do zero 11 dias depois em 27 de março ("basically another initial commit"), e já tinha suporte a LNURL e zap funcionando até 31 de março. O NDK saiu do zero para suportar zaps em 15 dias. Cinco dias após a criação do NDK, em 21 de março, a equipe do Alby criou o [NWC](https://github.com/getAlby/nostr-wallet-connect) (Nostr Wallet Connect), a implementação de referência do [NIP-47](/pt/topics/nip-47/) que conectava carteiras Lightning a aplicações Nostr. Os dois projetos que sustentariam os três anos seguintes de desenvolvimento Nostr baseado na web nasceram na mesma janela de 30 dias. A OpenSats ainda não havia lançado seu fundo Nostr; a primeira onda só viria em [julho de 2023](https://opensats.org/blog/nostr-grants-july-2023), quatro meses após a criação do NDK.

Outras criações notáveis naquele mês incluíram NostrGit, NostrChat, um projeto nostr-signing-device da LNbits e nostrmo. [Gossip](https://github.com/mikedilger/gossip), o cliente desktop em Rust focado em seleção inteligente de relay, lançou três releases. O protocolo estava em modo de construção, e as ferramentas criadas em março de 2023 ainda estão em uso três anos depois.

### Março de 2024: Maturação do protocolo

Março de 2024 foi sobre endurecer o protocolo para uso de longo prazo. O repositório de NIPs mergeou 12 pull requests. A mais significativa foi [NIP-34](/pt/topics/nip-34/) (Git Stuff), [PR #997](https://github.com/nostr-protocol/nips/pull/997), mergeada em 5 de março após mais de 130 comentários e 44 dias de review. A thread de discussão é uma cápsula do tempo da comunidade debatendo como construir um GitHub descentralizado. jb55 traçou paralelos com `git send-email`, Giszmo propôs usar hashes de root commit para descoberta entre forks ("something GitHub doesn't do and we could"), mikedilger sugeriu autenticação assinada por evento [NIP-98](/pt/topics/nip-98/) (HTTP Auth) em vez de chaves SSH, e fiatjaf descartou sem rodeios a necessidade de generalidade para controle de versão: "not for each version control system, just for git. No one uses the others." Em poucas horas após abrir o PR, fiatjaf já havia ajustado nak, go-nostr e gitstr para aceitar patches sobre Nostr. DanConwayDev, cujo ngit já era bolsista da OpenSats, esteve entre os contribuidores mais ativos da discussão. Um campo de bot para metadados de perfil também foi mergeado, dando aos clientes uma forma legível por máquina de distinguir contas automatizadas de humanas.

[Amethyst](https://github.com/vitorpamplona/amethyst) lançou v0.85.0 com suporte a eventos git, artigos wiki, renderização de dados médicos e edição de conteúdo em um único release. [Mostro](https://github.com/MostroP2P/mostro) chegou à v0.10.0. [Nosflare](https://github.com/Spl0itable/nosflare), um relay Nostr serverless rodando em Cloudflare Workers, provou que lógica de relay pode rodar na edge. A OpenSats emitiu uma [bolsa Long-Term Support para Bruno Garcia](https://opensats.org/blog/bruno-garcia-receives-lts-grant) por contribuições sustentadas ao cliente Amethyst.

### Março de 2025: Expansão de infraestrutura

Março de 2025 produziu 10 NIPs mergeados. O destaque foi [NIP-66](/pt/topics/nip-66/) (Relay Discovery and Liveness Monitoring), [PR #230](https://github.com/nostr-protocol/nips/pull/230), mergeado em 3 de março após uma jornada de 25 meses. dskvr primeiro propôs monitoramento de relays em fevereiro de 2023, ouviu que isso poderia ser feito do lado do cliente, explicou por que conectar-se a milhares de relays ao mesmo tempo era impraticável para clientes individuais, passou por sete drafts completos, construiu nós de monitoramento em oito regiões geográficas (Nordeste dos EUA, Brasil, Oeste dos EUA, Leste dos EUA, Austrália, Índia, Coreia e África do Sul) e esperou o ferramental de relay amadurecer. Quando foi mergeado, implementações já existiam em nostr.watch, relaypag.es, monitorlizard, Snort, noStrudel e Jumble. Os dados do NIP-66 depois alimentariam os benchmarks outbox da Nostrability [cobertos na Newsletter #12](/pt/newsletters/2026-03-04-newsletter/#outbox-model-under-the-microscope). O NIP-C0 (Code Snippets) também foi mergeado ([PR #1852](https://github.com/nostr-protocol/nips/pull/1852), 63 comentários), adicionando eventos kind 1337 para compartilhamento de código-fonte.

Os primeiros servidores MCP para Nostr apareceram nesse mês. [nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server) apareceu em 23 de março e [nwc-mcp-server](https://github.com/getAlby/nwc-mcp-server) em 14 de março, apenas quatro meses após a Anthropic anunciar o Model Context Protocol em novembro de 2024. Essas pontes iniciais precederam o SDK completo [ContextVM](/pt/topics/contextvm/) e o trabalho posterior de comércio de agentes no fim de 2025 e início de 2026.

[Gossip](https://github.com/mikedilger/gossip) lançou v0.14.0. [Coracle](https://github.com/coracle-social/coracle), o cliente web do hodlbod com gerenciamento de feed sensível a relays, lançou três releases. A OpenSats anunciou sua [décima onda de bolsas Nostr](https://opensats.org/blog/10th-wave-of-nostr-grants), continuando a linha de financiamento que vinha desde meados de 2023.

### Março de 2026: Convergência

*A atividade de março de 2026 é extraída das edições do Nostr Compass [#12](/pt/newsletters/2026-03-04-newsletter/) até [#15](#) (esta edição).*

Março de 2026 é o mês em que linhas antes separadas convergiram em sistemas funcionais. O [Marmot Development Kit](/pt/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release) lançou sua primeira versão pública com mídia criptografada, bindings multi-linguagem e uma migração para ChaCha20-Poly1305 que exigiu atualizações coordenadas entre spec, Rust e TypeScript. [Shopstr e Milk Market](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces) adicionaram superfícies de comércio MCP para compras dirigidas por agentes. O relay auth [NIP-42](/pt/topics/nip-42/) chegou simultaneamente em [Amber](/en/newsletters/2026-03-11-newsletter/#nip-42-relay-auth-across-bunker-signer-and-relay), strfry e OAuth Bunker, fechando o loop entre software de signer, relay e bunker. [Notedeck](/pt/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr) lançou atualizações de software nativas do Nostr usando eventos de release [NIP-94](/pt/topics/nip-94/) (File Metadata).

Nesta semana, [BigBrotr](#bigbrotr-mapeia-chaves-privadas-expostas-na-rede-de-relays) escaneou a rede completa de relays em busca de chaves privadas vazadas e publicou tanto a análise quanto um verificador DVM. [Nostr VPN](#nostr-vpn-é-lançado-como-alternativa-ao-tailscale) provou que o modelo de chaves do Nostr funciona para infraestrutura de rede, não apenas para mídia social. [DOOM](#doom-open-source-roda-peer-to-peer-sobre-o-nostr) demonstrou que descoberta via Nostr, criptografia Marmot e transporte QUIC podem rodar um jogo multiplayer em tempo real. [Amber](#amber-v500-e-v501) saltou para v5.0.0. [Wisp](#wisp-lança-16-releases-em-uma-semana) lançou 16 releases em sete dias. Vinte e cinco ou mais releases tagueados vieram de projetos importantes em uma única semana.

Sete NIPs foram mergeados nos primeiros 24 dias do mês. O protocolo adicionou marcação Djot ao [NIP-54](/pt/topics/nip-54/) (Wiki), limites de entrada ao [NIP-19](/pt/topics/nip-19/) (Bech32-Encoded Entities), lógica booleana de consulta ao [NIP-91](/pt/topics/nip-91/) (AND Operator for Filters), e assertions de Web of Trust ao [NIP-85](/pt/topics/nip-85/) (Trusted Assertions). Propostas abertas iam de agentes autônomos (NIP-AA) a programas WASM (NIP-A5) e extensões de ordenação de busca para [NIP-50](/pt/topics/nip-50/).

### Olhando para frente

Cinco marços do Nostr traçam um arco claro. Em 2021, uma pessoa fez dois commits em um protocolo que ainda não conseguia filtrar eventos por kind. Em 2023, NDK e NWC nasceram com cinco dias de diferença para absorver a explosão pós-Damus. Em 2024, uma thread de PR com 141 comentários debateu como colaboração git deveria funcionar sobre um protocolo social. Em 2025, uma spec de monitoramento de relays que havia sido pacientemente reescrita sete vezes ao longo de 25 meses finalmente foi mergeada. Em 2026, alguém se irritou com o fato de o Tailscale exigir conta e construiu uma VPN usando pares de chaves Nostr, enquanto outra pessoa lançou DOOM multiplayer que descobre pares por relays Nostr e criptografa a jogabilidade com Marmot. O escaneamento de 41 milhões de eventos em 1.085 relays pelo BigBrotr dá uma medida concreta de quanto a rede cresceu. A área de superfície do protocolo em março de 2026 seria irreconhecível para março de 2021, mas o modelo subjacente, eventos assinados por chaves secp256k1 e distribuídos por relays, não mudou.

---

É isso por esta semana. Construindo algo ou tem novidades para compartilhar? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via [NIP-17](/pt/topics/nip-17/) (Private Direct Messages) DM</a> ou nos encontre no Nostr.
