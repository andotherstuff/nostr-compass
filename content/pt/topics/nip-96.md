---
title: 'NIP-96: Armazenamento de arquivos HTTP'
date: 2026-02-11
draft: false
categories:
- NIPs
- Media
translationOf: /en/topics/nip-96.md
translationDate: '2026-03-07'
---

O NIP-96 define como os clientes Nostr carregam, baixam e gerenciam arquivos em servidores de mídia HTTP. Agora está marcado como "não recomendado" em favor do Blossom, mas ainda é importante porque os servidores e clientes existentes continuam a apoiá-lo durante a transição.

## Como funciona

Um cliente descobre as capacidades de um servidor de arquivos buscando `/.well-known/nostr/nip96.json`. Esse documento anuncia o URL da API de upload, o URL de download opcional, os tipos de conteúdo suportados, os limites de tamanho e se o servidor suporta transformações de mídia ou hospedagem delegada.

Para fazer upload, o cliente envia um `multipart/form-data` POST para a URL da API com um cabeçalho de autorização [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md). O servidor responde com um objeto de metadados em formato NIP-94 que inclui a URL do arquivo mais tags como `ox` para o hash original e, quando aplicável, `x` para o arquivo transformado que será realmente servido.

Os downloads usam `GET <api_url>/<sha256-hash>` com parâmetros de consulta opcionais, como largura da imagem. A exclusão usa `DELETE` com autenticação NIP-98. Os usuários publicam eventos kind `10096` para declarar seus servidores de upload preferidos.

## Detalhes do modelo de dados

Um detalhe útil é que o NIP-96 identifica os arquivos pelo hash do arquivo original, mesmo quando o servidor transforma o upload. Isso permite que um cliente exclua ou baixe novamente o ativo pelo mesmo identificador estável, enquanto ainda obtém miniaturas geradas pelo servidor ou variantes recompactadas, quando disponíveis.

O conhecido documento também suporta `delegated_to_url`, que permite que um relay aponte clientes para um servidor de armazenamento HTTP separado. Isso evitou que o software relay implementasse a API de mídia completa.

## Por que foi descontinuado

NIP-96 vinculou URLs de arquivos a servidores específicos. Se um servidor caísse, cada nota do Nostr que fizesse referência aos URLs desse servidor perderia sua mídia. Blossom inverte isso tornando o hash SHA-256 do conteúdo do arquivo o identificador canônico. Qualquer servidor Blossom que hospeda o mesmo arquivo o veicula no mesmo caminho de hash, tornando o conteúdo portátil entre servidores por padrão.

Blossom também simplifica a API: PUT simples para uploads, GET para downloads e eventos Nostr assinados (não cabeçalhos HTTP) para autorização. A suspensão de uso ocorreu em setembro de 2025 via [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## Notas de interoperabilidade

Servidores como nostr.build e void.cat suportaram NIP-96 e foram adicionados ou migrados para endpoints Blossom. Os clientes estão em vários estágios: Angor v0.2.5 adicionou configuração de servidor NIP-96 enquanto ZSP v0.3.1 carrega exclusivamente para servidores Blossom. A coexistência continuará até que as implementações restantes do NIP-96 concluam a migração.

Os eventos de preferência do servidor kind 10096 permanecem úteis para a seleção do servidor Blossom. Os metadados do arquivo NIP-94 (eventos kind 1063) descrevem as propriedades do arquivo, independentemente de qual protocolo de upload os criou.

---

**Fontes primárias:**
- [NIP-96: Armazenamento de arquivos HTTP](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Marcar NIP-96 como não recomendado](https://github.com/nostr-protocol/nips/pull/2047)

**Mencionado em:**
- [Boletim informativo nº 9: Aprofundamento do NIP](/pt/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-file-storage-and-the-transition-to-blossom)

**Veja também:**
- [Protocolo Blossom](/pt/topics/blossom/)
- [NIP-94: Metadados do arquivo](/pt/topics/nip-94/)
