"""FizzBuzz. Print out the values from 1 up to N.
   If N is divisible by 3, print Fizz
   If N is divisible by 5, print Buzz
   If N is divisible by 3 and 5, print FizzBuzz"""


def fizz_buzz(n):
    
    for i in range(1, n+1):

        output = ""

        if i % 3 == 0:
            output += "Fizz"

        if i % 5 == 0:
            output += "Buzz"

        print(str(i)) if output == "" else print(output)


if __name__ == "__main__":

    n = int(input("Enter n:"))

    fizz_buzz(n)
