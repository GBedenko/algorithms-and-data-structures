'''Recursive function that removes all vowels from a given string'''


def remove_vowels(s):
    '''Function that takes a string as input
       If the string is empty, return the empty string - this is the base case
       Otherwise, if the first letter is not a vowel, add it to the word
       If the first letter is a vowel, do not add the character to the word
       Call the same function for the remaining characters in the string
       Returns the word without vowels in it'''

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]    
    
    if len(s) == 0:

        return(s)  # This is the base case. Runs when string is empty

    elif s[0] not in vowels:
        
        # If first character is not a vowel, return the character
        # and call the recursive function for the remaining string
        return s[0] + remove_vowels(s[0+1:]) 
    
    elif s[0] in vowels:
        
        # If first character is a vowel, return an empty string and calls the
        # recursive function for the remaining string
        return "" + remove_vowels(s[0+1:]) 


if __name__ == "__main__":

    s = input("Enter a string:")

    print(remove_vowels(s))
