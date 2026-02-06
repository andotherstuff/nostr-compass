---
title: 'Nostr Compass #8'
date: 2026-02-04
translationOf: /en/newsletters/2026-02-04-newsletter.md
translationDate: 2026-02-04
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** rust-nostr entrega um grande redesign de API com 21 PRs reformulando a arquitetura do SDK. Nostria 3.0 lança com navegação em painel duplo, gerenciamento de listas e uma reformulação completa da UI. Vector adiciona aceleração SIMD alcançando speedups de 65x-184x e entrega suporte ao protocolo [Marmot](/pt/topics/marmot/) para mensagens de grupo criptografadas. Frostr traz assinatura de limiar para iOS via TestFlight. Damus implementa dicas de relay [NIP-19 (Entidades Codificadas em Bech32)](/pt/topics/nip-19/) para descoberta de conteúdo cross-relay. Primal Android adiciona criptografia NWC e exportações de transações de carteira. nostr-tools e NDK recebem melhorias de confiabilidade. NIP-82 (Aplicações de Software) expande para cobrir 98% das plataformas de dispositivos. O repositório de NIPs faz merge de suporte a hold invoice para [NIP-47 (Nostr Wallet Connect)](/pt/topics/nip-47/). Novas propostas de protocolo incluem NIP-74 para podcasting, NIP-DB para bancos de dados de eventos em navegador, e uma suíte TRUSTed Filters para curadoria descentralizada de conteúdo. Novos projetos incluem Instagram to Nostr v2 para migração de conteúdo, Pod21 lançando um marketplace descentralizado de impressão 3D, Clawstr introduzindo comunidades gerenciadas por agentes de IA, e Shosho e NosCall expandindo capacidades de streaming ao vivo e chamadas de vídeo.

## Notícias

### rust-nostr Entrega Grande Redesign de API

