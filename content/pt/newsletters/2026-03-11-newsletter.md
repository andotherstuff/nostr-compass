---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-03-11
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** [Shopstr](https://github.com/shopstr-eng/shopstr) e [Milk Market](https://github.com/shopstr-eng/milk-market) adicionam superfícies MCP para comércio orientado por agentes, enquanto [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) e [strfry](https://github.com/hoytech/strfry) adicionam relay-auth e suporte a eventos protegidos do [NIP-42](/pt/topics/nip-42/) (Autenticação de Clientes para Relays) em software de app, assinador e relay. [Route96](https://github.com/v0l/route96) lança duas versões em torno de rotulagem de IA, filas de moderação, hashing perceptual e documentação de servidor legível por máquina. [Samizdat](https://github.com/satsdisco/samizdat), já ativo na web, lançou seu primeiro alpha para Android e depois adicionou suporte de assinador do [NIP-55](/pt/topics/nip-55/) (Aplicativo Assinador para Android). [Formstr](https://github.com/formstr-hq/nostr-forms) adiciona cadastro por meio do [NIP-49](/pt/topics/nip-49/) (Criptografia de Chave Privada), [Amethyst](https://github.com/vitorpamplona/amethyst) lança trabalho de resolução do [NIP-05](/pt/topics/nip-05/) (Verificação de Domínio) baseado em Namecoin, [Mostro](https://github.com/MostroP2P/mostro) lança [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), e o repositório NIPs mergeia [NIP-91](/pt/topics/nip-91/) (Operador AND para Filtros) e orientações defensivas para o [NIP-66](/pt/topics/nip-66/) (Descoberta de Relays e Monitoramento de Disponibilidade).

## Notícias

### Shopstr e Milk Market Abrem Superfícies de Comércio MCP

[Shopstr](https://github.com/shopstr-eng/shopstr), o marketplace peer-to-peer com pagamentos Lightning e Cashu, mergeou o [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), adicionando um servidor MCP com autenticação por chave de API para gerenciamento de contas de agentes. A mudança adiciona `.well-known/agent.json` para descoberta de agentes, endpoints MCP de onboarding e status, rotas de criação de pedidos e verificação de pagamento, ferramentas dedicadas de compra e leitura, e uma tela de configurações para chaves de API. O [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) estende isso com ações do lado do vendedor para mensagens, endereços, atualizações de pedido e seleção de especificações de produto. Uma correção de segurança no [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) substitui o hashing de chave de API com SHA-256 de uma única iteração por PBKDF2 com salt em 100.000 iterações.

Agentes podem ler listagens do [NIP-99](/pt/topics/nip-99/) (Anúncios Classificados) e avançar pelo checkout usando os fluxos de pagamento existentes do [NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect) e do [NIP-60](/pt/topics/nip-60/) (Carteira Cashu), sem raspar páginas nem fazer engenharia reversa do comportamento do cliente.

[Milk Market](https://github.com/shopstr-eng/milk-market), um marketplace de alimentos no Nostr em [milk.market](https://milk.market), recebeu a mesma base de MCP e chave de API no [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). O [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) adiciona pedidos de assinatura, mudanças de endereço de entrega após a compra, e tratamento de checkout multi-merchant e multi-moeda para Stripe e outros fluxos de pagamento fiat. Um [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) de acompanhamento corrige um bug de inicialização do banco de dados em que a tabela de publicações com falha em relays não era criada em instalações novas, causando erros 500 no primeiro carregamento. A interface voltada a agentes funciona com checkout nativo em Bitcoin no Shopstr ou checkout misto em fiat e Bitcoin no Milk Market.

### Autenticação de Relay NIP-42 em Bunker, Assinador e Relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), um bunker [NIP-46](/pt/topics/nip-46/) (Nostr Connect) que faz a ponte entre provedores OAuth e assinatura Nostr, adicionou login [NIP-07](/pt/topics/nip-07/) (Assinador de Extensão de Navegador), seleção automática de identidade única e limpeza para identidades excluídas ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Quando existe apenas uma identidade, o bunker agora a seleciona automaticamente em vez de perguntar. Excluir uma identidade também remove suas atribuições e conexões pendentes. O [commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) adiciona um caminho de configuração `ALWAYS_ALLOWED_KINDS` para usuários atribuídos, com padrão no kind `30078` para dados específicos de app, para que identidades delegadas possam gravar em armazenamento específico de app sem aprovação por evento.

[Amber](https://github.com/greenart7c3/Amber), o principal assinador [NIP-55](/pt/topics/nip-55/) para Android, lançou [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) com quatro pre-releases ao longo da semana. O [PR #317](https://github.com/greenart7c3/Amber/pull/317) adiciona tratamento de autenticação de relay [NIP-42](/pt/topics/nip-42/) para requisições kind `22242`. A implementação adiciona uma nova coluna de banco de dados para rastrear permissões específicas de relay com um índice único em `(pkKey, type, kind, relay)`. Os usuários veem uma tela de auth dedicada onde podem permitir ou negar por relay ou em todos os relays com escopo curinga `*`, e persistir essa escolha. Permissões curinga limpam todas as entradas específicas de relay para um kind. O [PR #318](https://github.com/greenart7c3/Amber/pull/318) complementa isso refatorando telas de requisições multi-evento para exibir detalhes inline com cartões composable em vez de navegar para uma tela separada. A versão também atualiza os relays padrão de perfil, adiciona exibição de requisições em bottom sheet e corrige um crash em dispositivos MediaTek ao desabilitar o StrongBox keystore.

No lado do relay, o [strfry PR #156](https://github.com/hoytech/strfry/pull/156) implementa o tratamento NIP-42 para eventos protegidos do [NIP-70](/pt/topics/nip-70/) (Eventos Protegidos), e o [PR #176](https://github.com/hoytech/strfry/pull/176) rejeita reposts que incorporam eventos protegidos.

### Notedeck Adiciona Limites de Relay do NIP-11 e Recursos do Agentium

[Notedeck](https://github.com/damus-io/notedeck), o cliente desktop nativo da equipe do Damus, mergeou 14 PRs esta semana. O [PR #1316](https://github.com/damus-io/notedeck/pull/1316) adiciona busca de limitações de relay do [NIP-11](/pt/topics/nip-11/) (Documento de Informações do Relay), então todos os relays outbox agora respeitam `max_message_length` e `max_subscriptions` do documento de informações do relay. A implementação inclui processamento de jobs em background, exponential backoff com jitter para tentativas de reconexão, e headers HTTP Accept personalizados. O [PR #1312](https://github.com/damus-io/notedeck/pull/1312) corrige um bug em que DMs às vezes falhavam ao carregar após troca de conta, e o [PR #1333](https://github.com/damus-io/notedeck/pull/1333) adiciona um mecanismo de backoff à comunicação multicast com relays para evitar spam de broadcast em erros.

O subsistema Agentium (a UI de agente de programação embutida do Notedeck, internamente chamada de "Dave") recebeu colagem de imagem da área de transferência, configurações nomeadas de execução que sincronizam entre dispositivos via eventos kind `31991` ([NIP-33](/pt/topics/nip-33/) (Eventos Substituíveis Parametrizados)), um criador de git worktree e um seletor de modelo para escolher backends por sessão ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). O [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integra `egui_kittest` para testes headless de UI, e o [PR #1339](https://github.com/damus-io/notedeck/pull/1339) adiciona um cartão de dashboard rastreando novas criações de lista de contatos por cliente. Um [PR #1314](https://github.com/damus-io/notedeck/pull/1314) aberto porta para o Notedeck a resolução NIP-05 baseada em Namecoin do Amethyst com consultas ElectrumX, roteamento Tor via SOCKS5 e integração à barra de busca.

### diVine Lança v1.0.6 com Infraestrutura de Testes E2E e Importação NIP-49

[diVine](https://github.com/divinevideo/divine-mobile), o cliente de vídeo curto em loop que restaura arquivos do Vine em [divine.video](https://divine.video), lançou [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) com 127 PRs mergeados. A versão adiciona importação de conta [NIP-49](/pt/topics/nip-49/), suporte externo a [NIP-05](/pt/topics/nip-05/), tratamento de múltiplas contas, builds para macOS e Linux experimental, e uma biblioteca redesenhada de rascunhos e clipes baseada em armazenamento local.

No lado de engenharia, o [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) adiciona uma infraestrutura completa de testes de integração E2E usando Patrol para automação de UI nativa contra uma stack backend em Docker (relay, API, Blossom, Postgres, Redis, ClickHouse). Cinco testes de jornada de auth cobrem registro, verificação, redefinição de senha, expiração de sessão e refresh de token. O [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) muda o carregamento de vídeo de HLS-first para MP4 direto com fallback automático para HLS, reduzindo tempos de carregamento de 30-60 segundos para quase instantâneo. O [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) coloca em cache a resposta da API do feed inicial em SharedPreferences para exibição instantânea em cold start. O [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) aplica labels de conteúdo `ai-generated` como ocultas nos feeds, e o [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) adiciona uma configuração de segurança para mostrar apenas vídeos hospedados pelo diVine. A migração do cache de perfis de Hive para Drift continua pelos [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) e [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), substituindo cerca de 1.074 linhas de código Hive por DAOs Drift.

### Vector v0.3.2 Lança Sincronização Negentropy NIP-77 e Melhorias de MLS

[Vector](https://github.com/VectorPrivacy/Vector), um messenger desktop focado em privacidade que usa criptografia de grupo MLS com criptografia [NIP-17](/pt/topics/nip-17/) (Mensagens Diretas Privadas) e [NIP-44](/pt/topics/nip-44/) (Payloads Criptografados), lançou [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). A mudança principal é a negentropy NIP-77 para sincronização de grupos MLS ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), que recupera mensagens perdidas de forma significativamente mais rápida usando boot paralelo. A versão também adiciona um mecanismo de áudio reconstruído com suporte completo a Linux, spoilers de imagem com prévias borradas, hyperlinks clicáveis com rich link previews, pings `@mention` com `@everyone` para admins de grupo, autocomplete de shortcode de emoji, silenciamento de grupos, tocar para reagir em reações existentes e uploads de arquivos canceláveis. O Vector filtra explicitamente eventos de chat em grupo NIP-17 ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), usando MLS exclusivamente para criptografia de grupo.

## Lançamentos

### Route96 v0.5.0 e v0.5.1

[Route96](https://github.com/v0l/route96), um servidor de mídia com suporte a Blossom e [NIP-96](/pt/topics/nip-96/) (Armazenamento de Arquivos por HTTP), lançou [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) e [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). A v0.5.0 adiciona rotulagem automatizada por IA, backfill retroativo para uploads sem rótulo, filas de moderação para arquivos sinalizados, rejeição de privacidade baseada em EXIF e tratamento de hashes banidos.

A v0.5.1 adiciona hashes perceptuais de imagem, locality-sensitive hashing para busca de imagens similares, endpoints batch de admin, e um [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) publicado descrevendo a superfície de API Blossom e NIP-96 do servidor para ferramental de agentes. O [PR #58](https://github.com/v0l/route96/pull/58) move workers de background para tarefas Tokio totalmente assíncronas, e o [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) adiciona backoff para evitar hot loops.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), um leitor e publicador de textos long-form disponível em [samizdat.press](https://samizdat.press), lançou seu primeiro build Android em [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). O app abre em uma página Press curada de artigos long-form do Nostr com navegação por abas inferiores entre as visões Press, Feed, Saved e Write. O build Android adiciona armazenamento nativo de chaves por criptografia Android Keystore com desbloqueio biométrico, lida com URIs `nostr:` e deep links `samizdat.press`, e suporta handoff de assinador pelo seletor de apps do Android (Amber, Primal etc.) em vez de exigir importação direta de chave. Pull-to-refresh, tratamento de safe area em vários tamanhos de tela, e integrações nativas de compartilhamento, clipboard, haptics e splash screen agora fazem parte do shell Android, não do wrapper web.

O [commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) adiciona assinatura [NIP-55](/pt/topics/nip-55/) baseada em intent para fluxos Amber e Primal, e o [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) substitui uma solução provisória com bridge JavaScript por um plugin nativo do Capacitor usando `startActivityForResult`. O app exige Android 7.0+ (API 24), é distribuído como APK de debug neste alpha, e ainda não tem push notifications. A publicação atualmente depende de um app assinador, enquanto login com `nsec` cobre leitura local e acesso à conta.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), um app de calendário descentralizado com compartilhamento privado de eventos [NIP-59](/pt/topics/nip-59/) (Gift Wrap) disponível em [calendar.formstr.app](https://calendar.formstr.app), lançou [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) com o [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). A versão estende o tratamento de eventos recorrentes do [NIP-52](/pt/topics/nip-52/) (Eventos de Calendário), indo além da base de evento único da v0.1.0. As mudanças subjacentes também tocam armazenamento local de eventos, tratamento de assinador e plumbing de notificações no Android. Este é o segundo aplicativo ativo da organização Formstr após a migração de repositório no mês passado.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), a exchange peer-to-peer de Bitcoin construída sobre Nostr, lançou [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). As correções de restauração de sessão de disputa ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) e fechamento automático ([PR #606](https://github.com/MostroP2P/mostro/pull/606)) [cobertas na semana passada](/pt/newsletters/2026-03-04-newsletter/) estão incluídas. Novidade nesta versão: o [PR #625](https://github.com/MostroP2P/mostro/pull/625) adiciona um campo `days` a eventos de rating de usuário do kind `38384`, o [PR #612](https://github.com/MostroP2P/mostro/pull/612) adiciona expiração a esses eventos de rating, e o [PR #614](https://github.com/MostroP2P/mostro/pull/614) muda eventos de ordem para as configurações de expiração definidas em vez de uma janela hardcoded de 24 horas. O [PR #622](https://github.com/MostroP2P/mostro/pull/622) adiciona uma verificação de idempotência para impedir pagamentos duplicados de taxa de desenvolvimento.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), o cliente Flutter para a exchange P2P Mostro, lançou [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) com 11 novos recursos e 11 correções de bugs. A versão adiciona renderização de multimídia criptografada no chat de disputa ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), fechamento automático da UI de disputa quando ordens chegam a estado terminal ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), leitura de QR para importação de carteira NWC ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), traduções em francês e tratamento de push notifications FCM. O [PR #496](https://github.com/MostroP2P/mobile/pull/496) corrige um bug de padding em assinatura Schnorr ao fixar a dependência bip340 na v0.2.0.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), o cliente de mensagens estilo Telegram com suporte a Cashu, lançou [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) focado em correções para desktop Linux: ícones de dock do AppImage, renderização de emoji, travamentos de menu de contexto e travamentos da UI de responder/copiar. A versão também corrige problemas de upload de imagem e integração com npub.cash. O [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) elimina reconstruções desnecessárias da UI ao remover um timer de polling de 3 segundos que forçava repaints glassmorphic sem fazer nada, e destrava a inicialização de login ao carregar o cache de eventos em paralelo em vez de bloquear a inicialização de relay, contatos e canais.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), um assinador FROST threshold para Android com suporte a [NIP-55](/pt/topics/nip-55/) e [NIP-46](/pt/topics/nip-46/), lançou [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) e [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). A v0.6.0 adiciona coordenação de descritores de carteira e UI de gerenciamento, um fluxo de backup/restauração com autenticação biométrica ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), recuperação de nsec a partir de threshold shares ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), geração de frames QR animados cross-platform via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)), e uma trilha de auditoria de assinatura com verificação em cadeia ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). A v0.6.1 muda a licença de AGPL-3.0 para MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), o gateway estático para visualizar conteúdo Nostr em [njump.me](https://njump.me), lançou [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) com uma mudança incompatível no parsing de códigos `note1` e uma atualização da biblioteca nostr subjacente.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), um aplicativo descentralizado de relatórios de eventos rodoviários usando Nostr, lançou sua versão demo inicial [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). O app exibe eventos rodoviários em um mapa usando vector tiles do openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), um aplicativo de e-bills com camada de transporte Nostr e relay dedicado em [bit.cr](https://www.bit.cr/), lançou [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). O [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) adiciona campos `payment_actions` e `bill_state` à API para estado de pagamento e aceitação, e o [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) corrige o tratamento do endereço de assinatura para assinadores anônimos.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), um aplicativo de chat construído sobre as bibliotecas .NET MLS e C# do protocolo Marmot, lançou [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). A versão adiciona suporte a assinadores externos para fluxos Amber e [NIP-46](/pt/topics/nip-46/) ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), move a persistência de estado MLS para dentro do serviço MLS para eliminar perda de dados em janelas de crash ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), e publica builds para Windows, Linux e Android por meio de uma nova pipeline de CI.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), um copiloto de trading em Kotlin Multiplatform para Nostr, lançou [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). A versão empacota módulos KMP compartilhados para lógica de domínio, renderização de gráficos, autenticação e publicação Nostr, suporte a upload Blossom [NIP-96](/pt/topics/nip-96/) e hooks de inferência de IA baseados em ONNX em shells Desktop e Android. A arquitetura publicada também inclui um serviço FastAPI de IA para análise de screenshots de gráficos, pipelines de treinamento de modelos e um motor de risco que produz planos de trade estruturados com dimensionamento e alertas. O login suporta tanto chaves `nsec` brutas quanto assinadores externos, e o fluxo de saída termina em publicação de eventos Nostr em vez de análise apenas local.

## Atualizações de Projetos

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), a alternativa ao Google Forms no Nostr, mergeou o [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), adicionando um fluxo de cadastro usando chaves privadas criptografadas do [NIP-49](/pt/topics/nip-49/) (Criptografia de Chave Privada). Antes dessa mudança, os usuários precisavam de uma extensão de navegador [NIP-07](/pt/topics/nip-07/) ou de colar um `nsec` bruto para usar o Formstr. O novo fluxo gera um par de chaves no cliente, criptografa a chave privada com uma senha escolhida pelo usuário por meio do esquema scrypt + XChaCha20-Poly1305 do NIP-49, e armazena a string `ncryptsec` resultante. Depois, os usuários podem entrar novamente com sua senha sem instalar uma extensão de assinador. O gerenciamento de chaves permanece no cliente o tempo todo.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android rico em recursos, mergeou quatro PRs que entregam o trabalho de resolução do [NIP-05](/pt/topics/nip-05/) baseado em Namecoin que estava [aberto na semana passada](/pt/newsletters/2026-03-04-newsletter/). O [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) adiciona verificação NIP-05 resistente à censura via ElectrumX para identificadores `.bit`, `d/` e `id/`. Quando o Amethyst detecta um desses sufixos em um campo NIP-05, ele consulta um servidor ElectrumX-NMC pelo histórico de transações do nome, faz parsing do script `NAME_UPDATE` da saída mais recente para extrair a pubkey Nostr, e rejeita nomes com mais de 36.000 blocos (janela de expiração do Namecoin). Conexões ElectrumX passam por SOCKS5 quando Tor está habilitado, com seleção dinâmica de servidor entre endpoints clearnet e `.onion`. Um cache LRU com TTL de uma hora impede consultas repetidas à blockchain.

O [PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) corrige condições de corrida e a correção do resolver nesse fluxo. O [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) permite que novos usuários importem uma lista de follows durante o cadastro a partir de identificadores NIP-05 comuns ou baseados em Namecoin. O [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) adiciona configurações personalizadas de servidor ElectrumX para que usuários escolham qual servidor realiza suas consultas.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), uma biblioteca que fornece métodos auxiliares para armazenar eventos Nostr no IndexedDB, mergeou o [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) adicionando suporte a filtros de tag AND do [NIP-91](/pt/topics/nip-91/). A mudança adiciona semântica de interseção ao matching de filtros no lado do cliente, para que consultas IndexedDB possam exigir todos os valores de tag listados em vez de apenas um deles. O [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) atualiza a biblioteca para a interface mais recente do NIP-DB, e um [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) de acompanhamento corrige um deadlock de subscribe e remove nostr-tools como dependência de produção.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), um indexador Nostr archive-first com analytics em ClickHouse, mergeou o [PR #8](https://github.com/andotherstuff/pensieve/pull/8) adicionando enforcement de TTL de cache por entrada e coalescência de misses por chave para reduzir picos de CPU da API. Os endpoints de séries temporais de maior custo (estatísticas de engajamento, atividade por hora, atividade por kind) agora usam TTLs no servidor de 10 minutos em vez de disparar tempestades de recomputação sincronizadas.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), o protocolo e stack de servidor de hospedagem de mídia descentralizada, mergeou duas atualizações de autorização do BUD-11. O [PR #91](https://github.com/hzrd149/blossom/pull/91) move a autorização opcional para seu próprio BUD e esclarece o papel das tags `x` e `server`. O [PR #93](https://github.com/hzrd149/blossom/pull/93) limpa o comportamento de auth específico por endpoint e formaliza o header `X-SHA-256` para verificação de upload. Os dois PRs consolidam a lógica de auth no BUD-11 e removem ambiguidades em torno do hashing de requisição para fluxos de upload, exclusão e gerenciamento de mídia.

## Atualizações de NIP

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado:**

- **[NIP-91](/pt/topics/nip-91/) (Operador AND para Filtros)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): Adiciona semântica de interseção para filtros de tag, permitindo que relays respondam a consultas que exigem todos os valores de tag listados em vez de qualquer um deles. Reduz filtragem pós-processamento no lado do cliente e largura de banda em consultas pesadas de tags.

- **[NIP-66](/pt/topics/nip-66/) (Descoberta de Relays e Monitoramento de Disponibilidade): Medidas Defensivas** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): Seguindo o [trabalho de benchmark de outbox coberto na semana passada](/pt/newsletters/2026-03-04-newsletter/), a especificação agora adiciona alertas sobre caminhos problemáticos para dados de monitoramento de relay. Clientes não devem exigir eventos de monitoramento kind `30166` para funcionar. Um monitor pode estar errado, desatualizado ou ser malicioso. Espera-se que clientes cruzem fontes e evitem cortar grandes partes do grafo de relays de um usuário com base em um único feed.

- **[NIP-39](/pt/topics/nip-39/) (Identidades Externas em Perfis): Limpeza do Registro kind 10011** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): Adiciona a referência ao kind `10011` diretamente à especificação, alinhando-se com a implementação do Amethyst [coberta na semana passada](/pt/newsletters/2026-03-04-newsletter/).

**PRs abertos e discussões:**

- **[NIP-70](/pt/topics/nip-70/) (Eventos Protegidos): Rejeitar reposts que incorporam eventos protegidos** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): Se um relay aplica o NIP-70 ao evento original, mas aceita reposts carregando o mesmo conteúdo, a tag `-` não tem efeito prático. Este PR adiciona a regra de que relays também devem rejeitar reposts kind 6 e kind 16 de eventos protegidos. O [strfry PR #176](https://github.com/hoytech/strfry/pull/176) já implementa isso.

- **[NIP-71](/pt/topics/nip-71/) (Eventos de Vídeo): Múltiplas Faixas de Áudio** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): Adiciona tags `imeta` de áudio para faixas alternativas, variantes de idioma e streams apenas de áudio. Um cliente poderia manter um arquivo de vídeo estável enquanto alterna idiomas de áudio, ou servir áudio como faixa separada para conteúdo estilo podcast.

- **[NIP-11](/pt/topics/nip-11/) (Documento de Informações do Relay) e atributos de relay do [NIP-66](/pt/topics/nip-66/)** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): Adiciona um campo estruturado `attributes` a documentos de informações de relay, dando a clientes e ferramentas de descoberta metadados legíveis por máquina além da descrição de texto livre atual.

## Aprofundamento NIP: NIP-49 (Criptografia de Chave Privada)

[NIP-49](/pt/topics/nip-49/) define como um cliente criptografa uma chave privada com uma senha e codifica o resultado como uma string bech32 `ncryptsec`. O [Formstr](#formstr) usa o NIP-49 em seu novo fluxo de cadastro.

O formato não está ligado a um kind de evento dedicado. Um cliente começa com a chave privada secp256k1 bruta de 32 bytes, deriva uma chave simétrica da senha do usuário com scrypt, criptografa a chave usando XChaCha20-Poly1305 e então encapsula o resultado em uma string bech32 `ncryptsec`. Um flag de um byte registra se já se soube que a chave foi manipulada de maneira insegura antes da criptografia.

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

O evento JSON acima é um exemplo em nível de aplicação, não um requisito do NIP-49. O NIP padroniza o formato da chave criptografada. Um cliente pode armazenar o `ncryptsec` localmente, sincronizá-lo por armazenamento específico de app ou exportá-lo como string de backup. Senhas são normalizadas para Unicode NFKC antes da derivação da chave para que a mesma senha seja descriptografada de forma consistente entre clientes e plataformas.

O flag de segurança da chave de um byte tem três valores definidos: `0x00` significa que o histórico de manuseio da chave é desconhecido, `0x01` significa que se sabe que a chave foi tratada de forma insegura (por exemplo, colada como plaintext em um formulário web antes da criptografia), e `0x02` significa que a chave foi gerada e criptografada em um contexto seguro e nunca foi exposta. Clientes podem usar isso para mostrar avisos ao importar chaves com histórico conhecido de insegurança.

O NIP-49 protege chaves melhor do que a exportação em `nsec` puro, mas a criptografia só é tão forte quanto a senha e o custo scrypt configurado. Valores mais altos de `LOG_N` tornam tentativas offline mais difíceis, mas desaceleram operações legítimas de descriptografia. A especificação alerta contra publicar chaves criptografadas em relays públicos, já que atacantes se beneficiam de coletar ciphertext para cracking offline. Em comparação, a assinatura remota [NIP-46](/pt/topics/nip-46/) evita expor chaves por completo, e a assinatura Android [NIP-55](/pt/topics/nip-55/) mantém chaves dentro de um app assinador dedicado. O NIP-49 ocupa um papel diferente: backup criptografado portátil para usuários que gerenciam suas próprias chaves.

As implementações incluem [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) para cadastro, [Amber](https://github.com/greenart7c3/Amber) para backup e restauração de ncryptsec, [diVine v1.0.6](#divine-lanca-v106-com-infraestrutura-de-testes-e2e-e-importacao-nip-49) para importação de conta, [Keep v0.6.0](#keep-v060) para exportação de shares FROST, e ferramentas de gerenciamento de chaves como [nsec.app](https://nsec.app) e [Alby](https://github.com/getAlby/hub).

## Aprofundamento NIP: NIP-70 (Eventos Protegidos)

[NIP-70](/pt/topics/nip-70/) define eventos protegidos. Quando um evento carrega a tag `["-"]`, um relay deve rejeitá-lo a menos que o relay exija autenticação [NIP-42](/pt/topics/nip-42/) e a pubkey autenticada corresponda ao autor do evento.

O fluxo de auth do NIP-42 funciona assim: o relay envia um desafio `AUTH` contendo uma string aleatória, e o cliente responde com um evento assinado kind `22242` cujas tags incluem a URL do relay e o desafio. O relay verifica a assinatura e checa que a pubkey no evento de auth corresponde à pubkey no evento protegido que está sendo publicado. Se as pubkeys não corresponderem, o relay rejeita o evento com o prefixo de mensagem `restricted`.

O conteúdo do evento ainda pode ser público. A tag `-` controla apenas quem pode publicar o evento em um relay que respeita a tag. Isso cobre feeds semi-fechados do [NIP-29](/pt/topics/nip-29/) (Grupos Simples), espaços de relay apenas para membros, e outros contextos em que o autor quer limitar redistribuição pelo grafo de relays. O NIP-70 é uma convenção de tag única, não um novo kind de evento, então qualquer kind de evento existente pode carregar a tag `-`.

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

Mesmo que um relay bloqueie a publicação por terceiros do evento original, alguém ainda pode republicar o conteúdo dentro de um repost. O [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) trata disso exigindo que relays também rejeitem reposts kind 6 e kind 16 de eventos protegidos. O [strfry PR #156](https://github.com/hoytech/strfry/pull/156) adiciona tratamento de auth NIP-42 para eventos protegidos, e o [strfry PR #176](https://github.com/hoytech/strfry/pull/176) bloqueia reposts que incorporam conteúdo protegido.

O NIP-70 controla o comportamento do relay. Um destinatário ainda pode copiar o conteúdo para outro lugar, e a especificação diz isso explicitamente. A tag `-` dá aos relays um sinal legível por máquina para recusar republicação. Em comparação, o [NIP-62](/pt/topics/nip-62/) (Pedido para Desaparecer) pede que relays apaguem dados depois do fato, enquanto o NIP-70 impede publicação não autorizada no momento da ingestão. Os dois são complementares: um autor pode marcar eventos como protegidos para limitar disseminação e, depois, solicitar exclusão se quiser remover o conteúdo de relays que o aceitaram.

---

Isso é tudo por esta semana. Está construindo algo ou tem novidades para compartilhar? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via DM [NIP-17](/pt/topics/nip-17/)</a> ou nos encontre no Nostr.
