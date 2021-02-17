def bubblesort(l):
	for i in range(len(l)-1,0,-1):
		for j in range(i):
			if l[j]>l[j+1]:
				temp=l[j]
				l[j]=l[j+1]
				l[j+1]=temp
			
				
l=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
	elements=int(input())
	l.append(elements)
print(l)
bubblesort(l)
print("sorted array: ",l)