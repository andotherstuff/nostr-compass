---
title: "NIP-36 : Contenu sensible"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-36.md
translationDate: 2026-10-15
---

NIP-36 définit un tag `content-warning` facultatif, accompagné d’un motif lui aussi facultatif. Les clients peuvent l’utiliser pour masquer un event jusqu’à ce que le lecteur choisisse de l’afficher. L’event reste public.

## Implémentations

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) analyse le tag et son motif. [Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) utilise le paramètre du lecteur relatif au contenu sensible et propose une action permettant d’afficher le contenu. [noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) vérifie les préférences relatives aux avertissements et si le contenu est déjà déplié avant de présenter l’avertissement.

---

**Sources primaires :**
- [Spécification NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md)

**Mentionné dans :**
- [Newsletter #44 : Avertissements de contenu avant affichage](/fr/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**Voir aussi :**
- [NIP-32 : Étiquetage](/fr/topics/nip-32/)
