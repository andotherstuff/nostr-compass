---
title: "Cordn"
date: 2026-11-04
draft: false
categories:
  - Protocol
---

Cordn is a coordinator-assisted [MLS](/en/topics/mls/) messaging protocol that runs over [ContextVM](/en/topics/contextvm/) and Nostr, developed in the [Cordn repository](https://github.com/Cordn-msg/cordn). It is a separate project from Concord despite the similar name. Users can publish a last-resort KeyPackage on one or more coordinators so that others can invite them.

## Coordinator claims across devices

A user's devices share an encrypted meta document that carries the last-resort KeyPackage and the set of coordinators where it is currently published. [PR #12](https://github.com/Cordn-msg/cordn/pull/12), merged on October 30, changes that set from an accumulating union to a current publish claim. Adopting a peer's set replaces local claims, including retractions, so linked devices stop resurrecting removed coordinator relationships.

An absent `coordinators` field marks a legacy or unknown entry and MUST NOT be read as a retraction. An explicit empty array means the package is published nowhere. For a full unpublish, the device keeps the same KeyPackage entry with an empty claim set. When a newer entry carries claims, it is an explicit rotation and supersedes the old one, while a plain unpublished mint does not displace the current invite surface.

Until its own publish lands, a device with an unpublished local retraction or rotation defers adopting an older peer claim set. Each retraction is the previous explicit claim set minus the new one, not a mutable local marker.

Coordinators that are unreachable may still hold an orphaned remote copy. Retraction does not prove that copy was deleted, and automatic resolution MUST NOT re-adopt it. An explicit re-add can reconcile it later. Clients MAY pair an adopted retraction with retiring automatic coverage, which is local policy.

The change is merged protocol text and does not correspond to a client release.

---

**Primary sources:**
- [Cordn repository](https://github.com/Cordn-msg/cordn)
- [Cordn PR #12](https://github.com/Cordn-msg/cordn/pull/12) - Coordinator claim sets that converge across devices

**Mentioned in:**
- [Newsletter #47: Cordn makes coordinator retractions converge across devices](/en/newsletters/2026-11-04-newsletter/#cordn-makes-coordinator-retractions-converge-across-devices)

**See also:**
- [MLS (Message Layer Security)](/en/topics/mls/)
- [ContextVM](/en/topics/contextvm/)
