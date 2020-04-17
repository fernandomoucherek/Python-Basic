# Conditional Statements

# if - elif - else

'''
# if 

if <test condition>:
	<block if test is true>


# if - else 

if <test condition>:
	<block if test is true>
else:
	<block if test is not true>

# if - else (ladder)

if <test condition>:
	<block if test condition is true>
elif: <test condition 1>:
	<block 1>
elif: <test condition 2>:
	<block 2>
else:
	<block if test condition is true>
'''

# LOOP (for - while)

# for
# for a in (string,list,tuple)

# Exemple
Pets = ['cats', 'dogs','rabbits','hamsters']

for mypets in Pets:
	print(mypets)

for index, mypets in enumerate (Pets):
	print(index,mypets)

for i in range (6):
	print (i) 

# while
# while a ondition is true:
#	do A

count = 5
while count > 0:
	print("Counter =", count)
	count = count - 2

# Break
j = 0
for i in range(12):
 	j += 1
 	print ('i = ' + str(i) + ' => j = ' +str(j) )
 	if  j == 6:
 		break

 # Continue
k = 0
for i in range(12):
 	k += 6
 	print ('i = ' + str(i) + ' => k = ' +str(k) )
 	if  k == 6:
 		continue

# Try, Except

'''
try:
	do something
except:
	do something else when a error occurs

'''

try:
	ans = 12/0
	print(ans)
except:
	print ("An error occurred")