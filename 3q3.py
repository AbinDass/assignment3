str1=input("enter string: ")
vow=['a','e','i','o','u','A','E','I','O','U']
def vowremv(str2):
	st=' '
	vowremvd=[i for i in str2 if i not in vow]
	for i in vowremvd:
		st+=i
	return st
print(list(vowremv(str1)))