terms=int(input("entern the number of terms:"))
result=list(map(lambda x: x**2,range(terms)))
#print("the total terms are",terms)
for i in range(terms):
	print("power of ",i, "is",result[i])
