import requests

class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get_users(self):
        return self.session.get(f"{self.BASE_URL}/users")

    def get_user(self, user_id: int):
        return self.session.get(f"{self.BASE_URL}/users/{user_id}")

    def create_post(self, title: str, body: str, user_id: int = 1):
        return self.session.post(f"{self.BASE_URL}/posts", json={
            "title": title, "body": body, "userId": user_id
        })

    def update_post(self, post_id: int, title: str):
        return self.session.put(f"{self.BASE_URL}/posts/{post_id}", json={"title": title})

    def delete_post(self, post_id: int):
        return self.session.delete(f"{self.BASE_URL}/posts/{post_id}")
