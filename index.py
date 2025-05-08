# def plusMinus(arr):
#     n = len(arr)
#     smaller = 0
#     greater = 0
#     zero = 0
#     for num in arr:
#         if num < 0:
#             smaller += 1
#         elif num > 0:
#             greater += 1
#         else:
#             zero += 1

#     ratios_1 = smaller / n
#     ratios_2 = greater / n
#     ratios_3 = zero / n
#     print("{:.6f}".format(ratios_1))
#     print("{:.6f}".format(ratios_2))
#     print("{:.6f}".format(ratios_3))


# plusMinus([1, 1, 0, -1, -1])


##############################################


# def miniMaxSum(arr):

#     arr.sort()
#     min = sum(arr[0:4])
#     max = sum(arr[1:5])
#     print(min, max)


# miniMaxSum([1, 2, 3, 4, 5])


##############################################

# def timeConversion(s):
#     print(s)
#     period = s[-2:]
#     hour = int(s[:2])
#     rest = s[2:-2]

#     if period == "AM":
#         if hour == 12:
#             hour = 0
#     else:
#         if hour != 12:
#             hour += 12
#     print({f"{hour:02d}{rest}"})
#     return f"{hour:02d}{rest}"


# timeConversion("07:05:45PM")
# timeConversion("12:05:45AM")
########################################################

# import math

# def findMedian(arr):

#     arr.sort()
#     num = math.floor(len(arr) / 2)
#     mid = arr[num]
#     print(len(arr))
#     print(mid)


# findMedian([0, 1, 2, 3, 4, 5, 6])
############################################

# from collections import Counter


# def lonelyinteger(a):

#     lonely = list(filter(lambda x: a.count(x) == 1, a))
#     print(lonely[0])


# lonelyinteger([1, 2, 3, 4, 3, 2, 1])

############################################

# def diagonalDifference(arr):
#     n = len(arr)
#     primary_diagonal = 0
#     secondary_diagonal = 0
#     print(n)
#     for i in range(n):
#         primary_diagonal += arr[i][i]
#         secondary_diagonal += arr[i][n - 1 - i]
#     print(abs(primary_diagonal - secondary_diagonal))
#     return abs(primary_diagonal - secondary_diagonal)


# matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# diagonalDifference(matrix)
# # 11 5 -12
# # 4  5  10

######################################


# def countingSort(arr):
#     frequency = [0] * 100
#     for num in arr:
#         frequency[num] += 1
#         print(frequency)
#     return frequency


# arr_list = [
#     63,
#     25,
#     73,
#     1,
#     98,
#     73,
#     56,
#     84,
#     86,
#     57,
#     16,
#     83,
#     8,
#     25,
#     81,
#     56,
#     9,
#     53,
#     98,
#     67,
#     99,
#     12,
#     83,
#     89,
#     80,
#     91,
#     39,
#     86,
#     76,
#     85,
#     74,
#     39,
#     25,
#     90,
#     59,
#     10,
#     94,
#     32,
#     44,
#     3,
#     89,
#     30,
#     27,
#     79,
#     46,
#     96,
#     27,
#     32,
#     18,
#     21,
#     92,
#     69,
#     81,
#     40,
#     40,
#     34,
#     68,
#     78,
#     24,
#     87,
#     42,
#     69,
#     23,
#     41,
#     78,
#     22,
#     6,
#     90,
#     99,
#     89,
#     50,
#     30,
#     20,
#     1,
#     43,
#     3,
#     70,
#     95,
#     33,
#     46,
#     44,
#     9,
#     69,
#     48,
#     33,
#     60,
#     65,
#     16,
#     82,
#     67,
#     61,
#     32,
#     21,
#     79,
#     75,
#     75,
#     13,
#     87,
#     70,
#     33,
# ]


# countingSort(arr_list)
#########################################


# def findZigZagSequence(a, n):
#     a.sort()
#     mid = (n - 1) // 2
#     a[mid], a[n - 1] = a[n - 1], a[mid]

#     st = mid + 1
#     ed = n - 2
#     while st <= ed:
#         a[st], a[ed] = a[ed], a[st]
#         st = st + 1
#         ed = ed - 1
#     print(a)
#     for i in range(n):
#         if i == n - 1:
#             print(a[i])
#         else:
#             print(a[i], end="Hii ")


# findZigZagSequence([2, 3, 5, 1, 4, 7, 6], 7)

###############################################################
# n = towers
# m = hight of tower


# def towerBreakers(n, m):
#     print(n, m)
#     if m == 1:
#         return 2
#     elif n % 2 == 0:
#         return 2
#     else:
#         return 1


# # Read input from user or file
# t = int(input())  # Number of test cases
# for _ in range(t):
#     n, m = map(int, input().split())
#     print(towerBreakers(n, m))

# towerBreakers(2, 4)


###################################################

# def caesarCipher(s: str, k: int) -> str:
#     result = []
#     for char in s:
#         if char.isalpha():
#             base = ord("A") if char.isupper() else ord("a")

#             shifted = chr((ord(char) - base + k) % 26 + base)
#             result.append(shifted)
#         else:
#             result.append(char)
#         encry = "".join(result)

#     return encry


# caesarCipher("Ahmed Elarosi", 3)


############################################
# def fizzBuzz(n):
#     for i in range(1, n + 1):
#         if i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)


# fizzBuzz(45)


###############################################
# def minTime(files, numCores, limit):

#     total_time = 0
#     parallel_gain = []

#     for file in files:
#         if file % numCores == 0:
#             gain = file - (file // numCores)
#             print(gain)
#             parallel_gain.append((gain, file))
#             print(parallel_gain)

#         else:
#             total_time += file

#     parallel_gain.sort(reverse=True)

