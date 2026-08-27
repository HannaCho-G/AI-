# Uploader 자동화

Uploader 에이전트(`.claude/agents/uploader.md`)가 실제 판매 플랫폼(Amazon KDP, Gumroad, Digital24Store, Whop, Etsy, eBay)에 완성된 책을 올릴 때 쓰는 브라우저 자동화 스크립트와 로그인 세션이 있는 곳.

**여기 있는 것 중 어떤 것도 저장소에 실제 비밀번호나 로그인 세션을 저장하지 않는다** — `.env`와 `.auth/`는 저장소 최상위 `.gitignore`에 의해 커밋에서 제외된다.

## 왜 세션 재사용 방식을 쓰는가

Uploader가 매번 아이디/비밀번호로 로그인하는 대신, **처음 한 번은 사람이 직접 로그인**하고 그 로그인 상태(쿠키/세션)를 저장해서 재사용하는 방식을 기본으로 한다. 이유:

- 비밀번호를 코드/환경변수에 평문으로 두는 것보다 안전하다.
- 2FA/CAPTCHA 등 자동화가 원천적으로 어려운 구간을 사람이 직접 통과시킬 수 있다.
- Amazon KDP처럼 자동화 로그인에 민감한 플랫폼에서 계정 정지 리스크를 줄일 수 있다.

## 최초 로그인 절차 (플랫폼당 1회, 세션 만료 시 재실행)

이 저장소의 Playwright 환경은 이미 세팅되어 있다 (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`, 실행 파일 `/opt/pw-browsers/chromium`). 플랫폼별로 아래와 같은 형태의 1회성 로그인 스크립트를 실행해서 세션을 저장한다 (예시, Node.js + playwright 기준):

```js
// automation/uploader/login-once.js
// 사용법: node login-once.js <platform> <login-url>
const { chromium } = require('playwright');

(async () => {
  const [, , platform, url] = process.argv;
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium',
    headless: false, // 사람이 직접 로그인해야 하므로 헤드리스 금지
  });
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto(url);
  console.log('브라우저 창에서 직접 로그인(2FA 포함)하세요. 로그인 완료 후 이 터미널에서 Enter를 누르세요.');
  await new Promise((resolve) => process.stdin.once('data', resolve));
  await context.storageState({ path: `automation/uploader/.auth/${platform}.json` });
  await browser.close();
  console.log(`세션 저장 완료: automation/uploader/.auth/${platform}.json`);
})();
```

이후 실제 업로드 스크립트는 `storageState: 'automation/uploader/.auth/<platform>.json'`로 컨텍스트를 열어서 로그인 상태를 재사용한다. 세션이 만료되면(오래된 쿠키 등) 위 절차를 다시 실행한다.

## 폴더 구조 (계획)

```
automation/uploader/
  README.md            # 이 문서
  .env.example          # 세션 재사용이 안 되는 경우에만 쓰는 자격증명 템플릿 (실제 값은 .env에, 커밋 안 됨)
  .auth/                 # 플랫폼별 storageState (커밋 안 됨)
  login-once.js          # 최초 로그인 세션 저장 스크립트 (공용)
  kdp/                   # Amazon KDP 업로드 스크립트
  gumroad/               # Gumroad 업로드 스크립트
  digital24store/        # Digital24Store 업로드 스크립트
  whop/                  # Whop 업로드 스크립트
  etsy/                  # Etsy 업로드 스크립트
  ebay/                  # eBay 업로드 스크립트
```

> **현재 상태**: 안전 구조(세션 저장 방식, gitignore, Uploader 에이전트의 확인 절차)까지 세팅되어 있고, 플랫폼별 실제 업로드 스크립트(`kdp/`, `gumroad/` 등)는 아직 비어있다. 각 플랫폼의 리스팅 작성 화면 UI는 실제 로그인 세션으로 직접 붙어봐야 정확한 선택자(selector)를 확인할 수 있어서, 첫 실행 때 Uploader 에이전트가 사용자와 함께 화면을 보며 채워나가는 방식으로 구축하는 게 안전하다. 한 번 만들어두면 그 다음 책부터는 재사용된다.

## 플랫폼별 유의사항

### Amazon KDP
- **자동화에 가장 민감한 플랫폼.** 봇/스크립트를 통한 계정 조작에 대한 정책이 엄격한 편이라, 자동화가 계정 정지 등 실제 리스크로 이어질 수 있다. 처음에는 사람이 직접 로그인(2단계 인증 포함)하고, 자동화는 리스팅 정보 입력 등 저위험 구간부터 점진적으로 넓히는 것을 권장.
- 원고는 KDP가 요구하는 형식(EPUB 권장, 또는 KDP 자체 변환)에 맞춰야 한다.
- 카테고리/키워드/가격/로열티 옵션은 실수하면 판매에 바로 영향을 주므로 항상 최종 확인 후 제출.

### Gumroad
- 디지털 상품 업로드가 비교적 단순하고 API도 제공한다 — 장기적으로는 브라우저 자동화 대신 Gumroad API 사용을 고려할 수 있음.

### Digital24Store
- 국내 플랫폼 — UI/정책 확인 필요, 실제 계정으로 첫 업로드 시 화면 구조를 확인하며 스크립트를 만든다.

### Whop
- 디지털 상품/멤버십 중심 플랫폼. API 제공 여부 확인 후 가능하면 API 우선 고려.

### Etsy
- 원래 핸드메이드/빈티지/실물 중심 마켓플레이스. 디지털 다운로드 상품이 가능한 카테고리인지, 정책상 전자책이 허용되는지 업로드 전에 반드시 확인. 애매하면 사용자에게 먼저 확인.

### eBay
- 기본적으로 실물/중고 거래 중심 플랫폼. 디지털 다운로드 상품 지원이 제한적이거나 카테고리가 별도일 수 있다 — 전자책을 실제로 리스팅 가능한 카테고리/정책인지 먼저 확인 후 진행.

## Uploader 에이전트와의 관계

`.claude/agents/uploader.md`가 이 폴더의 스크립트/세션을 사용해서 실제 업로드를 수행한다. 최종 Publish/제출 전에는 항상 사용자 확인을 거치도록 되어 있다 — 이 폴더의 스크립트를 직접 수정하더라도 그 확인 단계는 유지한다.
