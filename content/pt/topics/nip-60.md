---
title: 'NIP-60: Carteira Cashu'
date: 2025-12-31
draft: false
categories:
  - Wallet
  - Ecash
translationOf: /en/topics/nip-60.md
translationDate: 2026-04-22
---

NIP-60 define como carteiras de ecash baseadas em Cashu operam dentro do Nostr. Informações da carteira são armazenadas em relays, habilitando carteiras portáveis que funcionam em diferentes aplicações sem exigir contas separadas.

## Como funciona

A NIP-60 usa três tipos centrais de evento armazenados em relays, mais um evento auxiliar opcional para quotes pendentes:

**Wallet Event, kind 17375:** um evento replaceable contendo configuração de carteira criptografada, incluindo URLs de mints e uma chave privada para receber pagamentos. Essa chave é separada da chave de identidade Nostr do usuário.

**Token Events, kind 7375:** armazenam proofs Cashu não gastas, criptografadas. Quando proofs são gastas, o cliente apaga o evento antigo e cria um novo com as proofs restantes, se houver.

**Spending History, kind 7376:** registros opcionais de transação mostrando movimentações de fundos, com conteúdo criptografado e referências a token events criados e destruídos.

**Quote Events, kind 7374:** estado criptografado opcional para mint quotes pendentes. A spec recomenda eventos de curta duração com tags de expiração, principalmente para casos em que o estado local não basta.

## Modelo de estado

A NIP-60 trata de sincronização do estado da carteira, não do ato de receber dinheiro em si. O wallet event diz a um cliente quais mints e qual chave de carteira usar, enquanto token events são o estado real do saldo porque contêm as proofs não gastas.

Essa distinção importa para interoperabilidade. Dois clientes só conseguem mostrar a mesma carteira se interpretarem rollover de tokens do mesmo jeito: gastar proofs, publicar proofs de substituição e apagar o token event gasto via [NIP-09](/pt/topics/nip-09/) para que outros clientes não continuem contando proofs gastas como saldo.

## Por que importa

- **Facilidade de uso** - novos usuários podem receber ecash imediatamente sem setup de conta externa
- **Interoperabilidade** - dados da carteira acompanham o usuário entre diferentes aplicações Nostr
- **Privacidade** - todos os dados da carteira são criptografados para as chaves do usuário
- **Gerenciamento de proofs** - acompanha transições de estado da carteira para que clientes converjam para o mesmo saldo

## Notas de interoperabilidade

Clientes primeiro procuram informações de relay da carteira por meio do kind 10019 e fazem fallback para a lista de relays do usuário na [NIP-65](/pt/topics/nip-65/) se não houver uma lista dedicada de wallet relays. Esse fallback é útil, mas também significa que a portabilidade da carteira ainda depende de relays realmente armazenarem e servirem os eventos criptografados da carteira.

A spec também exige que a chave privada da carteira permaneça separada da chave de identidade Nostr do usuário. Isso mantém o recebimento da carteira isolado da chave principal de assinatura e reduz a chance de uma mesma chave ser reutilizada para dois propósitos diferentes.

## Fluxo de trabalho

1. O cliente busca a configuração da carteira em wallet relays ou na lista de relays do usuário
2. Token events são carregados e descriptografados para obter fundos disponíveis
3. Gastos criam novos token events e apagam os antigos
4. Eventos opcionais de histórico registram transações para referência do usuário

---

**Fontes primárias:**
- [Especificação NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mencionado em:**
- [Newsletter #3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #11: NIP Deep Dive](/pt/newsletters/2026-02-25-newsletter/)
- [Newsletter #13: Shopstr e Milk Market abrem superfícies de comércio MCP](/en/newsletters/2026-03-11-newsletter/)

**Veja também:**
- [NIP-57: Zaps](/pt/topics/nip-57/)
- [NIP-09: Request de exclusão de evento](/pt/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