#     for i, (_, file) in enumerate(parallel_gain):
#         if i < limit:
#             total_time += file // numCores
#         else:
#             total_time += file
#     print(total_time)
#     return total_time


# files = [4, 1, 3, 2, 8]
# numCores = 4
# limit = 1
# minTime(files, numCores, limit)

###############################################


# def ordered_configuration(configuration: str):
#     parts = configuration.split("|")
#     seen_indices = set()
#     seen_values = set()
#     configs = []

#     for part in parts:
#         # Validate length
#         if len(part) != 14:
#             print(part)
#             return ["Invalid configuration_1"]

#         index = part[:4]
#         value = part[4:]

#         # Validate index
#         if not index.isdigit() or index == "0000":
#             return ["Invalid configuration_2"]

#         # Validate value: alphanumeric, 10 characters
#         if not value.isalnum() or len(value) != 10:
#             return ["Invalid configuration_3"]

#         # Uniqueness checks
#         if index in seen_indices or value in seen_values:
#             return ["Invalid configuration_4"]

#         seen_indices.add(index)
#         seen_values.add(value)
#         configs.append((int(index), value))

#     # Check for sequential indices starting from 1
#     indices = sorted([i for i, _ in configs])
#     if indices != list(range(1, len(parts) + 1)):
#         return ["Invalid configuration_5"]

#     # Return values ordered by index
#     return [value for _, value in sorted(configs)]


# configuration = "0002ffc22e7904|0001a3ad4214|000305d29f4a4b"
# print(ordered_configuration(configuration))


# import json
# import re


# def evaluate_deployments(deployments):
#     success_count = 0
#     fail_count = 0
#     error_count = 0

#     for deployment_str in deployments:
#         try:
#             # Parse JSON string
#             deployment = json.loads(deployment_str)

#             # Check required fields exist
#             if "deployment_id" not in deployment
#                   or "status" not in deployment:
#                 error_count += 1
#                 continue

#             # Validate deployment_id format
#             deployment_id = deployment["deployment_id"]
#             if not (
#                 isinstance(deployment_id, str)
#                 or not re.fullmatch(r"^d-[a-z0-9]{10}$", deployment_id)
#             ):
#                 error_count += 1
#                 continue

#             # Validate status
#             status = deployment["status"]
#             if status == "Success":
#                 success_count += 1
#             elif status == "Fail":
#                 fail_count += 1
#             else:
#                 error_count += 1

#         except json.JSONDecodeError:
#             error_count += 1

#     return [success_count, fail_count, error_count]


# print(
#     evaluate_deployments(
#         {"deployment_id": "d.12345678ac", "status": "ABCC"},
#     )
# )


# def gridChallenge(grid):
#     sorted_grid = ["".join(sorted(row.lower())) for row in grid]
#     print(sorted_grid)

#     n = len(sorted_grid)
#     m = len(sorted_grid[0])

#     for col in range(m):
#         print("C", col)
#         for row in range(n - 1):
#             print("R", row)
#             if sorted_grid[row][col] > sorted_grid[row + 1][col]:
#                 return "NO"

#     return "YES"


# grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
# print(gridChallenge(grid))


# def superDigit(n, k):
#     initial_digits = sum(int(digit) for digit in n) * k

#     def recursive_digit(x):
#         if x < 10:
#             return x
#         final_digit = recursive_digit(sum(int(d) for d in str(x)))
#         return final_digit

#     return recursive_digit(initial_digits)


# n = "9875"
# k = 4
# print(superDigit(n, k))


# def minimumBribes(q):
#     total_bribes = 0

#     for current_pos, person in enumerate(q):
#         original_pos = person - 1
#         if original_pos - current_pos > 2:
#             print("Too chaotic")
#             return
#         for j in range(max(0, original_pos - 1), current_pos):
#             print(q[j], person)
#             if q[j] > person:
#                 total_bribes += 1
#     print(total_bribes)


# q = [1, 2, 5, 3, 7, 8, 6, 4]
# qq = [1, 2, 5, 7, 3, 8, 6, 4]

# minimumBribes(q)
# # print(60 * "-")
# # print(minimumBribes(qq))


# counter = 0
# while counter < 5:
#     print("Counter:", counter)
#     counter += 1


# fruits = ["apple", "banana", "cherry", "Water"]
# # print(fruits[:4])
# fruits.append("kiwi")
# print(fruits)
# fruits.remove(fruits[3])
# print(fruits)
# fruits.insert(3, "Ahmed")
# print(fruits)
# fruits.extend("Hamdi")
# print(fruits)
# fruits.pop()
# print(fruits)
# del fruits[5:]
# print(fruits)

# coordinates = (10, 20)
# print(coordinates[0])

# person = {"name": "John", "age": 30, "city": "New York"}
# print(person["age"])
# person["age"] = 31
# print(person)
# del person["city"]
# print(person)
# person.pop("name")
# print(person)

# numbers = {1, 2, 3, 3, 4}

# print(numbers)
# numbers.add(5)
# print(numbers)
# numbers.remove(2)
# print(numbers)

# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# print(set_a | set_b)  # Union: {1, 2, 3, 4, 5}
# print(set_a & set_b)  # Intersection: {3}
# print(set_a - set_b)  # Difference: {1, 2}
# print(set_b - set_a)

counter = 0


# def increment():
#     global counter
#     counter += 1


# increment()
# print(counter)


# add = lambda a, b, c: a + b * c

# print(add(2, 2, 3))


# numbers = [1, 2, 3, 4, 4]
# squared = list(map(lambda x: x**3, numbers))
# print(squared)
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# from functools import reduce

# product = reduce(lambda x, y: x * y, numbers)

# print(product)
