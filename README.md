# 📈 StockWise - 智能投資分析工具  

**StockWise** 是一款智能投資分析工具，透過解析股票數據並結合本地語言模型 **Ollama**，為使用者提供投資建議。  
專案支援 **GUI 圖形介面**，讓使用者能夠更直覺地輸入股票數據、分析市場趨勢，並獲取 AI 生成的投資建議。

---

![alt text](<img/CleanShot 2025-03-02 at 11.02.00@2x.png>)

## ✨ 功能特點  

✅ **股票數據分析**：支援輸入股票代碼、自動擷取市場數據並分析基本面  
✅ **智能建議**：本地模型與 **Ollama AI** 提供投資建議  
✅ **圖形化介面**（GUI）：直覺化的 **PyQt6** 介面，無需命令列操作  
✅ **多數據來源**：支援 **網路爬蟲** 或 **本地文件** 來源  
🚀 **未來擴展**（規劃中）：  
- 📄 **PDF 財報解析**  
- 📊 **技術圖表影像分析**  

---

## 🔄 系統流程

以下流程圖展示了 StockWise 的工作原理和數據流向：

```mermaid
flowchart TD
    A[User Input] -->|Stock Code| B[Data Source]
    A -->|File Upload| F[File Analysis]
    
    B -->|Web Crawler| C[YFinance API]
    B -->|Local File| D[Text Parser]
    
    C --> E[Raw Stock Data]
    D --> E
    
    E --> G[Data Analyzer]
    F -->|PDF/Text| G
    
    G --> H[Analysis Result]
    
    H --> I[Local Suggestion]
    H --> J[Ollama AI]
    
    J -->|LLM Processing| K[AI Suggestion]
    
    I --> L[GUI Display]
    K --> L
    
    subgraph "Input Module"
    A
    B
    C
    D
    F
    end
    
    subgraph "Analysis Module"
    E
    G
    H
    end
    
    subgraph "Output Module"
    I
    J
    K
    end
    
    style A fill:#f9f9f9,stroke:#333,stroke-width:2px
    style L fill:#f9f9f9,stroke:#333,stroke-width:2px
    style J fill:#d4f0f0,stroke:#333,stroke-width:2px
    style K fill:#d4f0f0,stroke:#333,stroke-width:2px
```

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

3️⃣ **啟動 GUI**：
```sh
python stockwise_ui.py
```

4️⃣ **或在命令列執行測試**：
```sh
python main.py
```

---

## 🎨 圖形化介面（GUI）  

StockWise 提供了完整的 **PyQt6** 圖形介面，簡單直觀：

### **🔹 股票分析**
- **輸入股票代碼**（例如 `2330`）
- 選擇數據來源（**網路爬蟲** 或 **本地文件**）
- 點擊 **分析**，即時顯示：
  - **股票基本數據**
  - **分析結果**
  - **本地 AI 投資建議**
  - **Ollama AI 投資建議**

### **🔹 文件分析**
- 上傳 **財報（PDF）** 或 **技術圖表**
- 運行分析並獲取結果

### **🔹 設置**
- 更換 **Ollama AI 模型**
- 調整 **UI 語言與主題**
- 檢查 **Ollama 服務狀態**

---

## 🚀 使用方法  

### **1️⃣ 啟動應用**
```sh
python stockwise_ui.py
```
或使用命令列模式：
```sh
python main.py
```

### **2️⃣ 股票分析**
- 在 **「股票分析」** 選項卡中輸入 **股票代碼**
- 選擇數據來源（**網路爬蟲** / **本地文件**）
- 點擊 **「分析」** 按鈕，獲取分析結果與 AI 投資建議

### **3️⃣ 文件分析**
- 切換到 **「文件分析」** 選項卡
- 選擇 **文件類型（文字 / PDF / 圖像）**
- 上傳檔案並點擊 **「分析」**

### **4️⃣ 設置**
- 在 **「設置」** 選項卡選擇 **Ollama AI 模型**
- 變更 **界面語言與主題**
- 點擊 **「檢查 Ollama 狀態」** 確保 AI 服務可用

---

## 📌 開發進度  

- [x] **GUI 介面（PyQt6）**
- [x] **股票數據分析**
- [x] **Ollama AI 建議**
- [x] **股票代碼輸入**
- [x] **本地 / 網路數據來源**
- [ ] **整合 PDF 解析 🛠**
- [ ] **支援技術圖表影像分析 📊**

---

## 🤝 貢獻方式  

歡迎提交 **Issue** 或 **Pull Request**！請參考 [貢獻指南](CONTRIBUTING.md) 來進一步了解如何貢獻。  

---

## 📬 聯絡方式  

- **GitHub**: [Dylan0624](https://github.com/Dylan0624)  

---

## 📜 授權條款  

本專案採用 **MIT License**，詳細請參考 [LICENSE](LICENSE)。
