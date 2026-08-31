# Fact-Check Recheck — 08 Statistical Appendix (Gap-fill Update Only)

- **검증 대상**: `books/korea-family-transformation/02-chapters/08-appendix-statistical-references.md` (2026-08-29 갱신본)
- **비교 기준**: 이전 리포트 `books/korea-family-transformation/03-factcheck/08-appendix-statistical-references.md` (2026-08-28)
- **조사 근거**: `books/korea-family-transformation/01-research/08-appendix-gapfill.md` (Researcher, 2026-08-29) + 이번 리포트에서 직접 수행한 독립 웹 검증
- **검증 범위**: 지시받은 3항목만. 그 외 수치(TFR·임금격차·1인가구 등)의 진위는 이전 리포트에서 이미 CONFIRMED된 것으로 전제하고 재검증하지 않았다.

## 검증 환경상의 한계

이 세션에서도 `mods.go.kr`, `www.korea.kr`, `www.kci.go.kr`, `db.history.go.kr`가 이그레스 정책으로 차단되어 HTTP 응답(200/404)을 직접 확인하지 못했다. 검증은 검색엔진 인덱스에서 URL 문자열·제목·저자·쪽수·발표일이 교차 확인되는지로 이루어졌다. 이는 Researcher의 조사와 동일한 제약이며, **Production 직전 링크 전수 클릭 검사가 여전히 필수**라는 결론도 동일하다.

---

# 1. 「2025 통계로 보는 1인가구」 URL 및 발행기관명 통일

## 1-1. 주장: `https://mods.go.kr/board.es?mid=a10301010000&bid=10820&act=view&list_no=442130`가 「2025 통계로 보는 1인가구」(2025-12-09, 국가데이터처)를 가리킨다

**상태: CONFIRMED**

**근거**: 독립 웹 검색에서 이 URL이 문자열 그대로(파라미터 순서만 다름, `mainXml=Y` 부가) "2025 통계로 보는 1인가구 | 전체 | 보도자료 | 새소식 : 국가데이터처" 제목으로 인덱스된다. 동일 문서가 정책브리핑(`korea.kr/briefing/pressReleaseView.do?newsId=156734077`), KDI 경제정보센터(`eiec.kdi.re.kr/policy/materialView.do?num=274492`), 정책브리핑 전문자료(`docId=41561`), 네이트뉴스, 부산광역시사회복지협의회 재게시 등 **5개 이상의 독립 채널에서 동일 발표일(2025-12-09)·동일 수치로 재확인**된다. 본문 수치(2024년 1인가구 804만 5천 가구=36.1%, 연령순 70세 이상 19.8%>29세 이하 17.8%>60대 17.6%>30대 17.4%, 서울·경기 거주 42.7%, 단독주택 39.0%, 취업 1인가구 510만 가구, 연소득 3,423만 원)까지 문서 동일성 확인에 그대로 일치한다. 부록 76행의 각주 [1] 후반부(「2025 통계로 보는 1인가구」)와 정확히 일치.

**제한**: HTTP 200 응답 자체는 이번에도 직접 확인하지 못했다(도메인 차단). `list_no=` 형식 딥링크는 게시판 일련번호 의존적이므로 Production 직전 클릭 재확인 권고— 이 권고는 각주 [1]의 자체 주석에도 이미 반영되어 있다(부록 76행: "board.es/list_no form are board-sequence dependent and should be click-verified again immediately before production").

---

## 1-2. 주장: 발행기관 영문 표기를 "Statistics Korea"(~2025-09-30)와 "Ministry of Data and Statistics (MODS)"(2025-10-01~)로 나누어 쓴 것

**상태: CONFIRMED**

**근거**: 독립 검색 결과, 통계청이 **2025년 10월 1일** 기획재정부 외청에서 국무총리 직속 부(部)급 기관으로 승격되어 영문명 **"Ministry of Data and Statistics"**로 개편되었다는 사실이 Wikipedia 항목("Ministry of Data and Statistics"), GHDx(IHME) 국제기구 DB("Ministry of Data and Statistics (KOSTAT) (South Korea)"), 기관 공식 페이지(`mods.go.kr/menu.es?mid=a20604010000` "Organization Chart | Organization | About MODS")에서 일관되게 확인된다. 개편 전 기관은 "Statistics Korea"로 별도 확인됨. 부록 76행의 기관명 이원 표기(2024년 12월 문서→Statistics Korea, 2025년 12월 문서→Ministry of Data and Statistics)는 발행 시점 기준 원칙에 정확히 부합한다.

