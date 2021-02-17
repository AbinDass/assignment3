def fibinocci(n):
	if n<=1:
		return n
	else:
		return(fibinocci(n-1)+fibinocci(n-2))

terms=int(input("enter the terms:"))
if terms<=0:
	print("enter a +ve intiger:")
else:
	print("fibinocci sequence" )
	for i in range(terms):
		print(fibinocci(i))