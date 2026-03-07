---
title: "NIP-92: 미디어 첨부"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
NIP-92는 사용자가 URL과 해당 리소스를 설명하는 인라인 메타데이터 태그를 포함하여 Nostr 이벤트에 미디어 파일을 첨부할 수 있게 한다.

## 작동 방식

사용자는 이벤트 content에 미디어 URL을 직접 배치한다. 예를 들어 kind `1` 텍스트 노트에 넣을 수 있다. 그런 다음 매칭되는 `imeta` 태그가 해당 URL에 대한 기계 판독 가능한 세부 정보를 추가한다. 클라이언트는 이 메타데이터를 사용하여 미리보기를 렌더링하고, 레이아웃 공간을 예약하고, 노트가 이미 화면에 표시된 후 파일 속성을 추측하는 것을 피할 수 있다.

각 `imeta` 태그는 이벤트 content의 URL 하나와 매칭되어야 한다. 클라이언트는 매칭되지 않는 태그를 무시할 수 있으며, 이는 오래되거나 잘못된 메타데이터를 거부하는 간단한 규칙을 구현에 제공한다.

## imeta 태그

각 `imeta` 태그에는 `url`과 최소 하나의 다른 필드가 있어야 한다. 지원되는 필드는 다음과 같다:

- `url` - 미디어 URL (필수)
- `m` - 파일의 MIME 유형
- `dim` - 이미지 크기 (가로 x 세로)
- `blurhash` - 미리보기 생성용 Blurhash
- `alt` - 접근성을 위한 대체 텍스트 설명
- `x` - SHA-256 해시 (NIP-94에서 유래)
- `fallback` - 기본 URL 실패 시 대체 URL

`imeta`는 [NIP-94: File Metadata](/ko/topics/nip-94/)의 필드를 포함할 수 있으므로, 클라이언트는 독립 파일 메타데이터 이벤트에서 이미 이해하는 것과 동일한 MIME 유형, 크기, 해시, 접근성 텍스트를 재사용할 수 있다.

## 왜 중요한가

가장 직접적인 이점은 다운로드 전 더 나은 렌더링이다. `dim`이 있으면 클라이언트는 파일 로드 후 타임라인을 재배치하는 대신 이미지나 비디오에 적절한 공간을 미리 예약할 수 있다. `blurhash`가 있으면 저비용 미리보기를 먼저 표시할 수 있다. `alt`가 있으면 스크린 리더 및 저시력 사용자도 첨부 파일을 사용할 수 있다.

NIP-92는 게시물 자체를 진실의 원천(source of truth)으로 유지할 수 있게 한다. URL이 `content`에 남아 있으므로 이전 클라이언트에서도 일반 링크가 표시되고, 새로운 클라이언트에서는 같은 노트를 더 풍부한 미디어 카드로 업그레이드할 수 있다.

## 상호운용성 참고사항

NIP-92는 인라인 메타데이터이지 별도의 미디어 객체 형식이 아니다. 클라이언트가 자체 이벤트를 가진 재사용 가능한 파일 레코드가 필요하다면, [NIP-94: File Metadata](/ko/topics/nip-94/)가 더 적합하다.

## 예시

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**주요 출처:**
- [NIP-92 명세](https://github.com/nostr-protocol/nips/blob/master/92.md)
- [Primal Android PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) - 크기 및 종횡비 처리에 대한 구체적인 클라이언트 구현

**언급된 뉴스레터:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: News](/en/newsletters/2026-01-21-newsletter/#news)

**같이 보기:**
- [NIP-94: File Metadata](/ko/topics/nip-94/)
