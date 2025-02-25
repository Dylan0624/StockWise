# src/output/ollama_client.py
import ollama
import subprocess
import json

def check_available_models():
    """檢查本地已安裝的 Ollama 模型"""
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')[1:]  # 跳過表頭
        models = [line.split()[0] for line in lines if line]  # 提取模型名稱
        return models
    except subprocess.CalledProcessError:
        return []

def get_model_options():
    """返回可選模型清單"""
    return [
        "deepseek-r1:1.5b", "deepseek-r1:7b", "deepseek-r1:8b", "deepseek-r1:14b",
        "deepseek-r1:32b", "deepseek-r1:70b", "llama3:8b", "llama3:70b",
        "qwen2:7b", "qwen2:14b", "qwen2:32b"
    ]

def select_model(preferred_model="deepseek-r1:14b"):
    """選擇可用模型，若首選不在則從可選清單中挑選"""
    available_models = check_available_models()
    options = get_model_options()
    
    if preferred_model in available_models:
        return preferred_model
    else:
        print(f"首選模型 {preferred_model} 未安裝，可用模型: {available_models}")
        for option in options:
            if option in available_models:
                print(f"使用可用模型: {option}")
                return option
        print("無可用模型，請先安裝 Ollama 模型（例如：ollama pull deepseek-r1:14b）")
        return None

def generate_ollama_suggestion(analysis, model="deepseek-r1:14b"):
    """使用指定的 Ollama 模型生成投資建議"""
    selected_model = select_model(model)
    if not selected_model:
        return "無法生成建議：無可用模型"

    prompt = "以下是一隻股票的分析數據，請根據這些數據提供完整的投資建議（包括是否買入、賣出或持有，並解釋原因）：\n"
    for key, value in analysis.items():
        prompt += f"{key}: {value}\n"
    prompt += "\n請提供專業且具體的投資建議，並考慮基本面與技術面因素。"

    try:
        response = ollama.chat(
            model=selected_model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Ollama 服務異常: {e}"

if __name__ == "__main__":
    # 測試模型選擇與建議生成
    sample_analysis = {
        "stock_code": "2330", "data_date": "2025-02-23", "price": 1095,
        "prev_close": 1080, "change_pct": 1.39, "change_trend": "上漲"
    }
    print("可用模型:", check_available_models())
    print("\nOllama 建議:\n", generate_ollama_suggestion(sample_analysis))