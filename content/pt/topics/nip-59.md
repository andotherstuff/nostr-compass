---
title: 'NIP-59: Gift Wrap'
date: 2025-12-17
draft: false
categories:
- Privacy
- Protocol
translationOf: /en/topics/nip-59.md
translationDate: '2026-03-07'
---

NIP-59 define gift wrap, uma forma de encapsular um evento para que relays e observadores externos não descubram o verdadeiro remetente do evento externo que recebem.

## Estrutura

Um evento gift-wrapped possui três camadas:

1. **Rumor** - O evento alvo sem assinatura.
2. **Selo** (kind `13`) - O boato criptografado para o destinatário e assinado pelo verdadeiro remetente.
3. **Gift Wrap** (kind `1059`) - O selo criptografado novamente e assinado por uma chave única aleatória.

O selo deve conter tags vazio. O gift wrap externo geralmente carrega o destinatário `p` tag para que relays possa roteá-lo.

## O que esconde

A embalagem para presente esconde o remetente de relays e dos observadores da rede porque o evento externo é assinado por uma chave descartável. O destinatário, entretanto, ainda pode descriptografar o selo interno e saber qual chave de longo prazo o assinou. Portanto, o ganho de privacidade é a proteção de metadados na camada de transporte, e não o anonimato do destinatário.

A especificação também recomenda a randomização dos carimbos de data e hora do wrapper e, quando possível, o uso de relays que requer autenticação e serve apenas eventos empacotados ao destinatário pretendido. Sem esses comportamentos relay, os metadados do destinatário ainda podem vazar.

## Notas Operacionais

A embalagem para presente não é um protocolo de mensagens por si só. Outros protocolos, como sistemas de mensagens privadas, utilizam-no como um alicerce.

Os relays podem optar por não armazenar eventos empacotados por muito tempo porque eles não são úteis publicamente. A especificação também permite proof-of-work no wrapper externo quando as implementações desejam resistência extra a spam.

## Casos de uso

- Mensagens diretas privadas (NIP-17)
- Notas apenas para amigos (proposta NIP-FR)
- Notificação push payloads (proposta NIP-9a)
- Qualquer cenário que exija privacidade do remetente na rede

---

**Fontes primárias:**
- [Especificação NIP-59](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Mencionado em:**
- [Boletim informativo nº 8: Aprofundamento do NIP](/pt/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-59-gift-wrap)
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Boletim informativo nº 1: atualizações do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletim informativo nº 15: PRs abertos](/pt/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Veja também:**
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
