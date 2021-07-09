
#IoTtalk information
ServerURL = 'IoTtalk Server URL' 
device_name = 'Assing a name for WatchDog'
polling_cycle = 600 # unit: second. ODF polling cycle (How long an ODF will be pulled)


#WatchDog information
inspection_cycle = 1800 # unit: second. How long WatchDog will check the ODF timestamp
expiry_time = 1200 # unit: second. Longer than expiry_time, sends LINE notification. Note: There are frequent false alerts if expiry_time <= polling_cycle.
log_path = r'the dictionary storing log'


#LINE notify token
token_key = 'Put LINE notify token here'


