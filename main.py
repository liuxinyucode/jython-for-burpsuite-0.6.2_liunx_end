from get_selenium_info import Get_Selenium_Info as Selenium_Info
from rewrite_post_get import request_POST,request_GET
import to_mysql
import threading
#if __name__ == '__main__':
class Main():
    def __init__(self):
        pass
    def main(self,driver,argument,taskid):
            URL_Responses = []
            URL_Responses.append(taskid)
            #print('Start:',argument)
            URL_Responses.append(argument[0])
            URL_Responses.append(argument[1])
            if 'POST' in argument[0]:
                try:
                    #第一次获取token和对应的session
                    csrftoken, cookie = Selenium_Info(driver).Logining()
                    response = request_POST(argument=argument, csrftoken=csrftoken, cookie=cookie)
                    URL_Responses.extend(list(response))

                    #print('5、Response:',response)
                    #刷新
                    # 第2次获取token和对应的session,需要和第一次相同
                    refresh_csrftoken,refresh_cookie = Selenium_Info(driver).Logining()
                    refresh_response = request_POST(argument=argument, csrftoken='wrong_csrftoken', cookie=refresh_cookie)

                    if refresh_response:
                        #print('6、Refresh_response:',refresh_response)
                        URL_Responses.extend(list(refresh_response))
                    else:
                       #print('6、Refresh_response:','no_response')
                       URL_Responses.append('no_response')
                       URL_Responses.append('no_response')
                    #print(end2)

                    # 更换token后返回值是否相同,鉴权
                    if response == refresh_response:
                        URL_Responses.append('Same')
                        #print('7、Same')
                    elif response != refresh_response:
                        URL_Responses.append('Different')
                        #print('7、Different')
                    else:
                        URL_Responses.append('Abnormal')
                        #print('7、Abnormal')
                    #刷新
                    # 第3次获取token和对应的session,需要和第2次相同和第一次不同
                    second_refresh_csrftoken,second_refresh_cookie = Selenium_Info(driver).Logining()
                    # cookie是否相同,判断是否重新登录过
                    if cookie == second_refresh_cookie:
                        URL_Responses.append('Not Logout')
                        #print('8、Not Logout')
                    else:
                        URL_Responses.append('Logout')
                        #print('8、Logout')

                except Exception as e:  # 用Exception表示一下子抓住所有异常，这个一般情况下建议在异常最后面用，用在最后抓未知的异常
                    print('Exception:',e)
                    #xlsx_write(save_path=save_path, sheet='catalog', x=number, y=5, value='Failed', switch=False)
                    #xlsx_write(save_path=save_path, sheet='catalog', x=number, y=6, value='Failed', switch=False)


            elif 'GET' in argument[0]:
                try:
                    # 第一次获取token和对应的session
                    csrftoken, cookie = Selenium_Info(driver).Logining()
                    response = request_GET(argument=argument, csrftoken=csrftoken, cookie=cookie)
                    URL_Responses.extend(list(response))
                    #print('response:', response)
                    # 刷新
                    # 第2次获取token和对应的session,需要和第一次相同
                    refresh_csrftoken,refresh_cookie = Selenium_Info(driver).Logining()
                    refresh_response = request_GET(argument=argument, csrftoken='wrong_csrftoken',
                                                                    cookie=refresh_cookie)
                    if refresh_response:
                        URL_Responses.extend(list(refresh_response))
                        #print('refresh_response:', refresh_response)
                    else:
                        URL_Responses.append('no_response')
                        URL_Responses.append('')
                        #print('no_response')
                    # print(end2)

                    # 更换token后返回值是否相同,鉴权
                    if response == refresh_response:
                        URL_Responses.append('Same')
                        #print('Same')
                    elif response != refresh_response:
                        URL_Responses.append('Different')
                        #print('Different')
                    else:
                        URL_Responses.append('Abnormal')
                        #print('Abnormal')
                    # 刷新
                    # 第3次获取token和对应的session,需要和第2次相同和第一次不同
                    second_refresh_csrftoken,second_refresh_cookie = Selenium_Info(driver).Logining()
                    #print('second_refresh_cookie:',second_refresh_cookie)
                    # cookie是否相同,判断是否重新登录过
                    if cookie == second_refresh_cookie:
                        URL_Responses.append('Not Logout')
                        #print('Not Logout')
                    else:
                        URL_Responses.append('Logout')
                        print('Logout')

                except Exception as e:  # 用Exception表示一下子抓住所有异常，这个一般情况下建议在异常最后面用，用在最后抓未知的异常
                    print('Exception：',e)

            threading.Thread(target=to_mysql.sec_xss_INSERT,args=(URL_Responses,)).start()
            #to_mysql.run(URL_Responses)
            print('End:',URL_Responses)

