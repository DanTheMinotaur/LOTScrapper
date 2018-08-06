import mysql.connector
from mysql.connector import errorcode, Error


class Database:
    __db_conn = mysql.connector

    def __init__(self):
        try:
            self.__db_conn = mysql.connector.connect(
                user='LOTScrapper',
                password='LOTScrapper',
                host='localhost',
                database='lottery'
            )
            print('Database Connection Established')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def query_data(self, query, data=None):
        cursor = self.__db_conn.cursor()
        result = None
        try:
            if data is None:
                cursor.execute(query)
            else:
                cursor.execute(query, (data,))

            result = cursor.fetchall()
        except Error as err:
            print(err)
        finally:
            cursor.close()
            return result
