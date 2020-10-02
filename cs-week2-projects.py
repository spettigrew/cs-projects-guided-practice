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
# def number_of_steps(num):
#     steps = 0
#     while num > 0:  # loop over each item in the array
#         print('while')
#         if num % 2 == 0:  # if the number is even
#             num = num // 2  # divide the number by 2
#             print(num)
#         else:
#             num = num - 1  # if the number is odd
#         steps = steps + 1  # increase the step counter
#     return steps
#
# # print( number_of_steps(5000000))
# # Logarithmic As the input size increases, the runtime will grow slightly slower. This is a pretty good solution.
# # O(log n)
#
# """
# Classify the runtime complexity of the sorted_squares function below using Big O notation.
# """
# def sorted_squares(A):
#     N = len(A)
#     j = 0
#     while j < N and A[j] < 0:  # (while j is less than array length) and (A at
#         # index j
#         # is
#         # less than 0)
#         j += 1  # increment j
#     i = j - 1   # set index to j - 1
#
#     ans = []
#     while 0 <= i and j < N:  # (while 0 is less than or equal to index) and (
#         # j is less than array length)
#         if A[i]**2 < A[j]**2:   # if A at index of i is less than A at index
#             # of j
#             ans.append(A[i]**2)  # add A at index of i squared to the array
#             i -= 1
#         else:
#             ans.append(A[j]**2)  # else add A at index of j squared to the array
#             j += 1
#
#     while i >= 0:  # while i is greater than or equal to 0
#         ans.append(A[i]**2)  # add A at index of i squared to the array
#         i -= 1
#     while j < N:
#         ans.append(A[j]**2)  # else add A at index of j squared to the array
#         j += 1
#
#     return ans
# # print(sorted_squares([10, 2, 3, 4, 5]))
# #  O(n^2)
#
# """
# Classify the runtime complexity of the insertion_sort function below using Big O notation.
# """
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
#
# # arr = [4,87,2,7,3,]
# # insertion_sort(arr)
# # print(arr)
# # O(n2)
#
#
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
# # def removeEvens(numbers):
# #     return [num for num in numbers if num % 2 != 0]
# #     # below code didn't pass tests above did
# #     # for num in numbers:
# #     #     if num % 2 == 0 and num != 0:
# #     #         numbers.remove(num)
# #     # return numbers
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
def increasingSubstrings(s):
    string = ''
    subs = []
    i = 0
    if len(s) == 1:
        subs.append(s[0])
    else:
        for i in range(len(s) - 1):
            # print(s[i])
            if not string.startswith(s[i]):
                string = string + s[i]
            if ord(s[i]) != ord(s[i + 1]) - 1:
                # print(ord(s[i]))
                subs.append(string)
                string = s[i + 1]
                continue
        # print(f'-1: {ord(s[len(s) - 1])}, -2: {ord(s[len(s) - 2])}')
        if ord(s[len(s) - 1]) == ord(s[len(s) - 2]) + 1:
            string = string + s[len(s) - 1]
        subs.append(string)
        string = ''
    return subs


# strToSplit = "aaabaaabb"
# k = 0
# strToSplit = "aaabaaabb"
# k = 1
strToSplit = "aaabzaaabb"
k = 5
def goodSubstrings(strToSplit, k):
    smallest = ord(strToSplit[0])
    largest = 0
    subs = []
    s = ''
    for i in range(len(strToSplit)):
        # print('Letter', strToSplit[i],
        #       ord(strToSplit[i]))
        # print(f'smallest: {smallest} largest: {largest}')
        if ord(strToSplit[i]) < smallest:
            smallest = ord(strToSplit[i])
        if ord(strToSplit[i]) > largest:
            largest = ord(strToSplit[i])

        if largest - smallest <= k:
            s = s + strToSplit[i]
        else:
            # print(strToSplit[i])
            subs.append(s)
            s = strToSplit[i]
            smallest = ord(strToSplit[i])
            largest = ord(strToSplit[i])
            # print(f'smallest at bottom: {smallest}')
    if len(s) > 0:
        subs.append(s)
    # print(s)
    # print(subs)
    return len(subs)


print(goodSubstrings(strToSplit, k))
