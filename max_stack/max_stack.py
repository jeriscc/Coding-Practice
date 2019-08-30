# Reference: https://www.geeksforgeeks.org/find-maximum-in-a-stack-in-o1-time-and-o1-extra-space/
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self): 
        return "Node({})".format(self.value) 

    __repr__ = __str__

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.maximum = None
 
    def __str__(self): 
        temp=self.top 
        out=[] 
        while temp: 
            out.append(str(temp.value)) 
            temp=temp.next
        out='\n'.join(out) 
        return ('Top {} \n\nStack :\n{}'.format(self.top,out)) 
    
    #  __repr__ is same as __str__ 
    __repr__=__str__

    def getMax(self):
        if self.top is None:
            print("The stack is empty")
        else:
            print("The maximum element of the stack is: {}".format(self.maximum))

    def __len__(self):
        return self.count
    
    def push(self, value):
        if self.top is None:
            self.__push(value)
            self.maximum = value
        elif value > self.maximum:
            self.__push(2*value - self.maximum)
            self.maximum = value
        else:
            self.__push(value)
        print("Number Inserted: {}" .format(value))

    def __push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.count += 1
    
    def peek(self):
        if self.top is None: 
            print ("Stack is empty") 
        else:     
            if self.top.value > self.maximum: 
                print("Top Most Element is: {}" .format(self.maximum)) 
            else: 
                print("Top Most Element is: {}" .format(self.top.value))

    def pop(self):
        if self.top  is None:
            print("The stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if  removedNode > self.maximum:
                print ("Top Most Element Removed :{} " .format(self.maximum))
                self.maximum = (2*self.maximum - removedNode)
            else:
                print ("Top Most Element Removed :{} " .format(removedNode))
            self.count -= 1
