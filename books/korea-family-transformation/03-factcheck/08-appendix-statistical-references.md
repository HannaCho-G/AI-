# Fact Check Report — 08 Statistical Appendix and References

- **검증 대상**: `books/korea-family-transformation/02-chapters/08-appendix-statistical-references.md`
- **검증일**: 2026-08-28
- **검증자**: Fact Checker (독립 검증)
- **원 리서치 자료**: **없음.** `books/korea-family-transformation/01-research/` 디렉터리가 존재하지 않는다. 이 원고는 사용자가 직접 가져온 반쯤 완성된 원고이고, 대조할 내부 리서치 자료가 없으므로 **모든 주장을 원 출처에서 직접 교차검증**했다.
- **검증 범위 제외**: "Figure register for final layout" 표(Figure 1~14) — 지시에 따라 검증 대상에서 제외(Visual Director 소관).

## 검증 환경상의 한계 (먼저 밝힘)

이 세션의 네트워크 이그레스 프록시가 다음 도메인에 대한 직접 접속을 차단했다:
`mods.go.kr`, `www.oecd.org`, `journals.sagepub.com`, `journals.openedition.org`, `elaw.klri.re.kr`, `journal.kci.go.kr`, `www.humanrights.go.kr`, `www.nl.go.kr`.

따라서 **URL의 최종 HTTP 응답(200/404)을 직접 확인하지 못했다.** 대신 검색엔진 인덱스에 해당 URL 문자열이 그대로 존재하는지, 그리고 그 URL에 붙은 제목/기관/저자가 부록의 서술과 일치하는지로 간접 확인했다. 아래에서 "URL 문자열 일치 확인"이라고 쓴 것은 이 간접 확인을 의미하며, **실재성의 강한 증거이지만 링크 생존(link-rot) 여부의 증거는 아니다.** 최종 production 전에 링크 전수 클릭 검사가 반드시 필요하다.

---

# 요약 (Executive Summary)

| 구분 | CONFIRMED | NEEDS REVIEW | UNSUPPORTED |
|---|---|---|---|
| 통계 수치 | 11 | 6 | 0 |
| 법령/판례 | 4 | 2 | **1** |
| 참고문헌 URL/서지 | 6 | 11 | 0 |
| 원고 구조/각주 체계 | 0 | 1 | **3** |

## 즉시 수정이 필요한 확정 오류 (1건)

**노인장기요양보험법의 법률 번호가 틀렸다. "Law No. 8402"가 아니라 "법률 제8403호"다.** 날짜(2007.4.27 공포 / 2008.7.1 시행)는 맞다. 이 책이 "이미 각주/출처가 달린 법조문 인용 수준이 높아 신뢰도 있는 심층 콘텐츠"(00-brief.md 판매 포인트)를 내세우는 만큼, 법률 번호 오타는 신뢰도에 직접 타격을 준다.

## 구조적으로 더 심각한 문제 (수치 오류보다 우선)

**이 부록의 각주 [1]~[16]은 이 부록 안에서만 쓰인다. 본문 챕터(00~07)에는 인라인 각주 마커가 단 하나도 없다.** 즉 "출처가 달린 원고"라는 이 책의 핵심 판매 포인트가 현재 원고 상태로는 성립하지 않는다. 챕터 04·05·07이 0.72 / 0.75 / ~0.8 / 29% / 75%+ 같은 정량 주장을 각주 없이 서술하고 있다. 상세는 아래 D 섹션.

## 권고

**Editor로 넘기기 전에 Writer/Researcher 단계로 되돌릴 것을 권고한다.** 사유는 개별 수치의 오류율이 높아서가 아니다 — 오히려 핵심 수치의 정확도는 상당히 좋다(TFR·임금격차·1인가구 수치는 거의 전부 CONFIRMED). 되돌려야 하는 이유는 (1) 확정 법률번호 오류 1건, (2) 서지정보가 실제 출처와 다른 참고문헌 3건([9][11][16]), (3) 각주가 본문에 전혀 연결되어 있지 않은 구조적 결함이다. (3)은 Editor가 문장을 다듬어서 해결할 수 있는 종류의 문제가 아니다.

---

# A. 통계 수치 검증

## 주장: "Total Fertility Rate (TFR): Recorded at 0.72 in 2023"

**상태: CONFIRMED**

**근거**: 2023년 합계출산율 0.72는 통계청(현 국가데이터처) 인구동향조사 확정치로 널리 확인된다. 또한 국가데이터처 「2025년 출생·사망통계(잠정)」이 2025년 0.80이 2024년 0.75 대비 +0.05라고 밝히면서 2023→2024→2025 계열이 0.72 → 0.75 → 0.80으로 정합적으로 확인된다.

**제안 수정**: 없음. 다만 아래 "출처 귀속 불일치" 항목 참조.

---

## 주장: "with a modest rebound to 0.75 in 2024"

**상태: CONFIRMED**

**근거**: 「2025년 출생·사망통계(잠정)」 보도자료가 "2025년 합계출산율 0.80명, 2024년 0.75명 대비 0.05명 증가"로 2024년 값 0.75를 명시한다.

---

## 주장: "and about 0.8 in 2025 (provisional)"

**상태: CONFIRMED**

**근거**: 「2025년 출생·사망통계(잠정)」이 2025년 합계출산율을 **0.80명**으로 발표했다. "provisional(잠정)"이라는 표기도 원자료의 성격과 정확히 일치한다 — 확정치가 아니라 잠정치가 맞다.

**제안 수정**: "about 0.8"보다 "0.80 (provisional)"로 정확히 쓰는 편이 낫다. 원자료가 소수점 둘째 자리까지 확정 발표했는데 "about"으로 뭉갤 이유가 없고, 부록 자신이 요구하는 "exact series" 원칙에도 맞다.

---

## 주장: TFR 출처 귀속 — 본문은 "(Statistics Korea, Annual Vital Statistics)", 각주는 [5] OECD 웰빙 보고서

**상태: NEEDS REVIEW**

**근거**: 부록 4행은 TFR 0.72의 출처를 "Statistics Korea, Annual Vital Statistics"로 적었으나, 67행에서 같은 0.72에 붙인 각주는 [5] = OECD, *Inclusive and Sustainable Well-being in Korea* (2026)다. 두 출처 모두 실재하고 수치도 같지만, **1차 출처(통계청 인구동향조사)와 2차 인용(OECD 보고서)이 뒤섞여 있다.** 부록 자신이 선언한 "모든 정량적 주장은 출처의 기준 연도와 정의를 함께 읽어야 한다"는 편집 방침과 어긋난다.

