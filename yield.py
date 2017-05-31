#斐波拉契数列用列表生成式:著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

#1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fab(max):#定义函数名、形参
	n,a,b=0,0,1 #定义实参，类似：n=0;a=0;b=1
	while  n<max:	#
		yield b
	#	print (b)
		a,b=b,a+b #相当于：t=(b,a+b),a=t[0],b=t[1],其中,t是一个tuple,元组.a=b,b=a+b
		n=n+1
for n in fab(5):#打印数列
	print(n)
	
