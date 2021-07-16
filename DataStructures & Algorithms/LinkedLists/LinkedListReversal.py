# Reverse a linked list. It shall take in the head
# of the list and return the new head of the list

class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

def reversed(node):
    # My solution is occupying O(2) space.
    marker1 = node
    reversed_list = []

    while marker1 != None:
        # In order to reverse it you must make it double linked?
        reversed_list.append(marker1)
        marker1 = marker1.nextnode
    reversed_list[0].nextnode = None
    i = 0
    while i < len(reversed_list)-1:  # I could instead of creating a new array, use the nodes themselves to tranverse
    # while node is not None:
        reversed_list[i+1].nextnode = reversed_list[i]
        i = i+1
    return reversed_list[-1]

def reversed2(head):
    # Suggested solution
    # We want to do it in place and want to make the function operate in O(1) space
    # O(1) space means we don't want to create a new list....
    #  So we simply use the current nodes
    # Time-wise we can execute the reversal linearly : O(n) time
    # We will make sure to copy the current.nextnode into next_node
    # before setting the current.nextnode to the previous
    current  = head
    previous = None

    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode
    return previous

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    head = a

    print('---------Start of my solution---------')
    print(f'Current head value is: {head.value} ')
    print(a.nextnode.value)
    print(b.nextnode.value)
    print(c.nextnode.value)
    new_head = reversed(head)
    print(f'New head value is : {new_head.value}')
    print(d.nextnode.value)
    print(c.nextnode.value)
    print(b.nextnode.value)
    print('---------Start of the suggested solution---------')
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    head = a
    print(f'Current head value is: {head.value} ')
    print(a.nextnode.value)
    print(b.nextnode.value)
    print(c.nextnode.value)
    new_head = reversed2(head)
    print(f'New head value is : {new_head.value}')
    print(d.nextnode.value)
    print(c.nextnode.value)
    print(b.nextnode.value)

if __name__ == "__main__":
    main()