**제안 수정**: TFR은 1차 출처(국가데이터처 인구동향조사 / 출생통계)로 각주를 달고, OECD 보고서는 국제 비교 맥락에서만 별도로 인용한다.

---

## 주장: "Gender Wage Gap: Approximately 29% in 2023-2024"

**상태: CONFIRMED**

**근거**: OECD 기준 한국의 성별 임금격차는 2023년 **29.3%** (OECD 평균 11.3%의 약 2.6배). 2024년에 대해서도 복수 보도가 "약 29%"를 보고한다. 부록의 "approximately 29% in 2023-2024"는 정확하다.

---

## 주장: "down from about 34% in 2018"

**상태: CONFIRMED**

**근거**: 2018년 34.1% → 2023년 29.3%로 축소된 것이 확인된다. "about 34%"는 정확한 서술이다.

---

## 주장: "and still the highest (OECD Employment Database)"

**상태: CONFIRMED (단, 표현 보완 필요)**

**근거**: 한국은 1996년 OECD 가입 이래 현재까지 회원국 중 성별 임금격차 1위를 유지하고 있다.

**제안 수정**: "still the highest"의 비교 모집단이 문장에 없다. "still the highest **in the OECD**"로 명시할 것. 또한 출처를 "OECD Employment Database"로 적었으나 각주 [3]은 OECD Gender wage gap **indicator 페이지**를 가리킨다 — 둘 중 실제로 쓴 쪽으로 통일할 것.

---

## 주장: "measuring the difference between male and female median full-time earnings relative to male earnings" / [3] "generally using unadjusted gross earnings of full-time wage and salary workers"

**상태: NEEDS REVIEW (정의 일부 부정확)**

**근거**: OECD 공식 정의는 "the difference between median earnings of men and women relative to median earnings of men"이며, **"Estimates refer to full-time employees and to self-employed"** 즉 **자영업자(self-employed)를 포함**한다. 부록은 이를 "full-time wage and salary workers"(임금근로자)로 좁혀 서술했는데, 이는 OECD 정의와 다르다.

**제안 수정**: "full-time employees and self-employed workers"로 수정하거나, 실제로 임금근로자 한정 계열(예: 고용노동부 계열)을 쓴 것이라면 그 출처로 각주를 바꿀 것. 부록이 "OECD 정의를 따른다"고 선언한 바로 그 문단에서 OECD 정의를 잘못 옮긴 것이므로 그냥 넘기기 어렵다.

---

## 주장: "Tertiary Educational Attainment: Exceeds 75% for females aged 25–34 (OECD Education at a Glance)"

**상태: NEEDS REVIEW — 수치 자체는 뒷받침되나, 괄호 안 출처 귀속이 틀렸고 기준연도가 없다**

**근거**:
- 수치는 뒷받침된다: OECD 자료 기준 **2023년 한국 25~34세 고등교육 이수율은 여성 77%, 남성 63%** (OECD 평균 여성 54%, 남성 41%). 따라서 "여성 75% 초과"는 2023년 기준으로 사실이다.
- 그러나 이 성별 분리 수치가 실린 곳은 **[5] OECD *Inclusive and Sustainable Well-being in Korea*의 성별·연령·교육별 결과 챕터**(및 OECD Family Database CO3.1)이지, 부록이 괄호에 적은 *Education at a Glance*가 아니다. EAG 2025 한국 국가노트는 성별 미분리 71%만 보고한다.
- **기준연도가 표기되어 있지 않다.** 이는 부록 스스로가 69행에서 요구한 "any female-only estimate above 75% must therefore be accompanied by the relevant gender-specific table and reference year"를 8행 자신이 위반한 것이다.

**제안 수정**: "Exceeds 75% for females aged 25–34 (77% in 2023; OECD, *Inclusive and Sustainable Well-being in Korea*, outcomes by gender/age/education — cf. male 63%)"로 수정.

---

## 주장: "surpassing male cohorts in the same age demographic"

**상태: CONFIRMED**

**근거**: 2005년에 남녀 25~34세 이수율이 51%로 같아졌고 2006년부터 여성이 남성을 추월, 이후 계속 유지되어 2023년 여성 77% vs 남성 63%다.

---

## 주장(부록의 자기 경고): "The OECD's 2025 Korea country note reports tertiary attainment for 71% of 25–34-year-olds overall; any female-only estimate above 75% must therefore be accompanied by the relevant gender-specific table and reference year."

**상태: CONFIRMED — 이 지적은 타당하며, 방법론적으로 정확하다**

**근거**: 사용자가 지시한 재확인 항목이므로 명확히 답한다.
1. EAG 2025 한국 국가노트의 71%는 실제로 존재한다: "Korea has the highest rate of tertiary attainment among young adults across OECD countries: 71% of 25-34-year-olds, compared to the OECD average of 48%."
2. 여성 77% / 남성 63% (2023)도 실제로 존재한다.
3. **따라서 71%와 75%+는 서로 모순되는 수치가 아니다.** 71%는 남녀 통합값, 77%는 여성 단독값이며, 남성 63%와 여성 77%를 합하면 70%대 초반이 나오므로 세 숫자는 완전히 정합적이다.
4. 즉 부록의 경고는 "둘 중 하나가 틀렸다"는 경고가 아니라 **"성별 미분리 값과 성별 분리 값을 구분 표기하라"**는 경고이고, 이는 정확하고 타당한 지적이다. 검증 결과 이 주의사항은 **유지되어야 한다.**

**제안 수정**: 경고 자체는 그대로 두되, 이미 답이 나와 있으므로 부록에 실제 성별 분리 수치(여 77% / 남 63%, 2023)를 명시해 경고를 해소된 형태로 바꾸는 것을 권한다. 지금은 독자에게 "우리도 모른다"처럼 읽힌다.

---

## 주장: "Single-Person Households: Represents over 35% of all national residential units"

**상태: CONFIRMED (단, 용어 오류)**

**근거**: 2023년 1인가구는 782만 9천 가구로 전체 가구의 **35.5%**, 관련 통계 작성 이래 최대다.

**제안 수정**: **"residential units"는 잘못된 용어다.** 분모는 주택(housing units)이 아니라 **가구(households)**다. "over 35% of all households"로 반드시 수정할 것. 부록이 요구하는 "denominator를 명시하라"는 원칙을 부록 자신이 어긴 사례다.

---

## 주장: "The 2024 national one-person-household release reports 7.829 million one-person households in 2023, equal to 35.5% of all households.[1]"

**상태: CONFIRMED**

**근거**: 통계청 「2024 통계로 보는 1인가구」(2024.12.9. 발표)가 1인가구 782만 9천 가구, 전체의 35.5%로 보고한다. 발표일 2024년 12월 9일도 당일자 보도로 확인된다. 수치·연도·발표시점 모두 일치한다.

