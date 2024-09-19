'''
String Compression: 
Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, your method should return
the original string. 
You can assume the string has only uppercase and lowercase letters (a - z).
'''
import unittest


# Time: O(N) Space: O(N)
def compress_string(input:str) -> str:

    if not len(input):
        return input

    counter = 0
    current_char = input[0]
    output = ""
    for ch in input:
        if ch == current_char:
            counter += 1
        else:
            output += f"{current_char}{counter}"
            current_char = ch
            counter = 1
    
    if counter > 0:
        output += f"{current_char}{counter}"
    
    return output if len(output) < len(input) else input


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = compress_string(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
