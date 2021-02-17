def divgen(n):
	for i in range(1,n+1):
		if i%5==0 or i%7==0:
			yield i
a=int(input("enter the input:"))
for i in divgen(a):
	print(i,end=" ")