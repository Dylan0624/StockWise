# src/output/suggestion.py
def generate_suggestion(analysis):
    """根據分析結果生成投資建議"""
    suggestion = f"股票 {analysis.get('stock_code', '未知')}:\n"
    if "pe_assessment" in analysis:
        suggestion += f"本益比 {analysis['pe_ratio']} - {analysis['pe_assessment']}。\n"
    if "eps" in analysis:
        suggestion += f"每股盈餘 {analysis['eps']} - 顯示公司獲利能力穩定。\n"
    suggestion += "建議: 進一步觀察基本面與技術面趨勢。"
    return suggestion

if __name__ == "__main__":
    # 測試範例
    sample_analysis = {"stock_code": "2330", "pe_ratio": 15, "pe_assessment": "合理", "eps": 5.2}
    print(generate_suggestion(sample_analysis))