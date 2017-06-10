__author__ = 'lucas'

class attrtest(object):

	def __init__(self):
		
		pass
	def trygetattr0(self):
		self.name='lucas'
		print(self.name)
#equals to self.name
		print(getattr(self,'name'))
s=attrtest()
s.trygetattr0()

