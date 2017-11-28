from modules import *
import modules
import inspect

modulesTab = []

for m in modules.__dict__.iteritems():
	if inspect.ismodule(m[1]):
		try:
			print 'module loaded: ' + m[1].module_name
			modulesTab.append(m[1])
		except AttributeError:
			continue 
