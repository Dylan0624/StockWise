# main.py
from src.input.text import get_stock_data
from src.analysis.text_analyzer import analyze_text_data
from src.output.suggestion import generate_suggestion

def main():
    # 測試爬蟲獲取台股數據
    stock_data = get_stock_data(source="crawler", stock_code="2330")
    if stock_data:
        print("原始數據:", stock_data)
        
        # 分析數據
        analysis = analyze_text_data(stock_data)
        print("分析結果:", analysis)
        
        # 生成建議
        suggestion = generate_suggestion(analysis)
        print("投資建議:\n", suggestion)

if __name__ == "__main__":
    main()