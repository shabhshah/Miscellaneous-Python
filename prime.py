#imports
import time
import sys

#input number
user_number_input = abs(input("enter number to determine if prime or not: "))
time.sleep(1)
print "calculating"
time.sleep(1)

#even, 1 or 2
if user_number_input == 1 or user_number_input == 2 or user_number_input % 2 ==0:
	print "not a prime"
	sys.exit()

#rest of prime
n = 3
while True:
	if user_number_input % n == 0:
		print "not a prime"
		break
	if n == user_number_input:
		print "it's a prime!"
		break
	n += 1
	print n
