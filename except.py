#抛出异常:raise语句
def division(x,y):
	if y==0:
		raise ZeroDivisionError('The zero is not allow')
	return x/y
	
try:
	division(1,0)
except ZeroDivisionError as e:		
	print(e)


