#  Created date  : 2016-9-5
#  python version: 3.5
#  created by    : David

import urllib

from urllib.request import urlopen
try:
	with	urlopen("http://stackoverflow.com/questions/5685406/inconsistent-use-of-tabs-and-spaces-in-indentation", timeout=2)	as	present:	
		for target_list in present:
			print(target_list)	
	print("working connection") 
except Exception as err:
	print(err)
