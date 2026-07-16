---
title: "ProofMode"
date: 2026-07-15
translationOf: /en/topics/proofmode.md
translationDate: 2026-07-15
draft: false
categories:
  - Media
  - Provenance
---

[ProofMode](https://proofmode.org/) est une boîte à outils open-source de provenance média, construite par Guardian Project, WITNESS et Okthanks, qui attache des données vérifiables d'authenticité et de chaîne de contrôle aux photos et vidéos au moment de la capture. Ce n'est pas spécifique à Nostr ; les clients Nostr qui transportent des données ProofMode intègrent un standard externe existant plutôt qu'une nouvelle couche de protocole.

## Fonctionnement

Le composant Capture de ProofMode intègre les métadonnées de provenance directement dans les fichiers média pendant la capture, prenant en charge les mêmes standards interopérables utilisés par la Content Authenticity Initiative (CAI), les Content Credentials (CR) et C2PA. Un composant Verify séparé inspecte les fichiers audio, image et vidéo pour vérifier ces métadonnées à la recherche de signes de génération par IA ou de modification ultérieure, et un composant Preserve gère le stockage redondant sur le web décentralisé des données de preuve sous-jacentes pour l'archivage à long terme. Un SDK Develop permet aux applications d'intégrer la capture et la vérification sans construire elles-mêmes le format de provenance.

## Pourquoi c'est important

Pour un client Nostr de vidéo ou d'image, transporter des données ProofMode signifie qu'un spectateur dispose d'un moyen externe et multiplateforme de vérifier si un média a été capturé comme annoncé et n'a pas été silencieusement altéré depuis, sans se fier au client de publication ou au relay comme source de confiance. Cette distinction compte le plus pour une copie téléchargée ou réencodée d'un clip : les données de provenance qui survivent au téléchargement et à tout filigrane qu'un client applique sont ce qui rend l'attestation encore vérifiable après que le fichier a quitté l'application qui l'a produit.

## Implémentations

- [Divine](https://github.com/divinevideo/divine-mobile) - client Nostr de vidéo courte ; transporte les données de provenance ProofMode à travers les téléchargements de clips filigranés

---

**Sources primaires :**
- [ProofMode](https://proofmode.org/)

**Mentionné dans :**
- [Bulletin #17](/fr/newsletters/2026-04-29-newsletter/)
- [Bulletin #31 : Divine Mobile 1.0.16 livre un éditeur vidéo plus complet, le chiffrement au repos et la provenance ProofMode](/fr/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**Voir aussi :**
- [Blossom](/fr/topics/blossom/)
