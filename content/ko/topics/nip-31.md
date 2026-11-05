---
title: "NIP-31: 알 수 없는 이벤트 종류 처리"
date: 2026-11-04
draft: false
translationOf: /en/topics/nip-31.md
translationDate: 2026-11-05
categories:
  - NIPs
  - Protocol
---

> **상태 경고:** 현재 [NIP-31 명세](https://github.com/nostr-protocol/nips/blob/master/31.md)는 스스로를 "불필요하게 비대하다"는 이유로 `unrecommended`로 표시하고 있으며, 상태 줄에는 draft, unrecommended, optional로 적혀 있습니다. 릴레이에는 이미 이 관례를 따르는 이벤트가 저장되어 있으므로, 이 페이지에서는 클라이언트가 그런 이벤트를 어떻게 읽는지 설명합니다. 새 프로토콜에 NIP-31을 권장하지는 않습니다.

NIP-31은 최상위 `alt` 태그를 정의합니다. 이 태그에는 일반 텍스트 노트로 읽히도록 의도되지 않은 사용자 정의 이벤트 종류에 대한 짧은 평문 요약이 들어갑니다.

## 작동 방식 {#how-it-works}

사용자 정의 종류 이벤트의 작성자는 사람이 읽을 수 있는 레이블을 담은 `alt` 태그를 추가합니다. kind 1 중심으로 만들어진 클라이언트는 인식하지 못하는 모든 종류를 구독할 필요가 없습니다. 그래도 노트가 그런 이벤트를 참조하면 사용자가 해당 이벤트를 마주칠 수 있으며, 클라이언트가 그 종류를 구현하지 않았더라도 레이블이 어느 정도 맥락을 제공합니다.

완전한 이벤트가 아닌 태그 일부:

```
["alt", "<short plaintext summary>"]
```

읽을 수 있는 레이블은 표시만 담당합니다. 투표를 하거나, 지갑 요청을 처리하거나, 그 종류 고유의 다른 동작을 수행할 수는 없습니다. 더 풍부한 상호작용을 위해 명세는 [NIP-89: 권장 애플리케이션 핸들러](/ko/topics/nip-89/)를 안내합니다.

## 구현 {#implementations}

noStrudel의 [커밋 7c68acf 시점 unknown-event 카드](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)에서는 첫 번째 `alt` 태그의 앞뒤 공백을 제거한 값이 주 레이블이 되며, 선택적으로 `Using <client>` 줄이 붙습니다. 값이 없거나 비어 있으면 `Unknown event (kind ...)`가 표시되고, 콘텐츠는 최대 세 줄까지 별도로 나타납니다. 같은 컴포넌트는 NIP-89 핸들러 템플릿을 통해 `client` 태그를 해석합니다. 공유 가능한 주소가 있으면 Open 버튼을, 유효한 핸들러 링크가 해석되면 `Open in <client>`를 표시합니다. 설명과 앱 전환은 별개의 컨트롤입니다.

Amethyst의 [커밋 553f761 시점 UnknownEventDigest.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170)는 산문으로 분류한 콘텐츠를 우선 사용하고, 없으면 `alt`로 대체합니다. 파서는 값의 앞뒤 공백을 제거하고 비어 있지 않은 첫 번째 `alt`를 가져옵니다. 그 결과 첫 번째 `alt`가 비어 있는 이벤트는 여기서 noStrudel과 다른 레이블을 받을 수 있습니다. 두 설명 모두 해당 커밋 시점의 소스 코드를 반영한 것입니다. 어느 쪽도 릴리스된 버전의 동작을 확인해 주지는 않습니다.

## 한계 {#limits}

- `alt`는 태그이므로 [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)에 정의된 이벤트 ID와 서명이 이를 포함합니다. 유효한 서명은 작성자가 그 레이블을 게시했다는 사실을 보여 줍니다. 레이블이 정확하다는 것까지 보여 주지는 않으므로 요약이 오해를 불러일으킬 수 있습니다.
- 태그는 공개됩니다. 콘텐츠가 암호화된 이벤트에 붙은 `alt`는 요약을 노출하며, 콘텐츠가 숨기는 내용을 드러낼 수 있습니다.
- 위의 두 속성은 모두 NIP-01 이벤트 구조에서 비롯됩니다. NIP-31 본문은 이를 요구 사항으로 명시하지 않습니다.
- 최상위 `alt` 태그는 `imeta` 안의 이미지 설명용 `alt` 필드와 다르며, 렌더러는 둘을 따로 파싱합니다.

---

**1차 자료:**
- [NIP-31 명세](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [커밋 7c68acf 시점 noStrudel embedded-unknown.tsx](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [커밋 553f761 시점 Amethyst UnknownEventDigest.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**언급된 곳:**
- [뉴스레터 #47: NIP 심층 분석](/ko/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**함께 보기:**
- [NIP-89: 권장 애플리케이션 핸들러](/ko/topics/nip-89/)
- [NIP-73: 외부 콘텐츠 ID](/ko/topics/nip-73/)
- [NIP-01: 기본 프로토콜 흐름 설명](/ko/topics/nip-01/)
