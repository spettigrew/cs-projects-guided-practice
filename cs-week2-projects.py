"""
Given a sorted array `nums`, remove the duplicates from the array.

Example 1:

Given nums = [0, 1, 2, 3, 3, 3, 4]

Your function should return [0, 1, 2, 3, 4]

Example 2:

Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]

Your function should return [0, 1, 2, 3, 4, 5].

*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*
"""


def remove_duplicates(nums):
    # Your code here
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)
        else:
            i = i + 1
    return nums


"""
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.
Example:
Input: [1,3,3,2,1]
Output: True
Example:
Input: [0,1,2,3]
Output: False
*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""


def contains_duplicate(nums):
    # Your code here
    num_set = set(nums)
    if len(num_set) == len(nums):
        return False
    else:
        return True


# print(contains_duplicate([1, 3, 3, 2, 1]))

"""
Given two strings `a` and `b`, write a function to determine if `a` is an
**anagram** of `b`.
*Note: an anagram is a word, phrase, or name formed by rearranging the letters
of another, such as cinema, formed from iceman.*
**Example:**
Input: `a` = "anagram", `b` = "nagaram"
Output `True`
**Example:**
Input: `a` = "bat", `b` = "tar"
Output `False`
"""


def is_anagram(a, b):
    # Your code here
    pass


# # """
# # Example One
# # """
# # my_list1 = [1, 2, 3, 4, 5, 6]
# # my_list2 = my_list1
# # # How would you verify that my_list1 and my_list2 have the same identity?
# # print(id(my_list1) == id(my_list2))
# #
# # my_list1.append(7)
# # # Check if my_list1 and my_list2 still have the same identity.
# # # If they do, why is that?
# # print(id(my_list1) == id(my_list2))
# #
# #
# # #
# # # """
# # Example Two
# # """
# # my_text1 = "Lambda School"
# # my_text2 = my_text1
# # # How would you verify that my_text1 and my_text2 have the same identity?
# # print(id(my_text2) == id(my_text1))
# #
# # my_text1 += " is awesome!"
# # # Check if my_text1 and my_text2 still have the same identity?
# # print(id(my_text2) == id(my_text1))
# # # If they do not, why is that?
# #
# # # Now check if my_text1 and my_text2 have the same value?
# # print(my_text1, my_text2)
# # # Do they? Explain why or why not.
# #
# #
# #
# # """
# # Example Three
# # """
# # # Initialize a list and assign to produce
# # produce = ["Apple", "Banana", "Carrot"]
# # # Initialize a tuple and include a reference to the produce list in the tuple
# # store = ("Bill's Grocery", produce)
# # print(id(store))
# # # Add a new item to the produce list
# # produce.append("Dragonfruit")
# # print(id(store))
# #
# # # Did you notice that the identity of store remained the same?
# # # But I thought if you changed a mutable object, a new object would
# # # be created in memory? Why did that not occur here?
#
#
# #  - Constant O(1)	The runtime is entirely unaffected by the input size.
# # This is the ideal solution.
# #  - Logarithmic O(log n)	As the input size increases, the runtime will grow
# #  slightly slower. This is a pretty good solution.
# #  - Linear O(n)	As the input size increases, the runtime will grow at the
# #  same rate. This is a pretty good solution.
# #  - Polynomial O(n^c)	As the input size increases, the runtime will grow at
# #  a faster rate. This might work for small inputs but is not a scalable solution.
# #  - Exponential O(c^n)	As the input size increases, the runtime will
# # grow at a much faster rate. This solution is inefficient.
# #  - Factorial O(n!)	As the input size increases, the runtime will grow
# #  astronomically, even with relatively small inputs. This solution is exceptionally inefficient.
#
#
# """
# Classify the runtime complexity of the sorted_squares function below using Big O notation.
# """
import time
import random

