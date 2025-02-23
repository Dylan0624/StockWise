# src/output/suggestion.py
def generate_suggestion(analysis):
    """根據分析結果生成投資建議"""
    suggestion = f"股票 {analysis.get('stock_code', '未知')} ({analysis.get('data_date', '日期未知')}):\n"
    if "price" in analysis:
        suggestion += f"最新股價: {analysis['price']} 元\n"
    if "change_trend" in analysis:
        suggestion += f"漲跌幅: {analysis['change_pct']:.2f}% - {analysis['change_trend']}\n"
    if "pe_assessment" in analysis:
        suggestion += f"本益比: {analysis['pe_ratio']} - {analysis['pe_assessment']}\n"
    if "eps" in analysis:
        suggestion += f"每股盈餘: {analysis['eps']} - 顯示公司獲利能力穩定\n"
    if "volume_trend" in analysis:
        suggestion += f"成交量: {analysis['volume']} 股 - {analysis['volume_trend']}\n"
    if "yield_assessment" in analysis:
        suggestion += f"殖利率: {analysis['yield_rate']}% - {analysis['yield_assessment']}\n"
    if "dividend" in analysis:
        suggestion += f"年度股利: {analysis['dividend']} 元\n"
    if "market_cap" in analysis:
        suggestion += f"市值: {analysis['market_cap']:,} 元\n"
    if "year_high" in analysis and "year_low" in analysis:
        suggestion += f"52週區間: {analysis['year_low']} - {analysis['year_high']} 元\n"
    if "beta" in analysis:
        suggestion += f"Beta: {analysis['beta']} - {'高波動' if analysis['beta'] > 1 else '低波動'}\n"
    suggestion += "建議: 綜合評估基本面與市場趨勢後決定買賣策略。"
    return suggestion

if __name__ == "__main__":
    sample_analysis = {
        "stock_code": "2330", "data_date": "2025-02-23", "price": 1095, "prev_close": 1080,
        "change_pct": 1.39, "change_trend": "上漲", "pe_ratio": 25, "pe_assessment": "偏高",
        "eps": 5.2, "volume": 30000000, "avg_volume": 35000000, "volume_trend": "正常",
        "yield_rate": 2.5, "yield_assessment": "具吸引力", "dividend": 27, "market_cap": 28300000000000,
        "year_high": 1120, "year_low": 800, "beta": 1.08
    }
    print(generate_suggestion(sample_analysis))