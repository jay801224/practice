import requests
from bs4 import BeautifulSoup
import urllib.request,urllib.parse

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

def login_gettoken():
    url="http://x2casinov2.8belasbet.com/"  # 欲查詢網址
    loginsession = requests.Session()  # 模擬登陸
    response = loginsession.get(url)  # 獲得登陸頁面
    soup = BeautifulSoup(response.text)
    token = soup.form.find("input",{"name":"_token"})["value"]  # 獲得隱藏token
    values = {  # 填写post信息
          "username":"userc15",
          "password":"qwe123",
          "_token":token
           }
    r = loginsession.post(url, data = values, headers=headers, verify=False)  # 送出post

    return token
    print(r)

def originalurl_get():
    login_gettoken()
    # gameurl="https://cashprize.asia/launch-game/?brand=dewatangkasdev&game_url=aHR0cHM6Ly9zYW5kYm94LWFwaS5sYWtqc2RmZ2JxMzQ3OGRmaGFsc2VmaHE4OS5jb20vZ2FtZS9hdXRoP29wZXJhdG9ySWQ9Mjg3NDk1MTMwJnRva2VuPUZ2VXNjR2dyeTMySXRkMFkwZ2NoR1F3NUNsdVB0MTNTc0NQT2NoNkImZ2FtZUlkPWlzXzE5MDMmY3VycmVuY3k9SURSJmxhbmd1YWdlPWlkJmxvYmJ5VXJsPWh0dHA6Ly94MmNhc2lub3YyLjhiZWxhc2JldC5jb20=&session=FvUscGgry32Itd0Y0gchGQw5CluPt13SsCPOch6B&username=DWTKUSERC13&game_id=is_1903&hash=2b1eb2107da3e2782dee98b9d40f8d70/get"
    gameurl="http://x2casinov2.8belasbet.com/play/is_1820"
    urlsession = requests.get(gameurl)
    # soup = BeautifulSoup(urlsession.text)
    # urlga = soup.form.find("input",{"name":"_ga"})["value"]
    # urlgid = soup.form.find("input",{"name":"_gid"})["value"]
    # urlxsrftoken = soup.form.find("input",{"name":"XSRF-TOKEN"})["value"]
    # urlidnlivetesting = soup.form.find("input",{"name":"idnlivetesting"})["value"]
    # data = {
    #       "_ga":urlga,
    #       "_gid":urlgid,
    #       "popup":"userc15",
    #       # "_gat_gtag_UA_73285344_1":"1",
    #       "XSRF-TOKEN":urlxsrftoken,
    #       "idnlivetesting":urlidnlivetesting
    #        }
    # try :
    #     redirectsession = requests.get(gameurl, data = data, headers=headers, verify=False)
    #     if redirectsession.status_code == 200 :
    #         print('It is fine.')
    #         print(redirectsession.text)
    #     else :
    #         print('nonono')
    # except :
    #     print('?????????????????')
    return (urlsession.cookies)
def gameurl_get():
    login_gettoken()
    originalurl_get()
    return (url)

if __name__ == '__main__':
    print(login_gettoken())
    print(originalurl_get())
    print(gameurl_get())
 



