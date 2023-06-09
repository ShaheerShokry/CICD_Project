from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def predict(self):
        self.client.post("/predict",{
            "CHAS":{
                "0":0
            },
            "RM":{
                "0":6.575
            },
            "TAX":{
                "0":296.0
            },
            "PTRATIO":{
                "0":15.3
            },
            "B":{
                "0":396.9
            },
            "LSTAT":{
                "0":4.98
            }
        },
        headers={"Content-Type": "application/json"})
