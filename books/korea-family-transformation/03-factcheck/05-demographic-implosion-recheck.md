# Fact Check Recheck — Chapter 5: Demographic Implosion (Gap-Fill Additions Only)

- 검증 대상: `02-chapters/05-demographic-implosion.md` — `01-research/05-demographic-implosion-gapfill.md` 반영 이후 **새로 추가된 6개 항목만** 재검증
- 대조 자료: 위 gapfill 리서치 문서(자체적으로 "검색엔진 요약 기반, 1차 출처 URL 직접 열람 불가"라고 명시) + 이번 세션에서 독립적으로 재수행한 웹 검색
- 검증 수행일: 2026-08-31
- 방법: gapfill 문서가 인용한 각 수치를 최소 2회 이상의 독립 검색으로 재교차검증했다. 정부 1차 출처 도메인(kostat.go.kr, mods.go.kr, molit.go.kr, mohw.go.kr, kihasa.re.kr 등)과 다수 언론사 도메인(WebFetch)이 이번 세션에서도 egress 프록시에 의해 차단되어, **검증은 gapfill 문서와 동일하게 검색엔진 요약 교차대조 방식에 의존했다.** 이는 gapfill 리서치보다 신뢰도를 높이는 절차이긴 하나(별도 세션, 별도 검색으로 재현), 1차 출처 원문 대조는 여전히 이루어지지 못했다는 한계가 있다.
- 요약: **CONFIRMED 대부분 / NEEDS REVIEW 2건(그중 1건은 명백한 오류) / UNSUPPORTED 0건**

> **가장 중요한 발견 (먼저 읽을 것)**
> 항목 3(결혼비용 분담)에서 **챕터 본문의 연도 라벨이 틀렸다.** 본문은 "58.8:41.2 split recorded in **the 2024 edition** of the same survey"라고 쓰고 있는데, 독립 검색으로 재구성한 결과 그 58.8:41.2·3억6173만원 수치는 **2025년 3월 발표본**(2024년 11월 조사)이다. "2024 edition"이라 부를 수 있는 실제 보고서(2024년 2월 발표, 조사기간 미상)는 총액 2억9748만원·분담률 61.7:38.3으로 **전혀 다른 수치**다. 아래 항목 3에서 상세 근거와 수정안을 제시한다.

---

## 항목 1. 주거비 / PIR 수치

### 주장: "the price-to-income ratio (PIR) for owner-occupier households in Seoul ... stood at 13.9 in 2024, up from 13.0 in 2023 after peaking at 15.2 in 2022; the nationwide owner-occupier PIR ... was a flat 6.3."
상태: **CONFIRMED**
근거: 국토교통부 「2024년도 주거실태조사」(2025-11-16 발표, 전국 61,000가구) 관련 독립 검색 2건(한국일보 2025-11-16, 경기일보 2025-11-16 등)에서 서울 자가가구 PIR 13.9배, 그 다음으로 세종 8.2배·경기 6.9배·대구 6.7배·인천 6.6배 순으로 확인되어 "전국은 6.3배(더 낮음)"라는 본문 서술과도 방향이 일치한다(세종·경기 등 개별 시도가 전국 평균보다 높게 나오는 것은 전국 평균에 저PIR 지방이 다수 포함되기 때문이며 모순이 아니다). PIR 정의(자가가구 한정, 무주택자 진입장벽을 과소평가한다는 지적)도 gapfill 서술과 일치.
제안 수정: 없음.

### 주장: "the average time required to reach first-home ownership had reached 7.9 years, the longest on record."
상태: **CONFIRMED**
근거: 독립 검색(세정신문, 한국일보, 프리진뉴스 등 복수) 모두 "생애최초 주택마련 소요연수 7.9년, 2019년 6.9년 대비 약 2개월 증가, 역대 최장"으로 일치. 자가보유율 61.4%(+0.7%p), 자가점유율 58.4%(+1.0%p)도 본문·gapfill과 일치.
제안 수정: 없음.

