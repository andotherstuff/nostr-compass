---
title: 'Nostr Compass #5'
date: 2026-01-13
publishDate: 2026-01-13
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal para o Nostr.

**Esta semana:** O Bitchat passa por uma auditoria de segurança profissional pela Cure53, a mesma empresa que auditou o Signal e o [NIP-44](/pt/topics/nip-44/), com mais de 17 PRs já mesclados corrigindo descobertas críticas. O [NIP-71](/pt/topics/nip-71/) é mesclado, trazendo eventos de vídeo endereçáveis para o protocolo. Um NIP de criptografia pós-quântica abre discussão sobre como preparar o Nostr para o futuro contra ataques quânticos. O Amethyst v1.05.0 lança listas de favoritos, notas de voz e uma versão inicial para desktop, enquanto o Nostur v1.25.3 melhora as DMs do [NIP-17](/pt/topics/nip-17/) com reações e respostas. Em notícias de bibliotecas, o rust-nostr expande o suporte ao [NIP-62](/pt/topics/nip-62/) para os backends SQLite e LMDB, e o NDK corrige um bug de rastreamento de assinaturas.

## Notícias

### Bitchat Conclui Auditoria de Segurança da Cure53

O Bitchat, o mensageiro criptografado para iOS que combina Nostr com Cashu, passou por uma auditoria de segurança profissional pela Cure53, uma das empresas de segurança mais respeitadas do setor. A Cure53 auditou anteriormente o Signal, o Mullvad VPN e, notavelmente, a especificação de criptografia [NIP-44](/pt/topics/nip-44/) que sustenta as mensagens privadas modernas do Nostr.

A auditoria encontrou mais de 12 problemas de segurança (BCH-01-002 até BCH-01-013). A equipe do Bitchat respondeu com mais de 17 pull requests. As principais correções incluem:

