import yfinance as yf
import pandas as pd

# 1. 銘柄の設定（ここを好きな銘柄に変えてみてください）
# 米国株なら "AAPL", "TSLA" / 日本株なら "7203.T", "9984.T" など
symbol = "AAPL"
ticker = yf.Ticker(symbol)

print(f"--- {symbol} のデータ取得開始 ---")

# 2. 基礎情報の取得 (info)
# 業種や時価総額、PERなど膨大なデータが辞書形式で入っています
info = ticker.info
print(f"会社名: {info.get('longName')}")
print(f"業種: {info.get('industry')}")
print(f"現在のPER: {info.get('trailingPE')}")

# 3. 株価データの取得 (history)
# period: 1d, 5d, 1mo, 3mo, 1y, 2y, 5y, 10, ytd, max; (ytd is Year To Date(年初来))
# interval: 1m, 2m, 5m, 1h, 1d, 5d, 1wk, 1mo, 3mo
hist = ticker.history(period="1mo", interval="1d")
print("\n--- 直近5日間の株価 ---")
print(hist.tail())

# 4. 財務諸表の取得 (Financials)
# 損益計算書 (financials), 貸借対照表 (balance_sheet), キャッシュフロー (cashflow)
print("\n--- 直近の年間売上高 ---")
income_stmt = ticker.financials
print(income_stmt.loc['Total Revenue'] if 'Total Revenue' in income_stmt.index else "データなし")