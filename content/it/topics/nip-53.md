---
title: "NIP-53: Live Activities"
date: 2026-04-15
translationOf: /en/topics/nip-53.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Live Streaming
---

NIP-53 definisce il formato standard degli eventi per i metadati dei live stream su Nostr. Uno stream viene annunciato come evento addressable kind `30311`, cosi i client possono scoprirlo, mostrarne lo stato corrente e collegare la chat al contesto dello stream.

## Come funziona

Ogni stream usa un evento kind `30311` con un tag `d` come identificatore stabile. L'evento include di solito titolo e riassunto, un tag `streaming` con l'URL di riproduzione e un tag `status` (`planned`, `live` o `ended`). Poiché si tratta di un evento addressable, gli aggiornamenti sostituiscono i metadati precedenti per lo stesso valore `d` invece di creare una cronologia senza limiti.

L'evento puo includere tag tematici (`t`), riferimenti ai partecipanti (`p`) e campi facoltativi per il numero di partecipanti. La live chat usa eventi kind `1311` che fanno riferimento allo stream con un tag `a`, mantenendo i messaggi di chat legati a uno specifico record di live activity.

## Implementazioni

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) pubblica metadati di live stream e chat attorno a trasmissioni live native su Nostr.
- [Zap.stream](https://zap.stream/) usa eventi Nostr per la scoperta degli stream e l'interazione.
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) usa eventi di live chat kind `1311` nel suo contesto di internet radio.
- [Amethyst](https://github.com/vitorpamplona/amethyst) ha collegato gli obiettivi zap di [NIP-75](/it/topics/nip-75/) alla schermata Live Activities tramite [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469): ogni live stream mostra un'intestazione con obiettivo di raccolta, una barra di avanzamento, un pulsante zap con un tocco e una classifica dei top zapper calcolata dalle ricevute zap kind `9735` collegate all'evento kind `30311` dello stream. Le PR successive [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) e [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) aggiungono le proof-of-agreement di NIP-53, gli event builder e una schermata dedicata Live Streams con filtri e strumenti di scoperta.
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) aggiunge lo zapping con un tocco dalle card dei live stream, dove i sats compaiono nell'overlay della chat dello stream tramite NIP-53.

---

**Fonti primarie:**
- [Specifica NIP-53](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - intestazione obiettivo live stream e classifica top zapper
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - proof of agreement NIP-53 ed event builder

**Menzionato in:**
- [Newsletter #18: lancio di WaveFunc](/en/newsletters/2026-04-15-newsletter/)
- [Newsletter #19: obiettivi zap nei live stream di Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/)

**Vedi anche:**
- [NIP-29: Gruppi basati su relay](/it/topics/nip-29/)
- [NIP-75: Zap Goals](/it/topics/nip-75/)
- [NIP-57: Zaps](/it/topics/nip-57/)
- [NIP-C7: Messaggi di chat](/it/topics/nip-c7/)
