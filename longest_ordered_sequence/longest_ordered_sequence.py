'''Given a sequence of n integers, extract the sub-sequence of longest
   length which is in ascending order'''


def split_into_subsequences(sequence):
    '''Recursive function that takes an sequence as input and returns a list of lists
       Splits the sequence into subsequences where each one is in ascending order
       - If the sequence length is zero, return an empty list
       - For the first element of the list, add it to the sub sequence list
       - If the next element is bigger than or equal to the previous one, add it to the sub sequence
       - If the next element is smaller than the previous one, save the current sub sequence and
         run the function again for the remaining list
       Returns a list of sub sequence list, i.e. the original list split up into a
       list of smaller lists'''

    sub_sequences = []

    current_subsequence = []

    if len(sequence) == 0:
        return []

    i = 0
    while True:

        # If it is the last element and it should be added to current subsequence
        if i == len(sequence) - 1 and sequence[i] >= sequence[i - 1]:

            current_subsequence.append(sequence[i])

            sub_sequences.append(current_subsequence)

            return sub_sequences

        # If first element add it to list
        if i == 0:

            current_subsequence.append(sequence[i])
            i += 1

        # If element is bigger than previous element, add it to list
        elif sequence[i] >= sequence[i - 1]:

            current_subsequence.append(sequence[i])
            i += 1

        # If element is smaller than previous one, it's the end of a subsequence
        elif sequence[i] < sequence[i - 1]:

            sub_sequences.append(current_subsequence)

            # Call the function for the rest of the list
            return sub_sequences + split_into_subsequences(sequence[i:])


def compare_subsequences(subsequences):
    '''Function that takes a list of lists as input and returns which
       one of them is the longest
       - If it is the first list it is looking at, then this automatically
         becomes the longest list for comparisons
       - If the list it is looking at is longer than the current longest, then
         it becomes the new longest list
       Once iterated over all the lists, returns which one was longest'''

    for i in range(0, len(subsequences)):

        # First list is set as longest to be used for comparison
        if i == 0:
            longest_subsequence = subsequences[i]

        # If a subsequence is longer than the current one, replace current
        elif len(subsequences[i]) > len(longest_subsequence):
            longest_subsequence = subsequences[i]

    return longest_subsequence


if __name__ == "__main__":

    sequence = [1,2,3,1,2,3,4,5,6,7,1,2,3,4,5,1,2,3,4,5,6]

    subsequences = split_into_subsequences(sequence)

    longest_subsequence = compare_subsequences(subsequences)

    print("The longest subsequence from this list is: " + str(longest_subsequence))
