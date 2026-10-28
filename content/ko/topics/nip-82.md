---
title: "제안된 NIP-82(미할당): 소프트웨어 애플리케이션 카탈로그"
date: 2026-06-17
lastmod: 2026-10-28
translationOf: /en/topics/nip-82.md
translationDate: 2026-10-28
draft: false
categories:
  - Proposals
  - Apps
---

이 페이지에서 설명하는 소프트웨어 애플리케이션 카탈로그는 검토 중인 제안입니다. 승인된 NIP가 아닙니다. 이 제안은 "Zapstore spec"이라는 제목의 [nostr-protocol/nips 풀 리퀘스트 #2526](https://github.com/nostr-protocol/nips/pull/2526)에 있습니다. 이 페이지의 마지막 업데이트 시점 기준으로 해당 풀 리퀘스트는 열려 있고 병합되지 않았으며, 공식 NIPs master 브랜치에는 `82.md` 파일이 없습니다. "NIP-82"는 이 제안이 스스로 붙인 명칭입니다. 공식 NIP 번호가 아닙니다. 병합이 이루어지기 전에 event kind, tag, 동작이 바뀔 수 있습니다. 해당 풀 리퀘스트는 이전의 [풀 리퀘스트 #1336](https://github.com/nostr-protocol/nips/pull/1336)을 대체한다고 밝히고 있습니다.

## 제안된 event kind

초안은 소프트웨어 카탈로그를 여러 종류의 event로 나눕니다.

- **Kind 32267, 애플리케이션:** 앱을 설명하는 addressable event입니다.
- **Kind 30063, 릴리스:** 해당 앱의 한 버전에 대한 addressable event입니다. 그 버전의 에셋을 참조합니다.
- **Kind 3063, 에셋:** 다운로드 가능한 파일 하나를 설명하는 일반(regular) event입니다.
- **Kind 30267, 큐레이션:** 큐레이터가 앱을 묶거나 추천하기 위해 게시하는 addressable 목록입니다.
- **Kind 30509, 서명 인증서 링크:** APK 서명 인증서 같은 X.509 인증서를 소프트웨어를 게시하는 Nostr 키에 연결하는 addressable event로, 클라이언트가 해당 게시자가 어떤 인증서를 통제하는지 알 수 있게 해 줍니다. 이 event의 `d` tag는 DER 인코딩된 인증서의 SHA-256 해시입니다. 인증서의 개인 키로 만든 서명과 Unix 타임스탬프 형식의 만료 시점을 담고 있으며, 선택적으로 링크를 폐기됨으로 표시할 수 있습니다.
- **Kind 10067, relay 목록:** 카탈로그 event를 찾을 수 있는 relay들의 replaceable 목록입니다.

## 플랫폼, 무결성, 유효성

에셋 event에는 플랫폼 및 런타임 식별자가 들어 있어, 클라이언트가 기기에 맞는 파일만 보여 줄 수 있습니다. 각 에셋에는 파일 해시도 포함됩니다. 클라이언트는 이 해시로 다운로드한 바이트가 게시자가 서명한 내용과 일치하는지 확인할 수 있습니다. Android 패키지의 경우 초안에 서명 인증서 지문이 포함됩니다. 설치 프로그램은 업데이트를 제안하기 전에 이 지문을 이미 설치된 앱의 인증서와 비교할 수 있습니다. Android 패키지를 설치하기 전에 클라이언트는 인증서 해시로 kind 30509 event를 가져와야 합니다(SHOULD). 또한 그 인증서 서명을 APK에 내장된 인증서 및 에셋의 게시자와 대조해 검증하고, 증명이 만료되거나 폐기되지 않았는지 확인해야 합니다.

## 신뢰의 한계

유효한 서명이 보여 주는 것은 특정 키가 event를 게시했다는 사실뿐입니다. 그 키가 실제 개발자의 것이라거나, 소프트웨어가 안전하다거나, 큐레이터의 목록을 신뢰할 수 있다는 것까지 증명하지는 않습니다. 이 제안은 임의의 게시자에 대해 아무것도 보장하지 않습니다. 어떤 게시자 키와 큐레이터 키를 신뢰할지는 클라이언트와 사용자가 결정해야 합니다. 이 페이지는 어떠한 보안 감사나 프로덕션 환경에서의 상호 운용성도 주장하지 않습니다.

## NIP-89와의 관계

[NIP-89](/ko/topics/nip-89/) 핸들러 event는 어떤 애플리케이션이 어떤 event kind를 처리할 수 있는지 알립니다. 반면 이 제안은 소프트웨어 아티팩트와 그 입수처를 설명하므로, 두 사양은 서로 다른 관심사를 다룹니다.

---

**1차 출처:**
- [nostr-protocol/nips PR #2526: Zapstore spec](https://github.com/nostr-protocol/nips/pull/2526) (열림, 미병합; [PR #1336](https://github.com/nostr-protocol/nips/pull/1336)을 대체)

**언급된 곳:**
- [뉴스레터 #27: Amethyst v1.12.0 릴리스 소개(과거 참고 자료)](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [뉴스레터 #46: NIP-82로 제안된 소프트웨어 애플리케이션 카탈로그](/ko/newsletters/2026-10-28-newsletter/#software-application-catalog-proposed-as-nip-82)

**함께 보기:**
- [NIP-89: 애플리케이션 핸들러](/ko/topics/nip-89/)
