---
title: "Nostr Compass #38"
date: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
---

Bem-vindos de volta ao [Nostr Compass](https://nostrcompass.org), o seu guia semanal do Nostr.

**Esta semana:** o [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0 leva notas do Nostr verificadas e assinaturas de conteúdo longo a um leitor Android offline que lê artigos em voz alta, o [nostream](https://github.com/cameri/nostream) amplia o roteamento de tarefas no lado do relay e a operação autenticada, o [NDK for Dart](https://github.com/relaystr/ndk) corrige a negentropy e o tempo de vida de solicitações para vários relays, o [Divine Mobile](https://github.com/divinevideo/divine-mobile) torna determinísticos a exclusão e o processo de assinatura de mensagens envolvidas, o [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) protege por padrão as caixas de entrada de gift wraps, o [Amethyst](https://github.com/vitorpamplona/amethyst) lança destaques portáteis, e o [Mostro](https://github.com/MostroP2P/mostro) verifica ordens assinadas antes do seu filtro de spam. O [Napstr](https://github.com/lnbits/napstr) publica catálogos de áudio e sinais de atividade de seeders pelo Nostr enquanto transfere arquivos via Tor. Os lançamentos incluem o [MDK](https://github.com/marmot-protocol/mdk) e o [pakstr](https://git.nostrdev.com/stuff/pakstr); o trabalho de protocolo incorpora uma dica de paginação do [NIP-67](/pt/topics/nip-67/) e um esquema de tags de destaque do [NIP-84](/pt/topics/nip-84/) no [repositório de NIPs](https://github.com/nostr-protocol/nips), enquanto o [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc) adiciona totais de transações; e o Mergulho Profundo em NIP acompanha reposts e reações em seus formatos de event e implementações atuais.

## Histórias principais

### Voca 1.0 lê em voz alta notas e assinaturas verificadas do Nostr no Android

O [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) é um leitor Android offline que lê em voz alta artigos, PDFs, arquivos Markdown e notas do Nostr usando a própria voz de conversão de texto em fala do celular, enquanto a frase falada permanece iluminada na página. Seu [lançamento 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en), [publicado em 2026-08-27](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) com sua própria [chave de projeto](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu), torna o Nostr uma fonte de primeira classe: cole o endereço de uma nota, um identificador de event, um npub, um perfil ou um link comum da web que contenha uma entidade Nostr, e o aplicativo decodifica a referência, busca o event assinado nos relays e lê o texto do autor em vez da página web criada ao redor dele.

Dois comportamentos verificados definem a integração com o Nostr, ambos descritos no [anúncio assinado do Voca 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en). Primeiro, cada event buscado é conferido com seu id recalculado e sua assinatura Schnorr BIP-340 antes de ser persistido, usando os relays de bootstrap, a lista de relays [NIP-65](/pt/topics/nip-65/) do autor (um event kind `10002`, assinado e substituível, no qual o autor relaciona os relays que lê e nos quais escreve) e as dicas contidas na própria referência; assim, um relay pode recusar-se a responder, mas não pode colocar palavras na boca do autor. Segundo, adicionar o npub de um autor coloca seus artigos longos [NIP-23](/pt/topics/nip-23/) (publicações endereçáveis kind `30023` com títulos, resumos e imagens) em uma única caixa de entrada no dispositivo, ao lado de feeds RSS e Atom. A atualização 1.1.0, [anunciada em 2026-08-28](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca) e publicada no [Zapstore](https://zapstore.dev) em 2026-08-29, sincroniza a rolagem por frase, suaviza documentos longos e recupera o widget da tela inicial após rolagem manual, redimensionamento, reinicializações do processo e atualizações.


### nostream amplia o roteamento de DVM no lado do relay e a operação autenticada

Depois do [trabalho de ingestão de tarefas de 19 de agosto](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes), o [nostream](https://github.com/cameri/nostream), uma implementação de relay em TypeScript, [armazena e fornece events de manipuladores de aplicações NIP-89](https://github.com/cameri/nostream/pull/737). O [NIP-89](/pt/topics/nip-89/) (descoberta de manipuladores de aplicações) usa recomendações kind `31989` e informações de manipuladores kind `31990`, ambas já no intervalo parametrizado e substituível, para que um cliente possa consultar esses kinds e receber uma substituição quando houver colisão de uma tag `d`. O relay não publica informações de manipuladores para seus próprios workers.

Tarefas pendentes de [NIP-90](/pt/topics/nip-90/) (data vending machine) agora [chegam a um processo worker e retornam como events de resultado](https://github.com/cameri/nostream/pull/734). Em caso de sucesso, o relay assina um resultado kind 6000-6999 com sua própria chave. Um timeout ou uma falha do worker marca a tarefa como falha, em vez de deixá-la como enviada.

Sessões autenticadas e chamadas HTTP administrativas ficam em limites distintos. O [NIP-42](/pt/topics/nip-42/) (autenticação de clientes em relays) [acompanha a pubkey autenticada por socket](https://github.com/cameri/nostream/pull/716), pode exigir AUTH antes que clientes publiquem events e anuncia essa exigência no documento [NIP-11](/pt/topics/nip-11/) (informações do relay), com os dois controles desativados por padrão. Separadamente, [as rotas da API administrativa podem aceitar autorização HTTP assinada com NIP-98](https://github.com/cameri/nostream/pull/730). O [NIP-98](/pt/topics/nip-98/) (autenticação HTTP com events assinados) permanece desativado até que um operador o habilite e indique as pubkeys permitidas.

### NDK for Dart corrige negentropy, tempo de vida de solicitações para vários relays e verificação de assinaturas

Uma execução do [NIP-77](/pt/topics/nip-77/) (reconciliação de conjuntos por negentropy) no [NDK](https://github.com/relaystr/ndk), um kit de desenvolvimento em Dart para Nostr, retornava os conjuntos incorretos de itens presentes e necessários sem informar erro, porque o codec não era compatível com a v1 do protocolo [negentropy](/pt/topics/negentropy/). A [correção da codificação v1](https://github.com/relaystr/ndk/pull/722) agora retorna os ids mantidos pelo relay e os ids dos quais ele ainda precisa.

Filtros idênticos enviados a relays diferentes [eram combinados em uma única solicitação](https://github.com/relaystr/ndk/pull/705). Solicitações com o mesmo filtro agora permanecem distintas quando têm como destino relays diferentes ou têm tempos de vida diferentes, de modo que uma consulta curta não pode misturar events de outro relay ao resultado nem deixar uma assinatura ativa travada.

O mesmo kit [verifica uma assinatura uma vez e mantém o resultado](https://github.com/relaystr/ndk/pull/726). Uma entrega duplicada posterior deixa de gastar outra verificação ou sobrescrever o event verificado armazenado.

### Divine Mobile torna determinísticos a exclusão e o processo de assinatura de mensagens diretas envolvidas

Events kind `5` envolvidos do [NIP-09](/pt/topics/nip-09/) (solicitação de exclusão de event) que apontavam para uma mensagem nunca eram aplicados no [Divine Mobile](https://github.com/divinevideo/divine-mobile), um cliente móvel de vídeos curtos que publica pelo Nostr. O cliente [agora resolve cada exclusão com base na mensagem indicada](https://github.com/divinevideo/divine-mobile/pull/8174), em vez de tratar tudo o que não é uma reação como já processado. Uma segunda [solicitação de exclusão para todos enquanto a primeira ainda estava em andamento](https://github.com/divinevideo/divine-mobile/pull/8164) desaparecia sem erro e sem um kind `5` na rede; agora, exclusões simultâneas são publicadas individualmente.

Após o lançamento 1.0.22, já abordado, o envio do mesmo texto 1:1 de [NIP-17](/pt/topics/nip-17/) (DMs privadas em gift wraps) duas vezes no mesmo segundo [gerava um único id de rumor](https://github.com/divinevideo/divine-mobile/pull/8163), fazendo o segundo envio desaparecer; agora, cada envio carrega um token dentro do rumor de [NIP-59](/pt/topics/nip-59/) (gift wrap), para que os ids sejam diferentes.

Um chamador que já havia assinado um event kind `4` ou kind `5` [manteve essa assinatura](https://github.com/divinevideo/divine-mobile/pull/8173), em vez de receber uma tag de cliente anexada depois, o que alterava o id e fazia os relays rejeitarem o event como inválido.

### Conduit Relay reforça sua caixa de entrada protegida pelo NIP-42

Gift wraps kind `1059` são armazenados para um destinatário. O [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay), um relay em Go que mantém esses wraps em uma caixa de entrada protegida por destinatário, [adota o modo de imposição por padrão](https://github.com/Conduit-BTC/conduit-relay/pull/8): uma consulta kind `1059` deve apresentar autenticação [NIP-42](/pt/topics/nip-42/) como esse destinatário, ou o relay rejeita a solicitação. Filtros de vários kinds, curingas, contagens e [negentropy](/pt/topics/negentropy/) sobre esses wraps são `restricted`, de modo que outra AUTH não possa transformá-los em um despejo da caixa de entrada de outra pessoa.

A mesma [incorporação da caixa de entrada protegida](https://github.com/Conduit-BTC/conduit-relay/pull/8) exige um id de event canônico no event AUTH transmitido e aceita um event NIP-42 válido mesmo que `content` esteja vazio. O modo somente desafio ainda oferece AUTH sem bloquear a leitura; o modo desativado permite acesso livre. O padrão da biblioteca é imposição.

### Amethyst lança destaques NIP-84 e corrige dois caminhos de falha voltados aos relays

Depois do [trabalho de autorização do Blossom da semana passada](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads), o [Amethyst](https://github.com/vitorpamplona/amethyst), um cliente Nostr para Android, lança a [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0) com [NIP-84](/pt/topics/nip-84/) (destaques portáteis). Um trecho selecionado se transforma em um event kind `9802` por meio do compositor, de um feed de destaques ou de um compartilhamento para o aplicativo.

O lançamento adiciona controles de exclusão e arquivamento de canais [NIP-29](/pt/topics/nip-29/) ([PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)) e mede o comportamento dos relays por meio do tráfego que o cliente já realiza, depois amplia essas sondagens [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) com verificações de streaming, leitura, escrita e URL ([PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836), [PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)). O Amethyst também elimina uma vulnerabilidade de colisão de hash no SharedKeyCache e compara códigos de autenticação de mensagens em tempo constante ([PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)), corrige uma condição de corrida que podia perder a entrega de AUTH no momento da conexão ([PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)), distribui o bloqueio do estado de assinaturas para encerrar um comboio de ANRs ([PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)) e compara todos os filtros de assinatura em vez de apenas o primeiro ([PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)).

[A Newsletter #36 já abordou essas mudanças de autenticação em relays, backup e chat público](/en/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow); agora, a v1.14.0 lançou todas juntas. Soft bans do Concord fecham lacunas de autoridade encontradas por uma auditoria ([PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)). A autenticação em relays ganhou um fluxo de permissões redesenhado ([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)), aguarda a resolução do desafio em vez de atingir um timeout ([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)), configura novas contas para autenticar por padrão ([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), respeita essa preferência em relays fora do conjunto normal da conta ([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)) e mantém as concessões de sessão entre reconexões ([PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)). Um fluxo guiado de primeira execução e Configurações facilita encontrar os backups de chaves ([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)), o preenchimento retroativo de proofs do Cashu e a paginação do histórico impedem que os saldos da carteira sejam truncados ([PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)), e agora chats públicos podem ser silenciados ([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)).

Após essa tag, [listas confiáveis](https://github.com/vitorpamplona/amethyst/pull/3983) nos kinds `30392` a `30395` são indexadas pela busca de texto completo [NIP-50](/pt/topics/nip-50/) somente pelo título, de modo que uma lista citada em texto possa ser encontrada sem indexar os ids hexadecimais dos membros. Recusas de carteiras que chegaram via [NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect) [agora exibem o erro em vez de parecerem um toque que não fez nada](https://github.com/vitorpamplona/amethyst/pull/3987), incluindo `QUOTA_EXCEEDED` e `RESTRICTED`, além de um timeout quando a carteira nunca responde.

### Mostro valida ordens assinadas antes de operações dispendiosas e preserva events de auditoria das ordens

Depois da [base para escrow do Cashu da v0.18.1](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon), o [Mostro](https://github.com/MostroP2P/mostro), um daemon de exchange peer-to-peer que coordena ordens pelo Nostr, marcou a [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5), que usa por padrão o [NIP-44](/pt/topics/nip-44/) (cifragem de payload) para o transporte e mantém o gift wrap como adesão explícita.

O lançamento vincula os timeouts do estado de espera ao momento de tomada registrado para que um título do maker não seja penalizado com base no relógio errado ([PR #879](https://github.com/MostroP2P/mostro/pull/879)), despacha no máximo uma vez o pagamento ao comprador de cada ordem liquidada ([PR #881](https://github.com/MostroP2P/mostro/pull/881)) e encaminha esses pagamentos por esperas `send_payment` limitadas e não bloqueantes ([PR #883](https://github.com/MostroP2P/mostro/pull/883)). Uma tentativa de alteração para pagar o vencedor da penalidade por timeout ([PR #875](https://github.com/MostroP2P/mostro/pull/875)) foi revertida antes do lançamento da mesma tag ([PR #885](https://github.com/MostroP2P/mostro/pull/885)). O Mostro também deixa de republicar um livro de ordens pendentes inalterado a cada hora e na inicialização ([PR #888](https://github.com/MostroP2P/mostro/pull/888)), e seus events de disputas kind `38386` agora carregam uma tag `created_at` para ordenação posterior ([PR #878](https://github.com/MostroP2P/mostro/pull/878)).

Depois dessa tag, uma [verificação de assinatura agora é executada antes do filtro de spam](https://github.com/MostroP2P/mostro/pull/892). Um id de event não se compromete com `sig`, portanto uma cópia do kind `14` de uma vítima com assinatura inválida podia ocupar o espaço de repetição e descartar silenciosamente a mensagem válida; o daemon verifica primeiro e descarta um wrap inválido em vez de emitir um aviso e prosseguir.

Events de auditoria de taxas kind `8383` carregavam um [NIP-40](/pt/topics/nip-40/) (timestamp de expiração) de 15 dias. Agora eles [mantêm uma expiração de um ano](https://github.com/MostroP2P/mostro/pull/924), condizente com sua função de registro público de pagamentos. Em um nó com Cashu habilitado, tomar uma ordem [pede ao vendedor pelo Nostr que bloqueie um escrow 2 de 3](https://github.com/MostroP2P/mostro/pull/830), publica o event da ordem em espera e não cria uma fatura hold da Lightning. Isso completa o caminho da solicitação; por si só, não resolve todos os casos de escrow ou abuso no marketplace.

### Napstr publica catálogos de áudio no Nostr e transfere arquivos via Tor

O [Napstr](https://github.com/lnbits/napstr) é um cliente para desktop de compartilhamento de áudio que publica catálogos pesquisáveis e seeders ativos no Nostr, depois transfere os arquivos por um processo Tor integrado sem fallback para IP direto. A [versão 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) mantém públicos os perfis e metadados de catálogo, enquanto mantém solicitações, credenciais de transferência, conteúdo dos arquivos e endereços IP dos pares fora dos relays.

A descoberta usa dois kinds de events endereçáveis no [repositório do Napstr](https://github.com/lnbits/napstr). Entradas de catálogo kind `30421` identificam um arquivo por seu digest SHA-256, basename público, tamanho e formato de áudio, e um autor retira um arquivo substituindo essa coordenada por um marcador de exclusão. Sinais de atividade de disponibilidade kind `30422` expiram após dez minutos e relacionam os ids dos arquivos que o autor está disposto a semear, de modo que uma linha do catálogo só permanece ativa enquanto um sinal de atividade não expirado ainda contiver esse digest.

A conversa pública usa o [NIP-C7](/pt/topics/nip-c7/) (mensagens de chat kind 9) em vez de um grupo pertencente a um relay. O [repositório do Napstr](https://github.com/lnbits/napstr) define uma sala pública compartilhada e uma discussão por faixa vinculada ao digest do arquivo. Essas mensagens são assinadas e públicas. Elas não carregam endereços onion, credenciais de transferência nem bytes de arquivos.

Um download começa como uma negociação por [NIP-17](/pt/topics/nip-17/) (DMs privadas em gift wraps). O [repositório do Napstr](https://github.com/lnbits/napstr) envolve uma solicitação, uma oferta ou uma recusa em um rumor kind `14`, de modo que os relays não vejam o hostname onion v3 temporário nem a capacidade de uso único retornada por uma oferta aceita. O Tor integrado então transfere os bytes por esse onion, verifica o digest SHA-256 completo e revalida o áudio antes que o arquivo possa ser reproduzido.

A [comparação da v0.1.7 com a v0.2.0](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) adiciona coleções de audiolivros e o Napstrfy, um complemento Android opcional. Manifestos kind `30423` relacionam capítulos ordenados que continuam sendo arquivos comuns do catálogo, de modo que um cliente que ignore a coleção ainda possa buscar cada capítulo. Para esse fim, o Napstr cria uma pasta Audiobooks local sem destruir conteúdo. O Napstrfy é pareado com um desktop em execução por um código QR de uso único, depois pesquisa e solicita downloads pelos serviços Nostr e Tor já existentes nesse desktop, sem receber a chave secreta dele.

A mesma [comparação](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) aplica timeout a um handshake com o complemento que não for concluído. Um seeder copia e calcula o hash do arquivo compartilhado antes de servir bytes, grava dados recebidos em um arquivo temporário privado, limita os destinos de audiolivros a um filho real da pasta do Napstr e aborta se esse destino mudar durante a transferência.

## Lançamentos

### MDK v0.9.17: KeyPackages mais recentes, atividade de membros e envios duráveis

[A Newsletter #37 abordou o MDK 0.9.14 e 0.9.15](/en/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles), incluindo a mudança no [repositório do MDK](https://github.com/marmot-protocol/mdk) da seleção do KeyPackage mais antigo primeiro para o pacote válido mais recente do perfil atual, as barreiras de recuperação de lacunas entre epochs, a limpeza de contas e a separação entre relays de descoberta e operacionais. Essas correções continuam sendo a base dos dois lançamentos seguintes, por isso um pacote desatualizado já não bloqueia um membro que publicou um pacote utilizável.

[Events de membros e administradores agora fazem a lista de chats avançar](https://github.com/marmot-protocol/mdk/pull/1551) da mesma forma que uma mensagem nova: texto de prévia, ordenação, contagens de não lidas e marcadores de leitura são atualizados quando pessoas entram, saem ou mudam de função, e o ator do sistema local não é tratado como um perfil Nostr. Reconexões e reinicializações [reutilizam uma única identidade de envio em uma nova tentativa de enviar um texto durável](https://github.com/marmot-protocol/mdk/pull/1516), para que a mesma mensagem de grupo não seja publicada duas vezes.

Os dois lançamentos desde então se concentram no custo de manter grupos grandes saudáveis. A [versão 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16) [mede a divergência de epoch a partir do epoch atual, em vez de uma marca máxima](https://github.com/marmot-protocol/mdk/pull/1559), mantém acessíveis para busca os events de entrada recusados ([PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)), limita o rollback de repetição ao estado canônico do grupo ([PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)) e introduz o [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545), uma ABI C gerada por macros sobre os bindings UniFFI que permite aos hosts incorporar o mecanismo diretamente. A [versão 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17) então reúne as varreduras de admissão em [uma passagem pelos membros, em vez de uma passagem por membro](https://github.com/marmot-protocol/mdk/pull/1617), [verifica se o estado de um grupo está em disputa sem alimentar todo o grafo de histórico](https://github.com/marmot-protocol/mdk/pull/1620), [reduz o custo da consulta ociosa na varredura de deferred peel](https://github.com/marmot-protocol/mdk/pull/1621) e [aplica a leitura de componentes em lote aos três locais de projeção ignorados pela primeira passagem](https://github.com/marmot-protocol/mdk/pull/1622). Os artefatos correspondentes [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17) e [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) são compilados a partir do mesmo commit, portanto quem os incorpora recebe em conjunto os caminhos de manutenção mais econômicos.


### pakstr v0.16.0: identificadores kind-32267 na publicação

Depois do [pipeline de publicação no Zapstore das versões 0.13.0 a 0.15.0 da semana passada](/en/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit), o [pakstr](https://git.nostrdev.com/stuff/pakstr), uma CLI que empacota um aplicativo web em um APK Android assinado e o publica com uma chave Nostr, [registra os IDs dos events de aplicação kind `32267`](https://git.nostrdev.com/stuff/pakstr/pulls/67) que consulta, publica ou substitui. A [versão 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) imprime os IDs anterior e novo quando metadados de listagem desatualizados provocam uma republicação, de modo que um publicador possa confirmar qual event de listagem está ativo no relay.

O mesmo [registro de identificadores](https://git.nostrdev.com/stuff/pakstr/pulls/67) grava o ID encontrado durante a consulta antes de qualquer substituição e depois o ID do event que chegou, portanto uma reutilização sem alterações aparece como um ID repetido. Essa é a mudança marcada na [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0); os comportamentos de Content-Digest, publicação antes do upload e validação do publicador já foram lançados nas tags anteriores.

## Mudanças ainda não lançadas

### Zap Cooking limita os relays de bunker e assina endpoints pagos

Recarregar uma sessão de bunker no [Zap Cooking](https://github.com/zapcooking/frontend), um site de receitas baseado em events longos do Nostr, publicava a conversa cifrada do [NIP-46](/pt/topics/nip-46/) (assinatura remota por relays) em todos os relays que a página já usava. [Limitar o tráfego do assinador aos relays do próprio bunker](https://github.com/zapcooking/frontend/pull/633) agora aplica essa restrição na restauração de sessão e no pareamento por nostrconnect, o fluxo de conexão iniciado pelo assinador, em correspondência com o caminho de login por URL de bunker. Ele se recusa a instalar um conjunto vazio de relays vindo de um registro armazenado malformado, de modo que os relays que apenas hospedam receitas deixem de saber que a mesma pubkey mantém uma sessão de bunker ativa.

A [autenticação HTTP assinada](https://github.com/zapcooking/frontend/pull/630) agora protege o chat pago do assistente de culinária, a introdução do livro de receitas e as atualizações de receitas restritas conforme o [NIP-98](/pt/topics/nip-98/) (autenticação HTTP com um event Nostr assinado). O servidor lê o corpo da solicitação uma vez, verifica a assinatura com esse payload exato e obtém a identidade do event de autenticação verificado, em vez de uma chave pública fornecida no corpo. A prévia do chat continua funcionando sem cabeçalho, enquanto uma assinatura presente, mas inválida, é rejeitada, e a introdução do livro de receitas sempre exige uma assinatura. Atualizar uma receita restrita agora também exige que a chave verificada corresponda ao autor armazenado; qualquer outra pessoa é informada de que a receita não existe, assim o endpoint não confirma quais registros pagos existem.

### nostrord corrige DMs envolvidas e links de events compartilhados

Depois da [v2.9.0 da semana passada](/en/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media), o [nostrord](https://github.com/nostrord/nostrord), um cliente multiplataforma para comunidades hospedadas em relays, incorporou correções de entrega para que uma DM privada [NIP-17](/pt/topics/nip-17/) (em gift wrap) enviada de um dispositivo chegue à mesma conta em outro. [Publicar de forma independente a cópia do remetente para si mesmo](https://github.com/nostrord/nostrord/pull/295) impede que a primeira aceitação do wrap do destinatário por um relay descarte a cópia que outros dispositivos buscam. A mesma mudança reenvia um wrap depois que a autenticação [NIP-42](/pt/topics/nip-42/) (autenticação de clientes em relays) é concluída e marca o envio como bem-sucedido na primeira aceitação por um relay, para que um host com falha não possa travar os demais. [Novas tentativas de gift wraps estacionados](https://github.com/nostrord/nostrord/pull/297) cuja decifragem por [NIP-59](/pt/topics/nip-59/) (gift wrap) falhou agora ocorrem com um temporizador, para que um bunker que permanece conectado não deixe essas mensagens au... [truncated]

Uma resposta [NIP-C7](/pt/topics/nip-c7/) (mensagens de chat kind `9`) repete seu pai como um ponteiro `nevent` [NIP-19](/pt/topics/nip-19/) (entidades codificadas em bech32) inicial ao lado da tag `q`. [Remover esse ponteiro inicial para o pai](https://github.com/nostrord/nostrord/pull/292) quando ele abre o corpo e identifica o pai da resposta permite que a linha seja renderizada como uma única citação de resposta, enquanto um ponteiro no meio do corpo ou um ponteiro que seja o corpo inteiro continua sendo renderizado como cartão de citação. [Links para events citados agora codificam `nevent`](https://github.com/nostrord/nostrord/pull/293) com o autor, o kind e o relay do qual a citação foi lida, de modo que um event de [NIP-29](/pt/topics/nip-29/) (grupos gerenciados por relay) compartilhado em uma DM possa ser buscado por outro cliente, em vez de um identificador de nota puro, sem dicas de consulta.

## Atualizações de NIPs e trabalho de especificação do protocolo

### Possibilidades de implementação do Nostr

Duas mudanças de especificação foram incorporadas ao [repositório principal de NIPs](https://github.com/nostr-protocol/nips) nesta semana.

O [NIP-67](/pt/topics/nip-67/) define dicas que um relay pode acrescentar a uma mensagem `EOSE` (fim dos events armazenados) para que um cliente saiba se deve continuar a paginação. A [dica `"auth"` incorporada](https://github.com/nostr-protocol/nips/pull/2371) adiciona um terceiro valor ao lado de `finish` e `more`: agora, um relay pode sinalizar que outros events armazenados talvez fiquem visíveis caso o usuário se autentique, e deve enviar o desafio `AUTH` do [NIP-42](/pt/topics/nip-42/) (autenticação em relays) antes do `EOSE` que carrega a dica. A [adição correspondente ao NIP-42](https://github.com/nostr-protocol/nips/pull/2371) define o mesmo fluxo pelo lado do cliente, assim um cliente que recebe um `EOSE` com `auth` já tem o desafio ao qual precisa responder.

O [NIP-84](/pt/topics/nip-84/) (destaques portáteis, os events kind `9802` cujo suporte foi lançado pelo Amethyst acima) [incorporou uma atualização no esquema de tags](https://github.com/nostr-protocol/nips/pull/2454): agora, os destaques podem marcar sua fonte com tags `i` estruturadas segundo o [NIP-73](/pt/topics/nip-73/) (identificadores de conteúdo externo), além de tags `a`/`e` para events Nostr e tags `r` para qualquer outra coisa, e a renderização de destaques de citações passou de MUST para SHOULD, como em um quote repost.

### Nostr Wallet Connect

Uma resposta `list_transactions` pode informar quantas transações correspondem à solicitação, e não quantas linhas a página atual retornou. O [`total_count` opcional incorporado](https://github.com/nostr-wallet-connect/nwc/pull/4) no NWC-05 (a extensão de histórico da carteira) no [repositório de extensões do NWC](https://github.com/nostr-wallet-connect/nwc) adiciona esse campo à resposta usada com o [NIP-47](/pt/topics/nip-47/) (controle remoto cifrado de carteiras pelo Nostr).

O [commit que adiciona `total_count`](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67) documenta-o como um inteiro opcional: o número total de transações correspondentes aos filtros da solicitação.

O [commit que exclui a paginação da contagem](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e) afirma que esse total exclui a paginação, portanto conta todas as transações correspondentes em todas as páginas.

## Mergulho Profundo em NIP: Reposts e reações

Um contato pode recolocar uma nota existente diante de seus seguidores e anexar um like, dislike ou emoji compacto sem escrever uma resposta. O [NIP-18](/pt/topics/nip-18/) (reposts) publica essa redistribuição como seu próprio event assinado. O [NIP-25](/pt/topics/nip-25/) (reações) publica a resposta compacta como um event assinado separado. Ambos permanecem como arquivos `draft` `optional` na [especificação canônica de reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) e na [especificação canônica de reações](https://github.com/nostr-protocol/nips/blob/master/25.md): estão presentes no repositório de NIPs e são implementados por clientes, embora ainda sejam classificados como não finais.

### Reposts (NIP-18)

Seguidores recebem um ponteiro assinado para uma nota de texto kind 1 que alguém já publicou quando um cliente grava um event kind 6. A [especificação de reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) define `kind` como 6, coloca em `content` o JSON serializado dessa nota (`content` vazio é permitido e não recomendado), exige uma tag `e` cujo valor é o `id` da nota e cuja terceira entrada é a URL de um relay onde a nota pode ser buscada, e afirma que o event SHOULD também carregar uma tag `p` com a `pubkey` do autor original. Um repost de um event de [NIP-70](/pt/topics/nip-70/) (events protegidos) SHOULD manter `content` vazio, para que o payload protegido não seja copiado para o novo event.

Uma citação é uma referência dentro de algum outro event, não um wrapper kind 6. Quando um cliente menciona um `nevent`, `note` ou `naddr` [NIP-21](/pt/topics/nip-21/) (URI `nostr:`), deve converter essa menção em uma tag `q` no formato `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]`. [Tags de quote repost](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts) mantêm essas citações fora dos tópicos de respostas e permitem que clientes busquem e contem as citações de uma publicação.

Kind 6 é reservado para notas kind 1. Um repost genérico kind 16 pode envolver qualquer event kind que não seja kind 1. Ele SHOULD incluir uma tag `k` cujo valor seja o kind serializado do event interno. Quando esse event interno for substituível, o repost genérico SHOULD adicionar uma tag `a` com a coordenada `kind:pubkey:d-tag`; se essa tag `a` estiver ausente, o repost aponta para uma versão específica, e `content` deve conter a string JSON completa dessa versão. As [regras de reposts genéricos](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts) impedem que events longos, endereçáveis e outros que não sejam notas sejam publicados como se fossem kind 1.

O event kind 6 a seguir é um repost real recuperado de `wss://relay.damus.io` durante a preparação ([abrir o event](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)):

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

Seu `kind` é 6, a tag `e` aponta para a nota repostada, a tag `p` identifica o autor dessa nota e `content` carrega o event kind 1 original como JSON serializado. Esse event recuperado de um relay omite a dica de relay que a [especificação NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md) marca como obrigatória, o que demonstra por que leitores e clientes devem validar events reais e aceitar produtores que omitam campos.

### Reações (NIP-25)

Uma publicação pode receber likes, dislikes e emojis assinados sem que essas marcações entrem no tópico de respostas. A [especificação de reações](https://github.com/nostr-protocol/nips/blob/master/25.md) define essa marcação como um event kind 7 cujo `content` MUST carregar o valor da reação. `+` ou uma string vazia MUST ser interpretado como like ou voto positivo. `-` MUST ser interpretado como dislike ou voto negativo. Um emoji ou um shortcode do [NIP-30](/pt/topics/nip-30/) (emoji personalizado) SHOULD NOT ser interpretado como like ou dislike, e um cliente MAY exibir esse emoji na publicação.

O alvo está nas tags, não é inferido de `content`. MUST haver uma tag `e` definida com o `id` do event alvo, e essa tag SHOULD incluir uma dica de relay; tags `e` adicionais não são recomendadas e, se aparecerem, o `id` alvo deve ser o último. SHOULD haver uma tag `p` para o autor do alvo, por último caso apareçam várias tags `p`. Um alvo endereçável SHOULD também receber uma tag `a` com as coordenadas `kind:pubkey:d-tag`. As tags `e` e `a` SHOULD incluir dicas de relay e pubkey, as tags `p` SHOULD incluir dicas de relay, e uma tag `k` MAY carregar o kind serializado do event que recebeu a reação. [Essas regras de tags](https://github.com/nostr-protocol/nips/blob/master/25.md#tags) permitem que um cliente busque o alvo e notifique seu autor apenas com o event de reação.

Um cliente MAY colocar um único `:shortcode:` em `content` e uma tag `emoji` que associe esse shortcode a uma URL de imagem, seguindo as [regras de reações com emojis personalizados](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction). Se o alvo não for um event Nostr nativo, a reação MUST ser kind 17 e MUST carregar tags `k` e `i` do [NIP-73](/pt/topics/nip-73/) (IDs de conteúdo externo), como nas [regras de reações a conteúdo externo](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions). Kind 17 é uma reação a um site, episódio de podcast ou outro objeto externo. Não é uma reação event a event kind 7 nem um repost.

O event kind 7 a seguir é uma reação real recuperada de `wss://relay.damus.io` durante a preparação ([abrir o event](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)):

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

Seu `content` é `+`, o like convencional do [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md). A tag `e` identifica o event que recebeu a reação; a tag `a` acrescenta sua coordenada endereçável; a tag `p` identifica seu autor; e a tag `k` opcional registra o kind do alvo como uma string.

### Implementações atuais em clientes

O [Amethyst](https://github.com/vitorpamplona/amethyst), um cliente Nostr para Android, define o [tipo de event de repost](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) e o [tipo de event de reação](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt) em sua camada atual de protocolo.

O [Snort](https://github.com/v0l/snort), um cliente Nostr para web, implementa [funções auxiliares de NIP-18 que incluem o tratamento de tags de links de citação](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) e [cria tags de reações a events segundo o NIP-25](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

O [Ditto](https://github.com/soapbox-pub/ditto), um servidor Mastodon e relay Nostr combinados, [publica reposts genéricos kind 16 com uma tag `k` e uma coordenada `a` em alvos endereçáveis](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) e [aplica a semântica de reações kind 7 tratando a última tag `e` como o event alvo](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### Como funcionam em conjunto

Um event kind 6 ou kind 16 redistribui um event existente nos feeds dos seguidores de quem o reposta, seja incorporando o JSON desse event, seja apontando para uma coordenada substituível. Uma tag `q` marca uma citação dentro de outro event, para que a reconstrução do tópico possa contar referências sem tratar o event que cita como uma resposta, a distinção estabelecida na [seção sobre quote reposts](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts). Um event kind 7 mantém o event original onde está e anexa somente o valor da reação e as tags do alvo, conforme o contrato da [especificação de reações](https://github.com/nostr-protocol/nips/blob/master/25.md). Portanto, clientes que buscam uma pubkey veem os reposts dessa pubkey como novos events kind 6 ou 16 e as opiniões dessa pubkey como events kind 7 nas publicações de outras pessoas.

---

Envie uma DM NIP-17 para compartilhar um projeto ou notícia por meio do [projeto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
