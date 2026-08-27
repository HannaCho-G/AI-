---
name: new-book
description: 새 전자책 프로젝트를 시작하고 HannaK Ebook Team 파이프라인(Publisher → Researcher → Writer → Fact Checker → Editor → Visual Director → Production → Content Connector)을 순서대로 돌린다. 사용자가 "NEW BOOK", "새 책 시작", 한 줄 주제 아이디어, 또는 기획보고서 파일을 줄 때 사용한다.
---

# New Book

HannaK Ebook Team의 오케스트레이션 스킬. 아이디어 하나 또는 기획보고서 하나를 받아서 완성된 책까지 파이프라인을 순서대로 진행한다.

## 입력 형태 판별 (가장 먼저 할 일)

사용자가 이번에 준 것이 다음 중 무엇인지 확인한다:

- **한 줄 아이디어**: "OO 주제로 책 하나 만들자" 같은 짧은 문장뿐이고, 별도로 첨부된 기획 문서가 없다.
  → Publisher 서브에이전트를 **모드 A**로 호출 (`.claude/agents/publisher.md` 참고).
- **기획보고서 첨부**: 사용자가 파일을 첨부했거나, 이미 만들어진 기획서 텍스트를 통째로 붙여넣었다.
  → Publisher 서브에이전트를 **모드 B**로 호출한다. 이 경우 Publisher는 새로 기획하지 않고 기존 보고서를 표준 포맷으로 옮기기만 한다는 점을 호출 프롬프트에 명시한다.

어느 쪽인지 애매하면, 새로 만들지 말고 사용자에게 "이미 만들어둔 기획서가 있는지" 먼저 확인한다.

## 진행 순서

1. **프로젝트 폴더 준비**: 주제를 영문 kebab-case로 slug화해서 `books/<slug>/`를 만든다. `templates/`에서 카테고리에 맞는 템플릿(culture/history/biography/travel/food)을 고른다 — 모드 B라면 기획보고서에 이미 명시된 카테고리를 우선한다.
2. **Publisher** 호출 (모드 A 또는 B) → `books/<slug>/00-brief.md` 생성 → 사용자에게 보여주고 승인받는다.
3. 승인 후 **Researcher** 호출 → 기획서의 조사 범위대로 `books/<slug>/01-research/`에 챕터별 자료 저장.
4. 챕터마다 **Writer** 호출 (한 번에 한 챕터씩) → `books/<slug>/02-chapters/`.
5. 챕터마다 **Fact Checker** 호출 (Writer와 독립적으로) → `books/<slug>/03-factcheck/`. `UNSUPPORTED`가 많으면 Writer/Researcher로 되돌린다.
6. 검증된 챕터를 **Editor** 호출 → `books/<slug>/04-edited/`.
7. **Visual Director** 호출 → `books/<slug>/05-visuals.md`.
8. **Production** 호출 → `books/<slug>/06-production/` (합본 원고, 표지 브리프, 프로덕션 노트).
9. **Content Connector** 호출 → `books/<slug>/07-cross-sell.md` + 최상위 `books/CROSS-SELL-MAP.md` 갱신.

## 중간 승인 원칙

각 단계 산출물이 나오면 다음 단계로 자동으로 넘어가지 않는다. 사용자에게 결과를 요약해서 보여주고, 아래 중 하나를 확인한다:
- 승인 → 다음 단계 진행
- "이건 별로야/ 이거 추가해 / 이 방향으로 틀어" → 해당 에이전트를 같은 입력에 사용자 피드백을 더해서 재호출 (이전 단계로 되돌아감)

Writer 단계는 챕터 수만큼 반복 호출된다는 것을 항상 염두에 둔다 — 절대 "전체 원고 써줘" 식으로 한 번에 요청하지 않는다.

## 팀 재사용

이 스킬은 책마다 새로 만들어지지 않는다. `.claude/agents/`의 8개 에이전트는 고정이고, 책마다 `books/<slug>/`만 새로 생긴다. "NEW BOOK: <주제>" 또는 기획보고서 첨부만으로 다음 책을 바로 생산라인에 넣을 수 있어야 한다.