**부수 확인 — "National Data and Statistics Office" 오표기 제거는 타당했다.** 이전 리포트(C-1)가 지적한 이 오표기가 이번 갱신본에서 완전히 사라졌음을 확인했다. 검색 결과에도 이 조합은 등장하지 않는다.

**참고(경계 사례, 오류 아님)**: 개편 발표 직전 시점(2025-09-30) 영문 기사 제목은 "Statistics Korea to Officially Launch as 'National Data Agency' on October 1"으로, 정식 영문명 확정 전의 언론 임시 번역이 "National Data Agency"였다. 부록은 이 임시 번역을 쓰지 않고 기관 자신이 쓰는 "Ministry of Data and Statistics"를 택했으므로 이 선택은 **CONFIRMED**로 유지한다. 다만 독자가 "National Data Agency"라는 표현을 다른 매체에서 만날 수 있다는 점은 부록 각주가 이미 다루지 않았으므로, Editor 단계에서 한 줄 정도 언급해도 좋다(필수 아님, 권고).

---

# 2. 신규 각주 [17]–[22]

## 2-1. [17] Deuchler, *The Confucian Transformation of Korea* (1992), ch. 5 "Inheritance"

**상태: CONFIRMED**

**근거**: 독립 검색으로 확인한 이 책의 목차는 Introduction, Ch.1 "The Pre-Confucian Past", Ch.2 "Neo-Confucianism...", Ch.3 "Agnation and Ancestor Worship", **Ch.4 "Mourning and Funerary Rites", Ch.5 "Inheritance"(203쪽부터)**, Ch.6 "Confucian Legislation: The Consequences for Women", Conclusions 순이다. 각주가 지목한 "chap. 5, 'Inheritance'"는 정확하다. 이 책은 이 분야의 표준 레퍼런스로 조선 초기 균분상속 논증에 적합하다.

## 2-2. [18] Peterson, *Korean Adoption and Inheritance* (1996)

**상태: CONFIRMED**

**근거**: Cornell East Asia Series 80, Cornell University East Asia Program, 1996, xii+267쪽 — 서지사항이 Semantic Scholar 서평, Cornell University Press 서적정보, Project MUSE 서평에서 모두 일치한다. 내용도 각주가 뒷받침하려는 논지(균분상속에서 장자 우대로의 전환, 16~17세기)와 정확히 부합: 검색된 서평은 이 책이 "the transition from partible inheritance equally divided between sons and daughters to primogeniture"를 사례연구로 추적한다고 명시한다. **조선 초기 균분상속 근거로 적합하다.**

## 2-3. [19] 정긍식, 「16세기 財産相續과 祭祀承繼의 실태」, 『古文書硏究』 24 (2004)

**상태: CONFIRMED (쪽수 포함)**

**근거**: 독립 검색에서 저자·제목·학술지·권호·연도·**쪽수(1–44)**가 모두 일치 확인된다. 리서치 자료가 스스로 경고했던 "1–46으로 잘못 적힐 위험"이 실제 부록(112행)에는 반영되지 않고 **정확히 "1–44"로 기재되어 있음을 확인했다.** 약 250점의 16세기 문서(허여·화회·별급 유형 구분)를 분석한 연구로, 조선 초기(16세기) 균분상속의 코퍼스 근거로 적합하다.

## 2-4. [20] 정긍식, 「16세기 재산상속의 한 실례 — 1579년 權祉 妻 鄭氏 許與文記의 분석」, 『서울대학교 法學』 47(4) (2006)

**상태: CONFIRMED (서지) / NEEDS REVIEW (쪽수 268–302 미확인)**

**근거**: 저자·제목·학술지(서울대학교 法學)·권호(47권 4호)·연도(2006)는 검색으로 일치 확인된다. 노비를 성별·연령·가계별로, 전답을 면적·위치별로 분석한 사례연구라는 점도 확인되어 1579년 단일 문서 정밀분석이라는 각주의 설명과 부합한다. 다만 **정확한 쪽수(268–302)는 이번 검색으로 독립 확인하지 못했다** — KCI 도메인 차단으로 상세 서지 페이지에 직접 접근하지 못했기 때문이며, 서지 자체가 틀렸다는 근거는 없다. Production 직전 KCI 또는 도서관 목록에서 쪽수만 재확인 권고.

## 2-5. [21] 국사편찬위원회 한국사데이터베이스, 조선시대법령자료(경국대전 형전 사천조)

**상태: CONFIRMED**

