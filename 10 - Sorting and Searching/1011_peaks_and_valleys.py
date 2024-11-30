"""
PeaksandValleys:
In an array of integers,
a "peak" is an element which is greater than or equal to the adjacent integers 
and a "valley" is an element which is less than or equal to the adjacent integers. 

For example, in the array {5, 8, 6, 2, 3, 4, 6}, 
{8, 6} are peaks and {5, 2} are valleys. 
Given an array of integers, 
sort the array into an alternating sequence of peaks and valleys.
"""

"""
[5,3,1,2,3]
-> [1,2,3,3,5]
---> [5,1,3,2,3]

"""

import unittest


def sort_peak_and_valleys(input: list[int]) -> list[int]:

    arr = sorted(input)
    valley_index = 0
    peak_index = len(arr) - 1

    output = []
    use_peak = True
    while valley_index <= peak_index:
        if use_peak:
            output.append(arr[peak_index])
            peak_index -= 1
        else:
            output.append(arr[valley_index])
            valley_index += 1
        use_peak = not use_peak

    return output


def sort_peak_valleys_opt(input:list[int]) -> list[int]:

    for i in range(1, len(input), 2):
        biggest_idx = _max_index(input, i-1, i, i+1)
        if i != biggest_idx:
            (input[i], input[biggest_idx]) = (input[biggest_idx], input[i])

    return input

def _max_index(input, a, b, c):
    # TODO - check the maxes
    m = max(input[a], input[b], input[c])
    if m == input[a]:
        return a
    if m == input[b]:
        return b
    if m == input[c]:
        return c


class Test(unittest.TestCase):

    def test_peak_valleys(self):

        a = [5, 8, 6, 2, 3, 4, 6]
        b = [5, 3, 1, 2]
        self.assertEqual(sort_peak_and_valleys(a), [8, 2, 6, 3, 6, 4, 5])
        self.assertEqual(sort_peak_and_valleys(b), [5, 1, 3, 2])


if __name__ == "__main__":
    unittest.main()
