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


# Dutch National Flag Problem:
# Input: arr[] = {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}
# Explanation: {0, 0, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.


# Input: arr[] = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
# Explanation: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.

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
