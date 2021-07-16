class Deque(object):
    def __init__(self):
        self.items = []

    def addFront(self,item):
        return self.items.insert(0,item)

    def addRear(self,item):
        return self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def main():
    d = Deque()
    print(d)

    print(d.isEmpty())

    d.addRear('world')
    d.addFront('hello')
    print(d.isEmpty())
    print(d.size)
    print(d.isEmpty())
    print(f'{d.removeFront()} {d.removeRear()}')
    print(d.size)
    print(d.isEmpty())

if __name__ == "__main__":
    main()
