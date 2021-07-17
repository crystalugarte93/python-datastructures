class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

def linked_list_nth_to_last2(head,n):
    # Imagine you have a bunch of nodes and a 'block'  which is n-nodes wide
    # We could walk this 'block' all the way down the list, and once the front of the block reaches the end,
    # then the other end of the block would be at the Nth node
    # To implement this block, we would just have two pointers: a left and a right pair of pointers
    # Steps needed:
    # 1) Walk one pointer n nodes from the head, this will be the right_point
    # 2) Put the other pointer at the head, this will be the left_point
    # 3) Walk/Traverse the  block (both pointers) towards the tail, one node at a time
    # - keeping a distance of n between them
    # 4) Once the right_point has hit the tail, we know that the left point is at the target

    left_pointer = head
    right_pointer = head
    for i in range(n-1): # Width  of the bar
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')
        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode
    return left_pointer

def linked_list_nth_to_last(head,n):
    # Write a function that takes a head node and
    # an integer value n  and then returns the nth to
    # last node in the linked list
    current = head
    array = []
    k = 0
    while current != None:
        if current.value == n:
            k = 1
            target_node = current
        if k == 1:
            array.append(current)

        nextnode = current.nextnode
        current = nextnode
    return array, target_node

def main():
    print('---------Start of my solution---------')
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e
    array, target_node = linked_list_nth_to_last(a,2) # Understood target node as the N'th node element

    for node in array:
        print(node.value)
    print(f'Target node has value: {target_node.value}')

    print('---------Start of the suggested solution---------')

    target_node = linked_list_nth_to_last2(a, 2)
    print(f'Target node has value: {target_node.value}') # Seems N = meant to  be the width of the bar,
    # and thus := the left_point value of that bar


if __name__ == "__main__":
    main()