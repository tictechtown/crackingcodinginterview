# TODO
'''
Given an M x N matrix in which each row and each column is sorted in ascending order, 
write a method to find an element.

'''


def find_element(matrix:list[list[int]], target:int) -> tuple[int,int] | None:


    origin = (0,0)
    destination = (len(matrix), len(matrix[0]))

    return _find_element(matrix, target, origin, destination)

def _find_element(matrix:list[list[int]], target:int, origin:int, destination:int) -> tuple[int,int] | None:

    if origin > destination:
        return None


    # binary search on the diagonal (sorted)
    # gives us left and right where a[l] < target < a[r]
    # search again in those 2 subquadrant --> bottom-left and top-right

    left, right = binary_search_diagonal(matrix, origin, destination, target)

    if left == right:
        return left
    
    bottom_left_origin = (origin[0], right[1])
    bottom_left_destination =  (left[0], destination[1])
    top_right_origin = (right[0], origin[1])
    top_right_destination =  (destination[0], left[1])
    return _find_element(matrix, target, bottom_left_origin, bottom_left_destination) or _find_element(matrix, target, top_right_origin, top_right_destination)


def binary_search_diagonal(matrix, origin, destination, target):

    left = origin
    right = destination
    while left < right:

        middle = (left + right) // 2
        value = matrix[middle[0]][middle[1]]
        if target < value:
            right = (middle[0]-1, middle[1]-1)
        else:
            left = (middle[1]+1, middle[1]+1)
    
    return (left, right)