**근거**: `db.history.go.kr/joseon/law.do`가 국사편찬위원회(National Institute of Korean History) 한국사데이터베이스의 실제 "조선시대법령자료" 페이지로 확인된다. 조문 내용도 독립적으로 재확인했다: 경국대전 형전·사천조는 "부모가 생전에 나눠주지 않은 노비는 자녀의 생몰과 관계없이 나눠준다"고 규정하며, 적자녀 균급을 원칙으로 하되 승중자 가급·첩자녀 차등을 두었고, **이 자녀균분상속법은 중국법의 영향을 받지 않은 한국 고유법**이라는 점이 경향신문(이기환의 흔적의 역사) 등에서 확인된다. 이는 리서치 자료 2-A절의 서술 및 부록 각주 [21]의 설명과 정확히 일치한다. 부록이 승중자 가급·첩자녀 분수를 구체적 숫자로 명시하지 않은 것도 확인 결과와 부합하는 신중한 처리다(가급 비율은 1/5·1/10 두 계열이 상충하므로 숫자를 쓰지 않은 편이 안전하다는 리서치의 권고가 실제로 반영되었는지는 appendix 자체에 해당 숫자가 등장하지 않으므로 확인할 필요조차 없다 — 안전하게 처리됨).

## 2-6. [22] 문숙자, 『조선시대 재산상속과 가족』 (경인문화사, 2004)

**상태: CONFIRMED**

**근거**: 저자·서명·출판사·연도가 독립 검색에서 일치 확인된다. 분재기 분석 박사학위논문("조선전기의 재산상속")을 발전시킨 조선 전기 상속 연구의 대표 단행본이라는 설명도 우리역사넷 등에서 뒷받침된다.

## 2-7. 종합 판단 — [17]~[22]가 "조선 초기 균분상속"의 근거로 적합한가

**상태: CONFIRMED (서지·시기·내용 적합성) / NEEDS REVIEW (본문 연결 공백 — 아래 3절 참조)**

여섯 건 모두 실재하는 문헌이며, 시기(15~16세기)·주제(균분·partible 상속)가 부록 66행의 주장("studies that document equal or partible inheritance practices")과 정확히 부합한다. 특히 이전 리포트가 지적했던 옛 [11](김경숙, 조선 **후기** 단일 가문 사례연구)의 시기 불일치 문제는, **[11]을 삭제하지 않고 "후기 대비용"으로 재배치**하면서 조선 초기 근거를 [17]–[22]로 새로 채우는 방식으로 정확히 해소되었다(부록 96행 각주에 "It is retained here as the source for that later contrast... For sources documenting the earlier, equal-inheritance pattern, see [17]–[22]"라고 명시되어 있으며, 이는 리서치 자료의 권고와 문자 그대로 일치한다).

---

# 3. 잔존 구조적 문제 (지시 범위를 벗어나지만 반드시 기록)

## 3-1. [17]–[22]가 본문(챕터 1)에서 실제로 인용되지 않는다

**상태: UNSUPPORTED (본문 연결 공백 — 이전 리포트 D-1/D-2와 동일한 유형의 문제가 새 각주에도 그대로 반복됨)**

**근거**: `02-chapters/01-confucian-foundation.md` 전체를 검색한 결과, 각주 마커 `[17]`부터 `[22]`까지가 챕터 1 어디에도 등장하지 않는다. 본문은 Deuchler(1992)를 각주 없이 산문으로만 언급하고("Martina Deuchler's *The Confucian Transformation of Korea* (1992) remains its reference statement"), **Peterson(1996), 정긍식(2004/2006), 문숙자(2004)는 챕터 1 본문 어디에도 이름조차 등장하지 않는다.** 즉 부록이 새로 확보한 6건의 근거는 여전히 **부록에만 존재하는 고아 참고문헌**이며, 챕터 1의 조선 초기 균분상속 서술(§1.1, 특히 1566년 화회문기 분배표 부분)은 이 각주들과 기계적으로 연결되어 있지 않다.

이는 리서치 자료 자신이 "Writer에게 남기는 지시 요약" 5번("Deuchler(1992) ch.5와 Peterson(1996)을 본문에 최소 1회씩 명시 인용할 것")에서 이미 요구한 조치이며, **이번 부록 갱신은 참고문헌 목록만 고쳤을 뿐 그 지시를 아직 이행하지 않았다.**

**제안 수정**: Writer 단계에서 챕터 1 §1.1의 균분상속 서술 문장 끝에 `[17]`(Deuchler) 또는 `[17][18]`(Deuchler+Peterson)을, 1566년 화회문기 분배표 앞뒤에 `[19]`나 `[20]`(16세기 분재기 실증연구) 중 최소 하나를 인라인 마커로 삽입할 것. 옛 [11](김경숙 2010, 조선 후기)도 챕터 1 §1.3(장자 집중으로의 전환 서술)에 실제로 인용되지 않고 있으므로 함께 삽입 권고.

