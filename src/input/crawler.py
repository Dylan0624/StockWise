# src/input/crawler.py
import yfinance as yf
from datetime import datetime

def fetch_yfinance_data(stock_code):
    stock = yf.Ticker(f"{stock_code}.TW")
    info = stock.info
    
    # 獲取最新數據的日期
    market_time = info.get("regularMarketTime")
    data_date = datetime.fromtimestamp(market_time).strftime('%Y-%m-%d') if market_time else None
    
    data = {
        "股票號碼": stock_code,
        "最新股價": info.get("regularMarketPrice"),
        "前日收盤價": info.get("previousClose"),
        "漲跌幅": info.get("regularMarketChangePercent"),  # 當日漲跌百分比
        "本益比": info.get("trailingPE"),
        "EPS": info.get("trailingEps"),
        "成交量": info.get("volume"),
        "平均成交量": info.get("averageVolume"),  # 平均每日成交量
        "殖利率": info.get("dividendYield", 0) * 100 if info.get("dividendYield") else None,
        "股利": info.get("dividendRate"),  # 年度每股股利
        "市值": info.get("marketCap"),  # 單位：新台幣
        "52週高點": info.get("fiftyTwoWeekHigh"),
        "52週低點": info.get("fiftyTwoWeekLow"),
        "Beta": info.get("beta"),  # 波動性指標
        "數據日期": data_date
    }
    return {k: v for k, v in data.items() if v is not None}

if __name__ == "__main__":
    stock_data = fetch_yfinance_data("2330")
    print(stock_data)