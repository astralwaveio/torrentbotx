import os
import sys
import subprocess
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(BASE_DIR, ".venv")
REQ_FILE = os.path.join(BASE_DIR, "requirements.txt")
DB_SETUP = os.path.join(BASE_DIR, "torrentbotx", "db", "setup.py")
CONFIG_PATH = os.path.join(BASE_DIR, "torrentbotx", "config", "config.yaml")
EXAMPLE_CONFIG = os.path.join(BASE_DIR, "torrentbotx", "config", "example.yaml")

def create_venv():
    if not os.path.exists(VENV_DIR):
        print("🎯 未检测到虚拟环境，正在创建 venv ...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
        print("✅ 虚拟环境已创建：", VENV_DIR)
    else:
        print("✅ 已检测到虚拟环境：", VENV_DIR)

def pip_install():
    print("🔄 安装/升级 pip 及依赖 ...")
    pip_path = os.path.join(VENV_DIR, "bin", "pip")
    subprocess.check_call([pip_path, "install", "--upgrade", "pip"])
    subprocess.check_call([pip_path, "install", "-r", REQ_FILE])
    print("✅ 依赖已全部安装。")

def check_config():
    if not os.path.exists(CONFIG_PATH):
        print("⚠️ 未找到配置文件 config.yaml，正在复制 example.yaml ...")
        shutil.copy(EXAMPLE_CONFIG, CONFIG_PATH)
        print("✅ 已生成配置文件:", CONFIG_PATH)
    else:
        print("✅ 已检测到配置文件:", CONFIG_PATH)

def init_db():
    print("🔄 检查并初始化数据库表结构 ...")
    pip_path = os.path.join(VENV_DIR, "bin", "python")
    subprocess.check_call([pip_path, DB_SETUP])
    print("✅ 数据库检查/初始化完成。")

def main():
    create_venv()
    pip_install()
    check_config()
    init_db()

    print("\n🎉 项目环境准备完成！")
    print("下一步：")
    print(f"  source {VENV_DIR}/bin/activate")
    print(f"  python run.py")

if __name__ == "__main__":
    main()
