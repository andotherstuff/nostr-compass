---
title: "NIP-96: Armazenamento de Arquivos HTTP"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 definiu como aplicações Nostr fazem upload, download e gerenciam arquivos em servidores de mídia HTTP. Agora marcado como "não recomendado" em favor do Blossom, o NIP-96 permanece relevante enquanto projetos navegam a transição entre os dois padrões de mídia.

## Como Funciona

A aplicação descobre as capacidades de servidor de arquivos buscando `/.well-known/nostr/nip96.json`, que retorna a URL da API, tipos de conteúdo suportados, limites de tamanho e transformações de mídia disponíveis.

O upload consiste em POST `multipart/form-data` à URL da API com header de autorização NIP-98 (evento Nostr assinado provando a identidade de quem faz o upload). O servidor retorna estrutura de metadados de arquivo NIP-94 contendo a URL do arquivo, hashes SHA-256, tipo MIME e dimensões.

Downloads usam requisições GET a `<api_url>/<sha256-hash>`, com parâmetros de query opcionais em transformações do lado do servidor como redimensionamento de imagem. Exclusão usa DELETE com auth NIP-98. Usuários publicam eventos kind 10096 declarando seus servidores de upload preferidos.

## Por Que Foi Depreciado

NIP-96 vinculava URLs de arquivo a servidores específicos. Se servidor caísse, toda nota Nostr referenciando aquelas URLs perdia sua mídia. Blossom inverte isso tornando o hash SHA-256 do conteúdo do arquivo o identificador canônico. Qualquer servidor Blossom hospedando o mesmo arquivo o serve no mesmo caminho de hash, tornando conteúdo portável entre servidores por padrão.

Blossom simplifica a API: PUT simples em uploads, GET em downloads, e eventos Nostr assinados (não headers HTTP) na autorização. A depreciação aconteceu em setembro de 2025 via [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## A Transição

Servidores como nostr.build e void.cat suportavam NIP-96 e adicionaram ou migraram a endpoints Blossom. As aplicações estão em vários estágios: Angor v0.2.5 adicionou configuração de servidor NIP-96, enquanto ZSP v0.3.1 faz upload exclusivamente a servidores Blossom. A coexistência continuará até que as implementações NIP-96 restantes completem a migração.

Eventos de preferência de servidor kind 10096 continuam úteis na seleção de servidor Blossom. Metadados de arquivo NIP-94 (eventos kind 1063) descrevem propriedades de arquivo independente de qual protocolo de upload os criou.

---

**Fontes primárias:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Mencionado em:**
- [Newsletter #9: Deep Dive de NIP](/pt/newsletters/2026-02-11-newsletter/#deep-dive-de-nip-nip-96-armazenamento-de-arquivos-http-e-a-transição-ao-blossom)

**Veja também:**
- [Protocolo Blossom](/pt/topics/blossom/)
- [NIP-94: Metadados de Arquivo](/pt/topics/nip-94/)
