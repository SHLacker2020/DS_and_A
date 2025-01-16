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

# Example of a nested loop in Python
def nested_loop_example(nums):
    for i in nums:
        for j in nums:
            print(f"i: {i}, j: {j}")
            print(f"index i: {nums.index(i)}, index j: {nums.index(j)}")

nested_loop_example([66,67,68])
print(len([1,2,3,4,5]))

def two_sum(arr, targ):
    hashmap = {}
    for i in range(len(arr)):
        comp = targ - arr[i]
        if comp in hashmap:
            return [i, hashmap[comp]]
        hashmap[arr[i]] = i
