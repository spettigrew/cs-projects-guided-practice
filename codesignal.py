"""
Code Signal Interview Path
"""

"""
Arrays
"""

"""
*** First Duplicate ***
-----------------------
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be firstDuplicate(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.
"""

arr = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
# O(n^2) solution
# def firstDuplicate(a):
#     # keep track of matched index
#     matched = []
#     if len(a) < 2:
#         return -1
#     # iterate the list checking for duplicates of current number
#     for i, value in enumerate(a):
#         for j, val in enumerate(a):
#             if matched and matched[0] < i:
#                 continue
#             if j == i:
#                 continue
#             # if duplicate
#             if value == val:
#                 # if matched is empty just add the matched index
#                 if not matched:
#                     matched.append(j)
#                 # else check if theres a match with a larger index
#                 else:
#                     if matched[0] > j:
#                         # print('matched', matched, 'a', a[i])
#                         # if so replace it with the smaller index
#                         matched[0] = j
#     # if no matches return -1
#     if not matched:
#         return -1
#     else:
#         # there is a smallest match index return the value at that index
#         return a[matched[0]]
#
#
# print(firstDuplicate(arr))

arr = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]


# O(n) solution
def firstDuplicate(a):
    # define a set to hold non duplicate numbers
    nums = set()
    for i in range(len(a)):
        # if we hit a number that's duplicate (exists in the set) return it
        if a[i] in nums:
            return a[i]
        else:
            # else if its not duplicate add it to the set
            nums.add(a[i])
    # return -1 if no duplicates
    return -1


# print(firstDuplicate(arr))


"""
*** First not repeating character ***
-------------------------------------
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.
"""

s = "abacabad"


def firstNotRepeatingCharacter(s):
    for i in range(len(s)):
        if s[i] not in s[i + 1:] and s[i] not in s[:i]:
            return s[i]

    return '_'


# print(firstNotRepeatingCharacter(s))

"""
*** Rotate image ***
--------------------
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
"""

a = [[1, 2, 3],  # 1 -> [0 : len - 1] 2 -> [1 : len - 1] 3 -> [2 : len -1]
     [4, 5, 6],  # 4 -> [0 : len - 2] 2 -> [1 : len - 2] 6 [2 : len -2]
     [7, 8, 9]]  # 7 -> [0 : len - 3] 8 -> [1 : len - 3] 9 -> [2 : len -3]


# def rotateImage(a):
#     length = len(a[0])
#     for i in range(length // 2):
#         for j in range(i, length - i -1):
#             holder = a[i][j]
#             a[i][j] = a[length - 1 - j][i]
#             a[length - 1 - j][i] = a[length - 1 - i][length - 1 - j]
#             a[length - 1 - i][length - 1 - j] = a[j][length - 1 - i]
#             a[j][length - 1 - i] = holder
#
#     return a

# with zip
# def rotateImage(a):
#     return list(zip(*reversed(a)))

# with comprehension
def rotateImage(a):
    return [[x[i] for x in a][::-1] for i in range(len(a))]


# print(rotateImage(a))

"""
*** Sudoku 2 ***
----------------
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;

For

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.

The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.
"""

grid = [[".", "4", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "4", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "1", ".", ".", "7", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "3", ".", ".", ".", "6", "."],
        [".", ".", ".", ".", ".", "6", ".", "9", "."],
        [".", ".", ".", ".", "1", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "8", ".", ".", ".", ".", "."]]

# my solution
# def sudoku2(grid):
#     # check if any inner array contains duplicate numbers
#     # if so return false
#
#     def check_horizontal(grid):
#         for arr in grid:
#             for i in range(len(arr)):
#                 if arr[i] != '.' and arr[i] in arr[i + 1:]:
#                     return False
#         return True
#
#     def check_vertical(grid):
#         col = 0
#
#         while col < len(grid[0]):
#             temp_arr = []
#             for arr in grid:
#                 temp_arr.append(arr[col])
#             for i in range(len(temp_arr)):
#                 if temp_arr[i] != '.' and temp_arr[i] in temp_arr[i + 1:]:
#                     return False
#             col += 1
#         return True
#
#     def check_subgrid(grid, row, col):
#         print('row:', row)
#         print('col:', col)
#
#         row = row
#         # col = col
#         step = 0
#
#         subgrid = []
#         while step < len(grid[0]):
#
#             print('step:', step)
#             colu = col
#             temp_subgrid = []
#
#             for i in range(3):
#                 temp_subgrid.append(grid[row][colu])
#                 colu += 1
#             subgrid.extend(temp_subgrid)
#             if len(subgrid) == 9:
#                 for i in range(len(subgrid)):
#                     if subgrid[i] != '.' and subgrid[i] in subgrid[i + 1:]:
#                         return False
#
#             if step == 8:
#                 row = 0
#                 col = 0
#                 subgrid = []
#             row += 1
#             # col += 1
#             step += 3
#         return True
#
#     if not check_horizontal(grid):
#         return False
#     if not check_vertical(grid):
#         return False
#
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             print('***********')
#             sub = check_subgrid(grid, i, j)
#             if not sub:
#                 return False
#     return True

# most voted on codesignal
def check_unique(nums):
    s = set()
    for num in nums:
        if num == '.':
            continue

        if num in s:
            return False
        s.add(num)
    return True


def sudoku2(grid):
    for line in grid:
        if not check_unique(line):
            return False

    for i in range(9):
        if not check_unique([line[i] for line in grid]):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_unique(
                    grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][
                                                              j:j + 3]):
                return False

    return True


# print(sudoku2(grid))


"""
*** is crypt solution ***
-------------------------
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.

Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

Example

For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be
isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
the output should be
isCryptSolution(crypt, solution) = false.

Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that this is not a valid solution.
"""

crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

def isCryptSolution(crypt, solution):
    pass

print(isCryptSolution(crypt, solution))
