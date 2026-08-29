# Fact Check Report — 08 Statistical Appendix and References

- **검증 대상**: `books/korea-family-transformation/02-chapters/08-appendix-statistical-references.md`
- **검증일**: 2026-08-28 (2차 검증 — 1차 리포트를 전면 갱신함)
- **검증자**: Fact Checker (독립 검증)
- **원 리서치 자료**: **없음.** `books/korea-family-transformation/01-research/` 디렉터리가 존재하지 않는다. 이 원고는 사용자가 직접 가져온 반쯤 완성된 원고이므로 대조할 내부 리서치 자료가 없고, **모든 주장을 원 출처에서 직접 교차검증**했다.
- **검증 범위 제외**: "Figure register for final layout" 표(Figure 1~14) — 지시에 따라 제외(Visual Director 소관).

## 검증 환경상의 한계 (먼저 밝힘)

이 세션의 조직 이그레스 정책이 다음 도메인에 대한 직접 접속을 차단한다(TLS 문제가 아니라 정책 거부이므로 우회하지 않았다):
`www.oecd.org`, `mods.go.kr` / `kostat.go.kr`, `journals.sagepub.com`, `journals.openedition.org`, `elaw.klri.re.kr`, `journal.kci.go.kr`, `www.humanrights.go.kr`, `www.nl.go.kr`.

따라서 **URL의 최종 HTTP 응답코드(200/404)를 직접 확인하지 못했다.** 대신 검색엔진 인덱스에서 해당 URL 문자열·문서 제목·저자·기관이 그대로 확인되는지로 간접 검증했다. 아래에서 "인덱스 확인"이라고 쓴 것은 이 간접 확인이며, **문서 실재의 강한 증거이지만 링크 생존(link-rot)의 증거는 아니다.** Production 직전 링크 전수 클릭 검사는 여전히 필수다.

---

# 요약 (Executive Summary)

| 구분 | CONFIRMED | NEEDS REVIEW | UNSUPPORTED |
|---|---|---|---|
| 통계 수치·정의 | 12 | 5 | 0 |
| 법령/판례 | 6 | 2 | **1** |
| 참고문헌 URL/서지 | 11 | 6 | 0 |
| 원고 구조/각주 체계 | 0 | 1 | **3** |

## 사용자가 지정한 3대 확인 항목 — 결론

| # | 항목 | 판정 |
|---|---|---|
| 1 | 노인장기요양보험법 "Law No. 8402" | **확정 오류. 제8403호가 맞다.** 8402호는 전혀 다른 법(항공우주산업개발 촉진법 일부개정)으로 특정됨 |
| 2 | 1인가구 "over 35% of all national residential units" | **확정 오류(분모 용어).** households가 맞다. + 2024년 확정치 36.1%로 갱신 필요 |
| 3 | "about 0.8 in 2025 (provisional)" | **최신성 결함.** 2026-08-26 확정치 발표됨. 254,341명(+6.7%), TFR 0.80 확정 |

## 1차 리포트 대비 **판정이 뒤바뀐 항목 1건** (중요)

**"Tertiary Educational Attainment: Exceeds 75% for females aged 25–34 (OECD Education at a Glance)"** — 1차 검증은 이 괄호 출처 귀속이 **틀렸다**고 판정했으나(EAG는 성별 미분리 71%만 보고한다는 이유), **재검증 결과 이 판정이 잘못이었다.** EAG 2025(및 그 기반인 OECD Education GPS 한국 프로파일)는 25~34세 고등교육 이수율을 **여성 78.2% / 남성 63.7% / 전체 70.6%(2024년 기준)**로 성별 분리해 보고한다. 따라서 원고의 수치와 출처 귀속은 **둘 다 맞다.** 누락된 것은 기준연도뿐이다. 아래 A-7 참조.

## 권고

**Editor로 넘기지 말고 Writer/Researcher 단계로 1회 되돌릴 것.** 사유는 핵심 수치의 오류율이 높아서가 아니다 — 오히려 TFR·임금격차·고등교육이수율·1인가구 수치는 거의 전부 CONFIRMED다. 되돌려야 하는 이유는 (1) 확정 법률번호 오류 1건, (2) 통계 분모 용어 오류 1건, (3) 최신치 미반영 2건, (4) 서지정보가 실제 출처와 다른 참고문헌 3건([9][11][16]), (5) 각주가 본문 챕터에 전혀 연결되어 있지 않은 구조적 결함이다. (5)는 Editor의 문장 다듬기로 해결되는 종류가 아니다.

---

# A. 통계 수치·정의 검증

## A-1. 주장: "Total Fertility Rate (TFR): Recorded at 0.72 in 2023 (Statistics Korea, Annual Vital Statistics)"

**상태: CONFIRMED (수치) / NEEDS REVIEW (출처 귀속)**

**근거**: 2023년 합계출산율 0.72는 통계청(현 국가데이터처) 출생통계 확정치로 확인된다. 2024년 0.75, 2025년 0.80으로 이어지는 계열과도 정합적이다.

**출처 귀속 문제**: 부록 4행은 출처를 "Statistics Korea, Annual Vital Statistics"로 적었으나, 67행에서 같은 0.72에 붙인 각주는 **[5] = OECD, *Inclusive and Sustainable Well-being in Korea* (2026)**다. 두 출처 모두 실재하고 수치도 같지만 1차 출처(통계청 인구동향조사/출생통계)와 2차 인용(OECD 보고서)이 뒤섞여 있다. 부록 자신의 편집 방침("모든 정량적 주장은 출처의 기준 연도와 정의를 함께 읽어야 한다")과 어긋난다.

**제안 수정**: TFR은 1차 출처로 각주를 달고, OECD 보고서는 국제 비교 맥락에서만 별도 인용.

---

## A-2. 주장: "with a modest rebound to 0.75 in 2024"

**상태: CONFIRMED**

**근거**: 「2025년 출생·사망통계(잠정)」(2026-02-25)이 "2025년 0.80명, 2024년 0.75명 대비 +0.05명"으로 2024년 값 0.75를 명시한다. 2024년 확정치는 0.748.

---

## A-3. 주장: "and about 0.8 in 2025 (provisional)" — **[사용자 지정 확인항목 3]**

**상태: NEEDS REVIEW — 수치는 맞으나 "provisional" 라벨이 이미 낡았다 (최신성 결함)**

**근거**: 두 단계로 나뉘며, **사용자가 제기한 우려가 사실로 확인되었다.**

| 구분 | 발표일 | 출생아 수 | 전년 대비 | TFR |
|---|---|---|---|---|
| 잠정치 (부록 [2]가 인용) | 2026-02-25 | 254,500명 | +16,100명 (+6.8%) | 0.80 |
| **확정치 (신규)** | **2026-08-26** | **254,341명 (≈254,300)** | **+16,024명 (+6.7%)** | **0.80** |

- 확정치는 국가데이터처 「2025년 출생통계」로 **이 리포트 작성 이틀 전에 발표**되었다. 복수 매체(서울신문·정책브리핑·Korea Times·나은뉴스 계열)가 동일하게 254,300명 / 6.7% / TFR 0.80 / 2021년(0.81) 이후 4년 만의 0.8명대 회복을 보도한다.
- 즉 **TFR 0.80 자체는 잠정치와 확정치가 동일**하므로, 부록 4행의 "about 0.8"이라는 수치는 틀리지 않았다. 틀린 것은 **"(provisional)"이라는 상태 라벨**이다.
- 반면 부록 67행의 **"254.5 thousand live births ... and a 6.8% increase"는 확정치로 대체되었다.**

**제안 수정**:
- 4행: `"about 0.8 in 2025 (provisional)"` → `"0.80 in 2025 (final, released 26 August 2026)"`. "about"으로 뭉갤 이유가 없다 — 원자료가 소수 둘째 자리까지 확정 발표했고, 부록 자신이 59행에서 "exact series"를 요구한다.
- 67행: 확정치 254.3천 명 / +6.7%로 갱신. 잠정치를 남기려면 `"provisionally reported as 254.5 thousand (+6.8%), finalised at 254.3 thousand (+6.7%) in August 2026"`처럼 병기하고, 각주 [2]에 2026-08-26 확정 보도자료를 **추가** 인용할 것(잠정 보도자료를 삭제하지 말 것 — 부록 59행 자신의 "updates를 updates로 라벨링하라" 원칙에 따라 두 판본을 다 남기는 게 맞다).

---

## A-4. 주장: "Gender Wage Gap: Approximately 29% in 2023-2024"

**상태: CONFIRMED (2023년) / NEEDS REVIEW (2024년)**