---

## 주장: "up from 9.0% in 1990"

**상태: CONFIRMED (근거 강도: 중)**

**근거**: 1990년 인구주택총조사 기준 전국 1인가구 비중 9.0%는 널리 통용되는 값이며, 검색된 자료도 "1990년까지만 해도 1인 가구는 9%에 불과"를 뒷받침한다. 다만 검색 결과 중 일부는 **서울시 기준 9.1%**를 다루고 있어, 전국값과 서울값이 혼동될 여지가 있다.

**제안 수정**: 최종판에서는 1990년 인구주택총조사 원표(가구원수별 가구) 표번호를 명시해 전국 기준임을 못박을 것. 부록 자신이 "URL or table number"를 요구하고 있다.

---

## 주장: "Single-Person Households ... (Statistics Korea, Population and Housing Census)"

**상태: NEEDS REVIEW (출처 귀속 부정확)**

**근거**: 35.5%라는 수치가 실제로 인용된 문서는 「2024 통계로 보는 1인가구」라는 **가공·종합 보도자료**이고(각주 [1]), 그 기저 자료가 인구주택총조사(등록센서스)다. 반면 1990년 9.0%는 전통적 인구주택총조사에서 나온다. 두 수치의 조사 방식(전통센서스 vs 등록센서스)이 다르므로 단순 시계열 비교 시 각주가 필요하다.

**제안 수정**: "1990 figure from the traditional Population and Housing Census; 2023 figure from the register-based census as compiled in the 2024 one-person-household release" 식으로 구분 표기.

---

## 주장: "the preliminary 2025 birth-and-death release reports 254.5 thousand live births in 2025 and a 6.8% increase from 2024.[2]"

**상태: CONFIRMED**

**근거**: 「2025년 출생·사망통계(잠정)」: 2025년 출생아 수 **254,500명**, 전년 대비 **16,100명(6.8%) 증가**. 2010년 이후 15년 만의 최대 증가폭. 산술 검산도 맞는다(254.5천 − 16.1천 ≈ 238.4천 = 2024년 값).

---

## 주장: [2]의 발표일 "25 February 2026"

**상태: NEEDS REVIEW (경미)**

**근거**: 해당 보도자료의 존재는 확인했으나(국가데이터처 및 대한민국 정책브리핑에 게시), 발표 **일자**를 독립적으로 확정하지 못했다. 통계청/국가데이터처의 전년도 출생·사망통계(잠정)는 통상 2월 말 발표이므로 2026년 2월 25일은 개연성이 높다.

**제안 수정**: production 단계에서 보도자료 상단의 배포일자를 직접 확인해 확정할 것. 리스크는 낮음.

---

## 주장(부록의 방법론 지침): "Updates from 2024 and 2025 should be labeled as updates rather than silently mixed into historical charts."

**상태: CONFIRMED (타당한 방법론적 지침)**

**근거**: 사실 주장이 아니라 편집 지침이므로 진위 판정 대상은 아니나, 2023 확정치와 2025 잠정치를 같은 축에 섞지 말라는 요구는 통계 실무상 정당하다. 유지 권고.

---

# B. 법령 / 판례 검증

## 주장: "Civil Code of the Republic of Korea (Law No. 471): Promulgated Feb 22, 1958; Enforced Jan 1, 1960."

**상태: CONFIRMED**

**근거**: 대한민국 민법은 1957년 12월 17일 국회 통과, **1958년 2월 22일 법률 제471호로 공포**, **1960년 1월 1일 시행**. 법률번호·공포일·시행일 3개 항목 모두 일치한다.

---

## 주장: "(Original codification of the Hoju system)"

**상태: NEEDS REVIEW**

**근거**: 1958년 민법이 호주제를 **최초로 성문화(original codification)**했다는 서술은 오해를 부른다. 호주(戶主)를 중심으로 한 근대적 가(家)·호적 제도는 일제강점기 조선호적령·의용민법 체제에서 이미 법제화되어 있었고, 1958년 민법은 이를 대한민국 법전으로 **승계·재편**한 것에 가깝다. 이 책의 챕터 2(Colonial Disruption)가 바로 그 식민지 법제화를 다루고 있으므로, 부록의 이 표현은 **책 자신의 논지와도 충돌한다.**

**제안 수정**: "First codification of the *hoju* system in the Civil Code of the Republic of Korea, carrying forward the household-head framework given modern legal form under colonial rule" 정도로 한정할 것. 이건 문장 다듬기가 아니라 사실관계 수정이므로 Editor가 아니라 Writer 단계에서 처리해야 한다.

---

## 주장: "Constitutional Court Decision 2001Hun-Ga9 et al. (February 3, 2005): Landmark decision holding Civil Code Articles 778 and 781 (1) non-conforming to the Constitution (Heonbeop-bul-hapchi)."

**상태: CONFIRMED (단, 불완전)**

**근거**: 헌법재판소 전원재판부는 **2005년 2월 3일** 재판관 **6:3** 의견으로 호주제를 규정한 **민법 제778조, 제781조 제1항 본문 중 일부, 제826조 제3항 본문 중 일부**에 대해 **헌법불합치** 결정을 내렸다. 사건번호 2001헌가9 계열(2001헌가9~15 및 2004헌가5 병합)도 일치한다. 날짜·사건번호·결정형식 모두 정확하다.

**제안 수정**: 부록은 제778조와 제781조 제1항만 언급하고 **제826조 제3항(처의 부가입적)을 누락**했다. 호주제의 혼인 관련 축을 빠뜨린 것이므로 추가할 것. 또한 "et al."을 쓸 거라면 최소한 병합 사건번호 범위(2001헌가9·10·11·12·13·14·15, 2004헌가5 병합)를 최종판에 명시하는 편이 좋다. 6:3 의견 분포도 "landmark"라는 서술을 뒷받침하는 정보로 추가 가치가 있다.

---

## 주장: "Act on Registration of Family Relations (Law No. 8435): Promulgated May 17, 2007; Enforced Jan 1, 2008."

**상태: CONFIRMED**

**근거**: 「가족관계의 등록 등에 관한 법률」은 **법률 제8435호**로 **2007년 5월 17일 공포**, **2008년 1월 1일 시행**. 법률번호·공포일·시행일 3개 항목 모두 일치한다. (검색 과정에서 위키문헌의 "인감증명법(제8435호)" 페이지가 함께 잡히나, 이는 같은 법 부칙에 의해 개정된 타법의 판본 표기이므로 모순이 아니다.)

---

## 주장: "Act on Long-Term Care Insurance for the Aged (Law No. 8402): Enacted April 27, 2007; Enforced July 1, 2008."

