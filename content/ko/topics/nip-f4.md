---
title: "NIP-F4: 팟캐스트"
date: 2026-06-03
draft: false
translationOf: /en/topics/nip-f4.md
translationDate: 2026-07-01
categories:
  - NIPs
  - Protocol
  - Media
---

NIP-F4는 Nostr 클라이언트가 팟캐스트 에피소드를 참조하고, 표시하고, 사회적으로 상호 작용하는 방법을 정의한다. 2년 3개월의 draft 기간을 거쳐 2026-05-28에 병합되었으며, 이 spec은 에피소드에 kind 54 이벤트를 사용하고 기존 RSS 팟캐스팅 스택을 보완 계층으로 설계한다.

## 작동 방식

kind 54 팟캐스트 에피소드 이벤트는 `title` tag, 선택적 `image` tag, `description` tag, 오디오 파일용 하나 이상의 `imeta` tag (URL, mime type, hash, 지속 시간, bitrate, 언어 코드, fallback URL, NIP-96 서비스 플래그), `t` 토픽 tag, 그리고 fallback 표시를 위한 NIP-31 `alt` tag를 담는다.

부하를 견디는 설계 선택은 `podcast:item:guid:<guid>` 형식을 사용하여 에피소드의 RSS GUID를 담는 `i` tag이다. 이는 다음을 가능하게 한다:

- Nostr 클라이언트가 kind 54 이벤트를 표시하고 이를 모든 RSS 인식 팟캐스트 앱의 동일한 에피소드로 다시 링크
- RSS 인식 Nostr 클라이언트가 팟캐스터에게 호스팅 이전을 강요하지 않고 기존 팟캐스트의 에피소드를 kind 54 이벤트로 표시
- Podcasting 2.0 `<podcast:socialInteract>` 및 `<podcast:chat>` tag를 통한 크로스 프로토콜 댓글 스레딩

## RSS와의 공존

PR 스레드에서의 2년간의 논쟁 (Podcasting 2.0 공동 저자 Dave Jones, Alex Gleason, fiatjaf, Mike Terenzio, Pablo F7z, Jeff Gardner와 함께)은 공존으로 결론지어졌다. Nostr는 사회 및 발견 계층을 제공하고 RSS는 오디오 파일과 피드 메타데이터의 진실 소스를 유지한다. Nostr는 RSS 배포 계층을 복제하지 않는다.

이는 RSS를 대체하려는 이전 시도 (JSONFeed, RSS 3.0, 독점 팟캐스트 API)와 대조된다. Podcasting 2.0 네임스페이스는 이미 노트 ID로 Nostr 이벤트를 참조하는 `<podcast:socialInteract>`를 지원하므로, RSS 피드는 Nostr가 피드 자체를 미러링하지 않고도 컴패니언 Nostr 토론 스레드를 선언할 수 있다.

## 이벤트 예시

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["imeta", "url https://podcast.example.com/audio/ep42.mp3", "m audio/mpeg", "x b2e0a7a82ac9f3f3a71f1d9a78c381d5be9d1cf19dce258765c17c8a76287c93", "duration 4523", "bitrate 192000", "l en ISO-639-1"],
    ["i", "podcast:item:guid:9b2a4c7d-1e3f-4a5b-8c9d-0e1f2a3b4c5d"],
    ["t", "podcasting"],
    ["alt", "Podcast episode: Why RSS Won (43 min)"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

## 구현

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - 에피소드 목록과 인라인 플레이어가 있는 전용 팟캐스트 화면 (첫 번째 주요 클라이언트 구현, 2026년 5월)
- [Wavlake](https://wavlake.com) - 가장 큰 Nostr 네이티브 음악 및 팟캐스팅 플랫폼, 팟캐스트 콘텐츠에 대해 kind 54와 정렬될 것으로 예상
- [Fountain](https://fountain.fm) - Bitcoin 팟캐스트 앱, RSS와 NIP-F4를 연결할 것으로 예상

## 미해결 질문

병합된 spec은 구현체가 수렴할 여러 설계 질문을 남겨 두었다:

- 크리에이터별 pubkey는 권장되지만 필수는 아니므로, 하나의 pubkey 아래 많은 크리에이터를 게시하는 Wavlake와 같은 플랫폼은 여전히 유효하다
- 에피소드별 댓글과 토론은 전용 에피소드 댓글 kind 대신 NIP-22 일반 스레딩과 kind 1 타임라인 노트를 사용한다
- 팟캐스트별 메타데이터 (호스트, 네트워크, 언어, 라이선스)는 게시자의 kind 0 메타데이터 또는 별도의 kind 54 팟캐스트 수준 레코드에 존재한다

---

**주요 출처:**
- [NIP-F4 명세](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - 2년간의 논의 후 2026-05-28에 병합된 원본 제안
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - 첫 번째 주요 클라이언트 구현

**언급된 곳:**
- [Newsletter #25: NIP Updates and Deep Dive](/ko/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ko/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**참고:**
- [NIP-22 (Comments)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Alt tags)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (File Metadata)](/ko/topics/nip-94/)
- [NIP-96 (HTTP File Storage)](/ko/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
