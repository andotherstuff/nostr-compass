---
title: 'NIP-34: Colaboração Git'
date: 2026-02-04
draft: false
description: O NIP-34 permite hospedagem descentralizada de repositórios git e colaboração
  por meio de eventos Nostr.
categories:
- NIP
- Development
translationOf: /en/topics/nip-34.md
translationDate: '2026-03-07'
---

NIP-34 define o evento kinds para hospedar repositórios git, patches e problemas no Nostr relays. Isso permite a colaboração de código totalmente descentralizada sem dependência de plataformas de hospedagem centralizadas como GitHub ou GitLab.

## Como funciona

Os repositórios são representados como eventos endereçáveis ​​(kind 30617) contendo metadados como nome, descrição e URLs clones. O proprietário do repositório publica este evento para estabelecer o projeto no Nostr.

Patches (kind 1617) contêm conteúdo `git format-patch` que pode ser aplicado a um repositório. Os contribuidores enviam patches como eventos que fazem referência ao repositório de destino. Isso reflete o fluxo de trabalho de patch baseado em e-mail usado por projetos como o kernel Linux.

Issues (kind 1621) funcionam como rastreadores de problemas tradicionais. As solicitações pull usam kinds 1618 e 1619, e as atualizações de status usam 1630 a 1633. As respostas a problemas, patches e solicitações pull usam comentários [NIP-22](/pt/topics/nip-22/).

## Tipos de eventos

- **30617** - Anúncio do repositório (endereçável)
- **30618** - Anúncio do estado do repositório para filiais e tags
- **1617** - Envio de patch
- **1618** - Solicitação pull
- **1619** - Atualização da solicitação pull
- **1621** - Emissão
- **1630-1633** - Eventos de status abertos, mesclados/resolvidos, fechados e de rascunho

## Por que é importante

O NIP-34 separa a descoberta do transporte. O repositório real ainda pode residir em servidores Git comuns, mas os eventos Nostr fornecem uma camada distribuída pelo relay para descoberta, discussão, troca de patches e rastreamento de status. Isso significa que um projeto pode continuar usando ferramentas nativas do git sem depender do banco de dados ou API de uma forja.

O `r` tag com o commit exclusivo mais antigo é um dos detalhes mais importantes. Ele oferece aos clientes uma maneira de agrupar espelhos e bifurcações que representam a mesma linhagem de repositório subjacente, o que é difícil de inferir apenas pelos nomes.

## Status de implementação

- **ngit** – Ferramenta de linha de comando para publicar repositórios e patches no Nostr
- **gitworkshop.dev** - Interface da Web para navegar em repositórios hospedados no Nostr
- **Notedeck** - Cliente desktop com [suporte de rascunho para visualização NIP-34](https://github.com/damus-io/notedeck/pull/1279)

---

**Fontes primárias:**

- [Especificação NIP-34](https://github.com/nostr-protocol/nips/blob/master/34.md)

**Mencionado em:**

- [Newsletter #8 (2026-02-04)](/pt/newsletters/2026-02-04-newsletter/) - Notedeck adicionando visualizador NIP-34
- [Boletim informativo nº 9: Notedeck](/pt/newsletters/2026-02-11-newsletter/#notedeck)

**Veja também:**
- [NIP-22: Comentários](/pt/topics/nip-22/)
