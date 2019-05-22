# docker-locust
Docker Locust Performance Test with Wordpress

* [Locust](https://locust.io) is an open source loading test tool where users behavior can be simulated with python code.

## Scheme

*  Only nginx is on accessible network to the users and locust app.
*  Wordpress and MySQL can only be accessible from nginx.

![Screenshot](Diagram-Locust.png)

## How to use

### Configure containers

* Clone this repository.
* Run a command to create containers (locust, ngninx-proxy, wordpress and mysql).

```
$ cd docker
$ docker-compose build
$ docker-compose up -d
$ docker ps --format "table {{.Image}}\t{{.Status}}\t{{.Names}}\t{{.Ports}}"
```

* Verify if the 6 containers is up

```
IMAGE               STATUS              NAMES                 PORTS
nginx:latest        Up 5 minutes        nginx                 0.0.0.0:80->80/tcp
wordpress:latest    Up 5 minutes        docker_wordpress2_1   80/tcp
wordpress:latest    Up 5 minutes        docker_wordpress3_1   80/tcp
wordpress:latest    Up 5 minutes        docker_wordpress1_1   80/tcp
docker_locust       Up 5 minutes        docker_locust_1       0.0.0.0:8089->8089/tcp
mysql:5.5.60        Up 5 minutes        docker_db_1           3306/tcp
```

* Open `http://localhost`
* Install e configure WordPress 

* Open `http://localhost:8089` 
* Enter the parameters on the fields `Number of users to simulate` and `Hatch rate (users spawned/second)` on form and press the button `Start swarming`
* The locust will start to executing the tasks and collecting data from request and response.

### Locust config (optional)

* The `locustfile.py` on folder `/docker/locusts/scripts/` is the script.
* For this project I created 4 task to be tested -- Feel free to change with your own tasks.
* max_wait = will run until time (seconds) reach the end. -- in this case will run for 15 minutes.


```python
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
    max_wait = 15000
    #stop_timeout = 100
```

![Screenshot](Locust.png)
