## 챕터 3: The Hoju System & The Architecture of Legal Transformation

이 챕터는 법률번호·조문번호·날짜·헌재 사건번호가 문장 단위로 정확해야 하는 챕터다. 배정된 Figure 5, 6 모두 그 정확성이 핵심 정보이므로, 아래 두 항목 모두 **AI 이미지 생성 대상에서 제외(분류 3)**하고 실제 제작을 권장한다. AI 이미지 생성 모델은 한글/영문 텍스트, 조문 번호, 날짜 숫자를 안정적으로 정확히 그리지 못하며, 이 챕터에서 텍스트가 한 글자라도 틀리면 책 전체의 신뢰도(법률 정보 정확성)에 타격을 준다.

파일명 규칙 (Production 참고): 실제 제작된 파일은 `ch3-img01.png`, `ch3-img02.png` (또는 `.jpg`/`.pdf`, 벡터가 필요하면 `.svg`)로 저장해서 `06-production/images/`에 넣으면 이미지 ID로 원고에 자동 매칭 가능.

---

### [ch3-img01] 위치: Figure 5 — 3.5절 마지막 문단 뒤 (본문 중 `[FIGURE 5 — BEFORE/AFTER REGISTRATION ARCHITECTURE ...]` 표시 자리), Full page

- 종류: 등록 체계 Before/After 비교 다이어그램 (조직도/SmartArt형)
- 분류: **AI 생성 비권장 — 분류 3 (법률명·조문번호·인증서 명칭의 정확성이 핵심)**
- 내용 (실제 제작 시 아래 구조 그대로 사용):

  **왼쪽 패널 — BEFORE (Hojeok 체제, ~2007년까지)**
  - 최상단 노드: "Hoju 호주 (Head of Family)"
  - 그 아래 종속 노드들(같은 등록부에 나란히 종속 표시): "Spouse 처", "Children 자녀", "Other registered members (e.g., 동거인 지위의 재혼 배우자)"
  - 하나의 통합 문서로 표시: "Hojeok Deungbon 호적등본 — single omnibus document, discloses entire family's marital/divorce history to any requester"
  - 근거 법률 라벨: "Civil Act (민법) Articles 778, 781, 826(3) — pre-2005 text"

  **오른쪽 패널 — AFTER (개인별 등록, 2008년 1월 1일~)**
  - 중앙 노드: "Individual 개인" (호주 없이 독립적으로 존재)
  - 그로부터 뻗어나가는 5개의 개별 인증서 노드 (정확한 명칭 그대로):
    1. 가족관계증명서 Family Relation Certificate — 부모/배우자/자녀 3대만, 형제자매·본관 계보 제외
    2. 기본증명서 Basic Certificate — 출생·사망·신분변경·국적
    3. 혼인관계증명서 Marriage Relation Certificate — 본인의 혼인·이혼 이력만
    4. 입양관계증명서 Adoption Relation Certificate — 일반 입양 및 파양
    5. 친양자입양관계증명서 Special Adoption Certificate — 완전 입양, 친생관계 기록 봉인, 제14조 제2항에 따라 발급 제한
  - 근거 법률 라벨: "Act on Registration of Family Relations (가족관계의 등록 등에 관한 법률, Act No. 8435), effective 1 January 2008"

  하단 공통 캡션 (원고에 이미 지정됨): "The reform changed the administrative grammar of family without erasing social hierarchy." / Source: Act on Registration of Family Relations and Korean legal commentary.

- 제작 권장 방식: Canva의 "Comparison" 또는 "Org Chart" 템플릿, 혹은 PowerPoint SmartArt(계층 구조형)로 좌/우 두 트리를 나란히 배치. 인증서 5종은 아이콘 하나씩 붙여도 좋지만 명칭 텍스트가 정확히 들어가는 것이 아이콘보다 중요. 디자이너에게 위 구조를 그대로 전달하면 됨.

- (선택) 장식용 배경 이미지가 필요할 경우에만 아래 프롬프트 사용 — 텍스트나 실제 관인/직인처럼 보이는 요소는 절대 넣지 않도록 명시(공문서 위조로 오인될 위험):

  > "Abstract editorial background texture for a legal-history infographic: subtle network of thin connecting lines and faint document-grid patterns suggesting bureaucratic record-keeping, no readable text anywhere in the image, no official seals or stamps of any kind. Bold, vivid editorial infographic style like a premium travel magazine or National Geographic graphic — NOT a flat pastel minimalist AI-assistant style, NOT a gaudy neon/gradient AI-generated look. Use a confident deep indigo and warm terracotta accent palette with strong contrast, not muted pastels. Clean geometric composition with a clear focal gradient from left (dense, hierarchical node cluster) to right (loose, evenly distributed individual nodes), symbolizing a shift from hierarchy to individuation — purposeful use of color blocks to create visual interest, avoid excessive empty white space and avoid unrelated decorative icons. No gradients used as glow effects, no neon, no 3D bevels. 4:3 ratio, full-page ebook illustration, background only — designed to sit behind a separately typeset diagram, so keep the center-left area low-contrast enough for white diagram boxes and text to be legible on top."

