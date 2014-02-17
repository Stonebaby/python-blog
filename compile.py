'''import _config in site.py'''

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, currentdir) 

from _includes.site import Site
	
content = Site()
content.compile()