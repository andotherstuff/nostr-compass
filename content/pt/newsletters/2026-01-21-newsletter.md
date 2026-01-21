---
title: 'Nostr Compass #6'
date: 2026-01-21
publishDate: 2026-01-21
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal sobre Nostr.

**Esta semana:** Bitchat substitui C Tor pela implementação Rust Arti para melhor confiabilidade e desempenho. nostrdb-rs ganha consultas fold streaming que habilitam operações de banco de dados com alocação zero. Listr recebe uma grande refatoração com migração para NDK 3 beta e manutenção assistida por IA após um ano de inatividade. Zeus entrega 17 PRs mesclados focados em correções de [NIP-47](/pt/topics/nip-47/) (Nostr Wallet Connect para controle remoto do Lightning) e melhorias no Cashu, enquanto Primal Android adiciona fluxos de backup de carteira e suporte a [NIP-92](/pt/topics/nip-92/) (dimensões de mídia para proporções adequadas). Um novo rascunho de NIP propõe [Trusted Relay Assertions](/pt/topics/trusted-relay-assertions/) para pontuação padronizada de confiança de relays.

## Notícias

### Bitchat Migra para Rust Arti para Suporte Tor

Bitchat migrou do C Tor para [Arti](https://gitlab.torproject.org/tpo/core/arti), a implementação Rust do protocolo Tor. [PR #958](https://github.com/permissionlesstech/bitchat/pull/958) remove a dependência do C Tor e integra Arti, trazendo garantias de segurança de memória e confiabilidade aprimorada. A mudança elimina tentativas de despertar em modo dormente que causavam reinicializações de serviço em primeiro plano, um problema persistente com a implementação em C.

**O que isso significa para os usuários:** Mensagens criptografadas mais estáveis com menos desconexões, especialmente em dispositivos móveis. A implementação em Rust reduz riscos de falhas e drenagem de bateria devido a tentativas constantes de reconexão.

Arti é uma reescrita completa do Tor em Rust, desenvolvida pelo Tor Project para fornecer melhor segurança através de segurança de memória e integração mais fácil em aplicações. Para o Bitchat, as propriedades de segurança de memória reduzem a superfície de ataque ao lidar com mensagens criptografadas e conexões de relay. A migração segue a recente [auditoria de segurança Cure53](/pt/newsletters/2026-01-13-newsletter/#bitchat-completes-cure53-security-audit) da equipe (coberta no Newsletter #5), continuando suas melhorias de segurança.

O PR também introduz cobertura de testes abrangente para ChatViewModel e BLEService, remove código morto e estabiliza a suite de testes. Melhorias de confiabilidade da malha Bluetooth Low Energy acompanham as mudanças do Tor, abordando falhas de transferências grandes. Juntas, essas mudanças melhoram a resiliência do Bitchat para cenários de rede mesh offline onde o Tor fornece conectividade com a internet junto com comunicação BLE local.


### Listr Revitalizado com Manutenção Assistida por IA

JeffG anunciou uma grande refatoração do [Listr](https://github.com/erskingardner/listr), o aplicativo de gerenciamento de listas Nostr disponível em [listr.lol](https://listr.lol), após o projeto ter ficado inativo por mais de um ano. Usando assistência de IA, ele completou uma atualização abrangente incluindo migração para [NDK](https://github.com/nostr-dev-kit/ndk) 3 beta, atualizações para as versões mais recentes de Svelte e Vite, e todas as dependências atualizadas. A refatoração adiciona suporte de primeira classe para seguir pacotes, implementa paginação para listas excedendo 50 itens, e corrige inúmeros bugs que haviam se acumulado durante o período inativo.

**O que isso significa para os usuários:** Listr está de volta online com desempenho aprimorado e novos recursos para gerenciar listas de seguidores, coleções de conteúdo e curadoria de tópicos. A correção de paginação torna listas grandes realmente utilizáveis.

JeffG observou que sem assistência de IA, este trabalho de manutenção provavelmente nunca teria acontecido, impedindo que o projeto fosse abandonado. Listr habilita curadoria de conteúdo no Nostr, permitindo que usuários criem, gerenciem e compartilhem listas de perfis, tópicos e recursos. A atualização mantém o aplicativo compatível com os padrões atuais do Nostr e expectativas dos clientes à medida que o gerenciamento de listas se torna mais central para descoberta de conteúdo no protocolo.


## Atualizações de NIP

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mesclado:**

- **[NIP-29](/pt/topics/nip-29/)** (Grupos baseados em relay) - Esclarecimento de Chave de Relay ([#2190](https://github.com/nostr-protocol/nips/pull/2190) - mesclado) esclarece que a chave do relay é a própria URL do relay, não uma pubkey. A especificação agora afirma explicitamente "A chave do relay é a URL WebSocket do relay (por exemplo, wss://groups.example.com)" para evitar confusão. Isso afeta como os clientes identificam qual relay hospeda um determinado grupo, garantindo que os grupos sejam atribuídos adequadamente aos seus relays de hospedagem.

**PRs Abertos e Discussões:**

- **Trusted Relay Assertions** - Um rascunho de NIP propõe padronizar a pontuação de confiança de relay através de eventos kind 30385 contendo pontuações de confiança (0-100) calculadas a partir de métricas de [NIP-66](/pt/topics/nip-66/) (descoberta e monitoramento de relay), reputação do operador e relatórios de usuários. A especificação divide a confiança em componentes de confiabilidade (tempo de atividade, latência), qualidade (TLS, documentação, verificação do operador) e acessibilidade (jurisdição, barreiras, risco de vigilância). A verificação do operador inclui assinaturas criptográficas via [NIP-11](/pt/topics/nip-11/) (documentos de informações de relay), registros DNS TXT e arquivos .well-known. Usuários declaram provedores de assertivas confiáveis via eventos kind 10385, habilitando clientes a consultar múltiplos provedores para perspectivas diversas. A proposta complementa a descoberta de [NIP-66](/pt/topics/nip-66/) com avaliação, ajudando [NIP-46](/pt/topics/nip-46/) (assinatura remota/Nostr Connect) a avaliar a confiabilidade do relay em URIs de conexão.

- **Criptografia Pós-Quântica** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) (aberto) continua evoluindo desde que o [Newsletter #5](/pt/newsletters/2026-01-13-newsletter/#nip-updates) introduziu a proposta para algoritmos resistentes a quantum. A discussão desta semana focou em detalhes de implementação para cripto-agilidade: como clientes lidam com assinaturas duplas durante a migração, compatibilidade retroativa para clientes mais antigos e implicações de desempenho de assinaturas quânticas resistentes maiores. Contribuidores debateram se mandatar apenas ML-DSA-44 ou suportar múltiplos algoritmos (ML-DSA-44, Falcon-512, Dilithium) para flexibilidade. O consenso inclina-se para uma abordagem faseada: assinaturas quânticas opcionais inicialmente, tornando-se obrigatórias apenas após suporte generalizado do cliente e emergência de ameaça quântica real.


## Mergulho Profundo em NIP: NIP-11 e NIP-66

Esta semana examinamos dois NIPs que trabalham juntos para habilitar descoberta e avaliação de relay: NIP-11 define como relays se descrevem, e NIP-66 padroniza como medimos o comportamento do relay. Juntos, eles formam a fundação para sistemas de avaliação de confiança de relay.

### [NIP-11](/pt/topics/nip-11/): Documento de Informações de Relay

[NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md) define um documento JSON que relays servem via HTTP para descrever suas capacidades, políticas e informações do operador. Quando um cliente se conecta a \`wss://relay.example.com\`, ele pode buscar \`https://relay.example.com\` (substituindo \`wss://\` por \`https://\`) para recuperar o documento de informações do relay.

O documento usa negociação de conteúdo HTTP padrão com o cabeçalho \`Accept: application/nostr+json\`. Isso permite que relays sirvam seu site normal para navegadores enquanto fornecem metadados legíveis por máquina para clientes Nostr. A resposta inclui nome e versão do software do relay, informações de contato do operador (pubkey, email, contato alternativo), NIPs suportados e parâmetros operacionais como requisitos de pagamento ou restrições de conteúdo.

Importante, documentos básicos NIP-11 são JSON não assinado servido via HTTPS, confiando apenas em certificados TLS para autenticidade. Isso significa que qualquer pessoa controlando o servidor web do relay pode modificar o documento, tornando as alegações do operador não verificáveis. A proposta Trusted Relay Assertions aborda essa lacuna introduzindo atestados assinados através do campo \`self\` pubkey de um relay, habilitando prova criptográfica de identidade do operador similar a como relays usam eventos assinados para mecanismos de autenticação.

\`\`\`json
{
  "name": "relay.example.com",
  "description": "Um relay público de propósito geral",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "contact": "admin@example.com",
  "supported_nips": [1, 2, 4, 9, 11, 12, 16, 20, 22],
  "software": "git+https://github.com/relay/relay.git",
  "version": "1.2.3",
  "limitation": {
    "max_message_length": 16384,
    "max_subscriptions": 20,
    "max_filters": 100,
    "max_limit": 5000,
    "max_subid_length": 100,
    "min_prefix": 4,
    "max_event_tags": 2000,
    "max_content_length": 8196,
    "min_pow_difficulty": 0,
    "auth_required": false,
    "payment_required": false
  },
  "payments_url": "https://relay.example.com/payments",
  "fees": {
    "admission": [{"amount": 5000, "unit": "msats"}],
    "subscription": [{"amount": 1000, "unit": "msats", "period": 2592000}],
    "publication": []
  }
}
\`\`\`

O objeto \`limitation\` informa aos clientes quais restrições o relay aplica. \`max_message_length\` limita o tamanho do quadro WebSocket, \`max_subscriptions\` limita assinaturas REQ simultâneas por conexão, \`max_filters\` limita filtros por REQ, e \`max_limit\` restringe quantos eventos um único filtro pode solicitar. Esses parâmetros ajudam clientes a adaptar seu comportamento às capacidades do relay, evitando desconexões por exceder limites.

Informações de pagamento aparecem em \`fees\` e \`payments_url\`. Relays podem cobrar por admissão (acesso único), assinatura (acesso recorrente) ou publicação (taxas por evento). O \`payments_url\` aponta para detalhes sobre métodos de pagamento, tipicamente faturas Lightning ou mints de ecash. Relays pagos usam esses campos para comunicar preços antes que clientes tentem autenticação.

O array \`supported_nips\` permite que clientes descubram capacidades do relay. Se um relay lista [NIP-50](/pt/topics/nip-50/), clientes sabem que podem enviar consultas de busca de texto completo. Se [NIP-42](/pt/topics/nip-42/) aparecer, clientes devem esperar desafios de autenticação. Esta publicidade declarativa de capacidade habilita aprimoramento progressivo: clientes podem usar recursos avançados onde disponíveis enquanto degradam graciosamente em relays com suporte limitado.

Informações do operador constroem responsabilidade. O campo \`pubkey\` identifica o operador do relay no Nostr, habilitando comunicação direta via DMs de [NIP-17](/pt/topics/nip-17/) ou menções públicas. O email de \`contact\` fornece um backup fora do protocolo. Juntos, esses campos ajudam usuários a alcançar operadores para relatórios de abuso, solicitações de acesso ou problemas técnicos.

Documentos [NIP-11](/pt/topics/nip-11/) são auto-relatados: relays descrevem o que alegam suportar, não necessariamente o que realmente fazem. É aqui que NIP-66 se torna importante.

### [NIP-66](/pt/topics/nip-66/): Descoberta de Relay e Monitoramento de Disponibilidade

[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) padroniza a publicação de dados de monitoramento de relay no Nostr. Serviços de monitoramento testam continuamente relays para disponibilidade, latência, conformidade com o protocolo e NIPs suportados. Eles publicam resultados como eventos kind 30166, fornecendo status de relay em tempo real independente do auto-relato do relay.

Monitores verificam disponibilidade do relay conectando e enviando assinaturas de teste. Medições de latência rastreiam tempo de conexão, tempo de resposta de assinatura e atraso de propagação de eventos. Testes de conformidade de protocolo verificam se o comportamento do relay corresponde às especificações, capturando bugs de implementação ou desvios intencionais. Verificação de suporte a NIP vai além das alegações de [NIP-11](/pt/topics/nip-11/) testando realmente se recursos anunciados funcionam corretamente.

\`\`\`json
{
  "id": "a34b5c7d89e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
  "pubkey": "4e2d0bc6f8e7c3a5b9f1d2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4",
  "created_at": 1736784000,
  "kind": 30166,
  "tags": [
    ["d", "wss://relay.example.com"],
    ["rtt", "open", "143", "1736784000"],
    ["rtt", "read", "89", "1736784000"],
    ["rtt", "write", "92", "1736784000"],
    ["nips", "1", "2", "4", "9", "11", "12"],
    ["geo", "US", "United States", "New York"],
    ["other", "network", "clearnet"],
    ["other", "payment_required", "false"],
    ["other", "auth_required", "false"]
  ],
  "content": "{\\"last_check\\": 1736784000, \\"checks\\": 8760}",
  "sig": "8b9c4d5e6a7f8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b"
}
\`\`\`

A tag \`d\` contém a URL do relay, tornando este um evento substituível parametrizado. Cada monitor publica um evento por relay, atualizado conforme as medições mudam. Múltiplos monitores podem rastrear o mesmo relay, fornecendo redundância e validação cruzada. Clientes consultam múltiplas pubkeys de monitores para obter perspectivas diversas sobre a saúde do relay.

Tags de tempo de ida e volta (rtt) medem latência para diferentes operações. \`rtt open\` rastreia estabelecimento de conexão WebSocket, \`rtt read\` mede tempo de resposta de assinatura, e \`rtt write\` testa velocidade de publicação de eventos. Todos os valores estão em milissegundos. Clientes usam essas métricas para preferir relays de baixa latência para operações sensíveis ao tempo ou despriorizar relays lentos.

A tag \`nips\` lista suporte a NIP realmente verificado, não apenas suporte alegado. Monitores testam cada NIP exercitando sua funcionalidade. Se um relay alega busca [NIP-50](/pt/topics/nip-50/) em seu documento [NIP-11](/pt/topics/nip-11/) mas consultas de busca falham, monitores omitirão NIP-50 da lista verificada. Isso fornece verdade fundamental sobre capacidades do relay.

Informações geográficas ajudam clientes a selecionar relays próximos para melhor latência e resistência à censura. A tag \`geo\` contém código do país, nome do país e região. A tag \`network\` distingue relays clearnet de serviços ocultos Tor ou endpoints I2P. Juntas, essas tags habilitam diversidade geográfica: clientes podem se conectar a relays em múltiplas jurisdições para resistir à censura regional.

Dados de monitor alimentam seletores de relay em clientes, sites exploradores e a proposta Trusted Relay Assertions. Combinando documentos auto-relatados [NIP-11](/pt/topics/nip-11/) com dados medidos de [NIP-66](/pt/topics/nip-66/) e assertivas de confiança computadas, o ecossistema caminha para seleção informada de relay em vez de confiar em padrões codificados ou recomendações de boca a boca.

## Lançamentos

### 0xchat v1.5.3 - Recursos de Mensagens Aprimorados

[0xchat v1.5.3](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.3-release) traz melhorias significativas ao cliente de mensagens Nostr estilo Telegram. O lançamento aborda problemas de conformidade com [NIP-55](/pt/topics/nip-55/) (aplicativo assinador Android) que estavam impedindo assinatura adequada de eventos através de assinadores externos como Amber. Conformidade completa significa que 0xchat agora delega corretamente operações de assinatura, melhorando a segurança mantendo chaves privadas isoladas.

A atualização integra tanto FileDropServer quanto BlossomServer como opções de armazenamento de mídia padrão, dando aos usuários redundância para uploads de arquivo. [Blossom](https://github.com/hzrd149/blossom) fornece armazenamento endereçado por conteúdo onde arquivos são referenciados por seus hashes SHA-256, garantindo integridade e habilitando deduplicação através da rede. Salvamento automático de rascunho para Moments previne perda de dados ao compor conteúdo longo, abordando reclamações de usuários sobre posts perdidos durante trocas de aplicativo ou interrupções de conectividade.

Integração de carteira Cashu recebe polimento com filtragem automática de prova que remove tokens gastos da visualização da carteira. Isso resolve a UX confusa onde usuários viam provas inválidas ao lado de ecash válido, tornando cálculos de saldo não confiáveis. A filtragem acontece no lado do cliente, mantendo privacidade enquanto melhora a experiência de pagamento para transações peer-to-peer dentro de chats.

### Amber v4.1.0 Pré-lançamentos - Reformulação de UI

[Amber v4.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre1) até [v4.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre3) introduzem uma interface redesenhada para o popular assinador de eventos Android. A tela de login agora exibe claramente qual aplicativo está solicitando permissões de assinatura, abordando confusão do usuário sobre fluxos de autorização. A nova tela de eventos fornece inspeção detalhada de quais dados aplicativos querem assinar, permitindo aos usuários tomar decisões de segurança informadas antes de aprovar operações.

Gerenciamento de permissões recebe atenção significativa com uma interface reformulada mostrando exatamente quais capacidades cada aplicativo conectado recebeu. Usuários podem revogar permissões específicas sem desconectar completamente, habilitando controle de granularidade fina sobre delegação de assinatura. Os contadores de relay refatorados usando a biblioteca quartz atualizada fornecem estatísticas em tempo real sobre throughput de eventos e desempenho do relay. Conexões bunker de [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) (Nostr Connect) agora exibem mensagens de erro detalhadas quando conexões falham, substituindo erros de timeout crípticos por diagnósticos acionáveis.

## Mudanças notáveis em código e documentação

*Estes são pull requests mesclados e desenvolvimentos em estágio inicial que vale a pena acompanhar. Alguns são recursos experimentais que podem evoluir antes do lançamento.*

### Zeus (Carteira Lightning com Nostr Wallet Connect)

Zeus mesclou 17 pull requests esta semana, fortalecendo sua posição como implementação líder de [NIP-47](/pt/topics/nip-47/) Nostr Wallet Connect. As correções mais significativas abordam problemas de consistência de dados e conformidade de protocolo que estavam causando problemas de interoperabilidade com clientes Nostr.

**Correção de Histórico de Transações** - [PR #3542](https://github.com/ZeusLN/zeus/pull/3542) resolve um bug crítico onde listas de transações NWC exibiam entradas incorretas ou duplicadas. O problema ocorria quando Zeus armazenava em cache dados de transação sem lidar adequadamente com atualizações de eventos, fazendo usuários verem transações fantasma ou pagamentos faltando. A correção implementa deduplicação adequada de eventos e invalidação de cache, garantindo que o histórico de transações reflita com precisão o estado do nó Lightning.

**Conformidade de Protocolo** - [PR #3548](https://github.com/ZeusLN/zeus/pull/3548) aborda respostas incompletas de \`getInfo\` que quebravam compatibilidade com clientes esperando conformidade completa com NIP-47. Alguns clientes Nostr travavam ao receber respostas parciais faltando campos como \`block_height\` ou \`network\`. O PR garante que todos os campos obrigatórios retornem com padrões sensatos mesmo quando a implementação Lightning subjacente não os fornece, melhorando a compatibilidade do Zeus através do ecossistema.

**Resiliência de Conexão** - [PR #3543](https://github.com/ZeusLN/zeus/pull/3543) implementa notificações de timeout para conexões Nostr paralisadas. Anteriormente, usuários esperavam indefinidamente quando conexões de relay caíam silenciosamente. Agora Zeus exibe mensagens claras de timeout após 30 segundos de inatividade, permitindo aos usuários tentar novamente ou trocar relays. [PR #3541](https://github.com/ZeusLN/zeus/pull/3541) adiciona validação de backend para prevenir ativação de NWC em implementações Lightning incompatíveis, capturando erros de configuração antes que causem travamentos em tempo de execução.

**Condição de Corrida Cashu** - [PR #3531](https://github.com/ZeusLN/zeus/pull/3531) corrige um bug de concorrência no gerenciamento de tokens Cashu onde operações de mint simultâneas poderiam corromper o banco de dados de tokens. A condição de corrida ocorria quando múltiplas threads atualizavam contagens de tokens sem bloqueio adequado, ocasionalmente resultando em saldos incorretos. A correção adiciona proteção mutex ao redor de seções críticas, garantindo atualizações atômicas ao estado de token.

### Primal Android (Cliente)

Primal Android entregou 12 PRs mesclados com melhorias significativas à segurança da carteira e manuseio de mídia. A implementação de backup de carteira aborda um dos recursos mais solicitados, enquanto suporte a NIP-92 melhora a experiência visual através do aplicativo.

**Sistema de Backup de Carteira** - Uma série de quatro PRs ([#844](https://github.com/PrimalHQ/primal-android-app/pull/844), [#845](https://github.com/PrimalHQ/primal-android-app/pull/845), [#846](https://github.com/PrimalHQ/primal-android-app/pull/846), [#848](https://github.com/PrimalHQ/primal-android-app/pull/848)) implementa funcionalidade abrangente de backup de frase semente. Usuários agora podem exportar seu mnemônico de 12 palavras através de um fluxo seguro que previne capturas de tela, exibe status de backup no painel da carteira e guia usuários existentes através da migração. A implementação segue padrões BIP-39 e inclui validação para prevenir que usuários percam fundos devido à gravação incorreta de frases.

**Dimensões de Mídia (NIP-92)** - [PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) implementa suporte a [NIP-92](/pt/topics/nip-92/) para proporções adequadas de imagem e vídeo. Sem metadados de dimensão, clientes devem baixar imagens para determinar seu tamanho, causando saltos de layout conforme o conteúdo carrega. NIP-92 adiciona tags \`dim\` (como \`["dim", "1920x1080"]\`) a eventos de metadados de arquivo, permitindo que Primal reserve espaço correto antes de baixar mídia. Isso elimina refluxos bruscos em galerias de imagem e melhora desempenho percebido.

**Confiabilidade de Assinador Remoto** - [PR #841](https://github.com/PrimalHQ/primal-android-app/pull/841) corrige problemas de conexão [NIP-46](/pt/topics/nip-46/) onde prefixos \`wss://\` faltando causavam falhas silenciosas. O PR valida URIs de relay durante configuração de conexão bunker, adicionando o prefixo de protocolo automaticamente quando usuários colam domínios nus. [PR #843](https://github.com/PrimalHQ/primal-android-app/pull/843) aborda um bug de threading onde condições de rede ruins causavam respostas a postar como notas raiz, quebrando fluxo de conversa. A correção garante que IDs de evento pai persistam através de interrupções de rede.

### Protocolo Marmot: White Noise (Biblioteca de Chat de Grupo Criptografado)

White Noise, a biblioteca Rust alimentando chats de grupo criptografados do [Marmot](/pt/topics/marmot/) Protocol, mesclou seis PRs melhorando experiência do usuário e segurança. As mudanças aproximam Marmot da paridade de recursos com aplicativos de mensagens mainstream enquanto mantém sua arquitetura com privacidade em primeiro lugar.

**Confirmações de Leitura** - [PR #433](https://github.com/marmot-protocol/whitenoise-rs/pull/433) e [#436](https://github.com/marmot-protocol/whitenoise-rs/pull/436) implementam rastreamento de leitura de mensagens para conversas de grupo. O sistema armazena posições de leitura por usuário por grupo dentro de um único dispositivo, habilitando emblemas de contagem não lida. A implementação usa timestamps monotônicos para rastrear a última posição de mensagem lida para cada conversa. Este recurso fundamental habilita indicadores de UI mostrando contagens de mensagens não lidas por conversa.

**Fixação de Conversa** - [PR #442](https://github.com/marmot-protocol/whitenoise-rs/pull/442) adiciona fixação de conversa persistente através de um campo \`pin_order\` na tabela de junção \`accounts_groups\` que liga contas a grupos. Conversas fixadas mantêm sua posição no topo de listas de chat independentemente de atividade de mensagem, correspondendo expectativas do usuário do Signal e WhatsApp. A implementação usa ordenação inteira para permitir fixações ilimitadas com ordenação determinística.

**Resolução Determinística de Commit (MIP-03)** - [PR #152](https://github.com/marmot-protocol/mdk/pull/152) (aberto) implementa Marmot Improvement Proposal 03, resolvendo o problema crítico de condições de corrida de commit em chats de grupo distribuídos. Quando múltiplos membros enviam mudanças de estado de grupo (adicionar/remover membros, mudar permissões) simultaneamente, clientes poderiam divergir na ordenação de commits, fragmentando o grupo em estados incompatíveis. MIP-03 introduz snapshots de época e uma seleção determinística de vencedor: o commit com o timestamp \`created_at\` mais cedo vence, com ID de evento lexicográfico como desempate. Isso permite que todos os clientes convirjam no mesmo estado através de rollback e replay, mantendo coerência de grupo mesmo durante partições de rede.

**Endurecimento de Segurança** - [PR #443](https://github.com/marmot-protocol/whitenoise-rs/pull/443) previne cópia desnecessária de segredos criptográficos usando referências em \`resolve_group_image_path\`. Isso reduz a janela para ataques de memória onde segredos poderiam ser recuperados de alocações de heap liberadas. [PR #438](https://github.com/marmot-protocol/whitenoise-rs/pull/438) habilita criptografia de banco de dados SQLCipher através de parâmetros de chaveiro, protegendo histórico de mensagens em repouso. A integração de chaveiro permite armazenamento seguro de chaves em chaveiros de plataforma em vez de arquivos de configuração.

### nostrdb-rs (Biblioteca de Banco de Dados) - PR Aberto

**Implementação de Consultas Streaming** - [PR #58](https://github.com/damus-io/nostrdb-rs/pull/58) (aberto) propõe consultas fold streaming para habilitar operações de banco de dados com alocação zero. A implementação adiciona métodos \`fold\`, \`try_fold\`, \`count\`, \`any\`, \`all\` e \`find_map\` que processariam resultados de banco de dados um de cada vez sem materializar conjuntos de resultados inteiros em vetores. Esta abordagem reduziria consumo de memória e habilitaria terminação antecipada para padrões de consulta comuns.

A implementação técnica expõe callbacks de resultado de consulta de baixo nível (\`ndb_query_visit\`) como visitantes Rust com estado que mapeiam variantes \`ControlFlow\` para ações de visitante C. Uma vez mesclado, código de aplicação lerá como lógica de iterador enquanto roda perto da camada de banco de dados. Por exemplo, contar notas correspondentes transmitiria através de resultados em vez de coletá-los, e \`find_map\` retornaria o primeiro resultado útil sem processar linhas restantes.

nostrdb alimenta Damus e Notedeck, ambos clientes iOS/macOS e desktop respectivamente. As consultas streaming habilitariam padrões eficientes como paginação, filtragem condicional e verificações de existência. O PR muda 3 arquivos com +756 adições e -32 deleções, uma refatoração substancial da camada de consulta. Usuários de aplicativos baseados em nostrdb-rs veriam uso de memória reduzido ao navegar timelines grandes ou buscar através de bancos de dados extensos de eventos.

### nak (Ferramenta CLI)

nak, ferramenta Nostr de linha de comando de fiatjaf, mesclou seis PRs focados em melhorias de sistema de build e nova funcionalidade. [PR #91](https://github.com/fiatjaf/nak/pull/91) implementa um recurso de espelho Blossom, permitindo que nak sirva como um espelho para servidores de mídia Blossom. [Blossom](/pt/topics/blossom/) é um protocolo de armazenamento de mídia endereçado por conteúdo que funciona junto com eventos Nostr.

Os PRs restantes abordam compatibilidade de sistema de build através de plataformas Windows, macOS e Linux, habilitando suporte a sistema de arquivos FUSE para montar eventos Nostr como diretórios locais.

### Damus (Cliente iOS) - PRs Abertos

Damus tem 11 PRs abertos explorando melhorias arquiteturais significativas. Embora estes ainda não tenham sido mesclados, eles sinalizam direções importantes para desenvolvimento de cliente Nostr iOS, particularmente em torno de privacidade, eficiência de sincronização e otimização de dados móveis.

**Integração Tor** - [PR #3535](https://github.com/damus-io/damus/pull/3535) embute o cliente Arti Tor diretamente no Damus, habilitando conexões de relay anônimas sem dependências externas. Diferente de abordagens Orbot ou Tor Browser, embutir Arti fornece integração perfeita com sandboxing iOS e limites de execução em segundo plano. A implementação Rust traz segurança de memória para anonimização de rede, reduzindo superfície de ataque comparada ao C Tor. Usuários poderiam alternar modo Tor por relay ou globalmente, com o cliente lidando com gerenciamento de circuito de forma transparente.

**Protocolo de Sincronização Negentropy** - [PR #3536](https://github.com/damus-io/damus/pull/3536) implementa Negentropy, um protocolo de reconciliação de conjunto que melhora radicalmente a eficiência de sincronização. Em vez de baixar todos os eventos desde a última conexão, Negentropy troca impressões digitais compactas (árvores Merkle) para identificar exatamente quais eventos diferem entre cliente e relay. Para usuários seguindo centenas de pubkeys, isso reduz largura de banda de sincronização de megabytes para kilobytes. A implementação integra com RelayPool e SubscriptionManager, habilitando sincronização eficiente automática através de todos os relays conectados.

**Modo de Dados Baixos** - [PR #3549](https://github.com/damus-io/damus/pull/3549) adiciona recursos de conservação de dados celulares respondendo a feedback de usuários sobre consumo de largura de banda. O modo desabilita carregamento automático de imagem, pré-busca de vídeo e reduz limites de assinatura. Usuários com conexões medidas podem navegar conteúdo de texto sem medo de exceder limites de dados. A implementação respeita configurações de modo de dados baixos do iOS e fornece controles granulares para diferentes tipos de mídia.

**Otimizações de Banco de Dados** - [PR #3548](https://github.com/damus-io/damus/pull/3548) refaz armazenamento de snapshot nostrdb para consultas mais rápidas e uso de disco reduzido. A otimização muda como snapshots de banco de dados persistem em disco, melhorando tanto desempenho de leitura quanto amplificação de escrita. Isso aborda reclamações de drenagem de bateria de usuários com grandes bancos de dados de eventos.

---

É isso para esta semana. Construindo algo? Tem notícias para compartilhar? Quer que cubramos seu projeto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via DM NIP-17</a> ou nos encontre no Nostr.
