# src/input/crawler.py
import yfinance as yf
from datetime import datetime
import pandas as pd

def fetch_yfinance_data(stock_code, period="3mo"):
    """從 yfinance 抓取台股數據，包括即時與歷史資訊"""
    stock = yf.Ticker(f"{stock_code}.TW")
    info = stock.info
    
    # 獲取最新數據的日期
    market_time = info.get("regularMarketTime")
    data_date = datetime.fromtimestamp(market_time).strftime('%Y-%m-%d') if market_time else None
    
    # 即時數據
    data = {
        "股票號碼": stock_code,
        "最新股價": info.get("regularMarketPrice"),
        "前日收盤價": info.get("previousClose"),
        "漲跌幅": info.get("regularMarketChangePercent"),
        "本益比": info.get("trailingPE"),
        "EPS": info.get("trailingEps"),
        "成交量": info.get("volume"),
        "平均成交量": info.get("averageVolume"),
        "殖利率": info.get("dividendYield", 0) * 100 if info.get("dividendYield") else None,
        "股利": info.get("dividendRate"),
        "市值": info.get("marketCap"),
        "52週高點": info.get("fiftyTwoWeekHigh"),
        "52週低點": info.get("fiftyTwoWeekLow"),
        "Beta": info.get("beta"),
        "數據日期": data_date
    }

    # 獲取近三個月歷史數據
    history = stock.history(period=period)
    if not history.empty:
        data["近三個月平均股價"] = history['Close'].mean()
        data["近三個月平均成交量"] = history['Volume'].mean()
        data["近三個月股價變化率"] = ((history['Close'].iloc[-1] - history['Close'].iloc[0]) / history['Close'].iloc[0]) * 100
        data["近三個月最高股價"] = history['Close'].max()
        data["近三個月最低股價"] = history['Close'].min()
        data["近三個月股價標準差"] = history['Close'].std()

    return {k: v for k, v in data.items() if v is not None}

if __name__ == "__main__":
    stock_data = fetch_yfinance_data("2330")
    print(stock_data)