import time
from typing import List
import datetime
from elasticsearch import Elasticsearch, helpers

file_name = "path"
file_name2 = "path"

es = Elasticsearch(timeout=5000000)

start = time.time()
print(datetime.datetime.now().time())

with open(file_name1) as big_file:
    list_obj = []
    for line in big_file:
        obj_arr = line.split(',')
        obj = {
            "_index": "profile_index",
            "_source": {
                'user_id':  str(int(obj_arr[0])),
                'user_name': obj_arr[1],
                'user_phonenumber': obj_arr[2],
                'user_balance': obj_arr[3]
            }
        }
        list_obj.append(obj)
        if (len(list_obj) == 1000000):
            helpers.bulk(es, list_obj, request_timeout=100000000)
            list_obj = []

#########################################################################################

with open(file_name2) as big_file:
    list_obj = []
    count = 0
    for line in big_file:
        count = count + 1
        obj_arr = line.split(',')
        obj = {
            "_index": "phone-history_index",
            "_source": {
                'history_id': str(count),
                'datetime': obj_arr[0],
                'duration': obj_arr[3],
                'source-phone-number': obj_arr[1],
                'target-phone-number': obj_arr[2]
            }
        }
        list_obj.append(obj)
        if (len(list_obj) == 1000000):
            helpers.bulk(es, list_obj)
            list_obj = []


end = time.time()
total = end - start
print(datetime.datetime.now().time())
print("Total time: {:.5f}s".format(total))
