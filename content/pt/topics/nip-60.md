---
title: 'NIP-60: Carteira Cashu'
date: 2025-12-31
draft: false
categories:
- Wallet
- Ecash
translationOf: /en/topics/nip-60.md
translationDate: '2026-03-07'
---

O NIP-60 define como as carteiras ecash baseadas em Cashu operam dentro do Nostr. As informações da carteira são armazenadas nos relays, permitindo carteiras portáteis que funcionam em diferentes aplicativos sem a necessidade de contas separadas.

## Como funciona

O NIP-60 usa três tipos de eventos principais armazenados nos relays, além de um evento auxiliar opcional para cotações pendentes:

**Evento de carteira (kind 17375):** Um evento substituível contendo configuração de carteira criptografada, incluindo URLs mint e uma chave privada para recebimento de pagamentos. Essa chave é separada da chave de identidade Nostr do usuário.

**Eventos de token (kind 7375):** Armazene Cashu proofs criptografado e não gasto. Quando os proofs são gastos, o cliente exclui o evento antigo e cria um novo com os proofs restantes.

**Histórico de gastos (kind 7376):** Registros de transações opcionais mostrando movimentos de fundos, com conteúdo criptografado e referências a eventos de token criados/destruídos.

**Eventos de cotação (kind 7374):** Estado criptografado opcional para cotações pendentes do mint. A especificação recomenda eventos de curta duração com expiração tags, principalmente para casos onde o estado local não é suficiente.

## Modelo de Estado

O NIP-60 trata da sincronização do estado da carteira, não do ato de receber dinheiro. O evento de carteira informa ao cliente qual mints e chave de carteira usar, enquanto os eventos de token são o estado de saldo real porque contêm o proofs não gasto.

Essa distinção é importante para a interoperabilidade. Dois clientes podem mostrar a mesma carteira apenas se interpretarem o rollover de token da mesma maneira: gastar proofs, publicar proofs de substituição e excluir o evento de token gasto por meio de [NIP-09](/pt/topics/nip-09/) para que outros clientes não continuem contando proofs gasto como saldo.

## Por que é importante

- **Facilidade de uso** - Novos usuários podem receber ecash imediatamente sem configuração de conta externa
- **Interoperabilidade** - Os dados da carteira acompanham os usuários em diferentes aplicativos Nostr
- **Privacidade** - Todos os dados da carteira são criptografados com as chaves do usuário
- **Gerenciamento de provas** - Rastreia as transições de estado da carteira para que os clientes possam convergir para o mesmo saldo

## Notas de interoperabilidade

Os clientes primeiro procuram informações da carteira relay por meio de kind 10019 e recorrem ao [NIP-65](/pt/topics/nip-65/) lista de relays do usuário se nenhuma carteira dedicada lista de relays estiver presente. Esse substituto é útil, mas também significa que a portabilidade da carteira ainda depende dos relays realmente armazenar e servir os eventos criptografados da carteira.

A especificação também exige que a chave privada da carteira permaneça separada da chave de identidade Nostr do usuário. Isso mantém o processamento de recibos de carteira isolado da chave de assinatura principal e reduz a chance de uma chave ser reutilizada para duas finalidades diferentes.

## Fluxo de trabalho

1. O cliente busca a configuração da carteira da carteira relays ou da lista de relays do usuário
2. Os eventos de token são carregados e descriptografados para obter os fundos disponíveis
3. Os gastos criam novos eventos simbólicos e excluem os antigos
4. Eventos de histórico opcionais registram transações para referência do usuário

---

**Fontes primárias:**
- [Especificação NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mencionado em:**
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletim informativo nº 9: Aprofundamento do NIP](/pt/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)

**Veja também:**
- [NIP-57: Zaps](/pt/topics/nip-57/)
- [NIP-09: Solicitação de exclusão de evento](/pt/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
