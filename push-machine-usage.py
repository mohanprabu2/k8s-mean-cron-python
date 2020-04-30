import psutil
import socket    
from pymongo import MongoClient
import datetime
import os

client = MongoClient(host=os.environ['MONGO_DB_IP'], port=int(os.environ['MONGO_DB_PORT']))
db = client.utilization

result = {}

result['cpu'] = psutil.cpu_percent()
result['mem'] = dict(psutil.virtual_memory()._asdict())['percent']
result['ip'] = socket.gethostbyname(socket.gethostname())
result['time'] = datetime.datetime.now()

r = db.metrics.insert_one(result)

#print(r.inserted_id)