# why do we have big o notation?
# To evaluate performance
# to find out the time it takes to complete a function (relative to other input sizes)
# different computers run at different speeds
# because we care about efficiency
# O(n) -- linear
# O(n^2) -- quadratic
# O(1) -- constant -- the performance doesn't change regardless of input
# O(log n) -- logarithmic -- every time we double the input size, we only add one extra step
# O(2^n) -- exponential
# factorial
# O(n log n) -- linearithmic
"""
Classify the runtime complexity of the number_of_steps function below using Big O notation.
"""
# def number_of_steps(num):
#     # overall: O(log n)
#     # O(1) + O(log n * c) --> O(c log n + 1) --> O(log n)
#     steps = 0                  # constant O(1)
#     while num > 0:             # how many times does the loop run? log n times
#         if num % 2 == 0:       # code w/in the loop is constant
#             num = num // 2
#         else:
#             num = num - 1
#         steps = steps + 1
#     return steps
# #
# # for i in [8, 16, 32, 64]:
# #     print(f"number_of_steps | N: {i} \tsteps: {number_of_steps(i)}")
# print("-------")
# """
# Classify the runtime complexity of the sorted_squares function below using Big O notation.
# """
# def sorted_squares(A):
#     # overall runtime complexity? O(4N + 5) --> O(N)
#     N = len(A)                  # O(1)
#     j = 0                       # O(1)
#     while j < N and A[j] < 0:   # how many times does this loop run? at most N times -- O(N)
#         j += 1                  # O(1)
#     i = j - 1                   # O(1)
#     ans = []                    # O(1)
#     while 0 <= i and j < N:     # how many times does this loop run?  N -- O(N)
#         if A[i] ** 2 < A[j] ** 2:  # O(1)
#             ans.append(A[i] ** 2)  # appending to end of the list is usually constant
#             i -= 1
#         else:
#             ans.append(A[j] ** 2)
#             j += 1
#     while i >= 0:                   # how many times does this loop run? at most N
#         ans.append(A[i] ** 2)       # O(1)
#         i -= 1
#     while j < N:
#         ans.append(A[j] ** 2)
#         j += 1
#     return ans
# for i in [100, 1000, 10000]:
#     a = [j for j in range(-i // 2, i // 2)]
#     start = time.time()
#     sorted_squares(a)
#     end = time.time()
#     print(f"Sorted Squares | N: {i} \ttime: {end - start}")
# """
# Classify the runtime complexity of the insertion_sort function below using Big O notation.
# """
# def insertion_sort(arr):
#     # O(n*n) --> O(n^2)
#     for i in range(1, len(arr)):    # O(n)
#         key = arr[i]                # O(1)
#         j = i - 1                   # O(1)
#         while j >= 0 and key < arr[j]:  # at most N --> O(n)
#             arr[j + 1] = arr[j]     # O(1)
#             j -= 1                  # O(1)
#             for k in range(len(arr)):
#                 # this makes it O(n^3)
#                 # do stuff
#         arr[j + 1] = key
# print("-------")
# for i in [100, 1000, 10000]:
#     a = [random.randint(0, j) for j in range(i)]
#     start = time.time()
#     insertion_sort(a)
#     end = time.time()
#     print(f"insertion_sort | N: {i} \ttime: {end - start}")
# """
# Use Big O notation to classify the space complexity of the function below.
# """
#
#
# def fibonacci(n):
#     lst = [0, 1]
#     for i in range(2, n):
#         lst.append(lst[i - 2] + lst[i - 1])
#
#     return lst[n - 1]
# # O(n)
#
# """
# Use Big O notation to classify the space complexity of the function below.
# """
#
#
# def fibonacci_two(n):
#     x, y, z = 0, 1, None
#
#     if n == 0:
#         return x
#     if n == 1:
#         return y
#
#     for i in range(2, n):
#         z = x + y
#         x, y = y, z
#
#     return z
# # O(1)
#
# """
# Use Big O notation to classify the space complexity of the function below.
# """
#
#
# def do_something(n):
#     lst = []
#     for i in range(n):
#         for j in range(n):
#             lst.append(i + j)
#
#     return lst
# # O(n^2)
#
#
# # numbers = [2, 0, 0, 0]
# #
# #
# def removeEvens(numbers):
#     return [num for num in numbers if num % 2 != 0]
# below code didn't pass tests above did
# for num in numbers:
#     if num % 2 == 0 and num != 0:
#         numbers.remove(num)
# return numbers
# #
# #
# # print(removeEvens(numbers))
# #
# # import statistics
# #
# # sequence = [-1, 3, -2, 2]
# #
# # def arrayMedian(sequence):
# #     return statistics.median(sequence)
# #
# # print(arrayMedian(sequence))
#
# s = "TuVwXYZ"
#
# # s = "ABCDEFFDEfghCBA"
#
# # def originalIncreasingSubstrings(s):
# #     string = ''
# #     subs = []
# #     print(''.join(sorted(s)))
# #     i = 0
# #     for i in range(len(s) - 1):
# #         string = string + s[i]
# #         if s[i + 1] <= s[i]:
# #             subs.append(string)
# #             string = ''
# #             continue
# #     subs.append(s[len(s) - 1])
# #     i += 1
# #     return subs
#
# # s = "TuVwXYZ"
#
# # s = "ABCDEFFDEfghCBA"
# s = "f"
#
#
# def increasingSubstrings(s):
#     string = ''
#     subs = []
#     i = 0
#     if len(s) == 1:
#         subs.append(s[0])
#     else:
#         for i in range(len(s) - 1):
#             # print(s[i])
#             if not string.startswith(s[i]):
#                 string = string + s[i]
#             if ord(s[i]) != ord(s[i + 1]) - 1:
#                 # print(ord(s[i]))
#                 subs.append(string)
#                 string = s[i + 1]
#                 continue
#         # print(f'-1: {ord(s[len(s) - 1])}, -2: {ord(s[len(s) - 2])}')
#         if ord(s[len(s) - 1]) == ord(s[len(s) - 2]) + 1:
#             string = string + s[len(s) - 1]
#         subs.append(string)
#         string = ''
#     return subs
#
#
# print(increasingSubstrings(s))
#
#
# #  25 to binary 11001
# #  63 to binary 111111
# #  9 to binary 1001
# # 111 to binary 1101111
# # 78 to binary 01001110
# What is the number of possible integer values you can store with 4 bytes? How did you make that calculation?
# 4294967296

