import requests
from typing import Optional

class ReqResClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get_users(self, page: int = 2):
        return self.session.get(f"{self.base_url}/users", params={"page": page})

    def get_user(self, user_id: int):
        return self.session.get(f"{self.base_url}/users/{user_id}")

    def create_user(self, name: str, job: str):
        return self.session.post(f"{self.base_url}/users", json={"name": name, "job": job})

    def update_user(self, user_id: int, name: str, job: str):
        return self.session.put(f"{self.base_url}/users/{user_id}", json={"name": name, "job": job})

    def delete_user(self, user_id: int):
        return self.session.delete(f"{self.base_url}/users/{user_id}")

    def login(self, email: str, password: str):
        return self.session.post(f"{self.base_url}/login", json={"email": email, "password": password})

    def register(self, email: str, password: str):
        return self.session.post(f"{self.base_url}/register", json={"email": email, "password": password})
