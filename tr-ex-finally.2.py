def test2():
	i=0
	try:
		i+=1
		print('i in try: %s' % i)		
		raise Exception('hehe')#有异常转到except
	except Exception:
		i+=1
		print("i in except: %s" % i)
		return i #遇到return，锁定return的值，然后跳转到finally中
	finally:
		i+=1
		print('i in finally: %s' % i) #执行完，返回原return点，将之前锁定的值返回。

print('test3Return: %s' % test2())


#在except和try中遇到return时，会锁定return的值，然后跳转到finally中，如果finally中没有return语句，则finally执行完毕之后仍返回原return点，将之前锁定的值返回(即finally中的动作不影响返回值)，如果finally中有return语句，则执行finally中的return语句


