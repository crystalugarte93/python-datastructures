def string_comprehension(arr):
    #Skip to solution , this one was hard
    return print('skip')
def compress(s):
    # This solution compresses without checking.
    # Known as the RunLength Compression algorithm

    # Begin Run asa a empty string
    r = ''
    l = len(s)

    # Check for Length 0
    if l == 0:
        return ''

    # Check for length 1
    if l == 1:
        return s + '1'

    # Intialize values
    last = s[0]
    cnt = 1
    i = 1

    while i < l:
        # Check to see if it is the same letter
        if s[i] == s[i-1]:
            # Add count if same as previous
            cnt += 1
        else:
            #Otherwise store the previous data
            r = r + s[i-1] + str(cnt)
            cnt = 1
        # Add to index count to terminate while loop
        i +=1
    # Put everything back into run
    r = r + s[i-1] + str(cnt)

    return print(r)

def main():
    phrase = 'AAAAJJHHFSSSSUUUOVVVLLL'
    # Input 'AAB' --> Output 'A2B1' even though this takes more space
    # Input 'AAAaaa' --> Output: 'A3a3'

    print(f'Input : {phrase}')
    print(f'Output from the suggested solution: ')
    compress(phrase)
    print(f'Output from my solution:')
    string_comprehension(phrase)

if __name__ == "__main__":
    main()