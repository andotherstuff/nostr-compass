---
title: 'NIP-56: Relatórios'
date: 2026-02-18
draft: false
categories:
- Moderation
- Protocol
translationOf: /en/topics/nip-56.md
translationDate: '2026-03-07'
---

NIP-56 define eventos de relatório kind `1984`. Eles permitem que usuários e aplicativos publiquem sinais de moderação sobre contas, notas e blobs sem exigir uma única autoridade de moderação compartilhada.

## Como funciona

Um relatório deve incluir um `p` tag para o pubkey relatado. Se o relatório for sobre um evento específico, deverá incluir também um `e` tag para esse evento. O tipo de relatório aparece como o terceiro valor no `p`, `e` ou `x` tag relevante.

## Categorias de relatório

- **nudez**: conteúdo adulto
- **malware**: vírus, trojans, ransomware e similares payloads
- **palavrões**: linguagem ofensiva e discurso de ódio
- **ilegal**: conteúdo que pode violar leis
- **spam**: mensagens repetitivas indesejadas
- **falsificação de identidade**: reivindicações de identidade fraudulentas
- **outros**: violações que não se enquadram nas categorias acima

Os relatórios de blob usam `x` tags com o hash de blob e podem incluir um `server` tag apontando para o endpoint de hospedagem. Isso torna o NIP-56 utilizável para moderação de mídia, não apenas para notas e perfis.

## Modelo de segurança e confiança

Os relatórios são sinais, não veredictos. Os clientes podem avaliá-los usando confiança social, listas de moderação ou funções explícitas de moderador. Os relays também podem lê-los, mas as especificações alertam contra a moderação totalmente automática porque os relatórios são fáceis de manipular.

Classificação adicional pode ser adicionada com NIP-32 `l` e `L` tags, o que é útil quando um cliente deseja um vocabulário de moderação mais refinado do que os tipos de relatório de base sete.

---

**Fontes primárias:**
- [Especificação NIP-56](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Mencionado em:**
- [Boletim Informativo nº 10: Atualizações do Projeto](/pt/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-prep)

**Veja também:**
- [NIP-22: Comentário](/pt/topics/nip-22/)
