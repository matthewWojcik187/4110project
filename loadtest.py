from locust import HttpUser, between, task
import random
import string

import requests

def random_username(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

class MicroblogUser(HttpUser):
    wait_time = between(1, 5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sessionID = None

    def on_start(self):
        self.username, self.password, self.token = self.get_credentials()

        with self.client.post("/auth/register", data={
            "username": self.username,
            "email": f"{self.username}@test.com",
            "password": self.password,
            "token": self.token
        }, catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed to register with username:{self.username}, email: {self.username}@test.com, password: {self.password}. Response code: " + str(response.status_code))
            
            
        with self.client.post("/auth/login", json={
            "username": self.username,
            "password": self.password,
            "token": self.token
        }, catch_response=True) as response2:
            if response2.status_code == 200:
                # Create a post
                self.create_post()
            else:
                response2.failure("Failed to login. Response code: " + str(response2.status_code))





    def get_credentials(self):
        username = random_username(8)
        password = "test" 
        token = 123456
        return username, password, token

    @task
    def view_homepage(self):
        with self.client.get("/index", catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure("Failed to view homepage. Response code: " + str(resp.status_code))
    
    @task
    def view_account(self):
        with self.client.get(f"/user/{self.username}", catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure("Failed to view account. Response code: " + str(resp.status_code))

    @task
    def create_post(self):
        headers = {
            "Content-Type": "application/json"
        }
        form_data = {
            "post": "Testing",
            "submit": "Submit"
        }
        with self.client.post("/index", headers=headers, json=form_data, cookies={"session": self.sessionID}, catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure("Failed to create post. Response code: " + str(resp.status_code))

    @task
    def view_profile(self):
        self.client.get(f"/user/{self.username}")