# 💱 Exchange Rate DB

> Automated Exchange Rate Data Pipeline  
> 每日自动抓取汇率数据 → 存入 PostgreSQL → 为 BI 系统提供趋势数据

---

## 📘 项目简介

`Exchange Rate DB` 是一个自动化的数据更新系统，  
每天从公开汇率 API 获取最新汇率数据，存入 PostgreSQL 数据库，  
并生成趋势数据表供 BI 或分析平台使用。

适用于：
- 数据分析 / 数据科学 学习项目
- 自动化 ETL（Extract-Transform-Load）实践
- BI 仪表盘或报表的数据源准备

---

## 🎯 项目目标（MVP阶段）

| 阶段 | 目标 | 状态 |
|------|------|------|
| 第1步 | 安装 PostgreSQL，熟悉数据库连接 | ✅ 已完成|
| 第2步 | 使用 Python 调用汇率 API，保存为 CSV | ✅ 已完成 |
| 第3步 | 将数据写入 PostgreSQL，自动建表 | ✅ 已完成 |
| 第4步 | 配置定时任务（cron / Airflow）实现每日更新 |✅ 已完成 |
| 第5步 | 生成汇率趋势表，导出供 BI 使用 | ⏳ 计划中 |

---

## 🧩 技术栈

- **Language**: Python 3.12.7
- **Database**: PostgreSQL
- **Scheduler**: cron
- **OS**: macOS (Apple M4)
- **Version Control**: Git + GitHub

---

## ⚙️ 项目结构

exchange-rate-db/
├── config/
│   └── config.yaml              # API 与数据库配置
├── data/                        # 临时存储下载数据
├── scripts/
│   ├── fetch_exchange_rates.py # 调用 API 抓取数据
│   ├── insert_to_db.py         # 数据写入数据库
│   └── create_tables.sql       # 建表脚本
├── .env                         # 环境变量文件（不上传 GitHub）
├── .gitignore
├── requirements.txt
└── README.md


🧠 后续计划
 
 添加日志系统
 
 支持多货币对（USD/CNY, EUR/USD, JPY/USD）
 
 增加 API 重试机制与异常处理
 
 可视化输出：生成每日汇率折线图

 使用 Docker 进行部署（高级阶段）


 ✨ 作者

Vive

Data Analyst → Data Engineer in progress

📍 Shanghai / Remote