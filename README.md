# docker-locust-performance-test
Docker Locust Performance Test with Wordpress

## Scheme

![Screenshot](Diagram-Locust.png)

mysql
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