**Limpeza de Segredo DH do Protocolo Noise** - O [PR #928](https://github.com/permissionlesstech/bitchat/pull/928) corrige seis locais onde os segredos compartilhados Diffie-Hellman não estavam sendo zerados após o acordo de chaves, restaurando as garantias de forward secrecy. Quando os segredos persistem na memória por mais tempo do que o necessário, um dump de memória ou ataque cold boot poderia comprometer comunicações passadas.

**Verificação de Assinatura** - Múltiplos PRs fortalecem os caminhos de verificação criptográfica, garantindo que as verificações de autenticidade das mensagens não possam ser contornadas através de entradas malformadas.

**Thread Safety** - O [PR #929](https://github.com/permissionlesstech/bitchat/pull/929) adiciona sincronização de barreira às filas de confirmação de leitura no NostrTransport, prevenindo condições de corrida que poderiam causar corrupção de dados ou travamentos sob alto volume de mensagens.

**Segurança de Memória** - O [PR #920](https://github.com/permissionlesstech/bitchat/pull/920) otimiza o deduplicador de mensagens para melhor desempenho com alto throughput de mensagens, evitando esgotamento de memória.

**Validação de Entrada** - O [PR #919](https://github.com/permissionlesstech/bitchat/pull/919) fortalece a análise de strings hexadecimais para prevenir travamentos por entrada malformada, um vetor de ataque comum para negação de serviço.

O Bitchat lida com ecash Cashu, tornando a revisão de segurança profissional essencial. A auditoria segue a auditoria do Protocolo [Marmot](/pt/topics/marmot/) do ano passado e a auditoria do NIP-44 que verificou a camada de criptografia.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mesclados:**

- **[NIP-71](/pt/topics/nip-71/)** - Eventos de Vídeo Endereçáveis ([#1669](https://github.com/nostr-protocol/nips/pull/1669)) introduz os kinds 34235 (vídeo horizontal) e 34236 (vídeo vertical) como eventos endereçáveis. Uma tag `d` obrigatória fornece identificadores únicos, para que os metadados do vídeo possam ser atualizados sem republicar o evento inteiro. Uma tag `origin` opcional rastreia fontes de importação. Já implementado no Amethyst e nostrvine.

**PRs Abertos:**

- **Criptografia Pós-Quântica** - O [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) propõe adicionar algoritmos criptográficos resistentes a quantum ao Nostr. A especificação introduz ML-DSA-44 e Falcon-512 para assinaturas digitais, visando "eventos de valor super alto" como aplicações e autoridades, em vez de usuários individuais. Enquanto a criptografia simétrica do [NIP-44](/pt/topics/nip-44/) (ChaCha20) é resistente a quantum, sua troca de chaves usa secp256k1 ECDH que é vulnerável ao algoritmo de Shor. A proposta inclui ML-KEM para acordo de chaves para resolver essa lacuna. Esta é uma proposta em estágio inicial abrindo discussão sobre agilidade criptográfica para a segurança de longo prazo do Nostr.
- **BOLT12 para NIP-47** - Após 137 comentários e discussão extensiva, a comunidade decidiu que as ofertas BOLT12 merecem sua própria especificação em vez de estender o [NIP-47](/pt/topics/nip-47/). As ofertas BOLT12 fornecem melhorias significativas sobre faturas BOLT11, incluindo reutilizabilidade, melhor privacidade através de caminhos cegos e informações opcionais do pagador. O novo NIP definirá métodos como `make_offer`, `pay_offer` e `list_offers` para implementações do Nostr Wallet Connect.
- **NIP de Faixa de Áudio** - O [PR #1043](https://github.com/nostr-protocol/nips/pull/1043) propõe kinds 32100 para faixas de música e 32101 para episódios de podcast, dando ao conteúdo de áudio o mesmo tratamento de primeira classe que o NIP-71 fornece para vídeo. Atualmente, plataformas de áudio como Wavlake, Zapstr e Stemstr usam formatos de eventos proprietários, fragmentando o ecossistema. Um padrão comum permitiria interoperabilidade para que os usuários pudessem descobrir e reproduzir áudio de qualquer cliente compatível.
- **NIP-A3 Alvos de Pagamento Universais** - O [PR #2119](https://github.com/nostr-protocol/nips/pull/2119) propõe eventos kind 10133 usando URIs `payto:` RFC-8905 para expor opções de pagamento através de múltiplas redes. Em vez de criar kinds de eventos separados para Bitcoin, Lightning, Cashu ou trilhos de pagamento tradicionais, essa abstração permite que os clientes analisem tags padronizadas e invoquem manipuladores de pagamento nativos. A abordagem é à prova de futuro, já que novos métodos de pagamento precisam apenas de um esquema de URI `payto:`.

## Aprofundamento em NIPs: NIP-51 e NIP-65

Esta semana cobrimos dois NIPs que armazenam preferências do usuário: NIP-51 para organizar conteúdo e NIP-65 para organizar conexões de relay. Ambos usam eventos substituíveis, o que significa que cada nova publicação sobrescreve a versão anterior.

### [NIP-51](/pt/topics/nip-51/): Listas

O [NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) define múltiplos tipos de lista para organizar referências a eventos, usuários, hashtags e outros conteúdos. O Amethyst v1.05.0 adiciona suporte a favoritos, tornando este um bom momento para entender como as listas funcionam.

A especificação define vários kinds de lista, cada um servindo a um propósito diferente. O Kind 10000 é sua lista de silenciados para ocultar usuários, threads ou palavras. O Kind 10001 fixa eventos para destacar em seu perfil. O Kind 30003 armazena favoritos, que é o que o Amethyst agora suporta. Outros kinds lidam com conjuntos de seguidos (30000), coleções de artigos curados (30004), interesses de hashtags (30015) e conjuntos de emojis personalizados (30030).

As listas referenciam conteúdo através de tags. Uma lista de favoritos usa tags `e` para eventos específicos e tags `a` para conteúdo endereçável como artigos:

```json
{
  "id": "ae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 30003,
  "tags": [
    ["d", "saved-articles"],
    ["e", "abc123def456...", "wss://relay.example"],
    ["a", "30023:author-pubkey:article-id", "wss://relay.example"]
  ],
  "content": "<encrypted-private-bookmarks>",
  "sig": "908a15e46fb4d8675bab026fc230a0e3542bfade63da02d542fb78b2a8513fcd0092619a2c8c1221e581946e0191f2af505dfdf8657a414dbca329186f009262"
}
```

A tag `d` fornece um identificador único, para que você possa manter múltiplos conjuntos de favoritos como "saved-articles", "read-later" ou "favorites" sob o mesmo kind.

As listas suportam itens públicos e privados. Itens públicos aparecem no array de tags, visíveis para qualquer pessoa que busque o evento. Itens privados vão no campo `content`, criptografados usando [NIP-44](/pt/topics/nip-44/) para você mesmo. Essa estrutura dupla permite que você mantenha favoritos públicos enquanto anexa notas privadas, ou mantenha uma lista de silenciados sem revelar quem você silenciou. Para criptografar para você mesmo, use o NIP-44 com sua própria pubkey como destinatário.

Os kinds da série 10000 são substituíveis, o que significa que os relays mantêm apenas um evento por pubkey. Os da série 30000 são substituíveis parametrizados, permitindo um evento por combinação de pubkey e tag `d`. Em ambos os casos, atualizar uma lista significa publicar uma substituição completa; você não pode enviar mudanças incrementais. Os clientes devem preservar tags desconhecidas ao modificar listas para evitar sobrescrever dados adicionados por outras aplicações.

### [NIP-65](/pt/topics/nip-65/): Metadados de Lista de Relays

O [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) define eventos kind 10002 que anunciam quais relays um usuário prefere para leitura e escrita. Isso ajuda outros usuários e clientes a encontrar seu conteúdo.

```json
{
  "id": "bd2217a96b5835b59f9a6a42d8d8a36f8c9b7d4e5f0a1b2c3d4e5f6a7b8c9d0e1",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "f1c2d3e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

Cada tag `r` contém uma URL de relay e um marcador opcional. Um marcador `write` designa sua outbox: relays onde você publica seu conteúdo. Um marcador `read` designa sua inbox: relays onde você verifica menções, respostas e tags. Omitir o marcador indica ambos.

Quando Alice quer encontrar os posts de Bob, seu cliente busca o kind 10002 de Bob, extrai seus relays de escrita (sua outbox) e se inscreve lá. Quando Alice responde a Bob, seu cliente publica em seus relays de leitura (sua inbox) para que ele veja a menção. Esse roteamento consciente de relays é o "modelo outbox", e ele distribui os usuários entre muitos relays em vez de concentrar todos em poucos servidores centrais.

O NIP-65 lida com roteamento de conteúdo público, mas mensagens privadas usam uma lista separada. O [NIP-17](/pt/topics/nip-17/) define o kind 10050 para relays de inbox de DM, usando tags `relay` em vez de tags `r`. Ao enviar a alguém uma mensagem privada, os clientes procuram o evento kind 10050 do destinatário e publicam a mensagem gift-wrapped criptografada lá. Essa separação mantém o roteamento de DM distinto do roteamento de conteúdo público e permite que os usuários especifiquem relays diferentes para comunicação privada versus pública.

O modelo outbox melhora a resistência à censura, já que nenhum relay único precisa armazenar ou servir o conteúdo de todos. Os clientes mantêm conexões com relays listados nos eventos NIP-65 de seus usuários seguidos, conectando-se dinamicamente a novos relays conforme descobrem novas contas. O NIP-65 complementa as dicas de relay encontradas em outros NIPs. Quando você marca alguém com `["p", "pubkey", "wss://hint.relay"]`, a dica informa aos clientes onde procurar essa referência específica. O NIP-65 fornece a lista autoritativa controlada pelo usuário, enquanto as dicas oferecem atalhos incorporados em eventos individuais.

Para melhores resultados, mantenha sua lista de relays atualizada, já que entradas desatualizadas tornam você mais difícil de encontrar. A especificação recomenda de dois a quatro relays por categoria. Listar muitos relays sobrecarrega cada cliente que deseja buscar seu conteúdo, diminuindo sua experiência e aumentando a carga da rede. Os clientes armazenam em cache os eventos NIP-65 e os atualizam periodicamente para se manterem atualizados conforme os usuários atualizam suas preferências.

## Lançamentos

**Amethyst v1.05.0** - O popular cliente Android [lança uma atualização importante](https://github.com/vitorpamplona/amethyst/releases) com várias funcionalidades de destaque. As listas de favoritos [NIP-51](/pt/topics/nip-51/) kind 30003 permitem que os usuários salvem posts para referência posterior, sincronizando entre clientes compatíveis. As notas de voz agora funcionam em DMs e posts regulares com visualização de forma de onda, seleção de servidor de mídia e indicadores de progresso de upload. As pontuações de [Web of Trust](/pt/topics/web-of-trust/) agora são visíveis na interface, ajudando os usuários a entender como o algoritmo avalia contas em relação ao seu grafo social. A migração do banco de dados [Quartz](/pt/topics/quartz/) melhora o desempenho de consultas como parte do trabalho de Kotlin Multiplatform financiado pela OpenSats. Uma versão inicial para desktop traz o Amethyst para Windows, macOS e Linux via Compose Multiplatform, compartilhando a mesma base de código do aplicativo Android. Novos fluxos de onboarding suavizam a experiência para usuários de primeira viagem no Nostr.

**Nostur v1.25.3** - O cliente iOS e macOS [foca em mensagens privadas](https://github.com/nostur-com/nostur-ios-public/releases) com melhorias no [NIP-17](/pt/topics/nip-17/). As conversas de DM agora suportam reações e respostas, trazendo a interatividade dos posts públicos para mensagens criptografadas. A visualização de conversa foi reformulada com melhor threading para que trocas de múltiplas mensagens sejam mais fáceis de seguir, e os timestamps mostram "tempo atrás" na lista de DM para escaneamento rápido. Usuários de desktop ganham layouts de múltiplas colunas para visualizar múltiplos feeds ou conversas lado a lado. O suporte a assinante remoto [NIP-46](/pt/topics/nip-46/) permite que os usuários mantenham suas chaves privadas em aplicativos de assinatura dedicados como Amber ou nsec.app. Correções adicionais restauram a funcionalidade de DM no iOS 15 e iOS 16, resolvem atrasos de notificação e adicionam a capacidade de configurar quais relays recebem DMs publicadas.

## Mudanças notáveis de código e documentação

*Estes são pull requests abertos e trabalhos em estágio inicial, perfeitos para obter feedback antes de serem mesclados. Se algo chamar sua atenção, considere revisar ou comentar!*

### Citrine (Relay Android)

O [PR #89](https://github.com/greenart7c3/Citrine/pull/89) corrige uma vulnerabilidade de injeção SQL no aplicativo de relay pessoal para Android. O problema permitia que dados de eventos malformados executassem consultas arbitrárias ao banco de dados, uma falha séria para qualquer aplicativo que armazena e processa entrada não confiável. A correção sanitiza adequadamente todas as operações de banco de dados usando consultas parametrizadas. Nenhuma versão foi marcada ainda, então os usuários precisarão esperar pela próxima versão ou compilar a partir do código-fonte. O [PR #90](https://github.com/greenart7c3/Citrine/pull/90) otimiza o desempenho de consultas do ContentProvider com filtragem e paginação em nível de banco de dados, reduzindo a latência quando aplicativos externos como o Amethyst acessam o banco de dados de eventos do Citrine através da camada de comunicação entre processos do Android.

### rust-nostr (Biblioteca)

O suporte ao [NIP-62](/pt/topics/nip-62/) (Vanish Requests) está se expandindo pelos backends de banco de dados do rust-nostr. O [PR #1180](https://github.com/rust-nostr/nostr/pull/1180), mesclado há duas semanas, adicionou suporte ao NIP-62 para SQLite, lidando com requisições vanish `ALL_RELAYS` já que a camada de banco de dados não conhece URLs de relay específicos. O [PR #1210](https://github.com/rust-nostr/nostr/pull/1210) estende isso para o backend LMDB, garantindo que as requisições vanish sejam persistidas no disco e sobrevivam a reinicializações do relay. Uma implementação IndexedDB para ambientes de navegador também está em andamento. Juntas, essas mudanças dão aos desenvolvedores suporte consistente ao NIP-62 através de SQLite, LMDB e em breve armazenamento de navegador.

### NDK (Nostr Development Kit)

O [PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) corrige um bug no sistema de rastreamento seenEvents. O problema fazia com que certos padrões de assinatura marcassem incorretamente eventos como já vistos, levando à perda de conteúdo quando os usuários abriam novas assinaturas ou reconectavam a relays. A correção garante que os eventos sejam rastreados com precisão ao longo dos ciclos de vida das assinaturas, o que é particularmente importante para aplicações que assinam e cancelam assinaturas dinamicamente com base na navegação do usuário. O NDK foi atualizado para beta.70 com essa correção incluída.

### Damus (iOS)

O [PR #3515](https://github.com/damus-io/damus/pull/3515) corrige um travamento de inicialização afetando usuários do iOS 17. O problema decorreu de um overflow aritmético em `NdbUseLock`, uma classe de fallback usada porque Swift Mutexes não estão disponíveis no iOS 17. A correção substitui a abordagem de sincronização anterior por `NSLock`, que está disponível no iOS 17 e lida corretamente com as condições de corrida restantes. Usuários do iOS 18+ não foram afetados, já que têm acesso à implementação nativa de Swift Mutex.

Separadamente, um lote de melhorias para artigos longos foi implementado via [PR #3509](https://github.com/damus-io/damus/pull/3509). Barras de progresso de leitura rastreiam sua posição nos artigos, tempos estimados de leitura aparecem nas previews, e o modo sépia com configurações ajustáveis de altura de linha proporcionam leitura mais confortável. O modo de foco oculta automaticamente o chrome de navegação ao rolar para baixo e o restaura ao tocar, reduzindo a desordem visual para leitura sem distrações. Várias correções resolvem a exibição de imagens em conteúdo markdown e garantem que os artigos abram no topo em vez de no meio.

### Zap.stream (Transmissão ao Vivo)

A integração de chat do YouTube e Kick faz ponte de mensagens de plataformas de streaming externas para o Nostr. Streamers que transmitem simultaneamente para YouTube, Kick e Zap.stream agora podem ver todas as mensagens de chat em uma visualização unificada, com mensagens de cada plataforma aparecendo ao lado de comentários nativos do Nostr. Isso remove um grande ponto de atrito para criadores que desejam usar o Nostr para streaming, mas não podem abandonar audiências em plataformas estabelecidas. A integração exibe de qual plataforma cada mensagem se originou e lida com o fluxo de autenticação para conectar contas externas.

### Chachi (Grupos NIP-29)

O cliente de chat em grupo [NIP-29](/pt/topics/nip-29/) lançou seis PRs mesclados esta semana. Uma atualização de segurança resolve o [CVE-2026-22029](https://github.com/purrgrammer/chachi/pull/89), uma vulnerabilidade XSS no react-router que poderia permitir ataques de redirecionamento aberto; a correção atualiza para react-router-dom 6.30.0. O [PR #92](https://github.com/purrgrammer/chachi/pull/92) adiciona carregamento paginado de mensagens para chats em grupo, para que conversas longas carreguem incrementalmente em vez de todas de uma vez. O [PR #91](https://github.com/purrgrammer/chachi/pull/91) corrige vários bugs do NIP-29 incluindo uma condição de corrida que causava nomes de grupo em branco no carregamento inicial e listas de participantes indefinidas que travavam as visualizações de membros. A cobertura de tradução agora abrange todos os 31 locales suportados com 1060 chaves cada.

### 0xchat (Mensagens)

O cliente de mensagens estilo Telegram melhorou a conformidade com o [NIP-55](/pt/topics/nip-55/) salvando corretamente os nomes de pacote do assinante ao usar aplicativos de assinatura externos, corrigindo problemas onde o aplicativo perdia o rastro de qual assinante usar após reinicializações. O tratamento de respostas do NIP-17 agora inclui corretamente a tag `e` para threading, garantindo que as respostas apareçam no contexto de conversa correto entre clientes. Otimizações de desempenho resolvem lag de rolagem em listas de mensagens, um ponto de dor comum ao carregar históricos de chat longos. O salvamento automático de rascunhos previne perda de mensagem se você navegar para longe no meio da composição, e as opções de armazenamento de arquivos agora incluem endpoints padrão de FileDropServer e BlossomServer.

### Primal (iOS)

O suporte a assinante remoto [NIP-46](/pt/topics/nip-46/) chega ao iOS via [PR #184](https://github.com/PrimalHQ/primal-ios-app/pull/184), completando o lançamento multiplataforma que começou com Android há várias semanas. Os usuários agora podem manter suas chaves privadas em serviços bunker dedicados como nsec.app ou instâncias nsecBunker auto-hospedadas, conectando através de relays Nostr para assinar eventos sem expor chaves ao aplicativo cliente. Essa separação melhora a postura de segurança para usuários que desejam usar os recursos do Primal enquanto mantêm práticas de gerenciamento de chaves mais rigorosas. A implementação inclui escaneamento de código QR para URIs de conexão bunker e lida com o fluxo de requisição/resposta do NIP-46 através de mensagens de relay criptografadas.

---

É isso para esta semana. Construindo algo? Tem notícias para compartilhar? Quer que a gente cubra seu projeto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via DM NIP-17</a> ou nos encontre no Nostr.
