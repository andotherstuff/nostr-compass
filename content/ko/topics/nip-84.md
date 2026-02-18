---
title: "NIP-84: 하이라이트"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-02-18
draft: false
categories:
  - Content
  - Protocol
---

NIP-84는 사용자가 Nostr의 장문 콘텐츠에서 가치 있다고 생각하는 구절을 표시하고 공유할 수 있는 kind 9802 "하이라이트" event를 정의합니다.

## 작동 방식

`.content` 필드에 하이라이트된 텍스트가 담깁니다. Event는 Nostr 네이티브 콘텐츠에는 `a` 또는 `e` tag를, 외부 URL에는 `r` tag를 사용하여 출처 자료를 참조합니다 (클라이언트는 추적 파라미터를 제거해야 합니다). 선택적 `p` tag가 원저자를 표시하며, 선택적 `context` tag가 하이라이트가 더 긴 구절의 일부인 경우 주변 텍스트를 제공합니다.

## 인용 하이라이트

사용자가 `comment` tag를 추가하여 인용 하이라이트를 만들 수 있으며, 이는 인용 리포스트로 렌더링됩니다. 이를 통해 마이크로블로깅 클라이언트에서 중복 항목을 방지합니다. 댓글 내에서 `p` tag 언급은 저자/편집자 표시와 구별하기 위해 "mention" 속성이 필요하며, `r` tag URL은 출처 참조를 위한 "source" 속성을 사용합니다.

---

**주요 출처:**
- [NIP-84 명세](https://github.com/nostr-protocol/nips/blob/master/84.md)

**언급된 곳:**
- [뉴스레터 #10: 릴리스](/ko/newsletters/2026-02-18-newsletter/#prism-android에서-어디서든-nostr로-공유)

**참조:**
- [NIP-94: 파일 메타데이터](/ko/topics/nip-94/)
