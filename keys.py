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
class-
exec-#执行存储在字符串或文件中的python语句。
in-我记得的用法：if A in B：
raise-
continue-
finally-
is-
return-返回一个值
def-定义函数
for--for-loop(for循环)
lambda-
try-
eval-#用来计算存储在字符串中的有效Python表达式
