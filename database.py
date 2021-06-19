import mysql.connector
from mysql.connector import Error

class Database:

    def getConnection(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='be_project',
                                                user='root',
                                                password='')
            
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        return connection

