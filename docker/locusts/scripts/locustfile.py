import os                                                                                  
import string                                                                              
import random                                                                              
from locust import HttpLocust, TaskSet, task                                                     
                                                                                           
class SimpleTrafficRequest(TaskSet):       

    @task(1)
    def index(self):
        self.client.get("/")
    
    @task(2)
    def search_for_blog_post(self):
        self.client.get("/?s=ola-mundo")
    
    @task(3)
    def search_for_blog_unpost(self):
        self.client.get("/?s=test")

    @task(4)
    def search_for_blog_unpost(self):
        self.client.get("/locust/add-post.php")        

class WebsiteUser(HttpLocust):         
    host = os.getenv('TARGET_URL', "http://nginx")
    task_set = SimpleTrafficRequest                            
    min_wait = 5000
    #max_wait = 15000  
    #stop_timeout = 100