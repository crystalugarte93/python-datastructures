#given an array of integrers (pos or neg), find the largest continous sum
import random

def largest_cont_sum(arr):
    # Suggested solution
    if len(arr) == 0:
        return 0
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num , num)
        max_sum = max(current_sum, max_sum)
    print(max_sum)
    # Note that continuous sum means the largest sum possible in the specific order given
    # Compare with
    for num in random.sample(arr[1:], len(arr[1:])):
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    print(max_sum)

    # My try: thought to find the max sum possible regardless of order
    '''while current_sum <= max_sum:
        print(current_sum)
        print(max_sum)
        current_sum = 0
        new_arr = random.sample(arr,len(arr))
        for num in new_arr:
            current_sum += num
            print(f'this is the current sum : {current_sum}')'''

def main():
    arr = [1,2, -1,3,4,10,10,-10,-1]
    largest_cont_sum(arr)

if __name__ == "__main__":
    main()