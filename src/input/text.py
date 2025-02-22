# src/input/text.py
def read_text_input(file_path):
    """讀取文字檔案中的股票資料"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"檔案 {file_path} 不存在")
        return None

def parse_text_input(text):
    """解析文字輸入，返回字典格式"""
    data = {}
    for line in text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    return data

if __name__ == "__main__":
    # 測試範例
    sample_text = "股票號碼: 2330\n本益比: 15\nEPS: 5.2"
    parsed_data = parse_text_input(sample_text)
    print(parsed_data)