### 주장: "households headed by someone aged 39 or under were the only age group nationwide to see net assets contract over the preceding year, even as every other age bracket added wealth."
상태: **NEEDS REVIEW (방향은 맞으나 "순자산" 용어의 정밀도 미확인)**
근거: 「2025년 가계금융복지조사」(2025년 3월 말 기준) 관련 독립 검색에서 "39세 이하 가구만 유일하게 자산(資産) 0.3% 감소, 나머지 전 연령대는 증가"라는 서술은 다수 출처에서 반복 확인된다. 다만 이 표현들 대부분은 "자산"(총자산, gross assets)이라고만 하고, 본문이 쓰는 "net assets"(순자산 = 자산 − 부채)와 정확히 같은 지표인지는 검색 요약만으로 완전히 특정되지 않았다. 다만 그 하위 집단인 "30대"에 대해서는 한 출처가 명시적으로 "순자산은 2억5060만원으로 1.3% 줄었다"고 밝히고 있어, 30대 단위에서는 순자산 감소가 맞다. "39세 이하"라는 공식 구간 전체에 대해 통계청/국가데이터처 원표가 "순자산" 항목으로 감소를 보고했는지는 정부 도메인 차단으로 원표 대조가 불가능했다.
제안 수정: 최종판 제작 전, 국가데이터처 「2025년 가계금융복지조사」 원표(연령대별 순자산 증감표)를 직접 열람해 "net assets"가 정확한 용어인지 확인할 것. 확인 전까지는 "net assets"를 "assets"로 완화하거나, 확실히 검증된 "30대"만 특정해 "net assets among households in their 30s" 식으로 좁히는 것이 더 안전하다.

### 주장 (KB PIR 비교): "Commercial indices ... such as KB Kookmin Bank's PIR series, report a somewhat lower ratio of roughly 10.2–10.5 for the same period"
상태: **CONFIRMED**
근거: KB부동산 데이터허브 관련 검색 결과, 2026년 1분기 기준 서울 KB아파트담보대출 PIR 10.2, 3분위(중산층) 기준 매칭 PIR 10.5로 나타나 gapfill·본문의 수치 범위와 일치. 국토부 PIR(전체 주택·자가가구 전수)과 KB PIR(아파트 담보대출 실행자 기준)의 모집단 차이로 인한 괴리라는 설명도 타당.
제안 수정: 없음.

---

## 항목 2. 대·중소기업 임금격차 수치

### 주장: "the average monthly pre-tax income at large enterprises at 6.13 million won in 2024, against 3.07 million won at ... SMEs ... 50.1% ... essentially unchanged from 50.3% in 2023 (5.93 million versus 2.98 million won)."
상태: **CONFIRMED**
근거: 2024년분(2026-02-23 발표) 관련 독립 검색 3건(머니투데이, 한국경제, 서울경제) 모두 대기업 613만원 / 중소기업 307만원 / 전체 평균 375만원으로 일치하며, 격차가 "전년(295만원) 대비 11만원 확대되어 306만원"이라는 서술은 613−307=306과 정확히 부합한다. 2023년분(2025-02-25 발표)도 별도 검색(뉴스핌 계열)에서 대기업 593만원 / 중소기업 298만원으로 확인되어, 298/593=50.25%(반올림 50.3%), 307/613=50.08%(반올림 50.1%) 모두 산술이 맞다.
제안 수정: 없음.

### 주장: "The same gap holds using median rather than mean income: 5.11 million won at large enterprises versus 2.55 million won at SMEs, exactly double."
상태: **CONFIRMED**
근거: 2024년분 중위소득 관련 독립 검색(스레드/언론 요약)에서 "중위소득도 대기업 511만 원 vs 중소기업 255만 원"으로 명시적으로 확인됨. 511/255=2.004로 "exactly double"이라는 표현이 반올림상 타당함(511=255×2+1이므로 엄밀히는 2.004배지만, 공식 발표 자료 자체가 이를 "2배 이상"으로 요약하고 있어 오독 소지는 낮다).
제안 수정: 없음. 다만 문체적으로 "exactly double"보다 "roughly double" 또는 "just over double"이 더 엄밀하지만, 사실관계상 문제는 아니다.

---

## 항목 3. 결혼비용 분담 조사 (Duo 설문)

