#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    newdict = {}
    #starting with an empty dictionary
    key_index = 0
    #starting index number to determine location in list
    while key_index != len(keys):
        newdict[keys[key_index]] = values[key_index]
        key_index = key_index + 1
        #while index number has not reached the maximum
        #number of list items, the segment will keep
        #looping and add each item to the empty dictionary
    return newdict

def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below
    dictset1 = set(dict1.values())
    dictset2 = set(dict2.values())
    samesetvalues = dictset1 & dictset2
    return samesetvalues

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)