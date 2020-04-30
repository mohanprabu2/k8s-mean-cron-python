FROM python:3.6-alpine

RUN apk update

RUN apk add gcc musl-dev libc-dev linux-headers
RUN wget https://files.pythonhosted.org/packages/c4/b8/3512f0e93e0db23a71d82485ba256071ebef99b227351f0f5540f744af41/psutil-5.7.0.tar.gz
RUN gunzip psutil-5.7.0.tar.gz && tar -xvf psutil-5.7.0.tar
RUN cd psutil-5.7.0/ && ls -la && python setup.py install

RUN pip install pymongo

ENV MONGO_DB_IP=172.17.0.2
ENV MONGO_DB_PORT=27017

WORKDIR /

COPY push-machine-usage.py .

CMD ["python", "push-machine-usage.py"]
