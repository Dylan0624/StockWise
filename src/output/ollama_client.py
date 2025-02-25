# src/output/ollama_client.py
import ollama
import subprocess
import time

def check_available_models():
    """檢查本地已安裝的 Ollama 模型"""
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')[1:]  # 跳過表頭
        models = [line.split()[0] for line in lines if line]  # 提取模型名稱
        return models
    except subprocess.CalledProcessError:
        return []

def pull_model(model_name):
    """自動拉取指定的 Ollama 模型"""
    print(f"正在下載模型 {model_name}...")
    try:
        subprocess.run(['ollama', 'pull', model_name], check=True)
        print(f"模型 {model_name} 下載完成")
        return True
    except subprocess.CalledProcessError as e:
        print(f"無法下載模型 {model_name}: {e}")
        return False

def select_model(preferred_model="deepseek-r1:14b"):
    """選擇指定的模型，若不在本地則自動拉取"""
    available_models = check_available_models()
    
    if preferred_model in available_models:
        print(f"使用本地模型: {preferred_model}")
        return preferred_model
    else:
        print(f"首選模型 {preferred_model} 未安裝，可用模型: {available_models}")
        print(f"自動拉取指定模型 {preferred_model}")
        if pull_model(preferred_model):
            # 等待幾秒確保模型載入完成
            time.sleep(5)
            if preferred_model in check_available_models():
                print(f"成功載入模型: {preferred_model}")
                return preferred_model
            else:
                print(f"拉取 {preferred_model} 後仍不可用")
                return None
        else:
            print(f"自動拉取 {preferred_model} 失敗，請檢查 Ollama 服務或網路連線")
            return None

def generate_ollama_suggestion(analysis, model="deepseek-r1:14b"):
    """使用指定的 Ollama 模型生成投資建議"""
    selected_model = select_model(model)
    if not selected_model:
        return f"無法生成建議：無法使用或拉取模型 {model}"

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