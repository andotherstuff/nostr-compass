---
title: "NIP-85: Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-02-18
draft: false
categories:
  - Protocol
  - Relays
---

NIP-85는 비용이 많이 드는 계산을 신뢰할 수 있는 서비스 제공자에게 위임하고, 서비스 제공자가 서명된 결과를 표준 Nostr event로 게시하는 시스템을 정의합니다. Web of Trust 점수와 참여도 메트릭은 여러 relay를 크롤링하고 대량의 event를 처리해야 하며, 이는 모바일 기기와 브라우저 클라이언트에서는 비실용적인 작업입니다.

## 작동 방식

NIP-85는 다양한 주체 유형에 대한 어서션을 위해 네 가지 event kind를 사용합니다. 사용자 어서션 (kind 30382)은 팔로워 수, 게시물/답글/리액션 수, zap 금액, 정규화 순위 (0-100), 공통 주제, 활동 시간을 담습니다. Event 어서션 (kind 30383)은 댓글 수, 인용 수, 리포스트, 리액션, zap 데이터로 개별 노트를 평가합니다. Kind 30384는 주소 지정 가능한 event에 참여도 메트릭을 적용하고, kind 30385는 [NIP-73](/ko/topics/nip-73/)을 통해 참조된 외부 식별자 (책, 영화, 웹사이트, 위치, 해시태그)를 평가합니다.

각 어서션은 `d` tag에 주체가 포함된 교체 가능한 주소 지정 가능 event입니다: pubkey, event ID, event 주소, 또는 NIP-73 식별자. 서비스 제공자는 자체 키로 이 event에 서명하고, 클라이언트는 신뢰 관계에 따라 평가합니다.

## 제공자 검색

사용자는 kind 10040 event를 게시하여 신뢰하는 어서션 제공자를 선언합니다. 각 항목은 제공자 pubkey와 relay 힌트, 선택적 알고리즘 변형과 함께 어서션 유형을 지정합니다. 사용자는 제공자 환경설정을 비공개로 유지하기 위해 [NIP-44](/ko/topics/nip-44/)를 사용하여 tag 목록을 암호화할 수 있습니다. 클라이언트는 팔로우한 계정들이 신뢰하는 제공자를 확인하여 제공자 목록을 구축하며, 어서션 제공자 자체를 위한 탈중앙화 평판 레이어를 만듭니다.

## 보안 모델

제공자는 별개의 알고리즘에 서로 다른 서비스 키를 사용해야 하며, 알고리즘이 개인화될 때는 사용자당 고유한 키를 사용해야 합니다. 각 서비스 키는 알고리즘의 동작을 설명하는 kind 0 메타데이터 event를 받아 사용자에게 투명성을 제공합니다.

## 현재 채택 현황

Primal의 캐시 서버가 참여도 메트릭과 Web of Trust 점수를 계산합니다. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal)이 NIP-85 event kind를 사용하여 이 계산들을 표준 Nostr 클라이언트에 브릿지합니다. [Nostr.band](https://nostr.band)가 명세 자체 예시에서 참조된 `wss://nip85.nostr.band` relay를 운영합니다. [Amethyst](https://github.com/vitorpamplona/amethyst)가 `quartz` 라이브러리에 실험적인 Trusted Assertions 지원을 갖추고 있습니다.

---

**주요 출처:**
- [NIP-85 명세](https://github.com/nostr-protocol/nips/blob/master/85.md)

**언급된 곳:**
- [뉴스레터 #10: NIP 업데이트](/ko/newsletters/2026-02-18-newsletter/#nip-업데이트)
- [뉴스레터 #10: NIP 심층 분석](/ko/newsletters/2026-02-18-newsletter/#nip-심층-분석-nip-85-trusted-assertions)

**참조:**
- [NIP-11: Relay 정보 문서](/ko/topics/nip-11/)
- [NIP-73: 외부 콘텐츠 ID](/ko/topics/nip-73/)
- [NIP-44: 암호화 직접 메시지 v2](/ko/topics/nip-44/)
