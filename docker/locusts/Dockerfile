FROM python:3.6.6-alpine3.8

RUN pip install --upgrade pip

RUN apk add gcc libc-dev pkgconfig zeromq-dev curl

RUN apk --no-cache add g++ \ 
       && pip install locustio pyzmq

COPY ./scripts/locustfile.py /locustfile.py

ENTRYPOINT ["locust", "-f", "locustfile.py"] 
