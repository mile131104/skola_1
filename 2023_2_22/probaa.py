import mysql.connector as conn
import time


db = conn.connect(host="localhost", username="root",passwd="",database="aaaa")
cur = db.cursor()
cur.execute("create schema manga")
