import time
import sys
import random

def selection_sort(int_list):
    for i in range(len(int_list)):
        min = i
        for j in range(i + 1, len(int_list)):
            if int_list[min] > int_list[j]:
                min = j
        curr = int_list[i]
        int_list[i] = int_list[min]
        int_list[min] = curr


def insertion_sort(int_list):
    for i in range(1, len(int_list)):
        curr = int_list[i]
        pos = i
        while pos > 0 and int_list[pos - 1] > curr:
            int_list[pos] = int_list[pos - 1]
            pos -= 1
        int_list[pos] = curr
        

def merge_sort(int_list):
    if len(int_list) > 1:
        mid = len(int_list) // 2
        left = int_list[:mid]
        right = int_list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              int_list[k] = left[i]
              i += 1
            else:
                int_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            int_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            int_list[k] = right[j]
            j += 1
            k += 1


def selection_time(list1):
    init_time = time.time()
    selection_sort(list1)
    end_time = time.time()
    time1 = (end_time - init_time) * 1000
    print(round(time1, 2), end="")
    

def insertion_time(list2):
    init_time = time.time()
    insertion_sort(list2)
    end_time = time.time()
    time2 = (end_time - init_time) * 1000
    print(round(time2, 2), end="")


def merge_time(list3):
    init_time = time.time()
    merge_sort(list3)
    end_time = time.time()
    time3 = (end_time - init_time) * 1000
    print(round(time3, 2), end="")


# function to format output
def print_list(int_list):
    x = len(int_list)
    for i in range(len(int_list)-1):
        print(int_list[i], end = ", ")
    print(int_list[x - 1])
    

file = open(sys.argv[1], "r")
contents = file.readlines()
list1 = contents[0].split(",")
for i in range(0, len(list1)):
    list1[i] = int(list1[i])
list2 = list1.copy()
list3 = list1.copy()

print("Selection Sort (", end="")
selection_time(list1)
print(" ms): ", end="")
print_list(list1)

print("Insertion Sort (", end="")
insertion_time(list2)
print(" ms): ", end="")
print_list(list2)

print("Merge Sort (", end="")
merge_time(list3)
print(" ms): ", end="")
print_list(list3)
