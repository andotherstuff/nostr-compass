---
title: "NIP-49: 개인 키 암호화"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 키 관리
  - 보안
---

NIP-49는 클라이언트가 사용자의 개인 키를 비밀번호로 암호화하고 그 결과를 `ncryptsec` 문자열로 인코딩하는 방법을 정의합니다. 목표는 원시 `nsec` 저장보다 강력한 기본값을 가지면서 암호화된 키를 클라이언트 간에 쉽게 이동할 수 있는 이동성입니다.

## 작동 방식

클라이언트는 16진수나 bech32 문자열이 아닌 원시 32바이트 secp256k1 개인 키에서 시작합니다. 사용자의 비밀번호에서 scrypt를 사용하여 임시 대칭 키를 파생하며, 키별 무작위 솔트와 `LOG_N`으로 저장되는 조정 가능한 작업 계수를 사용합니다. 그런 다음 XChaCha20-Poly1305로 개인 키를 암호화하고, 버전 정보와 키 처리 메타데이터를 앞에 추가한 뒤, `ncryptsec` 접두사로 bech32 인코딩합니다.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

위의 이벤트는 예제 컨테이너이며 NIP-49 요구 사항이 아닙니다. NIP-49는 암호화된 키 형식 자체를 표준화하며, 이를 게시하기 위한 전용 이벤트 kind를 정의하지 않습니다. 클라이언트는 `ncryptsec`를 로컬에 저장하거나, 앱별 스토리지를 통해 동기화하거나, 백업 내보내기로 제공할 수 있습니다.

## 보안 모델

NIP-49는 두 가지를 동시에 수행합니다. 사용자 비밀번호를 적절한 암호화 키로 변환하고, 메모리 집약적 KDF로 무차별 대입 복구 시도를 느리게 만듭니다. 작업 계수가 중요합니다. 높은 `LOG_N` 값은 정당한 사용자의 복호화를 느리게 하지만, 공격자의 오프라인 추측 비용도 높입니다.

이 형식은 암호화 전에 키가 안전하지 않게 처리된 적이 있는지를 설명하는 1바이트 플래그도 포함합니다. 이는 암호문 자체를 변경하지 않지만, 클라이언트가 새로 생성된 보호 백업과 래핑되기 전에 이미 평문으로 복사된 키를 구별할 수 있게 합니다.

## 구현 참고 사항

- 비밀번호는 키 파생 전에 Unicode NFKC로 정규화되어 동일한 비밀번호가 클라이언트 간에 일관되게 입력될 수 있습니다.
- XChaCha20-Poly1305는 24바이트 논스와 인증 암호화를 사용하므로 암호문 변조는 복호화 시 깔끔하게 실패합니다.
- 대칭 키는 사용 후 제로화하고 폐기해야 합니다.
- 사양은 암호화된 키를 공개 relay에 게시하는 것을 권장하지 않습니다. 많은 암호화된 키를 수집하면 공격자의 오프라인 크래킹 위치가 개선되기 때문입니다.

## 구현체

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - NIP-49 암호화 개인 키를 사용한 가입 호환성 추가

---

**주요 출처:**
- [NIP-49 사양](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - NIP-49를 사용한 클라이언트 측 가입 흐름

**언급된 곳:**
- [뉴스레터 #13: Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [뉴스레터 #13: NIP 심층 분석](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**같이 보기:**
- [NIP-46: Nostr Connect](/ko/topics/nip-46/)
- [NIP-55: Android 서명자 애플리케이션](/ko/topics/nip-55/)
