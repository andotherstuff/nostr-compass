---
title: "NIP-34 (Colaboração Git)"
date: 2026-02-04
description: "NIP-34 permite hospedagem descentralizada de repositórios git e colaboração através de eventos Nostr."
---

NIP-34 define kinds de evento para hospedar repositórios git, patches e issues em relays Nostr. Isso permite colaboração de código totalmente descentralizada sem dependência de plataformas de hospedagem centralizadas como GitHub ou GitLab.

## Como Funciona

Repositórios são representados como eventos endereçáveis (kind 30617) contendo metadados como nome, descrição e URLs de clone. O proprietário do repositório publica este evento para estabelecer o projeto no Nostr.

Patches (kind 1617) contêm conteúdo de patch git que pode ser aplicado a um repositório. Contribuidores enviam patches como eventos referenciando o repositório alvo. Isso espelha o fluxo de trabalho baseado em email usado por projetos como o kernel Linux.

Issues (kind 1621) funcionam como rastreadores de issues tradicionais. Elas referenciam um repositório e contêm um título e descrição. Comentários em issues e patches usam eventos de resposta padrão.

## Kinds de Evento

- **30617** - Anúncio de repositório (endereçável)
- **1617** - Envio de patch
- **1621** - Issue
- **1622** - Status de issue (aberta/fechada)

## Implementações

- **ngit** - Ferramenta de linha de comando para publicar repos e patches no Nostr
- **gitworkshop.dev** - Interface web para navegar repositórios hospedados no Nostr
- **Notedeck** - Cliente desktop com [suporte draft para visualização NIP-34](https://github.com/damus-io/notedeck/pull/1279)

## Fontes Primárias

- [Especificação NIP-34](https://github.com/nostr-protocol/nips/blob/master/34.md)

## Mencionado Em

- [Newsletter #8 (2026-02-04)](/pt/newsletters/2026-02-04-newsletter/) - Notedeck adicionando visualizador NIP-34
