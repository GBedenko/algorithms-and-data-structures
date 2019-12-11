'''Binary Search. so that instead of outputting whether a specific
   value was found, it outputs whether a value within a range was found'''


def binary_search(list_input, search_value):
    '''Recursive function that searches through a list for a value
       Returns a boolean for whether the value is present in the list

       If the length of the list is zero, return false
       Otherwise, take the middle value of the list and compare it to the search value
       - If the middle value is the search value, then return true
       - If there is now only one element in the list and the middle value isn't the
         search value then return false
       - If the middle value is bigger than the search value, call the function again for
         the rest of the list up to this value's position
       - If the middle value is smaller than the search value, call the function again for
         the rest of the list from this value's position'''

    # Middle point is the value half of the length of the list
    # The value at the middle index is what is compared against
    middle_point = int(round(len(list_input) / 2))

    # If the length of the list is zero, return false
    if len(list_input) == 0:
        return False

    # If the index's value is equal to the search value, then the value is in the list, return true
    elif list_input[middle_point] == search_value:
        return True

    # If the index's value is not equal to the search value and there is only one element in the list, then return false
    elif list_input[middle_point] != search_value and len(list_input) == 1:
        return False

    # If the index's value is bigger than the search value, then search the rest of the list up to this index's position
    elif list_input[middle_point] > search_value:
        return binary_search(list_input[:middle_point], search_value)

    # If the index's value is lower than the search value, then search the rest of the list up from one after this
    # index's position
    elif list_input[middle_point] < search_value:
        return binary_search(list_input[middle_point + 1:], search_value)


if __name__ == "__main__":

    sorted_list = [1,2,4,8,16,32,64,128]
    print("List is: " + str(sorted_list))

    search_value = int(input("Enter search value:"))

    print(binary_search(sorted_list, search_value))
