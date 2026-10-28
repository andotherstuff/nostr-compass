---
title: 'Buzz 초안 NIP-RS: 기기 간 읽음 상태 동기화'
date: 2026-10-28
translationOf: /en/topics/nip-rs.md
translationDate: 2026-10-28
draft: false
---

**상태:** 이 문서는 Buzz 프로젝트에 한정된 초안 제안입니다. NIP-RS는 승인된 공식 NIP가 아닙니다. 이 명칭은 Buzz 프로젝트 문서에서 나온 것이며, 공식 NIPs 저장소는 이를 할당하거나 승인하지 않았습니다.

## 목적

NIP-RS를 사용하면 한 사용자의 여러 기기가 그 사용자가 어디까지 읽었는지를 공유할 수 있습니다. 각 설치본은 `kind:30078` addressable event를 게시합니다. 이 event의 `d` tag는 `read-state:` 뒤에 무작위 슬롯 ID가 붙은 값이며, 콘텐츠는 사용자 본인의 키로 NIP-44 암호화됩니다. 평문은 컨텍스트 ID를 타임스탬프 경계(frontier)에 매핑하고, 각 경계는 해당 시각 또는 그 이전의 모든 항목을 읽었다는 뜻입니다. 이 초안은 읽음 확인을 게시하지 않으며, 다른 사람들이 무엇을 읽었는지도 드러내지 않습니다.

## 한계

경계는 최근 활동에 대한 최선 노력(best-effort) 수준의 힌트일 뿐입니다. 읽은 메시지의 완전한 기록을 이루지는 않습니다. 툼스톤 하한(tombstone floor)을 포함한 수동 읽지 않음 재정의는 별도의 영속적 계약을 따릅니다. 전체 재정의 상태를 불러오는 과정은 클라이언트가 완전히 검증할 수 없는 relay의 순서 및 용량 동작에 의존하므로, 임의의 relay가 완전한 읽지 않음 상태를 반환하지 않을 수도 있습니다. 컨텍스트 ID는 대부분 하나의 클라이언트 계열 안에서만 의미를 가집니다.

열려 있는 풀 리퀘스트 #8639는 Buzz 클라이언트를 비공개 인증 HTTP API를 기반으로 하고 기본값으로 비활성화되어 있는 `buzz_v1` NIP-11 기능으로 옮기자고 제안합니다. 그 기능이 없는 relay에서는 NIP-RS가 그대로 유지됩니다.

## 1차 출처

- [Buzz NIP-RS 초안: 기기 간 읽음 상태 동기화(고정 리비전)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-RS.md)
- [Buzz 풀 리퀘스트 #8639: relay 기능을 통한 읽음 상태(열림)](https://github.com/block/buzz/pull/8639)

## 함께 보기

- [NIP-44](/ko/topics/nip-44/)
- [NIP-78](/ko/topics/nip-78/)

**언급된 곳:**

- [뉴스레터 #46: Buzz](/ko/newsletters/2026-10-28-newsletter/#buzz)
