'''
Factorial Zeros: 
Write an algorithm which computes the number of trailing zeros in n factorial.
'''


'''
4! = 1x2x3x4   = 24 
5! = 1x2x3x4x5 = 120
10! = xxx5x10 = xxxx5x5 = xx00
15! = xxx5x10x15 = xxxxx5x5x5 = xx000
20! = xxx5x10x15x20  = xxxxxxx5x5x5x5 = xx0000
25! = xxx5x10x15x20x25 = xxxxxx5x5x5x5x5x5 = xx000000
'''

import unittest


def factorial_zeros(n:int) -> int:

    # trailing zeroes == number of multiple of 5 in it
    count = 0
    while n >= 5:
        count += n // 5 
        n = n // 5
        if count % 5 == 0:
            count += 1
    
    return count


def factorial_zeros_sol(num:int) -> int:

    # trailing zeroes == number of multiple of 5 in it
    count = 0
    if num < 0:
        return -1
    
    i = 5
    while num // i > 0:

        count += num // i
        i = 5*i 
    
    return count


class Test(unittest.TestCase):

    def test_sorted_merge(self):

        self.assertEqual(factorial_zeros(5), factorial_zeros_sol(5))
        self.assertEqual(factorial_zeros(10), factorial_zeros_sol(10))
        self.assertEqual(factorial_zeros(15), factorial_zeros_sol(15))
        self.assertEqual(factorial_zeros(25), factorial_zeros_sol(25))
        self.assertEqual(factorial_zeros(35), factorial_zeros_sol(35))


if __name__ == "__main__":
    unittest.main()
