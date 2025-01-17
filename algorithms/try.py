
def max_team_size(arr):
    arr.sort() # sort the array
    max_team_size = 1 # initialize the max team size
    current_team_size = 1 # initialize the current team size

    for i in range(1, len(arr)): # iterate through the array
        if arr[i] - arr[i - 1] <= 1:
            current_team_size += 1
        else:
            max_team_size = max(max_team_size, current_team_size)
            current_team_size = 1

    max_team_size = max(max_team_size, current_team_size)
    return max_team_size

print(max_team_size([10, 12, 13, 9, 14]))


def count_names_with_prefixes(names, prefixes):
    result = []
    for prefix in prefixes:
        count = 0
        for name in names:
            if name.startswith(prefix) and name != prefix:
                count += 1
        result.append(count)
    return result
print(count_names_with_prefixes(['steve', 'stevens', 'danny', 'steves', 'dan', 'john', 'johnny', 'joe', 'alex', 'alexander'], ['steve', 'alex', 'joe', 'john', 'dan']))
