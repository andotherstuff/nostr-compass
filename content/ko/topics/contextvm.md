---
title: "ContextVM"
date: 2026-02-25
translationOf: /en/topics/contextvm.md
translationDate: 2026-03-07
draft: false
categories:
  - Infrastructure
  - AI
  - Protocol
---
ContextVM은 MCP(Model Context Protocol) 트래픽을 Nostr를 통해 전송하기 위한 프로토콜이자 도구 모음이다. MCP 클라이언트와 서버가 중앙 레지스트리, 도메인, OAuth에 의존하지 않고 서로를 발견하고 서명된 메시지를 교환할 수 있게 한다.

## 작동 방식

ContextVM SDK는 MCP over Nostr를 위한 TypeScript 클라이언트 및 서버 트랜스포트를 제공한다. 기존 MCP 서버는 기존 트랜스포트를 그대로 사용하면서 게이트웨이를 통해 Nostr에 노출할 수 있고, 네이티브 Nostr를 지원하지 않는 클라이언트는 프록시 레이어를 통해 연결할 수 있다.

릴레이는 메시지 버스 역할을 한다. 이벤트를 라우팅하고, 서명과 암호화로 엔드포인트 인증과 전송 프라이버시를 제공한다.

## 구성 요소

**SDK**: 클라이언트/서버 트랜스포트, 프록시 지원, 로컬 MCP 서버를 Nostr에 연결하는 게이트웨이 기능이 포함된 TypeScript 라이브러리.

**CVMI**: 서버 발견 및 메서드 호출을 위한 커맨드라인 인터페이스.

**Relatr**: 소셜 그래프 거리와 프로필 검증을 기반으로 개인화된 점수를 계산하는 신뢰 점수 서비스.

## 왜 중요한가

ContextVM은 MCP 자체를 대체하는 것이 아니라 트랜스포트 브릿지이다. 기존 MCP 서버가 도구 스키마나 비즈니스 로직을 재작성하지 않고도 Nostr 접근성을 확보할 수 있어 도입 비용을 낮춘다.

최근 ContextVM 작업은 gift-wrapped 트래픽을 위한 임시(ephemeral) 전달도 추진했다. 도구 호출이나 중간 응답처럼 내구적 릴레이 저장이 불필요하고 추가 프라이버시 노출이 될 수 있는 경우에 유용하다.

## 상호운용성 참고사항

2026년 2~3월에 프로젝트는 구현에서 표준화 단계로 이동했다. 팀은 MCP JSON-RPC over Nostr와 gift wrap의 임시 변형에 대한 NIP 제안을 제출했다. 이 제안이 변경되더라도, 프로토콜 경계를 더 명확하게 보여준다: MCP는 애플리케이션 레이어로 남고, Nostr는 발견과 전송을 담당한다.

---

**주요 출처:**
- [ContextVM 웹사이트](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245: Ephemeral Gift Wrap](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**언급된 뉴스레터:**
- [뉴스레터 #11: ContextVM 소식](/en/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [뉴스레터 #12](/en/newsletters/2026-03-04-newsletter/)

**같이 보기:**
- [NIP-90: Data Vending Machines](/ko/topics/nip-90/)
