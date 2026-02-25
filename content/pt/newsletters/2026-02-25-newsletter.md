---
title: 'Nostr Compass #11'
date: 2026-02-25
translationOf: /en/newsletters/2026-02-25-newsletter.md
translationDate: 2026-02-25
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) traz mensagens em tempo real e suporte ao assinador Amber com mais de 160 melhorias mergeadas. [diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) corrige problemas de reprodução de vídeo e adiciona eventos de visualização Kind 22236 para análises do criador. [Pika](https://github.com/sledtools/pika), [Ridestr](https://github.com/variablefate/ridestr) e [Unfiltered](https://github.com/dmcarrington/unfiltered) lançam atualizações. [FIPS](https://github.com/jmcorgan/fips) lança uma implementação Rust funcional de redes mesh nativas do Nostr. Notecrumbs recebe correções de estabilidade para pré-visualizações de links do damus.io. [ContextVM](https://contextvm.org) faz ponte entre o Nostr e o Model Context Protocol. Novos projetos incluem [Burrow](https://github.com/CentauriAgent/burrow) para mensagens criptografadas com MLS entre agentes de IA e humanos, e [Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) para gerenciamento de cofre e identidade baseado em navegador. Os deep dives cobrem NIP-55 para assinatura no Android e NIP-60 para sincronização de carteira Cashu.

## Notícias

### Melhorias de Estabilidade no Notecrumbs

[Notecrumbs](https://github.com/damus-io/notecrumbs), a API Nostr e servidor web que alimenta as pré-visualizações de links do damus.io, recebeu uma série de correções tratando problemas de confiabilidade.

Uma [correção de concorrência](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49) substituiu o mecanismo de deduplicação em voo por watch channels. Dois chamadores solicitando a mesma nota poderiam ambos se tornar buscadores, levando a um deadlock quando um completava antes que o outro se inscrevesse na notificação. Watch channels com operações atômicas garantem que apenas um buscador execute enquanto outros aguardam o resultado.

[Limitação de taxa](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17) implementa uma defesa em duas camadas contra martelo de relay. Quando usuários acessam repetidamente a mesma nota, o sistema agora faz debounce de requisições ao relay com uma janela de cooldown de 5 minutos. Essa proteção se estende a todos os tipos [NIP-19](/pt/topics/nip-19/) e feeds de perfil, prevenindo spam proporcional aos relays durante tráfego intenso.

[Melhorias de desempenho](https://github.com/damus-io/notecrumbs/commit/38670b3972b6) moveram buscas de dados secundários para tarefas tokio em background. As páginas agora renderizam instantaneamente com dados em cache em vez de bloquear em timeouts sequenciais de relay que poderiam somar até 7,5 segundos. Uma atualização para nostrdb 0.10.0 acompanhou essas correções.

### ContextVM: MCP Sobre Nostr

[ContextVM](https://contextvm.org) é um conjunto de ferramentas que faz ponte entre o Nostr e o [Model Context Protocol](https://modelcontextprotocol.io/) (MCP). Commits recentes introduziram a nova spec [CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/) habilitando pagamentos, e têm impulsionado melhorias no [SDK](https://github.com/ContextVM/sdk) ao longo de fevereiro.

O SDK fornece transportes cliente e servidor TypeScript para MCP sobre Nostr. Desenvolvedores podem expor servidores MCP através da rede Nostr e clientes podem se conectar a eles. Relays agem como um barramento de mensagens cego, apenas roteando eventos criptografados cegamente. Clientes sem suporte nativo ao Nostr se conectam através de uma camada de proxy. A biblioteca lida com gerenciamento de relay e assinatura criptográfica para autenticação de eventos. Funciona tanto em ambientes Node.js quanto de navegador.

[CVMI](https://github.com/ContextVM/cvmi) fornece uma CLI para descoberta de servidores e invocação de métodos. [Relatr](https://github.com/ContextVM/relatr) calcula pontuações de confiança personalizadas a partir da distância no grafo social combinada com validação de perfil.

ContextVM se posiciona como uma camada de ponte: servidores MCP existentes ganham interoperabilidade com Nostr enquanto mantêm seus transportes convencionais.

### White Noise Documenta Busca Descentralizada de Usuários

Um [post de blog de jgmontoya](https://blog.jgmontoya.com/2026/02/22/user-search.html) detalha como [White Noise](https://github.com/marmot-protocol/whitenoise) lida com a busca de usuários através da rede de relays descentralizada.

A distribuição de perfis cria o desafio: diferente de mensageiros centralizados com bancos de dados unificados, os perfis Nostr se espalham por dezenas de relays sem índice central. White Noise resolve isso através de uma arquitetura produtor-consumidor rodando em paralelo.

Um processo produtor expande continuamente o grafo social para fora a partir dos follows do usuário, buscando listas de follows em distâncias crescentes e enfileirando pubkeys descobertos para resolução de perfil. O consumidor resolve matches através de cinco camadas crescentemente caras: tabela de usuário local (mais rápido), perfis em cache de buscas anteriores, relays conectados, listas de relay de usuários por [NIP-65](/pt/topics/nip-65/) e consultas diretas a relays declarados pelo usuário (mais lento).

Buscas frias levam aproximadamente 3 segundos enquanto buscas quentes do cache caem para cerca de 10 milissegundos. Para novos usuários sem grafos sociais estabelecidos, o sistema injeta nós bootstrap bem conectados para garantir funcionalidade de busca. A participação em grupos fornece um sinal social implícito ao lado de follows explícitos.

Instrumentação provou ser crítica para otimização, observa o autor. Sem métricas, melhorias eram adivinhação.

### FIPS: Redes Mesh Nativas do Nostr

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System) é uma implementação Rust funcional de uma rede mesh auto-organizável que usa pares de chaves Nostr (secp256k1) como identidades de nó. A [documentação de design](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md) acompanha o código funcional.

O protocolo trata da independência de infraestrutura: nós se descobrem automaticamente sem servidores centrais ou autoridades de certificação. Uma árvore de cobertura fornece roteamento baseado em coordenadas enquanto filtros bloom propagam informações de alcançabilidade, deixando os nós tomarem decisões de encaminhamento com apenas conhecimento local. Agnosticismo de transporte significa que o mesmo protocolo funciona sobre UDP, Ethernet ou Bluetooth. Também suporta rádio LoRa ou qualquer meio capaz de datagramas.

Duas camadas protegem o tráfego. Link-layer encryption (padrão Noise IK) protege a comunicação salto por salto entre vizinhos com autenticação mútua e sigilo futuro. Session-layer encryption (padrão Noise XK) fornece proteção ponta a ponta contra roteadores intermediários, onde apenas o destino pode descriptografar a carga útil. Isso espelha como TLS protege o tráfego HTTP mesmo ao atravessar redes não confiáveis.

A arquitetura usa uma árvore de cobertura "greedy embedding" para roteamento. Cada nó recebe coordenadas baseadas em sua posição relativa à raiz da árvore e ao pai. Pacotes roteiam gananciamente em direção a coordenadas mais próximas do destino, com filtros bloom anunciando endpoints alcançáveis. Quando o roteamento ganancioso falha (mínimos locais), nós podem recorrer a caminhos baseados em árvore.

A implementação Rust já inclui transporte UDP com descoberta por filtro bloom. Trabalho futuro visa integração com relay Nostr para bootstrapping de pares.

## Lançamentos

Esta semana trouxe lançamentos através da infraestrutura de relay e aplicações cliente, com novos projetos também entrando no espaço.

### HAVEN v1.2.0

[HAVEN](https://github.com/bitvora/haven), o relay pessoal tudo-em-um reunindo quatro funções de relay com um servidor de mídia [Blossom](/pt/topics/blossom/), lançou [v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0). Este lançamento vai além do estágio RC [coberto na semana passada](/pt/newsletters/2026-02-18-newsletter/#haven-v120-rc3).

Suporte a múltiplos npubs permite que uma única instância HAVEN sirva várias identidades Nostr através de whitelisting, com nova funcionalidade de blacklist para controle de acesso. Um sistema de backup reescrito usa formato JSONL portátil, com um comando `haven restore` para importar notas de arquivos JSONL. Integração com armazenamento em nuvem adiciona flags `--to-cloud` e `--from-cloud` para gerenciamento de backup remoto.

Melhorias de [Web of Trust](/pt/topics/web-of-trust/) incluem níveis de profundidade configuráveis para cálculos de confiança e intervalos automáticos de atualização de 24 horas com otimização sem bloqueio reduzindo overhead de memória. Configuração de user-agent para requisições de relay, configurações de timeout do Blastr e exportação de dados para JSONL compactado completam o lançamento.

### White Noise v0.3.0

[White Noise](https://github.com/marmot-protocol/whitenoise), o app de mensagens criptografadas baseado em [MLS](/pt/topics/mls/) implementando o protocolo [Marmot](/pt/topics/marmot/), lançou [v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) com mais de 160 melhorias mergeadas.

Este lançamento traz mensagens em tempo real através de conexões de streaming em vez de polling, então mensagens chegam instantaneamente. Suporte ao Amber ([NIP-55](/pt/topics/nip-55/)) significa que chaves privadas nunca precisam tocar o app. Compartilhamento de imagem agora funciona com rastreamento de progresso de upload e placeholders blurhash durante o carregamento. Visualização em tela cheia suporta pinça para zoom.

Mensagens de grupo receberam melhorias de confiabilidade com listas de chat mostrando nomes de remetentes. A criptografia [MLS](/pt/topics/mls/) garante sigilo futuro. Busca de usuário se expande para fora dos follows até quatro graus de separação com resultados chegando em streaming conforme encontrados.

Uma mudança que quebra compatibilidade reseta todos os dados locais no upgrade devido a mudanças no protocolo Marmot e a mudança para armazenamento local criptografado. Usuários devem fazer backup das chaves nsec antes de atualizar.

### diVine 1.0.5

[diVine](https://github.com/divinevideo/divine-mobile), o cliente de vídeo de loop curto construído sobre arquivos Vine restaurados, lançou [1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) com extensas correções de reprodução de vídeo e um novo sistema de análises descentralizado.

Problemas de reprodução de vídeo dominaram as correções. Pausa fantasma está resolvida. Áudio duplo entre vídeos está corrigido. Flash preto entre miniaturas e primeiros quadros foi eliminado, e crashes de player descartado não ocorrem mais. Um player de vídeo em pool agora lida com o feed Home para reprodução consistente.

Eventos de visualização efêmeros Kind 22236 habilitam análises de criador e recomendações. O sistema rastreia fontes de tráfego (home, variantes de descoberta, perfil, compartilhamento e busca) junto com contagens de loop enquanto filtra auto-visualizações. Vazamentos de caminho de arquivo local em tags imeta de eventos Nostr são corrigidos com URLs Blossom canônicas construídas no lado do cliente por spec BUD-01.

Melhorias no assinador remoto [NIP-46](/pt/topics/nip-46/) incluem conexões de relay paralelizadas e suporte a URL de callback. Android reconecta conexões WebSocket ao retomar app após aprovação do assinador.

O Coracle também recebeu uma atualização esta semana.

### Coracle 0.6.30

[Coracle](https://github.com/coracle-social/coracle), o cliente Nostr baseado em web focado em gerenciamento de relay e moderação por [Web of Trust](/pt/topics/web-of-trust/), lançou [0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30) com suporte a miniaturas de vídeo, melhorando a navegação de mídia nos feeds.

Nostur trouxe novos recursos para iOS.

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public), o cliente Nostr para iOS, lançou [v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0) com uma nova seção de feed de Transmissões Ao Vivo e uma tela de Configurações redesenhada. GIFs agora podem hospedar em servidores de mídia Blossom, reduzindo dependência de serviços centralizados. Integração com Klipy GIFs fornece backup quando Tenor fica indisponível. Cabeçalhos de ano em conversas de DM e exibição de contagem de menções completam as mudanças voltadas ao usuário.

Ferramental para desenvolvedores e apps CLI também receberam atualizações esta semana.

### nak v0.18.5

[nak](https://github.com/fiatjaf/nak), o canivete suíço de linha de comando para Nostr de fiatjaf, lançou [v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5) com um novo subcomando `nak profile` para buscar e exibir perfis de usuário. O comando `git clone` agora suporta nomes [NIP-05](/pt/topics/nip-05/) em URIs `nostr://`, habilitando clonagem de repositório por identificadores legíveis por humanos.

Pika trouxe melhorias para seu mensageiro multiplataforma.

### Pika v0.5.3

[Pika](https://github.com/sledtools/pika), o mensageiro criptografado com [MLS](/pt/topics/mls/) para iOS, Android e desktop construído sobre o protocolo [Marmot](/pt/topics/marmot/), lançou [v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3). Commits recentes adicionam upload de arquivo ao app desktop. Suporte a arrastar e soltar mídia também chegou. Correções de deploy no Cloudflare Workers completam a atualização.

Pika usa um núcleo Rust que possui toda a lógica de negócio enquanto iOS (SwiftUI) e Android (Kotlin) agem como camadas finas de UI renderizando snapshots de estado. MDK (Marmot Development Kit) fornece a implementação MLS. O projeto nota status alfa e alerta contra uso para cargas de trabalho sensíveis.

Ridestr melhorou sua plataforma de carona descentralizada.

### Ridestr v0.2.6

[Ridestr](https://github.com/variablefate/ridestr), a plataforma de carona descentralizada com pagamentos Cashu, lançou [v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6). Este lançamento corrige problemas de acessibilidade TalkBack. Resolve bugs onde motoristas desapareciam da lista próxima ao trocar métodos de pagamento. Também corrige falhas de atualização de contagem quando motoristas ficavam offline.

O recurso "Enviar para Todos" agora é "Broadcast RoadFlare" com correções para falhas silenciosas em instalações frescas de motorista. Ridestr implementa escrow HTLC para pagamentos de carona sem confiança e sincronização de carteira [NIP-60](/pt/topics/nip-60/) entre dispositivos.

Unfiltered expandiu seu app de fotos para Android.

### Unfiltered v1.0.6

[Unfiltered](https://github.com/dmcarrington/unfiltered), o app de compartilhamento de fotos estilo Instagram para Android, lançou [v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6) com busca de usuário melhorada e reconexão automática de relay a cada 60 segundos.

Construído com Kotlin e Jetpack Compose, Unfiltered usa bindings rust-nostr e servidores compatíveis com Blossom para hospedagem de imagem. Integração com Amber ([NIP-55](/pt/topics/nip-55/)) lida com gerenciamento seguro de chaves. O app mostra posts de contas seguidas em ordem cronológica sem algoritmos ou anúncios.

Dois novos projetos de mensagens e assinatura também foram lançados esta semana.

### Burrow: Mensagens MLS para Agentes de IA

[Burrow](https://github.com/CentauriAgent/burrow) é um mensageiro implementando o protocolo [Marmot](/pt/topics/marmot/) para comunicação criptografada com MLS sem números de telefone ou servidores centralizados. Tanto usuários humanos quanto agentes de IA podem participar.

Um daemon CLI Rust puro com modo de saída JSONL lida com integração com sistemas automatizados. Um app Flutter multiplataforma cobre Android, iOS e Linux. Também suporta macOS e Windows. Anexos de mídia criptografam ao lado de mensagens, e WebRTC lida com chamadas de áudio e vídeo com servidores TURN configuráveis.

Burrow camada criptografia MLS sobre infraestrutura Nostr. Identidade usa pares de chaves Nostr (secp256k1) enquanto MLS KeyPackages publicam como eventos kind 443. Mensagens criptografam com [NIP-44](/pt/topics/nip-44/) como eventos kind 445, e convites de boas-vindas usam gift-wrapping [NIP-59](/pt/topics/nip-59/).

Integração com [OpenClaw](https://openclaw.ai) habilita participação de agente de IA com acesso completo a ferramentas. Listas de controle de acesso com registro de auditoria gerenciam permissões de contato e grupo. Essa combinação posiciona Burrow para cenários de mensagens agente-para-agente e agente-para-humano exigindo criptografia nível Signal sobre infraestrutura descentralizada.

Nostria Signer trouxe gerenciamento de identidade para navegadores.

### Extensão Nostria Signer

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) é uma extensão de navegador baseada em Chromium fornecendo gerenciamento de cofre e identidade para usuários Nostr.

Múltiplos cofres contendo múltiplas contas permitem usuários organizarem identidades para contextos diferentes. Internacionalização inclui suporte a idiomas RTL. Construído com Angular e TypeScript (79,2% do código), funciona tanto como extensão de navegador quanto Progressive Web App.

Nostria Signer implementa [NIP-07](/pt/topics/nip-07/) para assinatura de extensão de navegador, habilitando clientes Nostr baseados em web a solicitar assinaturas de eventos sem acessar chaves privadas diretamente. Migração automática de carteira lida com atualizações distribuídas através da Chrome Web Store. Usuários também podem fazer sideload da pasta `dist/extension`.

Desenvolvedores enfatizam o status experimental: usuários devem gerenciar suas próprias frases de recuperação secreta já que os desenvolvedores não podem restaurar acesso a chaves perdidas.

## Atualizações de Projetos

### Formstr Migra para Nova Organização

[Formstr](https://github.com/formstr-hq/nostr-forms), a alternativa ao Google Forms no Nostr, migrou seu repositório de `abh3po/nostr-forms` para a organização `formstr-hq`. Este beneficiário de subsídio OpenSats continua desenvolvimento no novo local.

### PRs Abertos Notáveis

Trabalho em progresso através de projetos Nostr:

- **Damus Outbox Model** ([PR #3602](https://github.com/damus-io/damus/pull/3602)): Plano de implementação para o modelo de relay gossip/outbox no iOS. Essa mudança arquitetural melhora entrega de mensagem publicando aos relays onde destinatários realmente leem.

- **Notedeck Cross-Platform Notifications** ([PR #1296](https://github.com/damus-io/notedeck/pull/1296)): Sistema de notificação nativo para o cliente desktop Damus cobrindo Android FCM, macOS e Linux.

- **NDK Cashu v3 Upgrade** ([PR #370](https://github.com/nostr-dev-kit/ndk/pull/370)): Atualiza a integração de carteira do Nostr Development Kit para cashu-ts v3.

- **Zeus Cashu Offline** ([PR #3742](https://github.com/ZeusLN/zeus/pull/3742)): Envio e recebimento de ecash offline para a carteira Lightning Zeus.

- **Shopstr Encrypted Digital Delivery** ([PR #231](https://github.com/shopstr-eng/shopstr/pull/231)): Adiciona entrega criptografada para bens digitais com suporte a peso dinâmico para itens físicos.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado Esta Semana:**

**[NIP-85 Service Provider Discoverability](https://github.com/nostr-protocol/nips/pull/2223)**: A spec [NIP-85](/pt/topics/nip-85/) agora inclui orientação sobre como clientes descobrem provedores de asserção confiáveis. Quando um cliente precisa de pontuações de [Web of Trust](/pt/topics/web-of-trust/) ou outras métricas computadas, pode consultar relays por anúncios kind 30085 de provedores que o usuário já segue ou confia.

**[NIP-29 Removes Unmanaged Groups](https://github.com/nostr-protocol/nips/pull/2229)**: A spec de chat de grupo [NIP-29](/pt/topics/nip-29/) descartou suporte para grupos não gerenciados (onde qualquer membro poderia adicionar outros). Todos os grupos NIP-29 agora exigem gerenciamento no lado do relay com papéis de admin explícitos, simplificando implementações e reduzindo vetores de spam.

**[NIP-11 Removes Deprecated Fields](https://github.com/nostr-protocol/nips/pull/2231)**: Documentos de informação de relay [NIP-11](/pt/topics/nip-11/) não incluem mais os campos depreciados `software` e `version`. Implementações devem remover esses de suas respostas.

**[NIP-39 Moves Identity Tags](https://github.com/nostr-protocol/nips/pull/2227)**: Reivindicações de identidade externa (tags `i` [NIP-39](/pt/topics/nip-39/) para GitHub, Twitter, etc.) moveram de perfis kind 0 para eventos dedicados kind 30382. Isso separa verificação de identidade de metadados de perfil.

**Progresso de NIPs de Agentes de IA:**

Quatro NIPs focados em IA continuam desenvolvimento ativo. Desde a [cobertura da semana passada](/pt/newsletters/2026-02-18-newsletter/#nips-de-agentes-de-ia-chegam):

**[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)** (atualizado 19 fev): Define identidade de agente com kind 4199 para definições de agente e kind 4201 para prompting ("nudges"). Agentes podem referenciar metadados de arquivo [NIP-94](/pt/topics/nip-94/) para descrições estendidas.

**[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)** (atualizado 18 fev): Padroniza mensagens conversacionais com sete kinds de evento efêmeros (25800-25806) para status, deltas de streaming, prompts e respostas. Também cobre chamadas de ferramenta, erros e cancelamento. Eventos "AI Info" kind 31340 permitem agentes anunciarem modelos e capacidades suportados.

**[NIP-AC: DVM Agent Coordination](https://github.com/nostr-protocol/nips/pull/2228)** (aberto 18 fev): Estende [NIP-90](/pt/topics/nip-90/) para fluxos de trabalho de agente autônomo. Adiciona heartbeats para descoberta de agente. Inclui revisões de trabalho para rastreamento de qualidade. Fornece escrow de dados para comprometimento de resultado, cadeias de fluxo de trabalho para pipelines de múltiplas etapas e licitação em enxame para seleção competitiva de provedor. Uma implementação de referência roda em 2020117.xyz.

**[NIP-AD: MCP Server Announcements](https://github.com/nostr-protocol/nips/pull/2221)** (aberto 12 fev): Padroniza anúncio de servidores Model Context Protocol e habilidades no Nostr. Já em uso na plataforma TENEX.

**Outros PRs Abertos:**

**[NIP-144: Service Authorization Protocol](https://github.com/nostr-protocol/nips/pull/2232)**: Define como clientes provam identidade e permissões a provedores de serviço no Nostr.

**[NIP-DC: Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)**: alexgleason propõe integrar Webxdc (aplicações web descentralizadas) com eventos Nostr.

## Deep Dive de NIP: NIP-55 (Android Signer Application)

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md) define como clientes Nostr Android solicitam operações criptográficas de aplicações assinadoras dedicadas. Com [White Noise v0.3.0](#white-noise-v030) e [Unfiltered v1.0.6](#unfiltered-v106) ambos adicionando suporte ao Amber esta semana, o protocolo de assinatura Android merece exame.

**Canais de Comunicação:**

NIP-55 habilita assinatura entre apps através de dois mecanismos. Intents fornecem aprovação manual do usuário com feedback visual para operações únicas. Content Resolvers habilitam assinatura automatizada quando usuários concedem permissões persistentes, deixando apps assinarem em background sem prompts repetidos.

Comunicação usa o esquema URI personalizado `nostrsigner:`. Um cliente inicia contato com:

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**Operações Suportadas:**

A spec define sete métodos criptográficos: assinatura de evento (`sign_event`) e recuperação de chave pública (`get_public_key`). Também oferece criptografia/descriptografia [NIP-04](/pt/topics/nip-04/) e criptografia/descriptografia [NIP-44](/pt/topics/nip-44/). Por fim, inclui descriptografia de evento zap (`decrypt_zap_event`).

**Modelo de Permissão:**

Clientes chamam `get_public_key` uma vez para estabelecer uma relação de confiança, recebendo o nome de pacote do assinador e pubkey do usuário. A spec determina que clientes salvem esses valores e nunca chamem `get_public_key` novamente, prevenindo ataques de fingerprinting.

Para requisições de assinatura, usuários podem aprovar uma vez ou conceder "lembrar minha escolha" para operações em background. Se usuários consistentemente rejeitam operações, o assinador retorna um status "rejeitado", prevenindo prompts repetidos.

**Implementações:**

[Amber](https://github.com/greenart7c3/amber) é o assinador NIP-55 primário para Android. Clientes suportando NIP-55 incluem [Amethyst](https://github.com/vitorpamplona/amethyst), [White Noise](#white-noise-v030) e [Unfiltered](#unfiltered-v106), entre outros. Aplicações web não podem receber respostas do assinador diretamente e devem usar URLs de callback ou operações de clipboard.

**Relação com Outros NIPs de Assinatura:**

NIP-55 complementa [NIP-07](/pt/topics/nip-07/) (extensões de navegador) e [NIP-46](/pt/topics/nip-46/) (assinatura remota sobre relays). Onde NIP-07 lida com navegadores desktop e NIP-46 lida com assinatura entre dispositivos, NIP-55 fornece integração nativa Android com latência mínima.

## Deep Dive de NIP: NIP-60 (Cashu Wallet)

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) define como carteiras ecash [Cashu](/pt/topics/cashu/) armazenam estado em relays Nostr, habilitando sincronização de carteira entre aplicações. Com [Ridestr v0.2.6](#ridestr-v026) usando NIP-60 para sincronização de carteira entre dispositivos, o protocolo merece exame.

**Kinds de Evento:**

NIP-60 usa quatro tipos de evento. O kind substituível 17375 armazena configuração de carteira incluindo URLs de mint e uma chave privada dedicada para receber pagamentos ecash P2PK. Eventos de token (kind 7375) contêm provas criptográficas não gastas, enquanto histórico de gastos (kind 7376) registra transações para transparência do usuário. Um kind opcional 7374 rastreia cotações de pagamento de mint.

**Arquitetura de Carteira:**

Estado de carteira vive em relays, tornando-o acessível através de aplicações. Um evento de carteira do usuário contém referências criptografadas a mints Cashu e uma chave privada específica da carteira separada da identidade Nostr do usuário. Essa separação importa: a chave da carteira lida com operações ecash enquanto a chave Nostr lida com funções sociais.

```json
{
  "kind": 17375,
  "content": "<config-carteira-criptografado-nip44>",
  "tags": [["d", "cashu-wallet"]]
}
```

**Gerenciamento de Prova:**

Provas Cashu são instrumentos ao portador. Uma vez gasta, uma prova se torna inválida. NIP-60 gerencia isso através de um mecanismo de rollover: ao gastar, clientes criam um novo evento de token com provas não gastas restantes e deletam o original via [NIP-09](/pt/topics/nip-09/). IDs de token destruídos vão em um campo `del` para rastreamento de estado.

Clientes devem periodicamente validar provas contra mints para detectar credenciais previamente gastas. Múltiplos eventos de token por mint são permitidos, e eventos de histórico de gastos ajudam usuários a rastrear transações mesmo sendo opcionais.

**Modelo de Segurança:**

Todos os dados sensíveis usam criptografia [NIP-44](/pt/topics/nip-44/). A chave privada da carteira nunca aparece em texto claro. Como relays armazenam blobs criptografados sem entender seus conteúdos, o estado da carteira permanece privado mesmo em relays não confiáveis.

**Implementações:**

Carteiras suportando NIP-60 incluem [Nutsack](https://github.com/gandlafbtc/nutsack) e [eNuts](https://github.com/cashubtc/eNuts). Clientes como [Ridestr](#ridestr-v026) usam NIP-60 para sincronização entre dispositivos, deixando usuários recarregarem no desktop e gastarem do mobile sem transferências manuais.

---

É isso por esta semana. Construindo algo ou tem novidades para compartilhar? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via [NIP-17](/pt/topics/nip-17/) DM</a> ou nos encontre no Nostr.
