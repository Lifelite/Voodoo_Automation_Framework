import os
import MySQLdb
from dotenv import load_dotenv


class Database:

    @staticmethod
    def my_sql_connect():
        load_dotenv(override=True)
        connection = MySQLdb.connect(host=os.getenv("HOST"),
                                     user=os.getenv("USERNAME"),
                                     password=os.getenv("PASSWORD"),
                                     database=os.getenv("DATABASE"),
                                     autocommit=True,
                                     ssl_mode="VERIFY_IDENTITY",
                                     ssl={
                                         "ca": "C:/ca/cacert.pem"
                                     })
        db = connection
        return db
