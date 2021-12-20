from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.error import HTTPError
import unittest
import requests.packages.urllib3

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
requests.packages.urllib3.disable_warnings()

urllist = [
('test0001','http://x2casinov2.8belasbet.com/our-games'),
('test0002','https://dewabetdev.com/')
]
urllist.sort(key =lambda s:s[0])

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

for (agentcode,link) in urllist :
	try:
		print (agentcode,link)
		reqlink = requests.get(link, headers=headers, verify=False)
	except HTTPError as e:
		print(e.code)
		print(e.reason)
	except URLError as e:
		if hasattr(e, 'reason'):
			print('We failed to reach a server.')
			print('Reason: ', e.reason)
		elif hasattr(e, 'code'):
			print('The server couldn\'t fulfill the request.')
			print('Error code:', e.code)
	else:
		print('It is fine.')
