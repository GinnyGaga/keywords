try:
	fh=open("mytest","w")	
	fh.write("this is my test file for exception handling!!")
finally:
	print("Error:can\'t find file or read data.")
