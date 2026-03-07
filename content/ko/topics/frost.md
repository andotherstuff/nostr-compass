---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
---
FROST(Flexible Round-Optimized Schnorr Threshold Signatures)는 어떤 참가자도 전체 비밀키를 보유하지 않은 상태에서 그룹이 하나의 유효한 Schnorr 서명을 생성할 수 있는 임계값 서명 방식이다.

## 작동 방식

FROST는 T-of-N 서명을 가능하게 한다. 임계값 이상의 참가자 집합이 협력하여 그룹 공개키에 대한 서명을 생성할 수 있다.

서명 프로토콜은 두 라운드로 구성된다:

1. **커밋 라운드**: 각 참가자가 암호학적 커밋먼트를 생성하고 공유한다
2. **서명 라운드**: 참가자들이 부분 서명을 결합하여 최종 집계 서명을 만든다

최종 출력은 일반 Schnorr 서명처럼 검증된다. 검증자는 공동 서명자 목록이 아니라, 하나의 공개키 아래 하나의 서명만 보게 된다.

## 보안 참고사항

nonce 처리가 핵심이다. RFC는 서명 nonce가 일회용임을 명시한다. 재사용 시 키 자료가 유출될 수 있다.

RFC는 분산 키 생성을 표준화하지 않는다. 서명 프로토콜 자체를 명세하며, 신뢰할 수 있는 딜러 키 생성만 부록으로 포함한다. 실제로 FROST 배포의 안전성은 서명 흐름과 함께 공유분(share)이 어떻게 생성되고 저장되었는지에 달려 있다.

## Nostr에서의 활용

Nostr 맥락에서 FROST는 다음을 지원할 수 있다:

- **정족수 거버넌스**: 그룹이 T-of-N 방식으로 nsec을 공유하여, 구성원이 스스로를 대표하거나 위원회에 위임할 수 있다
- **다중 서명 관리**: 여러 관리자 서명이 필요한 커뮤니티 모더레이션
- **분산 키 관리**: 중요한 운영을 위해 여러 당사자에 걸쳐 신뢰를 분산

## 상태

FROST는 [RFC 9591](https://datatracker.ietf.org/doc/rfc9591/)로 명세되어 있으며, 2024년 6월 IRTF 스트림에서 발행되었다. 프로토콜에 안정적인 공개 명세를 부여하지만, IETF 표준 트랙 RFC는 아니다.

---

**주요 출처:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST 논문 (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [Zcash Foundation Rust 구현체](https://github.com/ZcashFoundation/frost)

**언급된 뉴스레터:**
- [Newsletter #3: NIPs 저장소](/en/newsletters/2025-12-31-newsletter/#nips-repository)
- [Newsletter #8](/en/newsletters/2026-02-04-newsletter/)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)

**같이 보기:**
- [NIP-46: Nostr Connect](/ko/topics/nip-46/)
- [NIP-55: Android Signer Application](/ko/topics/nip-55/)
