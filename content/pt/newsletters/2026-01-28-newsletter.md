---
title: 'Nostr Compass #7'
date: 2026-01-28
translationOf: /en/newsletters/2026-01-28-newsletter.md
translationDate: 2026-01-28
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** Ridestr traz compartilhamento de caronas descentralizado para o Nostr com pagamentos [Cashu](/pt/topics/cashu/) e compartilhamento de localização criptografado. Pomade introduz recuperação baseada em e-mail para signatários multisig. Damus lança [negentropy](/pt/topics/negentropy/) para sincronização confiável de DMs. O aplicativo desktop do Amethyst adiciona busca, favoritos e zaps. Amber v4.1.1 exibe pontuações de confiança de relays. Marmot faz merge do MIP-03 e constrói um aplicativo de chat de referência em TypeScript. diVine adiciona autenticação por QR via [NIP-46](/pt/topics/nip-46/) e suporte a menções. Novas propostas de NIP abordam gerenciamento de comunidades, sincronização baseada em sequência e armazenamento de arquivos criptografados. Também olhamos para cinco anos de janeiros do Nostr, traçando a evolução do protocolo desde um punhado de adotantes iniciais em 2021 até o lançamento explosivo do Damus na App Store em 2023 e o ecossistema de clientes amadurecido de 2025.

## Notícias

### Ridestr Traz Compartilhamento de Caronas Descentralizado para o Nostr

