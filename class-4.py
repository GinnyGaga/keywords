#类定义
class people:
	name=''
	age=0 #定义基本属性
	__weight=0 #定义私有属性，私有属性在类外部无法直接进行访问
	def __init__(self,n,a,w): #定义构造方法
		self.name=n
		self.age=a
		self._weight=w
	def speak(self):
		print("%s 说：我 %d 岁。重 %d" % (self.name,self.age))

A=people('ginny',23,100)
A.speak()