---

### [ch3-img02] 위치: Figure 6 — Figure 5 바로 아래 (본문 중 `[FIGURE 6 — LEGAL REFORM TIMELINE ...]` 표시 자리), One-third page

- 종류: 법 개혁 연표 (타임라인)
- 분류: **AI 생성 금지 — 분류 3 (법률번호·날짜·헌재 사건번호가 문장 단위로 정확해야 함)**
- 내용 (실제 제작 시 아래 7개 항목을 시간순 가로 타임라인으로, 각 항목은 날짜 + 1줄 설명):

  1. **1958-02-22** — Civil Act promulgated (Act No. 471); Hoju system codified into statute; in force from 1960-01-01
  2. **1989-12-19 / 1990-01-13** — 1990 Amendment passed by National Assembly / promulgated (Act No. 4199); in force from 1991-01-01 — property division on divorce, gender-neutral custody & parental authority
  3. **2000** — Citizens' Alliance for the Abolition of the Hoju System (호주제폐지를 위한 시민연대) formed; strategic constitutional litigation begins
  4. **2005-02-03** — Constitutional Court decision of non-conformity (2001Hun-Ga9 et al., 헌법불합치) — Civil Act Art. 778, latter part of Art. 781(1), main text of Art. 826(3)
  5. **2005-03-02 / 2005-03-31** — National Assembly passes Civil Act amendment abolishing Hoju provisions / promulgated as Act No. 7427 (mostly effective 2008-01-01)
  6. **2005-12-22** — Constitutional Court decision (2003Hun-Ga5·6) — paternal-surname rule, first clause of Art. 781(1), also non-conformity
  7. **2008-01-01** — Hojeok closes; Act on Registration of Family Relations (Act No. 8435) takes effect; individualized registration begins

  캡션 (원고 지정): "Legal transformation unfolded through successive amendments and institutional implementation." / Sources: KLRI Civil Act; Constitutional Court and NHRC materials.

- 제작 권장 방식: 스프레드시트에 위 7행을 입력한 뒤 Canva "Timeline" 템플릿에 그대로 옮기거나, 디자이너에게 위 표를 그대로 전달. 1/3페이지 분량이므로 항목당 텍스트를 짧게(위 요약 수준) 유지할 것. 장식용 배경조차 필요 없을 만큼 작은 사이즈이므로 별도 AI 프롬프트는 제공하지 않음 — 필요하면 ch3-img01과 동일한 배경 프롬프트를 재사용하되 톤 다운해서 사용 가능.

---

### 주의사항 — 실존 인물 (이태영 변호사)

3.1절에 이태영 변호사(Lee Tai-young, 한국 최초 여성 변호사)가 실명으로 언급된다. 이번에 배정된 Figure 5·6에는 인물 삽화가 포함되지 않으므로 별도 이미지 ID는 만들지 않았다. 다만 향후 Production 단계나 다른 챕터에서 이태영 변호사를 시각적으로 표현하고 싶다면:

- 사실적 초상(realistic portrait)을 AI로 생성하지 말 것 — 실존 인물의 얼굴을 지어내는 것이므로 부정확하고 오해의 소지가 있다.
- 굳이 넣는다면 "예술적 삽화(artist's impression), 실제 초상이 아님"이라는 문구를 프롬프트와 캡션 모두에 명시하고, 얼굴 특징을 특정하지 않는 상징적/실루엣 형태(예: 법정에서 서류를 든 여성 변호사의 뒷모습 실루엣, 얼굴 비특정)로 제한할 것을 권장.

---

### Production 참고 요약

| 이미지 ID | Figure | 분류 | AI 생성 | 제작 방식 |
|---|---|---|---|---|
| ch3-img01 | Figure 5, full page | 등록 체계 Before/After 다이어그램 | 배경만 선택적 생성 가능 (본문 다이어그램은 실제 제작) | Canva/PowerPoint SmartArt, 조직도형 |
| ch3-img02 | Figure 6, one-third page | 법 개혁 연표 | 불가 | 스프레드시트 → Canva 타임라인 템플릿 |
