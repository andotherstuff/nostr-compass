---
title: "CLINK: Nostr 키를 위한 공통 Lightning 인터페이스"
date: 2026-06-17
draft: false
translationOf: /en/topics/clink.md
translationDate: 2026-07-01
categories:
  - Payments
  - Lightning
---

CLINK (Common Lightning Interface for Nostr Keys)는 발신자가 단일 noffer 인터페이스를 사용하여 Nostr 키 기반 신원에게 결제할 수 있도록 하는 제안된 결제 요청 형식이다. CLINK noffer는 수신자의 Nostr 공개 키와 함께 발신자의 지갑이 Lightning 결제, 온체인 결제 또는 향후 정산 프리미티브를 구성하여 수신자에게 전달할 수 있도록 하는 라우팅 메타데이터를 인코딩한다. 수신자는 신원당 하나의 noffer를 게시하고, 발신자는 수신 지갑이 Lightning, 온체인 또는 다른 경로로 정산하는지 알지 못한 채 이를 결제한다.

## 작동 방식

CLINK noffer는 발신자의 지갑이 구체적인 결제 지시로 디코딩하는 구조화된 결제 요청이다. noffer는 다음을 포함한다:

- 정규 신원 루트로서의 수신자 Nostr 공개 키
- 하나 이상의 결제 엔드포인트 (Lightning 노드 URI, 온체인 주소 파생 힌트, 향후 경로)
- 결제에 대한 선택적 메타데이터 (메모, 금액, 만료)
- noffer를 수신자의 Nostr 신원에 바인딩하는 수신자의 서명

CLINK를 지원하는 발신 지갑은 noffer를 읽고, 자신이 처리할 수 있는 경로를 선택한 뒤 (Lightning 전용 지갑은 Lightning 엔드포인트로 결제하고, 다중 경로 지갑은 가장 저렴한 경로를 선택), 결제를 제출한다. 수신자의 지갑은 해당 완료 이벤트를 게시하거나 조회하여 수신을 확인하며, Nostr 공개 키는 경로 간에 지속되는 신원 역할을 한다.

## Nostr 키 기반 인터페이스인 이유

LNURL과 BOLT-12는 이미 Lightning 결제 요청 형식으로 존재하며, Bitcoin에는 온체인 정산을 위한 잘 알려진 주소 형식이 있다. CLINK는 어느 것도 대체하지 않는다. Nostr 키를 루트로 하는 계층을 추가하여, 발신자가 수신자를 Nostr 신원으로 지정하고 지갑이 사용할 하위 경로를 결정하도록 한다. Lightning 공급자를 변경하거나, 새로운 mint를 열거나, 온체인 지갑을 이전한 사용자는 동일한 Nostr 키로 noffer를 다시 게시하며, 발신자는 주소록을 업데이트할 필요가 없다.

Zeus Pay (모든 계정에 대해 CLINK noffer를 생성)의 경우, 이는 발신자가 Nostr 키만으로 어떤 Zeus 사용자에게든 결제할 수 있음을 의미한다. Amethyst의 온체인 zap 드라이버의 경우, CLINK 검증 상태 머신은 온체인의 서명된 noffer가 zap 요청에서 주장하는 Nostr pubkey와 일치하는지 확인하여, 서명되지 않은 온체인 zap에 대한 위조 경로를 차단한다.

## 구현

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1)은 CLINK noffer 결제 지원을 출시했으며, Zeus Pay는 모든 계정에 대해 CLINK noffer를 생성하여 발신자가 Nostr 키만으로 어떤 Zeus 사용자에게든 결제할 수 있도록 한다
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)은 검증 상태 머신과 재검증 드라이버를 갖춘 온체인 zap 검증용 CLINK 드라이버를 출시했다 ([PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039), [PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177), [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182))

---

**주요 출처:**
- [Zeus v13.1.0-rc1 릴리스 노트](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - CLINK noffer 출시
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - NIP-BC 온체인 zap 검증 상태 머신 및 재검증 드라이버
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - CLINK (Common Lightning Interface for Nostr Keys) 구현
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - CLINK 프로토콜 DTO에 대한 kotlinx-serialization 지원 추가

**언급된 곳:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ko/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #27: Zeus v13.1.0-rc1 ships CLINK noffers and queue-less NWC](/ko/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**참고:**
- [NIP-57: Zaps](/ko/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)
