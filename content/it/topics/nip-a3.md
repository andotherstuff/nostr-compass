---
title: "NIP-A3: Destinazioni di pagamento"
date: 2026-09-09
translationOf: /en/topics/nip-a3.md
translationDate: 2026-09-11
draft: false
categories:
  - Protocol
  - Payments
---

NIP-A3 definisce un metodo portabile con cui un account Nostr può pubblicare indirizzi di pagamento per più reti e servizi. Un evento sostituibile di kind `10133` contiene uno o più tag `payto`.

## Come funziona

Ogni tag ha la forma `["payto", "<type>", "<address>"]`. Il tipo è in minuscolo, come `bitcoin`, `lightning` o `monero`. I client possono convalidare i formati noti e generare un URI di pagamento nativo, laddove ne esista uno; per i tipi sconosciuti viene usato come ripiego lo schema URI `payto:` definito nella RFC 8905.

L'evento dichiara le destinazioni, non un pagamento completato né uno zap Nostr. I client decidono comunque quali tipi di pagamento supportare, come convalidare un indirizzo e con quanta chiarezza mostrare la destinazione prima di passarla a un wallet.

## Implementazioni

- [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041) offre, su richiesta, il passaggio del pagamento quando riconosce una destinazione compatibile.
- [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) associa i tipi di destinazione consentiti agli URI di pagamento.
- [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) convalida le destinazioni Monero e interroga i relay dell'autore.

---

**Fonti primarie:**
- [Specifica NIP-A3](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905: lo schema URI payto](https://www.rfc-editor.org/rfc/rfc8905.html)

**Menzionato in:**
- [Newsletter n. 39: le destinazioni di pagamento NIP-A3 arrivano su tre client](/it/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**Vedi anche:**
- [NIP-47: Nostr Wallet Connect](/it/topics/nip-47/)