**상태: UNSUPPORTED — 법률번호 오류**

**근거**: 「노인장기요양보험법」의 법률번호는 **제8402호가 아니라 제8403호**다. 복수의 독립 자료(위키문헌 「노인장기요양보험법 (제8403호)」, 법령 DB 및 제정사 문헌)가 일치하여 **법률 제8403호, 2007년 4월 27일 공포, 2008년 7월 1일 시행**으로 확인한다. 제8402호를 노인장기요양보험법으로 지목하는 근거는 찾지 못했다.

날짜 부분(2007.4.27 / 2008.7.1)은 **CONFIRMED**다.

**제안 수정**:
- "Law No. 8402" → **"Law No. 8403"** 으로 수정 (필수).
- 부수 정보: 부칙상 총칙·장기요양인정 관련 일부 장·조문은 **2007년 10월 1일**에 먼저 시행되었고, 급여 제공을 포함한 본체가 2008년 7월 1일 시행이다. 본문에서 "2008년 시행"을 단정적으로 쓸 경우 각주로 이 단계적 시행을 밝히면 정확도가 올라간다.
- 부록은 이 항목만 "Enacted"라 쓰고 다른 두 법률은 "Promulgated"라 썼다. 용어를 "Promulgated"로 통일할 것.

---

# C. 참고문헌 URL 실재성 및 서지 정확성 ([1]~[16])

## 주장: `mods.go.kr`이 한국 정부 통계기관의 실제 도메인이다 ([1][2][14])

**상태: CONFIRMED**

**근거**: 통계청은 **2025년 10월 1일** 부(처)급 기관인 **국가데이터처**로 개편되면서 주 도메인을 `kostat.go.kr`에서 **`mods.go.kr`**로 변경했다. `mods.go.kr`, `data.mods.go.kr`(통계데이터센터), `mdis.mods.go.kr`(마이크로데이터), `lib1.mods.go.kr`(통계도서관) 등 하위 도메인이 모두 실재한다. MODS = **Ministry of Data and Statistics**. 즉 `mods.go.kr`은 정당한 정부 도메인이며, 이 부분에서 조작된 URL은 없다.

---

## 주장: [1][2][14]의 기관명 "National Data and Statistics Office"

**상태: NEEDS REVIEW — 기관명 부정확 + 시대착오(anachronism)**

**근거**:
1. **공식 영문명이 아니다.** 국가데이터처의 공식 영문 명칭은 **"Ministry of Data and Statistics" (MODS)**이며, 기관 자체 영문 사이트도 이 명칭을 쓴다(약칭 KOSTAT 병용). 일부 언론이 "National Data Agency"로 옮긴 사례는 있으나 "National Data and Statistics Office"는 확인되지 않는 조합이다.
2. **시대착오다.** [1]은 **2024년 12월 9일** 발표 자료인데, 그 시점의 발행 기관은 **통계청(Statistics Korea)**이다. 국가데이터처는 2025년 10월 1일에야 출범했다. 2024년 문서를 2025년에 생긴 기관 이름으로 인용하면 서지적으로 틀린다.

**제안 수정**:
- [1]: `Statistics Korea, "2024 Statistics of One-person Households," 9 December 2024`로 발행 당시 기관명 사용. 필요시 "(now Ministry of Data and Statistics)" 병기.
- [2]: 2026년 2월 자료이므로 `Ministry of Data and Statistics (MODS)`가 맞다.
- [14]: 현재 포털이므로 `Ministry of Data and Statistics`.

---

## 주장: [1] URL `https://mods.go.kr/board.es?mid=a20101000000&bid=11763&...&list_no=438857&ref_bid=`

**상태: NEEDS REVIEW — 이 세션에서 검증 불가 + 구조적으로 깨지기 쉬운 링크**

**근거**:
- `mods.go.kr`이 이그레스 차단되어 직접 응답 확인 불가.
- 검색으로 확인된 **국문판** 「2024 통계로 보는 1인가구」의 실제 주소는 `kostat.go.kr/board.es?mid=a10301010000&bid=10820&list_no=434103`으로, 부록의 `mid`/`bid`/`list_no`와 모두 다르다. 부록의 `mid=a20101000000`은 영문 보도자료 게시판 경로로 보이므로 값이 다른 것 자체는 모순이 아니지만, **일치를 확인하지 못했다.**
- 더 중요한 문제: `board.es?...&list_no=` 형식은 게시판 내부 일련번호에 의존하는 링크이고, **2025년 10월 kostat.go.kr → mods.go.kr 도메인 이전 과정에서 다수 딥링크가 깨진 것으로 보고되어 있다**(기관 스스로 캐시 삭제·대체 도메인 로그인 안내를 냈다).

**제안 수정**: 문서 자체의 존재와 수치는 CONFIRMED이므로 수치를 고칠 필요는 없다. 다만 URL은 production 직전에 반드시 재확인하고, 가능하면 국·영문 양쪽 주소를 병기하거나 KOSIS 통계표 번호를 함께 적을 것.

---

## 주장: [2] URL `https://mods.go.kr/board.es?mid=a20108010000&bid=11773&...&list_no=444910&ref_bid=11742,...`

**상태: NEEDS REVIEW — 위 [1]과 동일 사유**

**근거**: 도메인 차단으로 직접 확인 불가. 검색으로 확인된 국문 보도자료는 `mods.go.kr/board.es?mid=a10301020300&bid=204&list_no=443686`으로 부록의 `list_no=444910`과 다르다(영문판일 가능성). 문서와 수치의 실재는 CONFIRMED이나 URL 자체는 미확인. 또한 `ref_bid=`에 12개 이상의 게시판 ID가 나열된 매우 긴 세션성 파라미터가 붙어 있어 **브라우저 탐색 중 복사한 URL을 그대로 붙여넣은 흔적**으로 보인다. 영구 링크로 부적합하다.

**제안 수정**: `ref_bid` 등 불필요한 쿼리 파라미터를 제거한 최소 URL로 정리하고 접속 확인할 것.

---

## 주장: [3] OECD, "Gender Wage Gap: Definition and Source Dataset." `https://www.oecd.org/en/data/indicators/gender-wage-gap.html`

**상태: CONFIRMED (URL 실재) / NEEDS REVIEW (제목 표기)**

**근거**: 해당 URL은 OECD의 실제 "Gender wage gap" indicator 페이지로 확인된다. 정의 문구도 부록의 서술과 대체로 일치한다(단, 위 A섹션의 self-employed 포함 여부 지적 참조).

