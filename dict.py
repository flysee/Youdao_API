#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib
import urllib2
import json

def get(url,key):
	data=urllib.urlencode(key)
	full_url=url+'&'+data
	response=urllib2.urlopen(full_url)
	rejson=response.read()
	response.close()
	return json.loads(rejson)
def output(re):
	try:
		for fy in re['basic']['explains']:
			print fy
		print re['web'][1]['key']
		for fy in re['web'][1]['value']:
			print fy
		print re['web'][2]['key']
		for fy in re['web'][2]['value']:
			print fy
		print '-'*20
	except:
			print 'null'
def main():
	url='http://fanyi.youdao.com/openapi.do?keyfrom=yewanyi&key=1276761752&type=data&doctype=json&version=1.1'
	dict='xx'
	while 1:
		try:
			dict=raw_input('Input what you want to translate.\n')
			if dict!='x':
				key={'q':dict}
				re=get(url,key)
			else:
				print 'bye'
				break
		except:
			print 'input error'
		else:
			output(re)
if __name__ == '__main__':
	main()
