---
title: 'Nostr Compass #17'
date: 2026-04-08
translationOf: /en/newsletters/2026-04-08-newsletter.md
translationDate: 2026-04-09
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) lança a [v1.08.0](#amethyst-lanca-arti-tor-e-incorpora-mls-e-marmot-em-kotlin-puro) com integração Arti Tor e uma UI de Shorts redesenhada, enquanto incorpora implementações em Kotlin puro de [MLS](/pt/topics/mls/) e [Marmot](/pt/topics/marmot/) à sua biblioteca [Quartz](/pt/topics/quartz/). [Nostur](https://github.com/nostur-com/nostur-ios-public) lança a [v1.27.0](#nostur-v1270-adiciona-gravacao-de-video-e-respostas-privadas) com gravação de vídeo, perfis com GIF animado e respostas privadas. [Shosho](https://github.com/r0d8lsh0p/shosho-releases) lança a [v0.15.0](#shosho-v0150-lanca-shows-e-carrossel-vertical-de-video) com Shows (informações personalizadas de live conectadas ao OBS) e um carrossel vertical de vídeos no estilo TikTok. [Nymchat](https://github.com/Spl0itable/NYM) [reverte Marmot e lança chats de grupo NIP-17 aprimorados](#nymchat-reverte-marmot-e-lanca-chats-de-grupo-nip-17-aprimorados) com chaves efêmeras rotativas. [Nostr VPN](https://github.com/mmalmi/nostr-vpn) lança [suporte a exit nodes e empacotamento para Umbrel](#nostr-vpn-lanca-suporte-a-exit-nodes-e-empacotamento-para-umbrel) ao longo de seis releases. [Amber](https://github.com/greenart7c3/Amber) salta para a [v6.0.0-pre1](#amber-v600-pre1-adiciona-chaves-de-assinatura-nip-46-por-conexao) com chaves de assinatura [NIP-46](/pt/topics/nip-46/) por conexão e atualizações in-app via Zapstore. [Notedeck](https://github.com/damus-io/notedeck) chega à [v0.10.0-beta](#notedeck-v0100-beta-lanca-self-update-via-zapstore) com self-update de APK via Zapstore, e [NIP-58](/pt/topics/nip-58/) (Badges) recebe uma [migração de kind](#atualizacoes-de-nips). Dois deep dives de NIP cobrem [NIP-17](/pt/topics/nip-17/) (Private Direct Messages) e [NIP-46](/pt/topics/nip-46/) (Nostr Remote Signing).

## Notícias

### Amethyst lança Arti Tor e incorpora MLS e Marmot em Kotlin puro

[Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android mantido por vitorpamplona, lançou quatro releases da [v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3) até a [v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0) e incorporou um grande lote de trabalho ainda não lançado à sua biblioteca [Quartz](/pt/topics/quartz/) (o módulo Nostr compartilhado em Kotlin Multiplatform). O release principal é a v1.08.0 "Arti Tor", que migra a conectividade Tor do app da biblioteca Tor baseada em C para [Arti](https://gitlab.torproject.org/tpo/core/arti), a implementação em Rust do Tor Project. A migração resolve crashes aleatórios que aconteciam com os bindings anteriores de Tor em C. Arti é o substituto de longo prazo do Tor Project para a codebase em C, escrito do zero em Rust para memory safety e async I/O.

O release v1.07.3 redesenhou a UI de Shorts, substituindo o design paginado por feeds edge-to-edge para fotos, shorts e vídeos longos. O mesmo release migrou badges para kind `10008` e bookmarks para kind `10003`, alinhando-se à migração de kind de [NIP-58](/pt/topics/nip-58/) [mergeada nesta semana](#atualizacoes-de-nips). A v1.07.4 corrigiu um problema no tratamento de secret do Nostr Wallet Connect, e a v1.07.5 corrigiu um crash no upload de imagens.

Na branch main, mas ainda sem release com tag, a equipe escreveu uma implementação completa em Kotlin tanto de [MLS](/pt/topics/mls/) quanto do protocolo [Marmot](/pt/topics/marmot/), eliminando a necessidade de bindings nativos de bibliotecas C/Rust. O [PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147) adiciona a camada central de mensagens de grupo Marmot MLS, o [PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149) adiciona a UI de chat em grupo, o [PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146) adiciona processadores de mensagens de entrada e saída com um subscription manager, o [PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141) adiciona persistência do estado de grupo MLS e gerenciamento de rotação de KeyPackage, o [PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150) adiciona uma suíte completa de testes de MLS com assinatura de GroupInfo aprimorada, e o [PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158) adiciona rastreamento do status de publicação de KeyPackage. O [PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166) adiciona uma implementação secp256k1 em Kotlin puro para operações criptográficas de Nostr, substituindo a dependência da biblioteca nativa em C. Combinado com a implementação de MLS em Kotlin, [Quartz](/pt/topics/quartz/) pode executar assinatura Nostr e mensagens de grupo Marmot sem nenhum binding nativo, o que abre caminho para targets Kotlin Multiplatform incluindo iOS.

A equipe também está construindo suporte a [NIP-AC](/en/topics/nip-ac/) (P2P Voice and Video Calls): o [PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143) adiciona uma suíte completa de testes para a máquina de estados de chamadas do NIP-AC, e o [PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164) impede que ofertas de chamada antigas sejam disparadas novamente após reiniciar o app.

### Nostur v1.27.0 adiciona gravação de vídeo e respostas privadas

[Nostur](https://github.com/nostur-com/nostur-ios-public), o cliente Nostr para iOS, lançou a [v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0) em 2 de abril. O release adiciona gravação de vídeo dentro do app com corte antes do upload, para que usuários possam capturar clipes curtos, ajustá-los ao tamanho desejado e publicar sem sair do cliente. O suporte a GIF animado se estende a fotos de perfil e de banner, com renderização de WebP animado adicionada também. Uma nova integração com Shortcuts permite que usuários enviem posts Nostr a partir de automações do Apple Shortcuts. O release também adiciona respostas privadas e corrige problemas de compatibilidade de DM que afetavam a entrega de mensagens entre Nostur e outros clientes.

### Shosho v0.15.0 lança Shows e carrossel vertical de vídeo

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), o app de live streaming Nostr, lançou a [v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0) e a [v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1) em 7 de abril. O recurso principal é Shows: streamers podem configurar informações personalizadas do show antes de entrar ao vivo e conectar seu show ao OBS ou a qualquer encoder externo. Isso separa os metadados de "o que estou transmitindo" do ato de entrar ao vivo, de modo que streamers possam preparar títulos, descrições e produtos antes de começar a transmitir. O mesmo release adiciona um carrossel vertical de vídeo no estilo TikTok para navegar por lives, clipes e replays em um feed de tela cheia, além de Quick Add para publicar clipes de vídeo e adicionar produtos diretamente de uma página de perfil. A v0.15.1 corrige um bug em que o teclado escondia o campo de entrada do chat da live.

## Lançamentos

### Notedeck v0.10.0-beta lança self-update via Zapstore

[Notedeck](https://github.com/damus-io/notedeck), o cliente desktop e mobile da equipe Damus, lançou a [v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1) e a [v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2) como prereleases de teste para self-update de APK. O [PR #1417](https://github.com/damus-io/notedeck/pull/1417) adiciona self-update de APK via o atualizador Nostr/Zapstore no Android, expandindo o [trabalho de descoberta de atualizações nativa do Nostr da Newsletter #14](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr). O fluxo de atualização descobre novos releases por meio de eventos Nostr publicados em relays, depois baixa o APK de onde quer que o desenvolvedor o hospede (GitHub releases, Blossom CDN ou outras fontes), verifica o hash SHA-256 contra o evento Nostr assinado e faz a instalação. O [PR #1438](https://github.com/damus-io/notedeck/pull/1438) corrige um bug na tela de boas-vindas em que os botões Login e CreateAccount navegavam imediatamente de volta, e o [PR #1424](https://github.com/damus-io/notedeck/pull/1424) corrige overflow de texto na visualização de sessão do Agentium AI.

### Amber v6.0.0-pre1 adiciona chaves de assinatura NIP-46 por conexão

[Amber](https://github.com/greenart7c3/Amber), o app assinador [NIP-55](/pt/topics/nip-55/) (Android Signer Application), lançou a [v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1) em 4 de abril. A mudança mais importante é o uso de chaves de assinatura por conexão para o protocolo bunker [NIP-46](/pt/topics/nip-46/) (Nostr Remote Signing). Em vez de usar um único par de chaves para todas as conexões bunker, o Amber agora gera uma chave distinta para cada cliente conectado. Se a conexão de um cliente for comprometida, o invasor não pode se passar pelo signer para outros clientes.

O [PR #377](https://github.com/greenart7c3/Amber/pull/377) adiciona verificação e instalação de atualizações in-app via Zapstore, juntando-se ao [Notedeck](#notedeck-v0100-beta-lanca-self-update-via-zapstore) na adoção de distribuição de apps nativa do Nostr. O [PR #375](https://github.com/greenart7c3/Amber/pull/375) trata falhas de AndroidKeyStore de forma segura ao exibir um aviso aos usuários em vez de causar crash, e o [PR #371](https://github.com/greenart7c3/Amber/pull/371) adiciona limpeza de banco de dados com limites de tamanho e truncamento de conteúdo para impedir crescimento ilimitado de armazenamento. O pre-release também carrega a whitelist de relay auth [NIP-42](/pt/topics/nip-42/) e o login por frase de recuperação mnemônica do [ciclo v5.0.x coberto na semana passada](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504).

### Nostria lança app mobile nativo

[Nostria](https://github.com/nostria-app/nostria), o cliente Nostr multiplataforma mantido por SondreB, lançou um app mobile nativo para Android com oito releases da [v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11) até a [v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18). A nova capacidade mais importante é o suporte nativo a signer local para signers como [Amber](https://github.com/greenart7c3/Amber) e Aegis. Também estão disponíveis [instaladores desktop](https://www.nostria.app/download) para Linux, macOS e Windows. O [PR #610](https://github.com/nostria-app/nostria/pull/610) reduz a pressão de memória do feed com limites adaptativos em runtime e limpeza de preview URLs. A v3.1.14 corrige a integração com Brainstorm, um provedor de [Web of Trust](/pt/topics/web-of-trust/). A v3.1.15 se concentra em melhorias de música. O novo app Android está disponível no [Zapstore](https://zapstore.dev/apps/app.nostria).

### diVine 1.0.8 lança uploads retomáveis e DMs

[diVine](https://github.com/divinevideo/divine-mobile), o cliente de vídeo short-form, lançou a [1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8) com 87 PRs mergeados. Uploads retomáveis permitem que criadores continuem uploads interrompidos chunk por chunk em vez de reiniciar do zero em uma conexão instável. O release adiciona configurações de qualidade de vídeo e bitrate, double-tap para curtir e melhorias em DMs. O [PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722) adiciona um plugin de câmera para macOS para captura de vídeo no desktop, e o [PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820) migra o sistema de notificações para uma arquitetura BLoC com enriquecimento e agrupamento. A equipe também substituiu stickers e artes de categoria gerados por AI por SVGs do OpenMoji ([PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844), [PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)).

### Manent v1.3.0 adiciona desfoque de notas sensíveis e auth NIP-42

[Manent](https://github.com/dtonon/manent), o app privado de notas criptografadas e armazenamento de arquivos, lançou a [v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0) em 2 de abril. Usuários agora podem marcar notas como sensíveis para desfocá-las na visualização em lista, mantendo conteúdo privado oculto durante rolagens casuais. O release também adiciona suporte a [NIP-42](/pt/topics/nip-42/) (Authentication of Clients to Relays), permitindo que o Manent se autentique em relays que exigem isso antes de aceitar eventos. O Manent armazena todos os dados criptografados em relays Nostr usando o par de chaves do usuário, então o suporte a NIP-42 amplia o conjunto de relays que ele pode usar para armazenamento.

### Wisp v0.17.0 até v0.17.3 adicionam zaps em live stream e backup de carteira

[Wisp](https://github.com/barrydeen/wisp), o cliente Nostr para Android, lançou seis releases da [v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta) até a [v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta) com 44 PRs mergeados. O release v0.17.0 adiciona prompts de segurança para backup de carteira e melhorias na UX de zap. A [v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta) adiciona visibilidade de chat de live stream entre plataformas e funcionalidade de zap em live stream. O [PR #423](https://github.com/barrydeen/wisp/pull/423) adiciona auto-search de perfis, uma animação de sucesso de zap e melhorias de status do usuário. O [PR #426](https://github.com/barrydeen/wisp/pull/426) corrige um crash por falta de memória em `computeId` para eventos com listas grandes de tags. Os releases v0.16.x adicionaram autocomplete de shortcode de emoji, melhorias na UI de chat em grupo e filtragem de usuários bloqueados em todos os caminhos de notificação.

### Mostro lança deep links, taxas de câmbio do Nostr e uma correção para pagamento duplicado

[Mostro](https://github.com/MostroP2P/mostro), a exchange peer-to-peer de Bitcoin construída sobre Nostr, teve atualizações tanto em seu daemon de servidor quanto em seu cliente mobile nesta semana. No lado do servidor, o [PR #692](https://github.com/MostroP2P/mostro/pull/692) impede que escritas antigas de ordens causem pagamentos duplicados, um bug que poderia fazer com que um vendedor recebesse duas vezes pela mesma negociação. O [PR #693](https://github.com/MostroP2P/mostro/pull/693) usa atualizações direcionadas para escritas de dev_fee em vez de sobrescrever a ordem inteira.

[Mostro Mobile](https://github.com/MostroP2P/mobile), o cliente Flutter, lançou a [v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3) em 3 de abril. O release trata deep links de diferentes instâncias do Mostro, para que usuários possam tocar em links que os encaminham ao servidor de exchange correto. O [PR #498](https://github.com/MostroP2P/mobile/pull/498) detecta DMs de admin e de disputa no pipeline de notificações em background, e o app agora busca taxas de câmbio via Nostr com fallback HTTP/cache. O [PR #560](https://github.com/MostroP2P/mobile/pull/560) corrige um bug de bloqueio de conexão com relay que impedia o app de alcançar relays em certas condições de rede.

### Unfiltered v1.0.12 adiciona hashtags e comentários

[Unfiltered](https://github.com/dmcarrington/unfiltered), um cliente Nostr focado em conteúdo orientado por imagem, lançou a [v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12). O [PR #69](https://github.com/dmcarrington/unfiltered/pull/69) adiciona suporte a hashtag e o [PR #72](https://github.com/dmcarrington/unfiltered/pull/72) adiciona a capacidade de escrever e exibir comentários em posts. O [PR #71](https://github.com/dmcarrington/unfiltered/pull/71) corrige problemas de navegação com múltiplas imagens por post.

### Primal Android lança compartilhamento multi-conta de carteira e auto-reconnect do remote signer

[Primal](https://github.com/PrimalHQ/primal-android-app), o cliente Nostr para Android, lançou um release em 7 de abril. A atualização adiciona compartilhamento multi-conta de carteira e menu overflow com deleção de carteira em Dev Tools. O remote signer agora faz auto-reconnect quando a conexão cai, e o serviço de carteira ganhou sua própria lógica de auto-reconnect. As correções incluem votos de zap em enquetes que não aparecem mais como Top Zaps, prevenção de crash com opção de enquete vazia, ocultação do saldo da carteira quando não existe carteira, e mapeamento do tipo WalletException para códigos de erro em respostas NWC.

### Titan v0.1.0 lança navegador nativo nsite:// com registro de nomes no Bitcoin

[Titan](https://github.com/btcjt/titan), um navegador desktop nativo para a web do Nostr, lançou a [v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0) em 7 de abril. O Titan resolve URLs `nsite://` consultando nomes legíveis por humanos registrados no Bitcoin, consultando relays Nostr pelos eventos de conteúdo do site e renderizando páginas buscadas em servidores [Blossom](/pt/topics/blossom/). O resultado é uma experiência de navegação web sem DNS, sem certificados TLS e sem provedores de hospedagem. Os nomes são registrados por meio de uma [interface web](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register) vinculada a transações de Bitcoin. O release inicial sai como um `.dmg` para macOS (ARM, com suporte a Rosetta 2 para Intel) e inclui suporte a ambiente de desenvolvimento Nix.

### Bikel v1.5.0 lança serviço foreground nativo para telefones sem Google

[Bikel](https://github.com/Mnpezz/bikel), um rastreador de ciclismo descentralizado que transforma trajetos em dados de infraestrutura pública usando Nostr, lançou a [v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0) em 4 de abril. O release migra do Expo TaskManager dependente de GMS para um serviço foreground nativo customizado, garantindo rastreamento confiável de percursos em background em LineageOS, GrapheneOS e outras variantes Android sem Google. O Bikel Bot ganhou uma arquitetura dual-pocket com coleta autônoma de eCash via Cashu nutzaps. As v1.4.3 e v1.4.2 corrigem sincronização do rastreamento em background para ambientes Android não padrão, e o app adiciona toggles para pontos de mapa de bicicletários no OSM.

### Sprout adiciona suporte a NIP-01, NIP-23 e NIP-33

[Sprout](https://github.com/block/sprout), uma plataforma de comunicação da Block com um relay Nostr embutido, lançou a [desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7) em 6 de abril. Nesta semana a equipe adicionou suporte a artigos kind `30023` de [NIP-23](/en/topics/nip-23/) (Long-form Content), eventos parameterized replaceable [NIP-33](/en/topics/nip-33/) com substituição identificada por tag `d`, e notas de texto kind `1` e listas de follows kind `3` de [NIP-01](/pt/topics/nip-01/)/[NIP-02](/en/topics/nip-02/). O release também adiciona um sistema adaptativo de tema de IDE com 54 temas, polimento na UX do histórico de workflows e execuções de agentes, e uma limpeza da barra lateral de membros.

### mesh-llm v0.56.0 lança protocolo distribuído de configuração

[mesh-llm](https://github.com/michaelneale/mesh-llm), um sistema distribuído de inferência de LLM que usa pares de chaves Nostr para identidade de nó, lançou a [v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0) em 7 de abril. O release adiciona um protocolo distribuído de configuração com semântica de ownership, quantização assimétrica de cache KV (chaves Q8_0 com valores Q4) para reduzir uso de memória, armazenamento em keychain do SO para keystores de identidade, streaming suave de chat com fila de mensagens, e correções para layout em tela cheia e divisão de cache KV com flash attention.

### Nostr VPN lança suporte a exit nodes e empacotamento para Umbrel

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), uma VPN peer-to-peer que usa relays Nostr para sinalização e WireGuard para túneis criptografados, lançou seis releases da [v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0) até a [v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6) nesta semana. O ciclo v0.3.x adiciona suporte a exit node no Windows e macOS, permitindo que peers roteiem tráfego de internet por outros nós da rede. A propagação de invites e aliases agora sincroniza sobre Nostr, para que usuários possam compartilhar acesso à rede sem coordenação fora de banda. Os releases adicionam empacotamento para Umbrel para deployment self-hosted, NAT punch-through usando endpoints públicos memorizados, limpeza automática de exit nodes obsoletos e uma especificação de protocolo publicada. O projeto também estabilizou o tratamento de rotas no macOS com rotas padrão auto-recuperáveis e reparo de underlay, e adicionou uma build Android via Tauri. Há builds disponíveis para macOS (Apple Silicon e Intel), Linux (AppImage e .deb), Windows e Android.

### Nymchat reverte Marmot e lança chats de grupo NIP-17 aprimorados

[Nymchat](https://github.com/Spl0itable/NYM), o cliente de chat com suporte a MLS, lançou 14 releases da [v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261) até a [v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274). A mudança mais significativa é uma guinada de protocolo: a [v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261) adicionou chats de grupo Marmot MLS, mas a [v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268) reverteu de volta para [NIP-17](/pt/topics/nip-17/) porque o suporte multi-device do Marmot ainda não está concluído, o que causava problemas na sincronização do estado do chat de grupo entre dispositivos. A v3.58.271 introduz chats de grupo NIP-17 aprimorados com chaves efêmeras rotativas para todas as mensagens, projetadas para impedir ataques de timing e correlação. A semana também trouxe um sistema de friends com controle granular de settings ([v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)), sincronização de mensagens de chat em grupo MLS em settings criptografadas do app, e múltiplas correções de conectividade com relay.

### nak v0.19.5 adiciona multi-server Blossom e publicação por outbox

[nak](https://github.com/fiatjaf/nak), o toolkit de linha de comando Nostr do fiatjaf, lançou a [v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5). O comando `blossom` agora aceita múltiplas flags `--server` para fazer upload para vários servidores [Blossom](/pt/topics/blossom/) em uma só chamada. Um novo comando `key` expande chaves parciais preenchendo com zeroes à esquerda. O comando `event` ganha uma flag `--outbox` para publicar eventos pelo modelo outbox, e `fetch` agora sai com código de erro quando nenhum event é retornado.

## Em desenvolvimento

### White Noise adiciona previews com thumbhash e bridge de registro de push

[White Noise](https://github.com/marmot-protocol/whitenoise), o mensageiro privado construído sobre o protocolo [Marmot](/pt/topics/marmot/), mergeou cinco PRs. O [PR #549](https://github.com/marmot-protocol/whitenoise/pull/549) substitui previews de imagem com blurhash por thumbhash, um algoritmo mais novo que produz imagens placeholder mais nítidas com payload menor (normalmente abaixo de 30 bytes contra cerca de 50-100 bytes do blurhash), preservando a proporção e a distribuição de cores da imagem original. Blurhash permanece como fallback para conteúdo mais antigo. O [PR #548](https://github.com/marmot-protocol/whitenoise/pull/548) atualiza whitenoise-rs e adiciona a bridge de registro de push [MIP-05](/pt/topics/mip-05/), conectando ao cliente o [trabalho de spec de push notifications da semana passada](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications). O [PR #493](https://github.com/marmot-protocol/whitenoise/pull/493) adiciona paginação baseada em cursor para mensagens de chat, substituindo a estratégia anterior de carregamento por uma abordagem guiada por scroll.

### Route96 adiciona configuração dinâmica de labels e limpeza zero-egress

[Route96](https://github.com/v0l/route96), o servidor de mídia [Blossom](/pt/topics/blossom/) do v0l, mergeou três PRs. O [PR #80](https://github.com/v0l/route96/pull/80) adiciona configuração dinâmica de modelo de labels via a admin API, permitindo que operadores troquem modelos de classificação de conteúdo sem reiniciar o servidor. O [PR #82](https://github.com/v0l/route96/pull/82) adiciona campos de configuração de labels à admin UI. O [PR #79](https://github.com/v0l/route96/pull/79) adiciona uma política de limpeza de arquivos zero-egress que remove automaticamente arquivos que nunca foram baixados, reduzindo custos de armazenamento para operadores.

### Snort lança endurecimento de segurança e invoices de pagamento para DVM

[Snort](https://github.com/v0l/snort), o cliente web, lançou dois releases nesta semana junto com uma auditoria de segurança abrangente. As correções incluem verificação de assinatura Schnorr, proteção contra falsificação de mensagens de relay em [NIP-46](/pt/topics/nip-46/) (impedindo que atacantes injetem requests de assinatura por relays comprometidos), melhorias na criptografia de PIN e remoção da confiança em delegação NIP-26. Os ganhos de desempenho vêm de verificação Schnorr em lote em WASM, rotas lazy-loaded, traduções pré-compiladas e eliminação da verificação dupla por event. O [PR #618](https://github.com/v0l/snort/pull/618) adiciona exibição de invoice exigindo pagamento para kind `7000` de [NIP-90](/en/topics/nip-90/) (Data Vending Machine), de modo que quando um DVM responde com uma exigência de pagamento, o Snort renderiza a invoice Lightning diretamente no feed.

### Damus melhora compactação do LMDB

[Damus](https://github.com/damus-io/damus), o cliente iOS, mergeou o [PR #3719](https://github.com/damus-io/damus/pull/3719) adicionando compactação automática do LMDB em um cronograma, evitando que o banco de dados local cresça sem limites ao longo do tempo. O [PR #3663](https://github.com/damus-io/damus/pull/3663) melhora o BlurOverlayView para que pareça protetor em vez de quebrado.

### Captain's Log adiciona indexação de tags e sincronização de notas

[Captain's Log](https://github.com/nodetec/captains-log) (Comet), a ferramenta Nostr-native de escrita long-form da Nodetec, mergeou quatro PRs nesta semana. O [PR #156](https://github.com/nodetec/captains-log/pull/156) adiciona indexação de tags e suporte a sync entre notas, o [PR #157](https://github.com/nodetec/captains-log/pull/157) refatora a sincronização de notas e o tratamento de tags, e o [PR #159](https://github.com/nodetec/captains-log/pull/159) corrige a sync de notas enviadas para a lixeira para que notas deletadas permaneçam deletadas entre dispositivos.

### Relatr v0.2.x redesenha sistema de plugins com marketplace de validadores nativo do Nostr

[Relatr](https://github.com/ContextVM/relatr), um motor de pontuação de [Web of Trust](/pt/topics/web-of-trust/) que calcula rankings de confiança com base na distância do grafo social e em validadores configuráveis, lançou a família v0.2.x com um redesenho completo do sistema de plugins. Validadores agora são escritos em Elo, uma linguagem funcional portátil de expressões bifurcada para suportar capacidades em múltiplas etapas orquestradas pelo host (consultas Nostr, buscas no grafo social, resolução NIP-05). Plugins são publicados como eventos Nostr kind `765`, tornando a distribuição nativa da rede de relays. Um novo [plugin marketplace](https://relatr.net) permite que operadores descubram, instalem e ponderem validadores a partir do navegador, com um CLI (`relo`) para autoria e publicação local. A arquitetura é sandboxed: plugins só podem invocar capacidades que o host fornece explicitamente, então um validador malicioso não pode escapar de seu escopo definido. Instâncias do Relatr agora podem ser gerenciadas a partir do site, com visibilidade total sobre quais plugins compõem o algoritmo de pontuação e seus pesos individuais.

### Shopstr melhora navegação mobile e controle de acesso

[Shopstr](https://github.com/shopstr-eng/shopstr), o marketplace Nostr-native para compra e venda com Bitcoin, publicou 158 commits nesta semana entre seu app principal e o projeto complementar [Milk Market](https://github.com/shopstr-eng/milk-market). As correções incluem melhorias no layout mobile de comunidades, comportamento de fechar menus ao navegar e auto-close de dropdowns. Rotas protegidas não podem mais ser acessadas por URL direta sem login, e a lógica de correspondência de slug agora lida corretamente com múltiplas correspondências exatas.

### Pollerama adiciona notificações, busca de filmes e UI de avaliação

[Pollerama](https://github.com/formstr-hq/nostr-polls), um app de enquetes, surveys e rating social construído sobre Nostr, adicionou notificações de threads, um recurso de busca de filmes e uma reformulação da UI de avaliação. O release também corrige problemas de carregamento do feed e atualiza versões de dependências.

### Purser constrói daemon de pagamentos Nostr-native com criptografia Marmot

[Purser](https://github.com/EthnTuttle/purser), um daemon de pagamentos Nostr-native projetado como substituto do Zaprite, mergeou nove PRs nesta semana enquanto desenvolvia sua arquitetura central. O projeto usa MLS do [Marmot](/pt/topics/marmot/) via MDK para mensagens criptografadas entre merchant e customer, com Strike e Square como provedores de pagamento. Nesta semana entraram carregamento de config e catálogo, validação de schema de mensagens, a camada de comunicação MDK, implementações dos provedores Strike e Square, um polling engine, limitação anti-spam de taxa, persistência de pagamentos pendentes e o pipeline de processamento de pedidos. Todos os 99 testes agora exercitam operações reais de MLS do mdk-core depois que a equipe removeu MLS mockado em favor de criptografia real em modo local.

### Vector refatora anexos de DM e adiciona edição de perfil

[Vector](https://github.com/VectorPrivacy/Vector), o mensageiro Nostr focado em privacidade construído com Tauri, mergeou o [PR #55](https://github.com/VectorPrivacy/Vector/pull/55) refatorando o frontend. A decriptação e o salvamento de anexos de DM foram movidos para a biblioteca vector-core, e o app agora suporta edição de perfil. A flag de cancelamento de upload foi corretamente conectada via TauriSendCallback, e callbacks não usados de preview de anexos foram removidos.

## Trabalho de Protocolo e Spec

### Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado:**

- **[NIP-58](/pt/topics/nip-58/) (Badges): Profile Badges passam para kind 10008, Badge Sets para kind 30008** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Migra Profile Badges de kind `30008` para kind `10008` (um event replaceable, um por pubkey) e introduz kind `30008` para Badge Sets. Antes, Profile Badges usavam o mesmo kind (`30008`) que as definições de Badge, tornando-os eventos parameterized replaceable identificados por uma tag `d`. O novo kind `10008` é um event replaceable simples: um por pubkey, sem necessidade de tag `d`. Clientes consultam um único event replaceable por usuário em vez de varrer eventos parameterized replaceable. O Amethyst v1.07.3 já sai com essa migração.

- **[NIP-34](/pt/topics/nip-34/) (Git Stuff): adicionar follow lists relacionadas a git** ([PR #2130](https://github.com/nostr-protocol/nips/pull/2130)): Adiciona convenções de follow lists para tracking de repositórios e issues do NIP-34. Usuários publicam conjuntos de follows kind `30000` com tags `d` como `git-repos` ou `git-issues` contendo referências de tag `a` a repositórios (kind `30617`) que querem acompanhar. Clientes podem se inscrever nesses conjuntos de follows para mostrar atividade de repositório no feed de um usuário, de forma semelhante a como listas de contatos kind `3` funcionam para pubkeys.

**PRs abertos e discussões:**

- **NIP-AC: P2P Voice and Video Calls over WebRTC** ([PR #2301](https://github.com/nostr-protocol/nips/pull/2301)): Expande o NIP-100 original (implementado pelo 0xChat) com três mudanças: migração para criptografia [NIP-44](/pt/topics/nip-44/) encapsulada em gift wraps [NIP-59](/pt/topics/nip-59/) para eliminar vazamentos de metadados, um workflow WebRTC especificado para configuração de chamadas de voz e vídeo (offer, answer, ICE candidates), e um modelo mesh de chamadas em grupo em que cada peer estabelece uma conexão WebRTC direta com todos os demais peers. A spec não é backwards-compatible com o NIP-100. O Amethyst já está desenvolvendo contra ela, com uma suíte de testes para a máquina de estados de chamadas ([PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)) e tratamento de ofertas de chamada antigas ([PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)) entrando nesta semana.

- **[NIP-340](/en/topics/nip-340/) (FROST Quorum)** ([PR #2299](https://github.com/nostr-protocol/nips/pull/2299)): Propõe convenções para assinatura threshold [FROST](/pt/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) no Nostr. FROST permite que um grupo de signers controle coletivamente uma identidade Nostr em que qualquer conjunto t-of-n de membros pode assinar events sem reconstruir a chave privada completa. O NIP define como coordenar rodadas de assinatura, distribuir key shares e publicar events assinados por threshold, apoiando-se no trabalho do signer Igloo do [projeto FROSTR](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11).

- **[NIP-5D](/en/topics/nip-5d/) (Nostr Web Applets)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Define um protocolo `postMessage` para aplicações web sandboxed ("napplets") executadas em iframes se comunicarem com uma aplicação hospedeira ("shell"). O shell fornece ao napplet assinatura Nostr, acesso a relay e contexto do usuário por meio de uma API estruturada de mensagens, enquanto o sandbox do iframe impede acesso direto a chaves. Isso estende o modelo de hospedagem de sites estáticos de [NIP-5A](/en/topics/nip-5a/) em direção a aplicações interativas que podem ler e escrever events Nostr. O NIP está em desenvolvimento ativo com uma implementação runtime funcional.

- **[NIP-5C](/en/topics/nip-5c/) (Scrolls)** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Renomeado da proposta anterior NIP-A5. Define convenções para publicar e descobrir programas WebAssembly no Nostr. Binários WASM são armazenados como events Nostr, e clientes podem baixá-los e executá-los em um runtime sandboxed. Um [demo app](https://nprogram.netlify.app/) mostra scrolls executando no browser, com programas de exemplo publicados como events Nostr que qualquer cliente pode buscar e executar.

- **[NIP-85](/pt/topics/nip-85/) (Trusted Assertions): esclarecimentos** ([PR #2304](https://github.com/nostr-protocol/nips/pull/2304)): Torna mais precisa a linguagem da spec sobre múltiplas chaves e relays por provedor de serviço, esclarecendo como clientes devem lidar com assertions de provedores que operam em várias pubkeys ou endpoints de relay.

- **[NIP-24](/pt/topics/nip-24/) (Extra Metadata Fields): `published_at` para events replaceable** ([PR #2300](https://github.com/nostr-protocol/nips/pull/2300)): Generaliza a tag `published_at` de [NIP-23](/en/topics/nip-23/) (Long-form Content) para todos os events replaceable e addressable. A tag é apenas de exibição: se `published_at` for igual a `created_at`, clientes mostram o event como "created" naquele momento; se forem diferentes (porque o event foi atualizado), clientes podem mostrar "updated" no lugar. Isso permite que perfis kind `0` exibam datas de "joined at" e que outros events replaceable preservem seu timestamp original de publicação ao longo de atualizações. Uma proposta complementar de [NIP-51](/pt/topics/nip-51/) ([PR #2302](https://github.com/nostr-protocol/nips/pull/2302)) adiciona a mesma tag a list events.

- **[NIP-59](/pt/topics/nip-59/) (Gift Wrap): kind efêmero de gift wrap** ([PR #2245](https://github.com/nostr-protocol/nips/pull/2245)): Adiciona kind `21059` como contraparte efêmera do gift wrap kind `1059` existente. Events efêmeros (kinds `20000`-`29999`) seguem a semântica de [NIP-01](/pt/topics/nip-01/): relays não são obrigados a armazená-los e podem descartá-los após a entrega. Isso permite que aplicações enviem mensagens em gift wrap que desaparecem dos relays depois de entregues, reduzindo exigências de armazenamento para mensagens de alto volume e mantendo o mesmo modelo de criptografia em três camadas das DMs regulares [NIP-17](/pt/topics/nip-17/).

### OpenSats anuncia a décima sexta rodada de grants para Nostr

[OpenSats](https://opensats.org) anunciou sua [décima sexta rodada de grants para Nostr](https://opensats.org/blog/sixteenth-wave-of-nostr-grants) em 8 de abril, financiando quatro grants inéditos e uma renovação. [Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp) recebe financiamento para que o contribuidor Robert Nagy construa um app desktop standalone sobre os módulos [Quartz](/pt/topics/quartz/) e Commons, levando o conjunto de recursos do cliente Android para interfaces orientadas a mouse com conexões persistentes a relay. [Nostr Mail](https://github.com/nogringo/nostr-mail) recebe financiamento para construir um sistema completo de email sobre Nostr usando events kind `1301` encapsulados em gift wraps [NIP-59](/pt/topics/nip-59/), com um cliente Flutter e servidores bridge SMTP para compatibilidade com Gmail/Outlook. [Nostrord](https://github.com/Nostrord/nostrord) recebe financiamento para um cliente de grupos baseado em relay [NIP-29](/en/topics/nip-29/) em Kotlin Multiplatform com mensagens em grupo ao estilo Discord, moderação e threads. [Nurunuru](https://github.com/tami1A84/null--nostr) recebe financiamento para construir uma versão nativa iOS do cliente Nostr japonês, modelado sobre a interface familiar do LINE, com login biométrico baseado em passkey para onboarding. HAMSTR recebeu renovação de grant (financiado pela primeira vez na [décima primeira rodada](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr)).

## NIP Deep Dive: NIP-17 (Private Direct Messages)

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md) define o padrão atual para mensagens diretas privadas no Nostr. Ele substitui o esquema mais antigo [NIP-04](/pt/topics/nip-04/) (Encrypted Direct Messages), que vazava metadados (remetente, destinatário e timestamps ficavam todos visíveis nos relays) e usava uma construção de criptografia mais fraca. O NIP-17 combina [NIP-44](/pt/topics/nip-44/) (Encrypted Payloads) para criptografia com [NIP-59](/pt/topics/nip-59/) (Gift Wrap) para proteção de metadados, criando um sistema em três camadas em que relays não conseguem ver quem está falando com quem.

O protocolo usa três kinds de event empilhados um dentro do outro. A camada mais interna é a mensagem em si, um event kind `14` sem assinatura:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

O event kind `14` é deliberadamente sem assinatura (`sig` vazio). A spec descreve isso como fornecendo negabilidade, mas na prática a proteção é limitada. O selo kind `13` que encapsula o rumor é assinado pela chave real do remetente. Um destinatário pode mostrar o selo assinado a um terceiro, provando que o remetente se comunicou com ele, mesmo sem revelar o conteúdo da mensagem. Com provas de conhecimento zero, um destinatário pode provar o conteúdo exato da mensagem sem revelar sua própria chave privada. O rumor sem assinatura é como uma carta não assinada dentro de um envelope assinado: a assinatura do envelope liga o remetente ao conteúdo. Negabilidade real exigiria autenticação simétrica (como os HMACs do Signal), o que é incompatível com o modelo descentralizado de relay do Nostr, no qual mensagens precisam ser autoautenticáveis. Os pontos fortes reais do NIP-17 são privacidade de metadados e sigilo de conteúdo, não negabilidade.

Essa mensagem sem assinatura é então encapsulada em um selo kind `13`, que é assinado pelo remetente real e criptografado com [NIP-44](/pt/topics/nip-44/) para o destinatário:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

O selo não tem tags, então mesmo que seja decriptado ele não revelaria o destinatário. O selo é assinado pela chave real do remetente, o que permite ao destinatário autenticar a mensagem verificando que a `pubkey` do selo corresponde à `pubkey` do kind `14` interno.

O selo então é encapsulado em um gift wrap kind `1059`, assinado por uma chave aleatória descartável e endereçado ao destinatário:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

A `pubkey` do gift wrap é uma chave aleatória gerada apenas para esta mensagem, e o `created_at` é randomizado em até dois dias no passado. Essa é a camada mais externa que os relays realmente veem: uma mensagem de uma pubkey desconhecida endereçada ao destinatário, com um timestamp que não reflete quando a mensagem foi de fato enviada. O timestamp randomizado protege contra análise posterior de events armazenados, mas um adversário conectado ativamente aos relays ainda pode observar quando o gift wrap apareceu pela primeira vez, então essa defesa é limitada a observadores passivos que consultam dados de relay mais tarde. Como a pubkey é aleatória e o timestamp é falso, os relays não conseguem determinar o remetente real. Para ler a mensagem, o destinatário decripta o gift wrap usando sua própria chave e a pubkey aleatória, encontra o selo dentro dele, decripta o selo usando sua própria chave e a pubkey do remetente obtida do selo, e encontra a mensagem kind `14` dentro.

O NIP-17 não fornece forward secrecy. Todas as mensagens são criptografadas usando o par de chaves estático do Nostr (via derivação de chave do NIP-44 a partir das chaves do remetente e do destinatário). Se uma chave privada for comprometida, toda mensagem passada e futura criptografada para essa chave poderá ser decriptada. Esse é um tradeoff deliberado: como a criptografia depende apenas do nsec, um usuário que faz backup do seu nsec pode recuperar todo o histórico de mensagens a partir de qualquer relay que ainda armazene os gift wraps. Protocolos como MLS (usado por [Marmot](/pt/topics/marmot/)) fornecem forward secrecy por meio de material de chave rotativo, mas ao custo de exigir sincronização de estado e tornar impossível a recuperação histórica de mensagens após a rotação de chave.

O NIP-17 também define kind `15` para mensagens com arquivos criptografados, adicionando tags `file-type`, `encryption-algorithm`, `decryption-key` e `decryption-nonce` para que o destinatário possa decriptar um arquivo anexado que foi criptografado com AES-GCM antes do upload para um servidor Blossom. O kind `10050` é usado para publicar a lista preferida de relays de DM do usuário, para que remetentes saibam onde entregar gift wraps. O conjunto de tags `pubkey` + `p` em uma mensagem define uma sala de chat; adicionar ou remover um participante cria uma nova sala com histórico limpo.

As implementações cobrem a maior parte dos clientes principais. [nospeak](https://github.com/psic4t/nospeak) usa NIP-17 para todas as mensagens um a um. [Flotilla](https://gitea.coracle.social/coracle/flotilla) usa NIP-17 para suas DMs com proof-of-work. [Amethyst](https://github.com/vitorpamplona/amethyst), [Primal](https://github.com/PrimalHQ/primal-android-app), [Nostur](https://github.com/nostur-com/nostur-ios-public), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel) e [Coracle](https://github.com/coracle-social/coracle) implementam NIP-17 como seu protocolo principal de DM. A spec também suporta mensagens que desaparecem ao definir uma tag `expiration` no gift wrap.

## NIP Deep Dive: NIP-46 (Nostr Remote Signing)

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) define um protocolo para separar a chave privada do usuário da aplicação cliente. Em vez de colar um nsec em um app web, o usuário roda um signer remoto (também chamado de "bunker") que mantém a chave privada e responde a requests de assinatura por relays Nostr. O cliente nunca vê a chave privada. Isso reduz a superfície de ataque: um cliente comprometido pode solicitar assinaturas, mas não consegue extrair a chave em si.

O protocolo usa kind `24133` tanto para requests quanto para responses, criptografados com [NIP-44](/pt/topics/nip-44/) (Encrypted Payloads). Um cliente gera um `client-keypair` descartável para a sessão e se comunica com o signer remoto por mensagens criptografadas em NIP-44 marcadas com as pubkeys um do outro. Aqui está um request de assinatura de um cliente para um signer remoto:

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

O `content` criptografado contém uma estrutura semelhante a JSON-RPC:

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

O signer remoto decripta o request, o apresenta ao usuário para aprovação (ou aprova automaticamente com base nas permissões configuradas), assina o event com a chave privada do usuário e devolve o event assinado em uma response:

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Conexões podem ser iniciadas de qualquer lado. Um signer remoto fornece uma URL `bunker://` contendo sua pubkey e informações de relay. Um cliente fornece uma URL `nostrconnect://` com sua pubkey de cliente, relays e um secret para verificação da conexão. O parâmetro `secret` impede connection spoofing: apenas a parte que recebeu a URL fora de banda pode completar o handshake.

Oito métodos são definidos: `connect` para estabelecer a sessão, `sign_event` para assinar events, `get_public_key` para obter a pubkey do usuário, `ping` para keepalive, `nip04_encrypt`/`nip04_decrypt` para criptografia legada, `nip44_encrypt`/`nip44_decrypt` para criptografia atual, e `switch_relays` para gerenciamento de relay. A migração de relay é tratada pelo signer remoto, que pode mover a conexão para novos relays ao longo do tempo sem quebrar a sessão.

Clientes solicitam capacidades específicas no momento da conexão por meio de um sistema de permissões. Uma string de permissão como `nip44_encrypt,sign_event:1,sign_event:14` solicita acesso à criptografia NIP-44 e acesso de assinatura apenas para events kind `1` e kind `14`. O signer remoto pode aceitar, rejeitar ou modificar essas permissões. Isso significa que um cliente web para ler e publicar notas talvez receba apenas permissão `sign_event:1`, enquanto um cliente de DM pode também receber permissões `sign_event:14` e `nip44_encrypt`.

[Amber](https://github.com/greenart7c3/Amber) implementa NIP-46 no Android, e sua [v6.0.0-pre1](#amber-v600-pre1-adiciona-chaves-de-assinatura-nip-46-por-conexao) nesta semana adiciona chaves de assinatura por conexão para isolamento entre clientes. [nsec.app](https://github.com/nicktee/nsecapp) (antigo Nostr Connect) fornece um bunker baseado na web. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) inclui `BunkerSigner` para clientes JavaScript, e [o PR #530 da semana passada](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing) adicionou `skipSwitchRelays` para gerenciamento manual de relay. O protocolo também suporta auth challenges: quando um signer remoto precisa de autenticação adicional (senha, biometria ou token de hardware), ele responde com uma `auth_url` que o cliente abre no browser para que o usuário conclua o processo.

---

Isso é tudo por esta semana. Está construindo algo ou tem novidades para compartilhar? Envie uma DM para nós no Nostr ou nos encontre em [nostrcompass.org](https://nostrcompass.org).