**근거**: OECD 기준 한국 성별임금격차 **2023년 29.3%** (OECD 평균 11.3%의 약 2.6배)가 복수 독립 출처로 확인된다. **이는 다른 챕터 검증에서 CONFIRMED된 "OECD 2023년 29.3%"와 정확히 일치하며, 부록과 챕터 4·7의 서술이 서로 정합적이다.**

다만 **2024년 값은 이번 검증에서 OECD 원자료로 확인하지 못했다.** "2023-2024"라는 범위 표기는 2024년 값이 확정되지 않은 상태에서 두 해를 묶은 것일 수 있다.

**제안 수정**: 확인된 단일 연도로 좁혀 `"29.3% in 2023"`으로 쓰거나, 2024년 값을 OECD Employment Database에서 확인해 병기할 것.

---

## A-5. 주장: "down from about 34% in 2018"

**상태: CONFIRMED**

**근거**: **2018년 34.1% → 2023년 29.3%**로 축소된 것이 확인된다. 다른 챕터 검증에서 CONFIRMED된 값(2018년 34.1%)과 일치한다. "about 34%"는 정확하고 보수적인 서술이다.

---

## A-6. 주장: "and still the highest (OECD Employment Database)" / 정의 문구

**상태: CONFIRMED (순위) / NEEDS REVIEW (비교 모집단 누락 + 정의 오기)**

**근거**:
1. **순위**: 한국은 1996년 OECD 가입 이래 현재까지 회원국 중 성별임금격차 1위다. 비교 참고치 — 캐나다 16.5%, 호주 10.7%, 스웨덴 7.5%.
2. **비교 모집단이 문장에 없다.** "still the highest"만 쓰면 "세계 최고"로 읽힌다. `"still the highest in the OECD"`로 명시할 것. (챕터 5 검증에서 "World's Lowest TFR"이 같은 유형의 무한정 최상급 문제로 지적되었다 — 이 책 전체에 반복되는 패턴이다.)
3. **정의 오기**: 부록 69행은 OECD 정의를 `"generally using unadjusted gross earnings of full-time wage and salary workers"`로 옮겼는데, **OECD 지표 페이지의 실제 범위는 "full-time employees **and to self-employed**"** 즉 **자영업자를 포함**한다. 부록이 "OECD 정의를 따른다"고 선언한 바로 그 문단에서 OECD 정의를 좁혀 옮긴 것이므로 넘기기 어렵다.
4. 6행은 `"male and female median full-time earnings"`라 했으나 OECD 정의문은 "median earnings"이지 "full-time earnings"가 아니다(full-time은 범위 한정이지 소득 정의가 아니다).
5. 출처 표기가 6행("OECD Employment Database")과 각주 [3](OECD gender wage gap **indicator 페이지**)에서 불일치한다.

**제안 수정**: `"...relative to men's median earnings, based on unadjusted gross earnings of full-time employees and the self-employed (OECD gender wage gap indicator)"`로 통일.

---

## A-7. 주장: "Tertiary Educational Attainment: Exceeds 75% for females aged 25–34 (OECD Education at a Glance)" — **[1차 리포트 판정 번복]**

**상태: CONFIRMED (수치·출처 귀속 모두 정확) / NEEDS REVIEW (기준연도 누락)**

**근거**: OECD Education GPS 한국 프로파일(EAG 2025 기반, **2024년 기준연도**):

| 25–34세 고등교육 이수율 | 값 | OECD·파트너 40개국 중 순위 |
|---|---|---|
| 여성 | **78.2%** | 1위 |
| 남성 | **63.7%** | 1위 |
| 전체 | **70.6%** (국가노트 본문은 "71%"로 반올림) | 1위 (OECD 평균 48%) |

- 따라서 `"Exceeds 75% for females aged 25–34"`는 **사실이며(78.2%)**, 괄호 출처 `"(OECD Education at a Glance)"`도 **정확하다.**
- **다른 챕터 검증에서 CONFIRMED된 "EAG 2025 Korea: 25–34세 전체 70.6%, 남성 63.7%"와 완전히 정합적이다.** 산술 검산: (78.2 + 63.7)/2 ≈ 71.0 ≈ 70.6(코호트 남녀 인구비 반영 시 일치).
- **1차 리포트가 "이 성별 분리 수치는 EAG가 아니라 [5] OECD 웰빙 보고서에 있다"고 판정한 것은 잘못이었다.** 여기서 정정한다.
- 남은 결함은 **기준연도 누락 하나**다. 이는 부록 자신이 69행에서 요구한 "must therefore be accompanied by the relevant gender-specific table and **reference year**"를 8행이 스스로 위반한 것이다.

**제안 수정**: `"Tertiary educational attainment: 78.2% for women aged 25–34 versus 63.7% for men (2024; OECD Education at a Glance 2025 / Education GPS, Korea), against an overall rate of 70.6%."`

---

## A-8. 주장: "surpassing male cohorts in the same age demographic"

**상태: CONFIRMED**

**근거**: 2024년 기준 여성 78.2% vs 남성 63.7%로 **14.5%p 격차**. 2005년 남녀 51% 동률 이후 2006년부터 여성이 추월해 격차가 계속 벌어졌다.

---

## A-9. 주장(부록의 자기 경고, 69행): "The OECD's 2025 Korea country note reports tertiary attainment for 71% of 25–34-year-olds overall; any female-only estimate above 75% must therefore be accompanied by the relevant gender-specific table and reference year."

**상태: CONFIRMED — 71%도 정확하고, 경고의 방법론적 취지도 타당하다. 다만 이제 해소 가능하다.**

**근거**: 사용자가 지정한 정합성 확인 항목이므로 명확히 답한다.
1. 71%는 실재한다 — EAG 2025 한국 국가노트: "Korea has the highest rate of tertiary attainment among young adults across OECD countries: 71% of 25-34-year-olds, compared to the OECD average of 48%." 정밀값은 **70.6%**.
2. 여성 78.2% / 남성 63.7%도 실재한다(같은 EAG 2025 데이터, 2024년 기준).
3. **따라서 71%와 75%+는 모순되는 수치가 아니다.** 71%는 남녀 통합값, 78.2%는 여성 단독값이다. 세 숫자는 완전히 정합적이다.
4. 즉 부록의 경고는 "둘 중 하나가 틀렸다"는 경고가 아니라 **"성별 미분리 값과 성별 분리 값을 구분 표기하라"**는 방법론적 경고이며, 이는 정확하다.

**제안 수정**: 경고 자체의 취지는 유지하되, **이제 답이 확정되었으므로 미해결 상태로 남겨두지 말 것.** 현재 문장("any female-only estimate above 75% must therefore be...")은 독자에게 "저자도 아직 확인 못 했다"로 읽힌다. 실제 성별 분리 수치(여 78.2% / 남 63.7%, 2024)를 본문에 넣고 경고를 **해소된 형태의 방법론 주석**으로 바꿀 것.

---

## A-10. 주장: "Single-Person Households: Represents over 35% of all national residential units" — **[사용자 지정 확인항목 2]**

**상태: UNSUPPORTED (분모 용어) — 확정 오류**

**근거**: **사용자가 제기한 우려가 사실로 확인되었다.** 1인가구 비중의 분모는 **주택(residential units / housing units)이 아니라 가구(households)**다. 국가데이터처 원자료는 전부 "전체 **가구**의 35.5%" 형식으로 서술한다. "residential units"를 분모로 쓰면 전혀 다른 통계(주택 재고 대비 비율)가 되며, 그런 통계는 인용된 자료에 존재하지 않는다.

이는 부록 자신이 59행에서 요구한 **"including year, unit, denominator"** 원칙을 부록 10행이 정면으로 어긴 사례다. 통계 정의 오류이므로 문장 다듬기가 아니라 사실관계 수정이다.

**제안 수정**: `"over 35% of all national residential units"` → `"35.5% of all **households** (2023)"`.

---

## A-11. 주장(수치·기준연도): 1인가구 35.5% — **[사용자 지정 확인항목 2, 후반부]**

**상태: CONFIRMED (2023년 값) / NEEDS REVIEW (최신치 미반영)**

**근거**: **사용자가 제기한 우려가 사실로 확인되었다.**

| 기준연도 | 1인가구 수 | 전체 가구 대비 | 출처 / 발표일 |
|---|---|---|---|
| 2023 | 7,829천 가구 | **35.5%** | 「2024 통계로 보는 1인가구」, **2024-12-09** (부록 [1]) |
| **2024** | **8,045천 가구** | **36.1%** | 「2025 통계로 보는 1인가구」, **2025-12-09** (부록에 없음) |

