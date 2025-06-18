# 使用官方 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置环境变量（可选）
ENV PYTHONUNBUFFERED=1

# 安装依赖项
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    libffi-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 创建工作目录
WORKDIR /app

# 复制项目文件（假设外层目录是 torrentbotx 项目根目录）
COPY . .

# 安装 Python 依赖
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 暴露常用端口（如 Bot 回调或 Web 接口可用）
EXPOSE 8000

# 运行主入口（假设 run.py 是项目入口）
CMD ["python", "run.py"]
