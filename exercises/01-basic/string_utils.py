"""
字串處理工具模組
實作各種字串操作函數
"""

def reverse_string(text: str) -> str:
    """
    反轉字串
    
    參數:
        text: 要反轉的字串
    
    返回:
        反轉後的字串
    
    範例:
        >>> reverse_string("hello")
        "olleh"
    """
    pass


def count_words(text: str) -> int:
    """
    計算字串中的單字數量
    單字以空白字元分隔
    
    參數:
        text: 要計算的字串
    
    返回:
        單字數量
    
    範例:
        >>> count_words("Hello world")
        2
        >>> count_words("  Hello   world  ")
        2
    """
    pass


def remove_whitespace(text: str) -> str:
    """
    移除字串中所有的空白字元（空格、tab、換行等）
    
    參數:
        text: 要處理的字串
    
    返回:
        移除空白字元後的字串
    
    範例:
        >>> remove_whitespace("Hello World")
        "HelloWorld"
        >>> remove_whitespace("  H e l l o  ")
        "Hello"
    """
    pass


def capitalize_words(text: str) -> str:
    """
    將字串中每個單字的首字母轉為大寫
    
    參數:
        text: 要處理的字串
    
    返回:
        每個單字首字母大寫的字串
    
    範例:
        >>> capitalize_words("hello world")
        "Hello World"
        >>> capitalize_words("python programming")
        "Python Programming"
    """
    pass
