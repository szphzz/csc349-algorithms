import sys

def solo(int_list):
    n = len(int_list)
    mid = n // 2
    if n == 1: # first base case
        return int_list[0]
    elif n == 3: # second base case
        if int_list[0] == int_list[1]:
            return int_list[2]
        else:
            return int_list[0]
    
    elif int_list[mid] != int_list[mid - 1] and int_list[mid] != int_list[mid + 1]: # if mid is solo
        return int_list[mid]
    
    elif int_list[mid] == int_list[mid - 1]: # if duplicate with element before
        if len(int_list[mid + 1:]) % 2 == 0: # and rest of list has an even length
            return solo(int_list[:mid - 1]) # recurse on beginning of list
        else:
            return solo(int_list[mid + 1:]) # otherwise recurse on end of list
    
    elif int_list[mid] == int_list[mid + 1]: # if duplicate with element after
        if len(int_list[mid + 2:]) % 2 == 1: # and rest of list has an odd length
            return solo(int_list[mid:]) # recurse on end of list
        else:
            return solo(int_list[:mid]) # otherwise recurse on beginning of list
    

file = open(sys.argv[1], "r")
int_list = file.readlines()
for i in range(0, len(int_list)):
    int_list[i] = int(int_list[i])

print(solo(int_list))
