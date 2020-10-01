# """
# Example One
# """
# my_list1 = [1, 2, 3, 4, 5, 6]
# my_list2 = my_list1
# # How would you verify that my_list1 and my_list2 have the same identity?
# print(id(my_list1) == id(my_list2))
#
# my_list1.append(7)
# # Check if my_list1 and my_list2 still have the same identity.
# # If they do, why is that?
# print(id(my_list1) == id(my_list2))
#
#
# #
# # """
# Example Two
# """
# my_text1 = "Lambda School"
# my_text2 = my_text1
# # How would you verify that my_text1 and my_text2 have the same identity?
# print(id(my_text2) == id(my_text1))
#
# my_text1 += " is awesome!"
# # Check if my_text1 and my_text2 still have the same identity?
# print(id(my_text2) == id(my_text1))
# # If they do not, why is that?
#
# # Now check if my_text1 and my_text2 have the same value?
# print(my_text1, my_text2)
# # Do they? Explain why or why not.
#
#
#
# """
# Example Three
# """
# # Initialize a list and assign to produce
# produce = ["Apple", "Banana", "Carrot"]
# # Initialize a tuple and include a reference to the produce list in the tuple
# store = ("Bill's Grocery", produce)
# print(id(store))
# # Add a new item to the produce list
# produce.append("Dragonfruit")
# print(id(store))
#
# # Did you notice that the identity of store remained the same?
# # But I thought if you changed a mutable object, a new object would
# # be created in memory? Why did that not occur here?


#  - Constant O(1)	The runtime is entirely unaffected by the input size.
# This is the ideal solution.
#  - Logarithmic O(log n)	As the input size increases, the runtime will grow
#  slightly slower. This is a pretty good solution.
#  - Linear O(n)	As the input size increases, the runtime will grow at the
#  same rate. This is a pretty good solution.
#  - Polynomial O(n^c)	As the input size increases, the runtime will grow at
#  a faster rate. This might work for small inputs but is not a scalable solution.
#  - Exponential O(c^n)	As the input size increases, the runtime will
# grow at a much faster rate. This solution is inefficient.
#  - Factorial O(n!)	As the input size increases, the runtime will grow
#  astronomically, even with relatively small inputs. This solution is exceptionally inefficient.


"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""
def number_of_steps(num):
    steps = 0
    while num > 0:  # loop over each item in the array
        print('while')
        if num % 2 == 0:  # if the number is even
            num = num // 2  # divide the number by 2
            print(num)
        else:
            num = num - 1  # if the number is odd
        steps = steps + 1  # increase the step counter
    return steps

# print( number_of_steps(5000000))
# Logarithmic As the input size increases, the runtime will grow slightly slower. This is a pretty good solution.
# O(log n)

"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""
def sorted_squares(A):
    N = len(A)
    j = 0
    while j < N and A[j] < 0:  # (while j is less than array length) and (A at
        # index j
        # is
        # less than 0)
        j += 1  # increment j
    i = j - 1   # set index to j - 1

    ans = []
    while 0 <= i and j < N:  # (while 0 is less than or equal to index) and (
        # j is less than array length)
        if A[i]**2 < A[j]**2:   # if A at index of i is less than A at index
            # of j
            ans.append(A[i]**2)  # add A at index of i squared to the array
            i -= 1
        else:
            ans.append(A[j]**2)  # else add A at index of j squared to the array
            j += 1

    while i >= 0:  # while i is greater than or equal to 0
        ans.append(A[i]**2)  # add A at index of i squared to the array
        i -= 1
    while j < N:
        ans.append(A[j]**2)  # else add A at index of j squared to the array
        j += 1

    return ans
# print(sorted_squares([10, 2, 3, 4, 5]))
#  O(n^2)

"""
Classify the runtime complexity of the insertion_sort function below using Big O notation.
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# arr = [4,87,2,7,3,]
# insertion_sort(arr)
# print(arr)
# O(n2)


"""
Use Big O notation to classify the space complexity of the function below.
"""


def fibonacci(n):
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i - 2] + lst[i - 1])

    return lst[n - 1]
# O(n)

"""
Use Big O notation to classify the space complexity of the function below.
"""


def fibonacci_two(n):
    x, y, z = 0, 1, None

    if n == 0:
        return x
    if n == 1:
        return y

    for i in range(2, n):
        z = x + y
        x, y = y, z

    return z
# O(1)

"""
Use Big O notation to classify the space complexity of the function below.
"""


def do_something(n):
    lst = []
    for i in range(n):
        for j in range(n):
            lst.append(i + j)

    return lst
# O(n^2)


# numbers = [2, 0, 0, 0]
#
#
# def removeEvens(numbers):
#     return [num for num in numbers if num % 2 != 0]
#     # below code didn't pass tests above did
#     # for num in numbers:
#     #     if num % 2 == 0 and num != 0:
#     #         numbers.remove(num)
#     # return numbers
#
#
# print(removeEvens(numbers))
#
# import statistics
#
# sequence = [-1, 3, -2, 2]
#
# def arrayMedian(sequence):
#     return statistics.median(sequence)
#
# print(arrayMedian(sequence))

s = "TuVwXYZ"

# s = "ABCDEFFDEfghCBA"

# def originalIncreasingSubstrings(s):
#     string = ''
#     subs = []
#     print(''.join(sorted(s)))
#     i = 0
#     for i in range(len(s) - 1):
#         string = string + s[i]
#         if s[i + 1] <= s[i]:
#             subs.append(string)
#             string = ''
#             continue
#     subs.append(s[len(s) - 1])
#     i += 1
#     return subs

# s = "TuVwXYZ"

# s = "ABCDEFFDEfghCBA"
s = "f"


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


print(increasingSubstrings(s))