### 주장: "A 2026 survey of 1,000 recently married couples by ... Duo ... found that grooms bore 59.4% ... and brides 40.6% ... Housing accounted for 84.5% of the average total cost of 381.13 million won."
상태: **CONFIRMED**
근거: 독립 검색 다수(비즈니스코리아, 매거진한경, 아주경제, 뉴스1/네이트 등)에서 2026년 3월 발표 「2026 결혼비용 실태 보고서」(신혼부부 1,000명, 남녀 각 500명) 관련 수치가 반복 확인됨: 총액 3억8113만원, 주택 3억2201만원(=84.49%≈84.5%), 부담률 신랑 59.4%(2억2635만원) : 신부 40.6%(1억5478만원). 주택 항목 단독 부담률은 남 62.5% : 여 37.5%로 별도 확인됨(본문에는 이 세부치는 없음, 문제 아님).
제안 수정: 없음.

### 주장: "essentially unchanged from, and if anything slightly more skewed than, the 58.8:41.2 split recorded in **the 2024 edition** of the same survey."
상태: **NEEDS REVIEW — 사실상 오류. 연도 라벨을 정정해야 한다.**
근거: 독립 검색으로 듀오의 최근 3개 보고서를 시계열로 재구성하면 다음과 같다.
| 발표 시점 | 조사 대상 결혼 시점 | 총 결혼비용 | 신랑:신부 부담률 |
|---|---|---|---|
| **2024년 2월** 발표 | (2024년 2월 기사 기준 "2024 총 결혼 예상 비용") | 2억9748만원 | **61.7% : 38.3%** |
| **2025년 3월** 발표 (조사기간 2024-11-12~25) | 최근 2년 이내 결혼 | 3억6173만원 | **58.8% : 41.2%** |
| **2026년 3월** 발표("2026 결혼비용 실태 보고서") | 최근 2년 이내 결혼 | 3억8113만원 | **59.4% : 40.6%** |
전년 대비 증가율 기사("전년 대비 21.6% 증가", 2.9748억×1.216≈3.618억)가 2025년 3월 발표분과 2024년 2월 발표분을 명시적으로 연결하고 있어, 이 세 개 보고서가 서로 다른 3개 연도의 별개 조사라는 점은 확실하다. 즉 **58.8:41.2 수치는 "2024 edition"이 아니라 2025년(3월) 발표본**이며, 실제 "2024 edition"이라 부를 수 있는 보고서의 분담률은 61.7:38.3으로 본문에 전혀 등장하지 않는 다른 값이다. gapfill 리서치 문서 자체가 이미 이 수치를 "2024년 보고서 기준"이라고 잘못 라벨링했고(가pfill 문서 125행), 챕터가 이를 그대로 이어받아 오류가 전파되었다.
제안 수정:
- 본문 "the 2024 edition of the same survey" → **"the survey released in March 2025"** 또는 **"Duo's prior-year report (published 2025)"**로 수정.
- 만약 진짜 "2024년 발표본"(61.7:38.3, 총액 2.9748억)과 비교하고 싶다면, 그 경우 "59.4% versus 61.7% two years earlier" 식으로 다른 문장을 새로 써야 하며, 현재처럼 58.8:41.2와 섞어 쓰면 안 된다.
- 참고: 어느 쪽으로 비교하더라도 "신랑 부담이 완화되지 않았다"는 gapfill의 핵심 결론(항목 3의 본문 수정 제안)은 그대로 유지된다 — 61.7%(2024)→58.8%(2025)→59.4%(2026)는 등락은 있지만 어느 해든 신랑이 약 6:4로 더 부담하는 구조가 3년 연속 유지된다.

### 주장 (KIHASA 연구): "79.0% of brides received no parental financial support toward the newlywed home, compared with only 42.3% of grooms, and grooms' own personal financial contribution ran roughly three times higher than brides'."
상태: **CONFIRMED**
근거: 독립 검색에서 한국보건사회연구원 연구보고서(수시 2020-08, 최선영 외, 2012.8~2019.7 결혼 1,779가구)가 확인되며, "남편 측 부모 지원 없음 42.3%, 결혼 당사자 기여도는 남편이 부인의 약 3배"라는 서술이 별도 매체(다음뉴스 "[단독]" 기사)에서도 재확인된다. 신혼집 마련 비용 평균은 검색 요약마다 "1억9292만원"·"약 1억9000만원"·gapfill의 "약 1억9500만원"으로 근소하게(200만~500만원, 반올림 수준) 다르게 인용되나 이는 자릿수 반올림 차이로 보이며 본문에는 이 총액 자체가 직접 인용되지 않으므로 실질적 문제는 아니다.
제안 수정: 없음. 다만 본문·부록에 KIHASA 조사의 원 총액 수치를 넣을 계획이 있다면 "약 1억9,300만원(2015년 불변가격)" 정도로 통일해 반올림 오차를 줄일 것.

