import sqlite3
import pandas as pd

class DBConnector:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def query_table(self, table_name):
        return pd.read_sql_query(f"SELECT * FROM {table_name}", self.conn)

    def close(self):
        self.conn.close()
