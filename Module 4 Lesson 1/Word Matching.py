def match_words(words):
    ctr = 0
    ist = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            ist.append(word)

    print("List of words with the same first and last characters\n", ist)
    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words with the same first and last characters:", count)