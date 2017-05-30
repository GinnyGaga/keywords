class A:
	def printA(self):
		print("in A...")
class B(A):#继承--将其他类名写在class语句后的圆挂号内就表示继承于某类（B继承于A，B是A的子类）---class 类名（基类名）
	def printB(self):
		print("in B...")

print(issubclass(A,B))#判断 A不是B的子类
print(issubclass(B,A))#判断 B是A的子类
print(B.__bases__) #打印B的基类为A
b=B()
print(isinstance(b,B))# 询问b是否是B的实例
print(b.printA()) #访问A中的方法
print(b.printB())
