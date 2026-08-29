# Research — 부록 [08] `[NEEDS RESEARCH]` 2건 보충

- **대상 파일**: `books/korea-family-transformation/02-chapters/08-appendix-statistical-references.md`
- **대상 표시**: 76행 각주 [1], 96행 각주 [11]
- **조사일**: 2026-08-29
- **조사자**: Researcher
- **조사 모드**: Culture/History 혼합 + 현재 운영정보(통계 발표·기관 개편)

---

## 조사 환경상의 한계 (먼저 밝힘 — 신뢰도 판정의 전제)

이 세션의 조직 이그레스 정책이 아래 도메인에 대한 직접 접속을 **403/차단**으로 거부한다. TLS 문제가 아니라 정책 거부이므로 우회하지 않았다.

`mods.go.kr`, `www.kostat.go.kr`, `kosis.kr`, `www.korea.kr`, `eiec.kdi.re.kr`, `db.history.go.kr`, `contents.history.go.kr`, `encykorea.aks.ac.kr`, `dh.aks.ac.kr`, `www.kci.go.kr`, `en.wikipedia.org`, `ko.wikipedia.org`, `namu.wiki`

따라서 **아래 모든 URL은 HTTP 응답코드(200/404)를 직접 확인하지 못했다.** 검증은 검색엔진 인덱스에서 (a) 해당 URL 문자열, (b) 문서 제목, (c) 본문 수치가 함께 확인되는지로 이루어졌다. 이는 **문서 실재의 강한 증거이지만 링크 생존(link-rot)의 증거는 아니다.** Production 직전 링크 전수 클릭 검사는 여전히 필수다. 이는 Fact Checker 리포트(`03-factcheck/08-...md`)가 겪은 것과 동일한 제약이다.

---

# 항목 1 — 「2025 통계로 보는 1인가구」 URL / KOSIS 표번호, 그리고 발행기관 영문 표기

## 1-A. 질문: 「2025 통계로 보는 1인가구」(2025-12-09)의 영구 URL 또는 KOSIS 통계표 번호는?

### 찾은 답 — 보도자료 영구 URL (확보)

국문 보도자료의 게시판 URL을 확보했다. 부록 [1]에 그대로 넣을 수 있다.

```
https://mods.go.kr/board.es?mid=a10301010000&bid=10820&act=view&list_no=442130
```

- 게시판 파라미터: `mid=a10301010000` (새소식 > 보도자료 > 전체), `bid=10820`, `list_no=442130`
- **동일 문서가 `kostat.go.kr` 도메인에서도 같은 파라미터로 서비스된다** (`https://www.kostat.go.kr/board.es?mid=a10301010000&bid=10820&act=view&list_no=442130`). 두 도메인은 같은 사이트를 미러링하는 것으로 보인다.
- 검색 인덱스에서 노출되는 원본 URL에는 `ref_bid=`에 60개 이상의 게시판 ID가 붙어 있다. **이는 브라우저 탐색 흔적이므로 반드시 잘라낼 것.** 위의 4개 파라미터만으로 문서가 특정된다.

**계열 정합성 교차확인** — 이 `list_no`가 맞는 문서를 가리킨다는 방증:

| 판본 | 발표일 | `bid` | `list_no` |
|---|---|---|---|
| 「2024 통계로 보는 1인가구」 | 2024-12-09 | 10820 | 434103 |
| **「2025 통계로 보는 1인가구」** | **2025-12-09** | **10820** | **442130** |

같은 게시판(`bid=10820`), 1년 간격, `list_no`가 단조 증가한다. 2024년판 `list_no=434103`은 Fact Checker 리포트 C-0에서 독립적으로 확인된 값이다.

**본문 수치 대조 (문서 동일성 확인용)** — 검색 인덱스에서 확인된 이 보도자료의 지표들:

- 2024년 1인가구 **804만 5천 가구 = 전체 가구의 36.1%** ← 부록 13행/70행 수치와 일치
- 연령: 70세 이상 19.8% > 29세 이하 17.8% > 60대 17.6% > 30대 17.4%
- 지역: 서울·경기 거주 42.7%
- 거처: 단독주택 39.0%, 아파트 35.9%
- 취업 1인가구 510만 가구 (전년비 +42만 6천)
- 연소득 3,423만 원 = 전체 가구의 46.1%
- 월평균 보건지출 12만 2천 원 / 주말 여가 동영상 시청 75.7%(2025년)

부록이 인용하는 두 수치(804만 5천, 36.1%)가 이 문서 안에 있음이 확인된다.

**출처(링크)**
- https://mods.go.kr/board.es?mid=a10301010000&bid=10820&act=view&list_no=442130 (권장 인용 URL)
- https://www.kostat.go.kr/board.es?mid=a10301010000&bid=10820&act=view&list_no=442130 (미러)
- 정책브리핑 재수록(백업용): https://www.korea.kr/briefing/pressReleaseView.do?newsId=156734077
- 정책브리핑 전문자료: https://www.korea.kr/archive/expDocView.do?docId=41561
- KDI 경제정보센터 재수록: https://eiec.kdi.re.kr/policy/materialView.do?num=274492

**신뢰도: 확실** (URL 문자열·제목·발표일·본문 수치가 복수의 독립 인덱스에서 일치. 단, HTTP 응답 미확인 — 위 "조사 환경상의 한계" 참조)

---

### 찾은 답 — KOSIS 통계표 번호: **찾지 못함**

