"""
資料驗證模組
實作各種資料格式的驗證函數
"""

def is_valid_email(email: str) -> bool:
    """
    檢查電子郵件地址是否有效
    使用正規表示式驗證基本的電子郵件格式
    
    參數:
        email: 要驗證的電子郵件地址
    
    返回:
        True 如果電子郵件格式有效，否則 False
    
    範例:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("invalid.email")
        False
    """
    pass


def is_valid_phone(phone: str) -> bool:
    """
    檢查台灣手機號碼是否有效
    有效格式: 09xx-xxxxxx 或 09xxxxxxxx
    
    參數:
        phone: 要驗證的電話號碼
    
    返回:
        True 如果電話號碼格式有效，否則 False
    
    範例:
        >>> is_valid_phone("0912-345678")
        True
        >>> is_valid_phone("0912345678")
        True
        >>> is_valid_phone("1234567890")
        False
    """
    pass


def is_strong_password(password: str) -> bool:
    """
    檢查密碼強度
    強密碼必須:
    - 至少 8 個字元
    - 包含至少一個大寫字母
    - 包含至少一個小寫字母
    - 包含至少一個數字
    
    參數:
        password: 要檢查的密碼
    
    返回:
        True 如果密碼足夠強，否則 False
    
    範例:
        >>> is_strong_password("Abc12345")
        True
        >>> is_strong_password("weak")
        False
    """
    pass
