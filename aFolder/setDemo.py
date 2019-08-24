#! Write a Python program to display the first and last colors from the following list.
#! color_list = ["Red", "Green", "Blue", "Pink" ,"White" ,"Black"]

# We use set to do the work.

def firstAndLast() :
    color_list = ["Red", "Green", "Blue", "Pink" ,"White" ,"Black"]

    super_set = set(color_list) # convert the list into set

    sub_set = set(color_list[1:-1]) # Take all the elements between index 1 and index -1; element at Index -1 is excluded

    print(list(super_set - sub_set)) # The difference between two sets is the resulting set

firstAndLast()

