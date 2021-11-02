import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.environ['DATABASE_USER']
PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE = os.environ['DATABASE_DB']
HOST = os.environ['DATABASE_HOST']
PORT = os.environ['DATABASE_PORT']


class Database:
    def __init__(self):
        self._conn = psycopg2.connect(
            user=USERNAME, password=PASSWORD, host=HOST, port=PORT, dbname=DATABASE)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if(commit):
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
