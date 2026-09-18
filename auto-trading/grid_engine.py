"""
🔧 Grid Trading Engine (자체완결형, 실전용)
==========================================
업비트 BTC/KRW 그리드 트레이딩 봇.

⚠️  현실적으로 꼭 읽어주세요
------------------------------------------------------------
이 프로그램은 "며칠 안에 원금을 2배로" 만들어주는 도구가 아닙니다.
그리드 트레이딩은 가격이 오르내리는 변동성에서 수수료 이상의 작은
마진을 꾸준히 긁어모으는 전략입니다. 짧은 기간에 큰 수익을 노리면
그만큼 원금을 짧은 기간에 잃을 확률도 똑같이 커집니다.

이 코드가 실제로 지키는 것:
  1. 왕복 수수료보다 마진이 작은 그리드는 애초에 만들지 않음
     (수수료만 내고 손실 보는 매매를 구조적으로 차단)
  2. 평가자산이 설정한 손절선 아래로 떨어지면 즉시 전량 취소 후 정지
     (하락장에서 "물타기"가 무한 반복되며 원금을 다 태우는 것 방지)
  3. 평가자산이 "시드 × WITHDRAW_MULTIPLE"에 도달하면 시드금액만큼
     출금(알림 또는 자동)하고, 나머지 금액으로 계속 매매 (정지하지 않음)
  4. 그리드가 절반만 체결된 채 영원히 방치되지 않도록 자동 재중심

[실행]
  python grid_engine.py --check              # 설정값 검증만 (주문 없음)
  python grid_engine.py --status             # 현재 시장/레짐 상태 확인
  python grid_engine.py --once               # 1회 사이클만 실행
  python grid_engine.py                      # 무한 루프 (실전/모의)
  python grid_engine.py --backtest           # 그리드 백테스트
  python grid_engine.py --confirm-withdrawal # 수동으로 출금했다면 이 명령으로 시드 리셋
  python grid_engine.py --withdraw-now 50000 # 지금 즉시 실제 출금 API 1회 테스트 실행

[설정]
  모든 설정은 환경변수로 조절합니다 (.env 파일을 만들어 사용 가능).
  주요 값:
    UPBIT_ACCESS_KEY / UPBIT_SECRET_KEY  - 없으면 자동으로 모의(paper) 모드
    TRADING_CAPITAL_KRW   (기본 50000)   - 시드(원금). 출금 후에도 이 금액을 기준으로 다시 굴림
    WITHDRAW_MULTIPLE     (기본 2.0)     - 시드의 이 배수에 도달하면 출금 트리거 (5만→10만)
    STOP_LOSS_PCT         (기본 0.85)    - 이 비율 밑으로 떨어지면 전량 정지
    AUTO_WITHDRAW_ENABLED (기본 false)   - true면 실제 업비트 출금 API를 자동 호출
                                            (사전에 업비트에서 출금계좌 등록 + API 키
                                            출금권한/IP 화이트리스트 설정 필수. 기본값은
                                            false로, 알림만 하고 실제 출금은 사람이
                                            수동으로 한 뒤 --confirm-withdrawal로 확인)
"""

import os
import sys
import json
import time
import signal
import logging
import argparse
import urllib.request
from datetime import datetime
from typing import Dict, List, Optional

import ccxt
import numpy as np
import pandas as pd

# ============================================================
# .env 파일 로더 (별도 패키지 설치 없이 간단히 지원)
# ============================================================
def _load_dotenv(path: str = '.env'):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, _, val = line.partition('=')
            key, val = key.strip(), val.strip().strip('"').strip("'")
            os.environ.setdefault(key, val)

_load_dotenv()


def _env_float(key: str, default: float) -> float:
    try:
        return float(os.environ.get(key, default))
    except (TypeError, ValueError):
        return default


def _env_int(key: str, default: int) -> int:
    try:
        return int(os.environ.get(key, default))
    except (TypeError, ValueError):
        return default


def _env_bool(key: str, default: bool) -> bool:
    val = os.environ.get(key)
    if val is None:
        return default
    return val.strip().lower() in ('1', 'true', 'yes', 'y', 'on')


# ── 공통 파라미터 ────────────────────────────────────────────
SYMBOL          = os.environ.get('SYMBOL', 'BTC/KRW')
TIMEFRAME       = os.environ.get('TIMEFRAME', '15m')   # 2~3일 단위 대응 → 일봉은 너무 느림
CAPITAL         = _env_float('TRADING_CAPITAL_KRW', 50_000)   # 시드(원금)
FEE_RATE        = _env_float('FEE_RATE', 0.0005)              # 업비트 수수료 0.05%
MIN_ORDER_KRW   = 5_000         # 업비트 최소 주문금액 (거래소 고정값)

# ── 그리드 파라미터 ──────────────────────────────────────────
GRID_LEVELS      = _env_int('GRID_LEVELS', 4)       # 소액(5만원)에서는 레벨 적게 → 주문 크기 확보
GRID_ATR_MULT    = _env_float('GRID_ATR_MULT', 0.6)
GRID_MIN_PCT     = _env_float('GRID_MIN_PCT', 0.006)  # 그리드 간격 최소치: 현재가 대비 0.6%
GRID_CAPITAL_PCT = _env_float('GRID_CAPITAL_PCT', 0.80)
RECENTER_MULT    = _env_float('RECENTER_MULT', 2.0)   # 중심가 대비 이만큼(간격 배수) 벗어나면 재중심

# ── 리스크 관리 / 시드 출금 ───────────────────────────────────
STOP_LOSS_PCT       = _env_float('STOP_LOSS_PCT', 0.85)   # 평가자산이 시드의 85% 밑이면 정지
WITHDRAW_MULTIPLE   = _env_float('WITHDRAW_MULTIPLE', 2.0)  # 시드의 이 배수 도달 시 출금 트리거
AUTO_WITHDRAW_ENABLED = _env_bool('AUTO_WITHDRAW_ENABLED', False)  # true=실제 출금 API 자동 호출
WITHDRAW_ALERT_COOLDOWN_SEC = _env_int('WITHDRAW_ALERT_COOLDOWN_SEC', 3600)  # 알림 반복 간격

# ── 레짐 파라미터 ────────────────────────────────────────────
REGIME_PROB_MIN = _env_float('REGIME_PROB_MIN', 0.52)

# ── 드라이런 (실거래 투입 전 4단계용) ──────────────────────────
# true면 실제 API 키로 시세/잔고/미체결주문은 그대로 조회하지만,
# 매수/매도/취소/출금 등 "쓰기" 요청은 절대 거래소로 보내지 않고 로그만 남긴다.
# --dry-run 플래그로도 켤 수 있다 (main()에서 이 값을 덮어씀).
DRY_RUN = _env_bool('DRY_RUN', False)

