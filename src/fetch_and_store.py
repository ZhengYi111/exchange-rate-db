# src/fetch_and_store.py
import os#读取系统环境变量
import requests#获取 API 数据
import psycopg2#PostgreSQL 数据库适配器
from datetime import datetime
from dotenv import load_dotenv
from utils.logging_config import logger #报错

#加载环境变量​
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

#使用 Frankfurter.app的免费 API，获取以人民币为基础的汇率数据。
API_URL = "https://api.frankfurter.app/latest?from=CNY"

def fetch_exchange_rates():
    """从公共 API 获取最新汇率"""
    response = requests.get(API_URL)
    response.raise_for_status() # 如果请求失败抛出异常
    data = response.json()  # 解析 JSON 响应
    return data["rates"], data["date"]  # 返回汇率字典和日期

def store_exchange_rates(rates, date):
    """将汇率数据存入 PostgreSQL"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()   # 创建游标

    for currency, rate in rates.items(): # 遍历汇率字典
        cur.execute("""
            INSERT INTO exchange_rates (base_currency, target_currency, rate, date)
            VALUES (%s, %s, %s, %s) 
            ON CONFLICT (base_currency, target_currency, date)
            DO UPDATE SET rate = EXCLUDED.rate;
        """, ("CNY", currency, rate, date))#当发生冲突时，用新值覆盖已存在的旧值

    conn.commit()   # 提交事务
    cur.close()  # 关闭游标
    conn.close()
    print(f"✅ 数据已存储：{date}")

if __name__ == "__main__": #确保该脚本被直接运行时才执行此代码
    try:
        print("开始获取汇率数据...")
        rates, date = fetch_exchange_rates()
        print(f"获取到 {len(rates)} 种货币汇率，日期：{date}")
        
        print("开始存储数据...")
        store_exchange_rates(rates, date)
        
        logger.info(f"数据入库成功：{date}")
        print("✅ 数据存储完成")
        
    except Exception as e:
        logger.error(f"发生错误：{e}")
        print(f"❌ 错误：{e}")
