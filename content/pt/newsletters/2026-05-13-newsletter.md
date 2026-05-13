---
title: 'Nostr Compass #22'
date: 2026-05-13
publishDate: 2026-05-13
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-13-newsletter.md
translationDate: 2026-05-13
---

Bem-vindo ao Nostr Compass, o seu guia semanal sobre o desenvolvimento do protocolo Nostr.

**Esta semana:** O [Nostr VPN](https://github.com/mmalmi/nostr-vpn) lança [oito versões em sete dias](#nostr-vpn-lança-oito-versões-culminando-em-v4010) desde um fluxo de emparelhamento de dispositivos redesenhado até uma troca de AEAD que duplica aproximadamente o débito TCP. O [Marmot Protocol](https://github.com/marmot-protocol) (a fundação do [White Noise](https://github.com/marmot-protocol/whitenoise)) lança uma [versão frontend que completa a funcionalidade de bloqueio de utilizadores](#marmotwhite-noise-lança-frontend-com-bloqueio-completo-e-31-prs-em-mdk-e-backend) e 31 PRs em MDK e backend. O [Grain](https://github.com/0ceanSlim/grain) lança [v0.6.0](#grain-v060-adiciona-nip-40-nip-50-nip-70-e-nip-45) com quatro novas implementações de NIP num único marco. O [Citrine](https://github.com/greenart7c3/Citrine) lança [v3.0.0-pre1](#citrine-v300-pre1-traz-tor-integrado-e-agregação-de-relay) com Tor integrado e agregação de relay. O [Amber](https://github.com/greenart7c3/Amber) lança [v6.1.0-pre2](#amber-v610-pre2-melhora-o-fluxo-de-conexão-de-nova-app) com melhorias no fluxo de conexão e assinatura. O [Alby Hub](https://github.com/getAlby/hub) lança [v1.22.2](#alby-hub-v1222-adiciona-página-de-ia-e-agentes-e-suporte-ao-core-lightning) com uma página de IA e Agentes e integração com Core Lightning. O [Mostro](https://github.com/MostroP2P/mostro) lança bonds de taker concorrentes e o [mostro-core v0.11.0](#mostro-lança-bonds-de-taker-concorrentes-e-mostro-core-v0110). O [Jumble](https://github.com/CodyTseng/jumble) lança [cinco versões](#jumble-lança-cinco-versões-com-pesquisa-recente-e-persistência-de-conta) com histórico de pesquisa recente e correções de persistência de dados de conta. O [Nostrord](https://github.com/nostrord/nostrord) lança [três versões](#nostrord-lança-modais-de-partilha-de-grupo-upload-de-media-e-pacotes-arch-linux) com modais de partilha de grupo e pacotes Arch Linux. O [Flotilla](https://flotilla.social) lança [1.8.0](#flotilla-180-lança-videochamadas-renderização-de-email-e-menções-de-sala) com videochamadas, renderização de email e menções de sala. O [Calendar by Formstr](https://calendar.formstr.app) lança [v1.5.1](#calendar-by-formstr-lança-v151-com-agendamento-de-consultas-e-sincronização-com-calendário-android) com agendamento de consultas e sincronização com o calendário Android. O [Tamagostrich](https://github.com/Negr087/tamagostrich) lança um Tamagotchi NIP-78 descentralizado com recompensas em sats. As discussões de NIP apresentam Reservas, Serviços de Custódia, Listagens de Alojamento, Zaps Onchain e regras de comunidade verificáveis. Dois mergulhos profundos em NIP cobrem o NIP-78 (dados específicos de app) e o NIP-98 (HTTP Auth).

## Principais histórias

### Nostr VPN lança oito versões culminando em v4.0.10

O [Nostr VPN](https://github.com/mmalmi/nostr-vpn), a VPN mesh descentralizada baseada em Rust que usa Nostr para descoberta de pares e um protocolo noise apoiado em FIPS para o plano de dados, lançou oito versões de [v4.0.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.1) a [v4.0.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.10) em macOS, Linux, Windows e Android esta semana.

A mudança principal está no [v4.0.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.8): o AEAD foi trocado do backend soft `chacha20poly1305` do RustCrypto para o ChaCha20-Poly1305 do BoringSSL no `ring` 0.17, que usa NEON otimizado manualmente em aarch64 e AVX2/AVX-512 em x86_64. Os benchmarks Docker em hardware idêntico mostraram o débito TCP direto de 2 nós a saltar de 437 para 1097 Mbps. O formato wire não foi alterado.

No início da semana, o [v4.0.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.1) reconstruiu o fluxo de emparelhamento de dispositivos com proteção contra fuga de nó de saída, um bloco de configuração WireGuard unificado em Nós de Saída e artefactos macOS assinados e notarizados. O [v4.0.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.2) melhorou a descoberta LAN com sockets multicast reutilizáveis para que pares na mesma LAN prefiram caminhos de underlay diretos. O [v4.0.9](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.9) adicionou batching `sendmmsg(2)` no caminho de envio UDP, empurrando o stream único TCP de 1066 para 1548 Mbps (1,45×). O [v4.0.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.10) lançou uma revisão completa de UX para emparelhamento de dispositivos: Convidar Dispositivos e Aderir à Rede são agora cartões separados, a importação automática dispara ao colar uma string `nvpn://invite/`, e o emparelhamento próximo dividiu-se em dois toggles independentes de 15 minutos.

### Marmot/White Noise lança frontend com bloqueio completo e 31 PRs em MDK e backend

O [White Noise](https://github.com/marmot-protocol/whitenoise), a app de mensagens de grupo privadas construída sobre o protocolo [Marmot](/pt/topics/marmot/) baseado em MLS, lançou [v2026.5.7+24](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.5.7+24) a 7 de maio como a versão frontend que completa o conjunto de funcionalidades de bloqueio. A versão anterior lançou silêncio, pesquisa e arquivo; esta conclui o bloqueio. Um utilizador bloqueado fica agora oculto de convites, pré-visualizações de chat, linhas de tempo de mensagens, resultados de pesquisa e notificações, e as suas mensagens deixam de contar para os contadores de não lidos. Os anexos de vídeo funcionam de ponta a ponta em todos os dispositivos. O aviso de offline cobre agora todos os ecrãs.

O trabalho de suporte abrange 31 PRs em MDK e backend. O MDK recebeu a [PR #258](https://github.com/marmot-protocol/mdk/pull/258) com o formato wire da extensão v3 e o esquema `disappearing_message_secs`, preparando o terreno para mensagens temporárias.

O trabalho de frontend inclui a [PR #653](https://github.com/marmot-protocol/whitenoise/pull/653) que corrige resumos de chats arquivados usando uma consulta pontual para que os chats arquivados sejam renderizados corretamente, a [PR #644](https://github.com/marmot-protocol/whitenoise/pull/644) que expõe um stream `subscribe_to_group_state` ao Dart para atualizações reativas de UI, e a [PR #635](https://github.com/marmot-protocol/whitenoise/pull/635) que corrige a recuperação de notificações de signatário externo Android quando a app de assinatura é iniciada a frio.

### Grain v0.6.0 adiciona NIP-40, NIP-50, NIP-70 e NIP-45

O [Grain](https://github.com/0ceanSlim/grain), o relay Nostr e biblioteca de cliente baseados em Go, lançou [v0.6.0](https://github.com/0ceanSlim/grain/releases/tag/v0.6.0) a 6 de maio com quatro novas implementações de NIP e uma passagem de reforço de produção. O marco v0.6 adiciona expiração de eventos [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), pesquisa de texto completo [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md), eventos protegidos [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) e contagem de eventos [NIP-45](https://github.com/nostr-protocol/nips/blob/master/45.md).

A expiração de eventos via NIP-40 permite aos publicadores definir um timestamp de expiração para que o relay descarte eventos após expiração. A pesquisa de texto completo NIP-50 permite que clientes emitam filtros `search` em mensagens REQ. Os eventos protegidos via NIP-70 impedem relays de partilhar eventos sem permissão explícita do autor. As consultas de contagem NIP-45 permitem que clientes peçam a um relay para devolver uma contagem de eventos correspondentes, reduzindo a largura de banda para consultas do tipo "quantas notas tem este utilizador".

A versão também inclui reforço de produção: configurações padrão mais seguras, respostas de rejeição NIP-01 corrigidas e melhor contrapressão para consumidores lentos.

## Lançamentos desta semana

### Citrine v3.0.0-pre1 traz Tor integrado e agregação de relay

O [Citrine](https://github.com/greenart7c3/Citrine), a app Android que transforma um telemóvel num nó relay Nostr, lançou [v3.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0-pre1) como pré-lançamento esta semana. As principais adições são suporte Tor integrado para acesso a relay que preserva a privacidade e agregação de relay, onde o Citrine pode recolher eventos de múltiplos relays upstream e servi-los a clientes locais. A [PR #139](https://github.com/greenart7c3/Citrine/pull/139) adiciona suporte a [NIP-77 (Reconciliação Negentropy)](/pt/topics/nip-77/) para sincronização de eventos eficiente baseada em reconciliação de conjuntos. A [PR #137](https://github.com/greenart7c3/Citrine/pull/137) encaminha todos os URLs através do proxy Tor, a [PR #133](https://github.com/greenart7c3/Citrine/pull/133) alivia a pressão na thread de UI no caminho de receção de eventos, e a [PR #132](https://github.com/greenart7c3/Citrine/pull/132) reduz o consumo de bateria do agregador de relay. A versão também adiciona uma vista de análise de eventos com um gráfico circular que divide os eventos armazenados por tipo.

### Amber v6.1.0-pre2 melhora o fluxo de conexão de nova app

O [Amber](https://github.com/greenart7c3/Amber), a app Android de assinatura para [NIP-55 (Aplicação de Assinatura Android)](/pt/topics/nip-55/) e [NIP-46](/pt/topics/nip-46/), lançou [v6.1.0-pre2](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre2). As principais correções: o diálogo de assinatura fecha agora corretamente após aceitar um pedido bunker, pedidos bunker malformados mostram um ecrã de pedido inválido, e é adicionada limitação de taxa para pedidos de assinatura baseados em intent. A [PR #430](https://github.com/greenart7c3/Amber/pull/430) corrige fugas de memória e ineficiências no caminho de assinatura.

### Alby Hub v1.22.2 adiciona página de IA e Agentes e suporte ao Core Lightning

O [Alby Hub](https://github.com/getAlby/hub), o nó Lightning auto-custodial e servidor Nostr Wallet Connect, lançou [v1.22.2](https://github.com/getAlby/hub/releases/tag/v1.22.2) com várias adições importantes. A nova página de IA e Agentes expõe as capacidades Lightning e NWC do Alby Hub a agentes de IA e ferramentas compatíveis com MCP. Um modo de carteira onchain integrado permite aos utilizadores receber e enviar Bitcoin onchain diretamente do Alby Hub. Rótulos personalizados para transações melhoram a contabilidade. As páginas de definições foram redesenhadas para maior clareza. A funcionalidade mais solicitada desde o lançamento chegou: Core Lightning (CLN) é agora um backend suportado a par do LND e LDK.

### Mostro lança bonds de taker concorrentes e mostro-core v0.11.0

O [Mostro](https://github.com/MostroP2P/mostro), o protocolo de negociação Bitcoin peer-to-peer no Nostr, fundiu 11 PRs esta semana avançando a funcionalidade de bond de taker que previne griefing ao exigir que ambas as partes bloqueiem fundos antes de uma negociação prosseguir. A [PR #733](https://github.com/MostroP2P/mostro/pull/733) implementa bonds de taker concorrentes onde múltiplos takers podem submeter faturas de bond simultaneamente e o primeiro a bloquear ganha, descartando os outros. A [PR #735](https://github.com/MostroP2P/mostro/pull/735) alinha o memo da fatura de bond com a secção 6.1 da especificação.

O [mostro-core](https://github.com/MostroP2P/mostro-core) lançou [v0.11.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.11.0) com as adições correspondentes à biblioteca: a [PR #144](https://github.com/MostroP2P/mostro-core/pull/144) adiciona `Action::PayBondInvoice` e `Status::WaitingTakerBond`, e a [PR #143](https://github.com/MostroP2P/mostro-core/pull/143) adiciona o payload `BondResolution` para ações de liquidação e cancelamento de administrador. O [mostro-cli](https://github.com/MostroP2P/mostro-cli) lançou [v0.15.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.15.0) atualizando para mostro-core 0.11.0.

### Jumble lança cinco versões com pesquisa recente e persistência de conta

O [Jumble](https://github.com/CodyTseng/jumble), o cliente Nostr centrado em relay disponível como app web e app desktop Electron, lançou cinco versões esta semana: [v26.5.2](https://github.com/CodyTseng/jumble/releases/tag/v26.5.2) a [v26.5.6](https://github.com/CodyTseng/jumble/releases/tag/v26.5.6). O v26.5.2 agrupa notificações por Hoje / Esta semana / Este mês / Anteriores com cabeçalhos de data fixos. O v26.5.3 lança um `.zip` macOS a par do `.dmg` para que a versão desktop Electron possa aplicar atualizações automáticas no local. O v26.5.4 adiciona um seletor de emoji implementado internamente com abas de pacotes de emoji. O v26.5.5 adiciona histórico de pesquisa recente. Um bug crítico de persistência é corrigido no v26.5.6: as contas e dados em cache sobrevivem agora a um reinício completo da app.

### Nostrord lança modais de partilha de grupo, upload de media e pacotes Arch Linux

O [Nostrord](https://github.com/nostrord/nostrord), um cliente Nostr direcionado a grupos baseados em relay NIP-29, lançou [v1.0.0](https://github.com/nostrord/nostrord/releases/tag/v1.0.0), [v1.0.1](https://github.com/nostrord/nostrord/releases/tag/v1.0.1) e [v1.0.2](https://github.com/nostrord/nostrord/releases/tag/v1.0.2) esta semana. O v1.0.1 lança pacotes Arch Linux via AUR como `nostrord-bin` com artefactos `.pkg.tar.zst` assinados com PGP ([PR #44](https://github.com/nostrord/nostrord/pull/44)), um botão para saltar para o mais recente quando se está a rolar para cima num canal ativo ([PR #45](https://github.com/nostrord/nostrord/pull/45)), e colagem de imagem e media diretamente no input de chat ([PR #46](https://github.com/nostrord/nostrord/pull/46)). O v1.0.2 adiciona partilha de grupo via [PR #49](https://github.com/nostrord/nostrord/pull/49) com um modal de partilha que gera tanto um URI `nostr:naddr` (kind 39000, NIP-19 + NIP-21) como um link `nostrord.com/open/` compatível com web.

### FIPS v0.3.0 lança alcance multiplataforma, descoberta de pares Nostr e gateway para LANs não modificadas

O [FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System), o projeto de rede mesh nativo de Nostr coberto no [#20](/pt/newsletters/2026-04-29-newsletter/#fips-adiciona-bootstrap-udpnat-baseado-em-nostr), lançou [v0.3.0](https://github.com/jmcorgan/fips/releases/tag/v0.3.0) esta semana, um marco importante que alarga o projeto de Linux-only para Linux, macOS, Windows e OpenWrt.

A principal adição é a descoberta de pares mediada por Nostr com travessia NAT UDP assistida por STUN. Os nós publicam agora anúncios de overlay assinados como eventos substituíveis parametrizados kind:37195 em relays Nostr públicos. Quando ambos os pares estão atrás de NAT, o daemon coordena um hole punch usando sinalização [NIP-59 (Gift Wrap)](/pt/topics/nip-59/) para a troca offer/answer.

Um novo binário `fips-gateway` permite que hosts LAN não modificados alcancem destinos mesh sem executar o daemon FIPS. A mesma troca ring 0.17 ChaCha20-Poly1305 que impulsionou o salto de débito do Nostr VPN esta semana também chega ao FIPS v0.3.0. Os benchmarks em aarch64 mostram o stream único TCP de dois nós a passar de 437 para 1097 Mbps e a latência de ping do caminho de relay de três nós a cair de uma média de 7,68 ms para 0,72 ms.

### Camelus v1.10.1 lança versões desktop

O [Camelus](https://github.com/leo-lox/camelus), o cliente Nostr para Android e desktop, lançou [v1.10.1](https://github.com/leo-lox/camelus/releases/tag/v1.10.1) com versões desktop para Windows e Linux, expandindo de uma distribuição apenas para dispositivos móveis.

### Flotilla 1.8.0 lança videochamadas, renderização de email e menções de sala

O [Flotilla](https://flotilla.social), a app de chat de grupo baseada em relay [NIP-29](/pt/topics/nip-29/) do hodlbod, lançou [1.8.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.8.0) esta semana com várias adições notáveis. As salas de voz suportam agora vídeo: os participantes podem ligar câmaras ou partilhar o ecrã durante uma chamada. A renderização de email chega através de uma atualização à biblioteca welshman: o Flotilla pode agora receber mensagens que incorporam conteúdo de email HTML, renderizando o HTML inline com formatação, imagens e links intactos. As menções de sala permitem que os utilizadores referenciem outras salas e relays com links inline clicáveis. A pesquisa de espaço inclui agora conteúdo de mensagens e correspondências locais para além dos nomes de canais.

### Calendar by Formstr lança v1.5.1 com agendamento de consultas e sincronização com calendário Android

O [Calendar by Formstr](https://calendar.formstr.app) ([github.com/formstr-hq/nostr-calendar](https://github.com/formstr-hq/nostr-calendar)), uma app de calendário nativa Nostr para eventos públicos e privados, lançou [v1.5.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.0) a 10 de maio e [v1.5.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.1) a 11 de maio. O agendamento de consultas chega na [PR #89](https://github.com/formstr-hq/nostr-calendar/pull/89), permitindo que os utilizadores criem slots de tempo reserváveis no seu calendário. A integração de calendário Android somente leitura na [PR #123](https://github.com/formstr-hq/nostr-calendar/pull/123) sincroniza eventos Nostr com o calendário do dispositivo. As notificações de eventos chegam na [PR #130](https://github.com/formstr-hq/nostr-calendar/pull/130). O v1.5.1 segue com uma correção de bug de URL e atualização de metadados ZSP.

## Em desenvolvimento

### Amethyst adiciona posts agendados, regras de comunidade NIP-9A e relay local desktop

O [Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android rico em funcionalidades, fundiu 78 PRs esta semana em várias áreas de funcionalidades importantes.

Os posts agendados chegam ao Android na [PR #2765](https://github.com/vitorpamplona/amethyst/pull/2765): os utilizadores podem compor uma nota e definir um tempo de publicação futuro, com a fila gerida localmente no dispositivo. Uma versão desktop ganha um relay local embutido com persistência de eventos SQLite na [PR #2841](https://github.com/vitorpamplona/amethyst/pull/2841).

Três PRs implementam regras de comunidade NIP-9A diretamente no cliente: a [PR #2798](https://github.com/vitorpamplona/amethyst/pull/2798) valida posts contra regras de comunidade no compositor antes de enviar, a [PR #2799](https://github.com/vitorpamplona/amethyst/pull/2799) adiciona um editor de regras NIP-9A estruturado ao fluxo de nova comunidade, e a [PR #2800](https://github.com/vitorpamplona/amethyst/pull/2800) adiciona um filtro de feed NIP-9A opcional. A [PR #2812](https://github.com/vitorpamplona/amethyst/pull/2812) redige segredos e payloads sensíveis dos logs de debug. A [PR #2821](https://github.com/vitorpamplona/amethyst/pull/2821) adiciona tags ricas [NIP-92 (imeta)](/pt/topics/nip-92/) a cada evento HLS publicado e autopublica uma nota kind:1 auxiliar para que as transmissões ao vivo apareçam em feeds padrão.

### Shopstr adiciona registo de auditoria MCP e segurança de sessão

O [Shopstr](https://github.com/shopstr-eng/shopstr), o mercado descentralizado no Nostr, fundiu cinco PRs esta semana. O registo de auditoria para a camada de ferramentas MCP chega na [PR #456](https://github.com/shopstr-eng/shopstr/pull/456). A segurança de sessão reforça-se na [PR #477](https://github.com/shopstr-eng/shopstr/pull/477), que fixa sessões MCP à sua chave API de origem e adiciona desalocação por TTL para evitar sequestro de sessão.

### Dart NDK adiciona suporte web e verificação de assinatura de seal

O [Dart NDK](https://github.com/relaystr/dart_ndk), a biblioteca Dart para desenvolvimento de protocolo Nostr usada em apps Flutter, fundiu seis PRs esta semana. O suporte web chega no `SembastCacheManager` via [PR #571](https://github.com/relaystr/dart_ndk/pull/571). A verificação de assinatura de seal chega na [PR #595](https://github.com/relaystr/dart_ndk/pull/595) para o fluxo [NIP-59 (Gift Wrap)](/pt/topics/nip-59/).

### rust-nostr refatora tags e conexão proxy

O [rust-nostr](https://github.com/rust-nostr/nostr), o SDK Rust com bindings para Python, Kotlin, Swift e JavaScript, fundiu três PRs esta semana. A [PR #1347](https://github.com/rust-nostr/nostr/pull/1347) é uma grande reformulação de tags que normaliza o acesso a tags em todo o SDK. A [PR #1351](https://github.com/rust-nostr/nostr/pull/1351) substitui o tipo `Connection` por `Proxy` na camada SDK.

### Sprout lança v0.0.10 e v0.0.11

O [Sprout](https://github.com/block/sprout), o cliente Nostr e relay da Block coberto no [#21](/pt/newsletters/2026-05-06-newsletter/#sprout-lança-desktop-v004-e-v005-juntamente-com-autenticação-de-agente-nip-oa-e-o-sidecar-relay-de-emparelhamento), lançou [v0.0.10](https://github.com/block/sprout/releases/tag/v0.0.10) e [v0.0.11](https://github.com/block/sprout/releases/tag/v0.0.11) com melhorias no autocompletar de menções, suporte para download de imagens e correções de tratamento de erros de agentes.

### Clave continua o rollout de NostrConnect multi-conta

O [Clave](https://github.com/DocNR/clave), o signatário remoto iOS NIP-46 coberto no [#21](/pt/newsletters/2026-05-06-newsletter/#clave-v020-lança-multi-conta-no-ios-com-assinatura-nip-46-nostr-connect), lançou versões adicionais esta semana avançando o trabalho de NostrConnect multi-conta. A [PR #52](https://github.com/DocNR/clave/pull/52) promove o Connect de uma folha apresentada a partir da vista principal para um tab de nível superior entre contas. Uma correção de segurança no build 71 fecha um bypass do limite de 5 ligações por conta.

## Novos projetos

### Tamagostrich lança um Tamagotchi NIP-78 descentralizado com recompensas em sats

O [Tamagostrich](https://github.com/Negr087/tamagostrich) é um jogo de animal de estimação virtual baseado em browser lançado no IDENTITY Hackathon 2026 onde um avestruz bebé, Nori, evolui através da atividade social Nostr do utilizador. O estado do animal vive num evento [NIP-78](/pt/topics/nip-78/) kind:30078 para que sincronize em todos os dispositivos que partilham o mesmo par de chaves. Zaps, reações, reposts e novos seguidores concedem XP; sem atividade, a felicidade e energia decaem 100 pontos por 24 horas. As recompensas de marco pagam em sats automaticamente via [NIP-47 (Nostr Wallet Connect)](/pt/topics/nip-47/): 50 sats no nível 5, 210 sats no nível 10 e 420 sats no nível máximo 21.

## Trabalho de protocolo e especificação

O repositório de NIPs fundiu a [PR #2338](https://github.com/nostr-protocol/nips/pull/2338) corrigindo links de referência README para tipos de eventos Marmot e o kind geocaching 37516. Cinco novas propostas abriram esta semana:

A [PR #2331](https://github.com/nostr-protocol/nips/pull/2331) propõe o **NIP-9A: Regras de Comunidade Verificáveis**, introduzindo kind:34551, um evento substituível parametrizado que permite ao proprietário de uma comunidade publicar um documento de regras legível por máquina e assinado criptograficamente. Os clientes obtêm as regras antes de o utilizador submeter um post e rejeitam o rascunho localmente se violar alguma regra.

A [PR #2335](https://github.com/nostr-protocol/nips/pull/2335) propõe **Eventos de Reserva para Mercados Nostr**, definindo kind:32122 (eventos de reserva substituíveis parametrizados), kind:1326 (registos de auditoria de transição apenas de adição) e kind:32124 (avaliações pós-negociação). A negociação é privada: os rascunhos de propostas são enviados como eventos filho de mensagem estruturada embrulhados em gift wrap NIP-59 entre comprador e vendedor.

A [PR #2334](https://github.com/nostr-protocol/nips/pull/2334) propõe **Serviços de Custódia para Mercados Nostr**, usando kind:30303 para operadores de custódia declararem o seu endereço de contrato EVM, hash de bytecode, cadeia suportada, tabela de taxas e tokens aceites.

A [PR #2333](https://github.com/nostr-protocol/nips/pull/2333) propõe **Perfis de Listagem de Alojamento para Listagens de Mercado NIP-99**, estendendo as listagens classificadas NIP-99 com tags de índice geoespacial H3 e campos promovidos específicos de alojamento para listagens de arrendamento de curta duração.

A [PR #2332](https://github.com/nostr-protocol/nips/pull/2332) propõe **NIP-BC: Zaps Onchain (kind 8333)**, explorando uma identidade direta entre chaves Nostr e endereços Bitcoin Taproot: uma pubkey Nostr é uma chave secp256k1 x-only de 32 bytes, tal como uma chave interna BIP-341 P2TR, o que significa que qualquer utilizador Nostr já tem um endereço Bitcoin mainnet determinístico derivável da sua pubkey, sem necessidade de LNURL, custodiante ou endereço Lightning.

## Mergulho profundo em NIP: NIP-78 (Dados específicos de app)

O [NIP-78](/pt/topics/nip-78/) define uma forma padrão para as aplicações armazenarem dados arbitrários privados ou públicos em nome de um utilizador usando eventos Nostr. O tipo de evento principal é 30078, um evento substituível parametrizado onde a tag `d` é uma string de identificador definida pela aplicação. Uma aplicação dá ao seu slot de armazenamento uma tag `d` única (por exemplo `tamagostrich-pet-state` ou `amethyst-settings`) e publica um evento 30078 com o conteúdo JSON ou texto que precisa de persistir. Como 30078 é substituível e com âmbito por tag `d`, a aplicação pode atualizar o estado armazenado publicando um novo evento com a mesma tag `d`, e o relay retém apenas a versão mais recente.

```json
{
  "id": "<hex de 64 caracteres>",
  "pubkey": "<hex de 64 caracteres>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "tamagostrich-pet-state"]
  ],
  "content": "{\"level\":7,\"xp\":1420,\"happiness\":82,\"energy\":61}",
  "sig": "<hex de 128 caracteres>"
}
```

A motivação principal é a sincronização entre dispositivos sem um servidor centralizado. Qualquer cliente que conheça a chave pública de um utilizador e a tag `d` da aplicação pode obter o estado atual do conjunto de relays do utilizador e reconstruir o estado da aplicação em qualquer dispositivo. O utilizador é dono dos dados porque vivem em eventos assinados pelo seu par de chaves.

Para dados de aplicação privados, os eventos NIP-78 podem encriptar o campo de conteúdo usando [NIP-44 (Encriptação Versionada)](/pt/topics/nip-44/) ou o mais antigo [NIP-04](/pt/topics/nip-04/) antes de publicar. Para dados de aplicação públicos, como os distintivos de conquista do Tamagostrich exibidos no perfil do utilizador, podem ser armazenados sem encriptação.

A especificação deixa deliberadamente o formato do conteúdo em aberto. As aplicações escolhem o seu próprio esquema; o NIP-78 apenas padroniza o tipo de evento e o mecanismo de âmbito por tag `d`.

Os utilizadores atuais do NIP-78 incluem o Tamagostrich (sincronização de estado do animal), o Wisp (backup de carteira kind:30078 e sincronização de definições de segurança entre dispositivos), o NosPress (estado de orquestração CMS) e várias implementações de sincronização de definições de cliente Nostr.

---

**Fontes primárias:**
- [Especificação NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich): implementação em produção esta semana

**Ver também:**
- [NIP-51: Listas](/pt/topics/nip-51/)
- [NIP-65: Metadados de Lista de Relay](/pt/topics/nip-65/)

## Mergulho profundo em NIP: NIP-98 (HTTP Auth)

O [NIP-98](/pt/topics/nip-98/) define um esquema de autenticação HTTP que permite que pares de chaves Nostr autorizem pedidos a servidores HTTP, eliminando a necessidade de nomes de utilizador, palavras-passe ou tokens OAuth para acesso a API do lado do servidor. Um cliente constrói um evento Nostr de curta duração do kind 27235, assina-o com a sua chave privada, codifica o JSON em base64 e envia-o num cabeçalho HTTP `Authorization: Nostr <base64>`.

```json
{
  "id": "<hex de 64 caracteres>",
  "pubkey": "<hex de 64 caracteres>",
  "created_at": 1747180800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<hash-sha256-do-corpo-do-pedido>"]
  ],
  "content": "",
  "sig": "<hex de 128 caracteres>"
}
```

O evento kind 27235 inclui o método HTTP numa tag `method`, o URL completo do pedido numa tag `u` e um timestamp `created_at`. O servidor valida a assinatura, verifica que o método e URL correspondem ao pedido real, e confirma que o timestamp é recente (dentro de alguns minutos) para evitar ataques de replay.

O design significa que qualquer servidor que implemente NIP-98 pode autenticar utilizadores Nostr sem qualquer registo prévio, criação de conta ou segredo partilhado. Da perspetiva do utilizador, a autenticação é transparente: a sua chave de assinatura Nostr é também a sua credencial de API.

O NIP-98 é usado no Blossom ([BUD-01](https://github.com/hzrd149/blossom/blob/master/buds/01.md)) para autenticar uploads e downloads de blobs. O Routstr usa-o para controlo de acesso à API HTTP por pedido com RBAC a nível de npub. O Sprout usa-o para autenticação de transporte git e acesso REST ao relay. O Clave usa-o para chamadas de emparelhamento proxy. O Alby Hub usa autenticação derivada de NIP-98 para a sua API de administração, e o Nostr.build usa-o para autorização de upload.

A especificação define uma extensão opcional: uma tag `payload` contendo o hash SHA-256 do corpo do pedido, que permite ao servidor verificar que o evento assinado e o corpo do pedido foram criados juntos, impedindo um MITM de substituir um corpo diferente após o cliente ter assinado o evento de autenticação.

---

**Fontes primárias:**
- [Especificação NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)
- [BUD-01: Autenticação de upload Blossom](https://github.com/hzrd149/blossom/blob/master/buds/01.md)

**Ver também:**
- [NIP-96: Integração de Armazenamento de Ficheiros HTTP](/pt/topics/nip-96/)
