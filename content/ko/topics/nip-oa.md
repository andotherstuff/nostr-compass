---
title: 'Buzz 초안 NIP-OA: 소유자 증명'
date: 2026-10-28
translationOf: /en/topics/nip-oa.md
translationDate: 2026-10-28
draft: false
---

**상태:** 이 문서는 Buzz 프로젝트에 한정된 초안 제안입니다. NIP-OA는 승인된 공식 NIP가 아닙니다. 이 명칭은 Buzz 프로젝트 문서에서 나온 것이며, 공식 NIPs 저장소는 이를 할당하거나 승인하지 않았습니다.

## 목적

NIP-OA는 소유자 키가 에이전트 키에 event 게시 권한을 부여할 수 있게 하는 선택적 `auth` tag를 정의합니다. event의 작성자는 여전히 에이전트 키입니다. 유효한 tag는 권한 부여의 증거로만 간주되며, 에이전트가 소유자를 사칭할 수 있게 해 주지는 않습니다.

## 메커니즘

소유자는 에이전트 pubkey를 정확한 조건 문자열에 결합하는 도메인 분리 해시에 Schnorr 서명으로 서명합니다. 조건으로 특정 event kind를 요구할 수 있고, 자체 선언된 `created_at`에 범위를 지정할 수도 있습니다. 각 event가 조건을 충족하는 한, 에이전트는 자신의 event에 이 tag를 재사용할 수 있습니다. 검증자는 먼저 핵심 event를 검증한 다음 소유자 서명과 모든 조건을 확인합니다.

## 한계

빈 조건 문자열은 아무런 제약도 추가하지 않습니다. 타임스탬프 조항은 에이전트가 통제하는 필드를 제약하므로 실제 시각 기준의 만료를 제공하지 않습니다. 최신성이 필요하다면 누구든 이를 별도로 확인해야 합니다. tag를 공개적으로 게시하면 소유자 키와 에이전트 키가 서로 연결됩니다.

## 1차 출처

- [Buzz NIP-OA 초안: 소유자 증명(고정 리비전)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-OA.md)

## 함께 보기

- [NIP-01](/ko/topics/nip-01/)

**언급된 곳:**

- [뉴스레터 #46: Buzz](/ko/newsletters/2026-10-28-newsletter/#buzz)
