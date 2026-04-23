---
title: "NIP-57: Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57은 zap을 정의합니다. zap은 Lightning 결제를 Nostr 신원과 콘텐츠에 연결하는 방법입니다. 이 NIP는 zap 가능한 인보이스를 요청하는 방법과, 결제 후 wallet이 게시하는 receipt 이벤트를 모두 표준화합니다.

## 작동 방식

1. 클라이언트는 프로필 메타데이터나 대상 이벤트의 `zap` 태그에서 수신자의 LNURL endpoint를 발견합니다.
2. 클라이언트는 서명된 kind `9734` zap 요청을 릴레이가 아니라 수신자의 LNURL callback으로 보냅니다.
3. 사용자가 인보이스를 결제합니다.
4. 수신자의 wallet 서버가 zap 요청에 나열된 릴레이들에 kind `9735` zap receipt를 게시합니다.
5. 클라이언트가 zap을 검증하고 표시합니다.

## Zap 요청 (kind 9734)

zap 요청은 결제자와 대상 의도를 식별하는 서명된 이벤트입니다. 일반적으로 다음을 포함합니다:

- 수신자 pubkey를 담은 `p` 태그
- zap 대상 이벤트를 담은 `e` 태그 (선택)
- millisatoshis 단위 `amount` 태그
- receipt를 게시할 릴레이 목록인 `relays` 태그

addressable 콘텐츠는 `e` 태그 대신, 혹은 함께 `a` 태그를 사용할 수 있습니다. 선택적인 `k` 태그는 대상 kind를 기록합니다.

## Zap Receipt (kind 9735)

결제 확인 후 수신자의 wallet 서버가 게시합니다. 여기에 포함되는 것은 다음과 같습니다:

- `description` 태그 안의 원본 zap 요청
- 결제된 인보이스를 담은 `bolt11` 태그
- 결제를 증명하는 `preimage` 태그

클라이언트는 receipt를 수신자의 LNURL `nostrPubkey`, 인보이스 금액, 원본 zap 요청과 대조해 검증해야 합니다. 그 검증이 없는 receipt는 단지 주장일 뿐입니다.

## 신뢰와 트레이드오프

zap은 결제를 소셜 그래프 안에서 가시화하기 때문에 유용하지만, receipt는 여전히 수신자의 wallet 인프라가 생성합니다. 명세 자체도 zap receipt가 보편적 결제 증명이 아니라고 적고 있습니다. 가장 정확한 이해는, zap 요청에 연결된 인보이스가 결제되었다는 wallet 서명 진술이라는 것입니다.

클라이언트가 receipt를 zap으로 표시하기 전에는 네 가지를 확인해야 합니다. receipt 서명이 LNURL 응답의 `nostrPubkey`와 일치하는지, `bolt11` 인보이스 금액이 내장된 zap 요청의 `amount` 태그와 일치하는지, 인보이스의 description hash가 문자열화된 zap 요청에 커밋되는지, `preimage`가 인보이스의 `payment_hash`로 해시되는지입니다. 이 검사를 하지 않고 누적 zap 수를 표시하는 클라이언트는 공격자가 위조한 kind `9735` 이벤트로 쉽게 속일 수 있습니다.

## 비공개와 익명 zap

private zap은 여기에 기밀성 계층을 하나 더 얹습니다. 발신자는 zap 요청의 `content`를 수신자용으로 암호화하고 바깥쪽 요청에 `anon` 태그를 넣을 수 있으므로, 릴레이 네트워크는 결제 대상은 보되 첨부 메모는 읽지 못합니다. anonymous zap은 한 단계 더 나아가 zap 요청 자체를 위해 새 일회용 키페어를 생성하므로, receipt는 결제가 있었음을 증명하면서도 수신자는 이를 발신자의 장기 pubkey와 연결할 수 없습니다.

## Zap Goals와 Splits

NIP-57은 [NIP-75](/ko/topics/nip-75/)에서 규정한 zap-goal 시스템의 기반입니다. goal은 목표 금액과 receipt를 집계할 릴레이 집합을 선언하는 kind `9041` 이벤트이며, 클라이언트는 일치하는 kind `9735` 이벤트의 검증된 `bolt11` 금액을 합산해 진행률을 계산합니다.

NIP 부록에 정의된 zap split은, 수신자가 가중치가 달린 여러 `zap` 태그를 가진 kind `0` 프로필을 게시해 하나의 zap 결제가 여러 pubkey로 원자적으로 나뉘게 합니다. [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel)은 split-paying을 end-to-end로 구현합니다.

---

**주요 출처:**
- [NIP-57 명세](https://github.com/nostr-protocol/nips/blob/master/57.md)

**언급된 뉴스레터:**
- [Newsletter #1: News](/ko/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/ko/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #9: NIP Updates](/ko/newsletters/2026-02-11-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)
- [NIP-75: Zap Goals](/ko/topics/nip-75/)
- [NIP-53: 라이브 액티비티](/ko/topics/nip-53/)
