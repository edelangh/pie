
from subprocess import Popen, PIPE
import config
import re

module_name = 'giveme'

cmd = 'curl http://'+config.node_ip+'/chat/opencanal/benjamin'

def interest(input):
	res = re.search('.*give.*me.*', input);
        return res != None

def input(input):
	proc = Popen(cmd, stdout=PIPE)
        res = ''
        for line in iter(proc.stdout.readline, ''):
            res = res + line + '\n'
        return res
