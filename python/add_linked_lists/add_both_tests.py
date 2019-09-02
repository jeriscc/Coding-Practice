from add_both import *
from math import floor

def numToList(num):
    """Creates an linked list of digits from an integer number"""
    if (num > 10):
        new_node = Node(num % 10)
        new_node.next = numToList(floor(num / 10))
        return new_node
    else:
        return Node(num)

def listToNum(head):
    """Converts a linked list of digits into an integer number"""
    if head.next is None:
        return head.data
    else:
        return head.data + (listToNum(head.next) * 10)

def testNumPair(num1, num2):
    """Converts numbers to lists and tests if the addBoth functions works"""
    list1 = numToList(num1)
    list2 = numToList(num2)
    result = addBoth(list1,list2)
    assert listToNum(result) == num1 + num2,"Failed for {} and {}".format(num1, num2)

def main():
    testNumPair(1,2)
    testNumPair(0,25)
    testNumPair(1234,5678)

if __name__ == '__main__':
    main()