---
title: "NIP-90: Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - DVM
---

NIP-90은 Data Vending Machines (DVM)을 정의합니다. 이는 Nostr 위에서 유료 계산 작업을 요청하고 전달하기 위한 프로토콜입니다.

## 작동 방식

고객은 `5000-5999` 범위에 작업 요청 이벤트를 게시합니다. 각 요청은 하나 이상의 입력용 `i` 태그, 작업별 설정용 `param` 태그, 기대 출력 형식용 `output` 태그, `bid` 상한, 그리고 응답이 나타나야 할 위치를 가리키는 relay hint를 포함할 수 있습니다. 서비스 제공자는 `6000-6999` 범위의 대응 결과 kind로 응답하며, 결과 kind는 항상 요청 kind보다 `1000` 큽니다.

결과에는 원래 요청, 고객 pubkey, 그리고 선택적으로 `amount` 태그나 invoice가 포함됩니다. 제공자는 `payment-required`, `processing`, `partial`, `error`, `success` 같은 kind `7000` 피드백 이벤트도 보낼 수 있으므로, 최종 결과가 도착하기 전에 클라이언트가 진행 상황을 보여 줄 수 있습니다.

## 결제와 프라이버시

이 프로토콜은 의도적으로 business logic를 열어 둡니다. 제공자는 작업이 시작되기 전, 샘플을 반환한 뒤, 혹은 전체 결과를 전달한 뒤에 결제를 요구할 수 있습니다. 이런 유연성이 중요한 이유는 DVM 작업이 값싼 텍스트 변환부터 비용이 큰 GPU 작업까지 매우 다양하고, 제공자마다 감수하는 결제 위험도 같지 않기 때문입니다.

고객이 입력을 비공개로 유지하고 싶다면, 요청은 `i`와 `param` 데이터를 암호화된 `content`로 옮기고 이벤트에 `encrypted` 태그와 제공자의 `p` 태그를 붙일 수 있습니다. 이렇게 하면 프롬프트나 원본 자료를 릴레이 관찰자로부터 보호할 수 있지만, 동시에 개방 시장 요청을 브로드캐스트하는 대신 특정 제공자를 겨냥해야 한다는 의미이기도 합니다.

## 상호운용성 참고사항

NIP-90은 입력 타입이 `job`인 `i` 태그를 통해 작업 chaining을 지원합니다. 따라서 하나의 결과가 다음 요청의 입력으로 이어질 수 있습니다. 별도의 orchestration layer를 만들지 않아도 다단계 흐름을 만들 수 있다는 뜻입니다.

제공자 탐색은 요청/응답 루프 자체 바깥에 있습니다. 이 명세는 지원하는 작업 kind를 광고하기 위해 [NIP-89: Recommended Application Handlers](/ko/topics/nip-89/) 공지를 사용하라고 가리킵니다. 클라이언트는 이 방식으로 요청을 내기 전에 vendor를 발견할 수 있습니다.

---

**주요 출처:**
- [NIP-90 Specification](https://github.com/nostr-protocol/nips/blob/master/90.md)

**언급된 뉴스레터:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/ko/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: Forgesworn toll-booth-dvm](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Agent Reputation Attestations proposal](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-89: Recommended Application Handlers](/ko/topics/nip-89/)
