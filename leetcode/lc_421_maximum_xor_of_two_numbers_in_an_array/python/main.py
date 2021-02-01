from typing import List


class Solution:
    def findMaximumXOR_bruteforce(self, nums: List[int]) -> int:
        """

        Brute Force Solution

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        """

        # initialize max_xor
        max_xor = 0

        # loop through all numbers in nums
        for x in range(len(nums)):
            # loop through remaining numbers in nums
            for y in range(x+1, len(nums)):
                # check if XOR of the two elements is greater
                # than what we have saved as max_xor
                if nums[x] ^ nums[y] > max_xor:
                    max_xor = nums[x] ^ nums[y]

        return max_xor

    def findMaximumXOR_hashset(self, nums: List[int]) -> int:
        """

        Hash Set Solution

        Time Complexity: O(n)
        Space Complexity: O(n)

        """

        # initialize max_xor
        max_xor = 0
        # initialize L to be max number of bits needed
        L = len(bin(max(nums))) - 2  # minus 2 because formats to '0b...'

        # loop through bits in nums
        for shift in range(L)[::-1]:

            # left shift max_xor to make room for a byte
            max_xor <<= 1

            # initialize curr_xor as the maximum value we could have
            # by setting right most byte of max_xor to 1
            curr_xor = max_xor | 1

            # loop through all possible ways to get curr_xor with
            # the numbers we have by shifting all of them and
            # checking if any shifted num[i] XOR num[j] == curr_xor
            prefixes = {num >> shift for num in nums}
            print(prefixes)
            for prefix in prefixes:
                # if we do find one that matches, we know that max_xor
                # can equal curr_xor so we redefine and continue with
                # the loop to add more bytes to the end of max_xor

                # if no match is found, max_xor will keep the right most
                # 0 byte keep continuing from there
                if curr_xor ^ prefix in prefixes:
                    max_xor = curr_xor
                    break

        return max_xor

    def findMaximumXOR_trie(self, nums: List[int]) -> int:
        # TODO
        pass
