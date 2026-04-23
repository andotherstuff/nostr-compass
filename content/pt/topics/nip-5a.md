---
title: 'NIP-5A: Sites estáticos'
date: 2026-04-01
draft: false
categories:
  - Protocol
  - Hosting
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-22
---

NIP-5A define como hospedar sites estáticos sob keypairs Nostr. Autores de sites publicam eventos de manifesto assinados que mapeiam paths de URL para hashes SHA256 de conteúdo, e servidores host resolvem esses manifestos para servir os arquivos do site a partir de armazenamento Blossom.

## Como funciona

A spec usa dois kinds de evento. O kind `15128` é um manifesto de site raiz, um por pubkey, que serve como website padrão daquela chave. O kind `35128` é um manifesto de site nomeado, identificado por uma tag `d`, que funciona como um subdomínio. Cada manifesto contém tags `path` mapeando paths absolutos de URL para hashes SHA256 dos arquivos que devem ser servidos.

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

Um servidor host recebe um request HTTP, extrai a pubkey do autor a partir do subdomínio, busca o manifesto do site na lista de relays do autor, resolve o path solicitado para um hash de conteúdo e baixa o blob correspondente do ou dos servidores Blossom listados nas tags `server`.

## Resolução de URL

Sites raiz usam o npub como subdomínio. Sites nomeados usam uma codificação base36 de 50 caracteres da pubkey bruta seguida do valor da tag `d`, tudo em um único rótulo DNS. Como rótulos DNS são limitados a 63 caracteres e a pubkey em base36 sempre ocupa 50, identificadores de sites nomeados ficam limitados a 13 caracteres.

## Implementações

- [nsite](https://github.com/lez/nsite) - servidor host que resolve manifestos NIP-5A e serve arquivos
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - UI para construir e publicar manifestos de site

---

**Fontes primárias:**
- [Especificação NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - proposta original e merge
- [nsite](https://github.com/lez/nsite) - implementação de referência do host
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - UI de publicação e gerenciamento

**Mencionado em:**
- [Newsletter #16: merge da NIP-5A](/pt/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/pt/newsletters/2026-04-01-newsletter/)
- [Newsletter #19: proposta de applets NIP-5D](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [Blossom](/pt/topics/blossom/)
- [NIP-65: Metadados de lista de relays](/pt/topics/nip-65/)
- [NIP-96: HTTP File Storage](/pt/topics/nip-96/)
