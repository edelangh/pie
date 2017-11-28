
# Add app path in PythonPath

import sys
import os
sys.path.append(os.getcwd())

# Data
import data

# Module
from modules_manager import modulesTab

# os execv
from os import system
from os import popen

# Google Text to Speech
from gtts import gTTS

# other
import time

# =========== tmp =============

import socket
import re

serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
#serversocket.setblocking(0)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(("localhost", 8080))
serversocket.listen(1)

def getinput():
	text = "0"
	try:
		(client, address) = serversocket.accept()
		data_txt = client.recv(2048)
		try:
			text = re.search('GET /([^ ]*)', data_txt).group(1)
		except AttributeError:
			print 'Error parse: ' + data_txt
		client.close()
	except socket.error:
		print 'Connec'
	return text

# ========== function ===========

from subprocess import Popen

# from pygame import mixer # Load the required library

def say(text):
	print text
	tts = gTTS(text=text, lang=data.lang)
	tts.save(data.file_path)
        print data.cmd_player
	Popen(data.cmd_player)


# ============ start =============

print modulesTab

say(data.hello)

while True:
	input = getinput()
	print 'New input: ' + input
	for m in modulesTab:
		if m.interest(input):
			res = m.input(input)
                        res = res.lower();
                        print res
			say(res)
	time.sleep(2)

