from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.error import HTTPError
import unittest
import urllib.request

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()

urllist = [
('cs8901','https://sta.x2casino.com/our-games'),
('cs8902','https://idngoal.com/'),
('cs8903','https://tangkasbet88.asia/'),
('cs8904','https://botangslots.com/'),
('cs8905','https://dewatangkas.fun/'),
('cs8906','http://dewagg.com/'),
('cs8907','https://kdslots.com/'),
('cs8908','https://dewaslots.com'),
('cs8909','https://alexavegas.com/'),
('cs8910','https://paiza99.me/'),
('cs8911','https://dewascore.com/id'),
('cs8912','https://dewabet.asia/id'),
('cs8913','https://nagaikan.com/')
]

urllist.sort(key =lambda s:s[0])

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

for (agentcode,link) in urllist :
	try:
		print (agentcode,link)
		reqlink = urllib.request.urlopen(link, headers=headers,timeout=3,cafile=None, capath=None, cadefault=False, context=None)
	except urllib.request.HTTPError as e:
		print(e.code)
		print(e.reason)
	except urllib.request.URLError as e:
		if hasattr(e, 'reason'):
			print('We failed to reach a server.')
			print('Reason: ', e.reason)
		elif hasattr(e, 'code'):
			print('The server couldn\'t fulfill the request.')
			print('Error code:', e.code)
	else:
		print('It is fine.')
