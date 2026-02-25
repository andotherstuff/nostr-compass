---
title: "NIP-85"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - 신뢰
  - 인프라
---

NIP-85는 신뢰 어설션을 정의합니다. 비용이 많이 드는 계산을 신뢰할 수 있는 서비스 제공자에게 위임하고, 제공자가 서명된 결과를 Nostr event로 게시하는 시스템입니다.

## 동작 방식

신뢰 네트워크 점수, 참여 지표 및 기타 계산 값은 많은 relay를 크롤링하고 대량의 event를 처리해야 합니다. 이 작업은 모바일 기기에서 실행하기에 비현실적입니다. NIP-85는 전문 제공자가 이러한 계산을 수행하고 클라이언트가 쿼리할 수 있는 결과를 게시하도록 합니다.

서비스 제공자는 kind 30085 event를 통해 자신의 기능을 알립니다. 클라이언트는 사용자가 이미 팔로우하거나 신뢰하는 pubkey에서 이러한 공지를 쿼리하여 제공자를 발견합니다. 결과는 제공자가 서명한 kind 30382 event로 제공됩니다.

## 주요 특징

리소스 집약적 지표를 위한 위임 계산, 소셜 그래프를 통한 제공자 발견, 검증 가능한 결과를 위한 서명된 어설션, 클라이언트 측 신뢰 결정을 지원합니다.

---

**주요 출처:**
- [NIP-85 명세](https://github.com/nostr-protocol/nips/blob/master/85.md)

**언급된 곳:**
- [뉴스레터 #10: NIP-85 심층 분석](/ko/newsletters/2026-02-18-newsletter/#nip-심층-분석-nip-85-신뢰-어설션)
- [뉴스레터 #11: NIP-85 서비스 제공자 발견 가능성](/ko/newsletters/2026-02-25-newsletter/#nip-업데이트)

**참조:**
- [신뢰 네트워크](/ko/topics/web-of-trust/)
