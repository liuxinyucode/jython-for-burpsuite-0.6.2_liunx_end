import re
class Get_Burpsuite_Info:
    def __init__(self,result_path):
        self.result_path=result_path
        self.read = self.Read_Config()[0]
        self.all_read = self.Read_Config()[1]
    def Get_Config(self):
        result = []
        with open('save_config.txt', 'r', encoding='utf-8') as f:#encoding出过问题
            for line in f:
                if len(line)!=0 :

                    result.append(line.strip('\n'))
        return result
    def Read_Config(self,):
        result = []
        all_result=[]
        with open(self.result_path, 'r', encoding=self.Get_Config()[1]) as f:#encoding出过问题
            for line in f:
                all_result.append(line.strip('\n'))
                if len(line)!=0 and self.Get_Config()[5] in line and line not in result:
                    result.append(line.strip('\n'))
        return result,all_result
    def Get_URL(self,x):
        url = re.search(self.Get_Config()[7], self.read[x]).group()
        value = self.Get_Config()[7].find('(.*?)')
        value = value + 4 - len(self.Get_Config()[7])
        url = url[:value]
        return url


    def Get_POST_Params(self,target):
        params = str(target).strip('\n') + '&'
        find = re.findall(r'(.*?)&', params)
        dic = {}
        for x in find:
            partition = 0
            for y, y_value in enumerate(x):
                if y_value == '=':
                    partition = y
                    break
            key = x[:partition]
            value = x[partition + 1:]
            dic.update({key: value})
        return dic


    def Get_user_info(self):
        for x in range(len(self.read)):
            #print(x)
            url=self.Get_URL(x)
            dic = {'':''}
            if 'POST' in self.read[x][1:5]:
                #print('POST',url)
                for y,y_value in enumerate(self.all_read):
                    if url in y_value:
                        #print(Get_params(all_read[y+1]))
                        dic=self.Get_POST_Params(self.all_read[y+1])
                        break
                yield 'POST',url,dic
            if 'GET' in self.read[x][1:5]:
                #print('GET',url)
                yield 'GET',url