**제안 수정**: 제목 "Gender Wage Gap: Definition and Source Dataset"은 OECD 페이지의 실제 제목이 아니라 저자가 붙인 설명으로 보인다. 실제 제목은 "Gender wage gap"이다. 인용 접근일(accessed date)을 함께 적을 것(지표 페이지는 값이 갱신된다).

---

## 주장: [4] OECD, *Education at a Glance 2025: Korea* country note `...education-at-a-glance-2025_1a3543e2-en/korea_252c9ed2-en.html`

**상태: CONFIRMED**

**근거**: 해당 URL 문자열이 OECD 사이트의 실제 한국 국가노트 페이지로 확인되며, 대응하는 PDF(`.../education-at-a-glance-2025-country-notes_9749f4ff/korea_2b3410a2/252c9ed2-en.pdf`)도 존재한다. 부록이 이 문서에서 인용한 "71% of 25-34-year-olds"도 해당 국가노트의 실제 서술과 일치한다.

---

## 주장: [5] OECD, *Inclusive and Sustainable Well-being in Korea*, 2026, chapter on outcomes by gender, age, and education (긴 챕터 URL)

**상태: CONFIRMED**

**근거**: 챕터 URL 슬러그 `ensuring-inclusive-and-sustainable-well-being-for-korean-men-and-women-throughout-their-lives-outcomes-by-gender-age-and-education_23e274c3.html`이 OECD 사이트의 실제 챕터로 문자열까지 정확히 일치 확인된다. 보고서 본체(`a8940343-en`)는 **2026년 4월**, 한국의 OECD 가입 30주년을 계기로 발간된 것으로 확인되므로 "2026" 연도 표기도 맞다. 이 챕터가 성별·연령·교육별 결과를 다룬다는 서술도 정확하며, 앞서 확인한 여성 77%/남성 63% 수치의 출처로 정합적이다.

---

## 주장: [6] Korean Legislation Research Institute, "Civil Act," English reference translation. `https://elaw.klri.re.kr/eng_service/lawView.do?hseq=61788&lang=ENG`

**상태: NEEDS REVIEW**

**근거**: `elaw.klri.re.kr`이 한국법제연구원의 실제 영문 법령 DB(국내 유일의 공식 영문 법령 DB 서비스)라는 점은 CONFIRMED. 그러나 도메인 차단으로 **`hseq=61788`이 실제로 민법(Civil Act)을 가리키는지 확인하지 못했다.**

추가 우려: KLRI의 `hseq`는 **법령의 특정 개정 판본마다 부여되는 일련번호**다. 즉 이 링크는 "현행 민법"이 아니라 "특정 시점 판본의 민법"으로 고정되며, 이후 개정판이 올라오면 독자가 보는 조문이 본문 서술과 어긋날 수 있다. 호주제 관련 조문(제778조 등)은 이미 삭제된 조문이라 판본 문제가 특히 민감하다.

**제안 수정**: 접속 확인 후, 법령명·판본일자·법률번호를 서지에 함께 적을 것. 부록 65행이 이미 "최종판에는 국문 법령 원문을 병기해야 한다"고 스스로 인정한 항목이므로, 그 지적은 타당하며 반드시 이행할 것.

---

## 주장: [7] NHRC, "The Hoju System is Unconstitutional and a Violation of Human Rights," 11 March 2003 (`humanrights.go.kr/site/program/board/basicboard/view?currentpage=46&...&boardid=7000525`)

**상태: NEEDS REVIEW — 문서는 실재, URL 형식은 구식/취약, 날짜 미확인**

**근거**:
1. **문서 실재는 CONFIRMED.** 국가인권위원회 보도자료 「호주제는 위헌이며 인권침해 제도」가 실재한다. 2003년 1월 한국가정법률상담소의 요청과 헌재 계류 사건을 계기로 인권위가 헌재에 의견을 제출하기로 결정한 사안이며, 부록의 영문 제목은 국문 제목의 정확한 번역이다. 내용(호주 중심 가족 종속, 가족 위계, 혼인·이혼 시 가족구성 자유 제한, 부계 우선 승계에 따른 여성 권리 침해)도 부록의 "human-rights objections raised against the Hoju system"이라는 요약과 부합한다.
2. **URL은 구식이다.** 현재 인권위 사이트의 해당 자료 주소는 `humanrights.go.kr/base/board/read?boardManagementNo=24&boardNo=554553` 형식이다. 부록의 `/site/program/board/basicboard/view?...&boardid=7000525`는 이전 CMS 형식이며, 링크 생존이 의심된다.
3. **`currentpage=46`이라는 페이지네이션 파라미터가 박혀 있다.** 게시물이 추가되면 페이지 번호가 밀리므로 영구 링크로 부적합하다. [2]와 마찬가지로 브라우징 중 URL을 그대로 복사한 흔적이다.
4. **발표일 "11 March 2003"을 독립 확인하지 못했다.**

**제안 수정**: 현행 `boardNo=554553` 형식 주소로 교체하고, 게시일자를 원문에서 직접 확인해 확정할 것.

---

## 주장: [8] KWDI, "Rise of Single-person Households and Direction for Family Policy." `https://eng.kwdi.re.kr/inc/download.do?ut=A&upIdx=102029&no=1`

**상태: NEEDS REVIEW (URL 실재 확인, 서지 불충분, 본문 미인용)**

**근거**: 해당 URL 문자열과 제목이 한국여성정책연구원(KWDI) 영문 사이트의 실제 다운로드 링크로 확인된다. 그러나 (1) 저자·발행연도·보고서 번호가 전혀 없고, (2) `download.do?upIdx=` 형식의 **직접 다운로드 링크**라 랜딩 페이지가 아니며 파일 인덱스 변경 시 깨진다. (3) **이 참고문헌은 부록 본문에서도, 다른 어떤 챕터에서도 인용되지 않는다**(아래 D2 참조).

**제안 수정**: 저자·발행연도 보완 후 랜딩 페이지 URL로 교체. 실제로 어느 챕터의 어느 주장을 뒷받침하는지 명확히 하거나, 근거가 없다면 목록에서 제외.

---

## 주장: [9] Kim, M. S., "Rites and Rights: Lineage Property and Law in Korea," **Acta Koreana** / OpenEdition, 2020. `https://journals.openedition.org/acrh/11667`

**상태: NEEDS REVIEW — URL·제목·저자는 정확하나, 게재 학술지명이 틀렸다**

