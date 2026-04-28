import pytest
import allure
from api.client.jsonplaceholder_client import JSONPlaceholderClient

@pytest.fixture(scope="module")
def client():
    return JSONPlaceholderClient()

@allure.feature("JSONPlaceholder API")
class TestUsersAPI:

    @allure.title("GET /users returns 200 and 10 users")
    @pytest.mark.api
    def test_get_users_list(self, client):
        response = client.get_users()
        assert response.status_code == 200
        assert len(response.json()) == 10

    @allure.title("GET /users/1 returns 200 and user with email")
    @pytest.mark.api
    def test_get_single_user(self, client):
        response = client.get_user(1)
        assert response.status_code == 200
        data = response.json()
        assert "email" in data
        assert "@" in data["email"]

    @allure.title("POST /posts returns 201 with id")
    @pytest.mark.api
    def test_create_post(self, client):
        response = client.create_post("Test Title", "Test Body")
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Title"
        assert "id" in data

    @allure.title("PUT /posts/1 returns 200")
    @pytest.mark.api
    def test_update_post(self, client):
        response = client.update_post(1, "Updated Title")
        assert response.status_code == 200
        assert response.json()["title"] == "Updated Title"

    @allure.title("DELETE /posts/1 returns 200")
    @pytest.mark.api
    def test_delete_post(self, client):
        response = client.delete_post(1)
        assert response.status_code == 200
