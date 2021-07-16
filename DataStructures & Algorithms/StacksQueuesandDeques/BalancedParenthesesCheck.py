class Deque(object):
    def __init__(self):
        self.items = []

    def addFront(self, item):
        return self.items.insert(0, item)

    def addRear(self, item):
        return self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self,item):
        if self.items[-1] == item:
            self.items.pop(-1)
            return print(f'Successfully removed opposite parenthesis: {item}')
        else: return print(f'The parentheses are unbalanced: rear is {self.items[-1]} and item is {item}')

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def print(self):
        #print(self.items)
        for char in self.items:
            print(char)

def balance_check2(s):
    print('______Start of Suggested solution________')
    if len(s)%2 != 0:
        return print('Unbalanced parentheses')

    opening  = set('([{')
    matches = set([('(',')'), ('[',']'), ('{','}')])
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                print('Unbalanced parentheses')
            last_open = stack.pop()

            if (last_open,paren) not in matches:
                print('Unbalanced parentheses')
    if len(stack) == 0:
        print('Parentheses are balanced')

    print('______End of Suggested solution________')


def balance_check(s):
    #My proposed solution
    print('_______Start of My proposed solution________')
    d = Deque()
    for char in s:
        d.addRear(char)

    print(s[0: d.size()//2])
    for char in s[0: d.size()//2]:
        if str(char) == '(':
            d.removeRear(')')
        if str(char) == '[':
            d.removeRear(']')
        if str(char) == '{':
            d.removeRear('}')
    print('_______End of my proposed solution________')
    print('__________________________________________')

def main():
    s = '([[{}]])' #  balanced parentheses
    t = '([[{)]])' #  unbalanced parentheses

    balance_check(s)
    balance_check2(s)

    balance_check(t)
    balance_check2(t)


if __name__ == "__main__":
    main()