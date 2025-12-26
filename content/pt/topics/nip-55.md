---
title: "NIP-55: Aplicativo Assinador Android"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
translationOf: /en/topics/nip-55.md
translationDate: 2025-12-26
---

NIP-55 define como aplicativos Android podem solicitar operações de assinatura de um app assinador dedicado, permitindo que usuários mantenham suas chaves privadas em um local seguro enquanto usam múltiplos clientes Nostr.

## Como Funciona

NIP-55 usa a interface de content provider do Android para expor operações de assinatura. Um app assinador se registra como um content provider, e outros apps Nostr podem solicitar assinaturas sem nunca acessar a chave privada diretamente.

O fluxo:
1. App cliente chama o content provider do assinador
2. Assinador mostra UI de aprovação para o usuário
3. Usuário aprova ou nega a solicitação
4. Assinador retorna a assinatura (ou rejeição) para o cliente

## Operações Principais

- **get_public_key** - Recuperar a chave pública do usuário (chamar uma vez durante conexão inicial)
- **sign_event** - Assinar um evento Nostr
- **nip04_encrypt/decrypt** - Criptografar ou descriptografar mensagens NIP-04
- **nip44_encrypt/decrypt** - Criptografar ou descriptografar mensagens NIP-44

## Iniciação de Conexão

Um erro comum de implementação é chamar `get_public_key` repetidamente de processos em segundo plano. A especificação recomenda chamá-lo apenas uma vez durante a configuração inicial de conexão, e então armazenar o resultado em cache.

---

**Fontes primárias:**
- [Especificação NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mencionado em:**
- [Newsletter #1: Lançamentos](/pt/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: Notícias](/pt/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #2: Atualizações de NIP](/pt/newsletters/2025-12-24-newsletter/#nip-updates)

**Veja também:**
- [NIP-46: Nostr Connect](/pt/topics/nip-46/)
