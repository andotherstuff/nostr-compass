---
title: "NIP-C7: Messaggi di chat"
date: 2026-04-15
translationOf: /en/topics/nip-c7.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
---

NIP-C7 definisce il kind `9` come kind di evento dedicato ai messaggi di chat. L'obiettivo è separare il traffico orientato alla chat dal traffico dei feed social generali, cosi i client possono applicare regole UX e di moderazione diverse a ciascun contesto.

## Come funziona

Un evento kind `9` trasporta il contenuto del messaggio più i tag che identificano il contesto della chat. Nei gruppi basati su relay di [NIP-29](/it/topics/nip-29/), l'evento include un tag `h` con l'ID del gruppo. Il threading delle risposte usa tag `q` che fanno riferimento a eventi precedenti.

NIP-C7 si concentra su dove questi eventi devono essere mostrati. Invece di comparire nei feed globali delle note come gli eventi kind `1`, gli eventi kind `9` sono pensati per viste orientate alla chat, dove lo stato della conversazione e il threading sono espliciti.

## Implementazioni

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) e [Coracle](https://github.com/coracle-social/coracle) usano il kind `9` nei flussi di lavoro delle chat di gruppo.
- [Amethyst](https://github.com/vitorpamplona/amethyst) include il supporto al kind `9` nel proprio stack di messaggistica.
- [White Noise](https://github.com/marmot-protocol/whitenoise) usa il threading delle risposte di NIP-C7 con tag `q`.

---

**Fonti primarie:**
- [Specifica NIP-C7](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310: Restrict kind 9 to chat views](https://github.com/nostr-protocol/nips/pull/2310)

**Menzionato in:**
- [Newsletter #18: NIP Updates](/en/newsletters/2026-04-15-newsletter/)

**Vedi anche:**
- [NIP-29: Gruppi basati su relay](/it/topics/nip-29/)
- [NIP-17: Messaggi diretti privati](/it/topics/nip-17/)
