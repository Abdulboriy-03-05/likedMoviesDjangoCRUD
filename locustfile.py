import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("")
        # self.client.get("/world")

    @task(2)
    def view_items(self):
        for item_id in range(100):
            self.client.get(f"page/{item_id}", name="detail")
            time.sleep(1)
