#:不管是否出现异常，最后都会执行finally的语句块内容，用于清理工作所以，你可以在 finally 语句中关闭文件，这样就确保了文件能正常关闭

try:
	x=int(input('input x:'))
	y=int(input('input y:'))
	print('x/y=',x/y)
except ZeroDivisionError: #捕捉除0异常
	print("ZeroDivision")
except(TypeError,ValueError) as e: #捕捉多个异常
	print(e)
except:#捕捉其余类型异常
	print('it still wrong')
else:#没有异常时执行
	print('it work well')
finally: #不管是否有异常都会执行
	print('Cleaning up')
