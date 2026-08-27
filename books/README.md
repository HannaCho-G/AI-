# books/

각 전자책 프로젝트가 `books/<slug>/` 폴더 하나씩으로 들어간다. 폴더 구조와 파이프라인 단계는 최상위 `CLAUDE.md`를 참고.

책이 완성될 때마다 Content Connector 에이전트가 `CROSS-SELL-MAP.md`(이 폴더 최상위)를 갱신해서 책들 간의 교차판매 관계를 추적한다. 아직 완성된 책이 없으면 이 파일은 존재하지 않는다 — Content Connector가 첫 책 완성 시 생성한다.
