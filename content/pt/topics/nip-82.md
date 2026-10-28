---
title: "NIP-82 proposta (não atribuída): Catálogo de Aplicativos de Software"
date: 2026-06-17
lastmod: 2026-10-28
translationOf: /en/topics/nip-82.md
translationDate: 2026-10-28
draft: false
categories:
  - Proposals
  - Apps
---

O catálogo de aplicativos de software descrito nesta página é uma proposta em análise. Não se trata de uma NIP aceita. Ela está no [pull request #2526 de nostr-protocol/nips](https://github.com/nostr-protocol/nips/pull/2526), intitulado "Zapstore spec". Na data da última atualização desta página, esse pull request está aberto e não mesclado, e a branch master oficial de NIPs não contém nenhum arquivo `82.md`. "NIP-82" é o rótulo que a própria proposta usa para si. Não é um número oficial de NIP. Kinds de event, tags e comportamento podem mudar antes de qualquer merge. Segundo o pull request, ele substitui o [pull request #1336](https://github.com/nostr-protocol/nips/pull/1336), anterior.

## Kinds de event propostos

O rascunho divide um catálogo de software em vários kinds de event:

- **Kind 32267, aplicativo:** um event endereçável que descreve um app.
- **Kind 30063, lançamento:** um event endereçável para uma versão desse app. Ele referencia os assets dessa versão.
- **Kind 3063, asset:** um event regular que descreve um arquivo para download.
- **Kind 30267, curadoria:** uma lista endereçável que um curador publica para agrupar ou recomendar apps.
- **Kind 30509, vínculo de certificado de assinatura:** um event endereçável que vincula um certificado X.509, como um certificado de assinatura de APK, à chave Nostr que publica o software, para que os clientes saibam quais certificados esse publicador controla. Sua tag `d` é o hash SHA-256 do certificado codificado em DER. Ele contém uma assinatura feita com a chave privada do certificado e uma expiração na forma de timestamp Unix, e pode, opcionalmente, marcar o vínculo como revogado.
- **Kind 10067, lista de relays:** uma lista substituível de relays onde os events do catálogo podem ser encontrados.

## Plataforma, integridade e validade

Os events de asset trazem identificadores de plataforma e de runtime, de modo que um cliente pode exibir apenas os arquivos compatíveis com um dispositivo. Cada asset também traz um hash do arquivo. Com ele, um cliente pode verificar se os bytes baixados correspondem ao que o publicador assinou. No caso de pacotes Android, o rascunho inclui a impressão digital do certificado de assinatura. Antes de oferecer uma atualização, um instalador pode compará-la com o certificado de um app já instalado. Antes de instalar um pacote Android, os clientes DEVERIAM (SHOULD) buscar o event kind 30509 pelo hash do certificado. Eles deveriam verificar a assinatura de certificado desse event em relação ao certificado embutido no APK e ao publicador do asset, além de conferir se a prova não expirou nem foi revogada.

## Limites de confiança

Uma assinatura válida mostra apenas que uma determinada chave publicou um event. Ela não prova que a chave pertence ao desenvolvedor real, que o software é seguro nem que a lista de um curador é confiável. A proposta não oferece nenhuma garantia sobre publicadores arbitrários. Cabe aos clientes e usuários decidir em quais chaves de publicadores e curadores confiar. Esta página não alega nenhuma auditoria de segurança nem interoperabilidade em produção.

## Relação com a NIP-89

Os events de handler da [NIP-89](/pt/topics/nip-89/) anunciam quais aplicativos conseguem lidar com quais kinds de event. Já esta proposta descreve os artefatos de software e onde obtê-los; assim, as duas tratam de questões distintas.

---

**Fontes primárias:**
- [PR #2526 de nostr-protocol/nips: Zapstore spec](https://github.com/nostr-protocol/nips/pull/2526) (aberto, não mesclado; substitui o [PR #1336](https://github.com/nostr-protocol/nips/pull/1336))

**Mencionado em:**
- [Newsletter #27: cobertura do lançamento do Amethyst v1.12.0 (referência histórica)](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #46: catálogo de aplicativos de software proposto como NIP-82](/pt/newsletters/2026-10-28-newsletter/#software-application-catalog-proposed-as-nip-82)

**Veja também:**
- [NIP-89: Manipuladores de Aplicativos](/pt/topics/nip-89/)
