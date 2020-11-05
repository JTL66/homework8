
##1.





##2.

from random import randrange
a = randrange(5)

fileName = input("INTEGER DIVISIONS")
total = 0
try:
	f = open(fileName)
	while(True):
		l = f.readline()
		if(not l):
			break
		total += int(l)
	f.close()
except:
	print("Error Occured")

print("The total is:", total)

