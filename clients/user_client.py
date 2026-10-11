import requests

from config import BASE_URL, HEADERS


class UserClient:
    """用户模块接口封装（对应 Java 框架的 Service 层）"""

    def __init__(self, base_url=BASE_URL, headers=HEADERS):
        self.base_url = base_url
        self.headers = headers

    def list_users(self, limit=3):
        return requests.get(
            f"{self.base_url}/users",
            params={"_limit": limit},
            headers=self.headers,
            timeout=10,
        )

    def get_user(self, user_id):
        return requests.get(
            f"{self.base_url}/users/{user_id}", headers=self.headers, timeout=10
        )

    def create_user(self, payload):
        # 演示写操作：JSONPlaceholder 用 /posts 接收，无需真实后端
        return requests.post(
            f"{self.base_url}/posts", json=payload, headers=self.headers, timeout=10
        )

    def update_user(self, user_id, payload):
        return requests.put(
            f"{self.base_url}/users/{user_id}", json=payload, headers=self.headers, timeout=10
        )

    def delete_user(self, user_id):
        return requests.delete(
            f"{self.base_url}/users/{user_id}", headers=self.headers, timeout=10
        )
