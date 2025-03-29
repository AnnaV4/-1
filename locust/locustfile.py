from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def hello_world(self):
        self.client.get("https://obscure-engine-579x7q9rqg634x9q-8000.app.github.dev/")
    
    @task(2)
    def nocodb(self):
        self.client.get("https://ubiquitous-train-9gxjr557wwxfpqg6-8000.app.github.dev/nocodb-data/")

    @task(5)
    def admin(self):
        self.client.post("https://ubiquitous-train-9gxjr557wwxfpqg6-8000.app.github.dev/admin/login/?next=/admin/", {"username": "admin", "password": "123987"})

    @task(4)
    def polls(self):
        self.client.get("https://ubiquitous-train-9gxjr557wwxfpqg6-8000.app.github.dev/polls/")