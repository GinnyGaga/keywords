def test5():

	for i in range(5):
		try:
			print('do stuff %s' % i)
			raise Exception(i)
		except Exception:
			print('exception %s' % i) 
			continue
		finally:
			print('do finally %s' % i)

test5()
#在一个循环中，最终要跳出循环之前，会先转到finally执行，执行完毕之后才开始下一轮循环
