import os                                                                                  
import string                                                                              
import random                                                                              
from locust import HttpLocust, TaskSet, task                                                     
                                                                                           
class SimpleTrafficRequest(TaskSet):       

    @task(1)
    def index(self):
        self.client.get("/")
    
    @task(3)
    def get_post(self):
        self.client.get("/2019/03/10/ola-mundo")
    
    @task(2)
    def search_for_blog_post(self):
        self.client.get("/?s=ola")
    
    @task(2)
    def search_for_blog_unpost(self):
        self.client.get("/?s=test")

class WebsiteUser(HttpLocust):         
    host = os.getenv('TARGET_URL', "http://172.30.0.1")
    task_set = SimpleTrafficRequest                            
    min_wait = 5000