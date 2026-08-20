---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
translationOf: /en/newsletters/2026-08-12-newsletter.md
translationDate: 2026-08-12
draft: false
type: newsletters
description: "Ferramentas de identidade pós-quântica, mensagens criptografadas e assinatura mais robustas, configurações portáteis de comunidade e trabalho de protocolo em NIPs e Concord."
---

Bem-vindos de volta ao [Nostr Compass](https://nostrcompass.org), seu guia semanal de Nostr.

**Esta semana:** o [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) adiciona chaves pós-quânticas e mensagens protegidas opt-in ao lado de identidades Nostr existentes. O [Divine](https://github.com/divinevideo/divine-mobile) reforça o isolamento de contas, a validação de mensagens privadas e a confirmação de publicação; o [MDK](https://github.com/marmot-protocol/mdk) fortalece a convergência e a recuperação de grupos criptografados; e o [Amber](https://github.com/greenart7c3/Amber) torna explícitas as decisões de assinatura em grupo. Os lançamentos melhoram conexões de carteira, chat criptografado, descoberta social, sincronização entre dispositivos e assinatura remota, enquanto o trabalho de protocolo abrange identidade e comunidades criptografadas. Os mergulhos profundos explicam solicitações autenticadas de exclusão e denúncias descentralizadas.

## Histórias Principais

### nostr-wot-extension 0.4.0 adiciona chaves pós-quânticas ao lado de uma identidade Nostr

O [nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) é uma extensão de navegador para gerenciar identidades Nostr e assinar. Contas criadas a partir de uma seed de 24 palavras agora podem derivar chaves de criptografia ML-KEM-1024 e de assinatura ML-DSA-87 ao lado da chave Nostr existente. Um fluxo de um clique publica uma atestação kind `10203` que vincula a chave pública Nostr às duas chaves públicas pós-quânticas e inclui uma prova de posse ML-DSA. Contas importadas de um mnemônico de 12 palavras, `nsec` nu, signatário remoto ou chave somente leitura não podem usar o fluxo de derivação, e a extensão explica essa limitação na visualização da conta.

O lançamento também adiciona mensagens diretas pós-quânticas opt-in. Ele combina o segredo compartilhado ML-KEM com a [chave de conversa de mensagens criptografadas do NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) existente por meio de HKDF e mantém as camadas normais de gift-wrap do NIP-59 que ocultam metadados para entrega via relay. A criptografia nunca recua silenciosamente depois que o destinatário opta por entrar, enquanto a descriptografia seleciona automaticamente o caminho apropriado. Isso protege o novo caminho de mensagens contra a recuperação posterior de uma chave privada Nostr atual, mas não substitui assinaturas de eventos secp256k1; o lançamento deixa explicitamente essa migração maior para coordenação futura com relays e clientes.

### Divine Mobile 1.0.19 reforça contas, mensagens privadas e publicação

O [Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) é um cliente móvel de vídeos curtos que publica e recupera vídeos por meio do Nostr. Seu seletor de contas agora constrói cada identidade conectada em torno de um contêiner com escopo de conta, e uma correção de publicação impede que um vídeo seja enviado pela conta errada. Os caminhos de publicação em relays agora aguardam uma resposta `OK` com semântica explícita de sucesso, enquanto um frame `CLOSED` do relay pode encerrar sua própria consulta pendente em vez de deixar a requisição pendurada.

O [tratamento de mensagens privadas](https://github.com/divinevideo/divine-mobile/pull/6368) rejeita campos rumor não autenticados e seals não assinados, restaura quatro casos de mensagens ausentes e encaminha conversas em grupo de participantes totalmente seguidos para a caixa de entrada. O lançamento também preserva as tags em eventos de vídeo endereçáveis quando listas são atualizadas e consome solicitações de exclusão observadas para que vídeos removidos desapareçam do estado local. Essas mudanças seguem o trabalho de tempo limite de consulta por relay coberto na semana passada, mas deslocam o foco do isolamento de recuperação para limites de identidade, validação de mensagens e confirmação de publicação.

### MDK 0.9.11 endurece a convergência e a recuperação de grupos Marmot

O [MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) é um kit de desenvolvimento Rust para Marmot, um protocolo de mensagens em grupo criptografadas transportado sobre Nostr. O lançamento constrói um sistema maior de convergência e recuperação em torno da máquina de estados do grupo: passes de convergência obsoletos reabrem na ponta atual do grupo, projeções de capacidade de entrada são confirmadas atomicamente, mensagens adiadas recebem tempos de vida limitados entre reinicializações, e checkpoints endereçados por commit ajudam a recuperar os próprios forks de commit de uma identidade. Envios não estáveis podem ser enfileirados e recuperados, enquanto um caminho de estagnação de epoch escala para backfill e mensagens enviadas sobrevivem ao trabalho de convergência.

[Integrações de armazenamento e host](https://github.com/marmot-protocol/mdk/pull/1201) recebem um endurecimento paralelo. O MDK exclui com segurança projeções SQLite podadas, zera chaves privadas importadas, intermediários de exportação de chave criptografada NIP-49 e buffers de serialização OpenMLS, e redige chaves de imagem de grupo da saída de debug. A importação de conta pode ser retomada após interrupção, caminhos de armazenamento privado em iOS e Android são reparados, e hosts podem fechar explicitamente o armazenamento antes da suspensão. Novas projeções leves de roster e associação local reduzem o que os aplicativos precisam ler, enquanto o conector Hermes pode entregar várias imagens geradas por agentes como um álbum Marmot.

### Nostria 4.1.67 expande a administração de comunidades criptografadas

O [Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67) é um cliente social web e desktop para Nostr. Ele se baseia nos grupos gerenciados por relays experimentais NIP-29 e nas comunidades criptografadas Concord introduzidas na 4.1.53, adicionando dissolução de comunidade, administração de ícone e banner, uploads de fotos criptografadas com prévias comprimidas, um seletor completo de reações e um layout de dois painéis que mantém uma comunidade aberta enquanto o usuário lê notas ou artigos. O lançamento também adiciona mensagens encadeadas e um hub combinado para chats públicos, de grupo e privados.

### Amber 6.4.0 torna explícita cada decisão de assinatura em grupo

O [Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) é um signatário Android que mantém chaves privadas Nostr separadas dos aplicativos que solicitam assinaturas. Sua tela redesenhada de múltiplas requisições oferece controles Aprovar e Negar para cada requisição e cada grupo, substituindo o fluxo anterior de seleção e confirmação. Requisições negadas enviadas pela interface bunker mediada por relay do Amber agora recebem respostas de erro adequadas, para que o cliente solicitante possa distinguir rejeição de um signatário parado.

A [fonte marcada do Amber](https://github.com/greenart7c3/Amber/tree/v6.4.0) também adiciona rótulos localizados e legíveis por humanos para mais 113 kinds de evento em todos os locales publicados. As adições incluem eventos de grupo Concord, favoritos de repositório Git NIP-51 e eventos de presença em sala NIP-53, dando aos usuários mais contexto sobre dados desconhecidos antes de aprovar uma assinatura. Um guarda de mapa concorrente também corrige uma falha de inscrição em relay que podia produzir um `NegativeArraySizeException`.

### Safebox Acorn separa um componente portátil de recuperação do aplicativo web

O [Safebox Acorn](https://github.com/trbouma/safebox-acorn) é um componente Python autônomo e interface de linha de comando para salvaguardar chaves, fundos e registros controlados pelo usuário com estado respaldado por Nostr. Extrair o Acorn do aplicativo web Safebox mais amplo permite que outro projeto Python instale o runtime e use seus helpers de chave, perfil Nostr, relay, registro, Cashu, Lightning e criptográficos sem assumir a interface web. Suas primitivas atuais de proteção de registros podem gerar uma chave fresca de 256 bits, derivar uma a partir de entropia fornecida separadamente e codificar a chave exata como uma frase de recuperação de 24 palavras com checksum.

O [guia de recuperação e continuidade](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/) do projeto enquadra o Acorn como o componente de protocolo substituível dentro de um Safebox doméstico ou comunitário. O design mantém estado criptografado disponível por meio de um relay local e réplicas independentes, de modo que a recuperação não dependa de um único aparelho, aplicativo, relay, mint ou provedor de serviço. A documentação é cuidadosa quanto ao limite atual: a criptografia de registros protegidos permanece em design, portanto aplicativos não devem fazer registros dependerem da nova chave de proteção de registros até que esse perfil tenha sido implementado e revisado.


## Lançamentos com tag

### Mostro Core 0.14.2 altera o envelope de chat criptografado

O [Mostro Core](https://github.com/MostroP2P/mostro-core) é a biblioteca Rust de tipos compartilhados e funções peer-to-peer usada pelo daemon de exchange Mostro e seus clientes. A [versão 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) substitui mensagens de chat gift-wrapped por envelopes kind 14 que usam chaves separadas de criptografia de conversa e de assinatura derivadas do segredo compartilhado dos pares. O novo leitor valida o autor, a assinatura, o destinatário, o timestamp e o tamanho do conteúdo, enquanto helpers legados de gift-wrap permanecem disponíveis para que clientes possam ler ambos os formatos durante a migração.

### Mostro 0.18.1 inicia um caminho de escrow Cashu e endurece o daemon

O [Mostro](https://github.com/MostroP2P/mostro) é um daemon de exchange Lightning peer-to-peer que coordena ordens por meio do Nostr. A [versão 0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1) lança a base para um backend de escrow Cashu, incluindo configuração, helpers de banco de dados, integração com mint, wiring de inicialização e a primeira ação de lock. Ele também pode usar preços anunciados por um nó confiável sobre Nostr e anuncia requisitos de proof-of-work para primeiro contato em seu evento de info substituível. O lançamento atualiza sua dependência Nostr para uma correção de negação de serviço do NIP-44, remove chaves privadas de logs de sessão de restauração, rejeita mensagens de cancelamento cooperativo não autorizadas, endurece buscas LNURL contra server-side request forgery e travamentos, valida faturas de payout e restaura inscrições de hold invoice após reinicialização.

### LaWallet NWC 2.3.0 adiciona notificações Nostr e recibos de zap

O [LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) é uma plataforma Lightning Address de código aberto que conecta carteiras por meio do [Nostr Wallet Connect](/pt/topics/nip-47/). A [versão 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) permite que cada carteira envie notificações de recebimento e encaminhamento como eventos Nostr configuráveis, incluindo uma tag `p` de destinatário, relays selecionados, conteúdo templado e criptografia opcional [NIP-44](/pt/topics/nip-44/) (payloads criptografados); novas tentativas reutilizam o mesmo ID de evento assinado. Ele também aceita zap requests e publica recibos kind 9735 assinados do [NIP-57](/pt/topics/nip-57/) (zaps) após liquidação, enquanto uma nova visualização de capacidade de endereço mostra se o endereço resolvido suporta NIP-05, NIP-57 e protocolos Lightning Address relacionados.

### nostr-double-ratchet TypeScript 0.0.166 vincula convites públicos a chaves de sessão

O [nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet) fornece primitivas TypeScript e Rust para mensagens diretas e em grupo criptografadas de ponta a ponta sobre relays Nostr. O [TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) exige que uma resposta a convite prove posse de sua chave de sessão, impedindo que um convite público reutilizável vincule uma identidade Nostr à sessão de outra parte. O lançamento também rejeita campos rumor malformados e reforça a validação de payload; sessões existentes continuam funcionando, mas um convidador atualizado rejeita respostas sem prova de convidados mais antigos.

### cln-nip47 0.2.0 expande e isola requisições NWC

O [cln-nip47](https://github.com/daywalker90/cln-nip47) é um plugin Core Lightning que expõe um nó a carteiras por meio do [Nostr Wallet Connect](/pt/topics/nip-47/). A [versão 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) adiciona métodos NWC para criar, cancelar e liquidar hold invoices, além de uma notificação `hold_invoice_accepted`, e anuncia o conjunto de métodos que o nó conectado realmente suporta. Respostas de lista de transações agora param em 500 entradas e cerca de 128 kB, eventos de requisição são deduplicados por ID de evento, e a falha de notificação de um cliente não impede mais a entrega a outros clientes. O lançamento também remove os dois métodos de multipagamento que não fazem mais parte da especificação NWC.

### ClipRelay 0.1.3 restaura conexões de relay e signatário após períodos ociosos

O [ClipRelay](https://github.com/tajava2006/cliprelay) sincroniza a área de transferência de um usuário entre dispositivos por meio de relays Nostr, criptografando o conteúdo para a mesma identidade com [NIP-44](/pt/topics/nip-44/) (payloads criptografados). Os lançamentos [desktop](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) e [Android](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3) 0.1.3 adicionam uma caixa de texto para enviar texto digitado diretamente para a área de transferência de outro dispositivo. Eles também testam vivacidade com round trips reais de relay após períodos ociosos, escalando de reinscrição a substituição de socket e um pool de conexões reconstruído, enquanto chamadas de signatário [NIP-46](/pt/topics/nip-46/) (assinatura remota) paradas agora expiram e reconstruem automaticamente.

### NoorNote 1.3.2 move a descoberta de artigos para o grafo social

O [NoorNote](https://github.com/77elements/noornote) é um cliente Nostr para publicações sociais, mensagens criptografadas, artigos longos e outros tipos de evento em web, desktop e Android. A [versão 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) substitui seu feed global plano de artigos por descoberta extraída de contatos de primeiro, segundo e terceiro grau, dando aos leitores uma linha do tempo de artigos enraizada em seu grafo de seguidos. Ele também colapsa rajadas de mensagens diretas repetidas de remetentes desconhecidos em uma única notificação contínua em vez de produzir uma pilha de toasts conforme o histórico do relay chega.

### Bray 2.4.0 adiciona um dialeto compacto de assinatura remota

O [Bray](https://github.com/forgesworn/bray) é um servidor Nostr MCP que oferece a agentes de software e pessoas ferramentas para acesso a relays, identidade, publicação e assinatura remota. A [versão 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) aceita uma requisição de assinatura cujo evento é um objeto, além da forma stringificada usada pelo [NIP-46](/pt/topics/nip-46/), e adiciona `sign_event_compact`, que retorna apenas o ID do evento, a assinatura, a chave pública e o timestamp. Esse formato menor de requisição e resposta reduz o uso de memória para signatários de hardware restritos, enquanto o fluxo padrão `sign_event` permanece inalterado e ambos os dialetos produzem uma assinatura sobre o ID do evento recebido.


## Recém-descobertos

### Pact traz vínculos de agentes mutuamente consentidos ao Nostr

O [Pact](https://github.com/bobodread876/pact), recém-descoberto esta semana, é uma camada de relacionamento em estágio inicial para agentes de software construída sobre MATE.md e um transporte draft NIP-BD. Seus vínculos assinados e mutuamente consentidos são mantidos pelas próprias chaves dos agentes e podem ser publicados sobre Nostr, enquanto vínculos privados usam gift wrapping do [NIP-59](/pt/topics/nip-59/) (metadados ocultos). O monorepo inclui um servidor MCP, SDK TypeScript, cliente de linha de comando, daemon auto-hospedável e interface web. Sua atividade mais recente no repositório é anterior à janela semanal desta edição, portanto esta é uma nota de descoberta e não uma alegação de novo lançamento.


## Em desenvolvimento

### nostrord mantém silenciamento de grupo sincronizado entre dispositivos

O [nostrord](https://github.com/nostrord/nostrord) é um cliente multiplataforma para comunidades gerenciadas por relays. O [PR #250](https://github.com/nostrord/nostrord/pull/250) armazena as escolhas de silenciamento por grupo de cada conta em um evento kind `30078` auto-criptografado do [NIP-78](/pt/topics/nip-78/) (dados específicos de aplicativo), de modo que uma configuração feita em um dispositivo possa seguir o usuário para outro sem revelar a lista de grupos ao relay. O registro substituível usa ordenação por evento mais recente, escuta mudanças ao vivo e reverte a interface quando assinatura ou publicação falha, em vez de deixar o estado local dessincronizado. Grupos silenciados também deixam de contribuir com totais visíveis de não lidos, mantendo sua posição de não lidos para a próxima visita.

### Amethyst completa o ciclo de vida de convites do Concord

O [Amethyst](https://github.com/vitorpamplona/amethyst) é um cliente Nostr Android cujo suporte a comunidades criptografadas implementa o protocolo Concord. O [PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) permite que links de convite sobrevivam a um refounding de comunidade reemitindo seus bundles nas mesmas coordenadas endereçáveis, enquanto uma verificação de ban impede que um membro removido use esse caminho de recuperação. Ele também implementa a lista de convites criptografada CORD-05 tanto no aplicativo quanto no cliente de linha de comando `amy`, adiciona tombstones de revogação por link, e exige confirmação do relay antes de excluir a única chave de assinatura armazenada que pode aposentar um link. O mesmo trabalho dá ao `amy` os caminhos de entrega de control key, refounding, rekeying e recuperação de membros isolados necessários para seguir epochs posteriores da comunidade.

### Buzz transporta a aparência de cada comunidade entre desktop e mobile

O [Buzz](https://github.com/block/buzz) é um workspace comunitário baseado em Nostr com clientes desktop e mobile. Os PRs mergeados de desktop [PR #3653](https://github.com/block/buzz/pull/3653) e mobile [PR #3767](https://github.com/block/buzz/pull/3767) armazenam o tema, o destaque e a escolha de modo do sistema de cada comunidade como um registro NIP-78 criptografado no relay dessa comunidade. Ambos os clientes compartilham o mesmo payload versionado e mantêm caches locais com escopo de identidade, de modo que mudar de comunidade ou conta não possa aplicar a aparência errada enquanto o relay está indisponível. Ordenação de substituição, escritas protegidas e reinscrição após conexão fechada permitem que os dois clientes converjam novamente após reconectar.

O [Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10) veio antes do corte desta edição com uma passagem de desempenho e confiabilidade. Ele remove regressões introduzidas após a 0.5.9, acelera o carregamento de canais, limita a retenção inicial da linha do tempo, coalesce a persistência de estado de leitura, preserva linhas do tempo frescas de canal e impede que o worker de ingestão de relay falhe em reações a eventos de projeto. Ele também adiciona o envio de uma mensagem de thread para um canal e restringe a busca desktop ao escopo pretendido.


## Trabalho em protocolos e especificações

### NIPs

O [NIPs PR #2435](https://github.com/nostr-protocol/nips/pull/2435) é uma emenda aberta ao NIP-34, que padroniza colaboração em repositórios git por meio de eventos Nostr. Ele adiciona uma tag `b` opcional a um evento de pull request para que o autor possa nomear um branch de destino diferente do padrão do repositório. A proposta corresponde ao suporte já implementado no ngit e no GitWorkshop, mas ainda não entrou na especificação.

O [NIPs PR #2434](https://github.com/nostr-protocol/nips/pull/2434) é uma proposta aberta para chaves de identidade pós-quânticas. Ela deriva chaves pós-quânticas de criptografia e assinatura ao lado da chave secp256k1 existente a partir de uma seed de derivação de chaves mnemônica NIP-06 e, em seguida, vincula as chaves públicas à identidade Nostr com uma atestação kind `10203`. O rascunho limita sua reivindicação a proteger a confidencialidade de mensagens anteriores se o secp256k1 for quebrado posteriormente; ele não substitui as assinaturas de eventos atuais.

O [NIPs PR #2431](https://github.com/nostr-protocol/nips/pull/2431) é uma emenda aberta ao NIP-07 para signatários de navegador. Um cliente poderia anexar a chave pública que espera a requisições de assinatura ou criptografia, exigindo que o signatário use essa conta ou rejeite a chamada. Isso impediria que uma página continuasse silenciosamente sob uma identidade diferente depois que o usuário troca de conta no signatário.

O [NIPs PR #1813](https://github.com/nostr-protocol/nips/pull/1813) permanece uma proposta aberta de double-ratchet após trabalho substancial durante a janela. Ela especifica conversas criptografadas com forward secrecy cujas chaves avançam com as mensagens, com uma implementação já disponível na biblioteca nostr-double-ratchet e no Iris. Ainda é um rascunho, não um NIP mergeado.

O [NIPs PR #2433](https://github.com/nostr-protocol/nips/pull/2433) abriu e fechou sem merge durante a janela. Ele propôs esclarecer erros de relay do NIP-42 para que `auth-required` significasse que outra autenticação poderia alterar o resultado, enquanto `restricted` significaria que não poderia. A distinção tratava de conexões autenticadas para uma chave, mas ainda sem autorização para outra; o status fechado significa que a redação não entrou na especificação.

O [NIPs PR #2378](https://github.com/nostr-protocol/nips/pull/2378), coberto anteriormente enquanto ainda proposto, agora fechou sem merge. Seus eventos propostos de passaportes de agente, descoberta, tarefa, marketplace, fatura e conexão permanecem, portanto, fora do conjunto de NIPs.

O [NIPs commit 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab) mergeou uma correção apenas documental ao NIP-29. Ele adiciona uma tag `previous` ao exemplo de metadados de grupo, mostrando como um evento de substituição pode identificar o evento que substitui. Isso esclarece um exemplo e não introduz um novo recurso de protocolo.

### Concord e CORDs

O [CORD PR #18](https://github.com/concord-protocol/concord/pull/18) fragmentaria Community Lists criptografadas entre eventos kind `33302`, removeria o limite de 50 associações e podaria entradas aposentadas para permanecer dentro dos limites de relay. Duas outras propostas abertas adicionam [localizadores de menção privada](https://github.com/concord-protocol/concord/pull/16) e um [sinal de pausa](https://github.com/concord-protocol/concord/pull/17) que suspende o chat sem descartar mensagens.

O [CORD-02 PR #15](https://github.com/concord-protocol/concord/pull/15) mergeou em 6 de agosto e restringe escritas ao plano de controle de uma comunidade. Proprietários e equipe detêm um novo segredo de assinatura `control_root`, enquanto todos os membros retêm a chave pública derivada e a read key necessárias para verificar e descriptografar o estado de moderação. A write key é uma barreira contra spam, não um substituto para as assinaturas internas de ator e verificações de roster que estabelecem autoridade.

O [CORD PR #12](https://github.com/concord-protocol/concord/pull/12), coberto anteriormente como rascunho aberto, agora fechou sem merge. Sua porção de plano de controle foi substituída pela emenda CORD-02 mais estreita mergeada acima, enquanto canais de escrita restrita e o restante do material de rascunho não entraram na especificação.

## Mergulho Profundo em NIPs

### Solicitações de Exclusão de Eventos (NIP-09)

O [NIP-09](/pt/topics/nip-09/) (solicitações de exclusão de eventos), definido pela [especificação primária](https://github.com/nostr-protocol/nips/blob/master/09.md), dá a um autor de evento uma forma assinada de pedir a relays e clientes que parem de servir um ou mais eventos desse autor. Ele não apaga todas as cópias. Ele transporta a intenção do autor pela mesma rede de relays que distribuiu o evento original.

A requisição é um evento kind `5` assinado comum. Suas tags contêm uma ou mais referências `e` a IDs de evento específicos ou referências `a` a coordenadas de eventos endereçáveis, e as [regras de tag do NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request) dizem que deve incluir uma tag `k` para cada kind de evento referenciado. O `content` opcional pode explicar o motivo. Para uma referência `a`, um relay deve remover toda versão naquela coordenada cujo timestamp não seja posterior ao `created_at` da requisição, o que impede que uma requisição de exclusão antiga suprima uma substituição posterior.

[A autoria é a fronteira de segurança](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior). Um relay deve parar de publicar um evento referenciado apenas quando seu `pubkey` corresponder ao `pubkey` da requisição de exclusão, e um cliente deve executar essa verificação antes de ocultar um evento. Um relay pode não possuir o evento referenciado e, portanto, pode ser incapaz de validar o relacionamento ao aceitar a requisição, de modo que clientes não podem tratar a aceitação do relay como prova de que a exclusão foi autorizada. A especificação também pede que relays retenham a requisição kind `5`, porque outro cliente pode já possuir o evento original e encontrar a requisição depois.

Aqui está um [evento kind `5` assinado](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943):

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

A exclusão permanece uma política cooperativa, não revogação de um objeto assinado. Um relay, cache, screenshot ou cliente offline pode preservar os bytes originais, e excluir a própria requisição kind `5` não a desfaz. Clientes podem ocultar o alvo, marcá-lo como desautorizado ou exibir o motivo da requisição, mas devem dizer aos usuários que a exclusão universal não pode ser garantida. Isso difere do [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), onde uma tag `expiration` pede a relays que parem de armazenar um evento após um horário escolhido quando o evento é publicado. O NIP-09 trata de uma decisão posterior do autor e pode apontar para eventos já distribuídos.

Implementações atuais aplicam essa política em camadas diferentes. O [Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623) remove vídeos excluídos do armazenamento de eventos do cliente, o [strfry PR #251](https://github.com/hoytech/strfry/pull/251) estende requisições válidas de exclusão a destinatários gift-wrap, e o [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) declara suporte ao NIP-09 em seu cliente. O [cliente de grupo do nostrord](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) oferece outro caminho de implementação atual.

### Denúncias (NIP-56)

O [NIP-56](/pt/topics/nip-56/) (eventos de denúncia), definido pela [especificação primária](https://github.com/nostr-protocol/nips/blob/master/56.md), padroniza uma denúncia assinada sobre uma conta, evento ou blob referenciado. Ele separa o sinal de denúncia da decisão de moderação, permitindo que cada cliente ou relay escolha quais denunciantes confia e qual resposta se encaixa em sua política.

Uma denúncia usa kind `1984` e deve identificar a conta denunciada em uma tag `p`. Denunciar uma nota também exige uma tag `e` para o ID do evento. O terceiro valor da tag carrega uma das categorias especificadas: `nudity`, `malware`, `profanity`, `illegal`, `spam`, `impersonation` ou `other`. Uma denúncia sobre um blob pode usar seu hash em uma tag `x`, uma tag `e` para o evento que referenciou o blob, e uma tag `server` opcional para um local. Tags `L` e `l` opcionais do [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) (rotulagem) podem adicionar um rótulo com namespace quando a lista fixa de categorias não é precisa o suficiente.

[O evento prova apenas que uma chave fez uma alegação](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting). O conteúdo denunciado não se torna falso, ilegal ou removível apenas porque existe um kind `1984` válido, e um relay aberto não pode contar com segurança denúncias anônimas como votos. A especificação desaconselha moderação automática de relay porque denúncias são fáceis de manipular, enquanto permite que administradores de relay ajam sobre denúncias de moderadores em quem já confiam. Um cliente pode, em vez disso, ponderar denúncias pelo grafo social de um usuário, por exemplo borrando conteúdo depois que vários contatos confiáveis sinalizam a mesma conta.

Aqui está um [evento kind `1984` assinado](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2):

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56 e NIP-09 resolvem problemas diferentes](https://github.com/nostr-protocol/nips/tree/master). Uma denúncia kind `1984` pode mirar a conta ou evento de outra pessoa, mas não confere autoridade de exclusão. Uma requisição kind `5` expressa a intenção do autor original e é válida apenas contra os próprios eventos desse autor. Nenhuma garante remoção: o NIP-56 delega deliberadamente a ação à política local de moderação, enquanto o NIP-09 depende de relays e clientes honrarem uma requisição autenticada.

Implementações expõem essas escolhas em produtos diferentes. O [Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591) corrige a entrega de denúncias em um cliente de vídeo curto, o [Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) lê denúncias como contexto limitado para participantes de marketplace, e o [módulo NIP-56 do nostrord](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) publica e processa eventos de denúncia. O [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support) também lista suporte atual ao NIP-56.


---

Envie uma DM NIP-17 para compartilhar um projeto ou notícia por meio do [projeto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
