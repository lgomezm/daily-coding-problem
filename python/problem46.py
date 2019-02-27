def longest_palindrome(text):
    max_word = []
    for i in range(len(text)):
        word = [text[i]]
        for j in range(1, min(i+1, len(text)-i)):
            prev = text[i-j]
            next = text[i+j]
            if prev != next:
                break
            word.insert(0, prev)
            word.append(next)
        if len(word) > len(max_word):
            max_word = word
    return "".join(max_word)

print(longest_palindrome("aabcdcb"))
print(longest_palindrome("banana"))