**근거**:
- URL과 논문 제목은 **정확히 실재한다.** 저자는 **Marie Seong-Hak Kim**으로 "Kim, M. S."와 일치. 2020년 11월 발표도 일치.
- 그러나 게재지는 ***Acta Koreana*가 아니다.** 이 논문은 OpenEdition에 실린 ***L'Atelier du Centre de recherches historiques* (ACRH)**에 게재되었다(DOI 10.4000/acrh.11667). URL 경로의 `acrh`가 곧 학술지 코드다. *Acta Koreana*는 계명대 한국학연구원 발행 저널로 OpenEdition에 없다. **저자가 URL 경로의 `acrh`를 "Acta Koreana"의 약자로 오독했을 가능성이 높다.**
- 내용 정합성은 좋다: 이 논문은 조선의 유교 제사 승계가 재산 승계를 종속시킨 구조, 식민지기 제사상속 폐지와 근대 민법 편입, 1958년 민법에 남은 유교적 요소를 다루므로 이 책의 챕터 1~3 논지와 직접 연결된다.

**제안 수정**: `Kim, Marie Seong-Hak. "Rites and Rights: Lineage Property and Law in Korea." *L'Atelier du Centre de recherches historiques*, November 2020. DOI: 10.4000/acrh.11667.`

---

## 주장: [10] SAGE Journals, "The Impacts of Birth Order and Social Status on the Genealogy Register," 2010. `https://journals.sagepub.com/doi/10.1177/0363199009357158`

**상태: NEEDS REVIEW — URL·연도는 정확, 서지정보가 불완전/부정확**

**근거**:
- DOI 10.1177/0363199009357158은 실재하며 **Sangkuk Lee, "The Impacts of Birth Order and Social Status on the Genealogy Register **in Thirteenth- to Fifteenth-Century Korea**," *Journal of Family History* 35(2), 2010, pp. 115–127**이다. 연도 2010 일치.
- 문제 1: **제목이 잘렸다.** 시기 한정구("in Thirteenth- to Fifteenth-Century Korea")가 빠졌는데, 이 책이 고려~조선 초기 논의에 쓰는 자료인 만큼 **시기 정보야말로 빠뜨리면 안 되는 부분**이다.
- 문제 2: **"SAGE Journals"는 학술지명이 아니라 출판 플랫폼명이다.** 실제 저널은 *Journal of Family History*.
- 문제 3: **저자명이 없다.**

**제안 수정**: `Lee, Sangkuk. "The Impacts of Birth Order and Social Status on the Genealogy Register in Thirteenth- to Fifteenth-Century Korea." *Journal of Family History* 35, no. 2 (2010): 115–127.`

---

## 주장: [11] Korean Journal of Historical Studies, "research on equal inheritance and Joseon-period family/property history." `https://journal.kci.go.kr/hksh/archive/articleView?artiId=ART001482849`

**상태: NEEDS REVIEW — URL은 실재하나, 인용 설명과 실제 논문의 시기가 어긋난다 (이 부록에서 가장 실질적인 서지 문제)**

