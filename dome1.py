
import to_mysql
import datetime
import time
create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
value = ('IM', 0, 'admin', create_time, None, None)
to_mysql.sec_task_INSERT(value)
time.sleep(2)
start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
value = (1,start_time,create_time )
to_mysql.sec_task_UPDATA(value)


print(to_mysql.sec_task_SELECT(create_time))