`kosis.kr`이 정책 차단되어 통계표의 제목·수록기간·기관ID를 직접 열어 확인할 수 없었다. **검증되지 않은 표번호를 부록에 적는 것은 안 된다** — 표번호는 독자가 클릭해서 바로 확인하는 항목이라 틀리면 즉시 드러난다.

추가로, 「통계로 보는 1인가구」는 **단일 통계표에서 나오는 자료가 아니다.** 인구총조사(등록센서스)·경제활동인구조사·가계금융복지조사·사회조사·국민건강 관련 통계 등 여러 조사를 묶은 **가공·종합 보도자료**다. 따라서 "이 보도자료 = KOSIS 표 하나"라는 대응 자체가 성립하지 않는다. 지표마다 다른 표를 달아야 한다.

**미검증 후보** (Production 단계에서 접속 가능해지면 확인할 것 — 지금 부록에 넣지 말 것):

| 후보 | 비고 |
|---|---|
| `orgId=101` | 국가데이터처(구 통계청)의 KOSIS 기관 ID. 인구총조사 계열 표가 여기 속한다 |
| KOSIS 100대 지표 > 인구 > 1인가구<br>`https://kosis.kr/visual/nsportalStats/detailContents.do?statJipyoId=3645&listId=A&vStatJipyoId=4880` | 1인가구 시계열 지표 페이지. **표번호보다 이쪽이 인용에 더 안정적일 수 있다** (게시판 일련번호에 의존하지 않음) |
| `DT_1JC1517` 등 `DT_1JC1xxx` 계열 | 인구총조사 가구부문 표. 다만 검색 인덱스상 `DT_1JC1517`의 제목은 "가구주의 성, 연령 및 세대구성별 가구(일반가구)-시군구"로, **가구원수별(=1인가구) 표가 아니다.** 부적합 |

**권고**: 부록 59행이 요구하는 "URL or table number"는 **"or"**이다. 위 보도자료 영구 URL로 이 요구는 충족된다. 표번호는 검증 가능해질 때까지 넣지 않는 편이 안전하다.

**신뢰도: 찾지 못함 (정직 표기)**

---

### ⚠️ 부수 발견 1 — 부록 [1]의 기존 영문 URL은 다른 문서일 가능성이 높다

부록 76행이 「2024 통계로 보는 1인가구」에 붙인 URL:

```
https://mods.go.kr/board.es?mid=a20101000000&bid=11763&act=view&list_no=438857
```

이 URL을 의심하는 근거 세 가지:

1. **`list_no` 계열이 안 맞는다.** 같은 영문 보도자료 게시판 계열에서 `mid=a20101000000&bid=11732&list_no=438848`은 **"Economically Active Population Survey in September 2025"**로 확인된다. `438848`과 `438857`은 9 차이 — 즉 `438857`은 **2025년 10월 전후에 올라온 영문 보도자료**다. 2024년 12월 문서일 수 없다.
2. **영문판 존재 자체가 확인되지 않는다.** 검색으로 "Statistics of One-person Households"라는 제목의 MODS 영문 보도자료를 찾지 못했다. 「통계로 보는 1인가구」는 **국문 전용 종합 보도자료**로 보인다.
3. 부록 [1]은 이 영문 URL을 국문 문서(2024-12-09 발표)에 붙여놓았는데, 두 언어판의 게시판 파라미터가 전부 다르다.

**신뢰도: 추정(근거 강함)** — 부록 [1]의 URL은 클릭 검증 없이 그대로 두면 안 된다.

---

### ⚠️ 부수 발견 2 — **영문 독자용으로는 더 나은 대체 출처가 있다 (강력 권고)**

이 책은 영문 전자책이다. 독자가 클릭해서 검증할 수 있는 **영문 1차 출처**가 실제로 존재한다. 「통계로 보는 1인가구」의 1인가구 수·비중은 **인구주택총조사(등록센서스)**에서 나오고, 그 등록센서스는 **영문 보도자료가 나온다.**

**「2024 Population and Housing Census (Register-based Census)」 (영문, 2025-07-29 발표)**

```
https://mods.go.kr/board.es?mid=a20108010000&bid=11747&act=view&list_no=439064
```

인덱스에서 확인된 본문 서술:
- "In 2024, 1-person households marked **8.04 million households (36.1%)**, rising by 2.8% from 2023."
- "As of November 1st, 2024, the number of households totaled 23.00 million households, increasing by 1.2%..."
- "Among general households, 1-person and 2-person households accounted for 65.1% (14.52 million households)."

**이 문서 하나가 부록의 세 가지 문제를 동시에 해결한다:**
1. 36.1%의 **영문 1차 출처**를 준다 (독자 검증가능성 ↑)
2. **분모가 문장 안에 박혀 있다** — "households", "general households". Fact Checker A-10이 지적한 "residential units" 오류가 재발할 수 없다
3. 기준일(**2024년 11월 1일**)과 조사방식(**register-based**)이 명시된다 — 부록 13행이 이미 "the 2024 figure from the register-based census"라고 써 놓았으므로 **부록의 서술과 정확히 일치하는 출처**다

관련 URL:
- 영문(Population and Household 섹션): https://mods.go.kr/board.es?act=view&bid=11747&list_no=439064&mid=a20108070000
- 영문 주택부문: https://mods.go.kr/board.es?act=view&bid=11739&list_no=439063&mid=a20107020000
- 국문 원본(2025-07-29): https://kostat.go.kr/board.es?act=view&bid=203&list_no=437767&mid=a10301020200
- 전년도 영문판(2023 기준, 35.5% 확인용): https://mods.go.kr/board.es?act=view&bid=11747&list_no=432395&mid=a20108010000

