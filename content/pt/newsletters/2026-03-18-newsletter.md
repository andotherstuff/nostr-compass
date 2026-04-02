---
title: 'Nostr Compass #14'
date: 2026-03-18
translationOf: /en/newsletters/2026-03-18-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre o Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) implementa suporte completo aos métodos do [NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect), [Alby Hub](https://github.com/getAlby/hub) adiciona suporte a múltiplos relays na [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6), [Amber](https://github.com/greenart7c3/Amber) lança [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3) com Tor embutido e permissões de assinatura mais granulares, e [Zeus](https://github.com/ZeusLN/zeus) remove um caminho arriscado de keysend NWC no [PR #3835](https://github.com/ZeusLN/zeus/pull/3835). [Notedeck](https://github.com/damus-io/notedeck) lança um atualizador assinado na [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) que descobre releases através de eventos [NIP-94](/pt/topics/nip-94/) (File Metadata), enquanto [Damus](https://github.com/damus-io/damus) corrige estado obsoleto do [NIP-65](/pt/topics/nip-65/) (Relay List Metadata), [Nostrability Outbox](https://github.com/nostrability/outbox) revisa seus resultados de benchmark com dados corrigidos, e [Primal iOS](https://github.com/PrimalHQ/primal-ios-app) testa assinaturas diretas de relay para DMs. [Primal Android](https://github.com/PrimalHQ/primal-android-app) lança [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7), [Route96](https://github.com/v0l/route96) lança [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0), [OpenChat](https://github.com/DavidGershony/openChat) continua refinando a interoperabilidade Marmot na [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11), [Pika](https://github.com/sledtools/pika) consolida seu runtime na [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1), e [Nostria](https://github.com/nostria-app/nostria) adiciona filtragem Web of Trust via [NIP-85](/pt/topics/nip-85/) (Trusted Assertions). O repositório de NIPs mergeia a marcação Djot do [NIP-54](/pt/topics/nip-54/) (Wiki) e um limite de entrada de 5000 caracteres para [NIP-19](/pt/topics/nip-19/) (Bech32-Encoded Entities).

## Notícias

### Suporte a Wallet Connect se amplia, e clientes de carteira reforçam caminhos de falha

[Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android mantido por vitorpamplona, mergeou o [PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828), que aproxima sua implementação do [NIP-47](/pt/topics/nip-47/) da cobertura completa do protocolo. O patch adiciona `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`, métodos de hold invoice, suporte a keysend com registros TLV, descoberta de capacidades via kind `13194`, e eventos de notificação no kind `23197` com [NIP-44](/pt/topics/nip-44/) (Encrypted Payloads). Isso dá ao cliente uma superfície NWC muito mais ampla sem depender de extensões específicas de app.

A stack de carteiras ao redor se moveu na mesma direção. [Alby Hub](https://github.com/getAlby/hub), o nó Lightning auto-custodial e serviço de carteira por trás de muitos deployments NWC, lançou [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6) com suporte a múltiplos relays e fluxos de conexão e swap simplificados. [Zeus](https://github.com/ZeusLN/zeus), a carteira Lightning mobile, mergeou o [PR #3835](https://github.com/ZeusLN/zeus/pull/3835) removendo suporte a keysend NWC após identificar um caminho silencioso de drenagem de fundos nesse fluxo, enquanto também corrigiu tratamento de eventos pendentes e atividade Cashu. A conectividade de carteira no Nostr está ficando mais ampla, e implementadores estão removendo fluxos difíceis de proteger.

### Notedeck move descoberta de releases para o Nostr

[Seguindo a cobertura do Notedeck da semana passada](/en/newsletters/2026-03-11-newsletter/), [Notedeck](https://github.com/damus-io/notedeck), o cliente desktop nativo da equipe Damus, lançou [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) após mergear o [PR #1326](https://github.com/damus-io/notedeck/pull/1326). O novo atualizador se inscreve em eventos de release kind `1063` assinados, identifica a plataforma local, baixa o binário referenciado e verifica o hash SHA256 antes da instalação. Metadados de release não precisam mais vir da API do GitHub ou de um site do projeto. Uma pubkey de release confiável e uma conexão de relay são suficientes.

O mesmo patch adiciona um CLI `notedeck-release` que publica esses eventos a partir de artefatos de release do GitHub, o que significa que o pipeline de release agora tem um caminho de publicação nativo do Nostr assim como um caminho de descoberta nativo do Nostr. Isso também aproxima o modelo de atualizador do Damus e Notedeck do fluxo de release assinado publicado via relay da Zapstore: o ferramental `zsp` da Zapstore já trata ativos de software como eventos kind `1063` ou `3063`, então esse caminho não está limitado a um único cliente ou publicador. O restante do release candidate é trabalho prático de desktop, colunas de follows, "View As User" de perfil, suporte a [NIP-59](/pt/topics/nip-59/) (Gift Wrap), estatísticas de notas em tempo real e tratamento de limitações do [NIP-11](/pt/topics/nip-11/) (Relay Information Document), mas o atualizador é a parte que provavelmente vai durar além deste ciclo de release.

### Estado de relay se aproxima do comportamento em tempo de execução

[Damus](https://github.com/damus-io/damus) mergeou o [PR #3665](https://github.com/damus-io/damus/pull/3665), substituindo um ID de evento de lista de relays armazenado obsoleto por uma consulta direta ao banco de dados para o evento kind `10002` mais recente. Quando o valor antigo ficava obsoleto, operações de adicionar e remover relay podiam recorrer a listas bootstrap ou de um ano atrás, o que fazia algumas mudanças de relay parecerem bem-sucedidas enquanto deixavam o estado ativo inalterado. O [PR #3690](https://github.com/damus-io/damus/pull/3690) corrige um segundo caminho de falha deletando estado `lock.mdb` obsoleto durante compactação LMDB para que o app não quebre com `SIGBUS` no próximo lançamento.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) abriu o [PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194), que se inscreve diretamente nos relays de escrita [NIP-04](/pt/topics/nip-04/) (Encrypted Direct Messages) de um parceiro de chat enquanto uma conversa está aberta, mantendo o servidor de cache como fallback. [Nostur](https://github.com/nostur-com/nostur-ios-public) abriu o [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53), que combina pontuação randomizada de relay, filtragem de atividade [NIP-66](/pt/topics/nip-66/) do nostr.watch e Thompson sampling para mudar a seleção de relay de uma heurística fixa para uma política aprendida. Clientes há tempos tratam a escolha de relay como dados de configuração. Mais apps agora a tratam como estado vivo que precisa de lógica de medição e reparo.

## Lançamentos

### Primal Android 3.0.7

[Primal Android](https://github.com/PrimalHQ/primal-android-app), o cliente Android do Primal, lançou [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7) com um novo ciclo de enquetes e carteira. O [PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945) adiciona votação em enquetes baseada em zap, o [PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948) pagina o carregamento de votos para que enquetes maiores continuem usáveis, e o [PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965) busca recibos de zap para todas as transações. O mesmo lançamento também marca eventos suportados com metadados de cliente [NIP-89](/pt/topics/nip-89/) (Recommended Application Handlers) no [PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968), o que ajuda clientes downstream a atribuir origens de eventos de forma mais limpa.

### Amber v4.1.3

[Seguindo a cobertura do Amber da semana passada](/en/newsletters/2026-03-11-newsletter/), [Amber](https://github.com/greenart7c3/Amber), o app assinador Android para fluxos [NIP-55](/pt/topics/nip-55/) (Android Signer Application), lançou [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3). O lançamento se baseia em seu recente trabalho de relay-auth [NIP-42](/pt/topics/nip-42/) com mais endurecimento operacional: o [PR #327](https://github.com/greenart7c3/Amber/pull/327) adiciona Tor embutido junto com suporte Orbot, o [PR #324](https://github.com/greenart7c3/Amber/pull/324) substitui permissões de criptografia grosseiras baseadas em NIP por regras específicas por tipo de conteúdo, e o [PR #336](https://github.com/greenart7c3/Amber/pull/336) remove permissões de rede do flavor offline enquanto o [PR #335](https://github.com/greenart7c3/Amber/pull/335) adiciona verificações de CI para mantê-lo assim. O [PR #322](https://github.com/greenart7c3/Amber/pull/322) também move o armazenamento de PIN para DataStore criptografado.

Este lançamento reforça a fronteira do próprio assinador. Isso é útil para qualquer fluxo Android que entregue chaves reais ou decisões de relay-auth ao Amber, porque a parte difícil não é apenas o que o assinador pode fazer. É também quão estreitamente ele pode ser limitado.

### Route96 v0.6.0

[Seguindo a cobertura do Route96 da semana passada](/en/newsletters/2026-03-11-newsletter/), [Route96](https://github.com/v0l/route96), o servidor de mídia que suporta Blossom e [NIP-96](/pt/topics/nip-96/) (HTTP File Storage), lançou [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0). O lançamento move configuração e estado de whitelist para o banco de dados com hot reload e adiciona políticas de retenção para arquivos antigos ou frios. Também adiciona um endpoint `GET /user/files` mais rico além de rastreamento de file-stat para downloads e egress, o que dá aos operadores mais visibilidade sobre como seu servidor de armazenamento está sendo usado.

### OpenChat v0.1.0-alpha.11

[Seguindo a cobertura do OpenChat da semana passada](/en/newsletters/2026-03-11-newsletter/), [OpenChat](https://github.com/DavidGershony/openChat), o cliente de chat baseado em Avalonia construído sobre a stack Marmot, lançou [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11) após uma semana de trabalho rápido de protocolo. O [commit c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c) encapsula eventos Welcome em gift wrap [NIP-59](/pt/topics/nip-59/) e remove shims antigos de normalização de tags MIP-00, o [commit 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1) completa a auditoria de conformidade MIP-02, e o [commit 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f) faz o mesmo para criptografia de mensagem de grupo MIP-03. O [commit 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547) também consolida o tratamento NIP-44 na implementação compartilhada do marmot-cs, reduzindo o risco de drift de cripto do lado do cliente.

### nak v0.19.0 e v0.19.1

[nak](https://github.com/fiatjaf/nak), o toolkit de linha de comando Nostr do fiatjaf, lançou [v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0) e [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1). A série 0.19 adiciona uma interface de fórum de grupo no [commit 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47), muda edições de metadados de grupo para um fluxo de substituição completa no [commit da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3), e substitui o antigo tratamento `no-text` por `supported_kinds` no [commit bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf). Para implementadores de grupos, isso mantém o CLI alinhado com a direção que specs e clientes de grupo estão seguindo.

## Atualizações de Projetos

### Amethyst

[Seguindo a cobertura do Amethyst da semana passada](/en/newsletters/2026-03-11-newsletter/), [Amethyst](https://github.com/vitorpamplona/amethyst), o cliente Android com uma das mais amplas superfícies de protocolo no Nostr, continuou construindo sobre seu trabalho de carteira e relay após o patch NIP-47. O [PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853) adiciona consultas COUNT do [NIP-45](/pt/topics/nip-45/) (Event Counting) nas telas de gerenciamento de relay, para que usuários possam ver quantos eventos cada relay realmente mantém para feed principal, notificações, DMs e dados de índice. O [PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849) adiciona uploads de arquivos criptografados para chats [NIP-17](/pt/topics/nip-17/) (Private Direct Messages), com um caminho de retry para uploads não criptografados quando um host de armazenamento rejeita a versão criptografada.

O [PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791) também traz login completo de bunker desktop [NIP-46](/pt/topics/nip-46/) (Nostr Connect) com um indicador de heartbeat, o que importa porque falhas de assinatura remota frequentemente parecem quebras aleatórias de UI do lado do usuário. O cliente mostra se o assinador está vivo e quão recentemente ele respondeu, enquanto também torna óbvio quando a sessão atual usa um bunker.

### Nostria

[Nostria](https://github.com/nostria-app/nostria), o cliente multiplataforma construído em torno de uma stack local-first, mergeou o [PR #561](https://github.com/nostria-app/nostria/pull/561) adicionando filtragem Web of Trust para feeds e respostas de threads. O recurso usa os dados de rank do serviço de confiança existente e os expõe como filtro de feed e filtro de respostas, ocultando autores cujo rank não alcança o limiar enquanto preserva a estrutura da thread quando descendentes confiáveis estão presentes. Isso dá aos usuários uma camada intermediária entre "mostrar todos" e curadoria baseada em listas hardcoded.

A mesma semana também trouxe o [PR #563](https://github.com/nostria-app/nostria/pull/563), que adiciona filtragem de conteúdo e suporte a repost na página de resumo. Fora da lista de PRs rastreados, Nostria também tem preenchido mais de sua superfície para power users. Agora suporta o mais recente serviço Brainstorm Web of Trust com cadastro in-app, junto com fluxos de enviar e receber dinheiro em DMs usando NWC e invoices BOLT-11. Também adiciona tratamento de GIFs nativos do Nostr através do NIP de emoji e um caminho mais robusto de importação RSS para músicos que pode capturar splits Lightning existentes de feeds de podcast. Nostria está tratando ranking, mídia, pagamentos e publicação como uma superfície de app conectada.

### Nostur

[Nostur](https://github.com/nostur-com/nostur-ios-public), o cliente iOS mantido por nostur-com, abriu o [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53) para mudar o roteamento outbox de um plano fixo para uma política pontuada. O patch adiciona pontuação randomizada de relay, filtragem de atividade de relay [NIP-66](/pt/topics/nip-66/) com um feed cacheado do nostr.watch, e Thompson sampling para que dados de sucesso e falha de relay mudem seleções futuras. O design mantém uma válvula de segurança quando muitos relays seriam filtrados e preserva relays `.onion`. Este é um dos exemplos atuais mais claros de um cliente tratando seleção de relay como um sistema adaptativo.

### Nostrability Outbox

[Seguindo o relatório de benchmark Outbox anterior](/pt/newsletters/2026-03-04-newsletter/), [Nostrability Outbox](https://github.com/nostrability/outbox), o projeto de benchmark e análise focado no roteamento de clientes [NIP-65](/pt/topics/nip-65/) e [NIP-66](/pt/topics/nip-66/), passou a semana refinando suas próprias afirmações. O [PR #35](https://github.com/nostrability/outbox/pull/35) substitui resultados inflados de Thompson sampling por um re-benchmark completo em 1.511 execuções e recomenda a variante `CG3` para roteamento estilo NDK. O [PR #43](https://github.com/nostrability/outbox/pull/43) adiciona comparações de decay e caso de uso, corrige um bug de envenenamento de cache de `0 follows`, e re-executa o dataset Telluride após fixar TTLs de cache.

Isso não é trabalho de produto no sentido usual, mas importa para autores de clientes porque os números do projeto agora são mais precisos e menos lisonjeiros nos lugares onde haviam sobreclamado anteriormente. O resultado corrigido ainda é útil. Seleção randomizada continua superando roteamento puramente determinístico nos casos que o Outbox se preocupa, aprendizado estilo Thompson pode melhorar materialmente a cobertura quando clientes persistem histórico útil de relay, e filtragem de atividade [NIP-66](/pt/topics/nip-66/) elimina tempo desperdiçado em relays mortos. O trabalho também está se transformando em propostas concretas de implementação, incluindo [NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387), [Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53), [Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833), [rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282), [welshman #53](https://github.com/coracle-social/welshman/pull/53), e [applesauce #54](https://github.com/hzrd149/applesauce/pull/54) mais [applesauce #55](https://github.com/hzrd149/applesauce/pull/55).

### Backend do White Noise

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), o backend Rust usado pelo White Noise e outros ferramentais Marmot, mergeou dois patches de endurecimento de fronteira em torno do tratamento de mídia Blossom. O [PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637) impõe HTTPS em URLs Blossom e adiciona um timeout de upload, enquanto o [PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642) limita downloads de blob a `100 MiB` para bloquear pulls de mídia superdimensionados de se transformarem em um caminho de negação de serviço. Para software de mensagens privadas, URLs de mídia são uma das interfaces mais afiadas entre lógica de aplicação criptografada e infraestrutura de rede não confiável. Esta semana a equipe reforçou essa borda.

### rust-nostr

[rust-nostr](https://github.com/rust-nostr/nostr), a biblioteca de protocolo Rust, mergeou o [PR #1280](https://github.com/rust-nostr/nostr/pull/1280) adicionando construtores de conveniência para `LocalRelayBuilderNip42`. Os novos helpers de leitura e escrita dão a setups de relay embutido e teste uma forma mais clara de transformar política de auth [NIP-42](/pt/topics/nip-42/) em código. Este é um pequeno patch de biblioteca, mas importa para equipes construindo relays locais ou empacotados em apps que precisam de auth habilitado sem repetir boilerplate toda vez.

### Pika

[Seguindo a cobertura anterior do Pika](/pt/newsletters/2026-03-04-newsletter/), [Pika](https://github.com/sledtools/pika), o app de mensagens baseado em Marmot, lançou [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1) e [pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1) com um ciclo de release focado em convergência de runtime. O [PR #542](https://github.com/sledtools/pika/pull/542) introduz uma fachada de runtime Marmot compartilhada para o CLI e sidecar, com o host do app migrando para a mesma superfície. O [PR #556](https://github.com/sledtools/pika/pull/556) reforça o ciclo de vida do agente OpenClaw e estado de provisionamento, enquanto o [PR #600](https://github.com/sledtools/pika/pull/600) adiciona restauração de backup e segurança de recuperação mais rígida para ambientes gerenciados.

A superfície diretamente voltada ao usuário aqui é menor que no último writeup do Pika, mas a mudança arquitetural é significativa. Puxar lógica de grupo, mídia, chamada e sessão para trás de um runtime compartilhado reduz a chance do app e daemon divergirem conforme a stack Marmot cresce.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mergeado:**

- **[NIP-54](/pt/topics/nip-54/) (Wiki): Troca de Asciidoc para Djot** ([PR #2242](https://github.com/nostr-protocol/nips/pull/2242)): Conteúdo wiki no kind `30818` agora usa Djot como formato de marcação canônico. O texto mergeado adiciona comportamento explícito de wikilink, exemplos de merge-request para kind `818`, exemplos de redirecionamento para kind `30819`, e exemplos de normalização não-latina para tags `d`. Isso dá aos implementadores um alvo de parsing mais limpo que Asciidoc e remove mais um caminho de spec que dependia de um toolchain centrado em Ruby.

- **[NIP-19](/pt/topics/nip-19/) (Bech32-Encoded Entities): Adiciona limite de entrada** ([PR #2264](https://github.com/nostr-protocol/nips/pull/2264)): A spec agora recomenda limitar strings de entidades codificadas em Bech32 a 5000 caracteres. Esta é uma mudança pequena com valor real para parsers, porque strings NIP-19 agora aparecem em fluxos QR, deep links, share sheets e entrada colada por usuários em muitos clientes.

**PRs Abertos e Discussões:**

- **Arquivo de Chave Nostr para [NIP-49](/pt/topics/nip-49/) (Private Key Encryption)** ([PR #2269](https://github.com/nostr-protocol/nips/pull/2269)): Propõe um formato de arquivo `.nostrkey` para exportação e importação de chaves criptografadas por senha. Se mergeado, daria aos clientes um caminho de backup baseado em arquivo mais normal do que copiar strings `ncryptsec` brutas por aí.

- **Consistência de estado de membros para [NIP-43](/pt/topics/nip-43/) (Relay Access Metadata and Requests)** ([PR #2267](https://github.com/nostr-protocol/nips/pull/2267)): Adiciona uma seção clarificando que relays devem manter um estado de membros autoritativo por pubkey. Isso simplificaria a lógica de clientes de grupo em torno de mudanças de membros e histórico replicado.

- **Orientação de exclusão para [NIP-17](/pt/topics/nip-17/) (Private Direct Messages)** ([PR #2260](https://github.com/nostr-protocol/nips/pull/2260)): Propõe um caminho concreto para edição e exclusão de mensagens privadas através de eventos de exclusão encapsulados em gift wrap. O trabalho ainda está aberto, mas autores de clientes precisam de uma resposta aqui se NIP-17 vai substituir completamente os fluxos de DM mais antigos.

- **URI de share-intent para [NIP-222](/pt/topics/nip-222/)** ([PR #2266](https://github.com/nostr-protocol/nips/pull/2266)): O rascunho padronizaria como apps mobile e desktop entregam conteúdo compartilhado para um cliente Nostr. Essa é uma das bordas de interoperabilidade mais ásperas nos fluxos atuais de app para app.

## NIP Deep Dive: NIP-94 (File Metadata)

[NIP-94](/pt/topics/nip-94/) define kind `1063` como um evento de metadados de primeira classe para um arquivo. A [especificação](https://github.com/nostr-protocol/nips/blob/master/94.md) dá ao evento seu próprio `content` legível por humanos mais tags legíveis por máquina para URL de download, tipo MIME, hashes, dimensões, previews, fallbacks e dicas de serviço de armazenamento. Isso importa porque o arquivo se torna consultável nos relays como seu próprio objeto. Um cliente não precisa extrair metadados do conteúdo circundante para entender o que o arquivo é.

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

As tags fazem mais trabalho do que aparentam à primeira vista. `x` identifica o arquivo servido, enquanto `ox` identifica o arquivo original antes de qualquer transformação do lado do servidor. As tags de preview permitem que clientes construam índices de arquivos navegáveis sem baixar o ativo completo, e `summary` pode carregar um excerto curto ao lado deles. `fallback` dá uma segunda fonte quando a URL principal falha, e `service` indica o protocolo de armazenamento por trás do arquivo, como [NIP-96](/pt/topics/nip-96/) ou outro host. NIP-94 portanto fica abaixo de postagem social e acima de armazenamento bruto. Ele descreve o arquivo, não a conversa em torno do arquivo.

É por isso que o atualizador do Notedeck desta semana é interessante. O [PR #1326](https://github.com/damus-io/notedeck/pull/1326) usa eventos kind `1063` assinados para descoberta de releases de software, e então verifica o binário baixado contra o SHA256 publicado. O mesmo formato de evento pode descrever um artefato de software ou um upload de mídia. NIP-94 é antigo o suficiente para ser estável, mas ainda tem espaço para crescer porque mais projetos estão tratando eventos de metadados como um transporte para máquinas, não apenas como decoração para pessoas.

## NIP Deep Dive: NIP-54 (Wiki)

[NIP-54](/pt/topics/nip-54/) define kind `30818` como um evento de artigo wiki. A [especificação](https://github.com/nostr-protocol/nips/blob/master/54.md) trata a tag `d` como o tópico normalizado do artigo e permite que muitos autores publiquem entradas para o mesmo assunto. O corpo do artigo vive no `content`, enquanto tags tratam de identidade normalizada, título de exibição, resumos e referências a versões anteriores. Isso significa que NIP-54 não é apenas um formato de conteúdo. É também um problema de recuperação e ranking, porque cada cliente ainda precisa decidir qual versão do artigo mostrar.

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

O merge desta semana muda a marcação canônica de Asciidoc para Djot no [PR #2242](https://github.com/nostr-protocol/nips/pull/2242). Isso importa para implementadores porque Djot tem uma spec standalone mais precisa e uma história de parser mais simples entre linguagens. O texto mergeado também clarifica como wikilinks por referência resolvem, como merge requests usam kind `818`, como redirecionamentos usam kind `30819`, e como a normalização da tag `d` deve se comportar para scripts não-latinos. Essas são as partes que fazem dois clientes independentes concordarem sobre para qual artigo um link aponta.

NIP-54 também ocupa um lugar incomum no protocolo. Um cliente wiki precisa de renderização de conteúdo, mas também precisa de política de ranking. Reações, listas de relay, listas de contatos e sinais explícitos de deferência todos alimentam qual artigo vence para um dado tópico. A troca para Djot não resolve esse problema de ranking, mas remove uma das ambiguidades de parser que estava por baixo dele. É por isso que o merge importa agora: a mudança é menos sobre formatação de prosa mais bonita e mais sobre tornar o comportamento wiki multi-cliente mais fácil de implementar consistentemente.

Construindo algo, ou quer que cubram? Entre em contato via [NIP-17](/pt/topics/nip-17/) DM no Nostr em `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`.
