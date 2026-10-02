---
title: "FIPS 공개 도메인"
date: 2026-09-30
translationOf: /en/topics/fips-pub-domains.md
translationDate: 2026-10-02
draft: false
categories:
  - Protocol
  - Networking
  - Identity
---

fips-pub-domains는 익숙한 인터넷 도메인 이름을 [FIPS](/ko/topics/fips/) 메시 서비스로 해석하기 위한 초기 구현체다. 서명된 Nostr 클레임을 게시하지만, 서명은 누가 클레임을 만들었는지만 증명한다. 클라이언트는 클레임 작성자를 도메인 소유자로 취급하기 전에 DNS 또는 DNSSEC 증거, 신뢰할 수 있는 증인, 또는 이전에 고정해 둔 바인딩도 확인해야 한다.

## 검증과 오프라인 사용 {#verification-and-offline-use}

[첫 릴리스](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0)는 클레임, 리졸버 데몬, Android 통합을 추가했다. [버전 0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0)은 클레임에 DNSSEC 증명을 첨부할 수 있어, 메시 relay만 볼 수 있는 클라이언트도 이전에 본 적 없는 서명된 도메인을 DNS 루트 키에 대조해 검증할 수 있다. 또한 하나의 도메인에 둘 이상의 검증된 서버를 지원한다. [버전 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1)은 패키지에 포함된 서버 유닛을 수정하고 root 권한 없이 실행되도록 변경했으며, 기존 설치에는 교체된 유닛이 필요하다.

프로젝트의 [테스트 노트](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)는 2노드 사례와 메시 전용 relay 사례를 설명한다. 이는 유지관리자가 보고한 테스트이며, 더 넓은 배포의 증거는 아니다. 이 프로젝트의 [NIP-DB 제안](https://github.com/nostr-protocol/nips/pull/2487)은 아직 열려 있고, 초안의 event kind 번호는 할당된 Nostr kind가 아니라 임시 값이다.

---

**주요 출처:**
- [저장소와 README](https://github.com/fr34aky/fips-pub-domains)
- [릴리스 0.1.0–0.2.1](https://github.com/fr34aky/fips-pub-domains/releases)
- [제안된 NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [테스트 노트](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**언급된 뉴스레터:**
- [Newsletter #42: fips-pub-domains](/ko/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**같이 보기:**
- [FIPS](/ko/topics/fips/)
