# Count Subarrays having Sum K
# Given an unsorted array of integers, the task is to find the number of subarrays having a sum exactly equal to a given number k.


# Input : arr[] = [10, 2, -2, -20, 10], k = -10
# Output : 3
# Explanation: Subarrays: arr[0…3], arr[1…4], arr[3…4] have sum equal to -10.

def countSubs(arr, k):
    preSums = {}
    countSubs = 0
    currSum = 0

    for val in arr:
        currSum += val
        if currSum == k:
            res += 1
        if currSum - k in preSums:
            res += preSums[currSum - k]

        preSums[currSum] = 1 + preSums.get(currSum, 0)
    return res
