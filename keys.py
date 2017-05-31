Keyword:s#(关键字)
and-#与
def-#定义函数
from-#选择sys模组，例如from sys import argv
not- #非
while-#while-loop(while循环)：一直执行它下面的代码片段，直到它对应的布尔表达式为False时才会停下来。它有时会永不结束，它的用法：
	a:while后记得加：
	b:尽量少用while-loop, 大部分时候for-loop 是更好的选择。
	c:重复检查你的while语句，确定你测试的布尔表达式最终会变成
	  False.
	d:如果不确定，就在while-loop的结尾打印出你要测试的值，看看它
	  的变化。
as-#
elif-#有这样的组合：
	if ……：
		……

	elif ……：
		……

	elif ……：
		……

	else:
		……
global-#如果你想要为一个定义在函数外的变量赋值，那么你就得告诉python这个变量名不是局部的，而是全局的global语句用于声明x是一个全局变量 – 因此我们在函数内为x赋值后变化也会反映在主块中对x的使用中。你也可以使用一个global语句指定多个全局变量，比如global x, y, z
or-#或
with-#
assert-#assert是用来检查一个条件，如果它为真，就不做任何事。如果它为假，则会抛出AssertError并且包含错误信息
else-#同 14
if-#同14
pass-#
yield-#要把fib函数变成generator，只需要把print(b)改为yield b就可以.如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator.generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
break-#Python中的中断语句终止当前循环并在下一个语句中恢复执行，就像在C中发现的传统中断一样，中断最常用的方法是触发一些外部条件，要求从一个循环中匆忙退出。中断语句可以同时使用，也可以用于循环。
except-#http://www.tutorialspoint.com/python/python_exceptions.htm

import-#from sys import argv
print-#打印
class-#用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
exec-#执行存储在字符串或文件中的python语句。
in-#Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false ;我记得的用法：if A in B：
raise-#Python 使用 raise 语句抛出一个指定的异常.raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
continue-#Python continue 语句跳出本次循环，而break跳出整个循环。continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环;continue语句用在while和for循环中。
finally-#不管是否出现异常，最后都会执行finally的语句块内容，用于清理工作所以，你可以在 finally 语句中关闭文件，这样就确保了文件能正常关闭
is-#Python中的对象包含三要素：id、type、value。其中id用来唯一标识一个对象，type标识对象的类型，value是对象的值。is判断的是a对象是否就是b对象，是通过id来判断的。==判断的是a对象的值是否和b对象的值相等，是通过value来判断的
return-#返回一个值.python 函数返回值 return，函数中一定要有return返回值才是完整的函数。如果你没有python 定义函数返回值，那么会得到一个结果是None对象，而None表示没有任何值。
def-#定义函数
for--for-#loop(for循环)
lambda-#python 使用 lambda 表达式来创建匿名函数.lambda只是一个表达式，函数体比def简单很多;lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去;lambda函数拥有自己的名字空间，且不能访问自有参数列表之外或全局名字空间里的参数;虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
try-#ython的try语句有两种风格----一：种是处理异常（try/except/else）二：种是无论是否发生异常都将执行最后的代码（try/finally）
eval-#用来计算存储在字符串中的有效Python表达式
