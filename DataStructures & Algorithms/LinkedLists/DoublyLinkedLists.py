class DoublyLinkedListNode(object):

    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None

def main():

    # Create unlinked nodes:
    a = DoublyLinkedListNode(1)
    b = DoublyLinkedListNode(2)
    c = DoublyLinkedListNode(3)

    a.next_node = b
    b.prev_node = a
    b.next_node = c
    c.prev_node = b

    print(a.value)
    print(a.prev_node)

if __name__ == "__main__":
    main()