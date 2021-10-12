import mysql.connector
import platform
import os
import sys

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='qw0002004',
    database='alii'
)

my_cursor = my_db.cursor()
my_cursor.execute("CREATE TABLE IF NOT EXISTS login_parol(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,"
                  "first_name VARCHAR(30) NOT NULL,"
                  "last_name VARCHAR(30) NOT NULL,"
                  "age INT(3) NOT NULL,"
                  "login VARCHAR(30) NOT NULL,"
                  "password VARCHAR(30) NOT NULL)")
