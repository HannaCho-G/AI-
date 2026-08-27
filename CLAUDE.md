# HannaK Ebook Team

Claude Code를 지휘자로 삼아 전자책을 기획→조사→집필→검증→편집→비주얼→출판→업로드→교차판매 연결까지 파이프라인으로 생산하는 프로젝트.

한 번 세팅해두고, 새 책 아이디어가 나올 때마다 `books/`에 새 프로젝트만 만들어서 같은 팀을 재사용한다.

## 브랜드 전략 (최상위 문서)

`docs/brand-strategy.md`가 모든 책 위에 있는 최상위 브랜드/사업 전략 문서다. Publisher와 Content Connector는 새 책을 기획하거나 교차판매를 매핑할 때 반드시 이 문서를 먼저 확인한다. 핵심 요지:

- 최상위 브랜드는 **KOREA**, 하위 축은 Korean Food / Culture / History / Great Koreans / Beauty / Education / Lifestyle / Travel.
- 콘텐츠는 **본편(Core Series, 번호형)**과 **스페셜 에디션(Special Edition, 무번호·독립 출시)**의 이원 구조.
- 모든 콘텐츠는 제작 전 3가지 질문을 통과해야 한다: (1) 외국인이 실제로 궁금해할 질문인가 (2) 독립 구매할 맥락이 있는가 (3) 완성 후 최소 2개 이상의 연관 콘텐츠와 연결되는가.
- 초기 우선 축은 Korean Food / Korean Culture / Korean Travel. (현재 Food·Culture는 진행중 — 상세 진행 상황은 `docs/brand-strategy.md`의 "진행 상황" 표 참고)

## 팀 구성 (서브에이전트)

`.claude/agents/`에 9개의 역할이 정의되어 있고, Claude Code의 Agent 툴로 `subagent_type`을 지정해서 호출한다.

| 순서 | 에이전트 | 파일 | 역할 |
|---|---|---|---|
| 1 | Publisher | `.claude/agents/publisher.md` | 기획서 작성 (독자층/판매포인트/분량/목차/조사범위) |
| 2 | Researcher | `.claude/agents/researcher.md` | 주제별 모드(Culture/History/Travel 등)로 자료 조사 |
| 3 | Writer | `.claude/agents/writer.md` | 챕터 단위 집필 (한 번에 전체 원고 X) |
| 4 | Fact Checker | `.claude/agents/fact-checker.md` | Writer와 독립적으로 사실검증, CONFIRMED/NEEDS REVIEW/UNSUPPORTED 태깅 |
| 5 | Editor | `.claude/agents/editor.md` | 중복제거, 흐름, 외국인 독자 기준 문장 다듬기, 문체 통일 |
| 6 | Visual Director | `.claude/agents/visual-director.md` | 챕터별 시각자료(사진/비교표/타임라인/지도) 계획 |
| 7 | Production | `.claude/agents/production.md` | 원고 → EPUB/PDF, 목차/페이지번호/표지/내부링크/참고자료 |
| 8 | Uploader | `.claude/agents/uploader.md` | 완성된 전자책을 실제 판매 플랫폼(KDP/Gumroad/Whop/Etsy/eBay 등)에 브라우저 자동화로 업로드·제출 |
| 9 | Content Connector | `.claude/agents/content-connector.md` | 기존 책들과의 교차판매/연관 콘텐츠 매핑 |

너(HannaK)는 **Publisher/Creative Director**: 아이디어를 던지고, 각 단계 산출물을 승인하거나 "이건 별로야, 다시" 하면서 되돌린다.

```
너 (아이디어 + 승인)
 ↓
Publisher → Researcher → Writer → Fact Checker → Editor → Visual Director → Production → Uploader → Content Connector
 ↓
완성된 책 (플랫폼에 실제 업로드까지 완료)
```

## 새 책 시작하기

`/new-book` 스킬을 쓰거나, "NEW BOOK: <주제>" 라고 말하면 된다. 시작하는 방법은 두 가지다.

