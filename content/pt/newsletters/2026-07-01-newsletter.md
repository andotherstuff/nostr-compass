---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
translationOf: /en/newsletters/2026-07-01-newsletter.md
translationDate: 2026-07-01
draft: false
type: newsletters
---

Bem-vindos de volta ao Nostr Compass, seu guia semanal do Nostr.

**Esta semana:** o [FIPS v0.4.0](#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul) traz transporte pela mixnet Nym, descoberta opt-in na LAN via mDNS, troca de chaves sem interrupções sob perda de pacotes e uma reformulação do plano de dados, mantendo compatibilidade de rede com a v0.3.0. O [Whitenoise Linux](#whitenoise-linux-surfaces-as-a-desktop-marmot-client) surge como cliente Marmot para desktop em Rust e Slint, acompanhado de uma proposta de protocolo para mover efeitos de mensagens para um evento kind 9 dedicado. O [CustID v0.1.10-beta](#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow) é lançado como um cofre móvel de identidades respaldado por hardware, que atua como assinador remoto NIP-46 e responde a desafios de acesso físico via NFC. O [myco](#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh) estreia o compartilhamento ponto a ponto de nsites pela malha FIPS, com um novo transporte BLE L2CAP na v0.1.0. O [Nostr Codex Phone](#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr) é lançado como uma superfície de controle Android para um assistente de programação Codex local por DMs criptografadas do Nostr. A [linha ainda não lançada do Amethyst](#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section) adiciona parsing de handlers de aplicativos NIP-89, um feed de repositórios Git para NIP-34 e uma seção Discover para nSites e napplets. O [Notedeck](#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments) implementa NIP-37, NIP-52 e NIP-22 em uma semana. O [Applesauce](#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut) lança 12 versões de subpacotes, com auxiliares nbunksec para NIP-46 e atualização da carteira para Cashu-ts v4. O [Meiso v1.4.0](#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing) traz listas colaborativas de chave compartilhada em eventos endereçáveis kind 35000. O repositório de NIPs incorporou cinco PRs, entre eles um evento de funções de relay, a remoção do limite de 65.535 bytes do NIP-44, semântica de forks do NIP-34, metadados de cliente NIP-46 e o método `signevent` do NIP-86. Os mergulhos profundos abordam o [NIP-86 (API de gerenciamento de relays)](#nip-deep-dive-nip-86-relay-management-api) e o [NIP-89 (handlers de aplicativos recomendados)](#nip-deep-dive-nip-89-recommended-application-handlers).

---

## Histórias principais

### FIPS v0.4.0 traz transporte pela mixnet Nym, descoberta mDNS e uma reformulação do plano de dados {#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul}

O [FIPS](https://github.com/jmcorgan/fips) é uma rede mesh ponto a ponto privada e auto-organizável para o Nostr, na qual os nós descobrem uns aos outros e roteiam tráfego sem infraestrutura central. O [FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) incorpora um transporte pela mixnet Nym, descoberta opt-in na LAN via mDNS, uma reformulação do plano de dados, troca de chaves sem interrupções sob perda de pacotes, uma TUI `fipstop` reescrita sobre um harness de snapshots de renderização, um plano de observabilidade fora do caminho crítico e novos alvos de empacotamento apk para OpenWrt e flake para Nix. Tudo mantém compatibilidade de rede com a v0.3.0, para que malhas com versões mistas interoperem durante uma atualização gradual. Dois novos transportes para descoberta de peers sustentam o lançamento. Um novo [transporte de saída pela mixnet Nym](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) roteia o tráfego FIPS por um proxy SOCKS5 `nym-socks5-client`, misturando-o à rede de tráfego de cobertura da [Nym](https://nymtech.net/) para impedir que observadores no nível do link correlacionem quais peers da malha estão se comunicando. Um diretório `examples/sidecar-nostr-mixnet-relay/` demonstra um relay Nostr acessível por um link FIPS pareado de ponta a ponta através da mixnet. A descoberta opt-in na LAN via mDNS/DNS-SD permite que nós no mesmo link local se encontrem sem configurar endereços nem usar STUN, anunciando e adotando peers por um registro de serviço padrão quando `node.discovery.lan.enabled: true`.

O plano de dados foi reformulado para aumentar a vazão de um único nó. A criptografia e a descriptografia por peer agora rodam em workers dedicados fora do loop de recebimento, para que um peer ocupado não serialize a criptografia de todo o nó. No Linux, o caminho de envio usa generic segmentation offload e, quando disponível, um socket UDP conectado; o caminho crítico de recebimento evita as cópias de buffer antes realizadas para cada pacote; e o macOS ganha recebimento em lote com `recvmsg_x`, espelhando o lote `recvmmsg` do Linux introduzido na v0.3.0. Toda a superfície de leitura `show_*` do `fipsctl` e do `fipstop` agora é atendida por um snapshot por tick, publicado em um `ArcSwap` lock-free pela tarefa que aceita conexões de controle. Assim, consultas do operador respondem rapidamente mesmo quando o loop de recebimento está ocupado. Uma nova consulta `show_metrics`, apenas de contadores e exposta como `fipsctl stats metrics`, permite coleta pelo Prometheus sem custo no caminho crítico.

A troca de chaves das sessões FMP e FSP agora ocorre sem interrupções sob perda e reordenação de pacotes nas duas direções: frames recebidos são autenticados contra a sessão pendente antes que a transição pelo bit K a promova, impedindo que um frame antigo ou falsificado atrapalhe a troca; a retransmissão da mensagem 1 da troca de chaves é limitada; o heartbeat que detecta link inativo considera a troca; e corridas de iniciação dupla em links de alta latência são dessincronizadas com jitter simétrico. A TUI `fipstop` foi reconstruída sobre um harness de snapshots de renderização que valida o grid de texto exato e o estilo de cada célula de todas as telas contra saídas predefinidas do socket de controle. Novos alvos de empacotamento acompanham o lançamento: um `.apk` para OpenWrt 25 ou posterior, criado sem SDK ao reutilizar a compilação cruzada `.ipk` e o payload do sistema de arquivos instalado já existentes, e um `flake.nix` na raiz do projeto que compila os quatro binários (`fips`, `fipsctl`, `fips-gateway`, `fipstop`) a partir do código-fonte no Nix/NixOS com a toolchain fixada.

### Whitenoise Linux surge como cliente Marmot para desktop {#whitenoise-linux-surfaces-as-a-desktop-marmot-client}

O [Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git) é um cliente [Marmot](/pt/topics/marmot/) para desktop: mensagens de grupo MLS sobre relays Nostr, empacotadas em um único binário Rust com uma interface Slint que mantém todos os segredos em um cofre criptografado por senha.

A discussão mais relevante desta semana propõe transportar os efeitos de mensagens do Whitenoise em um evento kind 9 dedicado que referencia a mensagem original. O formato de rede atual acrescenta um marcador como `dmfx:sparkle` ao final do corpo da mensagem, poluindo o texto para qualquer renderizador que desconheça essa convenção. Mover os efeitos para eventos próprios mantém limpo o texto das mensagens e abre uma questão de design que todo o ecossistema Marmot terá de enfrentar: convenções embutidas no corpo ou eventos sidecar para recursos avançados opcionais.

### CustID é lançado como cofre móvel de identidades com NIP-46 e fluxo de desafios via NFC {#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow}

O [CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c) é a primeira beta pública do CustID, um cofre móvel de identidades baseado no Nostr e no protocolo SISTR. O CustID armazena várias identidades Nostr em armazenamento seguro respaldado por hardware, atua como assinador remoto [NIP-46](/pt/topics/nip-46/) para outros clientes e responde a desafios de acesso físicos e on-line por NFC e códigos QR.

A beta tem todos os recursos previstos para o assinador NIP-46 e o fluxo de desafio e resposta via NFC; os fluxos de acesso com provas de conhecimento zero continuam como objetivo futuro. Este lançamento também remove a camada de keep-alive [NIP-65](/pt/topics/nip-65/) em segundo plano do aplicativo, que abria um WebSocket por perfil para cada relay de leitura e recebia kinds descartados imediatamente pelo cliente. Agora, somente os sockets NIP-46 que transportam notificações de solicitações de assinatura permanecem ativos em segundo plano, correção que viabiliza usar o CustID como bunker para outros clientes em um celular.

### myco lança compartilhamento ponto a ponto de nsites pela malha FIPS {#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh}

O [myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0) foi aberto em 27 de junho e chegou à v0.1.0 em 1º de julho. O myco é um aplicativo Android em Rust que instala aplicativos recebidos de pessoas próximas: compartilhamento ponto a ponto de [nsites](/pt/topics/nip-5a/) por uma malha FIPS, usando qualquer transporte aceito pela malha (UDP, TCP, Tor, Bluetooth) e funcionando totalmente off-line. O design combina diretamente o FIPS como base de transporte com o formato de evento de sites estáticos do NIP-5A como payload, permitindo que um aplicativo distribuído como nsite passe entre peers da malha sem depender de relays nem HTTP.

A v0.1.0 adiciona um caminho de rádio Bluetooth L2CAP para que dois celulares com FIPS instalado possam se parear por BLE sem nenhuma rede, além de um teste de velocidade por peer e compartilhamento acionado por NFC na bottom sheet Circle do aplicativo. O myco também está publicado no Zapstore para instalação direta.

### Nostr Codex Phone é lançado como superfície de controle móvel para um worker Codex local pelo Nostr {#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr}

O [Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone) é lançado nesta semana como cliente Android que controla um worker local do assistente de programação Codex por mensagens diretas criptografadas do Nostr. O aplicativo aceita várias sessões de repositório, transcrição de voz, sessões roteadas do worker, uploads de mídia para Blossom e respostas faladas opcionais. Assim, quem executa um worker Codex em casa pode enviar solicitações pelo celular em qualquer lugar onde tenha acesso a relays.

O projeto é irmão direto do [CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr), lançado na edição nº 28. Ambos colocam fluxos de programação agêntica sobre o transporte Nostr com DMs criptografadas e tratam o Nostr como a camada de pareamento e mensagens que permite a um celular alcançar um worker doméstico sem abrir portas na rede. O uso do Nostr como plano de controle para agentes locais está se tornando um padrão consolidado.

### Coop Mobile publica suas primeiras compilações versionadas

O [Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1) e a [v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2) foram lançados nesta semana como as primeiras compilações versionadas do Coop Mobile, um cliente Android de mensagens diretas criptografadas [NIP-17](/pt/topics/nip-17/). Os dois lançamentos melhoram a segurança contra crashes no parsing de mensagens e no tratamento de códigos QR, além de apagar todos os dados armazenados ao sair da conta.

### Amethyst cria interface compatível com NIP-89, feed de repositórios Git e seção Discover para napplets {#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section}

A branch principal do [Amethyst](https://github.com/vitorpamplona/amethyst) criou várias superfícies novas nesta semana. Um [feed de repositórios Git](https://github.com/vitorpamplona/amethyst/pull/3406) transforma repositórios [NIP-34](/pt/topics/nip-34/) em uma categoria navegável da timeline do Android, filtrável por comunidade e autor, acompanhada de um [navegador git smart-HTTP](https://github.com/vitorpamplona/amethyst/pull/3415) que lê o conteúdo e os commits dos repositórios sem sair do aplicativo. O host de napplets ganhou uma [seção Discover](https://github.com/vitorpamplona/amethyst/pull/3409) que lista aplicativos web selecionados, além de nSites e napplets seguidos, com base em eventos de handlers [NIP-89](/pt/topics/nip-89/) e eventos de sites [NIP-5A](/pt/topics/nip-5a/). A exibição de notas agora [revela qual aplicativo Nostr criou um evento](https://github.com/vitorpamplona/amethyst/pull/3422) por meio de tags NIP-89. Na sincronização, o [suporte à negentropy do NIP-77](https://github.com/vitorpamplona/amethyst/pull/3434) traz reconciliação por streaming e janelas automáticas por `created_at` para contornar limites de resultados impostos pelos relays, reduzindo a largura de banda necessária para manter grandes conjuntos locais de eventos sincronizados com um relay.

### Buzz v0.3.38 reforça a superfície de ataque dos relays e adiciona seleção de modelos independente de provedor

O [Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38) reforça a [superfície de ataque dos relays](https://github.com/block/buzz/pull/1369) exposta quando o Buzz publica personas, equipes, agentes gerenciados e atestados de proprietário NIP-OA como eventos Nostr assinados. Um relay do Buzz é um registro público das identidades Nostr da equipe e de seu estado; este lançamento endurece a validação de entradas e a proteção contra replay nos kinds de evento conhecidos definidos pelo Buzz. O lançamento também generaliza a seleção de modelos, permitindo que uma equipe do Buzz use qualquer provedor para o qual existam adaptadores, inclusive um novo backend Databricks AI Gateway v2.

### Notedeck implementa relays de sincronização privada NIP-37, calendário NIP-52 e comentários NIP-22 {#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments}

O [Notedeck](https://github.com/damus-io/notedeck), cliente desktop nativo em Rust da equipe do Damus, implementou três protocolos em uma semana. Os relays de sincronização privada agora persistem em uma lista [NIP-37](/pt/topics/nip-37/) kind `10013`, separando o conjunto de relays de conteúdo privado do usuário de sua outbox pública NIP-65. O painel de calendário `horizon` lê eventos [NIP-52](/pt/topics/nip-52/) do nostrdb e recebeu um novo layout de três painéis. O painel `headway` adicionou um modelo de eventos de comentário [NIP-22](/pt/topics/nip-22/) no kind `1111`, definido pelo NIP-22 para a superfície unificada de comentários que substitui o encadeamento de respostas NIP-10.

### Applesauce incorpora sessões NIP-46 nbunksec e atualiza carteira para Cashu v4 {#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut}

O [Applesauce](https://github.com/hzrd149/applesauce), toolkit modular do Nostr para assinadores, relays, carteiras e conteúdo, fez um [lançamento coordenado da série 6.2.x](https://github.com/hzrd149/applesauce/releases) entre seus subpacotes. O pacote de assinadores ganhou auxiliares para importar e exportar `nbunksec`, tratando uma sessão de bunker [NIP-46](/pt/topics/nip-46/) como artefato portátil que pode ser transferido entre clientes. O pacote de carteira atualizou seus bindings de [Cashu](/pt/topics/nip-60/) para o `@cashu/cashu-ts` v4, no qual valores de proofs se tornam objetos de valor `Amount` e a API de decodificação de tokens muda.

---

## Lançamentos com tag

### mostro-core v0.14.0

O [mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0) traz a próxima iteração do protocolo da rede P2P de negociação fiduciária [Mostro](/pt/topics/nip-69/). O lançamento sucede a [v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2) e chega junto com o [mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0), que adota o novo core. Três PRs foram incorporados ao repositório do core nesta semana; o restante da stack, o daemon mostro e o Mostro mobile, acompanha a v0.14.0 do crate de tipos compartilhados.

### ngit v2.6.1

O [ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli), CLI canônico de git sobre Nostr para repositórios [NIP-34](/pt/topics/nip-34/), implementa a [semântica de forks GRASP-06 do NIP-34](https://github.com/nostr-protocol/nips/pull/2395), incorporada nesta semana, que substitui a tag `personal-fork` por uma tag `u` nos eventos de estado de repositório.

### mesh-llm v0.72.0 e v0.72.1

O [mesh-llm](https://github.com/Mesh-LLM/mesh-llm), componente de inferência da stack ContextVM que executa LLMs de código aberto por uma superfície JSON-RPC endereçável pelo Nostr, lançou as versões [v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0) e [v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1), com uma correção para crash de batching em prompts individuais grandes e a migração da ponte MCP para longe de auxiliares obsoletos.

### Meiso v1.4.0 traz listas colaborativas de chave compartilhada que substituem MLS no compartilhamento de tarefas {#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing}

O [Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0) apresenta um modelo de listas colaborativas de chave compartilhada que substitui o compartilhamento de tarefas anterior do projeto, baseado em MLS, por um design mais simples de eventos endereçáveis. Cada lista compartilhada gera uma chave Nostr dedicada, distribuída aos membros; as tarefas são eventos endereçáveis kind `35000`, identificados por `d=task-id`, com conteúdo autoencriptado por [NIP-44](/pt/topics/nip-44/); e os relays aplicam Last-Write-Wins por tarefa. O design abre mão do forward secrecy e da segurança pós-comprometimento do MLS em troca de uma implementação de cliente mais simples e resolução de conflitos no nível do relay.

### Cordn 0.3.2

O [Cordn 0.3.2](https://github.com/Cordn-msg/cordn) traz uma linha “more-private-coordinator” que remove pubkeys efêmeras dos remetentes da publicação de mensagens em grupo e reforça o fluxo de solicitações de entrada contra novas solicitações antigas. O Cordn é a stack de mensagens baseada em MLS abordada no [lançamento do Cordn Ad-hoc CVM na edição nº 28](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator); este lançamento é a atualização correspondente no lado do coordenador.

---

## Alterações ainda não lançadas

### diVine incorpora 108 PRs de aprimoramentos pós-lançamento

O [diVine](https://github.com/divinevideo/divine-mobile), cliente de vídeos curtos em loop que resgata o Vine, está em uma intensa onda de aprimoramentos pós-lançamento. O trabalho visível no Nostr nesta semana é uma rodada de estabilidade do fluxo de conexão [NIP-46](/pt/topics/nip-46/) que migra falhas de `nostrconnect://` para códigos de motivo estruturados.

### Zap Cooking prossegue com a correção NIP-46 entre projetos e a reformulação do compositor

O [Zap Cooking](https://github.com/zapcooking/frontend) é um cliente de compartilhamento de receitas no Nostr, no qual as receitas são publicadas como eventos Nostr de formato longo. O trabalho desta semana continua a correção [NIP-46](/pt/topics/nip-46/) entre projetos e a reformulação do compositor abordadas como ainda não lançadas na [edição nº 28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes).

### Conduit reforça o fluxo de anúncios e a correção do marketplace

O [Conduit](https://github.com/Conduit-BTC/conduit-mono) é um monorepo de marketplace com três aplicativos sobre o Nostr, cobrindo o mercado de compradores, o portal de comerciantes e o construtor de lojas. O trabalho desta semana dá continuidade ao esforço de correção do marketplace abordado na [cobertura do lançamento da edição nº 28](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default), apoiando-se na onda de comércio [NIP-99](/pt/topics/nip-99/) que foi a história de protocolo da edição anterior.

### Pollerama v1.12 a v1.13.1 adicionam escolha da tag de cliente, abas de perfil e limites de threads

O [Pollerama](https://github.com/formstr-hq/nostr-polls), cliente Android do Nostr concentrado em enquetes e notas, com uma forte camada de descoberta por web of trust, lançou as versões v1.12.0, v1.13.0 e v1.13.1 no Zapstore nesta semana. Agora os usuários podem escolher qual tag de cliente acompanha as notas e enquetes que criam, selecionando-a em uma lista predefinida ou informando uma própria. Cadeias muito aninhadas de comentários e respostas passam a parar após alguns níveis e oferecem um link para a thread completa na página da nota. As páginas de perfil abrem por padrão em Notes, divididas nas abas Posts e Conversations. Foi corrigido um bug de persistência em que contas recém-seguidas desapareciam após reiniciar o aplicativo, e os botões de seguir agora exibem progresso.

### getwired.app e get-tao.app corrigem o fluxo de envio de confissões NIP-13

O [getwired.app](https://github.com/smolgrrr/Wired) e o [get-tao.app](https://github.com/smolgrrr/TAO), que compartilham um fluxo de publicação anônima que adiciona proof-of-work NIP-13 para conter spam no envio, corrigiram o [fluxo de envio de confissões](https://github.com/smolgrrr/Wired/pull/57) para tornar coerente a experiência durante a mineração do PoW.

### nostui adiciona uma aba de timeline de menções

O [nostui](https://github.com/akiomik/nostui), cliente de terminal do Nostr em Rust, adicionou uma [aba de timeline de menções](https://github.com/akiomik/nostui/pull/463) que apresenta, em uma tela própria da TUI, eventos kind 1 que marcam a pubkey ativa.

### Heartwood incorpora URIs de bunker NIP-46 por identidade e uma ponte de assinatura em modo HSM

O [Heartwood](https://github.com/forgesworn/heartwood) é um assinador [NIP-46](/pt/topics/nip-46/) em que a chave de assinatura jamais chega ao cliente: o cliente fala NIP-46 com um pequeno relay, e o relay usa um protocolo de frames seriais para se comunicar com um dispositivo de hardware conectado que executa a assinatura. Nesta semana, o projeto incorporou uma [ponte de assinatura do relay para a porta serial](https://github.com/forgesworn/heartwood/pull/11) e [conexões de bunker por identidade](https://github.com/forgesworn/heartwood/pull/16), de modo que um único dispositivo de hardware com várias identidades exponha uma URI de bunker distinta para cada uma.

### Refatoração de autenticação e assinadores do Nostter

O [Nostter](https://github.com/SnowCait/nostter) reformulou sua [camada de autenticação e assinadores](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth) nesta semana, movendo o estado de login para um único signal e extraindo o despacho do assinador para módulos de estratégia. O caminho aponta para uma abstração limpa de assinadores em que a extensão web NIP-07, o bunker remoto NIP-46 e um nsec bruto compartilham um único fluxo de código.

### Dart NDK extrai o assinador NIP-07 e randomiza timestamps NIP-59

O [Dart NDK](https://github.com/relaystr/dart_ndk) moveu seu assinador [NIP-07](/pt/topics/nip-07/) para fora do pacote core e para o `ndk_flutter`, onde fica a WebView do Flutter, e [randomizou os timestamps de gift wraps NIP-59](https://github.com/relaystr/dart_ndk/pull/667) para reforçar a proteção de mensagens criptografadas contra correlação temporal.

### Milk Market adiciona páginas de loja NIP-23 e processamento de pagamentos pela Square

O [Milk Market](https://github.com/shopstr-eng/milk-market), vitrine de marketplace da equipe do Shopstr, deu a cada loja uma página de blog baseada nos eventos de formato longo [NIP-23](/pt/topics/nip-23/) do vendedor, com seções editáveis e uma rota direta para as configurações do blog. Na mesma semana, adicionou a [Square](https://github.com/shopstr-eng/milk-market/pull/30) como processador de pagamentos alternativo para vendedores e a compra automática de etiquetas de envio para pedidos pagos.

### Calendar by Formstr lança aplicativo para iOS

O [Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar) incorporou o [PR nº 159, IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159), nesta semana, levando o cliente de calendário [NIP-52](/pt/topics/nip-52/) ao iOS. O [PR nº 197](https://github.com/formstr-hq/nostr-calendar/pull/197) corrige o parsing de datas do calendário no horário local, e o [PR nº 201](https://github.com/formstr-hq/nostr-calendar/pull/201) adiciona um fluxo E2E do Playwright acionado por uma label `run-tests`.

### cagliostr aplica NIP-22, NIP-09 por coordenada e proof-of-work NIP-13

O [cagliostr](https://github.com/mattn/cagliostr), implementação de relay em Go, reforçou três caminhos de aplicação nesta semana: [proof-of-work NIP-13 configurável](https://github.com/mattn/cagliostr/pull/7) em eventos recebidos, [exclusão NIP-09 por coordenada endereçável](https://github.com/mattn/cagliostr/pull/8), para que eventos substituíveis possam ser apagados por sua tag `a`, algo que a exclusão apenas por id de evento não alcança, e [limites configuráveis de timestamp NIP-22](https://github.com/mattn/cagliostr/pull/9), que rejeitam eventos com data muito distante no passado ou no futuro.

---

## Novos projetos acompanhados e descobertos

A [suíte de bem-estar Vanderwarker](https://git.vanderwarker.family/wellbeing) publica telemetria do mundo físico como eventos Nostr sob uma chave de assinatura compartilhada do publicador. Ela reúne cinco aplicativos irmãos: o [Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android) é um contador de passos que ancora dados de atividade física no Nostr como `kind:30078`; o [Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android) publica diariamente quantas vezes o celular foi desbloqueado; o [Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android) publica a mídia em reprodução como User Status; o [Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android) publica nível, tensão e temperatura da bateria a cada 15 minutos; e o [Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android) publica o uso diário de dados. Os cinco apareceram no Zapstore entre 24 e 30 de junho.

O [ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9) é um aplicativo Android criptografado e sem servidor para compartilhamento de localização ao vivo, criado em Rust e Slint e lançado em 29 de junho. É irmão do [Haven](https://github.com/mehmetefeumit/Haven-App), aplicativo de localização baseado em [Marmot](/pt/topics/marmot/) abordado na [edição nº 28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot), mas usa outra arquitetura de transporte: DMs Nostr criptografadas carregam as atualizações de localização, enquanto o Haven usa mensagens de grupo Marmot.

O [NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell) é um scaffold inicial de shell para criar aplicativos Nostr. O projeto publicou sua primeira documentação voltada ao usuário nesta semana.

O [NIPs by Pollerama](https://nips.pollerama.fun), cujo repositório [abh3po/better-nips](https://github.com/abh3po/better-nips) foi criado em 29 de junho de 2026, é um novo cliente para NIPs `kind:30817` escritos pela comunidade do [NostrHub](https://nostrhub.io), apresentado como uma superfície alternativa ao nostrhub.io ponderada por confiança. Cada NIP `kind:30817` tem sua própria URL compartilhável (`#/nip/<naddr>`), com renderização completa de Markdown e os kinds de evento que define. O cliente oferece três feeds, Following, Web of Trust, com pessoas seguidas pelas pessoas seguidas, e Global, cada um ordenável por aprovações ponderadas por confiança ou pelos itens mais recentes. As aprovações são publicadas como labels [NIP-32](/pt/topics/nip-32/) no kind `1985`, com as tags `["L","nostrhub"]` e `["l","approve","nostrhub"]`, além de uma tag `a` apontando para o endereço do NIP-alvo e uma tag `client` que anuncia `better-nips`. Esse é exatamente o formato de evento assinado pelo próprio NostrHub, portanto as aprovações são compatíveis entre os dois clientes. A aprovação de alguém seguido diretamente tem mais peso no ranking do que a aprovação de segundo grau de alguém seguido por uma pessoa seguida.

A stack de assinatura usa [`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer), com um modal de login completo que cobre extensão web [NIP-07](/pt/topics/nip-07/), bunker e nostrconnect [NIP-46](/pt/topics/nip-46/), ncryptsec [NIP-49](/pt/topics/nip-49/) e assinador Android [NIP-55](/pt/topics/nip-55/); as sessões são reconectadas silenciosamente ao recarregar. A camada de rede passa por [`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay), um Web Worker que distribui a outbox [NIP-65](/pt/topics/nip-65/) do usuário entre relays para que um grande conjunto da web of trust não se espalhe para um único relay. A posição de design é que NIPs comunitários, sejam hospedados no NostrHub, no `better-nips` ou em futuros clientes, são equivalentes no nível do protocolo; o ranking vem do grafo social, não da curadoria de moderadores. Isso se alinha diretamente ao fluxo de labels NIP-32 abordado pelo mergulho profundo da [edição nº 25](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling).

Dois novos clusters de repositórios [NIP-34](/pt/topics/nip-34/) surgiram nesta semana. O [Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git) é um cliente Nostr voltado a vídeo; um [cluster nostrapps.com](wss://gitnostr.com) publica três projetos irmãos: [verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git), uma VM de napps para desktop; [hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git), cliente de comunidades personalizável; e [napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git), especificação e runtime de microaplicativos HTML. O cluster se posiciona em paralelo ao trabalho de [napplets](/pt/topics/nip-5d/) abordado na história principal da edição anterior.

---

## Trabalho de protocolo e atualizações de NIPs

### Incorporado: NIP-44 remove o limite de payload de 65.535 bytes

O [PR nº 1907](https://github.com/nostr-protocol/nips/pull/1907) foi incorporado em 28 de junho, após permanecer aberto desde setembro de 2024. A alteração remove o limite superior de 65.535 bytes do payload em texto simples de um envelope de criptografia versionada [NIP-44](/pt/topics/nip-44/), elevando-o para 4 GiB (`uint32_max`). O NIP-44 codifica o tamanho do payload como `uint16` no formato de rede, exigência estrita da especificação original para interoperabilidade; a alteração incorporada adota um campo de comprimento maior indicado no byte de versão, para que implementações v2 mantenham a compatibilidade de rede e implementações v3 ou posteriores carreguem o comprimento maior. Clientes que usam NIP-44 para mensagens diretas [NIP-17](/pt/topics/nip-17/), gift wraps [NIP-59](/pt/topics/nip-59/), payloads de assinadores remotos [NIP-46](/pt/topics/nip-46/) ou qualquer outra mensagem Nostr criptografada por NIP-44 agora podem trocar eventos individuais maiores que 64 KiB sem dividi-los na camada de aplicação.

### Incorporado: NIP-86 ganha método signevent e evento Relay Roles

O [PR nº 2389](https://github.com/nostr-protocol/nips/pull/2389) adiciona um método `signevent` à API JSON-RPC de gerenciamento de relays [NIP-86](/pt/topics/nip-86/), permitindo que um administrador peça ao relay que assine um evento com a pubkey do próprio relay. O [PR nº 2390](https://github.com/nostr-protocol/nips/pull/2390) complementar define um evento Relay Roles: evento substituível publicado por um relay para declarar seus administradores e moderadores. Juntos, eles permitem que clientes NIP-86 consultem a lista de administradores de um relay e verifiquem que uma solicitação autenticada veio de um administrador atual, sem confiança fora do protocolo. O mergulho profundo abaixo aborda as duas alterações.

### Incorporado: NIP-34 substitui personal-fork por `u` no GRASP-06

O [PR nº 2395](https://github.com/nostr-protocol/nips/pull/2395) foi incorporado em 24 de junho e substitui a tag `personal-fork` do [NIP-34](/pt/topics/nip-34/) em eventos de estado de repositório (`kind:30618`) por uma tag `u`, de “upstream”, alinhando o formato de rede à semântica de forks GRASP-06 implementada pela suíte GitWorkshop. A mudança encerra o [PR nº 2384](https://github.com/nostr-protocol/nips/pull/2384), `NIP-34: remove maintainers to solve expiry issues`, que propunha outra correção para a semântica de forks. A direção incorporada é a implementada pelo ngit v2.6.x, portanto a especificação e o CLI de referência agora estão alinhados. Repositórios existentes que usam `personal-fork` continuam interoperáveis; repositórios novos e a linha ngit v2.6 publicam a tag `u`.

### Incorporado: metadados de cliente NIP-46, agora upstream após a implementação pelo Amber

O [PR nº 2381](https://github.com/nostr-protocol/nips/pull/2381) foi incorporado em 23 de junho e adiciona metadados opcionais do cliente à solicitação `connect` do [NIP-46](/pt/topics/nip-46/), permitindo que o cliente publique seu nome, a URL de um ícone e a URL de uma página inicial no momento da conexão com o assinador. O [Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2) implementou a extensão de metadados na semana passada, como abordado na [edição nº 28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata); nesta semana, o NIP upstream alcança a implementação já distribuída.

### Aberto: chaves wrapper NIP-17 determinísticas por época

O [PR nº 2397](https://github.com/nostr-protocol/nips/pull/2397) e o [PR nº 2396](https://github.com/nostr-protocol/nips/pull/2396) abordam duas propostas convergentes de chaves para wraps NIP-17. O PR nº 2397 propõe derivar de forma determinística a chave de assinatura efêmera usada para criar um gift wrap [NIP-59](/pt/topics/nip-59/) a partir de uma seed por conversa vinculada a uma época temporal ampla, permitindo que quem conhece a chave da conversa preveja quais pubkeys deve assinar. A especificação atual exige uma chave aleatória nova por wrap, tornando impossível essa previsão. O PR nº 2396 é a alteração complementar: wraps de uma conversa deveriam ser assinados diretamente com a chave da conversa, para que a pubkey do wrap também funcione como identificador da conversa. Juntos, eles definem um caminho para conversas NIP-17 filtráveis sem vazamento de metadados. Ambos continuam abertos e em discussão.

### Aberto: NIP-59 deve rejeitar eventos seal kind 13 no relay

O [PR nº 2399](https://github.com/nostr-protocol/nips/pull/2399) propõe que relays rejeitem eventos kind 13, o seal interno de um gift wrap [NIP-59](/pt/topics/nip-59/), quando apareçam no nível superior de uma solicitação de publicação, pois um evento seal só faz sentido dentro de um wrap e seu vazamento expõe a pubkey do destinatário. A [issue nº 2398](https://github.com/nostr-protocol/nips/issues/2398) complementar vai além e defende que o seal seja redefinido como kind efêmero, já que kinds efêmeros NIP-01 não são armazenados pelos relays. Isso reforçaria a regra no nível do protocolo e eliminaria a dependência da política de cada relay.

### Aberto: estados de grupos NIP-29

O [PR nº 2372](https://github.com/nostr-protocol/nips/pull/2372) adiciona semântica explícita de estados de grupo ao [NIP-29](/pt/topics/nip-29/), sobre grupos baseados em relays, definindo o que significa um grupo estar aberto, fechado, público, privado ou arquivado e como as transições de estado interagem com eventos de membros. A proposta leva para a especificação dos relays uma semântica que antes era específica de cada cliente.

### Aberto: suporte opcional a vários mantenedores no NIP-34

O [PR nº 2324](https://github.com/nostr-protocol/nips/pull/2324) é a proposta complementar ao [PR nº 2395](https://github.com/nostr-protocol/nips/pull/2395), sobre a semântica de forks GRASP-06 abordada acima. O PR nº 2324 adiciona suporte opcional a vários mantenedores nos eventos de anúncio de repositórios [NIP-34](/pt/topics/nip-34/) (`kind:30617`), permitindo que um repositório declare mais de uma pubkey canônica de mantenedor por meio de tags `maintainer` repetidas. Patches e issues assinados por qualquer mantenedor declarado passam a ser aceitos pelos clientes como oficiais, resolvendo a antiga lacuna em que repositórios NIP-34 com vários mantenedores precisavam encaminhar tudo por uma única pubkey ou recorrer a coordenação fora do protocolo.

### Aberto: operador AND do NIP-91 para filtros, proposta ainda não incorporada

O [PR nº 2252](https://github.com/nostr-protocol/nips/pull/2252) é a proposta do operador AND para [filtros](/pt/topics/nip-01/) do Nostr, retomando um design discutido anteriormente no [PR nº 1365](https://github.com/nostr-protocol/nips/pull/1365), já encerrado. Já existem implementações no [nostr-rs-relay](https://github.com/v0l/nostr-rs-relay), no applesauce, no [Amethyst](https://github.com/vitorpamplona/amethyst) e no worker-relay, mas o PR da especificação continua aberto.

### Encerradas: quatro NIPs de comércio da pats2sats

Quatro propostas de comércio sobre o Nostr foram encerradas nesta semana: Escrow ([nº 2334](https://github.com/nostr-protocol/nips/pull/2334)), Reservations ([nº 2335](https://github.com/nostr-protocol/nips/pull/2335)), uma extensão de anúncios de marketplace [NIP-99](/pt/topics/nip-99/) ([nº 2346](https://github.com/nostr-protocol/nips/pull/2346)) e um perfil para anúncios de hospedagem ([nº 2333](https://github.com/nostr-protocol/nips/pull/2333)). A mesma superfície de comércio agora está sendo consolidada na [Gamma Market Spec](https://github.com/GammaMarkets/market-spec), repositório de extensões do projeto que se compõe sobre anúncios de marketplace NIP-99 com semântica de pedidos, checkout, escrow e disputas. O Compass agora acompanha esse repositório junto com Marmot e Blossom como repositório de especificação de protocolo externo ao próprio repositório de NIPs. Os PRs abertos nesta semana incluem um esclarecimento sobre atribuição de clientes ([nº 11](https://github.com/GammaMarkets/market-spec/pull/11)), uma tag supersedes para alterações de identidade de produtos ([nº 8](https://github.com/GammaMarkets/market-spec/pull/8)) e semântica de avaliações de comerciantes ([nº 7](https://github.com/GammaMarkets/market-spec/pull/7)).

### Aberto: vinculação de identidades Bitcoin

Duas propostas foram abertas nesta semana para vincular identidades Bitcoin a identidades Nostr: um [endereço de Silent Payments do Bitcoin NIP-352](https://github.com/nostr-protocol/nips/pull/2392) e uma [prova de vinculação de identidade Bitcoin-OTC](https://github.com/nostr-protocol/nips/pull/2401).

---

## Mergulho profundo em NIPs: NIP-86 (API de gerenciamento de relays) {#nip-deep-dive-nip-86-relay-management-api}

O [NIP-86](/pt/topics/nip-86/) define uma interface JSON-RPC para gerenciamento de relays, permitindo que clientes autorizados enviem comandos administrativos a relays por uma API padronizada. Um único cliente pode gerenciar qualquer relay compatível com NIP-86 sem ferramentas específicas de cada relay. Duas alterações da especificação incorporadas nesta semana, o [PR nº 2389](https://github.com/nostr-protocol/nips/pull/2389) e o [PR nº 2390](https://github.com/nostr-protocol/nips/pull/2390), fecham o ciclo entre eventos assinados por relays e administradores declarados por relays.

### O transporte

Uma solicitação de gerenciamento NIP-86 é um HTTP POST enviado à mesma URI em que o relay oferece conexões WebSocket, com `Content-Type: application/nostr+json+rpc`. O corpo da solicitação é um documento JSON no seguinte formato:

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

A autenticação usa um evento assinado de autenticação HTTP [NIP-98](/pt/topics/nip-98/) no header `Authorization`. O relay verifica se a pubkey de assinatura consta em sua lista de administradores antes de executar o método. A resposta do relay é um documento JSON no seguinte formato:

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### Os métodos que já existiam antes desta semana

O conjunto anterior de métodos abrange banimentos de pubkeys (`banpubkey`, `allowpubkey`, `listbannedpubkeys`), banimentos de eventos (`banevent`, `allowevent`, `listbannedevents`), metadados do relay (`changerelayname`, `changerelaydescription`, `changerelayicon`), gerenciamento da lista de kinds permitidos (`allowkind`, `disallowkind`, `listallowedkinds`) e um método `stats` que retorna estatísticas do relay. O formato é intencionalmente próximo de um serviço JSON-RPC padrão, para que um cliente possa criar bindings tipados sobre ele.

### O que mudou nesta semana

O [PR nº 2389](https://github.com/nostr-protocol/nips/pull/2389) adiciona um método `signevent` à especificação. O método recebe como argumento um template parcial de evento, com kind, tags e content, e pede que o relay assine e devolva um evento completo com a pubkey do próprio relay no campo `pubkey`. Essa é a condição necessária para um relay publicar eventos de protocolo sobre si mesmo: anúncios de pubkeys bloqueadas, metadados do relay e o novo evento Relay Roles abaixo exigem que o relay assine com sua chave controlada pelo operador, mas a maioria dos operadores não quer manter uma chave privada no cliente administrativo.

O [PR nº 2390](https://github.com/nostr-protocol/nips/pull/2390) define um evento Relay Roles: kind de evento substituível parametrizado que um relay publica, assinado com sua própria pubkey por meio de `signevent`, para declarar as pubkeys de seus administradores e moderadores com semântica explícita de funções. Um cliente compatível com NIP-86 pode buscar o evento Relay Roles em qualquer relay acompanhado, montar a lista de administradores com as tags do evento e validar que uma solicitação NIP-86 autenticada veio de um administrador atual sem confiança fora do protocolo nem configuração por relay. Juntos, os dois PRs fecham o ciclo: `signevent` é o mecanismo e Relay Roles é o primeiro kind de evento construído sobre ele.

### Exemplo de solicitação NIP-86

Uma solicitação NIP-86 `banpubkey` completa tem o seguinte formato:

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

com um header `Authorization` contendo um evento assinado NIP-98:

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

A pubkey de assinatura precisa constar no conjunto de administradores do relay, agora declarado no evento Relay Roles; a tag `u` precisa corresponder à URL HTTPS do relay; e a tag `payload` precisa corresponder ao SHA-256 do corpo JSON da solicitação. O relay devolve:

```json
{
  "result": true,
  "error": null
}
```

### Implementações

- O [Amethyst](https://github.com/vitorpamplona/amethyst) oferece uma interface de gerenciamento de relays NIP-86 no Android, a partir da v1.07.0.
- Entre os relays de referência que implementam a especificação estão o [strfry](https://github.com/hoytech/strfry), o [khatru](https://github.com/fiatjaf/khatru) e várias implementações menores ligadas pela seção `Implementation Status` da especificação.

Clientes compatíveis com NIP-86 começarão a tratar o evento Relay Roles como fonte canônica da lista de administradores de um relay quando as implementações adotarem as alterações `signevent` e Relay Roles.

---

## Mergulho profundo em NIPs: NIP-89 (handlers de aplicativos recomendados) {#nip-deep-dive-nip-89-recommended-application-handlers}

O [NIP-89](/pt/topics/nip-89/) define dois kinds de eventos substituíveis parametrizados: `kind:31990`, o handler de aplicativo publicado pelo desenvolvedor, e `kind:31989`, a recomendação que um usuário publica para um aplicativo usado por ele. Juntos, eles permitem que clientes descubram aplicativos capazes de lidar com um kind de evento desconhecido sem coordenação fora do protocolo: ao encontrar um evento `kind:30030` sem suporte nativo, um leitor de formato longo pode consultar o grafo NIP-89 em busca de handlers e oferecer ao usuário um fluxo `Open in...` para um aplicativo publicado que dê suporte ao evento. O NIP-89 é a infraestrutura original para o mesmo problema de roteamento entre aplicativos que o trabalho em napplets e napps presente nesta edição agora estende para applets Nostr nativos e componíveis.

### O evento de handler de aplicativo (`kind:31990`)

O desenvolvedor de um aplicativo publica um ou mais eventos de handler descrevendo quais kinds de eventos o aplicativo aceita e como abrir uma entidade Nostr nele:

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

A tag `d` identifica o handler, permitindo sua substituição; cada tag `k` declara um kind de evento aceito pelo aplicativo; e cada tag de plataforma (`web`, `ios`, `android`, ...) fornece um template de URL em que `<bech32>` serve de placeholder para uma entidade codificada conforme o [NIP-19](/pt/topics/nip-19/), substituída pelo cliente chamador no momento da abertura. Um evento de handler pode anunciar vários kinds aceitos quando todos compartilham o mesmo padrão de roteamento, mantendo compacta a descoberta de aplicativos e evitando um evento de handler para cada kind.

### O evento de recomendação do usuário (`kind:31989`)

Um usuário publica uma recomendação que declara quais aplicativos usa para determinado kind de evento:

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

A tag `d` contém o kind de evento recomendado. Cada tag `a` é um ponteiro de endereço NIP-01 para um evento de handler `kind:31990`, acompanhado do relay sugerido e da plataforma à qual a recomendação se aplica. Uma mesma recomendação pode listar vários aplicativos para plataformas distintas.

### A tag client e o tradeoff de privacidade

O NIP-89 também define uma tag `client` opcional que qualquer aplicativo publicador pode anexar aos eventos criados por ele:

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

Assim, qualquer cliente que exiba o evento pode apresentar o aplicativo de origem, consultar metadados mais ricos do handler e respeitar sugestões de renderização declaradas pelo handler. A especificação também aponta explicitamente o custo de privacidade: um cliente que emite uma tag `client` em todos os eventos publica a identidade do software usado e, com o tempo, revela padrões de uso. A especificação recomenda que os clientes permitam desativá-la.

O [PR nº 3422](https://github.com/vitorpamplona/amethyst/pull/3422) do Amethyst faz parsing e exibe tags NIP-89 `t`, `i`, `a` e `client` nos eventos, revelando diretamente na timeline qual aplicativo criou uma nota.

### Como funciona o fluxo de descoberta na prática

Um cliente que recebe um kind de evento desconhecido segue estas etapas. (1) Consulta o grafo de pessoas seguidas pelo usuário em busca de eventos `kind:31989` cuja tag `d` corresponda ao kind do evento. (2) Resolve cada tag `a` recomendada para seu evento de handler `kind:31990`. (3) Escolhe o handler cujo template de URL `web`, `ios` ou `android` corresponda à plataforma atual. (4) Substitui no template a codificação `bech32` da entidade. (5) Oferece ao usuário a URL resultante como opção `Open in...`. O fluxo é filtrado socialmente: um cliente que consulte eventos de handler arbitrários em relays não confiáveis pode acabar redirecionando usuários para aplicativos maliciosos, portanto começar por pessoas seguidas pelo usuário é um padrão mais seguro do que tratar todos os handlers publicados como igualmente confiáveis.

### NIP-89 e a camada de napplets

A seção Discover, o runtime do host de napplets e a exibição de tags `client` do Amethyst formam, juntos, uma superfície consumidora completa do NIP-89 no Android. A especificação de napplets, lançada na edição anterior, amplia o que esses eventos de handler NIP-89 podem apontar: applets em sandbox que executam um runtime Nostr nativo e componível sobre Nostr e Blossom. O NIP-89 é o grafo de descoberta e roteamento; o runtime de napplets é um dos alvos de execução para os quais ele pode apontar.

---

*Feedback, correções e projetos que deixamos passar: abra uma issue em [github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass) ou fale conosco por DM NIP-17 no npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923.*
