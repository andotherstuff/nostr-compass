---
title: "NIP-03: event에 대한 OpenTimestamps 증명"
date: 2026-10-28
translationOf: /en/topics/nip-03.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-03은 Nostr event에 대한 [OpenTimestamps](https://opentimestamps.org/) 증명을 게시하는 방법을 설명합니다. 이 증명은 해당 event가 특정 Bitcoin 블록 시점까지 존재했다는 증거입니다.

**경고:** 현재 사양에는 `draft`, `optional`, `unrecommended` 라벨이 붙어 있습니다. 사양의 헤더에는 이 사양이 특정한 공격 하나에 취약하며 업데이트가 필요하다고 적혀 있습니다. 그 공격이 무엇인지는 본문에 설명되어 있지 않습니다. 이 형식은 역사적 참고 자료로만 다루고, 사양이 개정될 때까지 새 작업에는 채택하지 마십시오.

## 작동 방식

증명은 별도의 kind 1040 event로 게시됩니다. 이 event의 `e` tag는 relay URL과 함께 대상 event id를 지정하고, `k` tag는 대상 event의 kind를 기록합니다. OpenTimestamps 증명은 대상 event id 자체를 다이제스트로 삼아 증명해야 합니다. id를 다시 해시하지는 않습니다.

`content`에는 base64로 인코딩된 전체 `.ots` 파일이 담기며, 여기에는 Bitcoin 어테스테이션(attestation)이 하나 이상 포함됩니다. 사양은 어테스테이션을 정확히 하나만 넣고 대기 중인(pending) 어테스테이션은 넣지 않을 것을 권장합니다. 대기 중인 어테스테이션은 검증에 도움이 되지 않으면서 바이트만 늘리기 때문입니다.

검증자는 kind 1040 event를 가져와 content를 디코딩한 뒤 Bitcoin을 기준으로 증명을 확인합니다. 유효한 증명은 어테스테이션이 가리키는 블록 시점까지 해당 event id가 커밋되었음을 보여 줍니다. 이를 통해 작성자가 직접 기록한 `created_at` 값에 의존하지 않는, event 생성 시각의 상한이 정해집니다. 다만 event 내용이 참이라는 것까지 보여 주지는 않습니다.

## 역사

[2023년 10월 11일 커밋](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)으로 증명이 위치하는 곳이 바뀌었습니다. 그 이전에는 증명이 event 자체에 붙는 `ots` 필드였습니다. 이 커밋 이후로는 각 증명이 대상을 가리키는 별도의 kind 1040 event가 되었습니다.

## 1차 자료

- [현재 NIP-03 사양](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [증명을 kind 1040 event로 옮긴 2023년 10월 11일 커밋](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## 뉴스레터 언급

- [뉴스레터 #46 (2026-10-28): 2023년 10월, event가 증거와 작업 요청을 담습니다](/ko/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## 함께 보기

- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
