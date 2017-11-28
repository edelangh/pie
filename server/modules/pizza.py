import win32clipboard
import json
import re
import config
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


module_name = 'helpme'

def interest(input):
	res = re.search('.*pizza.*', input);
	return res != None

def input(input):
	# get clipboard data
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	'''
	print data
	data = data.replace(' ', '%20');
	data = data.replace('\'', '%27');
	url = 'http://api.stackexchange.com/2.2/search?order=desc&sort=activity&tagged=node.js&intitle='+data+'&site=stackoverflow'
	print url
	gz_data = urllib2.urlopen(url).read()
	print gz_data
	f = open('tmp.gzip', 'wb')
	f.write(gz_data)
	f.close()
	inF = gzip.open('tmp.gzip', 'rb')
	#text = inF.read()
	#print text
	print '============='
	res = json.load(inF);
	inF.close()

	nb = len(res['items'])
	print res['items'][0]['link']
	print '============='
	return "i have found " + nb + ' helps'
	'''
	question = data
        url = "https://commande.dominos.fr/eStore/fr/ConfirmPayment/Adyen"
        params = {'paymentMethod': 'CreditCard'}

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
	return 'ok, i will open stack for your needs'
