'''
Diving Board: 
You are building a diving board by placing a bunch of planks of wood end-to-end. 
There are two types of planks, one of length shorter and one of length longer. 
You must use exactly K planks of wood. 
Write a method to generate all possible lengths for the diving board.
'''


# Time: 2**k, Space: 2**k
def diving_board(k:int) -> list[str]:

    output = set()


    def helper(k, size):

        if k == 0:
            output.add(size)
            return

        helper(k-1, size+['S'])
        helper(k-1, size+['L'])


    helper(k, [])
    return list(output)


# Time: O(n), Space: O(n)
def diving_board_2(k:int) -> list[str]:
    output = []
    for i in range(k):
        val = ['S']*i + ['L']*(k-1)
        output.append(val)

    return output