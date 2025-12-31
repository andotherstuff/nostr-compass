---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2025-12-31
draft: false
categories:
  - Carteira
  - Ecash
---

NIP-60 define como as carteiras de ecash baseadas em Cashu operam dentro do Nostr. As informações da carteira são armazenadas em relays, permitindo carteiras portáteis que funcionam em diferentes aplicações sem exigir contas separadas.

## Como Funciona

NIP-60 usa três tipos de eventos armazenados em relays:

**Evento de Carteira (kind 17375):** Um evento substituível contendo a configuração criptografada da carteira, incluindo URLs de mint e uma chave privada para receber pagamentos. Esta chave é separada da chave de identidade Nostr do usuário.

**Eventos de Token (kind 7375):** Armazenam provas Cashu não gastas e criptografadas. Quando as provas são gastas, o cliente exclui o evento antigo e cria um novo com as provas restantes.

**Histórico de Gastos (kind 7376):** Registros opcionais de transações mostrando movimentações de fundos, com conteúdo criptografado e referências a eventos de tokens criados/destruídos.

## Características Principais

- **Facilidade de uso** - Novos usuários podem receber ecash imediatamente sem configuração de conta externa
- **Interoperabilidade** - Os dados da carteira acompanham os usuários em diferentes aplicações Nostr
- **Privacidade** - Todos os dados da carteira são criptografados com as chaves do usuário
- **Gerenciamento de provas** - Rastreia quais eventos de token foram gastos para evitar gasto duplo

## Fluxo de Trabalho

1. O cliente obtém a configuração da carteira dos relays
2. Os eventos de token são carregados e descriptografados para obter os fundos disponíveis
3. Gastar cria novos eventos de token e exclui os antigos
4. Eventos de histórico opcionais registram transações para referência do usuário

---

**Fontes primárias:**
- [Especificação NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mencionado em:**
- [Boletim #3: Resumo de Dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-57: Zaps](/pt/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
