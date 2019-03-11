# docker-locust-performance-test
Docker Locusts Performance Test with Wordpress

## Scheme

![Screenshot](Diagram-Locust.png)


## How-To

*  create containers (proxy, wordpress and mysql)

```
$ docker-compose up -d
```

*  create containers (proxy, wordpress and mysql)

```
$ cd locusts
$ docker build -t locusts:latest .
$ docker run --rm -ti -p 8089:8089 --network=docker_default locusts:latest /bin/sh
```

* Go to url `http://localhost:8089` 

![Screenshot](Locust.png)
