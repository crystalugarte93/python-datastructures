
def rev_words(s):
    words = []
    length= len(s)
    spaces = [' ']

    i = 0
    # We will iterate through the entire string and cross check with the
    # spaces array (i.e. compare and exclude the white spaces)
    while i < length:
        if s[i] not in spaces:
            # Only when we find a character that is not a whitespace,
            # we identify the start of a new word
            word_start = i
            # Now we collect all chars until the next white space
            while i < length and s[i] not in spaces:
                i += 1
            # Only when we've done so, we
            # append the word to the list of words

            words.append(s[word_start:i])
        # Now we go on to the next part of the string
        i += 1

    return print(" ".join(reversed(words)))


def reverse_phrase(phrase):
    phrase = phrase.strip()
    list = phrase.split(' ')
    reversed_list = list[::-1]
    return print(' '.join(reversed_list))


def main():
    phrase = '  what the actual    godness sake '
    print(f'Input : {phrase}')
    print(f'Output from the suggested soltion: ')
    rev_words(phrase)
    print(f'Output from my solution:')
    reverse_phrase(phrase)

if __name__ == "__main__":
    main()