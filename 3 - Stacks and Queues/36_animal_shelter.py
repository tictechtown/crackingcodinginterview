'''
Animal Shelter: 
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. 
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, 
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 
They cannot select which specific animal they would like. 
Create the data structures to maintain this system and implement operations such as 
- enqueue
- dequeueAny
- dequeueDog
- dequeueCat

You may use the built-in Linked list data structure.
'''
import unittest

from LinkedList import LinkedListNode

#  [1(c),2(d),3(c),4(d),5(c)]
#  (1,c) -> (2,d) -> (3,c) -> (4,d) -> (5,c)
#
#
#
#

class AnimalShelter:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, animalId, animalType):
        if self.head is None:
            self.head = LinkedListNode((animalId, animalType))
            self.tail = self.head
        else:
            self.tail.next = LinkedListNode((animalId, animalType))
            self.tail = self.tail.next
    
    def dequeueAny(self):
        if not self.head:
            raise ValueError

        value = self.head.value[0]
        self.head = self.head.next
        return value

    def dequeueDog(self):
        return self._dequeueAnimalType(0)
    def dequeueCat(self):
        return self._dequeueAnimalType(1)
    def _dequeueAnimalType(self, animalType):

        if not self.head:
            raise ValueError
        
        if self.head.value[1] == animalType:
            val = self.head.value[0]
            self.head = self.head.next
            return val

        runner = self.head
        while runner.next and runner.next.value[1] != animalType:
            runner = runner.next
                
        if runner.next:
            val = runner.next.value[0]
            runner.next = runner.next.next
            return val

        # no animal found
        raise ValueError
    
class Test(unittest.TestCase):

    test = [1, 3, 2, 4, 5, 2, 6, 4]

    def test_stack(self):
        shelter = AnimalShelter()
        animals = self.test
        for i in range(len(animals)):
            shelter.enqueue(animals[i], i % 2)

        self.assertEqual(shelter.dequeueAny(), 1)
        self.assertEqual(shelter.dequeueDog(), 2)
        self.assertEqual(shelter.dequeueCat(), 3)
        self.assertEqual(shelter.dequeueDog(), 5)
        self.assertEqual(shelter.dequeueDog(), 6)
        self.assertEqual(shelter.dequeueCat(), 4)


if __name__ == "__main__":
    unittest.main()
