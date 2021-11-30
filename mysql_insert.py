import mysql.connector
import time
import datetime

start = time.time()
print(datetime.datetime.now().time())
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="dtb_name")

mycursor = mydb.cursor()

sql = "INSERT INTO call_history (date, call_id, receive_id, duration) VALUES (%s, %s, %s, %s)"

with open("file_name") as big_file:
    list_obj = []
    for line in big_file:
        words = line.split(',')
        obj = (words[0], words[1], words[2], words[3])
        list_obj.append(obj)
        if(len(list_obj) == 1000000):
            try:
                mycursor.executemany(sql, list_obj)
                list_obj = []
                mydb.commit()
            except:
                mydb.rollback()

#################################################################################################################

sql = """INSERT INTO users (customer_name, phone_number, money) VALUES (%s, %s, %s)"""

with open("file_name") as big_file:
    list_obj = []
    for line in big_file:
        words = line.split(',')
        obj = (words[1], words[2], words[3])
        list_obj.append(obj)
        if(len(list_obj) == 1000000):
            try:
                mycursor.executemany(sql, list_obj)
                list_obj = []
                mydb.commit()
            except:
                mydb.rollback()


end = time.time()
print(datetime.datetime.now().time())
total = end - start
print("Total time: {:.5f}s".format(total))
