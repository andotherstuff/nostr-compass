---
title: "NIP-90: Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - DVM
---
NIP-90은 Data Vending Machines(DVM)를 정의하며, Nostr를 통해 유료 연산 작업을 요청하고 전달하는 프로토콜이다.

## 작동 방식

고객은 `5000-5999` 범위의 작업 요청 이벤트를 발행한다. 각 요청에는 입력을 위한 하나 이상의 `i` 태그, 작업별 설정을 위한 `param` 태그, 기대하는 형식을 위한 `output` 태그, `bid` 상한, 그리고 응답이 전달될 릴레이 힌트를 포함할 수 있다. 서비스 제공자는 `6000-6999` 범위에서 요청 kind보다 항상 `1000` 높은 결과 kind로 응답한다.

결과에는 원본 요청, 고객의 pubkey, 그리고 선택적으로 `amount` 태그나 인보이스가 포함된다. 제공자는 `payment-required`, `processing`, `partial`, `error`, `success` 같은 kind `7000` 피드백 이벤트도 보낼 수 있어, 최종 결과가 도착하기 전에 클라이언트가 진행 상황을 표시할 수 있다.

## 결제와 프라이버시

프로토콜은 의도적으로 비즈니스 로직을 열어둔다. 제공자는 작업 시작 전, 샘플 반환 후, 또는 전체 결과 전달 후에 결제를 요청할 수 있다. DVM 작업은 저렴한 텍스트 변환부터 비용이 큰 GPU 작업까지 다양하고, 제공자마다 동일한 결제 위험을 감수하지 않기 때문에 이러한 유연성이 필요하다.

고객이 입력을 비공개로 하려면 `i`와 `param` 데이터를 암호화된 `content`로 옮기고 이벤트에 `encrypted` 태그와 제공자의 `p` 태그를 표시할 수 있다. 이는 릴레이 관찰자로부터 프롬프트나 원본 자료를 보호하지만, 개방형 시장 요청을 브로드캐스트하는 대신 특정 제공자를 지정해야 한다는 의미이기도 하다.

## 상호운용성 참고사항

NIP-90은 입력 유형 `job`을 사용하는 `i` 태그를 통해 작업 체이닝을 지원하므로, 하나의 결과가 다음 요청의 입력이 될 수 있다. 별도의 오케스트레이션 레이어를 만들지 않고도 다단계 흐름이 가능하다.

제공자 탐색은 요청/응답 루프 자체 외부에 있다. 스펙은 지원하는 작업 kind를 광고하기 위해 [NIP-89: Recommended Application Handlers](/ko/topics/nip-89/) 공지를 가리키며, 이를 통해 클라이언트가 요청을 발행하기 전에 벤더를 찾을 수 있다.

---

**주요 출처:**
- [NIP-90 명세](https://github.com/nostr-protocol/nips/blob/master/90.md)

**언급된 뉴스레터:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/en/newsletters/2026-02-25-newsletter/#nip-updates)

**같이 보기:**
- [NIP-89: Recommended Application Handlers](/ko/topics/nip-89/)
