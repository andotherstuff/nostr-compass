---
title: "NIP-90"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 define Data Vending Machines (DVMs), um protocolo de marketplace para solicitar e pagar por trabalho computacional no Nostr.

## Como Funciona

Clientes publicam eventos de requisição de trabalho (kinds 5000 a 5999) especificando o trabalho necessário. Provedores de serviço monitoram por requisições correspondendo suas capacidades e publicam resultados após completar a computação. Pagamento acontece através de Lightning ou outros mecanismos negociados no fluxo do trabalho.

Kinds de trabalho definem diferentes tipos de computação: geração de texto, geração de imagem, tradução, descoberta de conteúdo e mais. Cada kind especifica o formato de entrada e saída esperado.

## Recursos Principais

- Marketplace de computação descentralizado
- Sistema de tipo de trabalho baseado em kind
- Competição de provedor em preço e qualidade
- Extensível para novos tipos de computação

---

**Fontes primárias:**
- [Especificação NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mencionado em:**
- [Newsletter #11: NIP-AC Coordenação de Agente DVM](/pt/newsletters/2026-02-25-newsletter/#atualizações-de-nips)

**Veja também:**
- [NIP-85: Trusted Assertions](/pt/topics/nip-85/)
