square=lambda x : x**2
print(square(3))

sum=lambda x,y : x+y
print(sum(2,3))
#以上函数等于以下函数：
def square(x):
	return(x**2)
print (square(3))
# """
#python 使用 lambda 表达式来创建匿名函数
# lambda只是一个表达式，函数体比def简单很多
#lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
#lambda函数拥有自己的名字空间，且不能访问自有参数列表之外或全局名字空间里的参数
#虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
#"""
#可以这样认为,lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体。在这里lambda简化了函数定义的书写形式。是代码更为简洁，但是使用函数的定义方式更为直观，易理解。
