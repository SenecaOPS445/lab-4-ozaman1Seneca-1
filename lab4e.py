#!/usr/bin/env python3
# Author ID: ozaman1

def is_digits(sobj):
    # place code here - loop through each character in sobj 
    return sobj.isdigit()
    #isdigit() is a built-in method that checks if
    #all characters in a text string are digits
    
if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')