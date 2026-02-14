"""
資料處理範例
展示如何使用 Copilot 處理和分析資料
"""

from typing import List, Dict
from collections import Counter
import statistics


class DataProcessor:
    """資料處理工具類"""
    
    @staticmethod
    def remove_duplicates(data: List) -> List:
        """
        移除列表中的重複元素，保持原始順序
        
        參數:
            data: 輸入列表
        
        返回:
            移除重複後的列表
        """
        seen = set()
        result = []
        for item in data:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    @staticmethod
    def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
        """
        計算數值列表的統計資訊
        
        參數:
            numbers: 數值列表
        
        返回:
            包含統計資訊的字典（平均值、中位數、標準差等）
        """
        if not numbers:
            return {}
        
        return {
            "mean": statistics.mean(numbers),
            "median": statistics.median(numbers),
            "mode": statistics.mode(numbers) if len(numbers) > 1 else numbers[0],
            "std_dev": statistics.stdev(numbers) if len(numbers) > 1 else 0,
            "min": min(numbers),
            "max": max(numbers),
            "count": len(numbers)
        }
    
    @staticmethod
    def group_by_key(data: List[Dict], key: str) -> Dict[str, List[Dict]]:
        """
        根據指定的鍵將字典列表分組
        
        參數:
            data: 字典列表
            key: 分組依據的鍵
        
        返回:
            分組後的字典
        """
        result = {}
        for item in data:
            group_key = item.get(key)
            if group_key not in result:
                result[group_key] = []
            result[group_key].append(item)
        return result
    
    @staticmethod
    def filter_by_criteria(data: List[Dict], criteria: Dict) -> List[Dict]:
        """
        根據多個條件篩選資料
        
        參數:
            data: 字典列表
            criteria: 篩選條件（鍵值對）
        
        返回:
            符合所有條件的項目列表
        """
        result = []
        for item in data:
            if all(item.get(key) == value for key, value in criteria.items()):
                result.append(item)
        return result
    
    @staticmethod
    def find_most_common(data: List, n: int = 1) -> List[tuple]:
        """
        找出列表中最常出現的元素
        
        參數:
            data: 輸入列表
            n: 返回前 n 個最常見的元素
        
        返回:
            (元素, 出現次數) 的元組列表
        """
        counter = Counter(data)
        return counter.most_common(n)


# 使用範例
if __name__ == "__main__":
    # 範例資料
    numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    
    # 計算統計資訊
    stats = DataProcessor.calculate_statistics(numbers)
    print("統計資訊:")
    for key, value in stats.items():
        print(f"  {key}: {value:.2f}")
    
    # 範例：學生資料
    students = [
        {"name": "Alice", "grade": "A", "age": 20},
        {"name": "Bob", "grade": "B", "age": 21},
        {"name": "Charlie", "grade": "A", "age": 20},
        {"name": "David", "grade": "C", "age": 22}
    ]
    
    # 按成績分組
    by_grade = DataProcessor.group_by_key(students, "grade")
    print("\n按成績分組:")
    for grade, students_list in by_grade.items():
        print(f"  {grade}: {[s['name'] for s in students_list]}")
    
    # 篩選 A 級學生
    a_students = DataProcessor.filter_by_criteria(students, {"grade": "A"})
    print(f"\nA 級學生: {[s['name'] for s in a_students]}")
