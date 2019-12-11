'''Modified Binary Search algorithm so that instead of outputting whether a specific
   value was found, it outputs whether a value within a range was found'''


def range_binary_search(list_input, low_value, high_value):
    '''Recursive function that searches through a list for a range of values
       Returns a boolean for whether the list contains a value within the range

       If the length of the list is zero, return false
       Otherwise, take the middle value of the list and compare it to the high and low
       values of the input range
       - If the middle value is inbetween the low and high values, then return true
       - If there is now only one element in the list and the middle value isn't in the
         range then return false
       - If the middle value is bigger than the high value, call the function again for
         the rest of the list up to this value's position
       - If the middle value is smaller than the low value, call the function again for
         the rest of the list from this value's position'''

    # Middle point is the value half of the length of the list
    # The value at the middle index is what is compared against
    middle_point = int(round(len(list_input) / 2))

    # If the length of the list is zero, return false
    if len(list_input) == 0:
        return False

    # If the index's value is bigger than the low point and smaller than the high point, then the value is in the range
    elif list_input[middle_point] >= low_value and list_input[middle_point] <= high_value:
        return True

    # If the index's value is bigger than the high value or smaller than the low value and there is only one
    # element in the list, then return false
    elif ((list_input[middle_point] > high_value) or (list_input[middle_point] < low_value)) and len(list_input) == 1:
        return False

    # If the index's value is bigger than the high value, then search the rest of the list up to this index's position
    elif list_input[middle_point] > high_value:
        return range_binary_search(list_input[:middle_point], low_value, high_value)

    # If the index's value is lower than the low value, then search the rest of the list up from one after this
    # index's position
    elif list_input[middle_point] < low_value:
        return range_binary_search(list_input[middle_point + 1:], low_value, high_value)


if __name__ == "__main__":

    sorted_list = [1,2,4,8,16,32,64,128]
    print("List is: " + str(sorted_list))

    lower_bound = int(input("Enter value for lower bound:"))
    upper_bound = int(input("Enter value for upper bound:"))

    if lower_bound > upper_bound:
        raise ValueError("Lower bound needs to be less than or equal to the upper bound.")

    print(range_binary_search(sorted_list, lower_bound, upper_bound))
