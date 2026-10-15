---
title: "Nostr Compass #44"
date: 2026-10-14
publishDate: 2026-10-14
draft: false
type: newsletters
description: "Amethyst para desktop, correções de segurança no Amber, anexos privados, instalações autenticadas de software, avisos de conteúdo e status."
translationOf: /en/newsletters/2026-10-14-newsletter.md
translationDate: 2026-10-15
---

**[Amethyst](#amethyst)** leva sua interface Android ao desktop e adiciona suporte nativo ao Wayland. **[Amber](#amber)** corrige a revogação de permissões, a limpeza de segredos copiados e uma alteração nas configurações que podia causar perda de chaves. **[Keep](#keep-android)** restringe as permissões de assinatura automática, enquanto **[MDK](#mdk)** traz anexos privados com transferência em fluxo e sincronização de mensagens das mais antigas para as mais recentes. **[Zap Cooking](#zap-cooking)** incorpora salvaguardas para edições na lista de seguidos e associação autenticada. Os [detalhes dos lançamentos](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) vêm a seguir, junto com mudanças no protocolo e mecanismos de status público.

## Principais notícias

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0) leva ao desktop a interface compartilhada do cliente social para Android, com feeds personalizados, painéis para janelas largas, bloqueios opcionais, mídia criptografada e [uploads para Blossom](/pt/topics/blossom/). As pontuações de provedores do [NIP-85, declarações confiáveis](/pt/topics/nip-85/), são indexadas localmente para solicitações, notificações e distintivos, com provedores e limites selecionados pelo usuário.

O [lançamento de hoje, v1.19.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0), adiciona suporte nativo ao Wayland e compressão de vídeo no desktop usando FFmpeg e ffprobe instalados separadamente. Correções no armazenamento de chaves resolvem solicitações repetidas do chaveiro e falhas no chaveiro do Linux. Coleções de calendário e confirmações de presença passam a ser renderizadas, e a interface de login do Android adiciona [assinatura remota com NIP-46](/pt/topics/nip-46/). A abertura em paralelo de envelopes criptografados precede a indexação sequencial, enquanto a reconexão a relays e o tratamento das listas de relays dos autores do feed são corrigidos. O [cliente de relay respeita a espera por limitação de taxa](https://github.com/vitorpamplona/amethyst/pull/4422) antes de retomar assinaturas ou publicações.

A [mudança nos relays dos provedores de confiança](https://github.com/vitorpamplona/amethyst/pull/4437) trata os relays de provedores da lista kind 10040 do usuário como relays próprios e confiáveis. Essas conexões usam uma rota direta por padrão; para usar Tor, é necessário ativar a configuração de relays confiáveis. A [autenticação de relay com NIP-42](/pt/topics/nip-42/) do cliente principal pode revelar a chave pública do usuário a esses relays.

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9) corrige três falhas de segurança no assinador Nostr para Android. [Permissões revogadas](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw) não sobrevivem mais a uma condição de corrida no cache, e rejeições explícitas prevalecem sobre o status de confiança total. [Segredos copiados](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p) recebem uma limpeza da área de transferência agendada pelo sistema para após 60 segundos, inclusive quando o processo é encerrado; o conteúdo continua legível durante esse intervalo, e textos copiados mais recentemente também podem ser apagados. Alterar [“exigir dispositivo desbloqueado”](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5) preserva a chave de encapsulamento antiga até a conclusão da migração dos segredos, enquanto chaves perdidas anteriormente continuam perdidas. A versão corrige aprovações nostrconnect com múltiplas solicitações e respostas nos relays especificados no URI. Usuários da versão 6.6.8 e anteriores devem atualizar.

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0), um [assinador de limiar FROST](/pt/topics/frost/), adiciona geração distribuída de chaves no dispositivo e recuperação autenticada de operações interrompidas com fragmentos de chave. Também oferece suporte a dispositivos sem StrongBox. Na assinatura de limiar, os dispositivos participantes mantêm fragmentos do segredo de assinatura e cooperam para produzir uma assinatura; as etapas de configuração e recuperação determinam quais dispositivos podem participar.

