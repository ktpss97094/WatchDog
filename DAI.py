import time, requests, threading
import csmapi, DAN_extend as DAN, WatchDog
import config

ServerURL = config.ServerURL 
Reg_addr = None #if None, Reg_addr = MAC address

df_list=[]
for index in range(1,21): df_list.append('Monitor-O{}'.format(index))

DAN.profile['dm_name']= 'WatchDog'
DAN.profile['df_list']= df_list
DAN.profile['d_name']= config.device_name 

DAN.device_registration_with_retry(ServerURL, Reg_addr)

WDog = threading.Thread(target=WatchDog.main)
WDog.daemon = True
WDog.start()

while True:
    try:
        for index in range(1, 21):
            ODF = 'Monitor-O{}'.format(index)
            data = DAN.pull_with_ts(ODF)
            if data != None:
                device_id   = data[0][0][0] 
                device_name = data[0][0][1]
                timestamp = data[1]
                #print ('{}, {}, {}'.format(device_id, device_name, timestamp))
                WatchDog.update(device_id, device_name, timestamp)
            time.sleep(5)
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(config.polling_cycle)

