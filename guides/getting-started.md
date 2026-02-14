# GitHub Copilot 入門指南

## 什麼是 GitHub Copilot？

GitHub Copilot 是一個由 AI 驅動的程式碼助手，它使用機器學習模型來幫助開發者更快速、更有效率地編寫程式碼。

## 主要功能

### 1. 程式碼自動完成
當你開始輸入程式碼時，Copilot 會自動建議完整的程式碼行或函數。

**範例：**
```python
# 輸入註釋：計算兩個數字的和
# Copilot 會建議：
def add_numbers(a, b):
    return a + b
```

### 2. 程式碼生成
根據自然語言註釋生成完整的函數或類別。

**範例：**
```javascript
// 創建一個函數來驗證電子郵件地址
// Copilot 會建議完整的驗證函數
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}
```

### 3. 測試生成
自動生成單元測試程式碼。

**範例：**
```python
# 為上面的 add_numbers 函數生成測試
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
```

## 如何撰寫有效的提示

### 最佳實踐

1. **使用清晰的註釋**
   - 描述你想要做什麼
   - 包含輸入和輸出的預期格式

2. **提供上下文**
   - 使用描述性的變數名稱
   - 包含相關的型別資訊

3. **分解複雜任務**
   - 將大型任務分解為較小的步驟
   - 逐步引導 Copilot

### 提示範例

#### ❌ 不好的提示
```python
# 函數
def func(x):
```

#### ✅ 好的提示
```python
# 創建一個函數來計算列表中數字的平均值
# 參數：numbers - 數字列表
# 返回：平均值（浮點數）
def calculate_average(numbers):
```

## 快捷鍵

### Visual Studio Code

- **接受建議**: `Tab` 或 `Enter`
- **拒絕建議**: `Esc`
- **查看下一個建議**: `Alt + ]` (Windows/Linux) 或 `Option + ]` (Mac)
- **查看上一個建議**: `Alt + [` (Windows/Linux) 或 `Option + [` (Mac)
- **觸發 Copilot**: `Alt + \` (Windows/Linux) 或 `Option + \` (Mac)

## 使用技巧

### 1. 利用範例程式碼
在檔案中提供範例，Copilot 會學習你的編碼風格。

### 2. 使用型別提示
在 Python、TypeScript 等語言中使用型別提示可以獲得更準確的建議。

### 3. 命名規範
使用清晰、描述性的函數和變數名稱。

### 4. 逐步建構
從簡單的函數開始，逐步建構更複雜的功能。

## 常見問題

### Q: Copilot 的建議是否總是正確？
A: 不一定。始終要檢查和測試 Copilot 生成的程式碼。

### Q: 如何提高建議的品質？
A: 提供清晰的註釋、使用描述性的名稱，並提供足夠的上下文。

### Q: Copilot 支援哪些程式語言？
A: Copilot 支援大多數主流程式語言，包括 Python、JavaScript、TypeScript、Java、C++、Go 等。

### Q: 程式碼的版權歸屬？
A: 你生成的程式碼歸你所有，但建議檢查並理解所有生成的程式碼。

## 下一步

1. 完成 `exercises/01-basic/` 中的基礎練習
2. 探索 `examples/` 目錄中的範例
3. 閱讀 `guides/prompt-engineering.md` 了解進階提示技巧

## 相關資源

- [GitHub Copilot 文件](https://docs.github.com/en/copilot)
- [Copilot 快速開始](https://docs.github.com/en/copilot/quickstart)
- [負責任地使用 AI](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features)
