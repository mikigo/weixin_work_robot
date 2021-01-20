import requests, json
import datetime
import time

# 管理小组群的接口地址
wx_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b01af1d3-9d42-4ef7-a0de-15a76109a167"


def send_msg(content):
    data = json.dumps({"msgtype": "text", "text": {"content": content, "mentioned_list": ["@all"]}})
    r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))
    print(r.json)


def friday_doit():
    while True:
        if datetime.datetime.now().weekday() == 4 and \
                datetime.datetime.now().strftime("%H") == '9' and \
                datetime.datetime.now().strftime("%M") == '59' and \
                datetime.datetime.now().strftime("%S") == '59':
            send_msg("筒子们，填工时啦~")
        time.sleep(1)

if __name__ == '__main__':
    friday_doit()