A [versão 1.3.1](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1) impede que a assinatura automática se sobreponha a recusas memorizadas, permissões de Perguntar, aprovações expiradas ou falhas na leitura de permissões. A expiração remove a aprovação em segundo plano, mas mantém as negações. A [migração de políticas por aplicativo](https://github.com/privkeyio/keep-android/pull/532) move as permissões para o armazenamento gerenciado pelo núcleo, preservando decisões mais restritivas.

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21) [autentica a ponte nativa da carteira](https://github.com/jesuspirate/chama/pull/29) usada por seu aplicativo de negociações mediadas por Nostr, desativa o redirecionamento da ponte baseado em URL em produção e valida os valores de pagamento. Também se recusa a apagar uma carteira cujo conteúdo não possa ser lido.

A [versão 6.4.22](https://github.com/jesuspirate/chama/releases/tag/v6.4.22) reforça a reprodução contra events de terceiros, verifica relações de sucessão, rejeita conjuntos vazios de árbitros e deriva o prazo de reembolso do horário LOCK assinado. Suas mudanças de consenso se aplicam a events CREATE assinados a partir de 1º de novembro de 2026; as proteções do cliente se aplicam imediatamente. As notas da versão mantêm ressalvas sobre federações selecionadas pelo anúncio e pagamentos de valores ínfimos. As [mudanças posteriores no assinador e na recuperação](https://github.com/jesuspirate/chama/releases/tag/v6.4.23) adicionam leitores de sementes protegidas e bloqueios tardios recuperáveis, enquanto a [v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24) melhora listas extensas de negociações.

### Zap Cooking

O cliente social e de receitas [Zap Cooking incorpora salvaguardas para edições na lista de seguidos](https://github.com/zapcooking/frontend/pull/795) contra leituras incompletas, desatualizadas ou que indiquem uma redução inesperada da lista. As ações de seguir compartilham um único fluxo protegido de atualização que preserva as tags e o conteúdo existentes. A identidade do assinador é verificada antes da publicação. Sua [correção de autorização de membros](https://github.com/zapcooking/frontend/pull/802) usa a chave pública que assina a solicitação autenticada. Uma [rota que expunha um segredo administrativo foi removida](https://github.com/zapcooking/frontend/pull/801); a implantação ainda exige a rotação do segredo, algo que uma mudança incorporada, por si só, não permite confirmar. [Correções posteriores em conversas e favoritos](https://github.com/zapcooking/frontend/pull/833) preservam a raiz real das respostas e recuperam gravações de favoritos que falharam. Os [campos de tags de receitas](https://github.com/zapcooking/frontend/pull/836) não enviam mais as teclas digitadas a serviços de busca de perfis ou NIP-50, nem fazem o usuário sair do editor com alterações não salvas.

## Lançamentos com tag

### MDK

[MDK v0.13.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.13.0), o ambiente de execução para [grupos criptografados Marmot](/pt/topics/marmot/), adiciona anexos privados com transferência em fluxo e retomável, com indicação de progresso e cancelamento. Também envia [denúncias NIP-56](/pt/topics/nip-56/) privadas ao operador da implantação por meio de [encapsulamentos de presente NIP-59](/pt/topics/nip-59/), omitindo identificadores de mensagens, grupos e relays. A sincronização processa lotes de até 256 events, dos mais antigos para os mais recentes, e preserva recusas CLOSED dos relays. O roteamento SOCKS5 abrange relays, mídia e serviços de descoberta, sem alternativa de conexão direta.

O [guia da versão](https://github.com/marmot-protocol/mdk/blob/v0.13.0/docs/release/0.13.0.md) exige que bindings, cabeçalhos e artefatos nativos sejam atualizados em conjunto. Os esquemas de banco de dados avançam de 101 para 107, sem possibilidade de retorno à versão anterior. O armazenamento de segredos do host precisa de migração. MarmotKit e os artefatos C são estáveis; WN Agent continua sendo uma prévia de lançamento, e os crates do workspace não estão publicados no crates.io. O histórico que chega com mais de cinco [épocas MLS](/pt/topics/mls/) de atraso ainda pode ser impossível de descriptografar sem que haja um aviso de histórico incompleto, e clientes de agentes autenticados mantêm acesso à API inteira.

A versão também [repete tentativas de salvar perfis, listas de seguidos e listas de relays que ficaram pendentes após a primeira confirmação](https://github.com/marmot-protocol/mdk/pull/2228); essas novas tentativas em segundo plano não sobrevivem à reinicialização. A [busca de convites verifica a exclusão e a expiração do KeyPackage nos relays de descoberta](https://github.com/marmot-protocol/mdk/pull/2211), cujas respostas não podem comprovar que o destinatário ainda possui o material privado de seu KeyPackage. Os [alvos das reações de atividade](https://github.com/marmot-protocol/mdk/pull/2187) agora são derivados de forma consistente de atores autenticados e commits individuais do grupo; o histórico mais antigo sem atores permanece incompleto.

Trabalhos posteriores na branch master [encerram assinaturas de relay que ficaram abertas indevidamente e paginam reprocessamentos de ativação limitados a 500 events](https://github.com/marmot-protocol/mdk/pull/2274). A [recuperação de lacunas entre épocas](https://github.com/marmot-protocol/mdk/pull/2298) busca os 256 events mais recentes de um relay cuja comparação falhou, sem certificar que o histórico esteja completo. [Commits de autoatualização repetem a tentativa em cada relay de grupo que ficou de fora](https://github.com/marmot-protocol/mdk/pull/2275). Novas verificações de aviso abrangem [épocas sabidamente desatualizadas](https://github.com/marmot-protocol/mdk/pull/2273) e [commits ainda pendentes de envio aos relays](https://github.com/marmot-protocol/mdk/pull/2288); os usuários podem aceitar o risco, portanto essas verificações não garantem que um grupo não possa se bifurcar.

[Downloads de anexos bloqueados por falta de espaço de armazenamento](https://github.com/marmot-protocol/mdk/pull/2249) preservam o progresso para retomada quando o espaço livre é insuficiente. Downloads grandes solicitados explicitamente gravam os dados diretamente em arquivo, com a preparação intermediária e os pontos de retomada exigindo espaço livre equivalente a cerca de cinco a seis vezes o tamanho do corpo. [Prévias verificadas de events públicos](https://github.com/marmot-protocol/mdk/pull/2304) ganham um cache criptografado por conta, com tamanho limitado, enquanto [resultados de KeyPackage contendo apenas itens obsoletos](https://github.com/marmot-protocol/mdk/pull/2305) passam a ser distinguíveis de consultas incompletas a relays. Essas são alterações posteriores no código-fonte que exigem adoção correspondente pelo aplicativo hospedeiro; prévias por ID de event obtidas em buscas concluídas não verificam novamente exclusões posteriores.

As pontes de agentes também [limitam a saída do backend](https://github.com/marmot-protocol/mdk/pull/2103) para evitar que respostas excessivamente grandes esgotem a memória e [aceitam a resposta de exclusão efetivamente retornada pelo conector](https://github.com/marmot-protocol/mdk/pull/2301). O texto entregue anteriormente continua entregue quando um limite de saída interrompe um turno.

### Myco

[Myco v0.11.0](https://github.com/Origami74/myco/releases/tag/v0.11.0) adiciona conexões USB entre celulares ou computadores com fips e adota [o formato de manifesto atualmente proposto para a NIP-5D](https://github.com/Origami74/myco/pull/135), com hashes assinados de artefatos e ícones. Celulares mais antigos ainda podem ser pareados, mas precisam ser atualizados para abrir esses napplets. Suas [mudanças na política de download](https://github.com/Origami74/myco/pull/133) distinguem destinos de Internet, de rede mesh e HTTP configurados pelo usuário. Indicações fornecidas pelo autor e redirecionamentos não podem sondar redes locais sob a política de Internet, enquanto destinos configurados pelo usuário permanecem sem restrições. O cliente também [descobre blobs nos servidores Blossom BUD-03 do autor](https://github.com/Origami74/myco/pull/134). Isso melhora a descoberta de artefatos, mas expõe o tráfego de instalação a esses servidores. Essas mudanças de HTTP não estabelecem proteções equivalentes para conexões WebSocket. [Verificações de disponibilidade na rede mesh próxima](https://github.com/Origami74/myco/pull/132) consultam pares sobre blobs sem baixá-los nem contatar servidores Blossom públicos. Essas requisições HEAD limitadas exigem permissão de acesso à rede mesh; uma contagem de detentores não comprova que o artefato inteiro continue disponível.

A versão também [consulta servidores DNS upstream em paralelo, usando a resposta que chegar primeiro](https://github.com/Origami74/myco/pull/137), para evitar que tempos limite de operadoras em roaming bloqueiem consultas de relays e artefatos. As publicações via outbox são direcionadas a todos os relays de escrita listados, com entrega aos destinos mais lentos em segundo plano. A rede mesh pela Internet continua desativada por padrão, e imagens da web não são mantidas entre reinicializações.

### Unfiltered

[Unfiltered 1.0.13](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.13) adiciona listas de relays de leitura/escrita e roteamento via outbox ao seu cliente de fotos para Android. Suas [notas de versão](https://njump.me/nevent1qqsy8287ykdstql8ec2udgr8slj3czzkkdkjjc36xwn4lnjrrhggfwgu8dmj2) descrevem as funções dos relays, e contas sem uma lista começam com três relays públicos predefinidos. O recurso de proximidade usa geohashes de baixa precisão e células adjacentes; adicionar localização a uma publicação é opcional e vem desativado por padrão. Essas tags ainda revelam uma área publicamente. O resultado de publicação inspecionado significa que o envio foi enfileirado em um socket, com a aceitação pelo relay ainda não confirmada.

### monostr

[monostr 0.17.0](https://github.com/schmidt1024/monostr/releases/tag/v0.17.0) permite que usuários recebam gorjetas em Monero por meio de um monitor pessoal, enquanto a versão [0.18.0](https://github.com/schmidt1024/monostr/releases/tag/v0.18.0) oculta por padrão os valores das gorjetas e os nomes dos remetentes nas notificações em novas configurações. Por padrão, as imagens só são carregadas ao tocar, e as contagens opcionais do Primal e as tags de cliente ficam desativadas. Um monitor hospedado ainda toma conhecimento de todo pagamento recebido pela carteira cadastrada por meio de sua chave privada de visualização. Os recibos públicos mantêm o destinatário, o horário e a publicação referenciada, mesmo quando os valores estão ocultos.

### Grocery

[Grocery 1.0.2](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.2) combina listas de compras compartilhadas e criptografadas com identidades Nostr baseadas em passkeys e chat Marmot por lista. É possível entrar em listas colando uma chave ao portador, que concede acesso de leitura e edição. O login por passkey depende do suporte do navegador e do provedor à extensão de função pseudoaleatória do WebAuthn; as tags de membros permanecem visíveis para os relays. A [versão 1.0.3](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.3) preserva as listas ao reabrir o aplicativo ao armazenar localmente em cache o conteúdo descriptografado, corrigindo casos em que apenas a chave sobrevivia até que um relay entregasse a lista novamente.

### Roadstr

[Roadstr 1.1.0](https://github.com/roadstrapp/roadstr-app/releases/tag/v1.1.0) lê os kinds 1315/1316 de outro cliente Roadstr respeitando seus prazos de validade e regras de confirmação previstos. Um codec compacto preserva relatos assinados reconstruíveis para uma ponte experimental entre rádio MeshCore e relay. A publicação compatível e a transmissão por rádio ficam desativadas por padrão, com consentimento antes do compartilhamento. Os relatos por rádio expõem a posição, o horário e a chave pública de assinatura a qualquer pessoa ao alcance. Os testes usaram rádios simulados; hardware real, BLE no Android e publicação em relays públicos continuam sem verificação.

### OUTKAST

[OUTKAST 1.1.3](https://github.com/Lwb89dev/outkast/releases/tag/v1.1.3) melhora os comentários em artigos e o tratamento de publicações citadas em seu cliente Android. Comentários em artigos usam kind 1111, com o artigo como raiz e o comentário como pai, enquanto respostas a notas comuns continuam usando kind 1. A descoberta de citações aceita tanto tags q quanto menções `e` mais antigas que contêm links; citações recém-publicadas adicionam tags q. Falhas de publicação revertem reações aplicadas de forma otimista.

### Bookshelf

[Bookshelf 0.1.28](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.28) descreve a [leitura de índices de publicação aninhados](https://njump.me/nevent1qqs8pukgjrnuzryv0z67lze2y0jsshepdckuss25qggvwn5skxqfa7gslzul0) de kind 30040 que contêm tanto capítulos quanto índices filhos na ordem definida pelo publicador. As cópias offline mantêm essa hierarquia e marcadores vinculados a cada ocorrência. A atualização busca as revisões atuais por coordenada, mas mantém o download anterior quando os resultados são incompletos, mais antigos ou malsucedidos. A retransmissão preserva os descendentes assinados originais. A expansão limitada e as ramificações parciais legíveis impedem que uma estrutura com partes ausentes seja apresentada como um livro completo.

### Ditto

[Ditto 2.45.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.45.0) substitui Global por Descobrir em seus feeds de conteúdo. Descobrir reúne conteúdo de pessoas seguidas por quem o usuário segue e classifica as publicações por conexões em comum, excluindo o próprio usuário e as contas que ele já segue. Usuários desconectados e contas que não seguem ninguém veem, em vez disso, uma rede inicial selecionada. Isso muda o escopo da descoberta padrão para uma vizinhança social; a resistência a spam e a confiabilidade dessas contas continuam sendo questões distintas.

### Postr

[Postr 1.1.2](https://njump.me/nevent1qqsf4uu87v5r7awyfhktjqnuc9m6xzfngpvr7gj37zca05sx7lk03vqy4wq7x) mantém as identidades dos perfis selecionados vinculadas às menções nos rascunhos salvos e na publicação. O editor bloqueia alterações na conta, no texto, nas menções e nos anexos durante a assinatura e o envio, guardando os compartilhamentos recebidos até que essa operação termine. Novas tentativas preservam o event assinado original, incluindo publicações pendentes mais antigas. Digitar um nome após @ não é suficiente: os usuários precisam selecionar um perfil, e identidades já perdidas em rascunhos antigos precisam ser selecionadas novamente.

### Nostrautica

[Nostrautica Android 0.11.0](https://github.com/jooray/nostrautica/releases/tag/android-v0.11.0) vincula comunidades aos seus encontros. A aprovação para um encontro vinculado também pode conceder participação na comunidade sem uma segunda aprovação; o formulário de inscrição informa isso e permite que os candidatos recusem essa opção. Os participantes existentes recebem um convite de um toque. Os encontros mantêm seus próprios participantes, combinações e chat, enquanto a comunidade lista seus encontros. As notas da versão descrevem o suporte a coordenadores diferentes para encontros e comunidades, sem comprovar interoperabilidade independente ou testes de criptografia.

### Minibits

[Minibits v0.4.4 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.4-beta.1) corrige o processamento de pagamentos via [Nostr Wallet Connect](/pt/topics/nip-47/) no Android, que podia parar enquanto a carteira estava em segundo plano e acumular pendências até causar uma falha de aplicativo sem resposta. A versão nativa reúne cinco meses de alterações anteriores distribuídas remotamente. A [versão 0.4.5 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.5-beta.1) corrige a transferência por NFC do Android para o iOS; futuras atualizações distribuídas remotamente exigem essa versão. Essas correções são relatadas nas notas das versões, e o processamento em segundo plano continua dependendo das restrições de ciclo de vida do telefone.

### NoorNote

[NoorNote v1.9.0](https://github.com/77elements/noornote/releases/tag/v1.9.0) permite publicar receitas pelo editor de artigos, abrir pacotes de receitas compartilhados e explorar receitas de autores seguidos. Os cartões de sites e as grades de perfis abordados na semana passada agora estão incluídos na versão, junto com o tratamento de limites de requisições dos relays e links `nostr:` diretos no Android. Links para sites continuam sendo algo distinto da verificação do conteúdo desses sites; o acesso por um gateway expõe a esse gateway a requisição decorrente do clique.

### Gittr

[Gittr v1.0.2](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.2) empacota sua plataforma de hospedagem e colaboração Git baseada em Nostr para Android, usando o Amber por meio de [assinatura remota NIP-46](/pt/topics/nip-46/). O APK abre a aplicação hospedada existente `gittr.space`, portanto os usuários continuam dependendo do código fornecido por ela ao navegador e de sua disponibilidade. A assinatura por extensão de navegador não está disponível nesse invólucro; a hospedagem própria continua sendo uma implantação Git separada.

### Dart NDK

[Dart NDK 0.11.0 desenvolvimento zero](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.0) traz para uma prévia de lançamento o [gerenciador de consentimento para autenticação](https://github.com/relaystr/ndk/pull/862) do kit de ferramentas para Dart e Flutter e a troca de relay do assinador NIP-46. Essas alterações foram abordadas na semana passada como trabalho já integrado e agora foram lançadas. O assinador pode acompanhar uma lista substituta de relays, que os aplicativos precisam persistir. A [versão de desenvolvimento um](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.1) adiciona suporte a identificadores NIP com letras nas informações dos relays. Ambas as versões trazem alterações incompatíveis na integração.

### Cambium

[Cambium v0.9.0](https://github.com/forgesworn/cambium/releases/tag/v0.9.0) oferece aos aplicativos Android nativos [quatro opções de aprovação](https://github.com/forgesworn/cambium/pull/32): uma vez, uma hora, um dia ou por tempo indeterminado. As permissões são delimitadas por operação e kind de event. O Cambium encaminha solicitações a um assinador de hardware Heartwood por meio de assinatura remota; o Heartwood continua decidindo quais solicitações assina. As aprovações de sites continuam valendo para uma única vez. Assinadores pareados ganham controles de teste e reconexão, atualizações de relays de transporte compatíveis e diagnósticos com informações sensíveis ocultadas. Os lotes de [NIP-55, assinatura no Android](/pt/topics/nip-55/), preservam a ordem das solicitações e as rejeições individuais, com consentimento visível de uso único para intents reutilizados ambíguos.

### Grain

[Grain v0.8.1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.1) corrige a [autenticação em relays NIP-42](/pt/topics/nip-42/) de sua biblioteca cliente Go para aplicativos que atendem a vários usuários. Cada `UserContext` possui conexões autenticadas privadas, preferências de relays e mecanismos de retenção de conexões; o pool compartilhado nunca se autentica. A biblioteca valida IDs e assinaturas recebidos, verifica a correspondência com os filtros de subscrição e serializa corretamente filtros de tag e de tempo. Os chamadores autenticados precisam migrar para `UserContext`. O armazenamento e o fornecimento de dados pelos relays permanecem inalterados, e a autenticação ainda exige um desafio quando a conexão é aberta.

### Nmail

[Nmail v0.18.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.18.0), um cliente de e-mail criptografado, coloca remetentes desconhecidos em Solicitações e remetentes bloqueados em Spam. A aceitação e o bloqueio são sincronizados entre dispositivos. Os remetentes já presentes na caixa de entrada precisam ser aceitos, com a opção Aceitar todos disponível; o Spam permanece silencioso, e as solicitações pendentes evitam alertas repetidos sobre o remetente. As respostas usam a identidade que recebeu a mensagem. O gerenciamento de relays privados, as verificações de bloqueio do dispositivo antes de copiar códigos de sincronização, os temas compartilhados, a preservação mais completa dos contatos e um instalador para Windows acompanham correções na restauração da caixa de correio após redefinição ou login.

### Meiso

[Meiso v1.5.0](https://github.com/higedamc/meiso/releases/tag/v1.5.0) traz comentários criptografados e indicadores de não lidos para seu gerenciador de tarefas sincronizado via Nostr. Os comentários usam events endereçáveis de kind 35002 com [criptografia NIP-44](/pt/topics/nip-44/), mantendo a associação à tarefa dentro do texto cifrado. A versão [corrige envios offline](https://github.com/higedamc/meiso/pull/212), a recuperação de atualizações após a reconexão, a inicialização com relays salvos e a propagação de listas vazias. Ela também impede que a sincronização parcial exclua tarefas. Os recursos de não lidos e de recuperação de atualizações não adicionam um serviço de notificações para quando o aplicativo está fechado.

### Haps

[Haps v0.1.13](https://github.com/mmalmi/haps/releases/tag/v0.1.13), um instalador de software experimental, exige por padrão uma auditoria da versão exata proveniente da [rede de confiança](/pt/topics/web-of-trust/) do usuário. As auditorias podem comparar o código-fonte fixado e os artefatos recompilados, e permanecer privadas ou ser publicadas. A [versão 0.1.14](https://github.com/mmalmi/haps/releases/tag/v0.1.14) pede que os usuários confirmem o publicador ao instalar apenas pelo nome; a automação precisa especificar um publicador. As auditorias fornecem evidências, enquanto os programas nativos e as receitas de compilação continuam sendo executados sem um ambiente isolado. A exigência de auditoria pode ser ignorada para uma operação; as verificações de assinatura, integridade e confirmação do publicador permanecem.

### Sidecar

[Sidecar v1.16.0](https://github.com/dmnyc/sidecar/releases/tag/v1.16.0) adiciona [descoberta e reprodução de transmissões ao vivo](https://github.com/dmnyc/sidecar/pull/479) ao seu cliente social em forma de extensão de navegador, com chat assinado, reações e zaps. Os favoritos de transmissões salvos têm suporte a backup e restauração criptografados da conta, e o silenciamento privado de notificações permite controlar os alertas. A busca ganha controles para seguir e silenciar; alterações no bloqueio automático e na atualização do histórico da carteira os acompanham.

### Ants

A interface de busca [Ants v0.7.0](https://github.com/dergigi/ants/releases/tag/v0.7.0) [encaminha buscas estruturadas](https://github.com/dergigi/ants/pull/316) aos relays de escrita anunciados pelos autores e aos relays de leitura dos usuários mencionados por meio das [listas de relays NIP-65](/pt/topics/nip-65/), sem login. A descoberta limita o número de identidades e relays consultados e para em caso de cancelamento ou esgotamento do tempo limite. Na ausência de listas, o roteamento alternativo é mantido. As consultas de texto continuam usando [relays de busca NIP-50](/pt/topics/nip-50/) verificados.

### soyLI

[soyLI v0.27.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.27.0), um publicador e reprodutor de napplets para as propostas de [aplicações NIP-5D](/pt/topics/nip-5d/), adiciona atalhos de teclado e propostas sem fork por meio do GRASP, um serviço de hospedagem Git, com verificações da revisão exata nas novas tentativas. Sua [versão v0.26.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.0) distribui versões assinadas para relays de saída verificados após a publicação primária; a exclusão acompanha os destinos em que houve tentativa de envio, mas não pode recolher cópias desconhecidas. A [versão 0.26.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.1) eleva os limites de leitura, reprodução e revisão para 100 MiB, mantendo um limite de 25 MiB para novas compilações e publicação. Posteriormente, os [metadados diretos de apresentação](https://github.com/zeSchlausKwab/napplet-soy/pull/14) passam a colocar capas e clipes dos autores diretamente nos manifestos assinados, descontinuando o event complementar. Trabalhos antigos congelados continuam sendo compatíveis; essa extensão versionada do Soy exige leitores compatíveis e não faz parte da especificação NIP-5D fixada.

### nostream

O servidor relay [nostream v3.3.0](https://github.com/cameri/nostream/releases/tag/v3.3.0) adiciona sondas de [monitoramento de relays NIP-66](/pt/topics/nip-66/) para medir os tempos de ida e volta de leitura e escrita via WebSocket, detectar autenticação opcional e descobrir destinos de espelhamento. Ele emite avisos quando o comportamento observado diverge das [informações do relay NIP-11](/pt/topics/nip-11/). Respostas OK sujeitas a limitação de taxa podem incluir um quinto elemento opcional contendo um intervalo de espera em milissegundos. A [versão 3.4.0](https://github.com/cameri/nostream/releases/tag/v3.4.0) adiciona um quarto elemento, com um intervalo de espera em milissegundos, às [respostas CLOSED](https://github.com/cameri/nostream/pull/821) quando limites de mensagens por IP rejeitam `REQ` ou `COUNT`. Ela inclui o [núcleo de reconciliação negentropy em PostgreSQL](https://github.com/cameri/nostream/pull/809) e um inventário ordenado de event; as mensagens de relay no protocolo e o anúncio de capacidades do [NIP-77](/pt/topics/nip-77/) continuam sendo trabalhos separados.

### Bark

O [Bark v1.3.15](https://github.com/forgesworn/bark/releases/tag/v1.3.15) oferece controles por teclado para aprovações de assinatura remota, revisão explícita de event e identidade, e [um, cinco ou dez minutos para decidir](https://github.com/forgesworn/bark/pull/52). A aplicação dessas regras em segundo plano rejeita decisões expiradas e solicitações enfileiradas; falhas na entrega da decisão mantêm a janela pop-up aberta para uma nova tentativa. A [versão 1.3.17](https://github.com/forgesworn/bark/releases/tag/v1.3.17) disponibiliza a [assinatura no navegador via NIP-07](/pt/topics/nip-07/) quando o handshake com o assinador é concluído, enquanto os diagnósticos opcionais continuam. Ela restaura as pontes nas abas existentes após atualizações.

### Mostro

O [Mostro v0.19.3](https://github.com/MostroP2P/mostro/releases/tag/v0.19.3) responde a solicitações autenticadas por identidade sobre a reputação do próprio usuário, mesmo sem uma ordem aberta. A plataforma de negociação ponto a ponto envia respostas de forma privada à chave de negociação solicitante, e um [comando de CLI já integrado](https://github.com/MostroP2P/mostro-cli/pull/203) disponibiliza essa consulta. A importação de reputação continua sendo uma prévia cujas importações não estão implementadas; os operadores devem mantê-la desativada. Um [trabalho integrado posteriormente](https://github.com/MostroP2P/mostro/pull/1057) publica a margem do guardião da custódia Lightning e rejeita configurações inseguras; seu mínimo de 18 blocos pressupõe a configuração padrão de expiração de retenção do LND.

### Elisym

O [commerce 0.11.0 da Elisym](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.11.0) oferece suporte a taxas deduzidas da receita do comerciante, com uma tag assinada no perfil da loja declarando suporte a pagamentos divididos e recusa de lojas incompatíveis quando há uma taxa aplicável. Um [trabalho de administração já integrado](https://github.com/elisymlabs/elisym/pull/170) lê pedidos e anúncios de relays Nostr. Ele solicita a chave secreta da loja, exigindo confiança no código fornecido ao navegador e nas extensões; a administração local continua disponível. A implantação hospedada e a ativação de taxas na mainnet continuam sem verificação. O [Merchant-node 0.10.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.10.0) atualiza seu livro-razão sem suporte à reversão para uma versão anterior.

### Routstrd

O [Routstrd v0.4.16](https://github.com/Routstr/routstrd/releases/tag/v0.4.16) impede que uma recarga via [Nostr Wallet Connect](/pt/topics/nip-47/) cujo tempo limite foi excedido produza imediatamente outra fatura pagável. Ele [verifica a operação existente na mint](https://github.com/Routstr/routstrd/pull/144) até que o pagamento seja concluído ou falhe; um status indisponível mantém a recarga pausada. O gateway de inferência habilita provedores por rótulo de avaliação Nostr, sendo que rótulos experimentais exigem adesão explícita. A [versão 0.4.17](https://github.com/Routstr/routstrd/releases/tag/v0.4.17) inclui o SDK de suporte. A proteção contra operações não liquidadas permanece na memória, portanto reiniciar o daemon faz com que essa proteção seja perdida.

### Buzz

O [Buzz desktop 0.5.28](https://github.com/block/buzz/releases/tag/desktop-v0.5.28) permite que integrantes autenticados da equipe [naveguem por todas as comunidades e as moderem](https://github.com/block/buzz/pull/8027) em um relay sem trocar de conexão. As ações administrativas mantêm a comunidade, o relay e o assinador revisados; com a autenticação desativada, o console continua disponível para leitura. Separadamente, um [trabalho de relay já integrado](https://github.com/block/buzz/pull/8197) oculta event de exclusão devidamente marcados com tag para registros privados de autores, tanto em consultas quanto na entrega em tempo real. Essa correção do servidor exige implantação e não abrange cópias anteriormente divulgadas nem registros históricos de exclusão sem tag.

### Earthly

O [Earthly v0.1.21](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.21) permite que usuários [incorporem conjuntos de dados de mapas públicos do Nostr em sites](https://github.com/zeSchlausKwab/earthly/pull/35), com prévia e controles de aparência e posição inicial da câmera. Sua integração Maps MCP cria e publica mapas a partir do chat e depois gera links de compartilhamento ou incorporações. A integração continua sendo um piloto pessoal de plugin conectado. As incorporações aceitam conjuntos de dados em linha de até 300 feições e 48 KiB; conjuntos de dados privados, não publicados e baseados em blobs ficam de fora.

### Milk Market

O [Milk Market mobile v0.3.0](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.0) traz editores completos de design de vitrine para seu aplicativo de vendedores, com as mesmas seções e campos do editor web. O design de página por produto pode substituir as escolhas de tema e seções, incluindo metadados e imagens para redes sociais. A versão adiciona verificações para manter alinhadas as configurações mobile e web. A [versão 0.3.1](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.1) corrige o contraste no cartão de prévia mobile; os downloads para Android estão anexados às versões, com disponibilidade para iOS no TestFlight.

### Zeus

O [Zeus v13.2.3](https://github.com/ZeusLN/zeus/releases/tag/v13.2.3) inclui a [correção das taxas de roteamento do LDK](https://github.com/ZeusLN/zeus/pull/4353) abordada na semana passada, que agora foi lançada. Seu serviço Nostr Wallet Connect baseado em LDK pode incluir as taxas de roteamento informadas nas respostas e nos registros de gastos. As verificações de orçamento ainda consideram o valor da fatura antes da liquidação, com as taxas arredondadas debitadas posteriormente e um limite separado de 1.000 satoshis para taxas de roteamento. A versão também atualiza o LND integrado e inclui correções de segurança do rust-lightning; a validação em dispositivos NWC em operação continua sem verificação. A posterior [remoção do Zaplocker, já integrada](https://github.com/ZeusLN/zeus/pull/4933), descontinua seu fluxo de atestação e resgate via Nostr. Atualizar enquanto ainda há pagamentos retidos por esse servidor remove a possibilidade de resgate; os remetentes precisam aguardar a expiração da fatura de retenção e o reembolso. Essa descontinuação não faz parte da v13.2.3; sua implementação depende da desativação do servidor e do aviso aos usuários existentes.

## Em desenvolvimento

### nosvelte

A [correção do verificador de event do nosvelte](https://github.com/akiomik/nosvelte/pull/162) compara o ID fornecido de um event com o hash canônico de seus campos antes de verificar a assinatura. Anteriormente, o verificador padrão da biblioteca Svelte aceitava campos corretamente assinados que carregavam um ID substituído, permitindo que o conteúdo ocupasse a identidade de outro event e interferisse no tratamento de substituições. A alteração integrada se aplica aos caminhos de solicitação e envio da versão um que usam o verificador padrão; ela não certifica a exportação legada nem verificadores personalizados segundo o [formato de event do NIP-01](/pt/topics/nip-01/). Uma [correção posterior do filtro de solicitações](https://github.com/akiomik/nosvelte/pull/171) verifica e copia os campos de event do relay antes de compará-los. Dados malformados já não podem encerrar a assinatura do provedor padrão nem descartar seu próximo event válido. Clientes de mecanismo fornecidos pelo chamador podem manter o comportamento anterior de correspondência das dependências.

### nostter

O nostter [restringe indicações de relay fornecidas externamente](https://github.com/SnowCait/nostter/pull/2684) a URLs WebSocket seguras, rejeitando nomes de host locais e endereços IP não globais. Relays locais selecionados pela conta e URLs de assinadores remotos mantêm seus caminhos existentes; o DNS rebinding continua fora da verificação. O cliente web também [lê payloads experimentais separados de aviso de conteúdo](https://github.com/SnowCait/nostter/pull/2680) somente depois que o leitor pressiona Mostrar, verificando o ID do event referenciado, a correspondência do autor e uma tag `k` correspondente ao kind do event original. Reações e respostas têm como alvo o event original. Essas alterações integradas mantêm inalterado seu formato atual de publicação [NIP-36](/pt/topics/nip-36/).

### Coracle

O [editor de listas do Coracle](https://github.com/coracle-social/coracle/pull/679) restaura a edição e a exclusão ao aguardar a decodificação assíncrona antes de renderizar o formulário. Anteriormente, a edição perdia os campos da lista, e nem o salvamento nem a exclusão publicavam um event.

### Routstr Core

[O código-fonte da versão atual 0.5.0 do Routstr Core](https://github.com/Routstr/routstr-core/releases/tag/v0.5.0) [deixa de registrar nos logs as chaves privadas Nostr geradas automaticamente](https://github.com/Routstr/routstr-core/pull/812) e [preserva a identidade pública da primeira inicialização](https://github.com/Routstr/routstr-core/pull/818). [Os anúncios de provedores](https://github.com/Routstr/routstr-core/pull/823) excluem localhost e endereços HTTP literais privados ou locais de enlace; os nomes de host não são resolvidos nessa verificação. A tag atual inclui trabalho incorporado após sua data de publicação registrada, 7 de outubro, portanto os binários e as implantações históricos continuam sem verificação. Os logs expostos anteriormente ainda precisam ser revisados pelos operadores.

### Alby Hub

[A alteração na autorização de faturas do Alby Hub](https://github.com/getAlby/hub/pull/2629) limita a liquidação e o cancelamento às faturas criadas pelo aplicativo solicitante. A carteira auto-hospedada disponibiliza conexões de aplicativos por meio do [NIP-47, Nostr Wallet Connect](/pt/topics/nip-47/); a capacidade de uma conexão gerenciar suas faturas não deve conceder autoridade sobre as faturas de outro aplicativo. Uma [correção de privacidade separada para conexões isoladas](https://github.com/getAlby/hub/pull/2621) remove o endereço Lightning da carteira principal dos fluxos de sucesso no navegador para conexões isoladas.

### nak

[O comando relay incorporado ao nak](https://github.com/fiatjaf/nak/pull/222) verifica os tempos de conexão, leitura e escrita e as informações do relay, e então imprime events de descoberta de kind 30166 não assinados. Encaminhar esses resultados via pipe para `nak event` permite assiná-los e publicá-los, possibilitando o [monitoramento agendado de relays com NIP-66](/pt/topics/nip-66/) com a mesma ferramenta de terminal. As respostas de autenticação ou restrição observadas prevalecem sobre as informações anunciadas pelo relay. Os testes de escrita usam um event efêmero assinado por uma chave descartável; os anúncios de monitores de kind 10166 continuam sendo uma operação separada.

### Kehto

[A verificação de manifestos do Kehto](https://github.com/kehto/web/pull/277) verifica os manifestos assinados atuais de artefato único e os bytes dos artefatos antes da execução, mantendo separada a análise do formato legado. O shell napplet também [verifica os manipuladores recomendados](https://github.com/kehto/web/pull/294), consulta os usuários sobre conflitos com escolhas salvas e consome uma URL de invocação aceita para impedir entregas repetidas. A verificação do manifesto confere a identidade do publicador e os bytes do artefato; ela não estabelece que o código do aplicativo é seguro. [Os snapshots de gamepad](https://github.com/kehto/web/pull/297) agora acompanham o foco e a visibilidade. Os frames do Paja/playground bloqueiam o acesso nativo direto a gamepad, HID e USB antes da execução do código do aplicativo, deixando o acesso mediado a cargo do host. Os consumidores precisam dos pacotes de host correspondentes; a prontidão do shell é uma capacidade separada. Uma [alteração posterior na admissão do Paja](https://github.com/kehto/web/pull/305) alerta sobre domínios experimentais obrigatórios indisponíveis, mas permite o carregamento; esses domínios continuam sem disponibilizar APIs ou concessões de acesso.

### napplet SDK

[O napplet SDK implementa invocação baseada em URI e entrega retida](https://github.com/napplet/web/pull/228). [Os metadados de publicação são preservados no HTML autônomo](https://github.com/napplet/web/pull/226), e [referências opcionais de aplicativos](https://github.com/napplet/web/pull/239) conectam manifestos a listagens assinadas e capturas de tela sem alterar os hashes dos artefatos. O formato de referência de aplicativo continua sendo uma proposta. Os testes do shell de referência deixam a descoberta, a instalação e a verificação de assinaturas em produção a cargo dos hosts.

### rust-nostr

A biblioteca Rust para Nostr [rust-nostr preserva o progresso parcial de download junto com os erros terminais dos relays](https://github.com/nostrdevkit/nostr/pull/1483). O relay que falhou permanece no conjunto de falhas, de modo que os chamadores podem usar os events já recebidos sem perder a evidência de que a sincronização foi interrompida antes do fim.

### Pensieve

[A correção de segurança da reconciliação do Pensieve](https://github.com/andotherstuff/pensieve/pull/92) dá continuidade ao seu [trabalho de exclusão de events ausentes](https://github.com/andotherstuff/pensieve/pull/90). As ferramentas de relay e arquivamento solicitam novamente os IDs exatos que estão ausentes antes de classificar as falhas, impedindo que trechos finais de consultas truncadas por limites se tornem exclusões falsas. A contabilização de pausas é feita por tarefa, e os events já arquivados são tratados separadamente. Uma tarefa concluída pode manter registros explícitos de events ausentes; a conclusão, por si só, não comprova que o arquivo esteja completo.

[A reconciliação contínua do Premium Primal](https://github.com/andotherstuff/pensieve/pull/84) foi ativada em 12 de outubro. O [registro de implantação](https://github.com/andotherstuff/pensieve/pull/93) do operador informa que ambos os binários corrigidos foram implantados e que a pausa baseada em falhas foi ativada em 13 de outubro. Posteriormente, a [propagação de exclusões](https://github.com/andotherstuff/pensieve/pull/95) passou a reutilizar apenas exclusões originais comprovadas para o mesmo relay e uma janela sobreposta, excluindo propagações encadeadas e IDs recém-misturados; sua [implantação foi registrada naquela tarde](https://github.com/andotherstuff/pensieve/pull/97). A [verificação prévia do arquivo e a correção de travamento do cache](https://github.com/andotherstuff/pensieve/pull/98) foram [implantadas em 14 de outubro](https://github.com/andotherstuff/pensieve/pull/99). Uma [correção posterior na prioridade de propagação](https://github.com/andotherstuff/pensieve/pull/103) foi incorporada, mas ainda não havia sido implantada segundo seu registro de origem.

### njump

O visualizador web de Nostr [njump restaura os padrões de relay incorporados](https://github.com/fiatjaf/njump/pull/173) quando nenhum arquivo de substituição é fornecido. Ele também [isola renderizadores Markdown concorrentes](https://github.com/fiatjaf/njump/pull/171) e [cabeçalhos de resposta durante tempos limite](https://github.com/fiatjaf/njump/pull/169), corrigindo condições de corrida que podiam derrubar o processo ao renderizar events de formato longo citados ou atender a requisições simultâneas. Essas alterações do servidor foram incorporadas; a implantação em produção continua sem verificação.

### Nostr Components

[A correção na assinatura de zap do Nostr Components](https://github.com/saiy2k/nostr-components/pull/187) interrompe o fluxo de pagamento quando o assinador selecionado recusa a assinatura. Os widgets sociais incorporáveis não substituem mais a identidade por uma identidade anônima aleatória após a rejeição. Sua [agregação de recibos](https://github.com/saiy2k/nostr-components/pull/197) valida [recibos de zap do NIP-57](/pt/topics/nip-57/) antes de eliminar duplicatas de cópias de relays, faturas e IDs de requisições.

### rx-nostr

Na biblioteca de cliente reativa, [as alterações de verificação da versão quatro do rx-nostr](https://github.com/penpenpng/rx-nostr/pull/207) verificam a estrutura canônica dos events, os IDs e as assinaturas de maneira consistente entre JavaScript e WebAssembly. Uma lista vazia de condições de requisição não corresponde a nada e é concluída; o envio legado informa falha quando não tem destino. Os observadores de publicação não podem alterar a resolução, e os descendentes de requisições descartados não podem reiniciar. [Segmentos finitos de consulta](https://github.com/penpenpng/rx-nostr/pull/213) permitem que consultas retroativas sejam concluídas depois que todos os segmentos fornecidos terminarem. Essas alterações estão incluídas na [4.0.0 beta 2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%404.0.0-beta.2), uma versão de pré-lançamento com alterações incompatíveis na API.

### eHagaki

O cliente social [eHagaki adiciona entrega em etapas pela caixa de saída](https://github.com/Lokuyow/ehagaki/pull/268), fixando os relays de destino do autor antes da assinatura. Seu fluxo de publicações sensíveis envia a cada relay o payload antes da estrutura que faz referência a ele, usando a confirmação do próprio relay; o sucesso apenas do payload mantém o editor de publicações aberto. Uma [varredura completa do histórico de publicações](https://github.com/Lokuyow/ehagaki/pull/312) salva os resultados verificados de forma incremental. Intervalos ambíguos permanecem sem confirmação mesmo quando a varredura é exibida como concluída, com um controle de informações explicativo. O [suporte ao relay local Citrine](https://github.com/Lokuyow/ehagaki/pull/315) preserva os intervalos de navegação verificados e arquiva os events assinados exatos após uma publicação externa bem-sucedida. As confirmações locais não transformam um envio externo malsucedido em sucesso, e isso não adiciona uma fila de publicação offline. O [gerenciamento de mídia enviada](https://github.com/Lokuyow/ehagaki/pull/321) lista e exclui imagens e vídeos enviados em servidores NIP-96 e Blossom compatíveis. Uma [migração posterior do banco de dados](https://github.com/Lokuyow/ehagaki/pull/325) redefine o cache de exibição e o histórico de publicações, preservando rascunhos e solicitações de exclusão. Ela também impede que resultados de sincronização mais antigos na fila voltem a preencher o histórico após uma limpeza.

### Formstr

[A correção do resultado de envio do Formstr](https://github.com/formstr-hq/nostr-forms/pull/508) rejeita uma resposta ao formulário quando nenhum relay a aceita. O aplicativo de formulários Nostr mostra os resultados dos relays e oferece uma nova tentativa, preservando as respostas preenchidas. Webhooks e páginas de confirmação aguardam a aceitação, e o SDK recebe a mesma verificação. Uma confirmação do relay ainda é diferente de uma garantia de armazenamento de longo prazo, mas uma falha total de publicação não gera mais uma mensagem de sucesso.

### Auditable Voting

[Auditable Voting adiciona agrupamento opcional de cédulas por um worker privado](https://github.com/tidley/auditable-voting/pull/35). Definições assinadas pelo organizador selecionam a identidade de um worker, relays de DM e um limiar ou prazo para liberação. Os eleitores enviam [cédulas encapsuladas com gift wrap do NIP-17](/pt/topics/nip-17/) e autenticam os recibos em relação a esse worker; as delegações devem autorizar tanto o enfileiramento quanto a liberação. As cédulas liberadas usam a identidade do worker. O worker pode ler os envios, e os lotes liberados por prazo podem ser pequenos. Se nenhuma rota privada válida for encontrada, o cliente inspecionado recorre ao envio público. Este é um trabalho de desenvolvimento já integrado.

### MintRadar

[MintRadar adiciona alertas opcionais encapsulados com gift wrap](https://github.com/hroomnik007/MintRadar/pull/122) para problemas de mint ou melt, software desatualizado e perda de suporte a essas operações. Seu diretório de mints Cashu [conecta os controles da lista de acompanhamento](https://github.com/hroomnik007/MintRadar/pull/123) a essas configurações de notificação e as confirma após a resposta do servidor. Reservas atômicas impedem que verificações sobrepostas enviem o mesmo alerta, e uma publicação malsucedida nos relays libera a reserva para uma nova tentativa. [Mensagens privadas do NIP-17](/pt/topics/nip-17/) protegem o conteúdo das notificações; a aceitação pelo relay não confirma a leitura pelo destinatário.

### Nostr Docs

[A migração do Nostr Docs para um relay local](https://github.com/formstr-hq/nostr-docs/pull/65) encaminha as leituras e gravações do editor colaborativo de Markdown por um Web Worker com um cache de event em IndexedDB e uma caixa de saída para novas tentativas. Títulos de documentos e tags são preservados após recarregamentos, e edições sucessivas de metadados recebem marcações de tempo crescentes para que duas edições no mesmo segundo permaneçam distintas. O armazenamento existente de chaves de criptografia permanece intacto. A alternativa que usa o pool de rede não oferece a durabilidade da caixa de saída do worker, e aceitar uma publicação enfileirada não comprova a aceitação pelo relay.

### Pakstr

[O assinador local nativo do Pakstr](https://git.nostrdev.com/stuff/pakstr/pulls/105) permite que a camada nativa de seu aplicativo Android crie uma conta Nostr no dispositivo. A chave permanece na camada nativa, criptografada com uma chave de encapsulamento protegida pelo Android Keystore. Os resultados das assinaturas são verificados antes de retornar ao aplicativo web. A camada nativa oferece suporte à [assinatura no navegador via NIP-07](/pt/topics/nip-07/) e a solicitações criptografadas. A seleção do assinador só é aberta quando necessária e coordena solicitações simultâneas.

### Nostr WoT SDK

A biblioteca de rede de confiança [Nostr WoT SDK estende o consentimento de autenticação](https://github.com/nostr-wot/nostr-wot-sdk/pull/15) a solicitantes nativos e remotos tipados. Recusas armazenadas são verificadas antes das solicitações de consentimento, e o consentimento reutilizável fica vinculado ao transporte e ao destino solicitantes. As solicitações web continuam sendo de uso único por padrão. Seus [uploads gerenciados para Blossom](https://github.com/nostr-wot/nostr-wot-sdk/pull/13) validam bytes imutáveis, oferecem suporte a cancelamento e são interrompidos quando a sessão ativa muda, com autenticação vinculada ao servidor e restrições de redirecionamento.

### NosTube

[NosTube v0.2.49](https://github.com/flox1an/nostube/releases/tag/v0.2.49) fornece instaladores para desktop. Separadamente, um trabalho no servidor já integrado [adiciona publicação agendada durável](https://github.com/flox1an/nostube/pull/126). Os events são assinados antes do horário previsto, armazenados em SQLite e publicados por um worker que coloca as publicações em dia após períodos de inatividade. Seu [fluxo de edição e exclusão](https://github.com/flox1an/nostube/pull/124) acompanha marcadores de exclusão, a entrega a espelhos e a limpeza de arquivos de propriedade do usuário. A [configuração na primeira execução](https://github.com/flox1an/nostube/pull/134) distingue o assinador de navegador do usuário de uma chave de canal gerenciada pelo servidor. Blobs históricos sem proprietário permanecem fora da limpeza automática.

### diVine

[diVine 1.0.24](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.24) adiciona colaboração privada em clipes com créditos e verificações de proveniência assinada da captura ou edição. As legendas traduzidas selecionadas pelo espectador recorrem às originais enquanto a tradução está pendente ou não verificada. Essas verificações de proveniência não garantem uma gravação sem edições.

As [mudanças de roteamento](https://github.com/divinevideo/divine-mobile/pull/9884) do cliente de vídeos curtos consultam os relays de caixa de entrada dos destinatários para mensagens de chat de texto e vídeo e preservam resultados de entrega incertos. O [tratamento das cópias do remetente](https://github.com/divinevideo/divine-mobile/pull/10006) permite que as próprias mensagens de grupo dos usuários apareçam em seus outros dispositivos; cópias descartadas anteriormente exigem a reimportação da conta. [Envios parciais de grupo cancelados](https://github.com/divinevideo/divine-mobile/pull/10031) mantêm registros de “Não enviado a todos”; o cancelamento é definitivo e esses registros não permitem novas tentativas. A criação de grupos e o reconhecimento de novas salas iniciadas por outros participantes permanecem [condicionados a uma opção desativada por padrão](https://github.com/divinevideo/divine-mobile/pull/10020).

Mudanças posteriores no branch principal [mantêm cópias interrompidas de restauração do banco de dados fora do cache temporário](https://github.com/divinevideo/divine-mobile/pull/10118) e [preservam publicações agendadas, denúncias enfileiradas, edições de perfil e registros de chats removidos durante a reconstrução](https://github.com/divinevideo/divine-mobile/pull/10115). [Os prazos de envio incluem a reconexão aos relays](https://github.com/divinevideo/divine-mobile/pull/10127), reduzindo de 160 para 137 segundos o limite para tentar novamente envios abandonados. [As consultas de caixa de entrada ao indexador usam um pool separado e limitado](https://github.com/divinevideo/divine-mobile/pull/10116) para evitar a espera atrás de leituras do feed, e [os controles para seguir preservam a ação escolhida](https://github.com/divinevideo/divine-mobile/pull/10147) se a lista de contatos mudar antes da confirmação. Essas integrações posteriores deixam menos tempo para a confirmação dos relays durante reconexões lentas; reparos no banco de dados não podem restaurar dados perdidos anteriormente. Posteriormente, [cópias opcionais de gravações](https://github.com/divinevideo/divine-mobile/pull/10110) permitem que o backup da galeria no Android e no iOS preserve clipes recém-gravados. Cópias sem proveniência assinada recebem um aviso e não podem ser reimportadas; esse recurso fica desativado por padrão e exige armazenamento adicional.

### Conduit

Os aplicativos de comércio do [Conduit ganham uma caixa de entrada compartilhada durável](https://github.com/Conduit-BTC/conduit-mono/pull/616), mantendo a entrega e a recuperação de mensagens criptografadas entre Market e Merchant. A aceitação pelo relay do destinatário é preservada mesmo se a cópia para o próprio remetente falhar, com a recuperação reutilizando os mesmos bytes para evitar um segundo envio semântico. [Carteiras compartilhadas respaldadas por assinadores](https://github.com/Conduit-BTC/conduit-mono/pull/635) conectam os dois aplicativos. Esse caminho de recuperação confia ao assinador o texto em claro da recuperação; a integração do código-fonte, por si só, não comprova uma implantação em operação nem testes de aceitação com fundos. [Autorizações independentes de relay](https://github.com/Conduit-BTC/conduit-mono/pull/645) são preservadas quando várias rotas de conta compartilham uma URL. Desativar uma rota não apaga mais outra autorização assinada de lista de relays ou de caixa de entrada, e leituras incompletas ou que exigem autenticação mantêm um resultado de indisponibilidade. O [roteador de pagamentos já integrado](https://github.com/Conduit-BTC/conduit-mono/pull/613) divide um pagamento de aporte aprovado pelo comprador em repasses Lightning ao comerciante e ao fornecedor, seguidos da taxa do Conduit, com reconciliação exata da intenção e recuperação criptografada pela caixa de entrada Nostr compartilhada. A execução em produção e em homologação permanece desativada; a conclusão pelo provedor não comprova o resgate pelo destinatário nem a baixa do pagamento.

### Bitcredit

[A criptografia da persistência do Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1041) protege as chaves de identidade, de empresa e de títulos de seu aplicativo de títulos de crédito eletrônicos, incluindo a fila de reenvio Nostr, usando o mnemônico da identidade pessoal. A inicialização exige um mnemônico correspondente. O [gerenciamento de instâncias](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1043) permite que instâncias de testnet e mainnet mantenham suas assinaturas Nostr em segundo plano funcionando de forma independente em um único dispositivo.

## Novos projetos

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0) lança um gerenciador de senhas cujos cofres criptografados são sincronizados pelo Nostr. Ele oferece suporte a assinadores externos e mantém versões concorrentes dos itens, com importação e exportação em JSON do Bitwarden. As alterações são salvas localmente antes de aguardar a aceitação pelo relay. A versão inclui downloads para Android, desktop e CLI. O projeto se descreve como novo e recomenda um gerenciador comprovado para senhas críticas; a especificação do protocolo na versão marcada ainda está vazia. Seu [armazenamento web](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md) mantém a chave de criptografia junto aos dados protegidos.

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md) adiciona uma implementação em Common Lisp de chat em grupo com MLS sobre Nostr. O código de 9 de outubro adiciona convergência entre commits concorrentes e anexos Blossom criptografados, com testes de interoperabilidade com o cliente de linha de comando wn do MDK relatados pelo autor. A implementação não foi auditada, e as chaves de conta e os registros de mensagens não têm criptografia em repouso. Janelas temporizadas de convergência, reexecução além do horizonte de reversão e dissolução de grupos continuam sem implementação; a estrutura de testes inspecionada usa relays locais descartáveis.

### nalgorithm Android

[A versão Android do nalgorithm](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0) cria um feed Nostr classificado por preferências e um resumo em áudio gerado em segundo plano que pode ser reproduzido offline. Os usuários escolhem entre inferência hospedada, cobrada via Lightning, ou inferência com chave própria solicitada pelo telefone; são caminhos separados. O login oferece suporte ao Amber por meio de assinatura remota. As versões seguintes [corrigem a classificação com chave própria e a descoberta da lista de pessoas seguidas](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1), depois [preservam as curtidas de relays funcionais quando outro relay falha](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2) e melhoram a recuperação do resumo. [A versão 1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3) reorganiza a configuração do modelo e informa a ausência de dados necessários para o teste de conexão.

## Trabalho em protocolos e especificações

### Endpoints autenticados de napplets

Nas especificações NAP para aplicações napplet, os [identificadores de endpoint NAP-INC](https://github.com/napplet/naps/pull/104), incorporados em 9 de outubro, substituem nomes simples de handlers por identificadores autenticados. Nomes iguais de publicadores diferentes deixam de identificar o mesmo par. O ambiente de execução continua mediando a comunicação, e manifestos raiz ou de snapshot não precisam de uma coordenada `d` nomeada.

### Recomendações de handlers em links de invocação

[A recomendação em links de invocação](https://github.com/napplet/naps/pull/99), também incorporada em 9 de outubro, permite uma recomendação opcional de handler com `#naddr`. Um shell pode oferecer descoberta e instalação, recorrendo à resolução comum como alternativa. As preferências salvas e a política do shell têm precedência. Assim, um handler recomendado fornece uma pista para descoberta sem substituir a escolha existente do usuário nem transferir a autoridade de instalação ao remetente do link.

### Aceitação da entrega e trabalho da aplicação

[As alterações no anúncio de intenções e na entrega](https://github.com/napplet/naps/pull/91) derivam papéis e intenções do mesmo manifesto verificado, usando identificadores seguros para os publicadores. A aceitação da entrega deixa de depender de a aplicação de origem permanecer em execução. Uma resposta `ok: true` aceita a responsabilidade pela entrega; ela não significa que o trabalho da aplicação de destino foi concluído. O comportamento de novas tentativas e reinicializações continua sendo uma política do ambiente de execução sob essa alteração incorporada à especificação.

### Cadeias de ações do Cyberspace

[As regras revisadas de cadeias do Cyberspace](https://github.com/arkin0x/cyberspace/pull/48) fazem com que uma bifurcação invalide uma cadeia de ações assinada desde sua criação e exigem que os clientes confirmem a ponta atual antes de assinar outra ação. O mundo baseado em Nostr adiciona [140 cadeias sintéticas assinadas](https://github.com/arkin0x/cyberspace/pull/49) com vereditos normativos para as implementações. [As regras de atribuição de crédito em cópias](https://github.com/arkin0x/cyberspace/pull/47) usam referências `q` ao objeto original e notificam seu autor no caso de remixes públicos; cópias seladas omitem essa notificação. Essas são especificações incorporadas ao projeto, sem verificação da cobertura dos verificadores em produção.

### Confirmações de persistência de relays

[A proposta de persistência em aberto](https://github.com/nostr-protocol/nips/pull/2496) introduz confirmações de persistência, consultas PROOF e atestações opcionais de relay assinadas de kind 1797. Uma assinatura torna uma alegação de armazenamento atribuível a um relay; ela não comprova a retenção contínua. As consultas também revelam quais events interessam ao cliente.

### Fixações compartilhadas para grupos Marmot

[A proposta em aberto de fixação do Marmot](https://github.com/marmot-protocol/marmot/pull/434) define um estado compartilhado autenticado para até 64 referências a mensagens, com permissões para membros e administradores. Alterações efetivas exigem um MLS Commit e uma transição de época, e cada folha de membro resultante deve oferecer suporte ao recurso. As fixações não copiam o corpo das mensagens nem estendem a retenção, portanto os alvos indisponíveis continuam sem resolução. Os dados de teste fornecidos pressupõem um estado autenticado; eles não demonstram processamento criptográfico nem convergência entre clientes.

## NIP em profundidade: NIP-36 e NIP-38

### Avisos de conteúdo antes da exibição

[A NIP-36, sobre conteúdo sensível](/pt/topics/nip-36/), permite que autores adicionem uma tag `content-warning` a um event, incluindo opcionalmente um motivo. Um cliente pode ocultar o conteúdo até que o leitor escolha revelá-lo. A [especificação](https://github.com/nostr-protocol/nips/blob/master/36.md) deixa a interface a cargo dos clientes e permite tags suplementares de rotulagem. Adicionar um aviso não altera quem pode ler o event. Em uma publicação pública, relays e outros clientes continuam recebendo seu conteúdo.

[O analisador de tags de aviso do Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) reconhece a tag e trata um motivo ausente ou em branco como não especificado. [O editor do Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte) grava o motivo na tag; sua [visualização de conteúdo](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) respeita a configuração de conteúdo sensível do leitor e oferece uma ação para revelá-lo. [A visualização de notas do noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) aplica sua própria preferência de avisos e seu estado de expansão antes de mostrar a interface de aviso.

[A NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md) não criptografa events nem exige que sejam ocultados. A ausência de aviso não diz nada sobre o conteúdo; os clientes decidem como os avisos afetam as prévias e os controles de revelação.

### Status do perfil e expiração

[A NIP-38, sobre status de usuários](/pt/topics/nip-38/), usa events endereçáveis de kind 30315. O autor, o kind e a tag `d` identificam uma coordenada de status; `general` e `music` têm significados definidos. Um event mais recente substitui o status anterior nessa coordenada, enquanto um valor diferente de `d` permanece separado. Conteúdo vazio limpa um status. A [especificação](https://github.com/nostr-protocol/nips/blob/master/38.md) também permite referências a URLs, perfis, events e endereços.

Este event assinado da [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) mostra um status geral expirado. A grafia original do autor foi preservada.

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[O modelo de status do Damus](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift) lida com status gerais e musicais com expiração. [O serviço de status do Nostria](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts) ignora valores vazios ou expirados e publica status musicais usando a duração da faixa; suas assinaturas normais solicitam apenas os tipos geral e musical. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt) preserva o identificador `d` ao limpar um status. Tipos personalizados, portanto, exigem um acordo que vá além da estrutura compartilhada de transmissão.

Os status são declarações públicas de seus autores. Eles não comprovam a presença on-line nem que alguém ouviu uma faixa. Publicar músicas ou disponibilidade pode revelar hábitos, e a expiração opcional limita a exibição de informações desatualizadas sem prometer sua exclusão. A [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) continua sendo uma especificação opcional em rascunho, assim como a NIP-36. Os clientes podem implementar qualquer uma delas de forma independente, e suas configurações de exibição determinam o que os leitores veem.
