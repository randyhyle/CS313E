#  File: Hash.py

#  Description: Implement a cache with hash table and linked list

#  Student Name: Hoang Randy Hy Le

#  Student UT EID: hhl385

#  Course Name: CS 313E

#  Unique Number: 52590

import sys


# A class to represent a LinkedList node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# A class to represent a LinkedList
class LinkedList:
    def __init__(self):
        self.first = None

    # we want to always add this item at the front
    def insert_first(self, data):
        node = Node(data)
        node.next = self.first
        self.first = node


# A hash table mimicking a cache
class HashingCache:
    def __init__(self, size):
        self.con = [None for i in range(size)]

    # Return the size of the hash table
    def size(self):
        return len(self.con)

    # Return the hash index given a number to be hashed
    # DO NOT MODIFY THIS HASH FUNCTION
    def hash_idx(self, num):
        return num % len(self.con)

    # Input: a number to be hashed. Place this item in the table 
    # at the desired place
    # Output: n/a
    def hash(self, num):
        idx = self.hash_idx(num)
        prevnode = None
        if self.con[idx] is not None:
            firstnode = self.con[idx].first
        else:
            self.con[idx] = LinkedList()
            self.con[idx].insert_first(num)
            return

        currnode = firstnode
        while currnode is not None and currnode.data != num:
            prevnode = currnode
            currnode = currnode.next
        if currnode is None:
            self.con[idx].insert_first(num)
        else:
            prevnode.next = currnode.next
            self.con[idx].first = currnode
            currnode.next = firstnode

    # Input: a number to be found in the cache. If the number is
    # in cache, bring it to the front of the linked list at its
    # index.
    # Output: the node found, or None if it is not in cache
    def find(self, num):
        prevnode = None
        idx = self.hash_idx(num)
        if self.con[idx] is not None:
            firstnode = self.con[idx].first
        else:
            return None
        currnode = firstnode
        while currnode is not None and currnode.data != num:
            prevnode = currnode
            currnode = currnode.next
        if currnode is None:
            return None
        else:
            prevnode.next = currnode.next
            self.con[idx].first = currnode
            currnode.next = firstnode
            return currnode.data

    # Helper function to print out the hash table
    # DO NOT MODIFY THIS FUNCTION
    def __str__(self):
        res = '['

        for i in range(self.size() - 1):
            if (self.con[i] == None):
                res += 'None, '
            else:
                curr = self.con[i].first
                while (curr != None and curr.next != None):
                    res += str(curr.data) + '->'
                    curr = curr.next

                # last item
                if (curr != None):
                    res += str(curr.data) + ', '
        # print last item
        if (self.con[-1] == None):
            res += 'None'
        else:
            curr = self.con[-1].first
            while (curr != None and curr.next != None):
                res += str(curr.data) + '->'
                curr = curr.next

            # last item
            if (curr != None):
                res += str(curr.data)
        res += ']'
        return res


def main():
    size = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    cache = HashingCache(size)

    for i in range(n):
        cache.hash(int(sys.stdin.readline()))
    print(cache)

    m = int(sys.stdin.readline())
    for i in range(m):
        cache.find(int(sys.stdin.readline()))

    print(cache)


if __name__ == "__main__":
    main()
