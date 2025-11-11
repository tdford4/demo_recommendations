import sqlite3
import pandas as pd

def init_db(db_path="data/recommendations.db"):
    conn = sqlite3.connect(db_path)
    return conn

def load_data(conn):
    query = "SELECT * FROM interactions;"
    return pd.read_sql(query, conn)
