
# IoTtalk information
ServerURL = 'https://farm.iottalk.tw'
device_name = 'NanZhuang'
# unit: second. ODF polling cycle (How long an ODF will be pulled)(每次要詢問是否有新訊息的間隔時間)
polling_cycle = 600


# WatchDog information
# unit: second. How long WatchDog will check the ODF timestamp (每此時間檢查訊息是否有在expiry_time內收進來)
inspection_cycle = 1800
# unit: second. Longer than expiry_time, sends LINE notification. Note: There are frequent false alerts if expiry_time <= polling_cycle.
expiry_time = 1800
log_path = r'/home/user1/WatchDog/log'  # log資料夾的路徑


# LINE notify token (在LINE notify網頁註冊的權杖)
token_key = 'eOUh7Jm8IeEHqLzWcLz8ezBNPBgsbRBtk6zrl77qXbn'
