import requests
from bs4 import BeautifulSoup
import sys

def fetch_stock_data(stock_code, debug=False):
    """從 Yahoo Finance 抓取台股最新資訊"""
    url = f"https://tw.stock.yahoo.com/quote/{stock_code}.TW"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        if debug:
            print("=== Debug: HTML 輸出 ===")
            print(soup.prettify())
            print("=== End Debug ===\n")

        # 提取數據
        data = {"股票號碼": stock_code}

        # 嘗試抓取最新股價 (請根據頁面實際狀況調整選擇器)
        price = soup.select_one("span[class*='Fw(600)']")
        if price:
            data["最新股價"] = price.text.strip().replace(",", "")

        # 抓取右側資訊區塊 (根據 id 選擇區塊，若找不到可啟用除錯輸出檢查 HTML)
        info_section = soup.find("section", id="quote-summary")
        if info_section:
            items = info_section.find_all("li")
            for item in items:
                label = item.find("span", class_="C(#6e7780)")
                value = item.find("span", class_="Fw(600)")
                if label and value:
                    label_text = label.text.strip()
                    value_text = value.text.strip().replace(",", "")
                    if "成交" in label_text:
                        data["成交量"] = value_text
                    elif "本益比" in label_text:
                        data["本益比"] = value_text
                    elif "殖利率" in label_text:
                        data["殖利率"] = value_text.replace("%", "")
                    elif "每股盈餘" in label_text:
                        data["EPS"] = value_text
        else:
            if debug:
                print("Debug: 未找到 'quote-summary' 區塊，請檢查 HTML 結構。")
                
        return data
    except requests.RequestException as e:
        print(f"無法抓取 {stock_code} 的數據: {e}")
        return None

if __name__ == "__main__":
    # 若命令列帶入 'debug' 參數，則開啟除錯模式
    debug_mode = len(sys.argv) > 1 and sys.argv[1] == "debug"
    
    # 測試爬取台積電 (2330) 的數據
    stock_data = fetch_stock_data("2330", debug=debug_mode)
    if stock_data:
        print("抓取結果：")
        print(stock_data)
