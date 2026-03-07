---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
translationOf: /en/topics/nip-be.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Connectivity
---
NIP-BE는 Nostr 애플리케이션이 Bluetooth Low Energy를 통해 통신하고 동기화하는 방법을 명시하며, 오프라인 가능한 앱이 인터넷 연결 없이 근처 기기 간 데이터를 동기화할 수 있게 한다.

## 작동 방식

NIP-BE는 별도의 이벤트 모델을 만들지 않고 일반 Nostr 메시지 프레임을 BLE 위에서 재사용한다. 기기는 BLE 서비스와 기기 UUID를 광고하고, 만나면 UUID를 비교하여 어느 쪽이 GATT 서버가 되고 어느 쪽이 GATT 클라이언트가 될지 결정론적으로 결정한다.

GATT 서비스는 하나의 write 특성과 하나의 read/notify 특성을 가진 Nordic UART 스타일 형태를 사용한다. 이는 일반 Nostr 메시지를 전달하면서도 제한된 모바일 스택에 충분히 단순한 전송 계층을 유지한다.

## 메시지 프레이밍

BLE는 페이로드 크기 제한이 작아서, NIP-BE는 메시지를 DEFLATE로 압축하고, 인덱스가 붙은 청크로 분할하여, 한 번에 하나의 메시지만 전송한다. 스펙은 메시지를 64 KB로 제한하는데, 이 전송 계층이 대량 전송이 아닌 동기화와 로컬 전파용임을 상기시켜 준다.

## 동기화 모델

연결이 수립되면, 피어는 [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md) negentropy 메시지(`NEG-OPEN`, `NEG-MSG`, `EVENT`, `EOSE` 등)를 기반으로 한 반이중 동기화 흐름을 사용한다. 이 설계 선택이 중요한 이유는 BLE 전용 복제 알고리즘을 구축하는 대신 기존 릴레이 동기화 로직을 재사용할 수 있기 때문이다.

반이중 규칙은 불안정한 BLE 링크의 현실도 반영한다. 간헐적 근거리 연결은 각 측이 누구 차례인지 정확히 알 때 더 잘 작동한다.

## 왜 중요한가

NIP-BE는 Nostr 애플리케이션에 로컬 우선 네트워킹 경로를 제공한다. 두 대의 폰이 서로 가까이 있으면 인터넷이 없어도 직접 노트나 릴레이 상태를 동기화할 수 있다. 이는 검열 저항, 재난 상황, 저연결성 소셜 앱에 유용하다.

제약도 마찬가지로 중요하다: BLE 대역폭은 낮고, 연결은 수명이 짧으며, 큰 히스토리는 잘 맞지 않는다. 실제로 NIP-BE는 점진적 동기화와 근처 메시지 전파에 적합하지, 전체 아카이브 복제에는 적합하지 않다.

---

**주요 출처:**
- [NIP-BE 명세](https://github.com/nostr-protocol/nips/blob/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)

**언급된 뉴스레터:**
- [Newsletter #1: 뉴스](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**같이 보기:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
