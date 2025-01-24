# Count Subarrays having Sum K
# Given an unsorted array of integers, the task is to find the number of subarrays having a sum exactly equal to a
# given number k.
# Input : arr[] = [10, 2, -2, -20, 10], k = -10
# Output : 3
# Explanation: Subarrays: arr[0…3], arr[1…4], arr[3…4] have sum equal to -10.
# Sudocode: 1. Create a hashmap to store the prefix sum and the number of times it has occurred.
# 2. Initialize the prefix sum to 0 and the count of subarrays to 0.
# 3. Iterate through the array and calculate the prefix sum.
# 4. If the prefix sum is equal to k, increment the count of subarrays.
# 5. If the prefix sum - k is in the hashmap, increment the count of subarrays by the value of the prefix sum - k in the hashmap.
def countSubs(arr, k):
    hashMap = {}
    prefix_sum = 0
    count = 0
    for n in arr:
        prefix_sum += n
        if prefix_sum == k:
            count += 1
        if prefix_sum - k in hashMap:
            count += hashMap[prefix_sum - k]
        hashMap[prefix_sum] = 1 + hashMap.get(prefix_sum, 0)
    return hashMap
print(countSubs([10, 2, -2, -20, 10], k = -10))



# Dutch National Flag Problem:
# Input: arr[] = {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}
# Explanation: {0, 0, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.
# Input: arr[] = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
# Explanation: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.
# Sudo: 1. Create variables for low, mid, and high.
# 2. Iterate through the array and check the value at the mid index.
# 3. If the value is 0, swap the value at the low index with the value at the mid index and increment the low and mid index.
# 4. If the value is 1, increment the mid index.
# 5. If the value is 2, swap the value at the mid index with the value at the high index and decrement the high index.
# 6. Continue until the mid index is less than or equal to the high index.
# 7. Return the sorted array.
def dutchFlagProb(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        if arr[mid] == 1:
            mid += 1
        if arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
        return arr
print(dutchFlagProb([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]



# Write a program to find the factorial of a number, a factorial of a number is
# the product of all the integers from 1 to that number.
# Sudo: 1. Create a function that takes a number as input.
# Base case: If the number is 0, return 1.
# Recursive case: Return the number multiplied by the factorial of the number - 1.
def factorial(n, level = 0):
    # breakpoint()
    if n == 0:
        return 1
    return n * factorial(n - 1, level + 1)
print(factorial(5))
# Output: 120



# Write a program to find the nth Fibonacci number, the fibonacci sequence is a
# series of numbers in which each number is the sum of the two preceding ones.
# Sudo: 1. Create a function that takes a number as input.
# Base case: If the number is 0, return 0.
# If the number is 1, return 1.
# Recursive case: Return the sum of the fibonacci number of n - 1 and n - 2.
def fibonacci(n):
    # breakpoint()
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(18))
# Output: 2584

# Now write a program to make an array of the first n Fibonacci numbers.
# Sudo: 1. Create a function that takes a number as input.
# 2. Create an empty array to store the fibonacci numbers.
# 3. Iterate from 0 to n and append the fibonacci number of i to the array.
# 4. Return the array.
def fibonacciArray(n):
    fibArray = []
    for i in range(n):
        fibArray.append(fibonacci(i))
    return fibArray
# Recursive way
def fibonacciArrayRec(n, level = 0):
    # breakpoint()
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    fibArray = fibonacciArrayRec(n - 1, level + 1)
    fibArray.append(fibArray[-1] + fibArray[-2])
    return fibArray

# Write a program to find the HCF or Highest Common Factor of two numbers
# Example:
# Input: 70, 15
# Output: 5
# Sudo: 1. Create a function that takes two numbers as input.
# 2. Find the smaller of the two numbers.
# 3. Iterate from 1 to the smaller number.
# 4. If both numbers are divisible by the current number, store the number as the HCF.
# 5. Return the HCF.
def hcf(a, b):
    smaller = min(a, b)
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf

# Now with recursion
def hcfRec(a, b, level = 0):
    # breakpoint()
    if b == 0:
        return a
    return hcfRec(b, a % b, level + 1)

print(hcfRec(70, 15))



# Write a program to reverse the digits of a number.
def reverseNumber(n):
    return int(str(n)[::-1])

# Write a program to check if a number is a palindrome.
def isPalindrome(n):
    return n == reverseNumber(n)

# Write a program to check if a number is a prime number.
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# Recursive way
def isPrimeRec(n, i = 2):
    # breakpoint()
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return isPrimeRec(n, i + 1)

# Write a program to find the sum of digits of a number.
def sumOfDigits(n):
    for i in str(n):
        n += int(i)
    return n

# Find the LCM(Least Common Multiple) of two numbers. The LCM of two numbers is the smallest number that is a multiple of both numbers.
def lcm(a, b):
    smaller = min(a, b)
    while True:
        if smaller % a == 0 and smaller % b == 0:
            return smaller
        smaller += 1
print(lcm(4, 6))
# Output: 12

