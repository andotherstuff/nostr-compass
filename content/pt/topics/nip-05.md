---
title: 'NIP-05: Verificação de Domínio'
date: 2026-02-04
draft: false
description: NIP-05 permite identificadores legíveis para Nostr pubkeys por meio de
  verificação de domínio.
categories:
- Identity
- Discovery
translationOf: /en/topics/nip-05.md
translationDate: 2026-03-11
---

O NIP-05 mapeia as chaves públicas Nostr para identificadores de Internet legíveis por humanos, como `user@example.com`. Ele fornece aos usuários uma dica de identidade baseada em DNS que os clientes podem verificar por HTTPS.

## Como funciona

Um usuário reivindica um identificador adicionando um campo `nip05` aos metadados de seu perfil. O identificador segue o formato `name@domain`. Os clientes verificam a reivindicação buscando `https://domain/.well-known/nostr.json` e verificando se o nome está mapeado para pubkey do usuário.

O arquivo JSON no caminho conhecido contém um objeto `names` mapeando nomes locais para hexadecimal pubkeys:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Quando a verificação for bem-sucedida, os clientes poderão exibir o identificador em vez ou junto com o npub. Alguns clientes mostram um indicador de verificação, enquanto outros mostram o identificador como texto simples e deixam as decisões de confiança para o leitor.

## Modelo de confiança

NIP-05 não é um registro global de nomes de usuário. Isso prova o controle de um nome de domínio e do caminho do servidor web, e não da identidade legal ou da continuidade da conta a longo prazo. Se um proprietário de domínio alterar o mapeamento posteriormente, os clientes verificarão o novo mapeamento, a menos que mantenham o estado anterior.

Isso torna o NIP-05 útil para descoberta e reputação, mas é mais fraco do que os usuários costumam supor. Um bom cliente deve tratá-lo como controle de domínio verificado, e não como proof de que uma pessoa ou organização é quem afirma ser.

## Dicas de relay

O arquivo `nostr.json` pode incluir opcionalmente um mapeamento de objeto `relays` pubkeys para matrizes de URLs relay. Isso ajuda os clientes a descobrir onde encontrar eventos de um usuário específico.

## Notas de interoperabilidade

O requisito de letras minúsculas é mais importante do que parece. Nomes mistos ou pubkeys podem funcionar em uma implementação e falhar em outra, portanto, os clientes atuais devem esperar nomes e chaves hexadecimais em minúsculas em `nostr.json`.

Outro detalhe prático é o nome especial `_`, que permite que um domínio mapeie a forma de identificador simples como `_@example.com` ou apenas `example.com` em clientes que o suportam. Nem todo cliente expõe esse formulário da mesma maneira, então os usuários ainda obtêm resultados mais consistentes com identificadores `name@domain` explícitos.

## Status de implementação

A maioria dos principais clientes oferece suporte à verificação NIP-05:
- Damus, Ametista, Primal exibem identificadores verificados
- Muitos serviços relay oferecem identificadores NIP-05 como recurso
- Existem vários provedores NIP-05 gratuitos e pagos

---

**Fontes primárias:**
- [Especificação NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [PR #2208](https://github.com/nostr-protocol/nips/pull/2208) - requisito de letras minúsculas para nomes e chaves hexadecimais

**Mencionado em:**
- [Boletim informativo nº 8: Atualizações do NIP](/pt/newsletters/2026-02-04-newsletter/#nip-updates)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
- [NIP-65: Metadados da Lista de Relays](/pt/topics/nip-65/)