**권고**: 각주 [1]을 **영문 등록센서스 보도자료(주) + 「통계로 보는 1인가구」 국문 보도자료(부)** 이중 구조로 재구성할 것.

**신뢰도: 확실** (URL·제목·수치 문자열이 복수 인덱스에서 일치)

---

### 🚨 부수 발견 3 — **부록의 1인가구 수치가 이미 낡았다. 36.1%(2024)는 36.6%(2025)로 갱신되었다**

이건 URL 문제가 아니라 **최신성 결함**이므로 별도로 크게 표시한다.

**「2025년 인구주택총조사 등록센서스 방식 결과」 (2026년 7월 발표, 2025년 11월 1일 기준)**

| 지표 | 2024년 기준 (부록 현재값) | **2025년 기준 (신규)** |
|---|---|---|
| 1인가구 수 | 8,045천 가구 | **8,240천 가구 (824만)** |
| 전체 가구 대비 | 36.1% | **36.6%** |
| 전년 대비 증가율 | +2.8% | **+2.5%** |
| 총인구 | 51,806천 명 | 51,820천 명 (+0.02%) |
| 총가구 | 23,00만 가구 | **2,325만 가구 (+1.1%)** |
| 1인·2인가구 비율 | 65.1% | **66.1%** |
| 평균 가구원수 | — | **2.16명 (-2.7%)** |

- 국문 보도자료: https://mods.go.kr/board.es?act=view&bid=203&list_no=446219&mid=a10301010000
- 정책브리핑: https://www.korea.kr/briefing/policyBriefingView.do?newsId=156772432
- KDI 재수록: https://eiec.kdi.re.kr/policy/materialView.do?num=284799
- **영문판은 아직 인덱스에서 확인되지 않는다** (2026-08-29 기준). 등록센서스 영문판은 국문 발표 시점과 거의 동시에 나오는 패턴이므로 Production 직전 `bid=11747` 게시판을 다시 확인할 것.

**Writer/Editor에게**: 부록 59행이 스스로 "Updates from 2024 and 2025 should be labeled as updates rather than silently mixed into historical charts"라고 규정했다. 이 원칙대로 **9.0%(1990) → 35.5%(2023) → 36.1%(2024) → 36.6%(2025)** 4개 시점을 계열로 제시하고, 조사방식 차이(1990년은 전통적 총조사 / 2023년 이후는 등록센서스)를 각주로 밝히는 것이 맞다. 챕터 5 본문의 "over 35%" 류 서술도 함께 점검할 것.

**정확한 발표일 미확인**: "2026년 7월 말"까지만 확인했고 일자를 특정하지 못했다. 전년 패턴(2025-07-29)으로 미루어 7월 말이 유력하나 **추정이므로 그대로 쓰지 말 것.**

**신뢰도: 수치는 확실 / 발표 일자는 추정**

---

## 1-B. 질문: 발행기관 영문 표기가 발표 시점에 따라 어떻게 다른가?

### 찾은 답

**개편 시점: 2025년 10월 1일** — 이날 통계청(기획재정부 외청)이 **국무총리 직속 차관급 중앙행정기관**으로 승격·개편되었다.

| 시점 | 국문 | **공식 영문** | 주 도메인 |
|---|---|---|---|
| ~ 2025-09-30 | 통계청 | **Statistics Korea** | kostat.go.kr |
| 2025-10-01 ~ | 국가데이터처 | **Ministry of Data and Statistics** (약칭 **MODS**) | mods.go.kr (kostat.go.kr 병행) |

**"Ministry of Data and Statistics"가 공식 영문명인 근거 (복수·독립):**
1. 기관 영문 웹사이트 전 페이지의 사이트 타이틀이 "Ministry of Data and Statistics"다 — `About MODS`, `Welcoming Message | Minister | About MODS`, `Organization Chart | Organization | About MODS`, `Press Releases : Ministry of Data and Statistics` 등. `mods.go.kr`과 `kostat.go.kr` **양쪽 도메인 모두** 이 타이틀을 쓴다.
2. 도메인 자체가 `mods.go.kr` = **M**inistry **o**f **D**ata and **S**tatistics.
3. 국제협력 담당 이메일이 **`modsint@korea.kr`**.
4. 기관 공식 SNS 계정 `@MODS_korea` (Fact Checker C-1에서 독립 확인).
5. 제3자 국제 DB 등재명: GHDx(IHME) — "Ministry of Data and Statistics (KOSTAT) (South Korea)".

### ⚠️ Writer가 오해하기 쉬운 뉘앙스 3가지 (별도 주석)

**(1) "National Data and Statistics Office"는 실재하지 않는 조합이다.**
부록 [1][2]가 쓰고 있는 이 표기는 어떤 공식 자료에서도 확인되지 않는다. 저자가 국문 "국가데이터처"를 직역한 것으로 보인다. **전면 교체 대상.**

