---
title: 'Nostr Compass #19'
date: 2026-04-22
translationOf: /en/newsletters/2026-04-22-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) faz uma grande rodada de trabalho em Marmot, comunidades e salas de áudio com MoQ; [TollGate](https://github.com/OpenTollGate/tollgate) estabiliza acesso à internet pay-per-use sobre Nostr e Cashu na v0.1.0; e [nostream](https://github.com/Cameri/nostream) fecha uma semana intensa de trabalho em relay em torno de [NIP-45](/pt/topics/nip-45/), [NIP-62](/pt/topics/nip-62/), compressão, hardening de consultas e paridade completa com [NIP-11](/pt/topics/nip-11/). Forgesworn publica uma stack completa de assinatura, identidade e APIs pagas para Nostr. ShockWallet continua avançando em fluxos de carteira Lightning nativos de Nostr. A suíte Formstr, Pollerama, Forms e Calendar, mergeia 26 PRs em hardening de segurança, i18n e suporte a RRULE. StableKraft, Keep, topaz, WoT Relay, Flotilla e NipLock completam a lista de lançamentos. Os deep dives cobrem [NIP-72](/pt/topics/nip-72/) e [NIP-57](/pt/topics/nip-57/).

## Top Stories

### Amethyst lança conformidade MIP do Marmot, comunidades NIP-72, metas de zap e salas de áudio com MoQ

[Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android mantido por vitorpamplona, mergeou 57 PRs nesta semana. Os temas centrais são conformidade de grupos criptografados com [Marmot](/pt/topics/marmot/), comunidades moderadas de primeira classe, metas de zap em live streams e uma nova stack de salas de áudio construída sobre Media over QUIC.

No trabalho de conformidade com Marmot, o [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) alinha a implementação embarcada de [MDK](https://github.com/marmot-protocol/mdk) com os formatos wire de MIP-01 e MIP-05, adicionando codificação VarInt de prefixos de comprimento estilo TLS e validação round-trip contra vetores de teste do MDK. O [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) adiciona suporte a MIP-00 KeyPackage Relay List, e o [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) fecha lacunas restantes de admin gate e tratamento de mídia identificadas por testes cross-client com [White Noise](https://github.com/marmot-protocol/whitenoise). Duas correções de corretude chegaram no mesmo dia: o [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) corrige o framing de commits MLS para que welcomes criptografados serializem os mesmos bytes produzidos por mdk-core, e o [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) resolve um bug de descriptografia da camada externa que causava divergência de estado entre co-admins do Marmot. Uma segunda rodada de conformidade, nos [PR #2477](https://github.com/vitorpamplona/amethyst/pull/2477) e [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493), fecha lacunas adicionais em commits e criptografia de mensagens e adiciona um validador completo da criptografia de commits MLS contra vetores de referência.

Ao lado do trabalho de protocolo, o [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) lança `amy`, uma ferramenta de linha de comando para operações de grupo em Marmot e MLS dirigida pela implementação do próprio Amethyst. Amy dá a integradores um caminho scriptável para criar grupos, gerar KeyPackages, simular welcomes e validar commits contra um signer real do Amethyst, fechando hoje a maior lacuna de debugging para interop cross-client de Marmot.

O [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) adiciona criação e gerenciamento de comunidades [NIP-72](/pt/topics/nip-72/) como recursos de primeira classe. Usuários podem criar a definição de comunidade kind `34550`, adicionar moderadores e relay hints, enviar posts com uma tag `a` apontando para a comunidade e gerenciar aprovações pendentes por meio de eventos kind `4549`. O recurso fecha uma lacuna antiga entre Amethyst e [noStrudel](https://github.com/hzrd149/nostrudel) no campo de moderação de comunidades. Os [PR #2458](https://github.com/vitorpamplona/amethyst/pull/2458) e [PR #2473](https://github.com/vitorpamplona/amethyst/pull/2473) adicionam suporte a emoji sets e uma UI completa para gerenciamento de emoji packs da [NIP-30](https://github.com/nostr-protocol/nips/blob/master/30.md).

O [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) conecta metas de zap [NIP-75](/pt/topics/nip-75/) à tela Live Activities da [NIP-53](/pt/topics/nip-53/). Cada live stream agora carrega um cabeçalho de meta de arrecadação com barra de progresso, botão de zap com um toque e ranking dos principais zappers. O ranking lê recibos de zap kind `9735` vinculados ao evento kind `30311` da stream e os soma em relação ao alvo `amount` da meta. O [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) completa a superfície de live streams com uma tela dedicada de feed, o [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) adiciona proof of agreement e helpers de event builder para NIP-53, e o [PR #2461](https://github.com/vitorpamplona/amethyst/pull/2461) adiciona HLS na menor resolução no feed, picture-in-picture e seleção automática de resolução em tela cheia.

A superfície nova mais ambiciosa é o áudio em tempo real. O [PR #2494](https://github.com/vitorpamplona/amethyst/pull/2494) adiciona um cliente de transporte [Media over QUIC](https://datatracker.ietf.org/group/moq/about/) e suporte a salas de áudio. O modelo pub-sub do MoQ sobre QUIC se ajusta melhor a áudio ao vivo do que relays WebSocket, porque clientes podem assinar tracks e prioridades específicas e deixar o transporte lidar com congestionamento. Junto da nova tela Public Chats no [PR #2487](https://github.com/vitorpamplona/amethyst/pull/2487), o Amethyst agora tem uma superfície end-to-end para salas públicas de áudio ao lado de seu sistema de mensagens criptografadas com Marmot.

No lado de descoberta e confiabilidade, os [PR #2485](https://github.com/vitorpamplona/amethyst/pull/2485) e [PR #2490](https://github.com/vitorpamplona/amethyst/pull/2490) adicionam um feed de descoberta de Follow Packs e conectam conjuntos curados de follows ao onboarding padrão, dando a usuários novos uma timeline preenchida já no primeiro lançamento. O [PR #1983](https://github.com/vitorpamplona/amethyst/pull/1983) entrega um serviço de notificações sempre ativo para conexões em tempo real com relays, para que DMs Marmot e mentions cheguem sem que o app esteja em foreground, e o [PR #2480](https://github.com/vitorpamplona/amethyst/pull/2480) adiciona cache on-demand de vídeo HLS com dimensionamento adaptativo do cache.

### TollGate v0.1.0 estabiliza acesso à internet pay-per-use sobre Nostr e Cashu

[TollGate](https://github.com/OpenTollGate/tollgate) cortou seu release [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) em 21 de abril, o primeiro snapshot com tag do seu conjunto de especificações para acesso à rede pay-per-use. O protocolo permite que um dispositivo capaz de controlar conectividade, como um roteador WiFi, um switch Ethernet ou um tether Bluetooth, anuncie preços, aceite tokens de ecash [Cashu](/pt/topics/cashu/) e gerencie sessões por meio de tokens locais pré-pagos em vez de contas ou assinaturas. Um cliente com alguns sats em uma carteira Cashu local consegue comprar o próximo minuto ou megabyte de conectividade de qualquer TollGate compatível na rede.

O release fixa três camadas da arquitetura. A camada de protocolo, definida em [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md), especifica três formatos básicos de evento, Advertisement, Session e Notice, e a [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) adiciona pagamentos Cashu por cima, para que um cliente possa resgatar tokens de qualquer mint anunciada pelo gate. Acima disso está a camada de interface: [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) até HTTP-03 definem uma superfície em HTTP simples para dispositivos em sistemas operacionais restritivos, e [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) define o transporte por relay Nostr para clientes que conseguem abrir WebSockets. Por fim, [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) cobre a camada de meio, descrevendo o roteamento de captive portal para clientes pagantes.

Como o ativo de pagamento é um bearer token, um cliente pode chegar já com Cashu em uma carteira local e gastá-lo imediatamente para o primeiro minuto de conectividade. Gates também podem comprar uplink uns dos outros, então o alcance vai além de um único operador. A nova [página de tópico do TollGate](/pt/topics/tollgate/) cobre a pilha completa de camadas.

### nostream mergeia 53 PRs para NIP-45, NIP-62, compressão e hardening de consultas

[nostream](https://github.com/Cameri/nostream), a implementação de relay em TypeScript do Cameri, mergeou 53 PRs em uma única semana cobrindo novo suporte a NIPs, desempenho de consulta, hardening de segurança e polimento operacional.

No trabalho de features, o [PR #522](https://github.com/Cameri/nostream/pull/522) adiciona suporte `COUNT` da [NIP-45](/pt/topics/nip-45/), permitindo que clientes perguntem ao relay quantos eventos correspondem a um filtro sem buscá-los, e o [PR #544](https://github.com/Cameri/nostream/pull/544) adiciona o right-to-vanish da [NIP-62](/pt/topics/nip-62/) à lista de features anunciadas. O [PR #548](https://github.com/Cameri/nostream/pull/548) estende o schema de filtros para aceitar filtros de tags em maiúsculas, `#A` até `#Z`, seguindo as convenções recentes de case em tags, e o [PR #514](https://github.com/Cameri/nostream/pull/514) adiciona compressão gzip e xz à importação e exportação de eventos para que operadores consigam mover grandes dumps entre nós sem tooling extra.

Desempenho e corretude de consulta chegam via [PR #534](https://github.com/Cameri/nostream/pull/534), que introduz um benchmark harness e uma rodada de otimização na tradução de filtros para SQL. O [PR #524](https://github.com/Cameri/nostream/pull/524) corrige um bug de correspondência de pubkeys em whitelist e blacklist trocando prefix matching por verificação de correspondência exata, o [PR #553](https://github.com/Cameri/nostream/pull/553) adiciona um tie-breaker determinístico a `upsertMany` para que inserts concorrentes não disputem mais timestamps `created_at` iguais, e o [PR #493](https://github.com/Cameri/nostream/pull/493) restringe a confiança em `X-Forwarded-For` apenas a proxies configurados como confiáveis. O [PR #557](https://github.com/Cameri/nostream/pull/557) leva o relay à paridade completa com [NIP-11](/pt/topics/nip-11/), alinhando todos os campos anunciados com a spec atual, incluindo limites de retenção, hints de autenticação e o conjunto reduzido de campos opcionais.

## Shipping This Week

### Primal Android lança aba Explore, verificação NIP-05 e player de áudio

[Primal Android](https://github.com/PrimalHQ/primal-android-app) empurrou 11 PRs mergeadas em cima do redesenho de feed da semana passada. O [PR #1021](https://github.com/PrimalHQ/primal-android-app/pull/1021) introduz uma nova aba Explore construída em torno de usuários populares, follow packs e feeds curados, e o [PR #1015](https://github.com/PrimalHQ/primal-android-app/pull/1015) adiciona um editor de feed que pré-preenche a partir da DSL de Advanced Search do Primal. O [PR #994](https://github.com/PrimalHQ/primal-android-app/pull/994) entrega UI de verificação [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md) para perfis, e o [PR #997](https://github.com/PrimalHQ/primal-android-app/pull/997) embute um player de áudio no feed para anexos de arquivos de áudio. O [PR #1018](https://github.com/PrimalHQ/primal-android-app/pull/1018) adiciona pareamento nostr-connect [NIP-46](/pt/topics/nip-46/) a partir do scanner de QR da carteira, reutilizando o mesmo caminho de câmera para signer pairing e wallet linking.

### strfry adiciona métricas Prometheus do caminho de escrita e corrige envelope AUTH da NIP-42

[strfry](https://github.com/hoytech/strfry) lançou um lote de melhorias voltadas a operadores. O [PR #194](https://github.com/hoytech/strfry/pull/194) adiciona um exporter Prometheus dedicado para métricas do caminho de escrita e um novo gauge de conexões, e o [PR #197](https://github.com/hoytech/strfry/pull/197) registra bytes enviados e recebidos por conexão, além de índices de compressão para operadores acompanhando largura de banda. O [PR #192](https://github.com/hoytech/strfry/pull/192) promove o limite hardcoded de tags em filtros a uma opção configurável em runtime. Em corretude de protocolo, o [PR #201](https://github.com/hoytech/strfry/pull/201) altera respostas de falha AUTH da [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) de uma mensagem `NOTICE` para o envelope `OK` que a NIP realmente especifica, resolvendo uma incompatibilidade antiga para relays com autenticação obrigatória.

### Shopstr reforça segurança de storefront em 13 PRs

[Shopstr](https://github.com/shopstr-eng/shopstr), o cliente marketplace Nostr, mergeou 13 PRs nesta semana dominadas por correções de segurança. O [PR #434](https://github.com/shopstr-eng/shopstr/pull/434) fecha uma falha de JavaScript armazenado em links de storefront que permitia execução de scripts do vendedor no navegador do visitante, o [PR #417](https://github.com/shopstr-eng/shopstr/pull/417) escapa a renderização HTML da policy do storefront para bloquear XSS refletido, e o [PR #418](https://github.com/shopstr-eng/shopstr/pull/418) fecha uma API de deleção de eventos em cache sem autenticação que permitia remoção de dados entre usuários. O [PR #433](https://github.com/shopstr-eng/shopstr/pull/433) exige autenticação para leitura de mensagens em cache, o [PR #419](https://github.com/shopstr-eng/shopstr/pull/419) protege endpoints de mutação da storefront e do event cache atrás de auth adequada, e os [PR #435](https://github.com/shopstr-eng/shopstr/pull/435) e [PR #414](https://github.com/shopstr-eng/shopstr/pull/414) corrigem dois achados de SSRF de code scanning. No lado funcional, o [PR #421](https://github.com/shopstr-eng/shopstr/pull/421) torna segura contra replay a fila de publicações em relays que falharam, o [PR #425](https://github.com/shopstr-eng/shopstr/pull/425) repara uma busca quebrada de wallet events, e o [PR #392](https://github.com/shopstr-eng/shopstr/pull/392) revalida descontos salvos no carrinho antes do checkout.

### Nostria v3.1.26 até v3.1.28 adiciona reprodução de música em background no Android

[Nostria](https://github.com/nostria-app/nostria) cortou seis releases nesta semana, da [v3.1.22](https://github.com/nostria-app/nostria/releases/tag/v3.1.22) à [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28). A principal mudança da [v3.1.26](https://github.com/nostria-app/nostria/releases/tag/v3.1.26) é reprodução de música em background no Android: o app se mantém ativo enquanto o áudio toca, com controles de mídia na barra de notificações e na lock screen. As releases seguintes, [v3.1.27](https://github.com/nostria-app/nostria/releases/tag/v3.1.27) e [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28), fazem hardening dessa nova superfície de serviço de mídia. A [Newsletter #18](/en/newsletters/2026-04-15-newsletter/) cobriu o ciclo anterior, com geração local de imagens.

### Wisp v0.18.0-beta adiciona Normie Mode, feed For You e configuração de grupos NIP-29

[Wisp](https://github.com/barrydeen/wisp), o cliente Android em Kotlin e Jetpack Compose de barrydeen, lançou a [v0.18.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.18.0-beta) em 16 de abril. O release mira usuários vindos de contextos menos Bitcoin-native: o [PR #462](https://github.com/barrydeen/wisp/pull/462) adiciona um Normie Mode que mostra valores denominados em fiat em todo o app, e o [PR #464](https://github.com/barrydeen/wisp/pull/464) reformula o onboarding com seletor de tópicos e um coach para o primeiro post. O [PR #469](https://github.com/barrydeen/wisp/pull/469) adiciona um feed For You que mistura follows estendidos, eventos em alta e hashtags seguidas.

No trabalho de protocolo, o [PR #471](https://github.com/barrydeen/wisp/pull/471) adiciona configuração de grupos [NIP-29](/pt/topics/nip-29/) para flags, invites, papéis e prompts AUTH, e o [PR #478](https://github.com/barrydeen/wisp/pull/478) corrige uma falha de ordenação para que o Wisp espere AUTH [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) antes de emitir eventos de grupo `9021`, `9007` e `9009`, além de mostrar falhas do lado do admin. O [PR #481](https://github.com/barrydeen/wisp/pull/481) faz broadcast de notas aos inbox relays [NIP-65](/pt/topics/nip-65/) das pubkeys mencionadas para que replies alcancem seus alvos mesmo quando conjuntos de relays de remetente e destinatário não se sobrepõem.

### NoorNote v0.8.4 adiciona posts agendados e zaps em live stream

[NoorNote](https://github.com/77elements/noornote) lançou a [v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) e a [v0.8.5](https://github.com/77elements/noornote/releases/tag/v0.8.5). A principal adição da v0.8.4 é um add-on de Scheduled Posts: o app entrega um evento totalmente assinado a um relay operado pela NoorNote, que o publica no momento agendado, então as chaves privadas nunca saem do dispositivo. O mesmo release adiciona zaps com um toque em cards de live stream, em que os sats aparecem na sobreposição de chat da stream via [NIP-53](/pt/topics/nip-53/), e mantém o saldo da carteira visível quando a API de cotação fiat fica temporariamente indisponível. A v0.8.5 corrige um bug de deduplicação de timeline que causava posts duplicados em longos scrolls no Android.

### topaz v0.0.2 lança um relay Nostr para Android

[topaz](https://github.com/fiatjaf/topaz), um novo relay Nostr que roda em telefones Android, de [fiatjaf](https://github.com/fiatjaf), publicou a [v0.0.2](https://github.com/fiatjaf/topaz/releases/tag/v0.0.2) em 2026-04-17. O projeto é Kotlin-first e posiciona o telefone como um relay pessoal sempre disponível. Nesta fase o escopo é estreito: um relay funcional dentro de um pacote Android instalável.

### StableKraft v1.0.0 lança o primeiro release estável da PWA de música e podcasts

[StableKraft](https://github.com/ChadFarrow/stablekraft-app) é uma PWA em Next.js para descobrir, organizar e transmitir música puxada de feeds de podcast, usando Nostr para auth e recursos sociais e Lightning para pagamentos V4V. Ela chegou à [v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0) em 2026-04-18. Na mesma semana, o projeto endureceu ingestão de feeds com um [cache OPML de 15 minutos e stripping de XML inválido](https://github.com/ChadFarrow/stablekraft-app/commit/7ac90f6) e reduziu a janela de nightly reparse de 720 horas para 24 horas em um [ajuste posterior](https://github.com/ChadFarrow/stablekraft-app/commit/fbf337b), acelerando a autocorreção de feeds recém-adicionados.

### NipLock lança um gerenciador de senhas baseado em NIP-17

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) é um gerenciador de senhas que armazena e sincroniza credenciais entre dispositivos usando mensagens diretas gift-wrapped da [NIP-17](/pt/topics/nip-17/). Cada entrada de senha é uma DM NIP-17 da chave do próprio usuário para ela mesma, então os mesmos eventos se replicam para qualquer dispositivo autenticado com essa chave. A assinatura funciona com `nsec` bruto, extensões de navegador como [nos2x](https://github.com/fiatjaf/nos2x) ou [Amber](https://github.com/greenart7c3/Amber) via [NIP-46](/pt/topics/nip-46/), o que mantém a chave mestra fora do dispositivo cliente.

### flotilla-budabit refina sua superfície de repositórios NIP-34

O fork da comunidade Budabit do [Flotilla](https://gitea.coracle.social/coracle/flotilla), chamado [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit), lançou um conjunto de correções em seu fluxo de git-over-nostr da NIP-34. As atualizações desta semana [restauram controles de discussão de repositório](https://github.com/Pleb5/flotilla-budabit/commit/a6fb67e), [mantêm abas fixas visíveis em páginas de detalhe](https://github.com/Pleb5/flotilla-budabit/commit/e2b891a), [carregam anúncios de repositório a partir de relays GRASP salvos](https://github.com/Pleb5/flotilla-budabit/commit/43d5e9e) e [sincronizam o estado de patch aplicado pelo mantenedor](https://github.com/Pleb5/flotilla-budabit/commit/2dbb9f0). Mantendo-se próximo ao upstream do Flotilla, o fork prioriza a view de repositórios para contribuidores da comunidade Budabit.

### rx-nostr 3.7.2 até 3.7.4 adicionam verificador padrão e argumentos opcionais no construtor

[rx-nostr](https://github.com/penpenpng/rx-nostr), a biblioteca Nostr baseada em RxJS, lançou [3.7.2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.2), [3.7.3](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.3) e [3.7.4](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.4). O [PR #192](https://github.com/penpenpng/rx-nostr/pull/192) adiciona um verificador padrão de assinaturas Schnorr, eliminando a necessidade de quem chama ligar um verificador manualmente, e uma release emparelhada [crypto@3.1.6](https://github.com/penpenpng/rx-nostr/releases/tag/crypto%403.1.6) corrige um bug de uso em `@noble/curves` que estava produzindo falhas espúrias de verificação. O [PR #195](https://github.com/penpenpng/rx-nostr/pull/195), na 3.7.4, torna opcionais os argumentos de `createRxNostr()`, permitindo integrações rápidas com zero configuração.

### Keep Android v1.0.0 lança builds reproduzíveis e zero trackers

[Keep](https://github.com/privkeyio/keep-android), um gerenciador de senhas e segredos nativo de Nostr, lançou a [v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0) em 21 de abril após uma série de PRs de hardening. O [PR #241](https://github.com/privkeyio/keep-android/pull/241) adiciona uma receita de build reproduzível com toolchain fixada e verificada, o [PR #248](https://github.com/privkeyio/keep-android/pull/248) troca Google ML Kit por ZXing para remover dependência de Google Play Services, e o [PR #252](https://github.com/privkeyio/keep-android/pull/252) publica um [scan do Exodus Privacy](https://reports.exodus-privacy.eu.org/en/) mostrando zero trackers na build v1.0.0. O [PR #256](https://github.com/privkeyio/keep-android/pull/256) adiciona um manifesto `zapstore.yaml` para que o APK possa ser distribuído via [zapstore](https://zapstore.dev) sem publisher intermediário.

### Flotilla 1.7.3 e 1.7.4 adicionam encapsulamento kind 9 para salas NIP-29 mais ricas

[Flotilla](https://gitea.coracle.social/coracle/flotilla), o cliente de grupos [NIP-29](/pt/topics/nip-29/) do hodlbod, lançou [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) e [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4). A principal mudança de protocolo é o encapsulamento em kind `9` de tipos de conteúdo que não são chat, anunciado na [nota de release do hodlbod](nostr:nevent1qvzqqqqqqypzp978pfzrv6n9xhq5tvenl9e74pklmskh4xw6vxxyp3j8qkke3cezqyvhwumn8ghj76rzwghxxmmjv93kcefwwdhkx6tpdshszrnhwden5te0dehhxtnvdakz7qgawaehxw309a5x7ervvfhkgtnrdaexzcmvv5h8xmmrd9skctcqyrrclae7mhmm5dnumwfzhg3fxu74a4hh24jd8pvn8v0hye9w3g6tuljtr85) e rastreada contra o [NIP PR #2310](https://github.com/nostr-protocol/nips/pull/2310). Encapsular eventos de calendário, enquetes e outros payloads em kind `9` preserva o contexto da sala quando esses objetos são enviados a um grupo, permitindo que clientes renderizem o objeto embutido sem perder de qual sala ele veio.

Essa mesma linha de release adiciona enquetes, suporte ao esquema de URL Aegis para login [NIP-46](/pt/topics/nip-46/), compartilhamento nativo de invites para spaces, room mentions, colagem de imagem da área de transferência no mobile, drafts, vídeo em chamadas e melhorias de paginação do feed. É o primeiro release do Flotilla desde [1.7.0 e 1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0), cobertos na [Newsletter #16](/pt/newsletters/2026-04-01-newsletter/) por salas de voz e login por email.

### WoT Relay v0.2.1 migra eventstore para LMDB

[WoT Relay](https://github.com/bitvora/wot-relay), o relay filtrado por web of trust da bitvora, lançou a [v0.2.1](https://github.com/bitvora/wot-relay/releases/tag/v0.2.1) em 2026-04-22. O [PR #97](https://github.com/bitvora/wot-relay/pull/97) migra o eventstore para [LMDB](http://www.lmdb.tech/) e recalibra os fetches iniciais do grafo WoT para que o relay construa seu trust graph sem esgotar orçamentos de leitura upstream, e o [PR #99](https://github.com/bitvora/wot-relay/pull/99) faz upgrade de `golang.org/x/crypto` para v0.45.0 com as correções de segurança correspondentes. O [PR #100](https://github.com/bitvora/wot-relay/pull/100) atualiza a URL de software e a string de versão anunciadas via [NIP-11](/pt/topics/nip-11/) para o release.

### Suíte Formstr: hardening do Pollerama, i18n no Forms, suporte a RRULE no Calendar

A suíte Formstr mergeou 26 PRs nesta semana, espalhadas por Pollerama, Formstr Forms e Nostr Calendar, com um tema claro de segurança no app de enquetes e trabalho de feature no restante.

[Pollerama](https://pollerama.fun), o app [nostr-polls](https://github.com/formstr-hq/nostr-polls) para criação e voto em enquetes Nostr, endureceu seu tratamento de chaves. O [PR #182](https://github.com/formstr-hq/nostr-polls/pull/182) expira DMs em cache no logout para que um dispositivo compartilhado não vaze estado do usuário anterior, o [PR #175](https://github.com/formstr-hq/nostr-polls/pull/175) move a chave local para armazenamento seguro do navegador, e o [PR #171](https://github.com/formstr-hq/nostr-polls/pull/171) protege `JSON.parse` do conteúdo de perfil kind `0` em todo caminho de login, para que um perfil malformado não derrube a sessão. No lado de produto, o [PR #186](https://github.com/formstr-hq/nostr-polls/pull/186) conecta deep linking HTTPS de `pollerama.fun`, e o [PR #169](https://github.com/formstr-hq/nostr-polls/pull/169) torna clicáveis os nomes de autores nos resultados.

[Formstr](https://formstr.app), a suíte [nostr-forms](https://github.com/formstr-hq/nostr-forms) para forms nativos de Nostr, ampliou sua superfície de input e onboarding. O [PR #475](https://github.com/formstr-hq/nostr-forms/pull/475) adiciona suporte a URLs de áudio e vídeo para embeds de mídia dentro dos forms, o [PR #439](https://github.com/formstr-hq/nostr-forms/pull/439) introduz i18n no app web, e o [PR #466](https://github.com/formstr-hq/nostr-forms/pull/466) entrega um importador de onboarding para Google Forms, permitindo que criadores migrem sem reconstruir pesquisas do zero. O [PR #463](https://github.com/formstr-hq/nostr-forms/pull/463) fecha um vazamento de privacidade removendo logs sensíveis de chaves do console do navegador.

[Nostr Calendar by Formstr](https://calendar.formstr.app) lançou [v1.3.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.3.0) e [v1.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.0) no mesmo dia, com destaque para uma superfície adequada de regras de recorrência. O [PR #107](https://github.com/formstr-hq/nostr-calendar/pull/107) adiciona suporte a RRULE múltiplo e customizado, e o [PR #101](https://github.com/formstr-hq/nostr-calendar/pull/101) corrige um bug antigo ao interpretar datas RRULE flutuantes como UTC segundo a RFC 5545, eliminando deriva de horário entre timezones. O [PR #97](https://github.com/formstr-hq/nostr-calendar/pull/97) permite adicionar eventos compartilhados ao calendário pessoal, o [PR #86](https://github.com/formstr-hq/nostr-calendar/pull/86) introduz preferências de notificação por lista, e o [PR #112](https://github.com/formstr-hq/nostr-calendar/pull/112) entrega o caminho retrabalhado de login e loading presente na v1.4.0. Os três projetos se apoiam em eventos de calendário da [NIP-52](/pt/topics/nip-52/) e compartilham a mesma stack de login.

### Também lançaram: notedeck, nostr.blue, cliprelay, Captain's Log

Um punhado de clientes lançou releases iterativas sem um recurso dominante. O cliente em Rust da equipe Damus, [notedeck](https://github.com/damus-io/notedeck), publicou a [v0.10.0-beta.4](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.4) com correções em rendering de colunas e relay pool. O cliente em Rust baseado em Dioxus [nostr.blue v0.8.6](https://github.com/patrickulrich/nostr.blue/releases/tag/v0.8.6) puxou o [Dioxus 0.7.5](https://github.com/patrickulrich/nostr.blue/commit/d90b4ff) e destravou a build Android ao [converter a bridge de áudio nativa](https://github.com/patrickulrich/nostr.blue/commit/4207f0c) em um plugin `manganis::ffi`. [cliprelay](https://github.com/tajava2006/cliprelay), uma ferramenta de sincronização de clipboard entre dispositivos que retransmite entradas por Nostr, lançou [Desktop v0.0.3](https://github.com/tajava2006/cliprelay/releases/tag/desktop%2Fv0.0.3) e [Android v0.0.4](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.0.4), ajustando o loop de sync e removendo variantes Android de 32 bits. [Captain's Log](https://github.com/nodetec/comet) publicou três builds alpha cujo recurso mais útil é [detecção de liveness](https://github.com/nodetec/comet/releases/tag/alpha-95f47bd) no sync relay, substituindo sockets caídos sem ação do usuário.

## In Development

### whitenoise-rs refatora para views de conta com escopo de sessão

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), o daemon em Rust por baixo do cliente [Marmot](/pt/topics/marmot/), mergeou 15 PRs avançando uma refatoração em múltiplas fases, saindo de singletons globais para views `AccountSession` por conta. O objetivo é quebrar um monólito compartilhado em superfícies menores por conta, mais fáceis de entender, testar e evoluir sem vazamento de efeitos colaterais pelo daemon inteiro.

A fundação veio com o [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743), que introduz `AccountSession` e `AccountManager`, seguida por relay handles com escopo por conta no [PR #753](https://github.com/marmot-protocol/whitenoise-rs/pull/753). Fases posteriores moveram drafts e settings, operações de mensagem, leitura e escrita de grupo, membership, push notifications, leituras de key packages e criação de grupo para superfícies pertencentes à sessão ao longo dos [PRs #760 até #769](https://github.com/marmot-protocol/whitenoise-rs/pulls?q=is%3Apr+is%3Amerged+768+OR+763+OR+766). A fase 15 fecha o ciclo no [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770), que transfere o dispatch de eventos para a sessão, fazendo com que cada conta consuma seu próprio tráfego de relay sem contenção em um dispatcher compartilhado.

### White Noise adiciona UI de block/unblock, leave-group e avisos offline

[White Noise](https://github.com/marmot-protocol/whitenoise), o cliente [Marmot](/pt/topics/marmot/), adicionou os controles que faltavam no ciclo de vida dos grupos. O [PR #578](https://github.com/marmot-protocol/whitenoise/pull/578) lança a UI de block e unblock em cima de um block hook introduzido no [PR #573](https://github.com/marmot-protocol/whitenoise/pull/573), e o [PR #571](https://github.com/marmot-protocol/whitenoise/pull/571), junto do [PR #572](https://github.com/marmot-protocol/whitenoise/pull/572), conecta `clear_chat`, `delete_chat` e `leave_and_delete_group` do lado Rust ao app. Os [PR #569](https://github.com/marmot-protocol/whitenoise/pull/569) e [PR #576](https://github.com/marmot-protocol/whitenoise/pull/576) adicionam avisos offline nas telas de chat e settings para que usuários saibam quando o daemon não consegue alcançar seus relays. O [PR #585](https://github.com/marmot-protocol/whitenoise/pull/585) estreita o caminho amplo de delete all key packages para uma operação de delete legacy key packages, evitando que um cliente em migração entre formatos de KeyPackage apague chaves atuais junto das legadas.

### MDK adiciona suporte a invites entre versões mistas e convergência de SelfUpdate

[MDK](https://github.com/marmot-protocol/mdk), o [Marmot](/pt/topics/marmot/) Development Kit, mergeou sete PRs. O fio condutor do trabalho é compatibilidade, mantendo clientes em versões ligeiramente diferentes do Marmot capazes de convidar uns aos outros, rotacionar o próprio estado e recuperar-se limpos de entradas malformadas.

A correção principal é o [PR #261](https://github.com/marmot-protocol/mdk/pull/261), que computa `RequiredCapabilities` de um grupo como o LCD das capabilities dos convidados e desbloqueia invites entre versões mistas de [Amethyst](https://github.com/vitorpamplona/amethyst) e [White Noise](https://github.com/marmot-protocol/whitenoise). O [PR #264](https://github.com/marmot-protocol/mdk/pull/264) converge o formato wire de SelfUpdate entre implementações; SelfUpdate é a mensagem de controle que um membro de grupo envia quando rotaciona seu próprio KeyPackage ou estado de capabilities, então drift ali quebra silenciosamente a auto-rotação entre clientes mesmo quando invites e welcomes ainda fazem parse. Em robustez, o [PR #262](https://github.com/marmot-protocol/mdk/pull/262) faz parse dos key packages dos convidados antes de persistir o signer do criador para que um convidado malformado não deixe estado residual, o [PR #256](https://github.com/marmot-protocol/mdk/pull/256) corrige a validação de depletion de admin no lado do receiver, e o [PR #259](https://github.com/marmot-protocol/mdk/pull/259) impede que o backend de armazenamento in-memory evite estado crítico de segurança sob pressão. O [PR #265](https://github.com/marmot-protocol/mdk/pull/265) expõe um accessor `group_required_proposals` para que clientes possam inspecionar as proposals que DEVEM entrar antes de o próximo commit ser válido sem precisar mergulhar em internals do MDK.

### nostter adiciona criptografia NIP-44 a people lists, bookmarks e mutes

[nostter](https://github.com/SnowCait/nostter) mergeou 10 PRs. O [PR #2088](https://github.com/SnowCait/nostter/pull/2088) adiciona criptografia [NIP-44](/pt/topics/nip-44/) a mute lists, o [PR #2089](https://github.com/SnowCait/nostter/pull/2089) faz o mesmo para bookmarks e o [PR #2090](https://github.com/SnowCait/nostter/pull/2090) para people lists, migrando para longe da [NIP-04](/pt/topics/nip-04/) onde aplicável. O [PR #2087](https://github.com/SnowCait/nostter/pull/2087) remove um caminho legado de migração de mutes kind-30000 agora que o fluxo criptografado kind-10000 se estabilizou.

### zap.cooking lança pontuação Nourish e thread de comentários reutilizável

[zap.cooking](https://github.com/zapcooking/frontend), o cliente Nostr de receitas, mergeou 20 PRs nesta semana. O principal recurso é um novo módulo de pontuação de receitas chamado Nourish, nos [PR #317](https://github.com/zapcooking/frontend/pull/317) e [PR #319](https://github.com/zapcooking/frontend/pull/319), que avalia receitas em eixos nutricionais. Ao lado disso, uma refatoração em quatro estágios, do [PR #299](https://github.com/zapcooking/frontend/pull/299) ao [PR #302](https://github.com/zapcooking/frontend/pull/302), extrai o módulo Comments para um `CommentThread` reutilizável que pode ser inserido em qualquer view. O polimento do lado de receitas inclui scaling no [PR #309](https://github.com/zapcooking/frontend/pull/309), um botão unificado de upload de mídia no [PR #307](https://github.com/zapcooking/frontend/pull/307) e uma aba Replies no perfil no [PR #310](https://github.com/zapcooking/frontend/pull/310).

### ridestr extrai coordenador compartilhado de passageiros

[ridestr](https://github.com/variablefate/ridestr), o app descentralizado de ride-sharing, mergeou 10 PRs refatorando suas telas em Compose em componentes mais focados e extraindo a lógica de protocolo de passageiro e motorista para um módulo coordenador compartilhado `:common`, no [PR #70](https://github.com/variablefate/ridestr/pull/70). O [PR #60](https://github.com/variablefate/ridestr/pull/60) adiciona um receiver kind `3189` para driver-ping no lado Roadflare do app.

### Blossom rascunha cabeçalho BUD-01 Sunset para expiração de blobs

[Blossom](https://github.com/hzrd149/blossom), o protocolo do hzrd149 para armazenar blobs em servidores HTTP indexados por hash SHA-256, abriu o [PR #99](https://github.com/hzrd149/blossom/pull/99) para adicionar um cabeçalho `Sunset` ao BUD-01. Um servidor pode usar o cabeçalho para anunciar um timestamp futuro em que deixará de servir um blob, permitindo que clientes planejem em torno de retenção limitada antes de bater em um 404. Como a proposta usa semântica padrão da [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) e é apenas consultiva, o servidor continua livre para manter o blob por mais tempo ou honrar a expiração declarada em base best effort.

## New Projects

### Forgesworn publica um kit criptográfico de 29 repositórios para Nostr

[Forgesworn](https://github.com/forgesworn) lançou 29 repositórios open source em cinco dias cobrindo assinatura, identidade, atestações, web of trust e descoberta de APIs pagas sobre Nostr.

A stack de assinatura se ancora em [nsec-tree](https://github.com/forgesworn/nsec-tree), um esquema determinístico de derivação de subidentidades que transforma um único segredo mestre em identidades Nostr ilimitadas e não correlacionáveis, e em [Heartwood](https://github.com/forgesworn/heartwood), um signer remoto NIP-46 que roda em Raspberry Pi com Tor habilitado por padrão. [Sapwood](https://github.com/forgesworn/sapwood) adiciona uma UI web de gerenciamento para modelar um signer Heartwood, e [heartwood-esp32](https://github.com/forgesworn/heartwood-esp32) publica um experimento com a mesma lógica de token de assinatura em uma placa Heltec WiFi LoRa 32. [nsec-tree-cli](https://github.com/forgesworn/nsec-tree-cli) expõe os fluxos de derivação, prova e recuperação por Shamir para operação offline-first.

Em identidade e confiança, [Signet](https://github.com/forgesworn/signet) chegou à [v1.6.0](https://github.com/forgesworn/signet/releases/tag/v1.6.0) como um protocolo descentralizado de verificação de identidade para Nostr, com pareamento por QR em que a pubkey de sessão é validada e pinada ao relay. [nostr-attestations](https://github.com/forgesworn/nostr-attestations) define um evento kind `31000`, NIP-VA, para credenciais, endorsements, vouches, provenance, licensing e trust, consolidando o que hoje está espalhado por formatos ad hoc. [nostr-veil](https://github.com/forgesworn/nostr-veil) constrói uma web of trust que preserva privacidade por cima disso, com asserções NIP-85 apoiadas por [LSAG ring signatures](https://github.com/forgesworn/ring-sig) em secp256k1, de forma que um vouch possa provar membership em um grupo sem revelar qual membro o emitiu.

O lado de monetização cobre APIs pagas via Lightning e Nostr. [toll-booth](https://github.com/forgesworn/toll-booth) é um middleware L402 para Express, Hono, Deno, Bun e Cloudflare Workers que transforma qualquer API em um toll booth Lightning em uma linha, com [toll-booth-dvm](https://github.com/forgesworn/toll-booth-dvm) expondo a API protegida como um DVM da [NIP-90](/pt/topics/nip-90/) e [toll-booth-announce](https://github.com/forgesworn/toll-booth-announce) fazendo bridge para [402-announce](https://github.com/forgesworn/402-announce), que publica eventos parameterized replaceable kind `31402` para descoberta de serviços HTTP 402 no Nostr. [402-indexer](https://github.com/forgesworn/402-indexer) é o crawler que recolhe esses anúncios. A organização também publicou uma [coleção de 29 rascunhos de NIP](https://github.com/forgesworn/nip-drafts) cobrindo coordenação de serviços, confiança, pagamentos, disputas, hierarquia de chaves, curadoria de recursos e descoberta de API paga.

Tudo é escrito em TypeScript, sem dependências quando possível, e lançado por uma nova ferramenta bash-only chamada [anvil](https://github.com/forgesworn/anvil), reforçada para supply chain, com attestation de builds reproduzíveis em múltiplos runners e trusted publishing por OIDC. Várias primitivas do conjunto, incluindo ring signatures, range proofs e shares de palavras por Shamir, preenchem lacunas antigas da camada de bibliotecas Nostr.

### ShockWallet lança sincronização nativa de carteira Lightning via Nostr e conexões com múltiplos nós

[ShockWallet](https://github.com/shocknet/wallet2) é uma carteira Lightning que usa Nostr como transporte para conexão com nós Lightning self-custodial. O app faz pareamento com um ou mais nós [Lightning.Pub](https://github.com/shocknet/Lightning.Pub) sobre Nostr via um `nprofile`, e depois assina autorizações de pagamento end-to-end entre a carteira e o nó. A equipe lançou o [PR #608](https://github.com/shocknet/wallet2/pull/608) em 2026-04-18 com um passe de UI no dashboard de canais, acompanhado de um fluxo QR de admin invite link para novos usuários do PUB, [PR #606](https://github.com/shocknet/wallet2/pull/606), e de uma correção de legibilidade no dashboard de métricas, [PR #607](https://github.com/shocknet/wallet2/pull/607).

O ShockWallet usa eventos de dados específicos de aplicação [NIP-78](/pt/topics/nip-01/) para sincronização do estado da carteira entre dispositivos, de forma que a visão da carteira do usuário permaneça consistente entre navegador desktop e telefone sem um servidor centralizado de sync. Isso o coloca uma camada abaixo da [NIP-47](/pt/topics/nip-47/): NIP-47 é a interface que um app usa para pedir a uma carteira existente que pague, enquanto o ShockWallet usa Nostr como transporte de conta e sessão da própria carteira até o nó Lightning subjacente. Ao lado da carteira, a equipe segue empurrando o [CLINK](https://github.com/shocknet/CLINK), um protocolo de pareamento de sessão baseado em Nostr para conexões carteira-app, mantendo uma única codebase TypeScript que gera builds para web, Android e iOS.

### Issues do Nostrability migram para git over Nostr após censura do GitHub

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues), o rastreador de interoperabilidade de elsat para clientes e relays Nostr, está movendo seu fluxo de issues para git over Nostr depois que a organização Nostrability foi derrubada do GitHub e o suporte do GitHub não respondeu por duas semanas. O issue tracker migrado agora vive em GitWorkshop/ngit, onde as issues existentes foram carregadas e relatórios futuros de interoperabilidade podem permanecer em infraestrutura nativa de Nostr.

### nowhere codifica sites inteiros em fragments de URL e roteia pedidos por Nostr

[nowhere](https://github.com/5t34k/nowhere) é um novo projeto AGPL-3.0 de [5t34k](https://github.com/5t34k) que serializa um site inteiro no fragmento da URL depois de `#`, comprime esse conteúdo com substituição por dicionário e DEFLATE cru e então o codifica em base64url. Como o HTTP proíbe navegadores de enviar fragments ao servidor, o host que entrega a página nunca vê o conteúdo e o próprio site nunca fica armazenado em um servidor. O projeto lança oito tipos de site, incluindo event, fundraiser, store, petition, message, drop, art e forum, e cada um pode ser assinado criptograficamente pelo criador e criptografado com senha na própria URL.

Cinco dos oito tipos são puramente estáticos, mas store, forum e petition exigem comunicação ao vivo para pedidos, posts e assinaturas, e esse tráfego roda por relays Nostr usando chaves efêmeras com criptografia [NIP-44](/pt/topics/nip-44/), então o relay armazena eventos que não consegue ler de chaves descartáveis que não consegue rastrear. Uma loja com item único cabe em cerca de 120 caracteres, o que faz de um link nowhere um QR code imprimível para uso offline via o leitor [nowhr.xyz](https://nowhr.xyz/install). O repositório é um workspace pnpm dividido em um pacote `codec`, uma biblioteca de componentes Svelte 5 `web` com integração Nostr e pagamento e o app shell `nowhr` em [nowhr.xyz](https://nowhr.xyz/app).

### Pequenas novas superfícies: relayk.it e Brainstorm Search

Dois projetos pequenos merecem menção sem um changelog pesado. [relayk.it](https://relayk.it), construído por [sam](https://nostr.com/sam@relayk.it) da equipe Soapbox, é um cliente de descoberta de relays construído com [Shakespeare](https://shakespeare.diy) que roda inteiramente no navegador e aponta usuários para relays Nostr ativos. [Brainstorm Search](https://brainstorm.world) surge como uma UI de busca Nostr em página única focada em expor conteúdo pela rede.

## Protocol and Spec Work

### NIP Updates

Propostas e discussões recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Open PRs and Discussions:**

- **[NIP-67](/pt/topics/nip-67/): EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)): propõe adicionar um terceiro elemento opcional à mensagem `EOSE` da [NIP-01](/pt/topics/nip-01/) para que um relay sinalize se entregou todos os eventos armazenados que correspondem ao filtro. Hoje, `EOSE` marca a fronteira entre histórico e tempo real, mas não diz nada sobre completude. Um cliente que pede 500 eventos a um relay limitado a 300 recebe 300 eventos e um `EOSE`, sem saber se aquilo é tudo ou se o relay parou no meio. A proposta adiciona o formato `['EOSE', '<sub_id>', 'finish']` quando o relay entregou tudo e mantém o formato legado de dois elementos como caso sem alegação de completude. O desenho é backward compatible, já que relays que não anunciam suporte caem na heurística atual, e clientes que conhecem o suporte podem parar de paginar assim que veem o sinal positivo.

- **NIP-5D: Nostr Applets** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): propõe um novo kind para distribuir applets interativos em Nostr. Onde a [NIP-5A](/pt/topics/nip-5a/) cobre sites estáticos e a [NIP-5C](/pt/topics/nip-5c/) cobre scrolls executáveis em WASM, a NIP-5D mira o meio-termo de applets front-end autocontidos que rodam no iframe sandboxed ou WebView de um cliente, endereçáveis por evento Nostr e atualizáveis por uma tag replaceable. Clientes passam a ter uma maneira de distribuir experiências de terceiros, como enquetes, calculadoras e mini-games, sem precisar criar um sistema completo de plugins. O PR aberto continua iterando sobre o modelo de segurança de passagem de mensagens entre applet e host.

- **NIP-29: spec de subgrupos** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319)): estende grupos baseados em relay da [NIP-29](/pt/topics/nip-29/) com uma hierarquia de subgrupos para que um grupo único hospede vários canais paralelos sem precisar criar grupos independentes no mesmo relay. O PR define um identificador de subgrupo que se apoia na tag `h`, especifica como eventos de moderação da faixa kind `9000` passam a valer para um subgrupo e esclarece como clientes devem renderizar a hierarquia. A mudança preserva o formato de uma única tag `h` em mensagens simples, mantendo clientes antigos funcionais em salas com subgrupos.

- **NIP-29: permissões explícitas de papel em kind 39003** ([PR #2316](https://github.com/nostr-protocol/nips/pull/2316)): define um schema explícito de permissões no evento de papéis kind `39003` da [NIP-29](/pt/topics/nip-29/). Cada papel passa a ser um conjunto nomeado de operações concedidas, como invite, add-user, remove-user, edit-metadata, delete-event e add-permission, com expiração opcional. Hoje, dois relays NIP-29 rodando o mesmo grupo podem discordar sobre o que um moderator pode fazer, e clientes não têm como refletir essa diferença ao usuário; o schema corrige isso.

- **NIP-11: campo access_control para descoberta de relays restritos** ([PR #2318](https://github.com/nostr-protocol/nips/pull/2318)): adiciona um objeto opcional `access_control` ao Relay Information Document da [NIP-11](/pt/topics/nip-11/), listando o modo de restrição do relay, como open, invite, payment ou allowlist, e qualquer endpoint que um cliente possa usar para pedir acesso. O campo é apenas consultivo e permite que clientes e diretórios filtrem relays restritos para fora de listas públicas e mostrem aos usuários, de antemão, por que um relay se recusa a aceitar escritas.

- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): coberto na [Newsletter #18](/en/newsletters/2026-04-15-newsletter/). O PR continua iterando no formato do descritor de gateway de pagamentos kind `10164` e no layout dos campos para regras de assinatura por faixa.

- **NIP-XX: Agent Reputation Attestations, kind 30085** ([PR #2320](https://github.com/nostr-protocol/nips/pull/2320)): propõe um evento endereçável kind `30085` para atestações assinadas sobre agentes autônomos e serviços no Nostr, cobrindo confiabilidade, honest advertising e claims de resolução de disputas. Cada atestação aponta para uma pubkey alvo, carrega uma pontuação em faixa delimitada e referencia o evento de evidência que justifica a nota. A motivação é que DVMs da [NIP-90](/pt/topics/nip-90/) e outros mercados de serviço ainda não têm uma forma padrão para clientes publicarem feedback verificável que outros clientes possam filtrar.

- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): continua a partir da [Newsletter #18](/en/newsletters/2026-04-15-newsletter/) com mais iterações em torno do kind `20411`, do formato de criptografia por destinatário com [NIP-44](/pt/topics/nip-44/) e da semântica da tag `ttl` para retenção em relays.

- **marmot-ts 0.5.0 release PR** ([PR #70](https://github.com/marmot-protocol/marmot-ts/pull/70)): o PR pendente de release para `@internet-privacy/marmot-ts@0.5.0` empacota as primeiras breaking changes planejadas no cliente Marmot em TypeScript. O release faz `KeyPackageManager` suportar tanto eventos legados kind `443` quanto os novos kind `30443`, remove `KeyPackageStore` e as classes de armazenamento de estado de grupo em favor da passagem de um key-value store genérico diretamente para `KeyPackageManager` e `MarmotGroup` e move invites e gerenciamento de grupo para `MarmotClient.invites` e `MarmotClient.groups`. Projetos que embutem marmot-ts diretamente terão mudanças de construtor e camada de storage para absorver o release.

## NIP Deep Dive: NIP-72 (Moderated Communities)

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) define um modelo de comunidades baseadas em tópico no Nostr em que moderadores curam uma view de leitura sobre escritas que, em si, continuam irrestritas. Diferente de grupos baseados em relay da [NIP-29](/pt/topics/nip-29/), em que o relay é a autoridade tanto de membership quanto de moderação, uma comunidade NIP-72 vive em eventos Nostr comuns e qualquer relay que carregue os kinds relevantes pode servi-la. Qualquer pessoa pode publicar em uma comunidade, e apenas posts aprovados por um moderador reconhecido aparecem no feed da comunidade.

Uma comunidade é definida por um evento endereçável kind `34550` publicado por seu criador. O evento é replaceable com tag `d`, então o criador pode editar os metadados ao longo do tempo sem perder a identidade da comunidade. A tag `d` é o slug estável, tags `name`, `description`, `image` e `rules` carregam metadados de exibição, e uma série de tags `p` com marcador `moderator` lista as pubkeys cujas aprovações contam. Tags `relay` opcionais com marcadores `author`, `requests` ou `approvals` sugerem onde cada tipo de evento deve ser publicado e buscado.

```json
{
  "id": "f1e2d3c4b5a69788f1e2d3c4b5a69788f1e2d3c4b5a69788f1e2d3c4b5a69788",
  "pubkey": "c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2",
  "created_at": 1745280000,
  "kind": 34550,
  "tags": [
    ["d", "bitcoin-devs"],
    ["name", "Bitcoin Devs"],
    ["description", "A moderated community for Bitcoin protocol discussion."],
    ["image", "https://example.com/bitcoin-devs.png"],
    ["rules", "Stay on topic; cite sources."],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876", "", "moderator"],
    ["p", "a1b2c3d4e5f6a7b8c9d0a1b2c3d4e5f6a7b8c9d0a1b2c3d4e5f6a7b8c9d0a1b2", "", "moderator"],
    ["relay", "wss://relay.example.com", "author"],
    ["relay", "wss://relay.moderator.com", "approvals"]
  ],
  "content": "",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Um usuário envia um post publicando qualquer evento comum, uma nota kind `1`, um artigo long-form kind `30023`, um evento de calendário kind `31922` e assim por diante, e adicionando uma tag `a` cujo valor é a coordenada da comunidade `34550:<creator_pubkey>:<slug>`. O post é um evento Nostr totalmente válido por si só, e clientes sem suporte a NIP-72 simplesmente o veem como uma nota endereçada a uma coordenada com formato de comunidade. Clientes com conhecimento da comunidade filtram sua view para posts aprovados por um moderador reconhecido.

A aprovação é um evento separado kind `4549`, publicado por um moderador. A aprovação referencia a submissão por tag `e`, o autor por tag `p` e a comunidade por tag `a`, além de embutir o evento de submissão stringificado no campo `content` como cópia em cache. Essa cópia embutida mantém o post aprovado renderizável mesmo que o autor original apague depois o evento-fonte.

```json
{
  "id": "a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1745283600,
  "kind": 4549,
  "tags": [
    ["a", "34550:c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2:bitcoin-devs"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["p", "e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5"],
    ["k", "1"]
  ],
  "content": "{\"id\":\"b3c4d5e6...\",\"pubkey\":\"e4f5a6b7...\",\"kind\":1,\"content\":\"Question about sighash flags\",\"tags\":[[\"a\",\"34550:c3d2e1f0...:bitcoin-devs\"]],\"created_at\":1745283500,\"sig\":\"...\"}",
  "sig": "bbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aa"
}
```

O modelo de aprovação tem três propriedades úteis. Decisões de moderação são transparentes: toda aprovação é um evento Nostr assinado que qualquer um pode buscar, então um usuário cético pode auditar qual moderador aprovou qual post e em que momento. A moderação não é exclusiva: a mesma submissão pode ser aprovada por múltiplas comunidades, e um post rejeitado por uma pode ser aprovado por outra, porque a tag `a` é apenas um endereço para uma view curada. A moderação é reversível na camada de leitura: se uma comunidade remove um moderador de seu evento kind `34550`, aprovações anteriores desse moderador deixam de contar em clientes que respeitam a lista atual de moderadores.

É no lado da leitura que clientes diferem. A maior parte dos clientes com suporte a comunidades renderiza o feed filtrando eventos kind `4549` tagueados com a coordenada da comunidade, deduplicando pelo ID do evento subjacente e então renderizando o post embutido. Alguns clientes também buscam diretamente as submissões e usam aprovações apenas como whitelist, o que faz sentido quando aprovações estão incompletas ou stale. Alguns poucos clientes, incluindo [noStrudel](https://github.com/hzrd149/nostrudel) e, desde o [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) desta semana, [Amethyst](https://github.com/vitorpamplona/amethyst), expõem a fila de submissões pendentes aos moderadores como uma view separada.

Comparadas aos grupos baseados em relay da [NIP-29](/pt/topics/nip-29/), as trocas ficam claras. Comunidades NIP-72 funcionam sobre qualquer rede de relays sem suporte especial, então o caminho de escrita é portátil e a moderação é visível e passível de fork. Uma submissão é pública no momento em que é publicada, e posts não aprovados ficam ocultos na camada de renderização do cliente. Para espaços em que spam precisa ficar totalmente fora do wire, NIP-29 se encaixa melhor. Para comunidades públicas temáticas em que aprovação funciona mais como uma front page curada do que como um portão, NIP-72 se encaixa melhor.

## NIP Deep Dive: NIP-57 (Zaps)

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md) define zaps, uma forma de anexar pagamentos Lightning a identidades e eventos Nostr e de publicar um recibo verificável desse pagamento de volta aos relays. Um zap prova que um remetente específico pagou um valor específico a um destinatário específico por um alvo específico, e a prova pode ser lida por qualquer cliente Nostr sem confiar apenas na palavra do remetente. A spec atravessa três sistemas, LNURL, Lightning e Nostr, e fixa como eles precisam cooperar.

O fluxo tem quatro atores. O cliente do remetente descobre o endpoint LNURL do destinatário a partir do perfil kind `0`, campos `lud06` ou `lud16`, ou de uma tag `zap` no evento que receberá o zap. Esse cliente então assina um evento de request de zap kind `9734` descrevendo o pagamento pretendido e o envia ao callback LNURL do destinatário, não aos relays. Do outro lado, o servidor LNURL do destinatário valida o request, devolve uma invoice Lightning cujo description hash compromete a string do request e, depois que o remetente paga, publica um recibo de zap kind `9735` no conjunto de relays pedido pelo remetente.

Um request de zap, kind `9734`, é um evento assinado que declara a intenção do pagamento. Os campos críticos são uma tag `p` com a pubkey do destinatário, uma tag `e` ou `a` opcional identificando o evento ou conteúdo endereçável que está sendo zapeado, uma tag `amount` em millisats e uma tag `relays` listando onde o recibo deve ser publicado. O `content` carrega uma mensagem opcional do remetente acompanhando o zap. Uma tag `k` registra o kind alvo para que consumidores filtrem zaps pelo tipo de conteúdo financiado.

```json
{
  "id": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "pubkey": "a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876",
  "created_at": 1745280000,
  "kind": 9734,
  "tags": [
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["amount", "21000"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol", "wss://relay.nostr.band"],
    ["k", "1"]
  ],
  "content": "great post",
  "sig": "ccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbcc"
}
```

O recibo de zap, kind `9735`, é publicado pelo servidor de carteira do destinatário depois da confirmação do pagamento. Ele não é assinado pelo remetente; é assinado pelo servidor de carteira usando a `nostrPubkey` anunciada pelo destinatário na response LNURL. Um recibo válido carrega o request de zap stringificado na tag `description`, a invoice paga na tag `bolt11` e uma tag `preimage` provando que a invoice foi liquidada.

```json
{
  "id": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "pubkey": "e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0",
  "created_at": 1745280060,
  "kind": 9735,
  "tags": [
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["P", "a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["bolt11", "lnbc210n1pj...bolt11invoicestring"],
    ["description", "{\"id\":\"c1d2e3f4...\",\"pubkey\":\"a5b4c3d2...\",\"kind\":9734,\"content\":\"great post\",\"tags\":[...]}"],
    ["preimage", "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"]
  ],
  "content": "",
  "sig": "ddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccdd"
}
```

A regra de validação é onde a NIP-57 ganha suas garantias de confiança. Um cliente que exibe um recibo kind `9735` como zap deve verificar quatro coisas: a assinatura do recibo corresponde à `nostrPubkey` anunciada na response LNURL do destinatário, o valor da invoice `bolt11` corresponde à tag `amount` no request embutido, o description hash da invoice compromete a string do request de zap e a `preimage` gera o `payment_hash` da invoice. Um recibo que falha em qualquer uma dessas checagens é apenas uma alegação de pagamento, não uma prova. Clientes que renderizam contagens agregadas de zap sem fazer essas checagens são trivialmente falsificáveis por um atacante que publique eventos kind `9735` forjados.

Zaps privados adicionam uma camada de confidencialidade por cima. Um remetente pode criptografar o `content` do request de zap para o destinatário e incluir uma tag `anon` no request externo, de modo que a rede de relays veja o alvo do pagamento mas não consiga ler a nota anexada. Alguns clientes dão um passo adicional e geram um keypair efêmero novo para o próprio request, então o recibo ainda prova que um pagamento aconteceu, mas o destinatário não consegue ligá-lo à pubkey de longa duração do remetente. Esse padrão de anonymous zap é mais forte que um private zap simples, em que a mensagem fica escondida, mas a chave do remetente ainda pode ser visível ao longo do caminho do request.

A NIP-57 também sustenta o sistema de metas de zap especificado na [NIP-75](/pt/topics/nip-75/). Uma meta é um evento kind `9041` que declara um valor alvo e um conjunto de relays onde recibos contam, e qualquer recibo de zap vinculado ao ID do evento da meta contribui para seu progresso. Clientes contabilizam o progresso somando os valores `bolt11` validados de eventos kind `9735` correspondentes. O [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) do [Amethyst](https://github.com/vitorpamplona/amethyst) nesta semana conecta metas à tela Live Activities da [NIP-53](/pt/topics/nip-53/) e renderiza um ranking de top zappers a partir desses mesmos recibos.

Zap splits são definidos em um apêndice do NIP. Um destinatário pode publicar um perfil kind `0` com múltiplas tags `zap`, cada uma com um peso, para que um único pagamento de zap seja dividido entre várias pubkeys de acordo com os pesos publicados. Criadores de conteúdo, colaboradores e destinatários de taxas de plataforma podem todos ser pagos atomicamente a partir de um único request de zap assinado pelo remetente. Diversos clientes, incluindo [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus) e [noStrudel](https://github.com/hzrd149/nostrudel), implementam split-paying end-to-end.

---

É isso por esta semana. Se você está construindo algo ou tem notícias para compartilhar, mande DM no Nostr ou nos encontre em [nostrcompass.org](https://nostrcompass.org).
