---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2025-12-31
draft: false
categories:
  - 암호학
  - 프로토콜
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures)는 그룹의 참가자들이 어떤 단일 당사자도 완전한 개인 키를 보유하지 않으면서 협력하여 유효한 Schnorr 서명을 생성할 수 있게 하는 임계값 서명 체계입니다.

## 작동 방식

FROST는 T-of-N 임계값 서명을 가능하게 하며, 총 N명의 키 보유자 중 T명의 참가자가 협력하여 유효한 서명을 생성해야 합니다. 프로토콜은 두 라운드로 운영됩니다:

1. **커밋먼트 라운드**: 각 참가자가 암호학적 커밋먼트를 생성하고 공유
2. **서명 라운드**: 참가자들이 부분 서명을 결합하여 최종 집계 서명 생성

결과 서명은 표준 Schnorr 서명과 구별할 수 없어 기존 검증 시스템과의 하위 호환성을 유지합니다.

## 주요 특성

- **임계값 보안**: 단일 참가자만으로는 서명할 수 없으며, T명의 당사자가 협력해야 함
- **라운드 효율성**: 서명에 필요한 통신 라운드는 단 두 번
- **위조 방지**: 이전 임계값 체계에 대한 공격으로부터 보호하는 새로운 기술
- **서명 집계**: 여러 서명이 하나의 간결한 서명으로 결합
- **프라이버시**: 최종 서명은 어떤 T명의 참가자가 서명했는지 드러내지 않음

## Nostr에서의 사용 사례

Nostr 맥락에서 FROST는 다음을 가능하게 합니다:

- **쿼럼 거버넌스**: 그룹이 T-of-N 체계를 통해 nsec를 공유할 수 있으며, 구성원은 자신을 대표하거나 위원회에 위임 가능
- **다중 서명 관리**: 여러 관리자 서명이 필요한 커뮤니티 중재
- **분산형 키 관리**: 중요한 작업을 위해 여러 당사자 간에 신뢰 분산

## 표준화

FROST는 2024년 6월에 RFC 9591로 표준화되었으며, "The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures"라는 제목이 붙었습니다.

---

**주요 출처:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**언급된 곳:**
- [Newsletter #3: NIPs 저장소](/ko/newsletters/2025-12-31-newsletter/#nips-repository)

**참고 항목:**
- [NIP-XX Quorum 제안](https://github.com/nostr-protocol/nips/pull/2179)