## 3-2. "Chapter 7" 명명 불일치 (경미, Editor/Production 소관)

**상태: NEEDS REVIEW**

**근거**: 부록의 "Cited in Chapter N" 표시 중 TFR·성별임금격차·1인가구 세 항목이 "Chapter 7"을 인용처로 명시한다. 실제 파일은 `07-epilogue.md`이며 본문 제목은 "EPILOGUE: Reimagining Kinship in the 21st Century"이고, `00-introduction.md`의 목차 소개에서도 "Epilogue: Reassessing the 'crisis' vocabulary..."로 표기되어 **"Chapter 7"이라는 표현은 책 자신의 다른 어디에도 등장하지 않는다.** 내용상 인용은 정확하다(에필로그가 실제로 이 세 수치를 인용한다, 아래 4절 참조). 다만 독자가 부록의 "Chapter 7"과 본문의 "Epilogue"를 다른 장으로 오인할 위험이 있다. 사실관계 오류는 아니므로 UNSUPPORTED로 분류하지 않았으나, Editor 단계에서 "Chapter 7 (Epilogue)"처럼 병기해 정정할 것을 권고한다.

---

# 4. "Cited in Chapter N" 표시 8건 전수 재검증 (지시 3항목 중 마지막 항목)

지시받은 8개 통계·법령 항목에 붙은 인용처 표시를 각 대상 챕터 파일을 직접 열어 대조했다.

| # | 항목 | 부록의 표시 | 대상 챕터 확인 결과 | 판정 |
|---|---|---|---|---|
| 1 | TFR | Ch.5 §5.3; Ch.7 | `05-demographic-implosion.md` §5.3 "Deconstructing the Lowest Total Fertility Rate"에 0.72/0.75/0.80 계열 서술 확인. `07-epilogue.md` "Beyond Despair" 절과 "Methodological note"에 동일 계열 및 2026-08 확정치 서술 확인. | **CONFIRMED** |
| 2 | 성별임금격차 | Ch.4 opening; Ch.7 | `04-women-workforce.md` §4.2 이전 서두(“approximately 29% in 2023–2024…”)에 확인. `07-epilogue.md` "Beyond Despair" 절에 "approximately 29% in 2023–2024" 확인. | **CONFIRMED** |
| 3 | 고등교육이수율 | Ch.4 opening | `04-women-workforce.md` 서두(“77% of Korean women aged 25 to 34…”)에 확인. | **CONFIRMED** (단, 챕터 4는 2023년·77%를 쓰고, 리서치는 2024년·78.2%를 확보함 — 인용 위치 자체는 정확하나 연도 정합성은 별개 이슈, 이전 리포트 A-7·D-4 참조 — 이번 지시 범위 밖이므로 참고로만 기록) |
| 4 | 1인가구 | Ch.5 §5.2, §5.5; Ch.7 | `05-demographic-implosion.md` §5.2(1990~2024 계열), §5.5(2024년 연령별 구성, 70세 이상 역전)에 확인. `07-epilogue.md`에 "35.5%... 36.1%..." 확인. | **CONFIRMED** |
| 5 | 민법(471호) | Ch.3 opening; Ch.2 §2.1 | `03-hoju-system.md` 서두에 1958년 민법·호주제 성문화 서술 확인. `02-colonial-disruption.md` §2.1 "The Legal Construction of Household Headship, 1909–1939"에 식민지기 배경 서술 확인. | **CONFIRMED** |
| 6 | 2005 헌재결정 | Ch.3 §3.3; Introduction | `03-hoju-system.md` §3.3 "The Civil Coalition and the Landmark 2005 Constitutional Court Decision"에 확인. `00-introduction.md`에 "the Constitutional Court's ruling of constitutional non-conformity on 3 February 2005..." 요약 서술 확인. | **CONFIRMED** |
| 7 | 가족관계등록법(8435호) | Ch.3 §3.4 | `03-hoju-system.md` §3.4 "The 2008 Family Relation Registration Act: Institutional Individualization"에 확인. | **CONFIRMED** |
| 8 | 노인장기요양보험법(8403호) | Ch.5 §5.4, §5.6 | `05-demographic-implosion.md` §5.4에 "National Long-Term Care Insurance... Implemented in July 2008" 확인. §5.6에 장기요양보험 이용률(30.7%, 19.1%) 서술 확인. | **CONFIRMED** |

