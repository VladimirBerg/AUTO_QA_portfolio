import pytest
import allure
from api.client.reqres_client import ReqResClient

@pytest.fixture(scope="module")
def client(config):
    return ReqResClient(config["api_url"])

@allure.feature("Users API")
class TestUsersAPI:

    @allure.story("Get users list")
    @allure.title("GET /users?page=2 returns 200 and 6 users")
    @pytest.mark.api
    def test_get_users_list(self, client):
        response = client.get_users(page=2)
        assert response.status_code == 200
        data = response.json()
        assert len(data["data"]) == 6
        assert "page" in data

    @allure.story("Get single user")
    @allure.title("GET /users/2 returns 200 and valid email")
    @pytest.mark.api
    def test_get_single_user(self, client):
        response = client.get_user(2)
        assert response.status_code == 200
        email = response.json()["data"]["email"]
        assert "@" in email

    @allure.story("Create user")
    @allure.title("POST /users returns 201 and created user")
    @pytest.mark.api
    def test_create_user(self, client):
        response = client.create_user("John", "Tester")
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "John"
        assert data["job"] == "Tester"
        assert "id" in data
        assert "createdAt" in data

    @allure.story("Update user")
    @allure.title("PUT /users/2 returns 200")
    @pytest.mark.api
    def test_update_user(self, client):
        response = client.update_user(2, "Jane", "Developer")
        assert response.status_code == 200
        assert response.json()["job"] == "Developer"

    @allure.story("Delete user")
    @allure.title("DELETE /users/2 returns 204")
    @pytest.mark.api
    def test_delete_user(self, client):
        response = client.delete_user(2)
        assert response.status_code == 204


@allure.feature("Auth API")
class TestAuthAPI:

    @allure.story("Login")
    @allure.title("POST /login with valid data returns token")
    @pytest.mark.api
    def test_successful_login(self, client):
        response = client.login("eve.holt@reqres.in", "cityslicka")
        assert response.status_code == 200
        assert "token" in response.json()

    @allure.story("Login")
    @allure.title("POST /login with missing password returns 400")
    @pytest.mark.api
    def test_unsuccessful_login(self, client):
        response = client.login("eve.holt@reqres.in", "")
        assert response.status_code == 400
        assert "error" in response.json()

    @allure.story("Register")
    @allure.title("POST /register with valid data returns token")
    @pytest.mark.api
    def test_successful_register(self, client):
        response = client.register("eve.holt@reqres.in", "pistol")
        assert response.status_code == 200
        assert "token" in response.json()
        assert "id" in response.json()

    @allure.story("Register")
    @allure.title("POST /register with missing password returns 400")
    @pytest.mark.api
    def test_unsuccessful_register(self, client):
        response = client.register("eve.holt@reqres.in", "")
        assert response.status_code == 400
        assert "error" in response.json()
