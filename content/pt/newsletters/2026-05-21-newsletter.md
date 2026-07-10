---
title: 'Nostr Compass #23'
date: 2026-05-21
publishDate: 2026-05-21
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-21-newsletter.md
translationDate: 2026-07-01
---

Primal 3.5 lança uma shell Android reconstruída, Amethyst adiciona zaps Bitcoin onchain, White Noise ganha renderização de markdown e deep links, Keycast passa por uma auditoria de segurança, e AgentNoise permite controlar agentes de código IA locais através de chat criptografado pelo Marmot. Hostr lança uma plataforma de acomodações para aluguel P2P no Nostr com quatro NIPs em rascunho cobrindo listagens, reservas e escrow baseado em EVM. Angor migra mensageria criptografada de NIP-04 para NIP-44, Dart NDK adiciona NIP-77 e um signer web, Alby js-sdk v8 lança reconexão multi-relay NWC nativa, e KeyChat corrige uma lacuna de forward secrecy na exclusão de prekey único do Signal. No lado do protocolo, o bond anti-abuso do Mostro chega à Fase 2, Wisp lança respostas privadas e reações gift-wrapped, e uma onda de implementação NIP-05 do Namecoin toca meia dúzia de clientes em uma única semana.

## Matérias principais

### Primal 3.5 para Android

Primal, o cliente social apoiado por sua própria infraestrutura de relay de cache, lançou [3.5.9](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.9) esta semana com uma shell de aplicação reconstruída. O redesign substitui a estrutura de navegação anterior por um layout atualizado e uma nova tela Explore, dando à principal superfície de descoberta seu próprio home dedicado. A release adiciona reprodução de áudio para link previews, para que arquivos de áudio embutidos em notas sejam reproduzidos inline sem sair do feed. Badges de verificação NIP-05 agora aparecem inline nos perfis, apresentando confirmação de identidade em um relance. A filtragem de notificações recebeu uma reformulação, permitindo aos usuários restringir quais tipos de eventos chegam à sua lista de notificações. O editor ganhou melhor tratamento de event-links, e a camada de banco de dados subjacente recebeu correções de estabilidade.

### White Noise: markdown, deep links e metadados de áudio

