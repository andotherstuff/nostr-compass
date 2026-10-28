---
title: "NIP-CD: 슬래시 명령"
date: 2026-10-28
translationOf: /en/topics/nip-cd.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-CD는 슬래시 명령을 정의합니다. 서비스가 명령을 게시하면, 누구나 어떤 Nostr event의 콘텐츠에서든 일반 텍스트로 이를 호출할 수 있습니다. NIP-CD는 선택적 초안 사양입니다. 앞선 제안에 이어 2026년 10월 21일 Commands라는 제목으로 병합되었고, 2026년 10월 27일 선택적 설치된 명령 목록이 병합되면서 Slash Commands로 제목이 바뀌었습니다.

## 작동 방식

kind 31992 event가 명령을 정의합니다. 필수 tag에는 슬래시를 뺀 트리거 단어, 제목, 사용법 설명이 들어갑니다. 순서가 있는 `arg` tag는 위치 인수를 선언하며, 타입으로는 pubkey, event, relay, number, enum, text 등이 있습니다. `s` tag는 kind, relay, 작성자 또는 tag를 기준으로 어떤 event가 명령을 트리거할지 제한합니다. 이 범위는 필터처럼 작동합니다. 같은 타입의 값들은 서로 대안이 되며, 지정된 모든 타입이 일치해야 합니다.

호출은 event 콘텐츠의 인덱스 0에서 시작하는 텍스트로, 예를 들어 `/ban` 뒤에 인수가 오는 형태이며 tag는 전혀 갖지 않습니다. `@nostr:npub1...` 형태의 한정자를 덧붙이면 단일 실행자를 대상으로 지정할 수 있습니다. 한정자가 없으면 트리거가 일치하고 범위에 해당 event가 포함되는 모든 명령이 동작할 수 있습니다. 따라서 메시지 하나가 여러 서비스를 트리거할 수도 있습니다.

클라이언트 지원은 선택 사항입니다. 클라이언트는 자동 완성, 인수 선택기, 렌더링된 칩을 제공할 수 있습니다. 다만 호출을 보내기 위한 전제 조건으로 자체 지원을 요구해서는 안 되며, 파싱에 실패한 텍스트는 일반 콘텐츠로 보내야 합니다.

relay 기반 그룹에서는 정의와 호출이 그룹 relay로 전송됩니다. 브로드캐스트 용도라면 정의는 실행자의 outbox로, 호출은 실행자의 inbox로 전송됩니다.

## 설치된 명령 목록

사용자는 NIP-51을 따르는 선택적 kind 10992 목록을 유지할 수 있습니다. 이 목록에는 `a` tag가 담기며, 각 tag는 실행자 pubkey와 `d` 값으로 kind 31992 명령 정의를 가리키고 선택적으로 relay 힌트를 포함할 수 있습니다. 클라이언트는 자동 완성과 렌더링된 칩에 이 목록을 사용하는 것이 권장됩니다. 이 목록은 사용자의 표시 및 발견 선호를 기록합니다. 실행자에게 권한을 부여하지는 않으며, 일반 텍스트 호출은 이 목록 없이도 작동합니다. 사양의 이 부분은 2026년 10월 27일 PR #2525를 통해 병합되었습니다. 병합 사실만으로는 어떤 클라이언트가 이 목록을 구현했는지 알 수 없습니다.

## 1차 자료

- [NIP-CD 사양](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [2026년 10월 21일 NIP-CD 병합](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [설치된 명령 목록을 위한 PR #2525, 2026년 10월 27일 병합](https://github.com/nostr-protocol/nips/pull/2525)
- [병합 전 PR #2525 브랜치에서 작성된 2026년 10월 26일 커밋](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [2026년 10월 27일 설치된 명령 목록의 NIP-CD 병합](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## 언급된 곳
- [뉴스레터 #46: NIP-CD, 일반 텍스트로 호출하는 명령 정의](/ko/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) 뉴스레터

- [뉴스레터 #46: NIP-CD, 선택적 설치된 명령 목록 추가](/ko/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) 뉴스레터

- [뉴스레터 #46 (2026-10-28): 2026년 10월, 공유 쿼리 의미와 텍스트로 트리거되는 서비스](/ko/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## 함께 보기

- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
