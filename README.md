# docker-locust-performance-test
Docker Locusts Performance Test with Wordpress

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

```
$ cd locusts
$ docker build -t locusts:latest .
$ docker run --rm -ti -p 8089:8089 --network=docker_default locusts:latest /bin/sh
```

* Go to url `http://localhost:8089` 

![Screenshot](Locust.png)
