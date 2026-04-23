---
title: "Marmot Protocol"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot은 Nostr 위의 end-to-end encrypted 그룹 메시징 프로토콜입니다. Nostr의 신원과 릴레이 네트워크를 MLS와 결합해 그룹 키 관리, forward secrecy, post-compromise security를 제공합니다.

## 작동 방식

Marmot은 신원, 릴레이 transport, 이벤트 배포에는 Nostr를 사용하고, 그 위에 MLS를 올려 그룹 멤버십 변경과 메시지 암호화를 처리합니다. 일대일 메시징에 초점을 둔 [NIP-17](/ko/topics/nip-17/)과 달리, Marmot은 구성원이 시간에 따라 참여하고 떠나고 키를 교체하는 그룹을 위해 설계되었습니다.

## 왜 중요한가

MLS는 Nostr의 DM 방식만으로는 제공되지 않는 속성을 Marmot에 부여합니다. 그룹 상태 진화, 멤버 제거 의미론, 이후 키 업데이트를 통한 침해 후 복구가 그것입니다.

핵심 통찰은 이 역할 분담입니다. Nostr는 개방형 네트워크에서 신원과 transport를 해결하고, MLS는 인증된 그룹 키 합의를 해결합니다. Marmot은 둘을 연결하는 접착 계층입니다.

## 구현 현황

프로토콜은 여전히 실험적이지만, 이제 여러 구현체와 실제 애플리케이션 사용이 있습니다. [MDK](https://github.com/marmot-protocol/mdk)는 주요 Rust 레퍼런스 스택이고, [marmot-ts](https://github.com/marmot-protocol/marmot-ts)는 이를 TypeScript로 가져오며, [White Noise](https://github.com/marmot-protocol/whitenoise), [Amethyst](https://github.com/vitorpamplona/amethyst), Pika, Vector 같은 앱들이 Marmot 호환 구성 요소를 사용해 왔습니다.

최근 작업은 hardening과 interop에 집중되어 왔습니다. 감사 기반 수정이 2026년 초에 반영되었고, MIP-03은 concurrent group state change가 릴레이를 통해 경합할 때 클라이언트가 수렴할 수 있도록 결정적 commit 해석을 도입했습니다.

2026년 4월에는 Amethyst가 내장 MDK를 MIP-01과 MIP-05 wire format에 맞췄습니다. [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462)는 TLS 스타일 length prefix의 VarInt 인코딩과 MDK test vector에 대한 round-trip 검증을 추가했고, [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435)는 MIP-00 KeyPackage Relay List 지원을 더했으며, [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436)은 White Noise와의 cross-client 테스트에서 드러난 남은 admin-gate 및 media 처리 공백을 메웠습니다. [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466)은 암호화된 welcome 바이트가 mdk-core 출력과 일치하도록 MLS commit framing을 수정했고, [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471)은 공동 관리자의 상태 분기를 유발하던 outer-layer 복호화 버그를 고쳤습니다. 후속 [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493)은 포괄적인 MLS commit cryptography 검증을 추가했고, [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488)은 Amethyst 구현에 기반한 Marmot/MLS 그룹 작업용 CLI인 `amy`를 배포했습니다.

MDK는 [PR #261](https://github.com/marmot-protocol/mdk/pull/261)에서 그룹의 `RequiredCapabilities`를 초대 대상 capability의 LCD로 계산해 Amethyst와 White Noise 사이의 mixed-version invite를 가능하게 했고, [PR #262](https://github.com/marmot-protocol/mdk/pull/262)에서는 생성자의 signer를 저장하기 전에 invitee key package를 파싱하도록 했으며, [PR #264](https://github.com/marmot-protocol/mdk/pull/264)에서는 구현체 간 SelfUpdate wire format을 수렴시켰고, [PR #265](https://github.com/marmot-protocol/mdk/pull/265)에서는 `group_required_proposals` accessor를 노출했습니다.

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)는 글로벌 singleton에서 계정별 `AccountSession` 뷰로 옮기는 다단계 리팩터링의 한가운데 있습니다. [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743)은 `AccountSession`과 `AccountManager` 기반을 놓았고, 후속 단계들은 릴레이 핸들, draft와 settings, message ops, 그룹 읽기와 쓰기, 멤버십, push notification, key-package 읽기, 그룹 생성, 그리고 [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770) 기준 session-scoped 이벤트 디스패치까지 옮겼습니다. [marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68)은 TypeScript 클라이언트를 addressable kind `30443` key package로 옮깁니다.

---

**주요 출처:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit (MDK)](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [White Noise client](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - MIP-01/MIP-05 wire format alignment
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - Amy CLI

**언급된 뉴스레터:**
- [Newsletter #1: News](/ko/newsletters/2025-12-17-newsletter/)
- [Newsletter #1: Releases](/ko/newsletters/2025-12-17-newsletter/)
- [Newsletter #4](/ko/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/ko/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/ko/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Amethyst MIP compliance](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: MDK interop work](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: whitenoise-rs session refactor](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [MLS (Message Layer Security)](/ko/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/ko/topics/mip-05/)
- [NIP-17: 비공개 DM](/ko/topics/nip-17/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
