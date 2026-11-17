import sys
import requests

print("Hello, 这是我的第一个 Python 程序")
print("Python 版本:", sys.version.split()[0])
print("解释器路径:", sys.executable)
print("requests 版本:", requests.__version__)

# 顺手验证一下能不能联网调接口（后面第 5 周要天天干这件事）
r = requests.get("https://pypi.org/pypi/requests/json", timeout=10)
print("联网测试状态码:", r.status_code)
