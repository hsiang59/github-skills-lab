# Prompt Engineering 提示工程指南

## 什麼是 Prompt Engineering？

Prompt Engineering 是撰寫清晰、有效的提示來引導 AI 工具（如 GitHub Copilot）生成高品質程式碼的技術。

## 核心原則

### 1. 明確性 (Clarity)
使用清晰、精確的語言描述你的需求。

### 2. 上下文 (Context)
提供足夠的背景資訊讓 Copilot 理解任務。

### 3. 結構 (Structure)
使用良好的程式碼結構和命名規範。

### 4. 範例 (Examples)
在適當的時候提供範例格式或輸出。

## Prompt 模式

### 模式 1: 函數簽名 + 註釋

```python
def calculate_fibonacci(n: int) -> int:
    """
    計算斐波那契數列的第 n 項
    
    參數:
        n: 要計算的項數（從 0 開始）
    
    返回:
        第 n 項的斐波那契數
    
    範例:
        >>> calculate_fibonacci(0)
        0
        >>> calculate_fibonacci(5)
        5
    """
    # Copilot 會在這裡生成實作
```

### 模式 2: 逐步說明

```javascript
// 步驟 1: 驗證輸入
// 步驟 2: 轉換為小寫
// 步驟 3: 移除特殊字元
// 步驟 4: 返回清理後的字串
function sanitizeInput(input) {
    // Copilot 會根據步驟生成程式碼
}
```

### 模式 3: 型別導向

```typescript
interface User {
    id: number;
    name: string;
    email: string;
    createdAt: Date;
}

// 創建一個函數來驗證使用者物件
// 檢查所有必填欄位是否存在且格式正確
function validateUser(user: Partial<User>): boolean {
    // Copilot 會根據型別定義生成驗證邏輯
}
```

### 模式 4: 測試驅動

```python
# 測試案例定義預期行為
def test_parse_date():
    assert parse_date("2024-01-15") == datetime(2024, 1, 15)
    assert parse_date("invalid") is None
    assert parse_date("") is None

# 根據測試實作函數
def parse_date(date_string: str) -> Optional[datetime]:
    # Copilot 會根據測試生成實作
```

## 進階技巧

### 1. 使用有意義的變數名稱

❌ **不好的範例：**
```python
def f(x, y):
    return x + y
```

✅ **好的範例：**
```python
def calculate_total_price(base_price: float, tax_rate: float) -> float:
    # Copilot 能更好地理解意圖
```

### 2. 提供輸入/輸出範例

```python
def format_phone_number(phone: str) -> str:
    """
    將電話號碼格式化為標準格式
    
    輸入: "0912345678"
    輸出: "(09) 1234-5678"
    """
```

### 3. 指定演算法或方法

```java
// 使用二分搜尋法在排序陣列中查找元素
public int binarySearch(int[] arr, int target) {
    // Copilot 會實作二分搜尋
}
```

### 4. 說明邊界條件

```python
def divide_numbers(a: float, b: float) -> float:
    """
    兩數相除
    
    注意:
    - 當 b 為 0 時，返回 None
    - 處理負數情況
    - 返回結果四捨五入到兩位小數
    """
```

### 5. 參考現有程式碼

```javascript
// 類似於上面的 validateEmail 函數
// 但這次驗證電話號碼
function validatePhoneNumber(phone) {
    // Copilot 會參考 validateEmail 的模式
}
```

## 實戰範例

### 範例 1: API 客戶端

```python
class GitHubAPIClient:
    """
    GitHub API 的簡單客戶端
    
    功能:
    - 獲取使用者資訊
    - 列出使用者的儲存庫
    - 處理速率限制
    - 錯誤處理和重試
    """
    
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"
    
    def get_user(self, username: str) -> dict:
        """
        獲取 GitHub 使用者的公開資訊
        
        參數:
            username: GitHub 使用者名稱
        
        返回:
            包含使用者資訊的字典
        
        拋出:
            requests.HTTPError: 當請求失敗時
        """
        # Copilot 會生成實作
```

### 範例 2: 資料處理

```python
import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    清理銷售資料
    
    處理步驟:
    1. 移除重複記錄
    2. 處理缺失值：
       - price: 填充為平均值
       - quantity: 填充為 0
       - date: 移除該行
    3. 轉換資料型別
    4. 驗證數值範圍（價格和數量必須為正數）
    5. 標準化日期格式
    
    參數:
        df: 原始銷售資料框
    
    返回:
        清理後的資料框
    """
    # Copilot 會根據詳細步驟生成程式碼
```

### 範例 3: 演算法實作

```java
public class BinaryTree {
    class Node {
        int value;
        Node left, right;
        
        Node(int value) {
            this.value = value;
        }
    }
    
    private Node root;
    
    /**
     * 使用層序遍歷（廣度優先）印出二元樹
     * 每一層印在一行
     * 
     * 範例輸出:
     * 1
     * 2 3
     * 4 5 6 7
     */
    public void printLevelOrder() {
        // Copilot 會實作層序遍歷
    }
}
```

## 常見錯誤與解決方案

### 錯誤 1: 提示過於簡短
❌ `// 排序`
✅ `// 使用快速排序演算法對整數陣列進行升序排序`

### 錯誤 2: 缺乏上下文
❌ 
```python
def process(data):
```
✅ 
```python
def process_user_registration_data(registration_form: dict) -> User:
    """處理使用者註冊表單資料並創建 User 物件"""
```

### 錯誤 3: 模糊的需求
❌ `// 驗證資料`
✅ `// 驗證電子郵件格式、密碼強度（至少 8 字元、包含大小寫和數字）、使用者名稱唯一性`

## 練習建議

1. **從簡單開始**：先練習基本函數的提示
2. **逐步複雜化**：逐漸增加需求的複雜度
3. **比較結果**：嘗試不同的提示方式，比較結果
4. **迭代改進**：根據生成的程式碼調整提示
5. **建立模板**：為常見任務建立可重用的提示模板

## 檢查清單

在撰寫提示時，確認：
- [ ] 清楚說明函數的目的
- [ ] 定義輸入參數和型別
- [ ] 說明預期的返回值
- [ ] 描述邊界條件和錯誤處理
- [ ] 提供使用範例（如果適用）
- [ ] 使用描述性的命名
- [ ] 包含必要的上下文

## 相關資源

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [GitHub Copilot 最佳實踐](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [提示工程入門](https://www.promptingguide.ai/)

## 下一步

完成 `exercises/02-prompt-engineering/` 中的練習，實際應用這些技巧。
