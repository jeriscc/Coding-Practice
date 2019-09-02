# Reference: https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def stringifyList(head):
    """Helper function for stringifying linked list"""
    if head is None:
        return ' '
    curr_node = head
    result = ''
    while curr_node:
        result = result + curr_node.data + " "
        curr_node=curr_node.next
    return result

'''
	Function to add two numbers represented 
	in the form of the linked list.
	
	Function Arguments: head_a and head_b (heads of both the linked lists)
	Return Type: head of the resultant linked list.
    
    __>IMP : numbers are represented in reverse in the linked list.
    Ex:
        145 is represented as  5->4->1.
    
    resultant head is expected in the same format.
'''
def addBoth(head_a,head_b):
    if head_a is None:
        return head_b
    elif head_b is None:
        return head_a
    new_val = head_a.data + head_b.data
    if new_val >= 10:
        head_a.next = addBoth(head_a.next, Node(1))
    new_node = Node(new_val % 10)
    new_node.next = addBoth(head_a.next, head_b.next)
    return new_node