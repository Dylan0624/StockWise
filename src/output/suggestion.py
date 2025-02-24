# src/output/suggestion.py
import ollama

def generate_suggestion(analysis):
    """根據分析結果生成投資建議（使用本地方法）"""
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
    if "three_month_avg_price" in analysis:
        suggestion += f"近三個月平均股價: {analysis['three_month_avg_price']:.2f} 元\n"
    if "three_month_volume_trend" in analysis:
        suggestion += f"近三個月平均成交量: {analysis['three_month_avg_volume']:,} 股 - {analysis['three_month_volume_trend']}\n"
    if "three_month_trend" in analysis:
        suggestion += f"近三個月股價變化: {analysis['three_month_change_pct']:.2f}% - {analysis['three_month_trend']}\n"
    if "three_month_high" in analysis and "three_month_low" in analysis:
        suggestion += f"近三個月價格區間: {analysis['three_month_low']} - {analysis['three_month_high']} 元\n"
    if "three_month_std" in analysis:
        suggestion += f"近三個月股價標準差: {analysis['three_month_std']:.2f} 元\n"
    suggestion += "建議: 綜合評估基本面與市場趨勢後決定買賣策略。"
    return suggestion

def generate_ollama_suggestion(analysis):
    """使用 Ollama 的 deepseek-r1:14b 生成完整的投資建議"""
    prompt = "以下是一隻股票的分析數據，請根據這些數據提供完整的投資建議（包括是否買入、賣出或持有，並解釋原因）：\n"
    for key, value in analysis.items():
        prompt += f"{key}: {value}\n"
    prompt += "\n請提供專業且具體的投資建議，並考慮基本面與技術面因素。"

    try:
        response = ollama.chat(
            model="deepseek-r1:14b",
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Ollama 服務異常: {e}"

if __name__ == "__main__":
    sample_analysis = {
        "stock_code": "2330", "data_date": "2025-02-23", "price": 1095, "prev_close": 1080,
        "change_pct": 1.39, "change_trend": "上漲", "pe_ratio": 25, "pe_assessment": "偏高",
        "eps": 5.2, "volume": 30000000, "avg_volume": 35000000, "volume_trend": "正常",
        "yield_rate": 2.5, "yield_assessment": "具吸引力", "dividend": 27, "market_cap": 28300000000000,
        "year_high": 1120, "year_low": 800, "beta": 1.08,
        "three_month_avg_price": 1050, "three_month_avg_volume": 32000000, "three_month_volume_trend": "減少",
        "three_month_change_pct": 4.5, "three_month_trend": "上升", "three_month_high": 1120, "three_month_low": 1000,
        "three_month_std": 50
    }
    print("本地建議:\n", generate_suggestion(sample_analysis))
    print("\nOllama 建議:\n", generate_ollama_suggestion(sample_analysis))