# What is the number of possible integer values you can store with 8 bytes? How did you make that calculation?
#  18446744073709551616

# Let's say you need to store an array of 64-bit integers. Your array needs to have enough capacity for 24 integers. How many 1-byte slots of memory need to be allocated to store this array?
# 192

# Draw out a model of a section of memory that stores the string "Computer
# Science" as an array of 8-bit ASCII characters.

#  [01000011, 01001111, 01001101, 01010000, 01010101, 01010100,
#   01000101, 01010010, 01010011, 01000011, 01001001, 01000101,
#   01001110, 01000011, 01000101]
# print(8 * 24)
# print(8*5)

#
# param1 = 456
# param2 = 1734
#
# def additionWithoutCarrying(param1, param2):
#     # set variable to hold the added row answers
#     result = []
#     # function to find a digit in a number
#     def find_digit(number, place):
#         return number // 10**place % 10
#     # get larger number
#     larger = None
#     if param1 > param2:
#         larger = param1
#     else:
#         larger = param2
#
#     # using the index of the larger do the addition
#     count = 0
#     for i in range(len(str(larger))):
#         num1 = find_digit(param1, count)
#
#         num2 = find_digit(param2, count)
#         added_digits = num1 + num2
#         count += 1
#         result.append(added_digits % 10)
#     result.reverse()
#     number_string = map(str, result)
#     number_string = ''.join(number_string)
#     result = int(number_string)
#     return result
#
# print(additionWithoutCarrying(param1, param2))
#
# Given an array of positive integers a, your task is to calculate how many of its elements have an even number of digits.#
# Example
# For a = [12, 134, 111, 1111, 10], the output should be evenDigitsNumber(a) = 3.
#
# a = [12, 134, 111, 1111, 10]
#
# def evenDigitsNumber(a):
#     even_count = 0
#     for group in a:
#         if len(str(group)) % 2 == 0:
#             even_count += 1
#     return even_count
#
# print(evenDigitsNumber(a))

