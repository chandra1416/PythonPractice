import mysql.connector
from mysql.connector import Error
con=mysql.connector.connect(host="localhost",username="chandra",password="@chennai1")
cur=con.cursor()