[Ridestr](https://github.com/variablefate/ridestr) está desenvolvendo um aplicativo de compartilhamento de caronas peer-to-peer construído inteiramente no Nostr, permitindo transações diretas entre motoristas e passageiros com pagamentos em Bitcoin e [Cashu](/pt/topics/cashu/). O protocolo usa kinds de evento personalizados (30173, 3173-3175, 30180/30181) para coordenar corridas enquanto mantém a privacidade através de divulgação progressiva de localização e criptografia [NIP-44](/pt/topics/nip-44/).

O sistema funciona através de um fluxo cuidadosamente coreografado: motoristas transmitem disponibilidade usando localizações codificadas em geohash (~5km de precisão) via eventos kind 30173, passageiros solicitam corridas com estimativas de tarifa através de kind 3173, e pagamentos são garantidos usando tokens de escrow HTLC antes do início da corrida. A privacidade da localização é preservada através de divulgação progressiva, onde detalhes de embarque só são revelados quando os motoristas chegam e destinos são compartilhados após verificação de PIN. Toda comunicação entre as partes usa criptografia [NIP-44](/pt/topics/nip-44/) para privacidade.

Ridestr implementa segurança de pagamento através de escrow HTLC com assinaturas P2PK. Quando um passageiro aceita a oferta de um motorista, ele bloqueia tokens [Cashu](/pt/topics/cashu/) com um hash de pagamento que apenas o motorista pode reivindicar após a conclusão da corrida. O protocolo atualmente opera com arquitetura de mint único, exigindo que passageiros e motoristas usem o mesmo mint [Cashu](/pt/topics/cashu/). A implementação Android baseada em Kotlin do projeto lida com verificação de provas e recuperação de provas obsoletas através de verificações de estado NUT-07.

Ridestr enfrenta desafios que a maioria dos aplicativos Nostr evita: coordenação de localização em tempo real, escrow de pagamento com resolução de disputas e sistemas de reputação para interações no mundo físico. O projeto está em beta e demonstra que o modelo de eventos do Nostr pode suportar marketplaces de serviços peer-to-peer, não apenas compartilhamento de conteúdo.

### Pomade Lança Sistema de Recuperação Alpha para Signatários Multisig

[Pomade](https://github.com/coracle-social/pomade), desenvolvido por hodlbod, se baseia no ecossistema [FROSTR](https://github.com/FROSTR-ORG) existente para fornecer um serviço de assinatura de limiar focado em recuperação. Usando assinaturas [FROST](/pt/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) através da biblioteca @frostr/bifrost, Pomade adiciona fluxos de recuperação baseados em e-mail em cima da criptografia de limiar. O sistema fragmenta a chave secreta do usuário usando Shamir Secret Sharing, distribuindo fragmentos entre múltiplos signatários independentes com um limiar configurável (2-de-3, 3-de-5, etc.).

O protocolo opera inteiramente sobre o Nostr usando um único kind de evento (28350) com payloads criptografados [NIP-44](/pt/topics/nip-44/). Ao assinar, o cliente solicita assinaturas parciais de pelo menos `threshold` signatários, então agrega essas em uma assinatura Schnorr válida. Para criptografia, signatários colaboram para derivar segredos compartilhados via ECDH sem que nenhuma parte aprenda a chave completa.

A recuperação funciona através de dois métodos de autenticação: baseado em senha (usando argon2id com a pubkey do signatário como salt) ou OTP por e-mail. Para prevenir ataques MITM durante recuperação por OTP, cada signatário gera seu próprio código de verificação com um prefixo fornecido pelo cliente, exigindo que usuários se autentiquem independentemente com cada signatário. O protocolo requer prova de trabalho em eventos de registro (20+ bits por [NIP-13](/pt/topics/nip-13/)) para prevenir spam.

O modelo de confiança é explícito: se `threshold` signatários conspirarem, eles podem roubar a chave. Provedores de e-mail são totalmente confiáveis já que podem interceptar OTPs. Usuários não podem recuperar independentemente sua chave secreta completa; fazer isso requer cooperação de `threshold` signatários. O protocolo é projetado para integrar novos usuários não familiarizados com gerenciamento de chaves, com a recomendação explícita de que usuários migrem para auto-custódia uma vez confortáveis. Pomade alerta sobre potencial "perda de chave, roubo, negação de serviço ou vazamento de metadados" dado seu status alpha não auditado.

## Lançamentos

### Damus Lança Negentropy para Sincronização Confiável de DMs

[Damus v1.13](https://github.com/damus-io/damus/tree/v1.13) lança a implementação de negentropy [que previsualizamos como PR aberto na semana passada](/pt/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs). [PR #3536](https://github.com/damus-io/damus/pull/3536) adiciona suporte base de [negentropy](/pt/topics/negentropy/) à camada de rede, habilitando reconciliação de conjuntos com relays que suportam o protocolo. Um [PR #3547](https://github.com/damus-io/damus/pull/3547) complementar adiciona sincronização de DM por pull-to-refresh que usa negentropy para recuperar mensagens perdidas quando assinaturas REQ padrão falham.

A implementação segue uma abordagem conservadora: o carregamento normal de DM continua inalterado, com [negentropy](/pt/topics/negentropy/) disponível como mecanismo de recuperação quando usuários atualizam manualmente. Testes automatizados demonstram a correção gerando uma DM com timestamp antigo que consultas padrão perderiam, então usando sincronização [negentropy](/pt/topics/negentropy/) para recuperá-la com sucesso. Embora o suporte a [negentropy](/pt/topics/negentropy/) requeira relays compatíveis, a implementação lida graciosamente com ambientes de relay mistos usando o protocolo onde disponível.

### Amber v4.1.1 - Pontuações de Confiança de Relay

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1) lança exibição de pontuação de confiança de relay ([PR #289](https://github.com/greenart7c3/Amber/pull/289)), implementando os conceitos de avaliação de relay discutidos na [cobertura de Trusted Relay Assertions da semana passada](/pt/newsletters/2026-01-21-newsletter/#nip-updates). Pontuações de confiança agora aparecem na página de Relays e para solicitações de conexão NostrConnect, ajudando usuários a avaliar a confiabilidade do relay antes de autorizar conexões. O lançamento também inclui uma UI redesenhada de login/eventos/permissões e suporte para o método `switch_relays`. Melhorias de desempenho fazem cache de operações de keystore, abordando relatos de tempos de carregamento de 20+ segundos em dispositivos mais antigos.

### nak v0.18.2 - Integração MCP

[nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) de fiatjaf [v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2) adiciona suporte ao [Model Context Protocol](https://nostrify.dev/mcp) via `nak mcp`, permitindo que agentes de IA busquem pessoas no Nostr, publiquem notas, mencionem usuários e leiam conteúdo usando o modelo outbox. O lançamento também introduz um [instalador de uma linha](https://github.com/fiatjaf/nak/blob/master/install.sh) (`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`) que baixa binários pré-compilados, eliminando o requisito de toolchain Go para usuários finais. O modo Bunker agora suporta Unix sockets e `switch_relays`.

### Zeus v0.12.2 Beta - Correções NWC

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases) lança múltiplas correções NWC abordando problemas cobertos na [cobertura do Zeus da semana passada](/pt/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect).

## Atualizações de Projetos

### Amethyst Desktop - Fase 2A Lançada

[Amethyst](https://github.com/vitorpamplona/amethyst) lançou a [Fase 2A de seu aplicativo desktop](https://github.com/vitorpamplona/amethyst/pull/1676), adicionando Busca, Favoritos, Zaps, visualizações de Thread e conteúdo de formato longo (Reads) à experiência desktop. Um [PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683) complementar adiciona feedback transparente de transmissão de eventos para que usuários agora vejam status em tempo real por relay enquanto seus eventos se propagam pela rede, facilitando o diagnóstico de problemas de conectividade.

### Progresso do Notedeck: Aplicativo de Calendário e Polimento de UX

O cliente desktop [Notedeck](https://github.com/damus-io/notedeck) da equipe Damus fez merge do comportamento de auto-ocultar barra de ferramentas ([PR #1268](https://github.com/damus-io/notedeck/pull/1268)) que responde à velocidade de rolagem para mais espaço de tela em visualizações móveis. Um [draft PR #1271](https://github.com/damus-io/notedeck/pull/1271) adiciona um aplicativo de Calendário [NIP-52](/pt/topics/nip-52/) completo com visualizações de mês/semana/dia/agenda, suporte a RSVP e comentários [NIP-22](/pt/topics/nip-22/) em eventos de calendário, atualmente com feature flag para testes.

### Jumble Adiciona Modo Comunidade

[Jumble](https://github.com/CodyTseng/jumble), o cliente web focado em relay, adicionou [modo comunidade](https://github.com/CodyTseng/jumble/pull/738) e suporte para [presets de conjunto de relays via variáveis de ambiente](https://github.com/CodyTseng/jumble/pull/736), facilitando o deploy de instâncias temáticas como [nostr.moe](https://nostr.moe/).

### Dashboard de Pedidos do Shopstr

[Shopstr](https://github.com/shopstr-eng/shopstr) substituiu seu gerenciamento de pedidos baseado em chat por um [Dashboard de Pedidos](https://github.com/shopstr-eng/shopstr/pull/219) dedicado. A nova interface fornece uma visualização centralizada para comerciantes rastrearem status de pedidos, marcarem mensagens como lidas e gerenciarem fulfillment sem rolar através de threads de chat. A atualização descontinua cache IndexedDB em favor de APIs de status de pedido server-side e revisa como DMs de pedido são tagueadas para melhor filtragem.

### Formstr Adiciona Perguntas de Grade

[Formstr](https://github.com/abh3po/nostr-forms), o aplicativo de formulários nativo do Nostr, adicionou [perguntas de grade](https://github.com/abh3po/nostr-forms/pull/419) e [reescreveu seu SDK](https://github.com/abh3po/nostr-forms/pull/410) com suporte a embed. Uma [correção para signatários não-[NIP-07](/pt/topics/nip-07/)](https://github.com/abh3po/nostr-forms/pull/418) resolveu problemas para usuários com bunker ou signatários locais tentando enviar formulários com sua identidade.

### nostr-tools Atualiza Dependências de Criptografia

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), a biblioteca JavaScript principal, [atualizou para @noble/curves v2.0.1](https://github.com/nbd-wtf/nostr-tools/pull/520), abordando mudanças de API quebradas em 27 arquivos e adotando as últimas bibliotecas noble auditadas. fiatjaf também adicionou suporte `switch_relays` ao [NIP-46](/pt/topics/nip-46/), permitindo que clientes bunker mudem dinamicamente conexões de relay.

### Zeus Trabalhando em Reviews de Mint NIP-87

[Zeus](https://github.com/ZeusLN/zeus) tem um [PR aberto para reviews de mint [NIP-87](/pt/topics/nip-87/)](https://github.com/ZeusLN/zeus/pull/3576), permitindo que usuários descubram e avaliem mints [Cashu](/pt/topics/cashu/) filtrados por follows do Nostr. Reviews incluem classificações por estrelas e podem ser enviadas anonimamente ou com a nsec do usuário.

### Camelus Lança Suporte Completo a DM

[Camelus](https://github.com/camelus-hq/camelus), um cliente Android baseado em Flutter construído com Dart NDK para desempenho móvel eficiente em bateria, adicionou mensagens diretas abrangentes com 20+ commits esta semana. A atualização inclui categorias de chat, datas de mensagens, UI de envio otimista, funcionalidade de nota para si mesmo e tratamento adequado de relay de DM.

### Atualizações do Protocolo Marmot

A resolução determinística de commit MIP-03 [que cobrimos como PR aberto na semana passada](/pt/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library) agora foi mergeada. [MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152) garante que todos os chats de grupo baseados em [MLS](/pt/topics/mls/) convirjam para o mesmo estado quando múltiplos commits válidos chegam para a mesma epoch.

Um [spec PR #28](https://github.com/marmot-protocol/marmot/pull/28) complementar adiciona requisitos de ciclo de vida de init_key abordando lacunas de auditorias de implementação: material de chave privada de mensagens Welcome deve ser excluído com segurança após processamento (zeroização, limpeza de armazenamento), e novos membros devem realizar auto-atualizações dentro de 24 horas para forward secrecy.

O SDK TypeScript ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) está construindo um aplicativo de chat de referência. [PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37) adiciona criação/listagem de grupos, gerenciamento de key package com fluxos de publicar/transmitir/excluir e convites por QR code. Um [PR aberto #38](https://github.com/marmot-protocol/marmot-ts/pull/38) por hzrd149 implementa persistência de histórico de mensagens com paginação. O backend whitenoise-rs fez merge de 15 PRs esta semana incluindo suporte multi-idioma ([PR #455](https://github.com/marmot-protocol/whitenoise-rs/pull/455)) e referências de mídia MIP-04 v2 ([PR #450](https://github.com/marmot-protocol/whitenoise-rs/pull/450)).

### diVine Adiciona Recursos de Integração Nostr

[diVine](https://github.com/divinevideo/divine-mobile), o aplicativo de vídeos curtos, continua rápida integração com Nostr.

PRs abertos incluem autenticação por QR code [NIP-46](/pt/topics/nip-46/) ([PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019)) e mensagens diretas criptografadas [NIP-17](/pt/topics/nip-17/) ([PR #834](https://github.com/divinevideo/divine-mobile/pull/834)). A atividade desta semana focou em [suporte a menções](https://github.com/divinevideo/divine-mobile/pull/1098) convertendo URIs `nostr:` e @menções em links de perfil clicáveis, [fallbacks de avatar Classic Viners](https://github.com/divinevideo/divine-mobile/pull/1097) usando perfis Nostr, e ferramentas de edição de vídeo incluindo [desenho](https://github.com/divinevideo/divine-mobile/pull/1056), [filtros](https://github.com/divinevideo/divine-mobile/pull/1053) e [stickers](https://github.com/divinevideo/divine-mobile/pull/1050).

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mesclados:**

- **[Trusted Relay Assertions](https://github.com/nostr-protocol/nips/pull/1534)** - A proposta para padronizar pontuação de confiança de relay [que cobrimos na semana passada](/pt/newsletters/2026-01-21-newsletter/#nip-updates) foi mesclada. A especificação define eventos kind 30385 para asserções de confiança de relay com pontuação em confiabilidade, qualidade e acessibilidade. O debate que levou à mesclagem centrou-se em se pontuações de confiança devem ser "globais" (computadas uma vez para todos os usuários) ou "personalizadas" (relativas ao grafo social de cada observador). Algoritmos estilo PageRank como o [Trust Rank do nostr.band](https://trust.nostr.band/) e [GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs) resistem a ataques sybil dividindo qualquer rank passado através de contas falsas pelo tamanho da fazenda de bots.

**PRs Abertos e Discussões:**

- **Communikeys** - Uma [proposta abrangente](https://nostrhub.io) para gerenciamento de comunidades que usa npubs existentes como identificadores de comunidade em vez de abordagens baseadas em relay. Qualquer npub pode se tornar uma comunidade publicando um evento kind 10222; publicações visam comunidades via eventos kind 30222. Controle de acesso usa badges [NIP-58](/pt/topics/nip-58/), permitindo gerenciamento de membros delegado com armazenamento cold para chaves de comunidade.

- **[NIP-CF: Changes Feed](https://github.com/nostr-protocol/nips/pull/2196)** - Um rascunho propondo sincronização de eventos baseada em sequência como alternativa a filtros `since` baseados em timestamp. O problema: sincronização Nostr padrão usando timestamps `since` pode perder eventos quando múltiplos eventos compartilham o mesmo timestamp de precisão de segundo, relógios de cliente e relay divergem, ou checkpointing é impreciso. NIP-CF resolve isso fazendo relays atribuírem números de sequência monotonicamente crescentes a eventos armazenados, fornecendo ordenação total estrita. Clientes solicitam mudanças desde um número de sequência específico e recebem eventos em ordem garantida, com checkpointing preciso que nunca perde eventos. A proposta também suporta modo ao vivo/contínuo onde assinaturas permanecem abertas após sincronização inicial para atualizações em tempo real.

- **[NIP-XX: Encrypted File Sync](https://github.com/nostr-protocol/nips/pull/1947)** - Um protocolo definindo kinds 30800 (arquivos criptografados), 30801 (índices de vault) e 30802 (documentos compartilhados) para sincronizar conteúdo criptografado entre dispositivos usando relays Nostr. O protocolo permite que aplicativos de anotações local-first forneçam sincronização criptografada de ponta a ponta sem servidores centralizados. Conteúdos de arquivo, caminhos, nomes e estrutura de pastas são todos criptografados usando auto-criptografia [NIP-44](/pt/topics/nip-44/), então relays armazenam blobs que não podem ler. Anexos binários como imagens usam servidores [Blossom](/pt/topics/blossom/) com criptografia client-side. Kind 30802 permite compartilhamento de documentos entre usuários criptografando para a chave pública do destinatário.

## Cinco Anos de Janeiros do Nostr

[O newsletter do mês passado](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers) traçou os marcos de dezembro do Nostr desde o primeiro lançamento de cliente de fiatjaf até a doação catalítica de Jack Dorsey. Esta retrospectiva mapeia o que aconteceu em cada janeiro de 2021 até 2025, focando em desenvolvimentos técnicos verificados.

### Janeiro de 2021: Desenvolvimento Inicial

O terceiro mês do Nostr viu desenvolvimento contínuo no Branle, o cliente Vue.js de fiatjaf que havia lançado em dezembro de 2020. Um pequeno grupo de adotantes iniciais, provavelmente menos de 15 pessoas, se coordenava através do grupo Telegram [@nostr_protocol](https://t.me/nostr_protocol) (criado em 16 de novembro de 2020), testando o protocolo em um ou dois relays experimentais. O cliente de linha de comando noscl fornecia interação baseada em terminal.

A fundação técnica já estava definida: usuários identificados por chaves públicas secp256k1, posts assinados criptograficamente com assinaturas Schnorr, e relays servindo como armazenamento burro que não se comunicam entre si. Isso era deliberadamente criptografia nativa do Bitcoin, uma escolha de design que moldaria padrões de adoção anos depois.

### Janeiro de 2022: Descoberta por Desenvolvedores

Janeiro de 2022 abriu com o Nostr ainda agitado por sua [primeira aparição no Hacker News](https://news.ycombinator.com/item?id=29749061) (31 de dezembro de 2021), que gerou 110 pontos e 138 comentários. Na época daquele post, apenas cerca de sete relays alimentavam toda a rede, com comentaristas notando que "spam ainda não é um problema porque nostr é super novo e ninguém usa ainda." Robert C. Martin ("Uncle Bob") havia endossado o Nostr como potencialmente "a solução final para comunicação social." A discussão continuou em janeiro, com desenvolvedores debatendo arquitetura de relay versus P2P verdadeiro, resistência à censura versus moderação, e se a simplicidade poderia escalar.

O post do HN provocou uma onda de novas implementações. O próprio Uncle Bob começou [more-speech](https://github.com/unclebob/more-speech), um cliente desktop Clojure, em 18 de janeiro. A biblioteca [go-nostr](https://github.com/nbd-wtf/go-nostr) de fiatjaf (criada em janeiro de 2021) e o cliente de linha de comando [noscl](https://github.com/fiatjaf/noscl) forneciam ferramentas Go, enquanto [nostr-tools](https://github.com/nbd-wtf/nostr-tools) oferecia suporte JavaScript. Até dezembro de 2022, aproximadamente 800 perfis tinham bios. Branle permaneceu o cliente web principal, recebendo atualizações incluindo importação de chave privada e suporte multi-relay. Desafios técnicos eram evidentes: chaves hex de 64 caracteres se mostraram pouco intuitivas, atrasos de mensagens frustravam usuários, e a comunidade questionava se a arquitetura poderia lidar com tráfego em escala Twitter.

### Janeiro de 2023: A Explosão

Janeiro de 2023 transformou o Nostr de experimento em movimento. Damus, o cliente iOS de William Casarin (jb55), lutou contra o processo de aprovação da App Store da Apple. Rejeitado em 1º de janeiro, rejeitado novamente em 26 de janeiro, foi finalmente [aprovado em 31 de janeiro](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store). Essa aprovação desencadeou uma cascata: Damus imediatamente alcançou o #10 em Redes Sociais nos EUA. Jack Dorsey [chamou isso de](https://web.archive.org/web/20240304043638/https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store) "um marco para protocolos abertos."

Oito dias antes, em 23 de janeiro, [Edward Snowden anunciou](https://x.com/Snowden/status/1617623779626352640) sua presença no Nostr: "Uma das coisas legais sobre o Nostr... além da resistência à censura, é que você não está limitado a 280 caracteres." Seu endosso de um denunciante da NSA carregava peso em círculos conscientes de privacidade, e usuários imediatamente começaram a enviar zaps de sats via Lightning.

Clientes web correram para integrar o influxo. [Snort](https://github.com/v0l/snort), criado por kieran em dezembro de 2022, emergiu como um cliente React cheio de recursos; em 13 de janeiro, Snort integrou registro NIP-05 via API Nostr Plebs, permitindo que novos usuários reivindicassem identidades legíveis por humanos durante o onboarding. [Iris](https://iris.to), desenvolvido em tempo integral por Martti Malmi (um contribuidor inicial do Bitcoin que recebeu a segunda transação de Bitcoin de Satoshi), oferecia interfaces web e móvel com identidades NIP-05 gratuitas em iris.to. [Astral](https://github.com/monlovesmango/astral), construído por monlovesmango com Quasar (Vue.js) como fork do Branle, focava em gerenciamento de relay com seu recurso de agrupamento de relay que permitia usuários organizarem relays em conjuntos para postar e filtrar. Betas TestFlight para clientes iOS lotavam em horas, e Amethyst dominava o Android.

A infraestrutura lutou para acompanhar. Todos os relays eram operados por entusiastas pagando do próprio bolso. Relays pagos usando micropagamentos Lightning criavam filtragem natural de spam mas introduziam fricção de acesso. [Damus foi removido da App Store da China](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) apenas dois dias após aprovação, supostamente a pedido do principal órgão de vigilância da internet da China.

### Janeiro de 2024: Endurecimento do Protocolo

Janeiro de 2024 focou em padronização de protocolo e construção de comunidade. [Nostr PHX](https://www.nostrphx.com/events) começou o ano com um encontro em 5 de janeiro em Phoenix, reunindo cypherpunks locais. Este foi o primeiro de muitos eventos comunitários naquele ano incluindo BTC Prague (junho), Nostriga em Riga (agosto) e Nostrasia.

O desenvolvimento de protocolo mais significativo foi [NIP-59 (Gift Wrap)](https://github.com/nostr-protocol/nips/pull/716) sendo mergeado em 29 de janeiro, fornecendo proteção de metadados para comunicações criptografadas. Gift Wrap se baseia no [padrão de criptografia NIP-44](https://github.com/paulmillr/nip44) (que havia sido [auditado pela Cure53](https://cure53.de/audit-report_nip44-implementations.pdf) em dezembro de 2023) para esconder a identidade do remetente dos relays. O protocolo envolve mensagens criptografadas dentro de um evento externo assinado por um par de chaves aleatório de uso único. Relays veem apenas a pubkey descartável, enquanto a identidade real do remetente está enterrada no payload criptografado que apenas o destinatário pode descriptografar. Isso impede que operadores de relay e observadores de rede saibam quem está enviando mensagens para quem. Timestamps também podem ser randomizados para derrotar análise de timing.

O ecossistema expandiu além de mídia social. [Plebeian Market](https://plebeian.market) tornou-se totalmente nativo do Nostr com conformidade [NIP-15](/pt/topics/nip-15/), permitindo carrinhos de compras cross-stall e um navegador de stalls para descobrir comerciantes. [Shopstr](https://github.com/shopstr-eng/shopstr) emergiu como um marketplace sem permissão facilitando comércio Bitcoin. [Zap.stream](https://zap.stream/), construído por kieran, trouxe streaming ao vivo para o Nostr com pagamentos Lightning a 21 sats/minuto. Ferramentas de desenvolvimento amadureceram com [NDK](https://github.com/nostr-dev-kit/ndk) fornecendo abstrações TypeScript e [rust-nostr](https://github.com/rust-nostr/nostr) oferecendo bindings Rust. [Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/) lançou com importação de contatos Nostr e LND persistente, preparando o terreno para integração Nostr Wallet Connect em lançamentos posteriores.

No entanto, a sustentabilidade da infraestrutura [permanecia desafiadora](https://arxiv.org/abs/2402.05709). Pesquisa acadêmica deste período encontrou que 95% dos relays lutavam para cobrir custos operacionais, com 20% experimentando downtime significativo. A taxa de admissão para relays pagos era em média menos de 1.000 sats (~$0,45), insuficiente para sustentar operações.

*Uma nota sobre golpes: O "Nostr Assets Protocol" e o token "$NOSTR" associado que lançaram por volta desta época [foram publicamente denunciados por fiatjaf](https://www.aicoin.com/en/article/377704) como "100% fraudulentos" e "um golpe de afinidade" sem conexão com o protocolo Nostr real.*

### Janeiro de 2025: Maturação de Clientes

Janeiro de 2025 viu desenvolvimento contínuo de clientes em todo o ecossistema. [Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/) lançou em 13 de janeiro com sincronização cross-device para estados de leitura, suporte a login multi-sig [FROST](/pt/topics/frost/), e desempenho otimizado de banco de dados local. Amethyst continuou sua transição para o modelo outbox, compilando automaticamente conjuntos de relay baseados em listas de follows em vez de exigir configuração manual.

Principais clientes começaram a se afastar do [NIP-04](/pt/topics/nip-04/) para mensagens diretas, migrando para [NIP-17](/pt/topics/nip-17/) e o proposto [NIP-104](/pt/topics/nip-104/) para criptografia aprimorada e proteção de metadados. O modelo Gossip (comunicação outbox/inbox) ganhou adoção conforme o ecossistema convergiu para padrões de uso de relay mais eficientes. Observadores da indústria previram que este seria o ano em que o Nostr transicionaria de protocolo de nicho para reconhecimento mainstream, com uma potencial migração de plataforma de alto perfil que poderia dobrar a atividade diária.

### Janeiro de 2026: Segurança e Infraestrutura de Assinatura

Janeiro de 2026 trouxe avanços significativos em segurança e infraestrutura de assinatura. [Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) lançou assinatura remota [NIP-46](/pt/topics/nip-46/) e suporte a signatário local [NIP-55](/pt/topics/nip-55/), juntando-se a Amber e Aegis como um hub de assinatura completo para outros aplicativos Android. [Bitchat completou uma auditoria de segurança da Cure53](https://github.com/permissionlesstech/bitchat/pulls), a mesma firma que auditou Signal e NIP-44, com 17+ PRs corrigindo descobertas críticas incluindo limpeza de segredo DH e problemas de thread safety. Tanto Bitchat quanto Damus migraram de C Tor para Rust Arti para confiabilidade e segurança de memória aprimoradas.

O trabalho de protocolo continuou com [NIP-71](https://github.com/nostr-protocol/nips/pull/1669) (eventos de vídeo endereçáveis) sendo mergeado e um NIP de criptografia pós-quântica abrindo discussão sobre proteger o Nostr contra ataques quânticos. O rascunho Trusted Relay Assertions propôs padronizar pontuação de confiança de relay através de atestações assinadas. O [Protocolo Marmot](https://github.com/marmot-protocol/mdk) endureceu suas mensagens criptografadas baseadas em [MLS](/pt/topics/mls/) com 18 PRs mergeados abordando descobertas de auditoria.

Aplicações do mundo real expandiram com [Ridestr](https://github.com/variablefate/ridestr) desenvolvendo compartilhamento de caronas descentralizado usando escrow [Cashu](/pt/topics/cashu/) e criptografia [NIP-44](/pt/topics/nip-44/), e [Pomade](https://github.com/coracle-social/pomade) adicionando fluxos de recuperação baseados em e-mail à assinatura de limiar [FROST](/pt/topics/frost/). Damus lançou [negentropy](/pt/topics/negentropy/) para sincronização confiável de DM, enquanto o aplicativo desktop do Amethyst alcançou a Fase 2A com busca, favoritos e zaps.

### Olhando Adiante

Seis anos de janeiros revelam a evolução do Nostr desde desenvolvimento inicial (2021) até descoberta pública (2022) até crescimento explosivo (2023) até endurecimento de protocolo (2024) até maturação de clientes (2025) até infraestrutura de segurança (2026). O padrão é familiar para qualquer um que assistiu protocolos abertos crescerem: anos de construção silenciosa, uma explosão repentina quando as condições se alinham, então o trabalho mais longo de tornar tudo confiável. O que começou com sete relays e um thread no Hacker News agora é infraestrutura auditada com aplicações reais. A questão para 2027: quando alguém chamar uma carona, enviar uma mensagem criptografada, ou recuperar uma chave perdida usando Nostr, eles sequer saberão que estão usando?

---

É isso para esta semana. Construindo algo? Tem notícias para compartilhar? Quer que cubramos seu projeto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via DM NIP-17</a> ou nos encontre no Nostr.
