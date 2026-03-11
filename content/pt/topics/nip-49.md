---
title: 'NIP-49: Criptografia de Chave Privada'
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

O NIP-49 define como um cliente pode criptografar a chave privada de um usuário com uma senha e codificar o resultado como uma string `ncryptsec`. O objetivo é oferecer portabilidade com padrões mais fortes do que armazenar um `nsec` bruto, mantendo a chave criptografada fácil de mover entre clientes.

## Como funciona

O cliente começa com a chave privada secp256k1 bruta de 32 bytes, não com uma string hex ou bech32. Ele deriva uma chave simétrica temporária da senha do usuário com scrypt, usando um salt aleatório por chave e um fator de trabalho ajustável armazenado como `LOG_N`. Em seguida, criptografa a chave privada com XChaCha20-Poly1305, adiciona metadados de versionamento e de manuseio da chave, e codifica o resultado em bech32 sob o prefixo `ncryptsec`.

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

O evento acima é um contêiner de exemplo, não um requisito do NIP-49. O NIP-49 padroniza o formato da chave criptografada em si, não um kind de evento dedicado para publicá-la. Clientes podem armazenar um `ncryptsec` localmente, sincronizá-lo por armazenamento específico de app ou apresentá-lo como exportação de backup.

## Modelo de segurança

O NIP-49 faz duas coisas ao mesmo tempo. Ele transforma a senha do usuário em uma chave de criptografia apropriada e desacelera tentativas de recuperação por força bruta com um KDF memory-hard. O fator de trabalho importa. Valores mais altos de `LOG_N` tornam a descriptografia mais lenta para usuários legítimos, mas também elevam o custo de tentativas offline para atacantes.

O formato também carrega um flag de um byte descrevendo se a chave já foi tratada de forma insegura antes da criptografia. Isso não muda o ciphertext em si, mas dá aos clientes uma forma de distinguir um backup protegido recém-gerado de uma chave que já foi colada em plaintext antes de ser encapsulada.

## Notas de implementação

- Senhas são normalizadas para Unicode NFKC antes da derivação da chave, para que a mesma senha possa ser inserida de forma consistente entre clientes.
- XChaCha20-Poly1305 usa um nonce de 24 bytes e criptografia autenticada, então adulterações no ciphertext falham de forma limpa durante a descriptografia.
- A chave simétrica deve ser zerada e descartada após o uso.
- A especificação não recomenda publicar chaves criptografadas em relays públicos, porque coletar muitas chaves criptografadas melhora a posição de cracking offline de um atacante.

## Implementações

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Adiciona compatibilidade de cadastro usando chaves privadas criptografadas com NIP-49

---

**Fontes primárias:**
- [Especificação do NIP-49](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Fluxo de cadastro no cliente usando NIP-49

**Mencionado em:**
- [Newsletter #13: Formstr](/pt/newsletters/2026-03-11-newsletter/)
- [Newsletter #13: Aprofundamento NIP](/pt/newsletters/2026-03-11-newsletter/)

**Veja também:**
- [NIP-46: Nostr Connect](/pt/topics/nip-46/)
- [NIP-55: Aplicativo Assinador para Android](/pt/topics/nip-55/)
