---
title: "NIP-34: Git 협업"
date: 2026-02-04
translationOf: /en/topics/nip-34.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Development
---
NIP-34는 Nostr 릴레이에서 git 저장소, 패치, 이슈를 호스팅하기 위한 이벤트 종류를 정의한다. GitHub이나 GitLab 같은 중앙화 호스팅 플랫폼에 의존하지 않고 완전히 탈중앙화된 코드 협업을 가능하게 한다.

## 작동 방식

저장소는 이름, 설명, clone URL 등의 메타데이터를 포함하는 주소 지정 가능 이벤트(kind 30617)로 표현된다. 저장소 소유자는 이 이벤트를 게시하여 Nostr에 프로젝트를 등록한다.

패치(kind 1617)는 저장소에 적용할 수 있는 `git format-patch` 내용을 담는다. 기여자는 대상 저장소를 참조하는 이벤트로 패치를 제출한다. 이 방식은 Linux 커널 같은 프로젝트에서 사용하는 이메일 기반 패치 워크플로와 유사하다.

이슈(kind 1621)는 전통적인 이슈 트래커와 같은 기능을 한다. Pull request는 kind 1618, 1619를 사용하고, 상태 업데이트는 1630~1633을 사용한다. 이슈, 패치, pull request에 대한 답글은 [NIP-22](/ko/topics/nip-22/) 댓글을 사용한다.

## 이벤트 종류

- **30617** - 저장소 공지 (주소 지정 가능)
- **30618** - 브랜치 및 태그에 대한 저장소 상태 공지
- **1617** - 패치 제출
- **1618** - Pull request
- **1619** - Pull request 업데이트
- **1621** - 이슈
- **1630-1633** - 열림, 병합/해결, 닫힘, 초안 상태 이벤트

## 왜 중요한가

NIP-34는 탐색과 전송을 분리한다. 실제 저장소는 일반 Git 서버에 그대로 둘 수 있지만, Nostr 이벤트가 릴레이에 분산된 탐색, 토론, 패치 교환, 상태 추적 계층을 제공한다. 프로젝트가 하나의 포지(forge) 데이터베이스나 API에 의존하지 않으면서 git 네이티브 도구를 계속 사용할 수 있다는 뜻이다.

가장 초기의 고유 커밋을 가리키는 `r` 태그는 가장 중요한 세부사항 중 하나다. 이를 통해 클라이언트가 동일한 저장소 계보를 나타내는 미러와 포크를 그룹화할 수 있으며, 이는 이름만으로는 추론하기 어렵다.

## 구현 현황

- **ngit** - 저장소와 패치를 Nostr에 게시하는 커맨드라인 도구
- **gitworkshop.dev** - Nostr 호스팅 저장소를 탐색하는 웹 인터페이스
- **Notedeck** - [NIP-34 뷰어 초안 지원](https://github.com/damus-io/notedeck/pull/1279)이 있는 데스크톱 클라이언트

---

**주요 출처:**

- [NIP-34 명세](https://github.com/nostr-protocol/nips/blob/master/34.md)

**언급된 뉴스레터:**

- [뉴스레터 #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Notedeck NIP-34 뷰어 추가
- [뉴스레터 #9: Notedeck](/en/newsletters/2026-02-11-newsletter/#notedeck)

**같이 보기:**
- [NIP-22: 댓글](/ko/topics/nip-22/)
