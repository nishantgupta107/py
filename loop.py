#!/usr/local/bin/python3.4

a , b= 0, 1

c = int(input("Enter the limit of series: "))	#asking user for loop length

while (b<c):	#loop for fibonacci
	print (b, end=", ")
	a , b = b, b+a

print ("\nLoop end number {} reached!".format(c))
