class C:
	def __test(self):
		print('in C...')
	def call(self):
		self.__test()  #类内访问私有方法和特性

c=C()
c.call()

#Python 中默认情况下的方法和特性都是公有的，如果你想变为私有的，那么要在方法和特性的名字前加上双下划线 
#所以，你不可能完全限制其他人无法访问到你的类中方法和特性，所以，Python 并不能实现完全的封装
