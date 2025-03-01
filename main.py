# main.py
from src.input.text import get_stock_data
from src.analysis.text_analyzer import analyze_text_data
from src.output.suggestion import generate_suggestion, generate_ollama_suggestion

def main():
    # 測試爬蟲獲取台股數據
    stock_data = get_stock_data(source="crawler", stock_code="1301")
    if stock_data:
        print("原始數據:", stock_data)
        
        # 分析數據
        analysis = analyze_text_data(stock_data)
        print("分析結果:", analysis)
        
        # 生成本地建議
        local_suggestion = generate_suggestion(analysis)
        print("本地投資建議:\n", local_suggestion)
        
        # 生成 Ollama 建議
        ollama_suggestion = generate_ollama_suggestion(analysis)
        print("\nOllama 投資建議:\n", ollama_suggestion)

if __name__ == "__main__":
    main()