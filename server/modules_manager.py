from modules_dir import *
import modules_dir
import inspect

modules = []

for m in modules_dir.__dict__.iteritems():
	if inspect.ismodule(m[1]):
		try:
			print 'module loaded: ' + m[1].module_name
			modules.append(m[1])
		except AttributeError:
			continue 
