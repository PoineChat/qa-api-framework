from dataclasses import dataclass


@dataclass
class User:
    """请求/响应体的数据模型（对应 Java 框架里的 POJO）"""
    name: str
    job: str
    email: str = ""
    id: str = ""
