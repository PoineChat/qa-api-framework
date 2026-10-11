import allure
import pytest

from clients.user_client import UserClient


@allure.title("获取用户列表")
def test_list_users(user_client: UserClient):
    resp = user_client.list_users(limit=3)
    assert resp.status_code == 200
    assert len(resp.json()) >= 3


@allure.title("获取单个用户-存在")
def test_get_existing_user(user_client: UserClient):
    resp = user_client.get_user(1)
    assert resp.status_code == 200
    assert resp.json()["id"] == 1


@allure.title("获取单个用户-不存在返回 404(异常用例)")
def test_get_missing_user(user_client: UserClient):
    resp = user_client.get_user(999)
    assert resp.status_code == 404


@allure.title("创建用户-成功返回 201 且回显 id")
def test_create_user(user_client: UserClient):
    payload = {"title": "morpheus", "body": "leader", "userId": 1}
    resp = user_client.create_user(payload)
    assert resp.status_code == 201
    assert "id" in resp.json()


@pytest.mark.parametrize("user_id", [1, 2, 3])
@allure.title("批量获取用户-存在性校验(数据驱动)")
def test_get_users_parametrized(user_client: UserClient, user_id):
    resp = user_client.get_user(user_id)
    assert resp.status_code == 200
    assert resp.json()["id"] == user_id


@allure.title("更新用户-PUT 部分更新返回 200")
def test_update_user(user_client: UserClient):
    resp = user_client.update_user(1, {"name": "zion resident"})
    assert resp.status_code == 200


@allure.title("删除用户-返回 200")
def test_delete_user(user_client: UserClient):
    resp = user_client.delete_user(1)
    assert resp.status_code == 200
