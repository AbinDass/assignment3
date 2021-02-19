def make_pretty(func):
	def inner():
		print("i got decorated")
		func()
	return inner
def ordinary():
	print("i am ordinary")
	ordinary()

def abc(func):
	def inner():
		print("i dont know")
		func()
	return inner
@make_pretty
@abc
def ordinary():
	print("i am ordinary")
ordinary()			