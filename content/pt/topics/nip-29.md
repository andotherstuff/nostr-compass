---
title: "NIP-29: Grupos Baseados em Relay"
date: 2025-12-24
draft: false
categories:
  - Social
  - Groups
translationOf: /en/topics/nip-29.md
translationDate: 2025-12-26
---

NIP-29 define grupos baseados em relay, onde um relay gerencia membresia do grupo, permissões e visibilidade de mensagens.

## Tags de Acesso ao Grupo

- **private**: Apenas membros podem ler mensagens do grupo
- **closed**: Solicitações de entrada são ignoradas (apenas por convite)
- **hidden**: O relay esconde metadados do grupo de não-membros, tornando o grupo não descobrível
- **restricted**: Apenas membros podem escrever mensagens para o grupo

Essas tags podem ser combinadas. Um grupo pode ser `restricted` (escrita limitada) mas não `hidden` (ainda descobrível). Omitir uma tag habilita o comportamento oposto: sem `private` significa que qualquer um pode ler, sem `closed` significa que solicitações de entrada são atendidas.

## Como Funciona

O relay é a autoridade para operações de grupo:
- Mantém lista de membros e papéis
- Aplica permissões de escrita
- Controla o que não-membros podem ver

Clientes enviam mensagens de grupo para o relay, que valida a membresia antes de aceitá-las.

## Considerações de Privacidade

- Grupos `hidden` fornecem a proteção mais forte de descoberta: eles não aparecem em buscas ou listagens de relay
- Grupos `private` escondem conteúdo de mensagens de não-membros
- Grupos `closed` simplesmente ignoram solicitações de entrada; combine com `private` ou `hidden` para controle de acesso mais forte
- `restricted` controla quem pode escrever, independente do acesso de leitura

---

**Fontes primárias:**
- [Especificação NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)

**Mencionado em:**
- [Newsletter #2: Atualizações de NIP](/pt/newsletters/2025-12-24-newsletter/#nip-updates)
