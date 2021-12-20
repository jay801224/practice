from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.error import HTTPError
import unittest
import requests.packages.urllib3


urllist = [
('cs8901','https://sta.x2casino.com/our-games','https://sta.x2casino.com/user/login'),
('cs8902','https://idngoal.com/','https://idngoal.com/login'),
('cs8903','https://tangkasbet88.asia/','https://tangkasbet88.asia/user/login'),
('cs8904','https://botangslots.com/','https://botangslots.com/user/login'),
('cs8905','https://dewatangkas.fun/','https://dewatangkas.fun/user/login'),
('cs8906','http://dewagg.com/','http://dewagg.com/login'),
('cs8907','https://kdslots.com/','https://kdslots.com/login'),
('cs8908','https://dewatagames.com/','https://dewatagames.com/login'),
('cs8909','https://alexavegas.com/','https://alexavegas.com/loginUser'),
('cs8910','https://paiza99.me/','https://paiza99.me/loginUser'),
('cs8911','https://dewascore.com/id','https://dewascore.com/login'),
('cs8912','https://dewabet.asia/id','https://dewabet.asia/login'),
('cs8913','https://nagaikan.com/','https://nagaikan.com/login'),
('cs8914','https://mildcasino.asia/','https://mildcasino.asia/loginUser'),
('cs8915','https://lemacaubet.com/','https://lemacaubet.com/loginUser'),
('cs8916','https://unovegas.org/','https://unovegas.org/loginUser'),
('cs8917','https://vegas88.cc/','https://vegas88.cc/loginUser'),
('cs8918','https://mejahoki.org/','https://mejahoki.org/loginUser'),
('cs8919','https://dewacasino88.com/','https://dewacasino88.com/loginUser'),
('cs8920','https://asialive88.asia/','https://asialive88.asia/loginUser'),
('cs8921','https://dewavegas99.com/','https://dewavegas99.com/loginUser'),
('cs8922','https://igm247.co/','https://igm247.co/loginUser')
]

urllist.sort(key =lambda s:s[0])

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

for (agentcode,link,link2) in urllist :
	try:
		requests.packages.urllib3.disable_warnings()
		print (agentcode,link)
		reqlink = requests.get(link, timeout=10,headers=headers, verify=False, allow_redirects=False)
		print(reqlink.status_code)
		if reqlink.status_code == 200: 
			print ('It is fine.')
		elif 400 <= reqlink.status_code <=  405 :
			print ('client error ') 
		elif 300 <= reqlink.status_code <=  305 :
			print ('似乎被擋了') 	
		elif 500 <= reqlink.status_code < 503  or  503 < reqlink.status_code <= 505 :
			print ('backend error ')
		elif reqlink.status_code == 503 :
		    print("維護中")	
		elif reqlink.status_code == 522 :
		    print("域名還沒開")
		else :
		    print("?????")
	except:
		print('不明狀況')

