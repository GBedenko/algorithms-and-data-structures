'''Returns the highest square number which is
   less than or equal to a positive integer'''

from math import floor, sqrt


def highest_square_number(n):

    return floor(sqrt(n))**2


if __name__ == "__main__":

    n = int(input("Enter a number:"))

    print(highest_square_number(n))
