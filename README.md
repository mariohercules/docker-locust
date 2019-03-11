# docker-locust-performance-test
Docker Locust Performance Test with Wordpress

## Scheme

*  Only nginx is on a accessible network from users and locust app.
*  Wordpress and MySQL can only be accessible from nginx.

![Screenshot](Diagram-Locust.png)

## How-To

*  Create containers (proxy, wordpress and mysql).

```
$ docker-compose up -d
```

* Create docker image and container.
* Run docker image and add to existing network.
* Check what IP address was generated to container network and put it on locust call command --host=

```
$ cd locusts
$ docker build -t locusts:latest .
$ docker run --rm -ti -p 8089:8089 --network=docker_default locusts:latest /bin/sh
/ # locust -f locustfile.py --host=http://172.30.0.1
```

* Go to url `http://localhost:8089` 

![Screenshot](Locust.png)
