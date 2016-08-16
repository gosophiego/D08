#!/usr/bin/env python3
# HW08_ch11_ex01
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
###############################################################################
# Imports


# Body
def store_to_dict():
    open_txt = open('words.txt')
    new_dict = {}
    n = 1
    for each_line in open_txt:
        # When I create an empty dictionary within this for loop instead,
        # each word replaces the word that was appeneded before.
        # Would you mind explaning why that is?
        new_dict[each_line.strip()] = n
        n += 1
    return new_dict


###############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    if "this" in words_dict:
        print("Yup.")
    if "qwertyuiop" in words_dict:
        print("Hmm.")

if __name__ == '__main__':
    main()
