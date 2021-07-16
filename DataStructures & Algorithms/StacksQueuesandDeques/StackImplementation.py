# Basic implementation of a stack
class Stack(object):
    def __init__(self):
	    self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self): #return the top item, the item put into the stack
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def main():
    s = Stack()
    print(s.isEmpty()) # proves it is empty
    s.push(1)
    s.push(2)
    s.push('two')
    print(s.peek())
    print(s.size())
    s.push(True)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.isEmpty())
    print(s.pop())
    print(s.isEmpty())

if __name__ == "__main__":
    main()