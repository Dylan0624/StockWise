# src/input/crawler.py
import requests
from bs4 import BeautifulSoup

def fetch_stock_data(stock_code):
    """從 Yahoo Finance 抓取台股最新資訊"""
    url = f"https://tw.stock.yahoo.com/quote/{stock_code}.TW"  # .TW 是台股代碼後綴
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }  # 模擬瀏覽器避免被阻擋
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 檢查請求是否成功
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取關鍵數據（根據 Yahoo Finance 的 HTML 結構）
        data = {}
        data["股票號碼"] = stock_code
        
        # 股價（最新成交價）
        price = soup.select_one("span[class*='Fw(600)']")  # 可能需要根據實際 HTML 調整
        if price:
            data["最新股價"] = price.text.strip()

        # 本益比與 EPS（可能在其他區塊，需檢查 HTML）
        # 這裡簡化為假設數據在特定標籤中
        fundamentals = soup.select("li[class*='price-detail-item']")
        for item in fundamentals:
            label = item.find("span", class_="C(#6e7780)")
            value = item.find("span", class_="Fw(600)")
            if label and value:
                if "本益比" in label.text:
                    data["本益比"] = value.text.strip()
                elif "每股盈餘" in label.text:
                    data["EPS"] = value.text.strip()

        return data
    except requests.RequestException as e:
        print(f"無法抓取 {stock_code} 的數據: {e}")
        return None

if __name__ == "__main__":
    # 測試爬取台積電 (2330) 的數據
    stock_data = fetch_stock_data("2330")
    if stock_data:
        print(stock_data)