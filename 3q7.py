dkeys=[]
n=int(input("enter the number of elements in the key:"))
for i in range(0,n):
	elements=(input())
	dkeys.append(elements)
dvalues=[]
n=int(input("enter the elements in the value:"))
for i in range(0,n):
	elements=(input())
	dvalues.append(elements)
print("the key list is:",dkeys)
print("the value list is:",dvalues)

d={}
for key in dkeys:
	for value in dvalues:
		d[key]=value
		#dvalues.remove(value)
print("dictionary is",d)