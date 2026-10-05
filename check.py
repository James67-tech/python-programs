# Given a String s and an array of strings words,
# return the number of words[i] that is a subsequence of s

# A subsequence of a String is a new string generated from the original string with the some characters 
# (can be none) deleted without changing the order of the remaining characters

# Example : for a s "abcde" a string "abc" is its subsequence even ""(empty string), "cde" BUT NOT "bb","ecb"


def num_matching_subsequence(s,words):
    count = 0
    for word in words:
        j = 0
        for ch in s:
            if j<len(word)  and ch == word[j]:
                j+=1
        if j == len(word):
            count +=1
    print(count)

s = "abcde"
words = ["a","ab","bb","cde","df",""]

num_matching_subsequence(s,words)

 