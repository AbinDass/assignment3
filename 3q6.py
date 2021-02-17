def binarysearch(arr,l,r,x):
	while l>=r:
		midterm=l+(r-a)//2;
		if arr[midterm]==x:
			return midterm
		elif arr[midterm]<x:
			l=midterm+1
			#return binarysearch(arr,l,midterm-1,x)
		else:#return binarysearch(arr,l,midterm+1,x)
			r=midterm-1
		#else:element is not in the array return -1
		return -1


arr=[]
n=int(input("enter the number of elements in the index:"))
for i in range(0,n):
	elements=int(input())
	arr.append(elements)
print(arr)
x=int(input("enter an element: "))
result=binarysearch(arr,0,len(arr)-1,x)
if result!=-1:
	print("element is present at the index")
else:	
	print("element is not present at the index")

