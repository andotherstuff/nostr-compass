---
title: 'BUD-03: Lista de servidores de usuários'
date: 2025-12-17
draft: false
categories:
- Media
- Protocol
translationOf: /en/topics/bud-03.md
translationDate: '2026-03-07'
---

BUD-03 define como um usuário publica seus servidores Blossom preferidos, para que os clientes saibam onde fazer upload de blobs e onde procurar quando um URL de mídia parar de funcionar.

## Como funciona

Os usuários publicam um evento kind `10063` substituível por um ou mais `server` tags. Cada tag contém uma URL completa do servidor Blossom.

Os clientes podem então:
- fazer upload de blobs para os servidores preferidos do usuário
- descubra prováveis ​​locações de blob no pubkey do autor
- tente novamente a recuperação dos servidores listados quando um URL mais antigo for quebrado

## Detalhes úteis para o leitor

A ordem de `server` tags é importante. A especificação diz que os usuários devem listar primeiro seus servidores mais confiáveis ​​ou confiáveis, e os clientes devem pelo menos tentar o primeiro servidor para uploads. Isso significa que o BUD-03 não é apenas um diretório, é também um sinal de preferência fraco.

A orientação de recuperação também é prática: quando um cliente extrai um hash de blob de uma URL, ele deve usar a última string hexadecimal de 64 caracteres no caminho. Isso ajuda os clientes a recuperar blobs de URLs Blossom padrão e URLs de estilo CDN não padrão que ainda incorporam o hash.

---

**Fontes primárias:**
- [Especificação BUD-03](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Repositório Blossom](https://github.com/hzrd149/blossom)

**Mencionado em:**
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)

**Veja também:**
- [Protocolo Blossom](/pt/topics/blossom/)
- [NIP-51: Listas](/pt/topics/nip-51/)
