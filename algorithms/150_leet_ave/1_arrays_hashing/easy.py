from typing import List

# Easy Array Hashing Problems

class ContainsDuplicateSolution:
    def contains_dup(self, nums: List[int]) -> bool:
        """ Time: O(n)
            Space: O(n)

        Args:
            nums (List[int]): List to check

        Returns:
            bool: True if nums contains duplicate
        """
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False

    def contains_duplicate(self, nums):
        for i in nums:
            return False if nums[i]

print(ContainsDuplicateSolution().contains_dup([1,2,3,3,4,5])) # True
print(ContainsDuplicateSolution().contains_dup([1,2,3,4,5])) # False
print()


class AnagramSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s, hash_t = {}, {}
        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        return hash_s == hash_t

print(AnagramSolution().isAnagram("anagram", "nagaram")) # True
print(AnagramSolution().isAnagram("anagram", "Hello")) # False
print()

