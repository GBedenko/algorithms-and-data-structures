'''Count the number of trailing 0s in a factorial number'''

def factorial(n):
    '''Function that takes a integer n as input
       Using recursive calls it works out the factorial of the input
       Returns the factorial answer'''

    if(n > 1):
        answer = n * factorial(n-1)

    elif(n == 1):
        answer = n

    return(answer)


def count_zeroes(factorial_answer):
    '''Function that takes a number as input and counts how many zeroes it has
       Divides the input by 10, if there is no remainder then there is a zero
       Keeps doing this while there is no remainder and counts how many times it is done
       Comes out of the loop when there is a remainder
       Return the number of zeroes and prints it out'''
    
    count = 0

    # If the answer divides by 10 with no remainder, a zero is at the end
    # Repeat this while the number is divisible by 10 with no remainder
    # Else, come out of the loop, there are no more zeroes
    while(factorial_answer % 10 == 0): 
         
        count = count + 1
        factorial_answer = factorial_answer // 10   

    return(count)
    
# Take input for factorial function and get the answer
factorial_answer = factorial(int(input("Enter number:")))

# Use the factorial answer to count the number of zeroes using the count_zeroes() function
zeroes = count_zeroes(factorial_answer)

print("The number of zeroes at the end of this factorial is " + str(zeroes))
