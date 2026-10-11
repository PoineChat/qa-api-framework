# qa-api-framework（Python 版接口自动化测试框架）

对应简历里 Java + TestNG + RestAssured 方向的「学习用」实现。概念完全一致：
分层架构、数据驱动、Allure 报告。被测对象是公开教学 API **JSONPlaceholder**
（零配置、无需 key、无限流），**无需自建后端即可反复运行学习**。

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

## 运行步骤（本机已装好 Python 3.13，无需联网装环境）
```bash
# 首次：安装依赖
venv\Scripts\python -m pip install -r requirements.txt

# 跑全部用例
venv\Scripts\python -m pytest -q

# 生成 Allure 报告（可选，需另装 allure 命令行）
venv\Scripts\python -m pytest          # 先产出 allure-results
allure serve allure-results
```

## 学习路线
1. 先读 `clients/user_client.py`：理解「把 HTTP 请求封装成方法」这一层。
2. 再看 `tests/test_users.py`：每个 `@allure.title` 是一个用例，`@pytest.mark.parametrize` 就是「数据驱动」。
3. 体会分层：`tests` 只写断言，`clients` 只管发请求，`config` 只管环境切换——这就是面试常问的「框架分层 / 关注点分离」。
4. 学完 Python 版后，去 GitHub 克隆 Java 版（见对话）对照看，语法不同但结构一模一样。
