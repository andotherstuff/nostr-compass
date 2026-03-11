---
title: 'NIP-62: Solicitações de desaparecimento'
date: 2026-01-13
draft: false
categories:
- Privacy
- Protocol
translationOf: /en/topics/nip-62.md
translationDate: 2026-03-11
---

O NIP-62 define solicitações de desaparecimento, um mecanismo para os usuários solicitarem que relays exclua seu conteúdo. Embora aos relays não seja obrigada a honrar essas solicitações, o suporte ao NIP-62 dá aos usuários mais controle sobre seus dados publicados e fornece uma maneira padronizada de sinalizar a intenção de exclusão em toda a rede.

## Como funciona

Uma solicitação de desaparecimento é um evento kind 62 assinado pelo usuário que deseja que seu conteúdo seja removido. A solicitação pode ter como alvo eventos específicos incluindo seus IDs em `e` tags, ou pode solicitar a exclusão de todo o conteúdo desse pubkey omitindo totalmente `e` tags.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removing old posts",
  "sig": "sig1234..."
}
```

O campo `content` contém opcionalmente um motivo legível para a solicitação de exclusão. As dicas de relay em `e` tags informam aos relays onde os eventos originais foram publicados, embora relays possa honrar solicitações independentemente de elas terem os eventos especificados.

## Comportamento do relay

Os relays que suportam NIP-62 devem excluir os eventos especificados de seu armazenamento e parar de servi-los aos assinantes. A própria solicitação de desaparecimento pode ser retida como um registro de que a exclusão foi solicitada, o que ajuda a evitar que eventos excluídos sejam reimportados de outro relays.

Quando uma solicitação de desaparecimento omite todos os `e` tags, relays interpreta isso como uma solicitação para remover todos os eventos desse pubkey. Esta é uma ação mais drástica e relays pode lidar com isso de forma diferente, por exemplo, marcando pubkey como "desaparecido" e recusando-se a aceitar ou servir qualquer um de seus eventos daqui para frente.

Os relays não são necessários para suportar NIP-62. A rede Nostr é descentralizada e cada operador relay decide as suas próprias políticas de retenção de dados. Os usuários não devem presumir que seu conteúdo será excluído de todos os lugares simplesmente porque publicaram uma solicitação de desaparecimento.

## Por que é importante

O NIP-62 oferece aos clientes e operadores relay um sinal de exclusão compartilhado que vai além de APIs de moderação ad hoc ou painéis específicos do relay. Um usuário pode publicar uma solicitação assinada e deixar que cada relay decida como processá-la.

O limite prático é o escopo. Uma solicitação de desaparecimento afeta apenas relays que a vê, apoia e escolhe honrá-la. Não retira capturas de tela, bancos de dados locais, arquivos de terceiros ou cópias republicadas já fora do controle do relay.

## Considerações sobre privacidade

As solicitações de desaparecimento são um mecanismo de exclusão de melhor esforço, não uma garantia de privacidade. Mesmo após a publicação de uma solicitação de desaparecimento, cópias do conteúdo podem existir em outros lugares da rede, inclusive em outros relays que não suportam NIP-62, em caches locais em dispositivos clientes, em arquivos ou mecanismos de pesquisa de terceiros e em backups.

A solicitação em si também é um evento Nostr assinado, o que significa que se torna parte do seu registro público. Qualquer pessoa que veja a solicitação de desaparecimento sabe que você excluiu algo, mesmo que não consiga ver o que foi excluído.

Para conteúdo que deve permanecer privado, considere usar mensagens criptografadas como [NIP-17](/pt/topics/nip-17/) em vez de confiar na exclusão após o fato.

## Notas de interoperabilidade

NIP-62 complementa [NIP-09](/pt/topics/nip-09/). NIP-09 é o evento de solicitação de exclusão geral usado em todo o Nostr, enquanto NIP-62 fornece ao relays um sinal orientado a desaparecimento mais forte que pode cobrir eventos específicos ou todo o conjunto de conteúdo do pubkey. As implementações podem suportar ambos, e os back-ends de banco de dados do ferrugem-nostr agora expõem a configuração em torno desse limite de aplicação.

---

**Fontes primárias:**
- [Especificação NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Mencionado em:**
- [Boletim informativo nº 5: Mudanças notáveis no código](/pt/newsletters/2026-01-13-newsletter/#rust-nostr-library)
- [Boletim informativo nº 10: ferrugem-nostr](/pt/newsletters/2026-03-04-newsletter/#rust-nostr-nip-62-request-to-vanish)

**Veja também:**
- [NIP-09: Solicitação de exclusão de evento](/pt/topics/nip-09/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
