import requests
requests.packages.urllib3.disable_warnings()
import re
import threading


def get_config():
    result = ''
    with open('job1_config.txt', 'r', encoding='utf-8') as f:#encoding出过问题
        for line in f:
            if len(line)!=0 :
               line=line.strip(' ')
               result=result+line.strip('\n')
    return result

def make(find):
    dic = []
    for x in find:
        partition = 0
        for y, y_value in enumerate(x):
            if y_value == ':':
                partition = y
                break
        key = x[:partition]
        value = x[partition + 1:]
        dic.append([key, value])
    return dic

def request_POST(argument,csrftoken,cookie):
    try:
        post_header = re.findall(r"post_header:(.*?),", get_config())
        base_url = re.findall(r"base_url:(.*?),", get_config())
        headers={
            make(post_header)[0][0]: make(post_header)[0][1]+csrftoken,
            make(post_header)[1][0]: make(post_header)[1][1]+cookie,
        }
        #print('1、headers:',headers)
        url=base_url[0]+argument[1]
        #print('2、url:',url)
        params=argument[2]
        #print('3、params:',params)
        if make(post_header)[0][0] in params:
            params={make(post_header)[0][0]: csrftoken}
        r=requests.post(url=url,params=params,headers=headers, verify=False)
        #print('4.:',r)
        return r.text[:50],r.status_code

    except Exception as e:  # 用Exception表示一下子抓住所有异常，这个一般情况下建议在异常最后面用，用在最后抓未知的异常
        print('Exception:',e)
        #print('Exception:',argument)
        return False,False

def request_GET(argument,csrftoken,cookie):
    #print('进入GET')
    try:
        get_headers = re.findall(r"get_header:(.*?),", get_config())
        base_url = re.findall(r"base_url:(.*?),", get_config())
        headers={
            make(get_headers)[0][0]: make(get_headers)[0][1]+csrftoken,
            make(get_headers)[1][0]: make(get_headers)[1][1]+cookie,
        }
        #print('1、headers:',headers)
        url = base_url[0] + argument[1]
        #print('2、url:',url)
        r = requests.get(url=url, headers=headers, verify=False)
        return r.text[:50],r.status_code

    except Exception as e:  # 用Exception表示一下子抓住所有异常，这个一般情况下建议在异常最后面用，用在最后抓未知的异常
        print(e)
        print(argument)
        return ''


def Url_kind(vlaue):
    kind_atart = vlaue[::-1].find('?')
    kind_end = vlaue[::-1].find('.')
    if kind_atart > 0:
        kind = vlaue[::-1][kind_atart:kind_end][::-1]
    else:
        kind = vlaue[::-1][:kind_end][::-1]
    return kind


