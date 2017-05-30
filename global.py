x=60
def func():
	global x #定义全局变量x
	
	print("x is",x) #打印全局变量
	x=2
	print("Changed global x to",x)
 
#x=50 #先执行全局变量
func()#再执行函数
print ("Value of x is",x)
