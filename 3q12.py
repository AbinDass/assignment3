def divgen(n):
	for i in range(0,n+1):
		if i%2==0: 
			yield i
a=int(input("enter how many elements:"))
print("the even numbers of the range is:")
for i in divgen(a):
	print(i,end=" ")
