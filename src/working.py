"""
given a string of text, we want to see how many instances of the word "lambda" can be formed 
- each item in the string can onl;y be used once

UNDERSTAND:
- want to return and int that represents how many times we can create the word "lambda" out 
of the string 
    - more specifically we want to see how many times the letters appear in the string 


"""

def lambda_count(string):
# PLAN:
# 1. create a dict with the letters LAMB and their frequencies as the values 
    dict__counts = {}
    for char in string:
        if char not in "lambda":
            continue

        if char in dict__counts:
            dict__counts[char] += 1
        else:
            dict__counts[char] = 1

# 2. look at the values for each and return the minimum (divide by 2 for a)
    min_val = None
    for char, count in dict__counts.items():
        # account for two a's needed by implementing int division to get whole number
        if char == 'a':
            count = count // 2

        if min_val is None or if count < min_val:
            min_val = count
    
    return min_val