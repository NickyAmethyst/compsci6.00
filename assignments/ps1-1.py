# Problem Set 1
# Problem 1
# Nicole Wakeman
# Time: 12:34 2021-12-15
#
# Write a program that computes and prints the 1000th prime number.

# First create a function that checks if a given an input value is prime.

def is_prime(x):
	potential_factors = range(2,x)
	prime = True
	for n in potential_factors:
		if x%n == 0:
			prime = False
			return False
	return True

# itterate through the integers by +1  starting at at 1
# increase count by 1 each time is_prime(integer) returns True
# when count equals 1000 return the value of integer
integer = 1
count = 0
while count < 1000:
	integer += 1
	if is_prime(integer):
		count += 1
print(integer)
