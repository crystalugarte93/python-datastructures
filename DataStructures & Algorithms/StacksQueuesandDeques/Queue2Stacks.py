# Implement a Queue - Using Two Stacks
# Use a Python list data structure as your stack

class Queue2Stacks(object):
    def __init__(self):
        # Two Stacks
        self.instack = [] # one  is the in stack,
        self.outstack = [] # the other is the out stack

    def enqueue(self,element):
        # Key insight is that a stack reverses order while queues don't
        # A sequence of elements pushed on a stack comes back reversed when popped
        # Two stacks chained together will return elements in the same order,
        # since reversed then reversed again is original order
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack: # if there arte no elements in the outstack
            while self.instack: # Do this while there are elements in the instack
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

        # My try:
        #if self.outstack  == []:
        #    for i  in range(len(self.instack)):
        #        self.outstack.insert(i,self.instack.pop(-1))
        #else:

def main():
    q  = Queue2Stacks() # Two stacks in one queue data type
    print(q.stack1)
    print(q.stack2)


if __name__ == "__main__":
    main()