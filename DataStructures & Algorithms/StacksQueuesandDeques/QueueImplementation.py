
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0,item) # must append at the rear of the queue
        # insert attribute takes in the index and then the item it shall insert

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)



def main():

    q = Queue()
    print(q.items)

    print(q.isEmpty())

    q.enqueue(1)
    q.enqueue(2)
    print(q.items)
    print(q.isEmpty())



if __name__ == "__main__":
    main()