STATE_FILE       = os.environ.get('STATE_FILE', 'grid_state.json')
RISK_STATE_FILE  = os.environ.get('RISK_STATE_FILE', 'risk_state.json')
LOG_FILE         = os.environ.get('LOG_FILE', 'trading.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# ============================================================
# 설정값 검증 (주문 넣기 전에 반드시 통과해야 함)
# ============================================================
class ConfigError(Exception):
    pass


def validate_config():
    """
    잘못된 설정으로 실주문을 내지 않도록 시작 시점에 강제 검증.
    예전 버전은 이 검증이 없어서 소액 계좌에서 레벨당 금액이
    최소 주문금액 미만으로 계산돼도 그냥 조용히 스킵되고 넘어갔음.
    """
    problems = []

    grid_capital = CAPITAL * GRID_CAPITAL_PCT
    per_level = grid_capital / GRID_LEVELS if GRID_LEVELS > 0 else 0

    if GRID_LEVELS <= 0:
        problems.append("GRID_LEVELS는 1 이상이어야 합니다.")
    if per_level < MIN_ORDER_KRW:
        max_levels = int(grid_capital // MIN_ORDER_KRW)
        problems.append(
            f"레벨당 투입금액(₩{per_level:,.0f})이 업비트 최소주문금액"
            f"(₩{MIN_ORDER_KRW:,.0f})보다 작습니다. "
            f"현재 자본(₩{CAPITAL:,.0f})으로는 GRID_LEVELS를 최대 {max_levels}로 "
            f"낮추거나 TRADING_CAPITAL_KRW를 늘리세요."
        )
    if CAPITAL <= 0:
        problems.append("TRADING_CAPITAL_KRW는 0보다 커야 합니다.")
    if not (0 < STOP_LOSS_PCT < 1):
        problems.append("STOP_LOSS_PCT는 0과 1 사이여야 합니다 (예: 0.85).")
    if WITHDRAW_MULTIPLE <= 1.0:
        problems.append("WITHDRAW_MULTIPLE은 1보다 커야 합니다 (예: 2.0 = 시드의 2배).")
    if AUTO_WITHDRAW_ENABLED and not (
        os.environ.get('UPBIT_ACCESS_KEY') and os.environ.get('UPBIT_SECRET_KEY')
    ):
        problems.append(
            "AUTO_WITHDRAW_ENABLED=true인데 API 키가 없습니다. "
            "모의 모드에서는 실제 출금이 불가능하므로 false로 두거나 API 키를 설정하세요."
        )

    if problems:
        msg = "설정 오류로 실행을 중단합니다:\n" + "\n".join(f"  - {p}" for p in problems)
        raise ConfigError(msg)

    withdraw_target = CAPITAL * WITHDRAW_MULTIPLE
    logger.info(
        f"✅ 설정 검증 통과 | 시드 ₩{CAPITAL:,.0f} | 그리드 {GRID_LEVELS}단계 "
        f"| 레벨당 ₩{per_level:,.0f} | 출금 트리거 ₩{withdraw_target:,.0f} "
        f"(시드×{WITHDRAW_MULTIPLE}) | 손절선 {STOP_LOSS_PCT*100:.0f}% | "
        f"자동출금 {'ON' if AUTO_WITHDRAW_ENABLED else 'OFF(알림만)'}"
    )


# ============================================================
# Upbit API 연결
# ============================================================
class UpbitConnector:
    """
    실전 주문 실행 모듈.
    API 키 없으면 시세 조회만 가능 (모의/페이퍼 트레이딩 모드로 자동 전환).
    """
    def __init__(self):
        access = os.environ.get('UPBIT_ACCESS_KEY', '')
        secret = os.environ.get('UPBIT_SECRET_KEY', '')
        self.exchange = ccxt.upbit({
            'apiKey':          access,
            'secret':          secret,
            'enableRateLimit': True,
        })
        self.has_key = bool(access and secret)
        self.dry_run = DRY_RUN
        if self.has_key and self.dry_run:
            logger.warning("🧪 DRY_RUN 모드 — 실제 API 키로 조회는 하지만 주문/취소/출금은 절대 보내지 않습니다.")
        elif self.has_key:
            logger.info("✅ API 키 확인 → 실전 주문 가능")
        else:
            logger.warning("⚠️  API 키 없음 → 시세 조회만 가능 (모의 모드)")

    def fetch_ohlcv(self, limit: int = 150) -> pd.DataFrame:
        """
        최근 캔들 조회. limit<=200이면 단순 단일 호출 (가장 흔한 경우).
        200개를 넘으면 과거로 페이지네이션.
        """
        if limit <= 200:
            batch = self.exchange.fetch_ohlcv(SYMBOL, TIMEFRAME, limit=limit)
            all_ohlcv = batch
        else:
            all_ohlcv, since = [], None
            while len(all_ohlcv) < limit:
                batch = self.exchange.fetch_ohlcv(
                    SYMBOL, TIMEFRAME, since=since, limit=200)
                if not batch:
                    break
                all_ohlcv = batch + all_ohlcv
                tf_ms = self.exchange.parse_timeframe(TIMEFRAME) * 1000
                since = batch[0][0] - (200 * tf_ms)
                if len(batch) < 200:
                    break
                time.sleep(0.3)
            all_ohlcv = all_ohlcv[-limit:]

        df = pd.DataFrame(all_ohlcv,
                          columns=['timestamp','open','high','low','close','volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df.drop_duplicates().sort_index()

    def get_current_price(self) -> float:
        ticker = self.exchange.fetch_ticker(SYMBOL)
        return float(ticker['last'])

    def get_balance(self) -> Dict[str, float]:
        if not self.has_key:
            return {'KRW': CAPITAL, 'BTC': 0.0}
        balance = self.exchange.fetch_balance()
        return {
            'KRW': float(balance.get('KRW', {}).get('free', 0)),
            'BTC': float(balance.get('BTC', {}).get('free', 0)),
        }

    def get_open_orders(self) -> List[dict]:
        """거래소에 현재 실제로 남아있는 미체결 주문 전체 (재시작 시 대조용)"""
        if not self.has_key:
            return []
        try:
            return self.exchange.fetch_open_orders(SYMBOL)
        except Exception as e:
            logger.error(f"❌ 미체결 주문 조회 실패: {e}")
            return []

    def fetch_order(self, order_id: str) -> Optional[dict]:
        """주문 하나의 최신 상태 조회 (없으면 None, 실패도 None + 로그)"""
        if not self.has_key or not order_id:
            return None
        try:
            return self.exchange.fetch_order(order_id, SYMBOL)
        except Exception as e:
            logger.warning(f"⚠️  주문 상태 조회 실패 ({order_id}): {e}")
            return None

    def place_limit_buy(self, price: float, amount_krw: float) -> Optional[dict]:
        """지정가 매수 주문"""
        if amount_krw < MIN_ORDER_KRW:
            logger.warning(f"주문금액 부족: ₩{amount_krw:,.0f} < 최소 ₩{MIN_ORDER_KRW:,.0f}")
            return None
        qty = (amount_krw * (1 - FEE_RATE)) / price
        if not self.has_key:
            order_id = f'mock_buy_{int(time.time()*1000)}_{price:.0f}'
            logger.info(f"[모의] 매수 주문: ₩{price:,.0f} × {qty:.8f}BTC = ₩{amount_krw:,.0f}")
            return {'id': order_id, 'price': price, 'qty': qty, 'side': 'buy', 'status': 'open'}
        if self.dry_run:
            logger.info(f"🧪 [DRY-RUN] 매수 주문 생략: ₩{price:,.0f} × {qty:.8f}BTC (실제 전송 안 함)")
            return {'id': f'dryrun_buy_{int(time.time()*1000)}', 'price': price, 'qty': qty,
                    'side': 'buy', 'status': 'open'}
        try:
            order = self.exchange.create_limit_buy_order(SYMBOL, qty, price)
            logger.info(f"✅ 매수 주문: ₩{price:,.0f} × {qty:.8f}BTC")
            return order
        except Exception as e:
            logger.error(f"❌ 매수 주문 실패: {e}")
            return None

    def place_limit_sell(self, price: float, qty: float) -> Optional[dict]:
        """지정가 매도 주문 (최소 주문금액 미달이면 실패를 명확히 알림)"""
        notional = price * qty
        if notional < MIN_ORDER_KRW:
            logger.error(
                f"❌ 매도 불가: 주문금액 ₩{notional:,.0f}이 최소 ₩{MIN_ORDER_KRW:,.0f} 미만. "
                f"이 수량은 다른 매수 체결과 합쳐 다음 사이클에 재시도합니다."
            )
            return None
        if not self.has_key:
            order_id = f'mock_sell_{int(time.time()*1000)}_{price:.0f}'
            logger.info(f"[모의] 매도 주문: ₩{price:,.0f} × {qty:.8f}BTC")
            return {'id': order_id, 'price': price, 'qty': qty, 'side': 'sell', 'status': 'open'}
        if self.dry_run:
            logger.info(f"🧪 [DRY-RUN] 매도 주문 생략: ₩{price:,.0f} × {qty:.8f}BTC (실제 전송 안 함)")
            return {'id': f'dryrun_sell_{int(time.time()*1000)}', 'price': price, 'qty': qty,
                    'side': 'sell', 'status': 'open'}
        try:
            order = self.exchange.create_limit_sell_order(SYMBOL, qty, price)
            logger.info(f"✅ 매도 주문: ₩{price:,.0f} × {qty:.8f}BTC")
            return order
        except Exception as e:
            logger.error(f"❌ 매도 주문 실패: {e}")
            return None

    def cancel_order(self, order_id: str) -> Optional[float]:
        """
        주문 취소. 반환값은 '취소되기 직전까지 이미 체결돼 있던 수량'(float).
        취소 자체가 실패하면 None을 반환해서 호출부가 "체결량 0"과 "취소 실패"를
        절대 혼동하지 않게 한다 (부분체결된 BTC를 조용히 잃어버리지 않기 위함).
        """
        if not self.has_key:
            logger.info(f"[모의] 주문 취소: {order_id}")
            return 0.0  # 모의 모드는 부분체결을 모델링하지 않음
        if self.dry_run:
            logger.info(f"🧪 [DRY-RUN] 주문 취소 생략: {order_id}")
            return 0.0
        # 취소 전에 먼저 현재까지 체결된 수량을 확인해둔다.
        filled_qty = 0.0
        before = self.fetch_order(order_id)
        if before:
            filled_qty = float(before.get('filled') or 0)
        try:
            self.exchange.cancel_order(order_id, SYMBOL)
        except Exception as e:
            logger.error(f"❌ 주문 취소 실패: {e}")
            return None
        if filled_qty > 0:
            logger.warning(f"⚠️  취소 전 이미 부분체결됨: {order_id} → {filled_qty:.8f}BTC (회수 처리)")
        return filled_qty

    def sell_all_market(self, qty: float) -> Optional[dict]:
        """손절선 도달 시 즉시 청산용 시장가 매도"""
        if qty <= 0:
            return None
        if not self.has_key:
            logger.info(f"[모의] 시장가 전량 매도: {qty:.8f}BTC")
            return {'id': f'mock_market_sell_{int(time.time())}', 'qty': qty}
        if self.dry_run:
            logger.info(f"🧪 [DRY-RUN] 시장가 전량 매도 생략: {qty:.8f}BTC (실제 전송 안 함)")
            return {'id': f'dryrun_market_sell_{int(time.time())}', 'qty': qty}
        try:
            order = self.exchange.create_market_sell_order(SYMBOL, qty)
            logger.info(f"✅ 시장가 전량 매도 완료: {qty:.8f}BTC")
            return order
        except Exception as e:
            logger.error(f"❌ 시장가 매도 실패: {e}")
            return None

    def sell_market_krw(self, amount_krw: float, current_price: float) -> Optional[dict]:
        """지정한 원화 금액만큼만 시장가로 매도 (출금 재원 마련용)"""
        qty = amount_krw / current_price
        return self.sell_all_market(qty)

    def withdraw_krw(self, amount: float) -> Optional[dict]:
        """
        원화(KRW) 실제 출금. ccxt의 통합 withdraw()는 업비트에 한해 KRW를
        특수 처리해서 주소(address) 없이 호출 가능하다.

        ⚠️ 이 메서드는 실행 전 반드시 아래가 되어 있어야 성공합니다 (업비트 웹/앱에서
        1회 수동 설정, API로 대신할 수 없음):
          1. 업비트 마이페이지에서 본인 명의 은행계좌를 "출금 계좌"로 사전 등록
          2. Open API 키 발급 시 "출금하기" 권한 체크 + 허용 IP 등록
        이 사전조건이 안 되어 있으면 아래 호출은 예외를 던지고, 그 사유를 그대로
        로그에 남긴다 (여기서 추측해서 넘어가지 않고 실패를 명확히 알림).
        """
        if not self.has_key:
            logger.warning("[모의] 출금은 모의 모드에서 지원하지 않습니다 (실제 API 키 필요).")
            return None
        if self.dry_run:
            logger.info(f"🧪 [DRY-RUN] 출금 생략: ₩{amount:,.0f} (실제 전송 안 함)")
            return {'id': f'dryrun_withdraw_{int(time.time())}', 'amount': amount}
        try:
            result = self.exchange.withdraw('KRW', amount, None)
            logger.info(f"🏧 출금 요청 성공: ₩{amount:,.0f} → 등록된 계좌")
            return result
        except Exception as e:
            logger.error(
                f"❌ 출금 요청 실패: {e}\n"
                f"   확인할 것: (1) 업비트에 출금계좌가 등록/인증되어 있는지 "
                f"(2) API 키에 출금 권한 + 허용 IP가 설정되어 있는지 "
                f"(3) 신규/변경된 API 키라면 업비트 정책상 일정 시간(최대 72시간) "
                f"출금이 제한될 수 있습니다."
            )
            return None


# ============================================================
# 외부 센티멘트 수집기
# ============================================================
class SentimentCollector:
    """
    시장 외부 영향 요인 수집. API 실패 시 중립값으로 자동 폴백하여
    프로그램이 멈추지 않도록 설계됨.
    """
    TIMEOUT = 5

    def _fetch(self, url: str) -> Optional[dict]:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=self.TIMEOUT) as r:
                return json.loads(r.read())
        except Exception as e:
            logger.warning(f"⚠️  외부 데이터 수집 실패: {url[:40]}... → {e}")
            return None

    def get_fear_greed(self) -> dict:
        data = self._fetch("https://api.alternative.me/fng/?limit=1")
        if data and data.get('data'):
            val = int(data['data'][0]['value'])
            cls = data['data'][0]['value_classification']
            return {
                'value': val, 'classification': cls,
                'signal': 'BUY' if val < 25 else 'SELL' if val > 75 else 'NEUTRAL',
                'score': (50 - val) / 50, 'ok': True,
            }
        return {'value': 50, 'classification': 'Neutral', 'signal': 'NEUTRAL', 'score': 0.0, 'ok': False}

    def get_kimchi_premium(self, upbit_krw: float, usd_krw: float = 1350.0) -> dict:
        data = self._fetch("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        if data and 'price' in data and upbit_krw > 0:
            binance_krw = float(data['price']) * usd_krw
            premium = (upbit_krw / binance_krw - 1) * 100
            return {
                'premium_pct': round(premium, 2), 'binance_usd': round(float(data['price']), 0),
                'signal': 'OVERHEAT' if premium > 3 else 'DISCOUNT' if premium < -1 else 'NORMAL',
                'score': max(-1, min(1, -premium / 3)), 'ok': True,
            }
        return {'premium_pct': 0.0, 'signal': 'NORMAL', 'score': 0.0, 'ok': False}

    def collect_all(self, upbit_price: float = 0) -> dict:
        fg = self.get_fear_greed()
        kim = self.get_kimchi_premium(upbit_price)
        composite = fg['score'] * 0.6 + kim['score'] * 0.4
        ok_count = sum([fg['ok'], kim['ok']])
        return {
            'fear_greed': fg, 'kimchi_premium': kim,
            'composite_score': round(composite, 4),
            'sentiment': 'BULLISH' if composite > 0.2 else 'BEARISH' if composite < -0.2 else 'NEUTRAL',
            'data_quality': f"{ok_count}/2 수집 성공",
        }


# ============================================================
# 시장 분석기
# ============================================================
class MarketAnalyzer:
    """현재 시장 레짐 + ATR 계산"""

    @staticmethod
    def analyze(df: pd.DataFrame, collect_sentiment: bool = True) -> dict:
        close, volume = df['close'], df['volume']
        ma_fast = close.rolling(20).mean()
        ma_slow = close.rolling(60).mean()

        h, l, c = df['high'], df['low'], df['close']
        pc = c.shift(1)
        tr = pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
        atr = tr.ewm(alpha=1/14, adjust=False).mean()
        atr_val = float(atr.iloc[-1])
        cur_price = float(close.iloc[-1])

        # ATR이 0이거나 데이터 부족으로 NaN이면 가격의 0.3%를 대체값으로 사용
        # (예전 버전은 이 경우 그리드 6단계가 전부 같은 값으로 겹쳐버렸음)
        if not atr_val or np.isnan(atr_val) or atr_val <= 0:
            atr_val = cur_price * 0.003
            logger.warning("⚠️  ATR 계산값이 0/NaN → 가격의 0.3%로 대체")

        slope = ma_fast.diff(5) / ma_fast.shift(5)
        slope_val = float(slope.iloc[-1]) if not pd.isna(slope.iloc[-1]) else 0.0

        vol_5, vol_20 = volume.rolling(5).mean(), volume.rolling(20).mean()
        vol_trend = float((vol_5 / vol_20.replace(0, np.nan)).fillna(1.0).iloc[-1])

        ma_f, ma_s = float(ma_fast.iloc[-1]), float(ma_slow.iloc[-1])
        if pd.isna(ma_f) or pd.isna(ma_s):
            regime, direction, prob = 'SIDEWAYS', 'SIDEWAYS', 0.5
        else:
            if ma_f > ma_s and slope_val > 0.005:
                regime = 'TREND_UP'
            elif ma_f < ma_s and slope_val < -0.005:
                regime = 'TREND_DOWN'
            else:
                regime = 'SIDEWAYS'

            spread = (ma_f - ma_s) / atr_val
            prob_a = 1 / (1 + np.exp(-spread * 2))
            prob_b = 1 / (1 + np.exp(-slope_val * 200))
            vol_w = np.clip(vol_trend, 0.8, 1.2)
            combined = float(np.clip((prob_a * 0.5 + prob_b * 0.3) * vol_w, 0, 1))

            if combined > 0.55:
                direction, prob = 'UP', combined
            elif combined < 0.45:
                direction, prob = 'DOWN', 1.0 - combined
            else:
                direction, prob = 'SIDEWAYS', 0.5

        delta = close.diff()
        gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
        loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
        rsi_raw = (100 - 100 / (1 + gain / loss.replace(0, np.nan))).iloc[-1]
        rsi = float(rsi_raw) if not pd.isna(rsi_raw) else 50.0

        result = {
            'regime': regime, 'direction': direction, 'prob': round(prob, 4),
            'price': cur_price, 'atr': atr_val, 'atr_pct': round(atr_val / cur_price * 100, 2),
            'rsi': round(rsi, 1), 'vol_trend': round(vol_trend, 2),
            'slope': round(slope_val * 100, 3), 'sentiment': None,
        }

        if collect_sentiment:
            try:
                sent = SentimentCollector().collect_all(cur_price)
                result['sentiment'] = sent
            except Exception as e:
                logger.warning(f"센티멘트 수집 건너뜀: {e}")

        return result

    @staticmethod
    def print_status(info: dict):
        icon = {'TREND_UP': '📈', 'SIDEWAYS': '➡️', 'TREND_DOWN': '📉'}.get(info['regime'], '❓')
        print("\n" + "━" * 50)
        print(f"  📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"  💰 현재가:  ₩{info['price']:>15,.0f}")
        print(f"  {icon} 레짐:    {info['regime']}  (확률 {info['prob']:.3f})")
        print(f"  📊 RSI:     {info['rsi']:.1f}   📏 ATR: ₩{info['atr']:,.0f} ({info['atr_pct']:.2f}%)")
        if info.get('sentiment'):
            s = info['sentiment']
            print(f"  📡 센티멘트: {s['sentiment']} (점수 {s['composite_score']:+.3f}, {s['data_quality']})")
        print("━" * 50)


# ============================================================
# 그리드 엔진
# ============================================================
class GridEngine:
    """
    동적 그리드 트레이딩.

    기존 버전과 다른 점 (실행 테스트로 발견한 문제 수정):
      1. 그리드 일부만 체결된 채 방치되지 않도록, 가격이 중심가에서
         RECENTER_MULT × 간격 이상 벗어나면 자동으로 취소 후 재구성.
      2. 매도 체결까지 완료되면 해당 레벨을 grid_orders에서 아예 제거해
         같은 가격대를 다시 쓸 수 있게 함 (예전엔 'filled' 상태로 영구 점유).
      3. 그리드 간격이 왕복 수수료보다 작아지지 않도록 최소 간격을 강제.
    """
    def __init__(self, connector: UpbitConnector):
        self.connector    = connector
        self.grid_orders  = {}      # {price_key: order_info}
        self.grid_center  = None    # 마지막으로 그리드를 짠 기준가
        self.grid_interval = None
        self.realized_pnl = 0.0
        self.trade_log    = []
        self._load_state()

    def _load_state(self):
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                state = json.load(f)
                self.grid_orders   = state.get('grid_orders', {})
                self.grid_center   = state.get('grid_center')
                self.grid_interval = state.get('grid_interval')
                self.realized_pnl  = state.get('realized_pnl', 0.0)
                self.trade_log     = state.get('trade_log', [])
                logger.info(f"✅ 이전 상태 복원: 그리드 {len(self.grid_orders)}개, "
                            f"누적손익 ₩{self.realized_pnl:,.0f}")
        except FileNotFoundError:
            pass

    def _save_state(self):
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump({
                'grid_orders':   self.grid_orders,
                'grid_center':   self.grid_center,
                'grid_interval': self.grid_interval,
                'realized_pnl':  self.realized_pnl,
                'trade_log':     self.trade_log[-200:],  # 로그 무한 증식 방지
                'updated_at':    datetime.now().isoformat(),
            }, f, ensure_ascii=False, indent=2)

    def _effective_interval(self, market_info: dict, regime: str) -> float:
        price, atr = market_info['price'], market_info['atr']
        base = atr * (0.4 if regime == 'TREND_DOWN' else GRID_ATR_MULT)
        # 수수료(왕복 약 0.1%)보다 확실히 큰 마진을 남기도록 최소 간격 강제
        min_interval = price * GRID_MIN_PCT
        return max(base, min_interval)

    def build_grid(self, market_info: dict, regime: str) -> List[dict]:
        price = market_info['price']
        interval = self._effective_interval(market_info, regime)

        capital = CAPITAL * GRID_CAPITAL_PCT
        if regime == 'TREND_DOWN':
            capital *= 0.5  # 하락 추세에서는 노출 축소

        per_level = capital / GRID_LEVELS
        levels = []
        for i in range(1, GRID_LEVELS + 1):
            buy_price = price - interval * i
            sell_price = buy_price + interval
            if buy_price > 0 and per_level >= MIN_ORDER_KRW:
                levels.append({
                    'buy_price':  round(buy_price, -3),
                    'sell_price': round(sell_price, -3),
                    'amount_krw': per_level,
                })

        self.grid_center = price
        self.grid_interval = interval
        logger.info(f"📐 그리드 생성: {len(levels)}레벨 | 간격 ₩{interval:,.0f} "
                    f"({interval/price*100:.2f}%) | 레벨당 ₩{per_level:,.0f}")
        return levels

    def needs_recenter(self, current_price: float) -> bool:
        """가격이 그리드 중심에서 너무 멀어지면 재구성이 필요함을 판단"""
        if self.grid_center is None or self.grid_interval is None:
            return True
        drift = abs(current_price - self.grid_center)
        return drift > RECENTER_MULT * self.grid_interval

    def place_grid_orders(self, grid_levels: List[dict]):
        placed = 0
        for level in grid_levels:
            price_key = str(level['buy_price'])
            if price_key in self.grid_orders:
                continue
            order = self.connector.place_limit_buy(level['buy_price'], level['amount_krw'])
            if order:
                self.grid_orders[price_key] = {
                    'order_id':   order.get('id', ''),
                    'buy_price':  level['buy_price'],
                    'sell_price': level['sell_price'],
                    'amount_krw': level['amount_krw'],
                    'status':     'open',
                    'placed_at':  datetime.now().isoformat(),
                }
                placed += 1
                time.sleep(0.2)
        self._save_state()
        logger.info(f"✅ 그리드 주문 등록: {placed}개")

    def _record_trade(self, buy_price, sell_price, qty):
        """
        buy_price가 None이면(= 재시작 시 거래소에서 그대로 가져온, 매수단가를
        모르는 매도포지션) 손익 계산을 하지 않고 매출만 기록한다. 모르는 값을
        추정해서 realized_pnl에 섞는 것보다, 모른다고 명확히 남기는 쪽이 안전하다.
        """
        if buy_price is None:
            self.trade_log.append({
                'buy': None, 'sell': sell_price, 'qty': qty,
                'pnl': None, 'note': '재시작 시 거래소에서 그대로 가져온 주문 — 매수단가 불명, 손익 계산 생략',
                'at': datetime.now().isoformat(),
            })
            logger.warning(f"  ⚠️  매수단가 불명 포지션 매도 완료 (₩{sell_price:,.0f} × {qty:.8f}BTC) — 손익 미집계")
            return
        pnl = (sell_price - buy_price) * qty - (buy_price + sell_price) * qty * FEE_RATE
        self.realized_pnl += pnl
        self.trade_log.append({
            'buy': buy_price, 'sell': sell_price, 'qty': qty,
            'pnl': round(pnl, 0), 'at': datetime.now().isoformat(),
        })
        logger.info(f"  💵 확정손익 ₩{pnl:,.0f} | 누적손익 ₩{self.realized_pnl:,.0f}")

    def check_fills_and_place_sells(self, current_price: float):
        """
        매수 체결 확인 → 매도 등록 → 매도 체결 확인 → 레벨 회수(재사용 가능하게).

        실거래 모드에서는 항상 거래소의 실제 주문 상태를 다시 조회해서 판단하고
        (로컬 상태를 그냥 믿지 않음), 그 주문이 외부(업비트 앱 등)에서 취소된
        경우에도 이미 체결된 부분(partial fill)이 있으면 버리지 않고 매도
        대기열(sell_retry)로 넘겨 회수한다.
        """
        for price_key, info in list(self.grid_orders.items()):

            if info['status'] == 'open':
                buy_price = info['buy_price']
                if not self.connector.has_key:
                    if current_price <= buy_price:
                        info['qty'] = (info['amount_krw'] * (1 - FEE_RATE)) / buy_price
                        self._on_buy_filled(price_key, info)
                    continue

                o = self.connector.fetch_order(info['order_id'])
                if o is None:
                    continue  # 조회 실패 — 다음 사이클에 재시도, 상태는 건드리지 않음
                status = o.get('status')
                filled_amt = float(o.get('filled') or 0)

                if status == 'closed':
                    info['qty'] = filled_amt if filled_amt > 0 else \
                        (info['amount_krw'] * (1 - FEE_RATE)) / buy_price
                    self._on_buy_filled(price_key, info)
                elif status == 'canceled':
                    if filled_amt > 0:
                        logger.warning(
                            f"⚠️  매수주문이 거래소에서 외부적으로 취소됨(₩{buy_price:,.0f}), "
                            f"체결분 {filled_amt:.8f}BTC는 회수해서 매도 대기열로 전환합니다."
                        )
                        info['qty'] = filled_amt
                        info['status'] = 'sell_retry'
                    else:
                        logger.info(f"매수주문이 거래소에서 외부적으로 취소됨(체결 없음, ₩{buy_price:,.0f}) → 레벨 제거")
                        del self.grid_orders[price_key]
                # status == 'open' (부분체결 진행중 포함) → 그대로 대기

            elif info['status'] == 'sell_retry':
                sell_order = self.connector.place_limit_sell(info['sell_price'], info.get('qty', 0))
                if sell_order:
                    info['status'] = 'pending_sell'
                    info['sell_order_id'] = sell_order.get('id', '')

            elif info['status'] == 'pending_sell':
                if not self.connector.has_key:
                    if current_price >= info['sell_price']:
                        self._record_trade(info.get('buy_price'), info['sell_price'], info['qty'])
                        del self.grid_orders[price_key]
                    continue

                o = self.connector.fetch_order(info['sell_order_id'])
                if o is None:
                    continue
                status = o.get('status')
                filled_amt = float(o.get('filled') or 0)

                if status == 'closed':
                    self._record_trade(info.get('buy_price'), info['sell_price'], info['qty'])
                    del self.grid_orders[price_key]   # 레벨 회수 → 같은 가격 재사용 가능
                elif status == 'canceled':
                    remaining = max(info['qty'] - filled_amt, 0)
                    if filled_amt > 0:
                        logger.warning(
                            f"⚠️  매도주문이 거래소에서 외부적으로 취소됨(₩{info['sell_price']:,.0f}), "
                            f"{filled_amt:.8f}BTC는 이미 팔림 — 부분 확정, 나머지 {remaining:.8f}BTC 재매도 시도"
                        )
                        self._record_trade(info.get('buy_price'), info['sell_price'], filled_amt)
                    if remaining > 0:
                        info['qty'] = remaining
                        info['status'] = 'sell_retry'
                    else:
                        del self.grid_orders[price_key]
                # status == 'open' → 그대로 대기

        self._save_state()

    def _on_buy_filled(self, price_key: str, info: dict):
        buy_price = info['buy_price']
        logger.info(f"[체결] 매수 ₩{buy_price:,.0f} × {info['qty']:.8f}BTC")
        sell_order = self.connector.place_limit_sell(info['sell_price'], info['qty'])
        if sell_order:
            info['status'] = 'pending_sell'
            info['sell_order_id'] = sell_order.get('id', '')
        else:
            info['status'] = 'sell_retry'  # 매도 등록 실패(최소주문금액 미달 등) → 다음 사이클 재시도

    def cancel_all(self):
        """
        미체결 매수 주문만 취소. (체결 후 매도 대기중인 건 남겨서 익절 기회 유지 —
        정상적인 그리드 재중심 때 쓰는 취소이지 전량 청산이 아님. 손절 시에는
        liquidate_all()을 쓸 것.)

        부분체결된 상태로 취소된 주문은 조용히 버리지 않고 sell_retry로 돌려
        다음 사이클에 매도를 다시 시도하게 한다.
        """
        cancelled = 0
        for price_key, info in list(self.grid_orders.items()):
            if info['status'] == 'open':
                filled_qty = self.connector.cancel_order(info.get('order_id', ''))
                if filled_qty is None:
                    logger.error(f"주문 취소 실패, 다음 사이클에 재시도: ₩{info['buy_price']:,.0f}")
                    continue
                if filled_qty > 0:
                    info['qty'] = filled_qty
                    info['status'] = 'sell_retry'
                else:
                    del self.grid_orders[price_key]
                cancelled += 1
                time.sleep(0.1)
        self._save_state()
        logger.info(f"🛑 미체결 매수 취소: {cancelled}개")

    def liquidate_all(self):
        """
        손절/완전청산 전용. cancel_all()과 달리 '매도 대기중'(pending_sell) 주문도
        같이 취소해서 그 BTC를 자유잔고로 되돌린다 — 그래야 뒤이어 호출하는
        시장가 전량매도가 실제로 전량을 처리할 수 있다. cancel_all()만 쓰면
        pending_sell에 걸린 BTC가 손절 이후에도 그대로 시장에 노출된 채 남는다.
        """
        n = 0
        for price_key, info in list(self.grid_orders.items()):
            status = info['status']
            if status == 'open':
                filled_qty = self.connector.cancel_order(info.get('order_id', ''))
                if filled_qty is None:
                    logger.error(f"❌ 청산 중 매수취소 실패(수동 확인 필요): ₩{info['buy_price']:,.0f}")
                    continue
                if filled_qty > 0:
                    logger.warning(f"⚠️  청산 중 부분체결 회수: {filled_qty:.8f}BTC (뒤이은 시장가 매도에 포함됨)")
                del self.grid_orders[price_key]
                n += 1
            elif status == 'pending_sell':
                filled_qty = self.connector.cancel_order(info.get('sell_order_id', ''))
                if filled_qty is None:
                    logger.error(
                        f"❌ 청산 중 매도취소 실패(수동 확인 필요): ₩{info['sell_price']:,.0f} "
                        f"— BTC가 여전히 매도주문에 묶여있을 수 있습니다."
                    )
                    continue
                del self.grid_orders[price_key]
                n += 1
            elif status == 'sell_retry':
                del self.grid_orders[price_key]
                n += 1
            time.sleep(0.1)
        self._save_state()
        logger.info(f"🧹 전량 청산 정리: {n}건 취소/회수 완료 (남은 BTC는 이어서 시장가로 매도)")

    def reconcile_with_exchange(self):
        """
        재시작 시 로컬 상태(grid_state.json)와 거래소의 실제 상태를 대조한다.
        모의 모드에서는 대조할 실제 거래소 상태가 없으므로 아무 일도 하지 않는다.

          1. 로컬에 '진행 중'으로 기록된 주문들을 하나씩 실제 상태로 재조회해서
             프로그램이 꺼져 있던 동안 체결/취소/부분체결된 것들을 반영한다.
          2. 거래소에는 실제로 열려 있는데 로컬 상태 파일에는 전혀 없는 주문
             (state 파일 유실, 다른 곳에서 직접 주문 등)을 찾아서 로컬에
             편입시킨다 — 이게 없으면 그 주문은 프로그램에게 영원히 보이지 않고,
             재중심/손절 때도 취소 대상에서 빠진다.
        """
        if not self.connector.has_key:
            return

        logger.info("🔄 재시작 대조: 거래소의 실제 주문 상태와 로컬 상태를 비교합니다...")
        before = len(self.grid_orders)

        # 1) 로컬에 있는 항목들 재확인 — check_fills_and_place_sells와 동일한 로직을
        #    쓰면 되므로, current_price 없이도 처리 가능한 상태전이만 먼저 정리한다.
        for price_key, info in list(self.grid_orders.items()):
            if info['status'] == 'open':
                o = self.connector.fetch_order(info.get('order_id', ''))
                if o is None:
                    logger.warning(f"  ⚠️  로컬에만 있는 매수주문 조회 실패(거래소에 없을 수 있음): {price_key}")
                    continue
                status, filled_amt = o.get('status'), float(o.get('filled') or 0)
                if status == 'closed':
                    logger.info(f"  ↳ 오프라인 중 매수 체결됨: ₩{info['buy_price']:,.0f} → 다음 사이클에 매도 등록")
                    info['qty'] = filled_amt if filled_amt > 0 else \
                        (info['amount_krw'] * (1 - FEE_RATE)) / info['buy_price']
                elif status == 'canceled':
                    if filled_amt > 0:
                        logger.warning(f"  ↳ 오프라인 중 매수 부분체결 후 취소됨: {filled_amt:.8f}BTC 회수")
                        info['qty'] = filled_amt
                        info['status'] = 'sell_retry'
                    else:
                        logger.info(f"  ↳ 오프라인 중 매수 취소됨(체결 없음): ₩{info['buy_price']:,.0f} → 레벨 제거")
                        del self.grid_orders[price_key]
            elif info['status'] == 'pending_sell':
                o = self.connector.fetch_order(info.get('sell_order_id', ''))
                if o is None:
                    logger.warning(f"  ⚠️  로컬에만 있는 매도주문 조회 실패(거래소에 없을 수 있음): {price_key}")
                    continue
                status, filled_amt = o.get('status'), float(o.get('filled') or 0)
                if status == 'canceled' and filled_amt == 0:
                    logger.warning(f"  ↳ 오프라인 중 매도 취소됨: ₩{info['sell_price']:,.0f} → 재매도 대기열로 전환")
                    info['status'] = 'sell_retry'
                elif status == 'canceled' and filled_amt > 0:
                    remaining = max(info['qty'] - filled_amt, 0)
                    logger.warning(f"  ↳ 오프라인 중 매도 부분체결 후 취소됨: {filled_amt:.8f}BTC 확정 판매, 나머지 {remaining:.8f}BTC 재매도")
                    self._record_trade(info.get('buy_price'), info['sell_price'], filled_amt)
                    if remaining > 0:
                        info['qty'] = remaining
                        info['status'] = 'sell_retry'
                    else:
                        del self.grid_orders[price_key]
                # 'closed'(완전 매도 완료)는 다음 check_fills_and_place_sells 사이클에서
                # 정상적으로 손익 기록 후 레벨 회수됨 — 여기선 그대로 둔다.

        # 2) 거래소에는 있는데 로컬엔 없는 주문 — import
        known_ids = set()
        for info in self.grid_orders.values():
            if info.get('order_id'):
                known_ids.add(info['order_id'])
            if info.get('sell_order_id'):
                known_ids.add(info['sell_order_id'])

        exchange_orders = self.connector.get_open_orders()
        imported = 0
        for o in exchange_orders:
            oid = o.get('id')
            if not oid or oid in known_ids:
                continue
            side = o.get('side')
            price = float(o.get('price') or 0)
            amount = float(o.get('amount') or 0)
            if price <= 0 or amount <= 0:
                continue
            key = f"imported_{oid}"
            if side == 'buy':
                self.grid_orders[key] = {
                    'order_id': oid, 'buy_price': price,
                    'sell_price': round(price * (1 + GRID_MIN_PCT), -3),
                    'amount_krw': price * amount, 'status': 'open',
                    'placed_at': datetime.now().isoformat(),
                    'note': '재시작 대조 중 거래소에서 발견되어 자동 편입된 주문',
                }
            elif side == 'sell':
                self.grid_orders[key] = {
                    'order_id': '', 'sell_order_id': oid,
                    'buy_price': None,  # 매수단가 불명 — _record_trade가 손익집계 생략
                    'sell_price': price, 'qty': amount, 'status': 'pending_sell',
                    'placed_at': datetime.now().isoformat(),
                    'note': '재시작 대조 중 거래소에서 발견되어 자동 편입된 주문 (매수단가 불명)',
                }
            else:
                continue
            imported += 1
            logger.warning(
                f"  ⚠️  로컬에 없던 미체결 {side}주문을 발견해 편입했습니다: "
                f"₩{price:,.0f} × {amount:.8f}BTC (주문ID {oid}). "
                f"업비트 앱에서 이 주문이 맞는지 꼭 확인하세요."
            )

        self._save_state()
        after = len(self.grid_orders)
        logger.info(
            f"✅ 대조 완료: 로컬 {before}개 → {after}개 "
            f"(거래소에서 새로 편입 {imported}개). risk_state.json 기준 평가자산도 다시 확인하세요."
        )

    def get_summary(self) -> dict:
        total = len(self.grid_orders)
        by_status = {}
        for v in self.grid_orders.values():
            by_status[v['status']] = by_status.get(v['status'], 0) + 1
        return {'total': total, **by_status}

    def btc_in_flight(self) -> float:
        """체결됐지만 아직 안 팔린 BTC 수량 (평가자산 계산용)"""
        return sum(v.get('qty', 0) for v in self.grid_orders.values()
                   if v['status'] in ('pending_sell', 'sell_retry'))

    def backtest(self, df: pd.DataFrame, regime: str = 'SIDEWAYS',
                 rebuild_every: int = 20) -> dict:
        """
        그리드 백테스트. 예전 버전은 그리드를 처음 한 번만 짜고 다시 안 짜서
        가격이 범위를 벗어나면 그 뒤로는 거래가 아예 멈췄음.
        여기서는 rebuild_every 캔들마다 현재가 기준으로 재구성한다.
        """
        krw, btc = CAPITAL, 0.0
        trades, eq_curve = [], [krw]
        open_levels: Dict[str, dict] = {}   # buy_price_str -> {sell_price, qty, status}

        warmup = 60
        for i in range(warmup, len(df)):
            window = df.iloc[max(0, i - warmup):i + 1]
            price = float(df['close'].iloc[i])
            low, high = float(df['low'].iloc[i]), float(df['high'].iloc[i])

            if (i - warmup) % rebuild_every == 0:
                info = MarketAnalyzer.analyze(window, collect_sentiment=False)
                interval = max(info['atr'] * (0.4 if regime == 'TREND_DOWN' else GRID_ATR_MULT),
                              price * GRID_MIN_PCT)
                capital = CAPITAL * GRID_CAPITAL_PCT * (0.5 if regime == 'TREND_DOWN' else 1.0)
                per_level = capital / GRID_LEVELS
                if per_level >= MIN_ORDER_KRW:
                    for lv in range(1, GRID_LEVELS + 1):
                        bp = round(price - interval * lv, -3)
                        sp = round(bp + interval, -3)
                        key = str(bp)
                        if key not in open_levels:
                            open_levels[key] = {'sell_price': sp, 'amount_krw': per_level, 'status': 'open'}

            for key, lv in list(open_levels.items()):
                bp = float(key)
                if lv['status'] == 'open' and low <= bp and krw >= lv['amount_krw']:
                    qty = (lv['amount_krw'] * (1 - FEE_RATE)) / bp
                    krw -= lv['amount_krw']
                    btc += qty
                    lv['qty'] = qty
                    lv['status'] = 'holding'
                elif lv['status'] == 'holding' and high >= lv['sell_price']:
                    sell_val = lv['sell_price'] * lv['qty'] * (1 - FEE_RATE)
                    buy_val  = bp * lv['qty'] * (1 + FEE_RATE)
                    krw += sell_val
                    btc -= lv['qty']
                    trades.append({'pnl': sell_val - buy_val, 'buy': bp, 'sell': lv['sell_price']})
                    del open_levels[key]

            eq_curve.append(krw + btc * price)

        final_price = float(df['close'].iloc[-1])
        equity = krw + btc * final_price
        roi = (equity - CAPITAL) / CAPITAL * 100
        wins = [t for t in trades if t['pnl'] > 0]

        return {
            'roi': round(roi, 2), 'final_equity': round(equity, 0),
            'total_trades': len(trades), 'win_trades': len(wins),
            'winrate': round(len(wins) / len(trades) * 100, 1) if trades else 0,
            'avg_pnl': round(float(np.mean([t['pnl'] for t in trades])), 0) if trades else 0,
        }


# ============================================================
# 리스크 매니저 (원금 보호 / 시드 출금 처리)
# ============================================================
class RiskManager:
    """
    두 가지 일을 한다:
      1. 손절: 평가자산이 '현재 사이클 기준선'의 STOP_LOSS_PCT 밑으로
         떨어지면 전량 취소+매도 후 정지.
      2. 시드 출금: 평가자산이 '기준선 × WITHDRAW_MULTIPLE'에 도달하면
         기준선만큼(=시드) 출금하고, 봇은 정지하지 않고 나머지로 계속 매매.
         기준선은 출금이 성공할 때마다 그 시점의 잔여 평가자산으로 갱신되어,
         "항상 시드 5만원으로 굴리다가 2배 되면 5만원 빼는" 사이클을 반복한다.
    """
    def __init__(self, connector: UpbitConnector, grid: GridEngine, initial_capital: float):
        self.connector = connector
        self.grid = grid
        self.initial_capital = initial_capital
        self.halted = False
        self.baseline = initial_capital       # 이번 사이클의 기준 시드
        self.total_withdrawn = 0.0
        self.last_alert_at = 0.0
        self._load_state()

    def _load_state(self):
        try:
            with open(RISK_STATE_FILE, 'r', encoding='utf-8') as f:
                state = json.load(f)
                self.baseline = state.get('baseline', self.initial_capital)
                self.total_withdrawn = state.get('total_withdrawn', 0.0)
                logger.info(f"✅ 출금상태 복원: 기준선 ₩{self.baseline:,.0f}, "
                            f"누적출금 ₩{self.total_withdrawn:,.0f}")
        except FileNotFoundError:
            pass

    def _save_state(self):
        with open(RISK_STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump({
                'baseline': self.baseline,
                'total_withdrawn': self.total_withdrawn,
                'updated_at': datetime.now().isoformat(),
            }, f, ensure_ascii=False, indent=2)

    def get_equity(self, current_price: float) -> float:
        balance = self.connector.get_balance()
        btc_qty = balance['BTC'] if self.connector.has_key else self.grid.btc_in_flight()
        krw = balance['KRW'] if self.connector.has_key else (
            self.initial_capital - sum(
                v['amount_krw'] for v in self.grid.grid_orders.values()
                if v['status'] in ('pending_sell', 'sell_retry')
            ) + self.grid.realized_pnl
        )
        return krw + btc_qty * current_price

    def check_stop_loss(self, current_price: float, equity: float) -> bool:
        """True면 정상 진행, False면 손절 발동으로 이번 사이클 중단"""
        stop_line = self.baseline * STOP_LOSS_PCT
        if equity <= stop_line:
            logger.error(
                f"🛑 손절선 도달! 평가자산 ₩{equity:,.0f} <= 손절선 ₩{stop_line:,.0f} "
                f"(기준선의 {STOP_LOSS_PCT*100:.0f}%). 전량 청산 후 정지합니다."
            )
            # cancel_all()이 아니라 liquidate_all()을 쓴다: pending_sell(매도 대기)에
            # 걸린 BTC까지 전부 회수해야, 뒤이은 시장가 매도가 진짜 "전량"이 된다.
            self.grid.liquidate_all()
            balance = self.connector.get_balance()
            self.connector.sell_all_market(balance['BTC'])
            self.halted = True
            return False
        return True

    def check_withdraw(self, current_price: float, equity: float):
        """
        평가자산이 기준선×WITHDRAW_MULTIPLE에 도달하면:
          - AUTO_WITHDRAW_ENABLED=true : 실제 출금 API 호출까지 자동 수행
          - false(기본값)              : 반복 알림만 하고, 사람이 수동으로
                                          업비트 앱에서 출금 후 --confirm-withdrawal 실행
        """
        trigger = self.baseline * WITHDRAW_MULTIPLE
        if equity < trigger:
            return

        seed = self.baseline

        if not AUTO_WITHDRAW_ENABLED:
            now = time.time()
            if now - self.last_alert_at >= WITHDRAW_ALERT_COOLDOWN_SEC:
                logger.info(
                    f"🎯 목표 도달! 평가자산 ₩{equity:,.0f} >= ₩{trigger:,.0f} "
                    f"(시드 ₩{seed:,.0f}의 {WITHDRAW_MULTIPLE}배). "
                    f"업비트 앱에서 ₩{seed:,.0f}을 수동으로 출금한 뒤, "
                    f"'python grid_engine.py --confirm-withdrawal'을 실행해서 "
                    f"기준선을 리셋해주세요. 매매는 계속 진행됩니다."
                )
                self.last_alert_at = now
            return

        logger.info(f"🎯 목표 도달! 평가자산 ₩{equity:,.0f} → 시드 ₩{seed:,.0f} 자동 출금을 시도합니다.")
        balance = self.connector.get_balance()
        if balance['KRW'] < seed:
            shortfall = seed - balance['KRW']
            logger.info(f"현금이 부족(₩{balance['KRW']:,.0f})하여 ₩{shortfall:,.0f}만큼 BTC 시장가 매도로 확보합니다.")
            self.grid.cancel_all()
            self.connector.sell_market_krw(shortfall, current_price)
            balance = self.connector.get_balance()

        if balance['KRW'] < seed:
            logger.warning(f"⚠️  출금 재원 확보 실패 (KRW ₩{balance['KRW']:,.0f} < 시드 ₩{seed:,.0f}). 다음 사이클에 재시도합니다.")
            return

        result = self.connector.withdraw_krw(seed)
        if result:
            # 출금 직후에는 거래소 잔고에 아직 반영 안 됐을 수 있어(처리 지연),
            # 재조회 대신 방금 계산한 equity에서 출금액을 직접 차감한다.
            self.confirm_withdrawal(seed, current_price, source='auto', equity_before=equity)

    def confirm_withdrawal(self, amount: float, current_price: float,
                           source: str = 'manual', equity_before: Optional[float] = None):
        """
        출금(수동/자동) 완료를 확정하고 다음 사이클의 기준선을 재설정.

        - source='auto' (봇이 방금 출금 API를 호출한 직후): equity_before에
          "출금 API 호출 *전*에 계산해둔 평가자산"을 넘겨받는다. 거래소 잔고에는
          아직 출금이 반영되지 않았을 수 있으므로 amount를 직접 빼서 추정한다.
        - source='manual' (--confirm-withdrawal, 사용자가 이미 실제로 출금을 마친 뒤
          실행): equity_before를 넘기지 않는다. 이 시점에 조회되는 실제 잔고는
          이미 출금이 반영된 값이므로, amount를 또 빼면 이중 차감이 된다.
          현재 평가자산을 그대로 기준선으로 쓴다.
        """
        self.total_withdrawn += amount
        if equity_before is not None:
            remaining_equity = equity_before - amount
        else:
            remaining_equity = self.get_equity(current_price)
        self.baseline = max(remaining_equity, CAPITAL * 0.5)  # 너무 작아지지 않도록 하한 보호
        self._save_state()
        logger.info(
            f"✅ 출금 확정({source}): ₩{amount:,.0f} | 누적출금 ₩{self.total_withdrawn:,.0f} | "
            f"새 기준선 ₩{self.baseline:,.0f}로 계속 매매합니다."
        )

    def check(self, current_price: float) -> bool:
        """1사이클에 필요한 리스크 체크를 순서대로 수행. False면 이번 사이클 중단."""
        equity = self.get_equity(current_price)
        if not self.check_stop_loss(current_price, equity):
            return False
        self.check_withdraw(current_price, equity)
        logger.info(f"  💰 평가자산: ₩{equity:,.0f}  (기준선 대비 {equity/self.baseline*100:.1f}%, "
                    f"누적출금 ₩{self.total_withdrawn:,.0f})")
        return True


# ============================================================
# 오케스트레이터
# ============================================================
class GridBot:
    def __init__(self):
        self.connector = UpbitConnector()
        self.grid = GridEngine(self.connector)
        # 로컬 상태 파일을 그대로 믿지 않고, 재시작할 때마다 거래소의 실제 주문
        # 상태와 반드시 대조한다 (꺼져 있던 동안 체결/취소/부분체결된 것 반영 +
        # 로컬에 없는 미체결 주문 편입).
        self.grid.reconcile_with_exchange()
        balance = self.connector.get_balance()
        # 실제 잔고가 설정값보다 적으면 실제 잔고 기준으로 방어적으로 운용
        self.initial_capital = min(CAPITAL, balance['KRW']) if self.connector.has_key else CAPITAL
        self.risk = RiskManager(self.connector, self.grid, self.initial_capital)
        self._stop = False
        signal.signal(signal.SIGINT, self._handle_stop)
        signal.signal(signal.SIGTERM, self._handle_stop)

    def _handle_stop(self, signum, frame):
        logger.info("⏹️  종료 신호 수신 → 현재 상태 저장 후 종료 (미체결 주문은 그대로 유지됩니다)")
        self._stop = True

    def run_once(self):
        df = self.connector.fetch_ohlcv(limit=150)
        info = MarketAnalyzer.analyze(df)
        MarketAnalyzer.print_status(info)

        if not self.risk.check(info['price']):
            return

        regime = info['regime']
        if self.grid.needs_recenter(info['price']):
            logger.info(f"↔️  가격이 그리드 범위를 벗어남 → 재중심 (레짐: {regime})")
            self.grid.cancel_all()
            levels = self.grid.build_grid(info, regime)
            self.grid.place_grid_orders(levels)
        else:
            summary = self.grid.get_summary()
            logger.info(f"  기존 그리드 유지: {summary}")

        self.grid.check_fills_and_place_sells(info['price'])

    def run_loop(self, interval_sec: int):
        logger.info(f"🚀 자동매매 시작 (주기 {interval_sec}초, 자본 ₩{self.initial_capital:,.0f})")
        while not self._stop:
            try:
                self.run_once()
            except Exception as e:
                logger.error(f"❌ 루프 오류: {e}", exc_info=True)
            if self.risk.halted:
                logger.info("🛑 손절선에 도달해 정지했습니다 (목표 도달로는 더 이상 정지하지 않습니다). "
                            "grid_state.json / risk_state.json을 확인하고 필요 시 수동으로 재시작하세요.")
                break
            for _ in range(interval_sec):
                if self._stop:
                    break
                time.sleep(1)
        logger.info("👋 종료되었습니다.")


# ============================================================
# 메인
# ============================================================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='설정값만 검증 (주문 없음)')
    parser.add_argument('--status', action='store_true', help='현재 시장 상태 확인')
    parser.add_argument('--once', action='store_true', help='1회 실행 후 종료')
    parser.add_argument('--backtest', action='store_true', help='그리드 백테스트')
    parser.add_argument('--interval', type=int, default=180, help='실행 주기(초), 기본 3분')
    parser.add_argument('--confirm-withdrawal', action='store_true',
                        help='업비트 앱에서 수동으로 시드를 출금했다면 실행 → 기준선 리셋')
    parser.add_argument('--withdraw-now', type=float, metavar='AMOUNT',
                        help='지정한 금액을 지금 즉시 실제 출금 API로 1회 테스트 실행 (자동루프 없이 단발성)')
    parser.add_argument('--reconcile', action='store_true',
                        help='루프를 돌리지 않고, 로컬 상태와 거래소 실제 주문만 대조하고 종료 (재시작 전 점검용)')
    parser.add_argument('--dry-run', action='store_true',
                        help='실제 API 키로 시세/잔고/미체결주문은 조회하되, 매수/매도/취소/출금은 '
                             '절대 보내지 않음 (실거래 투입 전 4단계: 연결 확인용)')
    args = parser.parse_args()

    if args.dry_run:
        global DRY_RUN
        DRY_RUN = True

    try:
        validate_config()
    except ConfigError as e:
        logger.error(str(e))
        sys.exit(1)

    if args.check:
        print("✅ 설정 검증 통과. --status 또는 --once로 다음 단계를 진행하세요.")
        return

    connector = UpbitConnector()

    if args.reconcile:
        if not connector.has_key:
            logger.error("❌ API 키 없이는 대조할 실제 거래소 주문이 없습니다.")
            sys.exit(1)
        grid = GridEngine(connector)
        grid.reconcile_with_exchange()
        print(f"✅ 대조 완료. 현재 상태: {grid.get_summary()}")
        return

    if args.withdraw_now is not None:
        if not connector.has_key:
            logger.error("❌ API 키 없이는 실제 출금을 테스트할 수 없습니다.")
            sys.exit(1)
        logger.info(f"🧪 출금 단발 테스트: ₩{args.withdraw_now:,.0f}")
        result = connector.withdraw_krw(args.withdraw_now)
        if result:
            print(f"✅ 출금 요청이 접수되었습니다. 업비트 앱에서 처리 상태를 확인하세요: {result}")
        else:
            print("❌ 출금 요청이 실패했습니다. 위 로그의 확인사항을 먼저 점검하세요.")
        return

    if args.confirm_withdrawal:
        grid = GridEngine(connector)
        info = MarketAnalyzer.analyze(connector.fetch_ohlcv(limit=150), collect_sentiment=False)
        balance = connector.get_balance()
        initial_capital = min(CAPITAL, balance['KRW']) if connector.has_key else CAPITAL
        risk = RiskManager(connector, grid, initial_capital)
        risk.confirm_withdrawal(CAPITAL, info['price'], source='manual')
        print(f"✅ 수동 출금이 확정되었습니다. 새 기준선: ₩{risk.baseline:,.0f}")
        return

    if args.status:
        df = connector.fetch_ohlcv(limit=150)
        info = MarketAnalyzer.analyze(df)
        MarketAnalyzer.print_status(info)
        return

    if args.backtest:
        logger.info("🧪 그리드 백테스트 시작")
        df = connector.fetch_ohlcv(limit=1500)
        grid = GridEngine(connector)
        for regime in ['SIDEWAYS', 'TREND_DOWN']:
            result = grid.backtest(df, regime)
            print(f"\n{'━'*40}\n  그리드 백테스트: {regime}")
            print(f"  ROI: {result['roi']:+.2f}%  |  최종자산: ₩{result['final_equity']:,.0f}")
            print(f"  거래: {result['total_trades']}회  |  승률: {result['winrate']:.1f}%")
            print(f"  평균손익: ₩{result['avg_pnl']:,.0f}\n{'━'*40}")
        return

    bot = GridBot()
    if args.once:
        bot.run_once()
    else:
        bot.run_loop(args.interval)


if __name__ == "__main__":
    main()
