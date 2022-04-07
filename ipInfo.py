import json
from urllib import request


def ip_info(ip):
	r = request.urlopen(f'http://ipinfo.io/{ip}/json')
	js = json.load(r)
	print(js)
	

ip_info('Some IP')