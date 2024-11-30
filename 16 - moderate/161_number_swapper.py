"""
Number Swapper: 
Write a function to swap a number in place (that is, without temporary variables).
"""

import unittest

'''
nb = na ^ nb ^ na
'''


def swap_number(numA, numB):
    
    numA = numA ^ numB 
    numB = numA ^ numB # numB = numA ^ (numB ^ numB) = numA
    numA = numA ^ numB # numA = numA ^ numB ^ numA = numB ^ (numA ^ numA)
    
    return (numA, numB)


class Test(unittest.TestCase):

    def test_sorted_merge(self):

        self.assertEqual(swap_number(15, 29), (29, 15))


if __name__ == "__main__":
    unittest.main()
