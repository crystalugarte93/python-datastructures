def uni_char(s):
    return print(len(set(s)) == len(s))

def unique_char_in_string(s):
    # Given a string, determine if it is comprised of all unique characters.
    # e.g. 'abcde' has all unique characters and should return True
    # 'aabcde' should return False
    char = set() # empty seet

    for let in s:
        if let in char:
            return print(False)
        else:
            char.add(let)
    return print(True)

def main():
    s = 'sfbn'
    uni_char(s)
    unique_char_in_string(s)


if __name__ == "__main__":
    main()