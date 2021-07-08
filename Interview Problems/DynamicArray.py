import ctypes, sys

class DynamicArray(object):

    def __init__(self):
        self.n = 0 #counts of the elements of the array
        self.capacity = 1 #how many elements the array can hold
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self,k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')

        return self.A[k]

    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity isn't enough

        self.A[self.n] = ele
        self.n +=1

    def _resize(self,new_cap):

        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()


def main():
    arr= DynamicArray()

    for i in range(0,10000,500):
        arr.append(i)
        print(f'Appending {i} to the array {arr}')
        print(f'Printing new length {len(arr)}')
        print(f'{sys.getsizeof(arr)}')

    print(f'Printing first element of the array {arr[0]}')
if __name__ == "__main__":
    main()