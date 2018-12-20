# This problem was asked by Twitter.
#
# Implement an autocomplete system. That is, given a query string s 
# and a set of all possible query strings, return all strings in 
# the set that have s as a prefix.
# For example, given the query string de and the set of strings 
# [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data 
# structure to speed up queries.

def preprocess_dictionary(words):
    dictionary = {}
    for word in words:
        curr_dict = dictionary
        for c in word:
            if not c in curr_dict:
                curr_dict[c] = {}
            curr_dict = curr_dict[c]
    return dictionary

def autocomplete_rec(prefix, dictionary, list):
    if len(dictionary) == 0:
        list.append(prefix)
    for c, value in dictionary.items():
        autocomplete_rec(prefix+c, value, list)

def autocomplete(prefix, dictionary):
    curr_dict = dictionary
    for c in prefix:
        curr_dict = curr_dict[c]
    words = []
    autocomplete_rec(prefix, curr_dict, words)
    return words

dictionary = preprocess_dictionary(['dog', 'deer', 'deal'])
words = autocomplete('de', dictionary)
print(words)