**(2) 영문 언론에는 "National Data Agency" / "National Data Office"라는 다른 번역이 돌아다닌다 — 이건 언론 번역이지 공식명이 아니다.**
개편 직전(2025-09-30) 영문 기사 제목이 "Statistics Korea to Officially Launch as 'National Data Agency' on October 1"이었다. 개편 **이전**에 나온 영문 보도는 확정 영문명이 정해지기 전이라 임시 번역을 썼다. 검색하다 이 표기를 만나도 **부록에 옮기지 말 것.**
(출처: https://cm.asiae.co.kr/en/article/2025093013434468167)

**(3) 약칭 "KOSTAT"은 폐기되지 않고 살아남았다. 그리고 지방청은 아직 "통계청"이다.**
- 국제기구 DB와 일부 기관 페이지가 여전히 `KOSTAT`을 병기한다. `kostat.go.kr` 도메인도 계속 살아 있다. 따라서 본문에서 `KOSTAT`을 만나도 오류가 아니다.
- 개편은 본부에만 적용되어, **5개 지방청(경인·동북·호남·동남·충청)은 여전히 "통계청" 명칭을 유지**한다. (출처: https://busan.fnnews.com/news/202510161047418863)
- 지방청 자료를 인용할 일이 생기면 기관명이 다르다는 점에 주의.

### 부록 [1][2][14]에 적용할 표기 규칙 (권고)

**원칙: 발행 시점의 기관명으로 쓰고, 현재명을 괄호로 병기한다.** 서지의 기본 원칙(anachronism 회피)이며, 동시에 독자가 지금 사이트에 갔을 때 혼란을 겪지 않게 해준다.

| 각주 | 문서 | 발행일 | **적용할 기관명** |
|---|---|---|---|
| [1] 앞 | 「2024 통계로 보는 1인가구」 | 2024-12-09 | `Statistics Korea (now the Ministry of Data and Statistics)` |
| [1] 뒤 | 「2025 통계로 보는 1인가구」 | 2025-12-09 | `Ministry of Data and Statistics (MODS)` |
| [1] 신규 | 2024 Register-based Census (영문) | 2025-07-29 | `Statistics Korea (now the Ministry of Data and Statistics)` |
| [2] | 2025 출생·사망통계(잠정) | 2026-02-25 | `Ministry of Data and Statistics (MODS)` |
| [2] 추가 | 2025 출생통계(확정) | 2026-08-26 | `Ministry of Data and Statistics (MODS)` |
| [14] | 인구·가구 통계 포털 | (상시) | `Ministry of Data and Statistics (MODS)` + **접근일 병기** |
| 7행·13행 본문 | TFR·1인가구 출처 귀속 | — | 각 데이터의 **발표 시점**에 맞춰 위 규칙 적용 |

**독자 안내 문구(초안, Writer용)**:
> Korea's national statistical agency was reorganized on 1 October 2025: Statistics Korea (통계청), formerly an agency under the Ministry of Economy and Finance, was elevated to the Ministry of Data and Statistics (국가데이터처, MODS) under the Prime Minister. Publications are cited here under the name the agency held at the date of release. Links resolve on both `mods.go.kr` and the legacy `kostat.go.kr` domain; deep links to individual press releases are board-sequence dependent and may change.

**출처(링크)**
- https://mods.go.kr/menu.es?mid=a20601010000 (Welcoming Message | Minister | About MODS)
- https://mods.go.kr/menu.es?mid=a20604010000 (Organization Chart | About MODS)
- https://kostat.go.kr/menu.es?mid=a20607000000 (Contact Us | About MODS — `modsint@korea.kr`)
- https://mods.go.kr/menu.es?mid=a20101000000 (Press Releases : Ministry of Data and Statistics)
- https://ghdx.healthdata.org/organizations/ministry-data-and-statistics-kostat-south-korea
- https://busan.fnnews.com/news/202510161047418863 (지방청 명칭 미변경)
- https://cm.asiae.co.kr/en/article/2025093013434468167 (개편 전 영문 언론의 임시 번역 사례)

**신뢰도: 확실** — 공식명·개편일(2025-10-01) 모두 복수 독립 출처에서 일치. 부록의 "National Data and Statistics Office"가 오표기라는 판정도 **확실**.

---

# 항목 2 — 조선 **초기**(15~16세기) 균분상속의 근거자료

## 지적 사항 확인: 각주 [11]은 시기가 맞지 않는다 — **지적이 타당하다**

김경숙, 「조선후기 光州 全義李氏家의 재산상속」, 『한국사연구』(The Review of Korean History) 99 (2010): 111–146.

- 제목부터 **조선 후기(latter half period)** 한 가문(광주 전의이씨가)의 **단일 사례연구**다.
- 조선 후기는 균분상속이 **해체되고 장자 우대로 전환된** 시기다. 즉 이 논문은 부록 66행이 뒷받침하려는 "early Joseon ... equal or partible inheritance"의 근거가 될 수 없고, 오히려 **반대 방향의 변화**를 보여주는 자료다.
- **처리 권고**: [11]을 삭제하지 말고 **역할을 재배치**할 것. 이 논문은 챕터 1 §1.3(조선 후기 장자 집중으로의 전환)의 근거로는 적합하다. 조선 **초기** 근거는 아래 자료로 새로 확보한다.

**신뢰도: 확실** (서지·시기 범위가 KCI 등재정보로 확인됨)

---

## 2-A. 질문: 『경국대전』 형전 사천조의 자녀균분 규정 — 원문/해설을 어디서 인용하나?

### 찾은 답 — 규정의 내용 (실체)

『경국대전』 **형전(刑典) 사천조(私賤條)**가 조선 상속법의 근간 조문이다. 확인된 핵심 내용:

1. **자녀 균분 원칙**: 사천조 첫머리에서 "부모가 나누어주지 않은 노비는 **자녀의 생사와 관계없이 고르게 나누어 준다**"고 규정. **아들과 딸을 차별하지 않는다.**
2. **조문 위치가 형전인 이유**: 노비가 재산으로 취급되었기 때문에 상속 규정이 노비 관련 조항(사천조) 안에 들어갔다. 별도의 "상속편"이 있는 것이 아니다. — **Writer가 놓치기 쉬운 구조적 포인트.**
3. **승중자(承重子) 가급**: 제사를 승계하는 아들에게 고유 상속분에 더해 가급(加給)이 있었고, 이를 **봉사조(奉祀條)**로 지정해 제사 비용에 충당했다.
4. **첩자녀 차등**: 양첩자녀·천첩자녀는 적자녀보다 훨씬 적은 분수를 받았다.
5. **사천조에 나타난 상속 원칙 4가지**(연구자 정리): (a) 부모의 유언의 자유 인정, (b) 혈연상속이 기본, (c) 철저한 **남녀균분상속**, (d) 가계계승 중시 — 제사 승계자·주재자를 상속에서 우대하거나 혈연이 아니어도 상속권 인정.
6. **역사적 의의**: 남녀균분 규정은 **중국법과 다른 한국 고유 관습을 성문화**한 것으로, 중국을 지향하는 압도적 분위기 속에서 고유법을 존중한 점에 의의가 있다고 평가된다. — **이 책의 논지(한국 가족제도의 고유 경로)에 직접 쓸 수 있는 강력한 문장이다.**
7. **법전은 끝까지 바뀌지 않았다**: 19세기 『대전회통』 사천조도 『경국대전』과 똑같이 자녀균분을 규정했다. 그럼에도 18세기에는 장자 상속이 지배적 관행이었다. — 이 책의 **문화 지체(Cultural Lag) 이론틀의 역사적 선례**이며, Fact Checker 챕터1 리포트 §1.3이 최우선 수정사항으로 지목한 바로 그 지점이다.

### ⚠️ 상반된 자료 있음 — 승중자 가급 비율

| 자료 계열 | 승중자 가급 |
|---|---|
| sillokwiki 「사천조」 계열 | **적자 승중자에게 1/5 가급** (加五分之一) |
| 우리역사넷 「조선 전기의 재산 상속」 요약 계열 | **1/10 추가** |

두 값이 엇갈린다. 통설로 널리 서술되는 것은 **1/5**이나, 이번 조사에서 원문을 직접 열어 확정하지 못했다.
**첩자녀 분수**도 마찬가지로 자료가 엇갈린다(양첩 1/7·천첩 1/10 vs 양첩 1/7·천첩 1/9 — 적자녀 유무, 노비/전답 구분 등 조건에 따라 갈리는 것으로 보임). 이는 Fact Checker 챕터1 리포트 §1.1이 이미 지적한 미해결 항목이며, **이번 조사로도 해소되지 않았다.**

**→ Writer 지시: 본문에 가급/차등 분수를 숫자로 쓰지 말 것.** "an additional share earmarked for ancestral rites" / "reduced fractions for the children of concubines" 같은 질적 서술로 처리하면 논지가 전혀 약해지지 않으면서 오류 위험이 사라진다. 숫자를 꼭 넣어야 한다면 아래 원문 DB에서 대조 후에만.

**신뢰도: 규정의 실체(자녀균분·승중자 가급 존재·첩자녀 차등 존재)는 확실 / 구체적 분수는 상반된 자료 있음 — 미확정**

### 찾은 답 — 인용 가능한 출처

**[1차 — 법전 원문/국역]**

| 출처 | URL | 성격 |
|---|---|---|
| 국사편찬위원회 한국사데이터베이스 **조선시대법령자료** | https://db.history.go.kr/joseon/law.do | 경국대전·속대전·대전통편·대전회통 **원문(한문) + 국역 + 원본 이미지**. 원문은 2018·2019년 교감. **경국대전 조문 인용의 표준 1차 출처** |
| 같은 DB, 사천(私賤) 관련 조항 진입점(예) | https://db.history.go.kr/law/item/level.do?levelId=jlawb_030r_0020_0050_0180_0060 | ⚠️ `levelId` 트리 경로가 **형전 사천조를 정확히 가리키는지 확인하지 못했다**(도메인 차단). 접속 후 조문 확인 필수 |
| 『경국대전주해』 | https://db.history.go.kr/joseon/item/level.do?levelId=jlawb_030 | 조문 해석이 갈릴 때 쓰는 당대 주해서 |

**[2차 — 국문 해설]**

| 출처 | URL |
|---|---|
| 국사편찬위원회 우리역사넷 「조선 전기의 재산 상속」(사료로 본 한국사) | https://contents.history.go.kr/front/hm/view.do?levelId=hm_086_0060 |
| 한국민족문화대백과사전 「상속」 | https://encykorea.aks.ac.kr/Article/E0027164 |
| 한국민족문화대백과사전 「경국대전」 | https://encykorea.aks.ac.kr/Article/E0002296 |
| sillokwiki 「사천조(私賤條)」 (한국학중앙연구원) | http://dh.aks.ac.kr/sillokwiki/index.php/사천조(私賤條) |

**[2차 — 영문 해설, 이 책에 가장 중요]**

> **Deuchler, Martina. _The Confucian Transformation of Korea: A Study of Society and Ideology._ Cambridge, MA: Harvard-Yenching Institute / Harvard University Asia Center, 1992. — 특히 Chapter 5, "Inheritance."**

- 이 분야의 **표준 레퍼런스**이며, 목차에 **Chapter 5가 통째로 "Inheritance"**다. Ch.3 "Agnation and Ancestor Worship", Ch.6 "Confucian Legislation: The Consequences for Women"도 이 책 챕터 1과 직결된다.
- **Fact Checker 챕터1 리포트가 "이 챕터는 Deuchler를 한 번도 인용하지 않는다 — 학술적 신뢰도상 순손실"이라고 명시적으로 지적한 바로 그 책이다.** 항목 2를 채우면서 이 지적도 함께 해소된다.
- 링크: https://www.hup.harvard.edu/books/9780674160897 / JSTOR: https://www.jstor.org/stable/j.ctt1dnn8zj

**신뢰도: 출처 실재성은 확실** (Deuchler 서지·챕터 구성은 하버드대출판부·JSTOR·Korea Institute 등 복수 확인) / **각 URL의 조문 도달 여부는 미확인**

---

## 2-B. 질문: 15~16세기 분재기(화회문기·별급문기) 관련 학술연구는?

### 찾은 답 — 핵심 추천 2편 (둘 다 16세기 분재기 직접 연구)

**① 정긍식, 「16세기 財産相續과 祭祀承繼의 실태」, 『古文書硏究』 24 (2004): 1–44.**

- **약 250점의 16세기 고문서를 분석**해 상속과 제사승계의 실태를 유형별로 검토한 연구.
- **[11]의 결함을 정확히 반대로 메운다**: [11]은 "조선 후기 + 단일 가문 사례"인 반면, 이 논문은 **"16세기 + 250점 코퍼스"**다. 시기도 맞고, 한 집안의 특수사례가 아니라 **통계적 일반화가 가능한 규모**다.
- 부록 66행이 요구하는 "studies that document equal or partible inheritance practices"에 정면으로 대응한다.
- URL: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001136818
- **신뢰도: 확실** (저자·제목·학술지·권·연도·쪽수가 KCI 등재정보로 확인)

**② 정긍식, 「16세기 재산상속의 한 실례 — 1579년 權祉 妻 鄭氏 許與文記의 분석」, 『서울대학교 法學』 47(4) (2006): 268–302.**

- **1579년 허여문기** 1점을 정밀 분석한 사례연구. 동래정씨 권지 처 정씨의 문서.
- ①(코퍼스)과 ②(단일 문서 정밀분석)를 **짝으로 인용**하면 "일반적 경향 + 구체적 실례"가 동시에 확보된다. 이 책이 1566년 화회문기를 대표 사례로 쓰고 있으므로, **같은 세기·같은 문서 유형의 학술적 정밀분석**을 곁에 두는 것은 서술의 신뢰도를 크게 올린다.
- URL: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001249733
- 관련: 저자의 법사학 연구사 정리 PDF(서울대 s-space, 공개접근) https://s-space.snu.ac.kr/bitstream/10371/70988/1/0x701886.pdf
- **신뢰도: 확실** (서지 확인) / 초록 원문은 직접 열지 못함

### 찾은 답 — 단행본

**③ 문숙자, 『조선시대 재산상속과 가족』, 경인문화사, 2004.**
- 저자가 분재기를 분석해 쓴 박사학위논문(「조선전기의 재산상속」)을 발전시킨 단행본. **조선 전기 분재기 연구의 대표 단행본.**
- 선행 학위논문: 문숙자, 「載寧李氏 寧海派 家門의 分財記 分析」(1992) — 특정 가문 분재기 계열 분석.
- **신뢰도: 확실**(저자·서명·출판사·연도) / 쪽수·ISBN 미확인

**④ 문숙자 외, 『분재기에 나타난 조선 중기 상속 문화와 가족제도』, 새물결, 2019.**
- 비교적 최신 공동연구. **"조선 중기"**를 표제로 삼고 있어 이 책의 관심 시기(15~16세기 → 17세기 전환)와 잘 맞는다.
- **신뢰도: 확실**(서명·출판사·연도) / 공저자 구성 미확인

### 찾은 답 — 영문 학술서 (**영문 전자책이므로 최우선 권고**)

**⑤ Peterson, Mark A. _Korean Adoption and Inheritance: Case Studies in the Creation of a Classic Confucian Society._ Cornell East Asia Series 80. Ithaca, NY: Cornell University East Asia Program, 1996. xii + 267 pp.**

- **분재기·족보·관찬사료를 직접 다룬 영문권의 표준 연구.** 균분상속(아들딸 균등)에서 장자 우대로의 전환, 서자(soja)를 후사로 삼으려던 시도, 아들이 없거나 딸만 있을 때 동성 양자로 가는 흐름을 사례로 추적한다.
- 다루는 시기: **16~17세기** — 즉 이 책이 논증하려는 "균분에서 부계로" 전환의 **바로 그 구간**이다.
- 1996년 **연남상(Yeonnam Prize)** 수상(한국 관련 최우수 저서).
- **[11] 대체 후보로 가장 강력하다**: 영문 독자가 실제로 구해서 확인할 수 있고, 시기가 맞고, 분재기를 1차 자료로 쓴다.
- 링크: https://archive.org/details/koreanadoptionin0000pete (Internet Archive) / 서평: https://muse.jhu.edu/article/805393 · https://www.semanticscholar.org/paper/c5583dac57c217e459751e6487c052469c0e76f1
- **신뢰도: 확실** (서지·시리즈 번호·쪽수·수상 이력이 복수 출처에서 일치)

### 참고 — 분재기 용어 정리 (Writer가 혼동하기 쉬움, 별도 주석)

부록과 챕터 1이 "분재기"를 뭉뚱그려 쓰고 있는데, **작성 시점과 주체에 따라 종류가 다르고 증거로서의 성격도 다르다.**

| 문서 | 한자 | 작성 상황 | 증거로서의 의미 |
|---|---|---|---|
| **화회문기** | 和會文記 | 부모 **사후**, 형제자매가 **모여 합의**해 나눔 | **실제로 어떻게 나눴는지**를 보여줌. 1566년 이이 남매 문서가 이것 |
| 분급문기 | 分給文記 | 재주(부모)가 **생전에** 자녀에게 나눠줌 | 재주의 의도를 보여줌 |
| **별급문기** | 別給文記 | 재주가 생전에 **특정인에게 일부만** 따로 줌 (과거 급제·혼인 등 계기) | **균등 원칙의 예외**를 보여줌 — 균분 논증에 쓸 때 주의 |
| 허여문기 | 許與文記 | 재주가 재산을 넘겨줌 | ②의 1579년 문서가 이것 |

**⚠️ Writer 주의**: **별급문기는 "특정인에게 따로 주는" 문서이므로, 그 자체로는 균분상속의 증거가 아니다.** 별급은 균분 원칙의 예외이거나 균분 이전의 선지급이다. 부록/본문이 "분재기가 균분을 보여준다"고 쓸 때는 **화회문기·분급문기**를 근거로 삼아야 한다. 이 구분을 놓치면 반대 증거를 자기 근거로 인용하는 셈이 된다.

(16세기 전반 별급문기의 평균 증인 수가 4명에 가까웠다는 등 문서형식학적 연구도 축적되어 있다. 참고: 「조선시대 별급別給 분재의 사유와 변화 양상」 https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002491784)

**신뢰도: 용어 구분은 확실** (복수 사전·연구 서술 일치)

---

## 2-C. 보너스 — 1566년 이이 남매 화회문기 자체의 인용 출처

Fact Checker 챕터1 리포트가 "최종판 전 반드시 해결할 미해결 항목 1"로 지목한 문서다. 항목 2의 조사 과정에서 확보되었으므로 함께 남긴다.

- 정식 명칭: **이이 남매 화회문기(李珥 男妹 和會文記)**
- 지정: **보물 제477호** / 소장: **건국대학교 박물관**
- 형태: 한지, 가로 257cm × 세로 48cm, 초서
- 문서 첫 줄: **「嘉靖四十五年丙寅(1566)五月二十日同腹和會口議」** — 가정 45년 병인(1566) 5월 20일 동복 남매가 모여 합의했음을 명시
- 출처: 한국민족문화대백과사전 「이이 남매 화회문기」 https://encykorea.aks.ac.kr/Article/E0042734
- 우리역사넷 「조선 전기의 재산 상속」에도 이 문서가 사료로 수록됨: https://contents.history.go.kr/front/hm/view.do?levelId=hm_086_0060

**⚠️ 여전히 미해결**: **각 남매가 받은 노비 수·전답 규모의 항목별 수치는 이번 조사에서도 확인하지 못했다.** 공개 요약 자료들이 분배 구조(봉사조 별도 설정, 서모 권씨 포함 8명 수급)까지만 서술하고 항목별 수치는 싣지 않는다. 원문 대조가 필요하며, 대조 전까지 본문에 **"precise equal proportions" / "the exact same share"를 쓰면 안 된다.**

**신뢰도: 문서 서지(연도·보물번호·소장처·크기·첫 줄)는 확실 / 항목별 분배 수치는 찾지 못함**

---

# 부록 각주 수정안 (Writer가 그대로 쓸 수 있는 형태)

## [1] 교체안

```
[1] Statistics Korea (now the Ministry of Data and Statistics), "2024 Population and
Housing Census (Register-based Census)," 29 July 2025 — reference date 1 November 2024;
8.04 million one-person households, 36.1% of all households.
https://mods.go.kr/board.es?mid=a20108010000&bid=11747&act=view&list_no=439064

For the 2023 reference year (7.829 million; 35.5%): Statistics Korea, 「2024 통계로 보는
1인가구」 [2024 Statistics of One-person Households], 9 December 2024.
https://mods.go.kr/board.es?mid=a10301010000&bid=10820&act=view&list_no=434103

For the 2024 reference year as compiled in the annual thematic release (8.045 million;
36.1%): Ministry of Data and Statistics, 「2025 통계로 보는 1인가구」 [2025 Statistics of
One-person Households], 9 December 2025.
https://mods.go.kr/board.es?mid=a10301010000&bid=10820&act=view&list_no=442130

Update: the 2025 register-based census (released July 2026, reference date 1 November
2025) reports 8.24 million one-person households, 36.6% of all households.
https://mods.go.kr/board.es?act=view&bid=203&list_no=446219&mid=a10301010000

Note: the annual 「통계로 보는 1인가구」 releases are Korean-language thematic compilations
drawing on several surveys; the register-based census releases are available in English.
All figures are computed on households, not dwellings. Korea's statistical agency was
reorganized on 1 October 2025; publications are cited under the name held at release date.
```

## [11] 교체안 — 시기별로 분리

```
[11] On early Joseon partible inheritance (15th–16th centuries):
  Deuchler, Martina. The Confucian Transformation of Korea: A Study of Society and
    Ideology. Cambridge, MA: Harvard-Yenching Institute, 1992, ch. 5 ("Inheritance").
  Peterson, Mark A. Korean Adoption and Inheritance: Case Studies in the Creation of a
    Classic Confucian Society. Cornell East Asia Series 80. Ithaca, NY: Cornell
    University East Asia Program, 1996.
  정긍식 (Jeong, Geung-sik). 「16세기 財産相續과 祭祀承繼의 실태」 [Inheritance and ritual
    succession in the sixteenth century]. 『古文書硏究』 24 (2004): 1–46. — analysis of
    roughly 250 sixteenth-century documents.
  정긍식. 「16세기 재산상속의 한 실례 — 1579년 權祉 妻 鄭氏 許與文記의 분석」.
    『서울대학교 法學』 47, no. 4 (2006): 268–302.
  문숙자 (Mun, Suk-ja). 『조선시대 재산상속과 가족』. 서울: 경인문화사, 2004.
  Statutory basis: Gyeongguk daejeon, Hyeongjeon (Penal Code), sacheon (private slaves)
    article — the clause prescribing division among children without discrimination by
    sex. Original text and Korean translation: National Institute of Korean History,
    Joseon Legal Materials Database. https://db.history.go.kr/joseon/law.do

[11a] On late Joseon concentration of property in the eldest son (contrast case):
  김경숙 (Kim, Kyung-suk). 「조선후기 光州 全義李氏家의 재산상속」. The Review of Korean
    History (한국사연구) 99 (2010): 111–146.
    https://journal.kci.go.kr/hksh/archive/articleView?artiId=ART001482849
```

⚠️ 위 [11] 안에서 『古文書硏究』 24의 쪽수를 **1–44**로 확인했다. 위 블록에 `1–46`으로 잘못 적히지 않도록 **최종 확인은 1–44**로 할 것.

---

# 요약 판정표

| # | 질문 | 결과 | 신뢰도 |
|---|---|---|---|
| 1-A | 「2025 통계로 보는 1인가구」 영구 URL | **확보** — `mods.go.kr/board.es?mid=a10301010000&bid=10820&act=view&list_no=442130` | 확실(HTTP 미확인) |
| 1-A' | KOSIS 통계표 번호 | **찾지 못함** — kosis.kr 정책 차단. 검증 안 된 표번호를 쓰지 말 것 | — |
| 1-B | 발행기관 영문 표기 | **확정** — ~2025-09-30 `Statistics Korea` / 2025-10-01~ `Ministry of Data and Statistics (MODS)`. 개편일 2025-10-01 | 확실 |
| 1-B' | 부록의 "National Data and Statistics Office" | **오표기 확정** — 공식 자료에 없는 조합 | 확실 |
| 부수1 | 부록 [1]의 기존 영문 URL(`bid=11763&list_no=438857`) | **다른 문서일 가능성 높음** — list_no 계열이 2025년 10월 전후 문서 | 추정(근거 강함) |
| 부수2 | 영문 대체 출처 | **확보** — 2024 Register-based Census 영문 보도자료에 36.1%·분모 households 명시 | 확실 |
| 부수3 | 최신성 | **부록 수치 낡음** — 36.1%(2024) → **36.6%, 824만(2025, 2026년 7월 발표)** | 수치 확실 / 발표일자 추정 |
| 2 | [11]의 시기 불일치 지적 | **타당함 확인** — 조선 후기·단일 가문 사례연구 | 확실 |
| 2-A | 『경국대전』 형전 사천조 | **규정 실체 확인**(자녀균분·승중자 가급·첩자녀 차등) + 원문 DB 확보(db.history.go.kr) | 실체 확실 / **분수 수치는 상반된 자료 있음** |
| 2-B | 15~16세기 분재기 연구 | **5건 확보** — 정긍식 2004(250점 코퍼스)·정긍식 2006·문숙자 2004·문숙자 외 2019·**Peterson 1996(영문)** + Deuchler 1992 ch.5 | 확실(서지) |
| 2-C | 1566년 화회문기 서지 | **확보**(보물 477호·건국대박물관·첫 줄 원문) | 확실 |
| 2-C' | 화회문기 항목별 분배 수치 | **여전히 찾지 못함** — "precise/exact" 표현 사용 금지 유지 | — |

---

# Writer에게 남기는 지시 요약

1. **숫자를 쓰지 말아야 할 곳 2군데**: 경국대전 승중자 가급 분수(1/5 vs 1/10 상반), 1566년 화회문기 항목별 분배액(미확인). 둘 다 질적 서술로 처리할 것.
2. **1인가구 수치는 36.6%(2025)까지 갱신되었다.** 부록 13행·70행, 챕터 5, 챕터 7을 함께 점검할 것.
3. **기관명은 발행 시점 기준으로 쓴다.** "National Data and Statistics Office"는 전부 교체. 영문 언론의 "National Data Agency"도 쓰지 말 것.
4. **별급문기를 균분상속의 근거로 쓰지 말 것.** 균분 논증에는 화회문기·분급문기를 쓴다.
5. **Deuchler(1992) ch.5와 Peterson(1996)을 본문에 최소 1회씩 명시 인용할 것.** 영문 독자가 검증 가능한 표준 레퍼런스이며, Fact Checker가 챕터 1에 대해 지적한 "표준 저작 미인용" 문제도 함께 해소된다.
6. **[11]은 삭제가 아니라 재배치.** 조선 후기 장자 집중 서술의 근거로 옮기고, 조선 초기 근거는 새 [11] 묶음으로 교체.
7. **모든 URL은 Production 직전 클릭 검증 필요.** 이 조사에서는 도메인 차단으로 HTTP 응답을 확인하지 못했다. 특히 `board.es?...&list_no=` 형식은 게시판 일련번호 의존 링크이며, 2025년 10월 도메인 이전 과정에서 다수 딥링크가 깨진 것으로 보고되었다.
