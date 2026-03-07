---
title: "신뢰 기반 릴레이 평가"
date: 2026-01-21
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relays
---
신뢰 기반 릴레이 평가(Trusted Relay Assertions)는 서명된 제3자 릴레이 평가를 Nostr에 게시하여, 클라이언트가 자가 보고된 메타데이터만으로는 얻을 수 없는 맥락을 바탕으로 릴레이를 선택할 수 있게 하는 개념이다. 현재 표준화된 구성 요소는 [NIP-85: Trusted Assertions](/ko/topics/nip-85/)로, 사용자가 제공자를 신뢰하는 방법과 제공자가 서명된 계산 결과를 게시하는 방법을 정의한다.

## 작동 방식

릴레이 선택에는 세 가지 계층이 있다. [NIP-11: 릴레이 정보 문서](/ko/topics/nip-11/)는 릴레이가 자신에 대해 말하는 내용을 다룬다. [NIP-66: 릴레이 발견 및 활성 상태 모니터링](/ko/topics/nip-66/)은 관찰자가 측정할 수 있는 가용성과 지연 시간 같은 정보를 다룬다. 신뢰 기반 릴레이 평가는 나머지 격차를 채우려 한다: 제3자가 해당 데이터로부터 내린 결론과, 클라이언트가 그 결론을 신뢰할지 여부다.

더 넓은 NIP-85 모델에서, 사용자는 kind `10040` 이벤트로 신뢰하는 제공자를 지명하고, 제공자는 서명된 주소 지정 가능한 assertion 이벤트를 게시한다. 릴레이 점수 산정 애플리케이션은 클라이언트가 동의하는 두 가지 추가 요소가 필요하다: 릴레이를 주제로 식별하는 방법, 그리고 점수와 근거 증거를 나타내는 result 태그가 무엇인지.

전송과 신뢰 위임은 표준화되어 있지만, 릴레이별 점수 모델은 여전히 애플리케이션 패턴이라는 점이 중요하다. 서로 다른 제공자가 무엇이 릴레이를 신뢰할 만하게 만드는지에 대해 정당하게 의견이 다를 수 있다.

## 신뢰 모델

릴레이 신뢰 점수는 객관적 사실이 아니다. 한 제공자는 가동 시간과 쓰기 처리량을 우선시할 수 있고, 다른 제공자는 법적 관할권, 중재 정책, 운영자 신원을 우선시할 수 있으며, 또 다른 제공자는 감시 저항성을 가장 중요시할 수 있다. 유용한 클라이언트라면 점수만이 아니라 누가 점수를 산출했는지 보여줘야 한다.

여기서 [Web of Trust](/ko/topics/web-of-trust/)가 등장한다. 클라이언트가 이미 특정 사람이나 서비스를 신뢰한다면, 단일 글로벌 랭킹이 존재하는 척하는 대신 같은 소셜 이웃에서 오는 릴레이 평가를 선호할 수 있다.

## 왜 중요한가

[NIP-46](/ko/topics/nip-46/) 원격 서명자, 지갑 연결, 또는 낯선 릴레이를 제안하는 모든 앱에서, 제3자 릴레이 평가는 기본값에 대한 맹목적 신뢰를 줄일 수 있다. [NIP-65](/ko/topics/nip-65/) 릴레이 목록과 결합하면, 클라이언트는 "어떤 릴레이를 사용하는가"와 "이 작업에 어떤 릴레이를 신뢰하는가"를 분리할 수 있다.

주요 정확성 주의사항은 범위다. 2026년 1월 뉴스레터에서는 릴레이 신뢰 점수를 전용 제안으로 다뤘지만, NIPs 저장소에 병합된 표준은 더 넓은 [NIP-85: Trusted Assertions](/ko/topics/nip-85/) 형식이다. 릴레이 점수 산정은 해당 모델 위에 구축된 사용 사례이지, 별도의 확정된 릴레이 신뢰 와이어 포맷이 아니다.

---

**주요 출처:**
- [NIP-85 명세](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534: Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534)

**언급된 뉴스레터:**
- [Newsletter #6: 뉴스](/en/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP 업데이트](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #7: NIP 업데이트](/en/newsletters/2026-01-28-newsletter/#nip-updates)

**같이 보기:**
- [NIP-11: 릴레이 정보 문서](/ko/topics/nip-11/)
- [NIP-66: 릴레이 발견 및 활성 상태 모니터링](/ko/topics/nip-66/)
- [NIP-85: Trusted Assertions](/ko/topics/nip-85/)
- [Web of Trust](/ko/topics/web-of-trust/)
