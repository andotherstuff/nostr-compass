---
title: "NIP-49: Criptografia de Chave Privada"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 define como um cliente pode criptografar a chave privada de um usuário com uma senha e codificar o resultado como uma string `ncryptsec`. O objetivo é portabilidade com padrões mais seguros do que armazenar um `nsec` bruto, enquanto mantém a chave criptografada fácil de mover entre clientes.

## Como Funciona

O cliente começa com a chave privada secp256k1 bruta de 32 bytes, não uma string hex ou bech32. Ele deriva uma chave simétrica temporária da senha do usuário com scrypt, usando um salt aleatório por chave e um fator de trabalho ajustável armazenado como `LOG_N`. Então criptografa a chave privada com XChaCha20-Poly1305, anexa metadados de versionamento e tratamento de chave, e codifica o resultado em bech32 sob o prefixo `ncryptsec`.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

O evento acima é um container de exemplo, não um requisito do NIP-49. NIP-49 padroniza o formato da chave criptografada em si, não um kind de evento dedicado para publicá-lo. Clientes podem armazenar um `ncryptsec` localmente, sincronizá-lo através de armazenamento específico do app, ou apresentá-lo como exportação de backup.

## Modelo de Segurança

NIP-49 faz duas coisas ao mesmo tempo. Transforma uma senha de usuário em uma chave de criptografia adequada, e desacelera tentativas de recuperação por força bruta com uma KDF memory-hard. O fator de trabalho importa. Valores maiores de `LOG_N` tornam a descriptografia mais lenta para usuários legítimos, mas também aumentam o custo de adivinhação offline para atacantes.

O formato também carrega um flag de um byte descrevendo se a chave já foi manipulada de forma insegura antes da criptografia. Isso não muda o ciphertext em si, mas dá aos clientes uma forma de distinguir um backup protegido recém-gerado de uma chave que já foi copiada em texto plano antes de ser encapsulada.

## Notas de Implementação

- Senhas são normalizadas para Unicode NFKC antes da derivação de chave para que a mesma senha possa ser inserida consistentemente entre clientes.
- XChaCha20-Poly1305 usa um nonce de 24 bytes e criptografia autenticada, então adulteração do ciphertext falha de forma limpa durante a descriptografia.
- A chave simétrica deve ser zerada e descartada após uso.
- A spec não recomenda publicar chaves criptografadas em relays públicos, porque coletar muitas chaves criptografadas melhora a posição de cracking offline de um atacante.

## Implementações

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Adiciona compatibilidade de cadastro usando chaves privadas criptografadas com NIP-49

---

**Fontes primárias:**
- [Especificação NIP-49](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Fluxo de cadastro do lado do cliente usando NIP-49

**Mencionado em:**
- [Newsletter #13: Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**Veja também:**
- [NIP-46: Nostr Connect](/pt/topics/nip-46/)
- [NIP-55: Android Signer Application](/pt/topics/nip-55/)
