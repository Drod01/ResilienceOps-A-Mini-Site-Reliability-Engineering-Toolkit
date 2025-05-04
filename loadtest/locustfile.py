from locust import HttpUser, task, between

class ResilienceOpsUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def normal_request(self):
        self.client.get("/")

    @task(2)
    def slow_request(self):
        self.client.get("/slow")

    @task(1)
    def error_request(self):
        self.client.get("/error")
