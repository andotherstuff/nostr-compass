---
title: "NIP-90"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-02-25
draft: false
categories: ["NIP 명세", "DVM"]
---

NIP-90은 Data Vending Machine(DVM)을 정의합니다. Nostr에서 계산 작업을 요청하고 대가를 지불하는 마켓플레이스 프로토콜입니다.

## 동작 방식

클라이언트는 필요한 작업을 지정하는 job 요청 event(kind 5000-5999)를 게시합니다. 서비스 제공자는 자신의 기능과 일치하는 요청을 모니터링하고, 계산을 완료한 후 결과를 게시합니다. 결제는 Lightning이나 job 흐름에서 협의된 다른 방식으로 이루어집니다.

Job kind는 텍스트 생성, 이미지 생성, 번역, 콘텐츠 검색 등 다양한 계산 유형을 정의합니다. 각 kind는 예상 입력/출력 형식을 지정합니다.

## 주요 특징

NIP-90은 탈중앙화 컴퓨팅 마켓플레이스를 구현합니다. Kind 기반 job 유형 시스템으로 제공자들이 가격과 품질로 경쟁하며, 새로운 계산 유형을 위한 확장도 지원합니다.

---

**주요 출처:** [NIP-90 명세](https://github.com/nostr-protocol/nips/blob/master/90.md)

**언급된 곳:** [뉴스레터 #11: NIP-AC DVM 에이전트 조정](/ko/newsletters/2026-02-25-newsletter/#nip-업데이트)

**참조:** [NIP-85: Trusted Assertions](/ko/topics/nip-85/)