- 부록 [1]의 서지(제목·발표일 2024-12-09·수치 7.829백만/35.5%)는 **모두 정확하다.**
- 그러나 **2024년 확정치 36.1%(804만 5천 가구)가 이미 나와 있다.** 참고 2020년 31.7% → 2024년 36.1%(+4.4%p). 2024년 연령 구성: 70세 이상 19.8% > 29세 이하 17.8% > 60대 17.6% > 30대 17.4% (70세 이상이 29세 이하를 처음 추월).
- 부록 59행이 "Updates from 2024 and 2025 should be labeled as updates rather than silently mixed into historical charts"라고 스스로 규정해 놓고, **정작 1인가구 항목에 그 규정을 적용하지 않았다.**

**제안 수정**: 10행 → `"35.5% of all households in 2023, rising to 36.1% (8.045 million) in 2024"`, 각주 [1]에 「2025 통계로 보는 1인가구」(2025-12-09) 추가. 이 책은 "2025년 수준 통계"를 판매 포인트로 내세우므로(00-brief.md) 갱신은 선택이 아니다.

---

## A-12. 주장: "up from 9.0% in 1990"

**상태: CONFIRMED (근거 강도: 중)**

**근거**: 1990년 인구주택총조사 기준 전국 1인가구 1,021천 가구, 전체 가구의 9.0%. 이후 2000년 15.5%, 2010년 23.9%, 2015년 27.2%로 이어지는 표준 시계열과 정합적이다.

**제안 수정**: 검색 결과 일부가 **서울시 기준 9.1%**를 다루므로 혼동 여지가 있다. 최종판에서 인구주택총조사 원표(가구원수별 가구) 표번호를 명시해 전국 기준임을 못박을 것 — 부록 자신이 "URL or table number"를 요구한다.

---

## A-13. 주장: "Single-Person Households ... (Statistics Korea, Population and Housing Census)"

**상태: NEEDS REVIEW (조사 방식 혼합)**

**근거**: 35.5%가 실린 문서는 「통계로 보는 1인가구」라는 **가공·종합 보도자료**(각주 [1])이고, 기저 자료는 **등록센서스**다. 반면 1990년 9.0%는 **전통적 인구주택총조사**에서 나온다. 두 수치를 하나의 시계열로 제시하려면 조사 방식 차이를 각주로 밝혀야 한다.

**제안 수정**: `"1990 figure from the traditional Population and Housing Census; 2023–2024 figures from the register-based census as compiled in the annual one-person-household releases"`.

---

## A-14. 주장(방법론 지침): "The statistical appendix should reproduce the exact series used in the figures, including year, unit, denominator, and URL or table number." / "Updates from 2024 and 2025 should be labeled as updates..."

**상태: CONFIRMED (지침 자체는 타당) — 단, 부록이 자기 지침을 3회 위반했다**

**근거**: 사실 주장이 아니라 편집 지침이므로 진위 판정 대상은 아니나, 통계 실무상 정당한 요구다. 다만 위반 사례를 명기한다:
1. **denominator 위반** — 10행 "residential units" (A-10)
2. **year 위반** — 8행 고등교육이수율 기준연도 누락 (A-7)
3. **update 라벨링 위반** — 10행 1인가구가 2024년 확정치 미반영 (A-11), 67행 2025년 출생통계가 확정치 미반영 (A-3)

지침은 유지하되, 지침을 실제로 이행할 것.

---

# B. 법령 / 판례 검증 — **[사용자 지정 재검증 항목]**

## B-1. 주장: "Civil Code of the Republic of Korea (Law No. 471): Promulgated Feb 22, 1958; Enforced Jan 1, 1960."

**상태: CONFIRMED**

**근거**: 대한민국 민법은 1957년 12월 17일 국회 통과, **1958년 2월 22일 법률 제471호로 공포**, **1960년 1월 1일 시행**. 법률번호·공포일·시행일 3개 항목 모두 일치한다. (총 1,139개조 — 본문 1,111개조 + 부칙 28개조.)

---

## B-2. 주장: "(Original codification of the Hoju system)"

**상태: NEEDS REVIEW**

**근거**: 1958년 민법이 호주제를 **최초로 성문화(original codification)**했다는 서술은 오해를 부른다. 호주(戶主)를 중심으로 한 근대적 가(家)·호적 제도는 일제강점기 조선호적령·의용민법 체제에서 이미 법제화되어 있었고, 1958년 민법은 이를 대한민국 법전으로 **승계·재편**한 것에 가깝다. **이 책의 챕터 2(Colonial Disruption)가 바로 그 식민지 법제화를 다루므로, 부록의 이 표현은 책 자신의 논지와 충돌한다.**

**제안 수정**: `"First codification of the hoju system in the Civil Code of the Republic of Korea, carrying forward the household-head framework given modern legal form under colonial rule"` 정도로 한정. 문장 다듬기가 아니라 사실관계 수정이므로 Writer 단계 처리.

---

## B-3. 주장: "Constitutional Court Decision 2001Hun-Ga9 et al. (February 3, 2005): Landmark decision holding Civil Code Articles 778 and 781 (1) non-conforming to the Constitution (Heonbeop-bul-hapchi)."

**상태: CONFIRMED (날짜·사건번호·결정형식) / NEEDS REVIEW (심판대상 조문 누락 및 부정확)**

**근거**: 헌법재판소 전원재판부(주심 김영일)는 **2005년 2월 3일** 재판관 **6:3** 의견으로 호주제 근거 조항이 헌법 제36조 제1항(혼인·가족생활에서 개인의 존엄과 양성평등)에 위반된다며 **헌법불합치** 결정을 내렸다. 사건번호는 **2001헌가9·10·11·12·13·14·15, 2004헌가5(병합)**. 날짜·사건번호 계열·결정형식 모두 정확하다.

**심판대상 조문의 정확한 범위**:
- 민법 **제778조** (호주의 정의)
- 민법 **제781조 제1항 본문 후단**
- 민법 **제826조 제3항 본문** (처의 부가입적)

**제안 수정**:
1. 부록은 **제826조 제3항을 누락**했다 — 호주제의 혼인 관련 축을 통째로 빠뜨린 것이므로 추가할 것.
2. 부록은 `"781 (1)"`로 적었으나 정확히는 **제781조 제1항 본문 "후단"**이다. 제1항 전체가 아니라 후단부만 심판대상이었으므로 `"Article 781(1), latter part of the main text"`로 한정할 것. (국가법령정보센터 헌재결정례 제목 자체가 "민법 제781조 제1항 본문 후단부분 위헌제청 등"이다.)
3. "et al."을 쓸 거라면 최종판에 병합 사건번호 전체 범위를 명시하고, 6:3 의견 분포를 추가하면 "landmark"라는 서술이 뒷받침된다.

---

## B-4. 주장: "Act on Registration of Family Relations (Law No. 8435): Promulgated May 17, 2007; Enforced Jan 1, 2008."

**상태: CONFIRMED**

**근거**: 「가족관계의 등록 등에 관한 법률」은 **법률 제8435호**로 **2007년 5월 17일 공포**, **2008년 1월 1일 시행**. 대한변협 공고("[2007-05-17 공포] 가족관계의등록등에관한법률(법률8435호)")를 포함한 복수 출처가 일치한다. 법률번호·공포일·시행일 3개 항목 모두 정확하다.

부수 확인: 2005년 헌재 결정에 따라 호적제를 대체하고 **개인 단위** 등록부로 전환했다는 부록 17행의 괄호 설명("Establishment of the individual-based registry")도 정확하다. (같은 8435호 부칙으로 「재외국민의 가족관계등록창설...특례법」 등 타법이 함께 정비되어 검색 시 동일 번호의 다른 법이 잡히나, 이는 모순이 아니다.)

---

## B-5. 주장: "Act on Long-Term Care Insurance for the Aged (Law No. 8402): Enacted April 27, 2007; Enforced July 1, 2008." — **[사용자 지정 확인항목 1]**

**상태: UNSUPPORTED — 법률번호 확정 오류**

**근거**: **사용자가 제기한 우려가 사실로 확인되었으며, 이번 검증에서 근거가 더 강해졌다.**

