# src/query_rates.py
import os #读取操作系统环境变量
import psycopg2  #PostgreSQL 数据库连接库
import pandas as pd
from dotenv import load_dotenv  #从 .env文件加载配置

#从项目根目录的 .env文件加载数据库配置
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

def query_latest_rates():
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT
    )
    df = pd.read_sql("SELECT * FROM exchange_rates ORDER BY date DESC LIMIT 10;", conn)
    print(df)
    conn.close()

if __name__ == "__main__":
    query_latest_rates()
