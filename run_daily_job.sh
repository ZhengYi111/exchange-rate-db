# 进入项目目录
cd /Users/zhengyi/workspace/exchange_rate_project

# 激活虚拟环境
source venv/bin/activate

# 执行 Python 脚本 & 追加日志
python src/fetch_and_store.py >> logs/run.log 2>&1
