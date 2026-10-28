---
title: "NIP-06: 니모닉 기반 키 파생"
date: 2026-10-28
translationOf: /en/topics/nip-06.md
translationDate: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

NIP-06은 니모닉 시드 문구로부터 Nostr 키 쌍을 파생하는 방법을 설명합니다. [현재 공식 NIP-06 문서](https://github.com/nostr-protocol/nips/blob/master/06.md)는 초안(draft)이자 선택 사항(optional)으로 표시되어 있으며, 다음과 같은 경고를 담고 있습니다.

> __경고__ `unrecommended`: 단일 nsec 사용을 우선하십시오

이 페이지는 역사적 호환성을 위해 NIP-06을 다룹니다. 시드 파생 방식의 채택을 권장하는 것은 아닙니다.

## 작동 방식

[현재 사양](https://github.com/nostr-protocol/nips/blob/master/06.md)에 따르면 BIP39는 니모닉 단어를 생성하고 그 단어로부터 바이너리 시드를 파생하는 데 사용됩니다. 이어서 BIP32가 `m/44'/1237'/<account>'/0/0` 경로를 따라 키를 파생하며, 여기서 1237은 SLIP44에 등록된 Nostr 항목입니다. 기본적인 클라이언트는 account 0을 사용할 수 있습니다. account 값을 증가시키면 같은 시드에서 다른 키를 얻게 됩니다. 두 구현은 파생 단계에 대해 서로 일치하고 결과에 올바른 인코딩을 사용할 때에만 동일한 신원을 재현합니다.

## 테스트 벡터

[2023년 10월 12일 커밋](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)은 테스트 벡터 두 개를 추가했습니다. 하나는 12단어 니모닉으로, 다른 하나는 24단어 니모닉으로 만든 것입니다. 각 벡터에는 예상되는 개인 키와 공개 키가 hex로 나열되어 있고, 이에 대응하는 nsec 및 npub 인코딩도 함께 실려 있습니다. 개발자는 이 벡터를 활용해 구현을 교차 검증할 수 있습니다. 그러나 이 벡터는 키 보관에 대해서는 아무것도 말해 주지 않으며, 보안을 인증하지 않고, 보편적인 상호운용성을 보장하지도 않습니다.

## 함께 보기

- [NIP-01](/ko/topics/nip-01/)

**1차 자료:**

- [NIP-06 (현재)](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [NIP-06 테스트 벡터를 추가한 커밋 (2023년 10월 12일)](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**언급된 곳:**

- [뉴스레터 #46](/ko/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
