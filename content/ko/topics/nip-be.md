---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE는 Nostr 애플리케이션이 Bluetooth Low Energy를 통해 통신하고 동기화하는 방법을 지정하여, 오프라인 지원 앱이 인터넷 연결 없이 근처 기기 간에 데이터를 동기화할 수 있게 합니다.

## GATT 구조

두 가지 특성을 가진 Nordic UART Service를 사용합니다:
- **Write 특성** - 클라이언트가 서버로 데이터 전송
- **Read 특성** - 서버가 클라이언트로 데이터 전송(알림을 통해)

## 메시지 프레이밍

BLE는 작은 페이로드 제한(버전에 따라 20-256바이트)이 있으므로 메시지는:
- DEFLATE로 압축
- 2바이트 인덱스와 최종 배치 플래그가 있는 청크로 분할
- 최대 64KB 크기 제한

## 역할 협상

기기는 검색 시 광고된 UUID를 비교합니다:
- 더 높은 UUID가 GATT 서버(릴레이 역할)가 됨
- 더 낮은 UUID가 GATT 클라이언트가 됨
- 단일 역할 기기를 위한 미리 정의된 UUID 존재

## 동기화

표준 Nostr 메시지 유형(`EVENT`, `EOSE`, `NEG-MSG`)을 사용하는 반이중 통신으로 간헐적 연결에서 데이터 동기화를 조정합니다.

## 사용 사례

- 근처 기기 간 오프라인 이벤트 동기화
- 인터넷 없이 메시 스타일 메시지 전파
- 네트워크를 사용할 수 없을 때 백업 연결

---

**주요 출처:**
- [NIP-BE 사양](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**언급된 곳:**
- [뉴스레터 #1: 뉴스](/ko/newsletters/2025-12-17-newsletter/#news)

