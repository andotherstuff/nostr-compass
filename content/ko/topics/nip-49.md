---
title: "NIP-49: 개인 키 암호화"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - 키 관리
  - 보안
---

NIP-49는 클라이언트가 사용자 개인 키를 비밀번호로 암호화하고 그 결과를 `ncryptsec` 문자열로 인코딩하는 방법을 정의한다. 목표는 평문 `nsec`를 저장하는 것보다 더 강한 기본값을 제공하면서도, 암호화된 키를 클라이언트 사이에서 쉽게 옮길 수 있게 하는 것이다.

## 작동 방식

클라이언트는 hex나 bech32 문자열이 아니라 원시 32바이트 secp256k1 개인 키에서 시작한다. 키마다 무작위 salt를 사용하고 `LOG_N`에 저장된 조정 가능한 작업 계수를 적용한 scrypt로 사용자의 비밀번호에서 임시 대칭 키를 파생한다. 그런 다음 XChaCha20-Poly1305로 개인 키를 암호화하고, 버전 및 키 처리 메타데이터를 앞에 붙인 뒤, 결과를 `ncryptsec` 접두사로 bech32 인코딩한다.

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

위 이벤트는 예시 컨테이너일 뿐이며 NIP-49의 요구사항은 아니다. NIP-49는 이를 게시하기 위한 전용 event kind가 아니라, 암호화된 키 형식 자체를 표준화한다. 클라이언트는 `ncryptsec`를 로컬에 저장하거나, 앱 전용 저장소를 통해 동기화하거나, 백업 내보내기 형태로 제시할 수 있다.

## 보안 모델

NIP-49는 두 가지를 동시에 수행한다. 사용자 비밀번호를 올바른 암호화 키로 바꾸고, 메모리 하드 KDF를 통해 무차별 대입 복구 시도를 느리게 만든다. 작업 계수는 중요하다. `LOG_N` 값이 높을수록 정상 사용자의 복호화는 느려지지만, 공격자의 오프라인 추측 비용도 올라간다.

이 형식은 또한 키가 암호화되기 전에 안전하지 않게 처리된 적이 있는지를 설명하는 1바이트 플래그를 담고 있다. 이 값은 암호문 자체를 바꾸지는 않지만, 클라이언트가 새로 생성된 보호된 백업과 래핑되기 전에 이미 평문으로 노출된 키를 구분할 수 있게 해준다.

## 구현 메모

- 비밀번호는 키 파생 전에 Unicode NFKC로 정규화되므로, 클라이언트와 플랫폼이 달라도 같은 비밀번호를 일관되게 입력할 수 있다.
- XChaCha20-Poly1305는 24바이트 nonce와 인증된 암호화를 사용하므로, 암호문 변조는 복호화 시 명확하게 실패한다.
- 대칭 키는 사용 후 0으로 지우고 폐기해야 한다.
- 사양은 암호화된 키를 공개 relay에 게시하는 것을 권장하지 않는다. 많은 암호화 키를 수집할수록 공격자의 오프라인 크래킹 위치가 유리해지기 때문이다.

## 구현체

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - NIP-49 암호화 개인 키를 이용한 signup 호환성 추가

---

**주요 출처:**
- [NIP-49 Specification](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - NIP-49를 사용하는 클라이언트 측 signup 흐름

**언급된 뉴스레터:**
- [Newsletter #13: Formstr](/ko/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIP Deep Dive](/ko/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**같이 보기:**
- [NIP-46: Nostr Connect](/ko/topics/nip-46/)
- [NIP-55: Android Signer Application](/ko/topics/nip-55/)
