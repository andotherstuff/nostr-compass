---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** [Shopstr](https://github.com/shopstr-eng/shopstr) e [Milk Market](https://github.com/shopstr-eng/milk-market) adicionam superfícies MCP para comércio orientado por agentes, enquanto [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) e [strfry](https://github.com/hoytech/strfry) adicionam suporte a relay auth da [NIP-42](/pt/topics/nip-42/) (Authentication of Clients to Relays) e eventos protegidos em software de app, signer e relay. [Route96](https://github.com/v0l/route96) lança duas versões focadas em rotulagem de IA, filas de moderação, perceptual hashing e documentação de servidor legível por máquina. [Samizdat](https://github.com/satsdisco/samizdat), já disponível na web, lançou seu primeiro alpha para Android e depois adicionou suporte de signer da [NIP-55](/pt/topics/nip-55/) (Android Signer Application). [Formstr](https://github.com/formstr-hq/nostr-forms) adiciona cadastro via [NIP-49](/pt/topics/nip-49/) (Private Key Encryption), [Amethyst](https://github.com/vitorpamplona/amethyst) lança trabalho de resolução [NIP-05](/pt/topics/nip-05/) (Domain Verification) baseado em Namecoin, [Mostro](https://github.com/MostroP2P/mostro) lança a [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), e o repositório de NIPs faz merge da [NIP-91](/pt/topics/nip-91/) (AND Operator for Filters) e de orientações defensivas para a [NIP-66](/pt/topics/nip-66/) (Relay Discovery and Liveness Monitoring).

## Notícias

### Shopstr e Milk Market abrem superfícies MCP para comércio

[Shopstr](https://github.com/shopstr-eng/shopstr), o marketplace peer-to-peer com pagamentos Lightning e Cashu, mergeou o [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), adicionando um servidor MCP com autenticação por chave de API para gerenciamento de contas por agentes. A mudança adiciona `.well-known/agent.json` para descoberta por agentes, endpoints de onboarding e status do MCP, rotas de criação de pedidos e verificação de pagamento, ferramentas dedicadas de compra e leitura, e uma tela de configurações para chaves de API. O [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) estende isso com ações do lado do vendedor para mensagens, endereços, atualizações de pedido e seleção de especificação de produto. Uma correção de segurança no [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) substitui o hashing de chave de API com SHA-256 em uma única iteração por PBKDF2 com salt e 100.000 iterações.

Agentes podem ler anúncios da [NIP-99](/pt/topics/nip-99/) (Classified Listings) e seguir até o checkout usando os fluxos de pagamento já existentes da [NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect) e da [NIP-60](/pt/topics/nip-60/) (Cashu Wallet), sem fazer scraping de páginas nem reverse-engineering do comportamento do cliente.

[Milk Market](https://github.com/shopstr-eng/milk-market), um marketplace de alimentos em Nostr no [milk.market](https://milk.market), incorporou a mesma base de MCP e chaves de API no [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). O [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) adiciona pedidos por assinatura, mudanças de endereço de entrega após a compra e tratamento de checkout com múltiplos comerciantes e múltiplas moedas para Stripe e outros fluxos de pagamento em fiat. Um [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) posterior corrige um bug de inicialização do banco de dados no startup, em que a tabela de publicações falhadas em relays não era criada em instalações novas, causando erros 500 no primeiro carregamento. A interface voltada a agentes funciona com checkout Bitcoin-native no Shopstr ou checkout misto em fiat e Bitcoin no Milk Market.

### NIP-42 relay auth chega a bunker, signer e relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), um bunker [NIP-46](/pt/topics/nip-46/) (Nostr Connect) que conecta provedores OAuth à assinatura Nostr, adicionou login via [NIP-07](/pt/topics/nip-07/) (Browser Extension Signer), seleção automática de identidade única e limpeza de identidades deletadas ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Quando existe apenas uma identidade, o bunker agora a seleciona automaticamente em vez de exibir um prompt. Deletar uma identidade também remove suas atribuições e conexões pendentes. O [commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) adiciona um caminho de configuração `ALWAYS_ALLOWED_KINDS` para usuários atribuídos, com kind `30078` de dados específicos de app como valor padrão, para que identidades delegadas possam gravar em armazenamento específico do app sem aprovação por evento.

[Amber](https://github.com/greenart7c3/Amber), o principal signer [NIP-55](/pt/topics/nip-55/) para Android, lançou a [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) com quatro pre-releases ao longo da semana. O [PR #317](https://github.com/greenart7c3/Amber/pull/317) adiciona tratamento de autenticação de relay da [NIP-42](/pt/topics/nip-42/) para requisições kind `22242`. A implementação adiciona uma nova coluna no banco de dados para rastrear permissões específicas por relay, com um índice único em `(pkKey, type, kind, relay)`. Usuários veem uma tela dedicada de autenticação onde podem permitir ou negar por relay, ou em todos os relays com escopo curinga `*`, e persistir essa escolha. Permissões com curinga limpam todas as entradas específicas por relay de um kind. O [PR #318](https://github.com/greenart7c3/Amber/pull/318) complementa isso ao refatorar as telas de requisição multi-evento para exibir detalhes inline com cartões composable, em vez de navegar para uma tela separada. A release também atualiza os relays de perfil padrão, adiciona exibição de requisições em bottom sheet e corrige um crash em dispositivos MediaTek ao desabilitar o keystore StrongBox.

No lado do relay, o [strfry PR #156](https://github.com/hoytech/strfry/pull/156) implementa o tratamento da NIP-42 para eventos protegidos da [NIP-70](/pt/topics/nip-70/), e o [PR #176](https://github.com/hoytech/strfry/pull/176) rejeita reposts que incorporam eventos protegidos.

### Notedeck adiciona limites de relay da NIP-11 e recursos do Agentium

[Notedeck](https://github.com/damus-io/notedeck), o cliente desktop nativo da equipe do Damus, mergeou 14 PRs nesta semana. O [PR #1316](https://github.com/damus-io/notedeck/pull/1316) adiciona busca de limites de relay da [NIP-11](/pt/topics/nip-11/) (Relay Information Document), então todos os relays de outbox agora respeitam `max_message_length` e `max_subscriptions` do documento de informações do relay. A implementação inclui processamento em background, exponential backoff com jitter para retries de conexão e headers HTTP Accept customizados. O [PR #1312](https://github.com/damus-io/notedeck/pull/1312) corrige um bug em que DMs às vezes deixavam de carregar após a troca de conta, e o [PR #1333](https://github.com/damus-io/notedeck/pull/1333) adiciona um mecanismo de backoff à comunicação multicast com relays para evitar spam de broadcast em caso de erro.

O subsistema Agentium, a UI integrada de agente de programação do Notedeck, chamado internamente de "Dave", recebeu colagem de imagens da área de transferência, configurações nomeadas de execução que sincronizam entre dispositivos via eventos kind `31991` da [NIP-33](/pt/topics/nip-33/) (Parameterized Replaceable Events), um criador de git worktree e um seletor de modelo para escolher backends por sessão ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). O [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integra `egui_kittest` para testes headless de UI, e o [PR #1339](https://github.com/damus-io/notedeck/pull/1339) adiciona um cartão no dashboard para rastrear novas criações de listas de contatos por cliente. Um [PR #1314](https://github.com/damus-io/notedeck/pull/1314) ainda aberto porta a resolução Namecoin da NIP-05 do Amethyst para o Notedeck com buscas ElectrumX, roteamento Tor via SOCKS5 e integração com a barra de busca.

### diVine lança v1.0.6 com infraestrutura de testes E2E e importação NIP-49

[diVine](https://github.com/divinevideo/divine-mobile), o cliente de vídeos curtos em loop que restaura arquivos do Vine em [divine.video](https://divine.video), lançou a [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) com 127 PRs mergeados. A release adiciona importação de conta da [NIP-49](/pt/topics/nip-49/), suporte externo à [NIP-05](/pt/topics/nip-05/), tratamento de múltiplas contas, builds para macOS e Linux experimental, e uma biblioteca redesenhada de rascunhos e clips apoiada em armazenamento local.

No lado de engenharia, o [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) adiciona uma infraestrutura completa de testes de integração E2E usando Patrol para automação de UI nativa contra uma stack backend em Docker, relay, API, Blossom, Postgres, Redis e ClickHouse. Cinco testes da jornada de autenticação cobrem cadastro, verificação, redefinição de senha, expiração de sessão e refresh de token. O [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) muda o carregamento de vídeo de HLS-first para MP4 direto com fallback automático para HLS, reduzindo tempos de carregamento de 30 a 60 segundos para algo praticamente instantâneo. O [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) coloca em cache a resposta da API do feed inicial em SharedPreferences para exibição instantânea em cold start. O [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) força rótulos de conteúdo `ai-generated` a permanecerem ocultos nos feeds, e o [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) adiciona uma configuração de segurança para mostrar apenas vídeos hospedados pelo diVine. A migração do cache de perfil de Hive para Drift continua nos [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) e [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), substituindo cerca de 1.074 linhas de código Hive por DAOs em Drift.

### Vector v0.3.2 entrega sincronização negentropy da NIP-77 e melhorias de MLS

[Vector](https://github.com/VectorPrivacy/Vector), o mensageiro desktop focado em privacidade que usa criptografia de grupo MLS com a [NIP-17](/pt/topics/nip-17/) (Private Direct Messages) e criptografia da [NIP-44](/pt/topics/nip-44/) (Encrypted Payloads), lançou a [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). A principal mudança é a negentropy da NIP-77 para sincronização de grupos MLS ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), que recupera mensagens perdidas de forma muito mais rápida usando boot paralelo. A release também adiciona um motor de áudio reconstruído com suporte completo a Linux, spoilers de imagem com pré-visualizações borradas, hyperlinks clicáveis com rich link previews, notificações `@mention` com `@everyone` para admins de grupo, autocomplete de shortcode de emoji, silenciamento de grupos, toque para reagir em reações existentes e uploads de arquivo canceláveis. O Vector filtra explicitamente eventos de chat em grupo da NIP-17 ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), usando MLS exclusivamente para criptografia de grupo.

## Lançamentos

### Route96 v0.5.0 e v0.5.1

[Route96](https://github.com/v0l/route96), um servidor de mídia com suporte a Blossom e à [NIP-96](/pt/topics/nip-96/) (HTTP File Storage), lançou a [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) e a [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). A v0.5.0 adiciona rotulagem automatizada de IA, backfill retroativo para uploads sem rótulo, filas de moderação para arquivos sinalizados, rejeição de privacidade baseada em EXIF e tratamento de hashes banidos.

A v0.5.1 adiciona hashes perceptuais de imagem, locality-sensitive hashing para busca de imagens semelhantes, endpoints administrativos em lote e um [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) publicado descrevendo a superfície de API do servidor para Blossom e NIP-96 voltada a tooling de agentes. O [PR #58](https://github.com/v0l/route96/pull/58) move workers de background para tasks Tokio totalmente assíncronas, e o [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) adiciona backoff para evitar hot loops.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), um leitor e publicador de textos longos disponível em [samizdat.press](https://samizdat.press), lançou seu primeiro build Android na [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). O app abre em uma página Press curada com artigos longos no Nostr e navegação em abas inferiores entre Press, Feed, Saved e Write. O build Android adiciona armazenamento nativo de chaves usando criptografia do Android Keystore com desbloqueio biométrico, lida com URIs `nostr:` e deep links de `samizdat.press`, e oferece handoff para signer via seletor de apps do Android, Amber, Primal e outros, em vez de exigir importação direta de chave. Pull-to-refresh, tratamento de safe area em diferentes tamanhos de tela e integrações nativas de compartilhamento, clipboard, haptics e splash screen agora fazem parte do shell Android, e não do wrapper web.

O [commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) adiciona assinatura baseada em intent da [NIP-55](/pt/topics/nip-55/) para os fluxos Amber e Primal, e o [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) substitui um workaround de ponte em JavaScript por um plugin nativo Capacitor usando `startActivityForResult`. O app exige Android 7.0+ (API 24), é distribuído como APK de debug neste alpha e ainda não tem notificações push. Hoje a publicação depende de um app signer, enquanto o login com `nsec` cobre leitura local e acesso à conta.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), um app de calendário descentralizado com compartilhamento privado de eventos da [NIP-59](/pt/topics/nip-59/) (Gift Wrap) disponível em [calendar.formstr.app](https://calendar.formstr.app), lançou a [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) com o [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). A release estende o tratamento de eventos recorrentes da [NIP-52](/pt/topics/nip-52/) (Calendar Events), avançando além da base de evento único da v0.1.0. As mudanças subjacentes também tocam armazenamento local de eventos, tratamento de signer e plumbing de notificações no Android. Este é o segundo aplicativo ativo da organização Formstr após a migração de repositório no mês passado.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), a exchange peer-to-peer de Bitcoin construída sobre Nostr, lançou a [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). As correções de restauração de sessão de disputa ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) e de auto-close ([PR #606](https://github.com/MostroP2P/mostro/pull/606)) [cobertas na semana passada](/en/newsletters/2026-03-04-newsletter/) estão incluídas. Novidade nesta release: o [PR #625](https://github.com/MostroP2P/mostro/pull/625) adiciona um campo `days` a eventos de avaliação de usuário do kind `38384`, o [PR #612](https://github.com/MostroP2P/mostro/pull/612) adiciona expiração a esses eventos de avaliação, e o [PR #614](https://github.com/MostroP2P/mostro/pull/614) troca a expiração hardcoded de 24 horas de eventos de pedido por configurações de expiração definidas em configuração. O [PR #622](https://github.com/MostroP2P/mostro/pull/622) adiciona uma verificação de idempotência para evitar pagamentos duplicados de taxa de desenvolvimento.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), o cliente Flutter da exchange P2P Mostro, lançou a [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) com 11 novos recursos e 11 correções de bugs. A release adiciona renderização de multimídia criptografada no chat de disputa ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), auto-close da UI de disputa quando pedidos chegam a estado terminal ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), leitura de QR para importação de carteira NWC ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), traduções em francês e tratamento de notificações push via FCM. O [PR #496](https://github.com/MostroP2P/mobile/pull/496) corrige um bug de padding em assinaturas Schnorr ao fixar a dependência bip340 na v0.2.0.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), o cliente de mensagens ao estilo Telegram com suporte a Cashu, lançou a [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) focada em correções para desktop Linux: ícones de dock do AppImage, renderização de emoji, travamentos no menu de contexto e congelamentos na UI de resposta e cópia. A release também corrige problemas de upload de imagem e integração com npub.cash. O [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) elimina rebuilds desnecessários de UI ao remover um timer de polling de 3 segundos que forçava repaints glassmorphic sem fazer nada, e destrava a inicialização do login ao carregar o cache de eventos em paralelo, em vez de bloquear startup de relay, contatos e canais.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), um signer threshold FROST para Android com suporte à [NIP-55](/pt/topics/nip-55/) e à [NIP-46](/pt/topics/nip-46/), lançou a [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) e a [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). A v0.6.0 adiciona coordenação de descritores de carteira e UI de gerenciamento, fluxo de backup/restore com autenticação biométrica ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), recuperação de `nsec` a partir de threshold shares ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), geração cross-platform de frame QR animado via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)) e trilha de auditoria de assinatura com verificação de cadeia ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). A v0.6.1 troca a licença de AGPL-3.0 para MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), o gateway estático para visualizar conteúdo Nostr em [njump.me](https://njump.me), lançou a [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) com uma mudança incompatível no parsing de códigos `note1` e uma atualização da biblioteca Nostr subjacente.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), um app descentralizado de relato de eventos na estrada usando Nostr, lançou sua primeira demo na [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). O app exibe eventos rodoviários em um mapa usando vector tiles do openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), uma aplicação de e-bills com camada de transporte Nostr e relay dedicado em [bit.cr](https://www.bit.cr/), lançou a [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). O [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) adiciona os campos `payment_actions` e `bill_state` à API para estado de pagamento e aceitação, e o [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) corrige o tratamento de endereços de assinatura para signers anônimos.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), uma aplicação de chat construída sobre as bibliotecas .NET MLS e C# do protocolo Marmot, lançou a [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). A release adiciona suporte a signer externo para Amber e fluxos da [NIP-46](/pt/topics/nip-46/) ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), move a persistência do estado MLS para dentro do serviço MLS para eliminar perda de dados na janela de crash ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)) e publica builds para Windows, Linux e Android via um novo pipeline de CI.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), um copiloto de trading em Kotlin Multiplatform para Nostr, lançou a [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). A release empacota módulos KMP compartilhados para lógica de domínio, renderização de gráficos, autenticação e publicação em Nostr, suporte a uploads Blossom via [NIP-96](/pt/topics/nip-96/) e hooks de inferência de IA baseados em ONNX nos shells Desktop e Android. A arquitetura publicada também inclui um serviço de IA em FastAPI para análise de screenshots de gráficos, pipelines de treinamento de modelo e um risk engine que produz planos estruturados de trade com sizing e avisos. O login aceita tanto chaves `nsec` brutas quanto signers externos, e o fluxo de saída termina em publicação de eventos Nostr, e não apenas em análise local.

## Atualizações de Projetos

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), a alternativa ao Google Forms no Nostr, mergeou o [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), adicionando um fluxo de cadastro que usa chaves privadas criptografadas da [NIP-49](/pt/topics/nip-49/) (Private Key Encryption). Antes dessa mudança, usuários precisavam de uma extensão de navegador [NIP-07](/pt/topics/nip-07/) ou de colar um `nsec` bruto para usar o Formstr. O novo fluxo gera um par de chaves no lado do cliente, criptografa a chave privada com uma senha escolhida pelo usuário pelo esquema scrypt + XChaCha20-Poly1305 da NIP-49 e armazena a string `ncryptsec` resultante. Depois disso, usuários podem entrar novamente só com a senha, sem instalar uma extensão signer. O gerenciamento de chaves permanece no lado do cliente durante todo o processo.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android cheio de recursos, mergeou quatro PRs que entregam o trabalho de resolução [NIP-05](/pt/topics/nip-05/) apoiado em Namecoin que estava [aberto na semana passada](/en/newsletters/2026-03-04-newsletter/). O [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) adiciona verificação NIP-05 resistente à censura via ElectrumX para identificadores `.bit`, `d/` e `id/`. Quando o Amethyst detecta um desses sufixos em um campo NIP-05, ele consulta um servidor ElectrumX-NMC pelo histórico de transações do nome, analisa o script `NAME_UPDATE` da saída mais recente para extrair a pubkey Nostr e rejeita nomes mais antigos que 36.000 blocos, a janela de expiração do Namecoin. Conexões ElectrumX passam por SOCKS5 quando o Tor está ativado, com seleção dinâmica de servidor entre endpoints clearnet e `.onion`. Um cache LRU com TTL de uma hora evita consultas repetidas ao blockchain.

O [PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) corrige condições de corrida e problemas de corretude no resolver desse fluxo. O [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) permite que novos usuários importem uma lista de follows durante o cadastro a partir de identificadores NIP-05 comuns ou dos apoiados em Namecoin. O [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) adiciona configurações customizadas de servidor ElectrumX para que usuários escolham qual servidor fará suas consultas.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), uma biblioteca que fornece métodos auxiliares para armazenar eventos Nostr em IndexedDB, mergeou o [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) adicionando suporte a filtros de tag AND da [NIP-91](/pt/topics/nip-91/). A mudança adiciona semântica de interseção ao matching de filtros no lado do cliente, para que consultas em IndexedDB possam exigir todos os valores de tag listados, em vez de qualquer um deles. O [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) atualiza a biblioteca para a interface mais recente do NIP-DB, e um [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) posterior corrige um deadlock em subscribe e remove o nostr-tools como dependência de produção.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), um indexador Nostr archive-first com analytics em ClickHouse, mergeou o [PR #8](https://github.com/andotherstuff/pensieve/pull/8) adicionando enforcement de TTL de cache por entrada e coalescência de misses por chave para reduzir picos de CPU na API. Os endpoints de séries temporais mais caros, estatísticas de engajamento, atividade por hora e atividade por kind, agora usam TTLs de 10 minutos no servidor em vez de disparar tempestades sincronizadas de recomputação.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), o protocolo e stack de servidor para hospedagem descentralizada de mídia, mergeou duas atualizações de autorização do BUD-11. O [PR #91](https://github.com/hzrd149/blossom/pull/91) move a autorização opcional para seu próprio BUD e esclarece o papel das tags `x` e `server`. O [PR #93](https://github.com/hzrd149/blossom/pull/93) limpa o comportamento de autenticação por endpoint e formaliza o header `X-SHA-256` para verificação de upload. Os dois PRs consolidam a lógica de autenticação no BUD-11 e removem ambiguidades sobre hashing de requisições nos fluxos de upload, deleção e gerenciamento de mídia.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado:**

- **[NIP-91](/pt/topics/nip-91/) (AND Operator for Filters)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): Adiciona semântica de interseção para filtros de tags, permitindo que relays respondam a consultas que exigem todos os valores de tag listados, e não qualquer um deles. Isso reduz a pós-filtragem no lado do cliente e o consumo de banda em consultas pesadas em tags.

- **[NIP-66](/pt/topics/nip-66/) (Relay Discovery and Liveness Monitoring): Defensive Measures** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): Após o [trabalho de benchmark de outbox coberto na semana passada](/en/newsletters/2026-03-04-newsletter/), a spec agora adiciona avisos sobre caminhos de falha nos dados de monitoramento de relay. Clientes não devem exigir eventos de monitoramento kind `30166` para funcionar. Um monitor pode estar errado, desatualizado ou ser malicioso. Espera-se que clientes cruzem múltiplas fontes e evitem cortar grandes partes do grafo de relays de um usuário com base em um único feed.

- **[NIP-39](/pt/topics/nip-39/) (External Identities in Profiles): kind 10011 Registry Cleanup** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): Adiciona a referência ao kind `10011` diretamente na spec, alinhando-a com a implementação do Amethyst [coberta na semana passada](/en/newsletters/2026-03-04-newsletter/).

**PRs abertos e discussões:**

- **[NIP-70](/pt/topics/nip-70/) (Protected Events): Reject reposts that embed protected events** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): Se um relay aplica a NIP-70 ao evento original mas aceita reposts contendo o mesmo conteúdo, a tag `-` perde efeito prático. Este PR adiciona a regra de que relays também devem rejeitar reposts kind 6 e kind 16 de eventos protegidos. O [strfry PR #176](https://github.com/hoytech/strfry/pull/176) já implementa isso.

- **[NIP-71](/pt/topics/nip-71/) (Video Events): Multiple Audio Tracks** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): Adiciona tags `imeta` de áudio para trilhas alternativas, variantes de idioma e streams apenas de áudio. Um cliente pode manter um arquivo de vídeo estável enquanto troca o idioma do áudio, ou servir o áudio como faixa separada para conteúdo em estilo podcast.

- **[NIP-11](/pt/topics/nip-11/) (Relay Information Document) and [NIP-66](/pt/topics/nip-66/) Relay Attributes** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): Adiciona um campo estruturado `attributes` aos documentos de informação de relay, dando a clientes e ferramentas de descoberta metadados legíveis por máquina além da descrição em texto livre atual.

## NIP Deep Dive: NIP-49 (Private Key Encryption)

A [NIP-49](/pt/topics/nip-49/) define como um cliente criptografa uma chave privada com uma senha e codifica o resultado como uma string bech32 `ncryptsec`. O [Formstr](#formstr) usa a NIP-49 em seu novo fluxo de cadastro.

O formato não está ligado a um kind de evento dedicado. Um cliente começa com a chave privada secp256k1 bruta de 32 bytes, deriva uma chave simétrica a partir da senha do usuário com scrypt, criptografa a chave com XChaCha20-Poly1305 e então encapsula o resultado em uma string bech32 `ncryptsec`. Um flag de um byte registra se a chave já foi manipulada de forma insegura antes da criptografia.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

O evento JSON acima é um exemplo em nível de aplicação, não um requisito da NIP-49. O NIP padroniza o formato da chave criptografada. Um cliente pode armazenar o `ncryptsec` localmente, sincronizá-lo por meio de armazenamento específico do app ou exportá-lo como string de backup. Senhas são normalizadas para Unicode NFKC antes da derivação da chave, para que a mesma senha seja descriptografada de forma consistente entre clientes e plataformas.

O flag de segurança da chave, com um byte, tem três valores definidos: `0x00` significa que o histórico de tratamento da chave é desconhecido, `0x01` significa que a chave foi comprovadamente manipulada de forma insegura, por exemplo, colada como texto plano em um formulário web antes da criptografia, e `0x02` significa que a chave foi gerada e criptografada em um contexto seguro e nunca foi exposta. Clientes podem usar isso para exibir avisos ao importar chaves com histórico inseguro conhecido.

A NIP-49 protege chaves melhor do que um export simples de `nsec`, mas a criptografia só é tão forte quanto a senha e o custo scrypt configurado. Valores maiores de `LOG_N` tornam tentativas de adivinhação offline mais caras, mas também tornam operações legítimas de descriptografia mais lentas. A spec adverte contra publicar chaves criptografadas em relays públicos, já que atacantes se beneficiam de colecionar ciphertext para cracking offline. Para comparação, a assinatura remota da [NIP-46](/pt/topics/nip-46/) evita expor chaves por completo, e a assinatura Android da [NIP-55](/pt/topics/nip-55/) mantém chaves dentro de um app signer dedicado. A NIP-49 ocupa um papel diferente: backup criptografado portátil para usuários que gerenciam suas próprias chaves.

As implementações incluem o [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) para cadastro, o [Amber](https://github.com/greenart7c3/Amber) para backup e restore de `ncryptsec`, o [diVine v1.0.6](#divine-lanca-v106-com-infraestrutura-de-testes-e2e-e-importacao-nip-49) para importação de conta, o [Keep v0.6.0](#keep-v060) para exportação de FROST shares e ferramentas de gerenciamento de chaves como [nsec.app](https://nsec.app) e [Alby](https://github.com/getAlby/hub).

## NIP Deep Dive: NIP-70 (Protected Events)

A [NIP-70](/pt/topics/nip-70/) define eventos protegidos. Quando um evento carrega a tag `["-"]`, um relay deve rejeitá-lo a menos que exija autenticação da [NIP-42](/pt/topics/nip-42/) e que a pubkey autenticada corresponda ao autor do evento.

O fluxo de autenticação da NIP-42 funciona da seguinte forma: o relay envia um desafio `AUTH` contendo uma string aleatória, e o cliente responde com um evento kind `22242` assinado cujas tags incluem a URL do relay e o desafio. O relay verifica a assinatura e checa se a pubkey no evento de autenticação corresponde à pubkey do evento protegido que está sendo publicado. Se as pubkeys não corresponderem, o relay rejeita o evento com o prefixo de mensagem `restricted`.

O conteúdo do evento ainda pode ser público. A tag `-` controla apenas quem pode publicar o evento em um relay que respeita a tag. Isso cobre feeds semi-fechados da [NIP-29](/pt/topics/nip-29/) (Simple Groups), espaços de relay apenas para membros e outros contextos em que o autor quer limitar a redistribuição pelo grafo de relays. A NIP-70 é uma convenção de tag única, não um novo kind de evento, então qualquer kind existente pode carregar a tag `-`.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

Mesmo que um relay bloqueie a publicação de terceiros do evento original, alguém ainda pode republicar o conteúdo dentro de um repost. O [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) trata disso ao exigir que relays também rejeitem reposts kind 6 e kind 16 de eventos protegidos. O [strfry PR #156](https://github.com/hoytech/strfry/pull/156) adiciona tratamento de autenticação da NIP-42 para eventos protegidos, e o [strfry PR #176](https://github.com/hoytech/strfry/pull/176) bloqueia reposts que incorporam conteúdo protegido.

A NIP-70 controla o comportamento do relay. Um destinatário ainda pode copiar o conteúdo para outro lugar, e a spec diz isso explicitamente. A tag `-` dá aos relays um sinal legível por máquina para recusar republicação. Para comparação, a [NIP-62](/pt/topics/nip-62/) (Request to Vanish) pede que relays deletem dados depois do fato, enquanto a NIP-70 impede publicação não autorizada no momento da ingestão. As duas são complementares: um autor pode marcar eventos como protegidos para limitar a disseminação e, mais tarde, pedir deleção se quiser que o conteúdo seja removido dos relays que o aceitaram.

---

Isso é tudo por esta semana. Está construindo algo ou tem notícias para compartilhar? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Fale conosco por DM via [NIP-17](/pt/topics/nip-17/)</a> ou nos encontre no Nostr.
