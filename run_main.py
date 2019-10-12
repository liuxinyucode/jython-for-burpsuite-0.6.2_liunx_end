from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from main import Main
from get_burpsuite_info import Get_Burpsuite_Info
import threading
import to_mysql
import datetime
driver = webdriver.Remote(
    command_executor="192.168.99.100:32775/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME)

if __name__ == '__main__':
    Requsets = Get_Burpsuite_Info('get_url_burpsuite.txt').Get_user_info()
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    value = ('IM', 0, 'admin', create_time, None, None)
    to_mysql.sec_task_INSERT(value)
    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    value = (1,start_time, create_time)
    to_mysql.sec_task_UPDATA(value)
    taskid=to_mysql.sec_task_SELECT(create_time)

    while True:
        try:
            get_Requset=next(Requsets)
            Main().main(driver=driver, argument=get_Requset,taskid=taskid)
        except:
            driver.close()
            finish_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            value = (2,finish_time, create_time)
            to_mysql.sec_task_UPDATA_finish(value)
            break















