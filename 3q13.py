def insertion(l):
	for i in range(0,len(l)):
		a=l[i]
		j=i-1
		while j>=0 and a<l[j]:
			l[j+1]=l[j]
			j-=1 
		l[j+1]=a			
		pass

l=[]
n=int(input("enter the number of elements in the index:"))
for i in range(0,n):
	elements=int(input())
	l.append(elements)
print(l)
insertion(l)
print("the sorted array is :")
for i in range(len(l)):
	print(l[i])