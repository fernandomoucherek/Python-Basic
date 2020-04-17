print('Hello')

# In order to  store values, we use variables

# None: This represents  the absence of value.
# Numbers: 
			# Integer
			# Floating
			# Complex

#Sequences:
			# String
			# Tuples
			# Lists

# Arithmetic operators
# + add
# - subtraction
# * multiply
# / division

#Exemple - 1

# 2 + 3 
print(2 + 3)

# 2 - 3 
print(2 - 3)

# 2*3
print(2*3)

#2/3
print(2/3)
print(2./3.)
print(type(2./3.))

# 1 + 2 * 3
print(1 + 2 * 3)
print(type(1 + 2 * 3))

# (1 + 2) * 3
print((1 + 2) * 3)

#Assignment operators
# = 
# +=
# -=
# *=
# /=
# %=
# **=

# Strings
# A predefinied object which contais characters

name = 'Harsh'
print (name)

print (type(name))

print (name[0])
print (name[-2])

print (len(name))

print(name[len(name)-2])

name1 = name[1:]
name2 = name[2:]
print(name1)
print(name2)

# List
author = ['Joao','Maria','Pedro']
print (author)
print(type(author))

print (author[1])

# Tuples
tup = (3,4)

print(tup)
print(type(tup))

(a,b) = tup

print("The first element is",a)
