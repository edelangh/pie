import win32clipboard
import json
import re
from subprocess import Popen, PIPE

import config
#import urllib2
#import zlib
#import gzip

try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


module_name = 'googleit'

def interest(input):
	res = re.search('.*[gG]oogle.*', input);
	return res != None

def input(input):
	# get clipboard data
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	question = data
        url = "https://www.google.fr/search"
	params = {'q': question}

	url_parts = list(urlparse.urlparse(url))
	query = dict(urlparse.parse_qsl(url_parts[4]))
	query.update(params)
	url_parts[4] = urlencode(query)
	res = urlparse.urlunparse(url_parts)
	print res
	question = res
	url = "http://"+config.node_ip+"/tasks/benjamin/open"
	params = {'url': question}

	url_parts = list(urlparse.urlparse(url))
	query = dict(urlparse.parse_qsl(url_parts[4]))
	query.update(params)
	url_parts[4] = urlencode(query)
	res = urlparse.urlunparse(url_parts)
	print res
	proc = Popen('curl \'' + res + '\'', stdout=PIPE)
	return 'ok, i will open google for your needs'
