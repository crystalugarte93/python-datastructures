class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

def cycle_check(node):
    # If we where to have more than three nodes then we need more info
    #Given that we only have three nodes:
    return print(node.nextnode == node.nextnode.nextnode.nextnode.nextnode) # Your function should return a boolean

def cycle_check2(node):
    # We will have two markers  traversing through the list. Marker 1 and Marker 2
    # Both begin at the first node of the list and traversing through the linked list.
    # However, the second marker will move two nodes for every one node that the marker 1 moves.
    # By this logic we can imagine that the markers are 'racing' through the linked list, with marker 2
    # moving faster. If the linked list has a cycle  and is circularly connected, we will have the analogy of  track
    # In this case, marker 2 will eventually be 'lapping'  the marker 1 and they will equal each other
    # if the list has no cycle, then marker 2 should be able to continue on until the very end,
    # never equaling the first marker.
    marker1 = node
    marker2 = node
    while marker2  != None and marker2.nextnode!=  None:
        marker1 = marker1.nextnode
        marker2  = marker2.nextnode.nextnode

        if marker2 == marker1:
            return print(True)
    return print(False)

def main():
    #  Return true if the list contains a cycle.
    # A Cycle is when a node's next point actually points
    # back to the previous node in the list
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.nextnode = b
    b.nextnode = c
    c.nextnode = a
    # Cycled list check
    print('--- My solution---')
    cycle_check(b) # where n is the number of nodes all together
    # Noncycled list check
    c.nextnode = b
    cycle_check(b)
    print('--- Suggested solution---')

    cycle_check2(b)

if __name__ == "__main__":
    main()