---

## 항목 4. 1인 외식 인프라 관련 통계

### 주장: "single-person households devote 18.2% of their monthly consumption spending to food and accommodation ... a larger share ... than the 13.6% they spend on groceries ... their total monthly consumption spending (1.689 million won in 2024) is only 58.4% of the all-household average"
상태: **CONFIRMED**
근거: 독립 검색 2건(페이스북 공식 계정 인용 및 별도 요약)에서 국가데이터처 「2025 통계로 보는 1인가구」(2025-12-09 발표, 2024년 기준) 수치가 정확히 일치: 1인가구 월평균 소비지출 168만9천원(전체 가구 289만원의 58.4%), 지출 구성비 주거·수도·광열 18.4%, 음식·숙박 18.2%, 식료품·비주류음료 13.6%. 부가로 1인가구 804만5천 가구(36.1%), 연간소득 3,423만원(전체 가구의 46.1%)도 확인됨(본문에는 미인용, 참고용).
제안 수정: 없음.

### 주장 (관찰 서술): "an observation of the contemporary restaurant landscape rather than a claim drawn from a specific survey of restaurant design"
상태: **적절히 처리됨 — 별도 태깅 불필요**
근거: 본문이 이미 "1인석 칸막이·키오스크·1인용 화로구이" 묘사를 특정 통계에 근거한 것이 아니라 저자의 관찰임을 스스로 명시하고 있어, gapfill이 우려한 "출처 없는 인프라 묘사" 문제는 이번 개정에서 적절히 완화되었다. 통계(18.2%)와 관찰(인프라 묘사)이 서로 다른 근거 층위임을 문장 구조상 구분하고 있다.
제안 수정: 없음.

---

## 항목 5. 노인 사적이전소득 시계열

### 주장: "private transfers made up 46.5% of older people's household income in 2008, falling to 22.0% in 2017, 13.9% in 2020, and 8.0% in 2023, while earned and business income remained the largest single component at 53.8% and public transfers accounted for 25.9% in 2023."
상태: **CONFIRMED (2023년 구성비) / NEEDS REVIEW (2008·2017·2020 값과의 기준 일관성 미확인)**
근거: 2023년 수치(근로·사업소득 53.8%, 공적이전 25.9%, 사적이전 8.0%, 재산소득 6.7%)는 독립 검색에서 "2008년 대비 사적이전소득 비중이 큰 폭으로 감소하는 특징"이라는 보건복지부 보도자료 표현과 함께 정확히 재확인됨. 그러나 46.5%(2008)→22.0%(2017)→13.9%(2020)이라는 앞선 세 시점의 수치는, gapfill 문서 자신이 이미 "노인실태조사는 개인소득 구성과 가구소득 구성을 별도로 보고하며, 2020년 수치를 전한 일부 자료는 '개인소득 중'이라는 표현을 쓰고 있어 두 계열이 섞여 인용되었을 가능성이 있다"고 경고한 바 있다. 이번 세션에서도 보건복지부·KIHASA 원문(mohw.go.kr, kihasa.re.kr)이 차단되어 이 네 시점이 모두 "가구소득" 기준으로 통일되어 있는지 독립적으로 확인하지 못했다.
제안 수정: 최종판 제작 전 「2023년도 노인실태조사」 결과보고서(또는 「2020년도 노인실태조사」 결과보고서) 원문 표를 직접 열람해 2008·2017·2020·2023 네 시점이 모두 "가구소득 중 사적이전소득 비중" 기준인지 확인할 것. 만약 일부 연도가 "개인소득" 기준이라면 본문의 46.5%→8.0% 시계열은 기준 혼합 오류이므로, 가구소득 기준으로 확인된 연도만 남기거나 각주로 기준 차이를 명시해야 한다.

---

## 항목 6. 주 수발자 성별구성 수치

