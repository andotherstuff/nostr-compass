---
title: "NIP-82: 소프트웨어 애플리케이션"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-82.md
translationDate: 2026-07-01
categories:
  - Discovery
  - Apps
---

NIP-82는 Nostr 클라이언트가 애플리케이션 (Android APK, iOS 앱, 웹 앱, 데스크톱 바이너리)을 피드와 발견 표면에서 일급 객체로 렌더링할 수 있도록 소프트웨어 애플리케이션 이벤트를 정의한다. 이 spec은 일반 kind 1 노트나 [NIP-89](/ko/topics/nip-89/) 핸들러 추천을 통해 앱을 설명하는 이전 접근 방식을, 애플리케이션 메타데이터, 스크린샷, 저장소 링크 및 저자 신원을 담는 전용의 구조화된 이벤트로 대체한다.

## 작동 방식

NIP-82 소프트웨어 애플리케이션은 저자 pubkey와 `d` tag로 주소가 지정되는 단일 대체 가능 이벤트이다. 이벤트는 다음을 담는다:

- 표시용 `name`, `description`, `icon`, `image` tag
- 소스 및 홈페이지 URL용 `repository` 및 `web` tag
- 지원되는 대상 (android, ios, web, linux, macos, windows)을 열거하는 `platforms` tag
- 각 플랫폼별 바이너리 또는 웹 URL용 `download` tag
- 애플리케이션 스크린샷의 이미지 URL을 담는 `screenshots` tag
- 분류용 `t` 토픽 tag
- 현재 게시된 버전용 `version` tag

NIP-82 피드를 탐색하는 클라이언트는 애플리케이션 카드를 표시하고, 정규 저장소로 링크하고, Nostr 장문 게시물이나 타사 앱 스토어를 스크래핑하는 것으로 대체하지 않고도 스크린샷을 표시할 수 있다. 저자 pubkey는 애플리케이션의 진실 소스이므로, 클라이언트는 다운로드 링크를 홍보하기 전에 게시자가 예상 개발자 신원과 일치하는지 확인할 수 있다.

## 피드 시맨틱

NIP-82 이벤트는 주소 지정 가능하므로, 각 애플리케이션에는 저자당 하나의 정규 대체 가능 이벤트가 있다. 새 버전을 게시하는 개발자는 이전 이벤트를 제자리에서 대체하고, 구독자는 이벤트 이력을 관리하지 않고도 업데이트를 본다. 변경 로그를 원하는 클라이언트는 주소 지정 가능 이벤트를 구독하고 버전 범프를 애플리케이션 표면의 활동으로 렌더링할 수 있다.

이 spec은 [NIP-89](/ko/topics/nip-89/) (Application Handlers)와 결합한다: NIP-82 이벤트는 애플리케이션을 아티팩트로 설명하는 반면, NIP-89 이벤트는 해당 애플리케이션이 특정 event kind를 처리할 수 있음을 설명한다. 클라이언트는 다른 하나 없이 하나를 사용할 수 있지만, 이 쌍은 함께 작동하는 발견 표면 (NIP-82)과 위임 표면 (NIP-89)을 제공한다.

## 구현

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)은 상세 화면, 저자 정보 및 스크린샷이 있는 전용 NIP-82 소프트웨어 애플리케이션 피드를 출시했다 ([PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036), [PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078), [PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200))

---

**주요 출처:**
- [NIP-82 명세](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - 전용 피드와 함께 NIP-82 소프트웨어 애플리케이션 지원 추가
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - 전용 NIP-82 소프트웨어 앱 상세 화면 추가
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - 저자 정보 및 스크린샷으로 NIP-82 소프트웨어 앱 UI 개선

**언급된 곳:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ko/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**참고:**
- [NIP-89: Application Handlers](/ko/topics/nip-89/)
