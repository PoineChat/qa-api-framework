# qa-api-framework（Python 版接口自动化测试框架）

分层架构、数据驱动、Allure 报告。被测对象是公开教学 API **JSONPlaceholder**

## 目录结构
```
qa-api-framework/
├── config.py              # 基础地址 / 请求头（对应 Java 的 Config 层）
├── models.py              # 数据模型（对应 Java 的 POJO，本例暂未强用）
├── clients/               # 接口封装（对应 Java 的 Service 层）
│   └── user_client.py
├── tests/                 # 测试用例
│   └── test_users.py
├── conftest.py            # pytest fixture（对应 Java 的 BaseTest）
├── pytest.ini
└── requirements.txt
```

## 运行步骤
```bash
# 首次：安装依赖
venv\Scripts\python -m pip install -r requirements.txt

# 跑全部用例
venv\Scripts\python -m pytest -q

# 生成 Allure 报告（可选，需另装 allure 命令行）
venv\Scripts\python -m pytest          # 先产出 allure-results
allure serve allure-results
```


