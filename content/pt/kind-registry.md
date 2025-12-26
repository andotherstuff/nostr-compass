---
title: Registro de Kinds
url: /pt/kind-registry/
translationOf: /en/kind-registry.md
translationDate: 2025-12-26
---

Os kinds de eventos sao inteiros que categorizam os eventos do Nostr. Este registro lista todos os kinds padronizados com suas descricoes e NIPs que os definem.

**Intervalos de kinds** (de [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)):
- **0-999**: Eventos regulares (todas as versoes sao mantidas)
- **1000-9999**: Eventos regulares (continuacao)
- **10000-19999**: Eventos substituiveis (apenas o mais recente por pubkey e mantido)
- **20000-29999**: Eventos efemeros (nao armazenados, apenas encaminhados)
- **30000-39999**: Eventos enderecaveis (mais recente por pubkey + kind + d-tag)

## Eventos Principais (0-99)

| Kind | Descricao | NIP |
|------|-----------|-----|
| 0 | Metadados do Usuario | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 1 | Nota de Texto Curta | [10](https://github.com/nostr-protocol/nips/blob/master/10.md) |
| 2 | Recomendar Relay (descontinuado) | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 3 | Seguindo | [02](https://github.com/nostr-protocol/nips/blob/master/02.md) |
| 4 | Mensagens Diretas Criptografadas | [04](https://github.com/nostr-protocol/nips/blob/master/04.md) |
| 5 | Solicitacao de Exclusao de Evento | [09](https://github.com/nostr-protocol/nips/blob/master/09.md) |
| 6 | Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 7 | Reacao | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 8 | Concessao de Distintivo | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 9 | Mensagem de Chat | [C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) |
| 10 | Resposta em Thread de Chat de Grupo (descontinuado) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 11 | Thread | [7D](https://github.com/nostr-protocol/nips/blob/master/7D.md) |
| 12 | Resposta em Thread de Grupo (descontinuado) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 13 | Seal | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 14 | Mensagem Direta | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 15 | Mensagem de Arquivo | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 16 | Repost Generico | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 17 | Reacao a um website | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 20 | Imagem | [68](https://github.com/nostr-protocol/nips/blob/master/68.md) |
| 21 | Evento de Video | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 22 | Video Vertical Curto | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 40 | Criacao de Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 41 | Metadados do Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 42 | Mensagem do Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 43 | Ocultar Mensagem do Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 44 | Silenciar Usuario do Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 62 | Solicitacao de Desaparecimento | [62](https://github.com/nostr-protocol/nips/blob/master/62.md) |
| 64 | Xadrez (PGN) | [64](https://github.com/nostr-protocol/nips/blob/master/64.md) |

## Criptografia MLS (443-445)

| Kind | Descricao | NIP |
|------|-----------|-----|
| 443 | KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 444 | Mensagem de Boas-vindas | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 445 | Evento de Grupo | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |

## Eventos Regulares (1000-9999)

| Kind | Descricao | NIP |
|------|-----------|-----|
| 1018 | Resposta de Enquete | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1021 | Lance | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1022 | Confirmacao de Lance | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1040 | OpenTimestamps | [03](https://github.com/nostr-protocol/nips/blob/master/03.md) |
| 1059 | Gift Wrap | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 1063 | Metadados de Arquivo | [94](https://github.com/nostr-protocol/nips/blob/master/94.md) |
| 1068 | Enquete | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1111 | Comentario | [22](https://github.com/nostr-protocol/nips/blob/master/22.md) |
| 1222 | Mensagem de Voz | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1244 | Comentario de Mensagem de Voz | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1311 | Mensagem de Chat ao Vivo | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 1337 | Trecho de Codigo | [C0](https://github.com/nostr-protocol/nips/blob/master/C0.md) |
| 1617 | Patches | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1618 | Pull Requests | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1619 | Atualizacoes de Pull Request | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1621 | Issues | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1984 | Denuncia | [56](https://github.com/nostr-protocol/nips/blob/master/56.md) |
| 1985 | Rotulo | [32](https://github.com/nostr-protocol/nips/blob/master/32.md) |
| 2003 | Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 2004 | Comentario de Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 4550 | Aprovacao de Post da Comunidade | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 5000-5999 | Solicitacao de Trabalho | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 6000-6999 | Resultado de Trabalho | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7000 | Feedback de Trabalho | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7374 | Tokens Reservados de Carteira Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7375 | Tokens de Carteira Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7376 | Historico de Carteira Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 8000 | Adicionar Usuario | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 8001 | Remover Usuario | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 9000-9030 | Eventos de Controle de Grupo | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 9041 | Meta de Zap | [75](https://github.com/nostr-protocol/nips/blob/master/75.md) |
| 9321 | Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 9734 | Solicitacao de Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9735 | Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9802 | Destaques | [84](https://github.com/nostr-protocol/nips/blob/master/84.md) |

## Eventos Substituiveis (10000-19999)

| Kind | Descricao | NIP |
|------|-----------|-----|
| 10000 | Lista de silenciados | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10001 | Lista de fixados | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10002 | Metadados de Lista de Relays | [65](https://github.com/nostr-protocol/nips/blob/master/65.md) |
| 10003 | Lista de favoritos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10004 | Lista de comunidades | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10005 | Lista de chats publicos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10006 | Lista de relays bloqueados | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10007 | Lista de relays de busca | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10009 | Grupos de usuarios | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10012 | Lista de relays favoritos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10013 | Lista de relay de eventos privados | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 10015 | Lista de interesses | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10019 | Recomendacao de Mint Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 10020 | Midia seguida | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10030 | Lista de emojis do usuario | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10050 | Lista de relays para receber DMs | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 10051 | Lista de Relays KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 10063 | Lista de servidores do usuario | Blossom |
| 10166 | Anuncio de Monitor de Relay | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 10312 | Presenca na Sala | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 13194 | Informacoes da Carteira | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 13534 | Listas de Membros | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 17375 | Evento de Carteira Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |

## Autenticacao e Carteira (22000-27999)

| Kind | Descricao | NIP |
|------|-----------|-----|
| 22242 | Autenticacao de Cliente | [42](https://github.com/nostr-protocol/nips/blob/master/42.md) |
| 23194 | Solicitacao de Carteira | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 23195 | Resposta de Carteira | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 24133 | Nostr Connect | [46](https://github.com/nostr-protocol/nips/blob/master/46.md) |
| 24242 | Blobs armazenados em servidores de midia | Blossom |
| 27235 | HTTP Auth | [98](https://github.com/nostr-protocol/nips/blob/master/98.md) |

## Controle de Acesso (28000-29999)

| Kind | Descricao | NIP |
|------|-----------|-----|
| 28934 | Solicitacao de Entrada | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28935 | Solicitacao de Convite | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28936 | Solicitacao de Saida | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |

## Eventos Enderecaveis (30000-39999)

| Kind | Descricao | NIP |
|------|-----------|-----|
| 30000 | Conjuntos de seguidos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30002 | Conjuntos de relays | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30003 | Conjuntos de favoritos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30004 | Conjuntos de curadoria | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30005 | Conjuntos de videos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30007 | Conjuntos de kinds silenciados | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30008 | Distintivos do Perfil | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30009 | Definicao de Distintivo | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30015 | Conjuntos de interesses | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30017 | Criar ou atualizar uma loja | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30018 | Criar ou atualizar um produto | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30019 | UI/UX do Marketplace | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30020 | Produto vendido como leilao | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30023 | Conteudo Longo | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30024 | Rascunho de Conteudo Longo | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30030 | Conjuntos de emojis | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30063 | Conjuntos de artefatos de release | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30078 | Dados Especificos de Aplicacao | [78](https://github.com/nostr-protocol/nips/blob/master/78.md) |
| 30166 | Descoberta de Relay | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 30267 | Conjuntos de curadoria de apps | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30311 | Evento ao Vivo | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30312 | Sala Interativa | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30313 | Evento de Conferencia | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30315 | Status do Usuario | [38](https://github.com/nostr-protocol/nips/blob/master/38.md) |
| 30402 | Anuncio Classificado | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30403 | Rascunho de Anuncio Classificado | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30617 | Anuncios de repositorio | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30618 | Anuncios de estado do repositorio | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30818 | Artigo wiki | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 30819 | Redirecionamentos | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 31234 | Evento de Rascunho | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 31922 | Evento de Calendario Baseado em Data | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31923 | Evento de Calendario Baseado em Horario | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31924 | Calendario | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31925 | RSVP de Evento de Calendario | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31989 | Recomendacao de handler | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 31990 | Informacoes do handler | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 34550 | Definicao de Comunidade | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 38172 | Anuncio de Mint Cashu | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38173 | Anuncio Fedimint | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38383 | Eventos de ordem peer-to-peer | [69](https://github.com/nostr-protocol/nips/blob/master/69.md) |
| 39000-39009 | Eventos de metadados de grupo | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 39089 | Starter packs | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39092 | Starter packs de midia | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39701 | Favoritos da web | [B0](https://github.com/nostr-protocol/nips/blob/master/B0.md) |

*Ultima atualizacao: Dezembro de 2025*

Consulte o [repositorio de NIPs](https://github.com/nostr-protocol/nips) para a fonte oficial.
