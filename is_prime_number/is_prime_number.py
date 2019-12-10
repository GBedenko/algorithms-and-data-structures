"""Recursive function to check if a number is prime"""


def is_prime_number(n, factor = 3):
	"""A recursive function that works out if a number is prime.
	
	   Takes an integer as input and a factor to divide by which can be changed
	   If the number is less 2 then it is not prime
	   If the number is 2 or 3 then it is prime
	   If the number is even then it is not prime
	   Otherwise, divide the number by the factor. If it can be divided, then the number is not prime.
	   Keeps doing this by increasing factor by 2 until half of the integer's value.
	   If it gets this far and cannot be divided then it is a prime number.
	   Returns boolean (true or false) for whether it is a prime or not"""

	if n < 2: return False

	if n == 2 or n == 3: return True # 2 and 3 are the lowest primes and used as exceptions before checks

	if n % 2 == 0: return False # Even numbers except 2 are not prime
	
	# If the factor is greater than half of n, then there will be no factor that goes
	# into n, therefore this number must be a prime
	if factor > n/2: return True  

	else:

		if(n % factor == 0):

			return False # The factor has divided into the number with no remainder, therefore it is not a prime

		else:
			# Increase the factor by 2 to keep checking odd numbers that
			# may divide into the number, and keeps checking for if it is prime
			return is_prime_number(n, factor + 2) 


if __name__ == "__main__":

	n = int(input("Enter a number:"))

	if is_prime_number(n):
		print("This number is prime")
	else:
		print("This number is not prime")
