#the file(mytest-1) has permission to open the file in writing mode,so it can be excuted. 
try:
	fh=open("mytest-1","w")	
	try:
		fh.write("this is my test file for exception handling!!")
	finally:
		print("going to close the file")
		fh.close()		
except IOError:

	print("Error:can\'t find file or read data.")
