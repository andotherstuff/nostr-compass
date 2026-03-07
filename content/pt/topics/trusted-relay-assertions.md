---
title: Trusted Relay Assertions
date: 2026-01-21
draft: false
categories:
- Protocol
- Relays
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: '2026-03-07'
---

Trusted Relay Assertions é a ideia de publicar avaliações assinadas de terceiros de relays no Nostr para que os clientes possam escolher relays com mais contexto do que apenas metadados auto-relatados. O bloco de construção padronizado atual é [NIP-85: Asserções Confiáveis](/pt/topics/nip-85/), que define como os usuários confiam nos provedores e como os provedores publicam resultados computados assinados.

## Como funciona

A seleção do relay possui três camadas. [NIP-11: Relay Information Document](/pt/topics/nip-11/) cobre o que um relay diz sobre si mesmo. [NIP-66: Relay Discovery and Liveness Monitoring](/pt/topics/nip-66/) cobre o que os observadores podem medir, como disponibilidade e latência. As afirmações confiáveis ​​do relay tentam preencher a lacuna restante: o que um terceiro conclui a partir desses dados e se um cliente decide confiar nessa conclusão.

No modelo NIP-85 mais amplo, os usuários nomeiam provedores confiáveis ​​com eventos kind `10040`, e os provedores publicam eventos de asserção endereçáveis ​​assinados. Uma aplicação de pontuação relay precisaria então de mais duas peças com as quais os clientes concordassem: como um relay é identificado como o sujeito e qual resultado tags representa a pontuação e suas evidências de apoio.

Essa distinção é importante porque a delegação de transporte e confiança são padronizadas, mas o modelo de pontuação específico do relay ainda é um padrão de aplicação. Diferentes provedores podem discordar legitimamente sobre o que torna um relay confiável.

## Modelo de confiança

As pontuações de confiança do relay não são fatos objetivos. Um provedor pode priorizar o tempo de atividade e a taxa de transferência de gravação, outro pode priorizar a jurisdição legal, a política de moderação ou a identidade do operador, e um terceiro pode se preocupar mais com a resistência à vigilância. Um cliente útil deve mostrar quem produziu a partitura, e não apenas a partitura em si.

É aqui também que [Web of Trust](/pt/topics/web-of-trust/) entra em cena. Se um cliente já confia em determinadas pessoas ou serviços, pode preferir avaliações relay provenientes dessa mesma vizinhança social em vez de fingir que existe um único ranking global.

## Por que é importante

Para assinantes remotos [NIP-46](/pt/topics/nip-46/), conexões de carteira ou qualquer aplicativo que sugira relays desconhecido, avaliações relay de terceiros podem reduzir a confiança cega nos padrões. Combinado com listas [NIP-65](/pt/topics/nip-65/) relay, os clientes podem separar "quais relays eu uso" de "quais relays eu confio para esta tarefa".

A principal advertência de correção é o escopo. A cobertura do boletim informativo de janeiro de 2026 descreveu a pontuação de confiança relay como uma proposta dedicada, mas o padrão mesclado no repositório NIPs é o formato mais amplo [NIP-85: Asserções confiáveis](/pt/topics/nip-85/). A pontuação de relay continua sendo um caso de uso construído sobre esse modelo, e não um formato de fio de confiança relay finalizado e separado.

---

**Fontes primárias:**
- [Especificação NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534: Asserções confiáveis](https://github.com/nostr-protocol/nips/pull/1534)

**Mencionado em:**
- [Boletim informativo nº 6: Notícias](/pt/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Boletim informativo nº 6: Atualizações do NIP](/pt/newsletters/2026-01-21-newsletter/#nip-updates)
- [Boletim informativo nº 7: Atualizações do NIP](/pt/newsletters/2026-01-28-newsletter/#nip-updates)

**Veja também:**
- [NIP-11: Documento de Informações do Relay](/pt/topics/nip-11/)
- [NIP-66: Descoberta de relay e monitoramento de atividade](/pt/topics/nip-66/)
- [NIP-85: Asserções confiáveis](/pt/topics/nip-85/)
- [Web of Trust](/pt/topics/web-of-trust/)
