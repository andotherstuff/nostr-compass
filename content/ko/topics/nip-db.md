---
title: "제안된 NIP-DB: 도메인 서비스 바인딩"
date: 2026-09-30
translationOf: /en/topics/nip-db.md
translationDate: 2026-10-02
draft: false
categories:
  - Proposals
  - Networking
  - Identity
---

NIP-DB는 일반 인터넷 도메인을 키로 주소가 지정되는 서비스에 바인딩하기 위한 **열린 제안**이다. event kind와 문구는 아직 검토 대상이며, 이 페이지는 이를 채택된 Nostr 명세로 제시하지 않는다.

## 검증 모델 {#verification-model}

서비스를 제공하는 키는 도메인과 서비스를 명시한 서명된 클레임을 게시할 수 있다. 제안은 선택적인 DNS 또는 DNSSEC 증거, 증인 증명, 그리고 해당 도메인 아래 이름을 위한 존 레코드를 설명한다. 서명은 어떤 키가 클레임을 게시했는지 증명하지만 도메인에 대한 통제권은 증명하지 않는다. 클라이언트는 이름 해석에 바인딩을 사용하기 전에 DNS 증거, 신뢰할 수 있는 증인, 또는 이전에 고정해 둔 키로 바인딩을 검증해야 한다.

[fips-pub-domains](/ko/topics/fips-pub-domains/)는 FIPS 메시를 위한 작성자의 참조 구현체다. 문서화된 2노드 테스트와 메시 전용 테스트는 유지관리자가 보고한 구현 증거다. 이 테스트들이 제안의 열린 검토를 마무리하거나 더 넓은 배포를 입증하지는 않는다.

---

**주요 출처:**
- [열린 NIP-DB 풀 리퀘스트](https://github.com/nostr-protocol/nips/pull/2487)
- [작성자의 초안과 임시 event kind 번호](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [참조 구현체와 테스트](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**언급된 뉴스레터:**
- [Newsletter #42: 공개 도메인](/ko/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [Newsletter #42: 제안된 NIP-DB](/ko/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
