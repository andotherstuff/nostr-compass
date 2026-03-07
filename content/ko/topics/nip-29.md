---
title: "NIP-29: 릴레이 기반 그룹"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-03-07
draft: false
categories:
  - Social
  - Groups
---
NIP-29는 릴레이가 그룹 멤버십, 권한 및 메시지 가시성을 관리하는 릴레이 기반 그룹을 정의한다.

## 작동 방식

그룹은 릴레이 호스트와 그룹 ID의 조합으로 식별되며, 릴레이가 멤버십과 중재의 권한 주체이다. 그룹에 전송되는 사용자 생성 이벤트는 그룹 ID가 포함된 `h` 태그를 가진다. 릴레이가 생성하는 메타데이터는 릴레이 자체 키로 서명된 주소 지정 가능한 이벤트를 사용한다.

핵심 메타데이터 이벤트는 kind 39000이며, kind 39001~39003은 관리자, 멤버 및 지원되는 역할을 기술한다. 중재 작업은 `put-user`, `remove-user`, `edit-metadata`, `create-invite` 등의 9000 시리즈 이벤트를 통해 이루어진다.

## 접근 모델

- **private**: 멤버만 그룹 메시지를 읽을 수 있음
- **closed**: 릴레이가 초대 코드 처리를 사용하지 않는 한 가입 요청이 무시됨
- **hidden**: 릴레이가 비멤버에게 그룹 메타데이터를 숨겨 그룹을 발견할 수 없게 함
- **restricted**: 멤버만 그룹에 메시지를 쓸 수 있음

이 태그들은 독립적이다. 그룹이 모든 사람에게 읽기 가능하면서 멤버에게만 쓰기 가능하거나, 비멤버에게 완전히 숨겨질 수 있다. 이 분리가 중요한 이유는 클라이언트가 "private"를 모든 접근 규칙의 포괄적 약칭으로 취급해서는 안 되기 때문이다.

## 신뢰 모델

NIP-29는 무신뢰(trustless) 그룹 프로토콜이 아니다. 호스팅 릴레이가 어떤 중재 이벤트가 유효한지, 어떤 역할이 존재하는지, 멤버 목록이 표시되는지, 이전 또는 맥락 밖 메시지가 허용되는지를 결정한다. 클라이언트가 서명과 타임라인 참조를 검증할 수 있지만, 그룹의 실제 상태에 대해서는 여전히 릴레이 정책에 의존한다.

이로 인해 마이그레이션과 포크가 가능하지만 자동적이지는 않다. 같은 그룹 ID가 다른 릴레이에 다른 히스토리나 규칙으로 존재할 수 있으므로, 릴레이 URL이 실질적으로 그룹 정체성의 일부가 된다.

## 구현 참고사항

- 클라이언트는 릴레이 URL을 그룹 호스트 키로 취급해야 한다. 2026년 1월의 명확화에서 이를 사양에 명시하고 pubkey 사용에 대한 모호성을 제거했다
- 그룹 상태는 중재 히스토리로부터 재구성되며, 39000 시리즈 릴레이 이벤트는 해당 상태의 정보성 스냅샷이다
- 타임라인 `previous` 참조는 UI 스레딩 개선만을 위한 것이 아니라 릴레이 포크 간 맥락 밖 재브로드캐스팅을 방지하기 위한 것이다

---

**주요 출처:**
- [NIP-29 사양](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - `private`, `closed`, `hidden` 명확화
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - 릴레이 URL을 릴레이 키로 명확화
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - `unallowpubkey` 및 `unbanpubkey` 추가

**언급된 뉴스레터:**
- [Newsletter #2: NIP 업데이트](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: NIP 업데이트](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #11: NIP 업데이트](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: NIP 업데이트](/en/newsletters/2026-03-04-newsletter/#nip-updates)

**같이 보기:**
- [NIP-11: 릴레이 정보 문서](/ko/topics/nip-11/)
