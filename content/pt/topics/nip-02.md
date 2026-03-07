---
title: 'NIP-02: Seguir Lista'
date: 2025-12-24
draft: false
categories:
- Protocol
- Social
translationOf: /en/topics/nip-02.md
translationDate: '2026-03-07'
---

NIP-02 define eventos kind 3, que armazenam a lista de seguidores de um usuário. Este evento é a entrada básica para feeds iniciais, notificações de resposta e muitas estratégias de seleção de relays.

## Como funciona

Um evento kind 3 contém `p` tags listagem seguida de pubkeys:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Cada `p` tag tem quatro posições: o nome tag, o pubkey seguido (hex), uma dica de URL relay opcional e um "petname" opcional (um apelido local). A dica relay informa aos outros clientes onde encontrar os eventos daquele usuário. O petname permite atribuir nomes memoráveis ​​aos contatos sem depender de seus nomes de exibição autodeclarados.

## Comportamento substituível

O kind 3 está no intervalo substituível (0, 3, 10000-19999), então relays mantém apenas a versão mais recente por pubkey. Quando você segue alguém novo, seu cliente publica um novo kind 3 completo contendo todos os seus seguidores mais o novo. Isso significa que as listas a seguir devem ser completadas todas as vezes; você não pode publicar atualizações incrementais.

## Por que é importante

Para construir um feed inicial, os clientes buscam o kind 3 do usuário, extraem todos os `p` tag pubkeys e, em seguida, assinam os eventos kind 1 desses autores:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

O relay retorna notas correspondentes e o cliente as renderiza. O dicas de relay no kind 3 ajuda os clientes a saber quais relays consultar para cada usuário seguido.

Este evento é também onde o estado social obsoleto aparece primeiro. Se o kind 3 mais recente de um usuário estiver faltando nos relays que você consulta, o feed dele pode parecer vazio, mesmo que seus seguidores ainda existam em outro lugar. Os clientes que mesclam resultados de vários relays geralmente se recuperam melhor do que os clientes que confiam em um único relay.

## Nomes de animais de estimação e identidade

O campo petname permite um esquema de nomenclatura descentralizado. Em vez de confiar no nome que um usuário afirma em seu perfil, você pode atribuir seu próprio rótulo. Um cliente pode exibir "alice (My Sister)", onde "alice" vem de seu perfil kind 0 e "My Sister" é seu nome de animal de estimação. Isso fornece um contexto que os nomes de usuários globais não conseguem.

## Notas de interoperabilidade

Como os eventos kind 3 são substituíveis e devem ser concluídos, os clientes devem preservar o tags desconhecido durante a atualização. Se outro cliente adicionasse tags que seu cliente não entende, a substituição cega perderia esses dados.

O mesmo cuidado se aplica a dicas de relay e nomes de animais de estimação. Eles são campos opcionais, mas descartá-los durante a gravação pode piorar silenciosamente a experiência de outro cliente. Um caminho de atualização seguro é: carregar o kind 3 mais recente conhecido, modificar apenas o tags que você entende, manter o restante e republicar o evento completo.

---

**Fontes primárias:**
- [Especificação NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Mencionado em:**
- [Boletim informativo nº 2: Aprofundamento do NIP](/pt/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
- [NIP-10: Threading de notas de texto](/pt/topics/nip-10/)
- [NIP-65: Metadados da Lista de Relays](/pt/topics/nip-65/)