# You're writing a new programming language and you'd like it to have the capability of splitting a string into substrings with limited characters. More specifically, we'll call a substring good if the absolute difference in ASCII codes between any two of its characters is less than or equal to k.
#
# For example, if k = 3, then the string "bad" would be considered good, since the greatest difference in ASCII codes is 3 (between the a and d characters). The string "nice" would not be considered good, since there's a difference of 11 between the c and n characters.
#
# You are given a string strToSplit that consists of lowercase English letters only, and your task is to find the minimal number of good substrings you can split it into.
#
# Hint: Iterate over the string strToSplit and keep the ASCII codes of the smallest and the greatest characters in the current substring. Every time when the difference between them becomes greater than k, it means that the last considered symbol should be the first one in a new substring.
#
# Example
#
# For strToSplit = "aaabaaabb" and k = 0, the output should be goodSubstrings(strToSplit, k) = 4.
#
# strToSplit could be split into ["aaa", "b", "aaa", "bb"]. Each substring must consist of only one type of character, because it is required that |s[i] - s[j]| ≤ 0 for each substring s.
#
# For strToSplit = "aaabaaabb" and k = 1, the output should be goodSubstrings(strToSplit, k) = 1.
#
# Since the only characters in the string have a difference of 1, aaabaaabb meets the requirement |strToSplit[i] - strToSplit[j]| ≤ 1. So only 1 substring is required (and it's the full original string).
#
# For strToSplit = "aaabzaaabb" and k = 10, the output should be goodSubstrings(strToSplit, k) = 3.
#
# strToSplit could be split into ["aaab", "z", "aaabb"]. Since the z character has such a large difference with each of its adjacent characters, it must be in a substring of its own.
# def increasingSubstrings(s):
#     string = ''
#     subs = []
#     i = 0
#     if len(s) == 1:
#         subs.append(s[0])
#     else:
#         for i in range(len(s) - 1):
#             # print(s[i])
#             if not string.startswith(s[i]):
#                 string = string + s[i]
#             if ord(s[i]) != ord(s[i + 1]) - 1:
#                 # print(ord(s[i]))
#                 subs.append(string)
#                 string = s[i + 1]
#                 continue
#         # print(f'-1: {ord(s[len(s) - 1])}, -2: {ord(s[len(s) - 2])}')
#         if ord(s[len(s) - 1]) == ord(s[len(s) - 2]) + 1:
#             string = string + s[len(s) - 1]
#         subs.append(string)
#         string = ''
#     return subs


# strToSplit = "aaabaaabb"
# k = 0
# strToSplit = "aaabaaabb"
# k = 1
# strToSplit = "aaabzaaabb"
# k = 5
# def goodSubstrings(strToSplit, k):
#     smallest = ord(strToSplit[0])
#     largest = 0
#     subs = []
#     s = ''
#     for i in range(len(strToSplit)):
#         # print('Letter', strToSplit[i],
#         #       ord(strToSplit[i]))
#         # print(f'smallest: {smallest} largest: {largest}')
#         if ord(strToSplit[i]) < smallest:
#             smallest = ord(strToSplit[i])
#         if ord(strToSplit[i]) > largest:
#             largest = ord(strToSplit[i])
#
#         if largest - smallest <= k:
#             s = s + strToSplit[i]
#         else:
#             # print(strToSplit[i])
#             subs.append(s)
#             s = strToSplit[i]
#             smallest = ord(strToSplit[i])
#             largest = ord(strToSplit[i])
#             # print(f'smallest at bottom: {smallest}')
#     if len(s) > 0:
#         subs.append(s)
#     # print(s)
#     # print(subs)
#     return len(subs)
#
#
# print(goodSubstrings(strToSplit, k))

