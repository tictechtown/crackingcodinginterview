'''
Sorted Search, No Size: 

You are given an array-like data structure Listy which lacks a size method. 
It does, however, have an elementAt(i) method that returns the element at index i in 0( 1) time. 
If i is beyond the bounds of the data structure, it returns -1. 
(For this reason, the data structure only supports positive integers.) 
Given a Listy which contains sorted, positive integers, 
find the index at which an element x occurs. If x occurs multiple times, you may return any index.
'''

class Listy:

    def __init__(self, value:list[int]):
        self.value = sorted(value)

    def elementAt(self, position:int) -> int:
        if position >= len(self.value):
            return -1
        return self.value[position]
    

def sorted_search(input:Listy, target:int) -> int:

    suggested_left = 0
    suggested_right = 1
    while input.elementAt(suggested_right) != -1:
        value = input.elementAt(suggested_right)
        if value == target:
            return target
        if value > target:
            suggested_left = suggested_right
            suggested_right *= 2
        else:
            # target is between [suggested_left, suggested_right]
            break

        while suggested_left <= suggested_right:
            middle = (suggested_left + suggested_right) // 2
            value = input.elementAt[middle]
            if value == target:
                return middle
            
            if value == -1:
                suggested_right = middle - 1
            elif value < target:
                suggested_left = middle + 1
            else:
                suggested_right = middle -1 
            