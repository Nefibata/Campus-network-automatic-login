import requests    # 用于向目标网站发送请求
import socket
def get_host_ip(): # 查询本机ip并且返回ip
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
# 这是你需要根据自己的情况修改的地方


url = 'http://10.160.63.9:801/eportal/?c=Portal&a=login&callback=dr1683867797076&login_method=1&user_account='+'你的账号'+'@'+'账号的网络类型'+'@cmcc&user_password='+'账号密码'+'&wlan_user_ip='+get_host_ip()+'&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.0&_=1683852619821'
response = requests.get(url).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
print("状态码{}".format(response))  # 打印状态码