"""
computer memory basics guided
"""

"""
Given a string, implement a function that returns the string with all lowercase
characters.
Example 1:
Input: "LambdaSchool"
Output: "lambdaschool"
Example 2:
Input: "austen"
Output: "austen"
Example 3:
Input: "LLAMA"
Output: "llama"
*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""

string = "LambdaSchool"


def to_lower_case(string):
    result = ''
    for i in range(len(string)):
        if ord(string[i]) <= 90 or ord(string[i]) <= 65:
            result += chr(ord(string[i]) + 32)
        else:
            result += string[i]
    return result


# print(to_lower_case(string))


"""
In order to solve this challenge you will need to [review the rules of Roman
Numerals](https://www.mathsisfun.com/roman-numerals.html).
Given a Roman Numeral (as a string), convert it to an integer. Your input is
guaranteed to be a Roman Numeral value from 1 to 3999.
Example 1:
Input: "IV"
Output: 4
Example 2:
Input: "XII"
Output: 12
Example 3:
Input: "MCMLXXXIV"
Output: 1984
"""

roman = 'IV'
roman = 'XII'
roman = "MCMLXXXIV"


#  TODO finish this!
def roman_to_integer(roman):
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    # get the digits for each letter
    digits = []
    ordered = []
    if len(roman) < 2:
        return numerals.get(roman)
    tally = 0
    for i in range(len(roman)):
        digits.append(numerals.get(roman[i]))
    ordered = sorted(digits, reverse=True)
    # if the numbers are descending just sum them up
    if ordered == digits:
        return sum(digits)
    else:
        i, j = 0, 1
        print(digits)
        for _ in range(len(digits) - 1):
            if digits[i] < digits[j]:
                tally += digits[j] - digits[i]
            else:
                print('i:', digits[i])
                print('j:', digits[j])
                tally += digits[i] + digits[j]
            i += 1
            j += 1
    return tally


# print(roman_to_integer(roman))

"""
Given a list of integers `lst`, any integer with a frequency that is equal to its value is considered a **lucky integer**.
Write a function that returns the lucky integer from the array. If the array contains multiple lucky integers, return the largest one. If there are no lucky integers return -1.
**Example 1**:
Input: arr = [2,3,3,3,4]
Output: 3
**Example 2**:
Input: arr = [1,2,2,3,3,3,4,4,4,4]
Output: 4
**Example 3**:
Input: arr = [1,1,2,2,2]
Output: -1
"""

lst = [2, 2, 3, 3, 3, 4, 4, 4, 4]


#  O(n^2) because counting in the loop...
def find_lucky(lst):
    lucky = []
    for num in lst:
        if num == lst.count(num):
            lucky.append(num)
    if not lucky:
        return -1
    return max(lucky)


# print(find_lucky(lst))

"""
Challenge
Write a logarithmic expression that is identical to this exponential expression:

2^n = 64
log_2 64 = 6

Write an exponential expression that is identical to this logarithmic expression:

log_2 128 = n
2^7 = 128

What keywords should you look out for that might alert you that logarithms are involved?
doubles, halves
"""

"""
Rewrite the implementation of linear search below so that the algorithm searches from the end of the list to the beginning.
"""


def linear_search(arr, target):
    # loop through each item in the input array
    i = len(arr) - 1
    for idx in range(len(arr)):
        # check if the item at the current index is equal to the target
        if arr[i] == target:
            # return the current index as the match
            return i
        i -= 1
    # if we were able to loop through the entire array, the target is not present
    return -1


arr = [1, 2, 3, 4, 5, 6]
target = 3
# print(linear_search(arr, target))


"""
Write a recursive search function that receives as input an array of integers and a target integer value. This function should return True if the target element exists in the array, and False otherwise.
What would be the base case(s) we'd have to consider for implementing this function?
How should our recursive solution converge on our base case(s)?

In your own words, write out the three rules for recursion and how you can identify when a problem is amenable to using a recursive method.
- problem has an obvious base case
- the data changes predictably on the way to the base case 
- the function must call itself
"""


def recursive_search(arr, target):
    if arr[0] == target:
        return True
    elif len(arr[1:]) > 1:
        return recursive_search(arr[1:], target)
    return False


# print(recursive_search(arr, target))


"""
Binary Search
"""


def binary_search(arr, target):
    # 1. Declare min = 0 and max = length of array - 1
    min = 0
    max = len(arr) - 1
    while not max < min:
        # 2. Figure out the guess value by getting the middle integer between min and max
        guess = (max + min) // 2
        # 3. if array[guess] equals the target, we found the element, return the index
        if arr[guess] == target:
            return guess
        # 4. if the guess was too low, reset min to be one more than the guess
        elif arr[guess] < target:
            min = guess + 1
        # 5. if the guess was too high, reset max to be one less than the guess
        else:
            max = guess - 1
    # no match was found
    return -1


# target = 5
# print(binary_search(arr, target))

"""
What is the time complexity of our binary_search function above?
- logN
Can you turn the function above into a recursive function? Any variables tracked/updated in the while loop will have to become parameters for the recursive function.
"""
arr = [1, 2, 3, 4, 5, 6]
target = 55


def binary_recursive_search(arr, target, min_index, max_index):
    if min_index >= max_index:
        return -1
    guess = (max_index + min_index) // 2
    if arr[guess] == target:
        return guess
    elif target < arr[guess]:
        return binary_recursive_search(arr, target, min_index, guess - 1)
    else:
        return binary_recursive_search(arr, target, guess + 1, max_index)

# print(binary_recursive_search(arr, target, 0, len(arr)))

"""
Searching-recursion guided
"""

"""
I was bored one day and decided to look at last names in the phonebook for my
area.
I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.
When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."
Example:
surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]
Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.
*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
def find_rotation_point(surnames):
    # Your code here
    pass

