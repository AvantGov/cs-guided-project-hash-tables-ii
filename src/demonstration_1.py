"""
You are given a non-empty list of words.

Write a function that returns the *k* most frequent elements.

The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.

Example 1:

```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2

Output:
["lambda", "school"]

Explanation:
"lambda" and "school" are the two most frequent words.
```

Example 2:

```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4

Output:
["the", "is", "cloudy", "sky"]

Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```

Notes:

- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
"""
"""
Input:
words -> List[str]
k -> int

Output:
List[str]
"""

"""
UNDERSTAND: 
- given a list of words, return the most frequent elements in the sentence
- return a list of the strings that are most common in the given list 

- k will serve as the collector for the most common words, so that any items
that have k amount of words will be included in the list of words 

PLAN 
Option 1: implement with list.count()
- list.count(x) will return the number of times x appears in the list 
    - this would require us to iterate through the list each time for each different item

Option 2:
- use a dictionary to store the words as keys and number of appearances as values 
    - iterate through the words 
    - if the word is already in the dictionary, incremement the count and move closer 
    - if it is not, add it to the dictionary and set it to a count of 1

Option 3: 
- iterate over the values and return the leys for the top 4 items (alphabetically for ties)
    - this could be done as a heap 
    - we could also sort the list of words 
    - get max() k times and remove from the hash table

"""


"""
IMPLEMENTATION CHOICE:
Option 2:
- use a dictionary to store the words as keys and number of appearances as values 
    - iterate through the words 
    - if the word is already in the dictionary, incremement the count and move closer 
    - if it is not, add it to the dictionary and set it to a count of 1
"""
def top_k_frequent(words, k):
    ref_dict = {}
    for word in words:
        if word in ref_dict:
            ref_dict[word] += 1
        else:
            ref_dict[word] = 1
    print(ref_dict)

# reverse sort the list of keys to be in descending order 
    sorted_keys = sorted(ref_dict, key=ref_dict.get, reverse=True)
    print(sorted_keys)

# returning the top k items
    return sorted_keys[:k]
