---
title: 'Buzz 초안 NIP-AM: 에이전트 턴 지표'
date: 2026-10-28
translationOf: /en/topics/nip-am.md
translationDate: 2026-10-28
draft: false
---

**상태:** 이 문서는 Buzz 프로젝트 고유의 초안 제안입니다. NIP-AM은 승인된 공식 NIP가 아닙니다. 이 명칭은 Buzz 프로젝트 문서에서 나온 것이며, 공식 NIPs 저장소는 이를 할당하거나 승인하지 않았습니다.

## 목적

NIP-AM은 완료된 AI 에이전트 턴마다 사용량을 기록합니다. 에이전트는 턴마다 `kind:44200` event를 하나씩 게시하며, Buzz 관례에서는 이를 일반적인 추가 전용(append-only) event로 취급합니다. 콘텐츠는 에이전트가 소유자를 수신자로 하여 NIP-44로 암호화합니다. 여기에는 토큰 사용량 수치와 상관관계 ID가 함께 담기며, 비용 값이 있다면 모두 추정치입니다. 대화 기록은 포함되지 않습니다.

## 한계

공개 tag는 소유자와 에이전트를 식별하며, relay는 여전히 event가 언제 게시되는지 볼 수 있습니다. 따라서 이 형식은 활동이 있었다는 사실 자체를 숨기지 않습니다. 사용량 값이 없으면 알 수 없음을 뜻하며, 절대 0으로 계산해서는 안 됩니다.

## 위임된 열람자 제안

아직 열려 있는 문서 풀 리퀘스트 #8582는 소유자가 서명하는 최소 권한 부여(grant)를 제안합니다. 이 제안에 따르면 에이전트는 활성 열람자마다 별도의 암호화된 사본을 게시하고, 각 사본은 정확한 grant event ID에 연결됩니다. 이 풀 리퀘스트는 런타임 권한 부여를 전혀 바꾸지 않습니다. 제안된 grant kind `30180`와 열람자 수 상한은 아직 미결 문제이며, 철회 정책 역시 정해지지 않았습니다. 철회를 통해 relay 기록과 향후 열람을 제한할 수는 있습니다. 하지만 열람자가 이미 받은 사본까지 지울 수는 없습니다.

## 1차 자료

- [Buzz NIP-AM 초안: 에이전트 턴 지표 (고정된 리비전)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-AM.md)
- [Buzz 풀 리퀘스트 #8582: 위임된 지표 열람자 (열린 초안)](https://github.com/block/buzz/pull/8582)

## 함께 보기

- [NIP-44](/ko/topics/nip-44/)

**언급된 곳:**

- [뉴스레터 #46: 위임된 지표 열람자를 위한 NIP-AM 초안 텍스트](/ko/newsletters/2026-10-28-newsletter/#draft-nip-am-text-for-delegated-metric-readers)
- [뉴스레터 #46: Buzz](/ko/newsletters/2026-10-28-newsletter/#buzz)
