

# Create an algorithm that takes two lists of integers, and returns a list of integers that are in both lists.
def common_elements(list1, list2):
    com_els = []
    for i in list1:
        if i in list2:
            com_els.append(i)
    return com_els

print(common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))

# Create an algorithm that takes in a list of integers, and returns a hash with the number of times each integer appears in the list.
def count_elements(list1):
    count = {}
    for i in list1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

print(count_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Test Commit

def fibArr(n):
    arr = [0,1]
    for i in range(1, n):
        arr.append(arr[i-1] + arr[i])
    return arr

print(fibArr(5))

def primeNum(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(primeNum(999983))



def primeRec(n, i=2, level=0):
    # breakpoint()
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return primeRec(n, i+1, level+1)

# print(primeRec(999983))