1. 「노인장기요양보험법」의 법률번호는 **제8403호**다. 위키문헌 「노인장기요양보험법 (제8403호)」, 국가법령정보센터 제정·개정이유 DB, 서울대 사회보장법연구회 「노인장기요양보험법 제정사」(사회보장법연구) 등 복수의 독립 자료가 일치한다.
2. **결정적 근거 — 8402호가 무엇인지 특정됐다.** 법률 제8402호(2007-04-27 공포)는 **「항공우주산업개발 촉진법」 일부개정법률**로 확인된다. 즉 8402호는 단순히 "노인장기요양보험법이 아닌 번호"가 아니라 **전혀 다른 분야의 실재하는 법률**이다. 부록의 인용은 존재하지 않는 번호를 쓴 것이 아니라 **다른 법을 잘못 지목한 것**이므로, 그대로 출판되면 독자가 확인했을 때 즉시 드러난다.
3. **날짜는 정확하다**: 2007년 4월 27일 제정(공포), 2008년 7월 1일 시행 — 이 부분은 **CONFIRMED**.
4. 부칙 확인: 제1장(총칙), 제3장, 제23조 일부, 제6·8장, 제54조를 제외한 제9장, 제10장, 제58조를 제외한 제11장, 제12장은 **2007년 10월 1일**에 먼저 시행되었고, 급여 제공을 포함한 본체가 2008년 7월 1일 시행이다. 즉 **단계적 시행**이었다.

**제안 수정**:
- **[필수] `"Law No. 8402"` → `"Law No. 8403"`.**
- **[필수] `00-brief.md` 43행에도 같은 오기("노인장기요양보험법 제8402호")가 전파되어 있으므로 함께 수정할 것.** 브리프가 파이프라인 전체의 기준 문서이므로 여기를 고치지 않으면 Editor·Production 단계에서 오기가 재유입된다.
- [권고] 본문에서 "2008년 시행"을 단정할 경우 각주로 단계적 시행(2007-10-01 일부 / 2008-07-01 본체)을 밝힐 것.
- [권고] 이 항목만 "Enacted"라 쓰고 다른 두 법률은 "Promulgated"라 썼다. 용어를 통일할 것.

**심각도 판단**: 이 책은 "각주/출처가 달린 법조문 인용 수준이 높아 신뢰도 있는 심층 콘텐츠"를 핵심 판매 포인트로 내세운다(00-brief.md 24행). 다른 세 개 법률번호(471, 8435 및 판례번호)가 모두 정확한 상황에서 이 한 건의 오기는 **판매 포인트를 직접 훼손한다.** 출판 전 필수 수정.

---

# C. 참고문헌 URL 실재성 및 서지 정확성 ([1]~[16]) — **[사용자 지정 검증 항목]**

> 아래 "URL 인덱스 확인"은 검색엔진 인덱스에서 해당 URL 문자열 또는 동일 문서가 확인되었다는 뜻이며, HTTP 응답 확인이 아니다(위 "검증 환경상의 한계" 참조).

## C-0. 전제: `mods.go.kr`이 정당한 정부 도메인인가 ([1][2][14])

**상태: CONFIRMED**

**근거**: 통계청은 **2025년 10월 1일** 부(처)급 기관인 **국가데이터처**로 개편되면서 주 도메인을 `kostat.go.kr`에서 `mods.go.kr`로 변경했다. 검색 인덱스에서 `mods.go.kr/board.es?...` 형식의 실제 보도자료 URL이 다수 확인되며(예: 「2024 통계로 보는 1인가구」 `mods.go.kr/board.es?act=view&bid=10820&list_no=434103&mid=a10301010000`), `kostat.go.kr`도 아직 병행 서비스 중이다. **조작된 도메인은 없다.**

---

## C-1. [1] "National Data and Statistics Office, '2024 Statistics of One-person Households,' 9 December 2024."

**상태: CONFIRMED (문서·수치·발표일) / NEEDS REVIEW (기관명 시대착오, URL 미확인)**

**근거**:
- **문서·수치·발표일 전부 확인**: 「2024 통계로 보는 1인가구」, **2024-12-09** 발표, 2023년 1인가구 782만 9천 가구 = 전체 가구의 35.5%. 부수 지표(거처 단독주택 40.1%/아파트 34.9%, 취업자 1인가구 467만 5천, 연소득 3,223만 원 = 전체 가구의 44.9%)도 확인되어 문서 동일성이 확실하다.
- **기관명 문제 (시대착오)**: [1]은 2024년 12월 문서인데, 그 시점의 발행 기관은 **통계청(Statistics Korea)**이다. 국가데이터처는 **2025년 10월 1일**에야 출범했다. 2024년 문서를 2025년에 생긴 기관 이름으로 인용하면 서지적으로 틀린다.
- **기관 영문명 문제**: 국가데이터처의 영문명은 **"Ministry of Data and Statistics" (MODS)**다(Korea Times 등 영문 보도 및 기관 공식 SNS 계정 `@MODS_korea`에서 확인). **"National Data and Statistics Office"는 확인되지 않는 조합**이다.
- **URL 미확인**: 부록의 `mid=a20101000000&bid=11763&list_no=438857`은 국문판(`mid=a10301010000&bid=10820&list_no=434103`)과 모든 파라미터가 다르다. 영문 보도자료 게시판 경로일 가능성이 높아 값이 다른 것 자체는 모순이 아니지만, 일치를 확인하지 못했다. 또한 `board.es?...&list_no=` 형식은 게시판 내부 일련번호 의존 링크이고, **2025년 10월 도메인 이전 과정에서 다수 딥링크가 깨진 것으로 보고**되었다.

**제안 수정**: `Statistics Korea, "2024 Statistics of One-person Households," 9 December 2024 (agency now the Ministry of Data and Statistics).` + production 직전 URL 재확인, 가능하면 KOSIS 통계표 번호 병기.

---

## C-2. [2] "National Data and Statistics Office, 'Preliminary Results of Birth and Death Statistics in 2025,' 25 February 2026."

**상태: CONFIRMED (문서·발표일·기관명) / NEEDS REVIEW (URL 형식, 최신성)**

**근거**:
- **발표일 2026-02-25 확인됨** (1차 리포트에서 미확정이던 항목이 이번에 확정되었다). 「2025년 출생·사망통계(잠정)」, 국가데이터처, 2026년 2월 25일. 수치도 일치: 출생아 254,500명(+16,100명, +6.8%), TFR 0.80. 지역별(전남 1.10 / 세종 1.06 / 서울 0.63 / 부산 0.74)까지 확인되어 문서 동일성이 확실하다.
- **기관명은 이 항목에서는 맞다**: 2026년 2월 문서이므로 국가데이터처가 발행 기관이다. 다만 영문명은 "Ministry of Data and Statistics"로 고칠 것(C-1 참조).
- **URL 형식 문제**: `ref_bid=`에 12개 이상의 게시판 ID가 나열된 긴 세션성 파라미터가 붙어 있다. **브라우저 탐색 중 주소창을 그대로 복사한 흔적**이며 영구 링크로 부적합하다.
- **최신성**: A-3 참조. **2026-08-26 확정 보도자료를 각주에 추가해야 한다.**

**제안 수정**: `ref_bid` 등 불필요 파라미터 제거 + 확정치 보도자료 병기.

---

## C-3. [3] OECD, "Gender Wage Gap: Definition and Source Dataset." `https://www.oecd.org/en/data/indicators/gender-wage-gap.html`

**상태: CONFIRMED (URL 실재) / NEEDS REVIEW (제목 표기, 정의 인용)**

**근거**: 해당 URL이 OECD의 실제 "Gender wage gap" indicator 페이지로 인덱스 확인된다. 정의도 확인: "the difference between median earnings of men and women relative to median earnings of men", **"Estimates refer to full-time employees and to self-employed"**, unadjusted.

**제안 수정**:
1. 제목 "Gender Wage Gap: Definition and Source Dataset"은 OECD 페이지의 실제 제목이 아니라 저자가 붙인 설명이다. 실제 제목은 **"Gender wage gap"**.
2. 지표 페이지는 값이 갱신되므로 **접근일(accessed date)** 병기 필수.
3. 부록 본문의 정의 인용이 self-employed를 누락한 문제는 A-6 참조.

---

## C-4. [4] OECD, *Education at a Glance 2025: Korea* country note

**상태: CONFIRMED**

**근거**: URL `.../education-at-a-glance-2025_1a3543e2-en/korea_252c9ed2-en.html`이 실제 한국 국가노트 페이지로 인덱스 확인되며, 대응 PDF(`.../education-at-a-glance-2025-country-notes_9749f4ff/korea_2b3410a2/252c9ed2-en.pdf`)도 존재한다. 부록이 인용한 "71% of 25-34-year-olds"(정밀값 70.6%)도 이 문서의 실제 서술과 일치한다. **A-7의 성별 분리 수치(여 78.2%/남 63.7%)도 같은 EAG 2025 데이터 계열(Education GPS 한국 프로파일)에서 나오므로, 이 각주는 8행의 근거로도 유효하다.**

