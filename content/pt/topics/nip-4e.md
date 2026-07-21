---
title: "NIP-4E: Desacoplamento da criptografia da identidade"
date: 2026-07-15
draft: false
translationOf: /en/topics/nip-4e.md
translationDate: 2026-07-15
categories:
  - NIP
  - Protocol
  - Encryption
---

NIP-4E é um rascunho aberto, proposto por fiatjaf, para compartilhar dados privados entre os próprios dispositivos de um usuário sem que cada dispositivo precise ter a chave de identidade principal de Nostr do usuário. A proposta permanece sem merge e com status `draft`/`optional`.

## O problema que aborda

Muitos NIPs existentes, incluindo listas NIP-51 e carteiras Cashu NIP-60, criptografam dados do usuário para si mesmo usando a chave de identidade para poder lê-los de volta em qualquer dispositivo. Isso falha quando a chave de identidade não está diretamente acessível, por exemplo quando um assinante remoto está protegido por fragmentos de limiar FROST, MuSig2 ou um enclave seguro hospedado, já que criptografar e descriptografar requer então uma ida e volta a esse assinante toda vez. Também torna a criptografia offline impossível quando a chave de assinatura reside em um bunker remoto.

## Como funciona

NIP-4E separa uma "chave de cliente" por dispositivo de uma "chave de criptografia" compartilhada que não é a chave de identidade do usuário:

1. O primeiro cliente que um usuário configura gera um par de chaves de criptografia aleatório e anuncia sua metade pública em um evento `kind:10044` assinado pela chave de identidade do usuário.
2. Qualquer outro cliente que queira criptografar ou descriptografar dados para esse usuário calcula seu segredo compartilhado Diffie-Hellman contra a chave de criptografia anunciada em vez da chave de identidade.
3. Quando um segundo dispositivo instala um novo cliente, esse cliente gera sua própria "chave de cliente" local e publica um anúncio `kind:4454` (também assinado pela chave de identidade do usuário) pedindo ao primeiro cliente que compartilhe a chave de criptografia com ele.
4. O cliente original detecta o novo anúncio `kind:4454`, criptografa a chave de criptografia compartilhada para a chave do novo cliente usando [NIP-44](/pt/topics/nip-44/), e a publica para que o novo cliente possa descriptografá-la e usá-la dali em diante.

O resultado é que criptografia e descriptografia nunca requerem consultar o assinante de chave de identidade uma vez que um cliente tem a chave de criptografia compartilhada localmente, e uma configuração de assinante remoto (FROST, MuSig2, enclave hospedado) pode ser usada para identidade enquanto a criptografia comum permanece rápida e funciona offline.

## Por que importa

NIP-4E é citado como a base para outras propostas que precisam de uma chave simétrica por drive ou por conta sem depender de um assinante remoto para cada chamada de criptografia/descriptografia, incluindo uma proposta de drive criptografado privado ([PR #2412](https://github.com/nostr-protocol/nips/pull/2412)) e uma versão mais estreita da mesma ideia específica para NIP-17 ([PR #2361](https://github.com/nostr-protocol/nips/pull/2361)). Ambas permanecem abertas junto com NIP-4E, fazendo deste um área ativa e sem resolução do protocolo em vez de um bloco de construção finalizado.

---

**Fontes primárias:**
- [Rascunho NIP-4E, PR #1647](https://github.com/nostr-protocol/nips/pull/1647)

**Mencionado em:**
- [Newsletter #31: Aberta: drive criptografado privado que estende NIP-4E](/pt/newsletters/2026-07-15-newsletter/#open-private-encrypted-drive-extends-nip-4e)

**Veja também:**
- [NIP-44: Encrypted Payloads](/pt/topics/nip-44/)
- [NIP-17: Private Direct Messages](/pt/topics/nip-17/)
- [NIP-46: Nostr Connect](/pt/topics/nip-46/)
- [FROST](/pt/topics/frost/)
