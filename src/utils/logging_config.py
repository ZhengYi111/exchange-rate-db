import logging  # Python 标准日志库
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True) #创建logs文件夹，目录已存在时不报错

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"), # 写在logs/app.log 文件里
    level=logging.INFO,# 只记录INFO级别及以上
    format="%(asctime)s - %(levelname)s - %(message)s" # 记录格式：时间+等级+内容
) #设定记录规则：时间、级别、消息

logger = logging.getLogger(__name__) #创建日志记录器
