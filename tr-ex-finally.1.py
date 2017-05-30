def test1():
	try:
		print('to do stuff')#先执行
		print('to return in try')
		return 'try'#在try中遇到return时，也会立即强制转到finally中执行。
	except Exception:#try没有抛出异常，故except不执行
		print('process except')
		print('to return in except')
		return 'except' 
	finally:
		print('to return in finally')
		return 'finnaly'#在finally中遇到return 就返回

test1Return=test1()
print('test1Return:'+ test1Return)#这是啥？？？

#tr-ex-finally.py和tr-ex-finally.1.py得到的结论：

#无论是在try还是在except中，遇到return时，只要设定了finally语句，就会中断当前的return语句，跳转到finally中执行，如果finally中遇到return语句，就直接返回，不再跳转回try/excpet中被中断的return语句
