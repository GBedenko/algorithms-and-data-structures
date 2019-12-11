'''Recursive function that reverses the words in a sentence'''


def reverse_sentence(sentence):
    '''Function that takes a string as input
       If the length of the string is empty, return an empty string
       Else, check the string until there is a space, take these characters
       and add them to a word.
       Call the function again for the remaining string and keep adding the
       substrings to the word when there is a space.
       Returns the new words which will be in reverse order'''

    if len(sentence) == 0:
        # If string is empty, return an empty string
        return ""

    else:

        i = 0
        word = ""

        while i < len(sentence) and sentence[i] != " ":
        # If it is before the end of the string, and the character is not a space

            # Add the character to the word
            word += sentence[i]

            # Increment i to go to the next character
            i += 1

        # Once out of the loop it is either the end of the string or reached
        # a space. Call the function for the rest of the string and add it to the word
        if i == len(sentence):
            
            output = reverse_sentence(sentence[i + 1:]) + word

        else:

            output = reverse_sentence(sentence[i + 1:]) + " " + word
    
        return output


if __name__ == "__main__":

    s = input("Enter a sentence: ")

    reversed_sentence = reverse_sentence(s)

    print(reversed_sentence)
