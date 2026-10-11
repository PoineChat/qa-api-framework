import os

# 被测系统地址（JSONPlaceholder：测试教学标准用，零配置、无需 key、无限流）
BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")

HEADERS = {"Content-Type": "application/json"}
