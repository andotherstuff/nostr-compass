---
title: "NIP-29: 릴레이 기반 그룹"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-04-22
draft: false
categories:
  - Social
  - Groups
---

NIP-29는 릴레이 기반 그룹을 정의합니다. 여기서 릴레이는 그룹 멤버십, 권한, 메시지 가시성을 관리합니다.

## 작동 방식

그룹은 릴레이 호스트와 그룹 ID 조합으로 식별되며, 릴레이가 멤버십과 moderation의 권한 주체입니다. 그룹으로 들어가는 사용자 생성 이벤트는 그룹 ID를 담은 `h` 태그를 가집니다. 릴레이가 생성하는 메타데이터는 릴레이 자신의 키로 서명된 addressable event를 사용합니다.

핵심 메타데이터 이벤트는 kind `39000`이며, kind `39001`부터 `39003`까지는 관리자, 멤버, 지원 역할을 설명합니다. moderation 동작은 `put-user`, `remove-user`, `edit-metadata`, `create-invite` 같은 9000번대 이벤트로 이뤄집니다.

## 접근 모델

- **private**: 멤버만 그룹 메시지를 읽을 수 있음
- **closed**: 릴레이가 invite-code 처리를 하지 않으면 가입 요청을 무시함
- **hidden**: 릴레이가 비멤버에게 그룹 메타데이터를 숨겨 그룹이 발견되지 않게 함
- **restricted**: 멤버만 그룹에 메시지를 쓸 수 있음

이 태그들은 서로 독립적입니다. 그룹은 모두에게 읽기 가능하지만 멤버에게만 쓰기 가능할 수도 있고, 비멤버에게 완전히 숨겨질 수도 있습니다. 이 구분이 중요한 이유는 클라이언트가 "private"를 모든 접근 규칙을 한꺼번에 뜻하는 약칭으로 취급해서는 안 되기 때문입니다.

## 신뢰 모델

NIP-29는 trustless 그룹 프로토콜이 아닙니다. 어떤 moderation 이벤트가 유효한지, 어떤 역할이 존재하는지, 멤버 목록이 보이는지, 오래되었거나 맥락 밖인 메시지를 허용할지는 호스팅 릴레이가 결정합니다. 클라이언트는 서명과 타임라인 참조를 검증할 수 있지만, 그룹의 실제 상태는 여전히 릴레이 정책에 의존합니다.

따라서 마이그레이션과 포크는 가능하지만 자동은 아닙니다. 같은 그룹 ID가 서로 다른 릴레이에서 다른 히스토리나 규칙으로 존재할 수 있으므로, 실제로는 릴레이 URL이 그룹 정체성의 일부가 됩니다.

## 유용한 구현 참고사항

- 클라이언트는 릴레이 URL을 그룹 호스트 키로 취급해야 합니다. 2026년 1월 명확화가 이를 명시해 pubkey 사용에 대한 모호성을 없앴습니다.
- 그룹 상태는 moderation 히스토리로부터 재구성되며, 39000번대 릴레이 이벤트는 그 상태의 정보성 스냅샷입니다.
- 타임라인 `previous` 참조는 UI 스레딩 개선만이 아니라 릴레이 포크 간 맥락 밖 재브로드캐스트를 막기 위한 것입니다.

## 최근 명세 작업

- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310)과 hodlbod의 [Flotilla 1.7.3/1.7.4 release notes](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)는 캘린더 이벤트, poll, 기타 payload 같은 비채팅 콘텐츠를 kind `9`로 감싸 그룹 안으로 보낼 때 room context가 유지되도록 제안합니다.
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319)는 하나의 그룹이 같은 릴레이 위에서 독립 그룹을 새로 만들지 않고도 여러 병렬 채널을 가질 수 있도록 subgroup 계층을 명세에 추가합니다. subgroup 식별자는 기존 `h` 태그를 활용하므로 오래된 클라이언트용 단일 `h` 태그 메시지 형태를 유지합니다.
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316)은 kind `39003` 역할 이벤트에 명시적 권한 스키마를 정의해, 각 역할이 invite, add-user, remove-user, edit-metadata, delete-event, add-permission 같은 허용 작업 집합과 선택적 만료 시각을 가지게 합니다.

## 구현체

- [Flotilla](https://gitea.coracle.social/coracle/flotilla)는 hodlbod의 주요 NIP-29 클라이언트입니다. [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3)과 [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)는 kind-9 wrapping, polls, [NIP-46](/ko/topics/nip-46/) 로그인용 Aegis URL scheme, space invite용 native share, room mention, 모바일 clipboard 이미지 붙여넣기, drafts, 통화 중 video를 추가했습니다.
- [Wisp](https://github.com/barrydeen/wisp)는 [PR #471](https://github.com/barrydeen/wisp/pull/471)에서 flags, invites, roles, AUTH prompt를 포함한 NIP-29 그룹 설정을 추가했고, [PR #478](https://github.com/barrydeen/wisp/pull/478)에서 그룹 `9021`, `9007`, `9009` 이벤트를 보내기 전에 AUTH 순서를 강화했습니다.

---

**주요 출처:**
- [NIP-29 명세](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - `private`, `closed`, `hidden` 명확화
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - 릴레이 URL을 릴레이 키로 명확화
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - `unallowpubkey`와 `unbanpubkey` 추가
- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) - 비채팅 콘텐츠를 위한 kind-9 wrapping
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) - subgroups spec
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) - kind 39003의 명시적 역할 권한
- [Flotilla 1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)
- [Wisp PR #471](https://github.com/barrydeen/wisp/pull/471) - NIP-29 그룹 설정

**언급된 뉴스레터:**
- [Newsletter #2: NIP Updates](/ko/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #6: NIP Updates](/ko/newsletters/2026-01-21-newsletter/)
- [Newsletter #11: NIP Updates](/ko/newsletters/2026-02-25-newsletter/)
- [Newsletter #12: NIP Updates](/ko/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Flotilla 1.7.3/1.7.4](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Wisp NIP-29 config](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Updates (subgroups, role permissions)](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-11: 릴레이 정보 문서](/ko/topics/nip-11/)