### 주장(실제 삽입된 내용): "among older adults with functional limitations who receive care, 81.4% report family as a source of care and 30.7% report using long-term care insurance services (multiple responses were permitted ...) — the long-term care insurance figure up sharply from 19.1% in 2020"
상태: **CONFIRMED**
근거: 독립 검색에서 보건복지부 「2023년 노인실태조사」(2023-10-17 발표, 표본 10,078명) 결과로 "장기요양보험서비스 응답 비율이 2020년 19.1%에서 30.7%로 증가, 가족 81.4%, 친척·이웃 등 20.0%, 개인간병인 등 11.0%"라는 수치가 정확히 재확인됨. 복수응답이라는 점, 자녀 동거율이 같은 기간(20.1%→10.3%) 반토막 난 것과 시기적으로 대칭된다는 서술도 별도 검색(자녀동거 10.3%, 독거노인 32.8%, 2020년 대비 +13.0%p)으로 교차 확인됨.
제안 수정: 없음.

### 주장(성별 구성 수치 자체): 본문은 요청된 "주 수발자 성별 구성" 수치를 삽입하지 않고 `[NEEDS RESEARCH: ...]` 괄호를 그대로 유지했다.
상태: **적절한 처리 — UNSUPPORTED 항목을 만들지 않음**
근거: gapfill 문서가 스스로 "확정 인용 가능한 수치를 확보하지 못했다"고 명시했고(요양보호사 94.9% 여성, 가족 돌봄 제공자 여성 84.7%/남성 13.3%, 며느리 36.7%/딸 35.0% 등은 모두 "조사명·연도 불명" 또는 "원 통계표 미확인"으로 인용 비권장 처리됨), 챕터는 이 수치들을 삽입하지 않고 4장 시간사용조사 교차참조 + 유형별 돌봄제공자 수치(위 항목)로 대체했다. 이는 gapfill이 제시한 세 가지 대안 중 "권장" 옵션을 따른 것으로, 근거 없는 성별 수치를 지어내지 않았다는 점에서 이 책의 편집 방침에 부합한다.
제안 수정: 없음. 다만 향후 정부 도메인 접근이 가능해지면(또는 사용자가 「2023년도 노인실태조사」 결과보고서 PDF 제7장을 직접 확보하면) 주 수발자 성별 구성 수치를 추가하는 것이 5.6절의 젠더 비대칭 논지를 더 강하게 뒷받침할 것이다 — 이는 이번 재검증의 범위를 벗어나는 후속 조사 과제로 남긴다.

---

## 종합 판정

**Editor로 넘기기 전에 항목 3의 연도 라벨 오류(59.4:40.6을 "2024 edition"과 비교한 것)만 정정하면, 이번에 새로 추가된 6개 항목은 출판 가능한 수준이다.**

- 즉시 수정 필요: 1건 — 항목 3, "the 2024 edition of the same survey" → 실제로는 2025년 3월 발표본. 오류의 원인은 gapfill 리서치 문서 자체의 라벨링 오류(125행)가 챕터로 그대로 전파된 것이므로, Researcher 쪽 원인 규명 없이 Writer/Editor가 임의로 이 문장만 다시 쓰면 된다.
- 원문 대조가 필요해 완전히 닫지 못한 항목: 2건 — 항목 1의 "net assets"(순자산) 표현이 실제로 "39세 이하" 전체 구간에도 적용되는 공식 용어인지, 항목 5의 46.5%(2008)~13.9%(2020) 세 시점이 8.0%(2023)와 동일한 "가구소득" 기준인지. 두 건 모두 정부 1차 출처 도메인 차단으로 이번 세션에서 완전히 닫지 못했으며, 도메인 차단이 해제되면 우선적으로 재확인할 것.
- 나머지 항목(항목 2 전체, 항목 3의 듀오 본수치·KIHASA 수치, 항목 4 전체, 항목 5의 2023년 구성비, 항목 6의 돌봄유형 수치)은 각 2회 이상의 독립 검색으로 재현되어 CONFIRMED로 판정한다.
- 항목 6에서 챕터가 근거 없는 성별 수치를 지어내지 않고 `[NEEDS RESEARCH]` 괄호와 대체 수치로 처리한 것은 이 책의 팩트체크 방침이 실제로 작동하고 있다는 긍정적 신호다.
