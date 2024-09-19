'''
URLify: 
Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string. 
(Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
'''
import unittest


# Time: O(N). Space: O(1)
def urlify(input:list[str], length: int) -> str:

    right = len(input) - 1
    for i in range(length-1, -1, -1):
        if input[i] == ' ':
            input[right-2:right+1] = '%20'
            right -= 3
        else:
            input[right] = input[i]
            right -= 1
    
    return input


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
