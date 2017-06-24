def sumFunction(*args):
	result=0

	for x in args:
		result += x
	return result

sumFunction(3,4,5,6,8,9)

def someFunction(**kwargs):
	if 'text' in kwargs:
		print (kwargs['text'])
someFunction(text="foo")
