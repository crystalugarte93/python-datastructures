class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

def main():

    # Create unlinked nodes:
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextnode = b
    b.nextnode = c
    # c will automatically keep its None as next node and thus be the last node of this singly linked list

    print(a.value)
    print(a.nextnode.value)

if __name__ == "__main__":
    main()