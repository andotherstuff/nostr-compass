---
title: "NAP-FS: Virtual filesystem access"
date: 2026-10-21
draft: false
categories:
  - Protocols
---

NAP-FS is a proposed Napplet interface that gives napplets shell-mediated access to a runtime-owned virtual filesystem under `window.napplet.fs`. Host paths stay hidden. Access comes from runtime policy bound to the napplet's identity and from files the user picks. Every caller-supplied path still needs runtime authorization. The proposal is open and unmerged as napplet/naps PR #88 and is a non-NIP interface. Myco merged a picker-only subset for reading and writing entries the user selected. Directory operations and watching fall outside that subset. Myco caps each read or write at 1 MiB. Per window, it allows 4 MiB in flight and 64 files. Its replace offers non-atomic semantics, and `ifRevision` and past-end writes are unsupported operations.

## Primary sources

- [napplet/naps PR #88: NAP-FS proposal](https://github.com/napplet/naps/pull/88)
- [NAP-FS draft at commit bd1b9e9](https://github.com/napplet/naps/blob/bd1b9e912f05203bf38f7a1b04f920744fe6d625/naps/NAP-FS.md)
- [Origami74/myco PR #158: NAP-FS picker subset](https://github.com/Origami74/myco/pull/158)

## Mentioned in

- [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#myco)
