# Radix Sort - Anagrams
Consider the following problem: Given two lists of words, we wish to find all words in the first
list which have an anagram in the second list.

Strings r and s are anagrams of one another if the characters in s can be permuted to form r.
Trivially, if r = s, then they are anagrams of one another.

## Input
Both arguments, list1 and list2, are lists of strings. All characters are lowercase a-z. Neither
list contains duplicate strings, but there may be strings which appear in both lists.

## Output
A list of strings (in no particular order) from list1 which have at least one anagram appearing
in list2. Note that it is possible for two different strings in list1 to share an anagram in
list2.

## Example
```
list1 = [spot, tops, dad, simple, dine, cats]
list2 = [pots, add, simple, dined, acts, cast]
>>> words_with_anagrams(list1, list2)
[cats, dad, simple, spot, tops]
```

## Complexity
Your algorithm should run in O(L1M1 + L2M2) where
- L1 is the number of elements in list1
- L2 is the number of elements in list2
- M1 is the number of characters in the longest string in list1
- M2 is the number of characters in the longest string in list2

### Disclaimer
1. This case study derives from my school assignment.
2. Details of the actual case study has been sanitized and changed.

