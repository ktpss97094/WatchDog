# -*- coding: utf-8 -*-
import time, requests
from datetime import datetime as dt
import LINE_notify as LINE
import config

inspection_cycle = config.inspection_cycle # unit: second
expiry_time = config.expiry_time # unit: second

device_list={}

def update(device_id, device_name, timestamp):
    global device_list
    try:
        if '.' not in timestamp: timestamp = timestamp + '.000000'
        ts = dt.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
        device_list[device_id]= {'d_name':device_name, 'ts':ts}
        print('Update: {}, {}, {}'.format(device_id, device_name, timestamp))
        return True
    except ValueError as e:
        print('Wrong time format:', e)
        return False

def main():
    while True:
        for d_id in list(device_list):
            elapsed_time = (dt.now() - device_list[d_id]['ts']).total_seconds() 
            #print('Elapsed_time: {}, {}'.format(elapsed_time, device_list[d_id]['d_name']))        
    
            if elapsed_time > expiry_time:
                msg = '裝置{}疑似離線, 離線總時間{:1.0f}秒'.format(device_list[d_id]['d_name'], elapsed_time)
                print(msg)
                LINE.line_notify(msg)

        time.sleep(inspection_cycle)

