---
title: "Buzz NIP-FA: 연합 신원 어댑터"
date: 2026-10-21
draft: false
categories: ["NIPs"]
translationOf: /en/topics/nip-fa.md
translationDate: 2026-11-05
---

Buzz NIP-FA는 Buzz 프로젝트가 만든 선택적 초안 명세입니다. 공식 nostr-protocol/nips 저장소의 채택된 NIP에는 포함되지 않습니다.

이 명세는 Nostr 클라이언트와 엔터프라이즈 신원 어댑터 사이에 특정 제공자에 종속되지 않는 HTTP 계약을 정의합니다. 사용자가 브라우저로 로그인하면 어댑터가 해당 사용자의 세션을 유지합니다. 어댑터는 사용자를 Nostr 키에 결합하는 프로젝트 로컬 Buzz NIP-FI 어서션을 발급하며, 클라이언트는 [NIP-98](/ko/topics/nip-98/)로 그 키를 제어하고 있음을 증명합니다. [각 어서션의 수명은 운영자가 선택](https://github.com/block/buzz/pull/8934)합니다. 이 수명은 릴레이가 수용하는 발급자의 maximum_assertion_age를 준수해야 하며, exp는 어댑터 세션 만료 시각을 넘을 수 없습니다. 선택한 수명은 릴레이가 재시작된 후 폐기된 키가 재연결할 수 있는 기간의 상한이 되며, 클라이언트는 수명만을 이유로 어서션을 거부해서는 안 됩니다. NIP-FI와 공식 NIP는 변경되지 않습니다. 로그인에는 S256 핸드오프 챌린지와, 일회용 코드를 받는 `127.0.0.1` 또는 `[::1]`의 루프백 콜백이 사용됩니다. OIDC나 SAML 같은 업스트림 시스템은 어댑터 뒤에 위치합니다. 어떤 릴레이가 엔터프라이즈 신원을 요구하는지 찾는 방법은 다른 명세에 맡깁니다.

주요 출처: Buzz 저장소의 [NIP-FA 명세](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md).

## 에이전트 자격 증명 {#agent-credentials}

Buzz는 [소유자가 인가한 에이전트 자격 증명을 위한 NIP-FA 초안](https://github.com/block/buzz/pull/9015)을 병합했습니다. 이 초안은 소유자가 NIP-OA로 인가한 에이전트를 위한 그랜트, 어서션, 폐기 경로를 정의합니다. 그랜트는 소유자의 세션과 에이전트의 [NIP-98](/ko/topics/nip-98/) 증명을 짝짓는 RFC 8693 토큰 교환을 통해 발급됩니다. 어서션을 받을 때 에이전트는 자신의 증명과 함께 그랜트를 Bearer 토큰으로 제시하며, 클라이언트는 어서션의 `iss`를 그랜트의 발급자와 대조합니다. 에이전트 증명은 일회용이며 그랜트 경로와 어서션 경로에서만 사용됩니다. 폐기는 에이전트 증명 없이 소유자의 세션에서 수행되며, 에이전트 키와 해당 그랜트를 폐기하고 에이전트의 연결을 끊습니다. 그랜트 수명은 어댑터 정책이 결정합니다. 지원되지 않는 인가 조건은 거부되며, 폐기된 키는 다시 등록할 수 없습니다. NIP-FA는 채택된 NIP가 아니라 Buzz 명세입니다. 이번 병합은 소스에만 반영되었으며, 프로덕션 활성화, 릴리스된 빌드, 상호 운용성을 주장하지 않습니다.

## 주요 출처 {#primary-sources}

- [Buzz NIP-FA: 연합 신원 어댑터](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)

- [소유자가 인가한 에이전트 자격 증명 경로](https://github.com/block/buzz/pull/9015)

## 언급된 곳 {#mentioned-in}

- [뉴스레터 #47: Buzz 에이전트 자격 증명](/ko/newsletters/2026-11-04-newsletter/#buzz-defines-owner-authorized-agent-credential-routes)


- [뉴스레터 45](/en/newsletters/2026-10-21-newsletter/#buzz)