---

## C-5. [5] OECD, *Inclusive and Sustainable Well-being in Korea*, 2026, 성별·연령·교육별 결과 챕터

**상태: CONFIRMED**

**근거**: 챕터 URL 슬러그 `ensuring-inclusive-and-sustainable-well-being-for-korean-men-and-women-throughout-their-lives-outcomes-by-gender-age-and-education_23e274c3.html`이 문자열까지 정확히 인덱스 확인된다. 보고서 정식 제목은 **OECD (2026), *Inclusive and Sustainable Well-being in Korea: 30 Years of OECD Membership and Future Policy Opportunities*, OECD Publishing, Paris** — 2026년 한국 OECD 가입 30주년을 계기로 발간. "2026" 연도 표기 정확. 해당 챕터가 성별·연령·교육별 결과를 다룬다는 서술도 정확하다.

---

## C-6. [6] Korean Legislation Research Institute, "Civil Act," English reference translation. `elaw.klri.re.kr/eng_service/lawView.do?hseq=61788&lang=ENG`

**상태: CONFIRMED (지시 대상 확인) / NEEDS REVIEW (판본 고정 문제)**

**근거**: 1차 리포트에서 미확인이던 `hseq=61788`이 이번에 확인되었다 — **`hseq=61788`은 실제로 민법(Civil Act)을 가리키며, 구체적으로 법률 제19098호(2022년 12월 27일 개정) 판본**이다. `elaw.klri.re.kr`이 한국법제연구원의 공식 영문 법령 DB라는 점도 확인.

**남은 우려**: KLRI의 `hseq`는 **법령의 특정 개정 판본마다 부여되는 일련번호**다. 즉 이 링크는 "현행 민법"이 아니라 **2022년 개정 판본**으로 고정된다. 이 책이 다루는 **호주제 관련 조문(제778조, 제781조 제1항, 제826조 제3항)은 2005년 결정 이후 삭제·개정된 조문이므로, 2022년 판본에는 존재하지 않는다.** 독자가 링크를 눌러 조문을 찾으려 하면 찾을 수 없다.

**제안 수정**: 서지에 **법령명·법률번호·판본일자**를 명기하고(`Civil Act, Act No. 19098, amended 27 Dec 2022`), **폐지 조문은 별도로 개정 전 판본 또는 헌재 결정문에서 인용할 것.** 부록 65행이 이미 "최종판에는 공식 헌재 결정문과 국문 법령 원문을 병기해야 한다"고 스스로 인정한 항목이므로, 그 지적은 타당하며 반드시 이행할 것.

---

## C-7. [7] NHRC, "The Hoju System is Unconstitutional and a Violation of Human Rights," 11 March 2003

**상태: CONFIRMED (문서 실재·내용) / NEEDS REVIEW (URL 구식, 날짜 미확정)**

**근거**:
1. **문서 실재 확인**: 국가인권위원회 보도자료 「호주제는 위헌이며 인권침해 제도」가 실재하며, **현행 주소는 `humanrights.go.kr/base/board/read?boardManagementNo=24&boardNo=554553`**이다. 부록의 영문 제목은 국문 제목의 정확한 번역이다.
2. **내용 정합성 확인**: 인권위(위원장 김창국)가 헌재 계류 중인 호주제 위헌법률심판사건에 "호주제 관련 규정은 위헌이며, 호주제는 인권침해 제도"라는 의견을 제출하기로 결정한 사안. 계기는 **한국가정법률상담소가 2003년 1월 인권위에 공식 의견표명을 요청**한 것. 지적 내용(호주 중심 가족·여성 종속, 가족 간 서열화, 혼인·가족형성의 자유 침해, 남계혈통 승계로 인한 딸·아내·어머니로서 여성의 권리 침해)은 부록 65행의 요약("the human-rights objections raised against the Hoju system")과 정확히 부합한다.
3. **URL은 구식**: 부록의 `/site/program/board/basicboard/view?currentpage=46&...&boardid=7000525`는 **이전 CMS 형식**이다. 링크 생존이 의심된다.
4. **`currentpage=46` 파라미터가 박혀 있다.** 게시물이 추가되면 페이지 번호가 밀리므로 영구 링크로 부적합하다([2]와 같은 복사 흔적).
5. **발표일 "11 March 2003"은 이번에도 독립 확인하지 못했다.** 2003년 1월 요청 → 인권위 전원위 의결 → 헌재 의견 제출이라는 흐름과 3월이라는 시점은 개연적이나 확정하지 못했다.

**제안 수정**: URL을 `boardManagementNo=24&boardNo=554553` 형식으로 교체(불필요한 `page=` 파라미터 제거)하고, 게시일자를 원문 상단에서 직접 확인해 확정할 것.

---

## C-8. [8] KWDI, "Rise of Single-person Households and Direction for Family Policy."

**상태: CONFIRMED (URL·제목 실재) / NEEDS REVIEW (서지 불충분, 본문 미인용)**

**근거**: 부록의 URL `eng.kwdi.re.kr/inc/download.do?ut=A&upIdx=102029&no=1`과 제목이 한국여성정책연구원 영문 사이트의 실제 다운로드 링크로 **문자열까지 정확히 인덱스 확인**된다. KWDI는 1983년 설립된 국무총리 산하 젠더·가족 정책 연구기관으로 실재한다.

**남은 문제**:
1. **저자·발행연도·보고서 번호가 전혀 없다.**
2. `download.do?upIdx=` 형식의 **직접 다운로드 링크**라 랜딩 페이지가 아니며, 파일 인덱스 변경 시 깨진다.
3. **이 참고문헌은 부록 본문에서도, 어떤 챕터에서도 인용되지 않는다**(D-2 참조). 챕터 5 검증 리포트가 혼밥/혼술 인프라 서술의 잠재 근거로 [8]을 지목했으나, 그 문헌이 실제로 해당 내용을 다루는지는 미확인 상태다.

**제안 수정**: 저자·발행연도 보완 후 랜딩 페이지 URL로 교체. 실제로 어느 주장을 뒷받침하는지 명확히 하거나, 근거가 없다면 References가 아닌 Further reading으로 분리.

---

## C-9. [9] Kim, M. S., "Rites and Rights: Lineage Property and Law in Korea," **Acta Koreana** / OpenEdition, 2020.

**상태: NEEDS REVIEW — URL·제목·저자·연도는 정확하나, 게재 학술지명이 틀렸다**

**근거**:
- URL `journals.openedition.org/acrh/11667`과 논문 제목은 **정확히 실재한다.** 저자는 **Marie Seong-Hak Kim**으로 "Kim, M. S."와 일치. 2020년 발표도 일치.
- **그러나 게재지는 *Acta Koreana*가 아니다.** 이 논문은 ***L'Atelier du Centre de recherches historiques*, Revue électronique du CRH, 22 (2020)**에 게재되었다(DOI 10.4000/acrh.11667). **URL 경로의 `acrh`가 곧 이 저널의 코드**다. *Acta Koreana*는 계명대 한국학연구원 발행 저널로 OpenEdition에 없다. **저자가 URL 경로의 `acrh`를 "Acta Koreana"의 약자로 오독한 것으로 보인다.**
- 내용 정합성은 좋다: 식민지 판사들이 조선의 제사 관행과 일본 민법의 근대적 재산권 원리 사이에서 조정해야 했던 과정, 경제/의례·공/사·가족/국가의 경계 재획정을 다루므로 이 책 챕터 1~3의 논지와 직접 연결된다.

**제안 수정**: `Kim, Marie Seong-Hak. "Rites and Rights: Lineage Property and Law in Korea." L'Atelier du Centre de recherches historiques 22 (2020). DOI: 10.4000/acrh.11667.`

---

## C-10. [10] SAGE Journals, "The Impacts of Birth Order and Social Status on the Genealogy Register," 2010.

**상태: NEEDS REVIEW — URL·연도는 정확, 서지정보가 불완전/부정확 + 내용 적합성 의문**

