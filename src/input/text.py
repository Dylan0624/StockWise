# src/input/text.py
from .crawler import fetch_stock_data

def read_text_input(file_path):
    """讀取文字檔案中的股票資料"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"檔案 {file_path} 不存在")
        return None

def parse_text_input(text):
    """解析文字輸入，返回字典格式"""
    data = {}
    for line in text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    return data

def get_stock_data(source="crawler", file_path=None, stock_code=None):
    """獲取股票數據，可從檔案或爬蟲取得"""
    if source == "file" and file_path:
        text = read_text_input(file_path)
        if text:
            return parse_text_input(text)
    elif source == "crawler" and stock_code:
        return fetch_stock_data(stock_code)
    return None

if __name__ == "__main__":
    # 測試從爬蟲獲取數據
    stock_data = get_stock_data(source="crawler", stock_code="2330")
    if stock_data:
        print(stock_data)

    # 測試從檔案獲取數據
    # stock_data = get_stock_data(source="file", file_path="data/text/sample.txt")
    # if stock_data:
    #     print(stock_data)