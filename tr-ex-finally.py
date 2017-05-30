def test1():
	try:
		print('to do stuff')#先执行
		raise Exception('hehe')#发生异常 立刻转入except执行
		print('to return in try')
		return 'try'
	except Exception:
		print('process except')#再执行
		print('to return in except')#再再执行
		return 'except' #遇到return，强制转到finally中执行
	finally:
		print('to return in finally')
		return 'finnaly'#在finally中遇到return 就返回

test1Return=test1()
print('test1Return:'+ test1Return)#这是啥？？？
