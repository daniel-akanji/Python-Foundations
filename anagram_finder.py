def anagram(word1, word2):
    if len(word1) != len(word2):
        return (f"Output: Not an anagram")
    
    one = list(word1.lower())
    two = list(word2.lower())

    char_count1 = {}
    char_count2 = {}

    for char in one:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in two:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    
    if char_count1 == char_count2:
        return (f"Output: Anagram")
    else:
        return (f"Output: Not an anagram")


print(anagram("Silent", "Listen"))
print(anagram("Triangle", "Integral"))
print(anagram("Apple", "Pale"))
print(anagram("hello", "billion"))