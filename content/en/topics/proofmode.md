---
title: "ProofMode"
date: 2026-07-15
draft: false
categories:
  - Media
  - Provenance
---

[ProofMode](https://proofmode.org/) is an open-source media-provenance toolkit, built by Guardian Project, WITNESS, and Okthanks, that attaches verifiable authenticity and chain-of-custody data to photos and video at the moment of capture. It is not Nostr-specific; Nostr clients that carry ProofMode data are integrating an existing external standard rather than a new protocol layer.

## How It Works

ProofMode's Capture component embeds provenance metadata directly into media files during capture, supporting the same interoperable standards used by the Content Authenticity Initiative (CAI), Content Credentials (CR), and C2PA. A separate Verify component inspects audio, image, and video files to check that metadata for signs of AI generation or later editing, and a Preserve component handles redundant, decentralized-web storage of the underlying proof data for long-term archival. A Develop SDK lets apps integrate capture and verification without building the provenance format themselves.

## Why It Matters

For a Nostr video or image client, carrying ProofMode data means a viewer has an external, cross-platform way to check whether a piece of media was captured as claimed and has not been silently altered since, without relying on the publishing client or relay as the source of trust. That distinction matters most for a downloaded or re-encoded copy of a clip: provenance data that survives the download and any watermarking a client applies is what makes the attestation still checkable after the file leaves the app that produced it.

## Implementations

- [Divine](https://github.com/divinevideo/divine-mobile) - short-video Nostr client; carries ProofMode provenance data through watermarked-clip downloads

---

**Primary sources:**
- [ProofMode](https://proofmode.org/)

**Mentioned in:**
- [Newsletter #17](/en/newsletters/2026-04-29-newsletter/)
- [Newsletter #31: Divine Mobile 1.0.16 ships a deeper video editor, at-rest encryption, and ProofMode provenance](/en/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**See also:**
- [Blossom](/en/topics/blossom/)
