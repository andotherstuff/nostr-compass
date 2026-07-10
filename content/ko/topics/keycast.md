---
title: "Keycast: 팀용 Nostr 원격 서명"
date: 2026-05-21
draft: false
translationOf: /en/topics/keycast.md
translationDate: 2026-07-01
categories:
  - Signing
  - Security
  - Teams
---

Keycast는 팀을 위해 구축된 셀프 호스팅 NIP-46 원격 서명 서버이다. Nostr 개인 키를 SQLite에 저장 시 암호화하여 보관하고, NIP-46 bunker 연결 문자열을 생성하며, 구성 가능한 키별 정책에 따라 원격 서명 요청을 승인하거나 거부하는 signer 프로세스를 실행한다. 이 프로젝트는 Marmot Protocol 조직에서 유지 관리한다.

## 작동 방식

서버는 네 가지 주요 구성 요소를 가진다: 팀 관리 및 NIP-98 HTTP 인증을 처리하는 Axum API, NIP-07을 사용하여 인증하는 SvelteKit 웹 프런트엔드, 인증 행을 감시하고 인증당 하나의 `signer_daemon`을 생성하는 signer 관리자, 그리고 마이그레이션이 있는 SQLite 데이터베이스이다.

팀 구성원은 자신의 NIP-07 브라우저 확장 프로그램을 통해 로그인한다. 웹 앱은 확장 프로그램에 의해 로컬로 서명된 NIP-98 HTTP 인증 이벤트를 요청한 다음, 해당 인증 헤더를 API로 전송한다. API는 이벤트를 검증하고, pubkey를 추출하며, 팀 멤버십을 확인한다. 저장된 키는 이미지와 별도로 마운트되어야 하며 절대 커밋되지 않아야 하는 루트 `master.key` 파일로 암호화된다.

signer 데몬은 시작 시 저장된 키와 bunker 키를 복호화하고, 구성된 relay에 연결하며, 각 NIP-46 서명 요청을 승인하기 전에 `Authorization::validate_policy`를 호출한다. 정책은 특정 bunker 연결이 서명할 수 있는 event kind를 지정한다.

## 보안 감사 (2026년 5월)

2026년 5월에 완료된 보안 감사는 인증, 권한, 데이터 무결성 및 종속성 문제를 다루었다. 주요 변경 사항:

- NIP-98 인증은 이제 정확히 하나의 `u` tag와 하나의 `method` tag를 요구하고, 오래되거나 미래의 타임스탬프를 거부하며, 요청 본문 `payload` 해시를 검증한다
- `ALLOWED_PUBKEYS`는 정확하게 파싱되고 서버 측에서 시행된다; 프런트엔드는 `/api/config?pubkey=<hex>`를 노출하여 브라우저가 전체 서버 목록을 수신하지 않고도 허용 목록 상태를 확인할 수 있도록 한다
- 빈 정책은 기본적으로 sign/encrypt/decrypt 요청을 거부한다; 정책 생성은 알 수 없거나 잘못된 형식의 권한 구성을 거부한다
- SQLite 연결은 외래 키 시행을 활성화한다; 팀 삭제는 더 이상 정리 전에 권한 조인 데이터를 손실하지 않는다
- 서버 측 라우트 보호는 이제 `/teams/:id`와 같은 중첩된 앱 라우트를 포함한다
- 웹 응답은 CSP, frame, content-type, referrer, permissions 및 HSTS 헤더를 설정한다
- SQL 마이그레이션은 시작 시 이전 허용된 kind 권한 JSON을 `{"sign":[...]}`에서 `{"allowed_kinds":[...]}`로 정규화한다

감사는 실제 팀 키로 배포를 신뢰하기 전에 [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md)에서 잔여 항목을 확인한다.

## 배포

Docker Compose 배포는 `master.key`를 API 및 signer 컨테이너에 마운트하고, 읽기 전용 루트 파일 시스템을 가진 non-root UID/GID로 컨테이너를 실행하며, Caddy 라벨을 사용하여 `/api/*`를 API로, 나머지는 웹 앱으로 라우팅한다. `ghcr.io/marmot-protocol/keycast`에서 게시된 이미지는 `master`, `latest` 및 `sha-<commit>`으로 태그가 지정된다.

---

**주요 출처:**
- [Keycast 저장소](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - 2026년 5월 보안 감사 결과

**언급된 곳:**
- [Newsletter #23: Keycast Security Audit Complete](/ko/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**참고:**
- [NIP-46: Nostr Remote Signing](/ko/topics/nip-46/)
- [NIP-07: Browser Extension Signer](/ko/topics/nip-07/)
- [Marmot Protocol](/ko/topics/marmot/)