"""
You are a new author that is working on your first book. You are working on a
series of drafts. Each draft is based on the previous draft. The latest draft
of your book has a serious typo. Since each newer draft is based on the
previous draft, all the drafts after the draft containing the typo also include
the typo.
Suppose you have `n` drafts `[1, 2, 3, ..., n]` and you need to find out the
first one containing the typo (which causes all the following drafts to have
the typo as well).
You are given access to an API tool `containsTypo(draft)` that will return
`True` if the draft contains a typo and `False` if it does not.
You need to implement a function that will find the *first draft that contains
a typo*. Also, you have to pay a fee for every call to `containsTypo()`, so
make sure that your solution minimizes the number of API calls.
Example:
Given `n = 5`, and `draft = 4` is the first draft containing a typo.
containsTypo(3) -> False
containsTypo(5) -> True
containsTypo(4) -> True
"""
def firstDraftWithTypo(n):
    # Your code here
    pass

"""
Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a
jar of cookies with `n` cookies inside of it, how many ways could he eat all
`n` cookies in the cookie jar? Implement a function `eating_cookies` that
counts the number of possible ways Cookie Monster can eat all of the cookies in
the jar.
For example, for a jar of cookies with n = 3 (the jar has 3 cookies inside it),
there are 4 possible ways for Cookie Monster to eat all the cookies inside it:
He can eat 1 cookie at a time 3 times
He can eat 1 cookie, then 2 cookies
He can eat 2 cookies, then 1 cookie
He can eat 3 cookies all at once.
Thus, eating_cookies(3) should return an answer of 4.
Can you implement a solution that has a O(n) time complexity and a O(n) space
complexity?
*Note: Since this question is asking you to generate a bunch of possible
permutations, you'll probably want to use recursion for this. Think about base
cases that we would want our recursive function to stop recursing on (when do
you know you've found a "way" to eat the cookies versus when you have not?).*
"""
def eating_cookies(n, cache = None):
    # Your code here
    pass
