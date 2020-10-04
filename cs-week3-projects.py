# slicing

# my_list[start_index:end_index]
# my_list[:]  # This would be all of the items in my_list
# my_list[:5] # This would be the items from index 0 to 4
# my_list[5:] # This would be the items from index 5 to the end of the list


"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.
The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.
If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.
Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.
Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""

nums = [1, 7, 3, 6, 5, 6]
# nums = [1,2,3]


def pivot_index(nums):
    # iterate array starting at index 1
    # get sum of items on left of i and compare to sum of items on right of i
    # if they are equal return i else keep going to the next i
    for i in range(len(nums)):
        left = sum(nums[:i])
        right = sum(nums[i + 1:])
        if left == right:
            return i
    return -1

# print(pivot_index(nums))

"""
You are given a non-empty array that represents the digits of a non-negative integer.
Write a function that increments the number by 1.
The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.
You will not receive a leading 0 in your input array (except for the number 0 itself).
Example 1:
Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.
Example 2:
Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.
Example 3:
Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""


def plus_one(digits):
    # turn the numbers in the array into an integer
    # The repr() function returns a printable representation of the given object.
    numbers = (''.join(repr(int(n)) for n in digits))
    print(int(numbers) + 1)


print(plus_one([9,9,9]))
