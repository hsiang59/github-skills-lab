"""
Python 函數模板
複製並調整這些模板以適應你的需求
"""

# ========================================
# 基本函數模板
# ========================================

def function_name(param1: type, param2: type) -> return_type:
    """
    簡短的函數描述（一行）
    
    更詳細的說明（選填）
    
    參數:
        param1: 參數說明
        param2: 參數說明
    
    返回:
        返回值說明
    
    拋出:
        ExceptionType: 異常說明（如果適用）
    
    範例:
        >>> function_name(value1, value2)
        expected_result
    """
    # 實作內容
    pass


# ========================================
# 資料驗證函數模板
# ========================================

def validate_data(data: dict) -> bool:
    """
    驗證資料格式和內容
    
    檢查項目:
    - 必填欄位是否存在
    - 資料型別是否正確
    - 數值範圍是否有效
    - 格式是否符合規範
    
    參數:
        data: 要驗證的資料字典
    
    返回:
        True 如果資料有效，否則 False
    """
    pass


# ========================================
# 資料處理函數模板
# ========================================

def process_data(raw_data: list) -> list:
    """
    處理和轉換原始資料
    
    處理步驟:
    1. 清理資料（移除空值、重複等）
    2. 驗證資料格式
    3. 轉換資料型別
    4. 應用業務邏輯
    5. 返回處理後的資料
    
    參數:
        raw_data: 原始資料列表
    
    返回:
        處理後的資料列表
    """
    pass


# ========================================
# API 請求函數模板
# ========================================

def fetch_data_from_api(endpoint: str, params: dict = None) -> dict:
    """
    從 API 獲取資料
    
    參數:
        endpoint: API 端點 URL
        params: 查詢參數（選填）
    
    返回:
        API 回應的 JSON 資料
    
    拋出:
        requests.HTTPError: 當請求失敗時
        ValueError: 當回應格式無效時
    """
    pass


# ========================================
# 演算法實作模板
# ========================================

def sort_algorithm(arr: list) -> list:
    """
    使用 [演算法名稱] 對陣列進行排序
    
    時間複雜度: O(?)
    空間複雜度: O(?)
    
    參數:
        arr: 要排序的陣列
    
    返回:
        排序後的陣列
    
    範例:
        >>> sort_algorithm([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
    """
    pass


# ========================================
# 類別方法模板
# ========================================

class ClassName:
    """類別說明"""
    
    def __init__(self, param1: type, param2: type):
        """
        初始化物件
        
        參數:
            param1: 參數說明
            param2: 參數說明
        """
        self.param1 = param1
        self.param2 = param2
    
    def method_name(self, param: type) -> return_type:
        """
        方法說明
        
        參數:
            param: 參數說明
        
        返回:
            返回值說明
        """
        pass
    
    @staticmethod
    def static_method(param: type) -> return_type:
        """
        靜態方法說明
        
        參數:
            param: 參數說明
        
        返回:
            返回值說明
        """
        pass
    
    @property
    def property_name(self) -> type:
        """屬性說明"""
        return self._property_name


# ========================================
# 錯誤處理模板
# ========================================

def function_with_error_handling(param: type) -> return_type:
    """
    包含完整錯誤處理的函數
    
    參數:
        param: 參數說明
    
    返回:
        返回值說明
    
    拋出:
        ValueError: 當參數無效時
        TypeError: 當型別不匹配時
    """
    try:
        # 驗證輸入
        if not param:
            raise ValueError("參數不能為空")
        
        # 主要邏輯
        result = None  # 實作邏輯
        
        return result
        
    except ValueError as e:
        # 處理值錯誤
        raise
    except Exception as e:
        # 處理其他異常
        raise RuntimeError(f"處理失敗: {str(e)}")
