---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

Bem-vindo de volta ao Nostr Compass, seu guia semanal para o ecossistema do protocolo Nostr.

**Esta semana:** O Primal Android lança suporte para assinatura remota [NIP-46](/pt/topics/nip-46/) e assinatura local [NIP-55](/pt/topics/nip-55/), tornando-se um hub completo de assinatura para outros aplicativos Android. A equipe do [Marmot Protocol](/pt/topics/marmot/) abordou descobertas de uma auditoria de segurança com 18 PRs mesclados, fortalecendo a mensageria criptografada baseada em [MLS](/pt/topics/mls/). O Citrine atinge a v1.0 e o Applesauce lança a v5.0 em toda sua suíte de bibliotecas. O TENEX desenvolve supervisão de agentes de IA no Nostr, e o Jumble adiciona pooling inteligente de relays. Uma correção na especificação NIP-55 esclarece os campos de retorno do `nip44_encrypt`, e um PR do [NIP-50](/pt/topics/nip-50/) propõe extensões de expressões de consulta para busca avançada. Em nosso aprofundamento, explicamos [NIP-04](/pt/topics/nip-04/) e [NIP-44](/pt/topics/nip-44/): por que a criptografia legada tem falhas de segurança e como a substituição moderna as corrige.

## Notícias

**Primal Android se Torna um Hub Completo de Assinatura** - A [versão 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) adiciona tanto assinatura remota [NIP-46](/pt/topics/nip-46/) quanto assinatura local [NIP-55](/pt/topics/nip-55/), transformando o Primal em um assinador completo para outros aplicativos Nostr. A assinatura remota via NIP-46 permite que usuários se conectem a serviços bunker através de relays Nostr, mantendo as chaves completamente fora do dispositivo. A assinatura local via NIP-55 expõe o Primal como um provedor de conteúdo Android, para que aplicativos como Amethyst ou Citrine possam solicitar assinaturas sem nunca tocar na chave privada. [Vários PRs de acompanhamento](https://github.com/PrimalHQ/primal-android-app/pull/839) corrigiram problemas de compatibilidade com o requisito de pubkey hexadecimal da especificação NIP-55 e melhoraram o parsing de URIs `nostrconnect://` malformadas. O lançamento também inclui pré-cache de mídia para rolagem mais suave, tempos de carregamento de threads aprimorados e pré-cache de avatares.

**Marmot Protocol Fortalece Segurança Após Auditoria** - O [Marmot Development Kit](https://github.com/marmot-protocol/mdk) (mdk), que implementa mensageria criptografada de ponta a ponta baseada em MLS do [NIP-104](/pt/topics/nip-104/), recebeu extensas correções de segurança esta semana. Dezoito pull requests mesclados abordaram descobertas da auditoria, incluindo: [verificação de hash para imagens de grupo criptografadas](https://github.com/marmot-protocol/mdk/pull/97) para prevenir ataques de substituição de blob no nível de armazenamento, [paginação para boas-vindas pendentes](https://github.com/marmot-protocol/mdk/pull/110) para prevenir esgotamento de memória, [vazamento de Group ID MLS em mensagens de erro](https://github.com/marmot-protocol/mdk/pull/112), e [aplicação de codificação base64](https://github.com/marmot-protocol/mdk/pull/98) para pacotes de chaves. A [própria especificação Marmot foi atualizada](https://github.com/marmot-protocol/marmot/pull/20) com versionamento MIP-04 v2 e melhorias de segurança. PRs ativos continuam abordando reutilização de nonce, zeroização de segredos e vetores de poluição de cache.

**Nostrability Rastreia Suporte a Relay Hints** - Um novo [rastreador de compatibilidade de relay hints](https://github.com/nostrability/nostrability/issues/270) documenta como os clientes constroem e consomem relay hints em todo o ecossistema. O rastreador revela que, embora a maioria dos clientes agora construa hints conforme o [NIP-10](/pt/topics/nip-10/) e [NIP-19](/pt/topics/nip-19/), o consumo varia amplamente: alguns clientes incluem hints em eventos de saída, mas não usam hints de entrada para busca. Seis clientes ganharam status de nível "Completo" por implementação completa. O rastreador é útil para desenvolvedores verificando interoperabilidade e para usuários se perguntando por que alguns clientes encontram conteúdo que outros não conseguem.

**Nostria 2.0 Lança Reformulação de Recursos Multiplataforma** - O cliente [Nostria](https://nostria.app) [lançou a versão 2.0](https://njump.me/nevent1qqs9z4l8z82zphszjlmrjkr8whpvupnlaxc7xk5gfg9syzj0thygtzgpz4mhxue69uhhyetvv9ujuerpd46hxtnfduhszxthwden5te0wfjkccte9enrw73wd9hsz9nhwden5te0wfjkccte9ec8y6tdv9kzumn9wsq3gamnwvaz7tmjv4kxz7fwv3sk6atn9e5k7qgkwaehxw309aex2mrp0yhxgctdw4eju6t09uq32amnwvaz7tmwdaejumr0dshsz9mhwden5te0wfjkccte9ec82c30989ksmfnv9kzumn9wshsqgzxsnsv7pfqqd7rw4fvr0jnkpqmwzfqq3znlc4pqunagxrkl84u66y7fq9) em 30 de dezembro com adições significativas em iOS (TestFlight), Android (Play Store), Web e Windows. O lançamento adiciona suporte nativo a música com criação de playlists, upload de faixas, pagamentos de artistas via zap e um player estilo WinAmp com equalizador funcional. Transmissões ao vivo ganham integração com Game API mostrando metadados ricos durante streams de gameplay. Um novo recurso de Resumo gera digestos de atividade por hora, dia ou semana como visualizações de timeline comprimidas. A seção Descobrir oferece listas curadas para encontrar conteúdo e perfis. A publicação de mídia é simplificada com geração automática de posts curtos para descoberta entre clientes. Conexões com assinadores remotos agora funcionam via escaneamento de QR code sem configuração manual. A descoberta de perfis aborda um problema comum do Nostr: quando usuários migram entre relays sem trazer seus metadados, o Nostria localiza seu perfil e o republica nos relays atuais. Assinantes premium ganham integração com canais do YouTube, Memos privados, painéis de análise e backups automáticos de lista de seguidos com opções de mesclagem/restauração.

## Atualizações de NIPs

Mudanças recentes no [repositório de NIPs](https://github.com/nostr-protocol/nips):

**Mesclados:**
- **[NIP-55](/pt/topics/nip-55/)** - Corrigido o campo de retorno para o método `nip44_encrypt` ([#2184](https://github.com/nostr-protocol/nips/pull/2184)). Assinadores Android agora devem retornar o payload criptografado no campo `signature` (correspondendo ao `nip44_decrypt`) em vez de um campo separado. Isso alinha a especificação com implementações existentes no Amber e Primal.

**PRs Abertos:**
- **[NIP-50](/pt/topics/nip-50/)** - Extensões de Expressões de Consulta ([#2182](https://github.com/nostr-protocol/nips/pull/2182)) propõe estender a busca do NIP-50 com expressões de consulta estruturadas. O PR adiciona operadores como `kind:1`, `author:npub1...` e combinações booleanas (`AND`, `OR`, `NOT`), permitindo consultas de busca mais precisas além da simples correspondência de texto. Isso permitiria que clientes construíssem interfaces de busca avançada mantendo compatibilidade com strings de busca básicas.

## Aprofundamento em NIPs: NIP-04 e NIP-44

Esta semana cobrimos os padrões de criptografia do Nostr: o legado NIP-04 que você ainda encontrará, e sua substituição moderna NIP-44 que corrige falhas críticas de segurança.

### [NIP-04](/pt/topics/nip-04/): Mensagens Diretas Criptografadas (Legado)

O [NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md) foi a primeira tentativa do Nostr de mensageria criptografada, usando eventos kind 4. Embora simples de implementar, possui fraquezas de segurança conhecidas e está deprecado em favor do NIP-44.

**Como funciona:** O NIP-04 usa ECDH (Elliptic Curve Diffie-Hellman) para derivar um segredo compartilhado entre remetente e destinatário, depois criptografa com AES-256-CBC.

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

O fluxo de criptografia:
1. Computar ponto compartilhado: `shared = ECDH(sender_privkey, recipient_pubkey)`
2. Derivar chave: `key = SHA256(shared_x_coordinate)`
3. Gerar IV aleatório de 16 bytes
4. Criptografar: `ciphertext = AES-256-CBC(key, iv, plaintext)`
5. Formatar conteúdo: `base64(ciphertext)?iv=base64(iv)`

**Problemas de segurança:**

- **Sem autenticação:** AES-CBC fornece confidencialidade mas não integridade. Um atacante que controla um relay poderia modificar bits do ciphertext, causando mudanças previsíveis no plaintext (ataques de bit-flipping).
- **IV em claro:** O vetor de inicialização é transmitido junto com o ciphertext, e o modo CBC com IVs previsíveis permite ataques de plaintext escolhido.
- **Sem validação de padding:** Implementações variam em como lidam com padding PKCS#7, potencialmente permitindo ataques de padding oracle.
- **Exposição de metadados:** A pubkey do remetente, pubkey do destinatário e timestamp são todos visíveis para os relays.
- **Reutilização de chave:** O mesmo segredo compartilhado é usado para todas as mensagens entre duas partes, para sempre.

**Por que ainda existe:** Muitos clientes e relays mais antigos suportam apenas NIP-04. Você o encontrará ao interagir com sistemas legados. Assinadores como Amber e aplicativos como Primal ainda implementam `nip04_encrypt`/`nip04_decrypt` para compatibilidade retroativa.

### [NIP-44](/pt/topics/nip-44/): Criptografia Versionada

O [NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) é o padrão moderno de criptografia, projetado para corrigir as falhas conhecidas do NIP-04. Uma auditoria de segurança da Cure53 das implementações do NIP-44 identificou 10 problemas (incluindo ataques de timing e preocupações com forward secrecy) que foram abordados antes da especificação ser finalizada. Ele usa ChaCha20-Poly1305 com derivação de chave adequada e criptografia autenticada.

**Principais melhorias sobre o NIP-04:**

| Aspecto          | NIP-04                     | NIP-44                  |
|:-----------------|:---------------------------|:------------------------|
| Cifra            | AES-256-CBC                | XChaCha20-Poly1305      |
| Autenticação     | Nenhuma                    | MAC Poly1305            |
| Derivação de chave | SHA256(shared_x)         | HKDF com salt           |
| Nonce            | IV de 16 bytes, padrão reutilizado | Nonce aleatório de 24 bytes |
| Padding          | PKCS#7 (vaza tamanho)      | Preenchido para potência de 2 |
| Versionamento    | Nenhum                     | Prefixo de byte de versão |

**Fluxo de criptografia:**

1. **Chave de conversa:** Deriva uma chave estável para cada par remetente-destinatário:
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **Chaves de mensagem:** Para cada mensagem, gera um nonce aleatório de 32 bytes e deriva chaves de criptografia/autenticação:
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **Preencher plaintext:** Preenche até a próxima potência de 2 (mínimo 32 bytes) para ocultar o tamanho da mensagem:
   ```
   padded = [length_u16_be] + [plaintext] + [zeros até próxima potência de 2]
   ```

4. **Criptografar e autenticar:**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **Formatar payload:**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**Byte de versão:** O primeiro byte (`0x02`) indica a versão da criptografia. Isso permite atualizações futuras sem quebrar mensagens existentes. A versão `0x01` foi um rascunho anterior que nunca foi amplamente implantado.

**Descriptografia:**

1. Decodificar base64, verificar se o byte de versão é `0x02`
2. Extrair nonce (bytes 1-32), ciphertext e MAC (últimos 32 bytes)
3. Derivar chave de conversa usando a chave privada do destinatário e a chave pública do remetente
4. Derivar chaves de mensagem a partir da chave de conversa e nonce
5. Verificar MAC antes de descriptografar (rejeitar se inválido)
6. Descriptografar ciphertext, extrair prefixo de tamanho, retornar plaintext sem padding

**Propriedades de segurança:**

- **Criptografia autenticada:** O MAC Poly1305 garante que qualquer adulteração seja detectada antes da descriptografia
- **Forward secrecy (parcial):** Cada mensagem usa um nonce único, então comprometer uma mensagem não revela outras. No entanto, comprometer uma chave privada ainda revela todas as mensagens passadas (sem ratcheting).
- **Ocultação de tamanho:** Padding para potência de 2 obscurece o tamanho exato da mensagem
- **Resistência a ataques de timing:** Comparação em tempo constante para verificação de MAC

**Uso na prática:** O NIP-44 é a camada de criptografia para:
- Mensagens diretas privadas do [NIP-17](/pt/topics/nip-17/) (dentro do gift wrap)
- Comunicação com assinador remoto do [NIP-46](/pt/topics/nip-46/)
- Criptografia de seal do [NIP-59](/pt/topics/nip-59/)
- Mensagens de grupo do [Marmot Protocol](/pt/topics/nip-104/), onde o NIP-44 envolve conteúdo criptografado por MLS usando uma chave derivada do segredo exportador MLS
- Qualquer aplicação que necessite criptografia segura ponto a ponto

**Orientação de migração:** Novos aplicativos devem usar NIP-44 exclusivamente. Para compatibilidade retroativa, verifique se o cliente de um contato suporta NIP-44 (via metadados de app do [NIP-89](/pt/topics/nip-89/) ou suporte do relay) antes de recorrer ao NIP-04. Ao receber mensagens, tente primeiro a descriptografia NIP-44, depois recorra ao NIP-04 para conteúdo legado.

## Lançamentos

**Primal Android v2.6.18** - O [lançamento completo](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) adiciona assinatura remota [NIP-46](/pt/topics/nip-46/) e assinatura local [NIP-55](/pt/topics/nip-55/), transformando o Primal em um hub de assinatura para outros aplicativos Android. Melhorias de desempenho incluem pré-cache de mídia, pré-cache de avatares e carregamento mais rápido de threads. Correções de bugs abordam auto-menções em bios, crashes na galeria de mídia e fallbacks de título de stream. No iOS, o Primal usa reprodução de áudio em segundo plano para manter o aplicativo ativo para receber solicitações de assinatura NIP-46; usuários podem alterar o som ou silenciá-lo completamente nas configurações.

**Mostro v0.15.6** - O [último lançamento](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6) da plataforma de negociação P2P de Bitcoin [NIP-69](/pt/topics/nip-69/) completa a implementação do fundo de desenvolvimento com eventos de auditoria da Fase 4. Pagamentos de taxa de desenvolvimento agora são rastreados via eventos Nostr kind 38383 publicados após cada pagamento bem-sucedido, permitindo verificação de terceiros e análises. Os cálculos de valores foram corrigidos para mensagens de comprador/vendedor, e a lógica de premium foi alinhada com a implementação de referência do lnp2pbot.

**Aegis v0.3.5** - O assinador multiplataforma [adiciona modo escuro](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5), exibição melhorada de ícones de aplicativo e layouts de UI mais limpos. Correções de bugs abordam conflitos com o iCloud Private Relay do iOS e problemas de parsing de eventos. O lançamento também melhora como o JSON de eventos é passado para a função de assinatura Rust.

**Citrine v1.0.0** - O aplicativo de relay Android [atinge a versão 1.0](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0). O Citrine permite executar um relay Nostr pessoal diretamente no seu dispositivo Android, útil para cache local, backup ou como complemento NIP-55. Este lançamento adiciona um handler de relatório de crash, melhora a eficiência de consultas ao banco de dados e atualiza traduções via Crowdin.

**Applesauce v5.0.0** - A suíte de bibliotecas TypeScript do hzrd149 [lança uma versão major](https://github.com/hzrd149/applesauce/releases) com breaking changes focadas em correção e simplicidade. O pacote core agora [verifica assinaturas de eventos por padrão](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0) e renomeia métodos de coordenadas para usar terminologia mais clara de "address" (`parseCoordinate` -> `parseReplaceableAddress`). O pacote relay [reduz tentativas padrão de 10 para 3](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0) e ignora relays inalcançáveis por padrão, além de adicionar `createUnifiedEventLoader` para busca de eventos simplificada. O pacote wallet ganha [descoberta de mint Cashu](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet%405.0.0) do [NIP-87](/pt/topics/nip-87/). Dependências diretas do `nostr-tools` foram removidas dos pacotes, reduzindo tamanho do bundle e conflitos de versão.

## Mudanças notáveis de código e documentação

*Estes são pull requests abertos e trabalho em estágio inicial, perfeitos para obter feedback antes de serem mesclados. Se algo chamar sua atenção, considere revisar ou comentar!*

### Damus (iOS)

Uma série de PRs melhora a experiência de artigos longos. [Melhorias de UX de leitura](https://github.com/damus-io/damus/pull/3496) adicionam uma barra de progresso, tempo estimado de leitura, modo sépia, altura de linha ajustável e modo de foco que oculta a navegação durante a rolagem. [Correções de imagem](https://github.com/damus-io/damus/pull/3489) garantem que imagens em conteúdo markdown sejam exibidas com proporções adequadas, pré-processando imagens isoladas como elementos de nível de bloco. [Cards de preview de artigos longos](https://github.com/damus-io/damus/pull/3497) substituem texto inline `@naddr1...` por cards de preview ricos mostrando título e metadados do artigo. Uma nova [suíte de testes de integração de relay](https://github.com/damus-io/damus/pull/3508) adiciona 137 testes relacionados à rede, incluindo verificação do protocolo [NIP-01](/pt/topics/nip-01/) e comportamento sob condições de rede degradadas (simulação 3G).

### Bitchat (Mensageria Criptografada)

Fortalecimento de segurança no mensageiro iOS Nostr+Cashu. [Limpeza de segredo DH do protocolo Noise](https://github.com/permissionlesstech/bitchat/pull/928) corrige seis locais onde segredos compartilhados não estavam sendo zerados após acordo de chave Diffie-Hellman, restaurando garantias de forward secrecy. [Thread safety para filas de confirmação de leitura](https://github.com/permissionlesstech/bitchat/pull/929) adiciona sincronização de barreira para prevenir condições de corrida no NostrTransport. [Otimização do deduplicador de mensagens](https://github.com/permissionlesstech/bitchat/pull/920) melhora o desempenho com altos volumes de mensagens, e [hardening de parsing de string hexadecimal](https://github.com/permissionlesstech/bitchat/pull/919) previne crashes de entrada malformada.

### Frostr (Assinatura por Threshold)

O protocolo de assinatura por threshold baseado em [FROST](/pt/topics/frost/) [adicionou exibição de QR code](https://github.com/FROSTR-ORG/igloo-desktop/pull/62) para credenciais de grupo e credenciais de share durante o onboarding e na interface do assinador. Isso permite configuração mais fácil ao distribuir shares de chave entre múltiplos dispositivos, permitindo que usuários escaneiem credenciais em vez de copiar manualmente strings longas.

### Marmot mdk (Biblioteca)

Além das correções de segurança mencionadas acima, PRs ativos abordam descobertas restantes da auditoria: [Tipo Secret<T> para zeroização](https://github.com/marmot-protocol/mdk/pull/109) introduz um tipo wrapper que automaticamente zera dados sensíveis ao ser descartado, [paginação de consulta de mensagens](https://github.com/marmot-protocol/mdk/pull/111) previne esgotamento de memória ao carregar histórico de chat, e [armazenamento criptografado](https://github.com/marmot-protocol/mdk/pull/102) adiciona criptografia em repouso para o banco de dados SQLite que armazena estado do grupo e mensagens.

### Amethyst (Android)

Uma semana movimentada de correções de estabilidade no cliente Android. [Parsing JSON leniente](https://github.com/vitorpamplona/amethyst/commit/2c42796) previne crashes de eventos malformados tornando a serialização Kotlin mais tolerante. A validação de eventos agora [verifica o tamanho do campo kind](https://github.com/vitorpamplona/amethyst/commit/40f9622) antes do processamento para evitar exceções de valores oversized. A UI de score de confiança ganhou um ícone menor para reduzir interferência visual, e [logging de erros melhorado](https://github.com/vitorpamplona/amethyst/commit/69c53ac) ajuda a diagnosticar problemas de conexão com relays. Atualizações de tradução chegaram via Crowdin, e vários avisos do SonarQube foram tratados.

### TENEX (Agentes de IA)

O framework de agentes de IA nativo do Nostr teve 81 commits esta semana desenvolvendo capacidades autônomas. O novo [sistema de supervisão de agentes](https://github.com/tenex-chat/tenex/pull/48) implementa heurísticas comportamentais para monitorar ações de agentes e intervir quando necessário. [Transparência de delegação](https://github.com/tenex-chat/tenex/commit/b244c10) adiciona logging de intervenção do usuário aos transcripts de delegação, para que usuários possam auditar o que os agentes fizeram em seu nome. O [registro de provedores LLM](https://github.com/tenex-chat/tenex/pull/47) foi modularizado para integração mais fácil de diferentes backends de IA. Suporte a conversas entre projetos permite que agentes mantenham contexto através de múltiplos projetos baseados em Nostr.

### Jumble (Cliente Web)

O cliente web focado em relays adicionou várias melhorias de experiência do usuário. [Pool de relay inteligente](https://github.com/CodyTseng/jumble/commit/695f2fe) gerencia conexões de forma inteligente com base em padrões de uso. [Toggle de feed ao vivo](https://github.com/CodyTseng/jumble/commit/917fcd9) permite que usuários alternem entre streaming em tempo real e atualização manual. [Auto-mostrar novas notas](https://github.com/CodyTseng/jumble/commit/d1b3a8c) no topo exibe conteúdo fresco sem exigir recarregamento da página. [Cache persistente](https://github.com/CodyTseng/jumble/commit/fd9f41c) para feed de seguidos e notificações melhora os tempos de carregamento em visitas de retorno. Usuários agora podem [alterar relays padrão](https://github.com/CodyTseng/jumble/commit/53a67d8) através das configurações.

---

Isso é tudo para esta semana. Está construindo algo? Tem notícias para compartilhar? Quer que cobramos seu projeto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Entre em contato via DM NIP-17</a> ou nos encontre no Nostr.
