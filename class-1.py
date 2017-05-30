class Hello:
	def greet(self,name): #类里面用 def 定义方法，它不叫函数，因为每一个方法的第一个参数都是 self，但在调用时我们不必提供，程序会自动i				将第一个参数绑定到所属的实例上
		print("Hello,"+name)

me=Hello() #要加（）不然，不是实例
me.greet('Cheng')  #只需第一个参数 
