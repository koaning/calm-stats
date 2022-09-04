import random
from locust import HttpUser, between, task, tag

class WebsiteUser(HttpUser):
    wait_time = between(1, 1.5)

    def on_start(self):
        self.uid = str(random.randint(0, 100_000)).zfill(6)

    @task
    def attempt(self):
        self.client.get("/")
