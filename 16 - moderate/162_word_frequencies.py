'''
Word Frequencies: 
Design a method to find the frequency of occurrences of any given word in a book.
What if we were running this algorithm multiple times?
'''

from collections import Counter


def find_word_frequency(word: str, book: list[str]) -> int:
    counter = Counter(book)
    return counter[word] if word in counter else 0


'''
Follow up, multiple times?
'''

class BookFrequency:

    # we parse the book first
    def __init__(self, book):
        self.counter = Counter(book)
    
    def get_frequency(self, word:str) -> int:
        return self.counter[word] if word in self.counter else 0