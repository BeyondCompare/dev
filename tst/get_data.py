import requests
from bs4 import BeautifulSoup
import json

HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'http://stats.nba.com/scores/'}
res = requests.get("https://tvc4.forexpros.com/1e3d1724c903dac1f334c4f12f15a234/1535941605/6/6/28/history?symbol=945629&resolution=15&from=1534645517&to=1534647317", headers=HEADERS)
#res = requests.get("https://tvc4.forexpros.com/1e3d1724c903dac1f334c4f12f15a234/1535941605/6/6/28/history?symbol=945629&resolution=15&from=1534645517&to=1535941577", headers=HEADERS)
#res = requests.get("https://tvc4.forexpros.com/1e3d1724c903dac1f334c4f12f15a234/1535941605/6/6/28/history?symbol=945629&resolution=15&from=1497606300&to=1497607400", headers=HEADERS)
soup = BeautifulSoup(res.content)
print (soup)
data_dict = json.loads(str(soup))
for key in data_dict:
	print(key,data_dict[key])
	#print("%s:%f",key,data_dict[key])