**근거**:
- URL은 실재하며 `artiId=ART001482849`는 **김경숙, "조선후기 光州 全義李氏家의 재산상속" (The property inheritance practices of the Jeon'eui Yi Family of the Gwangju area during the latter half period of the Joseon dynasty), 2010**로 확인된다.
- **핵심 문제: 시기 불일치.** 부록 63행은 [15][16]과 함께 "early Joseon inheritance"와 "equal or partible inheritance practices"를 뒷받침하는 자료군을 제시하는 맥락에 있는데, 이 논문은 제목부터 **조선 후기(latter half period)** 한 가문의 재산상속 사례연구다. 조선 후기는 균분상속이 **해체되고 장자 우대로 전환된** 시기다. 즉 이 논문은 "초기 조선의 균분상속"을 입증하는 자료로 쓰기에 부적절하거나, 최소한 **정반대 방향의 변화를 보여주는 자료**다. 부록이 붙인 라벨("research on equal inheritance")이 실제 논문 내용과 일치하지 않는다.
- 부차 문제: 학술지명을 "Korean Journal of Historical Studies"로 적었으나 URL의 저널 코드는 `hksh`이며, 검색 결과는 이 논문의 게재지를 "The Review of Korean History" 99집(pp. 111–146)으로 표시한다. **부록의 영문 저널명이 실제 저널과 일치하는지 확인되지 않는다.** 저자명·발행연도·권호도 전혀 없다.

**제안 수정**: (1) 저자(김경숙)·연도(2010)·저널명·권호·쪽수를 정확히 보완할 것. (2) 더 중요하게, **이 논문을 "균분상속의 근거"로 인용하는 것이 맞는지 Writer/Researcher가 재판단할 것.** 초기 조선 균분상속을 입증하려면 『경국대전』 형전 사천조의 자녀 균분 규정, 15~16세기 분재기(화회문기·별급문기) 연구를 직접 인용해야 한다. 참고로 00-brief.md는 조사 범위에 "1566년 화회문기(이이/신사임당 가문)"를 명시했는데, **부록 참고문헌 [1]~[16] 어디에도 이를 뒷받침하는 출처가 없다**(D3 참조).

---

## 주장: [12] OECD, *Inclusive and Sustainable Well-being in Korea*, 2026. `...a8940343-en.html`

**상태: CONFIRMED**

**근거**: 보고서 랜딩 페이지 URL이 실재 확인된다. 정식 제목은 *Inclusive and Sustainable Well-being in Korea: 30 Years of OECD Membership and Future Policy Opportunities*, 2026년 4월 발간. 연도 표기 정확.

**제안 수정**: [5]와 [12]는 같은 보고서의 챕터/본체 중복 인용이다. 통합하거나 "[12], ch. X"처럼 종속 인용으로 정리 권고(서지 정확성 문제는 아님).

---

## 주장: [13] OECD, *Education at a Glance 2025*. `https://www.oecd.org/en/publications/2025/09/education-at-a-glance-2025_c58fc9ae.html`

**상태: NEEDS REVIEW**

**근거**: *Education at a Glance 2025*가 2025년 9월 발간된 실재 보고서라는 점은 CONFIRMED이며, `oecd.org/en/publications/<YYYY>/<MM>/...` 형식도 OECD의 실제 URL 패턴이다. 다만 검색으로 확인된 본체 landing은 `oecd.org/en/publications/education-at-a-glance-2025_1c0d9c79-en...` 계열이라 **부록의 DOI 접미사 `c58fc9ae`와 다르다.** 도메인 차단으로 어느 쪽이 유효한지 확정하지 못했다. (OECD는 같은 간행물에 대해 복수의 landing URL을 운용하므로 둘 다 유효할 수 있다.)

**제안 수정**: 접속 확인 필요. [4]와 [13]도 같은 간행물(국가노트 vs 본체)의 중복 인용이므로 정리 권고.

---

## 주장: [14] Statistics Korea / National Data and Statistics Office, Population and Household Statistics portal. `https://mods.go.kr/menu.es?mid=a20108000000`

**상태: NEEDS REVIEW**

**근거**: 도메인은 실재(CONFIRMED)하나 해당 `mid` 경로가 인구·가구 통계 포털인지 확인 불가(이그레스 차단). 또한 기관명 병기 방식("Statistics Korea / National Data and Statistics Office")이 [1][2]와 불일치하며, 후자는 공식 영문명이 아니다(위 참조). 이 항목 역시 본문에서 인용되지 않는다.

---

## 주장: [15] National Library of Korea, "Having a Glimpse of the Lives of Women in the Past." `https://www.nl.go.kr/EN/contents/EN32701000000.do`

**상태: CONFIRMED (URL 실재) / NEEDS REVIEW (증거력)**

**근거**:
- URL이 국립중앙도서관 영문 사이트의 실제 디지털 컬렉션 페이지로 **정확히 일치 확인**된다: "National Library of Korea > Collection > Digital Collection > Having a glimpse of the lives of women in the past > Introduction".
- 내용도 부록의 사용 취지와 부합한다: 조선시대 여성의 지위를 남성 중심 사회라는 통념만으로 보는 것을 경계하고, 딸·과부에 대한 사회적 배려를 보여주는 자료를 제시한다 — 부록 63행의 "historical variation and gradual transformation, not ... socially egalitarian"이라는 신중한 서술과 방향이 맞다.
- **증거력 문제**: 이는 도서관 디지털 컬렉션 **소개 페이지**이지 심사를 거친 학술 연구가 아니다. "초기 족보에 딸의 후손이 포함되었다"는 구체적 사료적 주장을 단독으로 지탱하기엔 약하다.

**제안 수정**: 유지하되, 균분상속/자녀안·족보 등재 관련 학술 논문을 최소 1편 보강할 것.

---

## 주장: [16] Korean Genealogy Research, "The Historical Background of the Popularity of Genealogies in Korea." `https://journals.sagepub.com/doi/abs/10.1177/0363199020928364`

**상태: NEEDS REVIEW — URL·제목은 정확, 학술지명이 실재하지 않는 명칭이다**

**근거**:
- DOI 10.1177/0363199020928364는 실재하며 **Sangwoo Han, "The Historical Background of the Popularity of Genealogies in Korea," *Journal of Family History*, 2020**으로 확인된다. URL·제목·연도 일치.
- **"Korean Genealogy Research"는 학술지명이 아니다.** [10]에서 플랫폼명("SAGE Journals")을 저널명 자리에 넣은 것과 같은 유형의 오류이되, 이쪽은 아예 **존재하지 않는 저널명을 만들어 넣은** 형태라 더 나쁘다. 실제 저널은 [10]과 동일한 *Journal of Family History*다.
- 내용 적합성 주의: 이 논문은 **족보가 왜 대중화되었는가**(주로 조선 후기~근대의 족보 확산)를 다루므로, 부록 63행이 이를 "초기 족보에 딸의 후손이 포함되었다"는 주장의 근거로 쓰는 것이 정확한지 재확인이 필요하다. [11]과 동일한 유형의 시기 정합성 문제일 수 있다.

**제안 수정**: `Han, Sangwoo. "The Historical Background of the Popularity of Genealogies in Korea." *Journal of Family History* (2020). DOI: 10.1177/0363199020928364.` 및 해당 논문이 실제로 뒷받침하는 주장 범위 재확인.

---

# D. 원고 구조 / 각주 체계 검증

## 주장(암묵): "이 책은 각주가 달린 원고다" (00-brief.md 판매 포인트: "이미 각주/출처가 달린 통계·법조문 인용 수준이 높아 신뢰도 있는 심층 콘텐츠로 차별화 가능")

**상태: UNSUPPORTED**

**근거**: `02-chapters/` 전체를 대상으로 각주 마커 `[숫자]`를 전수 검색한 결과, **마커 25개가 전부 `08-appendix-statistical-references.md` 한 파일 안에만 존재한다.** `00-introduction.md`, `01-confucian-foundation.md`, `02-colonial-disruption.md`, `03-hoju-system.md`, `04-women-workforce.md`, `05-demographic-implosion.md`, `06-generational-fractures.md`, `07-epilogue.md` — **여덟 개 챕터 모두 인라인 각주가 0개다.**

동시에 이 챕터들은 검증 대상 수치를 그대로 서술하고 있다:
- `05-demographic-implosion.md:31` — "TFR that dropped to 0.72 in 2023 (rising modestly to 0.75 in 2024 and about 0.8 in 2025)" (각주 없음)
- `04-women-workforce.md:3` — "the tertiary education attainment rate for young women aged 25 to 34 exceeded 75%" (각주 없음)
- `04-women-workforce.md:7` — "an OECD-leading gender wage gap of approximately 29% (2023-2024)" (각주 없음)
- `07-epilogue.md:11` — "0.72 in 2023 ... 0.75 in 2024 ... about 0.8 in 2025, a gender wage gap of about 29%" (각주 없음)

즉 **부록이 이 책 전체 사실검증의 기반 파일이라는 전제 자체가 현재 원고에서는 기능하지 않는다.** 부록은 독립된 참고문헌 목록으로 존재할 뿐, 본문의 어떤 주장과도 기계적으로 연결되어 있지 않다.

**제안 수정**: Writer 단계로 되돌려 본문 정량 주장마다 각주 마커를 삽입할 것. 이것은 Editor의 문장 다듬기로 해결되지 않는다.

---

## 주장(암묵): 참고문헌 [1]~[16]이 모두 실제로 인용된 자료다

**상태: UNSUPPORTED (고아 참고문헌 7건)**

**근거**: 부록 본문에서 실제로 호출되는 각주는 [1][2][3][4][5][6][7][15][16] 9건뿐이다. **[8], [9]는 본문 인용이 있으나([9]는 없음 — 재확인 결과 [9]도 미인용), 정확히는 [8], [9], [10], [11], [12], [13], [14] 7건이 어디에서도 인용되지 않는다.** ([9][10][11]은 63행이 "[15] [16]"만 호출하므로 인용되지 않는다.)

챕터에도 각주가 없으므로(D1), 이 7건은 **책 전체에서 단 한 번도 호출되지 않는 고아 항목**이다.

**제안 수정**: 각 항목이 어떤 주장을 뒷받침하는지 본문에 연결하거나, 연결되지 않으면 "Further reading"으로 섹션을 분리해 참고문헌과 구분할 것. 인용되지 않은 항목을 References로 제시하는 것은 출처가 있는 것처럼 보이게 하는 효과가 있어 그대로 두기 어렵다.

---

## 주장(암묵): 부록이 이 책의 역사 파트 주장을 뒷받침한다

**상태: UNSUPPORTED (역사 파트 출처 공백)**

**근거**: 00-brief.md는 조사 범위로 "고려~조선 초기 균분상속(경국대전), 1566년 화회문기(이이/신사임당 가문), 서류부가혼, 윤회봉사"를 명시한다. 그러나 부록의 [1]~[16] 중 **경국대전, 1566년 화회문기, 서류부가혼(壻留婦家婚), 윤회봉사(輪回奉祀) 중 어느 것도 직접 뒷받침하는 출처가 없다.** 역사 관련 참고문헌은 [9](조선~근대 종중재산과 법), [10](13~15세기 족보 등재와 출생순위), [11](조선 **후기** 한 가문 재산상속), [15](도서관 전시 소개), [16](족보 대중화 배경) 5건인데, 이 중 브리프가 지목한 4개 항목을 정면으로 다루는 것은 없다.

특히 화회문기 같은 **구체적 연도·문서명이 붙은 사료 주장**(1566년)은 출처 없이 서술될 경우 검증 불가능한 주장이 된다.

**제안 수정**: Researcher 단계로 되돌려 역사 파트 1차/2차 출처를 보강할 것. 최소한 (1) 『경국대전』 형전 사천조 자녀 균분 규정, (2) 1566년 이이 남매 화회문기(분재기) 관련 연구, (3) 윤회봉사·서류부가혼에 관한 한국사 연구를 각각 확보해야 한다. **본 검증에서는 해당 사료 주장들 자체를 검증하지 않았다** — 부록에 출처가 없어 검증할 대상이 없었기 때문이다(해당 챕터 담당 서브에이전트의 검증 결과와 대조 필요).

---

## 주장: 챕터 04의 "Throughout the 2010s and 2020s, the tertiary education attainment rate for young women aged 25 to 34 exceeded 75%"

**상태: NEEDS REVIEW (부록보다 강한 주장 — 교차 플래그)**

**근거**: 부록은 시기 한정 없이 "Exceeds 75%"라고만 하는데, 챕터 04는 이를 **"2010년대와 2020년대 내내(throughout)"**로 확장했다. 확인된 시계열 값은 1997년 27%, 2005년 남녀 51% 동률, 2006년 여성 추월, **2023년 77%**다. **2010년대 초반 값을 확인하지 못했고**, 2005년 51%에서 2023년 77%로 상승한 궤적을 고려하면 2010년대 초반에 이미 75%를 넘었을 가능성은 낮아 보인다. 확정적으로 틀렸다고 말할 근거는 없으나, **현재 확보된 근거로는 "throughout the 2010s"를 뒷받침할 수 없다.**

**제안 수정**: OECD Education at a Glance 연도별 성별 이수율 시계열을 확인해 실제로 75%를 넘긴 최초 연도를 특정하고, 그 전까지는 "by the early 2020s" 같은 안전한 표현으로 후퇴할 것. 부록 자신이 요구하는 "reference year 병기" 원칙을 챕터 04에도 적용해야 한다.

---

# E. 최종 판정 및 다음 단계 권고

## 잘 되어 있는 부분 (그대로 유지 권고)

- **핵심 통계 수치의 정확도가 높다.** TFR 0.72/0.75/0.80, 임금격차 29.3%(2023)·34.1%(2018)·OECD 1위, 1인가구 782.9만·35.5%, 2025년 출생아 254,500명·+6.8% — 전부 원자료와 일치한다. 반올림·근사 표현도 과장 없이 보수적이다.
- **부록의 자기 경고(71% vs 75%+)는 타당하다.** 검증 결과 두 수치는 모순이 아니라 성별 분리/미분리의 차이이며, 부록의 방법론적 지적이 정확했다. 이 경고는 **유지되어야 한다.**
- **"updates를 historical chart에 섞지 말라", "year/unit/denominator/URL을 명시하라"는 편집 원칙**도 정당하다. 다만 부록 자신이 몇 군데에서 이 원칙을 지키지 않았다(8행 기준연도 누락, 10행 denominator를 "residential units"로 오기).
- **법령/판례의 날짜는 4건 중 4건 모두 정확하다.** 1958.2.22/1960.1.1, 2005.2.3, 2007.5.17/2008.1.1, 2007.4.27/2008.7.1.

## 되돌림 권고: **Editor로 넘기지 말고 Writer/Researcher로 되돌릴 것**

우선순위 순:

1. **[필수·확정 오류] 노인장기요양보험법 "Law No. 8402" → "Law No. 8403"** 수정.
2. **[필수·구조] 본문 챕터 8개에 각주 마커가 0개.** Writer가 정량 주장마다 [n]을 삽입해야 한다. 이 책의 핵심 판매 포인트가 여기 걸려 있다.
3. **[필수·서지] [9] 학술지명 오류(Acta Koreana → L'Atelier du CRH), [16] 존재하지 않는 학술지명("Korean Genealogy Research" → Journal of Family History), [10] 제목 절단 및 플랫폼명을 저널명으로 표기.** 세 건 모두 URL은 맞고 서지 라벨이 틀린 유형이다.
4. **[필수·내용] [11]의 시기 불일치.** 조선 후기 사례연구를 초기 조선 균분상속의 근거로 쓰는 것은 부적절하다. Researcher 재작업 필요.
5. **[필수·공백] 역사 파트 출처 공백** (경국대전·1566년 화회문기·서류부가혼·윤회봉사). Researcher 단계.
6. **[권고] 용어 수정**: "residential units" → "households"; "still the highest" → "still the highest in the OECD"; 임금격차 정의에 self-employed 포함; "Original codification of the Hoju system" 한정; 2005년 결정에 민법 제826조 제3항 추가.
7. **[권고] 기관명 정정**: "National Data and Statistics Office" → 2024년 자료는 "Statistics Korea", 2025년 10월 이후 자료는 "Ministry of Data and Statistics (MODS)".
8. **[production 전 필수] 링크 전수 점검.** 이 세션에서 8개 도메인이 이그레스 차단되어 최종 확인이 불가능했다. 특히 `list_no=` / `currentpage=` / `download.do?upIdx=` 형식의 링크 5건([1][2][7][8] 및 [14])은 구조적으로 깨지기 쉬우므로 안정적 URL로 교체할 것.

## 검증하지 않은 항목

- Figure register 표(Figure 1~14) — 지시에 따라 제외.
- 다른 챕터 본문의 개별 주장 — 각 챕터 담당 서브에이전트 소관. 단 D4(챕터 04의 "throughout the 2010s")와 A/B 섹션의 수치·법령은 챕터 04·05·07에도 그대로 등장하므로, 본 리포트의 판정을 해당 챕터 리포트와 대조할 것.
