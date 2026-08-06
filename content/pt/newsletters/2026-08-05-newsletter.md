---
title: "Nostr Compass #34"
date: 2026-08-05
publishDate: 2026-08-05
translationOf: /en/newsletters/2026-08-05-newsletter.md
translationDate: 2026-08-06
draft: false
type: newsletters
description: "O Sandstr oferece visitas com dados simulados pelos clientes Nostr, o nostr-mill adiciona consentimento de assinatura por evento, e o nostrord amplia os grupos hospedados em relays. Os mergulhos profundos cobrem a busca em relays e os destaques portáteis."
---

Bem-vindos de volta ao [Nostr Compass](https://github.com/andotherstuff/nostr-compass), seu guia semanal de Nostr.

**Esta semana:** o [Sandstr](https://sandstr.app/) permite que recém-chegados explorem clientes Nostr simulados sem criar chaves nem instalar um aplicativo. O [nostr-mill](https://github.com/0ceanSlim/nostr-mill) adiciona consentimento do signatário por evento e recuperação de chaves entre clientes, enquanto o [nostrord](https://github.com/nostrord/nostrord) amplia os grupos hospedados em relays, os signatários, a moderação, os uploads e os destaques. O trabalho de protocolo abrange os formatos de eventos Nostr, as conexões de carteira, a descoberta de relays, os napplets, o Marmot e o Concord; os mergulhos profundos explicam a busca assistida por relays e os destaques portáteis.

## Histórias Principais

### nostr-mill 1.6.0 leva o consentimento de assinatura e a recuperação de contas ao navegador

O [nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) é um seletor de contas e signatário incorporável ao navegador. Agora ele pede consentimento por kind de evento e mostra o conteúdo e as tags decodificados antes de assinar, com concessões de duração limitada e um gerenciador de permissões. A versão também corrige um bug de primeira sessão que permitia que categorias configuradas para perguntar sempre assinassem sem perguntar. Sua integração opcional com o Google pode importar um `nsec` existente, armazena a chave criptografada na pasta de dados do aplicativo no Drive do usuário, suporta múltiplas identidades e pode exportar um `ncryptsec` no formato [NIP-49](/pt/topics/nip-49/) (formato de chave privada criptografada).

O [backup experimental em relays](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) deriva uma frase de recuperação forte com scrypt e HKDF, empacota a chave como `ncryptsec`, verifica os eventos obtidos e exige um quórum de relays antes da recuperação. O login via [NIP-55](/pt/topics/nip-55/) (intents de signatário no Android) agora usa o caminho de retorno pela área de transferência do Amber, e as conexões [NIP-46](/pt/topics/nip-46/) (assinatura remota mediada por relays) são silenciosas por padrão. Controles de marca e telas de permissão responsivas completam a versão sem alterar as integrações existentes, a menos que o operador opte por isso.

### nostrord 2.5.0 dá aos grupos de relays identidades estáveis e específicas do relay

O [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) é um cliente multiplataforma para comunidades hospedadas em relays. Agora ele deriva uma identidade [NIP-29](/pt/topics/nip-29/) (grupos gerenciados por relays) a partir do ID do grupo e do relay anfitrião, delimita a associação e os emblemas de administrador da mesma forma, aceita deep links `naddr` de grupo e sincroniza threads de grupos privados entre dispositivos.

A [versão](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) também adiciona uma caixa de entrada de moderação com [NIP-56](/pt/topics/nip-56/) (eventos de denúncia), login com Amber via NIP-55, recuo de limite de taxa para o tráfego do signatário NIP-46, renderização de [NIP-84](/pt/topics/nip-84/) (destaques portáteis) com novas tentativas para referências não resolvidas, e uploads de mídia via Blossom ou [NIP-96](/pt/topics/nip-96/) (armazenamento HTTP de arquivos). O login com Google agora faz backup da chave antes da criação da conta e confirma as desconexões. As respostas em threads ganham conteúdo mais rico e exclusão por administradores, enquanto correções no chaveiro do desktop e no teclado móvel mantêm esses recursos de protocolo utilizáveis.

### Primal Android 3.5.25 atualiza a assinatura remota e a filtragem da lista de seguidos

O [Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25) é um cliente móvel de Nostr com feeds, busca e assinatura remota. Ele atualiza seu signatário remoto para o comportamento atual do protocolo, adiciona uma lista de silenciados dos seguidos, abre a busca a partir do Explorar, repara automaticamente conexões de relay paralisadas, expõe os tempos limite das requisições na interface, rejeita entradas inválidas na lista de seguidos e atualiza as URLs de relay de reserva. A pré-busca de feeds, o menor uso de memória e um teto de cache de 100 MB reduzem o custo de manter esses feeds atualizados. Notas com uma única imagem agora usam toda a largura do conteúdo, e os controles de perfil e a pré-carga de mídia recebem correções menores de interação e ordenação.

### Nostur 1.30.2 amplia as respostas privadas e a mídia nas mensagens diretas

O [Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527) é um cliente de Nostr para plataformas Apple. Ele sempre expõe a ação de resposta privada, adiciona caches de mídia por conversa com limites e controles de limpeza, melhora o autocompletar de nomes e tags em publicações e chats, mostra mensagens referenciadas no chat ao vivo e inclui o título da sala nas notificações do chat. Correções na paginação do feed e nas respostas aninhadas tratam de regressões na recuperação e na renderização de conversas.

### Chama 5.7.0 adiciona registros de árbitros e recuperação de trocas em cache

O [Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0) coordena trocas entre pares e arbitragem por meio de cadeias de eventos Nostr assinados. Ele exibe o valor bloqueado de um árbitro, o tempo de vigência de sua fiança e seu outpoint de financiamento; registra quando um substituto substituiu um árbitro ausente; e define os eventos adormecidos de kind `38136` de atestação de falhas que exigem as assinaturas de ambos os principais. Um reparo explícito tenta novamente os históricos de relay incompletos contra o cache durável do dispositivo e republica os eventos recuperados, enquanto as publicações malsucedidas entram na fila para a próxima conexão. A versão também impede pagamentos duplicados entre dispositivos do prêmio de árbitro, tratando o evento de kind `38113` do autor como o registro de pagamento.

### Auditable Voting 0.1.165 restaura a entrega de cédulas delegadas

O [Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165) realiza votações verificáveis separando as credenciais do eleitor do conteúdo da cédula. Ele restaura a emissão delegada de cédulas cegas por meio de entrega autenticada de delegações e reposição de DMs de controle, mantém as mensagens diretas de credenciais cegas nos relays privados configurados e atualiza o proxy de auditoria para 0.1.52.

### Sandstr permite que recém-chegados experimentem clientes Nostr com dados simulados

O [Sandstr](https://sandstr.app/) oferece simulações interativas no navegador de clientes Nostr para que um recém-chegado possa comparar suas interfaces antes de instalar um ou criar um par de chaves. Seu lançamento em 3 de agosto inclui reproduções verificadas contra a referência de Damus, Amethyst, Primal, Snort, YakiHonne, Coracle e Wisp, além de prévias iniciais claramente rotuladas de Gossip, Keychat e Olas. Tudo roda localmente contra dados simulados, portanto as simulações não geram chaves nem se conectam a relays. Cada simulação leva ao site e ao repositório de código do cliente real, tornando o Sandstr uma ferramenta de integração e comparação de interfaces em vez de mais um cliente Nostr. Ele mostra como feeds, perfis, threads, mensagens diretas, busca, zaps e controles de relay funcionam sem pedir a um usuário de primeira viagem que tome uma decisão de identidade ou segurança antecipadamente.


### mineracks signer combina uma extensão de navegador com um bunker de desktop

O [mineracks signer](https://github.com/mineracks/mineracks-signer) oferece duas superfícies de assinatura a partir do mesmo projeto. Sua extensão de navegador implementa o [NIP-07](/pt/topics/nip-07/) para que aplicações web possam solicitar assinaturas sem receber a chave privada, enquanto o aplicativo de desktop expõe um signatário remoto [NIP-46](/pt/topics/nip-46/) para clientes que se comunicam por relays.

A [versão de desktop 0.1.0](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0) do projeto armazena o material de chaves com a codificação de chaves criptografadas do NIP-49 e mantém a chave descriptografada dentro do processo Rust em vez de passá-la à interface. Cada requisição mostra o aplicativo chamador e a ação solicitada, enquanto a aprovação automática por aplicativo é opcional e revogável. A primeira compilação de desktop suporta Apple Silicon, mas não Macs com Intel.

## Lançamentos

### Jumble 26.8.1 adiciona controles de prova de trabalho e prévias de comentários

O [Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1) é um cliente Nostr web e de desktop. Ele lembra a dificuldade da prova de trabalho para publicação, exibe emblemas de trabalho verificado, pré-visualiza os comentários vinculados acima do conteúdo externo, salva imagens do visualizador em tela cheia e expande biografias de perfil longas sob demanda. As notificações de reação agora descartam kinds de evento não suportados, os avisos de desconexão de relay ficam menos ruidosos, os relays padrão foram atualizados e um conflito de reprodução automática de mídia foi corrigido.

### nostr-calendar 2.1.0 restaura a vinculação do signatário em formulários privados

O [nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0) publica calendários, eventos e respostas de formulários como dados Nostr. Ele vincula os envios de formulários privados ao signatário ativo, salva eventos duplicados intencionais nos relays, corrige a busca em relays, analisa as datas do calendário em hora local e adiciona notificações no aplicativo além de um cliente iOS. A correção do signatário evita que uma identidade desatualizada produza uma resposta criptografada inutilizável.

### Manent 2.0.0 adiciona marcação e busca para notas salvas

O [Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0) é um arquivo pessoal para notas Nostr assinadas. Ele adiciona tags locais e busca, permitindo ao leitor organizar e recuperar os eventos salvos sem modificar seu conteúdo assinado.

### nosvelte 0.6.1 fecha assinaturas vazias após o EOSE

O [nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1) fornece componentes e hooks reativos de Svelte para dados de relay. Buscas vazias agora são concluídas ao chegar o End of Stored Events, o cancelamento fecha o `REQ` subjacente, as novas tentativas limpam erros obsoletos e os hooks de lista retornam seu valor vazio documentado. Ele também reconhece eventos endereçáveis independentemente de onde apareça sua tag `d`, substitui metadados e artigos superados, desduplica reações por ID de evento e mantém todos os eventos do primeiro lote de um relay.

## Mudanças não lançadas

### NMP vincula a admissão ao relay às declarações e amplia as consultas de grupo

O [NMP](https://github.com/pablof7z/nmp) é um kit de ferramentas TypeScript para construir aplicações Nostr e interfaces de grupos apoiados por relays. O [PR #1254](https://github.com/pablof7z/nmp/pull/1254) faz com que a admissão ao relay siga o proprietário da declaração que a autoriza, mantendo a decisão de permissão vinculada ao estado assinado do Nostr. O [PR #1255](https://github.com/pablof7z/nmp/pull/1255) generaliza as consultas de grupos gerenciados por relays do [NIP-29](/pt/topics/nip-29/) em vez de assumir uma única forma de consulta restrita. Ambas as mudanças estão mescladas, mas ainda não apareceram em uma versão marcada.

### Mosaico deriva a identidade de grupo gerenciado dos registros do relay

O [Mosaico](https://github.com/pablof7z/mosaico) é um cliente Nostr para explorar e administrar comunidades gerenciadas por relays. O [PR #758](https://github.com/pablof7z/mosaico/pull/758) deriva a identidade de um grupo gerenciado do relay que hospeda seus registros autoritativos. O [PR #757](https://github.com/pablof7z/mosaico/pull/757) observa o registro publicado do grupo ao resolver o estado de administração. Isso mantém distintos dois grupos com nomes semelhantes em relays diferentes e dá aos clientes uma fonte apoiada por relay para seus metadados de gerenciamento.

### Divine isola relays lentos durante consultas multi-relay

O [Divine](https://github.com/divinevideo/divine-mobile) é um cliente móvel de vídeo curto que publica e recupera vídeos via Nostr. O [PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673) dá a cada consulta de relay seu próprio tempo limite, em vez de deixar que uma conexão paralisada consuma o orçamento de tempo de toda uma requisição. Os resultados dos relays que respondem podem assim chegar enquanto o ponto final lento é abandonado de forma independente. A mudança melhora a recuperação sem tratar um relay como autoritativo para o resultado combinado.

### rust-nostr reforça criptografia, hashes e reconciliação

O [rust-nostr](https://github.com/rust-nostr/nostr) é uma biblioteca e kit de ferramentas Rust para clientes, relays e implementações do protocolo Nostr. O [PR #1421](https://github.com/rust-nostr/nostr/pull/1421) reduz as alocações em seu caminho de criptografia versionada do [NIP-44](/pt/topics/nip-44/), enquanto o [PR #1423](https://github.com/rust-nostr/nostr/pull/1423) introduz hashes tipados que tornam mais difícil misturar acidentalmente valores de resumo incompatíveis. O [commit 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69) impede que uma mensagem malformada de reconciliação de conjuntos Negentropy do [NIP-77](/pt/topics/nip-77/) desconecte o relay local. O trabalho mesclado reforça tanto o manuseio de cargas criptografadas quanto o comportamento de falha de reconciliação antes do próximo lançamento.

### Zeus serializa pagamentos NWC antes de debitar os orçamentos de gasto

O [Zeus](https://github.com/ZeusLN/zeus) é uma carteira móvel de Bitcoin e Lightning que pode expor operações da carteira via Nostr Wallet Connect. O [PR #4305](https://github.com/ZeusLN/zeus/pull/4305) conta os pagamentos pendentes contra um orçamento de [NIP-47](/pt/topics/nip-47/) Nostr Wallet Connect em vez de esperar pela liquidação. O [PR #4303](https://github.com/ZeusLN/zeus/pull/4303) serializa o manuseio de pagamentos para que requisições concorrentes não possam disputar o mesmo limite de autorização. O par mesclado fecha uma lacuna de aplicação de orçamento na superfície de controle Nostr da carteira.

### Nostr Components compartilha uma única tentativa de conexão ao relay

O [Nostr Components](https://github.com/saiy2k/nostr-components) é uma biblioteca reutilizável de componentes web para adicionar dados e interações Nostr a aplicações. O [PR #105](https://github.com/saiy2k/nostr-components/pull/105) permite que componentes montados ao mesmo tempo compartilhem uma tentativa de conexão ao relay em andamento. Cada consumidor ainda recebe a conexão resultante, mas montagens concorrentes não abrem mais sockets duplicados enquanto o primeiro handshake está pendente. A mudança reduz a carga evitável sobre os relays em aplicações montadas a partir de vários componentes independentes.

## Atualizações de NIPs e trabalho de especificação do protocolo

### Formatos de eventos Nostr e descoberta

O [PR de NIP #2430](https://github.com/nostr-protocol/nips/pull/2430) propõe pacotes de figurinhas como definições endereçáveis de kind `30031` e os pacotes instalados de um usuário como kind substituível `10031`. Cada tag de figurinha carrega um código curto, um hash SHA-256 e um tipo MIME; a imagem permanece em um servidor [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md) (armazenamento de blobs Blossom). O rascunho aberto padroniza assim a identidade e a instalação de pacotes sem colocar os bytes da imagem nos eventos.

O [PR de NIP #2429](https://github.com/nostr-protocol/nips/pull/2429) propõe documentos Gopher endereçáveis de kind `31436`. Cada evento contém um nó de texto ou menu UTF-8, e os nós assinados sob uma mesma pubkey formam um gopherhole que qualquer ponte RFC 1436 apoiada por relay pode servir. A proposta aberta usa o armazenamento comum de eventos endereçáveis em vez de vincular a publicação a um único nome de host Gopher.

O [PR de NIP #2428](https://github.com/nostr-protocol/nips/pull/2428) propõe grupos privados com tíquetes por época. Um grupo alterna as credenciais de associação entre épocas, e os clientes apresentam o tíquete da época atual para participar. O rascunho visa ao chat privado sem pedir a um relay que trate um token portador permanente como associação vitalícia.

O [PR de NIP #2425](https://github.com/nostr-protocol/nips/pull/2425), coberto como proposta na semana passada, agora mesclou um esclarecimento de URI no [NIP-B0](/pt/topics/nip-b0/) (favoritos web endereçáveis). Ele distingue prefixos HTTPS omitidos de esquemas URI explícitos quando um favorito armazena seu destino na tag `d`, impedindo que os clientes reconstruam um destino ambíguo.

### Pagamentos e conexões de carteira

O [PR de NIP #2419](https://github.com/nostr-protocol/nips/pull/2419), coberto como proposta na edição de 22 de julho, agora mesclou um núcleo menor do [NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect). URIs de conexão, transporte criptografado por relay, descoberta de capacidades, negociação de criptografia e métodos comuns permanecem no NIP; notificações, faturas retidas, keysend, histórico de transações, metadados e pareamento por deep link passam para um repositório de extensões dedicado. As conexões existentes permanecem compatíveis enquanto as carteiras podem implementar os contratos opcionais de forma independente.

O [PR de NWC #2](https://github.com/nostr-wallet-connect/nwc/pull/2), coberto como proposta na semana passada, agora mesclou os métodos de pagamento BIP-321 nesse repositório de extensões. O BIP-321 fornece um URI de pagamento Bitcoin comum que pode carregar diferentes trilhos, de modo que quem chama o NWC pode solicitar ou enviar um pagamento sem adicionar um novo RPC central para cada tipo de instrução subjacente.

### Capacidades do anfitrião de napplets

O [PR de NAP #95](https://github.com/napplet/naps/pull/95) propõe a descoberta de catálogos para aplicações em sandbox distribuídas pelo Nostr. Um napplet pergunta ao seu anfitrião quais aplicações e capacidades estão disponíveis, e o anfitrião retorna metadados filtrados por política em vez de expor todo o seu ambiente local. O contrato suporta decisões de lançamento sem conceder autoridade de execução durante a descoberta.

O [PR de NAP #33](https://github.com/napplet/naps/pull/33) propõe uploads de arquivos e blobs mediados pelo shell. Um napplet fornece os bytes e a intenção; o anfitrião seleciona um trilho NIP-96 ou Blossom, assina a autorização, relata o progresso e retorna URLs, hashes, dados MIME e tags [NIP-94](/pt/topics/nip-94/) (metadados de arquivo) prontas para anexar. Credenciais de armazenamento e autoridade HTTP nunca entram no napplet.

### Grupos criptografados Marmot

O [PR do Marmot #410](https://github.com/marmot-protocol/marmot/pull/410) mesclou regras de convergência e de entrada diferida. Os clientes distinguem um objeto ao qual falta uma dependência de época atual de uma entrada obsoleta ou inválida, mantêm-no elegível para nova busca após uma recusa de recursos e tentam novamente quando outro commit altera o contexto de descriptografia. Um compromisso de estado com separação de domínio oferece aos testes de conformidade um oráculo de convergência compartilhado sem adicionar um campo de produção ao protocolo.

### Planos comunitários do Concord

O [PR do Concord #14](https://github.com/concord-protocol/concord/pull/14) mesclou as mensagens que desaparecem do CORD-08. Um valor de metadados da comunidade define a duração; os rumores de chat e os invólucros criptografados carregam uma tag de [NIP-40](/pt/topics/nip-40/) (expiração de eventos), enquanto os eventos de exclusão e o aviso de temporizador de kind `1740` estão isentos. O temporizador assinado viaja com o estado da comunidade, embora a exclusão pelo relay continue sendo uma solicitação de retenção e não uma garantia criptográfica de eliminação.

O [PR do Concord #13](https://github.com/concord-protocol/concord/pull/13) mesclou no CORD-04 a fixação resistente a rotações. Cada canal tem uma lista de fixados que substitui por completo no plano de controle; as entradas carregam o selo assinado original mais chaves de expansão NIP-44 por mensagem, permitindo que um novo membro verifique o autor e o texto simples sem receber uma chave de época antiga. Listas privadas podem permanecer seladas a uma época do canal, limites restringem o tamanho da lista e exclusões do autor removem fixados sem bifurcar a cadeia do plano de controle.

## Mergulho Profundo em NIPs

### Capacidade de busca (NIP-50)

O [NIP-50](/pt/topics/nip-50/), definido na [especificação principal](https://github.com/nostr-protocol/nips/blob/master/50.md), adiciona um filtro de busca opcional para os relays. Os filtros comuns do Nostr funcionam quando um cliente já conhece um autor, um kind de evento, um identificador ou uma tag; o NIP-50 trata da descoberta quando a entrada é uma consulta humana como `best nostr apps`.

O [formato de rede do NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field) adiciona uma string `search` a um filtro normal dentro de uma mensagem `REQ`. Uma requisição pode combinar esse campo com `kinds`, `authors`, `ids`, filtros de tags e `limit`, e um REQ pode carregar vários filtros independentes. Um relay compatível deve buscar principalmente no `content` do evento, pode usar outros campos quando o kind de evento tornar isso útil e deve ordenar pela sua própria pontuação de relevância antes de aplicar o `limit`. Essa ordem difere do fluxo habitual de eventos do mais recente para o mais antigo.

A string de consulta pode incluir as [extensões `key:value`](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions) da especificação. Ela nomeia `include:spam`, `domain:`, `language:`, `sentiment:` e `nsfw:`; um relay deve ignorar as extensões que não implementa. Os clientes descobrem o suporte declarado por meio do campo `supported_nips` do [NIP-11](/pt/topics/nip-11/) do relay, mas ainda podem enviar o filtro a outros se estiverem preparados para rejeitar respostas não relacionadas.

A [especificação do NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) deliberadamente não padroniza tokenização, stemming, classificação, detecção de idioma, análise de sentimento nem classificação de spam. Dois relays conformes podem retornar eventos e ordenações diferentes para a mesma consulta. Isso torna o relay um provedor de índice e classificação, não uma fonte de verdade. A especificação recomenda consultar vários relays compatíveis, verificar se os eventos retornados atendem ao caso de uso do cliente e descartar relays cujos resultados tenham má precisão.

Isso difere da [filtragem exata do NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md). Um filtro de `authors` ou `#t` tem semântica de correspondência determinística que um cliente pode verificar diretamente, enquanto uma correspondência de busca pode depender de um índice e de uma pontuação opaca. O NIP-50 mantém o envelope de evento assinado e o transporte de relay do NIP-01, mas aceita variação no recall e na ordenação para tornar possível a recuperação aberta.

O evento abaixo é um resultado de busca ilustrativo usando os [sete campos de evento do NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Os valores hexadecimais repetidos são marcadores de posição e não uma assinatura válida.

```json
{
  "id": "0000000000000000000000000000000000000000000000000000000000000000",
  "pubkey": "1111111111111111111111111111111111111111111111111111111111111111",
  "created_at": 1785888000,
  "kind": 1,
  "tags": [["t", "nostr"]],
  "content": "A comparison of Nostr search relays and their indexes.",
  "sig": "22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
}
```

Os clientes atuais usam o mesmo filtro em diferentes superfícies de descoberta. O [Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts) envia buscas NIP-50 a relays de busca dedicados, o [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts) busca eventos por meio de seu pool de relays, e o [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts) coordena buscas apoiadas por relays para leitura de formato longo. Seu tratamento diferente dos resultados reflete a liberdade que o NIP-50 deixa a relays e clientes.

### Destaques (NIP-84)

O [NIP-84](/pt/topics/nip-84/), definido por sua [especificação principal](https://github.com/nostr-protocol/nips/blob/master/84.md), atribui o kind `9802` a um destaque. Ele transforma um trecho selecionado, ou uma referência a mídia não textual, em um evento assinado que pode circular entre clientes de leitura, sociais e de anotação.

O [`content` do evento](https://github.com/nostr-protocol/nips/blob/master/84.md#format) contém o texto selecionado e pode estar vazio quando a fonte é áudio, vídeo ou outro meio não textual. Um destaque aponta para uma fonte Nostr com uma tag `a` para um evento endereçável ou uma tag `e` para um evento comum; uma tag `r` identifica uma URL web. Os clientes que produzem URLs devem remover parâmetros de rastreamento e outros parâmetros de consulta não úteis antes de publicar, para que variantes cosméticas de URL não fragmentem as referências à mesma fonte.

As [tags `p`](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution) opcionais atribuem a fonte a uma ou mais pubkeys Nostr. Seu quarto valor pode identificar um papel como `author` ou `editor`, e uma tag `context` pode preservar o texto ao redor quando a seleção por si só seria pouco clara. Um destaque com citação adiciona uma tag `comment` em vez de publicar uma segunda nota de kind `1`: a tag `r` da fonte recebe o marcador `source`, enquanto pubkeys ou URLs mencionadas no comentário carregam `mention`, permitindo que os renderizadores distingam a atribuição da resposta do usuário.

A [definição do kind `9802`](https://github.com/nostr-protocol/nips/blob/master/84.md) torna um destaque um evento regular em vez de um substituível. Repetir ou corrigir uma seleção cria outro evento assinado, e remover um depende do fluxo normal de solicitação de exclusão e da política de retenção do relay. A especificação não define deslocamentos de bytes, seletores nem um instantâneo canônico do documento, portanto um cliente pode não conseguir relocalizar um trecho depois que sua fonte web mudar. Destaques públicos também revelam interesses de leitura; anotação privada exige um design separado de criptografia e compartilhamento.

O NIP-84 difere de um [evento de formato longo do NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md), que publica um artigo inteiro como kind `30023`; um destaque cita ou aponta para material que pode permanecer em outro lugar. Também difere de um [conjunto de favoritos do NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md), que armazena uma coleção substituível de referências. O NIP-84 torna cada seleção independentemente assinada, atribuível, descobrível e discutível.

Este destaque ilustrativo contém os [sete campos de evento do NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Seu identificador e sua assinatura são marcadores de posição.

```json
{
  "id": "3333333333333333333333333333333333333333333333333333333333333333",
  "pubkey": "4444444444444444444444444444444444444444444444444444444444444444",
  "created_at": 1785888000,
  "kind": 9802,
  "tags": [
    ["a", "30023:6666666666666666666666666666666666666666666666666666666666666666:relay-search", "wss://relay.example"],
    ["p", "6666666666666666666666666666666666666666666666666666666666666666", "wss://relay.example", "author"],
    ["context", "Search relays are indexes whose ranking policies can differ."]
  ],
  "content": "ranking policies can differ",
  "sig": "55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"
}
```

O formato já atravessa as fronteiras entre clientes. O [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) adicionou renderização de NIP-84 esta semana, o [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts) renderiza eventos de destaque em seu cliente de formato longo, e o [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts) os publica a partir do conteúdo selecionado. Essas implementações cobrem leitura, criação e renderização social sem exigir que um único serviço seja dono da anotação.

---

Envie uma DM por NIP-17 para compartilhar um projeto ou notícia por meio do [projeto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
