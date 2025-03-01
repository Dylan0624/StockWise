# 📈 StockWise - 智能投資分析工具  

**StockWise** 是一款智能投資分析工具，透過解析股票數據並結合本地語言模型 **Ollama**，為使用者提供投資建議。  
專案支援多種輸入格式，如文字（股票號碼、基本面資料）、PDF（財報），以及未來計畫中的技術圖表影像分析。

---

## ✨ 功能特點  

✅ **文字輸入**：解析股票號碼、基本面資料（如本益比、EPS）  
✅ **智能建議**：基於 **Ollama** 分析數據並生成投資建議  
🚀 **未來擴展**（規劃中）：  
- 📄 **PDF 財報解析**  
- 📊 **技術圖表影像分析**  

---

## 🛠 環境需求  

- Python **3.8+**  
- macOS（開發環境：MacBook Pro M4 Pro, 48GB RAM）  
- [Ollama](https://ollama.com/)（未來支援）  

---

## 📥 安裝與設定  

1️⃣ **複製專案**：
```sh
git clone https://github.com/Dylan0624/StockWise.git
cd StockWise
```
  
2️⃣ **安裝依賴**：
```sh
pip install -r requirements.txt
```

---

## 🚀 使用方法  

1️⃣ **準備輸入數據**（例如 `data/text/sample.txt`）：  
```
股票號碼: 2330
本益比: 15
EPS: 5.2
```

2️⃣ **運行程式**：
```sh
python src/input/text.py
```

---

## 📌 開發進度  

- [x] 初始化專案結構  
- [x] 文字輸入與基本分析  
- [ ] 整合 PDF 解析 🛠  
- [ ] 接入 **Ollama** 語言模型 🔄  
- [ ] 支援技術圖表影像分析 📊  

---

## 🤝 貢獻方式  

歡迎提交 **Issue** 或 **Pull Request**！請參考 [貢獻指南](CONTRIBUTING.md) 來進一步了解如何貢獻。  

---

## 📬 聯絡方式  

- **GitHub**: [Dylan0624](https://github.com/Dylan0624)  

---

## 📜 授權條款  

本專案採用 **MIT License**，詳細請參考 [LICENSE](LICENSE)。
