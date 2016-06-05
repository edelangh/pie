import win32clipboard
import json
import re
from subprocess import Popen, PIPE

#import urllib2
#import zlib
#import gzip

try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


module_name = 'youtube'

youtube_action = 0

def interest(input):
	global youtube_action
	res = re.search('.*(music|song|play).*', input)
	res2 = re.search('.*next.*', input)
	if res2 != None:
		print "Super youtuve !!!!"
		youtube_action = 1
		return True
	youtube_action = 0
	return res != None

def input(input):
	print youtube_action
	if youtube_action == 1:
		proc = Popen('curl \'http://192.168.0.12:8000/tasks/benjamin/new?action=nextYoutube\'', stdout=PIPE)
		res = ''
		for line in iter(proc.stdout.readline, ''):
			res = res + line + '\n'
		return res

	# get clipboard data
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	question = data
	url = "https://www.youtube.com/watch"
	params = {'v': 'uB85RY2Xk_U'}

	url_parts = list(urlparse.urlparse(url))
	query = dict(urlparse.parse_qsl(url_parts[4]))
	query.update(params)
	url_parts[4] = urlencode(query)
	res = urlparse.urlunparse(url_parts)
	print res
	question = res
	url = "http://192.168.0.12:8000/tasks/benjamin/open"
	params = {'url': question}

	url_parts = list(urlparse.urlparse(url))
	query = dict(urlparse.parse_qsl(url_parts[4]))
	query.update(params)
	url_parts[4] = urlencode(query)
	res = urlparse.urlunparse(url_parts)
	print res
	proc = Popen('curl \'' + res + '\'', stdout=PIPE)
	return 'ok, i will open your favority song for you'