O SDK [rust-nostr](https://github.com/rust-nostr/nostr) passou por uma reformulação arquitetural significativa esta semana com 21 PRs mergeados introduzindo breaking changes em toda a biblioteca. O redesign afeta APIs centrais das quais a maioria dos desenvolvedores Rust depende.

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245) redesenha APIs de notificação, enquanto [PR #1244](https://github.com/rust-nostr/nostr/pull/1244) substitui `RelayNotification::Shutdown` por `RelayStatus::Shutdown` para tratamento de estado mais limpo. As APIs de signer agora se alinham com outros padrões do SDK via [PR #1243](https://github.com/rust-nostr/nostr/pull/1243). Métodos de Client e Relay receberam limpeza em [PR #1242](https://github.com/rust-nostr/nostr/pull/1242), e opções de cliente agora usam um padrão builder ([PR #1241](https://github.com/rust-nostr/nostr/pull/1241)).

APIs de envio de mensagens foram redesenhadas em [PR #1240](https://github.com/rust-nostr/nostr/pull/1240), cancelamento de subscrição REQ em [PR #1239](https://github.com/rust-nostr/nostr/pull/1239), e remoção de relay em [PR #1229](https://github.com/rust-nostr/nostr/pull/1229). Um [PR aberto #1246](https://github.com/rust-nostr/nostr/pull/1246) adiciona suporte para APIs bloqueantes para completar o redesign.

As mudanças trazem consistência ao SDK mas exigirão esforço de migração de projetos existentes. Desenvolvedores construindo sobre rust-nostr devem revisar o changelog cuidadosamente antes de atualizar.

### Instagram to Nostr v2 Permite Migração de Conteúdo

Uma nova ferramenta permite que criadores migrem seu conteúdo existente de plataformas centralizadas para o Nostr. [Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2) suporta importação do Instagram, TikTok, Twitter e Substack sem exigir acesso às chaves privadas do usuário.

A ferramenta aborda uma barreira comum de onboarding: usuários hesitantes em começar do zero em uma nova plataforma podem agora preservar seu histórico de conteúdo. Ela também suporta presentear contas Nostr para novos usuários ou propor conteúdo para contas existentes, tornando-a útil para ajudar outros na transição para o protocolo.

### Pod21: Rede Descentralizada de Impressão 3D

[Pod21](https://github.com/gobrrrme/Pod21) ([pod21.com](https://pod21.com)) conecta operadores de impressoras 3D com compradores usando Nostr para coordenação de marketplace. A plataforma inclui um bot de DM compatível com [NIP-17 (Mensagens Diretas Privadas)](/pt/topics/nip-17/) que lida com interações de marketplace, permitindo que compradores solicitem impressões e negociem com makers através de mensagens diretas criptografadas.

Makers listam sua capacidade e recursos de impressão; compradores navegam nas listagens e iniciam pedidos via o bot. A arquitetura segue um padrão similar a outras aplicações de comércio Nostr: descoberta baseada em relay, mensagens criptografadas para coordenação de pedidos, e Lightning para liquidação. Pod21 se junta a Ridestr e Shopstr como aplicações Nostr coordenando transações do mundo real através do protocolo.

### Clawstr: Rede Social de Agentes de IA

[Clawstr](https://github.com/clawstr/clawstr) lança como uma plataforma inspirada no Reddit onde agentes de IA criam e gerenciam comunidades no Nostr. A plataforma permite que agentes autônomos estabeleçam comunidades temáticas, curem conteúdo e interajam com usuários. Comunidades funcionam como subreddits mas com moderadores e curadores de IA guiando discussões. A arquitetura usa o protocolo aberto do Nostr para interações agente-para-agente e agente-para-humano, estabelecendo um novo modelo para formação de comunidades em mídias sociais descentralizadas.

## Lançamentos

### Ridestr v0.2.0: RoadFlare Release

[Ridestr](https://github.com/variablefate/ridestr) entregou [v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0), apelidada de "RoadFlare Release", introduzindo redes pessoais de compartilhamento de caronas. O recurso permite que passageiros adicionem motoristas favoritos a uma rede de confiança. Motoristas aprovam seguidores e compartilham localizações criptografadas, permitindo que passageiros vejam quando motoristas de confiança estão online e próximos. Solicitações de corrida vão diretamente para motoristas conhecidos.

A confiabilidade de pagamento melhorou com recuperação automática de escrow, melhor sincronização de carteira entre dispositivos, e processamento de pagamento mais rápido via polling progressivo. [PR #37](https://github.com/variablefate/ridestr/pull/37) adiciona a infraestrutura da Fase 5-6 suportando esses recursos. [v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1) seguiu com hotfixes para bugs de diálogo de pagamento e o fluxo de "Adicionar aos Favoritos" pós-corrida.

### Nostria 3.0

[Nostria](https://github.com/nostria-app/nostria), o cliente cross-platform de sondreb construído para escala global, entregou a versão 3.0 com uma reformulação completa da UI, novo logo e centenas de correções. O lançamento representa um ciclo de desenvolvimento intensivo de seis semanas.

Navegação em painel duplo é a maior mudança de UX, permitindo que usuários desktop reduzam troca de contexto ao navegar entre listas, detalhes e threads. Uma nova seção Home fornece uma visão geral de todos os recursos disponíveis, e todas as telas compartilham uma barra de ferramentas, layout e funcionalidade unificados.

Gerenciamento de listas é a atualização de recurso mais significativa, integrando-se em toda a aplicação. Usuários podem gerenciar listas de perfis e filtrar conteúdo em qualquer recurso: Streams, Music ou Feeds. Cansado de spam em threads? Filtre por favoritos para ver apenas suas respostas. Quick Zaps adiciona zapping com um toque com valores configuráveis. Copy/Screenshot gera screenshots para a área de transferência para compartilhar eventos em qualquer lugar. Muted Words agora filtra em campos de perfil (name, display_name, NIP-05), permitindo que usuários bloqueiem todos os perfis bridgeados com uma única palavra banida. Configurações se tornaram pesquisáveis para mudanças de configuração mais rápidas.

O lançamento adiciona renderização de solicitações de pagamento BOLT11 e BOLT12, seleção de tamanho de texto e fonte, e mensagens "Nota para Si Mesmo" na seção de Mensagens com renderização de conteúdo referenciado como artigos e eventos. O novo diálogo de Compartilhar permite compartilhamento rápido via email, websites ou mensagens diretas para múltiplos destinatários. Recursos adicionais incluem conjuntos de emoji personalizados, Interests (listas de hashtags como feeds dinâmicos), Bookmarks, Public Relay Feeds e personalização completa de menu incluindo qual opção o ícone do Nostria abre.

Disponível no Android, iOS, Windows e web em [nostria.app](https://www.nostria.app/).

### Applesauce v5.1.0

A suíte de bibliotecas [Applesauce](https://github.com/hzrd149/applesauce) de hzrd149 lançou v5.1.0 em todos os pacotes. [applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0) adiciona suporte para métodos `switch_relays` e `ping` em remote signers Nostr Connect, útil para gerenciar conexões de signer programaticamente. [applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0) introduz `loadAsyncMap` para carregamento async paralelo. [applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0) adiciona argumentos de padding para `useAction().run()`. [applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0) atualiza mapeamento de evento para store para lidar com strings diretamente sem exigir `onlyEvents`.

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) de fiatjaf alcançou [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) com correções de estabilidade de mattn. O lançamento previne panics quando URLs de mint carecem do separador `://`, valida erros de dateparser antes de usar valores de data e lida com casos extremos em parsing de tags de desafio AUTH. Essas correções defensivas tornam o CLI mais resiliente ao processar inputs malformados.

### Aegis v0.3.7

[Aegis](https://github.com/ZharlieW/Aegis), o signer desktop cross-platform, entregou [v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7) adicionando suporte a Nostr App Browser com assinatura [NIP-07 (Interface de Extensão de Navegador)](/pt/topics/nip-07/). O lançamento registra eventos de criptografia [NIP-04 (Mensagens Diretas Criptografadas)](/pt/topics/nip-04/) e [NIP-44 (Criptografia Versionada)](/pt/topics/nip-44/), permitindo que usuários rastreiem quais aplicações solicitam operações de criptografia. O segmento de navegador agora filtra por plataforma para mostrar apenas web apps.

### Bitchat v1.5.1 (iOS)

[Bitchat](https://github.com/permissionlesstech/bitchat), o aplicativo de mensagens com capacidade offline usando Nostr e mesh Bluetooth, lançou [v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1) com endurecimento de segurança iOS. [PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012) valida assinaturas de evento Nostr antes do processamento, rejeita giftwraps e pacotes incorporados inválidos, limita payloads superdimensionados e bloqueia IDs de remetente de anúncio BLE falsificados. [PR #998](https://github.com/permissionlesstech/bitchat/pull/998) corrige autenticação de mesh BLE iOS vinculando IDs de remetente a UUIDs de conexão, prevenindo spoofing de identidade na rede mesh. [PR #972](https://github.com/permissionlesstech/bitchat/pull/972) adiciona limitação de taxa de notificação para prevenir floods de descoberta de peer quando múltiplos dispositivos mesh estão próximos.

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app) lançou [v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495) adicionando suporte [NIP-47](/pt/topics/nip-47/) Nostr Wallet Connect via [PR #148](https://github.com/keychat-io/keychat-app/pull/148). Usuários agora podem conectar carteiras Lightning externas para pagamentos dentro do aplicativo de mensagens. O lançamento também adiciona notificações desktop macOS.

### Nostrmo v3.5.0

[Nostrmo](https://github.com/haorendashu/nostrmo), o cliente Flutter cross-platform, entregou [v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0) reformulando seu sistema de feed. A atualização substitui feeds fixos por alternativas personalizáveis: General Feed, Mentioned Feed e Relay Feed, cada um configurável através de novas páginas de edição. O lançamento implementa suporte ao modelo outbox para melhor roteamento de eventos e expande funcionalidade de relay local com limites de tamanho configuráveis e suporte a subscrição.

### Shosho v0.11.1

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), o aplicativo de streaming ao vivo para Nostr, lançou [v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1) com capacidades de gravação e VOD. A atualização adiciona indicadores de presença de sala mostrando quem está assistindo streams, conversas de chat com threads para melhor organização de discussão, e suporte Nostr Connect no iOS via [NIP-46](/pt/topics/nip-46/). Streamers agora podem salvar suas transmissões para visualização posterior enquanto mantêm interações de chat em tempo real com sua audiência.

### NosCall v0.5.0

[NosCall](https://github.com/sanah9/noscall), o aplicativo de chamadas de áudio e vídeo para Nostr, entregou [v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release) com grupos de contato para organizar chamadas por categoria, gerenciamento de relay para otimização de conexão, e configurações de servidor ICE configuráveis para melhor traversal de NAT. O lançamento também adiciona suporte a modo escuro. NosCall usa Nostr para sinalização e coordenação de chamadas, permitindo chamadas peer-to-peer sem servidores centralizados.

### diVine 1.0.4

[diVine](https://github.com/divinevideo/divine-mobile), o cliente de vídeos curtos em loop de rabble, lançou [1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4) como um alpha pré-lançamento Android antes de sua submissão na Zapstore. O lançamento foca em testar gerenciamento de chave Nostr, incluindo importação de nsec, assinatura remota [NIP-46 (Nostr Connect)](/pt/topics/nip-46/) com nsecBunker e Amber, e tratamento de URL nostrconnect://. A equipe está solicitando feedback sobre compatibilidade de relay e interoperabilidade de vídeo com outros clientes. [PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265) corrige tratamento de caminho de arquivo iOS que causava clipes de vídeo se tornarem inutilizáveis após atualizações do app armazenando caminhos relativos em vez de caminhos de container absolutos. [PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251) corrige problemas de navegação ao visualizar perfis de comentários.

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus) entregou [v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2) como um lançamento estável, consolidando as [correções NWC cobertas em edições anteriores](/pt/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---correcoes-nwc).

### Frostr Igloo iOS TestFlight

[Frostr](https://github.com/FROSTR-ORG) ([frostr.org](https://frostr.org/)) lançou [Igloo para iOS](https://github.com/FROSTR-ORG/igloo-ios) no [TestFlight](https://testflight.apple.com/join/72hjQe3J), expandindo assinatura de limiar para dispositivos Apple. Frostr usa assinaturas FROST (Flexible Round-Optimized Schnorr Threshold) para dividir chaves nsec em shares distribuídos entre dispositivos, permitindo assinatura k-de-n com tolerância a falhas. Usuários entrando em "modo demo" participam de um experimento de assinatura de limiar 2-de-2 ao vivo, demonstrando as capacidades de coordenação em tempo real do protocolo. O lançamento iOS se junta ao [Igloo para Android](https://github.com/FROSTR-ORG/igloo-android) (v0.1.2), que foi entregue em dezembro com suporte [NIP-55 (Android Signer)](/pt/topics/nip-55/) para solicitações de assinatura cross-app. Ambos os clientes móveis complementam o [Igloo desktop](https://github.com/FROSTR-ORG/igloo-desktop) e a extensão de navegador [Frost2x](https://github.com/FROSTR-ORG/frost2x).

## Atualizações de Projetos

### Damus Implementa Dicas de Relay NIP-19

[Damus](https://github.com/damus-io/damus) fez merge do [PR #3477](https://github.com/damus-io/damus/pull/3477), implementando consumo de dicas de relay [NIP-19](/pt/topics/nip-19/) para busca de eventos. O recurso permite visualizar notas em relays não presentes no pool configurado do usuário extraindo dicas de referências [NIP-10 (Reply Threads)](/pt/topics/nip-10/), [NIP-18 (Reposts)](/pt/topics/nip-18/) e NIP-19. A implementação usa conexões de relay efêmeras com limpeza por contagem de referência, evitando expansão permanente do pool de relay.

Correções adicionais incluem parsing de Lightning invoice ([PR #3566](https://github.com/damus-io/damus/pull/3566)), carregamento de visualização de carteira ([PR #3554](https://github.com/damus-io/damus/pull/3554)), timing de lista de relay ([PR #3553](https://github.com/damus-io/damus/pull/3553)), e preloading de perfil para reduzir "popping" visual ([PR #3550](https://github.com/damus-io/damus/pull/3550)). Um [draft PR #3590](https://github.com/damus-io/damus/pull/3590) mostra suporte a DM privado [NIP-17](/pt/topics/nip-17/) em progresso.

### Primal Android Entrega Criptografia NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) teve uma semana muito ativa com 18 PRs mergeados focados em infraestrutura de carteira. O app agora se integra com Spark, o protocolo Lightning auto-custodial da Lightspark. [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) adiciona suporte a criptografia NWC, enquanto [PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872) envia eventos de info NWC quando conexões são estabelecidas.

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870) permite exportação CSV para transações de carteira, útil para contabilidade e propósitos fiscais. [PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716) adiciona um alternador de conta local no Editor de Notas. Múltiplas correções de restauração de carteira ([PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876), [PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875), [PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873)) abordam casos extremos para usuários com configurações de carteira não-Spark.

### SDK TypeScript Marmot Adiciona Histórico de Mensagens

A implementação TypeScript do protocolo [Marmot](https://github.com/marmot-protocol/marmot) continua em desenvolvimento. [PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) por hzrd149 implementa persistência de histórico de mensagens com paginação para a aplicação de chat de referência, enquanto [PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39) melhora a ergonomia da biblioteca.

No lado Rust, [PR #161](https://github.com/marmot-protocol/mdk/pull/161) implementa tratamento de estado com retry para preservar contexto de mensagem em falhas, e [PR #164](https://github.com/marmot-protocol/mdk/pull/164) muda para std::sync::Mutex para evitar panics do tokio com SQLite. O backend whitenoise-rs adiciona [integração Amber](https://github.com/marmot-protocol/whitenoise-rs/pull/418) ([PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)), [atualiza para MDK e nostr-sdk 0.44](https://github.com/marmot-protocol/whitenoise-rs/pull/467) ([PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467)), e introduz streaming de notificação em tempo real via [PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460) com tipos de evento NewMessage e GroupInvite.

### HAVEN Adiciona Atualização Periódica de WoT

[HAVEN](https://github.com/bitvora/haven), o relay pessoal, fez merge do [PR #108](https://github.com/bitvora/haven/pull/108) adicionando atualização periódica de [Web of Trust](/pt/topics/web-of-trust/). O recurso garante que pontuações de confiança permaneçam atualizadas conforme os grafos sociais dos usuários evoluem, melhorando a precisão da filtragem de spam ao longo do tempo.

### nostr-tools

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), a biblioteca JavaScript principal, recebeu múltiplas melhorias esta semana. Commits incluem uma [correção para parsing de hashtag após quebras de linha](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5) em menções [NIP-27 (Referências em Notas de Texto)](/pt/topics/nip-27/), [poda automática de objetos de relay quebrados com rastreamento de inatividade](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2) para limpeza de conexão, [remoção de fila de mensagens](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638) para otimização de desempenho single-threaded, e [exportações de arquivos fonte](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139) para melhores imports TypeScript.

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk) entregou [beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0) com uma [correção para reconexão após ciclos de sleep/wake do dispositivo e tratamento de conexão obsoleta](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3), abordando problemas de confiabilidade para aplicações móveis.

### Notedeck

[Notedeck](https://github.com/damus-io/notedeck), o cliente desktop da equipe Damus, tem um [PR aberto #1279](https://github.com/damus-io/notedeck/pull/1279) adicionando um visualizador [NIP-34 (Colaboração Git)](/pt/topics/nip-34/). Isso permitiria navegar repositórios git, patches e issues publicados em relays Nostr diretamente dentro do cliente, tornando Notedeck um potencial front-end para fluxos de trabalho baseados em ngit.

### njump

[njump](https://github.com/fiatjaf/njump), o gateway web Nostr, adicionou suporte para dois tipos de evento [NIP-51 (Listas)](/pt/topics/nip-51/) via [PR #152](https://github.com/fiatjaf/njump/pull/152). O gateway agora renderiza kind:30000 Follow Sets, que são agrupamentos categorizados de usuários que clientes podem exibir em diferentes contextos, e kind:39089 Starter Packs, que são coleções de perfis curadas projetadas para compartilhamento e seguimento em grupo. Essas adições permitem que njump exiba listas curadas pela comunidade quando usuários compartilham links nevent.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android, corrigiu um bug prevenindo compartilhamento de vídeo da visualização do player ([PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)). A opção "Compartilhar vídeo" estava falhando em aparecer porque o parâmetro de conteúdo não estava sendo passado para o componente de botões de controle. Usuários agora podem compartilhar conteúdo de vídeo Nostr para outros apps diretamente do player. [PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693) corrige crashes de desserialização Jackson JSON que ocorriam ao analisar certos eventos malformados.

### Jumble

[Jumble](https://github.com/CodyTseng/jumble), o cliente web focado em navegação de feed de relay, adicionou uploads de arquivo de áudio via clipboard em [PR #743](https://github.com/CodyTseng/jumble/pull/743). Usuários agora podem colar arquivos de áudio diretamente no editor de post, que faz upload para servidores de mídia configurados e incorpora a URL na nota. O recurso espelha a funcionalidade de colar imagem existente.

### Flotilla

[Flotilla](https://github.com/coracle-social/flotilla), o cliente de comunidades [NIP-29 (Grupos Baseados em Relay)](/pt/topics/nip-29/) de hodlbod, entregou notificações via [PR #270](https://github.com/coracle-social/flotilla/pull/270). A atualização refatora o sistema de alertas de polling baseado em âncora para notificações pull locais para web e notificações push para mobile. A arquitetura implementa o padrão NIP-9a proposto (veja [PR #2194](https://github.com/nostr-protocol/nips/pull/2194) abaixo), onde usuários registram callbacks de webhook com relays e recebem payloads de evento criptografados quando filtros correspondem.

### Formstr

[Formstr](https://github.com/abh3po/nostr-forms), a aplicação de formulários nativa do Nostr, adicionou importação de formulário e suporte a formulário criptografado em [PR #422](https://github.com/abh3po/nostr-forms/pull/422). Usuários agora podem importar formulários existentes por meio de um link de resposta ou outras instâncias Formstr. O recurso de criptografia permite que criadores de formulário restrinjam respostas para que apenas destinatários designados possam ler submissões, útil para pesquisas coletando informações sensíveis.

### Pollerama

[Pollerama](https://github.com/abh3po/nostr-polls) ([pollerama.fun](https://pollerama.fun)), construído em [nostr-tools](https://github.com/nbd-wtf/nostr-tools), adicionou compartilhamento [NIP-17](/pt/topics/nip-17/) DM para enquetes via [PR #141](https://github.com/abh3po/nostr-polls/pull/141) e [PR #142](https://github.com/abh3po/nostr-polls/pull/142). Usuários agora podem compartilhar enquetes diretamente para contatos através de mensagens diretas criptografadas.

### Nostrability Schemata

[Nostrability schemata](https://github.com/nostrability/schemata), a coleção de esquemas de verificação JSON para eventos Nostr, adicionou cobertura [NIP-59 (Gift Wrap)](/pt/topics/nip-59/) via [PR #59](https://github.com/nostrability/schemata/pull/59). A atualização inclui esquemas para eventos kind 13 (seal) e kind 1059 (gift wrap), complementando a cobertura de esquema [NIP-17](/pt/topics/nip-17/) existente.

### Vector

[Vector](https://github.com/VectorPrivacy/Vector), o mensageiro desktop focado em privacidade usando [NIP-17](/pt/topics/nip-17/), [NIP-44](/pt/topics/nip-44/) e [NIP-59](/pt/topics/nip-59/) para criptografia com zero metadados, fez merge do [PR #39](https://github.com/VectorPrivacy/Vector/pull/39) introduzindo otimizações de desempenho aceleradas por SIMD. Codificação hex roda 65x mais rápido, geração de preview de imagem até 38x mais rápido, e buscas de mensagem 184x mais rápido via indexação de busca binária. O PR adiciona intrinsics ARM64 NEON para Apple Silicon e AVX2/SSE2 x86_64 com detecção em runtime para Windows e Linux. Uso de memória caiu com structs de mensagem reduzidas de 472 para 128 bytes e armazenamento de npub cortado em 99,6% através de interning.

Vector v0.3.0 (dezembro de 2025) integrou [MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk) para mensagens de grupo baseadas em protocolo MLS, trazendo grupos criptografados de ponta a ponta com forward secrecy para o cliente. Compartilhamento de arquivo MIP-04 agora lida com anexos imeta para grupos MLS, projetado para interoperabilidade com [White Noise](/pt/newsletters/2026-01-28-newsletter/#marmot-protocol-updates). O lançamento também introduziu uma plataforma Mini Apps com jogos multiplayer P2P baseados em WebXDC, uma loja de apps descentralizada chamada The Nexus, integração de carteira PIVX para pagamentos in-app, edição de mensagens com rastreamento de histórico completo, e redução de memória de 4x durante uploads de imagem.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado:**

- **[NIP-47: Suporte a Hold Invoice](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/pt/topics/nip-47/) agora suporta hold invoices, permitindo fluxos de pagamento avançados onde receptores devem explicitamente liquidar ou cancelar pagamentos. O PR adiciona três novos métodos RPC: `make_hold_invoice` cria um hold invoice usando uma preimage e hash de pagamento pré-gerados, `settle_hold_invoice` reivindica pagamento fornecendo a preimage original, e `cancel_hold_invoice` rejeita pagamento usando seu hash de pagamento. Uma nova notificação `hold_invoice_accepted` dispara quando um pagador bloqueia o pagamento. Isso permite casos de uso como conteúdo pay-to-unlock, sistemas de escrow de marketplace e gating de pagamento. Implementações já estão em andamento em [Alby Hub](https://github.com/getAlby/hub/pull/1298), [Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382) e [dart NDK](https://github.com/relaystr/ndk/pull/147).

- **[NIP-05: Requisito de Minúsculas](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (Verificação de Domínio)](/pt/topics/nip-05/) agora explicitamente exige minúsculas tanto para chaves públicas hex quanto para nomes locais no arquivo `nostr.json`. Isso estava implícito na spec mas não declarado, causando problemas de interoperabilidade quando algumas implementações usavam maiúsculas e minúsculas misturadas enquanto outras normalizavam para minúsculas. Clientes validando identificadores NIP-05 agora devem rejeitar quaisquer respostas `nostr.json` contendo caracteres maiúsculos em chaves ou nomes.

- **[NIP-73: Códigos de País](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (Geotags)](/pt/topics/nip-73/) agora suporta códigos de país ISO 3166 como alternativa a geohashes. Eventos podem incluir tags `["g", "US", "countryCode"]` para indicar localização em nível de país sem exigir coordenadas precisas. Isso permite filtragem e descoberta de conteúdo baseada em país para aplicações onde localização exata é desnecessária ou indesejável. O PR também adicionou um exemplo de geohash faltante à documentação da spec.

**PRs Abertos e Discussões:**

- **[NIP-82: Aplicações de Software](https://github.com/nostr-protocol/nips/pull/1336)** - franzap anunciou uma grande atualização para esta especificação draft, que define como aplicações de software são distribuídas via Nostr usando eventos kind 30063 de release. A atualização agora cobre aproximadamente 98% das plataformas de dispositivos globalmente, incluindo macOS, Linux, Windows, FreeBSD, ambientes WASM, extensões VS Code, extensões Chrome e Web Bundles/PWAs. A equipe está focando em seguida no suporte Android, PWA e iOS, convidando desenvolvedores a convergir neste padrão compartilhado. Zapstore planeja migrar para o novo formato nas próximas semanas.

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)** - Define eventos endereçáveis para shows de podcast (kind 30074) e episódios (kind 30075). Shows incluem metadados como título, descrição, categorias e imagens de capa. Episódios referenciam seu show pai e incluem URLs de enclosure, durações e marcadores de capítulo. A spec se integra com padrões de metadados Podcasting 2.0 e inclui tags de valor para monetização V4V (value-for-value) via Lightning. Plataformas como [transmit.fm](https://transmit.fm), uma plataforma de publicação de podcast nativa do Nostr, podem publicar diretamente para relays usando este formato, permitindo que podcasters distribuam conteúdo sem intermediários.

- **[NIP-FR: Notas Apenas para Amigos](https://github.com/nostr-protocol/nips/pull/2207)** - Propõe um mecanismo para publicar notas visíveis apenas para uma lista de amigos definida pelo usuário usando uma chave simétrica compartilhada chamada ViewKey. O autor criptografa notas (kind 2044) com a ViewKey usando NIP-44. A ViewKey em si é distribuída a cada amigo uma vez via [NIP-59 (Gift Wrap)](/pt/topics/nip-59/). Amigos que possuem a ViewKey podem descriptografar e ler as notas; todos os outros veem apenas texto cifrado. Quando o autor remove um amigo, a ViewKey é rotacionada: uma nova chave é gerada e redistribuída a todos os amigos restantes via gift wrap, garantindo que o amigo removido perde acesso a posts futuros. Esta abordagem separa criptografia de conteúdo (simétrica, eficiente) de distribuição de chaves (assimétrica, por amigo), mantendo o protocolo leve enquanto habilita um recurso de privacidade frequentemente solicitado.

- **[NIP-DB: Interface de Banco de Dados de Eventos Nostr para Navegador](https://nostrhub.io/e/1a451c1581888215ae5c311d36c8a7c7d9e5e81f1f4010de4afaf7fcbd553e90)** ([spec](https://github.com/hzrd149/nostr-bucket/blob/master/nip.md)) - Propõe uma interface padrão `window.nostrdb` para extensões de navegador que fornecem armazenamento local de eventos Nostr. A API inclui métodos para adicionar eventos, consultar por ID ou filtro, contar correspondências e assinar atualizações. Aplicações web podem usar esta interface para ler de eventos cacheados localmente sem fazer requisições de relay, reduzindo largura de banda e latência. A extensão de navegador [nostr-bucket](https://github.com/hzrd149/nostr-bucket) de hzrd149 fornece uma implementação de referência, injetando a interface em todas as abas do navegador. Uma [biblioteca polyfill](https://github.com/hzrd149/window.nostrdb.js) complementar implementa a mesma API usando IndexedDB para ambientes sem a extensão.

- **[TRUSTed Filters](https://nostrhub.io/e/237667820943d1c8bbe7ab7732623ae51b337f177776ece439d4a8be84708eb7)** - Uma suíte de cinco propostas relacionadas para curadoria descentralizada de conteúdo, construindo sobre o mesclado [PR #1534 Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534) de vitorpamplona. A especificação principal introduz eventos kind 17570 para declarar Preferências de Provedor de Confiança, permitindo que usuários especifiquem quais serviços eles confiam para filtragem e ranking de eventos. Provedores de confiança publicam assertions (kind 37571), estatísticas (kind 37572) e rankings (kind 37573) que clientes podem assinar. O sistema usa uma arquitetura de plugin com tags W/w para especificar tipos de filtro e transformações. Isso permite que operações computacionalmente caras como detecção de spam, scoring de reputação e ranking de conteúdo rodem em infraestrutura dedicada enquanto usuários mantêm controle sobre quais provedores eles confiam. A suíte inclui specs separadas para presets de filtro, rankings de usuário, eventos confiáveis e definições de plugin.

- **[NIP-9a: Notificações Push](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbod propõe um padrão para notificações push baseadas em relay usando eventos kind 30390 de registro. Usuários criam um registro contendo filtros para eventos que eles querem receber e uma URL de callback de webhook. O registro é criptografado para a pubkey do relay (do campo `self` do seu NIP-11). Quando eventos correspondentes ocorrem, relays fazem POST para o callback com o ID do evento (plaintext para deduplicação) e o evento em si (criptografado NIP-44 para o usuário). Esta arquitetura permite que relays enviem notificações push enquanto protegem conteúdo de evento de servidores push intermediários. O [PR #270](https://github.com/coracle-social/flotilla/pull/270) do Flotilla implementa este padrão.

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - Propõe um protocolo de trabalho contratual descentralizado com escrow usando eventos kind 33400. O sistema define três papéis: árbitros anunciam disponibilidade e termos, patrocinadores criam tarefas financiadas com Bitcoin em escrow, e agentes livres completam trabalho para reivindicar pagamento. Árbitros resolvem disputas quando necessário. O protocolo permite coordenação de trabalho freelance trustless onde fundos são bloqueados até que entregas sejam aceitas ou arbitragem conclua.

## Deep Dive de NIP: NIP-47 (Nostr Wallet Connect)

[NIP-47](/pt/topics/nip-47/) define Nostr Wallet Connect (NWC), um protocolo para controle remoto de carteira Lightning usando Nostr como camada de comunicação. Com a adição de suporte a hold invoice desta semana, NWC agora cobre toda a gama de operações Lightning.

O protocolo funciona através de uma troca simples. Uma aplicação de carteira publica um evento "wallet info" (kind 13194) descrevendo suas capacidades. Aplicações cliente enviam requisições criptografadas (kind 23194) pedindo à carteira para executar operações como pagar invoices, criar invoices ou verificar saldos. A carteira responde com resultados criptografados (kind 23195).

NWC usa criptografia [NIP-44](/pt/topics/nip-44/) entre cliente e carteira, com um par de chaves dedicado para operações de carteira, mantendo-o separado da identidade principal do usuário. Esta separação significa que comprometer uma conexão NWC não expõe a identidade Nostr do usuário.

**Métodos Suportados:**

A spec define métodos para operações Lightning principais: `pay_invoice` envia pagamentos, `make_invoice` gera invoices para recebimento, `lookup_invoice` verifica status de pagamento, `get_balance` retorna o saldo da carteira, e `list_transactions` fornece histórico de pagamentos. O recém-mergeado `pay_keysend` permite pagamentos sem invoices, e `hold_invoice` suporta pagamentos condicionais.

**Eventos de Exemplo:**

O serviço de carteira publica um evento info (kind 13194) anunciando suas capacidades:

```json
{
  "kind": 13194,
  "pubkey": "<wallet service pubkey>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

Um cliente envia uma requisição criptografada (kind 23194) para pagar um invoice:

```json
{
  "kind": 23194,
  "pubkey": "<client ephemeral pubkey from connection URI secret>",
  "content": "<NIP-44 encrypted: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<wallet service pubkey>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<client ephemeral key signature>"
}
```

O serviço de carteira responde (kind 23195) com o resultado do pagamento:

```json
{
  "kind": 23195,
  "pubkey": "<wallet service pubkey>",
  "content": "<NIP-44 encrypted: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<client ephemeral pubkey>"],
    ["e", "<request event id>"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

A tag `e` na resposta referencia a requisição original, permitindo que clientes correspondam respostas às suas requisições.

**Hold Invoices:**

O [PR #1913](https://github.com/nostr-protocol/nips/pull/1913) desta semana adicionou suporte a hold invoice, permitindo pagamentos estilo escrow. Diferente de invoices padrão onde o receptor imediatamente reivindica o pagamento liberando a preimage, hold invoices permitem que o receptor adie esta decisão. Quando um pagador envia para um hold invoice, fundos são bloqueados ao longo da rota de pagamento. O receptor então escolhe liquidar (liberar a preimage e reivindicar fundos) ou cancelar (rejeitar o pagamento, retornando fundos ao pagador). Se nenhuma ação ocorrer, o pagamento expira e fundos retornam automaticamente. O PR adiciona três métodos NWC: `make_hold_invoice`, `settle_hold_invoice` e `cancel_hold_invoice`, mais uma notificação `hold_invoice_accepted`. Este mecanismo alimenta aplicações como o escrow de compartilhamento de caronas do Ridestr e resolução de disputas de marketplace.

**Implementações Atuais:**

Principais carteiras suportam NWC: Zeus, Alby e Primal (a partir do [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) desta semana) todos implementam suporte do lado da carteira. No lado do cliente, Damus, Amethyst e a maioria dos principais clientes Nostr podem conectar a carteiras NWC para zapping e pagamentos.

O protocolo permite uma separação de responsabilidades: usuários podem rodar sua carteira em um dispositivo enquanto interagem com o Nostr de outro, com relays Nostr servindo como canal de comunicação. Esta arquitetura significa que clientes móveis não precisam manter fundos diretamente, melhorando a segurança ao manter infraestrutura de carteira separada de clientes sociais.

**Considerações de Segurança:**

Conexões NWC devem ser tratadas como sensíveis. Enquanto a criptografia protege o conteúdo das mensagens, a pubkey da carteira e o segredo de conexão devem ser guardados. Aplicações devem permitir que usuários revoguem conexões e definam limites de gastos. O protocolo suporta restrições de capacidade, então carteiras podem limitar quais operações uma conexão específica pode executar.

## Deep Dive de NIP: NIP-59 (Gift Wrap)

[NIP-59](/pt/topics/nip-59/) define um protocolo para encapsular qualquer evento Nostr em múltiplas camadas de criptografia, escondendo a identidade do remetente de relays e observadores. As propostas desta semana para notas apenas para amigos (NIP-FR) e notificações push (NIP-9a) ambas dependem de gift wrapping, tornando-o uma primitiva de privacidade fundamental que vale a pena entender.

**As Três Camadas:**

Gift wrapping usa três estruturas aninhadas:

1. **Rumor** (evento não assinado): O conteúdo original como um evento Nostr sem assinatura. O rumor não pode ser enviado diretamente para relays porque relays rejeitam eventos não assinados.

2. **Seal** (kind 13): O rumor é criptografado usando [NIP-44](/pt/topics/nip-44/) e colocado em um evento kind 13. O seal É assinado pela chave real do autor. Esta é a prova criptográfica de autoria.

3. **Gift Wrap** (kind 1059): O seal é criptografado e colocado em um evento kind 1059 assinado por um par de chaves aleatório de uso único. O gift wrap inclui uma tag `p` para roteamento ao destinatário.

**Um Equívoco Comum: Negabilidade**

A spec menciona que rumors não assinados fornecem "negabilidade", mas isso é enganoso. A camada seal É assinada pelo autor real. Quando o destinatário descriptografa o gift wrap e então o seal, eles têm prova criptográfica de quem enviou a mensagem. O destinatário poderia até construir uma prova de conhecimento zero revelando a identidade do remetente sem expor sua própria chave privada.

O que gift wrap realmente fornece é **privacidade do remetente para observadores**: relays e terceiros não podem determinar quem enviou a mensagem porque eles só veem o gift wrap assinado por uma chave aleatória. Mas o destinatário sempre sabe, e pode provar.

**Eventos de Exemplo:**

Aqui está a estrutura completa de três camadas da spec (enviando "Você vai na festa hoje à noite?"):

O rumor (não assinado, não pode ser publicado em relays):
```json
{
  "created_at": 1691518405,
  "content": "Are you going to the party tonight?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

O seal (kind 13, assinado pelo autor real, contém rumor criptografado):
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

O gift wrap (kind 1059, assinado por chave efêmera aleatória, contém seal criptografado):
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

Note: a `pubkey` do seal é o autor real (`611df01...`), enquanto a `pubkey` do gift wrap é uma chave de uso único aleatória (`18b1a75...`). Relays só veem o gift wrap, então eles não podem atribuir a mensagem ao autor real.

**O Que Cada Camada Protege:**

O rumor não é assinado e não pode ser publicado em relays diretamente. O seal é assinado pelo autor real e prova autoria para o destinatário. O gift wrap é assinado por uma chave de uso único aleatória, escondendo o autor real de relays e observadores. Apenas o destinatário pode descriptografar através de ambas as camadas para alcançar o conteúdo original e verificar a assinatura do autor no seal.

**Aplicações Atuais:**

[NIP-17 (Mensagens Diretas Privadas)](/pt/topics/nip-17/) usa gift wrap para DMs criptografadas, substituindo o esquema NIP-04 mais antigo. O proposto NIP-FR (notas apenas para amigos) usa gift wrapping para distribuir ViewKeys aos amigos, que então descriptografam notas cifradas com essas chaves. NIP-9a (notificações push) criptografa payloads de notificação usando princípios de gift wrap.

**Proteção de Metadados:**

Timestamps devem ser randomizados para frustrar análise de timing. Relays devem exigir AUTH antes de servir eventos kind 1059 e só servi-los para o destinatário marcado. Ao enviar para múltiplos destinatários, crie gift wraps separados para cada um.

---

É isso para esta semana. Construindo algo? Tem notícias para compartilhar? Quer que cubramos seu projeto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via DM NIP-17</a> ou nos encontre no Nostr.
