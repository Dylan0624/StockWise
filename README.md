# StockWise

StockWise 是一個智能投資分析工具，旨在幫助使用者分析股票數據並提供投資建議。專案支援多種輸入格式，包括文字（股票號碼、基本面資料）、PDF（財報）以及未來計畫中的技術圖表影像。分析結果將結合本地語言模型（Ollama）生成建議。

## 功能

- **文字輸入**：解析股票號碼、基本面資料（如本益比、EPS）
- **未來擴展**：
  - PDF 財報解析
  - 技術圖表影像分析
  - 使用 Ollama 提供智能建議

## 環境需求

- Python 3.8+
- macOS（開發環境：MacBook Pro M4 Pro, 48GB RAM）
- 未來：Ollama（本地語言模型）

## 安裝

1. 複製專案：
```bash
git clone https://github.com/Dylan0624/StockWise.git
cd StockWise
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 準備文字輸入檔案（例如 data/text/sample.txt）：
```text
股票號碼: 2330
本益比: 15
EPS: 5.2
```

2. 運行程式：
```bash
python src/input/text.py
```

## 開發進度

- 初始化專案結構
- 實現文字輸入與基本分析
- 整合 PDF 解析
- 接入 Ollama 語言模型
- 支援技術圖表影像分析

## 貢獻

歡迎提交 Issue 或 Pull Request！

## 聯絡

- GitHub: Dylan0624