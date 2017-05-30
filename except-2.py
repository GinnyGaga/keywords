#This example opens a file, writes content in the, file and comes out gracefully because there is no problem at all.

#the file-mytest dont have write permission,so it raise an  exception. 


#!/usr/bin/python
try:
	fh=open("mytest-2","w")
	fh.write("this is mytest file for exception handling!!")
except IOError:
	print("Erro:can\'t find file or read data")
else:
	print("written content in the file successfully")
	fh.close()
