#  Created date  : 2016-9-5
#  python version: 3.5
#  created by    : David

import urllib

from urllib.request import *

 
class ConItnt:
	i=6
	data=[]

	def	__init__(self):		#invoked as instantiation
		data=[1,2,3,4,5]
		for i in data:
			print(i,"initialed as instantiation")

	def func(self):
		print("this is a function.")


	def conn(self):
		try:
			with urlopen("http://stackoverflow.com/questions/5685406/inconsistent-use-of-tabs-and-spaces-in-indentation",timeout=10) as target:
				for t in target:
					print(t)
			
		except expression as identifier:
			print(identifier)




if __name__=='__main__':
	x=ConItnt()
	x.conn()
