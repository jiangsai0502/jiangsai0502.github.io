#### 代码控制小米智能插

> [参考](https://blog.csdn.net/linzhiji/article/details/118194526)

```python
# 安装
pip3 install pycryptodome pybase64 requests
 
# 获取代码
git clone https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor

# 进项目目录
cd Xiaomi-cloud-tokens-extractor

# 获取token
python3 token_extractor.py
```

```bash
# 小米账号
Username (email or user ID): 2705000885
# 账号密码
Password: Js1122334
# 服务名称
Server (one of: cn, de, us, ru, tw, sg, in, i2) Leave empty to check all available: cn

Devices found for server "cn" @ home "58001483858":
   ---------
   NAME:     Mijia Smart Plug 3
   ID:       695877993
   MAC:      D4:F0:EA:01:65:F4
   IP:       192.168.0.102
   TOKEN:    6bd461b66ac46bee47392f22ec121d40
   MODEL:    cuco.plug.v3
   ---------
```

```python
# 安装python-miio库
pip3 install python-miio

# 获取设备信息（没用）
miiocli device --ip IP --token TOKEN info
 
 
# 获取插座状态（没用）
miiocli -d device --ip YOUR_DEVICE_IP --token YOUR_DEVICE_TOKEN raw_command get_properties "[{'did': 'MYDID', 'siid': 2, 'piid': 1 }]"
 
 
# 开
miiocli -d device --ip YOUR_DEVICE_IP --token YOUR_DEVICE_TOKEN raw_command set_properties "[{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':True}]"
 
# 关
miiocli -d device --ip YOUR_DEVICE_IP --token YOUR_DEVICE_TOKEN raw_command set_properties "[{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':False}]"
```

完整代码

```python
import subprocess
import time


def TurnOn():
    """打开开关"""
    command = [
        "miiocli",
        "-d",
        "device",
        "--ip",
        "192.168.0.102",
        "--token",
        "6bd461b66ac46bee47392f22ec121d40",
        "raw_command",
        "set_properties",
        "[{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':True}]",
    ]
    subprocess.run(command, capture_output=True, text=True)


def TurnOff():
    """关闭开关"""
    command = [
        "miiocli",
        "-d",
        "device",
        "--ip",
        "192.168.0.102",
        "--token",
        "6bd461b66ac46bee47392f22ec121d40",
        "raw_command",
        "set_properties",
        "[{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':False}]",
    ]
    subprocess.run(command, capture_output=True, text=True)


if __name__ == "__main__":
    while True:
        TurnOn()
        time.sleep(300)
        TurnOff()
        time.sleep(600)
```

