---
title: "ProofMode"
date: 2026-07-15
draft: false
translationOf: /en/topics/proofmode.md
translationDate: 2026-07-15
categories:
  - Media
  - Provenance
---

[ProofMode](https://proofmode.org/)은 Guardian Project, WITNESS, Okthanks가 만든 오픈소스 미디어 출처 확인 도구 모음으로, 촬영 시점에 사진과 영상에 검증 가능한 진위 및 관리 연속성 데이터를 붙입니다. Nostr 전용은 아니며, ProofMode 데이터를 실어 나르는 Nostr 클라이언트는 새로운 프로토콜 계층이 아니라 기존의 외부 표준을 통합하는 것입니다.

## 작동 방식

ProofMode의 Capture 구성 요소는 촬영 중에 출처 메타데이터를 미디어 파일에 직접 삽입하며, Content Authenticity Initiative(CAI), Content Credentials(CR), C2PA가 사용하는 동일한 상호 운용 표준을 지원합니다. 별도의 Verify 구성 요소는 오디오, 이미지, 비디오 파일을 검사해 해당 메타데이터에서 AI 생성이나 이후 편집의 흔적을 확인하고, Preserve 구성 요소는 장기 보관을 위해 기반 증명 데이터를 탈중앙 웹에 중복 저장합니다. Develop SDK는 앱이 출처 형식을 직접 만들지 않고도 촬영과 검증을 통합할 수 있게 합니다.

## 왜 중요한가

Nostr 비디오 또는 이미지 클라이언트에게 ProofMode 데이터를 실어 나른다는 것은, 게시 클라이언트나 relay를 신뢰의 근거로 삼지 않고도 시청자가 어떤 미디어가 주장대로 촬영되었는지, 그리고 그 이후 조용히 변경되지 않았는지를 외부의 플랫폼 독립적인 방법으로 확인할 수 있다는 뜻입니다. 그 구분이 가장 크게 작용하는 곳은 다운로드되거나 재인코딩된 클립 사본입니다: 다운로드와 클라이언트가 적용하는 워터마크를 견디고 남는 출처 데이터가 있어야, 파일이 그것을 만든 앱을 떠난 뒤에도 그 증명을 여전히 확인할 수 있습니다.

## 구현

- [Divine](https://github.com/divinevideo/divine-mobile) - 짧은 영상 Nostr 클라이언트; 워터마크가 적용된 클립 다운로드에서도 ProofMode 출처 데이터를 유지

---

**주요 출처:**
- [ProofMode](https://proofmode.org/)

**언급된 곳:**
- [Newsletter #17](/ko/newsletters/2026-04-29-newsletter/)
- [Newsletter #31: Divine Mobile 1.0.16이 더 깊어진 비디오 편집기, 저장 데이터 암호화, ProofMode 출처 정보를 출시하다](/ko/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**함께 보기:**
- [Blossom](/ko/topics/blossom/)
