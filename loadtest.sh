# The command will run load test on your deployed application by using locust. Remember to change "udacity-flask-ml-service" to your-app-service-name
locust -f locustfile.py --host https://flask-app-1.azurewebsites.net/
