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


import json
import re


# Function to read a file
# filepath: full path to the file
#
# Returns: a string containing file contents
def read_file(filepath):
    # [YOUR CODE HERE]
    fd = open(filepath)
    temp = fd.read()
    fd.close()
    return temp


# Function to convert a string to a list of lowercase words
# in_str: a string containing the text
#
# Returns: a list containing lowercase words
def convert_to_words(in_str):
    # [YOUR CODE HERE]

    alist = in_str.lower().split()
    #in_str = in_str.lower()
    #alist = re.split(r'[/, ;\n]+', in_str)
    return alist


# Function to count the words
# words: a list containing words
#
# Returns: a dictionary where keys are words and corresponding values are counts
def get_wc(words):
    word_counts = dict()
    # [YOUR CODE HERE]
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


# Function to store the dictionary as JSON
# dictionary: a python dictionary
# out_filepath: path to output file to store the JSON data
#
# Returns: a dictionary where keys are words and corresponding values are counts
def to_json(dictionary, out_filepath):
    # [YOUR CODE HERE]
    fd = open(out_filepath, 'w')
    json.dump(dictionary, fd)
    fd.close()
    return None




# Use this main function to test your code. Sample code is provided to assist with the assignment,
# feel free to change/remove it. If you want, you may run the code from terminal as:
# python text_analysis.py
# It should produce the following output (with correct solution):
#       $ python text_analysis.py
#       File loaded: THE ADVENTURES OF SHERLOCK HOL...
#       Words: ['the', 'adventures', 'of', 'sherlock', 'holmes']
#       The word sherlock appeared 96 times

def main():
    # read the entire file in a string
    content = read_file('adventure_sh.txt') #changed
 
    print(f'File loaded: {content[:30]}...')

    # Obtain words from the content
    words = convert_to_words(content)
    # Print the first 5 words
    print(f'Words: {words[:5]}')
    #print(f'Words: {words}')

    word_counts = get_wc(words)
    # Print word counts for alice
    word = 'sherlock'
    if word in word_counts:
        print(f'The word {word} appeared {word_counts[word]} times')
    else:
        print("Word not found")

    temp = 0
    sorted_dict = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse = True))
    for key, value in list(sorted_dict.items())[:100]:
        print(f'{key}: {value}')


    # Save these counts as a JSON file
    to_json(word_counts, 'temp.json') #changed








################ Do not make any changes below this line ################
if __name__ == '__main__':
    main()

