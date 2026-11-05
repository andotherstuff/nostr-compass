---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
translationOf: /en/newsletters/2026-11-04-newsletter.md
translationDate: 2026-11-05
---

Nesta semana, o [Amethyst](/pt/newsletters/2026-11-04-newsletter/#amethyst) lançou napplets inline com correções de uma [revisão de segurança de embeds](https://github.com/vitorpamplona/amethyst/pull/4710), o [Napplets](/pt/newsletters/2026-11-04-newsletter/#napplets---web-packages) vinculou a identidade dos applets a portas por documento, e as nightlies do [mdk do Marmot](/pt/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk) reforçaram as mensagens em grupo. Em outras frentes, relays, carteiras, bibliotecas de assinatura e novos apps mudaram, boa parte em código-fonte mergeado que ainda não foi lançado.

## Principais Notícias {#top-stories}

### Amethyst {#amethyst}

O Amethyst, cliente Android, lançou a [v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0), que executa napplets inline nas notas no Android 11+ e no desktop. Correções de uma [revisão de segurança de embeds](https://github.com/vitorpamplona/amethyst/pull/4710) fecham um caminho pelo qual qualquer napplet com acesso a relays podia ler DMs descriptografadas. A descriptografia agora exige uma permissão separada do usuário e `nostr.signEvent` exige permissão do signer, enquanto o renderizador Chromium do desktop continua sem sandbox. Uma [mudança na criptografia de anexos por arquivo](https://github.com/vitorpamplona/amethyst/pull/4701) dá a cada anexo de mensagem direta privada [NIP-17](/pt/topics/nip-17/) uma chave e um nonce AES-GCM novos, enquanto lotes de vários arquivos reutilizavam ambos. A descrição do risco feita upstream vem de análise de código, sem exploit reproduzido, e arquivos já enviados não são corrigidos.

### Marmot Protocol (mdk) {#marmot-protocol-mdk}

O mdk, kit de mensagens criptografadas do Marmot baseado em MLS para Nostr, publicou pré-lançamentos nightly apenas para testes, sem release estável nessa linha. Na nightly de 2 de novembro, [novos envios aguardam atrás dos mais antigos na fila](https://github.com/marmot-protocol/mdk/pull/2849) dentro de um grupo, mantendo as gerações de criptografia em ordem para membros que estão recuperando o histórico, embora isso não garanta contra mensagens perdidas. Um [reparo de Welcome perdido](https://github.com/marmot-protocol/mdk/pull/2936), mergeado e desativado por padrão, segue a [regra de heartbeat do Marmot](https://github.com/marmot-protocol/marmot/pull/497) e reenvia exatamente o Welcome retido assim que o heartbeat do destinatário mostra atividade pelo menos dez minutos após a publicação mais recente do carrier. A cadência do heartbeat ou o atraso de relógio podem adiar o reparo em uma hora ou mais, e a conclusão não tem limite superior. [Comandos de vinculação de dispositivos](https://github.com/marmot-protocol/mdk/pull/2922) continuam atrás da feature dev-device-groups, desativada por padrão, e ficam desligados em produção.

### Napplets - Pacotes Web {#napplets---web-packages}

O Napplets, os pacotes web para applets Nostr em sandbox, lançou [core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0), [nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0) e [shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0), que [vinculam a identidade do applet a uma MessagePort por documento](https://github.com/napplet/web/pull/302). A identidade verificada (dTag, artifactHash) fica atrelada à porta passada no hello a partir do iframe criado, e todo o tráfego NAP usa essa porta. Um documento carregado por navegação não recebe permissões. Shells que ainda usam mensagens via Window precisam atualizar, porque não há caminho de compatibilidade. Código-fonte posterior [trava o frame de pré-visualização no seu documento verificado](https://github.com/napplet/web/pull/305) com frame-src 'none'.

## Lançamentos com Tag {#tagged-releases}

### Marble {#marble}

O Marble, cliente beta construído sobre a assinatura por limiar do Cosign, consegue ler relays como feeds na [0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23). Um relay aberto pelo seu endereço mostra a própria descrição e depois suas postagens, das mais novas para as mais antigas. Relays favoritos ficam em uma lista kind 10012 e grupos de relays em conjuntos kind 30002, as mesmas listas que o Jumble usa. A release também reformula as reações, com uma bandeja de reações recentes e os emojis personalizados do próprio usuário.

### Sidecar {#sidecar}

O Sidecar, extensão de navegador para publicar notas e destaques da web, consegue apagar o backup da carteira dos relays na [1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6). Após uma confirmação, ele substitui a cópia criptografada por uma vazia e pede aos relays que a esqueçam, mantendo a carteira conectada. Não há garantia de que os relays apaguem o backup. Desde a [v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5), o Sidecar remove metadados EXIF, XMP e IPTC de JPEGs antes do upload, e sua [mudança na preparação de uploads](https://github.com/dmnyc/sidecar/pull/572) bloqueia qualquer JPEG que não possa ser limpo.

### Haps {#haps}

O Haps publica e instala pacotes nativos sob chaves Nostr. O [Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25) traz bundles para macOS, Linux e Windows com helpers htree fixados por checksum e um arquivo SHA256SUMS cobrindo todos os arquivos compactados. O código-fonte da 0.1.24 [grava referências Hashtree versionadas](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8) sob a especificação rascunho do Hashtree. O Haps 0.1.23 e anteriores não conseguem ler os novos catálogos sem um catálogo legado de transição ou um instalador ou build Cargo atualizado.

### Cosign {#cosign}

O Cosign, a biblioteca de assinatura por limiar por trás do beta do Marble, traz uma correção parcial de entrada em grupo na [0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9): uma entrada por meio de um convidador escaneado agora exige a contribuição desse convidador e partes de pelo menos dois remetentes distintos. Entradas de telefone para telefone continuam sem vínculo, então um atacante com duas chaves ainda é suficiente, e partes de descriptografia vazias ainda pulam a verificação de prova. Na [0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8), um servidor que escreve a lista de membros ainda pode escolher pontos de share com segredos conhecidos. Os telefones só recebem correções por meio de uma release do Marble.

### nostream {#nostream}

O nostream, relay em TypeScript com PostgreSQL, adiciona [sincronização de saída com peers](https://github.com/cameri/nostream/pull/1043) na [3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0). O worker lê os escopos de informação de relay [NIP-11](/pt/topics/nip-11/) de cada peer, autentica com a autenticação de cliente [NIP-42](/pt/topics/nip-42/) e reconcilia por meio da sincronização negentropy [NIP-77](/pt/topics/nip-77/), conferindo os eventos obtidos quanto a ID, assinatura e escopo. [Limites específicos por peer](https://github.com/cameri/nostream/pull/1034) só se aplicam depois que um peer configurado conclui o AUTH. Uma release de código-fonte não prova que algum relay a tenha implantado.

### diVine {#divine}

O diVine, cliente de vídeos curtos em loop, publicou a [Android 1.0.27 estável](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27) com stickers interativos em vídeos públicos; a disponibilidade para iOS e macOS não está confirmada. Uma [reconsulta abaixo da janela](https://github.com/divinevideo/divine-mobile/pull/10711), já mergeada, só roda depois que a restauração inicial do histórico termina, lendo gift wraps, DMs criptografadas [NIP-04](/pt/topics/nip-04/) descontinuadas e exclusões em páginas de 100 mensagens por relay. Ela percorre cada relay de forma independente, enquanto a drenagem de histórico existente compartilha um único cursor e pode pular o histórico mais antigo de um relay limitado. A cobertura é limitada e não recupera o histórico completo.

### Whistle {#whistle}

O Whistle, app móvel de compartilhamento de localização e chat em grupo, lançou a [2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1), sua primeira release pública no protocolo Marmot v2. Grupos existentes não podem ser migrados, então os grupos precisam ser recriados e todos os membros precisam atualizar, enquanto as identidades npub são mantidas. Escanear para entrar substitui códigos e links de convite. Em um problema conhecido, mensagens de chat enviadas offline podem chegar atrasadas ou nem chegar, o que a release atribui ao MarmotKit; o compartilhamento de localização não é afetado.

## Em Desenvolvimento {#in-development}

### Quartz {#quartz}

O Quartz, biblioteca Nostr em Kotlin Multiplatform, lançou a [retomada de assinaturas ao vivo após reconexão](https://github.com/vitorpamplona/quartz/pull/82) na release 2.14.0. Cada relay retoma a partir do created_at mais recente entregue, limitado ao relógio do dispositivo, e filtros de gift wrap recuam dois dias extras para cobrir datas retroativas. Eventos com timestamp mais antigo que um relay armazenou durante uma queda ainda podem ser perdidos. [Janelas negentropy que levam em conta contagens](https://github.com/vitorpamplona/quartz/pull/85), mergeadas e não lançadas, comparam uma contagem opcional de eventos [NIP-45](/pt/topics/nip-45/) com a contagem local e tratam as contagens dos relays como não confiáveis.

### Buzz {#buzz}

O Buzz mergeou uma mudança que [grava exclusões kind 5 e 9005 em uma única transação junto com o soft delete do alvo](https://github.com/block/buzz/pull/8944), de modo que uma falha não pode mais aceitar uma exclusão enquanto o alvo continua ativo. Linhas inconsistentes históricas não são reparadas. O perfil móvel da [NIP-RS](/pt/topics/nip-rs/), um rascunho do Buzz para estado de leitura entre dispositivos, foi mergeado e [sincroniza fronteiras de leitura entre dispositivos](https://github.com/block/buzz/pull/8998). Em relays mais antigos sem read_state_snapshot, as leituras locais continuam funcionando e a sincronização entre dispositivos para, sem fallback.

### Alby Hub {#alby-hub}

O Alby Hub, nó Lightning autocustodial que atende apps Nostr Wallet Connect [NIP-47](/pt/topics/nip-47/), mergeou uma [correção de migração de banco de dados](https://github.com/getAlby/hub/pull/2657) que preserva o contador de ID de cada tabela durante o db_migrate ou uma migração para Postgres. Antes dela, um novo app podia reutilizar o ID de um app excluído e herdar suas transações e seu saldo isolado. Nenhuma release com tag ou implantação contendo a correção foi identificada. Uma [mudança de notificações](https://github.com/getAlby/hub/pull/2677) separada isola falhas por app, embora notificações que falham ainda sejam descartadas sem nova tentativa.

### swift-nostr-client {#swift-nostr-client}

O swift-nostr-client, biblioteca Nostr em Swift 6, mergeou uma mudança incompatível que faz o [RemoteSigner executar o handshake de connect antes do primeiro comando](https://github.com/yysskk/swift-nostr/pull/287). A nova configuração connectsAutomatically tem padrão true, e um handshake que falha significa que o comando não é enviado. Como os segredos de assinatura remota [NIP-46](/pt/topics/nip-46/) são de uso único, apps que retomam uma sessão bunker com um par de chaves de cliente salvo precisam defini-la como false, ou o primeiro comando apresentará o segredo já usado. Nenhuma release foi marcada com tag.

## Novos Projetos {#new-projects}

### Trikey {#trikey}

O Trikey, uma carteira pré-alfa e não auditada cujo app de telefone e guardião se comunicam por mensagens criptografadas em relays Nostr, resolve o travamento do app ao abrir na [release 0.1.10-alpha](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf). Os dois lados agora mantêm um registro, que sobrevive a reinicializações, dos IDs de wraps já lidos e os ignoram antes de qualquer verificação de assinatura ou descriptografia. Dicas de expiração em pedidos e alertas não garantem exclusão pelos relays, e as medições de desempenho do publicador foram feitas em um laptop.

### Pacto {#pacto}

O Pacto, app desktop de organização comunitária que roda grupos Marmot legados junto com DMs NIP-17, lançou a [v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5) sem assinatura, com edição de mensagens enviadas por até um minuto. Suas [correções de entrega de DMs](https://github.com/covenant-gov/pacto-app/pull/425) fazem os envios falharem imediatamente quando o pool não tem relay confiável e encaminham indicadores de digitação por relays confiáveis. Pull requests abertos e não mergeados adicionariam [eventos de squad](https://github.com/covenant-gov/pacto-app/pull/488) e [documentos de squad criptografados](https://github.com/covenant-gov/pacto-app/pull/490).

### Mialuna {#mialuna}

O Mialuna, cliente Nostr em Flutter focado em mídia, publicou um [anúncio da release 0.19.0](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez) que adiciona pedidos de exclusão para os stories do próprio usuário quando expiram. O [commit do changelog](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886) registra pedidos de exclusão a relays e exclusão de mídia no Blossom, com contas de chave local fazendo isso automaticamente e contas Amber ou bunker aguardando até que o usuário escolha Delete now. O APK e seu comportamento no dispositivo não foram verificados de forma independente. Pedidos de exclusão não garantem que relays ou servidores apaguem os dados.

### whereAreYou {#whereareyou}

O whereAreYou, app Android que compartilha localização dentro de círculos aos quais se entra por QR code ou link de convite, criptografa coordenadas com AES-256-GCM e as envia por relays públicos. Um [commit de assinatura por membro](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e) impede que detentores da chave do círculo publiquem como outro membro, e todos os dispositivos precisam atualizar. Sobre o [backup de identidade em Base45](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc), o autor alerta que qualquer pessoa que fotografe o QR code poderia adivinhar seu código de oito dígitos offline, segundo a estimativa dele em dezenas de minutos de tempo de GPU; nenhum benchmark foi publicado. O código-fonte não traz nenhum aval de segurança.

## Trabalho em Protocolo e Especificações {#protocol-and-spec-work}

### O Buzz define rotas de credenciais de agentes autorizadas pelo dono {#buzz-defines-owner-authorized-agent-credential-routes}

O Buzz mergeou, na [NIP-FA](/pt/topics/nip-fa/), um [rascunho para credenciais de agentes autorizadas pelo dono](https://github.com/block/buzz/pull/9015), definindo rotas de concessão, asserção e revogação para agentes autorizados por meio da atestação de dono [NIP-OA](/pt/topics/nip-oa/). Uma concessão vem de uma troca de tokens RFC 8693 que combina a sessão do dono com uma prova de autenticação HTTP [NIP-98](/pt/topics/nip-98/) do agente, e a revogação desconecta o agente e impede que sua chave se inscreva novamente. A NIP-FA é uma especificação do Buzz mergeada apenas no código-fonte, sem alegação de ativação em produção ou interoperabilidade.

### Assinaturas de eventos pós-quânticas ganham regras exatas de validação {#post-quantum-event-signatures-gain-exact-validation-rules}

A antiga proposta aberta de assinaturas pós-quânticas ganhou [regras exatas de validação ML-DSA-44 para eventos Nostr](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6). Chaves e assinaturas têm comprimentos fixos, verificadores checam a assinatura sobre os 32 bytes brutos do digest do ID do evento com contexto vazio, e nenhum algoritmo de fallback é permitido. A identidade proposta não tem codificação bech32 [NIP-19](/pt/topics/nip-19/), e novas assinaturas não tornam payloads criptografados [NIP-44](/pt/topics/nip-44/) nem gift wraps [NIP-59](/pt/topics/nip-59/) seguros no cenário pós-quântico.

### Uma precondição assinada proposta evita substituições de eventos perdidas {#a-proposed-signed-precondition-prevents-lost-event-replacements}

Um pull request aberto no Buzz [propõe uma precondição assinada NIP-CS local ao projeto](https://github.com/block/buzz/pull/8835) para eventos substituíveis e endereçáveis, e ela não é uma NIP oficial. A tag assinada indica o ID atual do head ou `none`, e o relay a verifica atomicamente sob um lock de coordenada, rejeitando uma escrita desatualizada com um OK false ou HTTP 409 e sem armazenar nada. Escritas sem a tag funcionam como antes, e a tag não dá garantia de compare-and-swap entre relays.

## Mergulho em NIP: NIP-31 e NIP-73 {#nip-deep-dive-nip-31-and-nip-73}

Clientes frequentemente encontram conteúdo que não entendem nativamente. A [NIP-31: Lidando com tipos de evento desconhecidos](/pt/topics/nip-31/) dá a um tipo de evento desconhecido um rótulo legível, e a [NIP-73: IDs de conteúdo externo](/pt/topics/nip-73/) nomeia assuntos fora do Nostr, como livros ou páginas web. As duas convenções são especificações independentes já existentes ([texto da NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md), [texto da NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)).

### A NIP-31 está marcada como não recomendada {#nip-31-is-marked-unrecommended}

O [texto atual da NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md) abre com um aviso que a marca como `unrecommended` por ser "desnecessariamente inchada", e sua linha de status diz rascunho, não recomendada e opcional. Eventos que usam a convenção já existem em relays, então a mecânica abaixo descreve como os clientes os leem, sem recomendação para novos protocolos.

### O que uma tag alt carrega {#what-an-alt-tag-carries}

Segundo a [especificação](https://github.com/nostr-protocol/nips/blob/master/31.md), o autor de um kind personalizado que não foi feito para ser lido como texto adiciona uma tag `alt` com um breve resumo em texto simples. Não se espera que clientes centrados no kind 1 solicitem outros kinds, mas os usuários ainda podem referenciar esses eventos a partir de notas, onde um resumo fornece contexto. Um rótulo não pode registrar um voto nem atender a um pedido de carteira. Para interações mais ricas, a especificação aponta para a [NIP-89: Handlers de aplicativos recomendados](/pt/topics/nip-89/).

Como `alt` é uma tag, o ID do evento e a assinatura da [NIP-01](/pt/topics/nip-01/): [Descrição do fluxo básico do protocolo](https://github.com/nostr-protocol/nips/blob/master/01.md) a cobrem. Uma assinatura válida autentica um resumo controlado pelo autor: mostra que o autor publicou o rótulo sem mostrar que ele é preciso, então resumos enganosos são possíveis. Tags são públicas, então um `alt` em um evento com conteúdo criptografado expõe seu resumo e pode revelar o que o conteúdo oculta. Essas propriedades vêm do envelope da [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md), fora do texto normativo da NIP-31. Uma tag `alt` de nível superior também é distinta do campo `alt` de descrição de imagem dentro de `imeta`, e os renderizadores os interpretam separadamente.

### Como dois clientes leem alt {#how-two-clients-read-alt}

No [card de evento desconhecido do noStrudel no commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), a primeira tag `alt` tem os espaços aparados e se torna o rótulo principal, com uma linha opcional `Using <client>`. Um valor ausente ou em branco gera `Unknown event (kind ...)`, e até três linhas de conteúdo aparecem de forma independente. O mesmo componente resolve a tag `client` por meio de templates de handlers NIP-89, mostrando Open quando existe um endereço compartilhável e `Open in <client>` quando um link de handler válido é resolvido. Explicação e despacho para o app são controles separados.

O [UnknownEventDigest.kt do Amethyst no commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) prefere conteúdo que classifica como prosa e recorre ao `alt` como alternativa. Seu parser apara os valores e pega o primeiro `alt` não vazio, então um evento cujo primeiro `alt` está em branco pode receber aqui um rótulo diferente do que recebe no noStrudel. Ambas as descrições refletem o código-fonte nesses commits, não comportamento confirmado em release.

### Exemplo: uma enquete com rótulo alt {#example-a-poll-with-an-alt-label}

A enquete kind 1068 abaixo foi obtida de wss://relay.damus.io, e seu ID e sua assinatura BIP340 são válidos segundo as regras da [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md). Um renderizador genérico pode mostrar o texto bilíngue do `alt`, enquanto um cliente que entende enquetes lê as tags `option` e `polltype`.

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### Assuntos e famílias da NIP-73 {#nip-73-subjects-and-families}

A [especificação NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md) (rascunho, opcional, sem marcação de não recomendada) coloca um assunto externo em uma tag `i` e sua família de identificadores em uma tag `k`, para que clientes possam consultar um assunto exato ou uma família inteira. Um livro usa `["i", "isbn:9780765382030"]` com `["k", "isbn"]`, e uma página web usa sua URL com `k` definido como `web`. A NIP-73 não define nenhum kind de evento; outros eventos carregam as tags.

### Normalização e dicas de URL {#normalization-and-url-hints}

A correspondência depende de strings idênticas, então a [especificação](https://github.com/nostr-protocol/nips/blob/master/73.md) fixa uma forma por família: URLs normalizadas sem fragmento, ISBNs sem hífens, geohashes em minúsculas, códigos ISO 3166 em maiúsculas. Um terceiro elemento opcional do array traz uma dica de URL para clientes que não têm tratamento próprio para o identificador. O autor escolhe essa dica, e ela não faz parte da identidade. Ela também não prova propriedade nem nomeia um site canônico.

### O que um identificador compartilhado não prova {#what-a-shared-identifier-does-not-prove}

Pela [NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md), identificadores iguais unem conversas e não estabelecem mais nada. Um comentário assinado identifica seu comentarista, mas não autentica o livro, o site ou o publicador do podcast nem mostra quem os controla. Aliases, ISBNs específicos de edição e URLs que se normalizam de forma diferente podem dividir um mesmo assunto em várias threads. O contexto importa: a [NIP-22](/pt/topics/nip-22/): [Comentário](https://github.com/nostr-protocol/nips/blob/master/22.md) usa `I`/`K` maiúsculas para o escopo raiz e `i`/`k` minúsculas para o pai, e a [NIP-39: Identidades externas em perfis](/pt/topics/nip-39/) usa `i` para identidades de perfil, então nem toda tag `i` é um assunto NIP-73.

### NIP-73 em código de parser e renderizador {#nip-73-in-parser-and-renderer-code}

O [nip73.rs do rust-nostr no commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) interpreta prefixos conhecidos como um `ExternalContentId` tipado e transforma uma dica opcional em uma URL tipada, emitindo o terceiro elemento da tag apenas quando existe uma dica. Seus testes mantêm ISBNs com hífens: o parser remove o prefixo e armazena o restante sem aplicar a normalização da especificação, então o parsing tipado não garante strings canônicas. Ele separa IDs de cadeia da família, mapeando `ethereum:100:tx:<hash>` para `ethereum:tx`. Essa revisão não tem variante de país `iso3166`.

O [DisplayExternalId.kt do Amethyst no commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) envia identificadores de geohash e hashtag para exibições dedicadas. Identificadores de URL também têm exibição dedicada, enquanto outros tipos suportados vão para um chip de escopo genérico. Uma URL abre a rota de thread do próprio app para aquela página. Com as pré-visualizações desativadas, a renderização normal mostra um chip de link simples e não solicita pré-visualização. Com as pré-visualizações ativadas, buscar uma pré-visualização ausente pode contatar o site de destino. Desativar as pré-visualizações evita essa requisição na renderização normal. Nenhum dos arquivos estabelece comportamento de release.

### Exemplo: um comentário em uma página web {#example-a-comment-on-a-webpage}

Este comentário kind 1111, obtido de wss://nos.lol, coloca a mesma URL de uma thread pública do Reddit tanto no par `I`/`K` quanto no par `i`/`k`, com `web` como família sob a [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) e a NIP-73. Seu ID e sua assinatura são válidos, o que identifica quem escreveu o comentário e não diz nada sobre a página vinculada.

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
