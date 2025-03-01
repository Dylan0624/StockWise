import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, 
                            QGridLayout, QComboBox, QMessageBox, QFileDialog, QGroupBox,
                            QSplitter, QFrame)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon, QPixmap

# 导入项目模块
# 在实际使用时需要取消注释这些导入
from src.input.text import get_stock_data
from src.analysis.text_analyzer import analyze_text_data
from src.output.suggestion import generate_suggestion, generate_ollama_suggestion

class StockWiseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StockWise - 智能投資分析工具")
        self.setMinimumSize(1000, 700)
        
        # 初始化 UI
        self.init_ui()
        
    def init_ui(self):
        # 创建中央窗口
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        
        # 应用标题
        title_label = QLabel("StockWise")
        title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)
        
        # 子标题
        subtitle_label = QLabel("智能投資分析工具")
        subtitle_label.setFont(QFont("Arial", 12))
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(subtitle_label)
        
        # 创建选项卡
        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)
        
        # 创建不同功能的选项卡
        self.create_stock_analysis_tab(tab_widget)
        self.create_file_analysis_tab(tab_widget)
        self.create_settings_tab(tab_widget)
        
        # 状态栏
        self.statusBar().showMessage("就緒")
        
    def create_stock_analysis_tab(self, parent):
        """股票分析选项卡"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 输入区域
        input_group = QGroupBox("股票數據輸入")
        input_layout = QGridLayout()
        input_group.setLayout(input_layout)
        
        # 股票代码输入
        input_layout.addWidget(QLabel("股票代碼:"), 0, 0)
        self.stock_code_input = QLineEdit()
        self.stock_code_input.setPlaceholderText("例如: 2330")
        input_layout.addWidget(self.stock_code_input, 0, 1)
        
        # 数据源选择
        input_layout.addWidget(QLabel("數據來源:"), 0, 2)
        self.data_source_combo = QComboBox()
        self.data_source_combo.addItems(["網路爬蟲", "本地文件"])
        input_layout.addWidget(self.data_source_combo, 0, 3)
        
        # 分析按钮
        analyze_btn = QPushButton("分析")
        analyze_btn.clicked.connect(self.analyze_stock)
        input_layout.addWidget(analyze_btn, 0, 4)
        
        layout.addWidget(input_group)
        
        # 分析结果区域
        results_splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # 基本数据显示
        data_group = QGroupBox("股票基本數據")
        data_layout = QVBoxLayout()
        self.stock_data_display = QTextEdit()
        self.stock_data_display.setReadOnly(True)
        data_layout.addWidget(self.stock_data_display)
        data_group.setLayout(data_layout)
        results_splitter.addWidget(data_group)
        
        # 分析结果显示
        analysis_group = QGroupBox("分析結果")
        analysis_layout = QVBoxLayout()
        self.analysis_display = QTextEdit()
        self.analysis_display.setReadOnly(True)
        analysis_layout.addWidget(self.analysis_display)
        analysis_group.setLayout(analysis_layout)
        results_splitter.addWidget(analysis_group)
        
        layout.addWidget(results_splitter, 1)
        
        # 建议区域
        suggestion_splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # 本地建议
        local_suggestion_group = QGroupBox("本地投資建議")
        local_suggestion_layout = QVBoxLayout()
        self.local_suggestion_display = QTextEdit()
        self.local_suggestion_display.setReadOnly(True)
        local_suggestion_layout.addWidget(self.local_suggestion_display)
        local_suggestion_group.setLayout(local_suggestion_layout)
        suggestion_splitter.addWidget(local_suggestion_group)
        
        # Ollama 建议
        ollama_suggestion_group = QGroupBox("Ollama 智能建議")
        ollama_suggestion_layout = QVBoxLayout()
        self.ollama_suggestion_display = QTextEdit()
        self.ollama_suggestion_display.setReadOnly(True)
        ollama_suggestion_layout.addWidget(self.ollama_suggestion_display)
        ollama_suggestion_group.setLayout(ollama_suggestion_layout)
        suggestion_splitter.addWidget(ollama_suggestion_group)
        
        layout.addWidget(suggestion_splitter, 1)
        
        parent.addTab(tab, "股票分析")
        
    def create_file_analysis_tab(self, parent):
        """文件分析选项卡"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 文件选择区域
        file_group = QGroupBox("文件分析")
        file_layout = QGridLayout()
        file_group.setLayout(file_layout)
        
        # 文件类型选择
        file_layout.addWidget(QLabel("文件類型:"), 0, 0)
        self.file_type_combo = QComboBox()
        self.file_type_combo.addItems(["文字檔案", "PDF 財報", "技術圖表"])
        file_layout.addWidget(self.file_type_combo, 0, 1)
        
        # 文件路径
        file_layout.addWidget(QLabel("文件路徑:"), 1, 0)
        self.file_path_input = QLineEdit()
        self.file_path_input.setReadOnly(True)
        file_layout.addWidget(self.file_path_input, 1, 1, 1, 3)
        
        # 选择文件按钮
        browse_btn = QPushButton("瀏覽...")
        browse_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(browse_btn, 1, 4)
        
        # 分析文件按钮
        analyze_file_btn = QPushButton("分析文件")
        analyze_file_btn.clicked.connect(self.analyze_file)
        file_layout.addWidget(analyze_file_btn, 2, 4)
        
        layout.addWidget(file_group)
        
        # 文件分析结果
        file_results_group = QGroupBox("文件分析結果")
        file_results_layout = QVBoxLayout()
        self.file_results_display = QTextEdit()
        self.file_results_display.setReadOnly(True)
        file_results_layout.addWidget(self.file_results_display)
        file_results_group.setLayout(file_results_layout)
        
        layout.addWidget(file_results_group, 1)
        
        parent.addTab(tab, "文件分析")
        
    def create_settings_tab(self, parent):
        """设置选项卡"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Ollama 设置
        ollama_group = QGroupBox("Ollama 設置")
        ollama_layout = QGridLayout()
        ollama_group.setLayout(ollama_layout)
        
        # 模型选择
        ollama_layout.addWidget(QLabel("Ollama 模型:"), 0, 0)
        self.ollama_model_combo = QComboBox()
        self.ollama_model_combo.addItems(["deepseek-r1:14b", "llama3:70b", "qwen:14b"])
        ollama_layout.addWidget(self.ollama_model_combo, 0, 1)
        
        # 刷新模型列表
        refresh_models_btn = QPushButton("刷新模型列表")
        refresh_models_btn.clicked.connect(self.refresh_models)
        ollama_layout.addWidget(refresh_models_btn, 0, 2)
        
        # 检查 Ollama 状态
        check_ollama_btn = QPushButton("檢查 Ollama 狀態")
        check_ollama_btn.clicked.connect(self.check_ollama)
        ollama_layout.addWidget(check_ollama_btn, 1, 2)
        
        layout.addWidget(ollama_group)
        
        # 界面设置
        ui_group = QGroupBox("界面設置")
        ui_layout = QGridLayout()
        ui_group.setLayout(ui_layout)
        
        # 语言选择
        ui_layout.addWidget(QLabel("界面語言:"), 0, 0)
        self.language_combo = QComboBox()
        self.language_combo.addItems(["繁體中文", "简体中文", "English"])
        ui_layout.addWidget(self.language_combo, 0, 1)
        
        # 主题选择
        ui_layout.addWidget(QLabel("界面主題:"), 1, 0)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["淺色", "深色", "系統預設"])
        ui_layout.addWidget(self.theme_combo, 1, 1)
        
        # 应用设置按钮
        apply_settings_btn = QPushButton("應用設置")
        apply_settings_btn.clicked.connect(self.apply_settings)
        ui_layout.addWidget(apply_settings_btn, 2, 1, Qt.AlignmentFlag.AlignRight)
        
        layout.addWidget(ui_group)
        
        # 关于信息
        about_group = QGroupBox("關於")
        about_layout = QVBoxLayout()
        about_text = QTextEdit()
        about_text.setReadOnly(True)
        about_text.setHtml("""
        <h2>StockWise v1.0</h2>
        <p>StockWise 是一個智能投資分析工具，旨在幫助使用者分析股票數據並提供投資建議。</p>
        <p>版權所有 &copy; 2025 Dylan0624</p>
        <p>使用 MIT 許可證</p>
        """)
        about_layout.addWidget(about_text)
        about_group.setLayout(about_layout)
        
        layout.addWidget(about_group)
        
        parent.addTab(tab, "設置")
        
    def analyze_stock(self):
        """分析股票数据"""
        stock_code = self.stock_code_input.text()
        if not stock_code:
            QMessageBox.warning(self, "輸入錯誤", "請輸入股票代碼")
            return
            
        self.statusBar().showMessage(f"正在分析股票 {stock_code}...")
        
        # 在实际应用中取消注释以下代码

        source = "crawler" if self.data_source_combo.currentText() == "網路爬蟲" else "file"
        
        try:
            # 获取股票数据
            stock_data = get_stock_data(source=source, stock_code=stock_code)
            if not stock_data:
                QMessageBox.warning(self, "數據獲取失敗", "無法獲取股票數據，請檢查股票代碼或網絡連接")
                self.statusBar().showMessage("分析失敗")
                return
                
            # 显示原始数据
            self.stock_data_display.setPlainText(str(stock_data))
            
            # 分析数据
            analysis = analyze_text_data(stock_data)
            self.analysis_display.setPlainText(str(analysis))
            
            # 生成建议
            local_suggestion = generate_suggestion(analysis)
            self.local_suggestion_display.setPlainText(local_suggestion)
            
            # 尝试生成 Ollama 建议
            ollama_model = self.ollama_model_combo.currentText()
            ollama_suggestion = generate_ollama_suggestion(analysis, model=ollama_model)
            self.ollama_suggestion_display.setPlainText(ollama_suggestion)
            
            self.statusBar().showMessage(f"股票 {stock_code} 分析完成")
        except Exception as e:
            QMessageBox.critical(self, "錯誤", f"分析過程中出現錯誤: {str(e)}")
            self.statusBar().showMessage("分析失敗")

    def browse_file(self):
        """浏览文件"""
        file_type = self.file_type_combo.currentText()
        if file_type == "文字檔案":
            file_filter = "文字檔案 (*.txt)"
        elif file_type == "PDF 財報":
            file_filter = "PDF 檔案 (*.pdf)"
        else:
            file_filter = "圖像檔案 (*.png *.jpg *.jpeg)"
            
        file_path, _ = QFileDialog.getOpenFileName(self, "選擇檔案", "", file_filter)
        if file_path:
            self.file_path_input.setText(file_path)
            
    def analyze_file(self):
        """分析文件"""
        file_path = self.file_path_input.text()
        if not file_path:
            QMessageBox.warning(self, "輸入錯誤", "請選擇檔案")
            return
            
        file_type = self.file_type_combo.currentText()
        self.statusBar().showMessage(f"正在分析{file_type}...")
        
        # 实际应用中根据不同文件类型调用不同分析函数
        # 这里只做模拟
        self.file_results_display.setPlainText(f"分析檔案: {file_path}\n\n【分析結果】\n此為示範內容，實際開發中根據檔案類型調用相應的分析功能。\n\n如果是文字檔案，將解析其中的股票資訊；\n如果是PDF，將提取財報關鍵資訊；\n如果是技術圖表，將識別圖形模式。")
        
        self.statusBar().showMessage(f"{file_type}分析完成")
        
    def refresh_models(self):
        """刷新 Ollama 模型列表"""
        self.statusBar().showMessage("正在檢查可用模型...")
        
        # 实际应用中应调用 Ollama 客户端

        try:
            from src.output.ollama_client import check_available_models
            models = check_available_models()
            if models:
                self.ollama_model_combo.clear()
                self.ollama_model_combo.addItems(models)
                QMessageBox.information(self, "成功", f"發現 {len(models)} 個可用模型")
            else:
                QMessageBox.warning(self, "無可用模型", "未發現可用的 Ollama 模型，請確保 Ollama 服務正在運行")
        except Exception as e:
            QMessageBox.critical(self, "錯誤", f"檢查模型時出錯: {str(e)}")

        
        # 模拟刷新
        QMessageBox.information(self, "成功", "發現 3 個可用模型")
        self.statusBar().showMessage("模型列表已更新")
        
    def check_ollama(self):
        """检查 Ollama 状态"""
        self.statusBar().showMessage("檢查 Ollama 服務狀態...")
        
        # 实际应用中应尝试连接 Ollama 服务

        try:
            import ollama
            response = ollama.embeddings(model="deepseek-r1:14b", prompt="test")
            QMessageBox.information(self, "Ollama 狀態", "Ollama 服務正常運行中")
        except Exception as e:
            QMessageBox.critical(self, "Ollama 狀態", f"無法連接到 Ollama 服務: {str(e)}\n\n請確保 Ollama 已安裝且服務正在運行。")

        
        # 模拟检查
        QMessageBox.information(self, "Ollama 狀態", "Ollama 服務正常運行中")
        self.statusBar().showMessage("Ollama 服務正常")
        
    def apply_settings(self):
        """应用设置"""
        language = self.language_combo.currentText()
        theme = self.theme_combo.currentText()
        
        # 实际应用中应保存设置并应用
        QMessageBox.information(self, "設置已保存", f"語言設置為: {language}\n主題設置為: {theme}\n\n這些設置將在下次啟動時生效")
        self.statusBar().showMessage("設置已更新")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockWiseApp()
    window.show()
    sys.exit(app.exec())