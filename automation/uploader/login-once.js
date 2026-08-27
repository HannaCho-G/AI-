// 최초 로그인 세션 저장 스크립트 (플랫폼 공용).
// 사용법: node login-once.js <platform> <login-url>
// 예: node login-once.js kdp https://kdp.amazon.com/
//
// 브라우저 창이 뜨면 사람이 직접 로그인(2FA 포함)한다. 로그인 완료 후
// 터미널에서 Enter를 누르면 세션이 automation/uploader/.auth/<platform>.json 에 저장된다.
// 이 파일은 .gitignore로 제외되어 있어 저장소에 올라가지 않는다.

const path = require('path');
const { chromium } = require('playwright');

async function main() {
  const [, , platform, url] = process.argv;
  if (!platform || !url) {
    console.error('사용법: node login-once.js <platform> <login-url>');
    process.exit(1);
  }

  const browser = await chromium.launch({
    executablePath: process.env.PLAYWRIGHT_CHROMIUM_PATH || '/opt/pw-browsers/chromium',
    headless: false, // 사람이 직접 로그인해야 하므로 headless로 실행하지 않는다.
  });
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto(url);

  console.log('브라우저 창에서 직접 로그인(2FA 포함)하세요.');
  console.log('로그인이 끝나면 이 터미널에서 Enter를 누르세요.');
  await new Promise((resolve) => {
    process.stdin.once('data', resolve);
  });

  const authDir = path.join(__dirname, '.auth');
  const outPath = path.join(authDir, `${platform}.json`);
  await context.storageState({ path: outPath });
  await browser.close();

  console.log(`세션 저장 완료: automation/uploader/.auth/${platform}.json`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
