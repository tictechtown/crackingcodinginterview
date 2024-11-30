'''
Number Max: 
Write a method that finds the maximum of two numbers. 
You should not use if-else or any other comparison operator.
'''

def number_max(numA:int, numB:int) -> int:

    def sign(a):
        return (a >> 31 & 1)

    def flip(a):
        return 1^a

    delta_a = sign(numA - numB)
    delta_b = flip(delta_a)
    return numA*delta_a + numB*delta_b # delta_a = 1, delta_b = 0