# Python program to find number of
# local variables in a function

def check1():
	pass

def fun2():
	a, b, c = 1, 2.25, 333
	str = 'GeeksForGeeks'

print("Number of local variable in check 1 fun: ",check1.__code__.co_nlocals)
print("Number of local variable in fun2 fun:",fun2.__code__.co_nlocals)
