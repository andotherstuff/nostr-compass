---
title: 'Nostr Compass #2'
date: 2025-12-24
publishDate: 2025-12-24
draft: false
type: newsletters
translationOf: /en/newsletters/2025-12-24-newsletter.md
translationDate: 2025-12-26
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal do ecossistema do protocolo Nostr.

**Esta semana:** Três implementações de assinadores [NIP-55](/pt/topics/nip-55/) recebem atualizações: Amber adiciona cache de performance, Aegis ganha suporte a URI `nostrsigner:`, e Primal Android se junta a eles como um assinador local completo. Shopstr introduz "Zapsnags" para vendas relâmpago via zaps. Mostro adiciona um fundo de desenvolvimento. Quatro atualizações de NIP chegam incluindo Mensagens Públicas (kind 24) e melhorias de privacidade de grupos. Consultas de cache do NDK aceleram 162x, Applesauce adiciona reações e suporte a carteira NIP-60, e Tenex introduz arquitetura RAL para delegação de agentes IA. Em nosso aprofundamento, explicamos [NIP-02](/pt/topics/nip-02/) (listas de seguidos) e [NIP-10](/pt/topics/nip-10/) (threading de respostas), especificações fundamentais para construir timelines sociais e conversas.

## Notícias {#news}

**Primal Android Se Torna um Assinador NIP-55** - Construindo sobre o [suporte a Nostr Connect da semana passada](/pt/newsletters/2025-12-17-newsletter/#primal-android), Primal implementou capacidades completas de assinatura local através de oito pull requests merged. A implementação inclui um `LocalSignerContentProvider` completo que expõe operações de assinatura para outros apps Android via a interface de content provider do Android, seguindo a especificação [NIP-55](/pt/topics/nip-55/). A arquitetura separa responsabilidades de forma limpa: `SignerActivity` lida com fluxos de aprovação voltados ao usuário, `LocalSignerService` gerencia operações em background, e um novo sistema de permissões permite que usuários controlem quais apps podem solicitar assinaturas. Isso torna o Primal uma alternativa viável ao Amber para usuários Android que querem manter suas chaves em um app enquanto usam outros para diferentes experiências Nostr.

**Shopstr Zapsnags: Vendas Relâmpago via Lightning** - O marketplace nativo Nostr introduziu ["Zapsnags"](https://github.com/shopstr-eng/shopstr/pull/211), uma funcionalidade de venda relâmpago que permite compradores adquirirem itens diretamente do seu feed social com um único zap. A implementação filtra notas kind 1 tagueadas com `#shopstr-zapsnag` e as renderiza como cards de produto com um botão "Zap para Comprar" ao invés do fluxo de carrinho padrão. Quando um comprador zapeia, o sistema gera uma solicitação de pagamento usando [NIP-57](/pt/topics/nip-57/), consulta o recibo de zap kind 9735 para confirmar o pagamento, então encripta informações de envio usando gift wrapping [NIP-17](/pt/topics/nip-17/) antes de enviá-las de forma privada ao vendedor. A funcionalidade armazena detalhes do comprador localmente para compras repetidas e inclui um painel de comerciante para criar listagens de venda relâmpago. É uma combinação inteligente de primitivas sociais, de pagamento e privacidade que demonstra como o design componível do Nostr permite padrões de comércio novos.

**Mostro Introduz Fundo de Desenvolvimento** - A plataforma de trading P2P Bitcoin [NIP-69](/pt/topics/nip-69/) [implementou taxas de desenvolvimento configuráveis](https://github.com/MostroP2P/mostro/pull/555) para apoiar manutenção sustentável. Operadores podem definir `dev_fee_percentage` entre 10-100% da taxa de trading do Mostro (padrão 30%), que automaticamente é direcionada a um fundo de desenvolvimento em cada trade bem-sucedido. A implementação adiciona três colunas de banco de dados (`dev_fee`, `dev_fee_paid`, `dev_fee_payment_hash`) para rastrear contribuições e valida a porcentagem na inicialização do daemon. Documentação técnica em [`docs/DEV_FEE.md`](https://github.com/MostroP2P/mostro/blob/main/docs/DEV_FEE.md) explica o sistema. Este modelo opt-in permite que operadores apoiem desenvolvimento contínuo enquanto mantêm total transparência sobre alocação de taxas.

## Atualizações de NIP {#nip-updates}

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Novos NIPs:**
- **[NIP-A4](/pt/topics/nip-a4/) (Mensagens Públicas, kind 24)** - Um novo kind para mensagens de tela de notificação projetadas para amplo suporte de clientes ([#1988](https://github.com/nostr-protocol/nips/pull/1988)). Diferente de conversas threaded, estas mensagens não têm conceito de histórico de chat ou cadeias de mensagem. Elas usam tags `q` (citações) ao invés de tags `e` para evitar complicações de threading, tornando-as ideais para notificações públicas simples que aparecem no feed de notificações de um destinatário sem criar estado de conversa.

**Mudanças Significativas:**
- **[NIP-29](/pt/topics/nip-29/)** - Clarificação maior de semântica de grupos ([#2106](https://github.com/nostr-protocol/nips/pull/2106)). A tag `closed` agora significa "incapaz de escrever" (somente leitura para não-membros), desacoplada da mecânica de entrada. Uma nova tag `hidden` previne que relays sirvam metadados ou eventos de membros para não-membros, permitindo grupos verdadeiramente privados que são indescobríveis sem convite fora de banda. A tag `private` controla visibilidade de mensagens enquanto ainda permite metadados públicos para descoberta.
- **[NIP-51](/pt/topics/nip-51/)** - Adicionado kind 30006 para conjuntos de imagens curadas ([#2170](https://github.com/nostr-protocol/nips/pull/2170)), seguindo o padrão de 30004 (artigos) e 30005 (vídeos). Já implementado no Nostria.
- **[NIP-55](/pt/topics/nip-55/)** - Clarificado início de conexão para assinadores Android ([#2166](https://github.com/nostr-protocol/nips/pull/2166)). Desenvolvedores implementando sessões multi-usuário estavam usando mal `get_public_key` chamando-o de processos em background. A especificação atualizada recomenda chamá-lo apenas uma vez durante a conexão inicial, prevenindo um footgun de implementação comum.

## Aprofundamento NIP: NIP-02 e NIP-10 {#nip-deep-dive-nip-02-and-nip-10}

Esta semana cobrimos dois NIPs essenciais para funcionalidade social: como clientes sabem quem você segue e como conversas são threaded.

### [NIP-02](/pt/topics/nip-02/): Lista de Seguidos

[NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md) define eventos kind 3, que armazenam sua lista de seguidos. Este mecanismo simples potencializa o grafo social que torna timelines possíveis.

**Estrutura:** Um evento kind 3 contém tags `p` listando pubkeys seguidas:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Cada tag `p` tem quatro posições: o nome da tag, a pubkey seguida (hex), uma dica de URL de relay opcional, e um "petname" opcional (um apelido local). A dica de relay diz a outros clientes onde encontrar os eventos daquele usuário. O petname permite que você atribua nomes memoráveis a contatos sem depender dos nomes de exibição auto-declarados deles.

**Comportamento substituível:** Kind 3 cai no intervalo substituível (0, 3, 10000-19999), então relays mantêm apenas a versão mais recente por pubkey. Quando você segue alguém novo, seu cliente publica um novo kind 3 completo contendo todos os seus seguidos mais o novo. Isso significa que listas de seguidos devem ser completas a cada vez; você não pode publicar atualizações incrementais.

**Construindo timelines:** Para construir um feed home, clientes buscam o kind 3 do usuário, extraem todas as pubkeys das tags `p`, então se inscrevem em eventos kind 1 desses autores:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

O relay retorna notas correspondentes, e o cliente as renderiza. As dicas de relay no kind 3 ajudam clientes a saber quais relays consultar para cada usuário seguido.

**Petnames e identidade:** O campo petname habilita um esquema de nomes descentralizado. Ao invés de confiar em qualquer nome que um usuário declare em seu perfil, você pode atribuir seu próprio rótulo. Um cliente pode exibir "alice (Minha Irmã)" onde "alice" vem do perfil kind 0 dela e "Minha Irmã" é seu petname. Isso fornece contexto que nomes de usuário globais não podem.

**Considerações práticas:** Porque eventos kind 3 são substituíveis e devem ser completos, clientes devem preservar tags desconhecidas ao atualizar. Se outro cliente adicionou tags que seu cliente não entende, sobrescrever cegamente perderia esses dados. Anexe novos seguidos ao invés de reconstruir do zero.

### [NIP-10](/pt/topics/nip-10/): Threading de Notas de Texto

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md) especifica como notas kind 1 referenciam umas às outras para formar threads de resposta. Entender isso é essencial para construir views de conversa.

**O problema:** Quando alguém responde a uma nota, clientes precisam saber: A que isso é uma resposta? Qual é a raiz da conversa? Quem deve ser notificado? NIP-10 responde essas perguntas através de tags `e` (referências de evento) e tags `p` (menções de pubkey).

**Tags marcadas (preferidas):** Clientes modernos usam marcadores explícitos em tags `e`:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Ótimo ponto! Concordo.",
  "sig": "b7d3f..."
}
```

O marcador `root` aponta para a nota original que iniciou o thread. O marcador `reply` aponta para a nota específica sendo respondida. Se respondendo diretamente à raiz, use apenas `root` (nenhuma tag `reply` necessária). A distinção importa para renderização: o `reply` determina indentação em uma view de thread, enquanto `root` agrupa todas as respostas juntas.

**Regras de threading:**
- Resposta direta à raiz: Uma tag `e` com marcador `root`
- Resposta a uma resposta: Duas tags `e`, uma `root` e uma `reply`
- O `root` permanece constante através do thread; `reply` muda baseado no que você está respondendo

**Tags pubkey para notificações:** Inclua tags `p` para todos que devem ser notificados. No mínimo, tagueie o autor da nota que você está respondendo. A convenção é também incluir todas as tags `p` do evento pai (para que todos na conversa fiquem por dentro), mais quaisquer usuários que você @mencione em seu conteúdo.

**Dicas de relay:** A terceira posição em tags `e` e `p` pode conter uma URL de relay onde aquele evento ou conteúdo do usuário pode ser encontrado. Isso ajuda clientes a buscar o conteúdo referenciado mesmo se não estiverem conectados ao relay original.

**Tags posicionais depreciadas:** Implementações antigas do Nostr inferiam significado da posição de tag ao invés de marcadores: primeira tag `e` era root, última era reply, do meio eram menções. Esta abordagem está depreciada porque cria ambiguidade. Se você vir tags `e` sem marcadores, provavelmente são de clientes antigos. Implementações modernas devem sempre usar marcadores explícitos.

**Construindo views de thread:** Para exibir um thread, busque o evento root, então consulte por todos eventos com uma tag `e` referenciando aquela raiz:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Ordene resultados por `created_at` e use marcadores `reply` para construir a estrutura de árvore. Eventos cujo `reply` aponta para a raiz são respostas de primeiro nível; eventos cujo `reply` aponta para outra resposta são respostas aninhadas.

## Lançamentos {#releases}

**Zeus v0.12.0** - Construindo sobre o [suporte a pagamentos paralelos NWC da semana passada](/pt/newsletters/2025-12-17-newsletter/#zeus-lightning-wallet), o [lançamento maior](https://github.com/ZeusLN/zeus/releases/tag/v0.12.0) da carteira Lightning entrega um serviço completo [NIP-47](/pt/topics/nip-47/) Nostr Wallet Connect com suporte a relay personalizado e rastreamento de orçamento. Uma [correção de recarga de orçamento](https://github.com/ZeusLN/zeus/pull/3455) garante que conexões usem limites atuais. [Cópia de endereço Lightning](https://github.com/ZeusLN/zeus/pull/3460) não inclui mais o prefixo `lightning:`, corrigindo problemas de colagem em campos de perfil Nostr.

**Amber v4.0.6** - O assinador [NIP-55](/pt/topics/nip-55/) Android [adiciona cache de performance](https://github.com/greenart7c3/Amber/releases/tag/v4.0.6) a operações de assinatura e melhora tratamento de erros ao decriptar conteúdo malformado. Confiabilidade de conexão melhorou com lógica de retry para eventos de conexão de relay, e várias correções de crash abordam casos extremos em torno de URIs `nostrconnect://` inválidas e interações de tela de permissão.

**nak v0.17.3** - O [último lançamento](https://github.com/fiatjaf/nak/releases/tag/v0.17.3) da ferramenta de linha de comando Nostr restringe builds LMDB ao Linux, corrigindo problemas de compilação cross-platform.

**Aegis v0.3.4** - O assinador Nostr cross-platform [adiciona suporte](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.4) para o esquema de URI `nostrsigner:` definido em [NIP-55](/pt/topics/nip-55/), correspondendo ao fluxo de conexão do Amber. Dados de relay local agora podem ser importados e exportados para backup, e o lançamento inclui correções de bugs para erros de socket de relay e melhorias de UI para a interface de relay local.

## Mudanças notáveis de código e documentação {#notable-code-and-documentation-changes}

*Estes são pull requests abertos e trabalho em estágio inicial, perfeitos para obter feedback antes de serem merged. Se algo chamar sua atenção, considere revisar ou comentar!*

### Damus (iOS) {#damus}

[Persistência de lista de silenciados](https://github.com/damus-io/damus/pull/3469) corrige um problema onde listas de silenciados eram apagadas em cold start. A correção adiciona guardas para prevenir sobrescritas acidentais durante a inicialização do app. [Timing de stream de perfil](https://github.com/damus-io/damus/pull/3457) elimina um delay de ~1 segundo antes de perfis em cache aparecerem. Anteriormente, views esperavam por tarefas de inscrição reiniciarem; agora `streamProfile()` imediatamente retorna dados em cache do NostrDB, removendo a janela onde pubkeys abreviadas e imagens placeholder apareciam.

### White Noise (Mensagens Encriptadas) {#white-noise}

[Streaming de mensagens em tempo real](https://github.com/marmot-protocol/whitenoise/pull/919) substitui o mecanismo de polling anterior com uma arquitetura baseada em stream. O novo `ChatStreamNotifier` consome o stream de mensagens do SDK Rust diretamente, mantendo ordem cronológica e lidando com atualizações incrementais eficientemente. Testes mostraram melhoria significativa em responsividade. Uma [API de lista de chat](https://github.com/marmot-protocol/whitenoise/pull/921) adiciona `get_chat_list` para recuperar resumos de conversas, e uma [correção de ordenação estável](https://github.com/marmot-protocol/whitenoise/pull/905) previne loops de reordenação de mensagens usando `createdAt` com ID de mensagem como desempate.

### NDK (Biblioteca) {#ndk}

Dois pull requests entregaram melhorias dramáticas de performance de cache. [PR #371](https://github.com/nostr-dev-kit/ndk/pull/371) corrigiu um bug onde eventos lidos do cache SQLite eram imediatamente escritos de volta, causando 100% de escritas duplicadas no boot do app. A correção adiciona uma guarda `fromCache` e implementa verificação de duplicatas O(1) via um Set em memória. Para conjuntos de resultado pequenos (<100 eventos), transferência JSON direta substitui overhead de codificação binária. [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372) removeu chamadas desnecessárias `seenEvent` para eventos em cache. A busca no cache LRU custava 0.24-0.64ms por evento; para 5,700 eventos em cache, isso adicionava ~1.4 segundos de overhead. Resultado: consultas de cache caíram de ~3,690ms para ~22ms (162x mais rápido).

### rust-nostr (Biblioteca) {#rust-nostr}

[Suporte a REQ multi-filtro](https://github.com/rust-nostr/nostr/pull/1176) foi restaurado após ser removido em um refactor anterior. O SDK novamente aceita `Vec<Filter>` para solicitações de inscrição, permitindo consultas eficientes que combinam múltiplas condições de filtro com lógica OR. [Proveniência de relay](https://github.com/rust-nostr/nostr/pull/1156) foi adicionada a métodos `stream_events*`, então cada evento em stream agora inclui o `RelayUrl` de onde veio e um `Result` indicando sucesso ou falha, útil para rastrear confiabilidade de relay e debugar problemas de conexão. Uma [correção de segurança](https://github.com/rust-nostr/nostr/pull/1179) removeu a dependência `url-fork` seguindo RUSTSEC-2024-0421, eliminando uma vulnerabilidade conhecida.

### Applesauce (Biblioteca) {#applesauce}

A biblioteca TypeScript que potencializa [noStrudel](https://github.com/hzrd149/nostrudel) viu desenvolvimento significativo esta semana. Novos modelos incluem um [sistema de reações](https://github.com/hzrd149/applesauce) e casting de grupos de usuários. Funcionalidade de carteira expandiu com suporte NIP-60, uma aba de envio, e ferramentas melhoradas de recuperação de token. Uma nova propriedade `user.directMessageRelays$` expõe configuração de relay DM. Todas as ações foram refatoradas para usar interfaces async (removendo geradores async), e correções de bugs abordaram restauração de conteúdo encriptado e casos extremos de filtro de eventos baseados em tempo.

### Tenex (Agentes IA) {#tenex}

O [sistema de coordenação multi-agente](https://github.com/tenex-chat/tenex) construído sobre Nostr introduziu arquitetura RAL (Request-Action-Lifecycle) em [cinco PRs merged](https://github.com/pablof7z/tenex/pull/38). RAL permite que agentes pausem quando delegando tarefas e retomem quando resultados chegam, com persistência de estado no escopo da conversa. Ferramentas de delegação (`delegate`, `ask`, `delegate_followup`, `delegate_external`) agora publicam eventos Nostr e retornam sinais de parada ao invés de bloquear. O refactor inclui migração para AI SDK v6, infraestrutura de teste VCR para gravação determinística de interação LLM, e suporte a imagens multimodal.

---

Isso é tudo por esta semana. Construindo algo? Tem notícias para compartilhar? Quer que a gente cubra seu projeto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via NIP-17 DM</a> ou nos encontre no Nostr.
