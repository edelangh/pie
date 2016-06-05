
from subprocess import Popen, PIPE
import re

module_name = 'date'

cmd = 'date +"It is %H Hours %M and we are the %A of %B"'

def interest(input):
	res = re.search('.*what.*(date|time).*', input);
        return res != None

def input(input):
	proc = Popen(cmd, stdout=PIPE)
        res = ''
        for line in iter(proc.stdout.readline, ''):
            res = res + line + '\n'
        return res
