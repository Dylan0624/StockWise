# src/output/suggestion.py
def generate_suggestion(analysis):
    """根據分析結果生成投資建議"""
    suggestion = f"股票 {analysis.get('stock_code', '未知')}:\n"
    if "price" in analysis:
        suggestion += f"最新股價: {analysis['price']} 元\n"
    if "pe_assessment" in analysis:
        suggestion += f"本益比: {analysis['pe_ratio']} - {analysis['pe_assessment']}\n"
    if "eps" in analysis:
        suggestion += f"每股盈餘: {analysis['eps']} - 顯示公司獲利能力穩定\n"
    if "volume" in analysis:
        suggestion += f"成交量: {analysis['volume']} 股\n"
    if "yield_assessment" in analysis:
        suggestion += f"殖利率: {analysis['yield_rate']}% - {analysis['yield_assessment']}\n"
    suggestion += "建議: 綜合評估基本面與市場趨勢後決定買賣策略。"
    return suggestion

if __name__ == "__main__":
    # 測試範例
    sample_analysis = {
        "stock_code": "2330", "price": 1095, "pe_ratio": 25, "pe_assessment": "偏高",
        "eps": 5.2, "volume": 30000000, "yield_rate": 2.5, "yield_assessment": "具吸引力"
    }
    print(generate_suggestion(sample_analysis))