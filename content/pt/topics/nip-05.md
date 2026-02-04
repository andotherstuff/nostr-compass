---
title: "NIP-05 (Verificação de Domínio)"
date: 2026-02-04
description: "NIP-05 permite identificadores legíveis por humanos para pubkeys Nostr através de verificação de domínio."
---

NIP-05 mapeia chaves públicas Nostr para identificadores de internet legíveis por humanos como `usuario@exemplo.com`. Isso fornece uma maneira de verificar identidade através de propriedade de domínio sem exigir confiança em uma autoridade central.

## Como Funciona

Um usuário reivindica um identificador adicionando um campo `nip05` aos seus metadados de perfil. O identificador segue o formato `nome@dominio`. Clientes verificam a reivindicação buscando `https://dominio/.well-known/nostr.json` e verificando se o nome mapeia para a pubkey do usuário.

O arquivo JSON no caminho well-known contém um objeto `names` mapeando nomes locais para pubkeys hexadecimais:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Quando a verificação é bem-sucedida, clientes podem exibir o identificador em vez de ou junto com o npub. Alguns clientes mostram uma marca de verificação ou outro indicador para identificadores verificados.

## Dicas de Relay

O arquivo `nostr.json` pode opcionalmente incluir um objeto `relays` mapeando pubkeys para arrays de URLs de relay. Isso ajuda clientes a descobrir onde encontrar eventos de um usuário específico.

## Implementações

A maioria dos principais clientes suporta verificação NIP-05:
- Damus, Amethyst, Primal exibem identificadores verificados
- Muitos serviços de relay oferecem identificadores NIP-05 como recurso
- Existem vários provedores NIP-05 gratuitos e pagos

## Fontes Primárias

- [Especificação NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md)

## Mencionado Em

- [Newsletter #8 (2026-02-04)](/pt/newsletters/2026-02-04-newsletter/) - PR exigindo minúsculas para chaves hex e nomes
