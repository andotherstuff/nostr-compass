---
title: "NIP-24: 추가 메타데이터 필드"
date: 2025-12-17
translationOf: /en/topics/nip-24.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---
NIP-24는 기본적인 name, about, picture 외에 kind 0 사용자 메타데이터에 사용할 수 있는 추가 선택 필드를 정의한다.

## 추가 메타데이터 필드

- **display_name**: `name`보다 풍부한 문자를 사용할 수 있는 대체 표시 이름
- **website**: 이벤트 작성자와 관련된 웹 URL
- **banner**: 선택적 배경 표시를 위한 와이드(약 1024x768) 이미지 URL
- **bot**: 콘텐츠가 전체 또는 부분적으로 자동화되었음을 나타내는 불리언 값
- **birthday**: 선택적 year, month, day 필드를 가진 객체

사양에서는 두 개의 기존 필드를 사용 중단(deprecated)으로 표시하기도 한다: `displayName`은 `display_name`으로, `username`은 `name`으로 변경해야 한다. 실제로는 여전히 이전 필드가 사용되고 있으므로, 작성 시에는 새 필드를 사용하되 파서는 이전 필드도 허용하는 것이 호환성에 도움이 된다.

## 표준 태그

NIP-24는 범용 태그도 표준화한다:
- `r`: 웹 URL 참조
- `i`: 외부 식별자
- `title`: 다양한 이벤트 유형의 이름
- `t`: 해시태그 (반드시 소문자)

## 왜 중요한가

NIP-24는 주로 수렴에 관한 것이다. 이 필드들과 태그들은 이미 여러 클라이언트에서 사용되고 있었고, 사양이 이들에 일관된 이름과 의미를 부여한다. 이를 통해 배너가 `banner`에 있는지 앱 고유 키에 있는지에 대해 클라이언트 간 의견이 갈리는 것 같은 사소하지만 성가신 비호환성을 줄인다.

구현자를 위한 실용적인 포인트 하나: kind 0은 대부분의 클라이언트에서 빈번히 접근하는 경로이다. 추가 메타데이터는 가벼워야 한다. 별도의 가져오기 패턴이나 독립적인 업데이트 주기가 필요한 필드는 프로필 메타데이터를 비대하게 만들기보다 별도의 이벤트 kind에 두는 것이 좋다.

---

**주요 출처:**
- [NIP-24 사양](https://github.com/nostr-protocol/nips/blob/master/24.md)

**언급된 뉴스레터:**
- [Newsletter #1: NIP 업데이트](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**같이 보기:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
