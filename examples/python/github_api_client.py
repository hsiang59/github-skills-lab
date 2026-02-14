"""
GitHub API 客戶端範例
展示如何使用 Copilot 建立 API 客戶端
"""

import requests
from typing import Dict, List, Optional


class GitHubClient:
    """簡單的 GitHub API 客戶端"""
    
    def __init__(self, token: Optional[str] = None):
        """
        初始化 GitHub API 客戶端
        
        參數:
            token: GitHub 個人存取權杖（選填）
        """
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"
    
    def get_user(self, username: str) -> Dict:
        """
        獲取使用者資訊
        
        參數:
            username: GitHub 使用者名稱
        
        返回:
            使用者資訊字典
        """
        url = f"{self.base_url}/users/{username}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_repositories(self, username: str) -> List[Dict]:
        """
        獲取使用者的公開儲存庫列表
        
        參數:
            username: GitHub 使用者名稱
        
        返回:
            儲存庫列表
        """
        url = f"{self.base_url}/users/{username}/repos"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def search_repositories(self, query: str, language: Optional[str] = None) -> List[Dict]:
        """
        搜尋儲存庫
        
        參數:
            query: 搜尋查詢字串
            language: 程式語言篩選（選填）
        
        返回:
            符合條件的儲存庫列表
        """
        search_query = query
        if language:
            search_query += f" language:{language}"
        
        url = f"{self.base_url}/search/repositories"
        params = {"q": search_query, "sort": "stars", "order": "desc"}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()["items"]


# 使用範例
if __name__ == "__main__":
    # 創建客戶端實例
    client = GitHubClient()
    
    # 獲取使用者資訊
    user = client.get_user("octocat")
    print(f"使用者: {user['login']}")
    print(f"名稱: {user['name']}")
    print(f"公開儲存庫數: {user['public_repos']}")
    
    # 搜尋 Python 儲存庫
    repos = client.search_repositories("machine learning", language="python")
    print(f"\n找到 {len(repos)} 個儲存庫")
    for repo in repos[:5]:
        print(f"- {repo['full_name']} ({repo['stargazers_count']} stars)")
