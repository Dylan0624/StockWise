# src/analysis/text_analyzer.py
def analyze_text_data(data):
    """分析文字數據，返回結構化結果"""
    analysis = {}
    if "股票號碼" in data:
        analysis["stock_code"] = data["股票號碼"]
    if "最新股價" in data:
        analysis["price"] = float(data["最新股價"])
    if "前日收盤價" in data:
        analysis["prev_close"] = float(data["前日收盤價"])
    if "漲跌幅" in data:
        change_pct = float(data["漲跌幅"])
        analysis["change_pct"] = change_pct
        analysis["change_trend"] = "上漲" if change_pct > 0 else "下跌" if change_pct < 0 else "持平"
    if "本益比" in data:
        pe_ratio = float(data["本益比"])
        analysis["pe_ratio"] = pe_ratio
        analysis["pe_assessment"] = "合理" if pe_ratio < 20 else "偏高"
    if "EPS" in data:
        analysis["eps"] = float(data["EPS"])
    if "成交量" in data:
        analysis["volume"] = int(data["成交量"])
    if "平均成交量" in data:
        avg_volume = int(data["平均成交量"])
        analysis["avg_volume"] = avg_volume
        analysis["volume_trend"] = "活躍" if analysis.get("volume", 0) > avg_volume else "正常"
    if "殖利率" in data:
        yield_rate = float(data["殖利率"])
        analysis["yield_rate"] = yield_rate
        analysis["yield_assessment"] = "具吸引力" if yield_rate > 2 else "一般"
    if "股利" in data:
        analysis["dividend"] = float(data["股利"])
    if "市值" in data:
        analysis["market_cap"] = int(data["市值"])
    if "52週高點" in data:
        analysis["year_high"] = float(data["52週高點"])
    if "52週低點" in data:
        analysis["year_low"] = float(data["52週低點"])
    if "Beta" in data:
        analysis["beta"] = float(data["Beta"])
    if "數據日期" in data:
        analysis["data_date"] = data["數據日期"]
    if "近三個月平均股價" in data:
        analysis["three_month_avg_price"] = float(data["近三個月平均股價"])
    if "近三個月平均成交量" in data:
        three_month_avg_vol = float(data["近三個月平均成交量"])
        analysis["three_month_avg_volume"] = three_month_avg_vol
        analysis["three_month_volume_trend"] = "增加" if three_month_avg_vol > analysis.get("avg_volume", 0) else "減少"
    if "近三個月股價變化率" in data:
        three_month_change = float(data["近三個月股價變化率"])
        analysis["three_month_change_pct"] = three_month_change
        analysis["three_month_trend"] = "上升" if three_month_change > 0 else "下降" if three_month_change < 0 else "穩定"
    if "近三個月最高股價" in data:
        analysis["three_month_high"] = float(data["近三個月最高股價"])
    if "近三個月最低股價" in data:
        analysis["three_month_low"] = float(data["近三個月最低股價"])
    if "近三個月股價標準差" in data:
        analysis["three_month_std"] = float(data["近三個月股價標準差"])
    return analysis

if __name__ == "__main__":
    sample_data = {
        "股票號碼": "2330", "最新股價": "1095", "前日收盤價": "1080", "漲跌幅": "1.39",
        "本益比": "25", "EPS": "5.2", "成交量": "30000000", "平均成交量": "35000000",
        "殖利率": "2.5", "股利": "27", "市值": "28300000000000", "52週高點": "1120",
        "52週低點": "800", "Beta": "1.08", "數據日期": "2025-02-23",
        "近三個月平均股價": "1050", "近三個月平均成交量": "32000000",
        "近三個月股價變化率": "4.5", "近三個月最高股價": "1120", "近三個月最低股價": "1000",
        "近三個月股價標準差": "50"
    }
    result = analyze_text_data(sample_data)
    print(result)