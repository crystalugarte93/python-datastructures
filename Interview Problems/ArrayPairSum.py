
def array_pair_sum(array,k):
    # Solution proposed bythe author
    #O(N) algorith usesthe set data structure.
    # Create a seen elements dictionary,
    # and add seen elements there.
    # THe algorithm has complexity O(N) because we only do one linear scan the
    # array,and for each element we just check whether the corresponding number
    # to form a pair is in the set or add the current element to the set. Insert
    # and find operations of a set are both average O(1),
    # so the algorithm is O(N) in total.

    if len(array)<2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    for num in array:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target), max(num,target)))
    #return print(len(output))
    print('\n'.join(map(str,list(output))))

    # My attempt
    #pairs = []
    #for i in array:
    #    for j in array:
    #        if i+j == k:
    #            if (j,i) in pairs:
    #                pass
    #            else: pairs.append((i,j))
    #return print(list(set(pairs)))


def main():
    array = [1,3,2,2]
    k = 4
    array_pair_sum(array,k)

if __name__ == "__main__":
    main()
