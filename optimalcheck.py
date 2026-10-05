# this is an optimal version of the check program for counting subsequent strings

# instead of scanning s once per word, scan s once total
# How it works
# -imagine the words as people waiting in a line labbeled with the letter they need next
# -for s = "abcde", words = ["a","bb","acd","cde"], the lines astart like this:
#           line a : "a", "acd","ace"
#           line b : "bb"
# Now read s one character at a time. When you read a character, call everyone in that line forward, and each of them either finishes or move to the new line:
#       1. Read a : "a" has no letters left, so itd done count = 1. "acd" and "ace" now need c, so both move to line c
#Do the same and Read for the remaining characters in s and when a word is done add 1 to count, else don't

from collections import defaultdict

def num_matching_subsequence(s,words):
    waiting = defaultdict(list)  
    count = 0 
    for w in words:
        if not w:
            count += 1
        else:
            waiting[w[0]].append(iter(w[1:]))
    
    for c in s:
        batch = waiting.pop(c,[])
        for it in batch:
            nxt = next(it,None)
            if nxt is None:
                count += 1
            else:
                waiting[nxt].append(it)
    print(count) 

s = "abcde"
words = ["a","ab","bb","cde","df",""]

num_matching_subsequence(s,words)