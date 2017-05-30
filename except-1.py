#This example opens a file, writes content in the, file and comes out gracefully because there is no problem at all.

#the file-mytest has write permission,so it wont raise a  exception. 


#!/usr/bin/python
try:
	fh=open("mytest","w")
	fh.write("this is mytest file for exception handling!!")
except IOError:
	print("Erro:can\'t find file or read data")
else:
	print("written content in the file successfully")
	fh.close()
