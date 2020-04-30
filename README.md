# k8s-mean-cron-python

Prerequisites for this project:

  MongoDB should be running

To run this project in local machine:

  Prerequisites:
  
    Python should be installed
    pip install psutil
    pip install pymongo
    
  Run in local machine:
  
    git clone https://github.com/mohanprabu2/k8s-mean-cron-python.git
    cd k8s-mean-cron-python
    python push-machine-usage.py
  
To build this as docker image:
```
  git clone https://github.com/mohanprabu2/k8s-mean-cron-python.git
  cd k8s-mean-cron-python
  docker build -t k8s-mean-cron-python:latest . --rm
```
To run this docker image:
  ```
  docker run -d --env MONGO_DB_IP=172.17.0.2 --env MONGO_DB_PORT=27017 --name cron k8s-mean-cron-python:latest
```
