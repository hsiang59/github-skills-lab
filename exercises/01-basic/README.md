# 練習 1: GitHub Copilot 基礎

## 學習目標
- 學習 GitHub Copilot 的基本操作
- 練習程式碼自動完成
- 理解如何接受和拒絕建議

## 前置準備
確保已安裝並啟用 GitHub Copilot 擴充套件。

## 練習內容

### 任務 1: 簡單函數生成

在 `calculator.py` 中實作以下函數。輸入函數簽名和註釋，讓 Copilot 建議實作。

1. 加法函數
2. 減法函數
3. 乘法函數
4. 除法函數（處理除以零的情況）

### 任務 2: 資料驗證

在 `validator.py` 中實作驗證函數：

1. 電子郵件驗證
2. 電話號碼驗證（台灣格式）
3. 密碼強度檢查

### 任務 3: 字串處理

在 `string_utils.py` 中實作：

1. 字串反轉
2. 計算單字數量
3. 移除空白字元
4. 首字母大寫

## 提示

### 任務 1 提示範例
```python
def add(a: float, b: float) -> float:
    """將兩個數字相加並返回結果"""
    # 讓 Copilot 完成
```

### 任務 2 提示範例
```python
def is_valid_email(email: str) -> bool:
    """
    檢查電子郵件地址是否有效
    
    參數:
        email: 要驗證的電子郵件地址
    
    返回:
        True 如果電子郵件有效，否則 False
    """
    # 讓 Copilot 完成
```

## 驗證

完成後，執行以下命令測試你的實作：

```bash
python -m pytest test_calculator.py
python -m pytest test_validator.py
python -m pytest test_string_utils.py
```

## 成功標準

- [ ] 所有函數都能正確運作
- [ ] 通過所有測試案例
- [ ] 程式碼清晰易讀
- [ ] 包含適當的錯誤處理

## 延伸挑戰

1. 為計算機添加更多運算（平方根、次方等）
2. 實作更複雜的密碼驗證規則
3. 添加單元測試

## 學習重點

- 觀察 Copilot 如何根據函數名稱和註釋生成程式碼
- 嘗試不同的提示方式，看看結果有何不同
- 學會評估和修改 Copilot 的建議

## 下一步

完成這個練習後，繼續進行「練習 2: 提示工程」以學習更進階的技巧。
