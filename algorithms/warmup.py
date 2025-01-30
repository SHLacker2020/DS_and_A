# FizzBuzz: Write a function that prints the numbers from 1 to 100.
# But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz".
# For numbers which are multiples of both three and five, print "FizzBuzz".
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print(fizz_buzz(25))


# Example of using a hashmap in Python
# Write a function that checks if an array has two numbers that add up to a target number
def two_sum(arr, target):
    hashMap = {}
    for i in range(len(arr)):
        compare = target - arr[i]
        if compare in hashMap:
            return [hashMap[compare], i]
        hashMap[arr[i]] = i

print(two_sum([2,7,11,15], 22))
# output: [1, 3]


# Merge two arrays in Python
def merge_two_arrays(arr1, arr2):
    arr1 = arr2
    return arr1
print(merge_two_arrays([1,2,3], [4,5,6]))

def merge(nums1, m, nums2, n):
    nums1[m:] = nums2 # This is a way to merge two lists in Python
    nums1.sort()

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))


# Example of using .extend in Python
def extend_example():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)
    print(list1)

extend_example()

# Create a hashmap that counts the number of times an element appears in an array
def my_hash(arr):
    hashmap = {}
    for i in arr:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    return hashmap

print(my_hash([1,1,2,3,4,4,4,5,5,6,7,7,8,9,10]))

# Create a hashmap that counts the number of times a character appears in a string
def my_hash_string(s):
    hashmap = {}
    for i in s.lower().replace(" ", ""):
        hashmap[i] = hashmap.get(i, 0) + 1
    return hashmap

print(my_hash_string("Hhello  World"))

# isPalindrome: Given a int, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


print(is_palindrome(121))


# iterate through a list of strings and group them by their length in sublists
def group_by_length(strings):
    length_map = {}
    for string in strings:
        length = len(string)
        if length in length_map:
            length_map[length].append(string)
        else:
            length_map[length] = [string]
    return list(length_map.values())

print(group_by_length(["a", "bb", "ccc", "dd", "eee", "ffff"]))


def isAnagram(s, t):
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))


def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return list(anagrams.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))


def dutchFlagProb(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
