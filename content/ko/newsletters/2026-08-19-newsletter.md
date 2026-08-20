---
title: "Nostr Compass #36"
date: 2026-08-19
publishDate: 2026-08-19
translationOf: /en/newsletters/2026-08-19-newsletter.md
translationDate: 2026-08-19
draft: false
type: newsletters
description: "Amber와 Cambium을 아우른 서명자 보안 주간, 메일 브리지 출시, 휴대폰 릴레이 기능, 암호화 커뮤니티 중재, 스레드·암호화 파일·패치 프로토콜 작업."
---

주간 Nostr 가이드 [Nostr Compass](https://nostrcompass.org)에 다시 오신 것을 환영합니다.

**이번 주:** [Amber](https://github.com/greenart7c3/Amber)가 릴레이 인증을 강화하고 저장된 비밀을 암호화했으며, [Cambium](https://github.com/forgesworn/cambium)은 릴레이 인증 부하 아래에서 웹사이트용 서명을 처리합니다. [Citrine](https://github.com/greenart7c3/Citrine)은 휴대폰 릴레이에서 그룹과 정적 사이트를 호스팅하고, [Vector](https://github.com/VectorPrivacy/Vector)는 스팸 아래에서 중재를 큐잉하며 기기 간 뮤트를 동기화합니다. [Sonar](https://github.com/hedwig-corp/bitchat-to-sonar)는 스레드형 메시 메신저 답글을 추가했고, [Nostria](https://github.com/nostria-app/nostria)는 팟캐스트를 게시하며, [Nail](https://github.com/formstr-hq/nail)은 이메일을 gift wrap 이벤트로 브리지합니다. 릴리스에는 MDK 그룹 상태, 배지 발행, QR 서명자 페어링, Android 브라우저 서명, 공유 wallet-connect가 포함됩니다. 프로토콜 작업은 댓글 패치, 암호화 파일 메타데이터, 스레드 서식, Marmot 재시작 보장, Concord 멤버십 목록에 이르렀습니다. 심층 분석: 배지와 댓글.

## 주요 소식

### Amber 6.5.0, 릴레이 인증 confused deputy를 닫고 저장된 비밀을 암호화

[Amber](https://github.com/greenart7c3/Amber)는 Android [NIP-55](/ko/topics/nip-55/)(Android 서명자) 및 [NIP-46](/ko/topics/nip-46/)(원격 서명) 서명자입니다. [버전 6.5.0](https://github.com/greenart7c3/Amber/releases/tag/v6.5.0)은 공개된 네 가지 격차를 닫습니다. 사용자가 승인하지 않은 릴레이에 대해서도 임의 호출자가 kind `22242` [NIP-42](/ko/topics/nip-42/)(릴레이 인증) 이벤트를 얻을 수 있게 하던 [릴레이 인증 confused deputy](https://github.com/greenart7c3/Amber/security/advisories/GHSA-vx4h-56qj-wcp7), [NIP-46 재생 공격 격차](https://github.com/greenart7c3/Amber/security/advisories/GHSA-h9fv-9247-3582), 저장 시 envelope 암호화로 바뀐 [평문 연결 비밀과 로컬 키](https://github.com/greenart7c3/Amber/security/advisories/GHSA-5fjp-ghh8-wch8), 그리고 복호화 전 호출자 권한 부여, fail-closed 권한 파싱, plain `ws://` 경고, 보안 QR 화면, 로그 마스킹, 로그아웃 시 지연 키 제로화, 잠금 해제 기기 Keystore 선택 사용을 다루는 [8항목 강화 배치](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8844-q5vh-9j8f)입니다.

[버전 6.5.1](https://github.com/greenart7c3/Amber/releases/tag/v6.5.1)은 잠금 해제 기기 요구 토글 후 Keystore 키가 회전할 때 저장된 NIP-46 비밀을 재암호화하고 권한 편집기 충돌을 수정합니다. [버전 6.5.2](https://github.com/greenart7c3/Amber/releases/tag/v6.5.2)는 애플리케이션 목록이 렌더링하지 않는 열의 복호화를 중단하고, Keystore 핸들을 캐시하며, 시작 시 계정 캐시를 워밍하고, 릴레이 상태 알림을 디바운스합니다.

[지난주 6.4.0](/en/newsletters/2026-08-12-newsletter/#amber-640-makes-every-grouped-signing-decision-explicit)은 그룹화된 서명 결정을 명시적으로 만들었고, 6.5.x는 Amber가 무엇을 승인할지 자체를 바꿉니다.


### Cambium 0.4.0, 웹사이트용 서명과 릴레이 인증 폭주 처리

[Cambium](https://github.com/forgesworn/cambium)은 [NIP-46](/ko/topics/nip-46/)을 통해 Heartwood 하드웨어 서명자에 연결하는 Android [NIP-55](/ko/topics/nip-55/) 프록시입니다. 이틀 만에 여섯 번의 릴리스가 나왔습니다.

[버전 0.4.0](https://github.com/forgesworn/cambium/releases/tag/v0.4.0)은 서명 대상을 웹사이트로 확장합니다. 페이지는 검증된 `nostrsigner:` 콜백으로 서명을 요청할 수 있으며, 네이티브 애플리케이션에 부여된 권한을 물려받지 않아 브라우저 탭이 다른 앱의 승인을 빌려 쓰지 못합니다. 같은 릴리스는 사양의 최소 이벤트 형태를 수정합니다. `kind`와 `content`만 담긴 이벤트도 이제 올바르게 서명되며, Cambium이 짝지어진 NIP-46 신원, 현재 타임스탬프, 빈 태그 배열을 채운 뒤 rust-nostr에 넘깁니다. 네이티브 rust-nostr 계측은 같은 변경에서 필수 CI 게이트가 되었습니다.

[버전 0.3.6](https://github.com/forgesworn/cambium/releases/tag/v0.3.6)은 사양을 따르는 서명자와의 페어링을 복구합니다. Cambium의 구 rust-nostr 빌드는 NIP-46 `connect` 호출 결과로 문자열 `ack`만 받아들였기 때문에, 현재 사양이 요구하고 Heartwood 펌웨어가 하는 bunker URI secret 에코 응답은 unexpected-response 오류로 페어링이 끝났습니다. rust-nostr 0.44.2에서 0.44.8로 올리면 두 형태 모두 허용되며, 라이브 하드웨어와 여전히 `ack`로 답하는 `nak bunker`에 대해 검증되었습니다.

0.4.1부터 0.4.3 릴리스는 부하 아래 입장 제어입니다. [버전 0.4.1](https://github.com/forgesworn/cambium/releases/tag/v0.4.1)은 반응, 게시, 삭제, 암호화에 릴레이 인증과 백그라운드 복호화보다 앞선 예약 큐 슬롯을 주고, 큐잉된 호출을 제한하며, 호출자가 타임아웃되면 버리고, 과부하 시 포그라운드 서명 화면 대신 종료 unavailable 결과를 반환합니다. [버전 0.4.2](https://github.com/forgesworn/cambium/releases/tag/v0.4.2)는 다음 요청 전에 타임아웃되거나 오래 유휴한 NIP-46 세션을 버리고, 같은 kind `22242` 인증 이벤트의 동시 복사본이 하나의 하드웨어 서명을 공유하게 합니다. [버전 0.4.3](https://github.com/forgesworn/cambium/releases/tag/v0.4.3)은 신원당 서로 다른 인증 챌린지를 하드웨어 워커에 최대 하나만 허용하고, 인증을 내부적으로 재시도하지 않으며, 타임아웃 후 신원당 60초 쿨다운을 열고, 정확히 캐시된 중복에는 여전히 답합니다. 릴리스 노트의 측정은 GrapheneOS 휴대폰에서 [Amethyst](https://github.com/vitorpamplona/amethyst)를 구동한 결과입니다. 콜드 스타트 폭주에서 즉시 과부하 응답 33건과 서명자 타임아웃 없이 완료된 요청 13건이 나왔고, 인증 폭주 중 새 로그인은 승인 후 1.254초에 반환되었습니다.

### Citrine 3.1.0, 휴대폰 릴레이를 그룹 호스트와 사이트 호스트로

[Citrine](https://github.com/greenart7c3/Citrine)은 기기 내 Android 릴레이입니다. [버전 3.1.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.1.0)은 릴레이가 호스팅할 수 있는 것을 바꾸는 세 가지 기능을 추가합니다.

릴레이 자체가 멤버십과 중재 상태를 보관하는 [NIP-29](/ko/topics/nip-29/)(릴레이 기반 그룹) [사양](https://github.com/nostr-protocol/nips/blob/master/29.md) 지원으로 휴대폰이 그룹에 가입하는 대신 그룹을 호스팅할 수 있습니다. 인증된 JSON-RPC로 관리 작업을 노출하는 [NIP-86](/ko/topics/nip-86/)(릴레이 관리 API) [지원](https://github.com/nostr-protocol/nips/blob/master/86.md)은 설정 화면과 함께 도착해, 허용 목록과 차단을 API와 앱 모두에서 구동할 수 있습니다. [NIP-5A](/ko/topics/nip-5a/) [정적 웹사이트](https://github.com/nostr-protocol/nips/blob/master/5A.md) 지원으로 릴레이가 nsite를 웹 클라이언트에 제공하며, 아이콘, 검색, 최종 업데이트순 정렬, 설치 진행, 설명, 기본값 `nsite.run`, `nos.lol`, `nostr.land`인 가져오기 릴레이 집합을 갖춘 현대화된 탐색 목록이 따라옵니다.

중재 표면도 [같은 릴리스](https://github.com/greenart7c3/Citrine/releases/tag/v3.1.0)에서 함께 커졌습니다. 공개 키를 로컬에서 차단할 때 해당 작성자의 저장 이벤트를 제거할지 묻고, 설정 가능한 `REJECTED_KINDS` 목록이 운영자가 저장하지 않을 kind를 막으며, 접근 제어가 기존 목록에서 가져올 수 있습니다. 재방송 도구는 저장된 이벤트를 선택한 릴레이로 다시 밀어, 휴대폰 보관 아카이브가 네트워크를 재시드할 수 있게 합니다. 릴리스는 WebSocket `permessage-deflate` 확장을 제거하고, 쿼리 핫 경로를 조이며, Tor 노출 설정 변경 시 Tor가 시작/중지되지 않던 문제를 고치고, 로그를 로컬 데이터베이스로 옮기며 logcat은 디버그 빌드로 제한합니다.

### Vector 0.4.2, 스팸 폭주에서도 커뮤니티 중재가 버티게

[Vector](https://github.com/VectorPrivacy/Vector)는 데스크톱 및 Android [Concord](https://github.com/concord-protocol/concord) 메신저입니다. [버전 0.4.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.2)는 부하 아래 중재에 초점을 맞춥니다.

빠른 차단이 서로를 덮어쓰던 것이 이제 큐에 쌓이고 겹쳐 하나의 작업으로 정리되어, 계정 물결 전체를 차단할 때 키 회전 한 번이면 됩니다. 이미 해산된 커뮤니티 초대를 수락하면 이유를 설명하고 사용자가 소유한 모든 기기에서 초대를 제거하며, 사용자가 소유한 커뮤니티를 해산하면 모든 기기의 커뮤니티 목록에서 지워집니다. 이 수정은 [버전 0.4.3](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.3)에 도착했습니다. 백그라운드 따라잡기 중 도착한 커뮤니티 메시지는 방금 보낸 것처럼 알림을 울리지 않고, 타이핑 표시는 보낸 시점부터 만료되어 지연된 신호가 채널에 남지 않습니다.

[Concord](https://github.com/concord-protocol/concord)가 정의한 샤딩된 커뮤니티 목록은 다른 Concord 클라이언트 Armada와 교차 검토를 받았습니다. 이름 변경이 더 이상 목록을 부풀리지 않고, 동점은 두 클라이언트에서 동일하게 해결되며, 변경 없는 데이터는 릴레이에 다시 게시되지 않습니다. 뮤트도 DM 경로 밖으로 이동했습니다. 사용자는 메시지 기록 없이 커뮤니티에서 바로 뮤트할 수 있고, 뮤트는 채널과 DM의 알림과 배지에 적용되며 메시지 자체는 보입니다. 고정 메시지는 클릭 가능한 링크가 있는 공유 채널 표면이 되었고, 고정 메시지 편집은 나타나는 곳마다 따라갑니다. 차단 목록, 뮤트, 닉네임이 사용자 기기 간 동기화되고, 고정 채팅도 마찬가지입니다. 버전 0.4.3은 다른 Nostr 클라이언트가 같은 신원으로 로그인 중일 때 Vector가 타이핑 중임을 알리지 않게 하고, x64와 ARM64 Windows 모두 15%에서 멈추던 Tor 부트스트랩을 풉니다.

### Sonar, NIP-C7로 메시 메신저에 스레드 답글

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar)는 Bluetooth 메시 및 Nostr 메신저입니다. [버전 0.1-alpha.13.1](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.13.1)은 [NIP-C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) kind `9` 채팅에 Signal 스타일 답글과 멘션, 제한된 Bluetooth 재조립, 백업 상한, 메시 경로 서명 검증, FCM 푸시 폴백을 추가합니다. [버전 0.1-alpha.13.2](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.13.2)와 [0.1-alpha.13.3](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.13.3)은 Android 채팅 열기 충돌과 iOS 키보드 겹침을 고칩니다.

### Nostria, 팟캐스트 게시 시작과 릴레이 COUNT 요청

[Nostria](https://github.com/nostria-app/nostria)는 웹 클라이언트입니다. [버전 4.1.70](https://github.com/nostria-app/nostria/releases/tag/v4.1.70)과 [4.1.71](https://github.com/nostria-app/nostria/releases/tag/v4.1.71)은 프리미엄 구독자용 팟캐스트 게시를 추가하며, 에피소드는 서명된 Nostr 이벤트입니다. [버전 4.1.69](https://github.com/nostria-app/nostria/releases/tag/v4.1.69)는 피드에서 [NIP-45](/ko/topics/nip-45/)(COUNT) `COUNT`로 반응, 답글, zap 합계를 쓰고 현지화를 완료합니다. [지난주 4.1.67](/en/newsletters/2026-08-12-newsletter/#nostria-4167-expands-encrypted-community-administration)은 암호화 커뮤니티 관리를 확장했습니다.

## 태그 릴리스


### MDK 0.9.14: 더 빠른 그룹 생성과 fail-closed 그룹 기록

[MDK](https://github.com/marmot-protocol/mdk)는 Nostr 위 암호화 그룹 메시징 프로토콜 [Marmot](https://github.com/marmot-protocol/marmot)용 Rust 개발 키트입니다. [버전 0.9.12](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.12)는 여러 그룹 상태 경로를 추측 대신 fail-closed로 만듭니다. 누락된 fork anchor는 이제 하드 오류([PR #1329](https://github.com/marmot-protocol/mdk/pull/1329))이고, leave proposal은 원자적으로 영속화되어 충돌이 반쯤 적용된 탈퇴를 남기지 않으며([PR #1360](https://github.com/marmot-protocol/mdk/pull/1360)), incident replay는 manifest 없는 줄 단위 JSON 스트림에서 형식을 추측하지 않습니다([PR #1140](https://github.com/marmot-protocol/mdk/pull/1140)). 수렴 테스트도 넓어져 보존 기록 교차 경로 복구([PR #1350](https://github.com/marmot-protocol/mdk/pull/1350)), 교차 어댑터 수렴 보장([PR #1372](https://github.com/marmot-protocol/mdk/pull/1372)), 일반화된 격리 수렴 캠페인([PR #1357](https://github.com/marmot-protocol/mdk/pull/1357))이 포함됩니다. 릴레이 거부 진단은 일반 실패로 접히지 않고 보존됩니다([PR #1361](https://github.com/marmot-protocol/mdk/pull/1361)).

[버전 0.9.13](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.13)은 8월 18일 storage format v2([PR #1421](https://github.com/marmot-protocol/mdk/pull/1421)), 마이그레이션 레일, 라이브 계정 스냅샷을 대체하는 delta 쓰기([PR #1435](https://github.com/marmot-protocol/mdk/pull/1435)), 더 빠른 초대 따라잡기([PR #1444](https://github.com/marmot-protocol/mdk/pull/1444)), macOS 바인딩([PR #1402](https://github.com/marmot-protocol/mdk/pull/1402))과 함께 도착했습니다. [버전 0.9.14](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.14)는 8월 19일 그룹 생성 다듬기로 이어졌습니다. 사전 업로드된 창립 이미지([PR #1498](https://github.com/marmot-protocol/mdk/pull/1498)), KeyPackage 배치([PR #1494](https://github.com/marmot-protocol/mdk/pull/1494)), 원자적 초기 메시지 보존([PR #1497](https://github.com/marmot-protocol/mdk/pull/1497)), 계정 소유 릴레이와 함께하는 프로필 게시([PR #1495](https://github.com/marmot-protocol/mdk/pull/1495)). [MarmotKit 0.9.14](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-v0.9.14)와 [wn-agent 0.9.14](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.14)가 코어 crate와 함께 출하됩니다.

### Divine Mobile 1.0.20: 앱을 떠나지 않고 배지 발행

[Divine Mobile](https://github.com/divinevideo/divine-mobile)은 Nostr를 통해 동영상을 게시하고 가져오는 숏폼 클라이언트입니다. [버전 1.0.20](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.20)은 사용자가 [NIP-58](/ko/topics/nip-58/)(배지) 배지, 즉 이번 호의 첫 심층 분석에 나온 서명된 수여 이벤트를 발행해 다른 사람에게 수여할 수 있게 합니다. 프로필의 배지를 탭하면 획득 조건을 설명하는데, 정의 이벤트와 수여 이벤트가 따로 저장되기 때문에 보통 구현되지 않는 사양 부분입니다.

[릴리스](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.20)의 나머지는 클라이언트 작업입니다. 라이트 테마, 스톱모션 편집기의 자르기·회전·뒤집기, 녹화기에서 한 탭으로 가는 초안, 동영상 대비 캡션 타이밍, 이미 본 콘텐츠의 우선순위를 낮추는 피드, 편집기·녹화기·프로필 탭의 스크린 리더 지원, 모션 감소 처리, Divine 이메일·비밀번호 관리와 계정 연결/해제 설정. 삭제된 동영상은 이제 로컬 상태에서 제거되고 북마크는 유지됩니다. [지난주 1.0.19](/en/newsletters/2026-08-12-newsletter/#divine-mobile-1019-tightens-accounts-private-messages-and-publishing)는 계정 격리와 DM 검증을 강화했고, 배지 발행은 그 위의 새 게시 표면입니다.

### ClipRelay 0.2.0: 카메라로 서명자 페어링

[ClipRelay](https://github.com/tajava2006/cliprelay)는 Nostr 위에서 기기 간 클립보드를 동기화합니다. [Android 버전 0.2.0](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.2.0)은 `nostrconnect://` QR 로그인을 추가해 다른 휴대폰의 서명자 앱으로 로그인할 수 있고, bunker URL 카메라 스캔을 추가해 비밀 문자열을 메신저에 붙여 넣는 습관을 없앱니다. bunker 연결은 60초 후 타임아웃되고, Amber 로그인 실패 후 재시도 버튼이 동작합니다. [데스크톱 버전 0.2.0](https://github.com/tajava2006/cliprelay/releases/tag/desktop%2Fv0.2.0)은 타임아웃과 로그인 탭 수정을 담습니다.

[버전 0.1.4](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.1.4)는 짧은 릴레이 만료가 있는 민감 클립보드 동기화, 고정 서명자 세션 릴레이, 로컬 합성 `EOSE` 대신 실제 왕복을 요구하는 생존 프로브를 추가했습니다. [지난주 0.1.3](/en/newsletters/2026-08-12-newsletter/#cliprelay-013-restores-relay-and-signer-connections-after-idle-periods)은 유휴 후 연결을 복구했습니다.

### Bark 1.3.9: Android에서 동작하는 브라우저 서명자

[Bark](https://github.com/forgesworn/bark)는 [NIP-07](/ko/topics/nip-07/)(브라우저 서명) `window.nostr` 인터페이스, 즉 웹 페이지가 서명이나 암호화를 요청할 때 호출하는 객체를 제공하는 브라우저 확장입니다. [버전 1.3.9](https://github.com/forgesworn/bark/releases/tag/v1.3.9)는 Firefox 빌드에 Android 지원을 선언해 애드온 목록이 휴대폰에 설치됩니다. Android Firefox는 windows API를 구현하지 않아 팝업 창을 연 모든 승인이 거부되었는데, 승인 표면이 이제 포그라운드 탭으로 폴백합니다. 닫으면 거부, 검토 동작은 포그라운드, 요청이 정리되면 백그라운드가 닫힙니다. 릴리스 노트는 GrapheneOS의 Pixel 10 Pro XL, Firefox 153.0.4에서 검증했으며, Android Chromium은 확장 서브시스템을 컴파일에서 제외해 Chromium 계열 Android 브라우저는 Bark를 전혀 실행할 수 없다고 명시합니다.

[버전 1.3.8](https://github.com/forgesworn/bark/releases/tag/v1.3.8)은 반대 방향 NIP-46 상호운용 결함을 고쳤습니다. Bark가 Heartwood 서명 방언을 탐지하려 이벤트를 JSON 객체로 보냈는데, `nak`과 rust-nostr bunker처럼 엄격한 타입 서명자는 이를 파싱하지 못하고 조용히 버려 서명이 멈췄습니다. 이제 Heartwood로 자신을 밝힌 서명자에게만 프로브를 보내고, 나머지는 첫 서명부터 표준 `sign_event`를 받습니다.

### Bray 3.0.0과 Toll Booth 6.0.0, 공유 wallet-connect 라이브러리로 이전

[Bray](https://github.com/forgesworn/bray)와 [Toll Booth](https://github.com/forgesworn/toll-booth)는 모두 [NIP-47](/ko/topics/nip-47/)(Nostr Wallet Connect) NWC로 결제하며, 애플리케이션이 암호화 Nostr 이벤트로 지갑에 결제를 요청하는 사양입니다. [Bray 3.0.0](https://github.com/forgesworn/bray/releases/tag/v3.0.0)과 [Toll Booth 6.0.0](https://github.com/forgesworn/toll-booth/releases/tag/v6.0.0)은 각각 [nwc-kit](https://github.com/forgesworn/nwc-kit) 채택 breaking change를 선언하고, Toll Booth는 같은 변경에서 payer credential 흐름을 제거합니다. 둘 다 두 독립 러너에서 바이트 동일한 재현 가능 빌드를 게시하며, tarball 해시가 릴리스 노트에 인쇄되어 레지스트리 아티팩트를 검증할 수 있습니다.

Toll Booth 패치 세 개가 이어졌습니다. [6.0.1](https://github.com/forgesworn/toll-booth/releases/tag/v6.0.1)은 협상된 deploy 호스트 키를 고정하고, [6.1.1](https://github.com/forgesworn/toll-booth/releases/tag/v6.1.1)은 패치 대상 `cashu-ts` 버전을 고정하며, [6.1.2](https://github.com/forgesworn/toll-booth/releases/tag/v6.1.2)는 이미지 빌드를 복구합니다.

### NoorNote 1.3.4: 초대 링크로 암호화 커뮤니티 가입

[NoorNote](https://github.com/77elements/noornote)는 데스크톱, 웹, Android용 Nostr 클라이언트입니다. [버전 1.3.4](https://github.com/77elements/noornote/releases/tag/v1.3.4)는 암호화 Armada 및 Concord 커뮤니티를 애드온으로 추가합니다. 사용자는 초대 링크로 가입하고, 설정에 가입한 커뮤니티 목록을 보고, 활동 알림을 받습니다. 같은 릴리스는 외부 인용 게시, 즉 웹 기사 단락을 인용하는 하이라이트 노트를 전역 또는 작성자별로 숨기는 제어를 추가하며, 그 repost도 숨기고 사용자 자신의 하이라이트는 보입니다. 프로필 해석도 복구되어 프로필이 잘린 공개 키나 익명 placeholder로 렌더링되지 않습니다.

[버전 1.3.5](https://github.com/77elements/noornote/releases/tag/v1.3.5)는 긴 노트용 펼치기와 Armada 초대 링크 입력 레이아웃을 고칩니다. [지난주 1.3.2](/en/newsletters/2026-08-12-newsletter/#noornote-132-moves-article-discovery-into-the-social-graph)는 기사 발견을 소셜 그래프로 옮겼고, 커뮤니티 멤버십은 별도 표면입니다.

### Mostro, 분쟁 채팅을 gift wrap에서 이전

[Mostro](https://github.com/MostroP2P/mostro)는 주문과 메시지가 Nostr 이벤트로 이동하는 P2P 거래 데몬이며, [mostro-core](https://github.com/MostroP2P/mostro-core)가 공유 라이브러리, [Mostro Mobile](https://github.com/MostroP2P/mobile)이 클라이언트입니다. [Mobile 1.3.2](https://github.com/MostroP2P/mobile/releases/tag/v1.3.2)는 분쟁 채팅을 [NIP-59](/ko/topics/nip-59/)(gift wrap)에서 kind `14` 채팅 envelope로 마이그레이션하고 백로그를 대화별 내구 커서로 뒷받침합니다. [mostro-core 0.14.5](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.5)는 gift wrap 안 rumor 식별자를 직렬화([PR #164](https://github.com/MostroP2P/mostro-core/pull/164))하고, [0.14.4](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.4)는 평점 평균 버그를 고칩니다([PR #163](https://github.com/MostroP2P/mostro-core/pull/163)). [Mobile 1.3.1](https://github.com/MostroP2P/mobile/releases/tag/v1.3.1)은 암호화 채팅 첨부를 보관하는 Blossom 서버로 전환합니다. 데몬 [0.18.2](https://github.com/MostroP2P/mostro/releases/tag/v0.18.2) 또는 [0.18.4](https://github.com/MostroP2P/mostro/releases/tag/v0.18.4)를 사용하세요.

### NYM 3.73.522: 암호화 그룹 채팅과 암호화 로컬 저장소

[NYM](https://github.com/Spl0itable/NYM)은 자체 어시스턴트 통합이 있는 Nostr 클라이언트입니다. [버전 3.73.522](https://github.com/Spl0itable/NYM/releases/tag/v3.73.522)는 [3.73.521](https://github.com/Spl0itable/NYM/releases/tag/v3.73.521)이 암호화 그룹 채팅을 다듬은 뒤 로컬 SQLite 저장소를 암호화하고, [3.73.520](https://github.com/Spl0itable/NYM/releases/tag/v3.73.520)은 CSP 깨짐과 중복 새 메시지 표시를 고칩니다.

### Morganite 0.0.4: 캐시 전 blob 해시 검증

[Morganite](https://github.com/greenart7c3/Morganite)는 Android [Blossom](/ko/topics/blossom/) 서버로, 파일은 내용 SHA-256 해시로 주소 지정되고 보유 호스트가 제공하는 미디어 프로토콜입니다. [버전 0.0.4](https://github.com/greenart7c3/Morganite/releases/tag/v0.0.4)는 다운로드 중 blob 해시를 한 패스로 검증한 뒤 캐시해, 수신 측에서 content addressing이 의미 있게 동작하게 합니다. 릴리스는 저장마다 디렉터리 전체를 다시 스캔하지 않고 캐시 크기를 증분 추적하고, 블로킹 네트워크 호출을 I/O 스레드로 옮기고, MIME 감지용 Tika 인스턴스를 재사용하며, 로그를 로컬 DB에 영속화합니다.

## 새로 발견


### Nail, 이메일을 gift wrap 이벤트로 Nostr에

[Nail](https://github.com/formstr-hq/nail)은 [Formstr](https://github.com/formstr-hq/nostr-forms)과 [nostr-calendar](https://github.com/formstr-hq/nostr-calendar) 팀의 MIT 라이선스 메일 브리지·웹 클라이언트입니다. 8월 18일 [PR #7](https://github.com/formstr-hq/nail/pull/7)로 출시했으며, 22파일 변경으로 메일 이벤트에 `k` 태그, 설정의 키 복구, 환영 메시지를 추가했습니다. 배포는 [mailstr.app](https://mailstr.app)에서 돌아가며, 브리지 자체 `_smtp` [NIP-05](/ko/topics/nip-05/)(DNS 기반 이름-키 매핑) 레코드를 제공합니다.

메일 자체는 Nostr 이벤트입니다. 클라이언트 [constants](https://github.com/formstr-hq/nail/blob/main/client/src/lib/nostr/constants.ts)는 kind `1301` 메일 rumor가 kind `1059` [NIP-59](/ko/topics/nip-59/)(gift wrap) gift wrap 안에 실려, 비공개 DM과 같은 메타데이터 숨김 envelope로 수신자에게 도달함을 정의합니다. 전달 릴레이는 kind `10050` [NIP-17](/ko/topics/nip-17/)(비공개 DM) 받은편지함 목록과 그 뒤 kind `10002` [NIP-65](/ko/topics/nip-65/)(릴레이 목록) 릴레이 목록에서 옵니다. 폴더는 `mail` 네임스페이스 아래 kind `1985` [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) 라벨이고, 클라이언트 설정은 kind `30078` [NIP-78](/ko/topics/nip-78/)(애플리케이션 데이터) 이벤트에 있습니다. 60,000바이트보다 큰 첨부는 [NIP-44](/ko/topics/nip-44/)(암호화)가 암호화 평문을 65,535바이트로 제한하기 때문에 이벤트 대신 [Blossom](/ko/topics/blossom/)으로 갑니다. 주소는 도메인의 npub이고, NIP-05 레코드가 없는 로컬 도메인은 존재하지 않는 사서함으로 취급됩니다.

브리지 절반은 [mailcow](https://github.com/mailcow/mailcow-dockerized) 배포 옆에서 패치 없이 돌아가는 Node LMTP 서버입니다. Postfix가 해당 도메인을 브리지로 라우팅하고, 브리지가 SMTP로 답장을 주입합니다. 이 설계는 이메일 브리지의 가장 어려운 질문, `From` 헤더가 무엇을 증명하는지에 정직하게 답해야 합니다. Nail [receive path](https://github.com/formstr-hq/nail/blob/main/client/src/lib/mail/receive.ts)는 모든 메시지를 네 가지 출처 상태로 등급합니다. 설정된 브리지가 봉인했고 upstream에서 검증하지 않은 발신자는 릴레이하지 않음, 사용자가 직접 봉인, 주소 NIP-05가 봉인 키로 해석됨, 또는 헤더를 뒷받침하는 것이 없음. 마지막 경우 인터페이스는 봉인 공개 키로 폴백하는데, 이벤트가 실제로 증명할 수 있는 유일한 신원입니다. 브리지 API 호출은 [NIP-98](/ko/topics/nip-98/)(HTTP 인증) 서명 HTTP 이벤트로 인증됩니다.

### Glow, 패스키 파생 신원 아래 릴레이에 지갑 라벨 저장

[Glow](https://breez.technology/glow/)는 Breez 셀프 커스터디 Lightning 지갑입니다. 패스키 로그인이 Nostr 신원을 파생하고, 지갑 라벨은 그 신원 아래 릴레이에서 목록·저장되며, 부분 릴레이 커버리지에서도 바이트 동일 중복이 접힙니다.

## 개발 중

### Amethyst, 릴레이 인증 결정 흐름 재구성

[Amethyst](https://github.com/vitorpamplona/amethyst)는 Android Nostr 클라이언트입니다. 병합된 작업 블록이 [NIP-42](/ko/topics/nip-42/)(릴레이 인증) 처리 방식을 재형성합니다. 권한 인터페이스와 결정 흐름이 재설계되었([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899))고, 인증은 타임아웃 대신 챌린지 해결을 기다립니다([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)). 새 계정은 기본적으로 항상 릴레이와 인증합니다([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), "항상 로그인" 선택이 계정이 직접 쓰지 않는 릴레이에도 적용됩니다([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)). 인증은 [NIP-29](/ko/topics/nip-29/) 그룹과 Concord 커뮤니티를 가입한 venue로 인식([PR #3906](https://github.com/vitorpamplona/amethyst/pull/3906))해, 릴레이 호스트 그룹이 열릴 때마다 낯선 릴레이처럼 보이지 않게 합니다.

다른 두 변경은 프로토콜 표면을 건드립니다. [NIP-13](/ko/topics/nip-13/)(proof of work) 채굴은 채굴 중 `created_at`을 갱신하고 GPU 경로 분석을 얻었([PR #3911](https://github.com/vitorpamplona/amethyst/pull/3911))으며, 전체 화면 napplet 호스트가 입력기 inset을 처리합니다([PR #3932](https://github.com/vitorpamplona/amethyst/pull/3932)). 설정 진입점이 있는 안내형 첫 실행 키 백업([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909))과 공개 채팅 뮤트([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939))도 병합되었습니다.

### nostrord, 미병합 암호화 키 제안 구현

[nostrord](https://github.com/nostrord/nostrord)는 릴레이 범위 그룹 중심 Nostr 채팅 클라이언트입니다. Compass가 [7월 15일 호](/ko/newsletters/2026-07-15-newsletter/)에서 마지막으로 설명한 미병합 NIP-4e, 즉 메시지 암호화를 신원 키에서 분리하는 제안 구현을 병합했습니다. 계정이 자체 kind `10044` 암호화 키를 공표하고, 개인 절반을 로컬에 보관하며, 수신 DM을 프로세스 내에서 복호화해 bunker나 브라우저 확장을 읽기 경로에서 완전히 빼냅니다([PR #261](https://github.com/nostrord/nostrord/pull/261)). kind `4454`와 `4455` 기기 페어링이 그 키를 두 번째 기기로 옮기고, self-archive가 새 키를 향한 기록을 다시 게시합니다. 전송은 먼저 공표된 키를 향했([PR #247](https://github.com/nostrord/nostrord/pull/247))고, 후속 PR은 협상에 성공했지만 키를 넘기지 않던 페어링을 고쳤습니다([PR #271](https://github.com/nostrord/nostrord/pull/271)). PR은 공개 제안과 다른 지점에서 배포된 Jumble 구현을 따른다고 밝혀, 이 사양의 동작 정의가 문서가 아니라 출하 코드에 있다고 둡니다.

같은 배치에서 그룹 신원도 조였습니다. 그룹 식별자는 이제 릴레이 내에서만 고유([PR #269](https://github.com/nostrord/nostrord/pull/269))해, 두 릴레이의 같은 식별자는 두 그룹으로 취급([PR #272](https://github.com/nostrord/nostrord/pull/272))되고, 스레드 게시는 포럼 게시로 렌더링([PR #274](https://github.com/nostrord/nostrord/pull/274))됩니다. kind `22242` 서명 프롬프트를 반복 생성하던 연결 churn도 멈췄([PR #268](https://github.com/nostrord/nostrord/pull/268))으며, 이번 주 Cambium이 세 릴리스에 쓴 것과 같은 클래스의 서명자 압박입니다.

### nostream, 릴레이 모니터 추가와 초대 코드 발행

[nostream](https://github.com/cameri/nostream)은 TypeScript 릴레이 구현입니다. [NIP-66](/ko/topics/nip-66/)(릴레이 모니터링) 릴레이 모니터링 이벤트를 게시하는 클러스터 worker와 프로브 스케줄러를 병합([PR #724](https://github.com/cameri/nostream/pull/724))했고, 설정 스키마와 기본값([PR #689](https://github.com/cameri/nostream/pull/689)), 통합 테스트([PR #733](https://github.com/cameri/nostream/pull/733))가 있습니다. CLI 도구가 [NIP-43](/ko/topics/nip-43/)(릴레이 접근) 초대 코드를 발행([PR #732](https://github.com/cameri/nostream/pull/732))하고, 릴레이는 마침내 지원 목록에 [NIP-13](/ko/topics/nip-13/) proof of work를 광고([PR #680](https://github.com/cameri/nostream/pull/680))합니다. 구현만 있고 알리지 않던 부분입니다. DVM job 영속 마이그레이션과 저장소([PR #727](https://github.com/cameri/nostream/pull/727))도 추가되었고, 릴레이는 [NIP-90](/ko/topics/nip-90/)(DVM job 요청)을 가로채 job 저장소에 기록([PR #729](https://github.com/cameri/nostream/pull/729))합니다.

### rust-nostr, gift wrap 식별자 수정과 보호 repost 거부

[rust-nostr](https://github.com/nostrdevkit/nostr)는 이번 호 Rust·모바일 클라이언트 작업 상당수의 기반 Rust 라이브러리·SDK입니다. rumor 식별자를 gift wrap seal 암호화 전에 계산([PR #1444](https://github.com/nostrdevkit/nostr/pull/1444))하며, Mostro가 이번 주 자체 라이브러리에서 고친 결함과 같은 클래스입니다. 로컬 릴레이는 [NIP-70](/ko/topics/nip-70/)(보호 이벤트) 보호 이벤트 repost를 거부([PR #1445](https://github.com/nostrdevkit/nostr/pull/1445))하고, NIP-47 응답 파싱은 누락·null amount를 허용([PR #1450](https://github.com/nostrdevkit/nostr/pull/1450))해 생략하는 지갑에서도 실패하지 않습니다. 릴레이 URL 파싱도 강화([PR #1451](https://github.com/nostrdevkit/nostr/pull/1451))되었습니다.

### NDK, 포스트 양자 DM 추가와 GPL 의존성 제거

[NDK](https://github.com/relaystr/ndk)는 Nostr용 Dart SDK입니다. FIPS 203으로 표준화된 격자 KEM ML-KEM-1024를 쓰는 DM용 하이브리드 포스트 양자 암호화를 병합([PR #713](https://github.com/relaystr/ndk/pull/713))해, 고전 키 합의를 대체하지 않고 나란히 둡니다. 별도 변경은 GPL-3.0-only Dilithium 구현을 ML-DSA 표준 `fips204`로 교체([PR #712](https://github.com/relaystr/ndk/pull/712))해 kit을 embed하는 앱의 라이선스 제약을 없앱니다. 연결도 신원당 하나로 이동([PR #710](https://github.com/relaystr/ndk/pull/710))했습니다.

### Nostter, 북마크 목록·프로필 배지·Blossom 업로드

[Nostter](https://github.com/SnowCait/nostter)는 웹 클라이언트입니다. [NIP-51](/ko/topics/nip-51/)(목록) 북마크 목록의 표준·레거시 형태 모두([PR #2311](https://github.com/SnowCait/nostter/pull/2311)), NIP-58 프로필 배지 처리 갱신([PR #2281](https://github.com/SnowCait/nostter/pull/2281)), Blossom 미디어 업로더([PR #2298](https://github.com/SnowCait/nostter/pull/2298)), 멘션 자동완성의 [NIP-05](/ko/topics/nip-05/) 식별자 표시([PR #2303](https://github.com/SnowCait/nostter/pull/2303))를 병합했습니다.

### Zap Cooking, 관리 경로를 서명 요청에 묶고 저장 wallet 연결 암호화

[Zap Cooking](https://github.com/zapcooking/frontend)은 Nostr 장문 이벤트 기반 레시피 사이트입니다. 보안 배치는 저장 NWC 연결 문자열을 NIP-44 envelope로 저장 시 암호화([PR #622](https://github.com/zapcooking/frontend/pull/622))하고, 관리 경로의 위조 가능 공개 키 비교를 [NIP-98](/ko/topics/nip-98/) HTTP 인증, 즉 HTTP 요청을 승인하는 이벤트 서명으로 교체([PR #626](https://github.com/zapcooking/frontend/pull/626))하며, 로그아웃 시 계정 데이터를 지우고 보류 NIP-46 레코드를 제한([PR #627](https://github.com/zapcooking/frontend/pull/627))합니다.

## 프로토콜 및 사양 작업

### NIPs


이 기간 [nostr-protocol/nips](https://github.com/nostr-protocol/nips)에 병합된 PR은 없습니다. 이전 호 종료 후 여섯 제안이 열렸고, 그중 세 개는 초안이 처음 배포된 뒤인 8월 18일에 열렸습니다.

[NIPs PR #2438](https://github.com/nostr-protocol/nips/pull/2438)은 NIP-9A, 댓글 기반 패치를 제안합니다. 패치는 패치 대상을 부모로 참조하는 kind `1111` 댓글이며 `content`는 문자열 `PATCH`로 시작한 뒤 패치 줄이 이어집니다. 숫자로 시작하는 줄은 `<index> -<deleted> +<inserted> <inserted characters>` 형태로 대상 `content`를 편집하며, 바이트가 아니라 유니코드 문자로 셉니다. `t`로 시작하는 줄은 `title`, `description`, `subject`, `picture` 같은 사람이 읽는 태그를 교체합니다. 설계는 의도적으로 하위 호환입니다. 형식을 이해하지 못하는 클라이언트는 패치를 일반 라벨 댓글로 보여 주고, 이해하는 클라이언트는 패치를 적용하고 댓글을 숨깁니다. 제안은 kind `1`, `11`, `1111`, `24`, `1621`을 패치 가능으로 이름 짓고, 작성자와 독자 모두 너무 크거나 많거나 원본 이벤트 훨씬 뒤에 게시된 패치를 거부하도록 요청해, 불변 이벤트의 일반 편집 채널이 되지 않게 합니다.

[NIPs PR #2437](https://github.com/nostr-protocol/nips/pull/2437)은 [NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md), kind `1063` 이벤트로 업로드 파일을 설명하는 파일 메타데이터 사양에 파일 암호화를 제안합니다. `encryption-algorithm`(나열된 값은 `aes-gcm`만), hex `decryption-key`, `decryption-nonce` 세 optional 태그를 추가합니다. 태그 의미도 따라 바뀝니다. `m`은 암호화 전 MIME, `x`는 암호화 파일 해시, `ox`는 원본 해시이며, `thumb`, `image`, `fallback` 소스도 같은 키·nonce로 암호화됩니다. 목적은 공개 Blossom 운영자가 바이트 내용을 알 수 없게 하는 것이고, 저자는 [NIP-17](/ko/topics/nip-17/) DM 암호화 속성을 파일 메타데이터에 복사해 `imeta` 태그 안에서도 같은 처리가 되게 합니다.

[NIPs PR #2436](https://github.com/nostr-protocol/nips/pull/2436)은 [NIP-22](/ko/topics/nip-22/)(댓글) kind `1111` 답글이 있는 [NIP-7D](https://github.com/nostr-protocol/nips/blob/master/7D.md) 포럼 스레드 사양을 수정합니다. 스레드 게시를 kind `1` 노트처럼 인라인 이미지, 링크, [NIP-27](/ko/topics/nip-27/) 참조로 서식할 수 있다고 서식 절을 추가하고, 모호하지 않은 문법의 경량 마크업 언어 Djot도 지원할 수 있다고 합니다. 서식을 명시하지 않으면 결국 Markdown이 기본이 될 것이라는 논지이며, PR은 squalk를 기존 Djot 구현으로 가리킵니다.

[NIPs PR #2439](https://github.com/nostr-protocol/nips/pull/2439)은 [NIP-86](/ko/topics/nip-86/)에 `assign`·`unassign` 메서드를 추가해, 릴레이 관리자가 마스터 키를 공유하지 않고 다른 pubkey에 admin 권한을 부여할 수 있게 합니다.

[NIPs PR #2442](https://github.com/nostr-protocol/nips/pull/2442)는 [1월 호에서 Compass가 다룬](/ko/newsletters/2026-01-13-newsletter/) 오디오 트랙 제안을 이어 받습니다. 이전 PR은 닫혔고, 이 PR은 lightning.fm에서 kind `31337` 트랙, kind `31339` 릴리스, 밴드 프로필, 트랙별 기여자, 선택적 [NIP-57](/ko/topics/nip-57/) zap 분할을 쓰며 판매는 [NIP-99](/ko/topics/nip-99/)에 둡니다. 상호운용 계약은 [lightning.fm/interop](https://lightning.fm/interop)에 있고, 데스크톱 publisher와 self-hosted seller daemon은 오픈 소스입니다.

### Marmot

[Marmot PR #416](https://github.com/marmot-protocol/marmot/pull/416)은 8월 13일 병합되어 프로토콜 코어에 내구성·재시작 계약을 추가합니다. 채택 문서는 결정적 수렴, 보존 candidate-parent material, apply 전 publish, 기록 누락 시 fail-closed를 이미 정의했지만, 그 사이에서 프로세스가 중단될 때 무엇이 일어나는지에 대한 하나의 명확한 규칙은 없었습니다. 변경은 복구 가능 논리 사실, 재시작 동치, publish·수렴 중단 경계, observer-atomic 전환, 누락·손상 material 처리, application-effect 복구를 정의하고, 각각에 대한 crash·재시작 적합 시나리오를 추가합니다. transaction, journal, snapshot, replay 전략, scheduler, storage format은 구현 정의로 남기고, wire encoding 변경은 필요 없다고 합니다. 막는 구체적 실패는 외부에서 수락됐지만 로컬에서 확인되지 않은 publish, 또는 부분 적용된 선택 branch가 재시작 후 구현 의존 프로토콜 결과를 내는 경우입니다.

### Concord와 CORDs

[Concord PR #18](https://github.com/concord-protocol/concord/pull/18)은 지난주 호에서 열린 제안으로 다뤘으며 8월 15일 병합되었습니다. 암호화 커뮤니티 목록을 kind `33302` 이벤트로 샤딩하고, 50 멤버십 한도를 없애며, 은퇴 항목을 pruning해 목록이 릴레이 크기 한도 안에 머물게 합니다. Vector 이번 주 릴리스 노트는 동점 해결과 변경 없는 데이터 재게시 중단을 포함한 클라이언트 측 변경을 기록합니다.

[Concord PR #22](https://github.com/concord-protocol/concord/pull/22)는 커뮤니티 소유 AV broker를 제안합니다. CORD-02 메타데이터 entity가 relay 옆 optional `av_brokers` 목록을 carry하고 entity의 나머지처럼 edition으로 진화하며, CORD-07 rendezvous는 그 목록에서, 커뮤니티가 none을 게시하면 멤버 broker에서, 기존 room-keyed tie-break 순으로 뽑습니다. presence의 broker 태그는 잔여 split 보고에 여전히 읽히고 유용하며, 라우팅에서 강등하는 논지는 직접적입니다. broker로 라우팅하면 동료 멤버의 신뢰할 수 없는 입력이 커뮤니티 지시보다 우선합니다.

[Concord PR #23](https://github.com/concord-protocol/concord/pull/23)은 CORD-05에서 기존 구현 동작을 normative로 만듭니다. join을 영속하기 전에 owner genesis metadata edition이 전달된 키로 열려야 하고, 회전 plane은 compaction pair에 anchor합니다. PR은 처음부터 live 취약점이 아니었다고 밝힙니다. Vector bundle 수락은 전달 root가 owner genesis를 열 수 없는 bundle을 거부하고, 이미 보유한 커뮤니티 invitation을 주차하지 않으며, Armada는 held community base를 옮길 bundle을 drop합니다. gap은 사양이 요구하지 않아 사양 충실 클라이언트가 취약 버전을 출하할 수 있었다는 점입니다.

[Blossom upgrade 문서](https://github.com/hzrd149/blossom), [Napplet application 제안](https://github.com/napplet/naps), [Gamma Markets 사양](https://github.com/GammaMarkets/market-spec)은 이 기간 변경이 없었습니다.

## NIP 심층 분석

### 배지 (NIP-58)

[NIP-58](/ko/topics/nip-58/)은 [주 사양](https://github.com/nostr-protocol/nips/blob/master/58.md)이 정의하며, 한 Nostr 신원이 다른 신원에 이름 붙은 토큰을 수여하고, 수신자가 프로필 표시 여부를 통제하게 합니다. 해결하는 문제는 Nostr에서 사람에 대한 진술이 그냥 노트였다는 점입니다. 누가 주장을 발행했는지, 주장 이름, 모양, 대상이 수락했는지를 말하는 구조가 없었습니다. 배지는 그 주장에 세 가지 별도 서명 이벤트와 세 작성자 의도를 부여합니다.

[메커니즘](https://github.com/nostr-protocol/nips/blob/master/58.md)은 주소 지정 가능 정의, 수여, 표시 목록으로 이루어집니다. 배지 정의는 발행자가 게시하는 kind `30009` 이벤트로 `d` 태그로 주소 지정되어, 발행자가 `name`, `description`, `image`, `thumb` 태그를 나중에 고쳐도 다른 것이 가리키는 식별자는 바뀌지 않습니다. 수여는 같은 발행자의 kind `8` 이벤트로, 정의의 `30009:<issuer-pubkey>:<d-identifier>` 좌표를 담은 `a` 태그와 하나 이상의 수신자 `p` 태그를 carry합니다. 표시 목록은 수신자가 고정 `d` 값 `profile_badges`로 게시하는 kind `30008` 이벤트로, `a`와 `e` 태그 쌍을 나열합니다. `a`는 정의 좌표, `e`는 특정 수여 이벤트입니다. 쌍으로 읽으며, 짝 수여가 없는 `a`나 짝 정의가 없는 `e`는 무시되어 반쪽 참조 배지는 조용히 렌더링되지 않습니다.

[사양](https://github.com/nostr-protocol/nips/blob/master/58.md)이 거부하는 것에서 설계 tradeoff가 보입니다. 취소·만료 메커니즘이 없어 수여는 그 순간 발행자의 영구 진술이고, 마음이 바뀐 발행자는 수여가 가리키는 정의만 바꿀 수 있습니다. 양도가 없어 배지는 토큰처럼 유통되지 않습니다. 신뢰 issuer registry도 없어 신뢰 질문 전체가 클라이언트와 독자에게 밀립니다. 배지 가치는 보는 사람에게 발행자 공개 키가 가진 가치 그 자체입니다. 사양은 클라이언트가 수신자가 나열한 것보다 적게 표시하고 어떤 이미지 크기를 렌더할지 선택할 여지를 주어, 프로필이 제3자가 고른 그래픽 벽이 되지 않게 합니다.

가장 가까운 인접 사양은 [NIP-51](/ko/topics/nip-51/), [목록 사양](https://github.com/nostr-protocol/nips/blob/master/51.md)이며, 둘을 비교하면 배지가 왜 한 이벤트가 아닌 세 이벤트인지 드러납니다. 목록은 한 작성자가 참조를 큐레이션하고, 목록 작성자가 주장 작성자입니다. 배지는 authorship을 반으로 나눕니다. 발행자는 수여가 일어났다고 서명하고, 수신자는 표시를 수락한다고 서명합니다. 어느 한쪽도 보이는 결과를 혼자 만들 수 없고, 이것이 배지를 self-applied label과 구분합니다.

이번 주 [nos.lol](https://nos.lol)과 [relay.primal.net](https://relay.primal.net)에서 복구한 live kind `8` 수여:

```json
{
  "id": "08504dec368939bd63849a349cab83dea0ac199a852129dbf68cf35fe5c64e96",
  "pubkey": "bef514bd58c8ceea4beb9e6b84a8d983935f7be26f49e14df68098f1ba64156e",
  "created_at": 1787051248,
  "kind": 8,
  "tags": [
    ["a", "30009:bef514bd58c8ceea4beb9e6b84a8d983935f7be26f49e14df68098f1ba64156e:blocks_orange_league"],
    ["p", "92dfa05d915196a7a09152fa3f57871debfd422e1d278ac5af266a70c3350b1f", "wss://relay.damus.io"]
  ],
  "content": "Badge awarded!",
  "sig": "5bf0218dfec5e56b47339b0b4b992cceedd2e18798fb3d47cafea51850c00827f66251e4a3e08190370e04a5e1d4d092eeb441141b7219acdd18b80290a022f8"
}
```

현재 구현은 발행, 표시, 읽기를 다룹니다. [Divine Mobile 1.0.20](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.20)은 앱 안에서 배지를 발행·수여하고 독자가 탭하면 획득 조건을 설명하며, [Nostter PR #2281](https://github.com/SnowCait/nostter/pull/2281)은 웹 클라이언트 프로필 배지 처리를 갱신하고, [Amethyst](https://github.com/vitorpamplona/amethyst)는 자체 client tag를 담은 수여 이벤트를 게시하며 위 예시와 같은 릴레이 데이터에 나타납니다.

### 댓글 (NIP-22)

[NIP-22](/ko/topics/nip-22/)는 [주 사양](https://github.com/nostr-protocol/nips/blob/master/22.md)이 정의하는 일반 댓글 이벤트로, 짧은 텍스트 노트가 아닌 것에 답합니다. 짧은 노트 스레딩은 kind `1`과 reply chain 주변에서 자란 [NIP-10](/ko/topics/nip-10/)이 이미 있었습니다. NIP-22는 동영상, 기사, 캘린더 이벤트, wiki 페이지, URL처럼 대상 kind를 밝히고, 대상이 주소 지정 가능하거나 Nostr 이벤트가 전혀 없는 외부 자원일 때도 동작하는 reply 구조가 필요해서 존재합니다.

[메커니즘](https://github.com/nostr-protocol/nips/blob/master/22.md)은 대소문자 구분에 달려 있습니다. 댓글은 kind `1111` 이벤트로 두 세트 태그를 carry합니다. 대문자 태그는 토론 root, 소문자 태그는 직계 parent를 설명합니다. `E`, `A`, `I`는 root 이벤트, root 주소 지정 좌표, root 외부 식별자, `K`는 root kind, `P`는 root 작성자입니다. 소문자 `e`, `a`, `i`, `k`, `p`는 parent에 대해 같은 사실을 이름 짓는데, top-level 댓글에서는 parent가 root이고 nested reply에서는 다른 kind `1111` 댓글입니다. 분리 덕분에 클라이언트는 reply chain을 걷지 않고 대문자 root 태그 하나의 필터로 전체 토론을 가져올 수 있고, 소문자 parent 태그로 nesting을 올바르게 렌더합니다. `I`·`i` variant는 [NIP-73](/ko/topics/nip-73/) 형식 외부 식별자를 carry해, 웹 페이지, 팟캐스트 에피소드, 책에 댓글 스레드를 붙일 수 있습니다.

tradeoff는 대부분 NIP-22가 흡수하지 않기로 한 것에 관한 것입니다. [사양](https://github.com/nostr-protocol/nips/blob/master/22.md)은 kind `1` 노트에 답하는 데 댓글을 쓰지 말라고 하여, 같은 객체 위에서 두 스레딩 모델이 경쟁하지 않고 NIP-10이 이미 동작하는 곳에 남깁니다. nesting은 허용되지만 root는 고정되어, 깊은 스레드도 중간 이벤트를 잃어도 anchor를 잃지 않습니다. kind 태그가 부하를 짊어집니다. 대상 없이 댓글만 가져와도 `K`와 `k`로 무엇을 보고 있는지 알고, 그 kind를 렌더할 수 있는지 결정합니다. 사양이 제공하지 않는 것은 ordering·moderation 모델로, 표시 순서, 접기, 숨기기는 전적으로 클라이언트 정책입니다.

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md)과 비교하면 차이는 typing에 있습니다. NIP-10은 대상이 노트라고 가정하고 스레드 위치를 인코딩합니다. NIP-22는 대상 identity와 kind를 명시적으로 인코딩하고 그 밖은 가정하지 않습니다. 그 명시적 typing 때문에 이번 호의 새 제안들이 kind `1111`을 집습니다. 댓글은 이미 무엇에 붙었는지 기계가 읽을 수 있는 진술을 carry합니다.

이번 주 [nos.lol](https://nos.lol)과 [relay.primal.net](https://relay.primal.net)에서 복구한, 동영상 아래 다른 댓글에 답한 live kind `1111` 댓글:

```json
{
  "id": "c8d335f8bfea58ecd1a943d6000fb2045f4bddf4a36c67df53eb661671f7ab45",
  "pubkey": "3e911baba55ae247339cf805dd6ff49ad2cd6bee84ac44e088ce66450c49104f",
  "created_at": 1787062681,
  "kind": 1111,
  "tags": [
    ["E", "1c492f2bac17b79d66934a340fa43d8d30d0aea4c9fa329346c05573ef912d70", "", "482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839"],
    ["A", "34236:482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839:e64ba9ea157b1a315caff51dbca656ed73ce817d4494e3966adf24055a86f5c5", ""],
    ["K", "34236"],
    ["P", "482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839"],
    ["e", "7a14723b9ef999e74b1757a0fb74942cb6c121138d4ddafe096a57a67ed0a442", "", "8b69e548402afa997343d73e8088224a440f256350f6257b61acc4bb1fa4af4f"],
    ["k", "1111"],
    ["p", "8b69e548402afa997343d73e8088224a440f256350f6257b61acc4bb1fa4af4f"],
    ["client", "Divine", "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile", "wss://relay.divine.video"]
  ],
  "content": "niiice",
  "sig": "a5517fdea07647efa7ab1730fbea8df882690bba667e93ea5aeba4a73be6a49af1ee17c045535483650caf41dbbcb0897d5803fa39b59f395fd6f9bb193bb789"
}
```

대문자 태그는 동영상과 작성자를, 소문자 `e`와 `k`는 parent 댓글을 가리키며, 이것이 사양이 설명하는 형태입니다. kind `1111`을 읽고 쓰는 구현에는 위 이벤트에 client tag가 보이는 [Divine Mobile](https://github.com/divinevideo/divine-mobile), 같은 릴레이 결과에 댓글이 나타나는 [Amethyst](https://github.com/vitorpamplona/amethyst), 이번 주 스레드 게시를 포럼 게시로 렌더하는 [nostrord](https://github.com/nostrord/nostrord/pull/274)가 있습니다. [NIPs PR #2438](https://github.com/nostr-protocol/nips/pull/2438)의 제안 패치 형식도 같은 kind 위에 쌓입니다.

---

프로젝트나 소식을 [Nostr Compass 프로젝트](https://github.com/andotherstuff/nostr-compass)에 [NIP-17](/ko/topics/nip-17/) DM으로 보내 공유하세요.