White Noise, o app de mensageria de grupo criptografado pelo Marmot construído sobre Nostr e MLS ([RFC 9420](https://www.rfc-editor.org/rfc/rfc9420)), teve uma de suas semanas mais movimentadas nos repositórios de frontend e backend.

No frontend, [PR #665](https://github.com/marmot-protocol/whitenoise/pull/665) adiciona renderização completa de markdown para mensagens de chat, para que negrito, itálico, blocos de código e links agora sejam renderizados nativamente na visão de mensagem. [PR #675](https://github.com/marmot-protocol/whitenoise/pull/675) ativa o fluxo de sair de grupo que anteriormente era bloqueado para admins não-últimos, e [PR #661](https://github.com/marmot-protocol/whitenoise/pull/661) adiciona suporte nativo a deep link para URIs `whitenoise://` e `whitenoise-staging://` cobrindo usuários, chats e configurações, sem exigir nenhuma infraestrutura de redirecionamento HTTP.

No backend em whitenoise-rs, [PR #835](https://github.com/marmot-protocol/whitenoise-rs/pull/835) faz a rotação de key package funcionar corretamente reutilizando o slot `d_tag` para publicações kind:30443, ativando a semântica de eventos substituíveis NIP-33 para que rotações sucessivas de key package substituam o evento anterior nos relays, mantendo apenas o key package atual. [PR #833](https://github.com/marmot-protocol/whitenoise-rs/pull/833) estende `FileMetadata` com campos opcionais `duration_ms` e `waveform` para anexos de áudio, coordenado com o [PR #300](https://github.com/marmot-protocol/mdk/pull/300) do MDK que adiciona os mesmos campos às tags de mídia MIP-04. Uma nova crate `whitenoise-markdown` ([PR #836](https://github.com/marmot-protocol/whitenoise-rs/pull/836)) substitui o parser de tokens nostr-sdk anterior por uma biblioteca dedicada de renderização de markdown.

A própria especificação do protocolo Marmot recebeu uma correção de segurança no [PR #68](https://github.com/marmot-protocol/marmot/pull/68), que fecha um problema de segurança especificando explicitamente HKDF-SHA256 para derivações de chave de imagem no MIP-01, removendo ambiguidade que poderia levar à divergência de implementação. No MDK, [PR #307](https://github.com/marmot-protocol/mdk/pull/307) sanitiza motivos de falha em welcome e limita o comprimento armazenado, fechando uma constatação de segurança separada.

### Amethyst v1.10.0: Zaps Bitcoin Onchain

Amethyst lançou quatro releases esta semana, com [v1.10.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.10.0) como o destaque. A release adiciona suporte para zaps Bitcoin onchain NIP-BC, permitindo aos usuários enviar, receber e exibir zaps liquidados diretamente onchain via transações Bitcoin. Releases anteriores na sequência corrigiram a detecção de blob Blossom para rejeitar nomes de arquivo não conformes ([v1.09.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.09.2)), aplicaram patches nas regras do ProGuard para builds desktop, e mesclaram o pull request [#2977](https://github.com/vitorpamplona/amethyst/pull/2977) para mostrar zappers de Bitcoin onchain como uma linha ₿ dedicada na galeria expandida de reações. Uma tela de histórico de transações on-chain em progresso com paginação chegou no [PR #2974](https://github.com/vitorpamplona/amethyst/pull/2974).

### AgentNoise: controle agentes de código sobre White Noise

[AgentNoise](https://github.com/nvk/agentnoise) por nvk é um helper de desktop nativo em Rust que permite usar um telefone rodando White Noise como superfície de controle para sessões locais de agentes de código Codex e Claude. A ferramenta escuta um ou mais chats White Noise, autentica remetentes através de um fluxo de PIN de primeiro pareamento, e lança agentes de código locais através do launcher configurado. Enviar `/claude <prompt>` do seu telefone abre uma nova sessão de trabalho White Noise nomeada segundo o hostname da máquina e um curto resumo do prompt, então transmite atualizações de progresso e saída final de volta para esse chat. É intencionalmente Rust-first e mantém Node fora do caminho da ponte confiável. O projeto chegou à [v0.1.24](https://github.com/nvk/agentnoise/releases/tag/v0.1.24) esta semana, adicionando respostas mais curtas legíveis para o telefone, referências de job por prefixo curto único, e um watcher de sessão local opcional. AgentNoise dirige os CLIs `wn` e `wnd` de `marmot-protocol/whitenoise-rs` como subprocessos, então compartilha seu transporte Nostr com o próprio cliente White Noise.

### Auditoria de segurança do Keycast concluída

[Keycast](https://github.com/marmot-protocol/keycast), o servidor de assinatura remota NIP-46 orientado a equipes que armazena chaves privadas Nostr criptografadas em repouso no SQLite, completou uma auditoria de segurança em maio de 2026. A passagem de hardening abordou questões de autenticação, permissão, integridade de dados e dependências, e os resultados estão documentados em [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md). As mudanças incluem: HTTP auth NIP-98 agora requer exatamente uma tag `u` e uma tag `method`, rejeita timestamps obsoletos e valida hashes `payload`; a allowlist `ALLOWED_PUBKEYS` é parseada exatamente e aplicada no servidor; políticas vazias agora fazem default-deny em requisições de sign/encrypt/decrypt; a aplicação de foreign-key é ativada em conexões SQLite; e rotas de app aninhadas como `/teams/:id` são protegidas no servidor. Uma migração SQL normaliza o JSON antigo de permissão allowed-kinds no startup. O projeto ainda está em estágio inicial e a auditoria observa itens residuais antes de confiá-lo com chaves reais de equipe.

### Scramble: cliente Marmot para desktop e Android

[Scramble](https://github.com/DavidGershony/Scramble) (anteriormente OpenChat) é um cliente .NET/Avalonia para desktop e Android para o [Protocolo Marmot](/pt/topics/marmot/), implementando MIPs 00-04: publicação de KeyPackage (kind:30443), metadados de grupo com a extensão MLS NostrGroupData, eventos welcome gift-wrapped NIP-59 (kind:444), mensagens criptografadas ChaCha20-Poly1305 (kind:445) e anexos de mídia criptografados Blossom. É totalmente interoperável com White Noise e qualquer outro cliente compatível com Marmot.

O projeto lançou 13 releases esta semana, com suporte multi-dispositivo como recurso principal. Cada dispositivo gera um slot único de KeyPackage (uma tag `d` no kind:30443). No startup, Scramble busca os próprios KeyPackages do usuário nos relays, detecta IDs de slot de dispositivos pares, e os adiciona automaticamente a grupos MLS existentes usando o fluxo de commit em stage. O auto-add é restrito a grupos onde o usuário atual é admin; grupos não-admin são pulados com orientação para pedir ao admin do grupo. Um banner de divulgação de forward-secrecy informa a dispositivos recém-vinculados que mensagens antigas não estão disponíveis. Uma passagem de reconciliação de ID de slot (`TryReconcileSlotId`) lida com dispositivos migrados de versões pré-multi-dispositivo comparando bytes de KeyPackage do relay com material de chave local para adotar a tag `d` correta. A reconexão de signer externo para usuários Amber e NIP-46 também foi corrigida: o guard `IsConnected` que bloqueava a auto-reconexão embutida do `ExternalSignerService` foi removido em todos os nove pontos de chamada em `NostrService`.

### Hostr: acomodação para aluguel P2P no Nostr

[Hostr](https://hostr.network) ([fonte](https://github.com/sudonym-btc/hostr)) é uma plataforma peer-to-peer de acomodações para aluguel construída inteiramente no Nostr. Cobre todo o fluxo estilo Airbnb (buscar e listar propriedades, negociar reservas e liquidar pagamentos) usando quatro NIPs em rascunho que o projeto está desenvolvendo em paralelo com a aplicação.

O NIP de acomodação estende classificados [NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md) (kind:30402 ativo, kind:30403 rascunho) com tags específicas de acomodação para tipo (`room`, `house`, `apartment`, `villa`, `hotel`, `hostel`, `resort`), horários de check-in/check-out, estadia mínima, e índices de células geoespaciais H3 para busca baseada em localização em precisão configurável. O NIP de reserva define um protocolo completo de negociação e ciclo de vida: eventos de reserva substituíveis kind:32122 carregam um trade ID `d`, uma tag âncora `a` de listagem, e tags `p` de participantes com papéis (`buyer`, `seller`, `escrow`); rumors de mensagem estruturada kind:1327 entregam contraofertas privadas de estágio de negociação via gift wraps NIP-59 para que a negociação fique fora de relays públicos; eventos de transição append-only kind:1326 criam uma trilha de auditoria pública uma vez que uma reserva é confirmada. A privacidade do comprador é preservada através de chaves Nostr temporárias por trade vinculadas à identidade real do comprador via tags `participant_proof` criptografadas. O NIP de escrow define anúncios de serviço de escrow kind:30303 e declarações de confiança de usuário kind:17388; a implementação de referência usa contratos inteligentes EVM em Rootstock, com `contractBytecodeHash` permitindo aos clientes verificar se o contrato implantado corresponde a uma implementação auditada conhecida. O NIP de listagem de marketplace define tags genéricas compartilhadas entre todos os perfis de marketplace NIP-99, incluindo `instantBook`, `negotiable`, `quantity`, `securityDeposit`, `cancellationPolicy` e `maxDisputePeriod`. Esta semana o projeto preparou sua submissão à app store e mesclou suporte a identidade de cliente MCP para automação voltada a agentes.

Duas novas entradas apareceram na plataforma Shakespeare MiniApps esta semana: [InkPress](https://inkpress.shakespeare.wtf), um gerador de revista por IA que publica conteúdo estruturado no estilo revista como eventos Nostr, e [PressStr](https://pressstr.shakespeare.wtf), uma plataforma de escrita e publicação para a stack Soapbox.

## Lançando esta semana

### ngit v2.4.4

**ngit** lançou [v2.4.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.4), adicionando `ngit sync --trust-server` (`-t`) para casos em que um servidor git está fast-forward à frente do estado Nostr. Quando essa situação é detectada, o sync reporta as refs afetadas e requer a flag para assinar e publicar um evento de estado atualizado; uma configuração git `nostr.trust-server-domains` fornece uma allowlist separada por ponto e vírgula para servidores que devem ser confiados automaticamente sem a flag.

### Amber v6.1.0-pre3 adiciona assinatura PSBT

**Amber** lançou [v6.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre3) com layout melhorado para novas conexões de app, correções de crash, e uma opção select/deselect all na tela de permissões. [PR #438](https://github.com/greenart7c3/Amber/pull/438) adiciona suporte a assinatura PSBT através dos caminhos baseados em Intent e em relay NIP-46, permitindo ao Amber assinar Partially Signed Bitcoin Transactions sem expor a nsec ao app requisitante.

### Wisp v1.1.0 lança respostas privadas e remove suporte a Amber

**Wisp** lançou [v1.1.0](https://github.com/barrydeen/wisp/releases/tag/v1.1.0) com respostas privadas via gift wrap NIP-17 ([PR #540](https://github.com/barrydeen/wisp/pull/540)), reações gift-wrapped e zaps DIP-03 em respostas privadas ([PR #543](https://github.com/barrydeen/wisp/pull/543)), auto-tradução para notas ([PR #523](https://github.com/barrydeen/wisp/pull/523)), e uma entrada em fiat estilo register no diálogo de zap. [PR #541](https://github.com/barrydeen/wisp/pull/541) migra zaps privados de um esquema plaintext de DM-relay caseiro para DIP-03 com roteamento adequado de DM-relay. O mesmo ciclo de release removeu o suporte a signer remoto NIP-55 ([PR #531](https://github.com/barrydeen/wisp/pull/531)), abandonando Amber e outras integrações de signer externo, e removeu o relay local empacotado ([PR #533](https://github.com/barrydeen/wisp/pull/533)). Wisp é um cliente social Nostr para Android.

### Calendar by Formstr v1.5.4 corrige gift wrap para novos participantes

**Calendar by Formstr** lançou [v1.5.4](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.4) (a mais recente em uma sequência v1.5.2 → v1.5.4). [PR #160](https://github.com/formstr-hq/nostr-calendar/pull/160) corrige um bug onde editar um evento de calendário privado com novos participantes publicava o evento atualizado com as novas pubkeys em tags `p` mas nunca criava ou entregava convites gift wrap a esses participantes, quebrando o fluxo de convite para adições de última hora. [PR #156](https://github.com/formstr-hq/nostr-calendar/pull/156) adiciona tratamento de erro em torno da descriptografia de eventos privados para que clientes não lancem mais em eventos indecodificáveis, e [PR #138](https://github.com/formstr-hq/nostr-calendar/pull/138) corrige horários de eventos recorrentes que estavam desviando através de fusos horários.

### Applesauce v6.1.0 adiciona git casts NIP-34 e relays de lookup NIP-51

**Applesauce** lançou [v6.1.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.1.0) em seus pacotes com suporte significativo a NIP-34 (git-over-Nostr): applesauce-common adiciona novos casts `GitRepository`, `GitGraspList` e `FavoriteGitRepos` além de factories correspondentes, e expõe propriedades reativas `User.favoriteGitRepos$`, `User.gitAuthors$` e `User.graspServers$` para que aplicações possam listar repos git seguidos por um usuário, mantenedores de repo, e servidores GRASP configurados diretamente do mesmo objeto User. A mesma release adiciona suporte a listas de relay de lookup NIP-51 kind 10086, uma adição recente à família relay-list usada para descobrir onde encontrar dados específicos. applesauce-core ganha `replaceableAddress` em `EventCast` para lookup de endereço substituível NIP-01, além de `pointer`, `kind` e um helper `getReplaceableAddressForEvent`, e adiciona um método `timeline$()` no cast base `User`. [PR #73](https://github.com/hzrd149/applesauce/pull/73) corrige métodos manuais de pool que descartavam silenciosamente relays offline.

### Sprout v0.0.16 lança binário Sprig e protocolo huddle v2

**Sprout** pelo Block, um workspace de equipe auto-hospedado baseado em relay Nostr onde humanos e agentes IA compartilham as mesmas salas e log de eventos, lançou [v0.0.16](https://github.com/block/sprout/releases/tag/v0.0.16) do app desktop junto com builds contínuos do novo binário all-in-one Sprig ([PR #605](https://github.com/block/sprout/pull/605)), que empacota o harness ACP, agente e MCP de desenvolvedor em um único binário estilo busybox para implantação fácil. A flag `--no-memory` adicionada no [PR #611](https://github.com/block/sprout/pull/611) permite a operadores desativar a injeção de memória central NIP-AE para o harness ACP. No lado de tempo real, [PR #609](https://github.com/block/sprout/pull/609) estende o protocolo de voz huddle a um header de frame v2 suportando até 10 pares simultâneos.

### Nostrord v1.0.3 adiciona keychain do OS e multi-conta

**Nostrord** lançou [v1.0.3](https://github.com/nostrord/nostrord/releases/tag/v1.0.3) com armazenamento local de chave fortalecido usando keychain do OS e fallback de passphrase, suporte multi-conta, e um QR code de bunker tocável que abre o app signer no Android.

### Angor migra para NIP-44 e lança fortalecimento de segurança

**Angor**, o app de crowdfunding Bitcoin construído em Nostr e Taproot, lançou três releases instáveis esta semana ([v0.2.24](https://github.com/block-core/angor/releases/tag/v0.2.24), [v0.2.25](https://github.com/block-core/angor/releases/tag/v0.2.25) e [v0.2.26](https://github.com/block-core/angor/releases/tag/v0.2.26)) com um conjunto de mudanças de fortalecimento de segurança e integração Nostr. [PR #860](https://github.com/block-core/angor/pull/860) migra a mensageria criptografada Nostr de NIP-04 para NIP-44, substituindo o esquema baseado em XOR descontinuado por criptografia ChaCha20-Poly1305. [PR #861](https://github.com/block-core/angor/pull/861) permite uploads de mídia Blossom sem uma carteira selecionada usando uma chave de auth Nostr efêmera, desbloqueando uploads para usuários que ainda não conectaram uma carteira. A série de segurança abordou várias categorias fortalecidas: [PR #854](https://github.com/block-core/angor/pull/854) adiciona segurança de tipo para AngorKey e proteção de memória de mnemonic, [PR #856](https://github.com/block-core/angor/pull/856) impõe validação em nível de protocolo para timelocks, taxas de fee, limites de dust e regras de penalidade, e [PR #851](https://github.com/block-core/angor/pull/851) aplica fortalecimento não-disruptivo em oito categorias de severidade média e baixa. [PR #859](https://github.com/block-core/angor/pull/859) corrige compatibilidade com GrapheneOS habilitando compilação AOT e removendo geração de código em runtime, e [PR #855](https://github.com/block-core/angor/pull/855) evita perda de carteira em swipe-kill Android persistindo o estado da carteira antes do OS terminar o processo.

### Alby js-sdk v8.0 lança reconexão multi-relay NWC

**Alby js-sdk** lançou a linha v8.0 ([v8.0.1](https://github.com/getAlby/js-sdk/releases/tag/v8.0.1) até [v8.0.3](https://github.com/getAlby/js-sdk/releases/tag/v8.0.3)) com suporte a subscription NWC multi-relay. [PR #516](https://github.com/getAlby/js-sdk/pull/516) atualiza a dependência nostr-tools e habilita auto-reconexão nativa através de múltiplos relays, substituindo a abordagem anterior de polling por lógica de reconexão nativa de relay. [PR #542](https://github.com/getAlby/js-sdk/pull/542) substitui todas as chamadas `console.debug` por uma interface de logger injetável para que desenvolvedores de aplicações possam rotear diagnósticos SDK através de sua própria infraestrutura de logging. A release remove o polyfill WebSocket, exigindo Node.js 22 ou superior para consumidores do lado do servidor. v8.0.2 adicionou uma correção para um bug de import crypto de utils que quebrava certos bundlers.

### KeyChat v1.41.1 corrige forward secrecy

**KeyChat**, um app de mensageria que combina o protocolo Signal com transporte de relay Nostr, lançou [v1.41.1+6513](https://github.com/keychat-io/keychat-app/releases/tag/v1.41.1+6513). A correção em destaque impõe forward secrecy excluindo prekeys únicos Signal imediatamente após uma descriptografia bem-sucedida, fechando uma lacuna onde um prekey retido poderia ser usado para descriptografar mensagens passadas se o dispositivo fosse comprometido posteriormente. A release também adiciona preview de URL para mensagens consistindo de um único link, centraliza auto-download de mídia sob um novo `FileDownloadManager` com um limite automático de 20 MB, e refatora a busca de info de relay NIP-11 para forçar refresh em cold start para que configurações de fee de relay pago sempre carreguem corretamente.

## Em desenvolvimento

**Citrine** mesclou [PR #151](https://github.com/greenart7c3/Citrine/pull/151) implementando aplicação de NIP-70: o relay Android agora bloqueia reposts que embutem conteúdo de eventos protegidos, como a especificação requer. [PR #149](https://github.com/greenart7c3/Citrine/pull/149) adiciona ações de exibição e cópia para múltiplos endereços de conexão, localhost, Wi-Fi local e Tor, a partir da tela de configurações do relay. [PR #141](https://github.com/greenart7c3/Citrine/pull/141) adiciona tratamento de challenge AUTH NIP-42 através de integração com signer externo Amber.

**Mostro** chegou à Fase 2 de seu rollout de bond anti-abuso. [PR #737](https://github.com/MostroP2P/mostro/pull/737) aterrissa a lógica de slash de disputa dirigida pelo solver: handlers de admin agora consomem o payload `BondResolution` do mostro-core, permitindo que um admin dê slash no bond de qualquer parte ao resolver uma disputa. A Fase 1.5, mesclada no [PR #736](https://github.com/MostroP2P/mostro/pull/736), introduziu uma ação dedicada `PayBondInvoice` e status `WaitingTakerBond`, separando o pagamento do bond anti-abuso do taker do payout de trade do buyer. O cliente mobile adicionou o UX completo da Fase 1.5 no [PR #592](https://github.com/MostroP2P/mobile/pull/592). Mostro é um protocolo de câmbio Bitcoin peer-to-peer construído no Nostr.

**Damus** mesclou [PR #3773](https://github.com/damus-io/damus/pull/3773) restaurando o indicador de sinal de relay, e [PR #3775](https://github.com/damus-io/damus/pull/3775) corrige relays que se recusavam a reconectar após uma falha inicial de conexão.

**rust-nostr** mesclou [PR #1358](https://github.com/rust-nostr/nostr/pull/1358) adicionando traits de finalização de eventos e builders de evento específicos de NIP, tornando mais fácil construir eventos corretamente tipados para funções específicas de protocolo. [PR #1363](https://github.com/rust-nostr/nostr/pull/1363) faz backport de uma correção garantindo que o signer NIP-46 se inscreva em notificações antes de enviar a resposta de connect, fechando uma condição de corrida onde mensagens de cliente chegando imediatamente após connect poderiam ser perdidas.

**dart-nostr** mesclou [PR #44](https://github.com/ethicnology/dart-nostr/pull/44) adicionando um resolver de relay Namecoin `.bit` e registros TLSA pin, permitindo que aplicações Flutter resolvam URLs de relay `wss://example.bit/` através de DNS Namecoin para seus endereços WebSocket reais.

**Dart NDK** (o kit de desenvolvimento Nostr Dart/Flutter, agora em `relaystr/ndk`) mesclou [PR #464](https://github.com/relaystr/ndk/pull/464) implementando NIP-77, o protocolo de assinatura offline de eventos. No lado do signer, [PR #602](https://github.com/relaystr/ndk/pull/602) e [PR #601](https://github.com/relaystr/ndk/pull/601) adicionam um signer de evento específico da web e uma abstração `PlatformEventVerifier`, permitindo que apps Flutter web usem o signer da plataforma sem um caminho de código separado; [PR #604](https://github.com/relaystr/ndk/pull/604) introduz uma factory de signer de evento para seleção de signer em runtime. [PR #608](https://github.com/relaystr/ndk/pull/608) adiciona `getDmRelays()` para buscar a lista de relays de DM NIP-17 de um usuário (kind:10050), e [PR #600](https://github.com/relaystr/ndk/pull/600) corrige a preservação de campos assinados NIP-46 para que signers remotos não percam campos no round-trip.

**Pages by Form\*** ([repo](https://github.com/formstr-hq/nostr-docs)), o app colaborativo de documentos Nostr-native do Formstr hospedado em [pages.formstr.app](https://pages.formstr.app), mesclou quatro PRs esta semana apertando os fluxos de anexo criptografado e gerenciamento de documentos. [PR #37](https://github.com/formstr-hq/nostr-docs/pull/37) corrige imagens faltando em exportações DOCX, HTML e PDF fazendo inline de anexos criptografados: busca blobs `<encrypted-file>` de servidores Blossom, descriptografa-os com AES-GCM 256-bit usando a chave e nonce armazenados, valida o tipo MIME da imagem e os converte em URLs data base64 para que exportações preservem imagens que só existem no Blossom em forma criptografada. [PR #39](https://github.com/formstr-hq/nostr-docs/pull/39) adiciona um mecanismo de busca local de documentos, [PR #38](https://github.com/formstr-hq/nostr-docs/pull/38) limpa o fluxo de renomear, e [PR #40](https://github.com/formstr-hq/nostr-docs/pull/40) corrige o tratamento de backup compartilhado.

**Zap Cooking** mesclou [PR #396](https://github.com/zapcooking/frontend/pull/396), a primeira fase de uma reformulação de feed que assenta primitivas de renderização de feed sem nenhuma mudança visível ao usuário ainda. O PR introduz um parser de tag `imeta` NIP-92 que lê os slots `url`, `m` (MIME), `dim` (dimensões), `blurhash`, `alt`, `x` (hash de arquivo) e `fallback`, mais um decodificador blurhash canônico portado à mão (~200 LOC) que produz URLs data PNG via canvas com um fallback null seguro para SSR. Quando tags `imeta` estão ausentes, o parser recorre a extrair URLs brutos de imagem e vídeo do conteúdo do evento usando as mesmas heurísticas que o feed atual já usa.

**Nurunuru** (ぬるぬる, `tami1A84/null--nostr`), um cliente Nostr com variantes nativas Android, iOS e Web compartilhando um motor FFI Rust, mesclou seu sync Native → Web v1.5.0 no [PR #176](https://github.com/tami1A84/null--nostr/pull/176). O sync traz várias adições de recursos ao build Web que já foram lançadas no Android v1.4.9 e iOS 1.0.4: o [NotificationModal](https://github.com/tami1A84/null--nostr/pull/176) agora apresenta notificações de aniversário, detecção de zap de follow mútuo e notificações de reação com emoji customizado; o picker de reação abandona a linha rápida de reações padrão Unicode e centra o UX em emoji customizado; o motor de recomendação em `lib/recommendation.js` filtra usuários sem ícones ou display names e prioriza entradas Following com Recomendado carregando em background. Entrada de voz é o único recurso indo na outra direção: o build Web já usa streaming ElevenLabs Scribe, e v1.5.0 sincroniza parcialmente o lado Nativo para o `SpeechRecognizer` padrão do OS (Android) e `SFSpeechRecognizer` + `AVAudioEngine` (iOS) enquanto a integração completa do Native Scribe é adiada para v1.6.

## Trabalho de protocolo e especificação

**PR [#2251](https://github.com/nostr-protocol/nips/pull/2251)** aperta a especificação de eventos protegidos NIP-70: agora afirma explicitamente que reposts embutindo o conteúdo completo de um evento protegido devem ser rejeitados pelos relays. NIP-70 define a tag `-` que sinaliza que um autor de nota não consente com ter sua nota republicada. A especificação original cobria o comportamento de filtragem do relay, mas deixava o caso de repost ambíguo. Este PR fecha essa lacuna. O [PR #151](https://github.com/greenart7c3/Citrine/pull/151) do Citrine implementa a aplicação no lado do relay nesta mesma semana.

**PR [#1653](https://github.com/nostr-protocol/nips/pull/1653)** propõe um NIP de Drafts para salvar e sincronizar eventos de rascunho privados. A proposta usa eventos substituíveis com um status `draft` e criptografia NIP-44 para a própria chave do autor, permitindo aos clientes salvar trabalhos em progresso em relays sem que esses eventos sejam visíveis a mais ninguém. O evento draft carrega o evento de publicação pretendida completo como conteúdo criptografado, incluindo seu eventual kind e tags.

**Snapshots ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279))** é uma proposta aberta para definir um evento de snapshot imutável para preservar uma versão exata de um evento Nostr substituível. O evento snapshot carrega o conteúdo completo do evento substituível em um ponto dado no tempo, com uma tag `a` ligando-o de volta ao endereço do evento substituível para que todas as versões históricas sejam consultáveis juntas. Isso torna possível para observadores inspecionar estado histórico mesmo após relays pararem de reter versões antigas.

**Onda de NIP-05 Namecoin:** Esta semana viu um esforço coordenado para adicionar resolução NIP-05 `.bit` a clientes Nostr. O feed de discussão de NIP capturou PRs open-source contra Aegis ([#14](https://github.com/ZharlieW/Aegis/pull/14), que adiciona verificação no momento da assinatura no signer), nostter ([#2128](https://github.com/SnowCait/nostter/pull/2128)) e dart-nostr ([#44](https://github.com/ethicnology/dart-nostr/pull/44)), junto com um rascunho de NIP upstream ([PR #2349](https://github.com/nostr-protocol/nips/pull/2349)). O PR do Aegis é notável por colocar a verificação no lado produtor: o signer verifica a chain Namecoin antes de assinar qualquer evento kind:0 que reivindique uma identidade `.bit` e avisa o usuário em caso de mismatch, capturando o problema antes que o evento chegue a qualquer relay.

## Deep Dive de NIP: NIP-07 (window.nostr para Navegadores Web)

[NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) define a interface `window.nostr` que extensões de navegador expõem a aplicações web. É a interface de signer mais amplamente implantada na web, implementada por extensões incluindo Alby, nos2x, Flamingo e horse.

A interface tem dois métodos obrigatórios e vários opcionais. `window.nostr.getPublicKey()` retorna a chave pública do usuário como uma string hex sem nunca expor a chave privada à página chamadora. `window.nostr.signEvent(event)` recebe um evento parcial com `created_at`, `kind`, `tags` e `content`, e retorna o evento assinado completo com `id`, `pubkey` e `sig` adicionados. O ponto chave é que a chave privada nunca deixa o contexto isolado da extensão; a aplicação web submete um evento não assinado e recebe de volta um assinado.

Os métodos opcionais cobrem criptografia: `window.nostr.nip04.encrypt` e `window.nostr.nip04.decrypt` para o esquema mais antigo NIP-04 (agora descontinuado), e `window.nostr.nip44.encrypt` e `window.nostr.nip44.decrypt` para o esquema atual NIP-44. Extensões que suportam NIP-44 podem portanto lidar tanto com criptografia de mensagens diretas quanto com qualquer outra aplicação que precise de criptografia com chave por pubkey sem a página chamadora ver a nsec.

A especificação também inclui uma recomendação aos autores de extensões: carregue scripts com `"run_at": "document_end"` no manifest da extensão para que `window.nostr` esteja disponível sincronamente quando a página carrega, evitando condições de corrida onde um cliente verifica `window.nostr` antes de a extensão tê-lo injetado.

Um exemplo chave de NIP-07 em ação é o projeto Keycast coberto acima. O frontend web do Keycast usa NIP-07 para assinar eventos HTTP auth NIP-98: o app SvelteKit nunca manuseia a nsec do usuário diretamente. Ele chama `window.nostr.signEvent` para produzir o header de auth, então envia esse header à API do Keycast. Essa arquitetura significa que o material da chave fica na extensão do navegador durante todo o fluxo de gerenciamento de chaves de equipe.

```json
{
  "id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 1,
  "tags": [],
  "content": "Hello from a NIP-07 signed event",
  "sig": "0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2cdd"
}
```

## Deep Dive de NIP: NIP-39 (identidades externas em perfis)

[NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) define como um usuário Nostr pode declarar controle sobre identidades de plataformas externas em seu perfil. Cada declaração usa uma tag `i` dentro de um evento kind:10011, afirmando propriedade de uma conta específica em outra plataforma junto com uma prova que pode ser verificada independentemente.

Cada tag segue o formato `["i", "platform:identity", "proof"]`, onde `platform:identity` combina o nome da plataforma e o nome de usuário com um separador de dois-pontos (`github:semisol`, `twitter:semisol_public`). `proof` aponta para um artefato verificável na própria plataforma.

Para GitHub, a prova é um Gist ID. O usuário cria um Gist público de sua conta GitHub contendo o texto `Verifying that I control the following Nostr public key: npub1...`. Um cliente verificando a reivindicação busca `https://gist.github.com/<identity>/<proof>` e verifica que o Gist foi criado pelo nome de usuário GitHub reivindicado e contém a pubkey esperada. Para Twitter a prova é um tweet ID, para Mastodon um post ID, e para Telegram uma referência de mensagem em um grupo público.

O nome do provedor de identidade deve conter apenas `a-z`, `0-9` e os caracteres `._-/`, e não deve conter `:`. Nomes de identidade devem ser normalizados para minúsculas, com o alias primário usado quando múltiplos existem.

A discussão NIP-05 `.bit` do Namecoin acontecendo esta semana mostra o papel do NIP-39 na stack de identidade mais ampla: fornece uma forma padronizada e agnóstica a relay de cross-referenciar uma chave Nostr com uma identidade estabelecida em outro lugar, sem exigir nenhuma autoridade de verificação central. Um cliente pode verificar independentemente a prova buscando um artefato público na plataforma nomeada, e a prova está vinculada à pubkey Nostr específica no texto do Gist ou tweet, não a uma credencial genérica da plataforma.

```json
{
  "id": "b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 10011,
  "tags": [
    ["i", "github:semisol", "9721ce4ee4fceb91c9711ca2a6c9a5ab"],
    ["i", "twitter:semisol_public", "1619358434134196225"],
    ["i", "mastodon:bitcoinhackers.org/@semisol", "109775066355589974"]
  ],
  "content": "",
  "sig": "1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3eff"
}
```

---

É isso por esta semana. Se você está construindo algo ou tem novidades para compartilhar, mande uma DM para nós no Nostr ou nos encontre em [nostrcompass.org](https://nostrcompass.org).
