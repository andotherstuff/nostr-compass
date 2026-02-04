---
title: "NIP-34 (Git 협업)"
date: 2026-02-04
description: "NIP-34는 Nostr event를 통해 탈중앙화된 git 저장소 호스팅 및 협업을 가능하게 합니다."
---

NIP-34는 Nostr relay에서 git 저장소, 패치, 이슈를 호스팅하기 위한 event kind를 정의합니다. 이를 통해 GitHub나 GitLab과 같은 중앙 집중식 호스팅 플랫폼에 의존하지 않고 완전히 탈중앙화된 코드 협업이 가능합니다.

## 작동 방식

저장소는 이름, 설명, 클론 URL 등의 메타데이터를 포함하는 주소 지정 가능한 event(kind 30617)로 표현됩니다. 저장소 소유자는 이 event를 게시하여 Nostr에서 프로젝트를 설정합니다.

패치(kind 1617)는 저장소에 적용할 수 있는 git 패치 콘텐츠를 포함합니다. 기여자는 대상 저장소를 참조하는 event로 패치를 제출합니다. 이는 Linux 커널과 같은 프로젝트에서 사용하는 이메일 기반 패치 워크플로우를 반영합니다.

이슈(kind 1621)는 전통적인 이슈 트래커처럼 작동합니다. 저장소를 참조하고 제목과 설명을 포함합니다. 이슈와 패치에 대한 댓글은 표준 답글 event를 사용합니다.

## Event Kind

- **30617** - 저장소 공지 (주소 지정 가능)
- **1617** - 패치 제출
- **1621** - 이슈
- **1622** - 이슈 상태 (열림/닫힘)

## 구현

- **ngit** - 저장소와 패치를 Nostr에 게시하기 위한 커맨드라인 도구
- **gitworkshop.dev** - Nostr 호스팅 저장소를 탐색하기 위한 웹 인터페이스
- **Notedeck** - [NIP-34 뷰어에 대한 드래프트 지원](https://github.com/damus-io/notedeck/pull/1279)이 있는 데스크톱 클라이언트

## 주요 출처

- [NIP-34 명세](https://github.com/nostr-protocol/nips/blob/master/34.md)

## 관련 뉴스레터

- [Newsletter #8 (2026-02-04)](/ko/newsletters/2026-02-04-newsletter/) - Notedeck에 NIP-34 뷰어 추가
