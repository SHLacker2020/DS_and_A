

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
