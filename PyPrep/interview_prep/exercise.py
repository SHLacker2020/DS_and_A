# Exercises

# Map by name
# Write a function that takes in an array of hashes and returns a new array
# containing the "name" of each hash.

def map_by_name(arr) -> list[str]:
    """
    Given an array of hashes, return a new array containing the "name" of each hash.
    """
    # Create an array to store the names
    names = []
    for i in range(len(arr)):
        names.append(arr[i]["name"])
    return names

pets = [
    {"type": "dog", "name": "Rolo"},
    {"type": "cat", "name": "Sunny"},
    {"type": "rat", "name": "Saki"},
    {"type": "dog", "name": "Finn"}
]
friends = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
print(map_by_name(pets))  # ['Rolo', 'Sunny', 'Saki', 'Finn']
print(map_by_name(friends))  # ['Alice', 'Bob', 'Charlie']

