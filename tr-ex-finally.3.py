def test4():
	i=0
	try:
		i+=1
		return i
	
	finally:
		i +=1
		print('i in finally: %s'% i)
print('test4Return: %s' % test4())