- **한 줄 아이디어만 던지는 경우**: Publisher가 처음부터 기획서(독자층/판매포인트/분량/목차/조사범위)를 새로 작성한다.
- **기획보고서를 이미 만들어서 첨부하는 경우**: Publisher는 새로 기획하지 않는다. 첨부된 기획보고서를 그대로 표준 포맷(`00-brief.md`)으로 옮기고, 빠진 항목만 확인 질문을 하거나 "미정"으로 표시한다. 원본 보고서는 `books/<slug>/00-brief-original.md`로 같이 보관해서 나중에 대조할 수 있게 한다. 즉, **팀 전체가 사용자가 준 기획보고서를 기준으로 움직이는 워크플로우**를 기본으로 지원한다.

진행 순서:

1. `templates/`에서 템플릿 선택: `culture`, `history`, `biography`, `travel`, `food` (기획보고서에 카테고리가 명시돼 있으면 그걸 우선한다)
2. `books/<slug>/` 프로젝트 폴더 생성
3. Publisher 에이전트 호출(위 두 모드 중 하나) → `books/<slug>/00-brief.md` 작성
4. 승인 후 파이프라인 순서대로 각 에이전트 호출, 산출물은 `books/<slug>/` 아래 단계별 파일로 축적
5. 각 단계 끝날 때마다 사용자에게 산출물을 보여주고 승인/수정 지시를 받는다

자세한 오케스트레이션 절차는 `.claude/skills/new-book/SKILL.md` 참고.

## 책 프로젝트 폴더 구조 (`books/<slug>/`)

```
00-brief.md              # Publisher 기획서 (표준 포맷)
00-brief-original.md     # (기획보고서 첨부 모드일 때만) 사용자가 준 원본 그대로
01-research/             # Researcher 산출물 (챕터별 또는 주제별 파일)
02-chapters/             # Writer 산출물 (챕터별 .md, 한 파일 = 한 챕터)
03-factcheck/            # Fact Checker 리포트 (챕터별, CONFIRMED/NEEDS REVIEW/UNSUPPORTED)
04-edited/                # Editor가 다듬은 최종 원고 (챕터별)
05-visuals.md             # Visual Director의 시각자료 계획
06-production/            # Production 산출물 (EPUB/PDF, 표지 등 실제 파일은 여기)
07-upload/                # Uploader의 플랫폼별 제출 기록/상태 (실제 리스팅 URL 포함)
08-cross-sell.md          # Content Connector의 연관 콘텐츠 맵
```

## 원칙

- Writer는 챕터 단위로만 작업한다. 한 번에 60페이지를 요청하지 않는다.
- Fact Checker는 Writer의 결과를 그대로 신뢰하지 않고 독립적으로 검증한다. 날짜/숫자/역사적 사실/인물/지명/통계/현재 운영정보를 우선 확인한다.
- Editor 단계에서 "AI가 쓴 티"가 나는 화려한 표/도표보다, 실제 PPT SmartArt 같은 자연스러운 시각 정리를 지향한다 (Visual Director 기준에도 동일 적용).
- Content Connector는 책이 완성될 때마다 `books/` 전체를 훑어서 새 책과 연결되는 기존 책을 찾는다 (예: Hagwon → Korean Education → Korean Culture / Gyeongju → Silla → Korean History → Travel).
- Uploader는 실제 계정 자격증명(비밀번호/세션)을 저장소에 절대 커밋하지 않는다 — `automation/uploader/` 아래 gitignore 처리된 위치에서만 다룬다. 각 플랫폼에 최종 제출(Publish)하기 전에는 항상 사용자에게 제목/가격/카테고리/파일을 요약해서 보여주고 확인받는다.
- 팀은 책마다 새로 만들지 않는다. 하나의 팀(`​.claude/agents/`)을 계속 재사용하고, 책마다 `books/<slug>/`만 새로 생긴다.

## 업로드 자동화 (`automation/uploader/`)

Uploader 에이전트가 쓰는 브라우저 자동화(Playwright) 스크립트와 로그인 세션이 저장되는 곳. 자세한 내용과 플랫폼별 유의사항은 `automation/uploader/README.md` 참고. 실제 비밀번호나 세션 파일은 `.gitignore`로 제외되어 있어 저장소에는 절대 올라가지 않는다.
