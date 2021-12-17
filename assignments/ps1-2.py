# Problem Set 1
# Problem 2
# Nicole Wakeman
# Time: 12:34 2021-12-15
#
# Write a program that computes and prints the nth prime number.

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
# when count equals n  return the value of integer
def list_n_primes(n):
	integer = 1
	count = 0
	primes = []
	#n =int(input("enter an integer, n, and the nth prime will be printed"))
	while count < n:
		integer += 1
		if is_prime(integer):
			count += 1
			primes.append(integer)
	#print(primes)
	return primes
n = int(input("enter n for n primes: "))
primes = list_n_primes(n)

#This function takes a list as an argument and prints the sum of the natural
#logs of the elements, the length of the list, and the ratio of the two
from math import *
def answers(primes):
	sum = 0
	for x in primes:
		sum += log(x)
	l = len(primes)
	print(sum)
	print(l)
	print(l/sum)
answers(primes)
