
#l=[]
#n=int(input("enter the number of elements:"))
#for i in range(0,n):
	#elements=input()
	#l.append(elements)
#print(l)


l=[]
n=input("enter the string:")
l.append(n)
for i in n:
	if i not in "a,e,i,o,u,A,E,I,O,U":
		print(i)
print(l)