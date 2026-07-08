---
title: "Keycast: Assinatura Remota Nostr em Equipe"
date: 2026-05-21
draft: false
translationOf: /en/topics/keycast.md
translationDate: 2026-07-01
categories:
  - Signing
  - Security
  - Teams
---

Keycast é um servidor de assinatura remota NIP-46 auto-hospedado construído para equipes. Ele armazena chaves privadas Nostr criptografadas em repouso no SQLite, gera strings de conexão bunker NIP-46 e executa processos de assinatura (signer) que aprovam ou negam solicitações de assinatura remota de acordo com políticas configuráveis por chave. O projeto é mantido pela organização Marmot Protocol.

## Como funciona

O servidor possui quatro componentes principais: uma API em Axum que gerencia equipes e autenticação HTTP NIP-98, um frontend web em SvelteKit que usa NIP-07 para autenticação, um gerenciador de signer que observa as linhas de autorização e cria um `signer_daemon` por autorização, e um banco de dados SQLite com migrações.

Os membros da equipe fazem login por meio de sua extensão de navegador NIP-07. O app web solicita um evento de autenticação HTTP NIP-98 assinado localmente pela extensão, e então envia esse cabeçalho de autenticação para a API. A API verifica o evento, extrai a pubkey e checa a associação à equipe. As chaves armazenadas são criptografadas com um arquivo raiz `master.key` que deve ser montado separadamente da imagem e nunca comitado.

O daemon signer descriptografa a chave armazenada e a chave bunker na inicialização, conecta-se aos relays configurados e chama `Authorization::validate_policy` antes de aprovar cada solicitação de assinatura NIP-46. As políticas especificam quais kinds de evento uma determinada conexão bunker está autorizada a assinar.

## Auditoria de Segurança (maio de 2026)

Uma auditoria de segurança concluída em maio de 2026 tratou de questões de autenticação, permissão, integridade de dados e dependências. Principais mudanças:

- A autenticação NIP-98 agora exige exatamente uma tag `u` e uma tag `method`, rejeita timestamps obsoletos ou futuros e valida os hashes do `payload` do corpo da requisição
- `ALLOWED_PUBKEYS` é parseado de forma exata e aplicado no servidor; o frontend expõe `/api/config?pubkey=<hex>` para que o navegador possa verificar o status da lista permitida sem receber a lista completa do servidor
- Políticas vazias negam por padrão as requisições de assinatura, criptografia e descriptografia; a criação de políticas rejeita configurações de permissão desconhecidas ou malformadas
- As conexões SQLite habilitam a aplicação de chaves estrangeiras; a exclusão de equipe não perde mais dados de junção de permissão antes da limpeza
- A proteção de rotas no lado do servidor agora cobre rotas de app aninhadas, como `/teams/:id`
- Respostas web definem cabeçalhos CSP, frame, content-type, referrer, permissions e HSTS
- Uma migração SQL normaliza o antigo JSON de permissão de kinds permitidos, de `{"sign":[...]}` para `{"allowed_kinds":[...]}`, na inicialização

A auditoria observa itens residuais em [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) antes de confiar chaves reais de equipe ao deploy.

## Deploy

O deploy via Docker Compose monta `master.key` nos containers da API e do signer, executa os containers como um UID/GID não-root com sistema de arquivos raiz somente-leitura, e usa labels do Caddy para rotear `/api/*` para a API e tudo mais para o app web. A imagem publicada em `ghcr.io/marmot-protocol/keycast` é marcada com `master`, `latest` e `sha-<commit>`.

---

**Fontes primárias:**
- [Repositório do Keycast](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - Resultados da auditoria de segurança de maio de 2026

**Mencionado em:**
- [Newsletter #23: Auditoria de Segurança do Keycast Concluída](/pt/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**Veja também:**
- [NIP-46: Assinatura Remota Nostr](/pt/topics/nip-46/)
- [NIP-07: Signer via Extensão de Navegador](/pt/topics/nip-07/)
- [Protocolo Marmot](/pt/topics/marmot/)