**근거**:
- DOI 10.1177/0363199009357158은 실재하며 **Sangkuk Lee, "The Impacts of Birth Order and Social Status on the Genealogy Register **in Thirteenth- to Fifteenth-Century Korea**," *Journal of Family History* 35(2), 2010, pp. 115–127**이다. 연도 일치.
- **문제 1 — 제목 절단**: 시기 한정구("in Thirteenth- to Fifteenth-Century Korea")가 빠졌다. 이 책이 고려~조선 초기 논의에 쓰는 자료인 만큼 **시기 정보야말로 빠뜨리면 안 되는 부분**이다.
- **문제 2 — 플랫폼명을 저널명 자리에 넣었다**: "SAGE Journals"는 출판 플랫폼이고 실제 저널은 *Journal of Family History*.
- **문제 3 — 저자명 없음.**
- **문제 4 (신규) — 내용 적합성**: 이 논문은 현존 최고(最古) 족보인 **1476년 안동권씨 족보(성화보)**를 대상으로, **혈통선·형제 출생순위는 족보 등재에 유의한 영향이 없었고 직역(사회적 지위)이 훨씬 크게 작용했다**는 것이 핵심 발견이다. 즉 이 논문의 주제는 **출생순위·신분**이지, 부록 63행이 주장하는 **"딸의 후손 포함(inclusion of daughters' descendants)"이 아니다.** 대상 자료(성화보)가 딸의 후손을 등재한 대표 사례인 것은 맞지만, **이 논문이 그 논점을 입증하는 문헌은 아니다.** 게다가 [10]은 부록 본문에서 인용조차 되지 않는다(D-2).

**제안 수정**: `Lee, Sangkuk. "The Impacts of Birth Order and Social Status on the Genealogy Register in Thirteenth- to Fifteenth-Century Korea." Journal of Family History 35, no. 2 (2010): 115–127.` + 이 논문으로 무엇을 입증하려는지 Writer가 재확인할 것.

---

## C-11. [11] Korean Journal of Historical Studies, "research on equal inheritance and Joseon-period family/property history."

**상태: NEEDS REVIEW — URL은 실재하나 인용 라벨과 실제 논문의 시기가 어긋난다 (이 부록에서 가장 실질적인 서지 문제)**

