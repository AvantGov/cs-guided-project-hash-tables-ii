"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

```plaintext
Input:
"free"

Output:
"eefr"

Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```

Example 2:

```plaintext
Input:
"dddbbb"

Output:
"dddbbb"

Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```

Example 3:

```plaintext
Input:
"Bbcc"

Output:
"ccBb"

Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```

Inputs:
s -> str

Output:
str

"""
"""
UNDERSTAND: 
- given a string of letters, sort the string in desc order based on the amount of appearances 
    - there will be capital and lowercase items in the string, they should be treated differently
- return the items in decreasing order of appearances in the string 

** since the capital and lowercase items will be recognized as different upon comparison, we do not 
need to perform any kind of manipulation on the items 

PLAN:
- use a dictionary to store the different letters that appear in the string
    - iterate through the string, adding the different letters to the dict / iterating the count of items 

- sort the keys in a desc order 

- create collector string 
- iterate through the keys of the dictionary 
    for items in range 1 > num of appearances 
        append a copy of the key to the collector string 
    return collector string 

"""
# this is known as a type-note that just lets devs know the type of expected data input coming in
# this has no syntatic meaning 
# def frequency_sort(s: str) -> str:

def frequency_sort(string):
    dict__occurances = {}

    for letter in string:
        if letter in dict__occurances:
            dict__occurances[letter] += 1
        else:
            dict__occurances[letter] = 1
    print(dict__occurances)


    sorted_keys = sorted(dict__occurances, key = dict__occurances.get, reverse=True)
    print("sorted items:", sorted_keys)

    collector = ''

    for key in sorted_keys:
        count = dict__occurances[key]
        for i in range(count):
            collector += key
        print("new string:", collector)
    
    return collector



frequency_sort('free')
    