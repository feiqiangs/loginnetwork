# -*- coding:utf-8 -*-
#author :sfq
#description: login ucas network.
#date:2016-6-26


import urllib2,threading,urllib,traceback,re,json

#********config**************
default_passwd = 'ucas'
input_file='nums'
#****************************

def login(num_str):
	header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0'}
	login_url = 'http://210.77.16.21/eportal/InterFace.do?method=login'
	post_data  ={'operatorPwd':'',	
		'password':'ucas',
		'queryString':'wlanuserip%3Df39d702ca0df2e11a2255c72882701a3%26wlanacname%3D5fcbc245a7ffdfa4%26ssid%3D%26nasip%3D2c0716b583c8ac3cbd7567a84cfde5a8%26mac%3Db797ed2ab023e626efebdf25e303b028%26t%3Dwireless-v2%26url%3D709db9dc9ce334aa55e551ef049661032a4bc5c1106b8d46a6a775f3f24d084359ff9091ee2edfe0897d8064c70cbffa2a1691f4121dff765e07d3e755773622',
		'service':'',
		'userId':num_str,
		'validcode':''}
	data_encode = urllib.urlencode(post_data)
	try:
		req = urllib2.Request(login_url,data_encode,header)
		cf = urllib2.urlopen(req)
		res = cf.read()
		return res
	except Exception,e:
		print traceback.format_exc()

f = open(input_file)
lines = f.readlines()
num_set = set()
for line in lines:
	tt = re.sub('\s','',line)
	if tt:
		num_set.add(tt)

for num in num_set:
	print 'using num:',num
	res = login(num)
	if res:
		json_data = json.loads(res)
		if json_data and json_data.has_key('result') and json_data['result']=='success':
			print 'login with num:',num,'!!!!'
			break	
	