**근거**:
- URL `journal.kci.go.kr/hksh/archive/articleView?artiId=ART001482849`는 실재하며, 해당 논문은 **김경숙, "조선후기 光州 全義李氏家의 재산상속"(The property inheritance practices of the Jeon'eui Yi Family of the Gwangju area during the latter half period of the Joseon dynasty), 『한국사연구』(The Review of Korean History) 99 (2010): 111–146**으로 확인된다. 내용은 조선 후기 광주 거주 전의이씨가의 분재기 분석.
- **핵심 문제 — 시기 불일치**: 부록 63행은 [15][16]과 함께 **"early Joseon inheritance"**와 **"equal or partible inheritance practices"**를 뒷받침하는 자료군을 제시하는 맥락에 있는데, 이 논문은 제목부터 **조선 후기(latter half period)** 한 가문의 사례연구다. 조선 후기는 균분상속이 **해체되고 장자 우대로 전환된** 시기다. 즉 이 논문은 "조선 초기 균분상속"의 근거로 부적절하거나, 최소한 **정반대 방향의 변화를 보여주는 자료**다. 부록이 붙인 라벨("research on equal inheritance")이 실제 논문 내용과 일치하지 않는다.
- **부차 문제 — 저널명**: 부록은 "Korean Journal of Historical Studies"라 적었으나, KCI가 제시하는 이 저널(코드 `hksh` = 한국사연구)의 영문명은 **"The Review of Korean History"**다. 저자명·발행연도·권호·쪽수도 전혀 없다.

**제안 수정**:
1. `김경숙 (Kim, Kyung-suk). "조선후기 光州 全義李氏家의 재산상속." The Review of Korean History 99 (2010): 111–146.`으로 서지 보완.
2. 더 중요하게, **이 논문을 "균분상속의 근거"로 인용하는 것이 맞는지 Writer/Researcher가 재판단할 것.** 조선 초기 균분상속을 입증하려면 『경국대전』 형전 사천조의 자녀 균분 규정, 15~16세기 분재기(화회문기·별급문기) 연구를 직접 인용해야 한다. 참고로 00-brief.md는 조사 범위에 **"1566년 화회문기(이이/신사임당 가문)"**를 명시했는데, **부록 [1]~[16] 어디에도 이를 뒷받침하는 출처가 없다**(D-3 참조).

---

## C-12. [12] OECD, *Inclusive and Sustainable Well-being in Korea*, 2026.

**상태: CONFIRMED**

**근거**: 랜딩 페이지 URL `.../inclusive-and-sustainable-well-being-in-korea_a8940343-en.html`이 인덱스 확인된다. 정식 제목·연도는 C-5와 동일.

**제안 수정**: [5]와 [12]는 같은 보고서의 챕터/본체 중복 인용이다. `[12], ch. X` 형태의 종속 인용으로 정리 권고(서지 정확성 문제는 아님).

---

## C-13. [13] OECD, *Education at a Glance 2025*. `.../publications/2025/09/education-at-a-glance-2025_c58fc9ae.html`

**상태: NEEDS REVIEW**

**근거**: *Education at a Glance 2025*가 **2025년 9월** 발간된 실재 보고서라는 점은 CONFIRMED이며, `oecd.org/en/publications/<YYYY>/<MM>/...` 형식도 OECD의 실제 URL 패턴이다. 또한 EAG 2025는 **고등교육(tertiary education)에 특별한 초점**을 둔 판이므로 이 책의 인용 맥락에 적합하다.

다만 인덱스에서 확인되는 본체 landing은 `.../education-at-a-glance-2025_1c0d9c79-en...` 계열이라 **부록의 DOI 접미사 `c58fc9ae`와 다르다.** 도메인 차단으로 어느 쪽이 유효한지 확정하지 못했다. (OECD는 같은 간행물에 대해 복수 landing URL을 운용하므로 둘 다 유효할 수 있다.)

**제안 수정**: 접속 확인 필요. [4]와 [13]도 같은 간행물(국가노트 vs 본체)의 중복 인용이므로 정리 권고.

---

## C-14. [14] Statistics Korea / National Data and Statistics Office, Population and Household Statistics portal. `mods.go.kr/menu.es?mid=a20108000000`

**상태: NEEDS REVIEW**

**근거**: 도메인은 실재(C-0)하나, 해당 `mid` 경로가 인구·가구 통계 포털인지 확인하지 못했다. 기관명 병기 방식("Statistics Korea / National Data and Statistics Office")이 [1][2]와 불일치하며 후자는 공식 영문명이 아니다(C-1). 이 항목 역시 본문에서 인용되지 않는다(D-2).

**제안 수정**: 기관명을 "Ministry of Data and Statistics (MODS)"로 통일, 경로 접속 확인.

---

## C-15. [15] National Library of Korea, "Having a Glimpse of the Lives of Women in the Past."

**상태: CONFIRMED (URL·내용 정확히 일치) / NEEDS REVIEW (증거력)**

**근거**:
- URL `nl.go.kr/EN/contents/EN32701000000.do`가 국립중앙도서관 영문 사이트의 실제 디지털 컬렉션 페이지로 **문자열까지 정확히 확인**된다: "National Library of Korea > Collection > Digital Collection > Having a glimpse of the lives of women in the past > Introduction". 자매 페이지(`EN32702000000.do`, Introduction by Category)도 존재한다.
- **내용도 부록의 사용 취지와 정확히 부합한다**: 조선을 "남존여비(man is the heaven and woman is the earth)"라는 통념만으로 보는 것을 경계하고, **"딸은 남만 못하다"는 관념이 오류로 보인다**며 딸과 과부가 된 며느리에 대한 사회적 배려를 보여주는 자료를 제시한다. 부록 63행의 "historical variation and gradual transformation, not ... socially egalitarian"이라는 신중한 서술과 방향이 정확히 맞다.
- **증거력 한계**: 이는 도서관 디지털 컬렉션 **소개 페이지**이지 심사를 거친 학술 연구가 아니다. 소장 자료도 『태교신기』(1800), 『규합총서』(1809) 등 **19세기 초** 중상층 여성 문헌 중심이며, 페이지 자신이 "20세기 초까지 대부분의 여성이 문맹이었으므로 남아 있는 자료는 중상층 여성에 편중된다"고 밝힌다. 즉 **"초기 조선/고려의 족보에 딸의 후손이 포함되었다"는 사료적 주장을 단독으로 지탱하기엔 시기도 성격도 맞지 않는다.**

**제안 수정**: 유지하되, 균분상속·자녀안·족보 등재에 관한 **학술 논문을 최소 1편 보강**할 것.

---

## C-16. [16] Korean Genealogy Research, "The Historical Background of the Popularity of Genealogies in Korea."

**상태: NEEDS REVIEW — URL·제목·연도는 정확, 학술지명이 실재하지 않는 명칭이다**

**근거**:
- DOI 10.1177/0363199020928364는 실재하며 **Sangwoo Han, "The Historical Background of the Popularity of Genealogies in Korea," *Journal of Family History*, June 2020**으로 확인된다. URL·제목·연도 일치.
- **"Korean Genealogy Research"는 학술지명이 아니다.** [10]에서 플랫폼명("SAGE Journals")을 저널명 자리에 넣은 것과 같은 유형이되, 이쪽은 **존재하지 않는 저널명을 만들어 넣은** 형태라 더 나쁘다. 실제 저널은 [10]과 동일한 *Journal of Family History*다. **저자명도 없다.**
- **내용 적합성 (1차 리포트보다 우호적으로 정정)**: 이 논문은 족보 편찬 유행이 **17세기경 확산**된 배경을 다루므로 "초기 족보"와는 시기가 다르다. 다만 논문의 핵심 논점 중 하나가 **"한국 족보의 선별적 부계 기록과 잦은 인척(relatives-in-law) 포함"**이며, 이것이 중국 등 다른 동아시아 족보와의 차이를 설명한다고 본다. **인척 포함 = 외손 등재 논의와 직접 연결되므로, 부록 63행의 "딸의 후손 포함" 주장을 부분적으로는 뒷받침한다.** 1차 리포트가 이 점을 과소평가했으므로 여기서 정정한다. 그럼에도 "**early** genealogical records"라는 시기 한정과는 여전히 어긋난다.

**제안 수정**: `Han, Sangwoo. "The Historical Background of the Popularity of Genealogies in Korea." Journal of Family History (June 2020). DOI: 10.1177/0363199020928364.` + 본문에서는 이 논문이 실제로 뒷받침하는 범위(17세기 이후 족보 확산, 인척 포함의 한국적 특징)로 주장을 좁힐 것.

---

# D. 원고 구조 / 각주 체계 검증

## D-1. 주장(암묵): "이 책은 각주가 달린 원고다" (00-brief.md 24행 판매 포인트)

**상태: UNSUPPORTED**

**근거**: `02-chapters/` 전체에서 각주 마커 `[숫자]`를 전수 검색한 결과, **마커 25개가 전부 `08-appendix-statistical-references.md` 한 파일 안에만 존재한다.** `00-introduction.md`, `01-confucian-foundation.md`, `02-colonial-disruption.md`, `03-hoju-system.md`, `04-women-workforce.md`, `05-demographic-implosion.md`, `06-generational-fractures.md`, `07-epilogue.md` — **여덟 개 챕터 모두 인라인 각주가 0개다.**

동시에 이 챕터들은 검증 대상 수치를 그대로 서술한다:
- `05-demographic-implosion.md:31` — "TFR that dropped to 0.72 in 2023 (rising modestly to 0.75 in 2024 and about 0.8 in 2025)" (각주 없음)
- `04-women-workforce.md:3` — "the tertiary education attainment rate for young women aged 25 to 34 exceeded 75%" (각주 없음)
- `04-women-workforce.md:7` — "an OECD-leading gender wage gap of approximately 29% (2023-2024)" (각주 없음)
- `07-epilogue.md:11` — "0.72 in 2023 ... 0.75 in 2024 ... about 0.8 in 2025, a gender wage gap of about 29%" (각주 없음)

즉 **부록이 이 책 전체 사실검증의 기반 파일이라는 전제가 현재 원고에서는 기능하지 않는다.** 부록은 독립된 참고문헌 목록으로 존재할 뿐, 본문의 어떤 주장과도 기계적으로 연결되어 있지 않다.

**제안 수정**: Writer 단계로 되돌려 본문 정량 주장마다 각주 마커를 삽입할 것. Editor의 문장 다듬기로 해결되지 않는다.

---

## D-2. 주장(암묵): 참고문헌 [1]~[16]이 모두 실제로 인용된 자료다

**상태: UNSUPPORTED (고아 참고문헌 7건)**

**근거**: 부록 본문에서 실제로 호출되는 각주는 **[1][2][3][4][5][6][7][15][16] 9건뿐**이다. **[8], [9], [10], [11], [12], [13], [14] 7건은 부록 어디에서도 호출되지 않는다.** 챕터에도 각주가 없으므로(D-1), 이 7건은 **책 전체에서 단 한 번도 인용되지 않는 고아 항목**이다.

특히 [9][10][11]은 63행이 "[15] [16]"만 호출하기 때문에 인용되지 않는데, **내용상 63행(조선 초기 상속·족보)을 뒷받침해야 할 자료가 바로 이 셋**이다. 즉 가장 학술성이 높은 역사 문헌 3건이 정작 인용 사슬에서 빠져 있다.

**제안 수정**: 각 항목이 어떤 주장을 뒷받침하는지 본문에 연결하거나, 연결되지 않으면 "Further reading"으로 섹션을 분리할 것. 인용되지 않은 항목을 References로 제시하는 것은 **출처가 있는 것처럼 보이게 하는 효과**가 있어 그대로 두기 어렵다.

---

## D-3. 주장(암묵): 부록이 이 책의 역사 파트 주장을 뒷받침한다

**상태: UNSUPPORTED (역사 파트 출처 공백)**

**근거**: 00-brief.md 44행은 조사 범위로 **"고려~조선 초기 균분상속(경국대전), 1566년 화회문기(이이/신사임당 가문), 서류부가혼, 윤회봉사"**를 명시한다. 그러나 부록 [1]~[16] 중 **경국대전·1566년 화회문기·서류부가혼(壻留婦家婚)·윤회봉사(輪回奉祀) 중 어느 것도 직접 뒷받침하는 출처가 없다.**

역사 관련 참고문헌은 [9](조선~식민지기 종중재산과 법), [10](13~15세기 족보 등재의 출생순위·신분 효과), [11](조선 **후기** 한 가문 재산상속), [15](도서관 디지털 컬렉션 소개), [16](17세기 이후 족보 확산 배경) 5건인데, **브리프가 지목한 4개 항목을 정면으로 다루는 것은 하나도 없다.** 시기도 대부분 조선 후기 이후에 몰려 있어, 이 책이 논증하려는 "고려~조선 초기의 양측적 친족"과 어긋난다.

특히 **1566년 화회문기처럼 구체적 연도·문서명이 붙은 사료 주장**은 출처 없이 서술될 경우 검증 불가능한 주장이 된다.

**제안 수정**: Researcher 단계로 되돌려 역사 파트 1차/2차 출처를 보강할 것. 최소한 (1) 『경국대전』 형전 사천조 자녀 균분 규정, (2) 1566년 이이 남매 화회문기(분재기) 관련 연구, (3) 윤회봉사·서류부가혼에 관한 한국사 연구를 각각 확보해야 한다. **본 검증에서는 해당 사료 주장 자체를 검증하지 않았다** — 부록에 출처가 없어 검증 대상이 없었기 때문이다(해당 챕터 리포트와 대조 필요).

---

## D-4. 교차 플래그: 챕터 04의 "Throughout the 2010s and 2020s, the tertiary education attainment rate for young women aged 25 to 34 exceeded 75%"

**상태: NEEDS REVIEW (부록보다 강한 주장)**

**근거**: 부록 8행은 시기 한정 없이 "Exceeds 75%"라고만 하는데, 챕터 04는 이를 **"2010년대와 2020년대 내내(throughout)"**로 확장했다. 확인된 시계열은 2005년 남녀 51% 동률, 2006년 여성 추월, **2024년 여성 78.2%**다. **2010년대 초반 값을 확인하지 못했고**, 2005년 51%에서 2024년 78.2%로 상승한 궤적을 보면 2010년대 초반에 이미 75%를 넘었을 가능성은 낮다. 확정적으로 틀렸다고 말할 근거는 없으나, **현재 확보된 근거로 "throughout the 2010s"를 뒷받침할 수 없다.**

**제안 수정**: OECD EAG 연도별 성별 이수율 시계열로 75% 최초 돌파 연도를 특정하고, 그 전까지는 "by the early 2020s" 같은 안전한 표현으로 후퇴할 것.

---

# E. 최종 판정 및 다음 단계 권고

## 잘 되어 있는 부분 (그대로 유지 권고)

- **핵심 통계 수치의 정확도가 높다.** TFR 0.72/0.75/0.80, 임금격차 29.3%(2023)·34.1%(2018)·OECD 1위, **고등교육이수율 여 78.2%/남 63.7%/전체 70.6%**, 1인가구 782.9만·35.5%(2023), 2025년 출생아 254.5천(잠정)·+6.8% — **전부 원자료와 일치한다.** 반올림·근사 표현도 과장 없이 보수적이다.
- **부록의 자기 경고(71% vs 75%+)는 타당했고, 이번에 해소되었다.** 두 수치는 모순이 아니라 성별 미분리/분리의 차이이며, 부록의 방법론적 지적이 정확했다. 다만 이제 답이 확정되었으므로 미해결 상태로 남기지 말 것(A-9).
- **법령/판례의 날짜는 4건 중 4건 모두 정확하다.** 1958.2.22/1960.1.1, 2005.2.3, 2007.5.17/2008.1.1, 2007.4.27/2008.7.1. 법률번호도 471호·8435호는 정확하며, 판례 사건번호 계열(2001헌가9)도 정확하다.
- **참고문헌 URL의 실재성은 전반적으로 양호하다.** [1][2][3][4][5][6][7][8][9][10][11][12][15][16] 14건이 실재 문서로 확인되었다. **조작되거나 존재하지 않는 URL은 발견되지 않았다.** 문제는 URL이 아니라 **URL에 붙인 라벨(저널명·기관명·제목)**이다.

## 되돌림 권고: **Editor로 넘기지 말고 Writer/Researcher로 되돌릴 것**

우선순위 순:

1. **[필수·확정 오류] 노인장기요양보험법 `"Law No. 8402"` → `"Law No. 8403"`.** 8402호는 「항공우주산업개발 촉진법」 일부개정법률로 특정되었다. **`00-brief.md` 43행의 동일 오기도 함께 수정할 것.**
2. **[필수·확정 오류] 1인가구 분모 `"residential units"` → `"households"`.** 통계 정의 오류이며, 부록 자신의 "denominator 명시" 원칙 위반이다.
3. **[필수·최신성] 2025년 출생통계 확정치 반영** (254.3천 명 / +6.7% / TFR 0.80 확정, 2026-08-26 발표). 4행의 "(provisional)" 라벨 제거, 67행 수치 갱신, [2]에 확정 보도자료 추가.
4. **[필수·최신성] 1인가구 2024년 확정치 36.1%(804.5만 가구) 반영**, 35.5%는 2023년 값으로 라벨링, [1]에 「2025 통계로 보는 1인가구」(2025-12-09) 추가.
5. **[필수·구조] 본문 챕터 8개에 각주 마커가 0개.** Writer가 정량 주장마다 [n]을 삽입해야 한다. 이 책의 핵심 판매 포인트가 여기 걸려 있다.
6. **[필수·서지] 참고문헌 라벨 오류 3건**: [9] 저널명(Acta Koreana → *L'Atelier du Centre de recherches historiques*), [16] 존재하지 않는 저널명("Korean Genealogy Research" → *Journal of Family History*, 저자 Sangwoo Han), [10] 제목 절단 + 플랫폼명을 저널명으로 표기(저자 Sangkuk Lee, *Journal of Family History* 35(2): 115–127).
7. **[필수·내용] [11]의 시기 불일치.** 조선 **후기** 사례연구(김경숙 2010)를 조선 **초기** 균분상속의 근거로 쓰는 것은 부적절하다. Researcher 재작업 필요.
8. **[필수·공백] 역사 파트 출처 공백** (경국대전·1566년 화회문기·서류부가혼·윤회봉사). Researcher 단계.
9. **[권고] 기타 정정**:
   - 8행에 기준연도(2024) 추가, 성별 분리 수치(여 78.2%/남 63.7%) 명시
   - "still the highest" → "still the highest **in the OECD**"
   - 임금격차 정의에 **self-employed 포함** 반영, "full-time earnings" → "median earnings"
   - "Original codification of the Hoju system" 한정 (식민지기 선행 법제화 인정)
   - 2005년 결정에 **민법 제826조 제3항** 추가, 제781조는 **제1항 본문 후단**으로 한정
   - "Enacted" / "Promulgated" 용어 통일
10. **[권고] 기관명 정정**: `"National Data and Statistics Office"`는 확인되지 않는 영문명이다. 2024년 이전 자료 → **Statistics Korea**, 2025년 10월 이후 자료 → **Ministry of Data and Statistics (MODS)**.
11. **[Production 전 필수] 링크 전수 점검.** 이 세션에서 8개 도메인이 조직 정책상 차단되어 HTTP 응답 확인이 불가능했다. 특히 `list_no=` / `currentpage=` / `page=` / `download.do?upIdx=` 형식의 링크 5건([1][2][7][8][14])은 구조적으로 깨지기 쉬우며, [1][2][14]는 2025년 10월 `kostat.go.kr → mods.go.kr` 도메인 이전 영향권에 있다. [7]은 현행 주소(`boardManagementNo=24&boardNo=554553`)가 확인되었으므로 즉시 교체 가능하다.

## 검증하지 않은 항목

- **Figure register 표(Figure 1~14)** — 지시에 따라 제외(Visual Director 소관).
- **다른 챕터 본문의 개별 주장** — 각 챕터 담당 소관. 단 A/B 섹션의 수치·법령은 챕터 04·05·07에도 그대로 등장하므로 본 리포트 판정과 대조할 것.
- **[7] NHRC 보도자료의 게시일자(2003-03-11)** — 문서 실재와 내용은 확인했으나 날짜는 두 차례 시도에도 독립 확인하지 못했다. 원문 상단에서 직접 확인 필요.
- **2024년 성별임금격차 값** — 2023년 29.3%는 확인했으나 2024년 값은 OECD 원자료로 확인하지 못했다.
- **[13] EAG 2025 본체 landing URL의 DOI 접미사(`c58fc9ae`)** — 인덱스에서 확인된 계열(`1c0d9c79-en`)과 달라 유효성 미확정.

## 검증에 사용한 독립 출처

- 국가데이터처 「2025년 출생통계」(확정, **2026-08-26**) — 출생아 254,341명, +16,024명(+6.7%), TFR 0.80 (서울신문·정책브리핑·Korea Times)
- 국가데이터처 「2025년 출생·사망통계(잠정)」(2026-02-25) — 254,500명(+6.8%), TFR 0.80 [부록 [2]]
- 통계청 「2024 통계로 보는 1인가구」(2024-12-09) — 2023년 7,829천 가구, 35.5% [부록 [1]]
- 국가데이터처 「2025 통계로 보는 1인가구」(2025-12-09) — **2024년 8,045천 가구, 36.1%**, 연령 구성 70세 이상 19.8%
- OECD Education GPS 한국 프로파일 / EAG 2025 — 25–34세 이수율 **여 78.2% / 남 63.7% / 전체 70.6%**(2024), 각 40개국 중 1위
- OECD gender wage gap indicator 페이지 — 정의 및 범위("full-time employees and to self-employed"), 한국 2023년 29.3% vs OECD 평균 11.3%, 2018년 34.1%
- OECD (2026), *Inclusive and Sustainable Well-being in Korea: 30 Years of OECD Membership and Future Policy Opportunities*
- 위키문헌 「노인장기요양보험법 (제8403호)」 + 국가법령정보센터 제정·개정이유 + 「노인장기요양보험법 제정사」(사회보장법연구) — 제8403호, 2007-04-27 제정, 2008-07-01 시행(일부 2007-10-01)
- 법률 제8402호(2007-04-27) = 「항공우주산업개발 촉진법」 일부개정법률
- 대한민국 민법 — 법률 제471호, 1958-02-22 공포, 1960-01-01 시행
- 헌법재판소 2005-02-03 2001헌가9·10·11·12·13·14·15, 2004헌가5(병합) — 민법 제778조, 제781조 제1항 본문 후단, 제826조 제3항 본문 헌법불합치, 6:3
- 대한변협 공고 및 국가법령정보센터 — 가족관계의 등록 등에 관한 법률, 법률 제8435호, 2007-05-17 공포, 2008-01-01 시행
- 국가인권위원회 「호주제는 위헌이며 인권침해 제도」 (현행 URL `boardManagementNo=24&boardNo=554553`)
- KLRI `hseq=61788` = Civil Act, 법률 제19098호(2022-12-27 개정) 판본
- Marie Seong-Hak Kim, *L'Atelier du Centre de recherches historiques* 22 (2020), DOI 10.4000/acrh.11667
- Sangkuk Lee, *Journal of Family History* 35(2) (2010): 115–127
- Sangwoo Han, *Journal of Family History* (June 2020), DOI 10.1177/0363199020928364
- 김경숙, 『한국사연구』(The Review of Korean History) 99 (2010): 111–146 [KCI ART001482849]
- 국립중앙도서관 영문 디지털 컬렉션 `nl.go.kr/EN/contents/EN32701000000.do`
- KWDI 영문 사이트 `eng.kwdi.re.kr/inc/download.do?ut=A&upIdx=102029&no=1`
