'''
linear search approach 

iterate the list search pos
if pos number find print pos 
else print deafult num -1 

time complexity should O(n)

'''
# Best way of doing linear Search
"""
Using enumerate() (Best Pythonic Way)
Approach

Loop through array with (index, value) pairs automatically.


Why good?

No indexing manually

Clean and Pythonic
""" 
def search_enum(arr, target):
    for idx, value in enumerate(arr):
        if value == target:
            return idx + 1
    return -1


# chnage this from while loop to for loop 
def Search(arr, target):
    i, arr_len = 0, len(arr)
    while i < arr_len:
        if arr[i] == target:
            return i + 1 
        i = i + 1
    return -1

print(Search([1,3,4,6,5], 3))

# Linear Search using the for loop 
def Search_for(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1 
    return -1  

print(Search_for([1,3,4,5,2,7], 3))

# time complexity for both is O(n)
# space complexity both for O(1)

''''
Approach

Create an iterator of matching indexes → return first using next().

Why cool?

One-line

Still O(n)

Uses Python's iterator laziness (stops early)
'''
def search_next(arr, target):
    return next((i + 1 for i, v in enumerate(arr) if v == target), -1)

print(search_next([3,5,6,4,"er"], 3))