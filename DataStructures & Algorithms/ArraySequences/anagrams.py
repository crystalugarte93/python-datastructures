def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2. replace(' ', '').lower()

    #Alt 1: #####Edge Case Check####
    if len(s1) != len(s2):
        return print(False)

    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return print(False)
    return print(True)

    # Alt 2
    # return print(sorted(s1) == sorted(s2))

def main():
    anagram('client eastwood','olsd west action')
if __name__ == "__main__":
    main()