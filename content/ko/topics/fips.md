---
title: "FIPS"
date: 2026-02-25
translationOf: /en/topics/fips.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---
FIPS(Free Internetworking Peering System)는 Nostr 방식의 secp256k1 키쌍을 노드 신원으로 사용하는 자기 조직화 메시 네트워킹 프로토콜이다.

## 작동 방식

FIPS는 중앙 서버나 인증 기관 없이 피어 네트워킹을 구현하는 것을 목표로 한다. 노드는 이웃을 발견하고, 라우팅 상태를 구축하며, 로컬 정보만으로 패킷을 전달한다.

설계는 스패닝 트리와 bloom filter 도달 가능성 데이터를 결합한다. 각 노드는 트리 기준 좌표를 부여받고, 목적지를 향해 탐욕적(greedy) 라우팅을 수행한다. 탐욕적 라우팅이 실패하면, 트리가 대체 경로를 제공한다.

두 가지 암호화 계층이 트래픽을 보호한다. 링크 계층 암호화(Noise IK 패턴)는 이웃 간 홉 단위 통신을 보호한다. 세션 계층 암호화(Noise XK 패턴)는 중간 라우터로부터 종단 간 보호를 제공한다.

## 왜 중요한가

FIPS는 Nostr 개발자들이 이미 이해하는 동일한 키 모델을 재사용하되, 소셜 이벤트가 아닌 패킷 라우팅에 적용한다. 이를 통해 단순한 신원 체계를 갖추게 된다: 네트워크 신원이 암호화 키 자체이며, IP 할당이나 인증서 체인이 아니다.

전송 계층에 구애받지 않는 설계도 중요하다. 동일한 라우팅 및 신원 모델이 원칙적으로 UDP, Ethernet, Bluetooth, LoRa 위에서 모두 동작할 수 있어, 적대적이거나 불안정한 네트워크 환경에서 FIPS를 유용하게 만든다.

## 구현 현황

Compass에서 다뤘듯이, 현재 Rust 구현체에는 UDP 전송과 bloom filter 기반 디스커버리가 작동하고 있다. 릴레이 기반 부트스트래핑은 아직 향후 작업이므로, 현재 프로토콜은 완성된 Nostr 릴레이 대체물이라기보다 네트워킹 기반 레이어에 가깝다.

---

**주요 출처:**
- [FIPS 저장소](https://github.com/jmcorgan/fips)
- [설계 문서](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**언급된 뉴스레터:**
- [Newsletter #11: FIPS 소식](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**같이 보기:**
- [Marmot Protocol](/ko/topics/marmot/)
