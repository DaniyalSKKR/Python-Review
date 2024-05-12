# CS421: Natural Language Processing
# University of Illinois at Chicago
# Spring 2024
# Assignment 1
#
# Do not rename/delete any functions or global variables provided in this template and write your solution
# in the specified sections. Use the main function to test your code when running it from a terminal.
# Avoid writing that code in the global scope; however, you should write additional functions/classes
# as needed in the global scope. These templates may also contain important information and/or examples
# in comments so please read them carefully. If you want to use external packages (not specified in
# the assignment) then you need prior approval from course staff.
# This part of the assignment will be graded automatically using Gradescope.
# =========================================================================================================


# Function to decrease every element of input list by n 
# num_list: a list containing numerical values
#
#Returns: a list containing the updated values
def list_minus(num_list, n):
    # [YOUR CODE HERE]
    newList = []
    print(num_list)
    for i in num_list:
        i -= n
        newList.append(i)
    return newList
# def list_minus(num_list, n):
#     # [YOUR CODE HERE]
#     newList = [i-=n for i in num_list]
#
#     return num_list


# Function to process the list by decreasing every element by n and then raised to the third power
# You must use list_minus function
# num_list: a list containing numerical values
#
# Returns: a list containing the processed values
def process_list(num_list, n):
    # [YOUR CODE HERE]
    newList = list_minus(num_list, n)
    newList2 = []
    for i in newList:
        newList2.append(i**3)
    return newList2





# Use this main function to test your code. Sample code is provided to assist with the assignment,
# feel free to change/remove it. If you want, you may run the code from terminal as:
# python lists.py
# It should produce the following output (with correct solution):
#       $ python lists.py
#       The decreased list is: [-3, -2, 1]
#       The processed list is: [-27, -8, 1]

def main():
    # Calculate and print the decreased list
    decreased_list = list_minus([2, 3, 6], 5) 
    print(f'The decreased list is: {decreased_list}')

    # Process the list
    proc_list = process_list([2, 3, 6], 5)
    print(f'The processed list is: {proc_list}')



################ Do not make any changes below this line ################
if __name__ == '__main__':
    main()

