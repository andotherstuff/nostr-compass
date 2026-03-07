---
title: 'NIP-89: Manipuladores de aplicativos recomendados'
date: 2026-01-07
draft: false
categories:
- Discovery
- Clients
- Protocol
translationOf: /en/topics/nip-89.md
translationDate: '2026-03-07'
---

O NIP-89 define como os aplicativos podem anunciar seus recursos e como os usuários podem recomendar aplicativos que lidam com eventos específicos kinds.

## Tipos de eventos

- **kind 31990** - Manipulador de aplicativos (publicado por desenvolvedores de aplicativos)
- **kind 31989** - Recomendação de aplicativo (publicada pelos usuários)

## Como funciona

1. **Aplicativos** publicam eventos do manipulador descrevendo qual evento kinds eles suportam e como abrir o conteúdo
2. **Usuários** recomendam aplicativos que usam para eventos específicos kinds
3. **Clientes** consultam recomendações para oferecer a funcionalidade "abrir em..." para tipos de eventos desconhecidos

## Manipulador de aplicativos

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

O `k` tags especifica o evento suportado kinds. Os modelos de URL usam `<bech32>` como espaço reservado para entidades codificadas NIP-19.

O mesmo evento de manipulador pode anunciar vários kinds suportados se eles compartilharem o mesmo padrão de roteamento. Isso mantém a descoberta de aplicativos compacta e evita a publicação de um evento de manipulador por kind quando a lógica de destino é idêntica.

## Recomendação do usuário

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

O `d` tag é o evento kind recomendado. Vários `a` tags podem recomendar aplicativos diferentes para plataformas diferentes.

## Etiqueta do cliente

O NIP-89 também define um `client` tag opcional que os aplicativos de publicação podem anexar a eventos comuns. Ele registra o nome do cliente mais um ponteiro para o evento do manipulador, o que permite que outros clientes mostrem de onde veio uma nota ou procurem metadados de aplicativo mais ricos.

Isso tem implicações de privacidade. A especificação diz explicitamente que os clientes devem permitir que os usuários optem pela exclusão, porque a publicação da identidade do software em cada evento pode revelar padrões de uso que as pessoas podem não querer expor.

## Casos de uso

- Descobrindo aplicativos que podem exibir artigos longos (kind 30023)
- Encontrar clientes que suportam tipos de eventos específicos
- Funcionalidade "abrir em..." entre clientes
- Detecção de recursos do cliente para suporte de criptografia

## Notas de confiança e segurança

O NIP-89 melhora a interoperabilidade, mas também cria uma superfície de redirecionamento. Se um cliente consultar anúncios arbitrários de manipuladores de relays não confiáveis, ele pode acabar enviando os usuários para aplicativos maliciosos ou enganosos.

É por isso que o fluxo de recomendação começa com as pessoas que você segue. As recomendações filtradas socialmente não são perfeitas, mas são mais seguras do que tratar todos os manipuladores publicados como igualmente confiáveis.

---

**Fontes primárias:**
- [Especificação NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Mencionado em:**
- [Boletim informativo nº 4: Aprofundamento do NIP](/pt/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Boletim Informativo #12: Damus](/pt/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**Veja também:**
- [NIP-19: Entidades codificadas em Bech32](/pt/topics/nip-19/)
