---
title: "NIP-78: 앱별 데이터"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-78.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Data Storage
---

NIP-78은 애플리케이션이 Nostr 이벤트를 사용하여 사용자를 대신해 임의의 데이터를 저장하는 표준 이벤트 kind를 정의하며, 중앙 서버 없이 디바이스 간 상태 동기화를 가능하게 합니다.

## 작동 방식

핵심 이벤트 kind는 30078로, 매개변수화된 교체 가능 이벤트입니다. `d` 태그는 애플리케이션이 정의한 식별자 문자열로, 저장 슬롯을 특정 애플리케이션과 목적으로 범위를 한정합니다.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

애플리케이션은 고유한 `d` 태그(예: `tamagostrich-pet-state` 또는 `amethyst-settings`)와 유지해야 할 JSON 또는 텍스트 콘텐츠를 포함한 30078 이벤트를 게시합니다. 30078은 교체 가능하고 `d` 태그로 범위가 한정되므로, 저장된 상태를 업데이트한다는 것은 동일한 `d` 태그로 새 이벤트를 게시하는 것을 의미하며 릴레이는 최신 버전만 보유합니다.

## 디바이스 간 동기화

사용자의 공개 키와 애플리케이션의 `d` 태그를 아는 모든 클라이언트는 사용자의 릴레이 세트에서 현재 상태를 가져와 어떤 디바이스에서도 재구성할 수 있습니다. 데이터는 사용자의 키 쌍으로 서명된 이벤트에 존재하고 [NIP-65](/ko/topics/nip-65/) 릴레이 목록의 릴레이에 저장되므로 사용자가 데이터를 소유합니다.

## 비공개 데이터 vs. 공개 데이터

비공개 애플리케이션 데이터의 경우, 게시 전에 [NIP-44](/ko/topics/nip-44/)를 사용하여 콘텐츠 필드를 암호화할 수 있으므로 릴레이는 키 보유자만 복호화할 수 있는 암호문만 저장합니다. 공개 애플리케이션 데이터는 다른 클라이언트가 읽고 표시할 수 있도록 암호화하지 않고 저장할 수 있습니다.

## 콘텐츠 형식

NIP-78은 콘텐츠 형식을 의도적으로 열린 상태로 두며, 애플리케이션이 자체 스키마를 선택합니다. 일반적인 관례는 같은 릴레이를 사용하는 앱 간의 충돌을 방지하기 위해 `d` 태그에 애플리케이션 이름을 접두사로 붙이는 것입니다.

## 구현

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — `tamagostrich-pet-state` kind:30078 이벤트를 통한 디바이스 간 펫 상태 동기화
- [Wisp](https://github.com/barrydeen/wisp-android) — kind:30078 지갑 백업 및 디바이스 간 보안 설정 동기화; NIP-78 작성자 필터를 사용하여 단일 REQ로 병합된 아웃박스 구독
- [NosPress](https://github.com/nostrapps/nospress) — NIP-78 이벤트에 저장된 CMS 오케스트레이션 상태
- 여러 Nostr 클라이언트 설정 동기화 구현 (Amethyst 등)

---

**주요 출처:**
- [NIP-78 사양](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — 프로덕션 구현

**언급된 곳:**
- [뉴스레터 #22: NIP-78 딥 다이브](/ko/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [뉴스레터 #22: Tamagostrich](/ko/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**참고:**
- [NIP-51: 목록](/ko/topics/nip-51/)
- [NIP-44: 버전별 암호화](/ko/topics/nip-44/)
- [NIP-65: 릴레이 목록 메타데이터](/ko/topics/nip-65/)
