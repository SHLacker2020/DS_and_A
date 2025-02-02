
# DICTIONARY
# A dictionary is a collection which is unordered, changeable and indexed.
# No duplicate members.
hash = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(hash) # {"brand": "Ford", "model": "Mustang", "year": 1964}
print(hash["model"]) # Mustang
print(hash.get("model")) # Mustang
hash["year"] = 2018
print(hash) # {"brand": "Ford", "model": "Mustang", "year": 2018}
for x in hash:
    print(x) # brand model year
for x in hash:
    print(hash[x]) # Ford Mustang 2018
print(hash.values())
for x, y in hash.items():
    print(x, y) # brand Ford model Mustang year 2018
if "model" in hash:
    print("Yes, 'model' is one of the keys in the hash dictionary") # Yes, 'model' is one of the keys in the hash dictionary
print(len(hash)) # 3
hash["color"] = "red"
print(hash) # {"brand": "Ford", "model": "Mustang", "year": 2018, "color": "red"}
hash.pop("model")
print(hash) # {"brand": "Ford", "year": 2018, "color": "red"}
hash.popitem()
print(hash) # {"brand": "Ford", "year": 2018}
hash.clear()
print(hash) # {}
print()


# How to turn a sequence data type into a hash_counter as efficiently as possible

# Sequence data:
arr = ["String", "String", 1, 2, 3, 3, 2, 1, 3, 55, "Different String",]

# Create an empty hash:
hash = {}

# Iterate through the sequence data:
for el in arr:
    # Since we can't make the default value 0 and use += 1 like Ruby, we must be
    # much more explicit.
    hash[el] = 1 + hash.get(el, 0)
    # This says that we want to set the value with the key hash[el]
    # to be 1 + whatever the current value is, AND if there is no current value
    # yet, than set it to 0.
print(hash)

def longest_bitonic_subarray(arr):
    n = len(arr)
    if n == 0:
        return 0

    bitonic_subarrays = {}
    start = 0

    while start < n:
        end = start
        while end + 1 < n and arr[end] < arr[end + 1]:
            end += 1
        peak = end
        while end + 1 < n and arr[end] > arr[end + 1]:
            end += 1
        if start != end:
            bitonic_subarrays[(start, end)] = arr[start:end + 1]
        start = max(start + 1, end)

    longest_subarray = max(bitonic_subarrays.values(), key=len, default=[])
    return len(longest_subarray)

# Example usage:
print(longest_bitonic_subarray([1, 2, 3, 4, 5, 3, 1]))  # Output: 7
print(longest_bitonic_subarray([1, 11, 2, 10, 4, 5, 2, 1]))  # Output: 6
