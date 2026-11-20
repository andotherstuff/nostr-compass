---
title: "Nostr Archive Standards"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

Nostr Archive Standards (NAS) are independent project specifications for verifiable Parquet archives of Nostr events. They are not an accepted official NIP. A [standards commit](https://gitworkshop.dev/npub1manlnflyzyjhgh970t8mmngrdytcp3jrmaa66u846ggg7t20cgqqvyn9tn/relay.ngit.dev/nas?commit=27c573c52bb8f84159c1d31539c2aa75c2667899) moves the archive declarations to version 2. It also moves the extracted-data collections and catalogs to version 2.

The reference [data extractor](https://gitworkshop.dev/npub1manlnflyzyjhgh970t8mmngrdytcp3jrmaa66u846ggg7t20cgqqvyn9tn/relay.ngit.dev/nas-data-extractor?commit=80204569ebeec233b282abfb3ef851b026f1cc0b) was updated at the same time. It implements the revised declarations for extracted events and the format-v2 identifiers. When designations conflict, it compacts them. The extractor is a local file library and does not run as a relay service. Having reference code shows that the revised format can be implemented. It does not show that other tools have adopted it.

**Primary sources:**
- [NAS standards commit 27c573c](https://gitworkshop.dev/npub1manlnflyzyjhgh970t8mmngrdytcp3jrmaa66u846ggg7t20cgqqvyn9tn/relay.ngit.dev/nas?commit=27c573c52bb8f84159c1d31539c2aa75c2667899)
- [NAS data extractor commit 8020456](https://gitworkshop.dev/npub1manlnflyzyjhgh970t8mmngrdytcp3jrmaa66u846ggg7t20cgqqvyn9tn/relay.ngit.dev/nas-data-extractor?commit=80204569ebeec233b282abfb3ef851b026f1cc0b)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#nostr-archive-standards)

**See also:**
- [NIP-01: Basic protocol](/en/topics/nip-01/)
