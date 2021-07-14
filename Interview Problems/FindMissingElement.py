from collections import defaultdict

def find_missing_element(l1,l2):
    ### My attemptseenl1 = defaultdict()
    seenl1={}
    seenl2={}

    for num in l1+l2:
        seenl1[str(num)] = 0
        seenl2[str(num)] = 0
    for num in l1:
        seenl1[str(num)] += 1
    for num2 in l2:
        seenl2[str(num2)] += 1
    print(seenl1)
    print(seenl2)
    output = {}

    for k,v in seenl1.items():
        output[k] = v - seenl2.get(k,0)
        if output[k]<0:
            print(f'There are {abs(output[k])} missing elements of {k} in l2')
        elif output[k]>0:
            print(f'There are {abs(output[k])} missing elements of {k} in l1')

    #Suggested solution:
    #Naive solution is to go through every element in the
    #second array and check whether it appears in the first : O(N^2)
    #since we would two for loops

    #A more efficient solution is to sort the first array, so while checking whether an
    #element appears in the second, we can do a binary search  : O(NlogN)
def finder(arr1,arr2):
    result = 0
    # Perform an XOR between the numbers in the array
    print(arr1+arr2)
    for num in arr1+arr2:
        result ^= num
        print(result)
    return print(result)


    # if numbers are too long or too small, you may get overflow issues with this method
    # If we use exlusive or (XOR) - a logical operation that ouputs the true only when both
    # inputs differ (one is true, the other is false)
    # Instead of below we can use XOR (see above)

    #d = defaultdict(int)
    #for num in arr2:
   #     d[num] += 1
   # for num in arr1:
   #     if d[num] == 0:
   #         print(num)
   #         pass
    #    else:
     #       d[num] -= 1

    # insted of below simplified code that only splits out the first missing element,
    # we will be using hashed tables by using the module collections
    # arr1.sort()
    # arr2.sort()
    # for num1, num2 in zip(arr1,arr2):

    #    if num1!=num2:
   #         return print(num1)
    #return print(arr1[-1])'''

def main():
    l1 = [1,2,2,4]
    l2 = [1,4,3,3]
    #print('My solution:')
    #find_missing_element(l1,l2)
    print('Suggested solution')
    finder(l1,l2)


if __name__ == "__main__":
    main()