import time
import re

class Get_Selenium_Info:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(self.Read_Config()[1])
        self.key = self.Read_Config()[13]
        self.value = self.Read_Config()[15]

    def Read_Config(self):
        result = []
        with open('login_config.txt', 'r', encoding='utf-8') as f:#encoding出过问题
            for line in f:
                if len(line)==0:
                    line='null'
                result.append(line.strip('\n'))
        #results = [result[1],result[3],result[5],result[7],result[9],result[11],result[13]]
        return result

    def Logining(self):
        try:
            self.driver.refresh()
        except:
            print('Selenium Error')
            return 'Selenium Error'

        try:
            self.driver.find_element_by_xpath(self.Read_Config()[3]).send_keys(self.key)
            time.sleep(0.1)
            self.driver.find_element_by_xpath(self.Read_Config()[5]).send_keys(self.value)
            time.sleep(0.1)
            self.driver.find_element_by_xpath(self.Read_Config()[7]).click()
        except:
                #print('Not Logout')
                #return 'Not Logout'
                pass
        finally:
            try:
                cookies = self.driver.get_cookies()
                cookie = re.findall(self.Read_Config()[11], str(cookies))
                csrftoken = re.findall(self.Read_Config()[9], self.driver.page_source)
                #print('0、From Selenium:',csrftoken, cookie)
                return csrftoken[0],cookie[0]
            except:
                try:
                    print('Second Refresh')
                    self.driver.refresh()
                    self.driver.find_element_by_xpath(self.Read_Config()[3]).send_keys(self.key)
                    time.sleep(0.1)
                    self.driver.find_element_by_xpath(self.Read_Config()[5]).send_keys(self.value)
                    time.sleep(0.1)
                    self.driver.find_element_by_xpath(self.Read_Config()[7]).click()
                    cookies = self.driver.get_cookies()
                    cookie = re.findall(self.Read_Config()[11], str(cookies))
                    csrftoken = re.findall(self.Read_Config()[9], self.driver.page_source)
                    return csrftoken[0], cookie[0]
                except:
                    time.sleep(5)
                    print('Selenium Error,Failed')

    def Driver_Quit(self):
        self.driver.quit()