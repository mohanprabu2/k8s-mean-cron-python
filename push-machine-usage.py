import psutil
import socket    
from pymongo import MongoClient
import datetime

client = MongoClient(host='localhost', port=27017)
db = client.utilization

result = {}

result['cpu'] = psutil.cpu_percent()
result['mem'] = dict(psutil.virtual_memory()._asdict())['percent']
result['ip'] = socket.gethostbyname(socket.gethostname())
result['time'] = datetime.datetime.now()

r = db.metrics.insert_one(result)

#print(r.inserted_id)