**부수 확인**: 8번 항목의 법률번호가 이전 리포트(B-5)에서 확정 오류로 지적된 "8402호"에서 **"8403호"로 정정되어 있음을 확인했다** — 필수 수정 사항이 실제로 반영되었다. 4번 항목의 분모 용어도 "residential units"에서 **"households"로 정정**되어 있음을 확인했다(A-10 정정 반영 확인).

---

# 요약 및 권고

| 구분 | 판정 |
|---|---|
| [1] URL(list_no=442130) | CONFIRMED |
| [1] 발행기관명 이원 표기 원칙 및 개편일(2025-10-01) | CONFIRMED |
| "National Data and Statistics Office" 오표기 제거 | CONFIRMED (제거됨) |
| [17] Deuchler 1992 ch.5 | CONFIRMED |
| [18] Peterson 1996 | CONFIRMED |
| [19] 정긍식 2004 (쪽수 1–44 포함) | CONFIRMED |
| [20] 정긍식 2006 | CONFIRMED (쪽수만 NEEDS REVIEW) |
| [21] 경국대전 사천조 DB | CONFIRMED |
| [22] 문숙자 2004 | CONFIRMED |
| [17]-[22]가 조선 초기 균분상속 근거로 적합한지 | CONFIRMED |
| [17]-[22]가 챕터 1 본문에 실제 인용되는지 | **UNSUPPORTED** (인라인 인용 0건 — 신규 발견) |
| 8개 "Cited in Chapter N" 표시 | 전부 **CONFIRMED** |
| "Chapter 7" vs "Epilogue" 명명 | NEEDS REVIEW (경미) |
| 이전 확정 오류 2건(법률번호 8403호, 분모 households) 정정 여부 | 둘 다 **반영 확인됨** |

## 다음 단계 권고

이번 갱신 범위(URL/기관명, 신규 각주 6건, Cited-in-Chapter 표시)만 놓고 보면 **품질이 뚜렷이 개선되었고 새로운 오류는 발견되지 않았다.** URL·서지·시기 적합성은 전부 CONFIRMED이며, 이전에 지적된 두 개의 확정 오류(법률번호, 통계 분모)도 실제로 정정되어 있다.

다만 **Editor로 넘기기 전에 Writer 단계를 한 차례 더 거칠 것을 권고한다.** 이유는 새로 발견된 3-1항 때문이다: 부록이 조선 초기 균분상속의 근거로 [17]–[22]를 정성껏 채워 넣었음에도, 정작 그 근거를 사용해야 할 챕터 1 본문에는 이 여섯 문헌 중 어느 것도 각주 마커나 명시적 언급으로 연결되어 있지 않다. 참고문헌 목록의 정확성과 본문의 근거 연결은 별개 문제이며, 후자는 이전 리포트의 D-1/D-2가 이미 지적했던 구조적 결함이 새 각주에도 그대로 반복된 것이다. Editor의 문장 다듬기로는 해결되지 않는 종류의 문제이므로 Writer가 챕터 1에 인라인 인용을 삽입한 뒤 Editor 단계로 넘길 것을 권고한다.

## 검증에 사용한 독립 출처 (이번 리포트에서 신규로 확인한 것만)

- Wikipedia, "Ministry of Data and Statistics" — 개편일 2025-10-01, 기획재정부 외청→국무총리 직속 승격
- GHDx (IHME), "Ministry of Data and Statistics (KOSTAT) (South Korea)"
- mods.go.kr 기관 페이지(`mid=a20604010000`) — "About MODS" 타이틀 확인
- 정책브리핑/KDI/네이트뉴스 등 5개 채널의 「2025 통계로 보는 1인가구」(2025-12-09) 재게시 — list_no=442130 및 본문 수치 교차확인
- Harvard University Press / Korea Institute (Harvard) — Deuchler (1992) 목차, Ch.5 "Inheritance" (203쪽~)
- Semantic Scholar / Cornell University Press — Peterson (1996) 서지(Cornell East Asia Series 80, xii+267쪽) 및 서평 요지
- KCI 인덱스 검색 결과 — 정긍식 (2004) 저자·제목·권호·쪽수(1–44); 정긍식 (2006) 저자·제목·권호(서울대학교 法學 47(4))
- 경향신문(이기환의 흔적의 역사, 2023-02-28), 우리역사넷 — 경국대전 형전 사천조 자녀균분상속법 원문 취지
- 우리역사넷/예스24 등 — 문숙자, 『조선시대 재산상속과 가족』(경인문화사, 2004) 서지
- `02-chapters/01-confucian-foundation.md`, `02-colonial-disruption.md`, `03-hoju-system.md`, `04-women-workforce.md`, `05-demographic-implosion.md`, `07-epilogue.md`, `00-introduction.md` 원문 직접 대조
