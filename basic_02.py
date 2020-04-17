'''
Functions

functions are pre-written codes that perform a certain task

def FuncName (parameters):
	code detailing what the function should do
	return [expression]

'''
def product (num1,num2):
	prod = num1*num2
	print ('The product => ' + str(prod))
	return prod 

#product(120,987)

def fib(n):
	if n == 1:
		return 1 
	elif n == 2:
		return 2
	else :
		F = fib(n -1) + fib(n - 2)
		return F 
	return F

def fact(n):
	if n == 0:
		return 1
	else:
		F = n*fact(n - 1)
		return F

	return F


ans = fact(9)
print (ans)


def prime (number):
	for x in range (2,number):
		D = number % x
		if ( D == 0):
			return False
	return True

