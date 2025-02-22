# src/analysis/text_analyzer.py
def analyze_text_data(data):
    """分析文字數據，返回結構化結果"""
    analysis = {}
    if "股票號碼" in data:
        analysis["stock_code"] = data["股票號碼"]
    if "本益比" in data:
        pe_ratio = float(data["本益比"])
        analysis["pe_ratio"] = pe_ratio
        analysis["pe_assessment"] = "合理" if pe_ratio < 20 else "偏高"
    if "EPS" in data:
        analysis["eps"] = float(data["EPS"])
    return analysis

if __name__ == "__main__":
    # 測試範例
    sample_data = {"股票號碼": "2330", "本益比": "15", "EPS": "5.2"}
    result = analyze_text_data(sample_data)
    print(result)