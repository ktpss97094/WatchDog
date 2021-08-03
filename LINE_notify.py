import requests
import lineTool
import config

def line_notify(msg):
    token_key = config.token_key
    header = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":'Bearer '+token_key}
    URL = 'https://notify-api.line.me/api/notify'
    payload = {'message':msg}
    res=requests.post(URL,headers=header,data=payload)

if __name__ == '__main__':
    msg = '\n 中文字測試'
    line_notify(msg)
